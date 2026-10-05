# Phase 4 — Mathematics records

Status: **OPEN** after formal Gate-3 PASS in P3-S008.

Selected candidate: **CAND-01 — Computable randomness under finite-ambiguity observations**.

The exact formulation remains unchanged: for every fixed k>=1, consider everywhere-total computable fair-coin-preserving Cantor self-maps with at most k preimages of each point, with no effective inverse branches assumed.

## Completed mathematics

### P4-S001 — k=1 injective base case

P4-S001 proves that k=1 forces a computable fair-coin-preserving homeomorphism with an everywhere-total computable inverse. SRC-0015 / THM-0038 then yields computable-randomness invariance.

The inverse has a computable use modulus for each particular map, but there is no single fixed inverse-use bound across the whole class; coordinate permutations witness arbitrarily delayed inverse use.

This is programme mathematics, not a novelty result. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 no-consequence guard is preserved as the pre-Phase-4 baseline. P4-S001 establishes only k=1; k>=2 and general finite multiplicity remain unresolved here.

Publication remains CLOSED. Fairfax-Ball Randomness is not defined.

Records:
- phase4/P4-S001_MATHEMATICS.md
- phase4/P4-S001_CLOSE.md
- phase4/P4-S001_VALIDATION.md

Historical next step after P4-S001: **P4-S002**, now completed below.

## P4-S002 — k=2 finite-valued inverse boundary

P4-S002 proves that every k=2 map has a uniform descending computable-clopen presentation of each fibre, but the cardinal bound does not force an everywhere-total computable selector or a total two-branch fibre enumeration. An explicit total computable fair-coin-preserving map with exactly one double fibre makes every global selector/listing discontinuous at the collision output.

That obstruction does not itself destroy computable randomness: the example has an a.e.-computable measure-preserving inverse, so SRC-0015 / THM-0038 applies. The exactly two-to-one left shift gives a complementary positive example, preserving computable randomness by a direct martingale lift despite having no single a.e. inverse identity.

The general k=2 preservation/failure question therefore remains unresolved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No result is asserted for k>2, Gate 4 is not reviewed, and Phase 5 remains CLOSED.

Records:
- phase4/P4-S002_MATHEMATICS.md
- phase4/P4-S002_CLOSE.md
- phase4/P4-S002_VALIDATION.md

Historical next step after P4-S002: **P4-S003**, now completed below.

## P4-S003 — k=2 weighted-sheet and martingale-transfer boundary

P4-S003 strengthens the forced inverse information to a uniform two-prefix list at every requested input precision. It proves that an explicit computable clopen two-sheet decomposition into injective restrictions is sufficient for forward computable-randomness preservation, using conditional component measures, SRC-0015 / THM-0038 and DEF-0036.

The bare k=2 hypothesis does not force that global sheet structure: an explicit marker-and-delete map is fair-coin preserving, exactly two-to-one off one singleton, and has no continuous/clopen two-colouring separating all double fibres. It still preserves computable randomness and has an a.e. sheet description.

The general k=2 preservation/failure question remains unresolved. The remaining weighted obstruction is encoded by the computable bounded martingales w_sigma(tau)=2^{|tau|}lambda([sigma]∩F^{-1}([tau])). The attempted SRC-0061 scan completion fails because filler queries may pre-reveal later betting positions.

Records:
- phase4/P4-S003_MATHEMATICS.md
- phase4/P4-S003_CLOSE.md
- phase4/P4-S003_VALIDATION.md

Next recommended session: **P4-S004**, still bounded to k=2, on the conditional-weight stabilization/transfer obstruction versus an exact k=2 non-conservation witness.

## P4-S004 — k=2 conditional-weight stopping boundary

P4-S004 identifies the exact effectivity gap behind P4-S003's conditional weights. For each source cylinder [sigma], the points whose conditional weight ever falls below epsilon form a uniformly effectively open source set of measure at most epsilon. Hence Martin-Löf-random sources have positive persistent weight, but this is only an ML-test estimate; the computably-random source case still needs computable hitting measures, a computable stopped pullback, or another computable-randomness-level argument.

