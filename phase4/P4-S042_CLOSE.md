# P4-S042 Close

Date: 2026-10-07
Session: P4-S042
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: f14170a6275cafc23d672b3598ace83f0258cd78

Scope: localization of raw-radius-one divergence for the sustained \(R_2=OH\) one-hole normalization target.

## Results

- proved the **first changed-coordinate contact theorem**: if a radius-one companion diverges on input \(n\) while the target computation halts, the finite target trace must query the changed virtual support;
- defined the finite target-trace **support-lasso** relation and proved that remote divergence reduces semantically to a local finite refutation, a local divergence, or a correct local dependency cycle;
- showed that minimal input/use/first-contact selection gives no well-founded descent to the block;
- retained the exact support cycles \(q_1\leftrightarrow q_2\), \(q_0\leftrightarrow q_2\), and the \(111\) two-cycle-with-tail / oriented-three-cycle alternatives;
- constructed an explicit computable syntactically self-avoiding finite-use countermodel with remote divergence in all three raw directions but local status vector
  \[
  (A_0,B_1,B_2),
  \]
  proving that remote partiality can coexist with complete P4-S040 local decisiveness;
- proved that the P4-S041 pairwise status law is not strengthened by remote divergence traces through finite evidence alone;
- obtained no permitted uniform target-equivalent localization compiler from the committed data;
- proved the **persistent local Case-C necessity theorem**:
  \[
  X\in OH
  \Longrightarrow
  \text{infinitely many local Case-C block-direction pairs},
  \]
  and hence some fixed raw direction is Case C on infinitely many blocks;
- did **not** prove \(X\in OH\), did **not** prove an unconditional \(X\notin OH\), and did **not** prove OH non-invariance or \(R_2\subsetneq OH\).

## Records

- phase4/P4-S042_MATHEMATICS.md
- phase4/P4-S042_VALIDATION.md
- phase4/P4-S042_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S043**, on recurrent fixed-direction local Case C and whether the pairwise raw-adjacent laws let a finite family of one-hole scans progress without waiting for the recurrent divergent direction.
