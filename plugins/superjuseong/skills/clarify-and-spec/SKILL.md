---
name: clarify-and-spec
description: Use when a request is ambiguous, materially branching, architectural, says not to assume, or lacks testable acceptance criteria.
---

# Clarify And Spec

## Outcome

Reduce only the ambiguity that changes implementation, then produce an execution-ready specification when one is warranted.

## Workflow

1. Inspect available repository facts before asking about internals. Separate evidence from inference.
2. Identify the smallest unresolved human decision that changes scope, behavior, safety, or acceptance.
3. Ask one concise question. Do not batch interview rounds.
4. Repeat only while a decision-changing ambiguity remains.
5. When the task is clear, continue the requested safe work without asking for approval.

Skip the interview when intent, scope, and acceptance criteria are already sufficient.

## Artifacts

For context-heavy or cross-session work, write `docs/agent/context/YYYY-MM-DD-<slug>.md` with task, outcome, evidence, touchpoints, constraints, assumptions, unresolved decisions, and a prompt-safe handoff summary.

For architectural or materially branching work, write `docs/agent/specs/YYYY-MM-DD-<slug>-design.md` with intent, outcome, scope, non-goals, decision boundaries, constraints, repository evidence, acceptance criteria, verification, risks, assumptions, and handoff recommendation.

Do not create an artifact for a trivial request.

## Boundaries

- Ask only when the task is ambiguous or destructive.
- Do not ask the user for facts available in the repository.
- Do not require approval after ambiguity is resolved.
- Do not implement while the requested outcome is still materially ambiguous.
- Do not create runtime state, tmux sessions, teams, commits, or persistent loops.
