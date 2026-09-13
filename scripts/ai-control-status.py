#!/usr/bin/env python3
"""Read-only launchd inventory. Never print arguments, environment or log content."""
from datetime import datetime
from pathlib import Path
import plistlib
import subprocess

EXPECTED = {
    'daily-fetch', 'daily-ingest', 'lint-knowledge', 'dronewiki-self-update',
    'sync-dronewiki', 'extract-knowledge-graph', 'update-knowledge-graph',
    'apply-kinetic-rules', 'morning-report', 'weekly-lint', 'weekly-summary',
    'medic-wiki-fetch',
}


def loaded_jobs(text):
    """A loaded idle job has PID '-', distinct from an absent job."""
    jobs = {}
    for line in text.splitlines():
        parts = line.split()
        if len(parts) == 3 and parts[2].startswith('ai.2nd.'):
            jobs[parts[2]] = (parts[0], parts[1])
    return jobs


def schedule(data):
    value = data.get('StartCalendarInterval')
    entries = value if isinstance(value, list) else [value] if value else []
    rendered = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        clock = ':'.join(str(entry.get(k, '*')).zfill(2) for k in ('Hour', 'Minute'))
        extra = ','.join(f'{k}={entry[k]}' for k in ('Weekday', 'Day', 'Month') if k in entry)
        rendered.append(clock + (' ' + extra if extra else ' daily'))
    if data.get('StartInterval'):
        rendered.append(f'every {data["StartInterval"]}s')
    return '; '.join(rendered) or 'on-demand'


def latest_log(data, label=""):
    """Include wrapper logs as well as launchd stdout/stderr without reading them."""
    stamps = []
    for key in ('StandardOutPath', 'StandardErrorPath'):
        path = data.get(key)
        if isinstance(path, str):
            try:
                stamps.append(Path(path).stat().st_mtime)
            except OSError:
                pass
    if label.startswith('ai.2nd.'):
        stem = label.removeprefix('ai.2nd.')
        for name in (stem + '.log', '2nd-' + stem + '.log'):
            try:
                stamps.append((Path.home() / '2nd/.ua/logs' / name).stat().st_mtime)
            except OSError:
                pass
    return datetime.fromtimestamp(max(stamps)).astimezone().isoformat(timespec='seconds') if stamps else 'unknown'


def main():
    try:
        proc = subprocess.run(['launchctl', 'list'], capture_output=True, text=True, timeout=10)
        jobs = loaded_jobs(proc.stdout) if proc.returncode == 0 else {}
        available = proc.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        jobs, available = {}, False
    plists = {p.stem: p for p in (Path.home() / 'Library/LaunchAgents').glob('ai.2nd.*.plist')}
    labels = set(plists) | set(jobs) | {'ai.2nd.' + j for j in EXPECTED}
    print('AI control plane | local timezone | log timestamp = file modification time')
    for label in sorted(labels):
        data = {}
        state = 'missing'
        if label in plists:
            try:
                data = plistlib.loads(plists[label].read_bytes())
                state = 'present'
            except (OSError, ValueError, plistlib.InvalidFileException):
                state = 'invalid'
        pid, code = jobs.get(label, ('-', 'unknown'))
        loaded = ('yes' if label in jobs else 'no') if available else 'unknown'
        print(f'{label} | plist={state} loaded={loaded} pid={pid} exit={code} | '
              f'{schedule(data)} | log={latest_log(data, label)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
