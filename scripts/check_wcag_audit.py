#!/usr/bin/env python3
"""Inspect structured WCAG 2.1 audit coverage; NEVER certifies WCAG conformance.

Example: python scripts/check_wcag_audit.py evaluation/wcag21/sample-audit.json --json
"""
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAT = {x['id']: x for x in json.loads((ROOT/'knowledge/wcag21/criteria.json').read_text(encoding='utf-8'))['criteria']}
REQUIREMENTS = {f'5.2.{i}' for i in range(1, 6)}
STATUSES = {'pass', 'fail', 'not_applicable', 'not_tested', 'needs_manual_review'}


def check(report):
    errors = []
    def require(cond, msg):
        if not cond: errors.append(msg)

    require(report.get('standard') == 'WCAG 2.1', 'standard must equal WCAG 2.1')
    level = report.get('target_level')
    require(level in ('A','AA','AAA'), 'target_level must be A, AA, or AAA')
    levels = {'A': {'A'}, 'AA': {'A','AA'}, 'AAA': {'A','AA','AAA'}}
    expected = {cid for cid, criterion in CAT.items() if criterion['level'] in levels.get(level,set())}
    scope = report.get('scope')
    require(isinstance(scope,dict), 'scope must be an object')
    scope = scope if isinstance(scope,dict) else {}
    require(isinstance(scope.get('pages'),list) and bool(scope.get('pages')), 'scope.pages needs one or more explicit pages/route patterns')
    require(isinstance(scope.get('processes'),list), 'scope.processes must be a list (empty if no process)')
    require(isinstance(scope.get('browser_at_matrix'),list), 'scope.browser_at_matrix must be a list (can be empty before testing)')
    require(isinstance(report.get('criteria'),list), 'criteria must be a list')
    criteria = report.get('criteria') if isinstance(report.get('criteria'),list) else []
    outcomes = {}
    for i, item in enumerate(criteria):
        require(isinstance(item,dict),f'criteria[{i}] must be object')
        if not isinstance(item,dict):continue
        cid=item.get('id')
        require(cid in CAT,f'criteria[{i}] unknown criterion ID {cid!r}')
        if cid not in CAT:continue
        require(cid in expected,f'criteria[{i}] {cid} beyond target level {level}')
        require(cid not in outcomes,f'duplicate criterion {cid}')
        if cid in outcomes:continue
        outcomes[cid]=item
        status=item.get('status')
        require(status in STATUSES,f'{cid}: invalid status {status!r}')
        evidence=item.get('evidence',[])
        require(isinstance(evidence,list) and all(isinstance(e,str) and e.strip() for e in evidence),f'{cid}: evidence must be list of nonempty strings')
        if status in ('pass','fail'):
            require(isinstance(evidence,list) and len(evidence)>0,f'{cid}: {status} requires concrete evidence')
            require(isinstance(item.get('methods'),list) and bool(item.get('methods')),f'{cid}: {status} requires test methods')
        if status=='not_applicable':
            require(isinstance(item.get('applicability_reason'),str) and len(item['applicability_reason'].strip())>=10,f'{cid}: N/A requires specific applicability_reason')
            require(isinstance(evidence,list) and bool(evidence),f'{cid}: N/A requires recorded evidence')
    missing=sorted(expected - outcomes.keys(), key=lambda s:tuple(map(int,s.split('.'))))
    if missing:errors.append(f'{len(missing)} expected criteria missing: '+', '.join(missing))
    reviews=report.get('conformance_reviews')
    require(isinstance(reviews,dict), 'conformance_reviews must be an object')
    reviews=reviews if isinstance(reviews,dict) else {}
    for req in sorted(REQUIREMENTS):
        review=reviews.get(req)
        require(isinstance(review,dict),f'{req} conformance review missing')
        if isinstance(review,dict):
            require(review.get('status') in ('complete','incomplete','not_tested'),f'{req} review needs complete/incomplete/not_tested status')
            if review.get('status')=='complete':
                require(isinstance(review.get('evidence'),list) and bool(review['evidence']) and all(isinstance(e,str) and e.strip() for e in review['evidence']),f'{req} completed review requires evidence')
    counts=Counter(x.get('status') for x in outcomes.values())
    complete_outcomes=all(outcomes.get(cid,{}).get('status') in ('pass','fail','not_applicable') for cid in expected)
    all_favorable=all(outcomes.get(cid,{}).get('status') in ('pass','not_applicable') for cid in expected)
    all_reviews=all(isinstance(reviews.get(r),dict) and reviews[r].get('status')=='complete' for r in REQUIREMENTS)
    ready=not errors and all_favorable and all_reviews
    return {'standard':'WCAG 2.1','target_level':level,'expected_criteria':len(expected),'recorded_criteria':len(outcomes),
      'status_counts':{k:counts.get(k,0) for k in ('pass','fail','not_applicable','not_tested','needs_manual_review')},
      'coverage_complete':not missing and complete_outcomes and not errors,
      'ready_for_independent_human_conformance_review':ready,
      'conformance_certified':False,
      'note':'This checks report structure and evidence presence only. It does NOT verify real-world findings, whole-page and complete-process coverage, AT support, legal compliance, or conformance.',
      'errors':errors}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('audit',type=Path)
    p.add_argument('--json',action='store_true',help='Print machine-readable summary')
    args=p.parse_args()
    try:report=json.loads(args.audit.read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as e:p.error(str(e))
    if not isinstance(report,dict):p.error('Audit root must be an object')
    result=check(report)
    if args.json:print(json.dumps(result,indent=2))
    else:
        print('WCAG 2.1 coverage:',result['recorded_criteria'],'/',result['expected_criteria'],
             'criteria; statuses:',result['status_counts'])
        for e in result['errors']:print('INVALID:',e)
        if not result['errors']:
            print('Ready for independent HUMAN conformance review:',result['ready_for_independent_human_conformance_review'])
        print('Never a certificate of WCAG conformance.')
    return 2 if result['errors'] else 0


if __name__ == '__main__':raise SystemExit(main())
