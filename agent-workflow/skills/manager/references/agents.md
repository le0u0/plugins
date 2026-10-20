# Agents

The manager assigns each job to one agent. An agent does the job with the skills it holds and starts no agents.

| Agent | Use |
| --- | --- |
| `planner` | default |
| `architect` | ask first: cross-feature impact, a new architectural pattern, or unclear requirements |
| `helper` | default |
| `developer` | default |
| `senior-developer` | ask first: a complicated step |
| `e2e-tester` | default |
| `reviewer` | default |
| `senior-reviewer` | ask first: a risky or far-reaching change |

Each agent's skills, `model` and `effort` are in its file under `agents/`; the README summarizes them.

Assign the default agent of each role. To use another agent, ask the user first with one line naming it and why, such as `Use senior-developer for step 3, cross-feature impact?`, and start it only after the user agrees. A user who names an agent has approved it.

`developer` and `senior-developer` run unit specs per `develop`'s `unit-tests.md`; `e2e-tester` runs e2e specs once, before review. The others run no tests.

A skill's `metadata.tier` and `effort` apply when it is called alone; inside the manager, the agent's frontmatter decides.

## Start

Start the plugin agent, such as `agent-workflow:senior-developer`; it preloads its skills. Its frontmatter sets `model` and `effort`, so pass neither. A resumed agent keeps its model and effort, so settle the choice before starting.

Other hosts start no agents, so a skill runs on the chat's own model.

## Hand-off between skills

When a skill needs a skill its agent lacks, such as `develop` needing an e2e run from `run-e2e`, return the request to the manager as `Open`. Called directly without the manager, run that skill yourself.
