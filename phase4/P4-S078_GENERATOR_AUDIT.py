#!/usr/bin/env python3
"""P4-S078: exact finite algebra checks, not an OH-randomness proof."""
def S(x,n):
    y=x
    for j in range(n): y ^= ((x>>(3*j+2))&1)<<(3*j+1)
    return y
def Q(x,E,n):
    y=x
    for j in range(n):
        if (E>>j)&1:
            b,c=3*j+1,3*j+2
            if ((x>>b)^(x>>c))&1: y ^= (1<<b)|(1<<c)
    return y
def SE(x,E,n):
    y=x
    for j in range(n):
        if (E>>j)&1: y ^= ((x>>(3*j+2))&1)<<(3*j+1)
    return y
def mul(A,B):
    return tuple(__import__('functools').reduce(lambda u,v:u^v,(B[k] for k in range(3) if (row>>k)&1),0) for row in A)
I=(1,2,4); A=(5,3,7); G={'R':(2,1,4),'S':(1,6,4),'Q':(1,4,2)}
p=I
for op in 'RSQRSQRS': p=mul(G[op],p)
assert p==A, (p,A)
from collections import deque
seen={I:0}; q=deque([I])
while q:
    a=q.popleft()
    for g in G.values():
        b=mul(g,a)
        if b not in seen: seen[b]=seen[a]+1; q.append(b)
assert len(seen)==168
error=0
for E in range(16):
    for x in range(1<<12):
        y=Q(S(Q(S(Q(x,E,4),4),E,4),4),E,4)
        if y!=SE(x,E,4): error+=1
assert error==0,error
print('P4-S078 PASS: 65536 support/assignment identities; 168 GL3 matrices; H word length 8; zero errors')
