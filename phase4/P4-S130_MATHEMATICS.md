# P4-S130 — Variable degree, a fat local-unbounded locus, and a dyadic sheet obstruction

14 October 2026. EXACTLY ONE Phase4/CAND-01 owner-invoked mathematics session. Entry main `85498fa557b9223e737c3d92a64432b85c8b50f3`, S129 commit, sole parent `7dba7e3303607c9b782adde7ba81d4682747b163`, tree `37efd4338f6c64c778b37112c9a6e79ad207dd70`, PR #28 closed/merged as its same one-parent SHA. No intervening main commit, competing S130 branch or open PR at entry. Claims INTERNAL and reviewed adversarially by SAME agent, not formal, independent, novelty or external claims.

Definitions as frozen: X=2^omega with fair product lambda; F_k is ALL total computable globally fair maps with at most k ACTUAL infinite inverse streams over EACH output, no use bound unless specified. R_k={x: EVERY F_k image of x is computably random}; R_fin=intersection over all k. CR means no ordinary total rational nonnegative martingale with unbounded limsup. MLR is a subset of every R_k by test pullback. Never substitute finite compatible cells for ACTUAL fibre degree.

## A130-1: two genuine globally legal cap-three/c2 exceptional-fibre architectures

Use the complete prefix-free Kraft code P_k={0,10,...,1^(k-2)0,1^(k-1)} for k>=2; P_1={empty}. T_k(pu)=u (S127). For a=1 or 2 define on ALL inputs

    E_(a,3)(b u) = b T_a(u) if b=0, and = b T_3(u) if b=1.

This is a total computable map with output first bit equal to input first bit. On each clopen tagged half its conditional output law is fair, hence E is globally fair over EVERY cylinder. For y=0v the ACTUAL fibre is {0pv:p in P_a}, cardinality a; for y=1v it is {1pv:p in P_3}, cardinality three, with no other hidden inverses. T3 needs at most two extra tail bits; first m output bits require at most m+2 source bits (also at m=0). Thus BOTH E_(1,3) and E_(2,3) are globally legal additive-two members of F3, with genuinely degree-one or degree-two outputs and degree-three elsewhere.

Every source x=bpu and its output bv have the SAME infinite tail v after deleting fixed finite prefixes. Hence CR of source iff CR of output by ordinary finite-prefix CR invariance. In particular neither map destroys ANY CR source, much less an R2 source. The existence of variable-degree F3 maps nevertheless makes S129's exact-three-everywhere hypothesis materially narrower than general F3. The first failed separation line is replacing CR-source conservation of these examples by existence of a SAME-SOURCE x in R2 with nonCR output. We have NO such x or output winner. Do not infer R_j-image closure from the finite insertion bv; the displayed claim is strictly CR conservation.

Universal completion attack: start at an output of degree <=2, isolate its true inverse cones, and attempt B129's two-candidate normalized F2 completion. B129's 2:2 all-child balance requires a selected cone holding exactly TWO aligned cells along the target, and cannot simply be inferred from actual fibre degree 1 or 2 when FOUR finite cells may distribute 4, 3+1 or 2+2 with unbounded changes. A 3:1 row violates a two-candidate normalized price; applying a permanent fallback there changes the target unless target balance can first be proved. Conditional statement only: IF an isolating cone eventually contains precisely two aligned cells along the target, B129's legal global F2 normalization applies; IF it eventually contains one, S117's gated copy handles a bad output. The general R2/F3 SAME-SOURCE reduction is unresolved.

## B130-1: a dyadic clopen-sheet obstruction to a stationary five-surplus construction

**Theorem (integral-sheet divisibility).** Let G be total computable, globally fair and additive-c, N=2^c. Let B be the union of exactly a>0 distinct source length-c cylinders. Suppose: (i) at EVERY output prefix tau of length m, exactly a of the N compatible length-(m+c) source cells belong to B, and (ii) EVERY full output y has exactly ONE actual inverse inside B. Then a must be a POWER OF TWO.

