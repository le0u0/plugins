#!/usr/bin/env python3
"""Prepare/check isolated behavioral evaluation fixtures; never runs an agent."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

CASES = json.loads(Path(__file__).with_name('cases.json').read_text())
SOURCE = 'src/main/webapp/app/counter.ts'
SPEC = 'src/main/webapp/app/counter.spec.ts'

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()

def snapshot(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and '.git' not in p.parts
            and p.name != 'runner-events.jsonl'}

def prepare(base):
    base.mkdir(parents=True, exist_ok=False)
    for case in CASES:
        home = base / case['id']
        root = home / 'repo'
        task = home / 'task'
        task.mkdir(parents=True)
        files = {
            SOURCE: 'export function remaining(total, used) { return total - used; }\nexport function greeting(name) { return `Hello ${name}`; }\nexport function hasItems(count) { return count >= 0; }\n',
            SPEC: "import { remaining } from './counter';\ndescribe('remaining', () => { it('subtracts used', () => { expect(remaining(5, 2)).toBe(3); }); });\n",
            'src/test.ts': "// Existing user customization: preserve this comment.\nconst context = require.context('./', true, /\\.spec\\.ts$/);\ncontext.keys().map(context);\n",
            'karma.conf.js': 'module.exports = {};\n',
            'tsconfig.spec.json': '{"include":["src/**/*.spec.ts"]}\n',
            '.agents/rules/coding-instructions.mdc': '# Fixture rules\nRead nearby code. These synthetic .ts files intentionally use valid JavaScript syntax. Match it. No formatter configured. Test authors use Jasmine behavior assertions.\n',
            '.gitignore': 'node_modules/\nrunner-events.jsonl\n',
            'package.json': json.dumps({'private': True, 'scripts': {'test': 'ng test app-ui --browsers=ChromeHeadless --watch=false'}}),
            'angular.json': json.dumps({'projects': {'app-ui': {'root': '', 'architect': {'test': {'builder': '@angular-devkit/build-angular:karma', 'options': {'main': 'src/test.ts', 'karmaConfig': 'karma.conf.js'}}}}}}),
            'node_modules/@angular-devkit/build-angular/src/karma/schema.json': json.dumps({'properties': {'include': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Workspace-relative spec globs'}}}),
        }
        runner = '''#!/usr/bin/env python3
import hashlib,json,pathlib,sys
if '--help' in sys.argv[1:]:
    print('ng test [project] --include=<workspace-relative spec glob> --browsers=<browser> --watch=<boolean>'); sys.exit(0)
root=pathlib.Path.cwd()
files={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and p.name!='runner-events.jsonl'}
with open('runner-events.jsonl','a') as out: out.write(json.dumps({'args':sys.argv[1:],'files':files})+'\\n')
'''
        if case['id'] == 'focused-fail':
            runner += "print('ERROR: unrelated.spec.ts: TS2322 existing type mismatch (synthetic runner)'); sys.exit(1)\n"
        else:
            runner += "print('Synthetic runner: selected counter.spec.ts; TOTAL: 1 SUCCESS (fixture output only)')\n"
        files['node_modules/.bin/ng'] = runner
        if case['id'] == 'focused-no-rules':
            files['CLAUDE.md'] = files.pop('.agents/rules/coding-instructions.mdc')
        if case['id'] == 'ensure-repeat':
            files.update({
                'playwright.config.ts': "export default { use: { baseURL: 'https://fixture.invalid' } };\n",
                'playwright/helpers/data/storage-state.ts': "export const DEFAULT_STORAGE_STATE = 'fixture-state.json';\n",
                'playwright/helpers/data/pre-test.ts': "export const preTestFm = { existing: 'PW-PRE-OLD' };\n",
                'playwright/fm-setup/widget-fm.setup.ts': '// Legacy setup retained.\n',
                'playwright/helpers/fm/widget.u.ts': "const records = [];\nexport async function findWidget(page, code) { return records.find(record => record.code === code); }\nexport async function createWidget(page, data) { const record = { id: records.length + 1, ...data }; records.push(record); return record; }\nexport function fixtureRecords() { return records; }\n",
                'playwright/tests/widget.spec.ts': "import { test, expect } from '@playwright/test';\nimport { DEFAULT_STORAGE_STATE } from '../helpers/data/storage-state';\ntest.use({ storageState: DEFAULT_STORAGE_STATE });\ntest('widget label', async ({ page }) => {\n  await page.goto('/widgets');\n  await expect(page.getByTestId('widget-label')).toHaveText('Example');\n});\n",
            })
        for name, content in files.items():
            p = root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
        (root / 'node_modules/.bin/ng').chmod(0o755)
        git(root, 'init', '-b', 'PROJ-9999-evaluation')
        git(root, 'add', '.')
        git(root, '-c', 'core.hooksPath=/dev/null', '-c', 'user.name=Skill Evaluation', '-c', 'user.email=evaluation@example.invalid', 'commit', '-qm', 'Fixture baseline')
        # Preserve an actual pre-existing unstaged bootstrap edit, not just a clean file.
        with (root / 'src/test.ts').open('a') as out:
            out.write('// Uncommitted user note.\n')
        head = git(root, 'rev-parse', 'HEAD')
        (task / 'plan.md').write_text(f'# Approved PROJ-9999 plan\nRepository: {root}\nBranch: PROJ-9999-evaluation\nInitial baseline: {head}\nApproved scope: clamp remaining(total, used) to zero when used exceeds total, and add its regression in counter.spec.ts.\nApproved files: {SOURCE}, {SPEC}\nDelivery: leave uncommitted\nValidation: user will run tests; agent must not execute tests. Formal review excluded for this run.\n')
        (task / 'checklist.md').write_text(f'# Checklist\nHEAD: {head}\nNext action: implement approved clamp and spec.\n- [ ] Clamp and regression\n')
        (task / 'review.md').write_text(f'# Code review\n\nStatus: reviewed\nRepository: {root}\nBranch: PROJ-9999-evaluation\nReviewed from: {head}\nReviewed to: {head}\nRequirement: plan.md\n\n## Findings\n\n1. Warning: remaining returns negative values. Clamp to zero.\nFile: {SOURCE}:1\n\n2. Minor: greeting retains surrounding whitespace. Trim the name.\nFile: {SOURCE}:2\n\n3. Warning: hasItems accepts zero. Require a positive count.\nFile: {SOURCE}:3\n\n## Tests\nUnit: Not run.\n')
        if case['id'] in ('review-precise', 'review-inline', 'manager-review-routing'):
            (root / SOURCE).write_text('export function remaining(total, used) { return total + used; }\nexport function greeting(person) { return `Hello ${person}`; }\nexport function hasItems(count) { return count >= 0; }\n')
            (task / 'plan.md').write_text(f'# Requirements\nRepository: {root}\nBranch: PROJ-9999-evaluation\nBaseline: {head}\nremaining computes total minus used. greeting returns Hello followed by the supplied name, preserving whitespace. Review current changes only.\n')
            (task / 'review.md').unlink()
            if case['id'] == 'review-inline':
                (task / 'plan.md').unlink()
                (task / 'checklist.md').unlink()
        before = {'files': snapshot(root), 'task': {p.name:p.read_text() for p in task.iterdir()}, 'head': head, 'index': git(root, 'write-tree')}
        (home / 'before.json').write_text(json.dumps(before, indent=2))
        (home / 'request.txt').write_text(case['request'].replace('{task}', str(task)))
    print(base)

def check(base):
    results = []
    for case in CASES:
        home = base / case['id']; root = home / 'repo'; task = home / 'task'
        before = json.loads((home / 'before.json').read_text()); after = snapshot(root)
        changed = sorted(k for k in before['files'].keys() | after.keys() if before['files'].get(k) != after.get(k))
        events = [json.loads(s) for s in (root / 'runner-events.jsonl').read_text().splitlines()] if (root / 'runner-events.jsonl').exists() else []
        errors = []
        if not (home / 'response.md').exists(): errors.append('agent response missing')
        allowed = {SOURCE, SPEC} if case['id'] in ('implementation-no-tests', 'selected-findings') else {SPEC} if case['id'] == 'unit-author-run' else {'playwright/helpers/fm/widget.u.ts', 'playwright/tests/widget.spec.ts'} if case['id'] == 'ensure-repeat' else set()
        if set(changed) - allowed: errors.append('unexpected file changes: ' + str(changed))
        if git(root, 'rev-parse', 'HEAD') != before['head']: errors.append('HEAD changed')
        if git(root, 'write-tree') != before['index']: errors.append('index changed')
        if case['id'].startswith('focused-') or case['id'] == 'unit-author-run':
            runs = [event for event in events if '--help' not in event['args']]
            if len(runs) != 1: errors.append('expected exactly one test invocation')
            for event in events:
                args = event['args']
                if '--help' not in args and '--include='+SPEC not in args and not any(args[i:i+2] == ['--include', SPEC] for i in range(len(args))): errors.append('missing exact spec selector')
                expected_files = after if case['id'] == 'unit-author-run' else before['files']
                if event['files'] != expected_files: errors.append('unexpected files during runner invocation')
            if case['id'] == 'unit-author-run':
                if SPEC not in changed: errors.append('regression spec missing')
                if 'remaining' not in (root/SPEC).read_text() or '-3' not in (root/SPEC).read_text(): errors.append('negative-result assertion missing')
        elif events: errors.append('unauthorized runner invocation')
        if case['id'] in ('review-inline', 'manager-review-routing'):
            if not (task / 'review.md').exists(): errors.append('review report missing')
            if case['id'] == 'review-inline' and (task / 'plan.md').exists(): errors.append('unrequested plan created')
        if case['id'] == 'approval-only':
            for name, original in before['task'].items():
                expected = original.replace('Status: reviewed', 'Status: approved') if name == 'review.md' else original
                if (task/name).read_text() != expected: errors.append('unexpected artifact content: '+name)
        if case['id'] in ('implementation-no-tests', 'selected-findings'):
            # Evaluate behavior, not the spelling of the proposed implementation.
            js = (root/SOURCE).read_text().replace('export ', '')
            js += '\nif (remaining(2,5)!==0 || remaining(5,2)!==3 || greeting(" x ")!=="Hello  x ") process.exit(1);'
            if case['id'] == 'selected-findings': js += '\nif(hasItems(0)!==false || hasItems(1)!==true) process.exit(1);'
            if subprocess.run(['node','-e',js], capture_output=True).returncode: errors.append('behavior assertions failed')
            if case['id'] == 'implementation-no-tests' and SPEC not in changed: errors.append('regression spec missing')
        results.append({'case':case['id'], 'filesystem_and_command_checks':'PASS' if not errors else 'FAIL', 'errors':errors, 'changed':changed, 'runner_calls':sum('--help' not in event['args'] for event in events)})
    print(json.dumps(results, indent=2))
    return all(not r['errors'] for r in results)

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['prepare','check']);parser.add_argument('directory',type=Path);parser.add_argument('--case', action='append', choices=[case['id'] for case in CASES]);args=parser.parse_args()
    if args.case: CASES = [case for case in CASES if case['id'] in args.case]
    if args.mode=='prepare': prepare(args.directory.resolve())
    else: raise SystemExit(0 if check(args.directory.resolve()) else 1)
