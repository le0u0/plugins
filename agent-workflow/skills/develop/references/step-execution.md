# Execute One Step

## Start gate

1. The branch must contain the ticket key, such as `PROJ-123`, unless the user approved an exception or the project has no ticket convention. Otherwise warn and stop.
2. The step must be in approved scope. Stop when unrelated work overlaps it; ask when the plan is unclear.
3. Compare the saved repository, branch, baseline, HEAD, and task diff in `checklist.md` with the checkout. Invalidate stale evidence, never discard changes to match saved state, and ask only when drift makes scope ambiguous. In per-step commit mode, recorded commits must remain ancestors of `HEAD`.

## Step gate

Run workflow step 3 of `SKILL.md` for the whole step: specs written to fail, code, passing specs. The test runs are tester jobs the manager assigns.

With `Delivery` per-step commits, approving the plan approves every step, its commit, and the file deletions the plan lists. Mark the step done in `checklist.md`, commit per the commit gate, and start the next step without asking. Stop and ask the user only when:

- the same spec still fails after two fixes;
- a step needs a change outside the plan, or a file deletion the plan does not list;
- the plan is unclear.

Never loop on a failure: report it and discuss.

With `Delivery` uncommitted, stop at one approval gate per step and show the specs, the diff, and the passing output. Plan approval never approves a step then, unless the user pre-approved it, such as "all steps are approved".

When test runs are excluded, skip them and say so at the gate. A failing run never expands scope to bootstrap, configuration, or unrelated specs.

When a dependency such as a backend contract is unavailable, get approval for a feature-local temporary contract, leave generated code unchanged, and add one ticket-linked `FIXME` with its removal condition.

## Formatting and handoff

Format each changed file with the project's file-scoped command. When the staged-file workflow would change the index in leave-uncommitted mode, use a file-scoped equivalent or report formatting as pending. Preserve unrelated changes and the user's staging.

Record changed files, evidence, and next action in `checklist.md`. At the gate, print its `## Implementation` section with the current item marked.

## Commit gate

Applies when `Delivery` is per-step commits, or the user asks. Commit each finished step with its plan `Commit` message, exactly, as one line with no body or trailer. No other approval is needed. When the step's scope changed, propose a new one-line message and get approval first. Without a plan message, use the project's commit format, else `<type>: <description>`. Stage only the step's files or hunks; stop if unrelated staged changes would enter. Record the SHA. Never push.
