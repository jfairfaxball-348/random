# P4-S010 — k=2 branchwise-avoidable capped optional-projection boundary

Date: 2026-10-05
Session: P4-S010
Incoming checkpoint: ea87997cea224d458a80b72ea82089c31441e325
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **THRESHOLD CAPPING DOES NOT FORCE A COMPUTABLE OPTIONAL PROJECTION: AN EXACT GLOBAL k=2 SCAN HAS A BOUNDED CAPPED DEFERRED-WAGER VALUE WITH NONCOMPUTABLE FIRST PROJECTION. A FRESH ADAPTIVE SINGLETON-SPINE COMB CAN SATISFY THE GLOBAL SCAN GEOMETRY, BUT A COMPUTABLY RANDOM WINNING SOURCE IS NOT PROVED. NO EXACT k=2 DESTROYER OR FULL SCAN-PRESERVATION THEOREM IS OBTAINED.**

## Authority, uniqueness and scope

Live `main` matched the incoming checkpoint exactly before substantive work and again immediately before writes. Repository search returned no committed P4-S010 record. P4-S010 was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. P4-S001 through P4-S009 are preserved exactly. This session stays strictly at k=2.

P4-S005 through P4-S009 are treated as settled. In particular, this session does not revisit the P4-S004/P4-S005 low-weight crossing-measure problem, canonical-sheet mass, one-hole/XOR variants, persistent-hole winning scans, or the P4-S007 coherent width-two skeleton.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard remains historical. DEF-0020 and all catalogue/source convention guards are unchanged. No k>2, novelty/open-status, Gate-4, publication or outreach claim is made.

## Exact branchwise-avoidable question

Let T be a total computable adaptive no-repeat scan such that every infinite transcript omits at most one source coordinate. Let d be a computable nonnegative martingale on the T-output. P4-S008 reduces every possible winning computably random source to a singleton fibre, and P4-S009 reduces every genuinely unbounded sentinel turnover to the following form:

- at a finite T-state tau, a fresh sentinel j is eventually queried on the target continuation;
- there is also an infinite sibling continuation on which T never queries j;
- hence no finite uniform consumption deadline is available from tau.

P4-S010 asks whether stopping/capping d at a fixed output-capital threshold makes the deferred eventual-consumption value computable enough for an exact optional-projection martingale.

It does not.

## Lemma 1 — a computable branchwise-avoidable sentinel can have noncomputable consumption probability inside an exact global k=2 scan

Fix a c.e. noncomputable set K. For e>=0 let

[
t_e = 1^e0^{e+2}.
]

The strings t_e are prefix-free and have lengths 2e+2. Define the c.e. open set

[
U_K = igcup_{ein K}[t_e]
]

and put

[
alpha=lambda(U_K)=sum_{ein K}4^{-(e+1)}.
]

Then alpha is noncomputable.

**Proof of noncomputability.** The base-4 expansion uses only digits 0 and 1. If alpha were computable, membership in K could be decided successively. After the earlier digits are known, the e-th contribution is either 0 or (4^{-(e+1)}), while the entire later tail is at most

[
sum_{i>e}4^{-(i+1)}=rac13,4^{-(e+1)}.
]

A sufficiently accurate approximation to alpha separates these two cases. This contradicts noncomputability of K. ∎

Now define a no-repeat scan T with sentinel coordinate 0.

Before a trigger, T queries source coordinates 1,2,3,... in increasing order. At each finite transcript it also simulates the enumeration of K for sufficiently many steps and checks whether the already seen positive-coordinate bits extend some t_e whose e has appeared. If such a witness is discovered, T queries coordinate 0 next and thereafter enumerates all remaining unqueried positive coordinates in increasing order. If no witness is ever discovered, T queries every positive coordinate and omits 0 forever.

Because delayed enumeration of e is rechecked at all later stages, coordinate 0 is eventually queried exactly when the positive tail (z=x(1)x(2)ldots) lies in U_K.

