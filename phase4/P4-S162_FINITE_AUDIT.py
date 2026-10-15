#!/usr/bin/env python3
"""P4-S162: ALL-output finite row sanity and rational phase-selector arithmetic. Not infinitary proof."""
from fractions import Fraction as Q
def active(t):
    return all(t[i]=='0' for i in range(len(t)) if i%3 in (1,2))
def kids(t,row):
    m=len(t)
    if not active(t):
        p,q=[w for a,w in row if a=='P'];u,v=[w for a,w in row if a=='S']
        return ([('P',p+'0'),('P',p+'1'),('S',u+'0'),('S',v+'0')],
                [('P',q+'0'),('P',q+'1'),('S',u+'1'),('S',v+'1')])
    A=[w for a,w in row if a=='A'];B=[w for a,w in row if a=='B']
    if m%3==0:
        return ([(a,w+'0') for a,w in row],[(a,w+'1') for a,w in row])
    if m%3==1:
        a,b,c=A;d,=B
        return ([('A',a+'0'),('A',a+'1'),('B',d+'0'),('B',d+'1')],
                [('P',b+'0'),('P',b+'1'),('S',c+'0'),('S',c+'1')])
    a,b=A;c,d=B
    return ([('A',a+'0'),('A',a+'1'),('A',b+'0'),('B',c+'0')],
            [('P',b+'1'),('P',c+'1'),('S',d+'0'),('S',d+'1')])
def mass(t):
    return Q(0) if not active(t) else Q(1,2**sum(i%3==0 for i in range(len(t))))
def dist(rows,tag):
    m=len(next(iter(rows)))
    out={}
    for t,row in rows.items():
        if active(t):
            u=next(w for a,w in row if a==tag)
            out[u]=out.get(u,Q(0))+mass(t)
    assert sum(out.values())==1
    return out
def pref(D,s):
    return sum((p for t,p in D.items() if t.startswith(s)),Q(0))
def target_eta(rows,s):
    return sum((mass(t)*Q(sum(w.startswith(s) for _,w in row),4)
                for t,row in rows.items() if active(t)),Q(0))
def audit():
    levels=[]; rows={'':[('A','00'),('A','01'),('A','10'),('B','11')]}
    for m in range(13):
        assert len(rows)==2**m
        src=[w for row in rows.values() for _,w in row]
        assert len(set(src))==len(src)==2**(m+2)
        assert all(len(row)==4 for row in rows.values())
        levels.append(rows)
        if m==12: break
        new={}
        for t,row in rows.items():
            zero,one=kids(t,row)
            assert sorted(w+b for _,w in row for b in '01')==sorted(w for _,w in zero+one)
            new[t+'0']=zero;new[t+'1']=one
        rows=new
    A=dist(levels[10],'A');B=dist(levels[11],'B')
    checks=0
    for n in range(7):
        for i in range(2**n):
            s=format(i,'0%db'%n) if n else ''
            va,vb=pref(A,s),pref(B,s)
            expected=[(3*va+vb)/4,(3*va+vb)/4,(va+vb)/2]
            for m in range(n+3,13):
                assert target_eta(levels[m],s)==expected[m%3],(m,s)
                checks+=1
            if n and s.endswith('1'):
                u=s[:-1]
                assert pref(A,u)==pref(A,u+'0')+pref(A,u+'1')
                assert pref(B,u)==pref(B,u+'0')+pref(B,u+'1')
    for tag,phase in [('A',1),('B',2)]:
        for m in range(1,11):
            if m%3!=phase:continue
            D=dist(levels[m],tag)
            for t,row in levels[m].items():
                if not active(t):continue
                s=next(w for a,w in row if a==tag)
                assert pref(D,s)>=mass(t)
                checks+=1
    assert checks==672,checks
    assert Q(1,2)*Q(1,4)+Q(1,2)*Q(1,3)==Q(7,24)
    print({'finite_fraction_checks':checks,'rows_through_output_depth':12,
           'cesaro_eta_11_delta_half':'7/24','result':'PASS_FINITE_SANITY_ONLY'})
if __name__=='__main__':audit()
