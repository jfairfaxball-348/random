# Phase 4 — Mathematics records

**Live checkpoint: P4-S090 completed; P4-S091 next.** R₂⊊R₂^{cdz} and OH^iso⊊OH^aff are proved in the S090 record; R₂ versus MLR and Conjecture R remain unresolved. See authoritative/STATE.json and authoritative/NEXT_SESSION_PROMPT.md for current scope. Earlier session-specific next-step references below are historical.

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


## Mathematics checkpoint — P4-S029

P4-S029 shows that P4-S028's finite dependency frontier is sufficient but not necessary for bare canonical full-ticket admissibility.

Reuse the exact P4-S028 first-1-search global-k=2 scan, so the initial epoch still has no finite dependency frontier and a later unseen filler can trigger the sentinel at every depth. Change only the output martingale: if the first 1 appears at filler n, make a fractional sentinel wager of size (2^{-n}), then freeze. With H=1, the stored-sentinel-1 postmiss tickets are ((0,2^{-n})), with fair premiums (2^{-(n+1)}) for n>=2. Their whole zero-payout tail sums to 1/4, so reserve R=1/4 is globally admissible.

More generally, in the same first-1-search geometry a stake sequence (alpha_n) gives one-sided premium (alpha_n/2). Summable tails yield finite reserve; divergent tails fail on the stored-sentinel-1/all-zero sibling. Thus P4-S028 is the constant (alpha_n=1) insolvent case, while P4-S029 is the summably decaying solvent case.

P4-S011/P4-S027 remains a different recycling mechanism: its finite frontier makes each positive ticket deterministic, so premium equals certain payout and reserve one can recycle even when premiums diverge. P4-S005 through P4-S028 remain settled; P4-S011 and P4-S015 through P4-S028 are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Records:
- phase4/P4-S029_MATHEMATICS.md
- phase4/P4-S029_CLOSE.md
- phase4/P4-S029_VALIDATION.md

Recommended next bounded session: **P4-S030**, testing only whether no-frontier bare admissibility can survive divergent absolute premium sums through genuine self-financing payout recycling while arbitrarily late one-sided tickets remain.


## Mathematics checkpoint — P4-S030

P4-S030 separates no-frontier solvency from absolute premium summability. There is an exact total computable no-repeat fair-coin-preserving global-k=2 least-fresh scan whose active epochs have no finite dependency frontier and retain one-sided trigger opportunities at every arbitrarily late post-horizon depth, but whose canonical P4-S017 full-ticket account is globally admissible with reserve R=3/4 while premiums diverge on a completion run.

Take H=1 after one ignored dummy filler. In an active epoch, if the first later 1 appears immediately, expose stake 1 on the sentinel being 1; if it first appears at depth m>=2, expose stake 2^{-m}; if none appears, diverge. An immediate favorable trigger renews the active mode. Any late trigger or unfavorable sentinel makes all future stakes zero.

After r early favorable renewals, the P4-S015 savings wrapper has total capital r+1 and active risk 1, so the immediate skipped gain is a_r=1/(r+1). The first one-sided ticket has premium a_r/2 and favorable payout a_r. If it loses, the complete later premium tail is only a_r/4. Therefore an active epoch can draw down at most 3a_r/4, and reserve 3/4 funds every completion. On the all-early-favorable completion the premiums 1/(2(r+1)) diverge harmonically, while ticket payouts recycle and grow the bank.

P4-S029 is the summable-decay case; P4-S028 is the zero-payout divergent-deficit case; P4-S011/P4-S027 is deterministic-frontier recycling. P4-S030 is distinct: divergent premiums are funded by genuinely one-sided favorable payouts while no-frontier late risk remains.

Records:
- phase4/P4-S030_MATHEMATICS.md
- phase4/P4-S030_CLOSE.md
- phase4/P4-S030_VALIDATION.md

P4-S005 through P4-S029 remain settled. P4-S011 and P4-S015 through P4-S029 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: **P4-S031**, testing only whether P4-S030's terminalization of late triggers is essential, or whether every finite trigger can renew an active no-frontier epoch under one finite global reserve.

## Mathematics checkpoint — P4-S031 (not a gate review)

P4-S031 shows that P4-S030's late-trigger terminalization is not essential for bare no-frontier solvency. There is an exact P4-S012 total computable no-repeat fair-coin-preserving global-k=2 least-fresh scan in which every finite trigger, including an arbitrarily late genuinely one-sided trigger, renews another active no-frontier epoch.

Use H=1 after one ignored dummy filler and attach a positive scale c to every active epoch. The first post-horizon 1 exposes stake c if immediate and c2^{-m} if first seen at later depth m>=2. Immediate triggers keep scale c; late triggers renew at scale c/4. No trigger enters dead mode.

For an arbitrary P4-S015 savings-wrapper state, write beta for active risk divided by total q-capital. The whole possible premium exposure of one active epoch is at most 3 beta c/4 <= 3c/4. The invariant W>=c therefore closes with initial reserve R=1: an immediate positive trigger is self-financing and keeps scale c, while after any late trigger at least c/4 remains even if its nonnegative payout is ignored, exactly funding the renewed scale c/4. An infinite nontriggering epoch also remains within the same 3c/4 bound.

On the all-immediate-favourable completion, c remains 1 and the settled savings wrapper gives premium 1/(2(r+1)) and payout 1/(r+1) at epoch r. Premiums diverge harmonically while realized one-sided payouts finance later purchases.

P4-S030 is the terminal case; P4-S029 is the absolute-summability case; P4-S028 is the zero-payout divergent-deficit case; P4-S011/P4-S027 is deterministic-frontier recycling. P4-S005 through P4-S030 remain settled; P4-S011 and P4-S015 through P4-S030 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Recommended next bounded session: **P4-S032**, testing only whether the explicit positive scale contraction after late triggers can also be removed, so every finite trigger renews the same raw active stake scale under one finite global reserve, or else isolating the narrow stationary repeatable-late-trigger deficit condition.

## Overriding Phase-4 direction after P4-S031 — sustained finite-ambiguity pivot

Owner direction after completed P4-S031 freezes all validated mathematics through P4-S031 and changes the default Phase-4 trajectory.

Do **not** automatically continue the P4-S015–P4-S031 ticket/reserve/frontier/recycling refinement sequence. Those results remain settled machinery and may be reused if a deeper theorem needs them.

The organising question is now:

> **What mathematical resource is exposed by the jump from injective observation to one binary degree of inverse ambiguity, and what else does that resource control?**

The forward programme is organised around: robustness classes R_k; structural thresholds strictly between injective and bare k=2 maps; reverse/randomness-creation phenomena; selected cross-randomness comparisons; composition/factorisation and ambiguity budgets; identifying an invariant deeper than fibre cardinality; mutations of the P4-S011 machine; and converses from k=2 vulnerability to source-side predictive structure.

P4-S032 is the first reconnaissance/theorem-selection session of this sustained branch. It must perform enough exact mathematics across several axes to select the strongest theorem target for multi-session pursuit, rather than choosing the smallest available local lemma.

The old session-local strict-k=2 default is lifted only where finite k>2, composition or factorisation is mathematically required by this programme. No k>2 theorem is asserted merely by the pivot.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty/prior-art conclusion, Gate-4, publication or outreach work is authorized. Phase 4 remains OPEN and Phase 5 CLOSED.

Authoritative pivot record: phase4/P4_RESEARCH_PIVOT_AFTER_S031.md.
This note supersedes earlier P4-S032 recommendations that asked only for the next bankroll/ticket refinement.


## Mathematics checkpoint — P4-S032 (finite-ambiguity reconnaissance)

P4-S032 begins the sustained post-P4-S031 pivot and does not reopen the frozen ticket/reserve sequence.

It formalizes R_k and R_fin. Settled mathematics gives R_1=CR, monotonicity R_{k+1} subseteq R_k, and P4-S011 makes every R_k for k>=2 (and R_fin) a proper subclass of CR. THM-0035 gives MLR subseteq R_fin. THM-0036 gives a useful cross-randomness boundary: every total computable fair-coin-preserving image of a computably random source remains Schnorr random, so P4-S011 destroys CR without destroying Schnorr/Kurtz randomness.

The new structural theorem is null-ambiguity preservation. If a total computable fair-coin-preserving map has non-singleton output fibres only on a null set, its singleton-fibre locus supports an a.e.-computable fair-coin-preserving inverse, so THM-0038 yields CR preservation. Effective nullness is not needed. This boundary is measure-sharp: localizing P4-S011 in an arbitrarily small clopen cylinder yields global-k=2 destroyers with positive ambiguity measure below every epsilon. P4-S002's two-to-one left shift remains a measure-one-ambiguity preserving example, so ambiguity mass is not the invariant.

Composition obeys multiplicity jk and F_j(R_jk) subseteq R_k; binary factorisation alone therefore does not collapse R_2 to higher robustness because the intermediate image would need hereditary R_2 robustness.

In the adaptive no-repeat scan subclass, h permanently omitted coordinates give exactly 2^h preimages. Thus k=2 is exactly a one-hole budget. P4-S011 nevertheless destroys on a target with zero final holes, showing that the operative resource is renewable/migratory counterfactual ambiguity rather than a permanently hidden inverse bit.

P4-S032 selects the sustained theorem target **one-hole normalization**. Let OH be CR sources robust under every total computable one-hole adaptive no-repeat scan. Then MLR subseteq R_2 subseteq OH proper-subset CR. The next programme asks whether R_2=OH, so arbitrary k=2 destruction would normalize to the P4-S012 self-avoiding stake mechanism, or whether a genuinely non-scan resource exists.

Records:
- phase4/P4-S032_MATHEMATICS.md
- phase4/P4-S032_CLOSE.md
- phase4/P4-S032_VALIDATION.md

P4-S005 through P4-S031 remain settled; P4-S011 and P4-S015 through P4-S031 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

Recommended next session: **P4-S033**, attacking the first one-hole normalization step from the effective width-two inverse skeleton.

## Mathematics checkpoint — P4-S033 (first one-hole normalization step)

P4-S033 sharpens the selected equation R_2=OH without deciding it. P4-S007's width-two inverse skeleton supplies one binary inverse cohort, but a one-hole scan has a strictly stronger raw-coordinate property: every double fibre consists of two source points differing at exactly one coordinate. Thus width two alone does not canonically identify a scan hole.

