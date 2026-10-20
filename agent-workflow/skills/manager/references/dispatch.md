# Dispatch

## Agents

The manager assigns each job to one agent. An agent does the job itself with the skills it holds and starts no agents.

| Agent | Skills |
| --- | --- |
| `planner` | `think`, `plan` |
| `helper` | `triage-ticket` |
| `developer` | `develop`, `write-unit`, `write-e2e`, `resolve-review` |
| `unit-tester` | `run-unit` |
| `e2e-tester` | `run-e2e` |
| `reviewer` | `review` |

Start the plugin agent, such as `agent-workflow:developer`; it preloads its skills.

When a skill sends work to a skill this agent lacks, such as `develop` sending a test run to `run-unit`, return it to the manager as `Open`. Invoked directly without the manager, follow that skill yourself.

## Model and effort

Tiers: light is `haiku`, standard is `sonnet`, advanced is `opus`. Every agent start passes `model` and `effort` in the start call (the Agent tool's parameters). Agent frontmatter sets neither, so an unset start inherits the manager's model and effort and spends its quota.

| Agent | Default `model` | Default `effort` | Manager may start |
| --- | --- | --- | --- |
| `planner` | `opus` | high | |
| `helper` | `haiku` | low | |
| `unit-tester` | `haiku` | low | |
| `e2e-tester` | `haiku` | low | |
| `developer` | `sonnet` | medium | `opus`, medium, for a complicated step |
| `reviewer` | `opus` | medium | `sonnet`, medium, for a simple change; `opus`, high, when the user asks |

A resumed agent keeps its model and effort. Use the family alias (`haiku`, `sonnet`, `opus`), which resolves to the newest available model. Other hosts start no agents and use the chat's own model.

## Task folder

Task docs live in `~/.agent-workflow/tasks/{ticket}-{description}/`; see [planning.md](../../plan/references/planning.md) (section "Task folder") for its contents. Find it by globbing `~/.agent-workflow/tasks/{ticket}*`, with the ticket key from the user's message or the branch name. Several matches: use the oldest. None: ask; never assume there is no folder. Never write task docs to a scratchpad or temp directory.

## Written docs

Applies to every markdown file an agent writes, such as `plan.md`, `think.md`, `triage.md`, `investigation.md`, `checklist.md`, `jobs.md`, `review.md`, or any other the agent decides to create. Create an extra doc only when no named doc fits.

- Every point is one line, at most 15 words. No paragraphs; split or cut instead.
- Fragments. Drop articles, filler, hedging, and restated context: "Export button shows when flag off. Hide it." not "The Export button is currently displayed even though the preference is disabled, so it should be hidden."
- Code, identifiers, paths, and error strings stay exact.
- No history, dates, other findings, or how a decision was reached.
- Detail only the next reader needs to act goes in the point; reference detail goes in `<sub>`.

## Handoff

Send paths, never file contents: the resolved task folder, plan step number, files, review path. Send only the current step, not the whole plan. State the job, acceptance criteria, test authorization, and commit restrictions. The agent has none of the conversation.

## Report

An agent ends with at most eight lines:

```text
Status: done | failed | blocked
Changed: <files, or none>
Commands: <command → exit code, or none>
Artifacts: <paths, or none>
Open: <what remains or needs the user, or none>
```

No narrative, no restated plan, no code excerpts.

## Test report

`unit-tester` and `e2e-tester` end with this report instead of the one above, at most eight lines:

```text
Status: done | failed | blocked
Result: <counts>; failed: <spec file and test name each, or none>
Commands: <command → real exit code>
Changed: <files, or none>
Artifacts: <failure log path, or none>
Open: <or none>
```

- **done:** `Result` has the counts (such as `12 specs, 0 failed`) and `Commands` has exit 0. No log, no output.
- **failed:** list each failed spec file and test name in `Result`. `Artifacts` is a log holding only the failed tests' output (name, error, top stack lines), saved in the task folder, else the system temp directory. Never send the full output. Name no cause.
- **blocked:** `Open` has the reason and what the manager or user should do, such as `approve a full-suite run` or `start the backend at BASE_URL`. No log.

On a rerun after a fix, run only the previously failed specs plus the specs the fix changed. Run the wider scope only when the manager asks.

## Project references

This plugin holds no framework or domain rules. The project being changed owns them. Before any code or test work, find and read what applies:

- `AGENTS.md`, `CLAUDE.md`, and rule files in `.agents/rules/` or `.claude/rules/`. When the plan step lists the relevant rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`. Match the job against each skill's name and description, such as a `create-*` or `testing-*` skill, then read and follow the matching ones. Project skills win over this plugin's defaults where they conflict.
- The nearest comparable feature or spec. Search the checkout for a pattern by folder, file, or class name.

When nothing applies, say so and follow the nearest comparable code. Never copy project rules into this plugin's files or the task docs; link to them.

## Authorization

Routing never authorizes tests, resets, commits, pushes, external writes, or broader files.
