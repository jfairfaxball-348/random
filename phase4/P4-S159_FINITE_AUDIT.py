"""P4-S159 finite exact arithmetic sanity ONLY, not an infinite proof or CI."""
from fractions import Fraction as Q
from itertools import product
bits=lambda n: [''.join(z) for z in product('01',repeat=n)]
counts={'first_one_rows':0,'first_one_posterior':0,'quarter_rows':0,'rational_kernel_nodes':0,'tilted_rows':0}
def first_one(w):
    b,z=w[0],list(w[1:])
    k=next((i for i,x in enumerate(z) if x=='1'),None)
    if k is not None and k+1<len(z): z[k+1]=b
    return ''.join(z)
for m in range(1,10):
    bucket={t:[] for t in bits(m)}
    for s in bits(m+1): bucket[first_one(s)].append(s)
    for t,pre in bucket.items():
        assert len(pre)==2,(t,pre)
        counts['first_one_rows']+=1
    if m>1:
        j=m-2
        t='0'*j+'1'; t0,t1=t+'0',t+'1'
        sourceprefix=lambda u:Q(sum(a[0]=='0' for a in bucket[u]),2)
        assert sourceprefix(t0)==1 and sourceprefix(t1)==0
        counts['first_one_posterior']+=1
qvals=[Q(i,4) for i in range(5)]
for p in qvals:
    for a in qvals:
        for b in qvals:
            if a+b!=2*p:continue
            if p in (Q(1,4),Q(3,4)) and a!=b and a==Q(1,2):
                m0,m1=Q(2),Q(0)
            elif p in (Q(1,4),Q(3,4)) and a!=b and b==Q(1,2):
                m0,m1=Q(0),Q(2)
            else: m0,m1=Q(1),Q(1)
            assert m0+m1==2
            counts['quarter_rows']+=1
assert counts['quarter_rows']==13
def D(s): return Q(3,2)**s.count('0')*Q(1,2)**s.count('1')
def zeta(s):return (1+D(s))*Q(1,2)**(len(s)+1)
def ratio(s):return zeta(s+'0')/zeta(s)
def approx_ratio(s):
    n=len(s);N=2**(2*n+8);q=ratio(s)
    rounded=(q.numerator*N*2//q.denominator+1)//2
    return Q(rounded,N)
mass={'':Q(1)}
for n in range(9):
    for s in bits(n):
        p=approx_ratio(s)
        assert 0<p<1 and abs(p-ratio(s))<=Q(1,2**(2*n+8))
        mass[s+'0']=mass[s]*p;mass[s+'1']=mass[s]*(1-p)
        assert mass[s+'0']+mass[s+'1']==mass[s]
        counts['rational_kernel_nodes']+=1
for s in mass:assert mass[s]>=Q(31,32)*zeta(s)
for j in range(1,17):
    lam=Q(1,4**j);tilt=Q(1,2)+lam/2
    assert tilt>=Q(1,2)
    counts['tilted_rows']+=1
assert sum(counts.values())==1570
print('PASS finite exact Fraction sanity', counts)
