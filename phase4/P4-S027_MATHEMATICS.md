# P4-S027 — bare bankroll for the P4-S011 destroyer

Date: 2026-10-06
Session: P4-S027
Incoming checkpoint: `4bd698d8b0402bb03d5beabe01766d263476eb31`
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh P4-S011 / P4-S016–P4-S017 ticket architecture only

Result: **YES. THE P4-S011 WTT WITNESS MAY BE PUT IN A GLOBALLY USE-CLIPPED NORMAL FORM. A COMPUTABLE HORIZON THAT FIRST EXHAUSTS THAT FINITE USE FRONTIER MAKES EVERY POSITIVE POSTMISS P4-S016 LAST-CHANCE TICKET DETERMINISTIC: ITS FAIR PREMIUM EQUALS ITS CERTAIN PAYOUT. SINCE EVERY POSITIVE MULTIPLICATIVE SKIPPED GAIN IS AT MOST 1, RESERVE R=1 MAKES THE CANONICAL FULL-TICKET ACCOUNT GLOBALLY ADMISSIBLE ON EVERY SENTINEL-FIRST COMPLETION BRANCH. ON THE P4-S011 TARGET THE TOTAL PREMIUM AND REALIZED SKIPPED LOSS STILL DIVERGE WHILE THE TICKET CAPITAL STAYS CONSTANT, SO COERCIVITY, LOSS-PROPERNESS AND ALL LATER TRANSFER CERTIFICATES STILL FAIL EXACTLY AS SETTLED.**

## Authority, uniqueness and scope

Live `main` matched the requested incoming checkpoint exactly before substantive work. The incoming tree contained P4-S001 through P4-S026 and no P4-S027 mathematics, close or validation record, so P4-S027 was unused.

P4-S001 through P4-S026 and required CAND-01 authority were read. P4-S005 through P4-S026 are treated as settled. P4-S011 and P4-S015 through P4-S026 are preserved.

This session tests only the repeatedly deferred bare no-overdraft question for the canonical P4-S016/P4-S017 full-ticket account attached to the P4-S011 destroyer. It assumes no coercivity, loss-properness, searchable loss bars, tail modulus or boundary certificate.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No result is claimed for k>2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained P4-S011 and ticket data

P4-S011 fixes a computably random binary sequence Y and a weak-truth-table autoreduction M. On input j the target computation M^Y(j) halts with value Y(j), does not query j, and has a computable use bound. The least-fresh scan withholds the current sentinel j, reveals fresh non-sentinel fillers until a binary halt is finitely visible, then consumes j. It is everywhere total, no-repeat, fair-coin preserving and globally k=2. On Y every epoch triggers correctly and the P4-S011 output martingale d succeeds.

P4-S015 replaces d by q=Save(d), without increasing absolute fractional stakes. For every logical sentinel bit b,
[
0le ell_q(	au,b)le 1,
]
where (ell_q) is the positive multiplicative gain lost if that sentinel update is skipped.

P4-S016 fixes a computable finite horizon selector H. After a horizon miss, at each unresolved state v and before the next fresh filler is drawn, it defines
[
L_v(a)=
egin{cases}
ell_q(	au_{v,a},b),&	ext{if child }a	ext{ makes the logical sentinel trigger next},\
0,&	ext{otherwise,}
end{cases}
]
and the exact fair one-step premium
[
pi(v)=rac{L_v(0)+L_v(1)}2.
]

P4-S017 starts the canonical full-ticket account from reserve R and buys every such ticket. Bare admissibility means that no prescribed purchase ever makes the account negative on any sentinel-first completion branch.

## 2. Global use-clipped normal form for the wtt witness

The P4-S011 conversion did not need the wtt use bound, but the bound is available from SRC-0067 / SRC-0068 / THM-0076.

