# Saved Review

Follow the [written docs](../../manager/references/dispatch.md) (section "Written docs") rules. Issue and Fix are the main points, one line each.

```markdown
# Code review

Status: reviewed

## Issue Count

TODO: 1 · <sub>RESOLVED: 1 · IGNORED: 0</sub>
Total: 2 (Critical: 0, Warning: 2, Minor: 0)

## TODO

### 1. Warning — ProfileFormComponent

- **Issue:** Failed update leaves Save disabled. No retry.
- **Fix:** Clear pending state on error.
- <sub>**Files:** `profile-form.ts:123`</sub>

## RESOLVED

### 2. Warning — SidebarComponent

- **Issue:** Host test ID overwrites the parent's. Setting-tab selectors break.
- **Fix:** Remove host binding. Locate sidebar by its own ID.
- <sub>**Files:** `sidebar:24`, `settings.test:251`</sub>
- **Done:** Removed host binding; e2e uses the sidebar ID; dropped its unit cases.
- **Status:** fixed, not tested

## IGNORED

None.

## Manual review

1. `export-util.ts:120`
   -> Clears items on overflow. Reject path.
2. `layout.ts:1149`
   -> Reject save keeps old items.

## Tests

<sub>Unit: 2 specs passed<br>E2E: not run</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-example<br>Reviewed from: a1b2c3d<br>Reviewed to: e4f5g6h<br>Requirement: plan.md<br>Diff fingerprint: hash when work is uncommitted</sub>
```

## Fields

- **Heading:** number, severity, and the owning class or file.
- **Issue:** trigger and impact, one line.
- **Fix:** the corrective action, one line; one alternative at most.
- **Files:** file name and line, wrapped in `<sub>` so the reader's eye skips it. Add the shortest distinguishing folder only when two files share a name.
- **Done:** added by `resolve-review`. The final change only.
- **Status:** added by `resolve-review`, or alone when a re-review finds an author's fix. Such as `fixed (e4f5g6h)`, `fixed, tested`, `fixed, not tested`, `deferred`, `disputed`, or `ignored by user`.

- **Manual review:** files worth a human read, so the user can skip the rest of a large diff. Pick by risk, not size: logic, state, data flow, permissions. Skip renames, templates, styles, generated code, and specs. At most seven, riskiest first. Each is `file:line`, then `-> ` and a remark of at most 10 words saying what to check. `None.` when the diff is small or low-risk.

## Severity

- Critical: data loss, security breach, corruption, or blocking runtime failure.
- Warning: incorrect behavior, regression, or missing requirement.
- Minor: low-risk maintainability or convention issue.

## Sections

Wrap `Files`, `Tests`, `Reference`, and the `RESOLVED` and `IGNORED` counts in `<sub>`; the reviewer needs them, the reader does not. Order findings by severity. Numbers stay stable across sections; put `---` between findings. Keep all three finding sections, writing `None.` when empty. `TODO` holds open, deferred, and disputed findings; `RESOLVED` holds applied fixes; `IGNORED` needs the user's explicit choice. `Status: approved` records user approval only.

Write `review.md` only after the review completes; a re-review updates it. For uncommitted work, `Diff fingerprint` identifies the snapshot.
