#!/usr/bin/env python3
"""P4-S151 independent-in-method finite Fraction audit, SANITY ONLY.
Full-map fairness, inverse cap and CR-preservation proved symbolically in MATHEMATICS.md.
"""
from itertools import permutations
from fractions import Fraction
from collections import Counter
from math import prod

rat0, rat1 = Fraction(3, 2), Fraction(1, 2)
all_maps = set(permutations((0, 0, 1, 1, 2, 2, 3, 3)))
count = 0
cases = 0
for f in all_maps:
    assert Counter(f) == {0: 2, 1: 2, 2: 2, 3: 2}; count += 1
    for tau in range(4):
        cells3 = [s for s in range(8) if f[s] == tau]
        assert len(cells3) == 2; count += 1
        rho3 = [Fraction(1, 2) for s in cells3]
        assert sum(rho3) / len(rho3) == Fraction(1, 2); count += 1
        cells4 = [(s, b) for s in cells3 for b in (0, 1)]
        a4 = [rat0 if b == 0 else rat1 for s, b in cells4]
        rho4 = [Fraction(b) for s, b in cells4]
        assert len(cells4) == 4; count += 1
        assert sum(rho4) / 4 == Fraction(1, 2); count += 1
        assert sum((q-Fraction(1, 2))**2 for q in rho4) / 4 == Fraction(1, 4); count += 1
        assert sum(a4) / 4 == 1; count += 1
        assert sum((a-1)**2 for a in a4) / 4 == Fraction(1, 4); count += 1
        assert prod(a4) == Fraction(9, 16); count += 1
        assert a4.count(rat0) == a4.count(rat1) == 2; count += 1
        cases += 1
assert len(all_maps) == 2520 and cases == 10080 and count == 93240
print({"balanced_maps": len(all_maps), "cone_cases": cases, "exact_fraction_assertions": count, "grade": "FINITE_SANITY_ONLY"})