The session proves that R_2 is invariant under every computable fair-coin-preserving homeomorphism and introduces

OH^iso = {x in CR : H(x) is in OH for every computable fair-coin-preserving homeomorphism H}.

Hence MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR. Equality R_2=OH therefore requires OH itself to be homeomorphism-invariant. Any x in OH with H(x) outside OH would immediately give x in OH\R_2.

A positive same-source normalization theorem is proved for signed coordinate permutations, even with arbitrary computable fair-coin-preserving output homeomorphism: the virtual one-hole scan is compiled by permuting its queried coordinates and applying known child swaps to the martingale.

Literal map-level normalization is false. Precompose the exact P4-S011 one-hole destroyer with an explicit invertible three-bit linear source homeomorphism whose inverse maps a unit virtual-coordinate difference to Hamming weight 2, 2 or 3. The conjugate remains total, fair-coin preserving, globally k=2 and destructive, but every double fibre differs in at least two raw coordinates, so it is not a one-hole scan and cannot become one by output-homeomorphic postprocessing.

The remaining obstruction is therefore a **coded hole**: one binary inverse choice delocalized across several raw source coordinates. It remains open whether such coded-hole vulnerability always implies vulnerability to some different raw one-hole scan on the same source.

Records:
- phase4/P4-S033_MATHEMATICS.md
- phase4/P4-S033_CLOSE.md
- phase4/P4-S033_VALIDATION.md

All mathematics through P4-S032 remains preserved. The P4-S015–P4-S031 bankroll line remains frozen as the default trajectory. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

Recommended next session: **P4-S034**, testing homeomorphism invariance of OH at the explicit three-bit coded-hole map, first at the P4-S012 self-avoiding stake level.

## Mathematics checkpoint — P4-S034 (finite recoding invariance and spoiled-parity obstruction)

P4-S034 attacks OH homeomorphism invariance at the explicit P4-S033 three-bit source recoding without returning to the frozen ticket/reserve line.

At the P4-S012 stake level, a virtual self-avoiding wager pulls back through the three-bit linear map to a **coded/vector-self-avoiding** raw wager: it is invariant under the inverse image of the queried virtual unit flip, namely one of \((1,1,0),(1,0,1),(1,1,1)\). This need not avoid any individual raw coordinate.

A canonical support evaluator gives a stronger exact reduction. For any repeated invertible finite binary block matrix, evaluate a requested virtual parity by querying its still-fresh raw support; copy the virtual fractional wager on the last fresh pivot and hold on earlier support bits. If the whole support is already known, the virtual wager is **spoiled** and is skipped. The resulting raw scan is always one-hole. For the displayed three-bit matrix every raw column has weight at least two, so the evaluator is exhaustive and hence an effective isomorphism.

Therefore, on a computably random raw source, all copied live-pivot gain is bounded. If a martingale still succeeds after the three-bit recoding, its multiplicative gain over spoiled stages must be unbounded. The surviving resource is thus late selection of a wager on a virtual parity already determined by earlier raw queries.

P4-S034 also proves a genuine positive invariance theorem beyond P4-S033: **OH is invariant under every computable finite-coordinate fair-coin recoding**, hence under the group generated by such recodings and signed coordinate permutations. A finite CNOT is already outside the signed-permutation class. Every finite truncation of the repeated three-bit recoding therefore preserves OH; any failure for the full map must be infinitary.

No \(x\in OH\) with \(H(x)\notin OH\) is proved, so \(R_2\subsetneq OH\) is not claimed. The retained comparison is
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Records:
- phase4/P4-S034_MATHEMATICS.md
- phase4/P4-S034_CLOSE.md
- phase4/P4-S034_VALIDATION.md

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. Phase 4 remains OPEN; Phase 5 remains CLOSED.

Recommended next session: **P4-S035**, formalizing spoiled-stage raw determination times and separating early-decided from genuinely late-decided spoiled wagers.

## Mathematics checkpoint — P4-S035 (early-decision normalization and infinite dependency nonclosure)

P4-S035 sharpens the P4-S034 spoiled-parity obstruction without reopening the frozen ticket/reserve line.

For the displayed three-bit recoding, a computable support order separates spoiled determination pivots. If every spoiled fractional stake is uniformly fixed **before** its determining raw pivot is read, the spoiled-gain product itself is a computable raw martingale. Since P4-S034 forces any destruction to have unbounded spoiled gain, every actual destructive witness must use genuinely non-predictable late choice.

If a stake is selected only after the same pivot is seen, its factor splits into a legal raw martingale factor times an exact computable late-choice premium. Unbounded gain in that synchronous class therefore requires an unbounded product of those premiums.

A stronger finite-memory theorem holds for all repeated invertible finite binary block matrices of block size at least two: every block-closed, and more generally every uniformly bounded packet-closed, one-hole witness is harmless. The whole finite packet is pulled back by exact finite Doob conditional expectations, and the raw packet scan is exhaustive.

Bounded decision delay alone is not enough. P4-S035 gives an exact one-hole architecture in which the pending spoiled parity in block \(b\) takes its stake information from block \(b+1\), which creates the next pending parity. Every individual delay is bounded, but no finite packet closes the all-trigger dependency chain.

No OH non-invariance witness is proved. The retained comparison is
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Next: **P4-S036**, formalize the block-dependency graph and attack finite/well-founded closure versus a genuine infinite dependency ray.

## Mathematics checkpoint — P4-S036 (finite closure and infinite-component obstruction)

P4-S036 materially strengthens the P4-S035 closed-packet theorem. A standard persistent-savings transform turns every successful computable martingale into an exactly computable rational martingale whose capital tends to infinity. Therefore success cannot hide only inside larger and larger finite packets. For every repeated invertible finite binary block recoding of block size at least two, **every computably finite packet-closed witness is harmless, with no uniform packet-size bound**. The same finite Doob argument works for a total computable online closed packetizer which knows the complete finite packet at entry.

The dependency analysis also shows what this does not cover. Set-theoretic finite forward closure, semantic well-foundedness, finite/computable rank, and even uniformly computable finite forward closures do not by themselves imply finite packetization. Rank-one examples isolate both failures: closure completion can hide halting information, and finite forward closures can overlap into one infinite symmetrized interaction component even when there is no directed infinite ray.

For the displayed three-bit map, no reordering of raw coordinates can retain a pivot for \(u_2^{(b)}\) after \(u_0^{(b)},u_1^{(b)}\) have been produced. Every finite dependency-ray truncation nevertheless has an exact finite Doob compiler. The remaining issue is effective passage to the infinite limit: bounded computable martingales may have noncomputable pointwise limits, so classical bounded/uniformly-integrable convergence is not an effective compiler.

Applied to the recoded P4-S011 destroyer, the new theorem proves that no total computable finite closed packetizer can exist for that witness. It does not decide whether the obstruction is a genuine directed ray or overlapping finite wtt closures, and it does not prove the recoded source lies in \(OH\).

The retained comparison remains
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Records:
- phase4/P4-S036_MATHEMATICS.md
- phase4/P4-S036_CLOSE.md
- phase4/P4-S036_VALIDATION.md

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. The P4-S015–P4-S031 bankroll line remains frozen as the default trajectory.

Recommended next session: **P4-S037**, on rolling finite-state normalization and finite-horizon backward fair-price vectors for infinite interaction components.



## Mathematics checkpoint — P4-S037 (rolling renewal and persistent-claim boundary)

P4-S037 moves the positive one-hole normalization boundary beyond finite packetization.

A finite open-claim frontier is harmless when it has **effective fresh-frontier renewal**: a computably finite transition retires all old spoiled claims and hands off to new virtually unseen fair parities. The normalized continuation price then has conditional mean one and disappears exactly from the previous backward step. Combined with the P4-S036 persistent-savings transform, this yields one computable raw martingale.

Consequently the explicit P4-S035 infinite directed ray normalizes, and so does the concrete P4-S036 rank-one infinite overlap architecture. Neither an infinite directed ray nor an infinite symmetrized interaction component is by itself the obstruction.

The sharper negative boundary comes from the recoded P4-S011 witness. It has active nonzero open-claim width one and finite computable frontier state. A fixed half-stake sentinel martingale still succeeds while its local triggered prices stay in ([1/2,3/2]), ratio at most (3). Thus bounded width, finite state, uniform positivity and bounded price ratios do not suffice.

The surviving resource is **non-effective claim retirement / backward-price stabilization**: finite wtt value dependence does not decide whether a still-open sentinel computation will ever halt. Effective Cauchy convergence of the absolute backward prices of the persistent-savings martingale is sufficient, but is not supplied by the committed P4-S011 data.

No (X\in OH) source separation is proved. The retained comparison remains
[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
]

Records:
- phase4/P4-S037_MATHEMATICS.md
- phase4/P4-S037_CLOSE.md
- phase4/P4-S037_VALIDATION.md

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. The P4-S015–P4-S031 bankroll line remains frozen.

Recommended next session: **P4-S038**, on persistent-frontier claim retirement and effective backward-price stabilization.


## P4-S050 — forbidden-pair hedge and one-hole square exits (2026-10-08)

Records: [mathematics](P4-S050_MATHEMATICS.md), [validation](P4-S050_VALIDATION.md), [close](P4-S050_CLOSE.md).

A single finite positive square refutation excludes a two-bit atom on every epoch. The exact sequential fair hedge pays zero there and 4/3 at each of the other three atoms, with no trapped-epoch assumption. A total computable no-repeat fair-coin-preserving one-hole scan can execute the hedge and consume both raw bits, or timeout transient future t and retain old s.

A combined old/square scan earns factor 2 or 4/3 per positive exit. Infinite executed exits imply X not in OH. Under X in OH each computable combined policy eventually has one persistent old s, no finite old-branch refutation, and no further timely captured square event. The obstruction is algorithm-relative.

The unconditional hedge **resets the old sentinel**. Repeated passive refutations against one trapped old s are not repeated completed pair hedges, and no infinite cross-epoch capture policy for the committed X has been proved.

Retain MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR. Next: P4-S051 on positive multi-square capture across reset. PA-0001 unresolved under inspected evidence; DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED.


## P4-S051 — cross-target reset-free escrow (2026-10-08)

