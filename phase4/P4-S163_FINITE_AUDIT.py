#!/usr/bin/env python3
"""P4-S163 exact Fraction finite sanity, not an infinite proof."""
from fractions import Fraction as Q
from itertools import product
from math import comb
p=Q(1,3)
branches=(("0",Q(1,2)),("10",Q(1,4)),("11",Q(1,4)))
checks=0
def words(n): return (''.join(bits) for bits in product('01',repeat=n))
def G(w,m): return w[1:1+m] if w.startswith('0') else w[2:2+m]
def mu(t): return p**t.count('1')*(1-p)**t.count('0')
def nu(s):
    ans=Q(0)
    for c,w in branches:
        if s.startswith(c): ans+=w*mu(s[len(c):])
        elif c.startswith(s): ans+=w
    return ans
def eta(m,s):
    N=max(m+2,len(s))
    return sum((Q(1,2)**N*2**m*mu(G(w,m)) for w in words(N) if w.startswith(s)),Q(0))
for m in range(8):
    rows={t:set() for t in words(m)}
    for w in words(m+2): rows[G(w,m)].add(w)
    for t in words(m):
        assert len(rows[t])==4
        assert sum((Q(1,2)**(m+2) for _ in rows[t]),Q(0))==Q(1,2)**m
        assert {w[0] for w in rows[t]}=={'0','1'}
        checks+=3
    if m<7:
        nxt={t:set() for t in words(m+1)}
        for w in words(m+3): nxt[G(w,m+1)].add(w)
        for t in words(m):
            assert {w+b for w in rows[t] for b in '01'}==nxt[t+'0']|nxt[t+'1']
            assert not (nxt[t+'0'] & nxt[t+'1'])
            checks+=2
assert nu('')==1
for n in range(7):
    for s in words(n):
        assert nu(s)==nu(s+'0')+nu(s+'1')
        checks+=1
for m in range(7):
    for n in range(min(m,5)+1):
        for s in words(n):
            assert eta(m,s)==nu(s)
            checks+=1
for m in (12,24,36):
    k=(5*m)//12
    lam=sum((Q(comb(m,i),2**m) for i in range(k+1)),Q(0))
    biased=sum((comb(m,i)*p**i*(1-p)**(m-i) for i in range(k+1)),Q(0))
    assert 0<lam<1 and 0<biased<1
    checks+=2
assert checks==1335,checks
print("P4-S163 PASS FINITE SANITY ONLY: 1335 exact Fraction checks")
