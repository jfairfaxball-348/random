#!/usr/bin/env python3
"""P4-S116: finite counts only. Run locally: python3 phase4/P4-S116_FINITE_AUDIT.py"""
from collections import Counter
from itertools import product

def q(n):
    j=0
    while 4**j <= n:
        if n==4**j: return 2*4**j
        if n==2*4**j: return 4**j
        j+=1
    return n

def tree_ok(s):
    k=0
    while 2**k-1<len(s):
        if s[2**k-1]=="1": return k%2==0
        k+=1
    return True

def gt(prefix,m):
    a,u=prefix[0],prefix[1:]
    assert len(u)==m
    for n in range(1,m+1):
        if not tree_ok(u[:n]):
            return u if n>=m else u[:n]+a+u[n+1:]
    return u

def run():
    rows=[]
    for m in range(1,9):
        use=max(q(i) for i in range(m+1))+1
        assert use<=12
        counts=Counter("".join(str(int(w[q(j)]!=w[q(j+1)])) for j in range(m))
                       for w in product("01",repeat=use))
        assert len(counts)==2**m and set(counts.values())=={2**(use-m)}
        rows.append([m,use,2**(use-m)])
    tree_rows=[]
    for m in range(1,12):
        counts=Counter(gt("".join(w),m) for w in product("01",repeat=m+1))
        assert len(counts)==2**m and set(counts.values())=={2}
        tree_rows.append([m,2**m,2])
    print("PASS; q-map [output length, source use, each fibre prefix count]:",rows)
    print("PASS; G_T [output length, target cylinder count, each preimage count]:",tree_rows)

if __name__=="__main__":run()