The scan is everywhere total, computable and no-repeat. Every trigger branch eventually queries every source coordinate and hence has a singleton fibre. Every nontrigger branch queries every coordinate except 0 and hence has a two-point fibre. Therefore the induced map is globally k=2. Fresh-coordinate induction gives fair-coin preservation.

The sentinel is branchwise avoidable at the root because nontrigger continuations exist, while every source with positive tail in U_K consumes it.

## Lemma 2 — cap 2 already leaves a noncomputable eventual-consumption value

Define a computable martingale d on T-transcripts as follows.

- Before T requests coordinate 0, d keeps capital 1.
- At the logical step which queries coordinate 0, d bets all capital on output bit 1:
  [
  d(	au0)=0,qquad d(	au1)=2.
  ]
- Afterwards d freezes.

Thus (0le dle2). In particular, capping at output-capital threshold 2 changes nothing.

Let Z be the eventual-consumption/threshold payoff: if T consumes coordinate 0, take d immediately after that logical step; on a continuation that avoids coordinate 0 forever, take the bounded limiting value 1. Hence, writing b=x(0),

[
Z(x)=
egin{cases}
2b,& zin U_K,\
1,& z
otin U_K.
end{cases}
]

This is exactly the bounded payoff which a prequeried-sentinel completion would have to project onto its own filtration in order to hedge the deferred logical wager without loss.

## Theorem 3 — the capped optional projection need not be computable

Use the fixed-sentinel completion from P4-S008 for j=0: query coordinate 0 first, then follow T while T avoids 0, and if T later requests 0 switch to an exhaustive enumeration of the remaining coordinates. This is a total computable adaptive permutation.

After its first output bit b has revealed x(0), the exact conditional value of Z is

[
M(b)=mathbb E[Zmid x(0)=b]
     =(1-alpha)cdot1+alphacdot 2b
     =1+(2b-1)alpha.
]

Therefore

[
M(0)=1-alpha,qquad M(1)=1+alpha.
]

If the exact optional projection were a computable martingale, both first-level values would be computable reals, and then

[
alpha=rac{M(1)-M(0)}2
]

would be computable, contradicting Lemma 1.

So **boundedness and a fixed output-capital cap do not make the branchwise-avoidable deferred-wager value uniformly computable**. The obstruction appears already at one turnover, with threshold 2, a bounded d, an everywhere-total fair-coin-preserving global k=2 scan, and a genuine singleton consume branch.

This is a new scan-level optional-projection obstruction. It does not revisit or alter the settled P4-S004/P4-S005 crossing-measure result.

## Corollary 4 — finite truncations converge with no computable modulus in the example

Let alpha_s be the computable rational measure of those coded cylinders whose K-enumeration has been seen by stage s. Then alpha_s increases to alpha. The finite-horizon conditional values are

[
M_s(0)=1-alpha_s,qquad M_s(1)=1+alpha_s.
]

Each M_s is computable, but there is no computable uniform convergence modulus: such a modulus would compute alpha.

Thus threshold capping converts the unbounded-tail problem into a bounded martingale-convergence problem, but it does not supply the missing effective convergence rate.

P4-S009's finite conditional-expectation hedge is recovered exactly when the avoidance tree is finite. The present example shows why merely adding a capital cap does not extend that proof to an infinite avoidance tree.

## What this does and does not rule out

It rules out the proposed **exact capped optional-projection route** under the bare global k=2 scan hypotheses. There is no uniform procedure which takes the branchwise-avoidable turnover data and computes the exact bounded projected capital, because one valid instance already has a noncomputable first projected value.

It does **not** prove that every computable martingale transfer must calculate this exact conditional expectation, and therefore is not a full scan-preservation impossibility theorem.

It also does not itself give a destroyer: d is bounded by 2 and does not succeed.

## Exact adaptive singleton-spine witness attempt

After the negative projection result, an exact scan architecture was tested that removes the naive computable-control defect of the P4-S009 comb.

At epoch r let j_r be the least source coordinate not yet queried. Keep j_r as the current sentinel. Query other still-unqueried coordinates in increasing order and feed their bits to a computable c.e. trigger/prediction procedure. There are two possibilities.

