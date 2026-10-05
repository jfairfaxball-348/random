# P4-S007 validation

Date: 2026-10-05
Incoming baseline: b25136e24991cb988dc1186567a5639a3c41b38c
Result: **PASS** for uniqueness, k=2 scope discipline, coherent-tree calculations, finite-injury bounds, generalized collapse accounting and preserved authority/convention guards.

Checks:
- live main matched the incoming baseline before substantive work;
- repository search found no committed P4-S007 record on the incoming checkpoint;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- CAND-01's exact formulation is unchanged;
- P4-S001 through P4-S006 are not edited;
- P4-S005's crossing-measure non-effectivity result is treated as settled and not revisited;
- P4-S006's effective-Borel/Baire-1 sheet result and one-hole collapse are preserved;
- c(n) is obtained from the P4-S003 decidable search and made nondecreasing with c(n)>=n;
- P_n(y)=C_{n,c(n)}(y) is nonempty, has size at most two, and projections from level n+1 land inside level n;
- every actual fibre point gives a skeleton path;
- every skeleton path maps to y, using c(n)->infinity and the computable forward-use bound;
- for a double fibre, after the true split both distinct actual prefixes are present, so width two leaves no room for a phantom;
- for a singleton fibre, any phantom whose disagreement stayed below a fixed source precision along arbitrarily deep levels would yield a second infinite path, contradiction;
- at fixed n the compatible-prefix sets decrease inside the finite set 2^n, giving at most 2^n-1 deletions and at most one deletion after c(n);
- no computable last-injury time is inferred; such persistence data would exceed the selector/stabilization information ruled out by P4-S002/P4-S006;
- the singleton-fibre partial inverse searches for a deeper skeleton level whose candidates share the requested prefix and is claimed to halt only under the singleton-fibre promise;
- the one-bit-per-precision statement is not promoted to a coherent global branch bit;
- P4-S004's vanishing conditional-weight example and P4-S005's noncomputable stopping/counting masses remain valid obstructions to the existing transfer routes;
- the generalized collapse lemma uses only the fact that after c(n) there are at most two compatible n-prefixes: later information selecting one determines every coordinate on which they differ;
- SRC-0061 is not claimed to satisfy the resulting freshness condition and is not promoted to a finite-fibre witness;
- no exact k=2 computable-randomness destroyer is asserted;
- general k=2 preservation/failure remains unresolved;
- no result is asserted for k>2;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- the pre-Phase-4 Gate-3 guard remains historical and unchanged in meaning;
- DEF-0020 and catalogue records are unchanged;
- Gate 4 is not reviewed and Phase 5 remains CLOSED.

This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
