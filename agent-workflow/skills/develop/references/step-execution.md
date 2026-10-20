# Execute One Step

## Start gate

1. The branch must contain the ticket key, such as `PROJ-123`, unless the user approved an exception or the project has no ticket convention. Otherwise warn and stop.
2. The step must be in approved scope. Stop when unrelated work overlaps it; ask when the plan is unclear.
3. Compare the saved repository, branch, baseline, HEAD, and task diff in `checklist.md` with the checkout. Invalidate stale evidence, never discard changes to match saved state, and ask only when drift makes scope ambiguous. In per-step commit mode, recorded commits must remain ancestors of `HEAD`.

## Step gate

Run workflow step 3 of `SKILL.md` for the whole step: specs written to fail, code, passing specs. The test runs are tester jobs the manager assigns. Then stop at one approval gate and show the specs, the diff, and the passing output. When assigned by the manager, return to it and end.

Plan approval never approves a step. Skip the gate only when the user pre-approved it, such as "all steps are approved". After approval, mark the step done in `checklist.md` and start the next.

When test runs are excluded, skip them and say so at the gate. A failing run never expands scope to bootstrap, configuration, or unrelated specs.

When a dependency such as a backend contract is unavailable, get approval for a feature-local temporary contract, leave generated code unchanged, and add one ticket-linked `FIXME` with its removal condition.

## Formatting and handoff

Format each changed file with the project's file-scoped command. When the staged-file workflow would change the index in leave-uncommitted mode, use a file-scoped equivalent or report formatting as pending. Preserve unrelated changes and the user's staging.

Record changed files, evidence, and next action in `checklist.md`. At the gate, print its `## Implementation` section with the current item marked.

## Optional commit gate

Only when commits are requested. After the work and authorized checks, show the scope and exact message, the project's commit format, else `[TICKET] <type>: <description>`, and get approval unless already given for this diff. Stage only approved files or hunks; stop if unrelated staged changes would enter. Present again if staged-file checks change the diff materially. Record the SHA. Never push.
