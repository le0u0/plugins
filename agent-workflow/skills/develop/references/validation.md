# Final Validation

1. Compare delivered behavior and the full task diff, including untracked files, with `plan.md`.
2. Run the focused unit specs for the whole change per [unit-tests.md](unit-tests.md) when authorized. Record each command, outcome, and missing evidence in `checklist.md`, keeping environment failures apart from implementation failures.
3. Report `Open: run e2e` when the plan's `E2E` line is not `none`, else `Open: ready for review`. Include the initial baseline and the plan's test authorization. The manager runs `e2e-tester` and sends the full approved scope to the task's `reviewer`, which saves `review.md` in the task folder.
4. Report review findings apart from test results. Failed required checks or open requirements block a verified-complete claim; excluded checks are limits, never passes.
5. Add discovered work to `checklist.md`; ask before expanding scope.
6. When a required check or the review still fails after the fixes, stop and report it. Ask the user how to proceed; never loop.

Finish with delivered behavior, review outcome, validation limits, uncommitted files or commit SHAs, and the review path.
