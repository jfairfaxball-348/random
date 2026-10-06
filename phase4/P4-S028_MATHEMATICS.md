# P4-S028 — finite dependency frontiers and bare reserve demand

Date: 2026-10-06
Session: P4-S028
Incoming checkpoint: e94ff739fc2fbc77f519ce0afb0458624ebfc673
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh P4-S012 / P4-S016–P4-S017 ticket architecture only

Result: **P4-S027'S WTT USE BOUND IS NOT THE ESSENTIAL BANKROLL HYPOTHESIS. A COMPUTABLE PER-EPOCH FINITE DEPENDENCY FRONTIER WHOSE EXHAUSTION MAKES ALL LATER TRIGGER DATA INDEPENDENT OF FUTURE FILLER VALUES SUFFICES: A COMPUTABLE FRONTIER-EXHAUSTING HORIZON MAKES EVERY POSITIVE POSTMISS LAST-CHANCE TICKET DETERMINISTIC, SO RESERVE R=1 IS GLOBALLY ADMISSIBLE. SUCH A FRONTIER IS NOT FORCED BY THE P4-S012 PARTIAL-PREDICTOR SETTING. IN FACT ONE EXACT GLOBAL-k=2 LEAST-FRESH SCAN HAS, AFTER EVERY FINITE HORIZON, AN INFINITE AVOIDING SIBLING ON WHICH EACH LATER FILLER LEAVES A ONE-SIDED ALL-IN TRIGGER OPPORTUNITY. THE CANONICAL FULL TICKET THEN COSTS 1/2 AND PAYS 0 REPEATEDLY, SO NO FINITE RESERVE IS GLOBALLY ADMISSIBLE FOR ANY FINITE COMPUTABLE HORIZON SELECTOR. P4-S011 REMAINS ON THE POSITIVE SIDE BECAUSE P4-S027 SUPPLIES ITS FRONTIER.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work. The incoming tree contained P4-S001 through P4-S027, no P4-S028 mathematics, close or validation record, and commit search returned no P4-S028 commit. P4-S028 was therefore unique.

P4-S001 through P4-S027 and the required CAND-01 authority were read. P4-S005 through P4-S027 are treated as settled. P4-S011 and P4-S015 through P4-S027 are preserved.

This session tests only the structural bankroll boundary exposed by P4-S027. It does not reopen any transfer, loss-properness, searchability or effective-topology route.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No result is claimed for k>2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained ticket data

Fix a P4-S012 least-fresh self-avoiding partial predictor or stake functional. At a reached epoch state s, let j be the withheld sentinel and R_s the finite set of source coordinates already queried by the logical scan.

Fix a nonnegative rational output martingale d which is flat on fillers and bets only when the predictor/stake becomes visible, and let q=Save(d) be the settled P4-S015 savings wrapper. Then q is also flat on fillers and every positive multiplicative skipped-sentinel gain ell is at most 1.

For a computable finite horizon H, P4-S016 defines at every unresolved postmiss state v, immediately before the next fresh filler, the child losses
\[
L_v(a)=
\begin{cases}
\ell_q(\tau_{v,a},b),&\text{if filler child }a\text{ makes the sentinel trigger next},\\
0,&\text{otherwise,}
\end{cases}
\]
and exact fair premium
\[
\pi(v)=\frac{L_v(0)+L_v(1)}2.
\]

P4-S017's canonical full-ticket account buys every such ticket. Bare admissibility asks only that some finite reserve prevent overdraft on every sentinel-first completion branch.

## 2. Finite dependency frontier

### Definition — computable epoch dependency frontier

A computable finite dependency frontier for the least-fresh process is a total computable map D on reachable epoch states such that:

1. D(s) is a finite set of non-sentinel source coordinates;
2. if an epoch remains unresolved until every coordinate in D(s) has been revealed, then from that point onward all later trigger data for the current sentinel — whether a valid trigger becomes visible at each later scan step and, when it does, its prediction/stake value — are independent of every future filler value.

Additional simulation time may still reveal a trigger, and the epoch may still diverge forever. The condition is only value-independence after the finite frontier has been exhausted.

This is weaker data than the P4-S027 wtt presentation. No global use bound depending only on input j is assumed, no off-target totality is assumed, and D may depend on the full reachable epoch state. The hypothesis says only that the value-sensitive part of the current epoch has a computably known finite frontier.

