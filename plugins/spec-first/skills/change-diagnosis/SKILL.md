---
name: change-diagnosis
description: Use first on any bug, wrong output, failing check, or changed requirement in spec-governed work. Locates the first stage that produces a bad state or the spec node a requirement invalidates, computes the downstream set, and classifies depth as local, stage, or spec. Produces a routing decision, never code.
---

# change-diagnosis

## Purpose

Decide **where** a change belongs before anything is edited. Symptoms appear
at the end of a pipeline; causes usually live several stages earlier.

## When to use

- always, as the first response to a bug report, wrong result, failing test,
  or new or changed requirement on existing work
- when `patch-audit` reports a finding

## When not to use

- no ledger exists for new work — `spec-definition`
- diagnosis is done and depth is stage or spec — `upstream-fix`

## Procedure

1. **State the observed problem factually,** with the smallest reproduction.
2. **Find the first bad state.** Walk stages from the start in ledger order,
   checking each stage's outputs against its stated contract and invariants.
   The first stage whose output violates its contract is the origin — not the
   stage where the error surfaced.
3. **For requirement changes, find the earliest invalidated node** — the
   decision, assumption, constraint, or stage contract the new requirement
   contradicts.
4. **Compute the downstream set:** every stage reachable by `depends_on`.
   Mark each invalidated, needs recheck, or unaffected. Include unmapped
   transforms found in the code path.
5. **Apply the counterfactual test:** if this had been known when the origin
   stage was written, would it have been written this way?
6. **Assign one depth:** local, stage, or spec (see policy). Choose deeper
   when torn.
7. **Detect existing patches.** Note any downstream code that already
   compensates for this defect — it must be removed in the fix.

## Failure modes

- **Diagnosing at the point of failure.** The stage that throws is rarely the
  stage that broke.
- **Under-scoping** to keep the diff small.
- **Writing the fix here.** It anchors `upstream-fix` to a downstream patch.

## Output

```text
Problem:      eval accuracy 0.99, expected ~0.82
Origin:       S3 standardize — stats computed on full frame (invariant violated)
Depth:        stage
Downstream:   S4 fit (recheck) · S5 eval (recheck)
Existing patches: src/eval.py:41 rescales eval_X after predict — remove
Route:        upstream-fix, origin S3
Open question: none
```

No code, no replacement implementation.
