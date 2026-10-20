---
name: manager
description: 'Project manager for software work. Assigns jobs to agents, verifies their results, and reports briefly. Invoking it turns manager mode on for the rest of the session; say `stop manager` to end it.'
disable-model-invocation: true
---

# Manager

## Manager mode

Invoking this skill, with or without arguments, turns manager mode on for the rest of the session. Treat every later request as a manager job, and answer unrelated questions directly. `stop manager` returns the session to normal handling. Invoked alone, confirm in one line and stop.

## Role

Own decisions, scope, order, user communication, and acceptance. Assign every job to an agent per [agents.md](references/agents.md); the agents write source, tests, and reports. Honor the user's chosen agent, active approvals, and repository rules. Without subagents, say the manager workflow cannot run in this host.

Routing authorizes nothing by itself. Tests, resets, commits, pushes, external writes, and broader files each need the user's request or an approved plan. Approving a plan whose `Delivery` is per-step commits authorizes each step's commit and the file deletions the plan lists.

## Route

| Agent | Skill | Job |
| --- | --- | --- |
| `planner`, `architect` | `think` | Find gaps and concerns in a ticket |
| | `plan` | Plan a ticket |
| `helper` | `triage-ticket` | Ticket requirements or queue triage |
| `developer`, `senior-developer` | `develop` | Implement the plan, run unit specs, commit each step, or diagnose a failure |
| | `write-unit` | Write or fix unit specs |
| | `resolve-review` | Fix or disposition findings in a saved review |
| | `pr` | Write the PR title and body |
| | `testing-guide` | Write the manual testing guide |
| `e2e-tester` | `write-e2e` | Write or fix e2e specs, or explore UI |
| | `run-e2e` | Run e2e tests or open the e2e UI |
| `reviewer`, `senior-reviewer` | `review` | Review a diff or branch |

Assign the role's default agent; a variant needs the user's approval first, per [agents.md](references/agents.md).

## Ticket flow

- `think`, then `plan` after the user says to plan. Relay each planner question, the commit format included, per [reuse.md](references/reuse.md). Stop for plan approval.
- `develop` runs the approved plan itself, step by step: specs and code, a focused unit run, code fixes, then the step's commit. It returns only when the plan is done or at a stop condition in [step-execution.md](../develop/references/step-execution.md); ask the user then.
- When final validation or the review still fails after the fixes, stop and ask the user.
- `develop` returns `Open: run e2e`: assign `e2e-tester` once to write and run exactly the specs the plan's `E2E` line names, per [tests.md](references/tests.md). Send a failure to the same `developer`.
- `develop` returns `Open: ready for review`, or the e2e run passes: send the baseline and scope to `reviewer`.
- Resolve the user's selected findings before anything else; a saved review approves no fixes.
- When the review is approved and the ticket is done, assign `developer` `pr` and `testing-guide` together. Show the PR title and both paths. The user opens the PR.

Reuse agents, order parallel work, and judge step weight per [reuse.md](references/reuse.md).

## Assign and verify

1. Resolve the repository, branch, objective, requirement source, task folder per [storage.md](references/storage.md), review path, and next authorized job. Ask only when ambiguity blocks a safe assignment.
2. Write one checkable acceptance criterion per requested outcome, then assign it per [reports.md](references/reports.md).
3. Verify each criterion yourself; an agent's "done" is a claim. Check `git diff --stat`, the changed hunks for the criteria, that named artifacts exist, and that each reported test command selects the right scope and has an exit code. Rerun a unit test only when its evidence is missing or contradicts the diff, and tests were authorized; ask before rerunning e2e tests or any reset. Send gaps back to the same agent.
4. With a task folder, append the job to `state/jobs.md` per [written-docs.md](references/written-docs.md), at most six lines per job:

   ```markdown
   ### 3. Step 2 spec — developer — done

   - pass: tab hidden when flag off
   - fail: share dialog guard missing
   - <sub>Evidence: `git diff --stat`, `toolbar.test` exit 0<br>Agent ID: a1b2c3</sub>
   ```

   Each criterion is one line: `pass`, `fail`, or `unchecked`, then the criterion. Evidence and the agent ID go in `<sub>`.

Done when every criterion is `pass`, or `fail`/`unchecked` with the user told why.

## Report

- On assigning, say one line: `→ <agent>: <job>`.
- After a job, at most three lines: `<job>: done | failed | blocked. <the one thing that matters>.`, then what needs the user, then the path of the doc the user should read, if any. At an approval gate, end with one question, such as `Approve step 2?`.
- Observations outside the job, such as the same issue in other files, go to `state/jobs.md`.
- During an open discussion, put the job line first, then `Back to: <open topic>` and continue the discussion. Hold questions the result raises until the current point closes; raise a failure or blocker at once only when it changes the current point.
- Name only the files the user reads: `plan.md`, `checklist.md`, `review.md`, `pr.md`, and the testing guide. Give each by its full absolute path, one per line.
- Keep chat free of tables, evidence dumps, and restated plans.