## 3. A frontier-exhausting horizon is computable

Let
\[
m(s)=\max(D(s)\cup\{j\}).
\]
Choose
\[
H_D(s)
=
1+
\bigl|\{n\le m(s):n\ne j,\ n\notin R_s\}\bigr|.
\]

The least-fresh filler rule queries missing non-sentinel coordinates in increasing order. Hence, if the epoch survives to this horizon, every member of D(s) has been exposed. The extra filler is harmless and avoids a zero-horizon convention.

Thus H_D is total, computable and finite. It does not decide whether the epoch will ever trigger.

## 4. Frontier exhaustion makes all positive tickets deterministic

Fix an unresolved postmiss state v under H_D and consider its two next-filler children.

The frontier condition says that the new filler value cannot alter the later trigger decision or the prediction/stake value. Because d and q are flat on fillers, the two children also have the same pre-sentinel q-capital whenever they trigger.

Therefore exactly one of the following occurs:

- neither child triggers next, so L_v(0)=L_v(1)=0; or
- both children trigger next with one common positive skipped gain ell_v, so
  \[
  L_v(0)=L_v(1)=\ell_v,\qquad \pi(v)=\ell_v.
  \]

Every positive last-chance ticket is therefore deterministic. Since 0<ell_v<=1, reserve R=1 pays it and the certain payout restores the resolved account to 1.

### Theorem 1 — finite-frontier bare admissibility

Every P4-S012 least-fresh ticket stream with a computable finite dependency frontier has a total computable frontier-exhausting horizon H_D for which the canonical P4-S016/P4-S017 full-ticket account is globally admissible with reserve R=1.

No coercivity, loss-properness, absolute premium summability, searchable bar or trigger deadline is used.

## 5. P4-S012 does not force a finite frontier

The P4-S012 hypothesis is target-side and allows genuinely unbounded value-sensitive sibling dependence.

Consider the following self-avoiding partial predictor P.

- On input 0, query coordinates 1,2,3,... in order until the first value 1 is found; then halt with prediction 1. If every queried value is 0, diverge forever.
- On every input j>0, halt immediately with prediction 1.

The input-0 computation never queries coordinate 0.

At the first least-fresh epoch the sentinel is 0 and the fillers are exactly coordinates 1,2,3,... . After any finite string of zero fillers, the next unseen filler still matters: value 1 makes the prediction visible, while value 0 leaves the epoch unresolved.

Hence no finite D at the initial epoch can have the frontier property. Given any proposed finite D, set every coordinate in D to 0 and choose a later coordinate outside D; changing that later value from 0 to 1 changes the future trigger behavior.

So a computable finite dependency frontier is not forced by P4-S012 partial prediction.

## 6. Exact global-k=2 reserve-demand witness

Use the least-fresh scan generated by P above.

### Lemma 2 — totality, fair coin and global fibre bound

At every output stage the scan queries one fresh coordinate.

If the first epoch never triggers, fillers query every positive coordinate and omit only sentinel 0. The resulting output fibre has exactly two points, differing only at source coordinate 0.

If the first epoch triggers, sentinel 0 is consumed. Every later predictor halts immediately, so every later least-unqueried sentinel is consumed. The scan is exhaustive and the output fibre is a singleton.

Thus the induced map is everywhere total, computable, no-repeat, fair-coin preserving and globally fibre-bounded by two.

This is an exact P4-S012 global-k=2 scan. It is a bankroll boundary witness, not a new computable-randomness destroyer.

### Lemma 3 — every finite horizon leaves repeated one-sided trigger risk

Let d start with capital 1, remain flat on fillers, and at every visible prediction 1 bet all capital on sentinel bit 1. Let q=Save(d).

Consider the sentinel-first completion branch on which the stored first sentinel bit is
\[
b=x(0)=1
\]
and every positive-coordinate filler bit is 0.

The logical first epoch never triggers. Until a sentinel wager is actually taken, d and q remain at capital 1.

Let H be any finite horizon selector and let h=H(s_0) at the initial epoch. After h zero fillers the horizon is missed. At every later unresolved postmiss node v:

- next filler 1 would reveal the first 1, make the sentinel trigger next, and the skipped positive q-gain would be 1;
- next filler 0 leaves the epoch unresolved.

