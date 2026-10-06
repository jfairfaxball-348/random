# P4-S017 — self-financing last-chance reserves

Date: 2026-10-06
Session: P4-S017
Incoming checkpoint: 4f587d38ff58c3eb6314c4f1d22bfd57594c77ea
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh stake subclass only

Result: **THE P4-S016 ABSOLUTE PREMIUM-SUM BUDGET CAN BE REPLACED, FOR THE SAME LAST-CHANCE TICKET STREAM, BY A COERCIVE SELF-FINANCING RESERVE. EARLIER TICKET PAYOUTS MAY FUND LATER PREMIUMS. THE EXACT CONDITION FOR THE P4-S016 TICKET/RESTART DICHOTOMY IS: THE CANONICAL FULL-TICKET ACCOUNT STAYS NONNEGATIVE ON EVERY RUN, AND WHEN REALIZED POSITIVE SKIPPED LOSS DIVERGES ITS CAPITAL IS UNBOUNDED. BARE NO-OVERDRAFT IS NOT ENOUGH. NO INFINITE OPTIONAL PROJECTION IS USED. P4-S011 ADMITS NO SUCH COERCIVE RESERVE CERTIFICATE FOR ANY COMPUTABLE HORIZON SELECTOR.**

## Authority, uniqueness and scope

Live main matched the requested checkpoint 4f587d38ff58c3eb6314c4f1d22bfd57594c77ea exactly before substantive work. Repository search returned no committed P4-S017 record, so the session identifier was unused.

P4-S001 through P4-S016 and required CAND-01 authority were read. P4-S005 through P4-S016 are treated as settled. P4-S011's exact global-k=2 destroyer, P4-S015's weighted theorem and savings wrapper, and P4-S016's envelope-free last-chance-ticket theorem are preserved.

This session changes only the bankroll condition used to buy the P4-S016 exact one-step tickets after a finite-horizon miss. It does not reopen settled routes.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No result is claimed for k>2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained P4-S016 ticket stream

Fix a nonnegative rational-valued computable output martingale d and let q=Save(d) be the settled P4-S015 savings wrapper. Fix a total computable finite horizon selector H and use the settled globally exhaustive sentinel-first completion C.

After a horizon miss, at every unresolved postmiss state v the next physical bit is a fresh filler. P4-S016 computes exact nonnegative rational child losses `L_v(0),L_v(1)`, where `L_v(a)` is the positive multiplicative gain of q's deferred sentinel wager if filler answer a makes the sentinel trigger immediately, and is zero otherwise. The exact fair premium is

`pi(v)=(L_v(0)+L_v(1))/2.`

Along a completion run enumerate visited unresolved postmiss states as v_0,v_1,... . Put `pi_i=pi(v_i)` and let `e_i=L_{v_i}(a_i)` be the actual payout. Nonzero e_i are exactly the positive skipped-sentinel gains of missed epochs which later trigger.

P4-S016 assumed a uniform finite bound on `sum_i pi_i`. P4-S017 removes that absolute expenditure requirement.

## 2. Canonical self-financing ticket account

Start a ticket account with finite computable rational reserve R. Immediately before buying ticket i its cash capital is

`W_i^- = R + sum_{j<i} e_j - sum_{j<i} pi_j.`

Buying the full ticket is possible exactly when `W_i^- >= pi_i`. After resolution,

`W_{i+1}=R+sum_{j<=i}e_j-sum_{j<=i}pi_j.`

Each ticket is fair, so this account is a computable martingale whenever every prescribed purchase is affordable.

### Definition — self-financing admissibility

The ticket stream is R-admissible if on every completion run and every visited ticket node,

`R+sum_{j<i}e_j-sum_{j<=i}pi_j >= 0.`

Thus every next full premium is paid from initial reserve plus earlier ticket winnings, with no borrowing. The cumulative premium sum may be infinite.

## 3. Bare admissibility is not the transfer condition

The P4-S016 restart hedge D succeeds whenever d succeeds and the realized skipped-gain sum `sum e_i` is finite.

