# Running and Debugging

## Commands

- "Open the e2e UI": start the project's UI-mode script against the configured base URL, then wait for the user's selection.
- "Run e2e test": run the smallest test the request or context identifies. Ask when none is identifiable.

Take the command, project, arguments, and auth state from `package.json` and the runner config. Pass the base URL the project documents; ask when it cannot be resolved.

## Test selection

Select tests by file arguments and name filters. A run-only request changes no source, configuration, scripts, or specs; add no `.only` and disable no tests. Run without a pipe and report the real exit code; when it can't be captured, report it as unknown, never as 0. Report per the [test report](../../manager/references/dispatch.md) (section "Test report"): counts on success, the failed tests and a failed-only log on failure. Check wrapper scripts for file writes before running them, and compare the worktree before and after, even on failure. When selection is blocked, report it as `blocked` with the next step; never change the harness or broaden the suite without authorization.

## Debugging

Report the failed tests and the failed-only log path. Rerun only when verification was requested, and then only the failed tests; diagnosis goes to `developer`.
