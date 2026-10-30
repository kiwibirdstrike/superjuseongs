---
name: hk-submit
description: Use at feature freeze (about minute 140) or when the user says to wrap up. Runs patch-audit and every acceptance check fresh, writes the submission document, commits, and gives the user a Korean briefing for the AI-free follow-up questions. Invoke explicitly with $hk-submit.
---

# hk-submit

## Procedure

1. **Freeze.** No new features from here.
2. **Audit.** Run `patch-audit` on the full diff against the spec. Fix only
   FAIL findings that fit the remaining time; record the rest as limitations.
3. **Verify fresh.** Run every acceptance check from the spec now, not from
   memory. Record command and result.
4. **Check required outputs.** Every file name and format the task README
   requires exists at the exact path, saved.
5. **Write the submission document** — the name the task requires, otherwise
   `docs/SUBMISSION.md`:

```text
# <과제명>
## 결과 요약        무엇을 만들었고 어디까지 되나
## 실행 방법        명령어, 포트, 경로
## 설계와 결정      DECISIONS.md 핵심 3~5개 요약 + 링크
## 검증 결과        체크별 명령 → 결과 (PASS/FAIL)
## 한계와 다음 단계  남은 문제, 미검증 항목, 시간이 있었다면
## AI 활용 방식     위임한 일, 직접 검증한 일
```

6. **Commit** `submit: final` and show `git status` clean.
7. **Briefing for the user** (they answer without AI, 5 min per question):

```text
예상 질문 브리핑
1. 왜 <핵심 결정>? → <근거 한 줄>
2. <대안>은 왜 안 썼나? → ...
3. 어떻게 검증했나? → ...
4. 가장 약한 부분은? → ...
5. 시간이 더 있었다면? → ...
```

8. Remind: submit at least 10 minutes before the end; confirm submission ID,
   time, file count, and size on the completion screen.

## Boundaries

- Do not claim a check passed without running it in this step.
- Do not hide failures; a stated limitation scores better than a wrong claim.
