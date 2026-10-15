# P4-S156 — exact bounded-lag posterior compiler and its sharp limitation

15 October 2026. ONE owner-invoked Phase4 CAND-01 research session. Entry LIVE main `e7ccfef78f78ae2b1adef4e5f9a8a647ecd6c62d`, tree `82298c1c4bf7ebcf943bfce18bd64a95e6373a19`; S155 PR #55 merged at the same actual authored one-parent commit (parent `a3118c22412b131c7db04c2bf78942dc73813c93`). Open PRs []; no S156 records; Actions runs [] and commit checks/status contexts [] = ABSENT_NOT_PASS; rulesets []; main protection 403 UNKNOWN. SAME-AGENT INTERNAL mathematics only. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. Y/M/H/X, S101–S103, DEF-0020/PA-0001 and source grades frozen.

Let X=2^ω, λ fair coin, CR ordinary rational computable randomness. F_k consists of ALL total computable fair maps with at most k ACTUAL COMPLETE preimages above EACH output. R_k={x:∀F∈F_k F(x)∈CR}. An additive-c map has a uniform procedure computing its first m output bits from its first m+c source bits. Define for source word s, output word τ
`q_s(τ)=2^{|τ|} λ([s]∩G⁻¹[τ])`.
For a fair G, these are exact rational conditional probabilities; q_ε=1, q_s=q_s0+q_s1, and q_s(τ0)+q_s(τ1)=2q_s(τ).

## A156.1 — exact bounded-lag posterior compiler (INTERNALLY PROVED, CONDITIONAL THEOREM)

**Hypothesis CLS(c,h).** G is total computable, globally fair and additive-use-c, and h is a SPECIFIED nonnegative integer satisfying, for EVERY finite s and EVERY τ with |τ|≥|s|+h and EVERY v,
`q_s(τv)=q_s(τ)`.
Neither membership in CLS nor h is assumed decidable from a code for arbitrary G. This is a strong whole-output property, not eventual constancy merely along one y.

**Theorem.** Under CLS(c,h), for EVERY ordinary total nonnegative rational computable output martingale d there is an explicit total nonnegative rational computable SOURCE martingale e, uniform from G,c,h,d, with for EVERY source x and n:
`e(x↾n) ≥ 2^{-(c+h)} (d(G(x)↾(n+h))+1)/(d(ε)+1)`.
Consequently G preserves ALL ordinary CR, irrespective of a separate cap on complete fibres. In particular no hypothetical additive-two F₃ map satisfying CLS(2,h) can destroy any x∈R₂. The all-output F₂/e compiler for this restricted class takes **F₂=identity**, with e the martingale below. Identity is globally fair, total, exactly one preimage of EVERY output and so is legal F₂.

**Exact construction.** Put p=d+1, a strictly positive rational martingale with p(ε)>0. Define a computable probability measure on output cylinders
`μ([τ])=2^{-|τ|}p(τ)/p(ε)`.
For s of length n, put m=n+h and compute
`η([s])= Σ_{τ∈{0,1}^m} q_s(τ) μ([τ])`,
`e(s)=2^n η([s])`.
Every summand is an EXACT rational, computable by enumerating the finite m+c input words and evaluating G↾m. The sum is finite. Thus e is total exact rational without an oracle, limit computation or approximation-to-a-real subroutine.

**Projectivity and fairness.** Define `κ_y([s])=q_s(y↾(|s|+h))` for every infinite output y. CLS makes κ constant on that depth-(|s|+h) cylinder. For each y, κ_y(ε)=1 and κ_y([s])=κ_y([s0])+κ_y([s1]): compute the identity at output depth |s|+h+1, using stabilization of q_s, and the source-cylinder partition. Hence κ_y is a genuine probability measure on the source space, for EVERY y, not merely λ-almost-everywhere. Moreover κ_y is supported on G⁻¹{y}: if [s] misses that compact fibre, G([s]) is compact not containing y, so some prefix y↾j is absent from G([s]); then q_s(y↾j)=0, and CLS yields κ_y([s])=0. This supplies an everywhere-defined projective conditional kernel.

Integration gives η([s])=∫κ_y([s])dμ(y), and therefore η(ε)=1, η([s])=η([s0])+η([s1]); consequently e(ε)=1 and e(s0)+e(s1)=2e(s). No inferential use of computability of fibre-degree sets was made.

**Positive atom and quantitative transfer.** Fix ANY x, y=G(x), source prefix s=x↾n and m=n+h. The source aligned cylinder [x↾(m+c)] is contained in [s] and in G⁻¹[y↾m]. Thus q_s(y↾m)≥2^m2^{-(m+c)}=2^{-c}. This is for EVERY input and EVERY n; it uses source/output alignment and NOT merely a count of true complete inverses. CLS says κ_z([s])=q_s(y↾m) on the entire output cylinder [y↾m]. Hence
`η([s]) ≥ 2^{-c} μ([y↾m]) = 2^{-(c+m)}p(y↾m)/p(ε)`.
Multiplying by 2^n yields the stated `2^{-(c+h)}` bound. If d succeeds along y, p(y↾(n+h)) is unbounded as n grows; e succeeds on the SAME x. No known success time or rate is used. QED.

