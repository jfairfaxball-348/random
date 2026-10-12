#!/usr/bin/env python3
"""P4-S114: finite sanity only; no infinity, CR, or DP2 certification."""
from itertools import product
from collections import Counter

row_count=Counter()
for z in product((0,1,2), repeat=4):
    if sum(z)!=4: continue
    row_count[(z.count(0),z.count(1),z.count(2))]+=2**z.count(1)
assert row_count==Counter({(0,4,0):16,(1,2,1):48,(2,0,2):6})

input_checks=0
for m in range(1,10):
    counts={}
    for bits in product((0,1),repeat=m+1):
        a=bits[0];u=bits[1:]
        v=u if u[0]==0 else (1,a)+u[2:]
        out=v[:m]
        counts[out]=counts.get(out,0)+1
        input_checks+=1
    assert len(counts)==2**m and set(counts.values())=={2}
    assert sum(1 for y in counts if y[0]==0)==2**(m-1)
assert input_checks==sum(2**(m+1) for m in range(1,10))
print({"row_types":{"balanced":16,"hybrid":48,"folded":6},
       "depths":9,"source_prefix_tests":input_checks,
       "clopen_D1_measure":"1/2","status":"FINITE_SANITY_PASS"})
