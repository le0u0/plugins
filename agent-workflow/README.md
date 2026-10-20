# agent-workflow

A manager that plans, builds, tests and reviews a ticket with specialist agents. It works in any project: the process lives here, the rules come from your repo (`AGENTS.md`, `CLAUDE.md`, project skills).

```text
/plugin install agent-workflow@le0u0-plugins
```

## Use

```text
/agent-workflow:manager on
```

Describe the work. The manager assigns each job to an agent, checks the result, and reports in a few lines. `off` stops it. Every skill also works on its own.

## Agents

| Agent | Skills |
| --- | --- |
| `planner` | `think`, `plan` |
| `developer` | `develop`, `write-unit`, `write-e2e`, `resolve-review` |
| `reviewer` | `review` |
| `unit-tester` | `run-unit` |
| `e2e-tester` | `run-e2e` |
| `helper` | `triage-ticket` |

Task docs are saved in `~/.agent-workflow/tasks/`. More in [architecture](docs/architecture/ARCHITECTURE.md).
