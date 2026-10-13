#!/usr/bin/env python3
"""P4-S115 small finite sanity only; symbolic infinity proofs are in MATHEMATICS."""
from collections import defaultdict

def bitword(i,n):
    return format(i, "0%db"%n)
def in_tree(s):
    k=0
    while (1<<k)-1<len(s):
        if s[(1<<k)-1]=="1":
            return k%2==0
        k+=1
    return True
def first_bad(s):
    for n in range(1,len(s)+1):
        if not in_tree(s[:n]):
            return n
    return None
def out(s):
    a,u=s[0],s[1:]
    n=first_bad(u)
    return u if n is None or n==len(u) else u[:n]+a+u[n+1:]
rows=[]
for m in range(1,13):
    pre=defaultdict(list)
    for i in range(2**(m+1)):
        s=bitword(i,m+1)
        pre[out(s)].append(s)
    assert len(pre)==2**m
    assert all(len(v)==2 for v in pre.values())
    for y,P in pre.items():
        q=first_bad(y)
        assert (P[0][0]!=P[1][0])==(q is None or q==m)
    rows.append((m, len(pre),sum(P[0][0]!=P[1][0] for P in pre.values())))
print(rows)
