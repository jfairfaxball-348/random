"""P4-S120 finite toy inverse/posterior audit + rational finite-edit identity.
Finite sanity ONLY; infinitary proofs in P4-S120_MATHEMATICS.md."""
from itertools import product
from fractions import Fraction

TERMS=(("101",5),("001",7),("0110",8))
def trigger(out):
    return any(out.startswith(s) and len(out)>=stage for s,stage in TERMS)
def g(src,m):
    a=src[0]; u=src[1:]; out=""; pos=0; released=False; pending=False
    for j in range(m):
        if not released and trigger(out):
            out+=a; released=True; pending=True
        else:
            if pending: pos+=1; pending=False
            out+=u[pos]; pos+=1
    return out
checks=0
for m in range(1,13):
    fibers={"".join(p):[] for p in product("01",repeat=m)}
    for p in product("01",repeat=m+1):
        s="".join(p); fibers[g(s,m)].append(s)
    for y,ss in fibers.items():
        assert len(ss)==2; checks+=1
        t=next((j for j in range(m) if trigger(y[:j])),None)
        expected=1 if t is None else (2 if y[t]=="0" else 0)
        assert sum(x[0]=="0" for x in ss)==expected; checks+=1
        if m>1:
            assert all(g(x[:m],m-1)==y[:m-1] for x in ss);checks+=2
assert checks==32756

def d(s):
    return Fraction(2**len(s)) if set(s)<={"0"} else Fraction(0)
def mix(s):
    n=len(s); ans=Fraction(0)
    for bs in product((0,1),repeat=n):
        t="".join(str(int(ch)^b) for ch,b in zip(s,bs))
        w=Fraction(1)
        for i,b in enumerate(bs):
            p=Fraction(1,2**(i+2));w*=p if b else (1-p)
        ans+=w*d(t)
    return ans
checks2=0
for n in range(8):
    for word in product("01",repeat=n):
        s="".join(word)
        assert (mix(s+"0")+mix(s+"1"))/2==mix(s)
        checks2+=1
assert checks2==255
print("S120 FINITE SANITY PASS",checks,"inverse/posterior assertions;",checks2,"rational martingale assertions")
