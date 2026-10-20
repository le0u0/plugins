# Domain Docs

Domain notes live in `~/.agent-workflow/projects/{repository}/`, never in the repository. `{repository}` is the name from the `origin` remote, else the folder name.

```text
glossary.md
adr/0001-slug.md
```

Read the project's own `GLOSSARY.md` and `docs/adr/` too, if present. Never edit them.

## While asking

- Ticket word conflicts with a glossary term: ask which meaning is intended.
- Vague word: propose one precise term and ask.
- Code contradicts the user: ask which is right.

## Glossary

When an answer settles a term, add it to `glossary.md`: one or two sentences saying what it is, plus `_Avoid_:` synonyms. Project-specific terms only, no implementation details.

## ADR

Offer one only when the decision is hard to reverse, surprising without context, and a real trade-off. After the user accepts, write the next numbered file: a title, then one to three sentences of context, decision, and why.
