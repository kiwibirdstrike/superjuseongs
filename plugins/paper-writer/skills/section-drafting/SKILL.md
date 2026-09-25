---
name: section-drafting
description: Convert a settled argument skeleton into academic prose, one paragraph per argumentative function. Use after paper-planning or after upstream-revision has fixed the reasoning. Prioritizes content and structure over style; polish comes later from humanizer.
---

# section-drafting

## Purpose

Turn ledger nodes into academic prose without changing what they assert. The
skeleton decides what is said; this skill decides how it is said, at the level
of clarity and correctness only.

This is not the stylistic stage. Prose that is accurate and plainly ordered is
a success here even if it is not yet graceful.

## When to use

- an argument skeleton exists and a section needs to be written
- `upstream-revision` has recomputed a chain and the affected passages need
  new prose
- a section exists only as notes or bullet points

## When not to use

- no ledger exists yet — run `paper-planning` first
- the request is to improve existing, correct prose — that is `humanizer`
- feedback has arrived on drafted text — that is `revision-diagnosis`

## Procedure

1. **Assign each paragraph one function.** Before writing it, state in one
   phrase what the paragraph establishes: *introduces the discriminating
   condition*, *reports the held-out result*, *rules out the capacity
   explanation*. A paragraph with two functions is two paragraphs.

2. **Open with the function.** The first sentence tells the reader what this
   paragraph establishes. It is not a transition, not a restatement of the
   previous paragraph, and not scene-setting. A reader who reads only the
   opening sentences should see the argument.

3. **Keep evidence and interpretation in separate sentences.** Report what was
   observed, then say what it means. Fusing them ("the striking 4.2-point gain
   demonstrates the superiority of the objective") smuggles an inference into
   a result and makes the claim impossible to audit later.

4. **Write each claim at its graded strength.** The ledger's `support` field
   governs the verb:

   | grade | licensed language |
   |---|---|
   | directly supported | *shows*, *establishes*, *demonstrates* |
   | indirectly supported | *indicates*, *is consistent with* |
   | inference | *suggests*, *implies that*, *the more plausible reading is* |
   | hypothesis | *we hypothesize*, *one possibility is* |
   | speculation | *may*, *could*, explicitly flagged as speculative |
   | unsupported | not asserted at all; `[citation needed]` |

   Never let an association become a causation across a sentence boundary.
   If the design does not identify a causal effect, no verb in the paragraph
   may imply one.

5. **Carry the scope.** Conditions recorded as `L` nodes belong in the sentence
   that makes the claim, not deferred to a limitations section where the
   reader meets them after already generalizing.

6. **Leave unsettled material visibly unsettled.** Do not write smooth,
   confident prose over a node graded `hypothesis` or `placeholder`. Smoothness
   here is a hazard: it disguises which parts of the draft are load-bearing and
   which are provisional.

7. **Record placement.** Update each node's `appears_in` with the section and
   paragraph just written. Skipping this is what later produces stale claims in
   the abstract.

## Failure modes

- **Claims not in the ledger.** Prose that introduces a new assertion to make a
  paragraph flow bypasses planning and evidence grading entirely. If drafting
  reveals that a needed claim is missing, add it to the ledger — graded — and
  say so.
- **Strength inflation.** Drafting language that is one grade stronger than the
  node. This is the most frequent way unsupported claims enter a manuscript.
- **Transition-led paragraphs.** Opening with *Furthermore* / *In addition*
  hides the paragraph's function and lets weakly connected paragraphs sit
  adjacent without anyone noticing.
- **Premature polish.** Tuning cadence on text whose premises may change.
- **Result-and-meaning fusion.** See step 3.

## Output expectations

- drafted prose for the requested section, in academic register
- one function per paragraph, visible from the opening sentence
- claim strength matching ledger grades throughout
- explicit `[citation needed]` / `[source: …]` markers wherever support is absent
- an updated ledger with `appears_in` filled for every node used
- a short note listing any claim added during drafting and its grade
