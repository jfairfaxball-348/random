# P4-S006 validation

Date: 2026-10-05
Incoming baseline: b5881ac82a636c03c0b7c3ad9d6a36b5b47de123
Result: **PASS** for uniqueness, k=2 scope discipline, effective-Borel calculations, canonical-selector checks, one-hole obstruction accounting, authority synchronization target and preserved novelty/convention guards.

Checks:
- live main matched the incoming baseline before substantive work;
- repository search found no committed P4-S006 record on the incoming checkpoint;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- CAND-01's exact formulation is unchanged;
- P4-S001 through P4-S005 are not edited;
- P4-S005's crossing-measure non-effectivity result is treated as settled and is not re-proved or challenged;
- R_F={(x,z):F(x)=F(z)} is effectively closed because equality of all finite output prefixes is a computable-clopen approximation;
- K_rho=F([rho]) is uniformly computably compact/effectively closed;
- the canonical upper sheet satisfies U=union_rho ([rho1] intersect F^{-1}(K_{rho0})), giving a uniform effective F-sigma description;
- the lower sheet is its effective G-delta complement;
- the double-fibre output set is union_rho K_{rho0} intersect K_{rho1}, hence effective F-sigma;
- the clopen fibre approximants A_m(y) are nested and their lexicographic minima/maxima converge pointwise to the canonical fibre extrema, giving uniform effective Baire-1 selectors;
- P4-S002's collision example remains the guard that these selectors need not be continuous/computable;
- in the P4-S005 internal calibration map, each activated block removes exactly q_e/4 from the canonical upper sheet, so lambda(U)=1/2-(1/4)sum_{e in K}q_e and lambda(L)=1/2+(1/4)sum_{e in K}q_e;
- the already-established base-4 coding therefore makes both canonical sheet masses noncomputable;
- no inference is made from that noncomputable mass to randomness destruction; the P4-S005 map remains in the positive computable-clopen-split regime;
- the canonical Borel split is therefore not misrepresented as providing computable component measures, an a.e.-computable inverse pair, a stabilization modulus or one coherent source martingale;
- the one-hole/rotating-mask lemma is limited to that architecture: revealing one masked coordinate determines the common ambiguity and pre-reveals all other coordinates in the same two-way cohort;
- no claim is made that the one-hole lemma rules out more complex delayed-coalescence k=2 constructions;
- SRC-0061 is not claimed to have been converted to finite fibres;
- no exact k=2 computable-randomness destroyer is asserted;
- general k=2 preservation/failure remains unresolved;
- no result is asserted for k>2;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- the pre-Phase-4 Gate-3 guard remains historical and unchanged in meaning;
- DEF-0020 and catalogue records are unchanged;
- Gate 4 is not reviewed and Phase 5 remains CLOSED.

This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
