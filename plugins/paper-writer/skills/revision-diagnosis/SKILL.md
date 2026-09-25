---
name: revision-diagnosis
description: Analyze what a piece of feedback or self-critique actually changes, locate the earliest affected claim and everything downstream of it, and classify the revision depth as surface, local semantic, argumentative, or structural. Run this before any edit. Produces a diagnosis and routing decision, never replacement prose.
---

# revision-diagnosis

## Purpose

Decide the **scope** of a change before anything is rewritten. Feedback arrives
pointing at a sentence, but it rarely applies only to that sentence. This skill
finds where the change actually enters the dependency graph and what it
invalidates.

It is a routing decision, not a writing task. It produces no replacement prose.

## When to use

- **always**, as the first response to any feedback on existing text: user
  comments, reviewer reports, advisor notes, self-critique
- when `final-audit` or `humanizer` escalates a substantive problem
- before re-entering a revision loop iteration

## When not to use

- no manuscript text exists yet — that is `paper-planning`
- the diagnosis is complete and a rewrite is now required — hand to
  `upstream-revision`
- purely mechanical corrections the user has already scoped for you
  (a misspelled name, a wrong figure number) — apply them directly

## Procedure

1. **State what changed, factually.** In one sentence, in the feedback's own
   terms, with no interpretation added. *Parameter count was held constant
   across arms; the arms differed in training objective.* If the feedback is
   ambiguous about what it asserts, ask before diagnosing — a mis-scoped
   diagnosis propagates a wrong rewrite through the whole document.

2. **Locate the root affected node.** Walk the ledger and find the **earliest**
   node the new information contradicts, weakens, or redefines. Not the
   sentence the user commented on — the first node upstream of it that is no
   longer valid. Feedback on a conclusion is very often feedback on a premise
   three nodes back.

3. **Compute the downstream set.** Every node reachable from the root by
   `depends_on` edges. For each, mark whether it is invalidated, weakened,
   unaffected, or now needs a different justification. Then collect the union
   of their `appears_in` fields — that is the set of passages in the manuscript
   that must be inspected, and it will include places the user did not mention
   (abstract, introduction, conclusion, figure captions, section headings).

4. **Apply the counterfactual test** to each affected passage:

   > If this information had been known when the passage was first written,
   > would these sentences still have been written this way?

   - **Yes** → local revision is enough for that passage.
   - **No** → that passage requires upstream rewriting.

5. **Assign exactly one depth** for the change as a whole:

   - **Surface** — grammar, notation, terminology, wording. No node changes.
   - **Local semantic** — one node's statement changes; its dependents survive
     unchanged and their justifications still hold.
   - **Argumentative** — a premise, interpretation, causal relation,
     comparison, definition, or scope changes; dependents must be recomputed.
   - **Structural** — the framing, ordering, or architecture of the argument
     changes; the section plan itself must be revisited.

   When torn between local semantic and argumentative, choose **argumentative**.

6. **Route.** Surface and local semantic → local edit, then verify every
   `appears_in` location for consistency. Argumentative and structural →
   `upstream-revision`, mandatory. Structural additionally re-enters
   `paper-planning` for the affected part of the skeleton.

7. **Flag contradictions in the feedback itself.** If the new information
   conflicts with evidence already in the ledger, do not silently pick a
   winner. Report the conflict and ask which holds.

## Failure modes

- **Diagnosing at the point of complaint.** Treating the commented sentence as
  the root is the single most common cause of patched-looking manuscripts.
- **Under-scoping to avoid a large rewrite.** Rewriting is cheap; an
  internally inconsistent manuscript is not.
- **Skipping the `appears_in` sweep.** The abstract is the most frequently
  missed stale location, because feedback is usually given on body text.
- **Producing prose.** Drafting a suggested replacement here pre-empts
  `upstream-revision` and typically anchors it to the old phrasing.
- **Batching unrelated feedback into one diagnosis.** Independent changes get
  independent diagnoses; conflated roots produce over-broad rewrites.

## Output expectations

A diagnosis block, and nothing else:

```text
Change:        parameter count held constant; arms differ in training objective
Root node:     C1 (gain attributable to increased capacity) — invalidated
Downstream:    I1 invalidated · M weakened, needs new justification · L2 unaffected
Affected text: abstract ¶1 · §1 ¶2 · §4 ¶3 · §6 ¶1 · Fig. 2 caption
Counterfactual: no — these passages would not have been written this way
Depth:         argumentative
Route:         upstream-revision, root C1
Open question: none
```

No rewritten sentences. No stylistic commentary.
