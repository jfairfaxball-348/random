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


## P4-S012 — k=2 partial-predictor / scan-converse boundary

P4-S012 isolates the exact data used by P4-S011's least-fresh conversion. The weak-truth-table use bound is not used: it suffices that each generated target sentinel receives a finite visible self-avoiding correct partial prediction. Predictions at filler coordinates and totality on sibling oracles are unnecessary. More generally, the visible computation may output any rational fractional stake in [-1,1]; if the target stake capital is unbounded, the same least-fresh scan is total, no-repeat, fair-coin preserving, globally k=2, singleton on the target and defeated by a computable output martingale.

The converse is exact at the stake level. For a global-k=2 no-repeat scan winning on a computably random source, P4-S008 first forces singletonhood. For each coordinate j, simulate the scan from the start using the oracle away from j until the scan is about to query j. The winning rational martingale then determines a signed fractional stake. This partial functional never queries j, halts on the winning source for every j, and in the original scan order reproduces the output capital exactly.

A full all-correct bit-autoreduction converse is not obtained. Arbitrary fractional martingales may succeed while making infinitely many wrong favoured-bit wagers; all-in wagers on a succeeding path are necessarily correct. Re-embedding the scan-relative stakes into a different least-fresh order is also not justified automatically.

Records:
- phase4/P4-S012_MATHEMATICS.md
- phase4/P4-S012_CLOSE.md
- phase4/P4-S012_VALIDATION.md

Next recommended session: **P4-S013**, still at k=2, testing only the sibling-totality boundary: whether total-on-all-oracles, or a weaker effective uniform-totality/deadline condition, forces a computable source martingale for the least-fresh partial-stake subclass.

## P4-S013 — k=2 reachable-sentinel totality / finite-deadline boundary

P4-S013 proves a positive theorem for the P4-S011/P4-S012 least-fresh subclass. Full totality of the self-avoiding predictor/stake functional on every oracle and every input is sufficient, but is stronger than the scan actually needs.

The weaker condition is reachable-sentinel totality: whenever a run reaches an epoch with current sentinel j, the functional halts at j on that source. At a reachable epoch, the continuations on which no trigger is yet visible form a computable binary tree. Reachable-sentinel totality means that tree has no infinite path; finite branching then makes it finite, and a search for its first empty level gives a computable finite deadline. Thus qualitative sibling totality and a computably searchable deadline are equivalent in this architecture.

Consequently every epoch ends on every source. The scan queries every coordinate exactly once and all fibres are singleton. Its inverse is computable by simulating the output transcript until the requested source coordinate is queried. Hence the map is a computable fair-coin-preserving isomorphism and P4-S001 / SRC-0015 / THM-0038 gives computable-randomness invariance.

The finite deadline also makes the P4-S009 block hedge exact at every turnover, so the block hedges concatenate into one computable completion martingale.

Full oracle-totality is strictly stronger than needed: a functional may diverge on a coordinate which is always consumed as a filler and never becomes a sentinel.

This is a sufficient transfer boundary, not a necessary characterization of every preserving k=2 least-fresh scan. P4-S011 shows that target-only totality is insufficient and that branchwise avoidance can support destruction.

Records:
- phase4/P4-S013_MATHEMATICS.md
- phase4/P4-S013_CLOSE.md
- phase4/P4-S013_VALIDATION.md


## P4-S014 — computably budgeted avoidance tails

P4-S014 proves a preservation theorem strictly weaker than P4-S013 finite deadlines. At each reachable least-fresh epoch choose a total computable finite horizon H(s), and let p(s) be the exact conditional probability of still avoiding the sentinel at that horizon. If one finite computable budget bounds the sum of p(s) over all epoch states reached on every run, then every computable output-martingale win transfers to one computable source martingale.

The proof uses one globally exhaustive sentinel-first completion. A fair unit miss-ticket martingale succeeds if horizon misses occur infinitely often. A second finite-horizon conditional-expectation hedge tracks the output martingale exactly on good epochs; after a miss it copies later filler bets, skips only the already-revealed sentinel wager if that epoch eventually triggers, and restarts. Thus finitely many misses are harmless, while a permanently nontriggering missed epoch is copied forever. The sum succeeds whenever the output martingale succeeds, and P4-S001 transfers it back to the source.

The condition permits genuine infinite avoiding siblings. The zero-stake "wait for the next 1" functional has no finite deadlines, but horizons H_r=r+2 give tail budget at most 1/2. P4-S011 necessarily has no such budget certificate.

