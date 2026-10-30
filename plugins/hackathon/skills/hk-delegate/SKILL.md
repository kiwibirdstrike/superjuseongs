---
name: hk-delegate
description: Use before spawning a native subagent. Picks the role, writes a self-contained dispatch with background, ownership, constraints, and a short output format, and checks that the work is independent. Roles are defined here, not in installed profiles. Invoke explicitly with $hk-delegate <task>.
---

# hk-delegate

## Purpose

Subagents see nothing of this conversation. A dispatch that omits context
produces confident wrong work and wastes tracked tokens. Delegate only when it
saves wall-clock time.

## Delegate only if all hold

- the task does not depend on work still in progress
- no other agent edits the same files
- the leader has useful work to do meanwhile
- the result can be checked quickly

Otherwise do it directly.

## Roles (put the line into the dispatch)

| Role | Instruction line |
|---|---|
| explore | Read-only. Answer the repository question with paths, relationships, and gaps. |
| researcher | Read-only. Find primary documentation reachable in this environment; cite; never send task content outside. |
| debugger | Reproduce first; walk stages in spec order; report the first stage violating its contract and the check proving it. Do not fix. |
| executor | Implement only the assigned stage in the owned files; fix at the origin stage, never downstream; run the stage check. |
| verifier | Read-only. Ignore the implementer's report; run fresh checks against the spec; return PASS / FAIL / PARTIAL with evidence. |

## Dispatch template

```text
Role: <role line>
Background: <task in 3 lines; spec path; relevant decisions>
Known: <facts already established — do not re-derive>
Objective: <one bounded outcome>
Owns: <files it may edit, or "read-only">
Constraints: <stage contract, invariants, no git push, no outbound transfer>
Done when: <check or evidence>
Return: at most 15 lines — result, evidence (file:line / command output), gaps
```

## After it returns

Treat the report as evidence to inspect, not proof. Re-run its key check
yourself before building on it.
