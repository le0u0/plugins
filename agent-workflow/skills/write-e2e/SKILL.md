---
name: write-e2e
description: 'Write or fix end-to-end specs, helpers and test data, find locators, or explore UI, without running specs. Use for "add an e2e test", "find the locator for X" or "reproduce this in the UI".'
effort: medium
metadata:
  tier: standard
---

# Write E2E

Report per [reports.md](../manager/references/reports.md). Production changes, including missing test selectors, go to `develop`; test runs go to `run-e2e`.

1. Find the e2e test setup per [test-setup.md](../manager/references/test-setup.md); with none, write no specs and say so. Read the [project references](../manager/references/project-references.md) for e2e: rules, project-local e2e skills, the runner config, and the closest spec. Resolve the auth state, test data, helpers, and base URL they use.
2. Read one branch:
   - Author a spec or its data: [exploration.md](references/exploration.md) first, then [authoring.md](references/authoring.md).
   - Explore UI or discover locators: [exploration.md](references/exploration.md).
3. Do only the requested work. When you change a shared helper, selector, or test data, search for other specs that use it and list them in your report under `Affected`.
4. Check by reading: each requested behavior has an observable assertion, stable locator, deterministic wait, and repository-owned test data.

Never run specs in this skill, even after a fix; run them only per `run-e2e`, when authorized. Format only changed files. Formal review goes to `review`.
