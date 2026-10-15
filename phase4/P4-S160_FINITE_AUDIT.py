#!/usr/bin/env python3
"""P4-S160 finite exact sanity only; not proof of Cantor-space theorems."""
from fractions import Fraction as Q
from itertools import product
def words(n): return (''.join(w) for w in product('01', repeat=n))
def D(s):
    return Q(len(s)+2,2) if '1' not in s else Q(s.index('1')+1,2)
def first_one(a,m):
    b,z=a[0],a[1:]
    out=list(z[:m])
    try:
        k=z.index('1')
        if k+1<m: out[k+1]=b
    except ValueError: pass
    return ''.join(out)
def run():
    dcount=fair=parents=0
    for n in range(11):
        for s in words(n):
            assert D(s+'0')+D(s+'1')==2*D(s)
            dcount+=1
    assert D('')==1
    for m in range(1,9):
        n=m+1
        leaves=list(words(n))
        image=[first_one(a,m) for a in leaves]
        for y in words(m):
            assert image.count(y)==2
            fair+=1
        e={}
        for j in range(n+1):
            for s in words(j):
                e[s]=sum((D(image[i]) for i,a in enumerate(leaves) if a.startswith(s)),Q(0))/Q(2**(n-j))
        assert e['']==1
        for j in range(n):
            for s in words(j):
                assert e[s+'0']+e[s+'1']==2*e[s]
                parents+=1
        assert e['0'*n]==D('0'*m)
    for j in range(1,20):
        K=Q(j+1,2); residual=Q(1,2**(j+1))
        assert K/Q(2**j)+residual==Q(j+2,2**(j+1))
    assert (dcount,fair,parents)==(2047,510,1012),(dcount,fair,parents)
    print({'rational_D_parent_splits':dcount,'fair_first_one_cylinders':fair,
           'finite_source_parent_splits':parents,'ui_tail_checks':19,
           'status':'PASS_FINITE_SANITY_ONLY'})
if __name__=='__main__': run()
