from fractions import Fraction
from itertools import combinations
rows=[]
for q in (1,2,3):
    for zeroes in combinations(range(8),4):
        z=set(zeroes)
        t=sum(2*i+b in z for i in range(q) for b in (0,1))
        if 1<=t<=3:
            rows.append((q,t,tuple(0 if j in z else 1 for j in range(8))))
expected={(1,1):40,(1,2):15,(2,1):16,(2,2):36,(2,3):16,(3,2):15,(3,3):40}
assert len(rows)==178
assert {k:sum((q,t)==k for q,t,_ in rows) for k in expected}==expected
ratios=[(Fraction(i,6),Fraction(12-i,6)) for i in range(1,12)]
checks=0
for q,t,row in rows:
    for ratio in ratios:
        for j in range(4):
            b0,b1=row[2*j],row[2*j+1]
            gains=(ratio[b0],ratio[b1]) if b0!=b1 else (Fraction(1),Fraction(1))
            assert sum(gains,Fraction(0))==2
            checks+=1
assert checks==7832
budgets=0
for t in (1,2,3):
    for i in range(13):
        for j in range(13):
            a,b=Fraction(i,4),Fraction(j,4)
            assert (t*a+(4-t)*b<=4)==(sum([a]*t+[b]*(4-t))<=4)
            budgets+=1
assert budgets==507
def swap_bits(bits):
    a=list(bits)
    for j in range(0,len(a)-1,2):
        a[j],a[j+1]=a[j+1],a[j]
    return a
for m in range(12):
    n=m+1
    for v in range(1<<n):
        s=[(v>>(n-1-i))&1 for i in range(n)]
        row=[swap_bits(s+[b,0,0])[m] for b in (0,1)]
        assert (row[0]==row[1])==(m%2==1)
print('PASS finite only: rows=178 fair-parent=7832 budgets=507 swap-levels=12')