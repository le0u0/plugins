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
- **Test run:** run the named unit specs per [unit-tests.md](references/unit-tests.md) and report the result.
- **Failure to fix:** the manager sends a failed spec or a bug report. Diagnose per [diagnose.md](references/diagnose.md), then fix.
- **Approved plan:** a `plan.md` from `plan`. Follow [step-execution.md](references/step-execution.md); after the last step, [validation.md](references/validation.md).

## Rules

- Work on the current branch; never create or push branches. Commit only per the plan's per-step delivery, or when the user approves the work and the exact one-line message. Otherwise leave work uncommitted.
- Ask before going beyond the request or plan. Delete only files the plan lists.
- End-to-end coverage goes to `e2e-tester` (`write-e2e`), only when the user or plan asks.

## Workflow

1. Read the [project references](../manager/references/project-references.md) for the feature type: rules, project-local skills such as a `create-*` skill, and the nearest comparable feature.
2. When the request leaves out a choice a project skill asks for, such as a variant or target folder, ask once. Skip what the request already says.
3. Build test-first, batched per step (a direct request is one step), and do every part yourself:
   0. Find the unit test setup per [test-setup.md](../manager/references/test-setup.md). With none, write and run no specs, say so, and continue with 2 and 4.
   1. Write the step's failing specs per `write-unit`, one behavior at a time, at the seam the step's `Test` names. For a direct request, state the seam in one line and proceed.
   2. Write the smallest production change that matches nearby code, and only what the specs require.
   3. Run the step's focused unit specs per [unit-tests.md](references/unit-tests.md), and fix the code on a failure.
   4. When they pass, commit per [step-execution.md](references/step-execution.md) and start the next step.

   Without test authorization, stop after 2 and report the specs as not run. Skip the loop for changes with no unit-testable behavior, such as pure styling, and say so.
4. Format only changed files. Self-check: each requested behavior maps to a changed file and a spec, and the diff has nothing unrelated.
