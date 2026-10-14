#!/usr/bin/env python3
"""S136 exact finite SANITY only; does not prove any infinite assertion."""
from collections import Counter
from fractions import Fraction

def step(state, age, row):
    z=[[],[]]
    def add(side,tag,word): z[side].append((tag,word))
    if state=="SAFE":
        assert [t for t,_ in row]==["P","P","S","T"]
        p,q,s,t=[w for _,w in row]
        for tag,w in [("A",p+"0"),("A",p+"1"),("A",q+"0"),("B",s+"0")]:add(0,tag,w)
        for tag,w in [("P",t+"0"),("P",t+"1"),("S",q+"1"),("T",s+"1")]:add(1,tag,w)
        modes=[("ACTIVE",0),("SAFE",0)]
    elif age%3==0:
        for tag,w in row:
            add(0,tag,w+"0");add(1,tag,w+"1")
        modes=[("ACTIVE",age+1),("ACTIVE",age+1)]
    elif age%3==1:
        a,b,c,d=[w for _,w in row]
        assert [t for t,_ in row]==["A","A","A","B"]
        for tag,w in [("A",a+"0"),("A",a+"1"),("B",d+"0"),("B",d+"1")]:add(0,tag,w)
        for tag,w in [("P",b+"0"),("P",b+"1"),("S",c+"0"),("T",c+"1")]:add(1,tag,w)
        modes=[("ACTIVE",age+1),("SAFE",0)]
    else:
        a,b,c,d=[w for _,w in row]
        assert [t for t,_ in row]==["A","A","B","B"]
        for tag,w in [("A",a+"0"),("A",a+"1"),("A",b+"0"),("B",c+"0")]:add(0,tag,w)
        for tag,w in [("P",b+"1"),("P",c+"1"),("S",d+"0"),("T",d+"1")]:add(1,tag,w)
        modes=[("ACTIVE",age+1),("SAFE",0)]
    assert len(z[0])==len(z[1])==4
    assert sorted(w for side in z for _,w in side)==sorted(w+b for _,w in row for b in "01")
    return [(modes[i][0],modes[i][1],z[i]) for i in (0,1)]

def main():
    level={"":("SAFE",0,[("P","00"),("P","01"),("S","10"),("T","11")])}
    count=inc=active=safe=0
    for m in range(13):
        sources=[]
        for y,(mode,age,row) in level.items():
            count+=1;inc+=4
            active+=(mode=="ACTIVE");safe+=(mode=="SAFE")
            assert len(row)==4 and all(len(w)==m+2 for _,w in row)
            if mode=="SAFE":assert [t for t,_ in row]==["P","P","S","T"]
            else:assert [t for t,_ in row]==(["A","A","A","B"] if age%3!=2 else ["A","A","B","B"])
            sources.extend(w for _,w in row)
        assert len(set(sources))==len(sources)==2**(m+2)
        nxt={}
        for y,(mode,age,row) in level.items():
            for bit,result in enumerate(step(mode,age,row)):
                nxt[y+str(bit)]=result
        level=nxt
    assert (count,inc,active,safe)==(8191,32764,5130,3061)
    assert len(sources)==16384
    counts=Counter(v[0] for v in level.values())
    assert (counts["ACTIVE"],counts["SAFE"])==(5109,3083)
    # Finite-state stationary output-law mass, exact Fraction:
    S,A0,A1,A2=Fraction(3,8),Fraction(1,4),Fraction(1,4),Fraction(1,8)
    assert S+A0+A1+A2==1
    assert (S,A0,A1,A2)==((S+A1+A2)/2,(S+A2)/2,A0,A1/2)
    print("PASS_SANITY_ONLY", count,inc,active,safe,counts)
if __name__=="__main__":main()
