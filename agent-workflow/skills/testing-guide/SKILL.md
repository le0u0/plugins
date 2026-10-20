---
name: testing-guide
description: 'Write a short manual testing guide for a finished ticket, for a tester who knows nothing about the code. Use for "write the testing guide".'
effort: medium
metadata:
  tier: standard
---

# Testing Guide

Report per [reports.md](../manager/references/reports.md). Produce text only.

1. Gather `plan.md`, `think.md`, and the diff from the plan's initial baseline to find what changed for users. Use the screen names users see, with no file paths or component names.
2. Write the guide per [guide-format.md](references/guide-format.md).
3. Save it as `testing-guide-{short-description}.md` in the task folder, else in `~/.agent-workflow/reviews/{repository}/{branch}/`.
4. Reply with the path and the guide.

Done when every acceptance criterion in `plan.md` is covered by a guide step and every bullet is 15 words or fewer.
