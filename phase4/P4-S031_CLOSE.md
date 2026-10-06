# P4-S031 close

Date: 2026-10-06
Session: P4-S031
Incoming checkpoint: 3acf92913c8c89dc32b718832d7966ab5ba0f6bb
Scope: selected CAND-01; k=2 repeatable no-frontier self-financing boundary only
Status: **COMPLETED**

## Result

P4-S031 answers the bounded question **yes**.

P4-S030's terminal late-trigger branch is not essential. There is an exact P4-S012 total computable no-repeat fair-coin-preserving global-k=2 least-fresh scan in which every reached epoch is active, every active epoch has no finite dependency frontier, and every finite trigger — including arbitrarily late genuinely one-sided triggers — starts another active no-frontier epoch.

Use H=1 after one ignored dummy filler. Give each active epoch a positive scale c. The first post-horizon 1 triggers stake c if immediate and c 2^{-m} if first seen at later depth m>=2. Immediate triggers keep the next scale c; late triggers renew at scale c/4. No trigger ever enters dead mode.

For an arbitrary savings-wrapper state, if beta is active risk divided by total q-capital, the whole possible premium exposure of an epoch is at most 3 beta c/4 <= 3c/4. Starting an epoch with ticket capital W>=c therefore funds every purchase. An immediate trigger preserves W>=c; after a late trigger, even discarding its nonnegative payout leaves W>=c/4, exactly the invariant required by the renewed scale c/4. Thus reserve R=1 is globally admissible on every completion.

On the all-immediate-favourable completion, c remains 1 and the savings wrapper again gives premiums 1/(2(r+1)); they diverge harmonically while realized payouts 1/(r+1) finance later purchases.

P4-S030 is the terminal endpoint of the same reserve idea. P4-S029 remains the absolutely summable case, P4-S028 the zero-payout divergent-deficit case, and P4-S011/P4-S027 the deterministic-frontier recycling case.

## Guards

- P4-S005 through P4-S030 remain settled.
- P4-S011 and P4-S015 through P4-S030 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.
- Phase 4 remains OPEN; Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Next bounded task

P4-S032: test only whether the explicit positive scale contraction after late triggers can also be removed, so every finite trigger renews the same raw active stake scale while a finite global reserve still survives divergent premiums through savings-wrapper dilution and payout recycling; otherwise isolate the narrow stationary repeatable-late-trigger deficit condition.
