# E2E Authoring

## Setup

- Explore the flow first per [exploration.md](exploration.md), and write from the recorded locators and steps, not from source alone.
- Adapt generated code to the closest spec; drop APIs the repository's runner version lacks.
- Match the closest spec's auth state, test data, imports, and helpers.
- For test-specific records, reuse the project's data helpers. Give each fixture a stable identity from the domain's real unique key, look up before creating, and never delete and recreate fixtures. Rerun behavior is unverified until `run-e2e` runs it.

## Files and imports

- Keep tests, hooks, and assertions in the spec file. Put utilities, data builders, setup, and interaction mechanics where the project keeps them.
- Search the project's shared helpers first and reuse a fitting one; never copy its logic.
- Ticket-specific functions go in one util beside the spec, named per the project's convention. Ask for a name when there is none. Keep ticket data out of shared helpers.
- Import only from shared helpers or the current folder's utils, never from another test folder or a spec. When another test needs a function, move its reusable part to the shared helpers first.
- Before finishing, check the diff for inline utilities, copied helper logic, cross-test imports, and ticket data in shared helpers. Do not refactor unrelated tests.

## Locators

Follow the project's locator contract, such as test IDs, roles, or labels. Never replace an available stable selector with text or class selectors. Use a class selector only when no stable contract can exist, and say why. Report a missing selector to `develop`; never add one to production code yourself.

## Actions, waits, and assertions

- Rely on the runner's actionability checks; assert visibility only when it is the behavior under test.
- Wait on the final UI state. When asserting an HTTP request, start the project's response helper before the action.
- Use condition-based waits, never fixed sleeps; retry wrappers only for a documented irreducible race.
- Keep assertions observable and scoped to the requested behavior.