Records:
- phase4/P4-S014_MATHEMATICS.md
- phase4/P4-S014_CLOSE.md
- phase4/P4-S014_VALIDATION.md

Next recommended session: **P4-S015**, still at k=2, testing only whether a computable stake-weighted skipped-wager loss budget can weaken P4-S014 by allowing nonsummable raw horizon-miss probabilities.


## P4-S015 — stake-weighted skipped-wager loss budgets

P4-S015 weakens the P4-S014 unit miss-ticket budget for a fixed output martingale. Apply a computable savings wrapper so output success tends to infinity at all late prefixes without increasing fractional stakes. For each horizon-miss leaf, charge only a computable majorant of the positive multiplicative gain of the deferred sentinel wager that would be skipped if the epoch later triggers.

If H(s) is the finite horizon and w(s,b,rho) is the leafwise envelope, the exact fair ticket price is
c(s)=2^{-(H(s)+1)} sum_rho(w(s,0,rho)+w(s,1,rho)).
One finite computable uniform pathwise budget on sum c(s) is sufficient. Weighted tickets cover divergent realized miss weights; finite realized weight leaves the P4-S014 restart hedge at a positive multiplicative scale. P4-S001 then transfers the completion win to the source.

The coarser condition sum p(s)a(s)<infinity is sufficient when a computable epoch weight a(s) bounds every possible positive post-horizon sentinel gain. Raw miss probabilities need not be summable.

The weakening is strict at the scan/martingale certificate level. A two-control-bit stake functional triggers after 1 or 01 and diverges after 00. Permanent avoidance probability 1/4 at every epoch rules out every P4-S014 raw-tail certificate, while stakes a_j=2^{-(j+1)} have weighted ticket budget at most 1/4.

The exact pointwise minimal future-loss envelope is not uniformly computable. P4-S011's all-in destroyer necessarily violates every finite certificate of the P4-S015 form.

Records:
- phase4/P4-S015_MATHEMATICS.md
- phase4/P4-S015_CLOSE.md
- phase4/P4-S015_VALIDATION.md

Next recommended session: **P4-S016**, still at k=2, testing only whether the advance computable future-loss envelope can be replaced by incrementally purchased computable loss tickets under a computable total increment budget.


## Mathematics checkpoint — P4-S016 (not a gate review)

P4-S016 removes the extra advance future-loss envelope from P4-S015 inside the k=2 least-fresh stake subclass. After a finite-horizon miss, each unresolved state still has a fresh filler bit. Before that bit is drawn, both possible child states can be simulated. If a child makes the sentinel trigger, the exact positive skipped gain of the savings-wrapped output martingale is computable; otherwise its immediate loss is zero. The exact one-step fair ticket price is the average of those two child losses.

A finite computable uniform pathwise bound on the sum of these automatic last-chance fair prices funds one insurance martingale. If realized skipped gains diverge, insurance succeeds; if they have finite sum, the restart hedge keeps a positive multiplicative scale and succeeds with the savings-wrapped output martingale. The sentinel-first completion remains an effective isomorphism, so one source martingale follows.

No infinite optional projection, future supremum or advance computable loss envelope is used. The one-step premium is locally minimal for this ticket architecture. P4-S015 and P4-S016 numerical certificates are not claimed globally ordered.

P4-S011 violates the incremental premium condition on its target path for every computable horizon selector: its realized skipped-gain sum must diverge, and each final pre-trigger premium is at least half the realized loss.

P4-S005 through P4-S015 remain settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S017, still restricted to k=2, testing only whether the absolute pathwise premium-sum budget can be weakened to a computable self-financing reserve condition.

## P4-S017 — self-financing last-chance reserves

P4-S017 weakens the P4-S016 bankroll hypothesis for the same exact ticket stream. Earlier payouts may fund later premiums. The full-ticket account is admissible when it can buy every next ticket on every run without going negative, and coercive when divergent cumulative realized skipped gain forces it unbounded.

Admissibility plus coercivity is sufficient with the settled restart hedge. P4-S016 absolute premium summability implies this condition. For fixed H the converse can fail: a two-filler example has harmonic total premiums but reserve 1/2 grows from winning tickets. Bare solvency is not enough.

P4-S011 has no coercive reserve certificate for any computable horizon selector. Bare admissibility alone is not excluded.

