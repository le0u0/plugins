# Handoff and Reports

## Handoff

Send paths, not file contents: the resolved task folder, plan step number, files, review path. Send only the current step. State the job, acceptance criteria, test authorization, and commit rules. The agent has none of the conversation.

## Report

An agent ends with at most eight lines:

```text
Status: done | failed | blocked
Changed: <files, or none>
Commands: <command → exit code, or none>
Artifacts: <paths, or none>
Open: <what remains or needs the user, or none>
```

Keep it to facts: no narrative, restated plan, or code excerpts.

## Test report

`e2e-tester` after a run ends with this report instead, at most eight lines:

```text
Status: done | failed | blocked
Result: <counts>; failed: <spec file and test name each, or none>
Commands: <command → real exit code>
Changed: <files, or none>
Artifacts: <failure log path, or none>
Affected: <other specs that use the changed code, helpers, or selectors, not run, or none>
Open: <or none>
```

- **done:** `Result` has the counts (such as `12 specs, 0 failed`) and `Commands` has exit 0. Send no log or output.
- **failed:** list each failed spec file and test name in `Result`. `Artifacts` is a log holding only the failed tests' output (name, error, top stack lines), saved in the task folder's `state/`, else the system temp directory. State the symptom and leave the cause to the developer.
- **blocked:** `Open` has the reason and what the manager or user should do, such as `approve a full-suite run` or `start the backend`. Send no log.

Run only the specs the task changed, unless the user asks for more. On a rerun after a fix, run the previously failed specs plus the specs the fix changed. List other specs that may be affected under `Affected`, unrun.
