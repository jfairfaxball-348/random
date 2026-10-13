#!/usr/bin/env python3
"""P4-S128 full finite-cylinder audit, not an infinite-fibre proof."""
from collections import Counter
from fractions import Fraction

def audit(c,steps,path,schedule):
    n=2**c; r=n-1
    root=[(format(i,f'0{c}b'),0 if i<2 else i-1,'main') for i in range(n)]
    tree={'':('main',root)}
    checks=incidences=0
    for m in range(steps):
        for tau in sorted(q for q in tree if len(q)==m):
            typ,state=tree[tau]
            assert len(state)==n
            if typ=='main':
                count=Counter(t for _,t,_ in state)
                assert count[schedule(m)]==2 and len(count)==r
                assert all(v==1 for k,v in count.items() if k!=schedule(m))
                old,new=schedule(m),schedule(m+1); b=path(m)
                kids={0:[],1:[]}
                dbl=sorted(w for w,t,k in state if t==old)
                if new==old:
                    kids[b].extend((dbl[0]+i,old,'pair') for i in '01')
                    kids[1-b].extend((dbl[1]+i,old,'pair') for i in '01')
                else:
                    kids[b].append((dbl[0]+'0',old,'solo'))
                    kids[1-b].append((dbl[0]+'1',old,'solo'))
                    kids[1-b].extend((dbl[1]+i,old,'pair') for i in '01')
                    for w,t,k in state:
                        if t==new:kids[b].extend((w+i,t,'pair') for i in '01')
                for w,t,k in state:
                    if t!=old and (new==old or t!=new):
                        kids[0].append((w+'0',t,'solo'))
                        kids[1].append((w+'1',t,'solo'))
                tree[tau+str(b)]=('main',kids[b])
                tree[tau+str(1-b)]=('safe',kids[1-b])
            else:
                pair=sorted(w for w,t,k in state if k=='pair')
                assert len(pair)==2
                kids={0:[],1:[]}
                for b,w in enumerate(pair):
                    kids[b].extend((w+i,-1,'pair') for i in '01')
                for w,t,k in state:
                    if k=='solo':
                        kids[0].append((w+'0',t,'solo'))
                        kids[1].append((w+'1',t,'solo'))
                for b in (0,1):tree[tau+str(b)]=('safe',kids[b])
            for b in '01':
                kind,child=tree[tau+b]
                assert len(child)==n and len(set(w for w,t,k in child))==n
                assert all(len(w)==m+c+1 for w,t,k in child)
                if kind=='safe':
                    assert Counter(k for w,t,k in child)=={'pair':2,'solo':n-2}
                assert Fraction(n,2**(m+c+1))==Fraction(1,2**(m+1))
                checks+=1;incidences+=n
        words=[w for q,(kind,ws) in tree.items() if len(q)==m+1 for w,_,_ in ws]
        assert len(words)==2**(m+c+1) and len(set(words))==len(words)
    return checks,incidences

if __name__=='__main__':
    cases=[(2,10,lambda i:0,lambda i:i%2),
           (2,10,lambda i:i%2,lambda i:[0,0,2,1,1,0][i%6]),
           (3,9,lambda i:(i//2)%2,lambda i:i%7)]
    total=[0,0]
    for c,m,p,s in cases:
        x,y=audit(c,m,p,s)
        total[0]+=x;total[1]+=y
        print('PASS',c,m,x,y)
    assert total==[5114,24544]
    print('PASS 5114 rational finite cylinders / 24544 source incidences; SANITY ONLY')
