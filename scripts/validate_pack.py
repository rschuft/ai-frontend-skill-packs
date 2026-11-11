#!/usr/bin/env python3
"""Validate the combined skill pack structure, YAML, catalogs and routing metadata."""
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


def validate_skill_markdown(content: str, skill_name: str) -> str:
    """Validate the deliberately restricted, YAML-compatible skill frontmatter.

    JSON strings are valid YAML scalars. Requiring double-quoted descriptions
    avoids GitHub parsing failures from unquoted `: ` and similar characters
    without introducing a YAML parser dependency into the distributed pack.
    """
    check('\r' not in content, f'{skill_name}: SKILL.md must use LF line endings')
    header = re.match(r'\A---\n([^\n]+)\n([^\n]+)\n---\n', content)
    check(header is not None, f'{skill_name}: expected two-field YAML frontmatter')
    name_field, desc_field = header.group(1), header.group(2)
    check(name_field == f'name: {skill_name}', f'{skill_name}: frontmatter name must match directory')
    check(desc_field.startswith('description: "'), f'{skill_name}: description must be double-quoted')
    raw_description = desc_field[len('description: '):]
    try:
        description = json.loads(raw_description)
    except (ValueError, TypeError) as exc:
        raise AssertionError(f'{skill_name}: invalid quoted description: {exc}') from exc
    check(isinstance(description, str) and len(description.strip()) >= 40,
          f'{skill_name}: missing or short discovery description')
    check('disable-model-invocation' not in header.group(0), f'{skill_name}: not auto-discoverable')
    body = content[header.end():]
    check(re.match(r'\n# [^\n]+\n\n## Scope\n\n', body) is not None,
          f'{skill_name}: expected title followed by ## Scope')
    headings = re.findall(r'^## (.+)$', body, re.M)
    check(headings.count('Scope') == 1 and headings.count('Procedure') == 1,
          f'{skill_name}: require one Scope and one Procedure section')
    check(headings[0] == 'Scope' and headings[1] == 'Procedure',
          f'{skill_name}: Scope must precede Procedure')
    check(len(re.findall(r'^# ', body, re.M)) == 1,
          f'{skill_name}: SKILL.md must have exactly one H1')
    check(not any(h in headings for h in ('When to load', 'First-pass remediation inventory',
                                         'Process', 'Implementation workflow')),
          f'{skill_name}: use the canonical headings')
    check(len(body.strip()) > 250, f'{skill_name}: thin skill body')
    return description


