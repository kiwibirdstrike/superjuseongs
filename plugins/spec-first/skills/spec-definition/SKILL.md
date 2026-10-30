---
name: spec-definition
description: Use at the start of any new feature, pipeline, module, or experiment, before writing code. Produces a short stage ledger (stages, inputs, outputs, invariants, order, decisions) and acceptance checks. Required even when the request looks clear.
---

# spec-definition

## Purpose

Fix the shape of the system before code exists, so later fixes have a
correct place to land. Most compensating patches trace back to a stage whose
contract was never written down.

## When to use

- any new feature, pipeline, module, script, or experiment
- an existing system with no ledger is about to be changed substantially

## When not to use

- a ledger exists and the request is a bug or changed requirement — use
  `change-diagnosis`
- a one-line, behavior-preserving edit

## Procedure

1. **Read before asking.** Inspect the repository, data, and existing code.
   Separate evidence from assumption.
2. **Write the outcome in one sentence** and the acceptance check that would
   prove it (a command, a test, a metric threshold).
3. **List stages in data-flow order.** For each: purpose, inputs (by producing
   stage), outputs (with type or shape), invariants, `depends_on`.
   One stage = one transformation with one reason to change.
4. **Write the invariants that ordering protects.** Leakage boundaries, split
   timing, units, deduplication point, sort order, idempotency. These are what
   a later patch most often breaks.
5. **Record decisions (`D`) and assumptions (`A`)** that a stage relies on,
   with the reason. A fix that contradicts a decision must change the
   decision, not route around it.
6. **Ask only decision-changing questions,** one at a time, when the answer
   would change a stage, its order, or an invariant.
7. **Leave `implemented_in` empty** until code exists; fill it as stages are
   built.

## Artifact

`docs/agent/specs/<slug>/spec.md` — outcome, acceptance checks, stage ledger,
decisions, assumptions, non-goals. Keep it to what changes behavior; no prose
padding.

## Failure modes

- **Skipping because the task looks obvious.** Obvious tasks still have stage
  order and invariants.
- **Stages too coarse** ("process data") — a fix cannot be located in them.
- **Missing invariants** — the order is written but not why.
- **Spec as documentation** — long prose nobody updates. The ledger is state.

## Output

The spec file path, the stage list in order, and open questions (if any).
