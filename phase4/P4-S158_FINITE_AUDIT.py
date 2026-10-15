from fractions import Fraction
from itertools import product
def G(x,n):
    assert len(x)>=n+1
    b=x[0]; z=list(x[1:n+1])
    if 1 in z:
        k=z.index(1)
        if k+1<n: z[k+1]=b
    return tuple(z)
def q(s,t):
    m=len(t);N=max(len(s),m+1);a=0
    for r in product((0,1),repeat=N-len(s)):
        if G(tuple(s)+r,m)==tuple(t):a+=1
    return Fraction(a*2**m,2**N)
rows=ident=0
for m in range(10):
    d={t:0 for t in product((0,1),repeat=m)}
    for x in product((0,1),repeat=m+1):d[G(x,m)]+=1
    assert set(d.values())=={2}
    rows+=len(d)
    for n in range(min(m+1,3)+1):
        for s in product((0,1),repeat=n):
            for t in product((0,1),repeat=m):
                assert q(s,t)==(q(s,t+(0,))+q(s,t+(1,)))/2
                ident+=1
for j in range(16):
    t=(0,)*j+(1,)
    assert q((0,),t)==Fraction(1,2)
    assert (q((0,),t+(0,)),q((0,),t+(1,)))==(1,0)
S=[Fraction(i,4) for i in range(5)]
R={v:[(a,b) for a in S for b in S if a+b==2*v] for v in S}
assert [len(R[v]) for v in S]==[1,3,5,3,1]
bets=0
for v,L in R.items():
    for a,b in L:
        f=([2 if w==Fraction(1,2) else 0 for w in (a,b)] if v in (Fraction(1,4),Fraction(3,4)) and a!=b else [1,1])
        assert sum(f)==2
        bets+=1
inside={Fraction(1,4),Fraction(1,2),Fraction(3,4)}
one={v:max(sum(w in inside for w in p)/2 for p in R[v] if p[0]!=p[1]) for v in inside}
for v in inside:
    assert max(sum(one[w] if w in inside else 0 for w in p)/2 for p in R[v] if p[0]!=p[1])<=Fraction(1,2)
print("PASS",rows,ident,16,bets)
