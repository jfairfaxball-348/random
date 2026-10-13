#!/usr/bin/env python3
"""P4-S123 exact small-prefix SANITY, not an infinite proof or certification."""
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache

def A(bits,t):
    b=list(bits)
    if t is not None and t+1<len(b) and (t==0 or b[0]==1):
        b[t],b[t+1]=b[t+1],b[t]
    return tuple(b)

def B(bits,r):
    b=list(bits)
    if r is not None and r+2<len(b) and (r==0 or b[0]==1):
        b[r],b[r+1],b[r+2]=b[r+1],b[r+2],b[r]
    return tuple(b)

def d(bits):
    z=Q(1)
    for j,bit in enumerate(bits):
        z*=Q(3,2) if bit==j%2 else Q(1,2)
    return z

@lru_cache(None)
def chart(s,t,r):
    n=len(s)
    N=max(n+5,t+3 if t is not None else 0,r+4 if r is not None else 0)
    z=Q(0)
    for v in product((0,1),repeat=N-n):
        y=B(A(s+v,t),r)
        z+=d(y)
    return z/2**(N-n)

@lru_cache(None)
def mixture(s):
    n=len(s);T=n+4
    w=[(t,Q(1,2**(t+2))) for t in range(T)]
    w.append((None,Q(1,2)+Q(1,2**(T+1))))
    assert sum((p for _,p in w),Q(0))==1
    return sum((p*q*chart(s,t,r) for t,p in w for r,q in w),Q(0))

def release_at(y):
    for t in range(len(y)):
        if t>=2 and tuple(y[t-2:t])==(0,1):
            return t
    return None

def inverse_candidate(a,y):
    t=release_at(y)
    return (a,)+(tuple(y) if t is None else tuple(y[:t])+(0,)+tuple(y[t+1:]))

def observed(x,m):
    a=x[0];u=x[1:];ptr=0;out=[];released=False;skip=False
    for j in range(m):
        if not released and j>=2 and tuple(out[-2:])==(0,1):
            out.append(a);released=True;skip=True;continue
        if skip:
            ptr+=1;skip=False
        out.append(u[ptr]);ptr+=1
    return tuple(out)

def audit():
    count=0
    for n in range(4):
        for s in product((0,1),repeat=n):
            assert mixture(s)==(mixture(s+(0,))+mixture(s+(1,)))/2
            count+=1
    assert mixture(())==1
    assert A((1,0,1,0),1)==(1,1,0,0)
    assert A((1,1,0,0),1)==(1,0,1,0)
    candidates=0
    for m in range(1,9):
        for y in product((0,1),repeat=m):
            all_pre=[x for x in product((0,1),repeat=m+1) if observed(x,m)==y]
            assert len(all_pre)==2
            a0=inverse_candidate(0,y);a1=inverse_candidate(1,y)
            assert len(a0)==m+1 and len(a1)==m+1
            assert sum(observed(a,m)==y for a in (a0,a1))==(2 if release_at(y) is None else 1)
            candidates+=1
    print(f"PASS: {count} nonlinear two-clock martingale identities; {candidates} inverse/fibre checks; root=1")

if __name__=="__main__": audit()
