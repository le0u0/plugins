# Run Focused Unit Tests

## Steps

1. Read the `package.json` scripts (or the project's build files), the test runner config, and the runtime version. Check wrapper scripts first; pick a command that selects tests without rewriting source or configuration. Never install or upgrade a runner to gain a selector.
2. Select the spec with command arguments, such as a file path or name filter, using the project's documented command. Quote globs for zsh. Keep the configured project, browser, and watch options.
3. Record the worktree and index state first, including existing user edits to test setup and configuration. Run only the authorized target, without a pipe, and report its real exit code; when it can't be captured, report it as unknown, never as 0. Report per the [test report](../../manager/references/reports.md): counts on success, the failed specs and a failed-only log on failure. Report zero tests, compilation failures, and environment failures apart from assertion failures.
4. Check status and diff afterward, even on failure. Tracked source, configuration, and user files must be unchanged. When a helper rewrote files, stop using it, undo only this run's changes from the captured content, keep earlier edits, and report it. Never use a broad checkout or reset.

## Protected files

Test bootstrap and runner configuration, compiler configuration, and package scripts stay unedited. Add no focused or disabled tests. Repairing test infrastructure is separate explicit scope.

## Blocked selection

When the runner cannot select the tests or the command is blocked, report it as `blocked` with the exact limit and the next step. Ask before running the full suite; never rewrite the harness or unrelated tests. Report unrelated compilation failures without editing those specs.
