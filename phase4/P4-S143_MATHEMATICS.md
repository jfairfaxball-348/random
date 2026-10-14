# P4-S143 — Dynamic two-inverse posterior and effective gain-linked source escrow

14 October 2026, ONE owner-invoked Phase4 CAND-01 session; INTERNAL same-agent mathematics, not independent/formal review. ENTRY LIVE main 360919fb96124f3b983a0848b405d03cda2d6937, predecessor S142 PR #42 merged direct non-force, sole parent 6a76cddd2c6cee228fcd68c9301fff9a2403d2c5 and tree ea40ae555ed0618dc42f5fb7ca8986b8b81f4560. No open PR or competing S143 branch/record. Actions runs, check-runs and statuses=0 (ABSENT_NOT_PASS), rulesets=[], protection UNKNOWN_403, workflows listing inaccessible (400). Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.

Notation: Cantor space 2^ω with fair λ. A globally fair total computable map G has λ(G^-1[τ])=2^(-|τ|) for every output cylinder. F_k requires ≤k ACTUAL complete infinite inverse sequences for EVERY output. R_k tests ALL maps F_k against ordinary total nonnegative rational output martingales. Write d for a unit-initial-capital rational output martingale. S142's additive-use-two degree-two G has exactly FOUR aligned source cells per output prefix; isolating A/B cones have q_A∈{1,2,3}, not a mere two-cell inverse table.

## A143.1 — posterior likelihood telescope (internally verified elementary algebra)

On late true two-inverse target prefixes τ, q=q_A(τ) and t=q_A(τb) belong to {1,2,3}; the other output child has A-count 2q−t∈[0,4]. The SEVEN allowed (q,t,sibling) triples are (1,1,1), (1,2,0), (2,1,3), (2,2,2), (2,3,1), (3,2,4), (3,3,3). The exact cone-output posterior probability of target b is t/(2q), the fair-relative likelihood increment is t/q. Thus on any finite consecutive target segment in the stable isolated two-inverse regime,

    Π_i [q_A(τ_{i+1})/q_A(τ_i)] = q_A(τ_final)/q_A(τ_initial) ∈ [1/3,3].

This is an exact bounded telescoping identity, NOT a source martingale. Infinite 1↔2 or 2↔3 volatility cannot by itself create unbounded capital from q-posterior likelihood factors. It does not rule out output martingale d gains, effective source splitting or all gain-weighted compilers. A stabilisation level exists by compactness but may be noncomputable; no effective entry modulus asserted. S135 supplies a fully globally legal fair cap-three 3:1↔2:2 two-true-inverse oscillator, already CR-conserving.

## B143.1 — effective finite-window source escrow (internally PROVED, elementary sufficient hypothesis)

**Theorem.** For ANY total computable globally fair G, ANY total nonnegative rational output martingale d with d(ε)=1 and ANY total computable B:positive integers→nonnegative integers, if there are INFINITELY MANY k≥1 such that

   max_{0≤n≤B(k)} d(G(x)↾n) ≥ 2^(4k),

then one explicitly computable TOTAL nonnegative RATIONAL source martingale W_{G,d,B} succeeds on the SAME x. No use or fibre bound required.

**Proof.** Let V_k be the output event that the stated threshold is crossed by B(k). This is a computably clopen union of length-B(k) cylinders. The finite optional stopping/Ville inequality for a nonnegative unit λ-martingale gives λ(V_k)≤2^(-4k). Put U_k=G^-1(V_k). Total computability on compact Cantor space supplies an EFFECTIVELY FOUND uniform finite input use for the finite output horizon; thus U_k is computably clopen. GLOBAL fairness gives the exact computable rational/dyadic price p_k=λ(U_k)=λ(V_k)≤2^(-4k). For any source word s, h_k(s)=λ(U_k∩[s])/λ[s] is total rational, and h_k(s0)+h_k(s1)=2h_k(s).

Define M_k(s)=1 if |s|≤k. If |s|>k, let a=s↾k: set M_k(s)=h_k(s)/h_k(a) when h_k(a)>0 and set M_k(s)=1 when h_k(a)=0. A zero-price cone never meets U_k, so holding there is legal. At |a|=k the two children average to 1; at all deeper nodes the h-identity gives the martingale equation. Hence M_k is a TOTAL RATIONAL nonnegative unit source martingale ON EVERY source node, not merely on x.

If x∈U_k, then h_k(x↾k)>0 and h_k(x↾k)≤2^k p_k≤2^(-3k). At a sufficiently long prefix s≺x deciding U_k, h_k(s)=1, so M_k(s)≥2^(3k). Define

    W(s)= Σ_{1≤k≤|s|} 2^(-k) M_k(s) + 2^(-|s|).