Let u(j) be a total computable bound for the use of the target autoreduction computation. Replace M, if necessary, by the equivalent oracle machine (widehat M) which simulates M on input j but permanently abandons that prediction if the simulation attempts to query j or any oracle coordinate outside a fixed strict computable cap
[
U(j)>u(j).
]

On Y this clipping never changes the computation: M^Y(j) uses only coordinates below its computable use bound and never queries j. Thus
[
widehat M^Y(j)=Y(j)
]
for every j.

On siblings the clipping only converts an out-of-cap attempted computation into another permanently nontriggering computation. The P4-S011 scan proof is unchanged: the scan itself remains total by continuing to emit fresh non-sentinel fillers; a permanently nontriggering epoch omits exactly its sentinel; and an all-trigger run consumes every coordinate. Hence the globally use-clipped witness still gives an exact everywhere-total, fair-coin-preserving, global-k=2 P4-S011 destroyer with the same computably random target Y and the same all-trigger correct-prediction target analysis.

This is a normal-form choice inside the settled existential P4-S011 witness, not a truth-table totality assumption. (widehat M) may still diverge forever on sibling oracles. P4-S027 does not claim that every arbitrary off-target implementation of a wtt reduction, before this harmless clipping, has the bankroll property.

## 3. The use-exhausting horizon

At a reachable epoch state s let j be its current sentinel and R_s the finite set of source coordinates already logically queried.

Define
[
H_U(s)
=
1+
igl|{n<U(j): n
e j, n
otin R_s}igr|.
]

This is a total computable finite horizon selector.

The filler rule always queries the least fresh coordinate different from j. Therefore, after the first
[
igl|{n<U(j): n
e j, n
otin R_s}igr|
]
new fillers, every possible non-sentinel oracle coordinate below U(j) has been revealed. The harmless extra filler in H_U avoids any zero-horizon convention and is necessarily outside the still-missing bounded-use set.

Consequently, if the epoch misses H_U(s), every later computation of (widehat M(j)) has all oracle answers it can ever inspect already fixed. A later trigger may still appear because more machine simulation time has elapsed, but **no newly drawn filler bit can affect whether it appears or what binary prediction it returns**.

This is the key distinction from P4-S013 reachable-sentinel totality. The epoch may remain branchwise avoidable forever; H_U does not decide halting and does not give a finite trigger deadline.

## 4. Post-horizon tickets are deterministic

Consider any unresolved postmiss state v under H_U, immediately before its next fresh filler.

The hypothetical filler children 0 and 1 agree on every oracle coordinate below U(j), and (widehat M(j)) never reads the new filler coordinate. The deterministic finite simulation schedule at the two children is therefore identical as far as trigger visibility and prediction value are concerned.

Hence exactly one of the following holds:

1. neither child makes the sentinel trigger next, so
   [
   L_v(0)=L_v(1)=0,qquad pi(v)=0;
   ]
2. both children make the sentinel trigger next with the same prediction and the same pre-sentinel q-capital, so for one computable (ell_vin[0,1]),
   [
   L_v(0)=L_v(1)=ell_v,qquad pi(v)=ell_v.
   ]

Thus every positive last-chance ticket is a deterministic fair ticket: it costs (ell_v) and pays (ell_v) on either filler child.

There is no one-sided sibling loss after the use frontier. The only possible nonzero ticket in a missed epoch is the final one immediately before a delayed trigger; if the computation never triggers, all later ticket prices are zero.

## 5. Reserve one is globally admissible

Take R=1.

Inductively suppose the resolved ticket-account capital is 1 before an unresolved postmiss state v.

If (pi(v)=0), nothing is spent and the capital remains 1.

If (pi(v)=ell_v>0), then (0<ell_vle1). The account can pay the full premium without borrowing, leaving cash (1-ell_vge0). The ticket then pays (ell_v) on either child, restoring resolved capital exactly to 1.

Therefore on **every** sentinel-first completion branch and at **every** ticket node, the canonical full-ticket account remains nonnegative. In fact its resolved capital is identically 1.

