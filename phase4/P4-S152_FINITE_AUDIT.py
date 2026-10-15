#!/usr/bin/env python3
"""P4-S152 independent-in-method finite sanity only; symbolic proof is in MATHEMATICS."""
from collections import Counter
from itertools import combinations
from random import Random

def completions(f,n):
    u=len(f).bit_length()-1
    assert len(f)==2**u and u>=n+1
    groups=[[s for s in range(2**u) if f[s]==t] for t in range(2**n)]
    assert all(len(g)==2**(u-n) for g in groups)
    h=[None]*(2**u); k=h.copy()
    for t,g in enumerate(groups):
        for j,s in enumerate(g):
            h[s]=t*2**(u-n)+j
            k[s]=t*2**(u-n-1)+j//2
    return h,k

def check(f,n):
    u=len(f).bit_length()-1
    h,k=completions(f,n)
    assert sorted(h)==list(range(2**u))
    assert Counter(k)==Counter({j:2 for j in range(2**(u-1))})
    for s in range(2**u):
        assert h[s]//2**(u-n)==f[s]
        assert k[s]//2**(u-n-1)==f[s]
    for outputblock,blocklength in ((h,u),(k,u-1)):
        L=u+3
        for m in range(1,u+3):
            counts=Counter()
            for x in range(2**L):
                s=x//2**(L-u); z=x%2**(L-u)
                y=outputblock[s]*2**(L-u)+z
                counts[y//2**(blocklength+L-u-m)]+=1
            assert len(counts)==2**m and set(counts.values())=={2**(L-m)}

count=0
for ones in combinations(range(8),4):
    check([int(i in ones) for i in range(8)],1);count+=1
rng=Random(152)
for _ in range(256):
    f=[t for t in range(4) for _ in range(4)]
    rng.shuffle(f);check(f,2);count+=1
print('PASS',count,'balanced finite tables, both completions, prefixes, multiplicities and output cylinders')
