# spec_first — Orchestration Policy

This file defines **how the agent routes work** on a system whose behavior is
governed by a specification. Procedures live in the skills.

---

## 1. Identity

`spec_first` keeps a specification and the code that implements it in
agreement while both change. It exists to prevent one failure: the
**compensating patch**.

A compensating patch leaves the stage that produced a wrong state untouched
and repairs the result somewhere downstream. Every stage between the cause and
the patch keeps running on wrong data, and the next change to stage order,
inputs, or outputs silently breaks the repair.

Typical shapes:

- a pipeline normalizes too late, so a "fix-up" re-normalizes after the model
  has already consumed the raw values
- a loader emits duplicates, so a deduplication step is added after scoring
- a wrong split leaks data, so a correction is applied to the final metric
- an upstream type is wrong, so every caller converts it

**A system is a dependency structure of stages, not a sequence of edits.**
A fix is a dependency update at the stage that first went wrong.

---

## 2. Priority order

When two goals conflict, the earlier one wins.

1. correctness of the stage that produces each state
2. agreement between specification and code
3. stage order and data-flow invariants
4. explicit, inspectable data flow
5. minimal change size

**Keeping the existing code path is not on this list.** A smaller downstream
patch never beats a correct upstream fix.

---

## 3. Fundamental rule

> **Fix where the first bad state is produced. Do not compensate downstream.**

The diagnostic question for every proposed change:

> **If this had been known when the stage was first written, would the stage
> have been written this way?**

- **Yes** → a local edit inside the stage is enough.
- **No** → the stage (and possibly the spec) must be rewritten upstream, and
  every dependent stage rechecked.

A downstream step is legitimate only when it is a genuine new stage the spec
names (with its own inputs, outputs, and reason), not a repair of an earlier
stage's output.

---

## 4. Shared state: the stage ledger

All skills read and write one artifact:
`docs/agent/specs/<slug>/spec.md`. It is the system's dependency graph.
Keep it short and current; it is working state, not documentation.

```text
S3  stage
  purpose:        Standardize numeric features using train-split statistics.
  inputs:         S2.train_frame, S2.eval_frame
  outputs:        train_X, eval_X (float32, mean 0 / std 1 on train)
  invariants:     statistics computed on train only; runs before S4 (model fit)
  depends_on:     S2
  implemented_in: src/features.py::standardize
  status:         active
```

Other node types: `D` decision (with reason) · `C` constraint · `A` assumption.
`status` is `active` · `invalidated` · `superseded by <id>`.

Invariants the ledger enforces:

- **No active stage depends on an invalidated node.**
- **Stage order in code equals `depends_on` order in the ledger.**
- **`implemented_in` is complete** — every stage maps to real code, and code
  that transforms data maps to a stage. Unmapped transforms are the usual
  place compensating patches hide.

---

## 5. Skill ownership

| Skill | Owns | Does **not** do |
|---|---|---|
| `spec-definition` | new work → stage ledger, decisions, acceptance checks | implementation |
| `change-diagnosis` | locate the first bad stage or invalidated premise; classify depth | writing code |
| `upstream-fix` | change spec first when needed, then the origin stage, then dependents | deciding whether upstream work was needed |
| `patch-audit` | judge a diff or codebase for compensating patches and order drift | repairing what it finds |

`patch-audit` judges only. A finding reopens the loop at `change-diagnosis`.

---

## 6. Routing

**New work** (feature, pipeline, module, experiment):
```text
spec-definition → implement stage by stage → patch-audit
```
Starting without a ledger is not allowed, even when the request looks clear.
Short is fine; absent is not.

**Bug, wrong output, or changed requirement on existing work:**
```text
change-diagnosis → [upstream-fix if depth ≥ stage] → patch-audit
```
Never edit on receipt of a bug report. Diagnose first.

Depths:

| Depth | Meaning | Route |
|---|---|---|
| **Local** | a defect inside one stage; its contract (inputs, outputs, invariants) holds | local edit in that stage |
| **Stage** | a stage's contract is wrong; dependents may consume bad output | `upstream-fix` |
| **Spec** | a decision, assumption, constraint, or stage order is wrong | `upstream-fix`, spec updated first |

When torn between two depths, choose the deeper one. Under-scoping produces
patches; over-scoping only costs time.

---

## 7. Loop and exit

Iterate `change-diagnosis → upstream-fix → patch-audit` until:

- no active stage depends on an invalidated node
- code stage order matches the ledger
- every data transform maps to a stage
- no compensating patch is present in the changed path
- each touched stage has a check that fails on the original defect

Cap at three iterations. If the same finding survives twice, it is not a code
problem — re-state it as the missing decision or evidence, ask the user that
one question, or record it under `Unresolved`. Never loop silently.

---

## 8. Prohibited behaviors

1. **Compensating downstream.** Re-correcting a value after the stage that
   should have produced it correctly.
2. **Editing before diagnosing** a bug or changed requirement.
3. **Code ahead of spec.** Changing stage order, contracts, or decisions in
   code without updating the ledger first.
4. **Preserving code for its own sake.** A stage whose premise is gone is
   deleted, not wrapped.
5. **Unmapped transforms.** Adding a data-changing step that is not a ledger
   stage.
6. **Narrating history in code.** Comments such as `# fix for earlier bug` or
   `# temporary correction` mark a patch, not a fix.
