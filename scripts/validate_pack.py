#!/usr/bin/env python3
"""Validate the combined skill pack structure, catalogs, integrity and routing metadata."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check(ok: bool, message: str):
    if not ok:
        raise AssertionError(message)


def main():
    manifest = load('manifest.json')
    skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
    names = {p.parent.name for p in skills}
    ux_names = {name for name in names if name.startswith('ux-')}
    wcag_names = {name for name in names if name.startswith('wcag21-')}
    check(len(skills) == len(names) == 28, 'Need 28 unique skill directories')
    check(len(ux_names) == len(wcag_names) == 14, 'Pack skill counts must be 14+14')
    check(manifest['skill_count'] == 28, 'Manifest skill count mismatch')
    check({r['name'] for r in manifest['skills']} == names, 'Manifest skill names out of sync')
    check(len(manifest['skills']) == 28, 'Duplicate manifest entries')
    for name in names:
        item = next(r for r in manifest['skills'] if r['name'] == name)
        check(item['path'] == f'skills/{name}/SKILL.md', f'{name}: wrong manifest path')
        check(item['pack'] == ('ux-laws' if name.startswith('ux-') else 'wcag21'), f'{name}: wrong pack')
    for path in skills:
        name = path.parent.name
        content = path.read_text(encoding='utf-8')
        header = re.match(r'^---\n(.*?)\n---\n', content, re.S)
        check(header is not None, f'{name}: missing YAML frontmatter')
        check(re.search(r'^name:\s*' + re.escape(name) + r'\s*$', header.group(1), re.M) is not None,
              f'{name}: name does not match directory')
        desc = re.search(r'^description:\s*(\S.+)$', header.group(1), re.M)
        check(desc is not None and len(desc.group(1)) >= 40, f'{name}: missing discovery description')
        check('disable-model-invocation' not in header.group(1), f'{name}: not auto-discoverable')
        check(len(content[header.end():].strip()) > 250, f'{name}: thin skill body')
        check(next(r for r in manifest['skills'] if r['name'] == name)['description'] == desc.group(1),
              f'{name}: manifest description differs')
        for f in path.parent.rglob('*'):
            check(not f.is_symlink(), f'Symlink in skill folder: {f}')

    ux_prefix = 'knowledge/ux-laws/'
    principles = load(ux_prefix + 'principles.json')['principles']
    articles = load(ux_prefix + 'articles.json')['articles']
    classes = load(ux_prefix + 'issue_taxonomy.json')['categories']
    recipes = load(ux_prefix + 'remediation-recipes.json')['recipes']
    conflicts = load(ux_prefix + 'cross-law-conflicts.json')['pairs']
    law_ids = {p['id'] for p in principles}
    article_ids = {a['id'] for a in articles}
    class_ids = {c['id'] for c in classes}
    check(len(law_ids) == len(principles) == 30, 'Incomplete Laws of UX inventory')
    check(len(article_ids) == len(articles) == 8, 'Incomplete article inventory')
    check(len(class_ids) == len(classes) == 10, 'Incomplete UX taxonomy')
    check(len(recipes) == 30 and {r['category'] for r in recipes} == class_ids, 'Incomplete UX recipes')
    check(len(conflicts) >= 13, 'Missing UX conflict rules')
    check({c['skill'] for c in classes} | {'ux-diagnose','ux-review','ux-build','ux-validate'} == ux_names,
          'UX taxonomy has missing specialist')
    check(set().union(*(set(c['principle_ids']) for c in classes)) == law_ids, 'Some laws unclassified')
    for p in principles:
        check(p['primary_class'] in class_ids and set(p['related_classes']) <= class_ids,
              f"{p['id']}: invalid category")
        check(set(p['article_ids']) <= article_ids, f"{p['id']}: missing article")
        check(len(p['interventions']) >= 3 and p['source'].startswith('https://lawsofux.com/'),
              f"{p['id']}: inadequate synthesis")
    for r in recipes:
        check(set(r['principles']) <= law_ids and all(r.get(k) for k in ('implementation','acceptance_test','failure_modes')),
              f"{r['id']}: incomplete recipe")
    for pair in conflicts:
        check(set(pair['principles']) <= law_ids, f"Invalid UX conflict: {pair.get('tension','unknown')}")

    wcag_prefix = 'knowledge/wcag21/'
    criteria = load(wcag_prefix + 'criteria.json')['criteria']
    wcag_classes = load(wcag_prefix + 'issue_taxonomy.json')['categories']
    wcag_recipes = load(wcag_prefix + 'remediation_recipes.json')['recipes']
    wcag_conflicts = load(wcag_prefix + 'cross_criterion_conflicts.json')['pairs']
    conformance = load(wcag_prefix + 'conformance.json')
    ids = {c['id'] for c in criteria}
    wcag_class_ids = {c['id'] for c in wcag_classes}
    check(len(criteria) == len(ids) == 78, 'Missing or duplicate WCAG 2.1 success criteria')
    check(Counter(c['level'] for c in criteria) == Counter({'A':30,'AA':20,'AAA':28}), 'Incorrect WCAG levels')
    check(len({c['guideline_id'] for c in criteria}) == 13, 'Incorrect WCAG guideline count')
    check({c['principle'] for c in criteria} == {'Perceivable','Operable','Understandable','Robust'}, 'Missing POUR')
    check(len(wcag_class_ids) == len(wcag_classes) == 10, 'Missing WCAG specialist taxonomy')
    check(len(conformance['five_requirements']) == 5, 'Missing conformance requirements')
    check(conformance['levels']['AA']['criterion_count'] == 50, 'WCAG AA should include A+AA')
    check(len(wcag_recipes) == 31 and len(wcag_conflicts) >= 18, 'WCAG remediation coverage deficient')
    check({c['skill'] for c in wcag_classes} | {'wcag21-diagnose','wcag21-review','wcag21-build','wcag21-validate'} == wcag_names,
          'WCAG taxonomy specialists mismatch')
    check(set().union(*(set(c['primary_criteria']) for c in wcag_classes)) == ids,
          'WCAG primary classifications incomplete')
    for c in criteria:
        check(c['primary_category'] in wcag_class_ids and set(c['secondary_categories']) <= wcag_class_ids,
              f"{c['id']}: invalid WCAG class")
        check(c['normative_source'].startswith('https://www.w3.org/TR/WCAG21/#')
              and c['informative_understanding'].startswith('https://www.w3.org/WAI/WCAG21/Understanding/'),
              f"{c['id']}: missing authoritative links")
        check(all(len(c[k]) >= 25 for k in ('symptom', 'remediation','verification','exceptions_and_pitfalls')),
              f"{c['id']}: incomplete operational guidance")
    for r in wcag_recipes:
        check(set(r['criteria']) <= ids and set(r['categories']) <= wcag_class_ids,
              f"{r['id']}: invalid WCAG recipe refs")
    for pair in wcag_conflicts:
        check(set(pair['criteria']) <= ids, f"{pair['id']}: invalid WCAG conflict refs")
    for slug,diagnose in [('ux-laws','ux-diagnose'),('wcag21','wcag21-diagnose')]:
        knowledge = ROOT / 'knowledge' / slug
        for item in knowledge.iterdir():
            if item.is_file():
                copied = ROOT / 'skills' / diagnose / 'references' / item.name
                check(copied.is_file() and copied.read_bytes() == item.read_bytes(),
                      f'{slug}: installed reference differs from source {item.name}')
    ux_cases = load('evaluation/ux-laws/classification_cases.json')['cases']
    wcag_cases = load('evaluation/wcag21/classification_cases.json')['cases']
    ux_invoke = load('evaluation/ux-laws/invocation_cases.json')['positive']
    wcag_invoke = load('evaluation/wcag21/invocation_cases.json')['positive']
    check(len(ux_cases) >= 20 and len(wcag_cases) >= 40, 'Classification corpus incomplete')
    check({c['expected_skill'] for c in ux_invoke} == ux_names, 'UX invocation coverage incomplete')
    check({c['expected_skill'] for c in wcag_invoke} == wcag_names, 'WCAG invocation coverage incomplete')
    check((ROOT/'integration/AGENTS.fragment.md').is_file(), 'Missing combined routing fragment')
    check((ROOT/'NOTICE.md').is_file(), 'Missing third-party notice')
    index = ROOT / 'MANIFEST.sha256'
    if index.exists():
        actual = {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in ROOT.rglob('*') if p.is_file() and p != index
                  and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.pyo')}
        expected = {}
        for line in index.read_text(encoding='utf-8').splitlines():
            digest, name = line.split('  ', 1)
            check(name not in expected, f'Duplicate SHA manifest entry: {name}')
            expected[name] = digest
        check(all(actual.get(name) == digest for name, digest in expected.items()),
              'SHA-256 manifest does not match release files')
    print(f'PASS: {len(names)} skills (14+14), 30 laws, 8 articles, 78 WCAG criteria (30 A/20 AA/28 AAA), '
          f'{len(recipes) + len(wcag_recipes)} recipes, {len(conflicts) + len(wcag_conflicts)} conflict rules, '
          f'{len(ux_cases) + len(wcag_cases)} classification cases, {len(ux_invoke) + len(wcag_invoke)} invocation prompts.')
    print('NOTE: Structural checks only; not a live agent invocation, browser test or WCAG conformance certificate.')


if __name__ == '__main__':
    main()
