# Diagnose Doc

Record a diagnosis in `state/diagnose.md`: create it when missing, update it in place when it exists. `develop` writes it after diagnosing a failure, and `plan` writes it for a bug ticket whose diagnosis would clutter `plan.md`. Write it per the [written docs](../../manager/references/written-docs.md) rules:

```markdown
# Diagnose: PROJ-123 question

## Conclusions

- Root cause: `x` skips guard when flag off.
- Affected path: `a.ts:12` to `b.ts:40`.
- Unverified: prod flag default.

## Rejected

- Cache stale: value fresh in trace.

## Evidence

- <sub>fact: `a.ts:12` reads flag once.</sub>
- <sub>inference: `b.ts:40` never reruns.</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>HEAD: a1b2c3d</sub>
```

`Conclusions` come first, at most five bullets, only what affects scope, design, risk, or validation. `Rejected` is one short reason each. Label each evidence line fact, inference, or unverified.

The diagnosis is evidence, not authorization. Copy its conclusions into `plan.md` `## Decisions` for approval; never keep competing scopes across both files.

