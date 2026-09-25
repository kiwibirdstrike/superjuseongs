---
name: upstream-revision
description: Rewrite a manuscript from the earliest invalidated claim forward, recomputing all dependent reasoning, so the result reads as if the corrected information had been known from the start. Use when revision-diagnosis returns argumentative or structural depth. Never appends corrections after the affected text.
---

# upstream-revision

## Purpose

Recompute reasoning that new information has invalidated. The unit of work is
the dependency subgraph rooted at the affected claim, not the sentence that
received the comment.

> **Rewrite upstream, then propagate downstream.**

Given `A → B → C`, feedback that `A` is actually `A'` does **not** produce:

```text
A → B → C → "However, A is actually A'."
```

It produces a freshly computed:

```text
A' → B' → C'
```

where `B'` and `C'` are whatever follows from `A'` — which may be different
claims, weaker claims, or no claim at all.

## When to use

- `revision-diagnosis` returned depth **argumentative** or **structural**
- a premise, interpretation, causal relation, comparison, definition, scope,
  or conclusion has changed
- an `evidence-audit` finding shows a claim exceeds its support
- a stale claim from a previous revision has been found still asserted

## When not to use

- depth is surface or local semantic — make the local edit instead
- no diagnosis has been run — run it first; this skill needs a root node
- the problem is prose quality with sound reasoning — that is `humanizer`

## Procedure

1. **Start at the root node, not the edit site.** Take the root from the
   diagnosis. Rewrite the passage that first asserts it, from the corrected
   fact forward.

2. **Recompute each downstream node rather than editing its text.** For each
   node in the downstream set, ask what now follows from the corrected
   premises — then write that. Do not open the existing sentence and adjust it;
   old phrasing anchors the new claim to the old one. Some nodes will survive
   with the same statement and a different justification; some will need to be
   weakened a grade; some are simply gone.

3. **Delete rather than qualify.** A claim whose premise has been removed is
   deleted. It is not hedged, not moved to a limitations paragraph, and not
   retained "for context".

4. **Rewrite every `appears_in` location in the same pass.** Abstract,
   introduction, topic sentences, discussion, conclusion, figure captions,
   section headings. A revision that stops at the body creates exactly the
   inconsistency this plugin exists to prevent.

5. **Remove the sediment of earlier versions.** Sweep the affected passages and
   delete: invalidated claims · stale caveats that guarded a claim no longer
   present · duplicated explanations introduced because a point moved ·
   defensive hedging that was answering an objection to the old claim ·
   transitions (`however`, `although`, `it should be noted`) that existed only
   to manage a tension the rewrite has dissolved.

6. **State the corrected fact positively.** Write what is the case, not what
   turned out not to be the case. *Because parameter count was held constant,
   the difference cannot be attributed to capacity* — not *we initially
   attributed this to capacity, but parameter count was held constant.* The
   manuscript is not a record of its own revision history.

7. **Set the new strength from the evidence, not from the old sentence.** The
   replacement claim is graded fresh in the ledger. A confident claim replaced
   after feedback usually becomes a weaker one; do not inherit the old
   confidence.

8. **Update the ledger.** Mark invalidated nodes `invalidated` or
   `superseded by <id>`, add new nodes with grades and dependencies, refresh
   `appears_in`. Verify the invariant: no active node depends on an
   invalidated node.

9. **Read the rewritten passages cold.** If a reader could reconstruct that an
   earlier version said something different, the rewrite is not finished.

## Worked example

Ledger before: `C1` gain attributable to increased capacity → `I1` larger
models inherently better suited → `M` scale drives improvement.

Feedback: parameter count held constant; arms differed in training objective.

Wrong output — original retained, correction appended:

> The improvement is primarily attributable to increased model capacity. This
> suggests that larger models are inherently better suited for this task.
> However, parameter count was held constant, so the training objective may
> also have contributed.

Right output — `C1` deleted, `I1` recomputed, strength reset to what the
design supports:

> Because parameter count was held constant across the compared models, the
> observed performance difference cannot be attributed to increased model
> capacity. The results instead indicate that the training objective is the
> more plausible source of the improvement.

Note three things. The capacity claim is absent, not qualified. The
generalization about larger models is gone entirely, because its only premise
was the deleted claim — it was not merely softened. And the replacement says
*more plausible source*, an inference-grade verb, because a single controlled
comparison does not establish the objective as the cause.

## Failure modes

- **Editing in place.** Opening the old sentence and modifying it, which
  preserves its framing and usually its confidence.
- **Qualifying instead of deleting.** Turning an invalid claim into a hedged
  claim. The evidence for it is gone; hedging is not the remedy.
- **Stopping at the diagnosed section.** Leaving the abstract or conclusion
  asserting the superseded version.
- **Leaving orphaned caveats.** Sentences defending against objections to a
  claim that no longer exists — a strong signal of a patched manuscript.
- **Narrating the revision.** *Contrary to our initial interpretation…* The
  final text must not show that an interpretation was revised.
- **Inheriting old confidence.** Replacing a strong wrong claim with an equally
  strong new one that the evidence does not support either.

## Output expectations

- rewritten passages for every affected location, complete, not diffs against
  obsolete text
- an updated ledger with statuses, grades, and `appears_in` current
- a short changelog **for the user, kept out of the manuscript**: which nodes
  were invalidated, what replaced them, what was deleted
- prose containing no trace of the prior version
