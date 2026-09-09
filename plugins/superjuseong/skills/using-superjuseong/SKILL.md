---
name: using-superjuseong
description: Use when starting a coding, research, planning, review, or repository task under the Superjuseong operating contract.
---

# Using Superjuseong

Use the smallest workflow that can finish and verify the request.

- Clear, safe, reversible work: inspect, act, and verify directly.
- Ambiguous work: use `clarify-and-spec` only when a missing human decision changes the result.
- Nontrivial planning: use `consensus-plan`.
- Bugs or unexpected behavior: use `systematic-debugging`.
- Independent bounded subtasks: use `using-native-subagents` when parallelism improves speed or confidence.
- Behavior-changing code: use `test-driven-development`.
- Reviews: use `code-review`.
- Before a success claim: use `verification-before-completion`.

Ask only when the task is ambiguous or destructive. Do not stop for approval, execution-mode selection, or handoff when the requested next step is clear and reversible.

Store durable context, specifications, and plans under `docs/agent/`. Do not create runtime state, persistent loops, teams, or keyword-routing machinery.
