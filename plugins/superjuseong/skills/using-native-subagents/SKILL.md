---
name: using-native-subagents
description: Use when two or more independent bounded subtasks can run concurrently or when a specialist review materially improves confidence.
---

# Using Native Subagents

## Rule

Delegate only when separation improves speed, context quality, or independent verification. Direct work is the default for trivial, coupled, or shared-file tasks.

## Roles

- `explore`: repository-local facts and relationships
- `researcher`: official external documentation
- `dependency-expert`: package, SDK, license, maintenance, and migration choices
- `planner`: implementation sequencing
- `architect`: design and tradeoff review
- `debugger`: root-cause analysis
- `executor`: bounded implementation
- `verifier`: independent completion evidence

## Dispatch Contract

Each task names one bounded objective, ownership, constraints, required evidence, and expected output. Parallel tasks must not depend on each other's results or edit the same files.

The leader integrates all results, resolves conflicts, runs final verification, and solely owns the completion claim. A subagent summary is evidence to inspect, not proof of completion.

Do not create workers, teams, tmux sessions, mailbox protocols, state files, automatic escalation, or recursive orchestration. Wait only when no useful local work remains.
