---
name: testing-guide
description: 'Write a short manual testing guide for a finished ticket, for a tester who knows nothing about the code. Use for "write the testing guide", or when manager assigns it together with the PR text.'
effort: medium
metadata:
  tier: standard
---

# Testing Guide

Follow [dispatch](../manager/references/dispatch.md). Write text only.

1. Gather `plan.md`, `think.md`, and the diff from the plan's initial baseline to find what changed for users. Use the screen names users see; never file paths or component names.
2. Write the guide per [guide-format.md](references/guide-format.md).
3. Save it as `testing-guide.md` in the task folder, else `~/.agent-workflow/reviews/{repository}/{branch}/testing-guide.md`.
4. Reply with the path and the guide.
