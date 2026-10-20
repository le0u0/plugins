# Diagnose a Failure

Use when a test fails or a bug is reported. Redact secrets in anything you quote.

1. **Build a loop first.** One command you have already run that goes red on this exact failure, deterministically, in seconds, without a human. Try in order: a failing test at the right seam, a script against the running app, a replay of a captured input, a bisect between two known states. With no loop, stop and say what you tried. Never theorize without one.
2. **Reproduce and minimize.** Confirm it shows the reported symptom, then cut inputs and steps one at a time until each remaining piece is needed.
3. **Hypothesize.** Write 3 to 5 ranked, falsifiable guesses: "if X is the cause, changing Y fixes it." Show them to the user before testing when the user is present.
4. **Probe.** One change at a time, each tied to one hypothesis. Prefer a debugger or a targeted log. Prefix every temporary log with a unique tag such as `[DEBUG-a4f2]`.
5. **Fix.** Turn the minimal repro into a failing test at the seam where the bug really occurs, watch it fail, fix, watch it pass. With no right seam, report that as a finding.
6. **Clean up.** Re-run the loop, remove every tagged log and throwaway file, and state the confirmed cause in the report.
