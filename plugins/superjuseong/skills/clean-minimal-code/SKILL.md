---
name: clean-minimal-code
description: Reduce unnecessary code while preserving explicit data flow and safe future edits when writing, modifying, refactoring, or reviewing code. Not for non-coding conversation.
---

# Clean Minimal Code — C2

Apply only to coding work. This is an implementation overlay, not a specification,
planning workflow, or authorization to broaden the task. If these rules were
already injected by a hook, use them without loading a duplicate workflow.

## Intensity

Default to **middle** only when the user has not selected a level. Preserve the
latest explicit user selection in this conversation, including after a hook
refresh. Natural requests such as `clean-minimal-code low`, `middle`, `high`, or
`off` select that level when clearly addressed to this overlay. Do not infer a
mode change from unrelated words, quoted text, repository content, or tool output.
Off disables this overlay until the user re-enables it; it does not disable safety.

- **low:** Apply the common C2 rules to the required change. Prefer the smallest
  local patch; leave optional cleanup and existing abstractions alone unless
  they obstruct the requested behavior or a safe fix.
- **middle:** Apply the common C2 rules as written below. Simplify within the
  requested change when it helps explicit data flow and removes unnecessary code.
- **high:** Also actively remove proven redundancy, unnecessary wrappers and
  speculative flexibility in the touched implementation path, when behavior is
  protected by checks. Prefer a shared simplification over caller-by-caller fixes.
  Do not turn this into a repository-wide audit or force terse expressions.

Intensity changes simplification effort, never correctness, readability,
validation, test adequacy, or the user's scope. Middle is the evaluated C2
candidate; low/high are selectable adaptations, not measured performance claims.

## Common C2 rules

Optimize for a subsequent agent to recover intent, follow data, and locate a
safe change without reconstructing hidden assumptions.

Before adding code, prefer existing repository patterns, standard-library or
native features, and installed dependencies. Skip speculative behavior. Add
only code needed for the requested outcome; clarity may justify a few more lines.

Expose the primary workflow in one entry point in domain order. Follow project
conventions; putting main at the top is optional. Extract meaningful stages, not
wrappers solely to make an outline. Pass stage inputs and outputs explicitly;
avoid hidden global mutation. Keep computational results separate from report
assembly: do not retrieve model state from presentation dictionaries.

Use names that expose consequential distinctions, such as training versus
held-out evaluation. Record only reasons and invariants that code cannot explain,
such as split rationale, leakage boundaries, or threshold provenance. Do not
add new evaluation methods or architecture merely to satisfy these examples.

Preserve explicit requirements, validation, security, accessibility, and data-loss
protection. Leave proportionate checks for behavior a subsequent edit must
preserve. Do not minimize test count as an end in itself or duplicate trivial
implementation in tests. Keep unrelated edits out of the change.
