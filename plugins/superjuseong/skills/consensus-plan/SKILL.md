---
name: consensus-plan
description: Use when nontrivial work needs an implementation plan, architectural tradeoff review, test structure, or explicit planning consensus before execution.
---

# Consensus Plan

## Outcome

Produce one executable, evidence-grounded plan reviewed from planning, architecture, and verification perspectives.

## Input Gate

Use an existing specification when available. If a decision-changing ambiguity remains, use `clarify-and-spec`; otherwise plan without asking.

## Consensus Pass

1. **Planner:** define the outcome, constraints, affected files, dependencies, task order, acceptance criteria, and exact verification commands.
2. **Architect:** challenge boundaries, interfaces, failure modes, migration risk, and unnecessary complexity.
3. **Verifier:** check every requirement has a task and every completion claim has runnable evidence.
4. Revise once when a review finds a concrete gap. If the gap remains, report it instead of looping.

Use matching native subagents when available and useful. Otherwise perform the three labeled passes sequentially in one session. The leader owns the final plan.

Compare alternatives only when a real tradeoff exists. Record the decision drivers, chosen approach, rejected alternative, and reason.

## Artifact

Write `docs/agent/plans/YYYY-MM-DD-<slug>-plan.md`. Create a separate `-test-plan.md` only when the test design is substantial enough to be useful independently.

Each task must name exact files, behavior, dependencies, verification, and stop conditions. Avoid placeholders and speculative scaffolding.

## Boundaries

- Planning does not execute the plan.
- Do not start teams, modes, goals, state machines, or persistent loops.
- Do not require an execution-style choice after the plan when the user's requested next step is already clear.
