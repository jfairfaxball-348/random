#!/usr/bin/env python3
"""P4-S138 finite exact row/sibling sanity. Not an infinite proof or independent review."""
from fractions import Fraction
def G_children(row, st):
    if st == "S":
        p,q,s,t=[w for _,w in row]
        return ([("A",p+"0"),("A",p+"1"),("A",q+"0"),("B",s+"0")],"A0"),([("P",t+"0"),("P",t+"1"),("S",q+"1"),("T",s+"1")],"S")
    if st=="A0":
        return ([(a,w+"0") for a,w in row],"A1"), ([(a,w+"1") for a,w in row],"A1")
    a,b,c,d=[w for _,w in row]
    if st=="A1":
        return ([("A",a+"0"),("A",a+"1"),("B",d+"0"),("B",d+"1")],"A2"),([("P",b+"0"),("P",b+"1"),("S",c+"0"),("T",c+"1")],"S")
    return ([("A",a+"0"),("A",a+"1"),("A",b+"0"),("B",c+"0")],"A0"),([("P",b+"1"),("P",c+"1"),("S",d+"0"),("T",d+"1")],"S")
def H_children(row,st):
    a,b=row
    return (([a+"0",b+"0"],"P"),([a+"1",b+"1"],"S")) if st=="S" else (([a+"0",a+"1"],"S"),([b+"0",b+"1"],"S"))
G={"":([("P","00"),("P","01"),("S","10"),("T","11")],"S")}
H={"":(["0","1"],"S")}
for n in range(13):
    assert len(G)==len(H)==2**n
    gs=[w for row,st in G.values() for a,w in row]
    hs=[w for row,st in H.values() for w in row]
    assert len(gs)==len(set(gs))==4*2**n
    assert len(hs)==len(set(hs))==2*2**n
    assert all(len(w)==n+2 for w in gs)
    assert all(len(w)==n+1 for w in hs)
    assert all(len(row)==4 for row,st in G.values())
    assert all(len(row)==2 for row,st in H.values())
    if n in (8,10,12):
        ambiguous=sum(len({w[:2] for a,w in row})>1 for row,st in G.values())
        expected={8:Fraction(3,8),10:Fraction(61,256),12:Fraction(341,2048)}[n]
        assert Fraction(ambiguous,2**n)==expected
    if n==12:
        assert sum(st=="S" for row,st in G.values())==1519
        assert sum(st!="S" for row,st in G.values())==2577
        assert sum(st=="S" for row,st in H.values())==2731
        assert sum(st=="P" for row,st in H.values())==1365
    G={t+str(b):child for t,(row,st) in G.items() for b,child in enumerate(G_children(row,st))}
    H={t+str(b):child for t,(row,st) in H.items() for b,child in enumerate(H_children(row,st))}
print("P4-S138: exact finite row partitions and ambiguity sanity PASS through depth 12; NOT an infinite proof")
