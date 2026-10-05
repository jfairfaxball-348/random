# P4-S010 close

Date: 2026-10-05
Session: P4-S010
Incoming checkpoint: ea87997cea224d458a80b72ea82089c31441e325
Scope: selected CAND-01; k=2 branchwise-avoidable capped optional-projection boundary only
Status: **COMPLETED**

## Result

P4-S010 answers the threshold-capping subquestion negatively.

Using a prefix-free base-4 coding of a c.e. noncomputable set, the session constructs an everywhere-total computable adaptive no-repeat scan which queries positive coordinates until a c.e.-open trigger occurs, then consumes sentinel coordinate 0. Trigger branches are singleton fibres; nontrigger branches omit exactly coordinate 0. The map is therefore fair-coin preserving and globally k=2.

A computable output martingale stays at capital 1 until the logical sentinel step, then bets all on bit 1 and freezes. It is bounded by 2, so threshold-capping at 2 changes nothing. If alpha is the noncomputable trigger probability, the eventual-consumption/threshold payoff has exact conditional values (1-alpha) and (1+alpha) immediately after a fixed-sentinel completion prequeries bit 0. Hence the exact optional projection is not computable. Finite-horizon projections are computable but have no computable convergence modulus.

This blocks the exact capped optional-projection route, not every possible computable martingale transfer.

The session also tests a stronger adaptive singleton-spine comb. At each epoch the least unqueried coordinate is withheld as the current sentinel while other fresh coordinates drive a c.e. trigger/prediction procedure. If the trigger never occurs, every coordinate except the sentinel is enumerated; if it occurs, the sentinel is queried for the genuine wager and the next sentinel is chosen only afterwards from still-unqueried coordinates. This architecture is total, no-repeat, fair-coin preserving, globally k=2, singleton on the all-trigger spine, and satisfies the intended freshness/non-pre-revelation geometry.

The remaining unproved check is decisive: no proof is obtained that an all-trigger winning spine contains a computably random source. Finite computably normalized control blocks revert to the bounded regime and are source-martingale exploitable; genuinely c.e. noncomputable trigger masses avoid that immediate normalization but do not themselves supply a computably random witness.

No exact k=2 destroyer and no full global-k=2 scan preservation theorem is established. SRC-0061 is not reused.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001 through P4-S009 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S010_VALIDATION.md.

Next: P4-S011, still bounded to k=2, focused only on the adaptive c.e.-trigger singleton-spine architecture: determine whether its infinite correct-prediction spine can contain a computably random source, or whether the repeated graph-like trigger structure yields one computable source martingale despite noncomputable one-turnover normalization.
