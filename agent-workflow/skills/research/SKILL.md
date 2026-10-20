---
name: research
description: 'Investigate a question against primary sources and save cited findings. Use for "research X" or "what does this API do".'
effort: medium
metadata:
  tier: standard
---

# Research

Report per [reports.md](../manager/references/reports.md).

1. Resolve the question and the decision it feeds. Ask only when the question is unclear.
2. Investigate against primary sources: official docs, source code, specs, and first-party APIs. Follow each claim back to the source that owns it, and skip secondary write-ups.
3. Write the findings to `research-{topic}.md` in the task folder's `state/`, else in `~/.agent-workflow/reviews/{repository}/{branch}/`. Create it when missing; update it in place when it exists. Follow [written-docs.md](../manager/references/written-docs.md), with each claim's source link in `<sub>` beside it. Label a claim `unverified` when no primary source confirms it.
4. Reply with the answer in at most three lines and the path.

Done when every claim in the file cites a primary source or is labelled `unverified`, and the question has an answer or a stated gap.