### Theorem — bare bankroll exists for the normalized P4-S011 destroyer

For the globally use-clipped P4-S011 wtt witness, the total computable horizon selector H_U above and finite reserve R=1 make the canonical P4-S016/P4-S017 full-ticket account globally admissible on every sentinel-first completion branch.

Accordingly the negative alternative requested for P4-S027 does not occur: no sibling family can force an arbitrarily large premium deficit for this H, because every positive post-horizon premium is returned with certainty before another positive ticket can be required.

## 6. Explicit consistency with the P4-S011 target path

Let C(Y) be the settled sentinel-first completion of the P4-S011 computably random target.

P4-S016 proved, for **every** computable horizon selector, that the cumulative realized positive skipped gain on C(Y) diverges:
[
sum_i e_i=infty.
]
That applies in particular to H_U.

For H_U, every positive ticket is deterministic, so
[
pi_i=e_i
]
on every realized positive ticket. Therefore
[
sum_ipi_i=sum_i e_i=infty,
]
while the full-ticket account has
[
W_i=1
]
after every resolved ticket.

So P4-S027 is exactly consistent with every settled exclusion:

- **P4-S016:** there is no finite absolute pathwise premium-sum budget; the premium sum diverges on C(Y).
- **P4-S017:** the account is bare-admissible but not coercive; realized skipped loss diverges while ticket capital stays bounded.
- **P4-S018 / P4-S019:** for any K>1, C(Y) stays below K while E grows without bound, so b(K)=infinity; loss-properness and every coercivity modulus fail.
- **P4-S020 through P4-S026:** no later searchable-bar, scale-tail, finite-limit or boundary-complete transfer hypothesis is recovered.
- **P4-S011:** the ticket account does not succeed on C(Y), so no computable source martingale contradiction is produced. The exact k=2 non-conservation theorem is unchanged.

Bare admissibility is therefore a pure solvency fact, not a preservation mechanism.

## 7. What changed, and what did not

Established in P4-S027:

1. The wtt use information unused by the P4-S011 destroyer conversion can be used for bankroll control.
2. A globally use-clipped normal form preserves the P4-S011 target and exact global-k=2 scan proof.
3. A computable horizon can exhaust the finite dependency frontier before postmiss insurance begins.
4. Beyond that frontier every positive P4-S016 ticket is deterministic, with premium equal to certain payout.
5. R=1 globally funds the full canonical ticket stream.
6. On the computably random target, premiums and payouts both diverge while account capital remains constant.

Not claimed:

1. Bare admissibility is not sufficient for computable-randomness preservation.
2. No coercivity, loss-properness or searchable-bar condition is obtained.
3. No theorem is asserted for arbitrary P4-S012 partial predictors lacking an effectively exhaustible dependency frontier.
4. No theorem is asserted for every unnormalized off-target implementation of a wtt oracle program.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S005 through P4-S026 remain settled.

P4-S011's exact k=2 destroyer is unchanged in mathematical content; P4-S027 only records a harmless globally use-clipped representative of its wtt witness and a bankroll property of that representative.

P4-S015 through P4-S026 are preserved. In particular, all of their transfer hypotheses remain strictly stronger than the bare solvency established here.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## Next bounded question

The smallest remaining local question is whether the use-exhaustion mechanism is the exact structural reason for bare admissibility.

A bounded P4-S028 should stay strictly at k=2 and test only the P4-S012-style weakening: whether a computable per-epoch finite dependency frontier, weaker than a wtt autoreduction presentation but strong enough that all possible later trigger decisions are independent of future filler bits once the frontier is exhausted, is sufficient for a finite globally admissible full-ticket reserve. If that effective frontier is absent, test whether one can build an exact global-k=2 sibling family in which every computable horizon leaves one-sided future trigger opportunities that force unbounded reserve demand. Preserve the P4-S011 destroyer and all P4-S015 through P4-S027 boundaries.