1. The procedure eventually outputs a prediction b_r. Then query j_r next. An output martingale may wager on (x(j_r)=b_r), after which the next epoch starts with the new least unqueried coordinate.
2. The procedure never outputs. Then the scan remains in this epoch and continues enumerating every source coordinate other than j_r forever.

### Global checks that do succeed

**Totality and no-repeat.** At every output stage a fresh coordinate is computably selected. A nontrigger epoch still produces infinitely many output bits by enumerating all coordinates except its sentinel.

**Fair coin.** Every output bit is read from a fresh source coordinate selected from the previous transcript, so finite output cylinders have the fair-coin probabilities by induction.

**Global k=2 fibres.** If some epoch never triggers, exactly its current sentinel is omitted forever and all other coordinates are eventually queried, giving a two-point fibre. If every epoch triggers, each sentinel is eventually consumed. Since j_r is always the least unqueried coordinate and strictly moves right, every fixed source coordinate is eventually queried; such a path has a singleton fibre.

**Freshness and non-pre-revelation.** The current sentinel is not queried before the martingale's genuine wager on it. Future sentinels are not predesignated: after a turnover the next sentinel is chosen only from coordinates still unqueried at that moment. Hence a coordinate already exposed as filler is never later recycled as a genuine sentinel bet.

**Output success conditional on a winning spine.** If every epoch triggers and the sentinel prediction is correct at infinitely many full-wager epochs (in particular, if it is correct at every epoch), the corresponding computable output martingale is unbounded.

This architecture therefore meets the query-set, fair-coin, fibre, freshness and non-pre-revelation geometry that the earlier naive comb did not.

### The remaining failed check — a computably random winning source

No proof is obtained that the all-trigger winning spine contains a computably random source.

If the trigger/prediction decisions are replaced by computably bounded finite clopen control blocks, their winning branch probabilities are computably normalizable and the construction collapses back to the bounded regime already handled by P4-S009: a source martingale can bet on those finite favorable events, so repeatedly forcing full-wager wins does not provide a computably random witness.

Using genuinely branchwise-avoidable c.e. trigger domains with noncomputable conditional masses removes that immediate normalization, exactly as Theorem 3 demonstrates. But noncomputability of the normalization is only an obstruction to a transfer proof; it is not a proof that a computably random sequence exists on the infinite correct-prediction spine.

No construction or theorem in the committed record supplies that missing source-randomness fact. SRC-0061 is therefore not reused.

## Successful and failed mechanisms

Successful in P4-S010:

1. An exact global k=2 no-repeat scan whose branchwise sentinel-consumption probability is a noncomputable left-c.e. real.
2. A bounded computable output martingale with cap 2 for which the eventual-consumption/threshold payoff has noncomputable first optional-projection values.
3. A proof that finite-horizon projected values can converge without any computable modulus even after threshold capping.
4. A fresh adaptive singleton-spine comb whose totality, fair-coin, global fibre, singleton-spine, freshness and non-pre-revelation checks are all explicit.

Failed or incomplete:

1. Computing the exact capped optional projection in the branchwise-avoidable case.
2. Replacing exact projection by some different one-martingale transfer with no success-rate/query-time assumption.
3. Proving that the adaptive all-trigger correct-prediction spine contains a computably random source.
4. Constructing an exact total computable fair-coin-preserving global k=2 scan with a computably random source and non-computably-random image.
5. Proving full preservation for global k=2 scans or for general k=2 maps.

## Proof dependencies and guards

The new mathematics uses only the P4-S008/P4-S009 scan setup, elementary prefix-free coding of a c.e. noncomputable set, fair-coin independence of fresh queried coordinates, bounded martingale conditional expectation, and exact fibre counting for no-repeat scans. No new literature theorem is imported.

SRC-0061 / THM-0072 is not reused as a witness.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001 through P4-S009 are unchanged exactly.
- General k=2 scan preservation and general k=2 forward computable-randomness preservation/failure remain unresolved.
- No result is claimed for k>2.
- DEF-0020 and all catalogue/source convention records are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
