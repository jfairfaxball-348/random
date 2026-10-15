# P4-S154 — exact quantifier ledger

**PROVED INTERNALLY A154.1 (existing S003/S102/Rute transfer):**
∀ total computable G ∀x∈CR ∀s⊑x, `G|[s] injective ⇒ G(x)∈CR(G_*λ)`.
If in addition G is globally fair, then G(x)∈CR(λ). There is NO finite-fibre or additive-use assumption; injectivity of the entire *given neighbourhood* is additional and not computably recognizable from G in general.

**PROVED INTERNALLY A154.2:** ∀ total computable fair G ∀x∈CR,
`G(x)∉CR ⇒ ∀n ∃u,v∈[x|n] (u≠v ∧ G(u)=G(v))`.
Here the collision output G(u)=G(v) is NOT required to equal G(x). K_G is closed, NOT claimed effectively closed. S011 gives ∃CR Y on singleton F-fibre with Y∈K_F.

**FINITE SANITY ONLY:** ∀2,520 balanced 3→2 tables, output cylinders m=1..7 have exact fair masses, and complete fibres of T_f(vz)=f(v)z are cardinality exactly two. 640,080 fairness and 10,080 fibre checks. No infinite theorem inferred.

**FAILED A/E-08:** No uniform list, much less single F₂/e, known to catch an x∈R₂ from a bad same-x F₃ image of exactly-two actual inverses; 3:1↔2:2 q oscillations and the sharp paired four-cell budget remain unresolved.

**FAILED C/S-00:** No ∃ONE x∈R₂, G∈F₃ and rational d with d succeeds on G(x). S011 uses CR Y∉R₂; S135 traps source nonCR; S141 positive folds do not destroy CR.

**OPEN:** E-08; E-00=R₂⊆R₃ for arbitrary-use globally fair F₃; S-00=one strict witness; R₂=R₃ or R₂≠R₃. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
