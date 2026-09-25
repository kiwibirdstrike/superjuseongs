---
name: coherence-pass
description: Read the whole manuscript independently of the order in which it was drafted, to find and repair artifacts of sequential generation and revision — a broken argument spine, failed paragraph handoffs, framing that contradicts later sections, and stale claims left behind by earlier versions. Runs inside the revision loop and fixes what it finds.
---

# coherence-pass

## Purpose

Text written sequentially carries the marks of the order it was written in.
Early sections commit to framings that later sections abandon; paragraphs
adjoin because they were written adjacently, not because one leads to the
other; revised claims survive in places nobody reread.

This skill reads the finished artifact **as a whole object**, not as a stream,
and repairs those artifacts. It is the loop's repair pass: it makes changes.

The approach is adapted from the non-autoregressive writing pass idea in
`msimchowitz/writing-skills`, reworked here around the claim ledger: the
checks below are dependency checks over the ledger, not only prose checks.

## When to use

- after `section-drafting` completes a section
- after `upstream-revision` propagates a change
- before `evidence-audit` in a full-manuscript revision
- whenever the manuscript has been assembled from independently written parts

## When not to use

- as a substitute for `revision-diagnosis` when new feedback arrives
- to grade claims against evidence — that is `evidence-audit`
- to improve sentence texture — that is `humanizer`
- as the final gate — that is `final-audit`, which judges and does not fix

## Procedure

Run all four checks. Each reads a *deliberately partial* view of the
manuscript; the partiality is what makes the defect visible.

### 1. Argument spine

Extract and read **only** the title, the headings, and the first sentence of
every paragraph, in order, as a continuous text.

That extract should, on its own, present the argument the manuscript now
makes. If it reads as a list of topics rather than a line of reasoning, the
paragraphs are not doing argumentative work. If it contains a framing that the
body has since abandoned — a hypothesis dropped in revision, a comparison no
longer central — the spine is stale.

Repair by rewriting the opening sentences to state what each paragraph
establishes, and by reordering paragraphs whose position no longer matches the
reasoning. Do not repair a broken spine by inserting summary sentences.

### 2. Paragraph handoff

For each adjacent pair, read **only** the last sentence of the first paragraph
and the first sentence of the second. Ask whether the second follows from the
first — whether a reader arriving at that boundary has what they need.

Where the handoff fails, the cause is one of: the paragraphs are in the wrong
order; a step of reasoning between them is missing; or they are not actually
related and one belongs elsewhere. Fix the cause.

**Adding a connective is not a fix.** If inserting *However* or *Furthermore*
appears to solve the problem, the problem was a missing inference and the
connective has hidden it.

### 3. Dependency consistency

Compare what the manuscript commits to in its framing positions against what
the body now argues: abstract · introduction · every topic sentence ·
discussion · conclusion.

Check that each ledger node's statement is asserted *identically in substance
and in strength* at every one of its `appears_in` locations. Common failures: a
claim hedged in the body but stated flatly in the abstract; a contribution
promised in the introduction that the body no longer delivers; a conclusion
generalizing past the scope the results section established.

### 4. Stale-claim detection

Walk every node with status `invalidated` or `superseded by …` and grep the
manuscript for its content — not its exact wording, which will have changed,
but its substance, including paraphrases, presuppositions, figure captions,
and section titles.

Any surviving assertion of an invalidated claim is deleted and, where the
passage still needs to say something at that point, rewritten from the current
ledger.

Also flag the two tells of patched text: a sentence that contradicts an earlier
sentence in the same document, and a caveat with no live claim to guard.

## Failure modes

- **Reading straight through.** Sequential reading re-creates the drafting
  order in your head and hides exactly the defects this skill targets. Extract
  the partial views literally.
- **Repairing with transitions.** See check 2. This is the dominant failure.
- **Fixing the spine by adding signposting.** *In this section, we will…*
  announces structure instead of having it.
- **Checking only sections that were recently edited.** Staleness accumulates
  in the sections nobody has touched.
- **Drifting into style edits.** Rewriting for cadence here mixes concerns and
  wastes work that `humanizer` will redo.
- **Silent scope creep into claim grading.** If a claim looks unsupported,
  note it for `evidence-audit`; do not regrade it here.

## Output expectations

- the repaired manuscript
- the extracted argument spine, so the user can verify the flow independently
- a list of repairs made, grouped by check, each naming the cause
  (order / missing inference / stale claim / framing mismatch) rather than the
  symptom
- items handed off: claims to be graded by `evidence-audit`, problems requiring
  a new `revision-diagnosis`
- an updated ledger where `appears_in` or ordering changed
