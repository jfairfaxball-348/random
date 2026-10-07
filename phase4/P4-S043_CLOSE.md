# P4-S043 Close

Date: 2026-10-07
Session: P4-S043
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: 9027605cad65de83cca6ae23e7986cf41ceb9424

Scope: recurrent fixed-direction local Case C and asynchronous harvesting for the sustained \(R_2=OH\) one-hole normalization target.

## Results

- proved that the P4-S041 pairwise status implications are the complete local finite-table law and classified exactly 14 realizable A/B/C status triples;
- obtained the exact fixed-\(C_i\) pattern lists:
  \[
  C_0:\ CAA,CAC,CCA,CCC,
  \]
  \[
  C_1:\ ACA,ACB,ACC,CCA,CCC,
  \]
  \[
  C_2:\ AAC,ABC,ACC,CAC,CCC;
  \]
- proved an **asynchronous one-role extraction theorem** strictly extending P4-S040: a selected role may close immediately on its own positive A/B certificate and restart without waiting for the other two directions;
- proved that a selected Case C is an absorbing target epoch for this wait-for-own-status architecture;
- isolated the distinction between ambient raw-block recurrence and recurrence on a scan's endogenously selected fresh-block subsequence;
- proved that guaranteeing finite abandonment of every unresolved sentinel makes the scan exhaustive, returning it to the \(k=1\) computable-randomness-preserving regime;
- constructed, for every fixed recurrent C direction and every prescribed finite family of asynchronous wait policies, a computable finite-use syntactically self-avoiding structural countermodel on \(0^\omega\) with:
  - the chosen C direction on every block,
  - no triple-C block,
  - at least one visible Case-A direction on every block,
  - and every member of the finite family eventually trapped by a selected C;
- checked the special \(C_0\), \(C_1\wedge B_2\), \(C_2\wedge B_1\), mixed A/C and triple-C cases separately;
- did **not** prove recurrent triple Case C is necessary for \(X\in OH\);
- did **not** prove \(X\in OH\) or an unconditional \(X\notin OH\);
- did **not** prove OH non-invariance or \(R_2\subsetneq OH\).

## New boundary

The remaining obstruction is an **online selector / fresh-block reachability problem**.

A/B witnesses are positively visible once the corresponding raw role has been opened, but role choice precedes that evidence. Indefinite waiting preserves the one-hole resource and exposes the scan to an absorbing C. Guaranteed finite abandonment avoids the trap only by making the scan exhaustive.

A finite family of pure waiting policies does not bridge this gap.

## Records

- phase4/P4-S043_MATHEMATICS.md
- phase4/P4-S043_VALIDATION.md
- phase4/P4-S043_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S044**, on the online selector / fresh-block reachability obstruction: determine whether the actual wtt use structure yields a computable fresh-lane selector hitting infinitely many nontriple Case-A witnesses, or whether every computable role policy can be forced to become C-trapped or to consume those witnesses as support before they become sentinels.
