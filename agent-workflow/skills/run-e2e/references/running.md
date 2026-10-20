# Running and Debugging

## Commands

- "Open the e2e UI": start the project's UI-mode script against the configured base URL, then wait for the user's selection.
- "Run e2e test": run the smallest test the request or context identifies. Ask when none is identifiable.

Take the command, project, arguments, and auth state from `package.json` and the runner config. Pass the base URL the project documents; ask when it cannot be resolved.

## Test selection

Run exactly the spec files the manager's handoff names, taken from the `E2E` line in the plan's Testing section, by file argument and name filter. When the runner cannot select by file, report `blocked` with the limit. A folder, a tag, or the full suite runs only when the user asks. Reuse no earlier or cached result; report this run's.

A run-only request changes no source, configuration, scripts, or specs, adds no `.only`, and disables no tests. Run without a pipe and report the real exit code; when it can't be captured, report it as unknown. Report per [reports.md](../../manager/references/reports.md). Check wrapper scripts for file writes before running them, and compare the worktree before and after, even on failure.

When a changed helper, selector, or test data is used by other specs, find them by search and report them under `Affected`, unrun.

## Debugging

Report the failed tests and the failed-only log path. Rerun only when verification was requested, and then only the failed tests; diagnosis goes to `developer`.