**Scope:** a genuine infinite proof of a precise sufficiently strong regularity condition; NOT general E-08 and NOT a proof that any cap-three map satisfies CLS. Its fixed h is mathematically ESSENTIAL to the displayed constant-factor transfer. A general computable h(n) with h(n)-n unbounded would give a factor 2^{n-h(n)}, which can erase arbitrarily slow output-martingale growth. This is a warning, not a proof that no different compiler can work.

## A156.2 — quantifier-level negative condition

For EVERY fair additive-c G with a bad CR source image, and for EVERY fixed h, CLS(c,h) fails. Explicitly,
`∀h ∃s,τ,v : |τ|≥|s|+h ∧ q_s(τv)≠q_s(τ)`.
This is the CONTRAPOSITIVE of A156.1. These witness strings need not lie near the offending output y; it is NOT an on-path two-sheet oscillation theorem. A stronger assertion about every cone on x would be unjustified. If a fair additive-two cap-three destroyer exists it must evade all CLS(2,h) uniformity conditions.

## B. Direct E-08 / two-complete-inverse front — attempted, NOT resolved

Assume hypothetically G is globally fair total additive-two, cap THREE on all infinite outputs, with ONE x∈R₂, y=G(x) nonCR, and exactly TWO COMPLETE preimages of y. Apply A156.1 whenever a finite bound h is supplied: it would defeat x using legal identity/e and contradict x∈CR, hence this hard configuration must violate CLS(2,h) for every h. This is a concrete conditional same-source compiler; the key MISSING implication is deriving CLS (or an alternative computably financed local law) from cap-three and membership x∈R₂. The four length-(m+2) input candidates above each output prefix are not two complete inverse points. Presence of an actual second partner does not select a computable sheet.

All input cylinders / ALL output siblings are present in CLS. The finite q=1→2→t, 3→2→t distributions obey the two-step source-bank budget t·a+(4−t)·b≤4; bounded finite arrangements alone do not assert CLS. S117 eventually balanced separating B only along one selected output; its q_B=1/2 can be stable ON that y without a uniform bound on every off-path cylinder or on EVERY source prefix. The S135 legal F₃ oscillator has a fixed clopen A-sector posterior oscillating 3/4↔1/2 infinitely often on EACH y in T, so fails CLS for every h; all its source preimages of T are nevertheless NON-CR by S135's independent rational source martingale. S141 benign positive local folding shows that collisions can be harmless; not every CR-conserving map has been proved CLS. These are controls, not an E-08 conclusion.

S155's P_A satisfies CLS(1,0) exactly by its own proof, and A156.1 now constructs a direct rational preservation martingale for it despite potentially NONCOMPUTABLE measure of its double-fibre output stratum. Thus computably pricing that STRATUM is not necessary for THIS transfer. S005/S006 show noncomputable crossing masses/selection issues, and no such event price has been inferred here. S011's bad CR image arises from an adaptive no-repeat scan with no fixed additive-use-c bound; neither a finite h nor a global conditioned kernel is inherited. On-path posterior data alone may be misleading: κ need not be computable where nonCR y lies, nor atom prices effectively usable.

**Primitive sufficient financing criterion.** More generally, if for each rational output p a uniformly exact computable rational projective SOURCE probability η_p is supplied and along EVERY relevant (x,y=G(x)) there is a fixed positive computable K and fixed nonnegative integer h such that `η_p([x↾n])≥K·μ_p([y↾(n+h)])` for all sufficiently large n, then `e_p(s)=2^{|s|}η_p([s])` is a total rational source martingale and succeeds whenever p succeeds on y. A156.1 provides η, K=2^{-c}, h, and an explicit entire-space formula. This is an operational sufficient condition, NOT a minimality or necessity classification. Without exact computable rational projectivity and bounded shift, an ineffective limit/price cannot be spent.

## C. S-00 strictness fallback / E-00 — attempted, NOT resolved

Tried to upgrade S011's source witness Y or a folded P_A example into a coupled G∈F₃ witness. S011 gives Y∈CR but explicitly Y∉R₂, since its legal F₂ already defeats it. P_A preserves all CR and its uncomputable double-fibre mass does not generate a bad image. S135 supplies true degree-two outputs and nonCR outputs but ALL sources over its trap are defeated by a total rational SOURCE martingale. Thus NONE of these supply the quantifier order `∃x∈R₂ ∃G∈F₃ ∃d : d(G(x)↾n) unbounded`. Enumerating all partial Turing programs and imposing finite constraints does not effectively enumerate total globally fair fibre-capped F₂ programs; totality/limit complete fibre legality remain unproved, and a family of individual survivors `∀F₂∃x_F` cannot be promoted to one universal x. No genuine G,x,d triple is constructed.

The arbitrary-use E-00 bridge is also missing: A156.1 relies on FIXED m+c alignment; no general uniform use-reduction nor all-output cap-preserving modification has been shown. No R₂=R₃ equality or strictness result. No originality/priority, source-grade change or Phase5 claim.

**Verdict:** INTERNALLY PROVED A156.1 and its simple contrapositive under an explicit strong supplied CLS(c,h). General E-08/E-00/S-00 and R₂=R₃ vs strictness OPEN. Finite script is SANITY ONLY.
