# P4-S160 — Effective-L1 terminal densities beyond posterior grid stabilisation

2026-10-15. ONE explicitly owner-invoked Phase4/CAND-01 mathematics session. Entry LIVE main `247e73d651e0d8553f04f28f4a72b749798ad0ff` tree `027688e43482f6cadea61f1b24589ba9d3d34500`, PR #59 merged as DIRECT expected-main non-force fast-forward at its own one-parent commit (parent 3bdd0e18269a6a63ef3bca472eb916c268420317). No open PRs, no existing P4-S160 branch, no Actions runs/check-runs/individual commit statuses; ABSENT_NOT_PASS. Rulesets []; protection read 403 UNKNOWN_403. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. Frozen Y/M/H/X, S101–S103, DEF-0020, PA-0001 and source grades unchanged. All mathematics INTERNAL, not independently refereed or established as original.

Notation: fair product λ on Cantor 2^ω; CR = no successful total nonnegative rational computable martingale. Total globally fair computable observer G has computable input-use u(m), first m output bits fixed by first u(m) input bits, with no additive bound assumed. F_k is capped by k ACTUAL COMPLETE infinite preimages for EVERY output; R_k is survival under ALL legal F_k. This session does not change these definitions.

## A160.1 — terminal-density SAME-SOURCE compiler (conditional, internally proved)

Let D:2^{<ω}→Q_{>0} be a total positive rational output martingale with D(ε)=1. Assume a GIVEN effective L1 convergence modulus for the level-m density D_m(z)=D(z↾m): there exists an integrable nonnegative f (defined a.e.) with ∫f dλ=1 and a computable N(k) for ∥D_m−f∥_1≤2^-k whenever m≥N(k). No pointwise computable name for f is asserted; the L1 approximation name suffices. The source limit can be singular on exceptional paths, but f itself is the λ-absolute-continuous terminal density; L1 excludes lost mass.

**Theorem A160.1.** Uniformly from indices for G,D and the effective L1 modulus construct ONE total nonnegative exact RATIONAL computable SOURCE martingale e, e(ε)=1, with for ALL finite source s:
  e(s)≥(31/64)·2^|s|∫_[s] f(G(z))dλ(z).
If for a PARTICULAR x with y=G(x), a rational α>0 and infinitely many output levels m with D(y↾m) unbounded along those levels satisfy
  f(z)≥αD(y↾m) for λ-almost every z∈[y↾m],
then, at n=u(m) and s=x↾n,
  e(s)≥(31α/64)D(y↾m),
so e succeeds on THAT SAME x. There is NO bound on u(m)−m, NO uniform posterior limit, and NO q_s grid stabilisation. The conewise terminal lower bound is a separate, strong hypothesis on the specific winning path, NOT automatic for any nonCR y, let alone any fair F3 map.

Proof. For each source prefix s, define η[s]=∫_[s]f(G(z))dλ(z). Since G pushes λ to λ, ∥D_m∘G−f∘G∥_(L1 source)=∥D_m−f∥_(L1 output). The finite cylinder integral η_m[s]=∫_[s]D_m(G(z))dλ(z) is an EXACT computable rational: enumerate finite source words at precision at least max(|s|,u(m)), calculate first m output bits and D on those output words. The absolute error |η_m[s]−η[s]|≤2^-k for m≥N(k), without an all-output conditional-posterior modulus. Hence η is a computable REAL probability measure on source cylinders, η[ε]=1 and η[s0]+η[s1]=η[s] EXACTLY, also if η[s]=0. Use S159's explicit rationalisation: ζ[s]=(η[s]+2^-|s|)/2; for n=|s| approximate ζ[s0]/ζ[s] with rational r_s at error at most 2^(-2n-8). Positivity ζ[sb]≥2^(-n-2), ζ[s]≤1 ensures 0<r_s<1 and both relative split factors ≥1−2^(-n-6). Define ẑ[ε]=1, ẑ[s0]=ẑ[s]r_s, ẑ[s1]=ẑ[s](1−r_s). Then ẑ[s]≥(31/32)ζ[s]≥(31/64)η[s], since sum_n 2^(-n-6)=1/32. e(s)=2^|s|ẑ[s] is total exact rational and satisfies every source-child average e(s0)+e(s1)=2e(s). For s=x↾u(m), ALL z in [s] have G(z)∈[y↾m]; a.e. conewise floor (pulled back under fair G) gives η[s]≥2^(-u(m)) αD(y↾m). Substitution proves stated domination. A conewise λ-null exception has λ-null G-preimage by GLOBAL fairness, so no unjustified pointwise assertion is used. QED.

## B160.1 — explicit effective UI rational winner, with a pathwise oscillating posterior

