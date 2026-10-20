# Attachments

Cache every attachment of every fetched ticket, any type, including embedded images, under the task folder's `attachments/{ticket}/` with original names.

- **With the tracker's MCP:** use its attachment download tool with that folder as the output path, and run any returned download command at once; such links often expire quickly.
- **Without MCP:** use the tracker's REST API with an API token from the environment, writing to `<task folder>/attachments/<ticket>/<filename>`.

Skip cached files. Never print or save the token. When a download fails or a variable is unset, list the file as missing with the cause.
