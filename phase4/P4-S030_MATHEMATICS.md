# P4-S030 — no-frontier self-financing recycling with divergent premiums

Date: 2026-10-06
Session: P4-S030
Incoming checkpoint: 45b0a3b0d5b2715f2b9886e826803aa2994dcd2f
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh P4-S012 / P4-S016–P4-S017 ticket architecture only

Result: **YES. AN EXACT P4-S012 GLOBAL-k=2 SCAN CAN HAVE NO FINITE DEPENDENCY FRONTIER IN EVERY ACTIVE EPOCH, GENUINELY ONE-SIDED LAST-CHANCE TICKETS AT ARBITRARILY LATE FILLERS, AND DIVERGENT CUMULATIVE CANONICAL PREMIUMS ON A COMPLETION RUN, YET ADMIT A FINITE GLOBALLY ADMISSIBLE P4-S017 FULL-TICKET RESERVE THROUGH GENUINE PAYOUT RECYCLING. AN EXPLICIT CONSTRUCTION HAS H=1 AND RESERVE R=3/4.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work and again immediately before writes. The incoming tree contained P4-S001 through P4-S029 and no P4-S030 mathematics, close or validation record; commit search returned no P4-S030 commit. P4-S030 was therefore unique.

P4-S001 through P4-S029 and the required CAND-01 authority were read. P4-S005 through P4-S029 are treated as settled. P4-S011 and P4-S015 through P4-S029 are preserved.

This session tests only the bare-bankroll question exposed by P4-S029. It does not reopen transfer, coercivity, loss-properness, searchability or effective-topology results.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No result is claimed for k>2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained ticket accounting

Fix the settled sentinel-first completion and a computable horizon selector H. At every unresolved postmiss state v, P4-S016 supplies the exact last-chance child losses L_v(0),L_v(1), fair premium

[
pi(v)=rac{L_v(0)+L_v(1)}2,
]

and realized payout e(v)=L_v(a) on the actual fresh filler answer a.

For a visited ticket sequence, reserve R is globally admissible exactly when every prescribed purchase satisfies

[
R+sum_{j<i}e_j-sum_{jle i}pi_jge0.
]

P4-S029 obtained this by an absolute premium bound. P4-S030 instead makes the cumulative premium sum diverge on one run and uses earlier payouts to fund later tickets.

## 2. Active/dead self-avoiding stake functional

Use the P4-S012 least-fresh construction. At each reached epoch the current sentinel j is the least unqueried coordinate.

The functional has two finite-history modes.

- **Dead mode:** halt immediately with stake 0. The scan therefore consumes j at zero stake and remains dead forever.
- **Active mode:** query the least fresh non-sentinel coordinate once and ignore its value. Call this the dummy filler. Then query successive fresh non-sentinel coordinates until the first value 1 is found. Let m>=1 be its position among these post-dummy search fillers.
  - if m=1, halt with fractional stake theta=1 on sentinel bit 1;
  - if m>=2, halt with stake theta=2^{-m} on sentinel bit 1;
  - if no 1 is ever found, diverge forever.

After a triggered active epoch, the next epoch is active exactly when m=1 and the consumed sentinel bit was 1. Every late trigger m>=2 and every sentinel outcome 0 sends the future process to dead mode.

This is a computable self-avoiding partial stake functional. To compute the mode for a reached sentinel j, simulate the earlier least-fresh epochs from the start. Earlier fillers and sentinels all lie below j, so the reconstruction never queries j. In the current epoch the functional also never queries j.

Let d be the total computable output martingale which is flat on fillers and uses exactly the visible stake theta at the sentinel. In dead mode it is flat. Put q=Save(d) using the settled P4-S015 savings wrapper.

## 3. Exact global-k=2 scan check

The least-fresh scan queries one fresh source coordinate at every output stage.

If an active epoch never finds a post-dummy 1, it never triggers and eventually queries every coordinate other than its withheld sentinel. The output fibre then has exactly two points.

If every active epoch reached on a transcript triggers, each current sentinel is eventually consumed. An early favorable trigger may start another active epoch; every other trigger enters dead mode, where future sentinels are consumed immediately. Hence every coordinate is eventually queried and the fibre is a singleton.

Therefore every fibre has cardinality at most two.

For any finite output word, the queried source coordinates are pairwise distinct and are determined from the preceding output bits. Its preimage imposes exactly those independent fair-bit equations, so the map preserves fair coin.

