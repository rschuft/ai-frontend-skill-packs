#!/usr/bin/env python3
"""Deterministic WCAG target selection (policy/tooling helper, not legal advice).

The agent extracts explicit task/contract requirements and passes them as args;
this script does NOT attempt natural-language interpretation of prompts or AGENTS.md.
A project can optionally provide .frontend-a11y.json (documented in README).
"""
import argparse
import json
from pathlib import Path

STANDARDS = {'WCAG 2.1', 'WCAG 2.2'}
LEVELS = {'A', 'AA', 'AAA'}
DEFAULT = {'standard': 'WCAG 2.2', 'level': 'AA', 'wcag3_advisory': False}


def resolve(project: Path, task_standard=None, task_level=None):
    """Resolve explicit task > project policy > default, failing closed on bad config."""
    project = Path(project)
    policy_path = project / '.frontend-a11y.json'
    policy = {}
    if policy_path.is_file():
        try:
            policy = json.loads(policy_path.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f'Invalid {policy_path}: {exc}') from exc
        if not isinstance(policy, dict):
            raise ValueError('.frontend-a11y.json must be a JSON object')
        unknown = set(policy) - {'standard', 'level', 'wcag3_advisory'}
        if unknown:
            raise ValueError(f'Unknown .frontend-a11y.json keys: {sorted(unknown)}')
        if 'standard' in policy and policy['standard'] not in STANDARDS:
            raise ValueError('Project normative standard must be WCAG 2.1 or WCAG 2.2; WCAG 3.0 is a draft')
        if 'level' in policy and policy['level'] not in LEVELS:
            raise ValueError('Project level must be A, AA or AAA')
        if 'wcag3_advisory' in policy and type(policy['wcag3_advisory']) is not bool:
            raise ValueError('wcag3_advisory must be boolean')
    if task_standard is not None and task_standard not in STANDARDS | {'WCAG 3.0'}:
        raise ValueError('Unsupported task standard; use WCAG 2.1, WCAG 2.2, or WCAG 3.0 (research only)')
    if task_level is not None and task_level not in LEVELS:
        raise ValueError('Task level must be A, AA or AAA')
    if task_standard == 'WCAG 3.0':
        if task_level is not None:
            raise ValueError('WCAG 3.0 draft has no A/AA/AAA levels; do not use 2.x levels')
        return {'standard': 'WCAG 3.0', 'level': None, 'mode': 'research_only', 'conformance_allowed': False,
                'source': 'explicit-task', 'wcag3_advisory': True,
                'catalog': 'knowledge/wcag/3.0/draft-guidance.json',
                'note': 'WCAG 3.0 is a Working Draft; no conformance finding or certificate can result.'}
    version = task_standard or policy.get('standard', DEFAULT['standard'])
    level = task_level or (policy.get('level') if task_standard is None or task_standard == policy.get('standard') else None) or DEFAULT['level']
    source = 'explicit-task' if task_standard is not None or task_level is not None else 'project-policy' if policy else 'default'
    return {'standard': version, 'level': level, 'mode': 'normative', 'conformance_allowed': True,
            'source': source, 'wcag3_advisory': policy.get('wcag3_advisory', False),
            'catalog': 'knowledge/wcag/2.2/criteria.json' if version=='WCAG 2.2' else 'knowledge/wcag/2.1/criteria.json',
            'note': 'This selects a test target; it does not establish legal applicability or actual conformance.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--project', type=Path, default=Path('.'))
    p.add_argument('--task-standard', choices=['WCAG 2.1','WCAG 2.2','WCAG 3.0'])
    p.add_argument('--task-level', choices=['A','AA','AAA'])
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    try:
        result=resolve(args.project,args.task_standard,args.task_level)
    except ValueError as e:
        p.error(str(e))
    if args.json:
        print(json.dumps(result,indent=2))
    else:
        print(f"{result['standard']} {result['level'] or '(research only)'} [{result['source']}] — {result['mode']}")
    return 0


if __name__=='__main__':
    raise SystemExit(main())
