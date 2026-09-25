---
name: evidence-audit
description: Check every substantive claim against the evidence offered for it — grading support, catching claims stronger than their basis, catching correlation written as causation, verifying that citations say what they are cited for, and ensuring limitations constrain the conclusions. Prioritizes evidence alignment over citation formatting.
---

# evidence-audit

## Purpose

Verify that the manuscript claims exactly as much as its evidence licenses —
no more, and no less. Overclaiming is the more common failure, but a result
buried under unnecessary hedging is also a misalignment.

Citation *formatting* is not this skill's concern. Whether a citation actually
supports the sentence attached to it is.

## When to use

- after `coherence-pass` in a full-manuscript revision
- after drafting any section that makes empirical or causal claims
- whenever sources have been added, changed, or removed
- before `humanizer`, so that hedging is set correctly before prose is frozen

## When not to use

- the manuscript's structure is still in flux — grading claims that are about
  to be recomputed wastes the work
- the task is to fix a claim that fails the audit — that is `upstream-revision`
- formatting a bibliography to a style guide

## Procedure

1. **Enumerate substantive claims.** Every sentence that asserts a fact,
   relation, comparison, mechanism, or generalization. Skip only definitions,
   procedural description, and signposting.

2. **Grade each claim** against what is actually offered for it:

   - **directly supported** — the cited evidence or reported result states it
   - **indirectly supported** — it follows from cited evidence plus a stated,
     uncontroversial assumption
   - **inference** — a reasoned step beyond the evidence, presented as such
   - **hypothesis** — proposed for testing, not asserted
   - **speculation** — plausible, unestablished, and flagged
   - **unsupported** — nothing in the manuscript supports it

   Record the grade in the ledger. Any claim graded `unsupported` is reported
   as a defect regardless of how reasonable it sounds.

3. **Compare grade to language.** Read the verb and the modality against the
   grade table in `section-drafting` step 4. Flag every mismatch in either
   direction: *demonstrates* on an inference; *may possibly* on a directly
   supported result.

4. **Check every citation against its sentence.** Does the cited work claim
   what it is cited for? Watch for: citing a paper for a stronger version of
   its result; citing a survey for a primary finding; citing a preprint's
   abstract for a detail it does not contain; a citation inherited from an
   earlier draft whose sentence has since changed meaning.

   Where the source is not available to read, say so explicitly — mark it
   `unverified` rather than assuming it checks out.

5. **Audit causal language specifically.** For each causal verb — *causes*,
   *leads to*, *drives*, *because*, *due to*, *results in*, *attributable to* —
   identify what licenses the causal reading: an intervention, a control, an
   identification strategy. Where the design supports only association, the
   sentence must be rewritten to assert only association. Watch for causation
   that enters through a noun (*the effect of X on Y*) or through a mechanism
   story told alongside a correlational result.

6. **Check that limitations bind.** Each `L` node must constrain the claims it
   applies to, in the sentences that make them. A limitations section that
   lists a caveat the conclusion then ignores does not count.

7. **Check for fabrication.** Every citation, DOI, author, year, venue, and
   numeric result must trace to something real that was provided or verified.
   Anything that cannot be traced is replaced with `[citation needed]` or
   `[source: …]`. Do not preserve a plausible-looking reference on the
   assumption it came from somewhere.

8. **Report; do not rewrite the argument.** Findings that require changing what
   a claim says go to `upstream-revision`. This skill may adjust hedging
   language to match a grade, but may not restructure reasoning.

## Failure modes

- **Grading by how convincing the prose sounds.** Well-written speculation
  reads as established fact; grade against the evidence, not the sentence.
- **Accepting inherited citations.** A citation that was correct two revisions
  ago may now sit under a different claim.
- **Missing causation smuggled in by nouns or by narrative.** See step 5.
- **Treating the limitations section as sufficient.** A caveat quarantined at
  the end does not constrain a conclusion stated without it.
- **Fixing overclaims by adding hedges everywhere.** Blanket hedging destroys
  the reader's ability to tell strong results from weak ones. Grade precisely.
- **Prioritizing citation style over citation truth.**

## Output expectations

- a claim-by-claim table: claim · location · grade · evidence · verdict
- a list of misalignments, each with the specific defect (overclaim, causal
  overreach, citation mismatch, unbound limitation, unverifiable source)
- claims requiring `upstream-revision`, named with their ledger ids
- explicit placeholders inserted where support is missing
- an updated ledger with current `support` grades
- no fabricated references, and no silent removal of a citation that failed
  the check — report it
