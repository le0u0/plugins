# Guide Format

The reader tests by hand, knows nothing about the code, and has no source. Say what to do and what to expect.

```markdown
# PROJ-123: title

## Setup

- AC_1: account that can <what it must be able to do>.
- CL_1: clinic with <state it must be in>.
- Setting <name> is ON for CL_1.

## <Area>

- <screen>: <step>.
- <screen>: <step>.
- Expect: <result of the steps above>.

Edge cases:

- <screen>: <step>.
- Expect: <result>.

## Not affected

- <thing that must stay unchanged>.

## Flow

<optional diagram>
```

## Rules

- Title starts with the ticket number. With none, use a short feature description, so the guide is easy to find and never duplicated.
- Bullets only. At most 15 words each. One step per bullet.
- State an expected result only where a step needs one, usually once per group of steps.
- In each area, give the normal case first, then the edge cases.
- Setup says what must be set or exist before testing. Use placeholders AC_1, AC_2 for accounts and CL_1, CL_2 for clinics, and describe the concept each needs. Give a real account only when it needs a preference only the backend can set.
- No duplicates; state a shared rule once.
- Use words from the screen: menu, button, and field names. Never write file paths, component names, code names, or implementation detail.
- List only what the change affects. Put what must stay unchanged under Not affected.
- Add a short diagram only when a flow is hard to say in words. Prefer a simple Mermaid flowchart.
- Keep the whole guide short, about one screen per area.
