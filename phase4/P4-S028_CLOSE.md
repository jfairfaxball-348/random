# P4-S028 close

Date: 2026-10-06
Session: P4-S028
Incoming checkpoint: e94ff739fc2fbc77f519ce0afb0458624ebfc673
Scope: selected CAND-01; k=2 finite dependency frontier / bare reserve boundary only
Status: **COMPLETED**

## Result

P4-S027's bare-admissibility proof extends from a wtt use bound to the weaker structural datum it actually uses: a computable finite per-epoch dependency frontier whose exhaustion makes all later trigger data independent of future filler values.

A computable least-fresh horizon can exhaust that finite frontier. After a miss, both next-filler children then have identical trigger data and, because the P4-S012 martingale and its savings wrapper are flat on fillers, identical skipped positive gain. Every positive P4-S016 ticket is deterministic. Its premium equals its certain payout and is at most one, so reserve R=1 is globally admissible.

The broader P4-S012 partial-predictor setting does not force such a frontier. An exact first-1-search predictor gives a total fair-coin-preserving global-k=2 scan whose first epoch has no finite frontier. On the sentinel-first branch with stored sentinel 1 and all later fillers 0, every post-horizon node has payoff vector (0,1), premium 1/2, and actual payout 0. Hence every finite horizon leaves arbitrarily large premium deficit and no finite reserve is globally admissible.

This is an existence separation, not a necessity theorem: absence of a finite frontier is not claimed to force reserve failure for every partial predictor.

P4-S011 remains on the positive side because P4-S027's globally use-clipped witness supplies exactly such a finite frontier. Its reserve-one account is still noncoercive and non-loss-proper.

## Guards

- P4-S005 through P4-S027 remain settled.
- P4-S011 and P4-S015 through P4-S027 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.
- Phase 4 remains OPEN; Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Next bounded task

P4-S029: test only whether finite dependency frontiers are necessary for bare admissibility by seeking a no-frontier global-k=2 scan with arbitrarily late one-sided trigger opportunities but finite reserve, or a narrow nondegenerate necessity theorem.