---
name: upstream-fix
description: Use when change-diagnosis returns stage or spec depth. Updates the spec first if a decision or contract changed, fixes the origin stage, removes downstream compensations, and rechecks every dependent stage so the system reads as if it had been built correctly from the start.
---

# upstream-fix

## Purpose

Recompute the system from the origin of the defect. Given stages
`S1 → S2 → S3` and a defect in `S1`, the result is a corrected `S1' → S2' → S3'`,
never `S1 → S2 → S3 → fix(S1)`.

## When to use

- `change-diagnosis` returned depth stage or spec

## When not to use

- depth is local — edit inside the stage
- no diagnosis exists — run it first

## Procedure

1. **Spec first.** If depth is spec, or the origin stage's contract changes,
   update the ledger before code: mark invalidated nodes, add replacements,
   fix `depends_on` and order.
2. **Write the failing check** that reproduces the defect at the origin
   stage's output, not only at the final output.
3. **Fix the origin stage.** Rewrite it from its corrected contract; do not
   adjust its output after the fact.
4. **Remove compensations.** Delete every downstream workaround the diagnosis
   listed, and any you find while tracing. Re-run checks after removal.
5. **Recheck each downstream stage** against its contract with the corrected
   inputs. Recompute; do not assume they still hold.
6. **Delete stages whose premise is gone** instead of wrapping them.
7. **Update `implemented_in`** and confirm code stage order equals ledger
   order.
8. **Read the changed path cold.** If a reader could tell an earlier version
   was patched (history comments, double conversions, re-sorts, re-normalizing),
   the fix is not finished.

## Failure modes

- **Fixing the symptom site** because it is closer to the failing test.
- **Keeping the old patch "just in case."** Two corrections in series hide
  the next bug.
- **Code ahead of spec.** The ledger must change in the same pass.
- **Stopping at the origin stage** without rechecking dependents.

## Output

- changed files and the stage each belongs to
- ledger changes (invalidated, added, reordered)
- removed compensations
- check results: failing before, passing after
