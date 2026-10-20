# UI Exploration

Explore the flow before writing any spec. A spec written from source alone guesses locators, waits, and data, and fails on its first real run. Exploring opens the page and walks the flow; it never runs a spec.

- Use the browser tool the project names, named in the project docs, never one that would add a dependency to the project. Open the base URL with the project's auth state and the seeded data the spec will use. When the tool cannot load the auth state or reach the page, report it.
- Walk the whole flow the spec covers. Inspect targeted elements and attributes; take screenshots only for visual evidence. Send snapshots to files and read only the lines you need.
- Keep only the stable locators, the step order, loading and empty states, and the data the flow needs. Keep snapshots out of your notes and report.
- When seeded data is missing, report it; a reset needs the user's explicit request.
- Return behavior, generated interaction code, and stable locators. Generated code is authoring input, not compatibility proof. Change files only when asked.
