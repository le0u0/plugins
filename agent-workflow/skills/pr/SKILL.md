---
name: pr
description: 'Write the pull request title and body for a finished, approved ticket: a visual summary, before and after evidence, and merge danger. Use for "write the PR", "PR text", or when manager assigns it after the review is approved.'
effort: medium
metadata:
  tier: standard
---

# PR

Follow [dispatch](../manager/references/dispatch.md). Write text only: create no PR, push nothing.

1. Gather the task folder's `plan.md`, `checklist.md`, and approved `review.md`, and the diff from the plan's initial baseline. With no task folder, use the diff and what the user told you. Use the project's own terms.
2. Write the title as one line in the project's commit format.
3. Write the body per [pr-format.md](references/pr-format.md). Keep prose short and skip preambles.
4. Save it as `pr.md` in the task folder, else `~/.agent-workflow/reviews/{repository}/{branch}/pr.md`. The one-line rule for written docs does not apply to the body.
5. Reply with the title, the body, and the path.
