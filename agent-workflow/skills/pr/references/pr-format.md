# PR Format

```markdown
## Summary

<one visual>

## Evidence

- **Before:** <failing test run, output, or screenshot>
  **After:** <passing test run, output, or screenshot>

## Merge Danger

**Door:** one-way | two-way

**Blast Radius:** <one word>
<optional: what could break>
```

## Summary

Pick the smallest visual that makes the point:

- Logic: pseudocode.
- Runtime flow: call tree.
- UI structure: component tree.
- Broad refactor: shallow file tree.
- Interaction or data flow: Mermaid diagram.
- Change to an existing shape: a `diff` block of that shape, not of the files.

Show only the calls, files, and states that matter. Use one or two visuals, rarely more.

## Evidence

Show proof, not claims. A before and after screenshot is best for visual changes. Otherwise show the exact test that failed and now passes, as pseudocode, with the command and result from `checklist.md`. Never invent a result; write `not run` when there is none.

## Merge Danger

- **Door:** two-way if a revert is cheap. One-way for destructive or hard-to-reverse changes such as data migrations.
- **Blast Radius:** who or what is affected if it goes wrong, such as layout, consumers of an API, or mobile.
