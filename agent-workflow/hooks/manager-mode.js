#!/usr/bin/env node
// Session switch for manager mode.
// `/agent-workflow:manager on` sets a per-session flag; `off` clears it.
// While the flag is set, every prompt gets a reminder to route it through manager.

const fs = require('fs');
const os = require('os');
const path = require('path');

const FLAG_DIR = path.join(os.homedir(), '.agent-workflow', 'manager-mode');
const TOGGLE_RE = /^\/?(?:agent-workflow:)?manager\s+(on|off)\b/;

const MANAGER_SKILL = path.join(__dirname, '..', 'skills', 'manager', 'SKILL.md');

// manager sets disable-model-invocation, so point at its file instead of the Skill tool.
const ON_CONTEXT =
  'Manager mode is on for this session. Treat this request as a manager job: ' +
  `read ${MANAGER_SKILL} and follow it to assign the work to the matching agent. ` +
  'When the request is unrelated to project work, such as a general question, answer directly without creating a subagent.';
const OFF_CONTEXT = 'Manager mode is off for this session. Handle requests normally.';

function emit(additionalContext) {
  process.stdout.write(JSON.stringify({
    hookSpecificOutput: { hookEventName: 'UserPromptSubmit', additionalContext },
  }));
}

function main() {
  let data;
  try {
    data = JSON.parse(fs.readFileSync(0, 'utf8'));
  } catch {
    return;
  }

  const sessionId = typeof data.session_id === 'string' && /^[A-Za-z0-9_-]{1,128}$/.test(data.session_id)
    ? data.session_id
    : null;
  if (!sessionId) return;
  const flag = path.join(FLAG_DIR, sessionId);

  // A slash command can arrive raw or wrapped in <command-name>/<command-args> tags.
  let prompt = (data.prompt || '').trim().replace(/\s+/g, ' ');
  const name = /<command-name>\s*([^<\s]+)\s*<\/command-name>/.exec(prompt);
  if (name) {
    const args = /<command-args>\s*([^<]*?)\s*<\/command-args>/.exec(prompt);
    prompt = name[1] + (args && args[1] ? ' ' + args[1] : '');
  }

  const toggle = TOGGLE_RE.exec(prompt.toLowerCase());
  if (toggle && toggle[1] === 'on') {
    fs.mkdirSync(FLAG_DIR, { recursive: true });
    fs.writeFileSync(flag, new Date().toISOString() + '\n');
    emit(ON_CONTEXT);
    return;
  }
  if (toggle && toggle[1] === 'off') {
    fs.rmSync(flag, { force: true });
    emit(OFF_CONTEXT);
    return;
  }

  if (fs.existsSync(flag)) emit(ON_CONTEXT);
}

try {
  main();
} catch {
  // Never block the user's prompt because of this switch.
}