### Definition — coercive self-financing reserve

An R-admissible full-ticket account is coercive if on every completion run,

`sum_i e_i=infinity  =>  sup_n W_n=infinity.`

### Theorem 1 — coercive self-financing reserve theorem

Fix d, q=Save(d), and computable H. Suppose there is a finite computable rational R such that the canonical full-ticket account is R-admissible and coercive. Then there is one total nonnegative computable source martingale succeeding on every source x for which d succeeds on the logical least-fresh output.

#### Proof

Let J be the canonical ticket account. Admissibility makes J total and nonnegative; exact fair one-step pricing makes it a computable martingale. Let D be the settled P4-S016 truncated/restart martingale.

If `sum e_i=infinity`, coercivity makes J unbounded. If `sum e_i<infinity` and d succeeds, the settled restart-scale calculation leaves D at a positive multiplicative scale against q, and q tends to infinity on all sufficiently late prefixes of every d-success path. If a horizon-missed epoch never triggers, D copies q forever.

Hence `M=J+D` is one total nonnegative computable martingale on C(source) which succeeds whenever d succeeds. C is the settled computable fair-coin effective isomorphism, so P4-S001 transfers M to one computable martingale on the original source. No infinite optional projection or future-loss supremum is computed. QED.

## 4. Weakest condition established for this proof architecture

For the exact P4-S016 decomposition, D covers finite realized skipped gain. The only remaining case is divergent realized skipped gain, and the canonical ticket account covers exactly that case when it is unbounded.

Thus within the **canonical full-ticket plus settled restart-hedge architecture**, the established reserve condition is exactly:

1. global no-overdraft admissibility; and
2. success of the ticket account on every divergent-realized-loss run.

No absolute necessity is claimed for every possible computable transfer construction.

### Stronger easy form — computable coercivity cushion

A sufficient quantitative certificate is a computable nondecreasing unbounded function g on nonnegative rationals such that after each resolved ticket

`W_n >= g(E_n)`,

where `E_n=sum_{i<n}e_i`. A fixed retained fraction `W_n>=delta E_n` is a special case. The theorem itself needs no particular g or computable divergence rate.

## 5. P4-S016 is recovered

If P4-S016 holds with finite computable absolute premium budget B, take R=B. Writing `P_n=sum_{i<n}pi_i`,

`W_n=B+E_n-P_n >= E_n.`

So the account is admissible and divergent realized loss makes it unbounded. P4-S016 implies P4-S017.

## 6. Strict weakening for a fixed horizon/ticket stream

At an epoch with sentinel j, let a self-avoiding partial stake functional inspect fresh coordinates j+1 and j+2 in order, ignore the first value, then halt with all-in stake +1 if the second filler is 1 and diverge forever if it is 0.

A trigger branch consumes j and begins a new epoch; a nontrigger branch queries every coordinate except j forever. The scan is total, no-repeat, fair-coin preserving and globally k=2.

Let d hold on fillers and bet all capital on sentinel bit 1 whenever the trigger appears. Choose H=1. On a continuing run with r previous correct sentinel wins, the P4-S015 savings wrapper has savings r, active risk 1 and total capital r+1. The positive multiplicative gain at the next correct sentinel is

`ell_r=1/(r+1).`

At the last-chance node before the second filler, if the stored sentinel is 1 then filler 1 triggers with loss ell_r while filler 0 enters permanent nontriggering with loss 0, so `pi_r=ell_r/2`. If the stored sentinel is 0, the premium is zero.

Start J with R=1/2. Every positive-cost ticket either wins net ell_r/2 and reaches the next epoch, or loses ell_r/2 and enters a permanently nontriggering epoch after which all later premiums are zero. Thus J is globally nonnegative. Whenever cumulative payouts diverge, J grows as `1/2+E/2`, so it is coercive.

On the all-trigger run with every sentinel bit 1,

`sum_r pi_r=(1/2)sum_r 1/(r+1)=infinity.`