Records:
- phase4/P4-S017_MATHEMATICS.md
- phase4/P4-S017_CLOSE.md
- phase4/P4-S017_VALIDATION.md

Next recommended session: **P4-S018**, testing only whether semantic coercivity can be replaced by a local computable reserve-floor / retained-surplus modulus.

## Mathematics checkpoint — P4-S018 (not a gate review)

P4-S018 completed the k=2 effectivity-of-coercivity investigation for the P4-S017 self-financing last-chance account.

A computable running-maximum coercivity modulus is sufficient: for each integer K, a computable threshold h(K) may require that any finite history with cumulative realized skipped loss E>=h(K) has already reached ticket capital K. This uses only finite ticket history, may grow arbitrarily slowly, and remains strictly weaker than absolute premium summability.

The condition is not equivalent to semantic coercivity. A computable mode switch between the two settled P4-S017 gadgets gives a semantically coercive exact k=2 ticket stream with arbitrarily large finite deterministic-loss bursts while ticket capital stays 1. Thus no uniform loss-to-capital threshold exists even noncomputably. The exact set-theoretic strengthening is loss-properness b(K)=sup{E(v):W*(v)<K}<infinity.

P4-S011 admits no effective modulus for any computable horizon selector. P4-S005 through P4-S017 remain settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S019, testing only whether finite loss-properness bounds b(K) are automatically computably bounded.

## Mathematics checkpoint — P4-S019 (not a gate review)

P4-S019 resolves the remaining effectivity layer from P4-S018 negatively. For an admissible computable ticket account, b(K)=sup{E(v):W*(v)<K} is uniformly lower semicomputable, but finiteness of b(K) for every K does not force any computable uniform upper bound.

The exact k=2 counterexample uses only settled P4-S017 gadgets. Zero-stake controls choose a machine index, finitely many one-sided-trigger wins raise ticket capital to a computable level, zero-stake epochs wait on that machine, and a finite deterministic-ticket burst records its halting time in realized skipped loss while ticket capital stays fixed. For each fixed capital target K only finitely many machine indices can reach that waiting/burst phase below K, so b(K) is finite. If a computable function majorized all b(K), effective divergence of harmonic sums would turn that bound into a computable halting-time bound and decide the halting problem.

Thus the exact numerical extra condition for the settled ticket/restart proof is effective loss-properness: a computable U(K) uniformly bounding E on W*<K histories. Up to a harmless margin, this is equivalent to the P4-S018 running-maximum coercivity modulus. Mere set-theoretic loss-properness is strictly weaker.

P4-S011 is excluded more strongly: for every computable horizon selector, any globally admissible full-ticket account must fail loss-properness at some K; otherwise its divergent realized skipped loss on the computably random sentinel-first completion would force ticket-martingale success. Bare admissibility alone remains unruled-out.

P4-S005 through P4-S018 remain settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S020, testing only whether a natural local bound on zero-loss waiting / positive-loss reachability, or a weaker effectively searchable loss-bar condition, turns loss-properness into effective loss-properness without restoring absolute premium summability.

## Mathematics checkpoint — P4-S020 (not a gate review)

P4-S020 shows that merely bounding zero-loss waiting does not effectivize P4-S019 loss-properness. The halting-coded construction can be heartbeatized with summably small deterministic positive-loss tickets: any branch that will later realize more positive loss sees another positive loss within a fixed computable number of epochs, while nonhalting branches still accumulate only bounded heartbeat loss and a late halt still unlocks an effectively divergent finite burst. Thus the remaining obstruction is loss-scale nonuniformity, not simply long intervals on which E is constant.

A positive structural condition is a computable loss-level witness modulus D(K,m): whenever some history with W*<K has E>=m, one such witness occurs by depth D(K,m). Finite search then decides loss-level reachability and the complementary loss-bar predicate. Under set-theoretic loss-properness, searching for the first unreachable integer loss level computes a uniform bad-capital loss bound U(K), hence the P4-S018 coercivity modulus. A stronger branchwise amount-sensitive progress modulus implies this condition, but is not needed.

This searchability condition does not restore absolute premium summability: the settled one-sided-trigger harmonic account has computably searchable loss levels while its premium sum diverges on the all-trigger branch. P4-S011 remains excluded already at the stronger P4-S019 level: any globally admissible full-ticket account for it fails set-theoretic loss-properness at some K. Bare admissibility remains unruled-out.

