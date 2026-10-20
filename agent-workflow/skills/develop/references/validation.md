# Final Validation

1. Compare delivered behavior and the full task diff, including untracked files, with `plan.md`.
2. Return `Open:` for the authorized unit and e2e checks; the manager has `unit-tester` run them per `run-unit` and `e2e-tester` per `run-e2e`. Record each command, outcome, and missing evidence in `checklist.md`, keeping environment failures apart from implementation failures.
3. Report `Open: ready for review` with the initial baseline and the plan's test authorization. The manager sends the full approved scope to the task's `reviewer`, which saves `review.md` in the task folder.
4. Report review findings apart from test results. Failed required checks or open requirements block a verified-complete claim; excluded checks are limits, never passes.
5. Add discovered work to `checklist.md`; ask before expanding scope.

Finish with delivered behavior, review outcome, validation limits, uncommitted files or commit SHAs, and the review path.
