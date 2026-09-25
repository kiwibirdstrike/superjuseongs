# paper-writer

논문 작성을 위한 **paper-writing orchestrator** 플러그인.

문장을 잘 써주는 writing assistant가 아니라, 논문의 argument / evidence /
scope / causal claim / terminology를 **dependency structure**로 관리하면서
수정이 올바른 지점에 전파되도록 통제하는 오케스트레이터다.

---

## 해결하려는 문제

LLM으로 논문을 쓸 때 반복적으로 나타나는 실패는 문장 품질이 아니라
**수정의 축적 방식**이다.

피드백이 들어오면 모델은 보통 원래 문장을 그대로 둔 채 뒤에 정정을 덧붙인다.

> The improvement is primarily attributable to increased model capacity. This
> suggests that larger models are inherently better suited for this task.
> **However, parameter count was held constant, so the training objective may
> also have contributed.**

각 수정은 개별적으로는 정확하지만, 이런 수정이 쌓이면 원고는 서로 다른 시점의
전제들이 층층이 남은 패치 모음이 된다. 초록은 3차 수정본의 주장을, 본문은 5차
수정본의 주장을 하고, 사라진 주장을 방어하던 caveat이 그대로 남는다.

`paper_writer`는 수정을 **text mutation이 아니라 dependency update**로 취급한다.
전제가 바뀌면 그 전제를 처음 주장한 지점으로 돌아가 거기서부터 downstream
reasoning을 다시 계산한다.

> Because parameter count was held constant across the compared models, the
> observed performance difference cannot be attributed to increased model
> capacity. The results instead indicate that the training objective is the
> more plausible source of the improvement.

capacity 주장은 완화된 것이 아니라 **삭제**되었고, 그에 의존하던 일반화도 함께
사라졌으며, 대체 주장은 evidence가 허용하는 강도(`more plausible source`)로
다시 쓰였다.

---

## Architecture

```text
plugins/paper-writer/
├── AGENTS.md                         # orchestration policy (routing, loop, priority)
├── README.md
├── .codex-plugin/plugin.json         # Codex manifest
├── .claude-plugin/plugin.json        # Claude Code manifest
└── skills/                           # 양쪽이 동일한 SKILL.md 를 공유
    ├── paper-planning/SKILL.md       # argument skeleton + claim ledger
    ├── section-drafting/SKILL.md     # skeleton → academic prose
    ├── revision-diagnosis/SKILL.md   # 무엇이 어디까지 바뀌는가 (routing only)
    ├── upstream-revision/SKILL.md    # root claim부터 재계산
    ├── coherence-pass/SKILL.md       # 전체 문서 정합성 복구 (loop 내부)
    ├── evidence-audit/SKILL.md       # claim ↔ evidence 정렬 및 grading
    ├── humanizer/SKILL.md            # style only, 맨 마지막
    └── final-audit/SKILL.md          # 제출 전 gate (판정만, 수정 안 함)
```

공통 원칙은 `AGENTS.md`에만 둔다. 각 SKILL.md는 자기 책임 범위의 절차만 갖는다.

### 공유 상태: claim ledger

모든 skill은 하나의 `claims.md`(claim ledger)를 읽고 쓴다. 원고의 dependency
graph를 명시적으로 들고 있는 파일이다.

```text
C3  claim
  statement:  Instruction tuning accounts for most of the observed gain.
  depends_on: E1, E4, A2
  support:    inference
  appears_in: abstract, §1 ¶2, §4 ¶3, §6 ¶1
  status:     active
```

`appears_in`이 핵심이다. 본문에서 수정된 주장이 초록에 그대로 남는 실패는
이 필드가 있어야 잡힌다.

---

## Skill 책임

| Skill | 하는 일 | 하지 않는 일 |
|---|---|---|
| `paper-planning` | argument skeleton, dependency graph, ledger 생성 | prose |
| `section-drafting` | skeleton → prose | ledger에 없는 주장 만들기, 문체 다듬기 |
| `revision-diagnosis` | 변경 분류, root claim과 downstream 특정 | 대체 문장 작성 |
| `upstream-revision` | root claim부터 재작성 및 전파 | 재작성 필요 여부 판단 |
| `coherence-pass` | 전체 문서 정합성 **복구** | claim grading, style |
| `evidence-audit` | support grading, citation 정합성 | argument 구조 재작성 |
| `humanizer` | 문체만 | 의미·hedging·claim 변경 |
| `final-audit` | 최종 **판정** | 수정 (loop로 되돌림) |

`coherence-pass`와 `final-audit`의 경계: 전자는 loop 안에서 **고치고**, 후자는
loop 밖에서 **판정만 하고** 문제를 `revision-diagnosis`로 되돌린다.

