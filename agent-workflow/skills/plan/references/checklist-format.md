# Checklist Format

Create `checklist.md` beside the plan, progress first, one item per step. Mark one current item; several only when they share no files or state. Add discovered work, delete an item only with approval, and untick invalidated work with a short reason. Follow the [written docs](../../manager/references/written-docs.md) rules; `Step notes` is one line per step.

```markdown
# PROJ-123 checklist

## Implementation

- [x] Step 1: clamp remaining count
- [ ] Step 2: hide empty list - current

## Step notes

- Step 1: Spec failed, then passed after clamp.

## Task files

<sub>Modified: `src/example.test`</sub>

## Evidence

<sub>Unit: expected failure, then pass; command and checkout recorded here.</sub>

## Reference

<sub>Repository: /absolute/path/to/repo<br>Branch: PROJ-123-do-something<br>Initial baseline: a1b2c3d<br>Current HEAD: a1b2c3d<br>Current step: 2 of 2<br>Next action: approve Step 2</sub>
```

Update it after each step and before handoff, including finding IDs and dispositions. List unrelated existing changes separately. On resume, check drift per the start gate in [step-execution.md](../../develop/references/step-execution.md).