Thus this is an everywhere-total computable no-repeat fair-coin-preserving global-k=2 scan.

## 4. No active epoch has a finite dependency frontier

Choose the total computable horizon

[
H=1,
]

counting the ignored dummy filler. Every active epoch is still unresolved after that horizon.

After the dummy and any finite string of 0 search fillers, a later unseen search filler still matters genuinely: value 0 leaves the epoch unresolved, while value 1 makes the sentinel trigger next with a positive stake. Such a later coordinate exists beyond every proposed finite frontier, and the positive stake 2^{-m} is nonzero for every m.

Hence no active epoch has a finite P4-S028 dependency frontier. The postmiss ticket stream contains genuinely one-sided positive tickets at arbitrarily late filler depths.

## 5. Savings-wrapper scale after early renewals

Suppose r>=0 earlier active epochs have all renewed, meaning their first post-horizon search filler was 1 and their sentinel bit was also 1.

Inductively the P4-S015 savings wrapper has

[
S=r,qquad R_{mathrm{risk}}=1,qquad q=r+1
]

at the next active epoch.

Indeed an early stake theta=1 followed by sentinel bit 1 sends active risk 1 to 2; the wrapper saves one unit and resets active risk to 1.

Write

[
a_r=rac1{r+1}.
]

At the next active epoch with stored sentinel bit 1:

- an immediate post-horizon trigger m=1 has positive multiplicative skipped gain a_r;
- a late trigger m>=2 has positive skipped gain a_r 2^{-m}.

If the stored sentinel bit is 0, every positive stake is losing and the positive skipped gain is 0.

## 6. Exact one-sided tickets

Fix an active epoch r and stored sentinel bit 1.

At the first post-horizon search node,

[
(L_{r,1}(0),L_{r,1}(1))=(0,a_r),
qquad
pi_{r,1}=rac{a_r}{2}.
]

After the first search answer is 0, at later depth m>=2,

[
(L_{r,m}(0),L_{r,m}(1))
=
(0,a_r2^{-m}),
qquad
pi_{r,m}=a_r2^{-(m+1)}.
]

These tickets are genuinely one-sided at every depth.

The entire late tail after losing the first ticket is

[
sum_{m=2}^{infty}pi_{r,m}
=
rac{a_r}{2}sum_{m=2}^{infty}2^{-m}
=
rac{a_r}{4}.
]

Therefore the complete premium exposure of an active epoch along a zero-payout avoiding continuation is

[
rac{a_r}{2}+rac{a_r}{4}
=
rac{3a_r}{4}
lerac34.
]

A late trigger only adds a positive payout before the process enters dead mode.

## 7. Reserve 3/4 is globally admissible

Start the canonical P4-S017 full-ticket account with

[
R_0=rac34.
]

Let W_r be its resolved capital at the start of an active epoch after r earlier favorable early renewals.

Initially W_0=3/4. If the first post-horizon search filler is 1 and the stored sentinel is 1, the ticket costs a_r/2 and pays a_r. Hence

[
W_{r+1}=W_r+rac{a_r}{2}.
]

So W_r>=3/4 for every renewed active epoch.

If instead the first search filler is 0, every subsequent prescribed purchase through the entire unresolved tail costs in total at most 3a_r/4<=3/4<=W_r. Thus every finite purchase is affordable. If a later 1 eventually appears, that ticket pays a_r2^{-m} and the process enters dead mode. If no later 1 appears, the finite partial sums of premiums remain below the same 3a_r/4 bound. In either case there are no future positive ticket costs after that active epoch ends or remains forever unresolved.

If the stored sentinel is 0, all positive-loss tickets have premium zero. Dead-mode epochs also have zero premium.

Hence every completion branch and every prescribed ticket node satisfies the P4-S017 no-overdraft inequality.

### Theorem 1 — no-frontier divergent-premium bare admissibility

The exact global-k=2 scan above has no finite dependency frontier in every active epoch and has genuinely one-sided trigger opportunities at arbitrarily late fillers. With H=1, its canonical full-ticket account is globally admissible with finite reserve R=3/4.

## 8. Cumulative premiums nevertheless diverge

Consider the completion run on which every active epoch has stored sentinel bit 1 and its first post-horizon search filler is 1.

At active epoch r only the first ticket is visited, with

[
pi_r=rac{1}{2(r+1)},
qquad
e_r=rac{1}{r+1}.
]

