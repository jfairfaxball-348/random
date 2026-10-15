# P4-S161 — singular-posterior weighted finance and an unavoidable regularisation failure

2026-10-15. One owner-authorised Phase4 CAND-01 mathematics session. ENTRY LIVE main `0cd8e83e7846b7a938f1682039f163e82a1e2ed4`, tree `7ede66f4dfbaffa3ae87fe59ac3b407924b8dfc3`; S160 authored sole-parent commit (parent `247e73d651e0d8553f04f28f4a72b749798ad0ff`), PR #60 merged at identical SHA by the earlier expected-main non-force fast-forward. S161 had no competing branch, record, or open PR at entry. Zero hosted Actions runs/checks/individual status contexts = ABSENT_NOT_PASS, rulesets [], protection read 403=UNKNOWN_403. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. Frozen S101–S103 A–C, Y/M/H/X, DEF-0020, PA-0001 and source-grade rules untouched. Proof INTERNAL same-agent, not independent referee or novelty certification.

Notation: λ is fair product measure on Cantor space. F_k is the class of TOTAL computable λ-preserving self-maps having at most k ACTUAL COMPLETE preimages above EVERY output; R_k={x:∀F∈F_k, F(x)∈CR}. For G additive-use-two, source prefix s, output prefix τ of length m, let q_s(τ)=2^m λ([s]∩G⁻¹[τ]). For fixed s, q_s(τ0)+q_s(τ1)=2q_s(τ); these are conditional λ-posteriors, NOT true fibre-count ratios.

## A161.1 — the singular tilted source marginals do not converge

Use the ALREADY globally proved fair additive-two F₃ map G of S135 with the effective perfect null tree T={y:y_(3j+1)=y_(3j+2)=0}, and its two true inverse streams over every y∈T (three streams for y∉T). S135 constructs four aligned input cells above EACH output τ at depth m; its distinguished source prefix s=11 is the initial B sector. Directly from S135's complete child-row induction, for EVERY τ compatible with T and every m,
 q_11(τ) = 1/4 if m≡0 or 1 (mod 3), and =1/2 if m≡2 (mod 3).
This assertion includes all free-bit choices along T, not only 0^ω. Outside T other cells can appear; no off-T restriction is needed below.

Let d_T be S135's total exact rational output martingale that holds at free positions and doubles on a forced 0, losing on forced 1; μ_T[τ]=2^(-m)d_T(τ) is the computable probability measure on T, with μ_T(T)=1 and λ(T)=0. For ANY supplied rational 0<δ<1 set
 D_δ(τ)=δ+(1−δ)d_T(τ),  μ_δ=δλ+(1−δ)μ_T.
D_δ is one TOTAL strictly positive exact rational output martingale, D_δ(ε)=1, and D_δ(y↾3j)=δ+(1−δ)4^j→∞ on EVERY y∈T.

For each finite m define the (fully computable rational) source probability measure
 η_m[s]=∫_[s]D_δ(G(z)↾m)dλ(z)
       = Σ_(|τ|=m) μ_δ[τ] q_s(τ).
Every η_m is projective in s and satisfies η_m[ε]=1. The global fairness identity gives Σ_(|τ|=m)2^(-m)q_11(τ)=λ[11]=1/4. On the supported T level-m cells q_11 is constant, so Σ μ_T[τ]q_11(τ) equals 1/4,1/4,1/2 at phases m≡0,1,2. Therefore the EXACT identities for EVERY m are
 η_m[11]=1/4  (m≡0,1 mod 3);
 η_m[11]=(2−δ)/4  (m≡2 mod 3).
For δ=1/2 this is 1/4,1/4,3/8, repeatedly, with persistent gap 1/8. More generally its oscillation diameter (1−δ)/4>0. Hence η_m[11] is NOT Cauchy; no computable or even non-effective stagewise limit η[s]=lim_m η_m[s] exists for ALL s.

This is a **specific no-go for the canonical finite-stage posterior-marginal limit** proposed as a source finance mechanism. It is NOT a proof that no alternative computable projective source measure, modified kernel, or F₂ detector exists. In particular it cannot be extrapolated to hypothetical CR or R₂ inverse points: S135 separately constructs ONE rational source martingale W beating BOTH actual inverse streams of EVERY y∈T.

## B161.1 — singular weighted conditional odds and essential-floor collapse

For a T-compatible prefix τ of length m, the number of free positions is a(m)=#{i<m:i≡0 (mod3)}=ceil(m/3). Thus λ[τ]=2^(-m), μ_T[τ]=2^(-a(m)), and the likelihood ratio r_m=μ_T[τ]/λ[τ]=2^(m−a(m)). If the NEXT position m is forced (m≡1 or2 mod3), T always takes child 0 and
 μ_δ(τ0 | τ) = [δ/2+(1−δ)r_m]/[δ+(1−δ)r_m]
             =1−δ/[2(δ+(1−δ)r_m)].
