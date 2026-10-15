#!/usr/bin/env python3
"""P4-S155 finite rational sanity; NOT certification of any infinite theorem."""
from itertools import product
from fractions import Fraction
ACTIVE={0:4,2:8}
def tag(e): return "1"*e+"0"*(e+2)
def words(n): return map("".join,product("01",repeat=n))
def out(v,n):
    assert len(v)>=n+1
    for e,L in ACTIVE.items():
        if v.startswith(tag(e)) and L<n:
            return (v[:L]+v[L+1:])[:n]
    return v[:n]
def q(s,tau):
    n=max(len(s),len(tau));a=b=0
    for v in words(n+1):
        if out(v,len(tau))==tau:
            b+=1;a+=v.startswith(s)
    assert b>0
    return Fraction(a,b)
fair=post=0
for n in range(1,11):
    counts={}
    for v in words(n+1):
        y=out(v,n);counts[y]=counts.get(y,0)+1
    assert len(counts)==2**n and set(counts.values())=={2}
    fair+=len(counts)
for k in range(1,6):
    for s in words(k):
        for m in range(k,9):
            for tau in words(m):
                assert q(s,tau)==q(s,tau[:k])
                post+=1
assert (fair,post)==(2046,30380)
print("FINITE_SANITY_PASS",fair,post)
