# P4-S015 close

Date: 2026-10-06
Session: P4-S015
Incoming checkpoint: 7c47680ab22d21e9fd21cb1d276165f0406bc0e8
Scope: selected CAND-01; k=2 stake-weighted skipped-wager loss boundary only
Status: **COMPLETED**

## Result

P4-S015 strictly weakens the P4-S014 finite-horizon raw miss-probability budget at the scan/martingale transfer-certificate level.

For a successful output martingale, first apply a computable savings wrapper which tends to infinity along all sufficiently late prefixes whenever the original martingale is unbounded, while never increasing its fractional stake magnitude.

At a reachable epoch state s, choose a computable finite horizon H(s). For each sentinel bit b and finite horizon-miss filler leaf rho, supply a computable rational w(s,b,rho) majorizing the possible **positive multiplicative gain** of the deferred sentinel wager if that missed epoch later triggers. Losing or flat sentinel wagers have zero loss because skipping them cannot hurt the completion/source comparison.

The exact fair price of the finite weighted miss ticket is

c(s) = 2^{-(H(s)+1)}
       sum_{rho in A_s intersect 2^{H(s)}}
       (w(s,0,rho)+w(s,1,rho)).

If one finite computable constant bounds the pathwise sum of these prices over all reached epochs, then one computable source martingale succeeds whenever the output martingale succeeds. A weighted ticket martingale succeeds if the realized miss weights diverge. If their sum is finite, the P4-S014 truncated/restart hedge loses at most a factor 1+w at each skipped positive sentinel gain; the product of those factors stays finite, and the savings-wrapped output martingale tends to infinity at restart points. A permanently nontriggering missed epoch is again handled by copying filler wagers forever. Their sum succeeds on the globally exhaustive sentinel-first completion, and P4-S001 transfers success back to the source.

The simple corollary w<=a(s) yields the coarser sufficient condition sum p(s)a(s)<infinity, so raw sum p(s) may diverge.

The weakening is strict. A two-control-bit partial stake functional triggers after control 1 or 01, but diverges forever after 00. Every reached epoch therefore has permanent avoiding probability 1/4, so no horizon selector can satisfy the P4-S014 raw pathwise budget on an infinite all-trigger run. Giving sentinel j the small stake a_j=2^{-(j+1)} and using horizon one yields exact weighted ticket cost a_j/4; the sentinels increase, so the total weighted budget is at most 1/4.

The pointwise minimal future-loss envelope is not uniformly computable: a c.e. noncomputable trigger family with an all-in eventual stake makes the exact minimal envelope encode membership in a c.e. noncomputable set. Thus the computable envelope is genuine effective certificate data rather than something silently extractable from arbitrary partial stakes.

P4-S011 necessarily violates every finite certificate of the P4-S015 form. Its target sentinel wagers are all-in and correct, so every realized missed-then-triggered sentinel has positive skipped-gain loss exactly one. The P4-S015 dichotomy would otherwise transfer its winning output martingale to a computable martingale succeeding on the P4-S011 computably random source.

P4-S011 through P4-S014 remain unchanged. P4-S005 through P4-S014 remain settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S015_VALIDATION.md.

Recommended next bounded session: P4-S016, still at k=2 and inside the same least-fresh stake architecture, testing only whether the advance computable future-loss envelope can be replaced by incrementally purchased computable loss tickets as larger postmiss stakes become finitely visible, under a computable total increment budget.