For every fixed output stage m, the output martingale capital lifts exactly to a uniformly computable normalized source martingale. The unresolved issue is coherence across unbounded m. Static mixtures need a growth rate, and adaptive threshold selection returns to the same effective stopping problem.

An explicit asymmetric collision map F_thin is total computable, fair-coin preserving and globally k=2, with one actual double-fibre sheet satisfying w_0(0^m)=2^{-m}->0. Its thin point is computable and the map is a.e.-invertible off the collision output, so it is not a randomness-destruction witness.

General k=2 preservation/failure remains unresolved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No k>2, novelty/open-status, Gate-4 or publication claim is made.

Records:
- phase4/P4-S004_MATHEMATICS.md
- phase4/P4-S004_CLOSE.md
- phase4/P4-S004_VALIDATION.md

Historical next step after P4-S004: **P4-S005**, now completed below.

## P4-S005 — k=2 crossing-measure non-effectivity boundary

P4-S005 refutes the direct stopping-effectivization route isolated in P4-S004. An exact total computable fair-coin-preserving k=2 prefix-code map has a computable clopen partition [0],[1] into injective sheets, yet for a fixed c.e. noncomputable set K its low-weight crossing set satisfies
[
\lambda(V_{0,1/3})=\frac18\sum_{e\in K}4^{-(e+1)},
]
which is noncomputable. Thus the forced two-prefix inverse lists do not force computable low-weight hitting probabilities, even under strictly stronger effective sheet information.

A second natural branch-free route also fails uniformly: integrating inverse-point counts against fair coin gives a finite measure whose total mass can encode the same noncomputable set. Hence symmetric fibre counting does not automatically yield one computable pullback martingale.

The new map is not a randomness-destruction witness because its computable clopen injective-sheet split places it inside P4-S003's positive preservation theorem. The SRC-0061 pre-revealed-bet obstruction remains unresolved. General k=2 preservation/failure remains unresolved.

Records:
- phase4/P4-S005_MATHEMATICS.md
- phase4/P4-S005_CLOSE.md
- phase4/P4-S005_VALIDATION.md

Historical next step after P4-S005: **P4-S006**, now completed below.



## P4-S006 — canonical lexicographic two-sheet complexity

P4-S006 computes the canonical sheet complexity without revisiting P4-S005's settled crossing-measure result. The collision relation is effectively closed. Assigning the lexicographically least preimage to the lower sheet and the nonminimum point of a double fibre to the upper sheet gives an effective G-delta lower sheet and effective F-sigma upper sheet; the double-fibre output set is effective F-sigma. The lexicographic minimum and maximum inverse selectors are effective Baire-1 limits of computable continuous selectors from the descending clopen fibre approximants.

This effective Borel information is not enough to run the existing computable-randomness transfer. In the P4-S005 map, viewed only as an internal calibration example, the canonical upper and lower sheet masses encode the same noncomputable base-4 real, so the canonical component measures need not be computable. The selector approximations also have no forced computable stabilization modulus.

A single hidden/rotating filler bit does not repair SRC-0061: revealing one previously masked genuine betting coordinate identifies the common one-bit ambiguity and pre-reveals every other coordinate in that cohort. More complicated delayed-coalescence constructions are not ruled out.

General k=2 preservation/failure remains unresolved. No exact k=2 destroyer is obtained.

Records:
- phase4/P4-S006_MATHEMATICS.md
- phase4/P4-S006_CLOSE.md
- phase4/P4-S006_VALIDATION.md

Historical next step after P4-S006: **P4-S007**, now completed below.


## P4-S007 — k=2 delayed-coalescence inverse-tree boundary

P4-S007 shows that the raw many-candidate inverse approximation can be computably resampled into a coherent width-two skeleton. There is a computable monotone coalescence schedule c(n) such that the compatible n-prefixes after y↾c(n) form a nonempty set of size at most two, these sets project coherently down the source tree, and their infinite paths are exactly F^{-1}(y).

