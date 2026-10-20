---
name: review
description: 'Review a branch, diff or work-in-progress change against the project''s standards and the supplied objective or bug, and save review.md. Use for "review my branch", "review this diff", or when manager assigns it.'
effort: medium
metadata:
  tier: advanced
---

# Review

Follow [dispatch](../manager/references/dispatch.md).

## 1. Inputs

- **Requirements:** what the user supplied (text, a file, a ticket URL, or a matching `plan.md`). Never infer them from a ticket key or branch. With none, or when the ticket is unreachable, record `Requirement: none` and still apply the **Correctness** check in [checks.md](references/checks.md).
- **Report path:** the user's path; else the task folder's `review.md` per [task folder](../manager/references/dispatch.md) (section "Task folder"); else `~/.agent-workflow/reviews/{repository}/{branch}/review.md`. Ask only when several match.
- **Baseline:** [scope-baseline.md](references/scope-baseline.md).

## 2. Re-review

When `review.md` exists for this repository and branch, update it in place:

- Recheck each `TODO`. Fixed: move it to `RESOLVED` with `Status: fixed (<short SHA>)`. Still present: update its lines.
- Look for new findings only in changes after `Reviewed to`, numbered after the last one.
- Update `Issue Count` and `Reviewed to`; leave `Tests` to the manager.

## 3. Review pass

Review the code only; the manager runs the tests in parallel and writes their results into `Tests`. Run no tests yourself and record `Tests` as not run on a first pass. On a re-review, read the tester results the manager wrote in `review.md`; for each reported failure, check by reading code that the developer's fix addresses it. Only the testers rerun the tests.

Do the review pass:

- Read the scoped diff once, then changed functions and immediate callers as needed. Cover every changed hunk.
- When the repository has its own review skill, such as a review skill in `.claude/skills/` or `.agents/skills/`, use its method only, not its scope, delivery, or format. Otherwise use [review-method.md](references/review-method.md). Always apply the relevant [checks.md](references/checks.md), and the project's own rules from the [project references](../manager/references/dispatch.md) (section "Project references").
- Check that changed code follows guidance in the comments of the modified files.
- For a risky hunk, such as a changed condition or a removed guard, run `git log -L` or `git blame` on it and flag a change that undoes earlier intent. Skip this for other hunks.

On a re-review, a reported test failure in `Tests` that the fix does not address is a finding.

## 4. Filter

- Keep only findings introduced or exposed by the change, on lines the change touched.
- Keep a finding only when you confirmed it is real and will be hit in practice; a guess sends the developer after a false lead.
- Omit changes that look intentional, issues silenced by a lint-ignore comment, unreachable cases, style preferences, pure renames that keep behavior, and issues tooling enforces. A missing contract limits one finding, never the review.
- Deduplicate by root cause.
- Keep source read-only; add no `TODO` or `FIXME` comments to code.

## 5. Save and reply

- Pick the files worth a human read for `Manual review`, per [report-format.md](references/report-format.md).
- Write `review.md` in that format directly at the report path.
- Reply with the issue count, one line per open finding (severity, file and line, issue, fix), resolved numbers, and the `review.md` link. Say "No actionable findings" only after reading every hunk.
- Suggest no follow-up skill.