At m=3j+1, r_m=2·4^j; at m=3j+2, r_m=4·4^j. When δ=1/2 the probabilities of the forced 0 are, respectively,
 1−1/(2+4·4^j),   1−1/(2+8·4^j),
starting (5/6,9/10), then (17/18,33/34), then (65/66,129/130); they tend to 1, rather than 1/2. At the free position m≡0 the conditional probability of either bit is 1/2.

Let A_N be S158's effectively open event of at least N nonconstant q_11 changes. T⊂A_N for EVERY N, from S135's perpetual 1/4→1/2→1/4 cycle. Consequently μ_δ(A_N)≥1−δ for EVERY N, although λ(A_(2j+1))≤2^(-j). For δ=1/2 this is the S159 1/2 obstruction; here the exact odds explain how a positive singular part carries all repeated returns. These are μ_δ-output probabilities and do NOT form a total rational SOURCE martingale on a CR x.

Since d_T tends to zero λ-a.e. off T, D_δ,m→δ λ-a.e., but ∫D_δ,m dλ=1 while ∫δ dλ=δ<1; thus no L1 limit. Along y∈T the essential infimum of the a.e. terminal density δ on every [y↾3j] is δ, whereas D_δ(y↾3j)=δ+(1−δ)4^j. The ratio tends to 0. This directly refutes the attempt to use the λ-a.e. limiting density as an A160 conewise profitable floor on singular T paths; it does not forbid alternative winning martingales there (S160 explicitly gives one with effective L1 at y=0^ω, whose sources are nonetheless nonCR).

## C161.1 — a nonCR output for which NO winning effective-L1-plus-floor replacement exists

Let Y be S011's specifically imported computably random wtt-autoreducible source, and F its fully proved TOTAL globally fair cap-TWO adaptive no-repeat scan. S011 establishes Y∈CR and y=F(Y)∉CR, with actual F-fibre over y singleton. Suppose, toward contradiction, some total rational output martingale D succeeds on that SAME y and possesses a GIVEN effective L1 terminal density f AND a positive rational α such that essinf_[y↾m]f≥αD(y↾m) at infinitely many m on which D(y↾m) is unbounded. Apply S160 Theorem A160.1 to G=F and x=Y, with a computable use function supplied by totality of F. That theorem constructs ONE total rational SOURCE martingale e with e(Y↾u(m))≥(31α/64)D(y↾m) on that subsequence, contradicting Y∈CR.

Therefore this PARTICULAR nonCR y admits **no** winning rational D simultaneously satisfying the effective-L1 hypothesis AND the infinitely often profitable conewise floor. This rigorously defeats a proposed universal regularisation of *every* nonCR output winner into that class. It does NOT assert that no winning effective-L1 martingale exists at y absent the floor; nor that y is a legal R₂ separator: Y∉R₂ because F itself destroys it. This is a corollary of S011+S160, not an independent new constructive hierarchy witness.

## D161 — direct hierarchy and alternative-finance attacks

The central E-08 hypothesis remains G∈F₃ additive-two, x∈R₂, y=G(x) nonCR, exactly TWO ACTUAL COMPLETE inverses over y. A161/B161 provide a fully legal, three-inverse-on-safe-siblings oscillator and persistent singular probabilities, but its T inverses already fail CR by W. C161 is a genuine regularisation obstruction but uses x=Y∈CR\R₂ and a singleton y-fibre of a legal F₂ map. Neither is a same-source x∈R₂ witness.

**Failed branch 1 (posterior limit):** Treat finite η_m as if η_m[s]→η[s] uniformly or pointwise. A161 explicitly defeats even pointwise convergence at s=11. Rationalising each finite η_m gives a martingale for a FIXED m only; sending m→∞ does not give a single computable capital process.

**Failed branch 2 (tilt-to-source):** The output conditional odds become favourable on T, but turning μδ(A_N)≥1−δ into a computable source-child-averaged bettor with capital growth on an unknown x is not justified. The S135 source W proves only that THIS target already has no CR inverse.

**Failed branch 3 (winning savings universally UI+floor):** C161 falsifies universal replacement for all nonCR outputs. In particular strong savings may force divergence but does not automatically provide an effective terminal L1 modulus and a cone-essential lower bound.

**Failed branch 4 (strictness by reservoir count):** S117 paired reservoirs and S129 one-surplus leave real two-preimage c2 cases open; S141's positive joint folding is necessary but benign even at MLR sources; S155 noncomputable fold mass coexists with CR conservation; S158 late-reveal F₂ conserves CR. S011 Y∉R₂, so ∀F₂∃x_F cannot substitute for ∃x∀F₂. No legal new complete cap-TWO source destroyer for a hypothetical x∈R₂, nor coupled F₃ survivor/destroyer, emerged.

**Disposition:** A161.1/B161.1 exact scoped INTERNAL theorems and C161.1 formal consequence of established internal S011/S160; no hierarchy equality or separation. E-08/E-00/S-00, R₂=R₃, R₂=MLR and Phase4 Gate4 remain OPEN/UNREVIEWED. Source policy/grades and frozen objects unchanged.
