# Agent Handling

## Parallel work

Split cross-agent requests into jobs ordered by their inputs. Parallelize only read-only work or edits to disjoint files.

## Think relay

`planner` returns one numbered batch of questions. Show it unchanged. Send the user's answers to the same agent. Repeat until the user says to plan, then ask that agent to plan.

## Reuse

Agents stay alive for the ticket. Record each agent's ID and tier from its start result in `state/jobs.md`, and send all later work to the same ID with SendMessage, so it keeps its context. Resume the same agent for:

- `planner`: think, then plan, then the user's answers.
- `developer`: every later plan step of the same tier, follow-ups, gaps you found, review fixes. A failure goes to the developer that did the step.
- `e2e-tester`: writing and rerunning e2e specs.
- `unit-tester`: rerunning the failed and changed specs after a change.
- `reviewer`: re-review of the same branch, which updates `review.md` in place.

Start a fresh agent only when no agent of that type and tier exists on this ticket, never one per plan step. A resumed agent cannot change its model or effort, so pass them correctly at the start, per [agents.md](agents.md).

Judge each step. A complicated step, such as cross-feature impact, a new architectural pattern, or unclear requirements, goes to an advanced `developer` (`opus`, medium); start one the first time and resume it for later complicated steps. A simple change may go to a standard `reviewer` (`sonnet`, medium). Start an advanced-high reviewer only when the user asks. A ticket can hold a standard and an advanced developer at once; send each step to the one matching its weight.

When SendMessage to a recorded ID fails, start a fresh agent and point it at the plan, `checklist.md`, and `state/jobs.md`.
