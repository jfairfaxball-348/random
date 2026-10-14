#!/usr/bin/env python3
"""P4-S145 finite exact SANITY ONLY. Not a proof or general oracle-price calculation."""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache

# Effectively open U_k=[0^(4k)]\{0^omega} with computable price 2^(-4k).
# Removing this singleton changes no cylinder probability but does prevent
# compact clopen finite-horizon coverage of U_k.
def h(k,s):
    z='0'*(4*k)
    if s[:min(len(s),len(z))]!=z[:min(len(s),len(z))]:
        return F(0)
    return F(1,2**max(0,4*k-len(s)))

def ideal(k,s):
    if len(s)<=k:
        return F(1)
    a=s[:k]; R=2**(2*k)
    return (1+R*h(k,s))/(1+R*h(k,a))

@lru_cache(None)
def rounded(k,s):
    if len(s)<=k:
        return F(1)
    p=s[:-1]; n=len(p)
    z=ideal(k,p+'0')/ideal(k,p)
    den=2**(n+2*k+6)
    r0=F((z.numerator*den)//z.denominator,den)
    assert 0<r0<2
    return rounded(k,p)*(r0 if s[-1]=='0' else 2-r0)

checks=0
for k in range(1,4):
    assert h(k,'')==F(1,2**(4*k))
    for n in range(0,10):
        for ts in product('01',repeat=n):
            s=''.join(ts)
            assert 2*h(k,s)==h(k,s+'0')+h(k,s+'1')
            assert 2*ideal(k,s)==ideal(k,s+'0')+ideal(k,s+'1')
            assert 2*rounded(k,s)==rounded(k,s+'0')+rounded(k,s+'1')
            assert rounded(k,s)>=F(7,8)*ideal(k,s)
            checks+=4
    assert h(k,'0'*(4*k-1)+'1')==0
    assert h(k,'0'*(4*k))==1
    assert ideal(k,'0'*(4*k))>=F(2,3)*2**(2*k)
for q in [1,2,3]:
    pairs=[(t,2*q-t) for t in [1,2,3] if 0<=2*q-t<=4]
    assert len(pairs)==[0,2,3,2][q]
print('PASS:',checks,'exact finite Fraction assertions; seven q transitions')
