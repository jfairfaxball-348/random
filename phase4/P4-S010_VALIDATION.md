# P4-S010 validation

Date: 2026-10-05
Incoming baseline: ea87997cea224d458a80b72ea82089c31441e325
Result: **PASS** for uniqueness, k=2 scope discipline, capped-value noncomputability calculation, scan/fibre/fair-coin checks, witness-attempt accounting, authority synchronization and preserved novelty/convention guards.

Checks:
- live `main` matched the incoming baseline before substantive work and again immediately before writes;
- repository search found no committed P4-S010 record on the incoming checkpoint;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- CAND-01's exact formulation is unchanged;
- P4-S001 through P4-S009 are not edited;
- P4-S005 through P4-S009 are treated as settled and crossing-measure, canonical-sheet, one-hole/XOR and persistent-hole winning routes are not reopened;
- the code strings (t_e=1^e0^{e+2}) are prefix-free, have measure (4^{-(e+1)}), and encode a c.e. noncomputable set K into (alpha=sum_{ein K}4^{-(e+1)}) with a base-4 gap sufficient to recover K from any hypothetical computation of alpha;
- the one-sentinel scan is everywhere total and no-repeat, consumes coordinate 0 exactly on the c.e.-open trigger event, queries all coordinates on trigger branches, and queries every coordinate except 0 on nontrigger branches;
- hence its fibres are singleton on trigger branches and exactly two-point on nontrigger branches, so the scan is globally k=2;
- fair-coin preservation follows by induction because every output step reads a fresh coordinate chosen from the previous transcript;
- the output martingale remains at 1 before the sentinel, takes values 0/2 at the sentinel, freezes thereafter, and is bounded by threshold 2;
- the bounded eventual-consumption/threshold payoff is (2b) on trigger tails and 1 on avoiding tails;
- after prequerying sentinel bit b, its exact conditional value is (1+(2b-1)alpha), so a computable exact optional projection would compute the noncomputable alpha;
- finite truncations replace alpha by computable increasing rationals alpha_s; a computable convergence modulus would again compute alpha;
- this result is explicitly a scan-level optional-projection obstruction and does not alter the settled P4-S004/P4-S005 crossing-measure theorem;
- the adaptive singleton-spine comb queries the least unqueried coordinate only at the genuine wager, enumerates every other coordinate on a nontrigger branch, and chooses future sentinels only after prior turnover from still-unqueried coordinates;
- therefore the comb's totality, no-repeat, fair-coin, global k=2, singleton-spine, freshness and non-pre-revelation checks are valid;
- no computably random winning source for that comb is asserted;
- finite computably bounded control blocks are not claimed as witnesses; they fall back into computably normalized/bounded turnover behavior;
- noncomputable c.e. trigger masses are used only to block the immediate optional-projection computation, not as proof of source computable randomness;
- SRC-0061 is not promoted to a k=2 witness;
- no exact k=2 computable-randomness destroyer is asserted;
- general k=2 scan preservation and general k=2 preservation/failure remain unresolved;
- no result is asserted for k>2;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- the pre-Phase-4 Gate-3 guard remains historical and unchanged in meaning;
- DEF-0020 and catalogue records are unchanged;
- Gate 4 is not reviewed and Phase 5 remains CLOSED.

Repository/authority synchronization and final remote-head verification are performed in closeout. This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
