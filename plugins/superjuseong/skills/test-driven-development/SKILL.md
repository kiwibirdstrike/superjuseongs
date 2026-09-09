---
name: test-driven-development
description: Use when implementing or changing nontrivial behavior, fixing a reproducible bug, or refactoring logic whose contract must remain stable.
---

# Test Driven Development

## Cycle

1. Write the smallest check that expresses the required behavior.
2. Run it and confirm it fails for the intended reason.
3. Implement the minimum change that makes it pass.
4. Run the focused check and relevant surrounding checks.
5. Refactor only while the checks remain green.

Prefer a real behavior check over assertions about mocks or implementation details. One focused regression test is enough when it proves the branch, loop, parser, money/security path, or bug being changed.

## Proportionate Validation

- Trivial one-line changes with no behavioral branch: inspect the diff and run the smallest relevant check.
- Configuration, Markdown, manifests, and prompt files: validate syntax, schema, references, and observable loading behavior; do not manufacture a unit test.
- Generated or throwaway exploration: label it and discard it before production work.

Do not ask whether to use TDD when the category is clear. If a failing test cannot be produced, state why and use the closest runnable proof rather than pretending tests exist.
