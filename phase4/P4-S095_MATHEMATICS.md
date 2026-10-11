# P4-S095 — Closed bad-choice selection versus dense partial self-readers

2026-10-11. Phase 4 Mathematics ONLY; selected CAND-01. Incoming live main 4703cdf3c6cb88721771d49c05bcd32aef531985 (S094 sole atomic commit), sole parent f6733e313642001eb39998efb7dfe331da92261f (S093). No intervening commits; no open/recent PRs, Actions runs, check-runs or combined statuses at entry. S095 files and branch absent at entry. Session branch phase4/P4-S095-closed-bad-choice. Incoming prompt archived byte-for-byte in P4-S095_INCOMING_HANDOFF.md.

**Disposition: R₂ versus MLR remains UNRESOLVED after six linked gates.** Two rigorously limited results sharpen S094: (A) an arbitrary partial self-avoiding reader admits positive-measure EFFECTIVELY CLOSED wrong-or-diverge subconditions with asymptotically cheap conditional L¹ averages, even if divergence has empty clopen interior, but selection is not effective; (B) a dense-open convergence domain and a nowhere-dense positive-measure divergence class can still make EVERY clopen all-wrong substate capital-expensive at EVERY time, disproving the naive local-clopen repair. The gap between these facts and an EFFECTIVE non-MLR CR source is explicitly unresolved. No equality map or R₂ survivor was constructed.

## Gate 1: central quantifiers and frozen authority

Let F₂ be every everywhere-total computable measure-preserving G:2^ω→2^ω with |G⁻¹(y)|≤2 for ALL outputs. R₂={z∈CR: G(z)∈CR for every G∈F₂}. The central alternatives are:

(EQ) ∀z∈CR∖MLR ∃G∈F₂ ∃total rational computable martingale d which is unbounded on G(z).

(SEP) ∃z∉MLR ∀G∈F₂ ∀total rational computable martingale d: sup_t d(G(z)↾t)<∞.

S093 Theorem A identifies GOL with AR-cover: each z∈CR∖MLR is Turing-autoreducible after SOME computable fair homeomorphism. GOL is sufficient for EQ, NOT known necessary. Negating AR-cover requires z∈CR∖MLR∖AR^iso and is only a first step, NOT SEP. S094 refuted the explicitly unproved ASSCL; S093 conditional Proposition S must never be invoked as an operative construction.

Retained unaltered: MLR=R_tot⊆R_fin⊆R_k⊆R₂⊆OH^iso⊊OH^aff⊊OH^blk⊆OH^lin3⊆OH=OH_h=R_k^scan⊊CR (k≥2); MLR⊊R₂^cdz⊆R₂^dz⊆R₂^fd; R₂⊊R₂^cdz⊊R₂^fd and R₂⊊OH. All S084 predictable-error guards, S089 exact hit-cell Ψ(P,t), the K_mix/K′_mix preceding-control offset, and prior S001–S094 work remain frozen. CAND-01, PA-0001 and DEF-0020 unchanged.

## Gate 2: analytic partial-domain repair, and its effectiveness boundary

The next lemma is **PROVED AS EXISTENCE**, not an algorithm. It treats general partial readers rather than presupposing uniform convergence or divergence.

**Theorem A (effectively closed bad-choice balance).** Let K be any computable fair homeomorphism, Φ any partial binary Turing functional self-avoiding on input h, P a positive-measure effectively closed (Π⁰₁) subset of Cantor space, and f≥0 any integrable (L¹) real function. For every ε>0 there is h₀ such that for every h≥h₀ SOME effectively closed subcondition Q_{h,s}⊆P satisfies:

1. λ(Q_{h,s})≥(1/2−ε)λ(P)>0 (take 0<ε<1/2);
2. for every x∈Q_{h,s}, Φ^{K(x)}(h) either diverges or converges to a value DIFFERENT from K(x)_h;
3. (1/λ(Q_{h,s})) ∫_{Q_{h,s}} f dλ ≤ (1/λ(P))∫_P f dλ + ε.

The indices h,s and a Π⁰₁ index for Q_{h,s} exist; no effective search for an admissible s, measure lower bound or budget decision is asserted.

