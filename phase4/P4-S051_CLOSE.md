# P4-S051 Close

Date: 2026-10-08
Session: P4-S051
Incoming checkpoint: 96bfc1d1cfb351e14eb874202ff1858b0e0709aa
Status: **COMPLETED / VALIDATED**
Scope: positive multi-square reset-free escrow and effective capture limits.

## Mathematics established
1. Two finite positive raw-square refutations at the same unread old s, opposite old rows, and two distinct unread future targets t,u exclude one joint future target tuple.
2. A sequential rational fair 4/3 hedge queries only fresh t,u, not s. This is a *reset-free* completed gain. Same-target opposite-row exclusions at one future value give a single-target factor 2.
3. Exact finite projection criterion: for m fresh targets and refuted sets E_i, a strict universal target-only fair payoff exists precisely when some future tuple v has no compatible old value. The flat fair multiplier is 2^m/(2^m-r) when r target tuples are excluded.
4. After consuming t, a prior Ref(a,beta) orients old s only if observed t equals beta. Otherwise a single refutation supplies no old-bit prediction. Later positive evidence can force a fresh u only with correct old-row alignment.
5. An explicit finite-window two-square escrow controller with bounded symmetric simulations, support/sweep queries, and mandatory timeout release is everywhere total, no-repeat, fair-coin preserving, and globally at most one-hole despite temporarily protecting three raw coordinates.
6. Infinite *executed* positive exits by a single combined reset/escrow policy imply X not in OH.
7. The P4-S008 fixed-sentinel theorem sharpens the limit: because X is computably random, infinite profitable reset-free hedges on one forever-unread s are impossible. An infinite same-source destroyer still needs effective repeated turnovers of old sentinels.

## Not established
No proof of infinitely many effective opposed-row fresh captures or certified old-sentinel turnovers on the committed X. No proof X in OH or X not in OH, no R_2=OH resolution, no OH non-invariance or strict separation.

## Records
- phase4/P4-S051_MATHEMATICS.md
- phase4/P4-S051_VALIDATION.md
- phase4/P4-S051_CLOSE.md

PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Retain MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.
Recommended next bounded session: **P4-S052**, test finite escrow gains coupled to a positively certified old-sentinel turnover; avoid extrapolating fixed-sentinel success or certificate-time bounds.
