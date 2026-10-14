#!/usr/bin/env python3
"""P4-S132 exact finite SANITY, not proof of infinite fibres or universal randomness."""
from fractions import Fraction
from itertools import product
from collections import Counter

P={"000":("A","0"),"001":("A","10"),"010":("A","11"),
   "011":("B","1"),"100":("B","00"),"101":("B","01"),
   "110":("C","0"),"111":("C","1")}
def mass(sheet,tau):
    z=Fraction(0)
    for s,(sh,p) in P.items():
        if sh!=sheet: continue
        if tau.startswith(p): z+=Fraction(1,8)*Fraction(1,2**(len(tau)-len(p)))
        elif p.startswith(tau): z+=Fraction(1,8)
    return z
original=0
for m in range(1,9):
    for t in product("01",repeat=m):
        tau="".join(t); v=Fraction(1,2**m)
        d={sh:mass(sh,tau)/v for sh in ("A","B","C")}
        assert sum(d.values())==1
        assert d["B" if tau[0]=="0" else "A"]==Fraction(1,2)
        original+=1

def f(s):
    sh,p=P[s[:3]]
    v=p+s[3:]
    assert len(v)>=2
    y=v[1]+v[0]+v[2:]  # K: swaps first two output bits
    selected="B" if y[1]=="0" else "A"
    return ("1" if sh==selected else "0")+y
factored=words=0
for m in range(1,8):
    n=m+4
    counts=Counter(f("".join(b))[:m] for b in product("01",repeat=n))
    assert len(counts)==2**m
    assert set(counts.values())=={2**(n-m)}
    factored+=len(counts);words+=2**n
rows={q:[(a,2*q-a) for a in (1,2,3) if 1<=2*q-a<=3]
      for q in (1,2,3)}
assert rows=={1:[(1,1)],2:[(1,3),(2,2),(3,1)],3:[(3,3)]}
print("PASS SANITY ONLY",original,factored,words,rows)
