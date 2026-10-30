---
name: hk-decision
description: Use whenever a design choice is made, a default is assumed, a 업무 담당자 answer arrives, or a plan changes. Appends one entry to docs/DECISIONS.md and updates the spec ledger so the user can explain it later without AI. Invoke explicitly with $hk-decision.
---

# hk-decision

## Purpose

The follow-up questions are generated from the submitted files and work logs
and must be answered without AI. Every decision the user may be asked about
must exist in writing, in plain Korean, at the time it is made.

## When to use

- a choice between real alternatives (library, algorithm, data handling,
  interface, scope cut)
- the user pastes an answer from the 업무 담당자
- an assumption is made because no answer came
- a bug fix changed a stage contract or the spec

## Procedure

1. Append to `docs/DECISIONS.md`:

```text
## D<n>. <한 줄 결정>
- 선택: 무엇을 골랐나
- 근거: 왜 (측정값, 업무 담당자 답변, 제약)
- 대안: 무엇을 버렸고 왜
- 검증: 어떻게 확인했나 → 결과 (아직이면 "미검증")
- 한계: 남은 약점
- 출처: 업무 담당자 / 과제 README / 자체 판단
```

2. Mirror it in the spec ledger as a `D` node (or turn the matching `A` into
   `D` when an answer confirms or overrides an assumption). If it changes a
   stage contract, route through `change-diagnosis` first.
3. Commit with the decision id in the message.

## Boundaries

- One decision per entry. No prose essays.
- Never record a decision the code does not actually implement.