P4-S005 through P4-S019 remain settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S021, still restricted to k=2, testing whether searchable loss levels follow from local scale-tail data weaker than an explicit witness modulus—such as computable waiting bounds for losses at least 2^-n together with computable control of cumulative smaller losses while W*<K—or whether halting information can still move across infinitely many shrinking loss scales.


## Mathematics checkpoint — P4-S021 (not a gate review)

P4-S021 resolves the local scale-tail question in two layers. A computable waiting bound for reachable losses at least \(2^{-n}\), together with a computable bound on the total contribution of smaller realized losses inside each bad-capital tree, is enough to turn set-theoretic loss-properness into effective loss-properness. Coarse-scale accumulated-loss reachability is searchable by a finite witness-depth bound; one then searches for an unreachable coarse-scale amount and adds the computable small-loss tail bound. This yields U(K) and hence the P4-S018 coercivity modulus.

This does not restore absolute premium summability: the settled one-sided-trigger harmonic account satisfies the scale-tail condition while its premium sum diverges.

The stronger P4-S020 loss-level witness modulus does not follow. An exact globally k=2, globally admissible index-ladder/geometric-tail construction can have computable global deadlines for every fixed loss scale, an effectively vanishing small-loss tail and an explicit computable linear U(K), while exact \(\operatorname{Reach}(K_e,m_e)\) with \(K_e=e+2\), \(m_e=2e+2\) is equivalent to halting of machine e. A divergent machine approaches the boundary from below through shrinking losses; a halt triggers one finite correction block which attains it. The remaining obstruction is therefore anti-Zeno / boundary-isolation effectivity, not loss-mass effectivity.

P4-S011 fails the scale-tail hypothesis strongly under global admissibility: its computably random completion has bounded ticket capital but a divergent missed-epoch subseries of gains \(1/(r+1)\), so for every n the cumulative contribution of gains below \(2^{-n}\) is unbounded in one bad-capital tree. Bare admissibility remains unruled-out.

P4-S005 through P4-S020 remain settled. P4-S011 and P4-S015 through P4-S020 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S022, still at k=2, testing only whether a computable anti-Zeno / boundary-isolation condition weaker than an explicit P4-S020 witness modulus makes exact loss-level reachability decidable, or whether halting information survives another shrinking-scale coding.

## Mathematics checkpoint — P4-S022 (not a gate review)

P4-S022 derives computable fixed-scale exhaustion frontiers from P4-S021's effective loss bound and large-loss waiting modulus. At an n-quiet frontier, the remaining subscale contribution has a computable residual cap Q. A strict inequality (E+Q<m) is a finite certificate that no continuation in the bad-capital tree reaches the queried integer boundary.

If every false Reach(K,m) eventually has such a strict frontier certificate, exact Reach is decidable by dovetailing it with the already-c.e. positive witness search. A separate “must cross within bounded depth” arm is not needed.

This local condition is not strictly weaker than P4-S020 in final effective content: decidable Reach computes a witness modulus D(K,m). The difference is only that the primitive data are local scale-tail separation certificates rather than a root-level witness bound.

The P4-S021 geometric halting construction is sharp. On a nonhalting selected-e branch, the exact computable residual geometric tail equals the current gap to (m_e); a halt pays that residual in one finite correction. Hence nonstrict (E+Qle m) control leaves halting information intact.

P4-S011 remains outside the scale-tail regime under global admissibility. P4-S005 through P4-S021 remain settled; PA-0001 and DEF-0020 are unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: **P4-S023**, still at k=2, testing only whether semantic exclusion of nonattaining integer-boundary Zeno paths plus P4-S021 strong effective tail convergence forces a searchable strict frontier gap by effective compactness, or whether incompatible branches can preserve halting information.


## P4-S023 — semantic anti-Zeno plus effective compactness

P4-S023 proves that the strong P4-S021 tail form — computable global fixed-scale exhaustion together with a uniformly/effectively vanishing subscale tail — turns semantic anti-Zeno into the strict P4-S022 frontier certificate.

For false Reach(K,m), failure of every strict frontier gap would produce finer bad-capital nodes with E approaching m. Uniform tail convergence makes late additional loss negligible on all branches. Compactness therefore yields one infinite bad-capital branch whose loss converges to m from below without finite attainment, contradicting semantic anti-Zeno.

Hence exact Reach is decidable under the promise and P4-S020's witness modulus is recoverable. The proposed incompatible-branch halting escape cannot satisfy all strong-tail and semantic anti-Zeno hypotheses. P4-S011 remains outside the strong tail regime under global admissibility.

