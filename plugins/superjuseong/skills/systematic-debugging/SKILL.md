---
name: systematic-debugging
description: Use when code, tests, builds, integrations, or runtime behavior fail unexpectedly and the root cause is not yet proven.
---

# Systematic Debugging

## Principle

Fix the root cause once at the narrowest shared boundary. Do not patch the reported symptom before tracing the real flow and its callers.

## Workflow

1. Reproduce the failure with the smallest reliable command or scenario.
2. Read the complete error and identify the first bad state, not only the final exception.
3. Trace inputs, callers, transformations, and sibling paths through the shared boundary.
4. Form one falsifiable hypothesis and run the smallest diagnostic that can disprove it.
5. For a bug fix, leave one runnable regression check that fails before the fix.
6. Apply the minimum root-cause correction, then run the regression check and relevant surrounding checks.

When reproduction is unavailable, distinguish evidence, inference, and missing proof. Do not present a hypothesis as a diagnosis.

Use a `debugger` subagent only when an independent investigation materially improves confidence or latency. The leader verifies the result.

## Stop Rule

Stop when the cause and fix are directly supported by evidence, or report the exact unavailable proof source. Do not enter retry loops or broaden into unrelated cleanup.
