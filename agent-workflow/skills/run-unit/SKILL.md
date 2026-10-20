---
name: run-unit
description: 'Run focused unit tests and report failures with evidence, changing no files. Use for "run the unit tests for X".'
effort: low
metadata:
  tier: light
---

# Run Unit

Report per [reports.md](../manager/references/reports.md).

1. Read `AGENTS.md` and `CLAUDE.md`. Run tests only when the request or approved plan authorizes them; a later no-tests instruction wins.
2. Read [running.md](references/running.md) and run the exact target.
3. Report per the [test report](../manager/references/reports.md). Do not diagnose the cause; the manager sends diagnosis to `developer`.

Done when the scope passes, or the failed specs are reported with their fix owner: `write-unit` for the spec, `develop` for production code. Change no files.