def validate_security_catalog(root: Path, manifest: dict, security_names: set[str]) -> None:
    """Check completeness of ASVS metadata, cross-family links and test fixtures."""
    def data(rel):
        return json.loads((root / 'knowledge/security' / rel).read_text(encoding='utf-8'))
    index = data('asvs/5.0.0/index.json')
    requirements = index['requirements']
    ids = [r['id'] for r in requirements]
    check(len(requirements) == len(set(ids)) == 345, 'Security ASVS index incomplete or duplicated')
    check(len(index['chapters']) == 17 and {r['chapter'] for r in requirements} == {c['id'] for c in index['chapters']},
          'Security ASVS chapter coverage mismatch')
    check(all(re.fullmatch(r'v5\.0\.0-[0-9]+\.[0-9]+\.[0-9]+', r['id']) and
              r['id'] == 'v5.0.0-' + r['asvs_id'][1:] and r['level'] in (1, 2, 3)
              for r in requirements), 'Malformed ASVS 5.0.0 requirement index')
    check([sum(r['level'] <= n for r in requirements) for n in (1, 2, 3)] == [70, 253, 345],
          'ASVS level distribution differs from stable 5.0.0 source')
    check(all(c['requirement_count'] == sum(r['chapter'] == c['id'] for r in requirements)
              for c in index['chapters']), 'Security ASVS chapter counts incorrect')
    check(manifest['packs']['security']['skill_count'] == 14 and
          manifest['packs']['security']['requirement_index_count'] == 345,
          'Security pack manifest metadata mismatch')
    cats = data('issue_taxonomy.json')['categories']
    check(len(cats) == 10 and {c['skill'] for c in cats} |
          {'security-diagnose', 'security-review', 'security-build', 'security-validate'} == security_names,
          'Security taxonomy must cover all specialist skills')
    recipes = data('remediation_recipes.json')['recipes']
    check(len(recipes) == 40 and {r['category'] for r in recipes} == {c['id'] for c in cats} and
          all(r.get('implementation') and r.get('acceptance_test') and r.get('failure_modes') for r in recipes),
          'Security remediation recipes incomplete')
    top = data('top10-2025.json')['categories']
    check(len(top) == 10 and {x['id'] for x in top} == {f'A{i:02d}:2025' for i in range(1, 11)} and
          all(set(x['skills']) <= security_names for x in top), 'OWASP Top 10:2025 map invalid')
    nist = data('nist-ssdf-mapping.json')['practice_groups']
    check({p['id'] for p in nist} == {'PO', 'PS', 'PW', 'RV'} and
          all(set(p['skills']) <= security_names for p in nist), 'NIST SSDF mapping invalid')
    specmap = data('specialist_map.json')['categories']
    check({x['skill'] for x in specmap} == security_names -
          {'security-diagnose', 'security-review', 'security-build', 'security-validate'},
          'Security specialist mapping incomplete')
    check(set().union(*(set(c['chapters']) for c in cats)) == {c['id'] for c in index['chapters']},
          'Some ASVS chapters have no security specialist')
    for p in (root / 'knowledge/security').rglob('*'):
        if p.is_file():
            copy = root / 'skills/security-diagnose/references' / p.relative_to(root / 'knowledge/security')
            check(copy.is_file() and copy.read_bytes() == p.read_bytes(),
                  f'Security installed references differ from {p.relative_to(root)}')
    inv = json.loads((root/'evaluation/security/invocation_cases.json').read_text(encoding='utf-8'))
    check({x['expected_skill'] for x in inv['positive']} == security_names,
          'Security skill activation test fixtures incomplete')
    cases = json.loads((root/'evaluation/security/classification_cases.json').read_text(encoding='utf-8'))['cases']
    check(len(cases) >= 40 and {c['expected_skill'] for c in cases} ==
          {c['skill'] for c in cats}, 'Security classification fixtures incomplete')


