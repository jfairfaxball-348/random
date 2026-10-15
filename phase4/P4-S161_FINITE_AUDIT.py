#!/usr/bin/env python3
"""P4-S161: exact finite sanity only, not proof of any infinite theorem."""
from fractions import Fraction as Q
def compatible(t): return all(t[i]=='0' for i in range(len(t)) if i%3 in (1,2))
def mut(t):
    return Q(0) if not compatible(t) else Q(1,2**sum(i%3==0 for i in range(len(t))))
def children(t,row):
    m=len(t)
    if not compatible(t):
        p,q=[w for a,w in row if a=='P']
        r,s=[w for a,w in row if a=='S']
        return ([('P',p+'0'),('P',p+'1'),('S',r+'0'),('S',s+'0')],
                [('P',q+'0'),('P',q+'1'),('S',r+'1'),('S',s+'1')])
    A=[w for a,w in row if a=='A']; B=[w for a,w in row if a=='B']
    if m%3==0:
        assert len(A)==3 and len(B)==1
        return ([(a,w+'0') for a,w in row],[(a,w+'1') for a,w in row])
    if m%3==1:
        a,b,c=A;d,=B
        return ([('A',a+'0'),('A',a+'1'),('B',d+'0'),('B',d+'1')],
                [('P',b+'0'),('P',b+'1'),('S',c+'0'),('S',c+'1')])
    a,b=A;c,d=B
    return ([('A',a+'0'),('A',a+'1'),('A',b+'0'),('B',c+'0')],
            [('P',b+'1'),('P',c+'1'),('S',d+'0'),('S',d+'1')])
def run():
    tab={'':[('A','00'),('A','01'),('A','10'),('B','11')]}
    rows=splitchecks=odds=0
    for m in range(11):
        assert len(tab)==2**m
        allsources=[w for row in tab.values() for _,w in row]
        assert len(set(allsources))==2**(m+2)
        total_lam=total_sing=Q(0)
        for t,row in tab.items():
            assert len(row)==4 and len({w for _,w in row})==4
            q=Q(sum(w.startswith('11') for _,w in row),4)
            total_lam+=Q(1,2**m)*q
            total_sing+=mut(t)*q
            if compatible(t): assert q==(Q(1,4),Q(1,4),Q(1,2))[m%3]
            rows+=1
        assert total_lam==Q(1,4)
        assert total_sing==(Q(1,4),Q(1,4),Q(1,2))[m%3]
        for delta in [Q(1,4),Q(1,2),Q(3,4)]:
            got=delta*total_lam+(1-delta)*total_sing
            assert got==(Q(1,4) if m%3!=2 else (2-delta)/4)
        if m<10:
            ntab={}
            for t,row in tab.items():
                a,b=children(t,row)
                assert sorted(w+digit for _,w in row for digit in '01')==sorted(w for _,w in a+b)
                ntab[t+'0']=a;ntab[t+'1']=b
                splitchecks+=1
            tab=ntab
        if m%3 in (1,2):
            t='0'*m
            for delta in [Q(1,4),Q(1,2),Q(3,4)]:
                p=(delta*Q(1,2**(m+1))+(1-delta)*mut(t)) / (delta*Q(1,2**m)+(1-delta)*mut(t))
                r=mut(t)/Q(1,2**m)
                assert p==1-delta/(2*(delta+(1-delta)*r))
                odds+=1
    assert (rows,splitchecks,odds)==(2047,1023,21)
    print({'fair_all_output_rows':rows,'eight_child_partition_checks':splitchecks,
           'weighted_forced_conditional_checks':odds,'status':'PASS_FINITE_SANITY_ONLY'})
if __name__=='__main__': run()
