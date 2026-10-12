"""Exact finite sanity checks for S109; never an infinite-fibre/randomness proof."""
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

counts = Counter()
def check(value, group):
    assert value, group
    counts[group] += 1

TABLES = tuple(t for t in itertools.product((0,1), repeat=4) if sum(t)==2)
check(len(TABLES)==6, "two_row_exhaustion")
four = tuple(t for t in itertools.product((0,1), repeat=8) if sum(t)==4)
types = Counter()
for t in four:
    row = [sum(t[2*i:2*i+2]) for i in range(4)]
    types[row.count(1)] += 1
    check(sum(row)==4, "four_row_exhaustion")
check(types=={4:16, 2:48, 0:6}, "four_row_exhaustion")
check(tuple(b if s==0 else a for s,a,b in itertools.product((0,1),repeat=3)) in four,
      "hybrid_example")

def words(n):
    return list(itertools.product((0,1), repeat=n))

# Build g from unlabeled lexicographic truth tables, independently of normal-form labels.
def build(depth, choose):
    levels = [{(0,): (), (1,): ()}]
    for m in range(depth):
        out = {}
        prev = levels[-1]
        inv = {}
        for sigma,tau in prev.items():
            inv.setdefault(tau,[]).append(sigma)
        for tau, parents in inv.items():
            parents.sort()
            table = TABLES[choose(tau)%6]
            for j,sigma in enumerate(parents):
                for b in (0,1):
                    out[sigma+(b,)] = tau+(table[2*j+b],)
        check(all(v==2 for v in Counter(out.values()).values()), "exact_two_prefix_prices")
        check(all(out[s][:-1]==prev[s[:-1]] for s in out), "prefix_consistency")
        levels.append(out)
    return levels

def positive_d(tau):
    # Positive rational martingale with changing nonconstant stake direction.
    d=Fraction(1)
    for m,b in enumerate(tau):
        sign = 1 if (sum(tau[:m])+m)%2==0 else -1
        d *= 1 + Fraction(sign*(1 if b==0 else -1),3)
    return d

def audit(levels):
    depth=len(levels)-1
    labels=[{(0,):0,(1,):1}]
    klevels=[{(0,):(0,), (1,):(1,)}]
    info={}
    for m in range(depth):
        inv={}
        for sigma,tau in levels[m].items():
            inv.setdefault(tau,[]).append(sigma)
        lab={}; kval={}
        for tau,parents in inv.items():
            p0,p1=sorted(parents, key=lambda p: labels[m][p])
            row0=[levels[m+1][p0+(b,)][-1] for b in (0,1)]
            row1=[levels[m+1][p1+(b,)][-1] for b in (0,1)]
            balanced=row0[0]!=row0[1]
            check(balanced==(row1[0]!=row1[1]),"dichotomy")
            info[tau]=(balanced,row0[0])
            for p in (p0,p1):
                for b in (0,1):
                    q=p+(b,)
                    out=levels[m+1][q][-1]
                    lab[q]=labels[m][p] if balanced else b
                    kval[q]=klevels[m][p]+(out if balanced else b,)
        labels.append(lab); klevels.append(kval)
        check(len(set(kval.values()))==len(kval),"K_level_bijection")
        for tau in words(m+1):
            check(sorted(lab[p] for p in levels[m+1] if levels[m+1][p]==tau)==[0,1],
                  "candidate_labels")

    # Simulate the scan from its own transcript; it must not inspect the held bit to choose.
    for x in words(depth+1):
        v=klevels[-1][x]
        h=0; emitted=(); reconstructed=(); read=set()
        for m in range(depth):
            bal,flag=info[reconstructed]
            q=m+1 if bal else h
            check(q not in read,"scan_no_repeat")
            read.add(q)
            bit=v[q]
            emitted += (bit,)
            reconstructed += (bit if bal else bit^flag,)
            if not bal:
                h=m+1
            check(read==set(range(m+2))-{h},"scan_read_set")
            check(labels[m+1][x[:m+2]]==v[h],"held_label")
            check(reconstructed==levels[m+1][x[:m+2]],"normal_form_identity")

    # Independent H evaluation over arbitrary scan transcripts, followed by level bijection.
    himages=[]
    for s in words(depth):
        tau=()
        for bit in s:
            bal,flag=info[tau]
            tau += (bit if bal else bit^flag,)
        himages.append(tau)
    check(len(set(himages))==2**depth,"H_level_bijection")

    # Build the uniform gated rational compiler and check the source martingale identities.
    D={():Fraction(1),(0,):Fraction(1),(1,):Fraction(1)}
    for m in range(depth):
        for sigma,tau in levels[m].items():
            bits=[levels[m+1][sigma+(b,)][-1] for b in (0,1)]
            for b in (0,1):
                D[sigma+(b,)]=D[sigma]*(positive_d(tau+(bits[b],))/positive_d(tau)
                                          if bits[0]!=bits[1] else 1)
            check(D[sigma+(0,)]+D[sigma+(1,)]==2*D[sigma],"rational_compiler_identity")
            check(D[sigma+(0,)]>0 and D[sigma+(1,)]>0,"compiler_positivity")
    # Finite version of saturation: two persistent prefixes cannot encounter a later fold.
    for tau in words(depth):
        candidates=[p for p,y in levels[-1].items() if y==tau]
        a,b=candidates
        r=next(i+1 for i in range(depth+1) if a[:i+1]!=b[:i+1])
        for m in range(max(0,r-1),depth):
            check(info[tau[:m]][0],"separated_survivors_force_balance")

# Exhaust every depth-two 6-table assignment (root and two output children).
for choice in itertools.product(range(6), repeat=3):
    def choose(tau, choice=choice):
        return choice[0] if not tau else choice[1+tau[0]]
    audit(build(2,choose))

# A much deeper source-dependent mixture: not claimed to have two infinite inverse points.
audit(build(9,lambda tau: (len(tau)*17 + sum((i+3)*b for i,b in enumerate(tau)))%6))

# Exact-two, two-lookahead countermodel: delete first bit, then swap adjacent tail bits.
def qprefix(sigma,m):
    return tuple(sigma[(i+1 if i%2==0 else i-1)+1] for i in range(m))
def odd_bet(tau):
    capital=Fraction(1)
    for i,b in enumerate(tau):
        if i%2:
            capital*=2 if b==0 else 0
    return (capital+1)/2
for m in range(1,10):
    check(set(Counter(qprefix(s,m) for s in words(m+2)).values())=={4},
          "two_lookahead_prices")
D=Fraction(1); zeros=(0,)*14
for n in range(2,13):
    tau=qprefix(zeros,n-2)
    s=zeros[:n]
    nxt=[qprefix(s+(b,),n-1)[-1] for b in (0,1)]
    if nxt[0]!=nxt[1]:
        D *= odd_bet(tau+(nxt[0],))/odd_bet(tau)
    check(D==1,"blanket_compiler_countermodel")
check(odd_bet((0,)*10)>1,"countermodel_output_gain")

result={"status":"PASS_FINITE_SANITY_ONLY","assertions":sum(counts.values()),
        "groups":dict(sorted(counts.items())),"balanced_four_state_tables":dict(types),
        "not_proved_by_computation":["infinite_fibres","actual_CR_witness","DP2","CP2","EQ","SEP"]}
print(json.dumps(result,indent=2))
Path(__file__).with_name("P4-S109_FINITE_AUDIT.json").write_text(json.dumps(result,indent=2)+"\n")

