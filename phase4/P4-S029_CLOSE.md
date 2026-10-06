# P4-S029 close

Date: 2026-10-06
Session: P4-S029
Incoming checkpoint: dbdee97f6981e00cd2a677b742de042f36c7dacc
Scope: selected CAND-01; k=2 finite-frontier necessity / bare reserve boundary only
Status: **COMPLETED**

## Result

P4-S028's computable finite dependency frontier is **not necessary** for bare admissibility.

Reuse the exact first-1-search global-k=2 scan from P4-S028, so the first epoch still has no finite dependency frontier and one-sided trigger opportunities remain at arbitrarily late fillers. Change only the output martingale: if the first 1 appears at filler n, wager fractional size (2^{-n}) on the stored sentinel being 1, then freeze.

With horizon H=1, the stored-sentinel-1 postmiss tickets are
[
(0,2^{-n}),qquad pi_n=2^{-(n+1)},qquad nge2.
]
Their total premium mass is 1/4. Hence reserve R=1/4 makes the canonical P4-S016/P4-S017 full-ticket account globally admissible even on the all-zero avoiding sibling.

The same first-1-search family with stake sequence (alpha_n) has one-sided premium (alpha_n/2). Thus summable tails give finite reserve, while divergent tails fail on the zero-payout all-zero sibling. P4-S028 is the constant (alpha_n=1) case. P4-S011/P4-S027 remains different: frontier exhaustion makes tickets deterministic, so payouts recycle even when premiums diverge.

## Guards

- P4-S005 through P4-S028 remain settled.
- P4-S011 and P4-S015 through P4-S028 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.
- Phase 4 remains OPEN; Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Next bounded task

P4-S030: test only whether no-frontier bare admissibility can survive divergent absolute premium sums through genuine P4-S017 self-financing payout recycling, while retaining arbitrarily late one-sided tickets.
