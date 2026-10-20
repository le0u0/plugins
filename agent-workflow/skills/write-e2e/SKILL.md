---
name: write-e2e
description: 'Write or fix end-to-end specs, helpers and test data, find locators, or explore UI, without running specs. Use for "add an e2e test", "find the locator for X", "reproduce this in the UI", or when manager assigns it.'
effort: medium
metadata:
  tier: standard
---

# Write E2E

Follow [dispatch](../manager/references/dispatch.md). Production changes, including missing test selectors, go to `develop`; test runs go to `run-e2e`.

1. Read the [project references](../manager/references/dispatch.md) (section "Project references") for e2e: rules, project-local e2e skills, the runner config, and the closest spec. Resolve the auth state, test data, helpers, and base URL they use.
2. Read one branch:
   - Author a spec or its data: [exploration.md](references/exploration.md) first, then [authoring.md](references/authoring.md).
   - Explore UI or discover locators: [exploration.md](references/exploration.md).
3. Do only the requested work.
4. Check by reading: each requested behavior has an observable assertion, stable locator, deterministic wait, and repository-owned test data.

Never run specs, even after a fix; `e2e-tester` runs them, so a result comes from one place. Format only changed files. Formal review goes to `review`.
