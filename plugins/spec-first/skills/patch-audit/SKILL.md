---
name: patch-audit
description: Use after implementing new work or a fix, or to review an existing diff or code path, to judge whether it contains compensating patches, stage-order drift, unmapped transforms, or spec-code disagreement. Judges only; findings route back to change-diagnosis.
---

# patch-audit

## Purpose

Independent gate. Detect the patterns that mean a defect was covered instead
of fixed. Read the diff and ledger without the implementer's reasoning.

## Checks

For the changed path, answer each with evidence (file:line):

1. **Compensation:** does any change correct a value after the stage that
   produced it (re-normalize, re-sort, dedupe late, clip, rescale, recast,
   post-hoc metric adjustment)?
2. **Order drift:** does code stage order still equal ledger `depends_on`
   order? Did any step move relative to a stated invariant (split, fit,
   normalization, filtering)?
3. **Unmapped transforms:** does any data-changing code exist that is not a
   ledger stage?
4. **Spec agreement:** do contracts, decisions, and `implemented_in` match the
   code?
5. **Dead premises:** does any active stage depend on an invalidated node?
6. **Regression check:** is there a check that fails on the original defect at
   the origin stage?
7. **History markers:** comments or names like `fix`, `workaround`, `temp`,
   `hack`, `correct_*` attached to data transforms.

## Verdict

```text
PASS | FAIL | PARTIAL
Findings: <check #> <file:line> <one-line evidence>
Route:    change-diagnosis for each finding
```

## Boundaries

- Do not fix anything. A finding reopens `change-diagnosis`.
- Missing evidence is not a pass.