Records: [mathematics](P4-S051_MATHEMATICS.md), [validation](P4-S051_VALIDATION.md), [close](P4-S051_CLOSE.md).

Two positively refuted old/future square atoms with opposite old rows and distinct unread future targets exclude a future-only tuple. A fair sequential 4/3 payoff on the two future bits needs no old-sentinel query. A concrete finite-window escrow scan is everywhere total, no-repeat, fair-coin preserving and globally one-hole safe; same-target opposite rows can instead provide an immediate 2x target-only wager.

By P4-S008, infinite gains at one fixed permanently omitted old sentinel cannot occur on a computably random source. No source-specific infinite cross-epoch capture/turnover is established. X in OH, X not in OH, and R_2=OH remain unresolved. Next P4-S052: certified cash-out and repeated turnover; PA-0001 unresolved; DEF-0020 unchanged.


## P4-S052 — escrow cash-out and success-gated turnover (2026-10-08)

Records: [mathematics](P4-S052_MATHEMATICS.md), [validation](P4-S052_VALIDATION.md), [close](P4-S052_CLOSE.md).

After a cross-row 4/3 escrow, two of the three surviving future tuples positively orient old s, allowing extra fair 2x cash-out (8/3 total). The double nonmatch leaves s unconstrained, allowing only zero-stake old consumption on those witnesses. At a P4-S049 shielded old epoch every finite refutation has wrong future value and the actual escrow outcome is precisely that unoriented double nonmatch.

A total finite-window success-gated escrow controller mandatorily releases temporary futures and consumes old s after a positive exit. Infinite executed profitable turnovers would show X not in OH, but no infinite timely capture on X is established. Always forcing old reset on all transcripts would be a CR-preserving computable permutation. Next P4-S053, branchwise-avoidable effective cross-epoch capture. PA-0001 unresolved, DEF-0020 unchanged, Phase 4 OPEN, Phase 5 CLOSED.


## P4-S053 — adaptive finite-window promptness and the latency barrier (2026-10-08)

Records: [mathematics](P4-S053_MATHEMATICS.md), [validation](P4-S053_VALIDATION.md), [close](P4-S053_CLOSE.md).

A total computable success-gated finite-window escrow controller is globally fair, no-repeat and one-hole safe, with mandatory old/future support discipline and transient future releases. Its finite positive trace requires opposed-old-row refutations at two distinct fresh future targets to be discovered before both deadlines. If this pre-consumption promptness holds at each consecutively reached epoch on X, infinitely many executed profitable turnovers follow and X not in OH. This target condition is NOT established.

The first refutation already permits the P4-S050 local two-bit reset at the same 4/3 factor; escrow does not accelerate this first profitable reset and shielded epochs deny its oriented 8/3 upgrade. Yet changed future epochs prevent global domination. An eventual profitable old turnover on all continuations of a reached prefix is a computably searchable finite bar; universal old-reset across epochs gives a CR-preserving computable isomorphism without any prior uniform clock bound. An explicitly scoped COMPUTABLE ABSTRACT certificate calendar supplies strong eventual wrong-future witnesses only after every release; it is not an actual M or CR counterexample. X in OH and R_2=OH remain unresolved.

Next P4-S054 on source-specific promptness/capture law. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED.


## P4-S054 — actual M-cube witnesses and pure certificate latency (2026-10-08)

Records: [mathematics](P4-S054_MATHEMATICS.md), [validation](P4-S054_VALIDATION.md), [close](P4-S054_CLOSE.md).

The actual Y/M/H/X source forces at least one positive wrong-output certificate in an eight-corner raw cube at every value-closed future block: flipping raw x0,x1 together flips exactly one virtual input q, and the self-avoiding target M^Y(q) then finitely refutes that counterfactual corner. The computable use frontier can be fully exposed without reading old s or future t,u. The first wrong-halt clock sigma is partial computable from this finite transcript and halts at each actual X-derived cube, but no total computable stage bound follows.

A timely cube exclusion licenses an exact fair 8/7 s,t,u old-reset hedge. A globally legal total computable finite-window cube controller succeeds in a reservation precisely when sigma is within its chosen finite tenure. Infinitely many profitable old turnovers would give X not in OH, conditionally. Under hypothetical X in OH every such policy has a final old sentinel and infinitely many value-closed cubes with L<sigma<infinity. The pure timing obstruction is source-specific but does not prove capture or X in OH.

Next P4-S055: test total computable domination of the source-reached partial cube clock under genuinely legal branchwise-avoidable scheduling, or sharpen its necessary obstruction. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED.


## P4-S055 — four-run cube-clock normalization and slow target traces (2026-10-08)

Records: [mathematics](P4-S055_MATHEMATICS.md), [validation](P4-S055_VALIDATION.md), [close](P4-S055_CLOSE.md).

Pairing raw cube corners by flipping t,u together changes only virtual q, which M(q) never queries. Four representative clipped computations thus suffice exactly for the previous eight-corner wrong-halt clock, and a binary halt identifies the wrong mate. On X, the first-certificate clock is finite and bounded above by the true target-runtime T_Y(q). The Y-computable target-runtime cannot have a total computable eventual bound because this would make CR Y truth-table autoreducible. This is NOT a clock bound or non-domination theorem for the smaller sigma.

The legal four-run finite-window controller still consumes old s only after a sound 8/7 hedge and releases t,u at finite timeout. Under hypothetical X in OH every computable q-only clock b has a final sentinel and infinitely many distinct fresh q_k with max(1,b(q_k))<sigma(p_k)<=T_Y(q_k). The policy-dependent latency obstruction does not settle X in OH or R_2=OH. Next P4-S056, test source-specific promptness/thickness for the four-run minimum. PA-0001 unresolved, DEF-0020 unchanged, Phase 4 OPEN, Phase 5 CLOSED.


## P4-S056 — compulsory-old-reset four-run anti-promptness (2026-10-08)

Records: [mathematics](P4-S056_MATHEMATICS.md), [validation](P4-S056_VALIDATION.md), [close](P4-S056_CLOSE.md).

A finite value-closure, four-run, least-unread-s controller consuming s,t,u after BOTH positive 8/7 cube hedge and finite no-certificate timeout is total, no-repeat and a fair-coin-preserving computable homeomorphism. On the committed X in CR, infinite timely positive exits would make a computable output martingale unbounded despite computable-isomorphism preservation; impossible. Consequently for every total computable finite L(e,p) its own compulsory-reset source schedule has only finitely many positive captures, and eventually L(e,p_e)<sigma(p_e)<=T_Y(q_e) at fresh distinct targets. This is source-specific and UNCONDITIONAL on X in OH, but it DOES NOT transfer to success-gated retention of s on timeout.

Fixed-r all-valuation four-run BAR certificates are finitely decidable, yet no globally total renewable fresh verified-BAR provider can cover all forced-reset X epochs. No theorem about frequent timely gains on a success-gated schedule, X in OH, or R_2=OH follows. Freeze prior mathematics, including P4-S008/P4-S052/P4-S053; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED. Next P4-S057 — effective branchwise-avoidable renewal boundary.

## P4-S057 — unbounded success-gated renewal misses (2026-10-08)

Records: [mathematics](P4-S057_MATHEMATICS.md), [validation](P4-S057_VALIDATION.md), [close](P4-S057_CLOSE.md).

The globally legal actual four-run controller retains least-unread s after timeout and mandatorily releases t/u plus a non-s sweep. On CR X, infinite profitable old turnover would require W_e to overrun every total computable prospective epoch-start miss budget infinitely often; only a counterfactual finite-prefix compulsory-reset shadow is an effective isomorphism. Existence of infinite turnover is not established.

## P4-S058 — effective safety renewal obstruction (2026-10-08)

Records: [mathematics](P4-S058_MATHEMATICS.md), [validation](P4-S058_VALIDATION.md), [close](P4-S058_CLOSE.md).

The raw event G_n of n completed WINNING 8/7 old turnovers is uniformly c.e. open, with lambda(G_n)<=(7/8)^n from exact fair preservation and martingale maximality. Every finite raw source prefix has a continuation failing some large renewal target. The effective G-delta infinite-winning class is null; no effectively closed or effective F-sigma subset contains computably random X. This does not prohibit a genuinely Pi^0_2 renewal process on X and does not prove its existence. P4-S008, P4-S052, P4-S053, P4-S056 and P4-S057 remain frozen; X in OH and R_2=OH unresolved. PA-0001 and DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED. Next P4-S059.


## P4-S059 — effective finite-horizon escape (2026-10-08)

Records: [mathematics](P4-S059_MATHEMATICS.md), [validation](P4-S059_VALIDATION.md), [close](P4-S059_CLOSE.md).

For the unchanged actual success-gated four-run controller, C_{n,m} (n genuinely completed winning 8/7 old turnovers within m output bits) is uniformly computably clopen and has fair measure <=(7/8)^n. For every total computable output horizon h(n), computably random X reaches C_{n,h(n)} only finitely often: a rational computable martingale mixes the clopen conditional probabilities with a computable geometric tail. Thus hypothetical infinite winning on X requires its X-computable nth-win time to eventually dominate every computable function. The retained P4-S011 all-trigger scan already forces high degree for the Y/X source, so this is no solution of actual-X renewal. No infinite gains, X in OH, R_2=OH or OH non-invariance proved. P4-S057/P4-S058 frozen, PA-0001/DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED. Next P4-S060.

## P4-S060 — cumulative missed-reservation dominance (2026-10-08)

Records: [mathematics](P4-S060_MATHEMATICS.md), [validation](P4-S060_VALIDATION.md), [close](P4-S060_CLOSE.md).

Every m completed total finite-tenure reservations of unchanged success-gated T_L finish within computably bounded emitted bits b(m), by an effective finite decision tree over all source branches. D_{n,m} of n completed profitable 8/7 turnovers within m reservations is uniformly computably clopen, lambda(D_{n,m})<=(7/8)^n. On CR X, for any total computable reservation horizon h(n), only finitely many D_{n,h(n)} occur. Conditional infinite actual profits force the cumulative REAL zero-stake timeout reservation count S_n=sum_{e<n}W_e(X) eventually to dominate every total computable f. This follows from P4-S059 via b(m) and is an OPERATIONAL corollary, not independent of that theorem or a positive infinite-renewal result. Frozen P4-S057–P4-S059, X in OH and R_2=OH unresolved; PA-0001/DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED. Next P4-S061.