*Proof.* Let ψ_h=K⁻¹∘flip_h∘K. Since K⁻¹ has a computable modulus, ψ_h fixes every prescribed finite raw prefix for all sufficiently large h; λ is ψ_h-invariant. Approximation in L¹ by finite-cylinder simple functions gives ||1_P−1_P∘ψ_h||₁→0 and ||f−f∘ψ_h||₁→0. Put P_h=P∩ψ_h(P); this is nonempty Π⁰₁ for all large h, ψ_h(P_h)=P_h, and λ(P_h)→λ(P), ∫_{P_h}f→∫_P f.

On P_h, convergence of Φ^{K(x)}(h) is an effectively open set D_h (relative to P_h), invariant under ψ_h by self-avoidance. If it converges, the predicted bit is identical on x and ψ_h(x) while their K-bit at h differs, hence exactly ONE of the pair is wrong. If it diverges, BOTH diverge. Let W_h⊆P_h be the relatively effectively open wrong-convergence locus and F_h=P_h∖D_h the effectively closed divergence locus. Let V_h^0={x:K(x)_h=0}, a computable clopen set. The measurable set S_h=W_h ∪(F_h∩V_h^0) selects EXACTLY ONE member of each ψ_h-pair in P_h. Thus λ(S_h)=λ(P_h)/2 and ψ_h(S_h)=P_h∖S_h. By measure preservation,

  |avg_{S_h}(f)−avg_{P_h}(f)| ≤ ||f−f∘ψ_h||₁/λ(P_h) → 0.

Enumerate the wrong-convergence open set as increasing finite unions W_{h,s} of clopen cylinders (intersect P_h). Then S_{h,s}=(P_h∩W_{h,s}) ∪ (F_h∩V_h^0) is uniformly effectively closed IN (h,s), lies inside P, contains only bad outcomes, and increases to S_h. Monotone convergence of measures and absolute continuity of ∫ f imply λ(S_{h,s})→λ(P_h)/2 and avg_{S_{h,s}}f→avg_{S_h}f (the limit mass is positive). Choose h large and then s large to obtain all three displayed conditions. At each step the subset has positive measure, so finite nested iterations preserve compact nonemptiness. ∎

**Adversarial qualifications.** P need not be clopen. The no-interior Π⁰₁ divergence case is included and does not magically acquire a clopen substate. f may be a finite weighted sum of limiting protected savings bounds 2+B∞, which is integrable by S087; the theorem then balances that CONDITIONAL L¹ average. It does NOT bound S089's hit-cell Ψ on arbitrary closed states: indicators of whether G⁻¹[w] intersects a Π⁰₁ class and its class measure need not be decidable. It does NOT supply effective levels s, an effective ML-test, or a non-MLR survivor. Theorem A remains true for the S094 first-bit reader: selecting its cheap divergent 0-side and expensive wrong 1-side gives mean 1 for the sample biased first-bit capital, rather than choosing ONLY an expensive wrong state.

## Gate 2 continued: an exact dense-domain obstruction to the clopen repair

**Theorem B (dense convergent self-reader beats ALL clopen cheap wrong-or-diverge states).** In the IDENTITY frame K=G=id with P=2^ω, there exist one total rational computable nonnegative martingale d with d(∅)=1 and 0<d(σ)≤20/13<2 for all σ, and ONE self-avoiding partial binary reader Φ such that for EVERY h:
* the convergence domain D_h={x:Φ^x(h)↓} is effectively open dense, and its complement F_h is an effectively closed nowhere-dense set of POSITIVE measure;
* Φ^x(h)=0 on D_h; hence any nonempty clopen condition A on which Φ is wrong at h throughout satisfies Ψ_d(A,t)≥16/13 for EVERY t≥0;
* no nonempty clopen condition B is contained in F_h (so no clopen all-divergent branch).
But Ψ_d(P,t)=1 for every t. Therefore the natural S094 repair that asks for a cheap **clopen** all-wrong or all-divergent subcondition fails for every h and ε<3/13, even with dense convergence, a fixed bounded savings martingale (A=d<2,B=0), arbitrarily high h, and unrestricted choice of comparison time.

