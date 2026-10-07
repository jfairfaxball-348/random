# P4-S044 Close

Date: 2026-10-07
Session: P4-S044
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: dfd593bd3d0e2bc68d9b2e2097b31c5dbc443c17

Scope: online selector / fresh-block reachability under the actual wtt use horizon for the sustained \(R_2=OH\) one-hole normalization target.

## Results

- computed a uniform local **source-value horizon** from the committed wtt use cap:
  \[
  V(b)=\max_{r<3}U(3b+r),
  \qquad
  h(b)=\max\left\{b+1,\left\lceil V(b)/3\right\rceil\right\};
  \]
- proved every raw-adjacent A/B positive certificate at block \(b\) uses source values only below that horizon, even when a sibling computation diverges;
- separated finite source-value closure from unbounded certificate time;
- proved a fixed-future-reservation dichotomy: on a no-event continuation a globally one-hole scan cannot keep both the current sentinel and a different fixed future sentinel permanently unread;
- showed moving transient reservations are globally legal, but the actual next target is selected by certificate time;
- defined horizon intervals
  \[
  I_b=[b,h(b))
  \]
  and proved finitely many computable horizon lanes exist exactly when their overlap depth is uniformly bounded;
- proved bare wtt finiteness does not force this bounded-overlap condition;
- recorded that countably many lanes are always computably available but do not justify countable pigeonhole;
- isolated the exact conditional lane-success criterion on the scan's event-time-selected targets rather than on ambient lane recurrence;
- showed zero-stake support blocks need not preserve a raw sentinel because a legal future \(u_2\) support query can force complete raw-block consumption;
- proved a finite transient multi-sentinel race still has a no-rate abandonment obstruction: on the all-C branch all but at most one candidate must be consumed, and finite-use A certificates can be delayed beyond those finite consumption times;
- revisited recurrent \(C_0\) and the asymmetric \(ACB/ABC\) patterns and found the same certificate-time reachability obstruction;
- built a computable finite-use syntactically self-avoiding structural model on \(0^\omega\) with genuine horizon
  \[
  h(b)=2b+2,
  \]
  unbounded overlap, recurrent nontriple \(C_0\), visible A witnesses, and finite-family selector/race failure;
- sharpened the surviving source-side condition: if \(X\in OH\), no computable moving-reservation/role selector may eventually avoid C while selecting A infinitely often on infinitely many completed epochs;
- did **not** prove \(X\in OH\) or an unconditional \(X\notin OH\);
- did **not** prove OH non-invariance or \(R_2\subsetneq OH\).

## New boundary

The wtt use bound solves **source-value reachability** but not **certificate-time reachability**.

After the finite use window is exhausted, A/B status may still become visible after arbitrarily long computation. A globally one-hole scan must keep emitting fresh source queries during that delay. It cannot simultaneously preserve the current possible permanent hole and one fixed future target forever.

Thus the next missing resource is an effective **selector-thickness / certificate-time regularity** principle strong enough to force recurrent ambient A witnesses onto one computable moving-reservation selector's reached subsequence.

## Records

- phase4/P4-S044_MATHEMATICS.md
- phase4/P4-S044_VALIDATION.md
- phase4/P4-S044_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S045**, on certificate-time selector thickness after source-value closure: formalize moving-reservation selectors and test whether the actual computably random wtt-autoreducible source forces any recurrence/thickness property that defeats delayed-certificate evasion.