def main():
    manifest = load('manifest.json')
    skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
    names = {p.parent.name for p in skills}
    ux_names = {name for name in names if name.startswith('ux-')}
    wcag_names = {name for name in names if name.startswith('wcag-')}
    design_names = {name for name in names if name.startswith('design-')}
    security_names = {name for name in names if name.startswith('security-')}
    check(len(skills) == len(names) == 56, 'Need 56 unique skill directories')
    check(not list((ROOT/'skills').glob('wcag21-*')), 'Legacy WCAG skill directories must not exist')
    check(not (ROOT/'knowledge/wcag21').exists() and not (ROOT/'evaluation/wcag21').exists(), 'Legacy WCAG knowledge/evaluation directories must not exist')
    check(len(ux_names) == len(wcag_names) == len(design_names) == len(security_names) == 14, 'Pack skill counts must be 14 per family')
    check(manifest['skill_count'] == 56, 'Manifest skill count mismatch')
    check({r['name'] for r in manifest['skills']} == names, 'Manifest skill names out of sync')
    check(len(manifest['skills']) == 56, 'Duplicate manifest entries')
    for name in names:
        item = next(r for r in manifest['skills'] if r['name'] == name)
        check(item['path'] == f'skills/{name}/SKILL.md', f'{name}: wrong manifest path')
        check(item['pack'] == ('ux-laws' if name.startswith('ux-') else 'wcag' if name.startswith('wcag-') else 'visual-design' if name.startswith('design-') else 'security'), f'{name}: wrong pack')
    for path in skills:
        name = path.parent.name
        content = path.read_text(encoding='utf-8')
        description = validate_skill_markdown(content, name)
        check(next(r for r in manifest['skills'] if r['name'] == name)['description'] == description,
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

    wcag_prefix = 'knowledge/wcag/'
    criteria = load(wcag_prefix + '2.1/criteria.json')['criteria']
    criteria22 = load(wcag_prefix + '2.2/criteria.json')['criteria']
    standards = load(wcag_prefix + 'standards.json')
    wcag3 = load(wcag_prefix + '3.0/draft-guidance.json')
    wcag_classes = load(wcag_prefix + 'issue_taxonomy.json')['categories']
    wcag_recipes = load(wcag_prefix + 'remediation_recipes.json')['recipes']
    wcag_conflicts = load(wcag_prefix + 'cross_criterion_conflicts.json')['pairs']
    conformance = load(wcag_prefix + '2.1/conformance.json')
    conformance22 = load(wcag_prefix + '2.2/conformance.json')
    ids21 = {c['id'] for c in criteria}
    ids22 = {c['id'] for c in criteria22}
    all_wcag_ids = ids21 | ids22
    new_wcag_ids = ids22 - ids21
    wcag_class_ids = {c['id'] for c in wcag_classes}
    check(len(criteria) == len(ids21) == 78, 'Missing or duplicate WCAG 2.1 success criteria')
    check(Counter(c['level'] for c in criteria) == Counter({'A':30,'AA':20,'AAA':28}), 'Incorrect WCAG 2.1 levels')
    check(len(criteria22) == len(ids22) == 86, 'Missing or duplicate WCAG 2.2 success criteria')
    check(Counter(c['level'] for c in criteria22) == Counter({'A':31,'AA':24,'AAA':31}), 'Incorrect WCAG 2.2 levels')
    check(len(new_wcag_ids) == 9 and ids21 - ids22 == {'4.1.1'}, 'WCAG 2.2 delta must be nine new criteria minus 4.1.1')
    check({c['introduced_in'] for c in criteria22 if c['id'] in new_wcag_ids} == {'2.2'}, 'New criterion provenance wrong')
    check(len({c['guideline_id'] for c in criteria}) == len({c['guideline_id'] for c in criteria22}) == 13, 'WCAG guideline count')
    check({c['principle'] for c in criteria22} == {'Perceivable','Operable','Understandable','Robust'}, 'Missing POUR')
    check(len(wcag_class_ids) == len(wcag_classes) == 10, 'Missing WCAG taxonomy')
    check(len(conformance['five_requirements']) == len(conformance22['five_requirements']) == 5, 'Missing conformance requirements')
    check([conformance['levels'][l]['criterion_count'] for l in ('A','AA','AAA')] == [30,50,78], 'Invalid 2.1 cumulative counts')
    check([conformance22['levels'][l]['criterion_count'] for l in ('A','AA','AAA')] == [31,55,86], 'Invalid 2.2 cumulative counts')
    check(standards['default'] == {'standard':'WCAG 2.2','level':'AA'}, 'WCAG 2.2 AA must be planning default')
    check(standards['standards']['WCAG 3.0']['conformance_allowed'] is False
          and wcag3['publication_status'].startswith('W3C Working Draft'), 'WCAG 3.0 draft cannot be normative')
    check(len(wcag_recipes) >= 40 and len(wcag_conflicts) >= 26, 'Missing WCAG 2.2 remediation or conflicts')
    check({c['skill'] for c in wcag_classes} | {'wcag-diagnose','wcag-review','wcag-build','wcag-validate'} == wcag_names,
          'WCAG specialist taxonomy mismatch')
    check(set().union(*(set(c['primary_criteria']) for c in wcag_classes)) == all_wcag_ids,
          'WCAG union classifications incomplete')
    check(all(sum(cid in c['primary_criteria'] for c in wcag_classes) == 1 for cid in all_wcag_ids),
          'Each criterion must have exactly one primary category')
    for standard, cat in [('WCAG21',criteria),('WCAG22',criteria22)]:
        for c in cat:
            check(c['primary_category'] in wcag_class_ids and set(c['secondary_categories']) <= wcag_class_ids,
                  f"{c['id']}: invalid WCAG category")
            check(c['normative_source'].startswith(f'https://www.w3.org/TR/{standard}/#')
                  and c['informative_understanding'].startswith(f'https://www.w3.org/WAI/{standard}/Understanding/'),
                  f"{c['id']}: invalid {standard} authoritative links")
            check(all(len(c[k]) >= 25 for k in ('symptom','remediation','verification','exceptions_and_pitfalls')),
                  f"{c['id']}: incomplete operational guidance")
    for r in wcag_recipes:
        check(set(r['criteria']) <= all_wcag_ids and set(r['categories']) <= wcag_class_ids,
              f"{r['id']}: invalid WCAG recipe refs")
    check(new_wcag_ids <= {cid for r in wcag_recipes for cid in r['criteria']}, 'Missing WCAG 2.2 recipes')
    for pair in wcag_conflicts:
        check(set(pair['criteria']) <= all_wcag_ids, f"{pair['id']}: invalid WCAG conflicts")
    check((ROOT/'knowledge/wcag/standard-selection.md').is_file(), 'Missing version selection guidance')
    check(all((ROOT/'knowledge/wcag'/ver/name).is_file() for ver,name in [('2.1','criteria.json'),('2.1','criteria.csv'),('2.1','conformance.json'),('2.2','criteria.json'),('2.2','criteria.csv'),('2.2','conformance.json'),('3.0','draft-guidance.json')]), 'Missing version-specific WCAG reference')
    for ver, files in (('2.1', ('criteria.json', 'criteria.csv', 'conformance.json')),
                       ('2.2', ('criteria.json', 'criteria.csv', 'conformance.json')),
                       ('3.0', ('draft-guidance.json',))):
        for fname in files:
            source = ROOT / 'knowledge/wcag' / ver / fname
            bundled = ROOT / 'skills/wcag-diagnose/references' / ver / fname
            check(bundled.is_file() and source.read_bytes() == bundled.read_bytes(),
                  f'WCAG {ver}: bundled reference differs from {fname}')
    check((ROOT/'scripts/resolve_wcag_target.py').is_file(), 'Missing version resolver')
    check(manifest['version'] == '1.4.0', 'Incorrect semantic manifest version')
    check(manifest['packs']['wcag']['default_standard'] == 'WCAG 2.2', 'Manifest WCAG version mismatch')

    # Visual-design pack: seven principles/elements, curated article synthesis,
    # ten issue categories, 30 recipes, conflict guidance and offline routing cases.
    design_prefix = 'knowledge/visual-design/'
    dp = load(design_prefix + 'principles.json')['principles']
    de = load(design_prefix + 'elements.json')['elements']
    da = load(design_prefix + 'articles.json')['articles']
    dg = load(design_prefix + 'gestalt.json')['principles']
    dc = load(design_prefix + 'issue_taxonomy.json')['categories']
    dr = load(design_prefix + 'remediation_recipes.json')['recipes']
    dconf = load(design_prefix + 'cross_principle_conflicts.json')['conflicts']
    ids_design = {p['id'] for p in dp}
    article_ids = {a['id'] for a in da}
    class_ids_design = {c['id'] for c in dc}
    expected_principles = {'balance','contrast','emphasis','movement','pattern','proportion','unity'}
    expected_elements = {'line','shape','form','color','value','texture','space'}
    check(len(dp) == 7 and ids_design == expected_principles, 'Missing seven design principles')
    check(len(de) == 7 and {e['id'] for e in de} == expected_elements, 'Missing seven visual elements')
    check(len(dg) == 6 and len({g['id'] for g in dg}) == 6, 'Gestalt mapping incomplete')
    check(len(da) >= 20 and len(article_ids) == len(da), 'Supporting article map incomplete')
    check(len(dc) == 10 and len(class_ids_design) == 10, 'Incomplete visual issue taxonomy')
    check(len(dr) == 30 and len({r['id'] for r in dr}) == 30, 'Incomplete design repair recipes')
    check(len(dconf) >= 15, 'Missing cross-principle conflict checks')
    check({c['skill'] for c in dc} | {'design-diagnose','design-review','design-build','design-validate'} == design_names,
          'Design taxonomy specialists mismatch')
    check({p['primary_category'] for p in dp} <= class_ids_design, 'Invalid design category refs')
    check(all(set(p['article_ids']) <= article_ids and len(p['interventions']) >= 3 for p in dp),
          'Principle synthesis missing source/repair guidance')
    check({r['category'] for r in dr} == class_ids_design, 'Not all design categories have remediation recipes')
    check(all(r['skill'] in design_names and set(r['principles']) <= ids_design
              and all(r.get(k) for k in ('implementation','acceptance_test','failure_modes')) for r in dr),
          'Design recipes invalid or incomplete')
    check(all(a['url'].startswith('https://www.digitalpolo.com/') for a in da),
          'Invalid supporting article URL')
    check(all((ROOT / f'skills/{c["skill"]}/references/playbook.md').is_file() for c in dc),
          'Missing design specialist playbook')
    design_cases = load('evaluation/visual-design/classification_cases.json')['cases']
    design_inv = load('evaluation/visual-design/invocation_cases.json')['positive']
    check(len(design_cases) >= 40 and {c['expected_skill'] for c in design_cases} == {x['skill'] for x in dc},
          'Design classification examples incomplete')
    check({c['expected_skill'] for c in design_inv} == design_names, 'Design invocation prompts incomplete')

    for slug,diagnose in [('ux-laws','ux-diagnose'),('wcag','wcag-diagnose'),('visual-design','design-diagnose')]:
        knowledge = ROOT / 'knowledge' / slug
        for item in knowledge.iterdir():
            if item.is_file():
                copied = ROOT / 'skills' / diagnose / 'references' / item.name
                check(copied.is_file() and copied.read_bytes() == item.read_bytes(),
                      f'{slug}: installed reference differs from source {item.name}')
    ux_cases = load('evaluation/ux-laws/classification_cases.json')['cases']
    wcag_cases = load('evaluation/wcag/classification_cases.json')['cases']
    ux_invoke = load('evaluation/ux-laws/invocation_cases.json')['positive']
    wcag_invoke = load('evaluation/wcag/invocation_cases.json')['positive']
    check(len(ux_cases) >= 20 and len(wcag_cases) >= 49, 'Classification corpus incomplete')
    check(new_wcag_ids <= {c['supporting_criterion'] for c in wcag_cases}, 'Missing WCAG 2.2 classification scenarios')
    check(len(load('evaluation/wcag/version_routing_cases.json')['cases']) >= 7, 'Version-routing corpus incomplete')
    check({c['expected_skill'] for c in ux_invoke} == ux_names, 'UX invocation coverage incomplete')
    check({c['expected_skill'] for c in wcag_invoke} == wcag_names, 'WCAG invocation coverage incomplete')
    check((ROOT/'integration/AGENTS.fragment.md').is_file(), 'Missing combined routing fragment')
    check((ROOT/'NOTICE.md').is_file(), 'Missing third-party notice')
    check((ROOT/'CONTRIBUTING.md').is_file(), 'Missing contributing guide')
    validate_security_catalog(ROOT, manifest, security_names)
    print(f'PASS: {len(names)} skills (14 per family), 30 UX laws, 8 UX articles, WCAG 2.1 (78) + 2.2 (86) criteria, 7 design principles, 7 visual elements, {len(da)} design articles, '
          f'{len(recipes) + len(wcag_recipes) + len(dr)} UX/WCAG/design recipes and 40 security recipes, {len(conflicts) + len(wcag_conflicts) + len(dconf)} conflict rules, '
          f'{len(ux_cases) + len(wcag_cases) + len(design_cases)} UX/WCAG/design classification cases plus 40 security cases, {len(ux_invoke) + len(wcag_invoke) + len(design_inv)} existing plus 14 security invocation prompts.')
    print('NOTE: Structural/evidence-presence checks only; no live-agent, browser or penetration testing, WCAG certification or application security assurance.')


if __name__ == '__main__':
    main()
