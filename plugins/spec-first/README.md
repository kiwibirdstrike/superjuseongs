# spec-first

스펙을 먼저 고정하고, 결함은 **처음 틀린 상태를 만든 단계에서** 고치게 하는 플러그인.

## 해결하려는 문제

에이전트는 문제가 생기면 원인 단계를 고치지 않고 하류에 보정 코드를 덧붙인다.

```text
load → normalize → fit → predict → "eval_X를 다시 rescale"   # 보상 패치
```

정규화가 잘못됐는데 모델이 이미 틀린 값으로 학습한 뒤에 결과만 맞춘다. 이런 패치가
쌓이면 단계 순서가 꼬이고, 다음 수정 때 보정이 조용히 깨진다.

`spec-first`는 수정을 **코드 덧붙이기가 아니라 dependency update**로 다룬다.

```text
load → normalize' → fit' → predict'   # 원인 단계 수정 후 하류 재계산
```

paper-writer의 "upstream revision" 원칙을 코드에 옮긴 것이다.

## 구조

```text
plugins/spec-first/
├── AGENTS.md                  # 라우팅·우선순위·금지 행동
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
└── skills/
    ├── spec-definition/       # 새 작업 → stage ledger (코드 전 필수)
    ├── change-diagnosis/      # 처음 틀린 단계 찾기, 깊이 판정 (코드 X)
    ├── upstream-fix/          # 스펙 먼저 → 원인 단계 → 하류 재검증, 보정 제거
    └── patch-audit/           # 보상 패치·순서 이탈 판정만 (수정 X)
```

## 공유 상태: stage ledger

`docs/agent/specs/<slug>/spec.md` 하나를 모든 스킬이 읽고 쓴다.

```text
S3  stage
  purpose:        train 통계로 수치 피처 표준화
  inputs:         S2.train_frame, S2.eval_frame
  outputs:        train_X, eval_X
  invariants:     통계는 train에서만; S4(fit) 이전
  depends_on:     S2
  implemented_in: src/features.py::standardize
  status:         active
```

- 활성 단계는 무효화된 노드에 의존할 수 없다.
- 코드의 단계 순서 = ledger의 `depends_on` 순서.
- 데이터를 바꾸는 코드는 전부 어떤 단계에 매핑돼야 한다. 매핑 안 된 변환이 보상 패치가 숨는 곳이다.

## 흐름

```text
새 작업:      spec-definition → 단계별 구현 → patch-audit
버그/요구변경: change-diagnosis → upstream-fix → patch-audit  (최대 3회)
```

## superjuseong과의 관계

superjuseong은 작업 방식 전반(자율성, 검증, 서브에이전트)을 다루고 무상태다.
spec-first는 스펙과 코드의 정합성만 다루며 ledger라는 명시적 상태를 가진다.
같이 설치해도 역할이 겹치지 않는다.
