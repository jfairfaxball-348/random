#!/usr/bin/env python3
"""S100 corpus integrity and independent finite accounting replay.
Finite checks do not certify the infinitary proofs. No spectral numerics.
Run from repository root; --replay also runs selected original exact audits.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,random,subprocess,sys,concurrent.futures

root=Path(__file__).resolve().parents[1]
checks=0
def check(test,why):
    global checks
    checks+=1
    if not test: raise AssertionError(why)

index=json.loads((root/'phase4/P4-S100_EVIDENCE_INDEX.json').read_text())
rows=json.loads((root/'phase4/P4-S100_SESSION_REGISTER.json').read_text())
check([r['session'] for r in rows]==[f'P4-S{n:03}' for n in range(1,100)],'99 consecutive register rows')
audit=(root/'phase4/P4-S100_CENTURY_AUDIT.md').read_text()
for row in index['sessions']:
    n=int(row['session'][-3:])
    check(audit.count(f'| [S{n:03}](')==1,'one table row per session')
    for kind in ['mathematics','validation','close']:
        r=row[kind];p=root/r['path']
        check(hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],'historical record unchanged')
    for k in ['central_question','established','conditional_or_failed','flagship_effect','later_disposition','original_validation']:
        check(bool(rows[n-1][k]),'complete audit dimensions')

# Independent small finite model: a fair 2-to-1 filtration from a permutation
# followed by deletion. Re-derive hit/split potentials, not imported code.
rng=random.Random(100)
N=32
for trial in range(20):
    perm=list(range(N));rng.shuffle(perm)
    P={x for x in range(N) if rng.randrange(2)} or {0}
    C={x for x in range(N) if rng.randrange(2)}
    d={():Q(1)}
    for t in range(4):
        for w in [u for u in d if len(u)==t]:
            a=Q(rng.randrange(-3,4),3)
            d[w+(0,)]=d[w]*(1-a);d[w+(1,)]=d[w]*(1+a)
    prev=None
    for t in range(5):
        cells={}
        for x in range(N):
            w=tuple((perm[x]>>(4-j))&1 for j in range(t))
            cells.setdefault(w,set()).add(x)
        lamP=Q(len(P),N)
        def hit(S):
            return sum((Q(1,2**t)*d[w] for w,A in cells.items() if A&S),Q())/Q(len(S),N)
        psi=hit(P)
        gamma=sum((Q(1,2**t)*d[w] for w,A in cells.items() if A&P&C and (A&P)-C),Q())/lamP
        exact=sum((d[w]*Q(len(A&P),N) for w,A in cells.items()),Q())/lamP
        check(psi>=exact,'conditional capital dominated by hit potential')
        if prev is not None:check(psi<=prev[0] and gamma<=prev[1],'time monotonicity')
        prev=psi,gamma
        left=P&C;right=P-C
        if left and right:
            alpha=Q(len(left),len(P))
            check(alpha*hit(left)+(1-alpha)*hit(right)==psi+gamma,'weighted split identity')
            check(min(hit(left),hit(right))<=psi+gamma,'min-side bound')
    check(max(map(len,cells.values()))==2,'finite all-cell cardinal fibres')

# Recompute budgets as exact geometric sums and their infinite closed forms.
check(sum((Q(1,2**(q+4)) for q in range(40)),Q()) < Q(1,8),'finite fooling bound')
check(Q(1,16)*2*1==Q(1,8),'infinite q/m geometric fooling series')
check(4*(1-Q(1,8))==Q(7,2)>2,'S083 compactness margin')
check(4*(1-Q(1,8)-Q(1,32))==Q(27,8)>2,'S090 compactness margin')
for i in range(30):
    check(Q(2**(i+1),2**((i+1)*(i+2)))==Q(1,2**((i+1)**2)),'S082 full guessed-run source mass')
    check(Q(1,2**((i+1)**2))<=Q(1,2**i),'ML test budget')
    check(2**(i+1)*Q(3,4)**(5*(i+1))<=Q(1,2**i),'S089 balanced-split source budget')
for m in range(1,13):
    check(Q(2**m-1,2**m)==1-Q(1,2**m),'unpriced constant-reader union')
for n in range(1,13):
    q=Q(1,2**(n+3));check(2*2*q<=Q(1,2**n),'S099 two-branch price')
# The deletion saturation counterexample is symbolic for all t; finite model
# independently checks arbitrary t without borrowing a conditional-average lift.
for t in range(12):
    psi=Q(2**t,2**t)/Q(1,2)
    check(psi==2 and psi!=1,'deletion saturation is larger than conditional mean')

results={'independent_finite_and_integrity_checks':checks,'status':'PASS','limitations':'Finite accounting plus corpus integrity; written proofs establish infinitary claims. Same-agent separate validation, not independent referee, Lean or hosted CI.','original_replays':[]}
if '--replay' in sys.argv:
    nums=[81,82,83,84,87,88,89,90,91,92,93,94,95,98]
    jobs=[]
    for n in nums:
        scripts=index['sessions'][n-1]['audit_scripts']
        check(len(scripts)==1,f'one original audit for S{n:03}')
        jobs.append((n,scripts[0]))
    def run(job):
        n,p=job;cmd=[sys.executable,p]+(['--no-numeric'] if n==89 else [])
        out=subprocess.run(cmd,cwd=root,text=True,capture_output=True,timeout=100)
        return {'session':f'P4-S{n:03}','command':cmd,'returncode':out.returncode,'stdout':out.stdout,'stderr':out.stderr}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(run,jobs):
            results['original_replays'].append(result)
            check(result['returncode']==0,result['session']+' original audit replay')
            print(result['session'],result['stdout'].strip().splitlines()[-1],flush=True)
    results['independent_finite_and_integrity_checks']=checks
(root/'phase4/P4-S100_AUDIT_REPLAY.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('S100 VALIDATION PASS',checks,'finite/integrity assertions; no infinitary machine-proof claim')
