---
name: verification-before-completion
description: Use when work is about to be called complete, fixed, correct, passing, deployed, or ready to merge and observable verification is possible.
---

# Verification Before Completion

## Rule

No success claim without fresh evidence from the current state.

1. State the exact claim and acceptance criteria.
2. Choose the smallest command, inspection, or artifact check that can prove it.
3. Run or inspect that evidence now.
4. Read the complete result, including exit status and warnings.
5. Report PASS, FAIL, or PARTIAL with concrete evidence and any proof gap.

Prefer focused tests first, then typecheck, lint, build, integration, or smoke checks when they materially support the claim. Validate configuration, manifests, Markdown, and prompt files with syntax/schema checks and observable discovery rather than irrelevant unit tests.

Use a `verifier` subagent when independent validation materially improves confidence. The leader still owns the final claim and must inspect the verifier's evidence.

If verification fails, continue fixing within the requested safe scope. If the required proof source is unavailable, report the limitation; do not translate missing evidence into a pass.
