"""Finite exact sanity audit, S110. Not an infinite-randomness proof."""
from itertools import product
from collections import Counter
from fractions import Fraction
import json
counts=Counter()
def check(v,k):
    assert v,k
    counts[k]+=1
def words(n): return product((0,1),repeat=n)
def trigger(y):
    j=len(y)//2
    return int(j%3 != 2 and ((sum(y)+j)%3 != 1))
def out(x,m,policy):
    a=x[0];u=x[1:];y=[]
    for j in range((m+1)//2):
        t=policy(tuple(y))
        pair=u[2*j:2*j+2]
        check(len(pair)==2,"enough_lookahead")
        if a==0 and t: pair=pair[::-1]
        y+=pair
    return tuple(y[:m])
def inverse(y,a,policy):
    u=[]
    for j in range(len(y)//2):
        s=tuple(y[2*j:2*j+2]);t=policy(tuple(y[:2*j]))
        u.extend(s[::-1] if a==0 and t else s)
    return (a,)+tuple(u)
policies={"always":lambda y:1,"never":lambda y:0,"dynamic":trigger}
for name,policy in policies.items():
    for m in range(1,9):
        fibres={}
        for x in words(m+2): fibres.setdefault(out(x,m,policy),[]).append(x)
        check(len(fibres)==2**m,"image_surjective")
        for tau,candidates in fibres.items():
            check(len(candidates)==4,"exact_four_prefix_prices")
            for x in candidates:
                check(out(x,m-1,policy)==tau[:-1],"consistency")
            if m<8:
                rows=[]
                for x in candidates:
                    b0=out(x+(0,),m+1,policy)[-1]
                    b1=out(x+(1,),m+1,policy)[-1]
                    rows.append("P" if b0!=b1 else "C"+str(b0))
                check(rows.count("P") in (0,2),"permutive_row_cardinality")
                expected=(["C0","C1","P","P"] if m%2==0 and policy(tau) else ["C0","C0","C1","C1"])
                check(sorted(rows)==sorted(expected),"all_nodes_exact_transition_shape")
        for y in words(m if m%2==0 else m-1):
            if not y:continue
            for a in (0,1):
                x=inverse(y,a,policy)
                check(out(x,len(y),policy)==y,"global_inverse_prefix")
            check(inverse(y,0,policy)!=inverse(y,1,policy),"distinct_keys")
def d(tau):
    capital=Fraction(1)
    for j,b in enumerate(tau):
        sign=1 if (j+sum(tau[:j]))%2==0 else -1
        capital*=1+Fraction(sign*(1 if b==0 else -1),3)
    return capital
for j in range(4):
    for s in words(2*j):
        v=d(out((0,)+s,2*j,trigger))
        children=[d(out((0,)+s+q,2*j+2,trigger)) for q in words(2)]
        check(sum(children)/4==v,"four_to_one_block_martingale")
        check(v>0 and all(z>0 for z in children),"block_martingale_positive")
result={"status":"PASS_FINITE_SANITY_ONLY","assertions":sum(counts.values()),
"groups":dict(sorted(counts.items())),"policies":list(policies),
"not_proved_by_finite_computation":["fairness_for_all_infinite_outputs","exact_two_infinite_fibres","CR_conservation","DP2","CP2","EQ","SEP"]}
print(json.dumps(result,indent=2))
if __name__=="__main__":
    from pathlib import Path
    Path(__file__).with_name("P4-S110_FINITE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n")
