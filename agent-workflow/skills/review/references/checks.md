# Review Checks

Apply each relevant check to every changed file type: source, templates, styles, data and translation files, specs, helpers, and configuration. The project's own rules add to these.

- **Conventions:** naming, module and dependency wiring, resource cleanup, and access control, matching the surrounding code.
- **Async safety:** unloaded or missing data in initialization, getters, templates, create and edit modes, and first render.
- **UI:** user flow, visible and disabled states, loading, empty and error rendering, scoped styles, roles, labels, and stable test selectors.
- **Localization:** no hard-coded visible text, safe fallbacks, and locale parity, where the project localizes.
- **Unit tests:** placement beside the code, meaningful assertions, mocked dependencies, critical and invalid inputs, unloaded state, and regression coverage.
- **End-to-end tests:** stable locators, helper reuse, deterministic waits, response assertions, test-data ownership, and the requested run strategy.
- **Correctness:** runtime failures, wrong or stale data, regressions, missing behavior, and unnecessary changes.

## Code smells

Check the changed lines against [smells.md](smells.md).
