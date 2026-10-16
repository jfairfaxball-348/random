#!/usr/bin/env python3
"""P4-S172 exact finite Fraction sanity only; NOT an infinite-stream proof."""
from fractions import Fraction as Q
from itertools import product

def bank(w):
    b=0; active=True
    for i,bit in enumerate(w):
        if i%2==0 and active:
            if bit==0: b+=1
            else: active=False
    return b

def sav(w):
    active=True
    for i,bit in enumerate(w):
        if i%2==0 and active and bit: active=False
    return bank(w)+int(active)

sibling=0; event=0
for n in range(12):
    words=list(product((0,1),repeat=n))
    for w in words:
        assert sav(w)*2==sav(w+(0,))+sav(w+(1,))
        assert bank(w)<=sav(w)
        assert bank(w+(0,))>=bank(w) and bank(w+(1,))>=bank(w)
        sibling+=1
    assert Q(sum(map(bank,words)),2**n)==1-Q(1,2**((n+1)//2))
    for r in range(1,(n+1)//2+1):
        count=sum(all(w[2*i]==0 for i in range(r)) for w in words)
        assert Q(count,2**n)==Q(1,2**r)
        event+=1

def posterior(s,r):
    known=s[1:min(len(s),r+1)]
    if any(known): return Q(0)
    return Q(1,2**(r-len(known)))

post=0
for r in range(1,8):
    for n in range(8):
        for s in product((0,1),repeat=n):
            assert posterior(s,r)*2==posterior(s+(0,),r)+posterior(s+(1,),r)
            post+=1

def port(s):
    return sum((Q(1,2**(r//2))*2**r*posterior(s,r) for r in range(1,9)),Q(0))
for n in range(8):
    for s in product((0,1),repeat=n):
        assert port(s)*2==port(s+(0,))+port(s+(1,))

def u(w):
    return int(any(len(w)>=2*k+1 and w[:2*k+1]==(1,)*(2*k)+(0,) for k in (0,2,5)))
def zero_d(w):
    a=1; b=0
    for v in w:
        if a and v==0: b+=1
        else: a=0
    return b+a
for n in range(11):
    for w in product((0,1),repeat=n):
        b0=sum(w[:j]==(0,)*j for j in range(1,n+1))
        assert Q(b0+u(w),2)<=Q(zero_d(w)+1,2)
print("PASS FINITE SANITY ONLY",{"sibling":sibling,"events":event,"posterior":post,"hybrid_depths":11})
