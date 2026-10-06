# P4-S031 — repeatable no-frontier renewal by stake-scale contraction

Date: 2026-10-06
Session: P4-S031
Incoming checkpoint: 3acf92913c8c89dc32b718832d7966ab5ba0f6bb
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh P4-S012 / P4-S016–P4-S017 ticket architecture only

Result: **P4-S030'S TERMINAL LATE-TRIGGER BRANCH IS NOT ESSENTIAL. THERE IS AN EXACT P4-S012 GLOBAL-k=2 SCAN WITH NO FINITE DEPENDENCY FRONTIER IN EVERY ACTIVE EPOCH SUCH THAT EVERY FINITE TRIGGER, INCLUDING ARBITRARILY LATE GENUINELY ONE-SIDED TRIGGERS, RENEWS ANOTHER ACTIVE NO-FRONTIER EPOCH. WITH H=1, A FIXED RESERVE R=1 MAKES THE CANONICAL P4-S017 FULL-TICKET ACCOUNT GLOBALLY ADMISSIBLE. ON THE ALL-IMMEDIATE-FAVOURABLE COMPLETION THE CANONICAL PREMIUMS STILL DIVERGE HARMONICALLY AND ARE FUNDED BY REALIZED ONE-SIDED PAYOUTS. THE REPLACEMENT FOR TERMINALIZATION IS A COMPUTABLE POSITIVE CONTRACTION OF THE NEXT ACTIVE STAKE SCALE AFTER EACH LATE TRIGGER.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work and again immediately before writes. Repository search returned no committed P4-S031 record, so the session identifier was unused.

P4-S001 through P4-S030 and the required CAND-01 authority were read. P4-S005 through P4-S030 are treated as settled. P4-S011 and P4-S015 through P4-S030 are preserved.

This session tests only whether P4-S030 needs late-trigger terminalization for bare canonical full-ticket solvency. It does not reopen transfer, coercivity, loss-properness, searchability or effective-topology results.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No result is claimed for k>2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained ticket accounting

Fix the settled sentinel-first completion and horizon H. At every unresolved postmiss state v, P4-S016 defines exact child losses L_v(0), L_v(1), fair premium

pi(v) = (L_v(0)+L_v(1))/2,

and realized payout e(v)=L_v(a) on the actual next filler answer a.

P4-S017 bare admissibility asks for a finite reserve R such that every prescribed purchase is affordable on every completion branch:

R + sum_{j<i} e_j - sum_{j<=i} pi_j >= 0.

P4-S030 achieved this with a dead mode: after a late trigger, no later positive ticket was possible. P4-S031 removes dead mode entirely.

## 2. Contracting active stake functional

Use the P4-S012 least-fresh construction. At every reached epoch the current sentinel j is the least unqueried coordinate.

Every epoch is active and carries a positive dyadic scale c. Initially c=1.

In an active epoch:

1. query the least fresh non-sentinel coordinate once and ignore its value; this is the dummy filler;
2. then query successive fresh non-sentinel coordinates until the first value 1 appears;
3. let m>=1 be the position of that first 1 among the post-dummy search fillers;
4. if m=1, expose fractional stake theta=c on sentinel bit 1;
5. if m>=2, expose fractional stake theta=c 2^{-m} on sentinel bit 1;
6. if no 1 ever appears, diverge forever.

After every finite trigger the sentinel is consumed and another active epoch begins:

- if m=1, keep the next scale equal to c;
- if m>=2, set the next scale to c/4.

There is no dead mode and the sentinel outcome does not terminate activity. In particular an arbitrarily late finite trigger always starts another active epoch at the still-positive scale c/4.

The scale is computable from finite history: if l late triggers have occurred so far, c=4^{-l}. Let d be the total computable rational output martingale which is flat on fillers and uses the visible stake theta at the sentinel. Let q=Save(d) be the settled P4-S015 savings wrapper.

## 3. Self-avoidance and exact global k=2

At a reached sentinel j, all coordinates used in earlier completed least-fresh epochs are below j. Hence the prior trigger depths, and therefore the current scale c, can be reconstructed without querying j. In the current epoch the stake functional queries only fresh non-sentinel coordinates. It is self-avoiding and computable.

The scan queries one fresh source coordinate at every output stage.

If some active epoch never finds a post-dummy 1, the scan remains in that epoch forever and eventually queries every coordinate except its current sentinel. The fibre then has exactly two points, differing only at that omitted sentinel.

If every reached epoch triggers finitely, every current sentinel is eventually consumed. Each completed epoch uses only a finite contiguous block of fresh coordinates, so the next least-unqueried sentinel moves strictly right. Every source coordinate is eventually queried and the fibre is a singleton.

Thus every fibre has cardinality at most two. Fresh-coordinate induction gives fair-coin preservation exactly as in the settled P4-S011/P4-S012 least-fresh argument. The map is everywhere total, computable and no-repeat.

## 4. Every active epoch still has no finite dependency frontier

Choose the total computable horizon

H=1,

counting only the ignored dummy filler.

