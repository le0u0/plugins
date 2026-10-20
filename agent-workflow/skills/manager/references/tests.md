# Tests

`developer` runs the unit specs for its own steps, per its `unit-tests.md`. The manager assigns `e2e-tester` at these points, when the user or plan authorizes tests:

- Once, after the last step passes and the plan's `E2E` line is not `none`.
- A rerun after a fix: the failed specs.
- When the user asks for a run.

A kind with no setup in the project is skipped, per [test-setup.md](test-setup.md). Any other change triggers no run. Resetting environments or test data happens only on the user's explicit request.

## e2e scope

e2e is slow, so it runs once, before review, never per step. The plan's `E2E` line in `## Testing` is the whitelist: assign `e2e-tester` to write the specs it names, then run exactly those files. Put the exact spec paths in the handoff. A folder, a tag, or the full suite runs only when the user asks. Each run reports its own result and reuses no earlier or cached one.

## Review request

Start `reviewer`. When it finishes, write the unit results from `checklist.md` and the e2e result into the `Tests` section of `review.md` yourself, since the reviewer never edits it.
