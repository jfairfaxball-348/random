#!/usr/bin/env python3
"""P4-S144 finite row sanity for already-proved S135 construction; NOT infinite proof."""
from fractions import Fraction
import json
def active(y):
    return all(y[i]=="0" for i in range(len(y)) if i%3 in (1,2))
def split(y,row):
    m=len(y)
    if not active(y):
        p=[w for t,w in row if t=="P"];s=[w for t,w in row if t=="S"]
        assert len(p)==len(s)==2
        return ([("P",p[0]+"0"),("P",p[0]+"1"),("S",s[0]+"0"),("S",s[1]+"0")],
                [("P",p[1]+"0"),("P",p[1]+"1"),("S",s[0]+"1"),("S",s[1]+"1")])
    a=[w for t,w in row if t=="A"];b=[w for t,w in row if t=="B"]
    if m%3==0:return ([(t,w+"0") for t,w in row],[(t,w+"1") for t,w in row])
    if m%3==1:
        assert len(a)==3 and len(b)==1
        return ([("A",a[0]+"0"),("A",a[0]+"1"),("B",b[0]+"0"),("B",b[0]+"1")],
                [("P",a[1]+"0"),("P",a[1]+"1"),("S",a[2]+"0"),("S",a[2]+"1")])
    assert len(a)==len(b)==2
    return ([("A",a[0]+"0"),("A",a[0]+"1"),("A",a[1]+"0"),("B",b[0]+"0")],
            [("P",a[1]+"1"),("P",b[0]+"1"),("S",b[1]+"0"),("S",b[1]+"1")])
rows={"":[("A","00"),("A","01"),("A","10"),("B","11")]}
v=[]
for n in range(10):
    assert len(rows)==2**n
    words=[w for r in rows.values() for t,w in r]
    assert len(words)==2**(n+2) and len(set(words))==len(words)
    assert all(len(r)==4 for r in rows.values())
    v.append(str(Fraction(sum(t=="A" for t,w in rows["0"*n]),4)))
    nxt={}
    for y,r in rows.items():
        a,b=split(y,r)
        assert len(a)==len(b)==4
        assert set(w for t,w in a+b)=={w+bit for t,w in r for bit in "01"}
        nxt[y+"0"]=a;nxt[y+"1"]=b
    rows=nxt
assert v==["3/4","3/4","1/2"]*3+["3/4"]
print(json.dumps({"status":"PASS_SANITY_ONLY","depths":10,
                   "q_A_zero_ray":v,"last_rows":512,
                   "last_source_cells":2048,"infinite_proof":"NOT_CHECKED"},indent=2))
