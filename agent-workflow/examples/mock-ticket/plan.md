# PROJ-9999 — Prevent duplicate saves

Mock example. Ticket, paths, SHAs, and outcomes are fictional.

## TL;DR

- Prevent a second Save request while the first is pending.
- Restore Save after a failed request so the user can retry.
- Change only the profile form and its unit spec. Keep the API and permissions unchanged.
- Focused unit execution is authorized; E2E execution is not.

## Acceptance criteria

- The first Save click submits one update; repeated clicks submit no more.
- Save stays disabled during the request.
- Success closes the edit flow. Failure shows the existing error and permits retry.

## Steps

1. Add a repeated-click unit test.
2. Guard the submit path and show the pending state on Save.
3. Run the focused unit spec, then review the full task diff.

## Implementation details

- Production: `src/app/profile/profile-form.component.ts` and its template.
- Test: `src/app/profile/profile-form.component.spec.ts`.
- No temporary API contract or access-right change.
- Review may identify gaps; fixes still need the user's disposition.

## Reference

Status: approved for this example
Requirement source: example user request — "A second Save click must not send another request. Save must work again after a failed request."
Repository: /example/repo
Branch: PROJ-9999-prevent-duplicate-save
Initial baseline: a1b2c3d
Delivery: leave changes uncommitted
