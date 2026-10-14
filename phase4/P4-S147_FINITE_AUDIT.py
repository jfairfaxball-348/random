"""P4-S147 finite exact cell/payoff sanity; not an infinite proof."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb

counts=Counter()
for q in (1,2,3):
    a=set(range(2*q))
    for target in combinations(range(8),4):
        t=len(a.intersection(target))
        if t in (1,2,3) and 4-t in (1,2,3):
            counts[(q,t)]+=1
            assert counts[(q,t)]<=comb(2*q,t)*comb(8-2*q,4-t)
expected={(1,1):40,(1,2):15,(2,1):16,(2,2):36,(2,3):16,(3,2):15,(3,3):40}
assert dict(counts)==expected
assert sum(counts.values())==178
checks=178
for t in (1,2,3):
    for selected in combinations(range(4),t):
        target=set(selected)
        p=Fraction(t,4)
        assert p*Fraction(4,t)==1
        for a in [Fraction(i,12) for i in range(49)]:
            for b in [Fraction(j,12) for j in range(49)]:
                affordable=t*a+(4-t)*b<=4
                assert affordable == (p*a+(1-p)*b<=1)
                if a>1 and b>1: assert not affordable
                checks+=1
        assert max(Fraction(4,t),Fraction(1))==Fraction(4,t)
print({'labelled_rows':sum(counts.values()),'budget_assertions':checks,'result':'PASS_FINITE_ONLY'})
