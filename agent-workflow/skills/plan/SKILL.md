---
name: plan
description: 'Plan one ticket into plan.md and checklist.md for user approval, with no code changes. Use for "plan PROJ-123" or "break this into steps".'
effort: high
metadata:
  tier: advanced
---

# Plan

Report per [reports.md](../manager/references/reports.md).

- Take requirements only from supplied or explicitly retrieved context. Store a supplied ticket link; the key alone says nothing about requirements.
- For a ticket URL or explicit lookup, run `triage-ticket` first. Its brief is context, not approved scope.
- Read `think.md` in the task folder's `state/` when present. Its decisions are inputs; its open questions need an answer or the user's acceptance as assumptions.
- Write plan docs only: create `plan.md` and `checklist.md` when missing, update them in place when they exist. Follow the repository's `AGENTS.md`, `CLAUDE.md`, and project-local skills.

1. Settle the commit format. Read `~/.agent-workflow/projects/{repository}/commit-format.md`. When it is missing or empty, return the question to the manager as `Open`, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`, and save the user's answer there as one line plus an example. Update the file when the user gives a different format later. Write each `Commit` line after the format is known.
2. Read [plan-format.md](references/plan-format.md). Create or reuse the task folder per [storage.md](../manager/references/storage.md), clarify requirements, and write `plan.md`, then `checklist.md` per [checklist-format.md](references/checklist-format.md). For a bug ticket whose diagnosis would clutter the plan, add `diagnose.md` per [diagnose-format.md](../develop/references/diagnose-format.md).
3. Check the unit and e2e test setup per [test-setup.md](../manager/references/test-setup.md), and write `none: no setup` in a `Test` or `E2E` line when the project has no setup for it.
4. Make each step concrete enough for `develop` to run without new design decisions: affected files, public test seams, test authoring and run authorization, the one-line commit message, and delivery mode.
5. Return the plan and checklist for approval, and stop.

Done when every acceptance criterion maps to a step with a failing test named (or `none: no setup`), every step has a `Commit` line, and `Open` is `None.` or lists the blocking questions.