Records:
- phase4/P4-S023_MATHEMATICS.md
- phase4/P4-S023_CLOSE.md
- phase4/P4-S023_VALIDATION.md

P4-S005 through P4-S022 remain settled. P4-S011 and P4-S015 through P4-S022 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Next recommended session: **P4-S024**, restricted to whether uniform effective tail convergence can be weakened to pointwise or branchwise convergence while retaining semantic anti-Zeno.

## Mathematics checkpoint — P4-S024 (not a gate review)

P4-S024 shows that P4-S023's uniform-tail hypothesis cannot be weakened all the way to genuinely nonuniform pointwise/branchwise effective convergence. An exact computable globally k=2, globally admissible comb retains computable exhaustion of every fixed positive loss scale and an explicit computable bad-capital loss bound, while every individual bad-capital branch has only finitely many positive losses and is therefore eventually loss-constant and semantically non-Zeno.

Nevertheless exact \(\operatorname{Reach}(K_e,m_e)\), with \(K_e=e+2\) and \(m_e=2e+2\), is equivalent to halting. On divergence, later incompatible teeth have final losses approaching \(m_e\), while their Cantor-limit all-continue spine stays at \(m_e-2\). The branch-limit loss is discontinuous, so near-boundary mass can disappear at the compact limit and no searchable strict frontier gap is forced.

There is a positive boundary: if "branchwise effective" means one oracle-uniform functional returning a correct convergence modulus on every bad-capital branch, effective compactness finds a finite subcover of its halting cylinders and compiles those moduli into one computable global tail modulus. P4-S023 then applies. Thus this oracle-uniform form is not a genuine weakening.

P4-S011 remains outside even the weak pointwise-tail regime under global admissibility. P4-S005 through P4-S023 remain settled; P4-S011 and P4-S015 through P4-S023 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S025, testing only whether effective upper-semicontinuity of the branch-limit loss, or an equivalent computable local tail-cap basis, is enough with semantic anti-Zeno to recover searchable strict frontier separation.

## Mathematics checkpoint — P4-S025 (not a gate review)

P4-S025 shows that a complete effective upper-semicontinuity / local upper-cap basis for the bad-capital branch-limit loss is sufficient with semantic anti-Zeno, but is not genuinely weaker than P4-S023's uniform-tail regime. Tight local upper-cap cylinders form a c.e. cover of the computable pruned bad-capital branch space; effective compactness finds a finite subcover and yields a computable global uniform tail modulus. Conversely, a computable uniform tail modulus enumerates a complete effective upper-cap basis.

Semantic anti-Zeno therefore forces a searchable strict frontier gap, decidable Reach(K,m), and recovery of the P4-S020 witness modulus.

The sharp remaining obstruction is effectivity rather than ordinary continuity. An exact globally k=2, globally admissible delayed-activation comb has computable fixed-scale exhaustion, effective loss-properness, eventual loss-constancy and semantic anti-Zeno on every bad-capital branch, and a continuous branch-limit loss, yet \(\operatorname{Reach}(e+2,2e+2)\) is equivalent to machine-e halting. The missing information is the effective upper-cap / continuity modulus.

Boundary-specific effective caps can be weaker as primitive syntax, but if they cover all false integer Reach instances they amount to the already-settled positive semidecidability of Bar(K,m) and recover P4-S020 searchability.

P4-S011 remains outside even the finite branch-limit regime under global admissibility. P4-S005 through P4-S024 remain settled; P4-S011 and P4-S015 through P4-S024 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S026, testing only whether a one-sided effective boundary-modulus weaker than complete effective upper-semicontinuity can arise structurally without already restating searchable Bar / decidable Reach.

## Mathematics checkpoint — P4-S026 (not a gate review)

P4-S026 separates one-sided integer-boundary effectivity from full effective upper-semicontinuity. A computable globally admissible exhaustive k=2 deterministic-ticket stream can have constant branch-limit loss \(\alpha<1/4\) for a noncomputable left-c.e. real \(\alpha\). Every integer boundary \(m\ge1\) then has the trivial effective root cap \(1/4\), while a complete rational upper-cap basis would make \(\alpha\) right-c.e. as well as left-c.e., hence computable. Thus integer-boundary caps are genuinely weaker as presentation data than the P4-S025 upper-cap basis.

