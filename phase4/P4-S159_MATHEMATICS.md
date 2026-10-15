# P4-S159 — Effective relative inverse kernels, rational source finance and singular tilted posterior traps

2026-10-15. ONE owner-invoked Phase4 CAND-01 MATHEMATICS session, scoped INTERNAL SAME-AGENT work only. Entry independently pinned LIVE main `3bdd0e18269a6a63ef3bca472eb916c268420317` with tree `d4a0bfbe6cb5aec4713d4a735fafecb209772d10`; S158 actual authored sole-parent commit (parent 0651b04c968db3eea0ee25cb4a27115c4062e808), integrated via PR #58 by expected-head non-force fast-forward. There were no open PRs, no competing S159 branches/records. Hosted Actions run and check-run lists and individual commit status contexts empty = **ABSENT_NOT_PASS**; rulesets []; protection read 403 = **UNKNOWN_403**. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. Frozen S101–S103 A–C, original Y/M/H/X, DEF-0020, PA-0001 and existing grades are unchanged. No independent proof, originality, formalisation or paper claim.

Let Cantor space carry fair measure λ and let CR mean avoidance of all total nonnegative rational computable martingales. For a total computable globally fair map G with GIVEN computable common source-use u(m), write
  q_s(τ)=2^|τ| λ([s]∩G⁻¹[τ]),
an exact finite rational. We always have 0≤q_s≤1, q_ε=1, q_s=q_s0+q_s1, and q_s(τ0)+q_s(τ1)=2q_s(τ). F_k means at most k ACTUAL COMPLETE inverse streams over EVERY infinite output; R_k quantifies over all legal F_k observers. Finite aligned source cells are not genuine inverse streams.

## A159.1 — EFFECTIVE RELATIVE KERNEL COMPILER (conditional, internally proved)

**Hypotheses, explicitly NOT asserted universally.**
(H1) For EACH source prefix s and k≥1 a GIVEN total computable bound N(s,k) guarantees that for EVERY output word τ of length ≥N(s,k) and EVERY finite v,
  |q_s(τv)−q_s(τ)|≤2^-k.
This is an ALL-OUTPUT *uniformly effective* posterior Cauchy condition, stronger than pathwise eventual convergence. No finite-time exact equality is demanded.

(H2) A GIVEN total computable M(s)≥|s| and one rational α∈(0,1] have **relative support**: if κ_z[s] denotes the limit in (H1), then for ALL source s, ALL output τ with |τ|=M(s), and ALL z∈[τ],
  κ_z[s] ≥ α q_s(τ).
A mere absolute approximation without a relative lower bound does NOT imply (H2), especially when q_s(τ) is tiny. The comparison is required also off the candidate target output.

(H3) At one actual source x, the source-input price L_s−|s|, where s=x↾n, m=M(s) and L_s=max(n,u(m)), is bounded by a fixed finite B for INFINITELY MANY n. This is a witness-specific condition, NOT uniform across sources. No F_k cap is needed for the theorem itself.

**Claim.** For any total nonnegative rational computable output martingale d, construct effectively ONE total nonnegative RATIONAL source martingale e with e(ε)=1 such that for ALL x,n, putting s=x↾n, m=M(s), y=G(x),
  e(s) ≥ (31α/64) · 2^{-(max(n,u(m))−n)} D(y↾m),
where D is the exact positive strong-savings rational martingale associated to d in S157, D(ε)=1 and D(y↾m)→∞ on EVERY output y where d succeeds. Consequently (H1)–(H3) imply G(x)∈CR for every CR x satisfying (H3). The identity map is a legal F₂ observer, so this gives a *conditional* same-source F₂/e certificate, not a general E-08 resolution.

**Detailed effective proof and EXACT rationalisation.**

1. By (H1) the limits κ_z[s]=lim_m q_s(z↾m) exist uniformly in ALL z and effectively to arbitrary precision, with error ≤2^-k once m≥N(s,k). The finite source-child and output martingale identities pass to the limit. Thus κ_z[ε]=1, κ_z[s]=κ_z[s0]+κ_z[s1] for EVERY z, yielding a consistent probability kernel on source cylinders supported on actual inverse fibres (if z∉G([s]), compactness makes q_s(z↾m)=0 eventually). No global enumeration of fibre points is used.

