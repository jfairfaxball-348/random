#!/usr/bin/env python3
"""P4-S113 finite tag-shift sanity only; no infinity/rand proof."""
from itertools import product
def price(v,T,n):
    if v[:n] in T["leaves"]: return (1,1)
    j=next(k for k in range(1,n+1) if v[:k] not in T["nodes"])
    return (2,0) if v[j]=="0" else (0,2)
checks=0; trees=0;badtrees=0
for n in (1,2,3,4):
    leaves=["".join(x) for x in product("01",repeat=n)]
    for mask in range(1<<len(leaves)):
        S={x for i,x in enumerate(leaves) if (mask>>i)&1}
        nodes={""}
        for x in S: nodes.update(x[:k] for k in range(len(x)+1))
        T={"leaves":S,"nodes":nodes}; bad=False
        for ww in product("01",repeat=n+1):
            w="".join(ww); h0=price("0"+w,T,n);h1=price("1"+w,T,n)
            a=h0[0]+h1[0]; b=h0[1]+h1[1]
            checks+=4
            assert a+b==4
            assert 0<=a<=4 and 0<=b<=4
            bad |= a!=2
        checks+=1
        assert bad==(len(S)!=len(leaves))
        trees+=1;badtrees+=int(bad)
assert (trees,badtrees,checks)==(65812,65808,8471380)
def sub(r,d):
    if d==0:
        yield frozenset((r,)); return
    A=[frozenset()]+list(sub(r+"0",d-1))
    B=[frozenset()]+list(sub(r+"1",d-1))
    for a in A:
        for b in B: yield frozenset((r,))|a|b
nonpruned=0; checks2=0
n=3;allleaves={"".join(x) for x in product("01",repeat=n)}
for nodes in sub("",n):
    S={x for x in nodes if len(x)==n}
    T={"leaves":S,"nodes":nodes};bad=False
    for ww in product("01",repeat=n+2):
        w="".join(ww)
        a=price("0"+w,T,n)[0]+price("1"+w,T,n)[0]
        checks2+=1
        assert 0<=a<=4
        bad |= a!=2
    checks2+=1
    assert bad==(S!=allleaves)
    nonpruned+=1
assert (nonpruned,checks2)==(676,22308)
print({"result":"PASS_FINITE_ONLY","clopen_trees":trees,
       "rooted_nonpruned":nonpruned,"assertions":checks+checks2})
