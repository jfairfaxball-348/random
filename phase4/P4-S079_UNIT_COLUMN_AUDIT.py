#!/usr/bin/env python3
"""Exact finite F2 audit of P4-S079's infinite-block unit-column argument.

The infinite-scan legality is proved in the mathematics record, not by this audit.
"""
I=((1,0,0),(0,1,0),(0,0,1))
R=((0,1,0),(1,0,0),(0,0,1))
Q=((1,0,0),(0,0,1),(0,1,0))
S=((1,0,0),(0,1,1),(0,0,1))
A=((1,0,1),(1,1,0),(1,1,1))
steps=(R,S,Q,R,S,Q,R,S)

def mm(U,V):
    return tuple(tuple(sum(U[i][k]*V[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))

def act(U,x):
    return tuple(sum(U[i][k]*x[k] for k in range(3))%2 for i in range(3))

C=I
states=[]
for op in steps:
    C=mm(op,C)
    states.append(C)
assert C==A
remainder=[]
for i in range(8):
    B=I
    for j in range(i+1,8): B=mm(steps[j],B)
    assert mm(B,states[i])==A
    colweights=tuple(sum(B[r][k] for r in range(3)) for k in range(3))
    singleton=tuple((k,next(r for r in range(3) if B[r][k])) for k in range(3) if colweights[k]==1)
    remainder.append((B,colweights,singleton))
    for mask in range(8):
        x=tuple((mask>>j)&1 for j in range(3))
        assert act(B,act(states[i],x))==act(A,x)
        for k,q in singleton:
            xflip=tuple(x[j]^(j==k) for j in range(3))
            assert all(act(B,x)[r]==act(B,xflip)[r] for r in range(3) if r!=q)
            assert act(B,x)[q]^act(B,xflip)[q]==1
assert not remainder[0][2]
assert all(remainder[i][2] for i in range(1,7))
assert remainder[6][0]==S
print('H factorization: PASS, H=[101;110;111]')
for i,(B,w,unit) in enumerate(remainder):
    print('z%d -> Y rows=%s column_weights=%s unit_columns=%s' % (i, '/'.join(''.join(map(str,r)) for r in B),w,unit))
print('All 8 source assignments at 8 stages and all singleton-coordinate flip checks: PASS')
print('z1..z6 have an unbounded computable unit-column family; z0 has none: PASS')
