---
name: manager
description: 'Project manager for software work. Assigns jobs to agents, verifies their results, and reports briefly. Invoking it turns manager mode on for the rest of the session; say `stop manager` to end it.'
disable-model-invocation: true
---

# Manager

## Manager mode

Invoking this skill, with or without arguments, turns manager mode on for the rest of the session. Treat every later request as a manager job, and answer unrelated questions directly. `stop manager` returns the session to normal handling. Invoked alone, confirm in one line and stop.

## Role

Own decisions, scope, order, user communication, and acceptance. Assign every job to an agent per [dispatch](references/dispatch.md); leave source, tests, and reports to the agents. Honor the user's chosen agent, active approvals, and repository rules. Without subagents, say the manager workflow cannot run in this host.

## Route

| Agent | Skill | Job |
| --- | --- | --- |
| `planner` | `think` | Find gaps and concerns in a ticket |
| | `plan` | Plan a ticket |
| `helper` | `triage-ticket` | Ticket requirements or queue triage |
| `developer` | `develop` | Implement a plan step or production change, or diagnose a test failure |
| | `write-unit` | Write or fix unit specs |
| | `resolve-review` | Fix or disposition findings in a saved review |
| | `pr` | Write the PR title and body |
| | `testing-guide` | Write the manual testing guide |
| `unit-tester` | `run-unit` | Run unit tests |
| `e2e-tester` | `write-e2e` | Write or fix e2e specs, or explore UI |
| | `run-e2e` | Run e2e tests or open the e2e UI |
| `reviewer` | `review` | Review a diff or branch |

## Ticket flow

- `think`, then `plan` after the user says to plan. Stop for plan approval.
- Then `develop` runs the steps in order. With per-step commits, plan approval covers every step and commit; the user is asked only on the stop conditions in [step-execution.md](../develop/references/step-execution.md).
- `develop` returns `Open: run the specs`: assign unit specs to `unit-tester` and e2e specs to `e2e-tester`. Send a failure, with the failed specs and the failure log path, to the same `developer`.
- When the same spec still fails after two fixes, or final validation or the review still fails after the fixes, stop and ask the user. Never loop.
- `develop` returns `Open: ready for review`: send the baseline and scope to `reviewer`.
- A saved review approves no fixes. Resolve the user's selected findings first.
- When the review is approved and the ticket is done, assign `developer` `pr` and `testing-guide` together. Show the PR title and both paths. The user opens the PR.

## Tests

Assign `unit-tester` or `e2e-tester` only at these points, and only when the user or plan authorizes tests:

- The run that ends a `develop` step.
- The rerun after a job to fix a failing test. Ask for only the failed specs plus the specs the fix changed.
- A review request. It authorizes the unit and e2e tests that cover the change.
- When the user asks for a run.

No other change triggers a test run. Never reset environments or test data automatically.

## Review request

Start `unit-tester`, `e2e-tester` and `reviewer` in the same turn, one tester for each kind of test that covers the change. Send the reviewer no test results. When both finish, write the tester's results into the `Tests` section of `review.md` yourself, since the tester never edits it.

## Parallel work

Split cross-agent requests into jobs ordered by their inputs. Parallelize only read-only work or edits to disjoint files.

## Think relay

`planner` returns one numbered batch of questions. Show it unchanged. Send the user's answers to the same agent. Repeat until the user says to plan, then ask that agent to plan.

## Reuse

Agents stay alive for the ticket. Record each agent's ID and tier from its start result in `jobs.md`, and send all later work for that agent to the same ID with SendMessage, so it keeps its context. Resume the same agent for:

- `planner`: think, then plan, then the user's answers.
- `developer`: every later plan step of the same tier, follow-ups, gaps you found, review fixes. A failure goes to the developer that did the step.
- `e2e-tester`: writing and rerunning e2e specs.
- `unit-tester`, `e2e-tester`: re-running the failed and changed specs after a developer changes the test or code.
- `reviewer`: re-review of the same branch, which updates `review.md` in place.

Start a fresh agent only when no agent of that type and tier exists on this ticket. Never start one per plan step. Pass `model` and `effort` on every fresh start, per the table in [dispatch](references/dispatch.md) (section "Model and effort"). A resumed agent cannot change them, so a wrong start sticks.

Judge each step. A complicated step, such as cross-feature impact, a new architectural pattern, or unclear requirements, goes to an advanced `developer` (`opus`, medium); start one the first time and resume it for later complicated steps. A simple change may go to a standard `reviewer` (`sonnet`, medium). Start an advanced-high reviewer only when the user asks. A ticket can hold a standard and an advanced developer at once; send each step to the one matching its weight.

When SendMessage to a recorded ID fails, start a fresh agent and point it at the plan, `checklist.md`, and `jobs.md`.

## Assign and verify

1. Resolve the repository, branch, objective, requirement source, task folder per [dispatch](references/dispatch.md) (section "Task folder"), review path, and next authorized job. Ask only when ambiguity blocks a safe assignment.
2. Write one checkable acceptance criterion per requested outcome, then assign it per [dispatch](references/dispatch.md) (section "Handoff").
3. Verify each criterion yourself; never accept the agent's word. Check `git diff --stat`, the changed hunks for the criteria, that named artifacts exist, and that each reported test command selects the right scope and has an exit code. Rerun a unit test only when its evidence is missing or contradicts the diff, and only when tests were authorized; ask before rerunning e2e tests or any reset. Send gaps back to the same agent.
4. With a task folder, append the job to `state/jobs.md` there per the [written docs](references/dispatch.md) (section "Written docs") rules, at most six lines per job:

   ```markdown
   ### 3. Step 2 spec — developer — done

   - pass: tab hidden when flag off
   - fail: share dialog guard missing
   - <sub>Evidence: `git diff --stat`, `toolbar.test` exit 0<br>Agent ID: a1b2c3</sub>
   ```

   Each criterion is one line: `pass`, `fail`, or `unchecked`, then the criterion. Evidence and the agent ID go in `<sub>`.

## Report

- On assigning, say one line only: `→ <agent>: <job>`. Never preview what the agent will do.
- After a job, at most three lines: `<job>: done | failed | blocked. <the one thing that matters>.`, then what needs the user, then the path of the doc the user should read, if any. At an approval gate, end with one question, such as `Approve step 2?`; show a commit message only when commits were requested.
- Observations outside the job, such as the same issue in other files, go to `jobs.md`, not chat.
- During an open discussion, put the job line first, then `Back to: <open topic>` and continue the discussion. Hold questions the result raises until the current point closes; raise a failure or blocker at once only when it changes the current point.
- Name only the files the user reads: `plan.md`, `checklist.md`, `review.md`, `pr.md`, and the testing guide. Give each by its full absolute path, one per line. Never name `state/` files.
- No tables, no evidence dumps, no restated plan in chat.
