#!/usr/bin/env python3
"""P4-S154 exact finite-block SANITY only; never an infinite proof."""
from itertools import combinations
from fractions import Fraction
from collections import Counter

tables=0
fair_assertions=0
fibre_assertions=0
counts=Counter()
for a in combinations(range(8),2):
    remaining1=set(range(8))-set(a)
    for b in combinations(sorted(remaining1),2):
        remaining2=remaining1-set(b)
        for c in combinations(sorted(remaining2),2):
            f=[3]*8
            for tag,group in enumerate((a,b,c)):
                for v in group: f[v]=tag
            tables+=1
            assert all(f.count(tag)==2 for tag in range(4))
            # Map T_f(vz)=f(v)z: prefix cylinder counts at every m.
            for m in range(1,8):
                for tau in range(2**m):
                    if m<=2:
                        ct=sum(1 for v in range(8) if f[v]>>(2-m)==tau)
                        assert Fraction(ct,8)==Fraction(1,2**m)
                    else:
                        ct=f.count(tau>>(m-2))
                        assert Fraction(ct,2**(m+1))==Fraction(1,2**m)
                    fair_assertions+=1
            # Full y has two preimages v z, for each fixed output tag and tail z.
            for tag in range(4):
                assert sum(f[v]==tag for v in range(8))==2
                fibre_assertions+=1
            for n in range(4):
                for s in range(2**n):
                    tags=[f[v] for v in range(8) if v>>(3-n)==s]
                    key="injective" if len(tags)==len(set(tags)) else "colliding"
                    counts[n,key]+=1
assert (tables,fair_assertions,fibre_assertions)==(2520,640080,10080)
assert [(counts[n,"injective"],counts[n,"colliding"]) for n in range(4)]==[(0,2520),(1152,3888),(8640,1440),(20160,0)]
print("PASS: tables",tables,"fair",fair_assertions,"fibres",fibre_assertions)
for n in range(4): print(n,counts[n,"injective"],counts[n,"colliding"])
