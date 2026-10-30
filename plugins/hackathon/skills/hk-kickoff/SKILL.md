---
name: hk-kickoff
description: Use once, right after the hackathon task starts. Reads the task files, writes the spec with spec-definition, drafts questions for the 업무 담당자, initializes git and docs/DECISIONS.md, and returns a timed stage plan. Invoke explicitly with $hk-kickoff.
---

# hk-kickoff

## Purpose

Turn the first 20 minutes into a fixed spec, a question list, and a plan, so
the remaining time is spent building the right thing.

## Procedure

1. **Read everything provided.** `README.md`, every file it references,
   existing code, data samples, tests. List required output file names and
   formats exactly as the task states them.
2. **Write the spec** with `spec-definition` at
   `docs/agent/specs/<slug>/spec.md`: outcome, acceptance checks, stage ledger,
   decisions, assumptions, non-goals. Keep it under one screen.
3. **Draft questions for the 업무 담당자.** Only questions whose answer changes
   a stage, an interface, or acceptance. At most 5, numbered, each answerable
   in one line, written in Korean so the user can paste them into the
   messenger. For every question, state the default you will use if no answer
   comes, and record it as an assumption (`A`).
4. **Prepare the workspace.** `git init` if not a repository; create
   `docs/DECISIONS.md` with a header; commit `kickoff: spec and plan`.
5. **Timed plan.** Order stages by the ledger, estimate minutes per stage,
   and mark the minimum viable path that must run end to end by minute 90.
   Mark what will be cut first if time runs short.

## Output

```text
필수 산출물:  <file names / formats from the task>
업무 담당자 질문 (복사용):
  1. ...  (답 없으면: ...)
단계 계획:   S1 <name> ~15m · S2 ... · 최소 경로: S1→S2→S4
먼저 자를 것: ...
다음 행동:   S1 구현 시작
```

## Boundaries

- No implementation before the spec exists.
- Never ask what the task files already answer.