After the dummy and any finite string of zero search fillers, the next unseen search filler remains genuinely value-sensitive:

- answer 0 leaves the epoch unresolved;
- answer 1 makes the sentinel trigger next with a strictly positive stake.

The stake is c at depth 1 and c 2^{-m}>0 at every later finite depth m. Since c remains positive after every finite sequence of late renewals, no reached active epoch has a finite P4-S028 dependency frontier.

This remains true after arbitrarily many finite late triggers: at every finite stage the current scale is 4^{-l}>0.

## 5. Exact canonical one-sided ticket bounds at arbitrary wrapper state

Fix an active epoch of scale c. During its filler search the savings wrapper q is flat, so the ratio

beta = R_risk/q

is constant throughout that epoch and satisfies 0<=beta<=1.

If the stored sentinel bit is 0, every displayed positive stake would lose, so every positive skipped gain is zero and all canonical ticket premiums in that epoch are zero.

Now suppose the stored sentinel bit is 1.

At post-horizon search depth 1, the child-loss vector is

(L_1(0),L_1(1)) = (0, beta c),

so

pi_1 = beta c/2 <= c/2.

After a zero at depth 1, at every later depth m>=2,

(L_m(0),L_m(1)) = (0, beta c 2^{-m}),

and therefore

pi_m = beta c 2^{-(m+1)}.

The entire possible later tail is

sum_{m=2}^infinity pi_m = beta c/4.

Thus the complete gross premium exposure of one active epoch on a zero-payout continuation is at most

beta c/2 + beta c/4 = 3 beta c/4 <= 3c/4.

No assumption about the current savings level or active-risk level is needed beyond beta<=1.

## 6. Reserve-one potential invariant

Start the full-ticket account with

R=1.

At the start of an active epoch of scale c, maintain the invariant

W >= c,

where W is resolved ticket-account capital.

It holds initially because W=c=1.

### Immediate trigger

If m=1 and the stored sentinel is 1, the ticket costs beta c/2 and pays beta c. It is affordable because W>=c>=beta c/2, and after resolution

W' = W + beta c/2 >= c.

The next scale remains c, so the invariant persists.

If the stored sentinel is 0, the premium and payout are both zero. The next scale is again c and the invariant is unchanged.

Thus every immediate trigger renews an active epoch without drawing down the reserve potential.

### Late trigger

Suppose the first search answer is 0 and the trigger occurs later at some m>=2.

Ignoring all payouts, the total premiums purchased in the entire current epoch are at most 3c/4. Since W>=c, every finite purchase is affordable and immediately before any possible final payout the account still has at least

c - 3c/4 = c/4.

The late-trigger payout is nonnegative. The next active scale is c'=c/4, so after the trigger

W' >= c/4 = c'.

The invariant therefore closes exactly across a late renewal.

This also covers a stored sentinel 0, where all premiums are actually zero.

### Infinite nontriggering epoch

If no search filler is ever 1, no later epoch is reached. The finite partial premium sums stay below the same 3c/4 bound, so every prescribed purchase is affordable forever.

### Theorem 1 — repeatable no-frontier bare admissibility

For the exact global-k=2 scan above, H=1 and reserve R=1 make the canonical P4-S016/P4-S017 full-ticket account globally admissible on every completion branch.

Every finite trigger renews another active no-frontier epoch. Terminalization is not used.

## 7. Why contraction replaces terminalization

P4-S030 used a late trigger to send future positive cost to zero. The present proof instead gives future cost a smaller positive budget.

The bankroll identity is local. An active epoch at scale c can consume at most 3c/4 before replenishment. A late trigger leaves at least c/4 of the invariant reserve even if its own payout is discarded. Choosing the next scale c/4 converts exactly that residual capital into the reserve potential for the renewed active epoch.

More generally, if the same within-epoch exposure bound 3c/4 is used and a late trigger replaces c by lambda c, an invariant W>=C c closes whenever

C >= 3/4 + C lambda.

Thus any fixed 0<lambda<1 can be funded by a finite scale potential C>=3/(4(1-lambda)), with the additional trivial requirement that the first one-sided ticket be affordable. The explicit choice lambda=1/4 gives C=1.

P4-S030's terminal late branch is the limiting bankroll idea lambda=0: future scale is killed entirely. P4-S031 shows that a strictly positive renewal scale is enough.

This is a sufficient potential calculation, not a necessity theorem for all repeatable no-frontier streams.

## 8. Divergent cumulative premiums survive

Consider the completion run on which every active epoch has:

- stored sentinel bit 1; and
- first post-horizon search filler equal to 1.

No late trigger occurs, so the scale stays c=1 forever.

Exactly as in P4-S030, after r earlier immediate favourable renewals the P4-S015 savings wrapper has savings r, active risk 1 and total capital r+1. Hence

beta_r = 1/(r+1).

The visited canonical ticket at epoch r has

pi_r = 1/(2(r+1)),
e_r = 1/(r+1).

Therefore

sum_r pi_r = infinity.

