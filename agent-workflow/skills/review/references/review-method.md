# Standards and Requirements

Apply both axes in the single review pass.

- **Standards:** check changed hunks against repository instructions and cite the rule. Omit preferences, generic refactors, and checks tooling enforces.
- **Requirements:** compare expected behavior with changed control flow and outcomes: missing behavior, wrong implementation, or consequential scope creep. Without requirements, skip this axis.

## Evidence

Inspect callers, types, tests, and state handling only to confirm an issue. A finding needs a reachable trigger, impact, an exact changed location, and a feasible fix. A missing test is not a defect unless required or tied to a shown regression.

Done when every changed hunk is assessed. Missing evidence limits a finding; it never skips the review.
