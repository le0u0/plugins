---
name: develop
description: 'Implement production code from a request or an approved plan, following the project''s own rules and skills. Use for "implement step 2", "build this feature", or when manager assigns it.'
effort: medium
metadata:
  tier: standard
---

# Develop

Follow [dispatch](../manager/references/dispatch.md).

## Modes

- **Direct request:** implement what the user asked and report the changed files. No plan, task folder, checklist, or branch check.
- **Approved plan:** a `plan.md` from `plan`. Follow [step-execution.md](references/step-execution.md); after the last step, [validation.md](references/validation.md).

## Rules

- Never create or push branches. Leave work uncommitted unless the user approves the work and the exact commit message.
- Ask before going beyond the request or plan.
- End-to-end coverage goes to `write-e2e`, only when the user or plan asks.

## Workflow

1. Read the [project references](../manager/references/dispatch.md) (section "Project references") for the feature type: rules, project-local skills such as a `create-*` skill, and the nearest comparable feature.
2. When the request leaves out a choice a project skill asks for, such as a variant or target folder, ask once. Skip what the request already says.
3. Build test-first, batched per step (a direct request is one step). Do every part yourself:
   1. Write every failing spec for the step per `write-unit`, at the seam the step's `Test` names. For a direct request, state the seam in one line and proceed.
   2. Write the smallest production change that matches nearby code. Write only what the failing specs require; no speculative code.
   3. Return `Open: run the specs`. The manager has `unit-tester` run them per `run-unit`; a failure comes back to you for a fix, and the specs are rerun until they pass.

   Never run tests yourself. When told not to run tests, keep 1 and 2 and report the specs as not run. Work in vertical slices: one behavior, its failing spec, its minimal code, then the next, so each slice learns from the last. Skip the loop for changes with no unit-testable behavior, such as pure styling, and say so.
4. Format only changed files. Self-check: each requested behavior maps to a changed file and a spec, and the diff has nothing unrelated.
