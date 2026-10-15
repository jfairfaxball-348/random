#!/usr/bin/env python3
"""P4-S165 exhaustive finite sanity ONLY; independent of S011's special predictor."""
from collections import Counter
from fractions import Fraction

def challenge(tau):
    n=len(tau)
    return (n//3)%2 if n%3==2 else None

def children(row, phase, tau):
    if phase=='safe':
        assert Counter(k for k,_ in row)=={'P':2,'S':2}
        p,q=[s for k,s in row if k=='P']
        r,s=[s for k,s in row if k=='S']
        return (([('P',p+'0'),('P',p+'1'),('S',r+'0'),('S',s+'0')],'safe'),
                ([('P',q+'0'),('P',q+'1'),('S',r+'1'),('S',s+'1')],'safe'))
    if phase==0:
        assert Counter(k for k,_ in row)=={'A':3,'B':1}
        a0,a1,a2=[s for k,s in row if k=='A']
        b0=[s for k,s in row if k=='B'][0]
        p=challenge(tau)
        if p is None:
            return (([('A',a0+'0'),('A',a0+'1'),('A',a1+'0'),('B',b0+'0')],0),
                    ([('A',a1+'1'),('A',a2+'0'),('A',a2+'1'),('B',b0+'1')],0))
        win=[('A',a0+'0'),('A',a0+'1'),('B',b0+'0'),('B',b0+'1')]
        lose=[('P',a1+'0'),('P',a1+'1'),('S',a2+'0'),('S',a2+'1')]
        return ((win,1),(lose,'safe')) if p==0 else ((lose,'safe'),(win,1))
    assert phase==1 and Counter(k for k,_ in row)=={'A':2,'B':2}
    a0,a1=[s for k,s in row if k=='A']
    b0,b1=[s for k,s in row if k=='B']
    p=challenge(tau)
    if p is None:
        return (([('A',a0+'0'),('A',a0+'1'),('B',b0+'0'),('B',b0+'1')],1),
                ([('A',a1+'0'),('A',a1+'1'),('B',b1+'0'),('B',b1+'1')],1))
    win=[('A',a0+'0'),('A',a0+'1'),('A',a1+'0'),('B',b0+'0')]
    lose=[('P',a1+'1'),('P',b0+'1'),('S',b1+'0'),('S',b1+'1')]
    return ((win,0),(lose,'safe')) if p==0 else ((lose,'safe'),(win,0))

rows={'':([('A','00'),('A','01'),('A','10'),('B','11')],0)}
sibling_checks=0
cell_occurrences=0
for n in range(12):
    all_cells=[]
    for tau,(row,phase) in rows.items():
        assert len(row)==4 and len(set(s for _,s in row))==4
        assert all(len(s)==n+2 for _,s in row)
        all_cells.extend(s for _,s in row)
        cell_occurrences+=4
    assert len(set(all_cells))==len(all_cells)==2**(n+2)
    assert Fraction(4,2**(n+2))==Fraction(1,2**n)
    if n==11: break
    new={}
    for tau,(row,phase) in rows.items():
        left,right=children(row,phase,tau)
        source_children={s+b for _,s in row for b in '01'}
        assigned=[s for _,s in left[0]]+[s for _,s in right[0]]
        assert len(assigned)==len(set(assigned))==8
        assert set(assigned)==source_children
        assert len(left[0])==len(right[0])==4
        new[tau+'0']=left
        new[tau+'1']=right
        sibling_checks+=1
    rows=new
assert sibling_checks==2047 and cell_occurrences==16380
assert len(rows)==2048 and len(all_cells)==8192
assert len(set((0,0,1)))==len(set((1,2,2)))==2
print('PASS LOCAL SANITY: 2047 all-sibling transitions, 16380 aligned cells, 8192 terminal source words; no claims about infinite fibres')
