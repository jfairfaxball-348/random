# P4-S170 — Quantifier audit

H1 positive (NOT PROVED): ∀same x∈CR\\MLR ∃finite k ∃TOTAL computable λ-preserving G with ∀complete y |G^-1{y}|<=k ∃TOTAL computable nonnegative exact-rational martingale d: sup_n d(G(x)|n)=∞. H1 negative (NOT PROVED): ∃ONE x∈CR\\MLR ∀finite k∀G∈F_k∀such d: sup_n d(G(x)|n)<∞.

B170: ∀TOTAL computable G ∀y (IF |G^-1{y}| is FINITE THEN ∀x∈G^-1{y} ∃finite s≺x that isolates x ∃partial functional Phi_s with Phi_s^y TOTAL=x). With y<=_T x also x≡_T y, nonuniform. NO uniform map y→s, no effective fair sheet weights, no successful martingale transfer.

C170: D=X\\{0^ω}, E=X\\{0^ω,10^ω}; P:D→E and inverse E→D are partial computable and bijective, preserve λ exactly for EVERY measurable output event. ∀y∈E exactly ONE inverse in D, and no y outside E occurs. ∀TOTAL continuous H ∃CR source x∈D: H(x)≠P(x); indeed contradiction from two CR sequences approaching zero. ∀x∈CR P(x)∈CR. P is NEVER asserted TOTAL or in F_k, even though it has a.e. singleton fibres.

D170: ∃ONE frozen Y∈CR, ONE F∈F2 with F(Y)∉CR, ∀N F_N∈F1 and F_N(Y)∈CR and |{j:F_N(Y)(j)≠F(Y)(j)}|=∞. For any fixed N; cannot replace with growing N for infinitely many wins.

Levels: INTERNAL proof; local exact finite sanity lengths 2..11 (4072 rows) only; external JLC 2025 Theorem40 STATEMENT_INSPECTED on HTML, not proof; hosted CI ABSENT_NOT_PASS, branch protection UNKNOWN_403, rulesets []; no Lean/Palomar, no Gate4 or Phase5.