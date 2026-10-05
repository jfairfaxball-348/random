# P4-S006 close

Date: 2026-10-05
Session: P4-S006
Incoming checkpoint: b5881ac82a636c03c0b7c3ad9d6a36b5b47de123
Scope: selected CAND-01; k=2 canonical-sheet / moving-one-hole boundary only
Status: **COMPLETED**

## Result

P4-S006 determines the effective complexity of the canonical lexicographic two-sheet assignment induced by the compact collision relation.

For every exact k=2 map, the collision relation is effectively closed. The canonical nonminimum/upper source sheet is effective F-sigma (Sigma^0_2), the lower/minimum sheet is effective G-delta (Pi^0_2), and the double-fibre output set is effective F-sigma. The lexicographic minimum and maximum inverse selectors are uniform effective Baire-1 functions: they are pointwise limits of computable continuous selectors obtained from the descending clopen fibre approximants.

This information does not uniformly supply the missing computable-randomness transfer. Reusing the P4-S005 prefix-code map only as an internal calibration example, the canonical upper and lower sheet masses are
\[
\lambda(U)=\frac12-\frac14\sum_{e\in K}4^{-(e+1)},
\qquad
\lambda(L)=\frac12+\frac14\sum_{e\in K}4^{-(e+1)},
\]
so both are noncomputable. Therefore the canonical split need not yield computable component measures, and its Baire-1 selectors have no forced computable stabilization modulus. P4-S003's computable-sheet/isomorphism transfer and P4-S004's coherent stopped-pullback route therefore do not follow from the canonical Borel assignment alone.

The requested moving-sheet alternative was also tested. A single hidden/rotating mask bit has a precise collapse obstruction: once a later genuine bet reveals one coordinate that was masked by the current one-bit ambiguity, that revelation identifies the ambiguity bit and pre-reveals all other coordinates encoded in the same two-way cohort. Rotating to a fresh hole afterwards cannot undo those disclosures. Thus the SRC-0061 filler/pre-revealed-bet obstruction is still not globally resolved by a one-hole mask architecture.

No exact k=2 randomness-destruction witness is established. General k=2 forward computable-randomness preservation/failure remains unresolved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001 through P4-S005 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S006_VALIDATION.md.

Next: P4-S007, still bounded to k=2, on whether a delayed-coalescence inverse tree (allowing many finite-prefix candidates but at most two final fibre points) can either yield one computable martingale transfer or support an exact moving-sheet counterexample without the one-hole pre-revelation collapse.