Proof. The finite-count hypothesis gives for every output cylinder [tau]
lambda(B intersect G^-1[tau]) = a 2^(-(m+c)) = lambda(B)lambda([tau]).
By uniqueness and existence, G restricted to B is a continuous bijection onto X, hence a homeomorphism (compact-to-Hausdorff). For EACH source length-c cell [s] contained in B its image A=G([s]) is clopen in X. The just-proved conditional measure identity evaluated at A (extend from output cylinders to Borel sets, e.g. clopen finite unions) yields
lambda(A) = lambda([s])/lambda(B) = (1/N)/(a/N) = 1/a.
Every clopen subset of fair Cantor space has DYADIC rational measure, so the integer a has no odd factor: a=2^j. QED. No computable inverse or source randomness argument is needed.

At c=3, three disjoint root sectors each containing ONE actual inverse over EVERY output cannot have stationary all-output compatible multiplicity vector (3,3,2): 3 is not a power of two. The viable padded T3 occupancy (4,2,2) passes the divisibility test but is finite-prefix safe. This is an actual topological/measure obstruction to the particularly tempting compensated multi-surplus design; it does NOT rule out output-dependent sector populations, dynamically changing clopen tags, nonstationary paths, exact-three c3 globally, or a Schnorr-random nonCR bad output. A schedule programmed with an uncomputable fixed target is not a computable map. S129's one-surplus SOURCE rotation theorem cannot be transplanted to c3/r3: there are FIVE surplus cells, not one.

The lemma is also a general-k structural theorem: ANY integer a in this stationary, everywhere-one-in-sector regime divides 2^c in the strict sense a must itself be a power of two. Conversely a power of two is only a necessary local price condition, not a universal chart-completion theorem.

## C130-1: stronger restricted composition firewall

Let F be ANY element of F2, with arbitrary computable use, and H ANY fair total additive-one map with EXACTLY TWO full inverses above each output. S109's saturated additive-one CR conservation says H maps every CR input to CR. For x in R2, F(x) is CR by definition; therefore H(F(x)) is CR. Thus

    for ALL F in F2 and such saturated one-lookahead H,
    (H composed F)(R2) is contained in CR.

This strictly relaxes S129's extra requirement that the inner F also have additive-one use. The factor composite may be cap FOUR rather than THREE, and the statement is CR output, NOT an R2 image. In an exactly-three F2 composition, S128 requires H exact-two and F's double locus to select precisely ONE of its two preimages over every output. The new firewall says: to destroy an R2 source in such a factorization, the OUTER H must escape saturated additive-one CR conservation. No general nonfactorable F3 example follows, nor F2(R2) closure, nor R2 vs R4.

## D130-1: a pointwise-finite fair observer with a FAT local-unbounded-degree locus

**Theorem (fat-boundary countermodel to nullity).** There is a total computable globally fair G:X->X with finite ACTUAL fibres over EVERY output, but its closed local-unbounded-degree locus L_G has measure at least 7/8. In fact L_G is a computable positive-measure effectively closed nowhere-dense set C on which G is the identity; C contains actual MLR (hence R_fin) sources. The map still preserves CR of EVERY source. Thus locality alone cannot eliminate the R_fin source from L_G, and the claim "L_G is always null" is FALSE.

Explicit construction. Put d_n=n+3 and N_n=sum_(j=1)^n d_j, N_0=0. Partition X into successive consecutive variable-length blocks of lengths d_1,d_2,... . A point is in the boundary C iff NONE of its blocks equals the ALL-ZERO block 0^(d_n). Every point outside C has a unique FIRST all-zero block n; its corresponding prefix rho is a minimal removed cylinder [rho], and these cylinders partition U=X\C disjointly. Let G be identity on C. On a removed cylinder [rho] of stage n set

    G(rho u) = rho shift_n(u),