## P4-S061 — local logarithmic renewal-budget overrun spacing (2026-10-08)

Records: [mathematics](P4-S061_MATHEMATICS.md), [validation](P4-S061_VALIDATION.md), [close](P4-S061_CLOSE.md).

Each finite valid epoch-start transcript h admits a clopen k-success test with total prospective reservation budgets B and source mass <=2^(-|h|)(7/8)^k. A computably summable portfolio over all histories proves that, if committed CR X has infinitely many ACTUALLY completed profitable old turnovers, every sufficiently late reached epoch e has an individual completed W_j>=B(j,p_j) among the next K(m_e)=64ceil(log_2(m_e+2)) epochs, for every total computable B. This new local spacing restriction does NOT establish actual infinite renewal or decide X in OH / R_2=OH. Preserve P4-S057–P4-S060, class chain and governance; Phase 4 OPEN, Phase 5 CLOSED. Next P4-S062.

## P4-S062 — sharp near-critical conditional local spacing (2026-10-08)

Records: [mathematics](P4-S062_MATHEMATICS.md), [validation](P4-S062_VALIDATION.md), [close](P4-S062_CLOSE.md).

One finite clopen B-prompt test per emitted epoch-start OUTPUT length gives a weighted martingale whenever sum_m a(m)(7/8)^k(m) converges effectively with a(m)->infinity. The exact inequality 2^5*7^26<8^26 proves K_62(m)=ceil(26ceil(log_2(m+2))/5), replacing P4-S061's 64ceil(log_2(m+2)) with a strictly shorter necessary individual-overrun window, CONDITIONAL on actual infinite profitable old renewals on CR X. Disjoint independent triple tests show only a sharp limit of the stand-alone mass method, not legal infinite T_L renewal. No actual infinite win, X in OH, or R_2=OH established. Phase 4 OPEN, Phase 5 CLOSED; all earlier mathematics preserved. Next P4-S063.

## P4-S063 — frozen old-sentinel reflection and marked finite-renewal kernel (2026-10-08)

**Mathematics checkpoint, NOT a gate or novelty decision.** On the unchanged actual success-gated T_L, flipping the unread old sentinel leaves the entire pre-reset trace, first positive gate and real completed timeout count unchanged. Every finite prospective epoch gate has an EXACT computable rational reachability weight g. At its pre-consumption protected triple, one atom is forbidden zero, one is a fragile old-bit-sensitive 8/7 win, and six are robust old-bit-insensitive 8/7 wins; the marked probabilities are respectively g/8,g/8,3g/4. Fixed marked k-win words have finite clopen mass <=2^-m(1/8)^f(3/4)^r.

CONDITIONAL on infinitely many ACTUAL profitable old resets on committed CR X, for each total computable prospective B, every sufficiently late 2J(m_e)-epoch window (J=ceil(log_2(m+2))) either has W_j>=B(j,p_j) or strictly more than J(m_e) robust exits. The proof uses an effective finite-clopen portfolio bounded by sum_j(j+1)(3/4)^j. One-J all-fragile B-prompt windows are likewise excluded eventually. These MARKED laws do not replace the P4-S062 W-only K_62 law, and no infinitely executed profitable renewal is verified. All exact fresh-block, paired-trace, clipped, pre-consumption, timeout no-old-reset, fair ledger, global one-hole and earlier frozen theorem guards stand. X in OH and R_2=OH unresolved. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED; no Gate-4 or novelty/publication claim. No blocker; next P4-S064.

## P4-S064 — source-reached gate deficits and conditional renewal overlap (2026-10-08)

**Mathematics checkpoint, NOT Gate 4 or novelty.** For the UNCHANGED success-gated four-run controller and any valid finite epoch-start output h, its prospective first gate g_h^B and complementary no-gate deficit delta=1-g are exact computable rationals. The old-bit flip preserves both pre-reset gate and no-gate membership. Its conditional terminal partition is no gate 1-g; forbidden zero g/8; fragile 8/7 win g/8; robust 8/7 win 3g/4.

For each total computable prospective L,B, the RAW clopen event of an actually reached length-m epoch with delta_h<=r(m) AND B completed zero-stake, non-old-reset timeouts has measure <=r(m). If total computable a(m)->infinity and sum_m a(m)r(m) has a computable convergence modulus, a rational fair source martingale excludes infinitely many such events on EVERY CR source. Specifically r(m)=(m+2)^-3 and a(m)=m+2 have effective tail <=1/(N+1). Therefore all sufficiently late ACTUAL B-overruns on committed CR X have computably auditable gate deficit delta_h>(m+2)^-3.

ONLY CONDITIONAL on infinitely many ACTUAL profitable renewals, P4-S062's K_62(m_e) local window contains an actual W_j>=B(j,p_j) together with this positive gate deficit at the SAME source-reached epoch j. The overrun arms of P4-S063's 2J/J marked laws may be tagged similarly. No source-verified infinite winning is supplied; the new finite-gate constraint does not force one future timely certificate. Frozen P4-S008/P4-S052/P4-S053/P4-S056–P4-S063, total globally clipped paired traces, mandatory timeout t/u zero-stake release plus non-s sweep WITHOUT old reset, and zero/7-of-8 fair terminal ledger unchanged. Retain MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR and Y/M/H/X. X in OH and R_2=OH unresolved. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach. No owner/external blocker; next P4-S065.

## P4-S065 — actual-controller persistent-survival frontier and exact transition-hazard dichotomy (2026-10-08)

**Mathematics checkpoint, NOT Gate-4, novelty or real infinite-progress proof.** Retain the unchanged success-gated four-run T_L. For any finite reached epoch start h, the RAW first-n ACTUALLY completed t/u ZERO-stake timeout releases with NON-s sweep and no positive gate or old reset give computably clopen nested A_(h,n), exact conditional rational q_n, and effectively closed permanently unreset F_h with mass 2^-|h| q_infty. The rational frontier-averaged positive-gate hazards c_n=1-q_(n+1)/q_n retain true history dependence, are NOT conditional probabilities along the specific X trajectory, and satisfy q_infty>0 iff sum c_n finite (if all q_n positive).

If a CR source ACTUALLY remains stuck forever at reached h, P4-S058 forces q_infty>0, hence summable global survivor-frontier hazards and a positive possibly noncomputable lower bound delta_h^B=q_B>=q_infty for ALL finite B. Positive F_h contains SOME CR source and old-bit flip preserves/bisects its mass, but does NOT show X is stuck. ONLY CONDITIONALLY on UNVERIFIED q_infty(h)=0 at EVERY X-reached epoch, CR avoidance and correct M^Y positive certificates would force infinitely many actual 8/7 old resets. No L or source-specific verification is supplied. Preserve P4-S008, P4-S052, P4-S053, P4-S056–P4-S064 and ALL prior mathematics; least unread old s, least wholly unread disjoint t/u/v, clipped four paired traces, total prospective L, no reset on timeout, fair no-repeat one-hole fibres and one forbidden zero/seven 8/7 ledger.

Keep MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR, Y/M/H/X, X in OH and R_2=OH unresolved; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged; Gate 3 PASS, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/prior-art/Gate-4/publication/outreach claim. Blocker NONE; next P4-S066.

## P4-S066 — source-path local hazard summability at a permanent CR stall (2026-10-08)

**Mathematics checkpoint, NOT infinite progress, Gate 4 or novelty.** For the UNCHANGED actual success-gated four-run T_L, each finite post-timeout output transcript p has an exact computable rational next-reservation positive-gate hazard gamma(p). A computable fair OUTPUT martingale makes terminal 1/(1-gamma(p)) on a genuine timeout and 0 on a positive gate, and iterates these on consecutive REAL timeout histories. If any computably random raw source remains forever at fixed unread old s, P4-S008's fixed-sentinel computable-permutation completion transports this martingale to an effective-isomorphism output. Boundedness on CR forces the *actual trajectory* sum_n gamma(p_n)<infinity and product_n (1-gamma(p_n))>0. Unlike P4-S065's averaged frontier c_n, this concerns each individual permanent CR stall. An ABSTRACT positive-survival mixture shows averaged c_n summable while a nonrandom risky path has divergent local hazards. A CR survivor exists whenever q_infty>0, hence universal divergence on all stalled paths then fails; it does NOT settle whether committed X belongs to F_h.

NO actual-X source-specific hazard divergence or infinite real gate recurrence has been proved for any total L; no X in OH, X not in OH, R_2=OH or OH non-invariance decision. Keep P4-S008, P4-S052, P4-S053, P4-S056–P4-S065 and all earlier frozen mathematics; Y/M/H/X; MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR; genuine least-unread old/fresh triple, clipped four traces, finite prospective L, positive pre-consumption wrong-output gate, timeouts t/u ZERO stake + non-s sweep WITHOUT old reset, total fair no-repeat one-hole and forbidden-zero/seven-8/7 ledger. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Phase 4 OPEN; Phase 5 CLOSED; Gate 4 NOT reviewed. No novelty/openness/prior-art/publication/outreach claim. No blocker; next P4-S067.



## P4-S067 — exact short-gate leaf capacity and program-clock limitation (2026-10-08)

**Mathematics-only checkpoint; NOT source-X renewal or Gate-4.** For the UNCHANGED actual success-gated four-run T_L, every valid finite next-reservation output prefix p has a computable finite prefix-free set of positive pre-consumption gate-decision leaves G(p), exact gamma(p)=sum 2^-|w|, and computable shortest leaf length d(p), infinity if no gate. P4-S066's fixed-old-sentinel CR timeout martingale implies that on ANY hypothetical permanently stalled CR RAW source, sum_n 2^-d(p_n)<infinity and one source-dependent finite constant C bounds # {n:d(p_n)<=K} by C 2^K simultaneously for all K. Thus bounded-depth sibling positive gate opportunities cannot recur indefinitely; actual-X divergence of this series or of gamma has NOT been shown. Increasing d alone is insufficient because sibling gate-leaf multiplicities can keep gamma large. A separate **padded alternative M program** with constant positive L=K makes all reservations timeout and gamma=0 while preserving extensional autoreduction properties of the same Y: hence eventual target M^Y halt and clipped use alone cannot imply prospective gate hazards. This is NOT a modification or claim about the committed M.

