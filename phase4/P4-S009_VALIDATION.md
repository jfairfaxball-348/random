# P4-S009 validation

Date: 2026-10-05
Incoming baseline: 90f4441e1edde8f1c3a4e85652c2514e18cb77ac
Result: **PASS** for uniqueness, k=2 scope discipline, avoidance-tree compactness, bounded deferred-wager hedge calculations, savings/restart boundary accounting, witness checks, authority synchronization and preserved novelty/convention guards.

Checks:
- live main matched the incoming baseline before substantive work and again after the user continuation;
- P4-S009 mathematics/close/validation records were absent on the incoming checkpoint;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- CAND-01's exact formulation is unchanged;
- P4-S001 through P4-S008 are not edited;
- P4-S005 through P4-S008 are treated as settled and crossing-measure, canonical-sheet, one-hole/XOR and persistent-hole winning routes are not reopened;
- for a fresh coordinate j, finite transcript continuations that avoid j form a computable prefix-closed binary tree;
- if that tree has no infinite path, finite branching makes it finite, and the first empty level is found by a decidable finite search, giving a computable uniform query deadline;
- if the avoidance tree has nodes at every height, König's lemma gives an infinite continuation that never queries j; global k=2 then forces every other coordinate to be queried on that continuation;
- the bounded deferred-wager hedge uses only a finite product of fresh fair bits; its terminal payoff is d immediately after the logical j-step and has average d(tau) by finite repeated martingale averaging;
- conditional expectations on that finite tree therefore give a computable fair completion-stream martingale reaching the exact post-consumption d-capital, so no factor-two loss is claimed in the bounded-lifetime regime;
- the finite-horizon portfolio argument is explicitly limited to that family of savings/restart constructions: tail allocation tends to zero with delay, so no rate-free lower bound follows without a relation between delay and d-growth;
- no universal impossibility theorem for all computable martingale transfers is claimed;
- the singleton-spine comb is globally no-repeat, fair-coin preserving and k=2 at the query-set level, with an exhaustive singleton spine;
- the naive comb is explicitly rejected as a destroyer because its spine fixes a computable set of source control bits and is therefore not computably random;
- no adaptive comb satisfying the full freshness/non-pre-revelation conditions is claimed;
- SRC-0061 is not promoted to a k=2 witness;
- no exact k=2 computable-randomness destroyer is asserted;
- general k=2 scan preservation and general k=2 preservation/failure remain unresolved;
- no result is asserted for k>2;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- the pre-Phase-4 Gate-3 guard remains historical and unchanged in meaning;
- DEF-0020 and catalogue records are unchanged;
- Gate 4 is not reviewed and Phase 5 remains CLOSED.

- synchronized `authoritative/STATE.json`, `phase2/candidates.json` and unchanged `phase3/prior-art.json` parse successfully;
- PA-0001 remains `UNRESOLVED_UNDER_INSPECTED_EVIDENCE`;
- the incoming-baseline comparison changes only P4-S009 records and programme authority/index files; P4-S001 through P4-S008, Phase-3 prior-art records and catalogue files are absent from the changed-file set;
- authoritative state names P4-S009 as last completed, P4-S010 as next, keeps Phase 4 OPEN and Phase 5 CLOSED, and records no owner/external blocker.

This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
