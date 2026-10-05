# P4-S009 — k=2 singleton moving-hole deferred-wager boundary

Date: 2026-10-05
Session: P4-S009
Incoming checkpoint: 90f4441e1edde8f1c3a4e85652c2514e18cb77ac
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **UNIFORMLY UNAVOIDABLE SENTINELS HAVE COMPUTABLY SEARCHABLE DEADLINES AND THEIR DEFERRED WAGERS CAN BE HEDGED EXACTLY; THE ONLY UNBOUNDED SINGLETON TURNOVERS ARE CONSUMED ON THE TARGET BUT OMITTABLE ON A SIBLING CONTINUATION. THRESHOLD/SAVINGS RESTART DOES NOT REMOVE THAT UNBOUNDED STOPPING VALUE WITHOUT EXTRA RATE INFORMATION; NO EXACT k=2 DESTROYER OR FULL SCAN-PRESERVATION THEOREM IS OBTAINED.**

## Authority, uniqueness and scope

Live `main` matched the incoming checkpoint exactly before substantive work and again after the user continuation. The incoming `phase4` directory contained P4-S001 through P4-S008 only, and the expected P4-S009 work/close/validation files did not exist. P4-S009 was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. P4-S001 through P4-S008 are preserved exactly. This session stays strictly at k=2.

P4-S005 through P4-S008 are treated as settled. In particular, this session does not revisit crossing-measure computability, canonical-sheet mass, one-hole/XOR variants, the persistent-hole/double-fibre winning route, or the P4-S007 coherent width-two skeleton.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard remains historical. DEF-0020 and all catalogue/source convention guards are unchanged. No k>2, novelty/open-status, Gate-4, publication or outreach claim is made.

## Exact singleton moving-hole setting

Let T be a total computable adaptive no-repeat scan such that every infinite transcript omits at most one source coordinate. Let d be a nonnegative computable martingale on the T-output.

P4-S008 proves that if x is computably random and d succeeds on F_T(x), then T must query every source coordinate on x. Thus the winning transcript y=F_T(x), if it exists, has singleton fibre, while the unique low-coordinate hole visible at the P4-S007 sampling stages moves outward and is eventually consumed.

For a finite T-transcript tau, let Q(tau) be the already queried source coordinates and let q(tau) be T's next query.

## Lemma 1 — the sentinel-avoidance tree gives an exact bounded/unbounded dichotomy

Fix a finite transcript tau and a fresh coordinate j not in Q(tau). Define A_{tau,j} to be the binary tree of finite continuations u such that, while T is simulated from tau through the logical output bits u, it never requests j.

The tree A_{tau,j} is computable and prefix closed.

Exactly one of the following holds.

1. **Uniformly unavoidable.** There is an H such that no string of length H belongs to A_{tau,j}. Then every continuation of tau makes T request j within H logical T-steps. Moreover such an H is computably searchable from tau and j: test H=0,1,2,... and inspect the finitely many length-H continuations.
2. **Branchwise avoidable.** A_{tau,j} has nodes at every height. By König's lemma it has an infinite path, hence there is an infinite continuation of tau on which T never queries j.

Thus a fresh sentinel can have no computable consumption deadline on the basis of the current transcript only if there is a genuine sibling continuation on which that sentinel is omitted forever.

Under the global k=2 scan hypothesis, every such avoiding continuation queries every source coordinate other than j.

### Consequence for a singleton target

Suppose the actual singleton target continuation eventually consumes j but the uniform-bound search for j never halts. Then the target is necessarily paired, at that finite state, with an alternative continuation that permanently omits j. The target itself is still singleton; the alternative branch is used only to certify why no finite deadline is forced.

This localizes the P4-S008 obstruction. The hard case is not merely “the query time is large.” It is “the target consumes a coordinate whose nonconsumption remains possible on another continuation for arbitrarily long.”

## Lemma 2 — a computably bounded deferred sentinel wager can be hedged exactly

Fix tau, a fresh sentinel j, and a verified bound H such that every continuation requests j within H logical T-steps.

Consider the finite completion block that:

1. queries j first and records its fair bit b;
2. then follows T from tau;
3. whenever T asks a fresh coordinate different from j, queries it and appends its bit to the simulated T transcript;
4. when T asks j, appends the already-known bit b to the simulated T transcript without requesting a new source bit, and ends the block.

At most H logical T-steps occur, so this block depends on only finitely many fresh fair source bits.

Let K be the terminal value of d immediately after the simulated T-step that consumes j. K is a computable function on this finite product space. Its average is exactly d(tau).

**Reason.** In logical T-order the bits seen from tau through the j-query are fresh fair bits and the j-query occurs at a bounded stopping time. Equivalently, expanding the finite tree directly and averaging terminal d-values gives d(tau) by repeated use of the martingale equation.

Therefore the conditional-expectation process
M(s)=E[K | the completion-block prefix s]
is a computable fair martingale on the completion bits, starts at d(tau), and reaches exactly K on every terminal branch.

So **early disclosure of the sentinel itself causes no unavoidable factor-two loss when the sentinel has a computably verified finite lifetime**. The future d-wager on that bit can be prepaid exactly by a finite hedge.

This is stronger than the crude P4-S008 “copy then freeze” comparison, but only in the bounded-lifetime regime.

## Corollary 3 — infinitely many bounded turnovers are not intrinsically a savings problem

If a computable dynamic-sentinel completion has a sequence of turnover blocks for which every sentinel lifetime is accompanied by a computably verified finite bound, then the finite hedges of Lemma 2 can be concatenated: at the end of each block the hedge capital is exactly the current d-capital, so the next block starts with no multiplicative loss.

