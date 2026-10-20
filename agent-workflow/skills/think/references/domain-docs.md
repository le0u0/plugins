# Domain Docs

Domain notes live in `~/.agent-workflow/docs/`, never in a repository, so every project, ticket, and agent sees the same definitions.

```text
~/.agent-workflow/docs/glossary.md
~/.agent-workflow/docs/adr/0001-slug.md
```

Read the repository's own `GLOSSARY.md` and `docs/adr/` too, if present, and leave them unedited.

## While asking

- Ticket word conflicts with a glossary term: ask which meaning is intended.
- Vague word: propose one precise term and ask.
- Code contradicts the user: ask which is right.

## Glossary

`glossary.md` is one table:

```markdown
| Term | Meaning | Avoid | Scope |
| --- | --- | --- | --- |
| Export button | Toolbar button that downloads the current view. | Download link | all |
```

Add a row only after the user confirms the term and its meaning. Keep one sentence per meaning and no implementation details. `Scope` is `all` or the project the term belongs to.

## ADR

Offer one only when the decision is hard to reverse, surprising without context, and a real trade-off. After the user accepts, write the next numbered file in `~/.agent-workflow/docs/adr/`: a title, then one to three sentences of context, decision, and why.
