# P4-S156 — quantifiers and proof status

**INTERNALLY PROVED CONDITIONAL A156.1:**
∀ integers c,h≥0 ∀ TOTAL computable fair additive-c G satisfying **globally supplied** CLS(c,h) ∀ total nonnegative rational computable martingales d ∃ uniform total rational SOURCE martingale e such that
∀x∈2^ω ∀n≥0,
e(x↾n)≥2^{-(c+h)}[d(G(x)↾(n+h))+1]/[d(ε)+1].
Then ∀x∈CR, G(x)∈CR. For this **restricted class**, take F₂=id and e as the all-output E-08 compiler.

**EXPLICIT ALGORITHM:** p=d+1, μ[τ]=2^{-|τ|}p(τ)/p(ε);
e(s)=2^{|s|}Σ_{|τ|=|s|+h}q_s(τ)μ[τ].
No oracle, no infinite limiting or non-rational computations. Complete inverse atoms of computed κ_y have measure ≥2^{-c} for EVERY x∈G⁻¹{y}. A fixed h must be GIVEN, not discovered.

**CONTRAPOSITIVE:** ∀ fair additive-c G with ∃x∈CR G(x)∉CR, ∀h∈N ∃ finite s,τ,v with |τ|≥|s|+h and q_s(τv)≠q_s(τ). No assertion that witnesses lie on the offending output y.

**UNPROVED:** ∀G∈F₃ additive-two, CLS holds (FALSE in light of S135 oscillator); an effective weaker local substitute on a hypothetical SAME x∈R₂; whole E-08 compiler; arbitrary-use E-00; one coupled ∃x∈R₂∃G∈F₃∃d success (S-00), R₂=R₃ or R₂≠R₃.

Finite 8,190 posterior / 63 projectivity / 120 domination assertions SANITY ONLY. Same-agent internal proof; hosted CI ABSENT_NOT_PASS, branch protection UNKNOWN_403. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. Frozen Y/M/H/X and source provenance unchanged.