That weakening does not create a new exact-boundary searchability level. Any uniformly c.e. sound local certificate system complete for all branches with \(L_K<m\) semidecides true Bar(K,m) under semantic anti-Zeno: the certified cylinders cover the computable pruned bad-capital path space, and effective compactness finds a finite subcover. Since Reach(K,m) already has c.e. finite witnesses, dovetailing decides Reach and recovers the P4-S020 witness modulus.

The collapse is independent of certificate syntax. Rational caps, residual bounds, oracle-uniform integer-clearance functionals and arbitrary c.e. strict-sublevel certificates all have the same final effective consequence once they are boundary-complete. To remain below P4-S020, a future notion must sacrifice c.e. sound-certificate enumeration or completeness for every false boundary.

P4-S011 remains preserved. Under global admissibility its known completion has a bounded-capital branch with divergent realized skipped loss, so it remains outside the full finite-limit P4-S025 regime. The weaker P4-S026 boundary-only notion is not refuted by that branch because every integer boundary is eventually reached there. Bare admissibility remains unresolved.

P4-S005 through P4-S025 remain settled; P4-S011 and P4-S015 through P4-S025 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S027, testing only whether some computable horizon selector and finite reserve make the canonical P4-S016/P4-S017 full-ticket account for P4-S011 globally admissible, without coercivity or loss-properness.

## Mathematics checkpoint — P4-S027 (not a gate review)

P4-S027 resolves the repeatedly deferred bare-bankroll question for the settled P4-S011 wtt destroyer positively after the standard globally use-clipped normalization of its autoreduction witness.

Let U(j) be a computable strict use cap. At each least-fresh epoch choose a finite horizon long enough to expose every still-unqueried non-sentinel coordinate below U(j), plus one harmless extra filler. If the epoch is still unresolved after that horizon, every oracle bit the clipped predictor can ever inspect is already fixed. A later trigger can still be delayed by computation time or fail forever, so this does not restore reachable-sentinel totality.

At every postmiss P4-S016 last-chance node, the next filler bit is outside the dependency frontier. Consequently both filler children either remain unresolved or trigger with the same prediction and the same skipped positive gain. Every positive ticket is therefore deterministic: its exact fair premium equals its certain payout. Since all positive multiplicative skipped gains are at most 1, reserve R=1 funds every full ticket on every completion branch and the resolved account stays exactly 1.

On the P4-S011 computably random target, settled P4-S016 still forces divergent realized skipped gain for this horizon. Here the premium sum diverges equally while the ticket account stays constant. Thus P4-S016 absolute summability, P4-S017 coercivity, P4-S019 loss-properness and all later transfer/searchability hypotheses continue to fail. P4-S011 is preserved.

P4-S005 through P4-S026 remain settled; P4-S011 and P4-S015 through P4-S026 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: P4-S028, testing only whether an effectively exhaustible per-epoch dependency frontier is the weakest natural structural condition behind this bare-admissibility result, or whether its absence permits an exact global-k=2 sibling family forcing unbounded reserve demand.


## Mathematics checkpoint — P4-S028

P4-S028 isolates the structural content of P4-S027's use-bound argument. A wtt presentation is unnecessary: any computable finite per-epoch dependency frontier whose exhaustion makes later trigger data independent of future filler values yields a computable frontier-exhausting horizon. Beyond that horizon every positive P4-S016 ticket is deterministic, so its fair premium equals its certain payout and reserve R=1 is globally admissible.

The P4-S012 partial-predictor setting does not force such a frontier. A self-avoiding first-1-search predictor gives an exact total, fair-coin-preserving global-k=2 scan with no finite first-epoch frontier. On the sentinel-first sibling with stored sentinel 1 and all later fillers 0, every post-horizon node has last-chance loss vector (0,1), premium 1/2 and actual payout 0. Hence every finite horizon leaves unbounded cumulative premium deficit and no finite reserve can be globally admissible.

This is an existence separation, not a necessity theorem: no-frontier predictors may still conceivably be solvent when one-sided skipped gains decay. P4-S011 remains unchanged and lies on the positive side because P4-S027 supplies its finite use frontier. P4-S015 through P4-S027 remain settled.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Records:
- phase4/P4-S028_MATHEMATICS.md
- phase4/P4-S028_CLOSE.md
- phase4/P4-S028_VALIDATION.md

Recommended next bounded session: **P4-S029**, testing only whether finite dependency frontiers are necessary for bare admissibility or whether effectively decaying one-sided exposure gives an exact no-frontier solvent example.
