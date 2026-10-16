# P4-S169 — Quantifiers and type audit

**Positive H1:** ∀SAME x in CR\MLR ∃ONE finite k=k(x) ∃ONE TOTAL computable λ-preserving G:2^ω→2^ω with ∀infinite y |G⁻¹(y)|≤k ∃ONE TOTAL nonnegative exact rational computable martingale d with sup_m d(G(x)↾m)=∞.

**Negative H1:** ∃ONE SAME x∈CR\MLR ∀k≥1∀G∈F_k∀total exact rational d, sup_m d(G(x)↾m)<∞.

**B169 scan approximation:** ∀total computable no-repeat q ∀N∈N ∃UNIFORMLY computable F_N∈F1: ∀source x, F_N(x)↾N=F_q(x)↾N; ∀infinite y |F_N⁻¹(y)|=1; ∀finite τ λ(F_N⁻¹[τ])=2^-|τ|. Here N is fixed for each approximant, varying with requested precision for convergence. There is no generally fixed N for complete equality.

**B169 failure of closure:** ∃ONE frozen CR Y ∃one q with F_q∈F2 ∃one TOTAL exact rational d that wins on F_q(Y), while ∀N F_N(Y)∈CR. Neither CR preservation nor a fixed global fibre cap passes to this effective uniform limit.

**C169 degree explosion:** ∀N∀y, |T_N⁻¹(y)|=1; |T⁻¹(0^ω)|=2^aleph0, and |T⁻¹(y)|=1 for all y≠0^ω. No false promotion of T to F_k.

**D169 scoped source criterion:** ∀x∈CR with ∃an oracle procedure M computing EVERY x(j) without querying j (on the target oracle), ∃F∈F2 and ∃rational d winning on F(x). NOT ∀x∈CR\MLR such M exists.

**Scope and evidence:** H1/H2/H3 class equalities/strictness OPEN, H4 observer closure finding only, H5 global prime/modular work OPEN. Internal mathematics proof ≠ finite code sanity ≠ hosted CI ≠ independent/formal proof. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
