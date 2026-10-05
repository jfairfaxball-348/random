# P4-S011 — adaptive c.e.-trigger singleton spine: exact k=2 non-conservation

Date: 2026-10-05
Incoming checkpoint: 31cff4e4c442520b19054f19fac75bd8b5c7cc26

## Scope

This is one bounded Phase-4 mathematics session for selected CAND-01, strictly at k=2. P4-S001 through P4-S010 are authority. P4-S005 through P4-S010 are settled and are not reopened.

The only live question is the source-randomness step left by P4-S010: can the adaptive c.e.-trigger least-fresh-sentinel comb have an infinite all-trigger correct-prediction spine containing a computably random source while a computable output martingale succeeds?

Answer: yes.

No use of SRC-0061 is needed.

## Narrow external ingredient

P4-S011 records only the source facts needed for this source-randomness step.

- SRC-0067 / THM-0076: Merkle and Mihailovic prove that there exists a rec-random set that is weak truth-table autoreducible.
- SRC-0068: Mihailovic's thesis states the same result as Theorem 6.9 using the words "computably random", and gives the reduction convention used below: a wtt reduction is a Turing reduction with a computable use bound, while an autoreduction computes the bit at input n without querying oracle coordinate n.

The source theorem is not a finite-fibre map theorem. The conversion below is programme mathematics.

Fix a computably random sequence Y and an oracle machine M witnessing its wtt-autoreducibility. Thus M^Y(n) halts with value Y(n) for every n, and the autoreduction program never queries coordinate n while computing input n. The computable wtt use bound is available but is not needed by the conversion.

The decisive difference from truth-table autoreducibility is that M need not halt on every sibling oracle. That is exactly the branchwise-avoidable trigger behavior isolated by P4-S009 and P4-S010.

## The scan

The scan state at a finite output transcript contains the finite set R of source coordinates already queried and their observed bits.

At the start of an epoch choose the sentinel j to be the least natural number not in R.

During the epoch, simulate M on input j using the already observed source bits as a partial oracle.

At each output stage:

1. If a finite binary halting computation of M(j) is visible using only already observed coordinates, let its output be b, query the fresh sentinel j next, record b as the prediction, then end the epoch and start a new epoch.
2. Otherwise query the least fresh coordinate different from j and continue the same epoch.

If M(j) diverges on the actual source, the scan never waits: it keeps emitting fresh non-sentinel filler queries forever. If an off-target computation halts with a nonbinary value, treat that epoch as permanently nontriggering.

Let F(x) be the infinite sequence of source bits read by this adaptive scan on source x.

The finite simulation can be restarted from the finite transcript at every stage, so the next queried coordinate is a total computable function of the preceding output transcript.

## Lemma 1 — totality and no-repeat

At every finite stage the queried set R is finite.

If a binary halt is visible, the sentinel j is fresh. If not, there is a least fresh non-sentinel coordinate. Hence exactly one fresh source coordinate is queried at every output stage.

Therefore the scan is everywhere total, computable and no-repeat, and F is an everywhere-total computable Cantor self-map.

## Lemma 2 — fair-coin preservation

Fix an output string tau of length m.

The queried coordinates q_0,...,q_{m-1} are determined recursively from the earlier bits of tau and are pairwise distinct. Therefore F^{-1}([tau]) is exactly the event imposing the m independent equations x(q_s)=tau(s) for s<m.

Its fair-coin measure is 2^{-m}. Hence every output cylinder has the correct fair-coin measure and F preserves fair coin.

No stopping probability, conditional sheet mass, or optional projection enters this proof.

## Lemma 3 — global fibre bound at most two

Fix an infinite output y and follow its induced query set Q_y.

Case A: some epoch never triggers. The scan never leaves that epoch. Its filler rule eventually queries every coordinate except its sentinel j. Thus Q_y is the set of all naturals except j. The output fixes every source bit except x(j), so the fibre has exactly two points.

Case B: every epoch triggers. Each completed epoch consumes the current least unqueried coordinate. The successive sentinels are strictly increasing. If some coordinate n were never queried, every least-unqueried sentinel would remain at most n, which is impossible for an infinite strictly increasing sequence. Hence Q_y is all of N and the fibre is a singleton.

