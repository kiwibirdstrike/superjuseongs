---
name: code-review
description: Use when reviewing a coherent change, evaluating review feedback, or checking a diff against its request, specification, and risk boundaries.
---

# Code Review

## Review Contract

Read the request, applicable specification, complete diff, callers of changed shared functions, and available verification output.

Report findings first, ordered by severity. Each finding names the location, concrete failure mode, evidence, and smallest correction. Separate correctness, security, data-loss, and compatibility defects from optional simplification.

Do not invent findings to fill categories. If no actionable defect is found, say so and state the remaining verification gap.

## Receiving Feedback

Validate each suggestion against the code and requirements before applying it. Resolve unclear or technically questionable feedback with evidence. Do not implement a reviewer preference that broadens scope or weakens correctness.

Prefer one review after a coherent change. Use an independent reviewer for risky or broad changes when separation materially improves confidence; the leader owns integration and final verification.

Route completion proof to `verification-before-completion`.
