# P4-S101 — Minimal claim and dependency matrix

2026-10-12. Internal written reconstruction, not independent verification.
All section references below are to `P4-S101_PROOF_DOSSIER.md`.

| Claim | Exact quantifiers / status | Direct dependencies | Original numbered proof |
|---|---|---|---|
| Geometry | Every total computable map has effective clopen cylinder preimages; every fair map is onto; ALL-output cardinal bound gives uniform finite prefix lists | §2.1 compactness and finite search; no literature premise | S001 Lemmas 1–2; S003 Lemma 1; S007 Lemma 1 |
| Scan geometry | For EVERY transcript, fibre equals free assignments to omitted coordinates; finite holes h give 2^h preimages | §2.3 freshness and finite-product measure | S008 model/Lemma 1; S032 Lemma 8 |
| k=1 preservation | Every F∈F₁ is a computable fair inverse pair; R₁=CR | §2.2; E-ISO (SRC-0015/THM-0038, STATEMENT_INSPECTED) | S001 Lemmas 1–4 and corollary |
| k=2 nonconservation | ∃original CR Y ∃total fair scan D∈F₂ ∃rational d succeeding on D(Y); destructive fibre singleton | §2.4; E-WTT (SRC-0067 ABSTRACT_INSPECTED / SRC-0068 STATEMENT_INSPECTED); no SRC-0061 | S011 Lemmas 1–6; S012 Theorem 1; S027 clipped normalization |
| A | ∀fixed finite h≥1,k≥2: OH_h=OH=R_k^scan | §3 frontier/colour/pull/fill/product proof; §2.3; k=1 preservation/E-ISO | S081 Lemma 2, Theorem A, Corollary A1 |
| Potential engine | For every total fair G, Ψ decreases in time, dominates conditional capital, and has exact refinement with γ | §4 finite clopen geometry and nonnegative rational martingale equation | S082 Lemmas 2.1–2.3 |
| Savings | Total rational savings d has active <2, drop <2, and bounded savings implies bounded original d₀ | §4; no literature lemma assumed | S082 Lemma 2.4 |
| Candidate bound | Sum of split weights ≤Ψ for one-hole raw scans or one raw candidate per distinct finite block beyond all active frontiers | §4; effective frontier §3; block inverses §1 | S082 Lemmas 3.1–3.2 |
| Effective nonMLR certificate | All completed guesses form an ORDINARY uniformly c.e. test with λ(V_i)≤2^{−(i+1)^2}; true states nested and positive | §5 partial syntax, ℓ_i/N_i counts, true-run termination and invariant; NO validity oracle in test | S082 Propositions 4.1–4.2 / Theorem 5.1 |
| B | ∃ONE z∉MLR ∀computable finite-block K: K(z)∈OH | §5 compactness and savings; effective test; E-ISO is needed in A but not this direct B construction | S082 Proposition 4.3, Theorems 4.4/5.1 |
| Shared-fix / fooling control | At EVERY finite true state, false resolution requires all r opposite fixes; relative λ(W)≤1/8 | §6 class-separated runs; §7 opposite-fix union; no independence between events | S083 Lemmas 3.1–3.2, 3.4–3.5 |
| Destroyer legality | G=F_T*∘D′ total computable fair, cardinal fibres ≤2 for EVERY output, and d* total rational | §6 bounded simulations, read-set invariant, §2.3 | S083 Lemmas 2.1/3.3 |
| C | ∃ONE z∈OH^blk∖MLR and G∈F₂ with G(z)∉CR; therefore R₂⊊OH | §7 common compactness, 4·7/8>2, every-limit-hold termination; §6 legality; §2.3 inclusion R₂⊆OH | S083 Lemma 3.6, Proposition 3.7, Theorem 3.8, Corollary 4.1 |
| Recoding consequence | D′(z)∈CR∖OH; OH^iso⊊OH^blk | Same C witness plus E-ISO for D′ preservation and §1 precomposition | S033 Theorem 2; S083 Corollary 4.2 |
| Null ambiguity safe | Partial singleton inverse has full-measure effective G_delta domain containing EVERY CR input after pullback | §2.5 explicit CR⇒Kurtz proof; E-ISO | S032 Theorem 3; S100 domain clarification |
| S084 boundary | G has balanced double fibres a.e.; same z is an exceptional singleton destroyer | §8 effective null-resolution test, restart martingale, output-measurability and flip symmetry | S084 Theorem 3 / Corollary 4 |

A–C have no unresolved internal premise. Literature inputs retain the access
levels stated above and are assumptions pending future primary-proof verification.
B and the strictness proof of C themselves use only their written construction;
E-ISO supports A, recoding consequences and the foundation. E-WTT supports the
separate k=2 foundation/OH⊊CR, not the existence of the C witness.

Out of package: S081 van Lambalgen, S083 R_tot=MLR / SRC-0071, S087–S090
restricted-family survival, unbounded-width or arbitrary-F₂ cheap-coordinate
claims, EQ/SEP, R₂ versus OH^iso, U(H), original X∈OH, fixed-S preservation,
Conjecture R. None is promoted by this reconstruction. Gate 4 NOT REVIEWED.
