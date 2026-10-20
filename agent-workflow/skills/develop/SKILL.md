---
name: develop
description: 'Implement production code from a request or an approved plan, following the project''s own rules and skills. Use for "implement step 2" or "build this feature".'
effort: medium
metadata:
  tier: standard
---

# Develop

Report per [reports.md](../manager/references/reports.md).

## Modes

- **Direct request:** implement what the user asked and report the changed files. No plan, task folder, checklist, or branch check.
- **Failure to fix:** the manager sends a failed spec or a bug report. Diagnose per [diagnose.md](references/diagnose.md), then fix.
- **Approved plan:** a `plan.md` from `plan`. Follow [step-execution.md](references/step-execution.md); after the last step, [validation.md](references/validation.md).

## Rules

- Work on the current branch; never create or push branches. Commit only per the plan's per-step delivery, or when the user approves the work and the exact one-line message. Otherwise leave work uncommitted.
- Ask before going beyond the request or plan. Delete only files the plan lists.
- End-to-end coverage goes to `e2e-tester` (`write-e2e`), only when the user or plan asks.

## Workflow

1. Read the [project references](../manager/references/project-references.md) for the feature type: rules, project-local skills such as a `create-*` skill, and the nearest comparable feature.
2. When the request leaves out a choice a project skill asks for, such as a variant or target folder, ask once. Skip what the request already says.
3. Build test-first, batched per step (a direct request is one step). Do every part yourself:
   1. Write every failing spec for the step per `write-unit`, at the seam the step's `Test` names. For a direct request, state the seam in one line and proceed.
   2. Write the smallest production change that matches nearby code. Write only what the failing specs require; no speculative code.
   3. Return `Open: run the specs`. The manager has `unit-tester` run them per `run-unit`; a failure comes back to you for a fix, and the specs are rerun until they pass.

   Hand every test run to the manager as `Open`. When told not to run tests, keep 1 and 2 and report the specs as not run. Work in vertical slices: one behavior, its failing spec, its minimal code, then the next, so each slice learns from the last. Skip the loop for changes with no unit-testable behavior, such as pure styling, and say so.
4. Format only changed files. Self-check: each requested behavior maps to a changed file and a spec, and the diff has nothing unrelated.