Define initial-zero-run L(z)=min{i:z_i=1}, finite λ-a.e. Put f(z)=(L(z)+1)/2 on these streams (the value at 0^ω is immaterial). Distribution P(L=k)=2^(-(k+1)); ∫f=1. Its exact level-m conditional expectation, rational and STRICTLY POSITIVE, is
  D(τ)= (|τ|+2)/2  if τ=0^|τ|;
       = (k+1)/2    if the first 1 in τ is at coordinate k<|τ|.
At τ=0^m, children have values (m+3)/2 and (m+1)/2, averaging D(τ)=(m+2)/2; elsewhere both child values equal D(τ). Thus D is one globally legal rational output martingale, D(ε)=1 and D(0^m)=1+m/2→∞. L1 error comes only from [0^m]: conditioned on 0^m the residual zero-run R has geometric(1/2) law, E|R−1|=1, so ∥D_m−f∥_1=2^(-(m+1)) EXACTLY. For EVERY m≥1, on [0^m] essentially f≥(m+1)/2≥(2/3)D(0^m). A160.1 therefore gives a single exact rational source winner on EVERY source x with G(x)=0^ω for ANY total computable globally fair G of ANY input-use, and at level u(m), e(x↾u(m))≥(31/96)D(0^m). This is a CONCRETE arbitrary-use example beyond S159's uniform q-grid condition, not a hierarchy separator: 0^ω itself is computably nonrandom and its full preimage is effectively closed null.

Take G=S135's already verified global additive-two F3 oscillator, and B-sector source prefix s=11. Its q_s(0^m) cycles 1/4→1/4→1/2→1/4 along 0^ω∈T, so q_s does NOT converge on that path, let alone uniformly all outputs. Nevertheless this D has the above source compiler; both actual inverse sources of 0^ω were already beaten by S135's W, independently of the new certificate. The theorem does not require replacing that existing proof of globally fair sibling rows or complete inverse count.

## C160.1 — quantitative μ_D tail **under** effective uniform integrability

Let A_N be S158's effectively open ≥N aligned-change event for S135's distinguished q_s. S158 proves λ(A_(2j+1))≤2^-j. Write μ_D(E)=∫_E f dλ (here true because effective L1 convergence). For EVERY measurable E and integer k≥0,
  μ_D(E)≤ (k+1)/2·λ(E) + ∫(f−(k+1)/2)_+dλ
        = (k+1)/2·λ(E) + 2^(-(k+1)),
using E[(L−k)_+]=2^-k. Choosing k=j yields for all j≥0
  μ_D(A_(2j+1))≤(j+2)/2^(j+1).
So the tilted posterior-change tails are EFFECTIVELY SMALL despite 0^ω lying in every A_N and D winning on 0^ω; μ_D({0^ω})=0. This is a genuine quantitative contrast to S159's positive SINGULAR tilt D*=(1+d_T)/2, where μ_(D*)(A_N)≥1/2 for all N. A computable μ_D null test for an exceptional output is NOT a direct CR source test; A160.1 supplies a distinct exact source martingale only when its conewise floor is met.

## D160 — hostile attempted E-08/E-00 and hierarchy closure

For central E-08 suppose G∈F3 additive two, x∈R2, y=G(x) nonCR, exactly TWO complete preimages over y. If one can FIND a winning rational D with supplied effective L1 limit AND the conewise lower-floor hypothesis on a winning subsequence, A160 immediately contradicts x∈R2 using identity as legal F2 and e as rational output bettor. BUT neither those hypotheses nor a suitable replacement D is forced by the bare E-08 premises. S159's singular tilt on S135 specifically violates L1: its terminal density equals 1/2 λ-a.e. but finite martingale expectations all equal1; hence no L1 convergence. Its conewise floor relative to D* along T tends to0. The new proof does not cover it.

S158's first-one-reveal map is TOTAL fair EXACT-two-inverse and has arbitrarily delayed q_(0) revelation; A160 handles its inverse sources of 0^ω despite no global EVCS, but those sources are computable and not R2. For outputs outside 0^ω the map preserves all CR as S158 already proved. S141 benign folds and S155 noncomputable degree-two mass remain harmless controls. S011's CR Y is destroyed by an F2, so Y∉R2. S117 paired reservoirs and S129 one-surplus do not supply conewise L1 floors.

There is NO constructed arbitrary fair F3→F2 factorisation, NO universally legal cap-two detector for the hypothetical bad x, NO coupled x∈R2\R3, and no unbounded-use E-00 solution for arbitrary output martingales. Specifically this effective-L1 conditional result cannot be promoted to "all output winners" by a growth-only savings trick: an arbitrary d-winning path may have exclusively singular surviving mass or zero essential inf on every winning cone. Full fairness, all siblings and true fibres are inherited from S135 and S158, not proved by the finite audit in this session.

**Disposition:** A160.1/B160.1/C160.1 INTERNAL scoped theorems; effective-L1 finance is genuinely nonuniform in output but assumes stronger terminal-density support. E-08/E-00/S-00 and R2=R3 equality/strictness OPEN. No source/novelty grade, Gate4, Phase5 or publication advancement.