The geometric tail is EXACT: every k>|s| account still equals 1 at s. In particular W(ε)=1 and W(s0)+W(s1)=2W(s) including account-activation edges; the formula is a FINITE rational computation, not an infinite computable-real sum. Whenever x∈U_k, at sufficiently late source precision W≥2^(-k)2^(3k)=2^(2k). Infinitely many such k yield unbounded W along x. QED.

**Corollary/necessary escape condition.** For EVERY x∈CR, total fair G, unit total rational output d and total computable B, there are INFINITELY MANY k such that max_{n≤B(k)}d(G(x)↾n)<2^(4k). Hence any proposed x∈R2 with G∈F3 and a winning d must satisfy this rate-evasion property for every total computable B. This is standard-style effective stopping machinery, NOT a new priority/novelty claim and NOT R2=R3. It does not imply the non-CR image has noncomputable first-hit time at EACH k; it denies infinitely-many uniformly scheduled large crossings.

**WHY THE STRONG HYPOTHESIS MATTERS.** Bare output success d(G(x)|n) unbounded gives pointwise finite crossing time for each k, but the sequence of crossing times may have NO total computable bound satisfying the displayed infinitely-many criterion. Replacing B(k) by a y-dependent oracle choice invalidates effective clopen pricing and total rational W. The S011 genuine F2 observer F maps a CR source Y to a d-success output; since Y is CR, this (F,Y,d) MUST evade every computable B as above. Thus the universal claim 'finite stopping approximants automatically compile' is FALSE even for F2. This identifies the exact missing effective scheduling hypothesis, rather than silently solving known non-conservation.

## A — hostile dynamic c2 attempt: NOT a same-source F2 simulator

At q=1→2, BOTH children of the unique A parent can enter the chosen target output: d gains on that output may have no associated source-bit wager. At q=2→1, the target occupies one of four A children, but the strategy may not inspect the target bit before betting on the source continuation; the sibling has count THREE. At q=2→3, the minority A child is in the OTHER output sibling, and a candidate that bets the low side can lose on the actual source. Exact likelihood q factors telescope; a proposed rational F2 transfer must finance both source outcomes and complete all output siblings. S129 eventual q=2 F2 fallback compiler and S117 eventual q=1 gated source tests do not settle arbitrary oscillation. No globally TOTAL fair ≤2-fibre F/e on the SAME bad-source x constructed. E-08 OPEN.

## B — arbitrary-use and effective gain-linked certificate

B143 is an exact sufficient *gain-linked* condition for a SOURCE detector, valid for arbitrary computable use and no fibre cap; unlike S141 positivity-only folding it genuinely pays stopping capital. But its computable schedule may fail precisely on a CR-source nonCR image. Arbitrary positive folds and rational conditional μ_A prices cannot supply B automatically, nor yield source inverse charts; conditional output μ_A-CR equivalence from S142 does not turn an A-source CR x into a μ_A-CR output. S141's legally fair cap-two fat fixed K shows even positive folds in EVERY joint neighbourhood with density→0 along many MLR/R2 fixed x remain safe. No general source disintegration, arbitrary-use E-00 or F2(R2) closure obtained.

## C — independent one-source separator attempt and obstruction

To prove strictness needs ONE globally total fair cap-three G, one rational output winner d, and ONE x meeting all universal F2/e tests while d(G(x)) succeeds. B143 imposes rate-evasion on any such x but supplies no survival construction. S011 furnishes CR bad-image sources that FAIL R2; S135's bad-output perfect T admits ONE rational SOURCE martingale excluding all CR preimages; S141 gives R2 sources but output unchanged and MLR. The preimage of d-success has λ measure ZERO, so intersecting it with the conull R2 class is invalid. Enumerating partial codes is not a legality oracle. No simultaneous finite-extension budget and no single x/G/d found; S-00 OPEN.

## Hostile verdict

A143 and B143 are INTERNAL scoped algebra/finite-stopping deductions with S142/S141, classical Ville and S011 proof reuse, NOT an independent theorem of R2/R3 closure, publication priority, formalization or outside check. Exact Fraction SANITY: 7 legal q transitions, 5736 consecutive walks length≤8 telescoping, 25 concrete delayed source capital inequalities; finite only. E-08/E-00/S-00, R2=R3 and R2≠R3 remain OPEN. Y/M/H/X, S101–S103 frozen A–C, DEF-0020, PA-0001/source grades unchanged.
