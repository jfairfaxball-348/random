"""P4-S153 SANITY ONLY: left-shift surrogate, not S011 destruction."""
from itertools import combinations,product
def words(n): return ["".join(t) for t in product("01",repeat=n)]
def check(tab):
    u,N=3,1
    buckets={t:[] for t in words(N)}
    for s in words(u): buckets[tab[s]].append(s)
    assert all(len(w)==4 for w in buckets.values())
    b={}; k={}
    for t,ss in buckets.items():
        for i,s in enumerate(ss):
            b[s]=t+format(i,"02b")
            k[s]=t+format(i//2,"01b")
    assert len(set(b.values()))==8
    selected=words(3)[0]
    D_count={p:0 for p in words(5)}
    K_count={p:0 for p in words(5)}
    for s in words(3):
        for z in words(3):
            # Shift T(z)=z[1:]: fair cap-two but preserving CR.
            D=(b[s]+(z[1:] if s==selected else z))[:5]
            K=(k[s]+z)[:5]
            D_count[D]+=1; K_count[K]+=1
    assert all(c==2 for c in D_count.values())
    assert all(c==2 for c in K_count.values())
    assert all(b[s][:1]==tab[s] and k[s][:1]==tab[s] for s in b)
    return len(D_count)
if __name__=="__main__":
    checks=0
    w=words(3)
    for comb in combinations(w,4):
        one=set(comb)
        checks+=check({s:("1" if s in one else "0") for s in w})
    assert checks==2240
    print("PASS: 70 fair tables; 2240 output-prefix counts; finite SANITY ONLY")
