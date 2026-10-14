#!/usr/bin/env python3
"""P4-S133 exact finite SANITY, not proof of all true inverse/fairness claims."""
from itertools import product
from fractions import Fraction
from collections import Counter

def words(n): return (''.join(x) for x in product('01',repeat=n))

def obs(s):
    head=s[:2];tail=s[2:]
    if head=='00':return '0'+tail,'A'
    if head=='01':return '1'+tail,'A'
    if head=='10':return tail,'B'
    return tail,'C'

def labelled(s):
    y,base=obs(s)
    assert y
    sheet=('B' if base=='A' else 'A' if base=='B' else 'C') if y[0]=='1' else base
    return y,sheet

checked=checked_f=total_cells=0
for m in range(1,9):
    n=m+2
    census={t:Counter() for t in words(m)}
    fcount=Counter()
    for s in words(n):
        y,j=labelled(s)
        t=y[:m]; census[t][j]+=1
        heavy='A' if y[0]=='0' else 'B'
        f=('1' if j==heavy else '0')+y
        fcount[f[:m]]+=1
        total_cells+=1
    for t,ct in census.items():
        expected={'A':2,'B':1,'C':1} if t[0]=='0' else {'A':1,'B':2,'C':1}
        assert dict(ct)==expected,(t,ct,expected)
        assert sum(ct.values())==4
        assert Fraction(sum(ct.values()),2**n)==Fraction(1,2**m)
        checked+=1
    assert set(fcount)==set(words(m))
    assert set(fcount.values())=={4}
    checked_f+=len(fcount)

rows2={q:[(a,2*q-a) for a in (1,2,3) if 1<=a<=3 and 1<=2*q-a<=3] for q in (1,2,3)}
rows3=[(a,b,c) for a in (1,2) for b in (1,2) for c in (1,2) if a+b+c==4]
assert rows2=={1:[(1,1)],2:[(1,3),(2,2),(3,1)],3:[(3,3)]}
assert sorted(rows3)==[(1,1,2),(1,2,1),(2,1,1)]
print({'result':'PASS_SANITY_ONLY','G_cylinders':checked,'F_cylinders':checked_f,'source_prefixes':total_cells,'three_sheet_possible_vectors':rows3,'two_sheet_local_rows':rows2})
