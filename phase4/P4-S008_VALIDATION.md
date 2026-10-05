# P4-S008 validation

Date: 2026-10-05
Incoming baseline: 22fa3f66558a92eae070ded127035dec2f128e1e
Result: **PASS** for uniqueness, k=2 scope discipline, scan-fibre calculations, fixed-sentinel permutation completion, singleton reduction, authority synchronization and preserved novelty/convention guards.

Checks:
- live main matched the incoming baseline before substantive work;
- expected P4-S008 work/close/validation records were absent on the incoming checkpoint and the session ledger contained only forward scheduling for P4-S008;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- CAND-01's exact formulation is unchanged;
- P4-S001 through P4-S007 are not edited;
- P4-S005 through P4-S007 are treated as settled and no crossing-measure, canonical-mass or one-hole/XOR route is reopened;
- for a no-repeat scan, a transcript prefix fixes exactly the queried source coordinates, so the number of compatible n-prefixes is 2^(n-|Q_m intersect n|);
- therefore P4-S007's bound of at most two compatible n-prefixes at c(n) implies at most one unqueried source coordinate below n;
- global scan fibres have size at most two exactly when every infinite transcript omits at most one source coordinate;
- for fixed j, the sentinel scan queries j first, follows T while T avoids j, and switches to an increasing enumeration of remaining coordinates if T requests j;
- if T never requests j, global k=2 forces T to query every coordinate other than j, so the sentinel scan is exhaustive on that branch too;
- the sentinel scan is everywhere total, computable, no-repeat, fair-coin preserving and bijective, with a computable inverse obtained by simulating until the requested coordinate is queried;
- the transferred martingale ignores the first sentinel bit, copies the original output martingale while T avoids j, and freezes before the filler switch, so the martingale equation is preserved;
- if the original scan omits j on x, the transferred martingale has the same unbounded capital path, contradicting P4-S001 preservation when x is computably random;
- hence any scan-based k=2 counterexample source must be on a singleton fibre and its scan must query every coordinate eventually;
- on such a singleton path the unique low-coordinate hole allowed at c(n) is eventually consumed and recurrent holes move outward, by the P4-S007 singleton-phantom theorem;
- no computable consumption deadline is inferred from c(n), consistent with P4-S007's no-last-injury boundary;
- no countable mixture or dynamic-sentinel argument is misrepresented as a completed preservation theorem;
- SRC-0061 is not claimed to satisfy the singleton moving-hole freshness requirement and is not promoted to a finite-fibre witness;
- no exact k=2 computable-randomness destroyer is asserted;
- general k=2 preservation/failure remains unresolved;
- no result is asserted for k>2;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- the pre-Phase-4 Gate-3 guard remains historical and unchanged in meaning;
- DEF-0020 and catalogue records are unchanged;
- Gate 4 is not reviewed and Phase 5 remains CLOSED.
- synchronized `authoritative/STATE.json`, `phase2/candidates.json` and unchanged `phase3/prior-art.json` parse successfully, with PA-0001 still `UNRESOLVED_UNDER_INSPECTED_EVIDENCE`;
- the final incoming-baseline comparison changes only P4-S008 records and programme authority/index files; P4-S001 through P4-S007, Phase-3 prior-art records and catalogue files are absent from the changed-file set;
- authoritative state names P4-S008 as last completed, P4-S009 as next, keeps Phase 4 OPEN and Phase 5 CLOSED, and records no owner/external blocker.

This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
