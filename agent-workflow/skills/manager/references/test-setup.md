# Test Setup

Each project has its own unit and e2e setup, and some have none. Before writing or running tests of a kind, find what the project uses:

- **Unit:** the runner config, the `package.json` scripts or build files, the existing spec files with their location and naming, and any project test rule or skill.
- **E2E:** the e2e runner config, its scripts, the e2e folder and existing specs, plus the base URL, auth state, and test data the project documents.

Write and run with exactly that runner, command, placement, and convention. Install and configure nothing.

When a kind has no setup, meaning no runner, no script, and no existing spec:
- Skip writing and running that kind.
- Say `no <unit|e2e> test setup` in the report, and under `Evidence` in `checklist.md`.
- Set one up only when the user asks.

When the setup is partial, such as a runner without a script, ask the user.
