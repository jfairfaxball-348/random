# P4-S029 — finite dependency frontiers are not necessary for bare reserve

Date: 2026-10-06
Session: P4-S029
Incoming checkpoint: dbdee97f6981e00cd2a677b742de042f36c7dacc
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh P4-S012 / P4-S016–P4-S017 ticket architecture only

Result: **FINITE EPOCH DEPENDENCY FRONTIERS ARE NOT NECESSARY FOR BARE ADMISSIBILITY. THE EXACT P4-S028 FIRST-1-SEARCH GLOBAL-k=2 SCAN CAN RETAIN NO FINITE INITIAL FRONTIER AND GENUINELY ONE-SIDED TRIGGER OPPORTUNITIES AT EVERY ARBITRARILY LATE FILLER, WHILE A COMPUTABLE DECAY OF THE SKIPPED POSITIVE GAIN MAKES THE CANONICAL FULL-TICKET RESERVE FINITE. WITH FRACTIONAL SENTINEL STAKE alpha_n=2^{-n} WHEN THE FIRST 1 APPEARS AT FILLER n AND H=1, THE POSTMISS LOSS VECTORS ON THE STORED-SENTINEL-1/ALL-ZERO SIBLING ARE (0,2^{-n}), THE FAIR PREMIUMS ARE 2^{-(n+1)}, AND THEIR WHOLE TAIL SUM IS 1/4. HENCE R=1/4 IS GLOBALLY ADMISSIBLE. THE SHARP PARAMETRIC BOUNDARY IN THIS SAME NO-FRONTIER GEOMETRY IS SUMMABILITY OF THE ONE-SIDED PREMIUM MASS: P4-S028 IS alpha_n=1 AND HAS UNBOUNDED DEFICIT; THE PRESENT alpha_n=2^{-n} EXAMPLE HAS FINITE DEFICIT. P4-S011/P4-S027 IS DIFFERENT AGAIN: FRONTIER EXHAUSTION MAKES TICKETS DETERMINISTIC, SO PAYOUTS RECYCLE EVEN WHEN PREMIUMS DIVERGE.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work and again immediately before writes. Commit search showed P4-S028 as the latest completed session and repository search returned no committed P4-S029 record. P4-S029 was therefore unique.

P4-S001 through P4-S028 and the required CAND-01 authority were read. P4-S005 through P4-S028 are treated as settled. P4-S011 and P4-S015 through P4-S028 are preserved.

This session tests only whether P4-S028's computable finite dependency frontier is necessary for bare admissibility of the canonical P4-S016/P4-S017 full-ticket account. It does not reopen the transfer, coercivity, loss-properness, searchability or effective-topology routes.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No result is claimed for k>2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained ticket accounting

Fix a computable horizon selector H. Along a sentinel-first completion run, enumerate the visited unresolved postmiss ticket nodes as v_0,v_1,... . Write

[
pi_i=pi(v_i)=rac{L_{v_i}(0)+L_{v_i}(1)}2
]

for the exact fair premium and e_i for the realized ticket payout.

By the settled P4-S017 definition, a reserve R is globally admissible exactly when every prescribed purchase is affordable on every completion run:

[
R+sum_{j<i}e_j-sum_{jle i}pi_jge 0.
]

Equivalently, for this fixed canonical ticket stream the least global reserve is controlled by the purchase-time premium deficit

[
Delta
=
sup_{	ext{runs}}sup_i
left(
sum_{jle i}pi_j-sum_{j<i}e_j
ight).
]

Thus finite-frontier determinism is one way to keep (Delta) finite, but the definition itself allows a second mechanism: genuinely one-sided tickets may be affordable if their unreplenished premium mass is summable.

## 2. The same no-frontier scan as P4-S028

Reuse exactly the P4-S028 self-avoiding predictor P.

- On input 0, query coordinates 1,2,3,... in order until the first value 1 is found; then halt with prediction 1. If every queried value is 0, diverge forever.
- On every input j>0, halt immediately with prediction 1.

The induced least-fresh scan is everywhere total, computable, no-repeat, fair-coin preserving and globally k=2.

If the first epoch never triggers, every positive coordinate is queried and only sentinel 0 is omitted, so the fibre has size two. If it triggers, sentinel 0 is consumed and all later sentinels are consumed immediately, so the scan is exhaustive and the fibre is a singleton.

