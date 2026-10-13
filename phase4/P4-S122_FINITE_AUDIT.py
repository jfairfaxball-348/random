#!/usr/bin/env python3
"""P4-S122 finite exact SANITY, NOT an infinite proof or formal certification."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product

def a(t,i,j):
    return (j>=t) and ((j-t+2*i)%3==0)
def b(t,i,j):
    return (j>=t) and ((2*(j-t)+i)%5 in (0,1))
def d(s):
    v=Q(1)
    for j,bit in enumerate(s):
        v*=Q(3,2) if bit==(j//2)%2 else Q(1,2)
    return v
def two(s):
    n=len(s)
    W=[(t,Q(1,2**(t+2))) for t in range(n)]
    W.append((None,Q(1,2)+Q(1,2**(n+1))))
    assert sum((w for _,w in W),Q(0))==1
    result=Q(0)
    for t,wt in W:
        I=[(i,Q(1,2)) for i in (0,1)] if t is not None else [(0,Q(1))]
        for r,wr in W:
            J=[(j,Q(1,2)) for j in (0,1)] if r is not None else [(0,Q(1))]
            for i,wi in I:
                for j,wj in J:
                    out=tuple(bit^int(a(t,i,k) if t is not None else 0)^int(b(r,j,k) if r is not None else 0) for k,bit in enumerate(s))
                    result+=wt*wr*wi*wj*d(out)
    return result
@lru_cache(None)
def td(s): return two(s)
def finite(s):
    n=len(s)
    P=[Q(1,2**(i+2)) for i in range(n)]
    result=Q(0)
    for F in product((0,1),repeat=n):
        w=Q(1)
        for i,bit in enumerate(F): w*=P[i] if bit else 1-P[i]
        result+=w*td(tuple(s[i]^F[i] for i in range(n)))
    return result
@lru_cache(None)
def fd(s): return finite(s)
def transduce(x,m,masked=False):
    key=x[0]; u=x[1:]; ptr=0; y=[]; released=None; erase=False
    for j in range(m):
        if released is None and j>=2 and tuple(y[-2:])==(0,1):
            y.append(key); released=j; erase=True
            continue
        if erase: ptr+=1;erase=False
        bit=u[ptr];ptr+=1
        if masked and released is not None: bit^=int((key+j-released)%3==0)
        y.append(bit)
    return tuple(y),released
def main():
    c2=cf=check=0
    for n in range(7):
        for s in product((0,1),repeat=n):
            assert td(s)==(td(s+(0,))+td(s+(1,)))/2
            c2+=1
    for n in range(5):
        for s in product((0,1),repeat=n):
            assert fd(s)==(fd(s+(0,))+fd(s+(1,)))/2
            cf+=1
    for masked in (False,True):
        for m in range(1,10):
            hist={}
            for x in product((0,1),repeat=m+1):
                y,rel=transduce(x,m,masked)
                hist.setdefault(y,[]).append(x)
            assert len(hist)==2**m and all(len(v)==2 for v in hist.values())
            for y,pre in hist.items():
                rel=transduce(pre[0],m,masked)[1]
                zeros=sum(x[0]==0 for x in pre)
                assert zeros==(1 if rel is None else 2 if y[rel]==0 else 0)
                check+=1
    print("PASS: two_clock_identity",c2,"finite_edit_identity",cf,"fair_fibres_posterior",check)
if __name__=="__main__": main()