---

## Revision loop

```text
requirements / research context
        ↓
     outline  (paper-planning)
        ↓
      draft   (section-drafting)
        ↓
 substantive evaluation
        ↓
 revision diagnosis  ──┐
        ↓              │
 upstream revision     │  substantive issue 남아 있으면 반복
        ↓              │  (최대 3회)
 coherence pass  ──────┘
        ↓
 evidence audit
        ↓
 humanization
        ↓
 final audit
        ↓
 final manuscript
```

**Routing 규칙.** 모든 피드백은 먼저 `revision-diagnosis`를 거친다. 수정 깊이가
surface / local semantic이면 local edit, argumentative / structural이면
`upstream-revision`이 강제된다. 애매하면 argumentative로 올린다 — 과소 판정은
패치된 원고를 만들고, 과대 판정은 토큰만 더 쓴다.

**종료 조건.** factual contradiction 없음, invalidated premise에 의존하는 claim
없음, evidence보다 강한 claim 없음, abstract/intro/conclusion이 body와 일치,
남은 문제가 stylistic 수준. 같은 문제가 두 번 연속 살아남으면 루프를 멈추고
unresolved issue로 명시한다.

---

## Humanizer가 마지막인 이유

**Do not humanize unstable reasoning.**

두 가지 이유가 있다. 하나는 단순한 낭비다 — 다시 쓸 문장을 다듬는 비용.

더 중요한 쪽은 두 번째다. 다듬어진 산문은 완성된 것처럼 보이고, **틀린 주장일수록
매끄러운 문장 안에서 눈에 띄지 않는다.** 논리가 흔들리는 단계에서 문체를 먼저
정리하면 검토가 멈추는 지점을 인위적으로 앞당기게 된다.

그래서 `humanizer`는 loop 밖에서 한 번만 돌고, meaning에 대한 권한이 없다.
hedging은 `evidence-audit`이 설정한 epistemic grade이므로 style이 아니라
content로 취급한다. 작업 중 논리 문제를 발견하면 고치지 않고
`revision-diagnosis`로 escalate한다.

---

## Evidence policy

source에 접근할 수 없으면 citation, DOI, 저자, 연도, 결과를 만들지 않는다.
`[citation needed]` 또는 `[source: …]` placeholder를 쓰고 ledger에서
`unsupported`로 등급을 매긴다. 확인되지 않은 내용을 확신 있는 문장으로 쓰는 것이
눈에 보이는 placeholder보다 나쁘다.

---

## 사용 예시

### 설치

Codex:

```bash
codex plugin marketplace add https://github.com/kiwibirdstrike/superjuseongs
codex plugin add paper-writer@superjuseongs
```

`install.py` 를 실행하면 `superjuseong` 과 함께 자동으로 설치된다.

Claude Code:

```bash
/plugin marketplace add kiwibirdstrike/superjuseongs
/plugin install paper-writer@superjuseongs
```

개별 skill만 쓰고 싶으면 `skills/` 하위 디렉터리를 `~/.claude/skills/` 로 복사해도 된다.

### 새 section 쓰기

```text
> Results 섹션을 써줘. 실험 결과는 results.csv에 있고, 두 arm은 training
> objective만 다르고 파라미터 수는 동일해.

→ paper-planning     : E/C/I/M 노드와 dependency chain 구성, ledger 생성
→ section-drafting   : 문단별 기능을 정해 prose 작성, 강도는 grade에 맞춤
→ coherence-pass     : argument spine과 문단 handoff 점검
```

### 전제를 바꾸는 피드백

```text
> 파라미터 수는 사실 고정이었어. 차이는 training objective뿐이야.

→ revision-diagnosis : root = C1(capacity 귀인), downstream = I1, M,
                       affected = abstract ¶1 · §1 ¶2 · §4 ¶3 · Fig.2 caption
                       depth = argumentative
→ upstream-revision  : C1 삭제, I1/M 재계산, 5개 위치 전부 재작성
→ coherence-pass     : 사라진 주장을 방어하던 caveat 제거, spine 재확인
```

"However, parameter count was held constant…"를 뒤에 붙이는 결과는 나오지 않는다.

### 내용 확정 후 문체만

```text
> 내용은 확정. 문장만 사람이 쓴 것처럼 다듬어줘.

→ humanizer   : 기계적 패턴 제거, hedging·용어·citation은 보존
→ final-audit : 의미 변화 없었는지 대조, revision integrity 판정
```

---

## Philosophy

- A manuscript is a dependency structure, not a sequence of sentences.
- Revision should recompute affected reasoning, not preserve obsolete prose.
- Style optimization belongs after reasoning stabilization.
- A final manuscript should look as if it was written once with full knowledge
  of the final argument.