Exactly as in P4-S028, there is no finite dependency frontier at the initial epoch. After every finite string of zero fillers, a later unseen filler still changes the trigger behavior: value 1 makes the prediction visible while value 0 leaves the epoch unresolved.

This absence of a frontier is structural and is unchanged by the martingale chosen below.

## 3. A decaying single-sentinel martingale

Define a computable rational output martingale d as follows.

It starts with capital 1 and is flat on every filler. If the first epoch becomes visible because the first filler value 1 occurs at coordinate n>=1, then immediately before the withheld sentinel 0 is queried let d make a fractional wager

[
alpha_n=2^{-n}
]

on sentinel bit 1. Thus at that one sentinel node,

[
d(	au_n1)=d(	au_n)(1+alpha_n),
qquad
d(	au_n0)=d(	au_n)(1-alpha_n).
]

After that sentinel is consumed, d freezes forever. If the first epoch never triggers, d stays identically 1.

This is a total nonnegative computable rational martingale. Let q=Save(d) be the settled P4-S015 savings wrapper.

Before the unique possible nonzero sentinel wager, q has savings 0 and active risk 1. Therefore its fractional stake there is exactly (alpha_n), and on stored sentinel bit b=1 the positive skipped gain is

[
ell_q(	au_n,1)=alpha_n=2^{-n}.
]

For stored sentinel bit b=0 the wager is losing, so the positive skipped gain is 0.

No later epoch has any positive skipped gain because d, and hence q, is flat after the first sentinel consumption.

## 4. H=1 leaves arbitrarily late one-sided tickets

Choose the total computable horizon H=1 at every epoch.

If the first filler is 1, the first epoch triggers within the horizon and there is no postmiss ticket. Suppose instead that the first filler is 0, so the first epoch misses its horizon.

On the sentinel-first completion branch with stored sentinel bit b=1, after zeros have appeared at filler coordinates 1,...,n-1, where n>=2, consider the unresolved node immediately before filler n.

- filler 0 leaves the first epoch unresolved, so its last-chance loss is 0;
- filler 1 makes the prediction visible and makes the sentinel trigger next, with skipped positive q-gain (2^{-n}).

Hence

[
(L_n(0),L_n(1))=(0,2^{-n}),
qquad
pi_n=2^{-(n+1)}.
]

These are genuinely one-sided positive tickets at every n>=2. They persist arbitrarily far beyond the horizon. Therefore no finite dependency frontier has been smuggled back into the example.

If the stored sentinel bit is b=0, both positive-loss values are zero, so every ticket premium is zero.

## 5. Reserve one quarter is globally admissible

The whole possible postmiss premium mass in the only positive-cost first epoch is

[
sum_{n=2}^{infty}pi_n
=
sum_{n=2}^{infty}2^{-(n+1)}
=
rac14.
]

All later epochs have zero premiums because q is flat after first-sentinel consumption.

Therefore the P4-S016 absolute premium certificate already holds with computable bound B=1/4. In particular the canonical P4-S017 full-ticket account is globally admissible with reserve

[
R=rac14.
]

The direct purchase-time check is also exact.

On the stored-sentinel-1/all-zero avoiding branch, every realized payout is 0. After buying the tickets through filler N>=2, the remaining cash is

[
rac14-sum_{n=2}^{N}2^{-(n+1)}
=
2^{-(N+1)}>0.
]

So every next full premium is affordable, although the cash tends to 0 along the infinite avoiding branch.

If the first 1 eventually occurs at filler n, all earlier tickets paid 0 and the nth ticket pays (2^{-n}), which can only improve the account. If b=0, no positive premium was ever charged. Thus no other completion branch is worse.

### Theorem 1 — finite frontier is not necessary

There exists an exact P4-S012 total fair-coin-preserving global-k=2 least-fresh scan with no finite dependency frontier at its first epoch and with positive one-sided trigger opportunities at arbitrarily late fillers, together with a computable horizon H and a finite computable rational reserve R, such that the canonical P4-S016/P4-S017 full-ticket account is globally admissible.

The explicit values above are H=1 and R=1/4.

Hence P4-S028's finite dependency frontier is a sufficient structural condition for bare admissibility, not a necessary one.

## 6. Parametric form: premium mass is the sharp boundary in this witness family

The same proof works with any computable rational sequence

[
0<alpha_nle 1
]

