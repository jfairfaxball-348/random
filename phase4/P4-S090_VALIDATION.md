# P4-S090 validation — nonlinear readable separation

Date: 2026-10-10. Phase 4 Mathematics only. Review mode: structured adversarial self-review; no second agent, Lean, or external review is claimed.

## Entry and reconciliation

* Git ls-remote and an independent GitHub API read agreed on 560f8a1e16a69aaf98a6b8328bfc893b09398d30.
* This is the S089 atomic close, parent 0009e00dff9d75b70539e513e544f4b89b8040f4, reconciling S089's self-identifying outgoing checkpoint.
* No S090 file, executed-session entry, or session branch existed. A log mention was S089's forward handoff. Live open pull requests: none.
* No tracked GitHub workflow files; hosted runs for the incoming SHA: zero. The connector rejected the workflow-collection URL; no inference is drawn from that rejected query. No hosted CI success is claimed.
* CAND-01, Gate-3 PASS, both pivots, historical summaries and the detailed proof dependencies listed in the mathematics record were reviewed.

## Proof review

**Lemma 1 — PASS.** The pool is a positive-density arithmetic progression of raw odd coordinates. H group endpoints are O(H), so a density-zero error hits o(H) groups. Arbitrary sparse classes would not justify this. Dominant cosets are an existence device, not algorithmic advice.

**Lemma 2 — PASS.** Every completed length-m run fixes m(m+1) independent data parities, even on invalid guesses. The ML-test bound is therefore unconditional. True-run halting follows from Lemma 1 and the S088 potential argument. Incomparable guesses use disjoint stage pools after their first disagreement; shared constraints agree in support and value. True finite states impose no control constraints. This is a relative-measure calculation, not an assumption about independence of the finally selected infinite point.

**Lemma 3 — PASS.** Given any earlier controls the incoming state is a mixture of 01,10,11. At the last support position p, delta at p-1 has probability at least 1/2 of being 1; then the fresh control at p makes the parity fair. Prior separation indicators are measurable before the next support. The tower property proves E[2^(-S_L)] <= (7/8)^L without independent trials. A draft sentence claiming that the imposed gap was necessary was removed; the proof uses it only as a sufficient condition.

**Stall cover — PASS.** At most q+1 disjoint supports have minimum at most q. The rational search for m_q terminates. H_q is clopen and control-only once its finite true guess is fixed, with measure at most 2^(-q-6). H has relative measure at most 1/32 under every true state. It is c.e. relative to V, not claimed effectively open without V. Only compactness/witness selection uses H; the observer and ML test never call V or H.

**Lemma 4 — PASS.** Bounded universal-machine simulation ensures total next-query computation even if invalid or self-referential guessed runs diverge. Holds are odd virtual positions. Any intervening control is genuinely read at zero stake. On every transcript there are no repeated queries; either all coordinates are read, or only the last hold remains. Predictions are computed before the held bit. The fair-child identity and the global fibre bound are exact.

**Lemma 5 — PASS.** H covers failure at every possible hold q. If a hold persisted, the true length-m_q run would eventually finish its bounded simulation and have all support below the frontier. Its separating equations all imply the actual held bit, forcing resolution. No computable uniform deadline is claimed.

**Lemma 6 — PASS.** Which equations separate depends only on controls and a fixed completed run. The winning run may depend on data, but the proof takes a union over all runs, so it never conditions on winning that race. Under a true state and fixed controls, a shared selected equation makes anti-consistency impossible; otherwise all selected supports are disjoint from all true supports and simultaneous failure has probability exactly 2^(-r). Sum over q and 2^m guesses gives 1/8. W is effectively open without V.

**Theorem 7 — PASS.** The finite open subcover and savings drop bound give weighted capital greater than 4 on a region of relative measure at least 27/32, hence Phi > 27/8 > 2. The relative H/W bounds remain valid at later true stages. Every valid CDZ2 martingale, including identity observers, is bounded at the selected point. The nonlinear observer resolves infinitely and correctly there. Its destructive fibre is singleton. Witness complexity is V-prime; no arithmetical bound on V is asserted.

**Corollary 8 and scope — PASS.** The same point is in R2^cdz, hence OH^aff, and outside OH^iso because K_mix(z) is not in OH. Both strict inclusions follow. G_* is outside CDZ2 by the definition of R2^cdz and the demonstrated destruction. No equality between R2^cdz and OH^aff, universal observer, or impossibility for every guessed-run construction follows. Conjecture R remains unresolved and S089's barrier remains conditional.

## Executed checks

* python3 phase4/P4-S090_READABILITY_AUDIT.py: **92,802 exact checks PASS**. Inverse/held-bit algebra; all tested nonzero incoming states and future parities; repeated conditional bounds; control-dependent shared/disjoint selection; exact budgets.
* python3 phase4/P4-S088_COSET_AUDIT.py: **92,724 checks PASS**.
* python3 phase4/P4-S089_HALVING_AUDIT.py: **143,921 checks PASS**, including reproduction of its already labelled small-level experiment. No new spectral experiment or promotion.

These are finite verification aids. The separation of infinite randomness classes rests on the written proof.

## Record and guard checks

Closeout parses repository JSON, verifies exact S091 prompt identity with the close record, reconciles current state pointers, and checks the diff for whitespace and changes to frozen mathematics/source records. Previously stale scalar pointers inside phase4_mathematics (S084/S085) are synchronized to S090/S091; historical nested findings are preserved.

Source access, PA-0001, DEF-0020, original Y/M/H/X and all prior session mathematics remain unchanged. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. Active owner/external blocker: none. No novelty, external openness, priority, publication or outreach claim.

The single session commit is pushed and non-force fast-forwarded to main, followed by independent remote-SHA verification. A commit cannot embed its own resulting hash; the final report supplies the independently observed hash.