*Construction.* Partition ℕ into consecutive blocks B_n, n≥1, of lengths n+10. Let E_n be the clopen event that ALL bits in B_n are 1. Then U=∪_{n≥1}E_n is effectively open dense and λ(U)≤∑2^{−n−10}=2^{−10}. Let m_n(σ) be the fair-coin cylinder martingale that multiplies by 2 for every 1 already read in B_n and becomes 0 upon the first 0 of B_n; before that block starts it equals 1, and after all 1s it equals 2^{n+10}. Define

  r(σ)=1/2 + ∑_{n≥1}2^{−n−1}m_n(σ).

Only finitely many blocks meet σ; all not-yet-started terms have an exactly computable geometric tail. Thus r is an EXACT rational computable nonnegative martingale with r(∅)=1. At the end of every E_n, its n-th summand is 2^{−n−1}2^{n+10}=512. Let τ(x) be the first prefix time r(x↾t)≥4, or ∞, and m(σ)=r(σ↾min(|σ|,τ(σ))) its stopped martingale. Because every nonnegative fair martingale obeys r(σb)≤2r(σ), 0≤m(σ)≤8 and m(∅)=1. Each x∈U hits τ<∞, with m∞(x)≥4. Finally set d(σ)=(12+m(σ))/13. It is rational computable, fair, starts at 1, and is bounded by 20/13<2. It has uniformly integrable limit d∞.

For each input h, Φ queries only blocks B_n NOT containing h, sequentially searching for an E_n witness, and outputs 0 at the first one; otherwise diverges. Thus it never queries x_h. Its convergence domain U_h=∪_{n:h∉B_n}E_n is effectively open dense (infinitely many future blocks remain), and F_h=2^ω∖U_h is Π⁰₁ nowhere dense, with λ(F_h)≥1−2^{−10}>0. The wrong locus is U_h∩{x_h=1} and is effectively open.

For an arbitrary clopen all-wrong A⊆U_h∩{x_h=1}, necessarily A⊆U. The bounded stopped martingale satisfies m_t(w)=E[m∞|[w]] by bounded martingale convergence. Because m∞≥4 on U, m_t(w)≥4λ(A∩[w])/λ[w]. Let H_t(A) be the union of all length-t cylinders meeting A, so λ(H_t(A))≥λ(A). S089's *hit-cell*, NOT simply conditional-average, potential obeys

  Ψ_d(A,t) = (1/λA)∑_{|w|=t, [w]∩A≠∅}2^{−t}d(w)
  ≥ (12/13)λ(H_t(A))/λA + (4/13)
  ≥ 16/13.

For P=whole space all cells are hit, so Ψ_d(P,t)=d(∅)=1. F_h has no clopen interior. This proves the quantified counterexample. ∎

This strictly strengthens the S094 first-bit obstruction: a clopen divergence escape need not exist at all. It does NOT refute Theorem A: the positive-measure Π⁰₁ divergence class is available for a closed, but not clopen, bad-choice requirement.

## Gate 3: attempt at CR∖MLR∖AR^iso

Use S093 Theorem A to enumerate requirements (K_e,Φ_e,h₀). For a finite true guessed prefix, Theorem A allows a positive-measure Π⁰₁ condition satisfying the e-th wrong-or-diverge requirement at some h≥h₀ while keeping the conditional integral of ANY fixed integrable protection density f within a summable ε budget. Repeating over e and h₀ with ε_i summable yields nested nonempty compact conditions and a nonempty limit class. For protection, f could be a nonnegative weighted sum of S087 integrable savings ceilings 2+B∞ for every valid computable martingale. This makes the ANALYTIC survival account plausible even against Theorem B's dense reader.

**The construction STOPS HERE.** The selected s and the positivity/capital inequalities are not uniformly computably searchable. Most critically, the resulting countable family of Π⁰₁ conditions is not shown to have a uniformly effective enumeration giving a Martin-Löf test; a singleton or intersection selected using arithmetical true-path information can be ML-RANDOM. Nonemptiness and conditional L¹ bounds alone are not a source z∈CR∖MLR. S082's guessed-run proof uses decidable finite-clopen hit-cell potentials and an effective bound on branch measure. Theorem A does not supply their Π⁰₁ analogues. No valid first separated witness z∈CR∖MLR∖AR^iso is established.