Preserve all P4-S001–P4-S066, the actual committed Y/M/H/X, MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR, exact least-unread old and t/u/v, global clipped four paired M traces, positive ordinary wrong-output/nonbinary pre-consumption certificates, total prospective L, t/u ZERO-stake timeout release plus NON-s sweep WITHOUT old reset, global fair no-repeat one-hole and one forbidden ZERO/seven 8/7 ledger. X in OH and R_2=OH UNRESOLVED. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Phase 4 OPEN; Phase 5 CLOSED; Gate 4 NOT REVIEWED. No novelty/openness/prior-art/publication/outreach claim. No owner/external blocker; next P4-S068.

### P4-S068 — gate-certificate multiplicity via true value closure (2026-10-08)

**COMPLETED / VALIDATED.** The actual P4-S057 four-paired-M controller, not an alternative padded implementation, fixes its c(p) new value-closure queries from a pre-reservation transcript p. For each of their 2^c assignments the finite prospective L and capped four paired traces decidably determine whether an ordinary timely positive gate exists; let a(p) count positive assignments. Since the subsequently emitted simulation fillers lie outside M's clipped oracle-use frontier, their values cannot change that decision. Hence **gamma(p)=a(p)2^{-c(p)}**, equivalent to S067's gate-leaf Kraft sum but with inert filler depth eliminated. By S066, every permanently stalled CR source must have sum_n a(p_n)2^{-c(p_n)}<infinity, and its positive-certificate stages of closure size <=K number at most B2^K for one finite source-dependent B. A multiplicity-weighted divergent series on the **real endogenous X timeout path** would force gates, but neither the fixed M nor eventual M^Y halting supplies that lower bound yet. No infinite real 8/7 old resets, X in OH classification or R_2=OH equality established.

