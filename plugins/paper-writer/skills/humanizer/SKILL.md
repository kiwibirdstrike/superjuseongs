---
name: humanizer
description: Remove the mechanical texture of machine-generated academic prose — formulaic constructions, transition overuse, manufactured tripartite lists, inflated significance language, redundant signposting and summary — without changing any meaning. Runs once, after the argument is stable, and has no authority over claims, hedging, or structure.
---

# humanizer

## Purpose

Improve prose texture only. By the time this skill runs, the reasoning is
settled; what remains are the surface regularities that make generated academic
writing recognizable and tiring to read.

**This skill has no authority over meaning.** It may not add, remove,
strengthen, or weaken a claim; may not change hedging level; may not reorder
argument. Hedges encode epistemic grades set by `evidence-audit` — they are
content, not style.

## When to use

Only when **all** preconditions hold:

- the argument is stable and the revision loop has exited
- factual and evidence issues are resolved
- paragraph structure is settled
- the remaining changes are prose-level only

Also usable for a genuine style-only request on content the user has frozen.

## When not to use

- **inside the revision loop.** Do not humanize unstable reasoning. Polishing
  text that is about to be recomputed wastes effort, and — worse — makes
  wrong claims read as confident, which is exactly the condition under which
  reviewers and authors stop noticing them.
- when a substantive issue is still open
- when the user's request implies a meaning change; route to
  `revision-diagnosis` instead

## Procedure

Work paragraph by paragraph. For each pattern, remove **instances that do no
work**, not the pattern itself — every one of these constructions is
legitimate when it is earned.

1. **Formulaic constructions.** `not X but Y` used for emphasis rather than
   genuine contrast; `it is important to note that`; `plays a crucial role in`;
   `serves to`; `in order to` where `to` suffices; `a wide range of`.

2. **Transition overuse.** Repeated `however` / `therefore` / `moreover` /
   `furthermore` / `additionally`. Where the logical relation is already clear
   from content and order, delete the connective. Never add one.

3. **Manufactured three-part lists.** Triples where the third item is a
   restatement or a weak filler exists to complete the rhythm. Cut to the items
   that carry distinct content.

4. **Inflated significance.** `significantly`, `substantially`, `dramatically`,
   `remarkably`, `crucially`, `strikingly` used for emphasis rather than
   measurement. In quantitative writing `significant` is a statistical term;
   do not use it loosely. **Removing an intensifier must not change a claim's
   strength** — if it would, the word was doing epistemic work and stays.

5. **Generic paragraph closers.** Final sentences that restate the opening
   without adding anything: *Taken together, these results highlight the
   importance of…*. Delete; end on the substantive sentence.

6. **Excessive signposting.** *In this section, we will…*, *As mentioned
   above…*, *We now turn to…*. Keep only navigation a reader genuinely needs in
   a long document.

7. **Repetitive topic-sentence syntax.** Consecutive paragraphs opening with
   the same shape (*Another factor is…*, *A further consideration is…*). Vary
   the construction; keep each opening's function visible.

8. **Redundant summary.** Mid-document recaps of what was just said. Keep the
   abstract and the conclusion; cut the rest.

9. **Generic academic filler.** *In recent years, there has been growing
   interest in…*, *This raises important questions about…*. Replace with the
   specific content, or delete.

10. **Defensive over-hedging.** Stacked hedges (*may potentially suggest that
    it could be possible*) reduced to a single hedge at the **same** epistemic
    level. One hedge stays. Removing the last hedge is a meaning change and is
    prohibited.

### Preserve without exception

technical terminology · epistemic uncertainty and hedging level · citations and
their placement · equations, notation, symbols, units · scientific
qualifications and scope conditions · the author's own established voice, where
existing text shows one · deliberate repetition that aids clarity (a term
repeated rather than elegantly varied is usually correct in technical prose).

### Escalation

If a logical problem, an unsupported claim, or a stale claim surfaces while
editing: **stop, do not fix it here**, and escalate to `revision-diagnosis`.
Style work resumes after the substantive loop closes again.

## Failure modes

- **Running early.** The single most damaging misuse: polished unstable prose
  looks finished and stops getting scrutinized.
- **Hedge stripping.** Deleting *may* or *suggests* to make a sentence
  crisper. This silently upgrades a claim's strength — an evidence violation
  dressed as a style edit.
- **Elegant variation of technical terms.** Swapping a defined term for a
  synonym to avoid repetition changes the referent.
- **Over-humanizing.** Conversational register, rhetorical questions, first
  person where the venue does not use it, contractions in formal prose. The
  target is unmechanical academic writing, not casual writing.
- **Pattern purging.** Deleting every `however` in the document produces prose
  as uniform as what it replaced.
- **Fixing logic in passing.** See escalation.

## Output expectations

- the edited manuscript, meaning-identical to the input
- a change summary by category, with counts
- an explicit statement that no claim, hedge, citation, or scope condition was
  altered — and, if any edit came close to that line, the specific sentence
  flagged for the user to confirm
- anything escalated to `revision-diagnosis`, listed