A proposed shortcut of assuming every positive-measure effectively closed condition contains a CR non-MLR point is false: for a universal ML test (V_n), the positive-measure Π⁰₁ set 2^ω∖V_m (any m with λ(V_m)<1) contains ONLY MLR points. Thus positive Π⁰₁ forcing alone has no non-MLR guarantee.

## Gate 4: full F₂ survival test (no candidate to promote)

Theorem A protects only a CONDITIONAL L¹ density for chosen closed states and reader failure requirements. It neither maintains the S082 all-strategy Ψ potential nor establishes uniform survival under all everywhere-total fair global-two-fibre maps. A legitimate SEP candidate must simultaneously neutralize S084's computably random ENTIRE predicted-error streams (not independent fair coins); fractional one-hole martingales; all frame transports including K_mix/K′_mix with the preceding-control offset; all genuinely non-scan maps and phantom fibres; and the precise ∃z∀G∀d quantifiers. This session has no such candidate, no all-map capital bound and no new inclusion.

## Gate 5: attack equality independently

Attempt A: From a failing universal ML test derive a frame K and a self-avoiding autoreduction on each source. This is exactly AR-cover by S093 Theorem A and still lacks an orientation mechanism; the universal test also covers both hold partners (S092 Proposition 3). The fact that Theorem A supplies bad choices on a positive-measure class is consistent with every MLR point being non-autoreducible and gives no counterexample inside CR∖MLR.

Attempt B: Let a computable non-orientation G∈F₂ carry the non-MLR information into a computably detectable output martingale. On an infinitely resolving scan, S084 Theorem 1 forces any computably predictable error subsequence of G(z)∈CR to be a CR error stream, with limiting frequency 1/2, and restart wagers must absorb infinitely many wrong predictions. A fixed positive per-bet edge cannot simply be assumed. Non-scan G requires global totality, exact fairness and fibre≤2 for EVERY transcript/output, not just the target's fibre. No construction satisfying these constraints and universal source coverage was found. Failure here proves NEITHER EQ nor SEP.

## Gate 6: adversarial validation, remaining implication

Validated symbolically: (A) ψ_h's high-coordinate invariance follows from computable homeomorphic inverse modulus; Π⁰₁ P_h=P∩ψ_hP is ψ_h-invariant and approaches P in measure; wrong and divergence pairwise law uses syntactic self-avoidance; W_{h,s} finite clopen, S_{h,s} Π⁰₁, λ limit half and L¹ limit give positive cheap conditions. The theorem's ε bound presupposes ε<1/2 for its positive lower mass; for arbitrary large ε simply replace it with min(ε,1/4). (B) exact geometric tail for r; martingale optional stopping; overshoot bound 8; d(∅)=1 and d≤20/13<2; U_h dense and F_h positive; m_t=E[m∞|prefix] is legal by bounded convergence; the hit-cell lower bound is valid AT SMALL AND LARGE t and for ALL clopen wrong A. The dense reader never queries h. Arbitrary positive weights multiply the cost gap: ε<w·3/13 is impossible in Theorem B. An auxiliary exact Python Fraction audit checks 3,447 finite identities/instances (P4-S095_DENSE_READER_AUDIT.py), PASS; it does NOT verify an infinite randomness claim. Written self-review, not Lean, hosted CI, independent referee or proof assistant.

**PROVED:** Theorem A non-effective Π⁰₁ wrong-or-diverge L¹ selection; Theorem B dense-domain counterexample to ALL clopen repair. **REFUTED:** S094-style blanket local-clopen cheap wrong-or-diverge lemma. **CONDITIONAL/INCOMPLETE:** effective arithmetical closed-class stage choice plus computable ML-null branch coding. **UNRESOLVED:** R₂=MLR or a strict survivor; AR-cover/GOL or its negation; R₂ vs OH^iso; U(H), X∈OH, fixed-S preservation; Conjecture R. Original CR Y, unchanged globally clipped wtt M, repeated three-bit H (matrix rows 101,110,111) and X=H⁻¹Y preserved. Sources SRC-0015,0019,0028,0060,0069–0074 at recorded levels; no new source, openness, novelty, priority, outreach or publication claim. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.
