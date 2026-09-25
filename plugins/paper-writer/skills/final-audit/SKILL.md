---
name: final-audit
description: Terminal pre-submission gate. Checks the manuscript for logical soundness, structural integrity, revision integrity (no appended corrections or patch-quilt texture), and that humanization changed no meaning. Judges and reports pass/fail; it does not repair — failures reopen the revision loop.
---

# final-audit

## Purpose

The last check before the manuscript leaves. It reads as a skeptical reviewer
seeing the document for the first time, with no knowledge of how it was
produced — and asks whether anything betrays that it was produced iteratively.

**This skill judges; it does not repair.** Everything it finds is routed back.
Repairing here would mean unaudited changes shipping in the final artifact.

## When to use

- after `humanizer`, at the end of a full-manuscript revision
- before submission, sharing with co-authors, or handing to the user as final
- after a style-only pass on frozen content

## When not to use

- mid-loop quality checking — that is `coherence-pass`
- as a way to fix problems: it reports them
- before `humanizer`, since one of its checks is that humanization preserved
  meaning

## Procedure

Run all four groups. Report every finding with location and severity.

### Logical

- no two statements in the document contradict each other
- no claim rests on a premise that the document itself undercuts
- no conclusion exceeds the evidence presented for it, in strength or in scope
- terminology is consistent: each defined term used with one meaning, each
  concept referred to by one term, notation stable throughout
- numbers agree across text, tables, figures, and abstract

### Structural

- the abstract describes the paper that exists, including its actual result
  and its actual scope
- every contribution the introduction promises is delivered in the body
- the discussion engages the results presented, not results from an earlier
  version of the analysis
- the conclusion introduces no claim, comparison, or implication that the body
  has not established
- section ordering matches the argument's dependency order

### Revision integrity

This group is the reason the skill exists. Look for the signature of a
manuscript assembled through patches:

- corrections appended after the claims they correct, rather than replacing them
- `however` / `nevertheless` / `strictly speaking` / `that said` / `more
  precisely` positioned so as to walk back an earlier sentence instead of
  contrasting two live positions
- obsolete wording: terminology, framing, or hypotheses from a superseded
  version still present anywhere, including headings and captions
- caveats guarding claims that no longer appear
- the same point explained twice because it moved during revision
- an uneven register or argumentative density suggesting sections written at
  different times under different assumptions
- passages a reader could use to reconstruct what an earlier draft said

The standard: **the manuscript must read as if written once, by someone who
had the final argument in hand from the first sentence.**

### Style

- `humanizer` changed no meaning: spot-check claims, hedges, scope conditions,
  citations, and numeric values against the pre-humanization version
- the prose has not been flattened into generic academic voice; where the
  author had a distinctive register, it survives
- no conversational drift, and no mechanical patterns reintroduced

## Routing on failure

| Finding | Route |
|---|---|
| logical or evidence defect | `revision-diagnosis` → `upstream-revision` |
| appended correction or stale claim | `revision-diagnosis` → `upstream-revision` |
| structural mismatch (abstract, promises, ordering) | `coherence-pass` |
| meaning changed during humanization | revert that sentence, then re-run `humanizer` on it |
| residual mechanical prose | `humanizer` |

After any substantive route-back, `final-audit` runs again in full. Do not
spot-check only the changed passage — a repair is itself a revision and can
leave its own traces.

## Failure modes

- **Passing the document because it reads smoothly.** Smooth prose is what
  `humanizer` produces; it is evidence of nothing about correctness. Audit
  against the ledger, not against impressions.
- **Fixing findings in place.** Produces unaudited final text.
- **Skipping the pre-humanization comparison.** The meaning-preservation check
  requires both versions; without it, hedge stripping ships.
- **Checking only sections that changed recently.** Contradictions live
  between a recent section and an old one.
- **Reporting findings without severity.** A numeric inconsistency in a results
  table and an awkward transition are not the same class of problem.
- **Declaring pass with open placeholders unremarked.** `[citation needed]`
  markers are legitimate output, but they must be surfaced prominently, never
  quietly left in the text.

## Output expectations

- a verdict per group: pass, or fail with findings
- each finding: location · severity (blocking / should-fix / optional) ·
  the specific defect · the route it takes
- an explicit list of every remaining placeholder and unresolved issue
- when everything passes: a plain statement that the manuscript is ready, with
  the placeholder list attached if any remain
- no edits to the manuscript
