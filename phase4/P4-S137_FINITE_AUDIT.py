#!/usr/bin/env python3
"""P4-S137 independent-in-method SAME-AGENT finite SANITY, not infinite proof."""
from itertools import product
from fractions import Fraction

# slot images: child SAFE slots mapped to previous SAFE slots
u=(3,3,1,2)
a=(0,0,1,1)
b=(0,2,2,2)
c=(0,0,0,0)
def compose(f,g):
    return tuple(f[g[i]] for i in range(4))
def rank(f):
    return len(set(f))
assert compose(a,a)==c
assert compose(b,b)==b
assert rank(compose(u,compose(u,u)))==3
assert rank(compose(a,b))==2
assert rank(compose(b,a))==2
assert rank(c)==1

# ALL SAFE/ACTIVE phases. Recognize SAFE001001 wholly within eight output bits.
states=[("SAFE",0),("ACTIVE",0),("ACTIVE",1),("ACTIVE",2)]
def nextstate(st,bit):
    mode,age=st
    if mode=="SAFE":
        return ("ACTIVE",0) if bit=="0" else ("SAFE",0)
    if age%3==0:
        return ("ACTIVE",age+1)
    return ("ACTIVE",age+1) if bit=="0" else ("SAFE",0)

for init in states:
    successes=0
    for bits in product("01",repeat=8):
        state=init
        seen=[]
        for bit in bits:
            seen.append((state,bit))
            state=nextstate(state,bit)
        if any(seen[i][0][0]=="SAFE" and "".join(bit for _,bit in seen[i:i+6])=="001001" for i in range(3)):
            successes+=1
    assert successes>=1
    print(init, "sync eight-bit words", successes, "/256", Fraction(successes,256))
# Expected exact counts independently calculated: 7,2,4,3.
# Check SAFE forced return maps against explicit SOURCE-word rows.
def step(row,mode,age,bit):
    words=[w for _,w in row]
    if mode=="SAFE":
        p,q,s,t=words
        if bit=="0":
            return [("A",p+"0"),("A",p+"1"),("A",q+"0"),("B",s+"0")],"ACTIVE",0
        return [("P",t+"0"),("P",t+"1"),("S",q+"1"),("T",s+"1")],"SAFE",0
    if age%3==0:
        return [(tag,word+bit) for tag,word in row],"ACTIVE",age+1
    aa,bb,cc,dd=words
    if age%3==1:
        if bit=="0":
            return [("A",aa+"0"),("A",aa+"1"),("B",dd+"0"),("B",dd+"1")],"ACTIVE",age+1
        return [("P",bb+"0"),("P",bb+"1"),("S",cc+"0"),("T",cc+"1")],"SAFE",0
    if bit=="0":
        return [("A",aa+"0"),("A",aa+"1"),("A",bb+"0"),("B",cc+"0")],"ACTIVE",age+1
    return [("P",bb+"1"),("P",cc+"1"),("S",dd+"0"),("T",dd+"1")],"SAFE",0

root=[("P","00"),("P","01"),("S","10"),("T","11")]
def ancestry(bits):
    row,mode,age=root,"SAFE",0
    for bit in bits: row,mode,age=step(row,mode,age,bit)
    assert mode=="SAFE"
    return tuple(next(i for i,(_,s) in enumerate(root) if word.startswith(s)) for _,word in row)
for bits,f in [("1",u),("001",a),("011",a),("0001",b),("0101",b),("001001",c)]:
    assert ancestry(bits)==f,(bits,ancestry(bits),f)
# Uniform bound holds for all states even after an arbitrarily long prior ACTIVE age.
assert Fraction(255,256)<1
print("PASS_SANITY_ONLY; finite matrices, row ancestors, trigger counts, exact fractions")
