# Project References

This plugin holds no framework or domain rules. The project being changed owns them. Before code or test work, find and read what applies:

- `AGENTS.md`, `CLAUDE.md`, and rule files in `.agents/rules/` or `.claude/rules/`. When the plan step lists the relevant rule files, read only those.
- Project-local skills in `.claude/skills/` and `.agents/skills/`. Match the job against each skill's name and description, such as a `create-*` or `testing-*` skill, then read and follow the matching ones. They win over this plugin's defaults where they conflict.
- The nearest comparable feature or spec, found by searching the checkout for a folder, file, or class name.

When nothing applies, say so and follow the nearest comparable code. Link to project rules instead of copying them into task docs.
