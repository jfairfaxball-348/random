#!/usr/bin/env python3
"""P4-S076 exact Fraction audit for genuine staged raw-filler prices."""
from fractions import Fraction as F
from itertools import product
SIGNS=(-1,1)
def saved(path):
    k=1
    while 2**k<=max(path):k+=1
    z=F(0)
    for j in range(1,k+1):
        hit=next((v for v in path if v>=2**j),path[-1])
        z+=F(1,2**j)*hit
    return z+F(1,2**k)*path[-1]
def cap(path,cs,r,q,prev,mode):
    h=list(path)
    for j,c in enumerate(cs):
        h.append(h[-1]*(1+q*c*r*(prev if j==0 else 1)))
    return h[-1] if mode=='direct' else saved(h)
def price(path,prefix,m,q,prev,mode):
    s=F(0)
    for tail in product(SIGNS,repeat=m-len(prefix)):
        for r in SIGNS:s+=cap(path,prefix+tail,r,q,prev,mode)
    return s/F(2**(m-len(prefix)+1))
checked=0
for m,q in [(3,F(1,2)),(3,F(3,4)),(4,F(7,8)),(5,F(15,16)),(6,F(31,32))]:
    for prev in SIGNS:
        for path in [[F(1)],[F(1),F(7,4),F(21,16)]]:
            for mode in ('direct','savings'):
                K=path[-1] if mode=='direct' else saved(path)
                assert price(path,(),m,q,prev,mode)==K
                for cs in product(SIGNS,repeat=m):
                    p=[price(path,cs[:k],m,q,prev,mode) for k in range(m+1)]
                    assert all(x>0 for x in p) and p[0]==p[1]==K
                    for k in range(m):
                        assert (price(path,cs[:k]+(-1,),m,q,prev,mode)+price(path,cs[:k]+(1,),m,q,prev,mode))/2==p[k]
                    for r in SIGNS:
                        last=cap(path,cs,r,q,prev,mode)
                        assert (last+cap(path,cs,-r,q,prev,mode))/2==p[-1]
                        e=K
                        for k in range(m):e*=p[k+1]/p[k]
                        e*=last/p[-1]
                        assert e==last
                        checked+=1
                assert price(path,(-1,),m,q,prev,mode)==price(path,(1,),m,q,prev,mode)==K
    print('m',m,'q',q,'PASS')
q=F(1,2);p2=1+q*q;plus=1+3*q*q;minus=1-q*q
assert (plus+minus)/2==p2==F(5,4)
assert plus/p2==F(7,5) and minus/p2==F(3,5)
print('triple invalid mean',p2,'correct c2',plus/p2,minus/p2)
def check_scan(groups):
    pos=[];x=0
    for m in groups:pos.append(x);x+=m
    virtual=[]
    def add(kind,b):virtual.append((kind,b))
    for k in range(groups[0]):add('v',2*(pos[0]+k))
    for i,m in enumerate(groups):
        if i+1<len(groups):
            add('v',2*pos[i+1]);add('u',2*pos[i+1])
            for k in range(1,groups[i+1]):add('v',2*(pos[i+1]+k))
        for k in range(m):add('w',2*(pos[i]+k))
        for b in range(2*pos[i],2*(pos[i]+m)):
            for kind in ('u','v','w'):
                if (kind,b) not in virtual:add(kind,b)
    assert len(virtual)==6*x==len(set(virtual))
    for E in ('all','even'):
        raw=[];silent=0
        for kind,b in virtual:
            selected=(E=='all' or b%2==0)
            if kind=='v' and selected:
                if ('c',b) not in raw:raw.append(('c',b))
                raw.append(('b',b))
            elif kind=='w' and selected:
                if ('c',b) not in raw:raw.append(('c',b))
                else:silent+=1
            else:raw.append(({'u':'a','v':'b','w':'c'}[kind],b))
        assert len(raw)==6*x==len(set(raw))
        for i in range(len(groups)-1):
            pivot=virtual.index(('u',2*pos[i+1]))
            assert all(virtual.index(('v',2*(pos[i]+k)))<pivot<virtual.index(('w',2*(pos[i]+k))) for k in range(groups[i]))
        print('scan',E,'groups',groups,'raw',len(raw),'silent',silent,'PASS')
check_scan([3,4,5,6])
assert checked==2048
print('PASS exact endpoint checks',checked,'zero discrepancies')