where shift_n discards the first n bits of the infinite tail u. This is a globally defined map, no noncomputable oracle or patched-up partial branch.

Total effective continuity: to compute m output bits, examine the finitely many blocks whose end N_n is <m. If an all-zero block is found, output its complete rho followed by the tail bits offset n; otherwise output the original m input bits. If the first removed block ends at N_n>=m, the alteration is after m and cannot change the required prefix. Since n<=m for N_n<m, at most 2m source bits suffice. This establishes a total computable uniform prefix algorithm (not fixed additive overhead).

Fairness: each removed cylinder maps ONTO ITSELF by a fair n-bit tail shift, so conditional cylinder prices in that cylinder are preserved exactly; on C the map is identity. The disjoint measurable partition C plus the removed cylinders therefore preserves lambda on every Borel set. Over a removed output y=rho v the EXACT inverse list is {rho q v : q in {0,1}^n}, cardinality 2^n; for y in C the ONLY inverse is y itself. All fibres are finite, globally unbounded.

C is effectively closed and nowhere dense: in every surviving basic block cylinder the next prescribed all-zero subblock is removed. Its measure is the convergent product

    lambda(C)= product_(n>=1)(1-2^(-(n+3)))
             >= 1 - sum_(n>=1)2^(-(n+3)) = 7/8 >0.

For each y in C and each output neighbourhood [tau] containing y, arbitrarily late removed cylinders lie inside [tau] and have fibre degree 2^n tending to infinity. Thus y belongs to L_G. For each y in any removed cylinder [rho], that cylinder itself is a neighbourhood with constant fibre cap 2^n. Therefore L_G=C exactly, not merely a subset. Since lambda(MLR)=1 and lambda(C)>0, C contains an MLR point x. Such x belongs to R_fin, lies in L_G under G, and satisfies G(x)=x, which IS CR; this does NOT witness an R_fin failure. Every source maps to an output with the same infinite tail after a finite deletion (inside patches), or stays fixed (on C), so CR is preserved for all sources. This directly defeats any attempt to show L_G contains no R_fin points or is null, without constructing a bad image. C even has computable measure by effective convergence, a stronger positive example than an uncontrolled closed set.

This is a result about the ALL-FINITE front, NOT a solution of R_fin vs MLR/pointwise-finite robustness. It shows that the D129 local theorem is genuinely conditional: its exceptional set can be large and random-rich. It refutes neither a potential stronger theorem exploiting source-specific price structure nor the prospect of R_fin preservation by EVERY pointwise-finite map.

## E130: central hierarchy / detector scorecard

* General R2=R3, R3=MLR, original R2=MLR, and any ONE nonMLR R2 or R_fin survivor: UNRESOLVED. The quantified demand remains a single source that defeats EVERY legal observer, not a finite sample or varying x_k.
* E_(a,3) proves variable-fibre cap-three/c2 maps exist globally, but they are all-CR safe; no rational output winner with a protected same source.
* Stationary all-output c3 (3,3,2) three-single-sheet strategy is IMPOSSIBLE by B130-1, but compensated output-dependent multi-surplus circulation and a Schnorr-random nonCR target remain open.
* Exact-three general F2-factorization and F2(R2) closure remain OPEN; C130-1 gives a strictly larger restricted NO-DESTRUCTION composition class.
* L_G can contain positive measure of genuine R_fin sources, but the displayed G acts as identity on L_G, so no separating bad image. No quantifier exchange of forall k exists x_k with exists x forall k.
* S126-S129 correction audit: rechecked argument lines and finite row/fallback/mixture counters, no newly confirmed fatal gap; no historical quarantines or source-grade upgrades.

Frozen Y/M/H/X, DEF-0020, PA-0001, E-ISO/E-WTT grades, S101-S103 A-C and historical mathematics not altered. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. No Lean, Palomar, novelty campaign, outside contact or publication.
