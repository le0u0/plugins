# Scope and Baseline

## Baseline order

1. User-supplied baseline.
2. `Reviewed to` SHA from the matching `review.md`.
3. An evidenced Git parent, for a first review.
4. Ask when uncertain.

Before reviewing, confirm the baseline resolves and the diff is not empty; otherwise stop and say so.

When a saved SHA is missing, invalid, or not an ancestor of `HEAD`, stop and ask. Never fall back to a larger range.

## Range

Changes after the baseline through `HEAD`, plus staged, unstaged, and untracked source or test changes. Review the full plan scope from its initial baseline only when asked.

## Refs

Resolve refs locally first. For a first review, reuse the plan's `Initial baseline` when it matches this checkout. Fetch only when a ref is missing locally or the user asks for a remote comparison; never enumerate all remote branches.

## Parent branch

Never infer it from the branch name; a branch created from A compares with A, not the default branch. Check the reflog and candidate ancestry; a tracking branch alone is not proof. When still ambiguous, ask one question.

## Exclude

Ignored files, generated or build output, dependencies, reports, screenshots, and traces.
