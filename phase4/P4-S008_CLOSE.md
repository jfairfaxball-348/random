# P4-S008 close

Date: 2026-10-05
Session: P4-S008
Incoming checkpoint: 22fa3f66558a92eae070ded127035dec2f128e1e
Scope: selected CAND-01; k=2 scan-freshness / permutation-completion boundary only
Status: **COMPLETED**

## Result

P4-S008 sharpens the P4-S007 freshness obstruction for adaptive no-repeat scans.

For a scan transcript, compatible length-n source prefixes are exactly the assignments to as-yet-unqueried coordinates below n. Hence P4-S007's schedule c(n) has a concrete scan meaning: after c(n), every transcript has queried at least n-1 of the first n source coordinates.

The main new result is a fixed-sentinel permutation completion. For any coordinate j, query j first, then follow the original scan until it tries to query j; if that happens, stop simulating it and enumerate all remaining coordinates. If the original scan never queries j, the global k=2 condition forces it to query every other coordinate. The resulting scan is therefore an everywhere-total computable adaptive permutation and lies in P4-S001's k=1 preservation regime.

Any output martingale can be copied along this permutation until the sentinel would be consumed, then frozen. Consequently, if a computably random x were a winning source for a global k=2 scan and some coordinate j were never queried on x, the corresponding permutation martingale would succeed on a computably random permutation image, contradiction.

Thus **every possible scan-based k=2 destroyer must win on a singleton fibre**: along the winning source the scan must eventually query every coordinate. The only surviving freshness pattern is the P4-S007 singleton phantom specialized to scans—a unique low-coordinate hole that, when present at c(n), must move outward and is eventually consumed.

This does not yet yield full scan preservation. On a singleton path every fixed sentinel is eventually consumed, and c(n) supplies no computable deadline for that event. A static mixture of fixed-sentinel completions has no proved growth-rate compensation, while a dynamic sentinel completion can again pre-reveal a future genuine betting coordinate. No exact k=2 destroyer and no general preservation theorem is established.

SRC-0061 is therefore not reused. Its committed mechanism has no proved singleton-fibre moving-hole freshness theorem with the required global fibre and non-pre-revelation checks.

General k=2 forward computable-randomness preservation/failure remains unresolved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001 through P4-S007 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S008_VALIDATION.md.

Next: P4-S009, still bounded to k=2, on the singleton-fibre moving-hole case isolated here: determine whether threshold-triggered/dynamic-sentinel permutation completions can be combined into one computable martingale without a computable success-rate, or whether an exact globally k=2 singleton-winning scan witness can be constructed.