Thus the same H=1 ticket stream has no P4-S016 absolute premium-sum bound but does have a finite coercive self-financing reserve.

This is a strict separation **for a fixed horizon selector/ticket stream**. It is not claimed that the scan/martingale pair lacks a P4-S016 certificate after re-optimizing H. The example is not a new randomness-destruction witness.

## 7. Sharp obstruction — solvency can recycle capital forever

Modify the preceding functional so that after the same two fresh fillers it always halts with all-in stake +1, independent of the second filler. Keep H=1.

With stored sentinel bit 1, both second-filler children trigger with the same positive q-gain ell_r. Hence

`L_v(0)=L_v(1)=ell_r`

and `pi_r=ell_r`. The ticket costs ell_r and pays ell_r surely. With R=1 the ticket account is globally solvent and stays constant.

Along the path with every sentinel bit 1, q has capital r+1 at epoch r and `ell_r=1/(r+1)`, so realized skipped gain diverges harmonically while J stays bounded.

The restart hedge skips every positive sentinel update. Its relative scale is multiplied by

`(1+ell_r)^(-1)=(r+1)/(r+2)`,

exactly cancelling q's growth, so its absolute capital at epoch boundaries stays bounded. Thus J+D need not succeed.

This is the sharp obstruction to replacing P4-S016 by bare no-overdraft. It is only an obstruction to this ticket/restart architecture, not a universal martingale impossibility theorem, and the displayed path is not asserted computably random.

## 8. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source and d its successful output martingale. Fix any total computable H and q=Save(d).

P4-S016 already proves that along the sentinel-first completion of Y, `sum_i e_i=infinity`.

If a P4-S017 coercive reserve certificate existed, its canonical ticket account J would be a total nonnegative computable martingale and coercivity would make it unbounded on C(Y). But C is an everywhere-total computable fair-coin effective isomorphism, so P4-S001 preserves computable randomness from Y to C(Y). Contradiction.

Therefore P4-S011 admits no finite coercive self-financing full-ticket reserve certificate for any computable H.

P4-S017 does not prove that P4-S011 lacks every finite reserve satisfying bare no-overdraft. If such a merely solvent account exists, it must fail coercivity and stay bounded on C(Y) despite divergent realized skipped loss.

## 9. Successes and limits

Successful:

1. P4-S016 absolute premium summability is replaced, for the same ticket stream, by self-financing admissibility plus coercivity.
2. Earlier ticket payouts may fund later premiums.
3. The reserve is a total computable fair martingale under admissibility.
4. Divergent realized loss is handled by coercivity; finite realized loss by the settled restart hedge.
5. Their sum gives one completion martingale and P4-S001 gives one source martingale.
6. P4-S016 is recovered by taking initial reserve equal to its absolute premium budget.
7. A fixed-H example has divergent absolute premiums but a finite coercive reserve.
8. A deterministic-ticket example shows bare solvency is insufficient.
9. P4-S011 violates every coercive reserve certificate for every computable horizon selector.

Not claimed:

1. No absolute necessity theorem for all possible transfer constructions.
2. No equivalence between semantic coercivity and a computable coercivity modulus.
3. The fixed-H separation does not rule out a P4-S016 certificate using another horizon.
4. Bare admissibility alone is not ruled out for P4-S011.
5. No settled route is reopened.
6. No result for k>2.
7. No novelty, Gate-4, publication or outreach claim.

## Preserved boundaries

P4-S011's exact k=2 destroyer is unchanged.
P4-S015's weighted theorem and savings wrapper are unchanged.
P4-S016's envelope-free theorem is unchanged and recovered as a stronger bankroll hypothesis.
PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
DEF-0020 is unchanged.

## Next bounded question

The remaining gap is effectivity of coercivity itself. A bounded P4-S018 should test only whether coercivity can be replaced by a local computable reserve-floor / retained-surplus modulus, possibly arbitrarily slow, without restoring absolute premium summability; or whether cross-branch nonuniformity separates semantic coercivity from every such effective modulus. P4-S011 should again be checked explicitly.
