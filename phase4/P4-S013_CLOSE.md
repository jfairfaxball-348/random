# P4-S013 close

Date: 2026-10-06
Session: P4-S013
Incoming checkpoint: 8a5409b662cf548d711485f45d7c35a090f9b917
Scope: selected CAND-01; k=2 sibling-totality / finite-deadline boundary only
Status: **COMPLETED**

## Result

P4-S013 gives a positive preservation theorem for the least-fresh partial-stake subclass and identifies the exact local totality condition used by the proof.

Full totality of the self-avoiding predictor/stake functional on every oracle and every input is sufficient, but stronger than necessary. The weaker condition is reachable-sentinel totality: whenever the least-fresh process on any source reaches an epoch with sentinel j, the functional must halt on that source at j. Equivalently, from every reachable epoch state every compatible sibling continuation eventually triggers.

For each reachable state, continuations that still avoid the sentinel form a computable finitely branching tree. Reachable-sentinel totality says this tree has no infinite path. König compactness therefore makes it finite, and its first empty level is found by a computable search. Thus no separate deadline modulus is needed: uniform eventual triggering and a computably searchable finite deadline are equivalent here.

Every epoch then ends on every source. The least-fresh scan queries every coordinate exactly once, so every fibre is singleton and the map is an everywhere-total computable fair-coin-preserving bijection with computable inverse. It therefore falls into the P4-S001 k=1 effective-isomorphism regime and preserves computable randomness.

The same deadlines also make the P4-S009 finite conditional-expectation hedges concatenate without loss. For any successful output martingale they yield one computable martingale on an exhaustive completion stream; P4-S001 then forces a computable source martingale.

Full oracle-totality is strictly stronger than needed. An explicit self-avoiding stake functional can diverge forever on input 1 while coordinate 1 is always consumed as the first epoch's filler and hence never becomes a sentinel; all actually reachable sentinels still halt and the scan remains exhaustive.

The theorem is not claimed as a necessary characterization of all preserving k=2 least-fresh scans. A branchwise-avoidable epoch may still preserve computable randomness for other reasons. P4-S011 shows only that target-only totality is insufficient and that branchwise avoidance can support exact destruction.

P4-S011's exact k=2 destroyer and P4-S012's structural boundary are preserved. P4-S005 through P4-S012 remain settled. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S013_VALIDATION.md.

Recommended next bounded session: P4-S014, still at k=2 and still inside the least-fresh architecture, testing only whether computable summable avoidance-tail bounds weaker than finite deadlines suffice for a one-martingale transfer, and whether the P4-S011 destroyer necessarily violates such bounds.
