# P4-S170 — Validation and hostile audit

**Proof evidence:** SAME-AGENT INTERNAL mathematical argument in MATHEMATICS. No Lean, Palomar, hosted CI, external peer review, publication novelty or proof-inspected original Rute/Petrović source.

**Exact finite-prefix script (local Python 3):** for L=2..11 enumerate all binary words s of length L, let n be the first 1 index. On the L-word domain where n+1<L (exclude 0^L and 0^(L-1)1), compute P_L(s)=s[n+1] + 0^n + 1 + s[n+2:]. Check |domain|=|image|=2^L-2, no duplicates and exact image consists of words having a 1 at some coordinate after the first output bit. PASS ALL 4,072 inputs, 2..11. This verifies finite cylinder code algebra ONLY; it cannot verify topological continuity/nonextendibility, measure on infinite Borel events, or class-level H1.

**Reproduction:**
```python
from itertools import product
def P(s):
    n=s.find("1")
    if n<0 or n+1>=len(s): return None
    return s[n+1]+"0"*n+"1"+s[n+2:]
total=0
for L in range(2,12):
    domain=["".join(t) for t in product("01",repeat=L) if P("".join(t)) is not None]
    images=[P(s) for s in domain]
    target={"".join(t) for t in product("01",repeat=L) if "1" in "".join(t)[1:]}
    assert len(set(images))==len(domain)==2**L-2
    assert set(images)==target
    total+=len(domain)
assert total==4072
print("PASS",total)
```

**Hostile checks:** B170 requires *actual complete* finite fibre and one isolating input cylinder for the chosen y/x; the oracle y only semi-decides membership exclusion from EFFECTIVELY COMPACT image, not positive membership or uniform branch location. No inverse selector computable uniformly for every y is claimed. C170 is NOT total; exactly two outputs are absent from its range, and 0^omega is absent from its domain; measure loss zero, no global F_k cap claim. Its nonextension uses TWO families of CR inputs tending to SAME exceptional input, not two sources proposed for H1. Borel λ conservation follows by countably many equally weighted matched prefix cylinders. D170 uses a different finite hardcoded flip mask for each N if necessary, which is legitimate as a nonuniform contradiction, not an effective source compiler.

**External scope:** JLC 35(8) 2025 Randomness and invariance, Theorem40 and Definitions15–18 read on publisher HTML (STATEMENT_INSPECTED); proof of Theorem40 and exact Rute/Petrović antecedent construction NOT inspected. No external originality claim.

**GitHub entry:** S169 commit 16177e2a0f12cc39ca63f7b5f569d7569dd13ab3, tree 30ba0b9163268d695a39ac1249eb470e6b61b9cd, sole parent 909009..., PR #70 merged. No S170 branch/PR; check-runs [], statuses [], Actions [], rulesets []; protection API UNKNOWN_403. At completion recheck outgoing atomic commit, parent/tree, changed paths, branch/main, checks/status/jobs separately. ABSENT_NOT_PASS ≠ PASS.

**Gate/targets:** Gate3 PASS, Gate4 NOT_REVIEWED, Phase4 OPEN, Phase5 CLOSED. H1–H3 and unrestricted R2=R3 undecided, H4 observer distinction not randomness-class strictness, H5 exploratory.