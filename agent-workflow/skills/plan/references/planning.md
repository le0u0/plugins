# Requirements and Plan

## Task folder

Use a user-supplied path. Otherwise create or reuse:

```text
~/.agent-workflow/tasks/{ticket}/
  plan.md
  checklist.md
  review.md
  pr.md
  testing-guide-{short-description}.md
  attachments/        # cached ticket files, by ticket
  state/
    jobs.md
    think.md          # from think
    triage.md         # from triage-ticket
    investigation.md  # optional
    logs
```

The user reads only the files above `state/`. Everything the plugin keeps for itself goes in `state/`.

Name it after the ticket key, such as `PROJ-123`, to keep paths short. When the work spans linked tickets, use the one the user works under. Ask when no ticket is linked; a task with no tracker uses a short kebab-case description instead. Use one folder per ticket across repositories; when several exist, use the oldest. Never keep task state in a repository, including `.scratch` and `docs/superpowers`.

## Commit format

Read `~/.agent-workflow/projects/{repository}/commit-format.md`. When it is missing or empty, ask the user for the format, with an example such as `feat: xyz` or `[PROJ-123] feat: xyz`, and save the answer there as one line plus an example. Never infer it from the git log. When the user gives a different format later, update the file. Write no `Commit` line before the format is known.

## Planning

Brainstorming belongs to `think`.

Read the [project references](../../manager/references/dispatch.md) (section "Project references") and nearby code. Resolve the objective, current and expected behavior, acceptance criteria, edge and error cases, roles, permissions, test data, dependencies, exclusions, temporary contracts, design, and wording. Once expected behavior is clear, ask once for an optional screenshot.

Write `plan.md` per the [written docs](../../manager/references/dispatch.md) (section "Written docs") rules, as simple as a [review report](../../review/references/report-format.md). Latest approved scope only. Write no other doc, such as `requirements.md`; goal and acceptance criteria live in `plan.md`.

```markdown
# Plan: PROJ-123 do something

Status: draft

## Goal

Hide Export button when feature flag off.

## Acceptance criteria

- Flag off: Export button hidden in the toolbar.
- Flag on: no change.

## Steps

### 1. Gate Export button

- **Do:** Add `isExportEnabled` check in `buildActions`.
- **Test:** Spec: tab absent when flag off. Run: yes.
- **Commit:** `feat: hide export button when flag off`
- <sub>**Files:** `toolbar`, `toolbar.test`</sub>

## Decisions

- Keep Print button as is.

## Open

None.

## Reference

<sub>Requirement source: PROJ-123<br>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>Initial baseline: a1b2c3d<br>Delivery: per-step commits</sub>
```

- **Goal:** one or two lines.
- **Acceptance criteria:** observable results, one line each, key error and edge cases included.
- **Steps:** short numbered milestones. Each has `Do`, `Test`, `Commit`, and `Files` in one line each. `Commit` is the step's one-line message in the confirmed commit format, with no body. Mark any file the step deletes `delete` in `Files`; approving the plan approves those deletions, and no other file may be deleted without asking. `Test` names one behavior through a public seam, one failing test first, and whether tests may run. Put test seams, temporary contracts, access-right changes, and precedents in `Do` or `Files`, only when the developer needs them.
- **Decisions:** only choices that change scope or design, one line each. Link `investigation.md` when it drove one.
- **Open:** blocking questions only, or `None.`.
- **Reference:** `Delivery` is per-step commits by default, or uncommitted when the user says so.

A triage document becomes scope only through user approval. Ask before changing an approved plan. Drop superseded scope instead of marking it inactive.

## Optional investigation

Create `investigation.md` in `state/` only when root-cause analysis, a broad trace, or competing hypotheses would clutter `plan.md`. Gather read-only evidence yourself. Write it per the [written docs](../../manager/references/dispatch.md) (section "Written docs") rules:

```markdown
# Investigation: PROJ-123 question

## Conclusions

- Root cause: `x` skips guard when flag off.
- Affected path: `a.ts:12` to `b.ts:40`.
- Unverified: prod flag default.

## Rejected

- Cache stale: value fresh in trace.

## Evidence

- <sub>fact: `a.ts:12` reads flag once.</sub>
- <sub>inference: `b.ts:40` never reruns.</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>HEAD: a1b2c3d</sub>
```

`Conclusions` come first, at most five bullets, only what affects scope, design, risk, or validation. `Rejected` is one short reason each. Label each evidence line fact, inference, or unverified.

Investigation is evidence, not authorization. Copy its conclusions into `plan.md` `## Decisions` for approval; never keep competing scopes across both files.

## Live checklist

Create `checklist.md` beside the plan, progress first, one item per step. Mark one current item; several only when they share no files or state. Add discovered work, never delete an item without approval, and untick invalidated work with a short reason. Follow the [written docs](../../manager/references/dispatch.md) (section "Written docs") rules; `Step notes` is one line per step.

```markdown
# PROJ-123 checklist

## Implementation

- [x] Step 1: clamp remaining count
- [ ] Step 2: hide empty list - current

## Step notes

- Step 1: Spec failed, then passed after clamp.

## Task files

<sub>Modified: `src/example.test`</sub>

## Evidence

<sub>Unit: expected failure, then pass; command and checkout recorded here.</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>Initial baseline: a1b2c3d<br>Current HEAD: a1b2c3d<br>Current step: 2 of 2<br>Next action: approve Step 2</sub>
```

Update it after each step and before handoff, including finding IDs and dispositions. List unrelated existing changes separately. On resume, check drift per gate 3 of the [start gate](../../develop/references/step-execution.md) (section "Start gate").
