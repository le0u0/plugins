---
name: write-unit
description: 'Write or fix unit specs for changed code, following the project''s test rules, without running them. Use for "add unit tests" or "fix this spec".'
effort: medium
metadata:
  tier: standard
---

# Write Unit

Report per [reports.md](../manager/references/reports.md). Production fixes go to `develop`; test runs go to `run-unit`.

## Workflow

1. Read the [project references](../manager/references/project-references.md) for testing: unit-testing rules, project-local testing skills, the test framework's config, and the nearest comparable spec. Follow their conventions for mocking, setup, and file placement. Then read [test-quality.md](references/test-quality.md).

2. List each changed behavior from the diff or named files; cover only those unless asked. Read the target and its nearest comparable spec.

3. Create or update only the spec files the project places beside the code. Directly above each new or changed top-level `describe`, keep a coverage comment for the whole unit:

   ```ts
   /**
    * Covered:
    * - <behavior the spec tests>
    *
    * Not Covered:
    * - <behavior that should be tested but is not>
    */
   describe('...', () => {
   ```

   `Covered` lists every behavior tested, old and new. `Not Covered` lists behaviors that should be tested but are not, including unchanged ones outside scope; omit it when empty.

   Done when each changed behavior has setup and a meaningful assertion covering the regression and relevant missing, invalid, unloaded, and edge inputs, and the comment is accurate.

4. Self-check by reading: setup reaches the intended state, and assertions would fail on the regression. Report production defects found. Hand back without running tests.

Leave the protected files listed in [running.md](../run-unit/references/running.md) and unrelated specs unchanged. `review` owns formal review.
