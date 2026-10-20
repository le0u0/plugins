---
name: plan
description: 'Plan one ticket into plan.md and checklist.md for user approval, with no code changes. Use for "plan PROJ-123", "break this into steps", or when manager assigns it.'
effort: high
metadata:
  tier: advanced
---

# Plan

Follow [dispatch](../manager/references/dispatch.md).

- Requirements come only from supplied or explicitly retrieved context. Store a supplied ticket link; never infer requirements from its key.
- For a ticket URL or explicit lookup, run `triage-ticket` first. Its brief is context, not approved scope.
- Read `think.md` in the task folder's `state/` when present. Its decisions are inputs; its open questions need an answer or the user's acceptance as assumptions.
- Change no production code or tests. Follow the repository's `AGENTS.md`, `CLAUDE.md`, and project-local skills.

1. Read [planning.md](references/planning.md). Settle the commit format first, per its section "Commit format". Create or reuse the task folder, clarify requirements, and write `plan.md` and `checklist.md`. Add `investigation.md` only when diagnosis would clutter the plan.
2. Make each step concrete enough for `develop` to run without new design decisions: affected files, public test seams, test authoring and run authorization, the one-line commit message, and delivery mode.
3. Return the plan and checklist for approval, and stop.
