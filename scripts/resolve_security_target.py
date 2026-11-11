#!/usr/bin/env python3
"""Resolve an OWASP ASVS target from explicit task, project policy, or default.

Structured inputs only. This does not parse prose, approve testing, or certify security.
"""
import argparse
import json
from pathlib import Path

POLICY_NAME = '.frontend-security.json'
STANDARD = 'OWASP ASVS'
VERSION = '5.0.0'
DEFAULT_LEVEL = 2


def validate(level, label):
    if type(level) is not int or level not in (1, 2, 3):
        raise ValueError(f'{label} must be integer 1, 2, or 3')


def resolve(project: Path, task_standard=None, task_version=None, task_level=None):
    project = Path(project)
    path = project / POLICY_NAME
    policy = {}
    if path.is_file():
        try:
            policy = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError) as exc:
            raise ValueError(f'Invalid {path}: {exc}') from exc
        if not isinstance(policy, dict):
            raise ValueError(f'{POLICY_NAME} must be a JSON object')
        unknown = set(policy) - {'standard', 'version', 'level'}
        if unknown:
            raise ValueError(f'Unknown {POLICY_NAME} fields: {sorted(unknown)}')
        if policy.get('standard', STANDARD) != STANDARD or policy.get('version', VERSION) != VERSION:
            raise ValueError('Project policy must use OWASP ASVS 5.0.0; other baselines are not indexed')
        if 'level' in policy:
            validate(policy['level'], 'Project security level')
    if task_standard is not None and task_standard != STANDARD:
        raise ValueError('Only OWASP ASVS is supported as a requirements baseline')
    if task_version is not None and task_version != VERSION:
        raise ValueError('Only stable ASVS 5.0.0 is indexed')
    if task_level is not None:
        validate(task_level, 'Task security level')
    source = ('explicit-task' if any(x is not None for x in (task_standard, task_version, task_level))
              else 'project-policy' if policy else 'default')
    level = task_level if task_level is not None else policy.get('level', DEFAULT_LEVEL)
    return {
        'standard': STANDARD, 'version': VERSION, 'level': level, 'source': source,
        'catalog': 'knowledge/security/asvs/5.0.0/index.json',
        'note': 'Level 2 is only a planning fallback. Complete scope and authorized testing are required before any assurance claim.'
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--project', type=Path, default=Path('.'))
    p.add_argument('--task-standard')
    p.add_argument('--task-version')
    p.add_argument('--task-level', type=int)
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    try:
        result = resolve(args.project, args.task_standard, args.task_version, args.task_level)
    except ValueError as exc:
        p.error(str(exc))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['standard']} {result['version']} L{result['level']} [{result['source']}]")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
