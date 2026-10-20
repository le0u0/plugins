# Storage

Every file this plugin writes lives under `~/.agent-workflow/`, so any repository can reach it. The repository receives only the source and test changes the job requires.

```text
~/.agent-workflow/
  tasks/{ticket}/
    plan.md
    checklist.md
    review.md
    pr.md
    testing-guide-{short-description}.md
    attachments/{ticket}/   # cached ticket files
    state/
      jobs.md
      think.md
      triage.md
      diagnose.md           # optional
      research-{topic}.md   # optional
      logs
  reviews/{repository}/{branch}/   # review.md, pr.md, testing guide when there is no task folder
  docs/                            # glossary.md and adr/, shared by every project
  projects/{repository}/           # commit-format.md
```

The user reads the files above `state/`. The plugin keeps everything else in `state/`.

Write only the files listed here. Create a file when it is missing; when it exists, update it in place. A new version, a rerun, or a changed plan edits the same file and never adds a numbered or dated copy.

## Task folder

Name it after the ticket key, such as `PROJ-123`. With no ticket, use a short kebab-case description. When work spans linked tickets, use the one the user works under. One folder serves a ticket across repositories.

Find it by globbing `~/.agent-workflow/tasks/{ticket}*`, with the key from the user's message or the branch name. Several matches: use the oldest. None: ask. A user-supplied path wins.