For a double fibre, every skeleton level after the first true split consists exactly of the two true branch prefixes. For a singleton fibre, there is one true prefix and at most one phantom; recurrent phantoms must move their first disagreement arbitrarily far right. At fixed precision the approximation has a computable finite mind-change bound and at most one injury after c(n), but no computable last-injury time is forced.

This gives one choice bit per precision and a partial inverse on singleton fibres, but not computable branch masses, persistence decisions or a coherent pullback martingale. P4-S004 and P4-S005 therefore remain controlling for the measure/effectivity obstruction.

The session also generalizes P4-S006's one-hole collapse: after c(n), all unresolved first-n information is one binary cohort. Later information that distinguishes the two candidates determines the entire n-prefix and therefore pre-reveals every other differing coordinate below n. Any SRC-0061-style finite-fibre completion must prove a global freshness condition relative to c(n); the committed mechanism does not provide one.

General k=2 preservation/failure remains unresolved. No exact k=2 destroyer is obtained.

Records:
- phase4/P4-S007_MATHEMATICS.md
- phase4/P4-S007_CLOSE.md
- phase4/P4-S007_VALIDATION.md

Next recommended session: **P4-S008**, still bounded to k=2, on the freshness constraint: determine whether a total adaptive scan completable to global k=2 can retain enough genuinely fresh nonmonotonic bets to defeat a computably random source, or whether the constraint yields a computable martingale/permutation-style preservation theorem.

## P4-S008 — k=2 scan freshness / permutation-completion boundary

P4-S008 specializes P4-S007's freshness constraint to total adaptive no-repeat scans. At stage c(n), every transcript has queried at least n-1 of the first n source coordinates, so all remaining low-coordinate freshness is concentrated in at most one hole.

For any fixed coordinate j, querying j first and then following the scan until it requests j yields a total computable adaptive permutation completion: if j is never requested, global k=2 forces the original scan to query every other coordinate; if it is requested, the completion switches to exhaustive fillers. Any output martingale can be copied until that switch and then frozen.

Therefore a computably random winning source cannot have a persistent omitted coordinate. Any scan-based k=2 destroyer must win on a singleton fibre, where every coordinate is eventually queried and any low-coordinate hole moves outward.

The singleton moving-hole case remains unresolved. c(n) supplies no computable consumption deadline, fixed-sentinel mixtures have no proved growth-rate compensation, and dynamic sentinels can again pre-reveal later genuine bets. SRC-0061 is not reused. No exact k=2 destroyer and no full scan-preservation theorem is obtained.

Records:
- phase4/P4-S008_MATHEMATICS.md
- phase4/P4-S008_CLOSE.md
- phase4/P4-S008_VALIDATION.md

Next recommended session: **P4-S009**, still bounded to k=2, on the singleton-fibre moving-hole route: determine whether threshold-triggered/dynamic-sentinel permutation completions can be combined into one computable martingale without a computable success-rate/query-time bound, or whether an exact globally k=2 singleton-winning scan witness can be constructed with all global checks.


## P4-S009 — k=2 singleton moving-hole deferred-wager boundary

P4-S009 proves that not every moving-sentinel turnover carries a multiplicative martingale penalty. From a finite scan state, the continuations avoiding a proposed fresh sentinel form a computable binary tree. If every continuation eventually consumes the sentinel, finite branching makes this tree finite and a uniform consumption deadline is computably searchable.

With such a deadline, the future logical wager on the already-revealed sentinel bit can be hedged exactly: take the finite conditional expectation of the output martingale's capital immediately after sentinel consumption. This gives a computable fair martingale on the completion bits that starts at the current output capital and ends at exactly the post-consumption output capital. Bounded turnovers therefore concatenate without factor-two loss.

The hard singleton case is now exact: the target consumes the sentinel, but some sibling continuation can omit it forever. Finite-horizon portfolio/savings schemes have tail coverage tending to zero as the delay grows, so unbounded output capital alone supplies no rate-free guarantee across infinitely many such turnovers. This does not rule out a different transfer theorem.

