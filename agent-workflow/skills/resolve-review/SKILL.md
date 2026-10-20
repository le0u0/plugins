---
name: resolve-review
description: 'Fix selected findings from a saved review.md, record numbered dispositions, or set its status to approved. Use for "fix review findings 1 and 3", "approve the review", or when manager assigns it.'
effort: medium
metadata:
  tier: standard
---

# Resolve Review

Follow [dispatch](../manager/references/dispatch.md).

1. Resolve the review path, or the one matching task folder under `~/.agent-workflow/tasks/`. Ask when ambiguous. Read `review.md` and the user's dispositions.
2. For "set review status to approved", update or insert only `Status: approved` below the review title, then check the diff. No new review, source edits, or tests; findings stay as they are. Stop here. Otherwise continue at step 3.
3. Read `plan.md`, `checklist.md`, the [project references](../manager/references/dispatch.md) (section "Project references"), and the checkout. Compare repository, branch, and reviewed SHAs. Reverify each selected finding against current code; ask when drift makes it ambiguous.
4. Keep finding IDs. Record each disposition: accepted, deferred, disputed, or ignored. When a finding is already fixed or unsupported, explain with evidence.
5. Fix each accepted finding yourself: production code per `develop`, unit specs per `write-unit`. Return e2e spec findings to the manager as `Open`, for `e2e-tester` to fix per `write-e2e`, with the finding ID, scope, files, test authorization, and commit restrictions. Run authorized unit specs per `run-unit`; send authorized e2e runs to `run-e2e`. Leave changes uncommitted unless the user approves the work and an exact commit message.
6. Check the diff against the selected findings. Update `review.md` and the checklist: add `Done` and `Status`, and place each finding in its section, per [report-format.md](../review/references/report-format.md). Keep the original reviewed range. A fix is not a new review.

Finish when each selected finding has an evidenced outcome. Report resolved and open IDs, validation limits, and the artifact path. Use `review` for a re-review. Send no external review reply unless asked.
