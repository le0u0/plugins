# Agent Workflow

Shared terms for this plugin.

## Roles

| Term | Meaning |
| --- | --- |
| Manager | `manager`, the main thread. Assigns each job to an agent, verifies the result itself, and decides the next step. Never does agent work. |
| Agent | `planner`, `helper`, `developer`, `unit-tester`, `e2e-tester`, or `reviewer`. Holds several skills and does each job itself. Only agents carry role names. |
| Skill | An action, such as `write-unit`. Called directly or used by an agent. |
| Tier | A skill's `metadata.tier` (light, standard or advanced), mapped to haiku, sonnet and opus. Each agent has a default tier and effort; the table is in `agents.md`. |

## Skill structure

| Term | Meaning |
| --- | --- |
| Reference | A file in a skill's `references/`, read only for one branch of its workflow, linked directly from `SKILL.md`. |
| Project references | Rules, project-local skills, and comparable code in the repository being changed. Every skill reads them; none copies them. |
| Project-local skill | A skill inside the repository, such as in `.agents/skills/` or `.claude/skills/`. Followed over this plugin's defaults where they conflict. |

## Tickets and tasks

| Term | Meaning |
| --- | --- |
| Ticket | A task ID such as `PROJ-123`. Requirements come from supplied or retrieved context, never the key alone. |
| Task folder | `~/.agent-workflow/tasks/{ticket}/`, with `plan.md`, `checklist.md`, `review.md`, `pr.md`, and a testing guide. Plugin files live in its `state/` subfolder. |
| Step | A reviewable milestone in an approved plan. Work stays uncommitted unless the user approves a commit. |
| Test-driven slice | One behavior: one failing test through a public seam, then the minimum code to pass it. |
| Temporary contract | A feature-local stand-in used until a real dependency exists, with a ticket-linked `FIXME` and removal condition. |

## Code

| Term | Meaning |
| --- | --- |
| Test selector contract | A stable selector defined by `write-e2e` and implemented in production by `develop`. |

## Review

| Term | Meaning |
| --- | --- |
| Self-check | A skill checking its own work before finishing. Not a review. |
| Formal review | `review`'s single pass of the project's review skill (else standards and requirements) and review checks. |
| Review baseline | Where the review starts: a user-supplied baseline, else the saved `Reviewed to` SHA, else the parent branch. Never assumed to be the default branch. |
