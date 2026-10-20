# agent-workflow

A manager that plans, builds, tests and reviews a ticket with specialist agents. It works in any project: the process lives here, the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

```text
/plugin install agent-workflow@le0u0-plugins
```

## Use

```text
/agent-workflow:manager on
```

Describe the work. The manager assigns each job to an agent, checks the result, and reports in a few lines. Say `stop manager` to end it. Every skill also works on its own.

## Agents

| Agent | Skills | Model |
| --- | --- | --- |
| `planner`, `architect` | `think`, `plan` | opus medium, opus high |
| `developer`, `senior-developer` | `develop`, `write-unit`, `resolve-review`, `pr`, `testing-guide` | sonnet medium, opus medium |
| `reviewer`, `senior-reviewer` | `review` | opus medium, opus high |
| `e2e-tester` | `write-e2e`, `run-e2e` | sonnet medium |
| `helper` | `triage-ticket` | haiku low |

The manager uses `planner`, `developer`, `reviewer` and `helper` by default, and asks you before using another.

Task docs are saved in `~/.agent-workflow/tasks/`. More in [architecture](docs/architecture/ARCHITECTURE.md).
