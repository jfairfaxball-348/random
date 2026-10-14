#!/usr/bin/env python3
"""P4-S149 independent-in-method FINITE sanity, not a proof of infinite maps/fibres."""
from fractions import Fraction as Q
from itertools import product

def words(n): return [''.join(z) for z in product('01',repeat=n)]
def p(t):
    d=Q(1)
    for b in t: d*=Q(3,2) if b=='0' else Q(1,2)
    return d+1
def G(kind,s,n):
    if kind=='identity': return s[:n]
    if kind=='delete': return s[1:n+1]
    if kind=='swap': return ''.join(s[i+1] if i%2==0 else s[i-1] for i in range(n))
    if kind=='xor': return ''.join(str((int(s[i])^int(s[i+1])) if i%2==0 else int(s[i])) for i in range(n))
    if kind=='majority': return ''.join(str(int(s[3*i:3*i+3].count('1')>=2)) for i in range(n))
    if kind=='constant': return '0'*n
    raise ValueError(kind)
def u(kind,n):
    if n==0: return 0
    return {'identity':n,'delete':n+1,'swap':n+1,'xor':n+1,'majority':3*n,'constant':n}[kind]

checks=0
for kind in ('identity','delete','swap','xor','majority','constant'):
    e={'':Q(1)}; debt={'':Q(1)}
    for n in range(1,5 if kind=='majority' else 7):
        old_e,new_e=e,{}
        old_debt,new_debt=debt,{}
        delta=u(kind,n)-u(kind,n-1)
        for s in words(u(kind,n-1)):
            tau=G(kind,s,n-1)
            w={t:p(G(kind,s+t,n))/p(tau) for t in words(delta)}
            a=sum(w.values(),Q(0))/2**delta
            assert a>0
            for t in words(delta):
                leaf=s+t
                new_e[leaf]=old_e[s]*w[t]/a
                new_debt[leaf]=old_debt[s]*a
                assert new_e[leaf]*new_debt[leaf]==p(G(kind,leaf,n))/p('')
                checks+=1
            assert sum(new_e[s+t] for t in words(delta))==2**delta*old_e[s]
            checks+=1
        e,debt=new_e,new_debt
    print(kind,len(e),'final-level source words')
assert checks==6774,checks
print('PASS FINITE SANITY ONLY:',checks,'exact Fraction assertions')
