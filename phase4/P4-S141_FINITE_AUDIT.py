#!/usr/bin/env python3
"""Finite exact arithmetic sanity for B141 dense-pocket fair F2 example.
Does NOT verify infinite theorem or randomness preservation."""
from collections import Counter
from fractions import Fraction
from itertools import product

def words(n):
    return ("".join(z) for z in product("01", repeat=n))

def build_pockets(stages=14):
    chosen=[]
    j=0
    for size in range(stages):
        for sigma in words(size):
            if j>=stages:
                return chosen
            if any(sigma.startswith(p) for p in chosen):
                j+=1
                continue
            length=max(j+4,len(sigma)+1)
            def free(pref):
                if any(pref.startswith(p) for p in chosen):
                    return None
                if len(pref)==length:
                    return pref
                return free(pref+"0") or free(pref+"1")
            p=free(sigma)
            assert p is not None
            chosen.append(p)
            j+=1
    return chosen

def out_prefix(source, n, pockets):
    eligible=next((p for p in pockets if len(p)<n and source.startswith(p)), None)
    return (eligible+source[len(eligible)+1:])[:n] if eligible else source[:n]

P=build_pockets()
assert len(P)==14
assert all(not a.startswith(b) and not b.startswith(a) for i,a in enumerate(P) for b in P[i+1:])
mass=sum((Fraction(1,2**len(p)) for p in P),Fraction(0))
assert mass<=Fraction(1,8)
rows=incidences=0
for n in range(1,11):
    tally=Counter(out_prefix(x,n,P) for x in words(n+1))
    assert len(tally)==2**n and set(tally.values())=={2},(n,tally)
    rows+=len(tally)
    incidences+=sum(tally.values())
assert rows==2046 and incidences==4092
print("PASS_SANITY_ONLY",{"pockets":P, "pocket_mass":str(mass),
    "max_level":10,"output_rows":rows,"source_incidences":incidences})
