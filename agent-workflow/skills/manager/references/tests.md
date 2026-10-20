# Tests

Assign `unit-tester` or `e2e-tester` at these points, when the user or plan authorizes tests:

- The run that ends a `develop` step.
- The rerun after a fix to a failing test: the failed specs plus the specs the fix changed.
- A review request, which authorizes the unit and e2e tests that cover the change.
- When the user asks for a run.

Any other change triggers no run. Resetting environments or test data happens only on the user's explicit request.

## Review request

Start `unit-tester`, `e2e-tester` and `reviewer` in the same turn, one tester for each kind of test that covers the change. Withhold test results from the reviewer. When all finish, write the testers' results into the `Tests` section of `review.md` yourself, since testers never edit it.
