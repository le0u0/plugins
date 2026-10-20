---
name: think
description: 'Think through one ticket with the user before planning: missing requirements, unclear acceptance criteria, edge cases, risks, concerns. Use for "think through PROJ-123" or "what is unclear here".'
effort: high
metadata:
  tier: advanced
---

# Think

Report per [reports.md](../manager/references/reports.md). Write no plan, production code, or tests.

1. Gather the ticket from supplied context. For a ticket URL or explicit lookup, run `triage-ticket` first. Use the [task folder](../manager/references/storage.md).
2. Read the [project references](../manager/references/project-references.md) and the code the ticket likely touches, enough to judge feasibility.
3. Find what the ticket leaves open: missing or conflicting requirements, unclear acceptance criteria, edge and error cases, roles and permissions, test data, dependencies, design and wording, risks to existing behavior, and simpler alternatives.
4. Ask one numbered batch of at most seven questions, most important first. Include a glossary term clash or an ADR-worthy decision as a question. Give each a recommended answer and one line on why it matters. Skip what the ticket or code already answers.
5. Record each answer in `think.md` in the task folder's `state/` per the [written docs](../manager/references/written-docs.md) rules, one line each. Ask a follow-up batch only for gaps the answers opened.
6. Save each settled term to the glossary, and an ADR the user accepts, per [domain-docs.md](references/domain-docs.md).

```markdown
# Think: PROJ-123 title

## Decisions

- Export button hidden when flag off. Print unchanged.

## Open questions

None.

## Concerns

- Share dialog has no flag guard today.
```

Done when `think.md` holds a decision, or an assumption the user accepted, for every question asked, and the user says to plan or no questions remain. Report the decision count and open questions. Planning goes to `plan`.
