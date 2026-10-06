# P4-S012 close

Date: 2026-10-06
Session: P4-S012
Incoming checkpoint: 491c671be615abd9bef9b3e9239ccdb74b76b22b
Scope: selected CAND-01; k=2 partial-predictor / scan-converse boundary only
Status: **COMPLETED**

## Result

P4-S012 isolates the exact information used by the P4-S011 least-fresh singleton-spine conversion.

The wtt use bound is not needed. A still weaker sentinel-local condition suffices: at each least-fresh sentinel generated on the target, a finite self-avoiding partial computation becomes visible and correctly predicts that sentinel. Predictions are not needed on filler coordinates, and no sibling-oracle totality is required. More generally, bit predictions can be replaced by rational self-avoiding fractional stakes; if every target epoch triggers and those stakes have unbounded capital, the same total no-repeat least-fresh scan is fair-coin preserving, globally k=2, singleton on the target and defeated by the corresponding computable output martingale.

The converse is exact at this stake level. For any global-k=2 no-repeat scan winning on a computably random source, P4-S008 first forces the source transcript to be singleton and to query every coordinate. For each coordinate j, simulate the scan using the oracle away from j until it is about to query j, then output the signed stake encoded by the winning rational martingale. This partial functional never queries j, halts on the winning source for every j, and in the original scan order reproduces the martingale capital exactly.

The stronger all-correct bit-autoreduction converse is not obtained. A succeeding martingale may make infinitely many wrong favoured-bit wagers; all-in wagers are error-free, but arbitrary success does not force all-in behavior. The stake functional also reproduces success only in the original scan order, so re-embedding it in a new least-fresh order is not justified automatically.

Thus the structural boundary after P4-S012 is partiality versus sibling totality, not the wtt use bound.

P4-S011's exact k=2 destroyer is preserved. P4-S005 through P4-S011 remain settled. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S012_VALIDATION.md.

Recommended next bounded session: P4-S013, still at k=2, testing only whether total-on-all-oracles or a weaker uniform-totality condition on the self-avoiding predictor/stake functional forces preservation for the least-fresh scan subclass and thereby identifies the sharp totality boundary excluding the P4-S011 mechanism.
