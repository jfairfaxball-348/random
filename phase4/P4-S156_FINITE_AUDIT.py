#!/usr/bin/env python3
"""Finite exact sanity for S156 only; NOT an infinite proof or cap-three test."""
from fractions import Fraction as Q
from itertools import product

def words(n):
    return ("".join(z) for z in product("01", repeat=n))

def q(s, t):
    # G(x)=shift^2(x): four complete inverse streams.
    n=max(len(s), len(t)+2)
    return Q(sum(a.startswith(s) and a[2:2+len(t)]==t for a in words(n))*2**len(t),2**n)

def p(t):
    return Q(1) if not t else (Q(3,2) if t[0]=="0" else Q(1,2))

def mu(t):
    return p(t)/2**len(t)

def eta(s):
    return sum((q(s,t)*mu(t) for t in words(len(s))),Q(0))

stable=projective=domination=0
for n in range(6):
    for s in words(n):
        for m in range(n,n+2):
            for t in words(m):
                for b in "01":
                    assert q(s,t)==q(s,t+b)
                    stable+=1
        assert eta(s)==eta(s+"0")+eta(s+"1")
        projective+=1
for n in range(3,7):
    for s in words(n):
        # Any extension with two fresh input bits yields the displayed n-output prefix.
        y=(s+"00")[2:2+n]
        assert (2**n)*eta(s)>=Q(1,4)*p(y)
        domination+=1
assert (stable,projective,domination)==(8190,63,120)
print("PASS finite SANITY only:",stable,projective,domination)