Therefore
\[
L_v(0)=0,\qquad L_v(1)=1,\qquad \pi(v)=1/2.
\]

On the displayed all-zero continuation the actual payout is 0. The canonical full-ticket account therefore loses 1/2 at every visited postmiss node and receives no replenishing payout.

### Theorem 4 — no finite reserve works for any computable horizon

Fix any total computable finite horizon selector H and any finite reserve R.

On the branch above, after N postmiss zero fillers the cumulative net ticket deficit is N/2. Choosing N>2R makes a prescribed full premium unaffordable.

Hence the canonical P4-S016/P4-S017 full-ticket account is not R-admissible.

The same scan defeats every finite H and every finite R. Computability of H is not used beyond the programme setting; finiteness is enough.

This is the exact sibling family requested by P4-S028: every finite horizon leaves arbitrarily many one-sided future trigger opportunities before any possible replenishment.

## 7. What this proves, and what it does not

P4-S028 establishes a sharp structural sufficiency/separation statement.

1. A computable finite dependency frontier is sufficient for P4-S027-style reserve-one admissibility.
2. The wtt use bound itself is not essential.
3. P4-S012 does not force such a frontier.
4. Without a frontier, exact global-k=2 scans can have arbitrarily deep one-sided trigger risk and unbounded reserve demand.
5. Absence of a frontier is not claimed, by itself, to imply reserve failure for every partial predictor. Small or decaying stakes could in principle make the remaining one-sided exposure affordable. The theorem is an existence separation, not a necessity theorem.

The last point is important: P4-S028 does not identify finite frontier with bare admissibility. It identifies finite frontier as a clean structural sufficient condition and shows that the broader P4-S012 class genuinely contains the opposite reserve behavior.

## 8. Explicit P4-S011 check

P4-S011 remains on the positive side.

P4-S027 globally clips its wtt autoreduction witness to a computable use cap U(j). At each reachable epoch, the still-possible oracle dependencies below U(j) form a computable finite dependency frontier in the sense of Section 2.

Therefore Theorem 1 recovers the P4-S027 horizon and reserve R=1.

On the computably random P4-S011 target, cumulative positive premiums and payouts still diverge while the ticket account stays exactly 1. Thus:

- P4-S016 absolute premium summability still fails;
- P4-S017 coercivity still fails;
- P4-S019 loss-properness still fails under admissibility;
- P4-S020 through P4-S026 searchability/effective-tail hypotheses are not restored;
- P4-S011's exact k=2 non-conservation theorem is unchanged.

The new reserve-demand witness does not modify or replace P4-S011.

## 9. Successes and limits

Successful:

1. Isolated a computable per-epoch finite dependency frontier as the exact data used by P4-S027's solvency proof.
2. Proved a computable frontier-exhausting horizon exists.
3. Proved all positive postmiss tickets are deterministic after frontier exhaustion.
4. Proved reserve R=1 is globally admissible.
5. Proved the P4-S012 partial-predictor setting does not force a finite frontier.
6. Built one exact total, fair-coin-preserving global-k=2 scan with no initial frontier.
7. Proved every finite horizon leaves infinitely many one-sided all-in trigger opportunities on one completion sibling.
8. Proved the canonical ticket deficit is N/2 after N such losses, so no finite reserve is globally admissible.
9. Checked P4-S011 explicitly and recovered P4-S027.

Not claimed:

1. No necessity of finite frontiers for bare admissibility.
2. No new computable-randomness destroyer.
3. No reopening of P4-S015 through P4-S027 transfer boundaries.
4. No result for k>2.
5. No novelty, Gate-4, publication or outreach claim.

## Preserved boundaries

P4-S005 through P4-S027 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015 through P4-S027 are preserved exactly.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

## Next bounded question

P4-S029 should stay strictly at k=2 and test only whether the P4-S028 finite dependency frontier is necessary for bare admissibility. In the P4-S012 least-fresh partial-stake/predictor class, try to construct an exact no-frontier scan with genuinely one-sided trigger opportunities at arbitrarily late fillers but a finite globally admissible canonical full-ticket reserve for some computable horizon, for example by making the positive skipped gains decay effectively. If such a separation fails under a natural nondegeneracy hypothesis, state and prove the narrow necessity theorem. Compare explicitly with P4-S028's constant-1/2 deficit witness and P4-S011's deterministic frontier case.