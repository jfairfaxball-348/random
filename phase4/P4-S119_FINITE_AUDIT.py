#!/usr/bin/env python3
"""Exact finite sanity only (NOT infinite fibre, randomness or formal proof)."""
from itertools import product
def pi(a,i):
    if a==0:return i+1 if i%2==0 else i-1
    if i==0:return 0
    return i+1 if i%2 else i-1
def out(a,u,m):return tuple(u[pi(a,i)] for i in range(m))
n=0
for m in range(1,10):
    cells={t:[] for t in product((0,1),repeat=m)}
    for a in (0,1):
        for u in product((0,1),repeat=m+1):
            cells[out(a,u,m)].append((a,u));n+=1
    for y,rows in cells.items():
        assert len(rows)==4 and sum(a==0 for a,u in rows)==2;n+=1
        for a in (0,1):
            v=[u for aa,u in rows if aa==a];assert len(v)==2
            forms=[tuple(out(a,u+(b,),m+1)[-1] for b in (0,1)) for u in v]
            assert [sum(out(a,u+(b,),m+1)[-1]==j for u in v for b in (0,1)) for j in (0,1)]==[2,2]
            assert sorted(forms)==([(0,1),(0,1)] if pi(a,m)==m+1 else [(0,0),(1,1)])
            n+=4
# Finite artificial halting schedule, NOT actual undecidable K.
halts={0:3,2:8}
def marker(t):
    for e in range(5):
        c=(0,)*(2*e+1)+(1,)
        if len(t)>=len(c) and tuple(t[:len(c)])==c:return e
    return None
def release(a,u,m):
    o=[];cur=0;flag=False
    for stage in range(m):
        e=marker(o) if not flag else None
        if e is not None and e in halts and stage>=halts[e]:
            o.append(a);flag=True
        else:o.append(u[cur]);cur+=1
    return tuple(o)
for m in range(1,11):
    cells={t:[] for t in product((0,1),repeat=m)}
    for a in (0,1):
        for u in product((0,1),repeat=m):
            cells[release(a,u,m)].append((a,u));n+=1
    for y,rows in cells.items():
        assert len(rows)==2
        assert sum(a==0 for a,u in rows) in (0,1,2)
        n+=2
    if m==10:
        changed=sum(sum(a==0 for a,u in rows)!=1 for rows in cells.values())
        assert changed==2**m*17//64;n+=1
assert n==21471,n
print("P4-S119 finite exact assertions: 21,471 PASS (sanity only)")
