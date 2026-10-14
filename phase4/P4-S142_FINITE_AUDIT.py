#!/usr/bin/env python3
"""P4-S142 rational finite q-cell sanity ONLY (not proof of infinite global maps)."""
from fractions import Fraction
q_options = {}
edges = []
for q in (1, 2, 3):
    opts = [(u, 2*q-u) for u in range(5) if 0 <= 2*q-u <= 4]
    assert len(opts) == {1:3, 2:5, 3:3}[q]
    assert all(Fraction(u, 2*q)+Fraction(v, 2*q)==1 for u,v in opts)
    q_options[q] = opts
    for target, sibling in opts:
        if 1 <= target <= 3:
            edges.append((q, target, sibling))
assert edges == [(1,1,1),(1,2,0),(2,1,3),(2,2,2),(2,3,1),(3,2,4),(3,3,3)]
# Denominator q in conditional posterior must be the *parent's* A-cell count.
for q, target, sibling in edges:
    assert Fraction(target, 2*q)+Fraction(sibling, 2*q)==1
    assert not (q==1 and target==3) and not (q==3 and target==1)
print({"all_valid_split_cases":sum(map(len,q_options.values())),
       "two_true_cone_target_edges":len(edges),"edges":edges,
       "scope":"FINITE_EXACT_SANITY_NOT_INFINITE_MAP_PROOF"})
