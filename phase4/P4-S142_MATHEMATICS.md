# P4-S142 — Rational conditional output comparisons and zero-density local folding

**14 October 2026; one internally checked Phase4 CAND-01 mathematics session.** Entry live main `6a76cddd2c6cee228fcd68c9301fff9a2403d2c5`, S141 PR #41 integrated directly at its one authored commit (sole parent `5dca4c42509a78d248d25a0c1a1f995e43e5d49c`, tree `4209b216aee09461883566c6992e7fda1f8f107d`). Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. No rival S142 branch, record or PR on entry. No independent/formal validation or novelty claim.

Notation: Cantor space X=2^ω, fair measure λ; F_k total computable globally λ-preserving observers with ≤k ACTUAL full inverses above EVERY output. R_k tests ALL members F_k against ordinary TOTAL rational nonnegative martingales. For computably clopen source A of λ(A)>0 and total computable G, let μ_A(V)=λ(A∩G⁻¹V)/λ(A); this is a computable *rational-cylinder* measure, not generally fair. S141 proved source-local a.e.-injective firewall by Rute 7.11; it did NOT prove arbitrary many-to-one preservation.

## A142.1 — exact two-way target computable-randomness comparison (INTERNALLY PROVED)

Let μ be any computable probability measure with exactly rational cylinder masses, satisfying μ[τ]≤C·2^{-|τ|} for every τ for one fixed rational C>0. Suppose y has μ[y↾n]>0 for all n and liminf_n 2^n μ[y↾n]>0. Then
    y is μ-computably random  ⇔  y is ordinary λ-computably random.
The first implication actually requires only μ≤Cλ and all prefixes in μ-support, not the positive liminf. The converse requires just a positive lower bound on 2^n μ[y↾n] EVENTUALLY; this is a pathwise bound, NOT a globally computable lower-density modulus. Neither implication asserts a computable inverse for G or conservation of CR from x to G(x).

PROOF λ-nonCR⇒μ-nonCR: Let d be any total nonnegative rational λ-martingale winning on y, ν[τ]=2^{-|τ|}d(τ). On μ-positive τ set h(τ)=ν[τ]/μ[τ] (rational); ν may put weight on a μ-zero child, so h is only a μ-supermartingale. Define a *total rational μ-martingale* m by m(ε)=h(ε), and on μ-positive τ set Δ=ν[τ]−Σ_{b:μ[τb]>0}ν[τb]≥0, r=m(τ)−h(τ)≥0, and m(τb)=h(τb)+r+Δ/μ[τ] for μ-positive children. Set m=0 below μ-zero nodes. Weighted children average equals m(τ), and m≥h by induction. Hence on y, m(y↾n)≥ν[y↾n]/μ[y↾n]≥d(y↾n)/C. This is S141's reserve calculation applied beyond clopen-cone notation; all divisions are by decidable positive rationals. No equality on μ-null children is needed.

PROOF μ-nonCR⇒λ-nonCR with lower density: Let e be a total nonnegative rational μ-martingale winning on y, interpreting μ-zero-node values harmlessly. Put M(τ)=2^{|τ|} μ[τ]e(τ). Then M is an exact total rational fair-coin martingale since Σ_b μ[τb]e(τb)=μ[τ]e(τ), including zero nodes. On all sufficiently late prefixes y↾n, M(y↾n)≥c e(y↾n) for some positive c (the value need not be computed by the strategy). Therefore M succeeds. QED. When μ[τ]=0, multiplying by zero is exact and creates no evaluation problem.

**A142.2 — the c2 two-inverse posterior prices are NOT the obstacle (INTERNALLY PROVED, CONDITIONAL ON ISOLATING CONES).**
Let G be total globally fair additive-use-two with a target y having EXACTLY two distinct actual inverse points. Choose disjoint *cylinder* cones A,B isolating them. Compactness implies that at all sufficiently late m, ALL four compatible source (m+2)-cells over τ=y↾m lie in A∪B, and each cone contains ≥1. Let q_A(τ) be the number of those cells in A, so q_A∈{1,2,3}, q_B=4−q_A. The conditional output cylinder mass is exactly
  μ_A[τ]=q_A(τ)·2^{-(m+2)}/λ(A),      2^m μ_A[τ]=q_A(τ)/(4λ(A)).
Thus the ratio stays within [1/(4λ(A)),3/(4λ(A))] ALONG y after a finite non-effective entry level. Since globally μ_A≤λ/λ(A), A142.1 gives μ_A-CR(y) ⇔ λ-CR(y), with entirely rational conversion and no inverse decoding modulus. This DOES NOT imply CR(x)⇒μ_A-CR(G(x)): the restriction G|A can retain positive-measure multiple fibres. The true missing step is SOURCE lifting through these folds, not pricing the output μ_A test.

At all τ for which the A-source cells are fully aligned, the next-bit posterior is exactly
  μ_A([τb] | [τ])= q_A(τb)/(2 q_A(τ)).
Since q_A(τ0)+q_A(τ1)=2q_A(τ), the admissible child-count pairs are q=1: (0,2),(1,1),(2,0); q=2: (0,4),(1,3),(2,2),(3,1),(4,0); q=3: (2,4),(3,3),(4,2). If the chosen target child is required to retain BOTH full inverse cones, the transition graph is exactly
  1→1 (sibling A1), 1→2 (sibling A0);
  2→1 (sibling A3), 2→2 (sibling A2), 2→3 (sibling A1);
  3→2 (sibling A4), 3→3 (sibling A3).
