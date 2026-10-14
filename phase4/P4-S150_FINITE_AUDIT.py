#!/usr/bin/env python3
"""P4-S150 exact Fraction finite SANITY; NOT an all-output infinite fibre proof."""
from fractions import Fraction as Q
from itertools import product, combinations
def words(n): return [''.join(w) for w in product('01',repeat=n)]
def U(kind,n):
 if n==0:return 0
 return {'identity':n,'identity_overread':n+1,'delete':n+1,'swap':2*((n+1)//2)+n,'xor':2*((n+1)//2)+n,'majority':3*n}[kind]
def G(kind,s,n):
 if kind in ('identity','identity_overread'):return s[:n]
 if kind=='delete':return s[1:n+1]
 if kind=='swap':return ''.join(s[k^1] for k in range(n))
 if kind=='xor':return ''.join(str(int(s[k])^int(s[k+1])) if k%2==0 else s[k] for k in range(n))
 if kind=='majority':return ''.join('1' if s[3*k:3*k+3].count('1')>=2 else '0' for k in range(n))
 raise ValueError(kind)
checks=0;by_map=[]
for kind in ('identity','identity_overread','delete','swap','xor','majority'):
 count=0
 for n in range(4 if kind=='majority' else 6):
  N=U(kind,n);delta=U(kind,n+1)-N
  assert delta>0
  for tau in words(n):
   group=[s for s in words(N) if G(kind,s,n)==tau]
   assert len(group)==2**(N-n);checks+=1;count+=1
   r0,r1=Q(3,2),Q(1,2);probs=[];A=[]
   for s in group:
    rho=Q(sum(G(kind,s+t,n+1)[-1]=='1' for t in words(delta)),2**delta)
    a=(1-rho)*r0+rho*r1
    assert 0<a<2;checks+=1;count+=1
    probs.append(rho);A.append(a)
   assert sum(probs,Q(0))==Q(len(group),2);checks+=1;count+=1
   assert sum(A,Q(0))==len(group);checks+=1;count+=1
   assert sum((a-1)**2 for a in A)==(r1-r0)**2*sum((rho-Q(1,2))**2 for rho in probs);checks+=1;count+=1
   prod=Q(1)
   for a in A:prod*=a
   assert prod<=1;checks+=1;count+=1
 by_map.append((kind,count))
rowcounts={}
for q in (1,2,3):
 for pick in combinations(range(8),4):
  t=sum(i<2*q for i in pick)
  if not(1<=t<=3 and 0<=2*q-t<=4):continue
  key=q,t;rowcounts[key]=rowcounts.get(key,0)+1
  for a,b in ((Q(0),Q(0)),(Q(1),Q(1)),(Q(4,t),Q(0)),(Q(0),Q(4,4-t)),(Q(1,2),Q(1,2))):
   budget=t*a+(4-t)*b
   assert (budget<=4)==(t*a+(4-t)*b<=4);checks+=1
  assert not(t*Q(101,100)+(4-t)*Q(101,100)<=4);checks+=1
assert sorted(rowcounts.items())==[((1,1),40),((1,2),15),((2,1),16),((2,2),36),((2,3),16),((3,2),15),((3,3),40)];checks+=1
assert sum(rowcounts.values())==178;checks+=1
assert checks==8532,checks
print('PASS FINITE SANITY ONLY',checks,by_map,rowcounts)
