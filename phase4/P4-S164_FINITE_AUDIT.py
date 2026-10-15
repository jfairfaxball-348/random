#!/usr/bin/env python3
"""P4-S164 exact Fraction sanity; cannot verify infinite quantifiers."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

@lru_cache(None)
def mix(s):
    return F(s.index("1")+1,2) if "1" in s else F(1)+F(len(s),2)
def pos(s):
    return (mix(s)+1)/2
@lru_cache(None)
def finance(s):
    if not s: return F(1)
    p=s[:-1]; n=len(p); eps=F(1,2**(n+2))
    r=pos(p+"0")/(2*pos(p))
    a=(1-eps)*r+eps/2
    den=2**(n+6)
    q=F((a*den).numerator//(a*den).denominator,den)
    assert abs(q-a)<=eps/4 and 0<q<1
    assert q>=(1-eps)*r and 1-q>=(1-eps)*(1-r)
    return 2*finance(p)*(q if s[-1]=="0" else 1-q)
def component(i,s):
    j=min(i,len(s))
    return F(2**j) if s[:j]=="0"*j else F(0)

checks=0
for n in range(10):
    for bits in product("01",repeat=n):
        s="".join(bits)
        assert mix(s)>=0
        assert mix(s+"0")+mix(s+"1")==2*mix(s)
        assert finance(s+"0")+finance(s+"1")==2*finance(s)
        assert finance(s)>=(1+mix(s))/4
        checks+=4
        if n<=7:
            head=sum((F(1,2**(i+1))*component(i,s) for i in range(n)),F(0))
            tail=F(1,2**n)*component(n,s)
            assert head+tail==mix(s)
            checks+=1
for i in range(11):
    for n in range(11):
        assert component(i,"0"*n)<=2**i
        checks+=1
for n in range(1,14):
    assert mix("0"*n)==1+F(n,2)
    checks+=1
for k in range(1,9):
    N=k+2
    hits=sum(1 for tup in product("01",repeat=N) if "".join(tup).startswith("0"*k))
    assert F(hits,2**N)==F(1,2**k)
    checks+=1
print("PASS",checks,"EXACT_FRACTION_FINITE_GROUPS_ONLY")
