---
name: paper-planning
description: Build the argument skeleton and dependency graph for a paper or section before any prose is written. Use when starting a new paper, a new section, or when a structural revision requires re-planning the argument. Produces the claim ledger, not prose.
---

# paper-planning

## Purpose

Decide what the paper argues and what that argument rests on, before a single
sentence of prose exists. This skill produces the **claim ledger** (see
`AGENTS.md` §4) — the dependency graph that every later skill reads from.

Paragraph order is an output of the argument, not an input to it. Determine
dependencies first; ordering follows.

## When to use

- starting a new paper, or a new section of an existing one
- a structural revision has changed the argument architecture and the skeleton
  must be recomputed
- the user supplies raw results or notes and wants them turned into a paper
- an existing draft has no ledger and needs one reconstructed before revision

## When not to use

- any request that is about wording, flow, or polish
- responding to feedback on existing prose — that starts at `revision-diagnosis`,
  which will call this skill only if it diagnoses a structural change
- a single paragraph whose place in the argument is already fixed

## Procedure

1. **Separate the inputs.** Sort everything the user has given you into:
   research question · main claim · supporting claims · evidence ·
   assumptions · competing explanations · limitations · expected conclusion.
   Keep these categories strictly apart. The most common planning error is
   filing a hoped-for conclusion under "evidence".

2. **Grade every evidence node honestly.** For each `E`, record what it
   actually shows and where it comes from. Evidence you do not have gets a
   node with `status: placeholder` and an explicit `[source: …]` marker — not
   an omission, and not an assumption dressed as a finding.

3. **Build the dependency chain.** Write the graph explicitly:

   ```text
   E1  held-out accuracy +4.2pts under objective B
   E2  parameter count identical across arms
        ↓
   C1  the gain is not attributable to capacity
        ↓
   I1  the training objective is the more plausible source
        ↓
   M   objective design, not scale, drives the improvement in this regime
   ```

   Every arrow must be a real inference someone could challenge. If you cannot
   state what licenses an arrow, the arrow is missing a premise — add it as an
   `A` node rather than leaving it implicit.

4. **Name the competing explanations.** For each `I`, ask what else would
   produce the same evidence. Record survivors as `X` nodes with the evidence
   that would discriminate between them. An interpretation with no considered
   alternatives is not yet an interpretation.

5. **Bound the scope.** State the population, regime, dataset, and condition
   under which `M` holds. Record each boundary as an `L` node. Scope written
   down at planning time is scope that will not silently inflate during drafting.

6. **Derive the section plan.** Only now map nodes onto sections and
   paragraphs, so each paragraph has one job and each `appears_in` field can be
   filled during drafting.

7. **Check the skeleton before handing off.** Every `C` and `I` traces back to
   at least one `E` or an openly declared `A`; nothing in the ledger is
   orphaned; `M` follows from the chain rather than merely being compatible
   with it.

## Failure modes

- **Evidence invented to complete a chain.** If a chain needs a fact you do not
  have, the correct output is a placeholder node and a note that the argument
  is currently unsupported — not a plausible-sounding finding.
- **Assumptions left implicit.** An unstated premise cannot be invalidated by
  feedback, so it survives revisions it should not have survived.
- **The conclusion planned first, evidence back-filled.** Build forward from
  evidence; if the chain does not reach the desired `M`, report that.
- **Planning at paragraph granularity.** Producing an outline of headings
  rather than a dependency graph defeats the purpose; later skills will have
  nothing to propagate through.
- **Drifting into prose.** Full sentences here get recycled as draft text and
  escape the drafting skill's discipline.

## Output expectations

- the claim ledger, in the format of `AGENTS.md` §4, with every node typed,
  graded, and linked
- an explicit dependency chain from evidence to main conclusion
- a section plan mapping nodes to sections and paragraph slots
- an explicit list of what is not yet supported, and what source or experiment
  would support it
- no prose, no topic sentences, no draft paragraphs