Consequently savings/restart is unnecessary in that regime. If the resulting completion scan is globally exhaustive, it is a computable adaptive permutation and P4-S001 applies.

The P4-S008 singleton problem survives because no such verified lifetime sequence is forced. At an unbounded turnover Lemma 1 says there is an avoiding sibling continuation, so the finite conditional-expectation construction has no certified terminal depth.

## Lemma 4 — finite-horizon portfolios do not give a rate-free infinite-turnover bound

A natural repair is to split capital among finite horizon guesses. At one turnover let a_H be the capital fraction assigned to a hedge that is exact provided the sentinel is consumed by horizon H, with sum_H a_H <= 1. If the actual delay is L, the total fraction carried by guesses capable of surviving that turnover is at most

p(L)=sum_{H>=L} a_H.

For every such summable allocation, p(L) tends to 0 as L tends to infinity.

Hence there is no positive retention factor uniform in the finite delay. Across infinitely many turnovers a bookkeeping proof based only on these finite-horizon portfolios accumulates factors p_r(L_r). Because each p_r(L) can be made arbitrarily small by a sufficiently long still-finite delay, unboundedness of d alone supplies no lower bound forcing

d-capital times product_r p_r(L_r)

to be unbounded.

This remains true if the horizon allocation at turnover r is chosen computably from the previous transcript and previously observed d-capital: once that allocation is fixed, the unresolved future delay can lie arbitrarily far out on an avoiding branch.

This is a limitation of the proposed **finite-horizon split / savings accounting**, not a theorem that every possible computable martingale transfer is impossible.

## Threshold-triggered savings/restart does not remove the stopping value

The same point appears in the “skip one deferred wager” implementation. If the completion simply copies d while the sentinel is unconsumed and does not realize the eventual logical d-wager on the already-seen sentinel bit, one turnover can lose a factor as large as two relative to d. Repeating this at r turnovers gives only the crude comparison 2^{-r}d.

Thresholds can compensate for that loss only if the number/timing of turnovers is effectively related to new capital growth. P4-S008 supplies no such relation. A singleton scan may consume arbitrarily many sentinels while d remains below the next chosen threshold and only later attain a new peak.

A stronger hedge would compute the conditional value of the deferred wager at its eventual consumption. Lemma 2 computes that value for a bounded stopping tree. In the hard case the stopping tree has an infinite avoiding branch, so finite truncations have no forced computable convergence modulus. Savings changes where capital is stored; it does not compute this missing tail value.

Thus P4-S009 does not obtain one computable martingale from threshold-triggered or dynamic-sentinel restart under the bare P4-S008 hypotheses.

## Exact witness attempt — a singleton-spine comb

The global fibre constraint itself does not forbid infinitely many “avoidable but consumed” holes.

A simple computable comb illustrates the geometry. Partition coordinates into computable pairs (c_r,j_r). At epoch r query c_r.

- On one control outcome, permanently omit j_r and enumerate every other remaining coordinate.
- On the other outcome, query j_r and continue to epoch r+1.

Every transcript omits at most one coordinate, so the induced scan map is globally k=2 and fair-coin preserving. The continuation that always takes the second outcome is a singleton-fibre spine and consumes infinitely many successive holes.

However this simple comb is **not** a randomness-destruction witness. Its singleton spine fixes one outcome on the computable control coordinates c_r, so that source is not computably random. Making the controls genuinely adaptive enough to admit a computably random spine returns to the unresolved nonmonotonic-freshness problem: the control/betting coordinates must not be pre-revealed by the global completion, and the full fair-coin/fibre checks must hold on every side branch.

No such adaptive comb is completed here. SRC-0061 is not reused, because the committed theorem supplies no proof that its decisive betting coordinates can serve as this singleton spine while satisfying the global k=2 and non-pre-revelation requirements.

## What P4-S009 adds

Successful:

1. A computable avoidance-tree dichotomy for every proposed sentinel.
2. A proof that uniform eventual consumption automatically yields a computably searchable finite deadline.
3. An exact finite conditional-expectation hedge for a bounded deferred sentinel wager, eliminating the apparent factor-two turnover loss in that regime.
4. A reduction of every genuinely unbounded singleton turnover to an “avoidable on a sibling branch, consumed on the target” configuration.
5. A precise reason finite-horizon capital splitting and savings/restart do not yield a rate-free infinite-turnover proof from unbounded d-capital alone.
6. An exact globally k=2/fair-coin singleton-spine comb showing that the query-set geometry is combinatorially feasible, while also exposing why the naive computable-control spine is not a computably random witness.

Failed or incomplete:

1. Computing the unbounded deferred-wager value when the sentinel is avoidable on a sibling continuation.
2. Proving that source computable randomness itself supplies the missing relation between sentinel delay and output-capital growth.
3. Turning threshold-triggered/savings restart into one computable martingale across infinitely many unbounded turnovers.
4. Upgrading the singleton-spine comb to a computably random source with a non-computably-random output.
5. Reusing SRC-0061 with full global freshness, fibre and non-pre-revelation checks.
6. Proving full preservation for global k=2 scans or general k=2 maps.

## Proof dependencies and guards

The new mathematics uses only the P4-S008 no-repeat scan model, elementary computable finitely-branching-tree compactness, finite conditional expectation, and the computable-martingale equation. P4-S001 is used only for the already-settled fact that a globally exhaustive computable adaptive scan is in the effective-isomorphism regime.

No new literature theorem is imported. SRC-0061 / THM-0072 is mentioned only as the previously recorded unrestricted total non-conservation mechanism and is not promoted to a finite-fibre witness.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001 through P4-S008 are unchanged exactly.
- General k=2 forward computable-randomness preservation/failure remains unresolved.
- No result is claimed for k>2.
- DEF-0020 and all catalogue/source convention records are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
