#!/usr/bin/env python3
"""Exact Fraction sanity for P4-S135, finite only."""
import json
from fractions import Fraction
def active(t): return all(b=="0" for i,b in enumerate(t) if i%3 in (1,2))
def audit(depth=12):
 rows={"":[("A","00"),("A","01"),("A","10"),("B","11")]}
 total=aa=ss=0
 for m in range(depth+1):
  words=[]
  for tau,row in rows.items():
   total+=1
   assert len(row)==4 and len({s for _,s in row})==4
   assert all(len(s)==m+2 for _,s in row)
   assert Fraction(4,2**(m+2))==Fraction(1,2**m)
   words += [s for _,s in row]
   if active(tau):
    assert [t for t,_ in row]==(["A","A","B","B"] if m%3==2 else ["A","A","A","B"])
    aa+=1
   else:
    assert [t for t,_ in row]==["P","P","S","S"]; ss+=1
  assert len(words)==len(set(words))==2**(m+2)
  if m==depth: break
  nxt={}
  for tau,row in rows.items():
   if active(tau):
    A=[s for t,s in row if t=="A"];B=[s for t,s in row if t=="B"]
    if m%3==0:
     z=[("A",a+"0") for a in A]+[("B",b+"0") for b in B]
     o=[("A",a+"1") for a in A]+[("B",b+"1") for b in B]
    elif m%3==1:
     z=[("A",A[0]+b) for b in "01"]+[("B",B[0]+b) for b in "01"]
     o=[("P",A[1]+b) for b in "01"]+[("S",A[2]+b) for b in "01"]
    else:
     z=[("A",A[0]+b) for b in "01"]+[("A",A[1]+"0"),("B",B[0]+"0")]
     o=[("P",A[1]+"1"),("P",B[0]+"1"),("S",B[1]+"0"),("S",B[1]+"1")]
   else:
    p,q,u,v=[s for _,s in row]
    z=[("P",p+b) for b in "01"]+[("S",u+"0"),("S",v+"0")]
    o=[("P",q+b) for b in "01"]+[("S",u+"1"),("S",v+"1")]
   assert {s for _,s in z+o}=={s+b for _,s in row for b in "01"}
   nxt[tau+"0"]=z;nxt[tau+"1"]=o
  rows=nxt
 return dict(result="PASS_SANITY_ONLY",levels=depth,output_cylinders=total,
  aligned_source_occurrences=4*total,active_nodes=aa,safe_nodes=ss,last_source_words=2**(depth+2))
if __name__=="__main__": print(json.dumps(audit(),indent=2))