In particular 1↔3 direct steps are impossible. The 1→2 transition sends every A-child into the target child and leaves its output sibling entirely to B. The 3→2 transition leaves the sibling entirely to A. Those sibling constraints are necessary and exactly explain why a naive 2:2 stationary F2 tag fails on S135's legal cycle. They DO NOT create a cap-two F2/e source certificate.

## B142 — severe quantitative false-positive: local fold density can tend to ZERO (INTERNALLY PROVED from S141's legal P plus classical density theorem)

Use EXACTLY S141's complete globally fair additive-one F₂ map P from disjoint densely distributed shift pockets O=⋃_j[ρ_j], preserving every pocket and acting as the identity on the computably closed K=X\O, with λ(K)≥7/8. For x∈K and any n, no pocket can properly contain [x↾n] (it would contain x), so every pocket intersecting [x↾n] is entirely inside it. Consequently
  B_n=[x↾n] ∩ P⁻¹([P(x)↾n]) = [x↾n].
The set of outputs with ≥2 full inverses **inside B_n** is exactly O∩[x↾n]. Pocketwise preservation gives the exact conditional-fold mass
  μ_{B_n}{z: |P⁻¹(z)∩B_n|≥2}
       = λ(O∩[x↾n]) / λ([x↾n]).
This is strictly POSITIVE for EVERY n by pocket density. Yet by the usual Cantor-space Lebesgue density theorem, for λ-almost EVERY x∈K the ratio tends to ZERO as n→∞, since K has positive measure and is measurable. Martin-Löf random points have full λ-measure, so the set of x∈K∩MLR for which BOTH statements hold has measure λ(K)≥7/8. All such x lie in R₂ and satisfy P(x)=x∈MLR, hence no output rational martingale wins. This is a sharper counterexample to **any argument relying ONLY on pointwise persistence of positive local fold mass**. No effective decay rate on individual x or uniform bound on all x∈K is claimed, and no gain-coupled sufficient criterion is refuted. It is a derived classical density application, not a new originality claim.

## Front A — honest E-08 attempt / exact failure
Try to transfer an output winner d by rational μ_A comparison. A142.2 does yield a rational μ_A winner on y; it does NOT yield an A-source martingale on x. At one output row q_A=2, the two source cells may send child incidences (1,3)/(3,1), and selecting a “half-price” A-cell is not a global fair F₂ map. At 1→2, BOTH children of a unique A cell go to the same output child, so naïvely copying a conditional output bet onto one source bit violates the source martingale identity. At 2→1, only one of FOUR A-children goes to the chosen output bit, but selecting it using knowledge of the target output bit is future-dependent; incorrectly buying only the realised good branch is a sure-win oracle trick. S135's all-output legal 3:1→2:2→3:1 oscillation survives these objections and is itself CR conserving. No globally total fair cap-two simulator plus total rational e winning on SAME x was produced; E-08 remains OPEN. S129 eventual q=1/2 clauses and one-surplus results unaffected.

## Front B — gain versus folding, arbitrary use
For ANY computably clopen A, μ_A prices are rational, and A142.1's λ→μ conversion is uniform; μ→λ comparison along a particular path additionally needs nonvanishing density. For arbitrary-use G there is NO fixed four-cell occupancy identity and no pathwise lower density guarantee. Exact rational conditional output prices do NOT compute the conditional *source inverse* or a martingale under λ_A. Attempting to lift the μ_A output winner through a positive-measure many-to-one restriction is the first unsupported implication. The S141 pocket map, now with almost-everywhere vanishing but always positive local fold density, blocks unpriced/positivity-only claims. A sufficient gain-linked, computably budgeted source certificate remains OPEN.

## Front C — strictness / coupled construction failed
To separate R₂ from R₃ requires ONE globally legal cap-three G, ONE rational output d, ONE x with d(G(x)|n) unbounded, AND all legal F₂/rational e tests bounded on that SAME x. The source set above d-success is λ-null by fairness; crossing it with a conull class of R₂ points is invalid. Attempted use of the fat K locus fails because P fixes MLR points and gives no winning d. Indexing partial candidate F₂ codes does not decide legality, and no complete simultaneous finite-extension reserve preserving all three-inverse bounds was obtained. S011's genuine F₂ destroyer, S083/S101 A–C and S140/S141 necessary positive internal folds remain screening constraints. S-09 is OPEN; no separator claimed.

## Decision
A142.1–A142.2 and B142 are INTERNAL scoped deductions with S141/Rute reuse and classical density theorem, not E-00 or S-00, not peer review, not newness. Two-side measure equivalence narrows the c2 bottleneck to SOURCE-side disintegration in oscillating two-true-inverse fibres. Exact finite transition enumeration is SANITY ONLY; the proof is the cylinder counting and compactness argument. No result about arbitrary G∈F3 and x∈R₂ with bad image; R₂=R₃ and R₂≠R₃ both OPEN. Next S143 must attack the source disintegration itself, not merely enumerate more output posteriors.
