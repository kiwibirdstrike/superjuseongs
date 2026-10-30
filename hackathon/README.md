# hackathon

SK하이닉스 AI 해커톤(Codex 제공 환경)용 설정. 원본 `config/`·`install.py`는 개인 환경용 예시로 두고,
시험 규정에 맞게 다시 정리한 버전이다.

## 원본과 다른 점

| 항목 | 원본 (`config/`, `install.py`) | hackathon |
|---|---|---|
| 운영 계약 | 전역 `~/.codex/AGENTS.md` 덮어쓰기 | 작업 폴더 `AGENTS.md`, 과제가 준 파일이 있으면 안 건드림 |
| Codex 설정·에이전트 프로필 | `config.toml` 수정, `~/.codex/agents` 설치 | **아무것도 안 건드림** |
| 서브에이전트 역할 | TOML 프로필 | `$hk-delegate` 디스패치 안에 역할 문장으로 |
| 요구사항 출처 | 사용자 | 업무 담당자(메신저) → 사용자가 전달 |
| 산출 | 코드 | 코드 + `docs/DECISIONS.md` + 제출 문서 + 서술형 브리핑 |

## 당일 설치

```bash
git clone https://github.com/kiwibirdstrike/superjuseongs.git ~/superjuseongs
cd <과제 작업 폴더>
python3 ~/superjuseongs/hackathon/setup.py --dry-run   # 먼저 확인
python3 ~/superjuseongs/hackathon/setup.py
codex
```

사전 체험(15분)에서 설치, `/status`·`/model`, `$hk-kickoff` 인식까지 먼저 확인한다.
플러그인이 안 되면 `AGENTS.md`만으로도 같은 흐름으로 진행된다.

## 치트시트

| 시점 | 입력 |
|---|---|
| 0분, 과제 시작 | `$hk-kickoff` |
| 업무 담당자 답 받음 | `$hk-decision 업무 담당자 답: <붙여넣기>` |
| 선택·가정이 생김 | `$hk-decision <무엇을 왜>` |
| 20 / 90 / 140분 | `$hk-checkpoint <경과 분>` |
| 결과가 이상함 | `$change-diagnosis <증상>` → 결과 보고 `$upstream-fix` |
| 병렬로 맡길 일 | `$hk-delegate <일>` |
| 140분 | `$hk-submit` |
| 170분 | 직접 "제출하고 문제풀기" |

## 시간 체크포인트

20분 스펙 → 90분 최소 경로 동작 → 140분 기능 동결 → 165분 문서·커밋 → 170분 제출 시작.

서술형은 AI 없이 문항당 5분. `$hk-submit`이 마지막에 주는 예상 질문 브리핑을 제출 전에 읽어둔다.
