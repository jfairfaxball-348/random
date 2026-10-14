#!/usr/bin/env python3
"""P4-S131: exact Fraction finite sanity, never an infinite proof."""
from fractions import Fraction
from itertools import combinations,product
D={'A':[('000','0'),('001','10'),('010','11')],
   'B':[('011','1'),('100','00'),('101','01')],
   'C':[('110','0'),('111','1')]}
ROOT={s:(tag,p) for tag, pairs in D.items() for s,p in pairs}
def ws(n):return (''.join(z) for z in product('01',repeat=n))
def price(tag,t):
    z=Fraction(0)
    for s,p in D[tag]:
        if t.startswith(p):z+=Fraction(1,8*(2**(len(t)-len(p))))
        elif p.startswith(t):z+=Fraction(1,8)
    return z
def swprice(tag,t):
    if not t:return Fraction(len(D[tag]),8)
    if len(t)==1:return sum((price(tag,b+t) for b in '01'),Fraction())
    return price(tag,t[1]+t[0]+t[2:])
def gp(s,m):
    if m==0:return ''
    z=ROOT[s[:3]][1]+s[3:]
    assert len(z)>=max(2,m)
    return (z[1]+z[0]+z[2:])[:m]
occ={};total=cases=0
for m in range(8):
    ct={t:[0,0,0] for t in ws(m)}
    for s in ws(m+3):
        ct[gp(s,m)]['ABC'.index(ROOT[s[:3]][0])]+=1
        cases+=1
    for t,v in ct.items():
        assert sum(v)==8
        for i,k in enumerate('ABC'):assert Fraction(v[i],2**(m+3))==swprice(k,t)
        assert sum((swprice(k,t) for k in 'ABC'),Fraction())==Fraction(1,2**m)
        occ.setdefault(m,set()).add(tuple(v));total+=1
assert occ[0]==occ[1]=={(3,3,2)}
assert all(occ[m]=={(2,4,2),(4,2,2)} for m in range(2,8))
trans={}
for a in (1,2,3):
    h={}
    for row in combinations(range(8),4):
        b=sum((i//2<a) for i in row)
        if b in (1,2,3):h[b]=h.get(b,0)+1
    trans[a]=h
assert [sorted(trans[k]) for k in (1,2,3)]==[[1,2],[1,2,3],[2,3]]
stationary=sorted({tuple(sorted(x)) for x in product((1,2,4,8),repeat=3) if sum(x)==8})
assert stationary==[(2,2,4)]
print({'cylinders_exact':total,'source_prefix_cases':cases,'occupancies':{k:sorted(v) for k,v in occ.items()},'transitions':trans,'stationary':stationary,'status':'SANITY_ONLY_NOT_PROOF'})
