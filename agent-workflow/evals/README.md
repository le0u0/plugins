# Evals

Behavioral cases for the skills: file changes and executed commands, not just frontmatter and links.

## Run

1. Prepare disposable fixtures outside any real checkout. This creates git repos with a synthetic test runner and installs nothing.

   ```bash
   python3 evals/fixture.py prepare /private/tmp/agent-workflow-evals-UNIQUE
   ```

2. For each case in `cases.json`, give a fresh agent only the skill path (from `skills/`, not an installed cache), the generated `request.txt`, and the `repo` directory. Do not give it `checks`, `before.json`, or the fixture script. Have it save its final answer as `response.md` beside `repo`.

3. Check files and commands:

   ```bash
   python3 evals/fixture.py check /private/tmp/agent-workflow-evals-UNIQUE
   ```

4. Read the traces and responses against each case's `checks`. For the manager cases, confirm each handoff and that agents start no extra subagents.

5. Repeat without the skill as a baseline. A case that passes both ways may be redundant, so shorten it unless it guards safety, approval, or scope.

Use `--case CASE_ID` (repeatable) with `prepare` and `check` to run a subset.

## Limits

The runner is synthetic. It logs arguments and file hashes at each call, so it catches config or spec edits used to narrow a run. It cannot validate real tests, browsers, or ticket tools. A failing focused command must stay a reported failure.
