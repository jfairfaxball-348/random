#!/usr/bin/env python3
"""S166 finite sibling+forced B0 local sanity; NO claims of infinite validation."""
def step(row,mode,p):
    aa=[s for t,s in row if t=='A']; bb=[s for t,s in row if t=='B']
    if mode=='safe':
        a,b=[s for t,s in row if t=='P']; c,d=[s for t,s in row if t=='S']
        return (([('P',a+'0'),('P',a+'1'),('S',c+'0'),('S',d+'0')],'safe'),([('P',b+'0'),('P',b+'1'),('S',c+'1'),('S',d+'1')],'safe'))
    if mode==0:
        a,b,c=aa; q=bb[0]
        if p is None: return (([('A',a+'0'),('A',a+'1'),('A',b+'0'),('B',q+'0')],0),([('A',b+'1'),('A',c+'0'),('A',c+'1'),('B',q+'1')],0))
        w=([('A',a+'0'),('A',a+'1'),('B',q+'0'),('B',q+'1')],1)
        f=([('P',b+'0'),('P',b+'1'),('S',c+'0'),('S',c+'1')],'safe')
    else:
        a,b=aa; c,q=bb
        if p is None: return (([('A',a+'0'),('A',a+'1'),('B',c+'0'),('B',c+'1')],1),([('A',b+'0'),('A',b+'1'),('B',q+'0'),('B',q+'1')],1))
        w=([('A',a+'0'),('A',a+'1'),('A',b+'0'),('B',c+'0')],0)
        f=([('P',b+'1'),('P',c+'1'),('S',q+'0'),('S',q+'1')],'safe')
    return (w,f) if p==0 else (f,w)
def test(style):
    def pred(t):
        n=len(t)
        if style=='none':return None
        if style=='always':return 0
        if style=='periodic':return (n//3)%2 if n%3==2 else None
        if style=='late':return (n//5)%2 if n>7 and n%5==0 else None
        if style=='alternate':return (n//2)%2 if n%2 else None
    rows={'':([('A','00'),('A','01'),('A','10'),('B','11')],0)}
    checks=bzeros=0
    for n in range(12):
        allwords=[s for row,mode in rows.values() for t,s in row]
        assert len(allwords)==len(set(allwords))==2**(n+2)
        if n==11:break
        new={}
        for t,(row,mode) in rows.items():
            q=pred(t); pair=step(row,mode,q)
            src={s+b for z,s in row for b in '01'}
            both=[s for branch,m in pair for z,s in branch]
            assert len(both)==len(set(both))==8 and set(both)==src
            for bit,(child,phase) in enumerate(pair):
                new[t+str(bit)]=(child,phase)
                if mode==1 and q is not None and bit==q:
                    assert [s[-1] for label,s in child if label=='B']==['0']
                    bzeros+=1
            checks+=1
        rows=new
    assert checks==2047
    print(style,'PASS LOCAL',checks,'sibling allocations;',bzeros,'phase1 winner B0 cases')
for schedule in ('none','always','periodic','late','alternate'):test(schedule)