Keep the least-unread old and least wholly unread t/u/v, globally clipped 4 paired M traces, prospective L, only ordinary pre-consumption certificate, zero-stake t/u release + mandatory non-s sweep WITHOUT old reset, global fair no-repeat one-hole fibres and one forbidden ZERO/seven 8/7. Freeze P4-S001–S067; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged; Gate 3 PASS, Phase 4 OPEN, Phase 5 CLOSED, Gate 4 NOT REVIEWED. No novelty/openness/prior-art/publication/outreach claim. Mathematics/validation/close: \`phase4/P4-S068_*.md\`. Next P4-S069; no blocker.


## P4-S069 — actual-source closure-certificate latency deficit and exceptional target locus

Records: P4-S069_MATHEMATICS.md, P4-S069_VALIDATION.md, P4-S069_CLOSE.md. **VALIDATED bounded mathematics, not X recurrence.** In the UNCHANGED four-paired-M success-gated controller, timely finite closure certificates a are exactly eventual certificates b minus finite-but-post-deadline certificates d_L. Thus gamma=(b-d_L)2^-c. At every X timeout the genuine closure assignment is eventually positive but late. On every hypothetical permanent CR-X stall, all sufficiently late small-closure stages have no timely positive sibling assignment at all; any divergent eventual mass must be accompanied by late mass of the same divergent scale. Additionally the original M's everywhere-correct-autoreduction set is null/meagre, also after H, so a generic positive-mass CR survivor is not automatically an original-M autoreduced target. No proved X-specific hazard divergence, actual infinite positive reset, X in OH or R_2=OH. Freeze P4-S001–S068, Y/M/H/X, exact P4-S057 timeout/filler/hedge invariants and PA-0001/DEF-0020/Gate-3/Phase-4 guards. Next P4-S070; no blocker.


## Strategic pivot after P4-S069 — global coded-hole/one-hole comparison (owner direction, NOT a mathematics session)

**ACTIVE NEXT THEOREM DIRECTION**: \`P4_STRATEGIC_PIVOT_AFTER_S069.md\`. After P4-S069's exact eventual-minus-late closure-hazard decomposition and necessary timeout restrictions, no further routine local certificate, clock, gate, renewal or hazard strengthening should be presumed the default. P4-S070 shall test the GLOBAL H-preservation of OH for the explicit three-bit fair-coin homeomorphism, meaning **same-source** raw one-hole vulnerability rather than literal factorization of D o H (already refuted in S033). Proving H preservation would classify committed X notin OH because H(X)=Y notin OH; refuting H preservation with any z in OH and H(z) notin OH would show R_2 proper-subset OH. A parallel longer-term target is R_2=OH^iso, separate from invariance. These implications are conditional, NOT findings. Freeze all P4-S001–S069 and original M/Y/H/X, exact P4-S057 t/u ZERO timeout release and non-s sweep WITHOUT old reset, globally fair no-repeat one-hole fibres, four clipped traces and seven 8/7/one ZERO payoff. No X in OH or R_2=OH decision, no Gate 4, publication, novelty or openness claim. Phase 4 OPEN, Phase 5 CLOSED; next session P4-S070 NOT YET RUN.


## P4-S070 — global block-linear amplification (2026-10-08)

**COMPLETED / VALIDATED; Phase 4 Mathematics only.** Pinned post-S069 strategic-pivot remote main at 32b4fce1400cf5f38d23732bc24d32d71bb213ca; P4-S070 unique. The committed triple matrix A has A^7=I. For every computable block set E, conjugating the selective swap of positions 1 and 2 by H yields the selective two-coordinate XOR shear S_E: (a,b,c)->(a,b xor c,c). By S033 OH invariance under computable signed coordinate permutations, H-preservation is equivalent to preservation under **all** such supported shears; uniform finite Gaussian-elimination words upgrade that to preservation under **every computable blockwise GL(3,F_2) matrix sequence**. The intermediate class OH^{lin3} of robustness after all those blockwise recodings satisfies R_2 subseteq OH^{iso} subseteq OH^{lin3} subseteq OH, and H-pres iff OH^{lin3}=OH. This is a new globally quantified equivalence, NOT a proof that any of these equalities holds. A supported-shear OH counterexample, if found, would prove R_2 proper-subset OH; none is exhibited. If H-pres is proved later, committed X notin OH follows from H(X)=Y notin OH. X in OH, H-pres, R_2=OH, R_2=OH^{iso} unresolved. Case-C divergence and exact one-hole all-transcript restriction remain; S057–S069 hazards not reactivated.

Preserve all previous mathematics, original Y/M/H/X, S057 true t/u ZERO timeout release and mandatory non-s sweep WITHOUT old reset, exact clipped four traces and seven 8/7/one ZERO outcomes. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/prior-art/publication/outreach claim. No owner/external blocker. Next P4-S071 tests supported-shear OH preservation globally. Records: phase4/P4-S070_MATHEMATICS.md, phase4/P4-S070_VALIDATION.md, phase4/P4-S070_CLOSE.md.


## P4-S071 — globally supported shear: same-source exposure-discount theorem (2026-10-08)

**COMPLETED / VALIDATED; mathematics ONLY.** Live main pinned exactly to post-S070 303cbb1ce2d4fc202462901bc0071bcbf7cc8b7a; S071 unique. For every computable supported XOR shear S_E, total virtual one-hole scan T and rational martingale d, there is an explicit same-source TOTAL computable raw no-repeat ONE-hole scan P_E,T and rational martingale e. In a selected block the virtual parity v=b xor c is evaluated with a real zero-stake fresh c read then fresh b; a later request for virtual w=c is silently reconstructed. Every transcript omits at most one raw coordinate, and infinitely many real raw bits are emitted. The exact pointwise capital bound is e_{n(m)} >= d_m exp(-B_m), where B_m sums absolute fractional stakes on the w wagers spoiled by preceding v queries. Consequently z in OH prohibits virtual success with bounded B_m; every supported-shear OH counterexample must have unbounded non-summable spoiled-w exposure satisfying log d_m<=C+B_m. Finite 276,480-case two-block audit supports bookkeeping but is not the proof. This specializes S034's general spoiled-gain mechanism, not a full shear preservation/separation theorem. All S001–S070, Y/M/H/X and exact S057 controller frozen; X in OH, H-pres, R_2=OH and R_2=OH^iso UNRESOLVED. PA-0001/DEF-0020 unchanged, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED, no novelty/prior-art/publication/outreach claims. Blocker NONE; next P4-S072. Records: phase4/P4-S071_MATHEMATICS.md, phase4/P4-S071_VALIDATION.md, phase4/P4-S071_CLOSE.md.


## P4-S072 — online fair settlement of late supported-shear wagers (2026-10-08)

**COMPLETED / VALIDATED CONDITIONAL MATHEMATICS; not universal shear preservation.** Live incoming main matched exactly `3a588efd41939b1f2c193fd877bbdbab61e38bf0`; P4-S072 unique. Retain S071 globally legal same-source raw one-hole evaluator P. For any total computable positive FAIR one-credit-per-real-pivot registrar faithful to the spoiled virtual w wagers, the rational live-copy martingale L and credit martingale F satisfy **L_{n(m)} F_{n(m)} = d_m A_m**, where A_m is the product of pending credit factors. The single rational source martingale h=(L+F)/2 obeys h>=sqrt(d_m A_m). On z in OH virtual success requires pending inventory A_m to approach ZERO along capital peaks; bounded inventory downside forces preservation for this registrar subclass. An all/alternating-shear two-block schedule v_even,u_odd,w_even,u_even,v_odd,w_odd has genuinely late cross-block stake choice, no possible exact pre-c universal stake forecast, but a later fresh u_odd pivot carries a fair 1/2 vs 3/2 credit; 128 assignment sanity audit PASSED. This is NOT general shear preservation, X in OH, R_2=OH or R_2=OH^iso. S034–S036 and S071 earlier results frozen. S057–S069 finite hazard work NOT reopened; retain original Y/M/H/X and exact four clipped traces / prospective deadlines / REAL fillers / t/u ZERO timeout release / mandatory non-s sweep WITHOUT old reset / seven 8/7 + one ZERO. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Blocker NONE; next P4-S073 to test multi-claim/shared-pivot pricing and effective pending inventory. Records: `phase4/P4-S072_MATHEMATICS.md`, `phase4/P4-S072_VALIDATION.md`, `phase4/P4-S072_CLOSE.md`.

## P4-S073 — shared-pivot aggregate joint prices and financed four-block example (2026-10-08)

**COMPLETED / VALIDATED CONDITIONAL MATHEMATICS; NOT unrestricted shear preservation.** Incoming live main matched \`9394fc898b1f152666524d27c1e60d037f658e4a\`; P4-S073 unique. Under a TOTAL pre-bit finite bundle registrar on the unchanged S071 globally legal one-hole raw scan, normalize the joint payoff G_p on one real pivot by fair computable price pi_p=(G_p(0)+G_p(1))/2. Live and normalized bundle martingales obey **L F Pi=d A** at faithful virtual stages; single h_2=(L+F)/2>=sqrt(d A/Pi). Additional total computable positive financing martingale Q gives h_3=(L+F+Q)/3>=(d A Q/Pi)^(1/3). Virtual success on z in OH forces A/Pi, and A Q/Pi for any such Q, arbitrarily small at capital peaks. Individual common-pivot fair factors 1+alpha r and 1+beta r multiply to price 1+alpha beta, so naive unfunded exact product fails unless alpha beta=0. An exhaustive four-block all/even shear example has TWO spoiled w claims using the SAME genuinely later fresh u pivot: a fair prior real c-filler price bet (3/4 or 5/4) and fair normalized u wager give one globally computable raw martingale e>=d/4 at all virtual checkpoints, exact at packet boundaries. 8192 finite assignment checks passed with zero discrepancies. Price premium accumulation and still-open downside remain different obstacles for nonclosed infinite overlaps; no universal registrar/financier. All S001–S072, original Y/M/H/X and exact S057 controller frozen (four paired globally clipped traces, prospective deadlines, real fillers, zero-stake t/u timeout release, mandatory non-s sweep WITHOUT old reset, seven 8/7 and one ZERO). No X in OH, H/shear invariance, R_2=OH, R_2=OH^iso or full homeomorphism result. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED; Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claims. Blocker NONE; next P4-S074 nonclosed rolling aggregate price-escrow question. See \`phase4/P4-S073_MATHEMATICS.md\`, validation and close.


## P4-S076 (2026-10-09)

Validated conditional multistage genuine c-filler Doob financing for three or more spoiled w wagers sharing later fresh a; an explicit globally legal all/even S071 scan has growing computably finite overlapping inventory m_i=i+3 and exact S036 savings settlement mirrors. No general H/shear preservation. Full mathematics, validation, close and runnable audit: P4-S076_MATHEMATICS.md, P4-S076_VALIDATION.md, P4-S076_CLOSE.md, P4-S076_MULTISTAGE_AUDIT.py. Next P4-S077.


## P4-S077 (2026-10-09) — global finite-support OH invariance

P4-S077 (2026-10-09): DIRECT global OH test. A computable fair homeomorphism supported on ANY given finite raw coordinate set F preserves OH. For EVERY virtual global one-hole scan T and computable martingale d, a raw scan preloads F as genuine zero-stake bits, silently resolves only finitely many virtual-F queries, and reads every other virtual query as a fresh raw bit; one positive fair raw e satisfies (d+1)/2 ≤ 2^|F| e at all associated virtual cuts. No effective claim retirement or negative sibling-halt certificate is assumed. Thus finite supported S_E universally preserve OH; supports E,E' differing finitely have equivalent preservation status. Infinite H/shears and X∈OH, R₂=OH, R₂=OH^iso UNRESOLVED, since the 2^|F| bound cannot be passed to growing F. 256 raw assignments/2048 checks zero errors. Original Y/M/H/X and S037/S073–S076 unchanged; S057 untouched. PA-0001/DEF-0020 unchanged, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; no novelty/prior-art/publication claim, blocker NONE. See phase4/P4-S077_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md. Next P4-S078: GLOBAL infinite-support same-source invariance/separation only.

## P4-S078 (2026-10-09) — one fixed infinite shear replaces all computable supports

P4-S078 (2026-10-09): GLOBAL single-shear criterion. Writing S=S_N (a,b,c)->(a,b xor c,c) on EVERY three-bit block and Q_E the computable within-block b/c swap on decidable E, the exact full-Cantor identity S_E=Q_E S Q_E S Q_E proves all computable-support shear preservation iff preservation under the ONE FIXED infinite-support S; by S070 this is equivalent to committed H-preservation and all computable GL(3,2)-block recoding preservation. Independently, the exact committed H factors as S R Q S R Q S R (right-to-left; R swaps a/b globally, Q swaps b/c), giving THREE explicit all-shear witness-transition candidates on the fixed X->Y chain IF X lies in OH. This is only a global algebraic quantifier reduction, NOT S-preservation, not nonpreservation, not X membership and not R2=OH; R2=OH^iso stays separate. All 65536 four-block support/source identities and 168 GL3 generator states passed with zero discrepancies. S037/S073–S077, exact S057 controller and ORIGINAL Y/M/H/X preserved; no finite truncation limit, effective-retirement assumption or new raw compiler. Gate 3 PASS, Gate 4 NOT REVIEWED; Phase 4 OPEN, Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. No novelty, openness, prior-art, publication or outreach claim. Blocker NONE. Next P4-S079: prove or disprove preservation under this fixed S with an actual OH source, or classify committed X directly.

## P4-S079 — direct global unit-column one-hole extraction (2026-10-09)

P4-S079 proved a globally legal restricted-sentinel destroyer: for a target-correct self-avoiding partial predictor on ANY infinite decidable raw-coordinate family, choose least fresh sentinel in that family, fill least-fresh non-sentinel coordinates while running bounded checks, place a genuine prediction wager, and after EVERY successful sentinel query one genuine zero-stake least-unread sweep. On nontriggering branches exactly one sentinel remains unread; on all-trigger branches infinitely many sweeps exhaust ALL raw indices. This yields total fair no-repeat globally one-hole winning scans, without sibling totality or advance wagers. Apply unchanged M^Y via the exact remaining block matrices Y=B_i(z_i) in S078's R,S,Q,R,S,Q,R,S path: B_i has a unit column for EVERY i=1,...,6, so z1,...,z6 are UNCONDITIONALLY in CR minus OH. The first source z0=R(X) has NO unit-column certificate and remains unclassified. If X in OH, the FIRST shear pair (z0,z1) is a real fixed-S failure and R2 proper-subset OH; it is not proved that X in OH. Therefore universal fixed-S preservation, R2=OH, R2=OH^iso and original X membership remain unresolved. Exact 8-input F2 algebra/column independence audit passed; infinite-scan correctness proved separately. Original Y/M/H/X, S001–S078, S037/S057/S073–S078 retained. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; no novelty/open/prior-art/publication/outreach claim. Owner/external blocker NONE. Next P4-S080 targets z0=X up to signed permutation, not further residue tables. Files: phase4/P4-S079_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _UNIT_COLUMN_AUDIT.py.


## P4-S080 — record-level universal reformulation of the z0 question (2026-10-09)

P4-S080 (2026-10-09): RECORD-LEVEL DECISION OF THE PRIMARY TARGET'S FORM. The record fixes Y only existentially (P4-S011 'Fix a computably random sequence Y and an oracle machine M'; P4-S027 'settled existential witness'), so an admissible pair is any CR Y with a self-avoiding clipped wtt autoreduction M (class WAR). Chained-substitution spreading: from any admissible (W,N) with nondecreasing cap U, the greedy computable bijection tau(n)=(i_n, least unused >U(i_n), least unused >U(j_n)) gives V=W o tau in CR with a BLOCK-AVOIDING autoreduction (later in-block queries answered by earlier in-block predictions). Then EVERY computable blockwise recoding of V, including H^{-1}(V), is wtt-autoreducible and outside OH. Hence (Y1,M1)=(V,M_V) satisfies every record hypothesis while H^{-1}(Y1) notin OH: z0=R(X) in OH is NOT derivable from the record, and X notin OH follows from the record exactly when U(H) holds (U(H) is unresolved, so X notin OH is NOT established): H^{-1}(Y') notin OH for every Y' in WAR. Failure of U(H) gives R2 proper-subset OH (and record-independence of X); universal fixed-S preservation implies U(H). GL(3,2) classification: U(K) holds for every K with a unit column (S079 Thm 2 for arbitrary admissible pairs) and U(PKQ)<=>U(K) for permutation matrices; the no-unit-column matrices are exactly the 18-element double coset S3 A S3, closed under inversion, so U(H)<=>U(H^{-1}). Any U(H) counterexample needs, for EVERY autoreduction, infinitely many target in-block two-cycles {1<->2} and {0<->2} (target-only role refutation). Calibration: KLR subset OH; every element of OH minus R2 (any separation, any U(H) refutation) is non-MLR, and apart from KLR subset OH (which yields no known non-MLR member) the programme has no way to show OH membership beyond MLR; OH=MLR would decide R2=OH but give KLR=MLR (QST-0001, SOURCE-STATED OPEN in the catalogue; no new openness claim). Exact finite audit PASS (GL(3,2) coset, tau bijection, toy substitution model, 1408 role cases). U(H), committed X in OH, fixed-S preservation, R2=OH, R2=OH^iso, OH=MLR UNRESOLVED. Original Y/M/H/X unaltered; S001–S079, S037, S057 (not invoked), S070–S079 frozen. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; no novelty/open/prior-art/publication/outreach claim. Owner/external blocker NONE. Next P4-S081: OH-certification gate (non-MLR OH member or exact obstruction), then test against R2/H-images; a proof of U(H) is acceptable. Files: phase4/P4-S080_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _ADMISSIBILITY_AUDIT.py.


## P4-S081 — bounded-hole collapse, van Lambalgen for OH, sharpened certification gate (2026-10-09)

P4-S081 (2026-10-09): STRUCTURAL SHARPENING OF THE OH-CERTIFICATION GATE; GATE NOT PASSED. Step (0): the catalogue (recorded access levels only) contains no statement separating randomness against total computable non-monotonic strategies (or KLR) from MLR; no openness inference. Theorem A (bounded-hole collapse): OH_h=OH for every finite h, i.e. robustness against total computable adaptive no-repeat scans with at most h unread coordinates on every transcript equals one-hole robustness (compactness frontier gives at most h held coordinates at any time; online first-fit colouring gives h one-hole colour scans plus a fill scan that is an effective isomorphism; the log-capital splits). Corollaries: R_k^scan=OH for all k>=2 (the scan multiplicity hierarchy collapses at two); held-bit normal form (on CR sources a one-hole destruction is carried by bets on held coordinates, which are least unread at entry, strictly increasing, one at a time); OH = randomness against total computable non-monotonic strategies of uniformly bounded postponement width, with KLR subset TKLR subset OH; bounded-window predictors of any nonconstant window function exclude OH membership; if Y' in CR is block-predictable then K^{-1}(Y') notin OH for EVERY computable blockwise recoding K, so a U(H) counterexample must be block-unpredictable (in addition to S080's target two-cycles). Theorem B: x(+)y in OH iff x in OH^[y] and y in OH^[x] (uniform relativization; OH analogue of THM-0024); the gate is self-similar under joins. Exact remaining certification obstruction: the sparse late-revealed window construction needs (i) independence of window placement from the random background and (ii) control of blind fill bets on revealed window content under a small c.e. family; not closed. Exact finite audit PASS (9660 factor identities, window scan, join split). OH\MLR nonempty, OH=MLR, U(H), committed X in OH, fixed-S preservation, R2=OH, R2=OH^iso UNRESOLVED. Original Y/M/H/X unaltered; S001-S080, S037, S057 (not invoked), S070-S080 frozen. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; no novelty/open/prior-art/publication/outreach claim. Owner/external blocker NONE. Next P4-S082: certification construction against the exact obstruction, or proof of its unavoidability, or U(H). Files: phase4/P4-S081_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _COLOURING_AUDIT.py.


## P4-S082 — consistency potentials; OH-certification gate passed (2026-10-10)

P4-S082 (2026-10-10): THE OH-CERTIFICATION GATE IS PASSED. This is a Phase-4 mathematical milestone, NOT Gate 4.
* **Theorem 4.4.** OH∖MLR ≠ ∅: some computably random, non-Martin-Löf-random z lies in OH, with z ≤_T ∅‴.
* **Method.** A consistency potential Ψ(σ,m) = 2^{|σ|}E_λ[X_m·1(G⁻¹[G(z)↾m] meets [σ])] works for any total computable fair map G. It is non-increasing in time, it dominates the [σ]-conditional expected capital, and it obeys an exact refinement identity: the average over a new fixed bit equals Ψ plus that coordinate's capital-weighted split weight.
* **Where bounded width enters.** For one-hole scans, split weights below the computable frontier sum to at most Ψ. Guessed runs (Π⁰₂ validity) fix 2i+2 minimal-weight bits at stage i to potential-minimizing values, keeping Φ < 2. The 2^{i+1} runs form a Martin-Löf test, and compactness gives z.
* **S081 §7 obstruction.** Both halves (independence; blind fill bets) are bypassed: there is no random background, and the potential controls the bets.
* **Theorem 5.1.** There is z∉MLR with K(z)∈OH for every computable finite-block recoding K. So H(z)∈OH and z∈OH^{lin3}: potential-built witnesses cannot separate OH from its blockwise images.
* **Theorem 6.1** gives a general cheap-coordinate criterion.
* **Example E1** shows that unbounded width breaks the accounting, so nothing follows about TKLR, KLR or QST-0001.
* **Proposition 6.2 (counting potential for globally ≤2-to-1 maps).** Fixing becomes free and all cost moves to tracking. The exact R₂ gap: transient fresh splits have no computable modulus, and fixings can concentrate untracked double-fibre mass.
* **New landscape.** MLR ⊊ OH. R₂=MLR would give R₂⊊OH, deciding the north star negatively; R₂=OH would require R₂∖MLR≠∅. S080 Corollary 7(b)'s route via OH=MLR is closed.
* **Calibration sources.** SRC-0069 (Kastermans–Lempp preprint; STATEMENT_INSPECTED, §2 proof read) and SRC-0070 (Bienvenu–Hölzl–Kräling–Merkle, CCA 2009; ABSTRACT_INSPECTED), with THM-0077/0078. Their non-adaptive partial notions are incomparable with OH; only the method is adapted. No novelty, priority or openness inference.
* **Unresolved.** R₂=OH, R₂=OH^iso, R₂ vs MLR, OH^iso vs MLR, U(H), X∈OH, fixed-S preservation.
* **Frozen.** Original Y/M/H/X; S001–S081; S037; S057 (not invoked); S070–S081. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty/open/prior-art/publication/outreach claim. Owner/external blocker NONE.

Next: P4-S083, decide R₂ versus MLR. Files: phase4/P4-S082_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _POTENTIAL_AUDIT.py.


## P4-S083 — tail-coded holes; north star decided negatively, R₂ ⊊ OH (2026-10-10)

P4-S083 (2026-10-10): THE NORTH STAR R₂ = OH IS DECIDED NEGATIVELY. This is a Phase-4 mathematical result, NOT Gate 4.
* **Theorem 3.8.** There is a computably random, non-Martin-Löf-random z (≤_T ∅‴) with K(z)∈OH for every computable finite-block recoding K, while D′(z)∉OH. Here D′ is the computable fair homeomorphism D′(z)₀ = z₀, D′(z)ᵢ = zᵢ⊕zᵢ₋₁.
* **The destroyer.** G = F_{T*}∘D′ is a total computable fair-coin-preserving map with all fibres of size ≤ 2, and G(z)∉CR. Hence z∈OH^{blk}∖R₂.
* **Mechanism (tail-coded holes).** A one-hole scan of D′(z) holding v_q knows z↾q exactly and the raw tail up to one global complement, so any single absolute tail value determines v_q.
  * The construction is S082 §5 with candidates taken from pairwise disjoint classes C_{ε↾(i+1)}.
  * T* waits, holding the least unread virtual bit, until a completed guessed run that is consistent below q shows r = q+2m+4 relatively consistent fixes in [q,∞). It then predicts v_q all-in.
  * A wrong prediction forces anti-consistency on all r fixes, and class separation bounds this fooling set W by ⅛ of every [σ*_j].
  * Compactness with L_e = 2+4/w_e selects z∈S∖(O∪W).
  * Raw holes cannot do this: the potential always fixes a coordinate outside a raw hole, but every candidate above q lies inside a tail-coded hole.
* **Corollaries.**
  * R₂ ⊊ OH, R_k ⊊ OH (all k ≥ 2) and R_fin ⊊ OH.
  * OH^iso ⊊ OH^{blk}: OH is not invariant under computable fair homeomorphisms.
  * Raw one-hole normalization (the P4-S032 target) fails.
  * The S082 trichotomy loses case (γ). R₂ versus MLR (α: R₂ = MLR, collapse; β: MLR ⊊ R₂ ⊊ OH) is now the decisive CAND-01 question, and it remains OPEN.
* **Calibration.**
  * SRC-0060 §10 (Rute) read in full: endomorphism and automorphism randomness, the chain (10.1), Question 10.8 (recorded as QST-0002, SOURCE-STATED OPEN, 2016), and footnote 11.
  * SRC-0071 (Petrović, sequence-set strategies; preprint STATEMENT_INSPECTED with proofs read, journal version METADATA_ONLY), THM-0079.
  * SRC-0019 upgraded to STATEMENT_INSPECTED, THM-0081. SRC-0072 ABSTRACT_INSPECTED. THM-0080 and DEF-0066.
  * Proposition 1.1, a programme deduction: robustness under ALL total computable fair maps equals MLR (R_tot = MLR). These maps have unbounded fibres, so bounded fibre size is exactly what separates R₂ from MLR.
  * No novelty, priority or openness inference.
* **Analysis (§7.1).** The exact savings potential β is a fixing-martingale for every total fair map, so the only obstruction to potential constructions is computable choice.
* **Audit.** The exact finite audit passes (tail algebra; toy class-separated runs and T* with the exact fooling equivalence; an exact ≤2 fibre count on 2¹⁴ prefixes; the ⅛ series). The frozen S082 audit was re-run and passes.
* **Unresolved.** R₂ vs MLR, R₂ vs OH^iso, OH^iso vs MLR, R_fin vs R₂, U(H), X∈OH, fixed-S preservation, block-H invariance of OH, TKLR∖MLR, QST-0001.
* **Frozen.** Original Y/M/H/X; S001–S082; S037; S057 (not invoked); S070–S082. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty/open/prior-art/publication/outreach claim. Owner/external blocker NONE.

Next: P4-S084, decide R₂ versus MLR. Files: phase4/P4-S083_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _SEPARATION_AUDIT.py.

## P4-S084 — predictable T* errors and balanced a.e. two-sheet destruction (2026-10-10)

Phase 4 mathematics ONLY. Proved: predictable selection of infinitely many output bits of a computably random sequence yields a computably random prediction-error stream (frequency of mistakes 1/2). Hence a putative R₂ survivor with infinitely many S083 T* resolutions needs an entire CR error stream, not one wrong guess. Anti-consistency cylinders give λ(E_Q)≤2^(−Q−3); an exact restart martingale shows infinitely many T* resolutions occur only on an effectively ML-null input class. Consequently S083's UNCHANGED k=2 fair destroyer G=F_T*∘D′ has exactly two equal-conditional-weight preimages for almost every output, while still destroying an exceptional computably random singleton-fibre z∈OH^blk∖MLR. This refines the existing proof R₂⊊OH, NOT the still-unresolved R₂=MLR versus MLR⊊R₂. Finite sanity audit 8,201 checks, no infinitary computational claim. All original Y/M/H/X, P4-S001–S083, S037/S057, Gate-3 PASS, PA-0001, DEF-0020 frozen; Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No new literature access, novelty, openness or publication assertions. Next P4-S085: bounded-fibre universality or high-entropy R₂ survivor. Records in phase4/P4-S084_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _EXTRACTION_AUDIT.py.

## P4-S085 — exact global width-two universality formulation

P4-S085 (2026-10-10), Phase 4 mathematics ONLY: exact global dyadic-filtration criterion for total computable fair maps with all fibres at most two: for every raw precision n, some effectively searchable output depth c(n) has at most two compatible n-prefixes in every output cell. Theorem 3 gives the exact bounded-width universal-test formulation of R₂=MLR versus MLR⊊R₂, using the correct quantifier order, with the identity filtration automatically enforcing source CR. Posterior n-prefix support/entropy gives a concrete obstruction for specific proposed strategy filtrations, and homeomorphic re-encoding cannot repair fibres of cardinality >2. These are a structural reduction and compilation boundary derived from S003/S007 and S083, NOT a proof of either alternative and NOT a no-go for all width-two universal strategies. S084's CR error-stream and balanced a.e. two-fibre results frozen. No new sources or source-access promotions; original Y/M/H/X, PA-0001, DEF-0020 and all P4-S001–S084 frozen. R₂ vs MLR still UNRESOLVED; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. Next: P4-S086; records phase4/P4-S085_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md.

## P4-S086 — rank-one global universality obstruction (not a gate review)

P4-S086 (2026-10-10), mathematics ONLY: global impossibility for one fair observer and ALL observer families differing only by CR-preserving output postprocessing. Theorem 1 (from catalogued SRC-0015/THM-0007 no randomness from nothing + THM-0035 ML conservation): every y∈CR\MLR has a CR\MLR preimage under each total computable fair F. Thus even all computable output martingales cannot make one width-two filtration universal on CR\MLR. Theorem 3: if F_i=Q_i∘F with every Q_i CR-preserving, a SINGLE CR\MLR source survives ALL F_i; for fair computable homeomorphic Q_i all vulnerability sets are identical. This is a genuine GLOBAL method impossibility, not a no-go for independent pairs, and does not swap ∀F∃x for ∃x∀F or decide R₂ vs MLR. S083/S084/S085 and all Y/M/H/X frozen. SRC-0015 and other literature at recorded evidence levels only. PA-0001/DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; owner/external blocker NONE. Next P4-S087; phase4/P4-S086_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md.

## P4-S087 — dispersed survivor and E₀-breaking frontier (not a gate review)

P4-S087 (2026-10-10), Phase 4 mathematics ONLY: dispersed-survivor theorem. Lemma 2 bounds the S082 split-weight excess, limsup_t(Σγ−Ψ) ≤ 2^|σ|E[(2+B_∞)(f_∞−1)^+], using compactness and the savings transform only (no width modulus; the time is searched). Theorem 4: ONE z∈CR\MLR has G(z)∈CR for EVERY total computable fair ≤2-to-1 G whose double fibres a.s. have density-zero difference sets (DZ₂ ⊇ FD₂, finite differences). The quantifier order is ∃z∀G over an infinite non-rank-one class that includes non-scan maps, phantoms and every one-hole scan of every block recoding. Corollaries 6–7: no family contained in a single computable frame's DZ₂^J is universal for CR\MLR. The graded frame J_f (f(i)=⌊√i⌋) contains every one-hole scan of every K∘D′ʲ(z), so every T∘D′ including S083's T*. Theorem 8: R₂⊊R₂^fd, via a CR non-MLR z surviving all of FD₂ but destroyed by the tail-coded F_T*∘D′∉FD₂. Proposition 9: R₂^fd is closed under homeomorphisms with E₀-preserving inverse, not under D′. Lemma 10: FD₂^J maps have symmetric fibre weights. R₂ versus MLR is NOT decided; it now lies exactly at E₀-breaking (non-dispersible) binary ambiguity in every frame. Frame straightening for finite families is open. Route A race analysis and the Route B counting-potential overcount schema are recorded as analysis only. Finite audit: 8,261 exact checks. Original Y/M/H/X and all P4-S001–S086 results frozen; no source fetched or upgraded. PA-0001/DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; owner/external blocker NONE. Next P4-S088; records phase4/P4-S087_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _DISPERSION_AUDIT.py.

## P4-S088 — asymmetric loci and countable-coset survivor (not a gate review)

P4-S088 (2026-10-10), Phase 4 mathematics ONLY. Theorem A: F₂ admits positive-measure asymmetric double loci. An explicit total computable fair ≤2-to-1 G_asym has, on a closed set A with λ(A)=∏_{k≥2}(1−2^{−k})≈0.5776, exactly two preimages with exact conditional weights ¼, ¾. So by P4-S087 Lemma 10, G_asym∉FD₂^J for every computable frame J, and FD₂ frame straightening fails for a single map. G_asym nevertheless preserves CR (P4-S003 clopen split), and a diluted copy lies in DZ₂, so Lemma 10 is FD-specific. Theorem B: for every computable fair homeomorphism J there is a computable c with the translation-pair map G_c (fibres {x,x⊕c}; a one-hole scan after a linear frame; CR-preserving) outside DZ₂^J. Every finite set of translation pairs straightens linearly. Theorem C: ONE z∈CR\MLR has G(z)∈CR for EVERY G∈CDZ₂, the width-two maps whose double-fibre difference vectors occupy countably many cosets of the density-zero subgroup. CDZ₂ contains DZ₂, FD₂^K and all one-hole scans after every computable affine K, and every T∘D′∘J for affine J, including S083's T*∘D′. It is not co-dispersible in any single frame. The mechanism is frame-free: fresh parities annihilate all dominant difference cosets of the active observers at once. Corollaries: R₂^cdz\MLR≠∅; R₂^cdz⊊R₂^fd; OH^aff\MLR≠∅; OH^aff⊊OH^blk; no family inside one CDZ₂^J is universal; the S084 error-stream requirement is met on all affine frames. Proposition D: for explicit nonlinear causal frames K_mix and K′_mix, one-hole scans have atomless difference cosets. No fresh parity is jointly invariant, and neither natural frame co-disperses the pair. This is a mechanism result only, since the fixed-hold witnesses preserve CR. R₂ versus MLR is NOT decided; it is now located at nonlinear (uncountable-coset) E₀-breaking ambiguity in every frame. R₂⊊R₂^cdz is not proved. Finite audit: 92,724 exact checks; P4-S087 audit still passes. Original Y/M/H/X and all P4-S001–S087 results frozen; no source fetched or upgraded. PA-0001/DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; owner/external blocker NONE. Next P4-S089; records phase4/P4-S088_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _COSET_AUDIT.py.

## P4-S089 — halving survivor theorem, spectral barrier and the rigid three-core (not a gate review)

P4-S089 (2026-10-10), Phase 4 mathematics ONLY. Theorem 1 (halving survivor theorem): every halving-dispersible class of width-two strategies has one common survivor z in CR\MLR. Halving-dispersible means that for every finite subfamily, every clopen state P and every eps there is a balanced clopen split of P (linear or not, fresh or not) separating at most an eps-fraction of the capital-weighted double-fibre pairs inside P, relative to lambda(P) plus that pair mass. The split is found by a single-candidate Sigma^0_1 search because split weights are non-increasing in time. P4-S087 Theorem 4 and P4-S088 Theorem C are instances. Proposition 2: on fresh windows FD2^{K_mix} union FD2^{K'_mix} acts through two order-four groups, control-dependent data translations by the solution space S_W(a) and data-dependent control translations by S'_W(b); the K_mix holds 0 and 1 generate all S(a)-translations. Theorem 3 (spectral barrier): partner involutions of fixed-hold scans after causal frames are tree automorphisms; fresh functions split into signed level operators M_n. A uniform gap ||M_n||_top <= 1-eta forces separation >= eta/2 for fresh exact halvings and >= (3/8)min(eta,eta_0)lambda(P) for every balanced split of an orbit state, violating halving-dispersibility. Lemma 4 (no local frustration): for finitely many causal maps sum_n lambda(F_W(n)) <= |W|, so rigidity of a causal family can only be a global expander phenomenon. Proposition 5.2 (invariance-neutralization dichotomy): absolute neutralization cost is bounded by the initial pair mass, normalized cost is not, and the potential-minimizing rule keeps the side with larger normalized pair weight. Corollary 5.1 (CONDITIONAL on Conjecture R): the two-frame union is not halving-dispersible, via the CR-preserving three-core {U_0,U_1,U'_0}; a mechanism barrier, not a survival barrier. EXPERIMENT only: the three-core's top signed level eigenvalues lie in [0.9737,0.9762] at levels 12-20, the window-only gap is ~0.077, and there are no frustrated cycles of length <= 9 at levels 9-14; the dihedral core {psi_0,psi'_0} is non-rigid (eigenvalues 1 or cos(pi/L) -> 1). Conjecture R is OPEN. R2 versus MLR is NOT decided; (A') is NOT decided; R2 proper-subset R2^cdz is not proved. Finite audit: 143,921 exact checks; the P4-S088 audit still passes. Original Y/M/H/X and all P4-S001-S088 results frozen; no source fetched or upgraded. PA-0001/DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; owner/external blocker NONE. Next P4-S090; records phase4/P4-S089_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _HALVING_AUDIT.py.

## P4-S090 — nonlinear self-reading defeats countable-coset robustness (not a gate review)

P4-S090 (2026-10-10), Phase 4 mathematics ONLY. Authorized alternative (C) proved: Theorem 7 constructs z∈R₂^{cdz}∖MLR and a total computable one-hole scan T such that F_T(K_mix(z))∉CR, with infinitely many correct predictions and a singleton destructive fibre. Corollary 8: R₂⊊R₂^{cdz}, OH^iso⊊OH^aff, and R₂^{cdz} is not K_mix-invariant. The CDZ₂ construction fixes only data parities in disjoint positive-density stage pools; every finite true state leaves the control sequence fair. A uniform conditional separation probability ≥1/4 gives Pr(fewer than r separating constraints)≤2^r(7/8)^L without independent trials. A control-only open stall cover H has relative measure ≤1/32 at every true state, and class separation bounds false readings by 1/8. Compactness uses 4(1−1/8−1/32)=27/8>2. H may be c.e. only relative to validity V; the observer uses bounded simulations of all guesses and no V or H. Witness complexity V′ only. This defeats S089's beacon-mimic obstruction for the selected witness, not for all constructions or all CR∖MLR points.

R₂ versus MLR, Conjecture R, survival of the two-frame union, universal width-two observers and general readable-neutralization impossibility remain unresolved. S089's rigidity barrier stays conditional; fixed-hold maps are not claimed destructive. The S084 whole-error-stream requirement is satisfied for affine observers on z and violated by the nonlinear attacker. Exact S090 audit: 92,802 checks PASS; frozen S088/S089 audits PASS. Written self-review, no Lean or independent-agent review. Original Y/M/H/X, all S001–S089 mathematics, source-access records, PA-0001 and DEF-0020 unchanged. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, external openness, priority, publication or outreach claim. Owner/external blocker NONE. Next P4-S091, targeting full R₂ versus MLR through survival against nonlinear self-readers or a global obstruction. Records: phase4/P4-S090_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _READABILITY_AUDIT.py.
