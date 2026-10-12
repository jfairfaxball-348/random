#!/usr/bin/env python3
"""P4-S111 finite sanity; infinite proof is in P4-S111_MATHEMATICS.md."""
from itertools import product
checks = 0
def allbits(n):
    return (''.join(p) for p in product('01', repeat=n))
def ok(s, L):
    for q in range(len(s)//2+1):
        pat = '00'*(2*q+L) + '11'
        start = 2*q
        if start+len(pat) <= len(s) and s[start:start+len(pat)] == pat:
            return False
    return True
def first_bad(s, L):
    for n in range(2,len(s)+1,2):
        if not ok(s[:n],L):
            return n
    return None
def swap_until_exit(s,L):
    out, exited = '', False
    for k in range(len(s)//2):
        blk = s[2*k:2*k+2]
        if not exited and not ok(s[:2*k+2],L):
            exited=True
        out += blk if exited else blk[::-1]
    return out+(s[-1] if len(s)%2 else '')
def tree_switch(a,u,L):
    n = first_bad(u,L)
    return u if n is None else u[:n]+a+u[n+1:]
def hybrid_map(a,u,m,L):
    v=tree_switch(a,u,L)
    return (swap_until_exit(v[:m+(m%2)],L) if a=='0' else v)[:m]
for L in (0,1,2):
    for n in range(0,13,2):
        for w in allbits(n):
            p=swap_until_exit(w,L)
            assert ok(w,L)==ok(p,L)
            assert first_bad(w,L)==first_bad(p,L)
            assert swap_until_exit(p,L)==w
            checks+=3
    for m in range(1,10):
        counts={}
        for x in allbits(m+2):
            y=hybrid_map(x[0],x[1:],m,L)
            counts[y]=counts.get(y,0)+1
        assert len(counts)==2**m and set(counts.values())=={4}
        checks+=1+2**m
    for m in range(0,11,2):
        for tau in allbits(m):
            if not ok(tau,L):
                continue
            rows=[]
            for a in '01':
                v=swap_until_exit(tau,L) if a=='0' else tau
                for t in '01':
                    vals=[]
                    for b in '01':
                        y=hybrid_map(a,v+t+b,m+1,L)
                        assert y[:m]==tau
                        vals.append(y[m]);checks+=1
                    rows.append(''.join(vals))
            assert sorted(rows)==['00','01','01','11']
            checks+=1
print('P4-S111 finite assertions PASS:',checks)