Therefore every fibre of F has cardinality at most two.

This is the full global k=2 check, not merely a check on the winning path.

## Lemma 4 — Y is an all-trigger correct-prediction spine

Consider an epoch on source Y with sentinel j.

The target computation M^Y(j) halts, outputs Y(j), and never queries j. It uses only finitely many other source coordinates and finitely many machine steps.

If the epoch has not yet triggered, the filler rule continues querying fresh coordinates other than j. Eventually every oracle answer used by the finite target computation has been revealed. A sufficiently long finite simulation then detects the halt.

Thus every epoch on Y triggers after finitely many fillers, and every prediction is correct.

Because every epoch triggers, Lemma 3 also gives F^{-1}(F(Y))={Y}. The winning source is therefore on a singleton fibre and every source coordinate is eventually queried.

## Lemma 5 — freshness and non-pre-revelation

At each epoch the sentinel is chosen from the currently unqueried coordinates and is never used as filler. It is queried only after the prediction computation has visibly halted.

Coordinates exposed as fillers are permanently marked queried and cannot become future sentinels.

Therefore each genuine wager is placed before its sentinel bit is read, and no already exposed coordinate is later recycled as a fresh betting position. This is exactly the global freshness condition left open by P4-S010.

## Lemma 6 — one computable output martingale succeeds

Define a rational-valued martingale d on output strings, starting with capital 1.

From a finite output transcript, reconstruct the scan state.

- If the next source query is a filler, give both output children the current capital.
- If the next source query is a sentinel with visible prediction b, put all capital on b: the b-child gets twice the current capital and the other child gets zero.

This is a total computable martingale satisfying the fair martingale equation exactly.

Along F(Y), every sentinel prediction is correct. After r completed epochs the capital is 2^r. Hence d succeeds on F(Y), so F(Y) is not computably random.

## Theorem — exact k=2 non-conservation

There exist a computably random source Y, an everywhere-total computable fair-coin-preserving Cantor self-map F with |F^{-1}(z)|<=2 for every z, and a computable martingale d such that d succeeds on F(Y).

Moreover F is induced by an adaptive no-repeat scan and Y lies on a singleton fibre.

Therefore forward computable-randomness preservation already fails at k=2 in the exact CAND-01 class.

No claim is made for k>2.

## Consequence for the repeated-trigger alternative

P4-S010 left open a positive possibility: perhaps infinitely many graph-like trigger constraints automatically combine into one computable source martingale even when one-turnover normalization is noncomputable.

The theorem above rules that out in general. The infinite correct-prediction graph contains the computably random sequence Y. Any computable source martingale forced to succeed on every such all-trigger correct-prediction spine would succeed on Y, contradicting computable randomness.

The hard mechanism is precisely partiality on siblings: on Y the predictor halts and correctly predicts the withheld bit; on a sibling continuation it may fail to halt; the scan remains total by exhausting every coordinate other than the sentinel.

This realizes exactly the branchwise-avoidable turnover isolated by P4-S009.

## Failed route recorded

A prospective positive route was to regard the successive factor-one-half correct-prediction constraints as automatically producing a computably graded null test or one computable source martingale.

That inference is false without a stronger totality condition. The computably random wtt-autoreducible witness belongs to the infinite correct-prediction graph.

This is consistent with the inspected source boundary: SRC-0067 contrasts existence of rec-random wtt-autoreducible sets with the known impossibility of rec-random truth-table-autoreducibility. Uniform total prediction is a stronger regime.

## Preserved boundaries

P4-S011 does not reopen or alter P4-S005 crossing-measure noncomputability, P4-S006 canonical-sheet/Baire-1 analysis, P4-S006/P4-S007 one-hole/coalescence collapse, P4-S008 persistent-hole permutation completion, P4-S009 bounded deferred-wager hedging, or P4-S010 capped optional-projection counterexample.

SRC-0061 is not reused.

PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. The new autoreducibility sources are mathematical ingredients, not exact finite-fibre prior-art matches and not novelty findings.

DEF-0020 is unchanged.

Phase 4 remains OPEN. Gate 4 is not reviewed. Phase 5 remains CLOSED.