Therefore

[
sum_rpi_r=infty.
]

The P4-S016 absolute premium-sum hypothesis fails on this very run.

At the same time the ticket account gains

[
e_r-pi_r=rac{1}{2(r+1)}
]

at every renewal. Its resolved capital is

[
rac34+rac12sum_{t<r}rac1{t+1},
]

so the divergent gross premiums are genuinely funded by realized one-sided payouts. This is not merely a finite initial premium budget in disguise.

No randomness property is asserted for this completion run.

## 9. The exact zero-payout obstruction remains

The positive construction does not weaken the elementary P4-S017 obstruction.

If some completion run has a tail with no payouts and divergent remaining premium sum, then its purchase-time deficit diverges and no finite reserve can be globally admissible. More generally, the exact obstruction is unbounded cumulative premium minus prior payout.

P4-S030 avoids that obstruction by making the two relevant kinds of branch behave differently:

1. the branch which renews another active epoch receives a contemporaneous payout larger than the premium just spent;
2. a branch which exposes the arbitrarily long late one-sided tail has only a summable unreplenished premium mass, and a late trigger terminalizes future positive cost.

Thus no completion can concatenate infinitely many unpaid bad tails.

## 10. Explicit comparison with the settled cases

### P4-S029 — summable-decay no-frontier solvency

P4-S029 has the same qualitative no-frontier geometry, but its whole positive ticket stream is absolutely summable. Reserve 1/4 is already a P4-S016 certificate. No payout recycling is required.

P4-S030 removes that absolute budget: the all-early-favorable premium sum is harmonic and divergent.

### P4-S028 — constant-1/2 zero-payout deficit

P4-S028 keeps a one-sided all-in ticket of premium 1/2 available after every later zero filler on one infinite sibling. That sibling never pays and its deficit grows without bound.

P4-S030 preserves arbitrarily late one-sided tickets but makes the unreplenished late tail summable inside each active epoch. Only a favorable ticket can renew the expensive regime, and that ticket pays for the renewal.

### P4-S011/P4-S027 — deterministic-frontier recycling

P4-S027 exhausts a finite dependency frontier. Positive tickets are deterministic:

[
(L(0),L(1))=(ell,ell),qquad pi=ell,
]

so reserve one is spent and restored with certainty even while premiums diverge.

P4-S030 has no such frontier. Its positive tickets remain genuinely one-sided. Recycling is therefore contingent on an actual favorable filler/sentinel outcome, not deterministic repayment.

### P4-S017 — earlier fixed-frontier recycling example

P4-S017 already showed divergent premiums with one-sided payout recycling for a fixed H, but its trigger decision was resolved by a fixed second filler. P4-S030 adds the missing P4-S029/S028 feature: arbitrarily late value-sensitive trigger opportunities and no finite epoch dependency frontier.

## 11. What changed, and what did not

Established in P4-S030:

1. Finite dependency frontiers are not needed even when cumulative premiums diverge.
2. Absolute P4-S016 premium summability is not needed for bare no-frontier admissibility.
3. Genuinely one-sided ticket payouts can self-finance later one-sided tickets.
4. An exact global-k=2 scan can retain arbitrarily late one-sided risk in every active epoch and still have finite reserve 3/4.
5. A zero-payout sibling with divergent premium deficit remains a sufficient failure condition.
6. The relevant distinction is bounded unreplenished drawdown plus paid renewal, not dependency depth or gross premium mass alone.

Not claimed:

1. No new computable-randomness destroyer is constructed.
2. No new transfer theorem is proved.
3. No necessity theorem is claimed beyond the exact purchase-time deficit criterion already settled in P4-S017.
4. No settled P4-S005 through P4-S029 route is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S005 through P4-S029 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015 through P4-S029 are preserved exactly.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

## Next bounded question

The construction uses one terminalization device: a late trigger, or an unfavorable sentinel, turns future positive ticket cost off. The smallest remaining bankroll question is whether that terminalization is essential.

P4-S031 should stay strictly at k=2 and test only whether there is an exact no-frontier global-k=2 scan in which **every finite trigger, including arbitrarily late one-sided triggers, renews another active no-frontier epoch**, cumulative premiums diverge on some run, and one finite global full-ticket reserve remains admissible by recycling. Otherwise isolate the narrowest repeatable-late-trigger deficit condition forcing failure.