in place of (2^{-n}), using the same first-1-search scan and one sentinel wager of fractional size (alpha_n) when the first 1 occurs at filler n.

For H=h, on the stored-sentinel-1/all-zero branch the postmiss tickets are

[
(L_n(0),L_n(1))=(0,alpha_n),
qquad
pi_n=alpha_n/2
]

for every n>h.

Therefore:

- if the tail (sum_{n>h}alpha_n) has a finite computable bound, that bound divided by 2 supplies a finite global reserve;
- if (sum_{n>h}alpha_n=infty), the all-zero branch has zero payouts and unbounded purchase-time premium deficit, so no finite reserve is globally admissible.

This gives an exact quantitative boundary inside one fixed no-frontier scan geometry.

P4-S028's witness is the nondecaying case (alpha_n=1). Its premium is 1/2 at every postmiss node and the deficit after N nodes is N/2.

P4-S029 takes (alpha_n=2^{-n}). The trigger dependence is just as late and just as one-sided, but the whole premium deficit is bounded by 1/4.

A simple natural nondegeneracy corollary is therefore available without asserting frontier necessity: if a zero-payout avoiding sibling carries infinitely many one-sided opportunities whose positive skipped gains are bounded below by some fixed (arepsilon>0), then each corresponding premium is at least (arepsilon/2), so no finite reserve can be globally admissible. P4-S028 is the special case (arepsilon=1).

## 7. Explicit comparison with P4-S011/P4-S027

P4-S011 remains unchanged.

P4-S027 puts its wtt witness in a globally use-clipped form. P4-S028 reformulates that clipping as a computable finite epoch dependency frontier. After the frontier is exhausted, every positive postmiss ticket is deterministic:

[
(L_v(0),L_v(1))=(ell_v,ell_v),
qquad
pi(v)=ell_v.
]

The purchase may require as much as one unit because (0leell_vle1), but the certain payout immediately restores the spent amount. Thus reserve R=1 can recycle forever even when the cumulative premium sum diverges.

The three cases are therefore genuinely distinct:

1. **P4-S011/P4-S027 deterministic-frontier case:** potentially divergent premiums, but each premium is certainly repaid; reserve 1 recycles.
2. **P4-S028 constant one-sided case:** no frontier, ((0,1)) tickets, premium 1/2 and zero payout on one avoiding sibling; deficit diverges.
3. **P4-S029 decaying one-sided case:** no frontier, ((0,2^{-n})) tickets at arbitrarily late fillers, but total zero-payout premium deficit is only 1/4.

Bare admissibility is therefore governed by bounded purchase-time deficit, not by finite dependency frontiers alone.

## 8. What changed, and what did not

Established in P4-S029:

1. Finite dependency frontiers are not necessary for bare canonical full-ticket admissibility.
2. The exact P4-S028 no-frontier scan geometry already supports the separation; only the skipped-gain scale changes.
3. Genuine one-sided trigger dependence may persist arbitrarily late while the canonical reserve remains finite.
4. A computably summable positive-gain schedule gives an explicit finite reserve.
5. Within the first-1-search family, summability versus divergence of the one-sided premium mass is the exact bankroll boundary.
6. A uniform positive lower bound on infinitely many zero-payout one-sided opportunities forces reserve failure.

Not claimed:

1. No new computable-randomness destroyer is constructed.
2. No general characterization of bare admissibility for all P4-S012 scans beyond the settled purchase-time deficit definition is claimed.
3. No coercivity, loss-properness or searchable-bar conclusion is obtained.
4. No settled P4-S005 through P4-S028 route is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S005 through P4-S028 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015 through P4-S028 are preserved exactly.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

## Next bounded question

The new separation uses the stronger P4-S016 mechanism: its one-sided premium mass is absolutely summable. The smallest remaining bankroll question is whether no-frontier bare admissibility can persist **without** any finite absolute premium-sum budget, through genuine self-financing recycling of earlier one-sided ticket winnings.

A bounded P4-S030 should stay strictly at k=2 and test only whether there is an exact P4-S012 no-frontier global-k=2 scan with arbitrarily late one-sided tickets, divergent cumulative premiums on some completion run, yet a finite globally admissible canonical P4-S017 reserve because payouts recycle capital; otherwise isolate the narrow obstruction forcing a zero-payout sibling to inherit divergent deficit.