A simple globally k=2 fair-coin singleton-spine comb shows that infinitely many avoidable-but-consumed holes are compatible with the fibre constraint, but the naive computable-control spine is not computably random. No adaptive exact witness is completed and SRC-0061 is not reused.

General k=2 preservation/failure remains unresolved.

Records:
- phase4/P4-S009_MATHEMATICS.md
- phase4/P4-S009_CLOSE.md
- phase4/P4-S009_VALIDATION.md

Next recommended session: **P4-S010**, still bounded to k=2, on whether threshold-capping makes the branchwise-avoidable deferred-wager value computable enough for an optional-projection transfer, or whether an exact adaptive singleton-spine witness can be built.

## P4-S010 — k=2 branchwise-avoidable capped optional-projection boundary

P4-S010 shows that output-capital capping does not by itself make the hard deferred-wager value computable. An exact total computable adaptive no-repeat scan consumes a fixed sentinel on a c.e.-open event of noncomputable fair-coin probability alpha and omits it otherwise; trigger fibres are singleton and nontrigger fibres have size two, so the scan is globally k=2 and fair-coin preserving. A computable martingale already bounded by 2 has eventual-consumption payoff whose exact first projected values after prequerying the sentinel are 1-alpha and 1+alpha. Hence the exact capped optional projection need not be computable, and its computable finite-horizon approximants need not have a computable convergence modulus.

This blocks the exact capped-projection route only; it is not a universal impossibility theorem for martingale transfer.

The session also verifies an adaptive least-unqueried-sentinel comb with the required global geometry. It is total, no-repeat, fair-coin preserving and globally k=2; all-trigger paths are singleton fibres; genuine sentinel bets are fresh; and future sentinels are chosen only after turnover from still-unqueried coordinates. The remaining decisive check is source randomness: no proof is obtained that an infinite all-trigger correct-prediction spine contains a computably random source. SRC-0061 is not reused.

No exact k=2 destroyer and no full global-k=2 scan preservation theorem is obtained. General k=2 preservation/failure remains unresolved.

Records:
- phase4/P4-S010_MATHEMATICS.md
- phase4/P4-S010_CLOSE.md
- phase4/P4-S010_VALIDATION.md

Next recommended session: **P4-S011**, still bounded to k=2, on whether the adaptive c.e.-trigger singleton-spine can contain a computably random winning source or instead forces one computable source martingale.

## P4-S011 — exact k=2 destruction via a computably random wtt-autoreducible spine

P4-S011 closes the source-randomness gap left by P4-S010. SRC-0067 / SRC-0068 / THM-0076 provide a computably random weak-truth-table-autoreducible sequence Y.

Use the autoreduction as the trigger predictor in the least-fresh-sentinel comb. While a prediction is unresolved, query fresh non-sentinel fillers. On a visible prediction, query the sentinel and begin the next epoch. The scan is everywhere total and no-repeat; finite output prefixes constrain distinct fair-coin source coordinates, so the induced map preserves fair coin.

If an epoch never triggers, fillers exhaust every coordinate except that epoch's sentinel, giving a two-point fibre. If every epoch triggers, every coordinate is eventually queried, giving a singleton fibre. Thus the map is globally k=2.

On Y every prediction halts and is correct. A computable output martingale stays flat on fillers and doubles on every sentinel, hence succeeds. Therefore exact k=2 forward computable-randomness preservation fails.

SRC-0061 is not reused. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. No k>2, novelty, Gate-4 or publication claim is made.

Records:
- phase4/P4-S011_MATHEMATICS.md
- phase4/P4-S011_CLOSE.md
- phase4/P4-S011_VALIDATION.md

Next recommended session: P4-S012, still at k=2, abstracting the weakest partial-predictor/autoreduction hypothesis sufficient for the destroyer and testing the converse inside the adaptive no-repeat scan subclass.