The ticket account gains e_r-pi_r=1/(2(r+1)) at every renewal, so the divergent premiums are genuinely funded by realized one-sided payouts. This is not a finite P4-S016 absolute premium budget.

No randomness property is asserted for this completion run.

## 9. Every finite trigger really renews active no-frontier risk

The construction has no hidden terminal branch.

- An immediate trigger with sentinel 1 renews at the same scale.
- An immediate trigger with sentinel 0 renews at the same scale.
- A late trigger with sentinel 1 renews at one quarter scale.
- A late trigger with sentinel 0 renews at one quarter scale.

In every case the next scale is strictly positive and the next epoch again performs the dummy plus unbounded first-1 search. Hence the renewed epoch again has arbitrarily late genuinely one-sided trigger opportunities and no finite dependency frontier.

A branch may contain infinitely many late triggers, causing scales to tend to zero, but no finite trigger ever makes the process inactive.

## 10. Explicit comparison with the settled cases

### P4-S030 — terminal late-trigger recycling

P4-S030's immediate favourable trigger renews the active regime, but any late trigger or unfavourable sentinel enters dead mode. Its reserve 3/4 therefore never has to fund two unreplenished late tails.

P4-S031 removes dead mode. Late triggers can repeat indefinitely. Solvency is preserved because each late trigger contracts the next active exposure from c to c/4, and the reserve invariant W>=c pays for the resulting geometric succession of possible drawdowns.

### P4-S029 — absolute summability

P4-S029 has one no-frontier epoch whose whole positive ticket stream is absolutely summable; reserve 1/4 works without recycling.

P4-S031 may visit infinitely many active epochs and has a completion with divergent total premiums. Local late tails are summable, but global solvency comes from a combination of payout recycling on immediate favourable renewals and geometric contraction after late renewals.

### P4-S028 — constant 1/2 deficit

P4-S028 leaves a one-sided all-in opportunity after every later zero filler. On the all-zero sibling the premium is always 1/2 and payout is always zero, so one single unresolved epoch has divergent deficit.

P4-S031 changes the within-epoch late stake profile to 2^{-m}; therefore each unresolved epoch has at most 3c/4 gross exposure. Repetition across late-triggered epochs is then made summable in reserve potential by c -> c/4.

### P4-S011/P4-S027 — deterministic-frontier recycling

P4-S027 exhausts a finite dependency frontier, after which every positive ticket is deterministic and premium equals certain payout. Its reserve recycles without one-sided risk.

P4-S031 stays on the opposite structural side: there is no finite frontier and all positive tickets remain genuinely one-sided. The reserve survives by contingent payout recycling plus contraction of future exposure, not by certain repayment.

## 11. Repeatable-late-trigger boundary exposed by P4-S031

P4-S030's terminalization is therefore not the essential condition.

The durable sufficient mechanism is a **renewal reserve potential**: after each branch segment which can incur unreplenished one-sided premium drawdown, the remaining ticket capital must dominate a computable budget for the renewed active state. Terminalization makes that next budget zero; P4-S031 instead makes it a smaller positive value.

The exact P4-S017 obstruction remains unchanged. If a repeatable branch can return to active states while cumulative premium minus prior payouts becomes unbounded, no finite reserve is globally admissible. P4-S031 avoids that obstruction by forcing the worst unreplenished late-renewal budget to contract geometrically.

No general necessity theorem for such a potential is claimed beyond the already-settled purchase-time deficit criterion.

## 12. Successes and limits

Successful:

1. Removed P4-S030's late-trigger terminalization completely.
2. Constructed an exact total, computable, no-repeat, fair-coin-preserving global-k=2 scan.
3. Made every finite trigger renew another active epoch.
4. Preserved no finite dependency frontier in every reached active epoch.
5. Preserved genuinely one-sided trigger opportunities at arbitrarily late filler depths.
6. Proved a finite global canonical full-ticket reserve, explicitly R=1.
7. Allowed infinitely many late-trigger renewals by positive scale contraction.
8. Preserved a completion run with divergent harmonic canonical premiums.
9. Verified that those divergent premiums are funded by realized one-sided payouts.
10. Preserved P4-S028, P4-S029, P4-S030 and P4-S011/P4-S027 as distinct bankroll regimes.

Not claimed:

1. No new computable-randomness destroyer is constructed.
2. No new transfer theorem is proved.
3. No necessity of geometric contraction or of any particular reserve potential is claimed.
4. No settled P4-S005 through P4-S030 result is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S005 through P4-S030 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015 through P4-S030 are preserved exactly.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

## Next bounded question

P4-S032 should stay strictly at k=2 and test only whether P4-S031's **explicit contraction after a late trigger** is essential. Try to construct an exact repeatable no-frontier global-k=2 stream in which every finite trigger renews the same raw active stake scale, with no dead mode and no explicit scale contraction, yet one finite canonical full-ticket reserve survives divergent premiums through savings-wrapper dilution and payout recycling. Otherwise isolate the narrow stationary repeatable-late-trigger deficit condition forcing failure. Compare explicitly with P4-S031, P4-S030, P4-S028 and P4-S011/P4-S027.
