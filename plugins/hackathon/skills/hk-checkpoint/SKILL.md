---
name: hk-checkpoint
description: Use when the user reports elapsed time or asks where things stand. Compares progress with the hackathon checkpoints (20/90/140/165/170 min), states what is done, at risk, and what to cut, and gives the single next action. Invoke explicitly with $hk-checkpoint <elapsed minutes>.
---

# hk-checkpoint

## Purpose

The agent cannot see the clock. The user supplies elapsed minutes; this skill
turns that into a decision about scope.

## Checkpoints

| Minute | Must be true |
|---|---|
| 20 | spec written, questions sent, first stage started |
| 90 | minimum path runs end to end |
| 140 | feature freeze — only fixes, verification, docs |
| 165 | docs final, files saved, committed |
| 170 | user starts submission ("제출하고 문제풀기") |

## Procedure

1. Read the spec ledger and `git log --oneline` to establish real progress.
   Do not trust memory of the conversation.
2. Place the elapsed time against the table. For each passed checkpoint,
   mark met / missed with evidence.
3. If behind: propose the smallest scope cut that restores the next
   checkpoint, and record it with `hk-decision` once the user agrees.
4. Past minute 140: refuse new features; only fixes, `hk-submit`.

## Output

```text
경과: 95분 · 다음 체크포인트: 140분 (기능 동결)
완료: S1, S2, S3 (커밋 a1b2c3)
위험: S4 미구현, 최소 경로 미완
조치: S5 제외 → S4만 구현 (hk-decision 필요)
다음 행동: S4 구현
```
