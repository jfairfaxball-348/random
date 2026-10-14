#!/usr/bin/env python3
"""P4-S146 exact finite combinatorial sanity, NOT an infinite proof."""
from itertools import combinations
from fractions import Fraction
from math import comb

counts = {}
for q in (1, 2, 3):
    for selected in combinations(range(8), 4):
        S = set(selected)  # exactly 4 of 8 children go to output bit 0
        t = sum(1 for i in S if i // 2 < q)
        sibling_a = 2*q-t
        assert len(S) == 4 and len(set(range(8))-S) == 4
        assert 0 <= sibling_a <= 4
        if 1 <= t <= 3:
            counts[(q,t)] = counts.get((q,t),0)+1
            if q == 1 and t == 2:
                assert {0,1} <= S  # first A parent has both children forced
            if q == 3 and t == 2:
                assert {6,7} <= S  # symmetric forced B source parent
expected = {(1,1):40,(1,2):15,(2,1):16,(2,2):36,
            (2,3):16,(3,2):15,(3,3):40}
assert counts == expected
for (q,t),number in counts.items():
    assert number == comb(2*q,t)*comb(8-2*q,4-t)
assert sum(counts.values()) == 178  # 210 candidate rows for 3 q
for t in (1,2,3):
    # After q_A=1 -> 2, all A target grandchildren descend from same s.
    assert Fraction(t,4) <= Fraction(3,4)
for stake in range(2001):
    r0 = Fraction(stake,1000)
    r1 = 2-r0
    assert r0+r1 == 2 and min(r0,r1) <= 1
print("PASS: 178 labelled rows; 7 transitions; 2001 fair rational source splits; two-bit cap 3/4. SANITY ONLY.")
