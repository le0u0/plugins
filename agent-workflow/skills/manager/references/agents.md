# Agents

The manager assigns each job to one agent. An agent does the job with the skills it holds and starts no agents.

| Agent | Skills | Runs tests | `model` | `effort` | Manager may start |
| --- | --- | --- | --- | --- | --- |
| `planner` | `think`, `plan` | none | `opus` | high | |
| `helper` | `triage-ticket`, `research` | none | `haiku` | low | `sonnet`, medium, for a research job |
| `developer` | `develop`, `write-unit`, `resolve-review`, `pr`, `testing-guide` | unit specs, per `develop`'s `unit-tests.md` | `sonnet` | medium | `opus`, medium, for a complicated step |
| `e2e-tester` | `write-e2e`, `run-e2e` | e2e specs, once, before review | `sonnet` | medium | |
| `reviewer` | `review` | none | `opus` | medium | `sonnet`, medium, for a simple change; `opus`, high, when the user asks |

Tiers: light is `haiku`, standard is `sonnet`, advanced is `opus`. Each skill's `metadata.tier` and `effort` match its agent's default, except `run-e2e`, which is light when called alone.

## Start

Start the plugin agent, such as `agent-workflow:developer`; it preloads its skills. Pass `model` and `effort` in the Agent tool call on every start, because agent frontmatter sets neither and an unset start inherits the manager's. Use the family alias, which resolves to the newest model. A resumed agent keeps its model and effort.

Other hosts start no agents, so a skill runs on the chat's own model.

## Hand-off between skills

When a skill needs a skill its agent lacks, such as `develop` needing an e2e run from `run-e2e`, return the request to the manager as `Open`. Called directly without the manager, run that skill yourself.