2. Set μ_D[τ]=2^-|τ|D(τ), a computable probability measure on outputs, possibly singular relative to λ. Define η[s]=∫κ_z[s]dμ_D(z). Its values are computable nonnegative REALS, generally NOT exact rationals. To approximate η[s] within 2^-k, choose m≥N(s,k) and compute the FINITE rational sum
  A_m(s)= Σ_|τ|=m 2^-m D(τ) q_s(τ).
The supremum error bound for κ transfers through any probability μ_D. By source projectivity, η[ε]=1 and η[s]=η[s0]+η[s1] exactly. Thus η is a computable probability measure on source cylinders.

3. Rationalise, rather than silently treating computable reals as rational martingale values. Define ζ[s]=(η[s]+2^-|s|)/2. This is a computable probability measure with ζ[sb]≥2^{-(|s|+2)}>0. For |s|=n set ρ_s=ζ[s0]/ζ[s] and approximate it by an EXACT rational r_s satisfying |r_s−ρ_s|≤2^{-2n-8}; the previous strict bound ensures 0<r_s<1. Both ρ_s and 1−ρ_s are ≥2^{-(n+2)}, since ζ[s]≤1 and ζ[sb]≥2^{-(n+2)}. Hence each of r_s/ρ_s and (1−r_s)/(1−ρ_s) is at least 1−2^{-n-6}. Define a rational probability measure recursively: ż[ε]=1, ż[s0]=ż[s]r_s, ż[s1]=ż[s](1−r_s). Then at EVERY finite source word s,
  ż[s] ≥ ζ[s] ∏_{j<|s|}(1−2^{-j-6}) ≥ (31/32)ζ[s] ≥ (31/64)η[s].
The product lower bound follows from ∏(1−a_j)≥1−Σa_j and Σ_{j≥0}2^{-j-6}=1/32. Put e(s)=2^|s|ż[s]. It is ONE exactly RATIONAL total nonnegative computable source martingale, e(s0)+e(s1)=2e(s) on EVERY source parent and e(ε)=1.

4. Let x, s=x↾n, m=M(s), y=G(x), L=max(n,u(m)), τ=y↾m. Then [x↾L] ⊂ [s]∩G⁻¹[τ], so q_s(τ)≥2^{m-L}. By H2 every z∈[τ] has κ_z[s]≥α q_s(τ), whence
  η[s]≥α q_s(τ)μ_D[τ]≥α 2^{m-L}·2^-m D(τ)=α2^-L D(τ).
Thus e(s)≥(31α/64)2^{n-L}D(τ). Along infinitely many n with bounded L−n, m≥n→∞ and D(y↾m)→∞; e is unbounded on this SAME x. A hypothetical CR x with bad output cannot meet all three hypotheses and bounded-price recurrence.

This is a genuine extension of the *form* of S157's exact posterior kernel and finance to a computable-real limit, but it does NOT establish existence of the required H1/H2/M for an arbitrary F₃ map. In particular it does not solve E-08.

## B159.1 — QUARTER-GRID COLLAPSE (internally proved, hard limitation)

For fixed additive input lookahead c, after m+c≥|s| every q_s(τ) lies in {0,1/2^c,...,1}. Under H1, choose one computable K≥N(s,c+1) (and K+c≥|s|). For EVERY |τ|≥K and every v, |q_s(τv)−q_s(τ)|≤2^{-(c+1)}<2^-c; since both lie on the same 2^-c grid, they are EQUAL. Therefore M_exact(s)=max(N(s,c+1), |s|−c,0) is a computable all-output exact S157 EVCS cutoff. **For c=2, the new H1 hypothesis collapses to the OLD exact condition, even before H2**. Hence A159 adds possible arbitrary-use scope only; it cannot finance S135's q oscillations by renaming exact stabilisation as effective convergence. Conversely exact EVCS implies H1 and H2 with α=1; both conditional criteria agree in the fixed-grid regime.

## C159.1 — A STRICTLY POSITIVE SINGULAR-TILT COUNTERMODEL (internally proved using S135)

Use S135's ALREADY globally legal total additive-two fair F₃ map G and its effectively closed perfect null set T={y:y_(3j+1)=y_(3j+2)=0 for all j}. For the distinguished source-tag prefix s, q_s along EVERY y∈T cycles 3/4→3/4→1/2→3/4 forever: infinitely many aligned nonconstant changes. S135 independently proved BOTH actual inverse source points over each y∈T fail CR, so this is emphatically NOT a hierarchy separator.

