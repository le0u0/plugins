# Agent Workflow

Project-agnostic workflow for ticket-driven development in Claude Code. The plugin holds the process only: manager, agents, and skills. Framework and domain rules come from the project being changed: `AGENTS.md`, `CLAUDE.md`, rule files, and project-local skills in `.claude/skills/` or `.agents/skills/`.

## Install

```text
/plugin marketplace add le0u0/plugins
/plugin install agent-workflow@le0u0-plugins
```

For ticket triage, connect your tracker's MCP (such as Atlassian for Jira) in your agent. `triage-ticket` uses it to read tickets and download attachments.

## Agents and skills

Start with `/agent-workflow:manager`. It assigns each job to an agent, verifies the result, and reports in one line. Add `on` to keep manager mode for the session, `off` to stop. Every skill is also callable directly.

| Agent | Skills |
| --- | --- |
| `planner` | `think`, `plan` |
| `helper` | `triage-ticket` |
| `developer` | `develop`, `write-unit`, `write-e2e`, `resolve-review` |
| `unit-tester` | `run-unit` |
| `e2e-tester` | `run-e2e` |
| `reviewer` | `review` |

| Skill | Description |
| --- | --- |
| `manager` | Assign jobs, verify results, report briefly. |
| `think` | Find gaps and concerns in a ticket with you, before planning. |
| `triage-ticket` | Read ticket requirements, comments, and images. |
| `plan` | Write `plan.md` and `checklist.md` for approval. |
| `develop` | Implement a plan step or production change, test-first. |
| `write-unit` | Write unit specs for changed code. |
| `run-unit` | Run unit tests and report failures. |
| `resolve-review` | Apply selected findings or approval status. |
| `write-e2e` | Write end-to-end specs and test data. |
| `run-e2e` | Run end-to-end tests or open the runner UI. |
| `review` | Review a diff and save `review.md`. |

Task docs live in `~/.agent-workflow/tasks/{ticket}-{description}/`.

See [architecture](docs/architecture/ARCHITECTURE.md) and [models](docs/architecture/models.md).