Let d_T(ε)=1 be the globally total rational output martingale which at free coordinates 3j keeps capital and at forced coordinates 3j+1,3j+2 doubles on output 0 and goes to zero on output 1. Its induced computable probability μ_T[τ]=2^-|τ|d_T(τ) is supported on T (indeed free coordinates remain unbiased). Put D=(1+d_T)/2, still a globally TOTAL, STRICTLY POSITIVE rational martingale with root1, and μ_D=(λ+μ_T)/2. Let A_N be S158's effectively open set of outputs with ≥N aligned nonconstant changes in q_s. For EVERY N, T⊂A_N by the complete S135 cycle, so
  μ_D(A_N) ≥ μ_D(T)=1/2,
whereas by B158.1, λ(A_(2j+1))≤2^-j→0. Thus **no function f(t)→0 can uniformly bound μ_D(A_N) by f(λ(A_N)) even for ONE globally valid c2 cap-three observer, ONE source prefix, and ONE STRICTLY POSITIVE rational winning D**. The failure is due to the singular component of μ_D, not a defect in the fair-coin tail computation. A d that wins on T cannot be paid on x by unqualified source pulling-back; S135's source W already destroys those points.

For finite j, T↾3j comprises 2^j output cylinders of total λ mass 4^-j but full μ_T mass 1. Hence μ_D(T↾3j)=1/2+1/(2·4^j)≥1/2, an EXACT finite-cylinder check. The infinite identity needs continuity of measures and S135's complete construction, not the finite audit alone.

## D. Direct attempts on E-08/E-00 and strictness — unsuccessful with specific first failure

**Same source:** Start with G∈F₃ c2, one x∈R₂ and y=G(x) nonCR with EXACTLY two complete inverses. S141 requires positive source-local folding in EVERY joint input-output neighbourhood. S117's paired reservoirs and S135's exact 3:1↔2:2 transitions show no computable relative kernel or favorable price can be presumed. A159 assumes H1 and H2 rather than building them; for c2 H1 forces exact EVCS and therefore excludes the 3:1 oscillator. No new same-source F₂ map or martingale from general E-08 was found.

**Two hidden reservoirs:** A naive independent second deleted bit appended to S158 first-one release has FOUR complete preimages over outputs where both hidden bits are eventually redundant; it is an F₄ construction, not F₃. Conditional repair requiring the second reservoir only on a c.e. trigger was NOT validated on all sibling outputs, and could have compact limit ghosts, so no legal new F₃ construction is asserted. S135's legal F₃ construction remains the full-space oscillator control.

**Source-priced upcrossings:** The output martingale W_s from S158 is valid and exponentially wins on odd-quarter→half returns, but multiplying W_s(G(x)↾m) by source-prefix-dependent factors does not automatically preserve e(s0)+e(s1)=2e(s), since source bits can force output bits. The four-cell target/fallback inequality t·a+(4−t)·b≤4 continues at every four-aligned-cell stopping row. C159 exhibits a stronger failure of the proposed λ-tail→μ_D-tail path: even a strictly positive rational D puts ≥1/2 mass on infinitely volatile outputs. Neither fact proves a no-go for ALL possible F₂ compilers.

**Arbitrary-use E-00:** A159 handles arbitrary GIVEN computable u CONDITIONALLY under H1/H2 and recurring cheap use. It supplies no reduction from arbitrary use to c2, and artificial clock padding can inflate price. The central arbitrary-use obligation remains unsolved.

**Strictness:** ONE coupled x∈R₂, legal fair F₃ map G and rational output d defeating G(x) remains absent. S011's CR source Y is NOT R₂. Neither noncomputability of y nor two actual complete inverse streams ensures R₂ membership; S135 proves this failure directly. Do not reverse ∃x∀F₂ into ∀F₂∃x_F or count partial machines as certified legal maps.

## E. Validation and result scope

Finite exact arithmetic script P4-S159_FINITE_AUDIT.py checked 1,022 first-one fair rows through output level9; 8 explicit late-reveal branch identities; all 13 quarter-grid transition rows; 511 rationalised-kernel source parent splits together with relative lower domination through depth9; and 16 finite tilted T-branch identities. ALL PASS as FINITE SANITY ONLY. Infinite proofs above are separate and SAME-AGENT, no hosted CI or independent review. Source/gate status unchanged. **Result: A159/B159/C159 scoped internal theorems, E-08/E-00/S-00 and R₂=R₃ equality/strictness still OPEN; S160 future ONLY.**
