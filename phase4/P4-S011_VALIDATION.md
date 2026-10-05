# P4-S011 validation

Date: 2026-10-05
Incoming baseline: 31cff4e4c442520b19054f19fac75bd8b5c7cc26
Core mathematics commit checked: ed7c64b97c4f413610bdcb3b84406e30e4edf36a

Result: PASS for uniqueness, k=2 scope discipline, source theorem support, total-scan construction, fair-coin preservation, global fibre bound, computably random source, output-martingale success, authority synchronization and preserved scope guards.

## Repository and scope checks

- live main matched the requested incoming baseline before substantive work;
- repository search and the phase4 directory showed no pre-existing P4-S011 record on the incoming baseline;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- P4-S001 through P4-S010 were read and not edited;
- P4-S005 through P4-S010 were treated as settled;
- the incoming-baseline comparison after the core commit changes only P4-S011 records, the narrowly needed source/theorem/author catalogue entries, and current programme authority/index/summary files;
- no P4-S001 through P4-S010 record appears in the changed-file set;
- catalog/definitions.json is unchanged, so DEF-0020 is preserved;
- phase3/prior-art.json is unchanged, and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- no k>2, novelty, Gate-4, publication or outreach claim is made;
- SRC-0061 is not reused.

## External source checks

- SRC-0067 records the Merkle–Mihailovic Journal of Symbolic Logic article and its publisher abstract statement that a rec-random weak-truth-table-autoreducible set exists;
- SRC-0068 records Mihailovic's 2007 thesis, whose Theorem 6.9 explicitly states that there is a computably random wtt-autoreducible sequence;
- the thesis definition inspected in P4-S011 states that wtt reducibility is Turing reducibility with a computable use bound and that autoreducibility forbids querying the current input;
- DEF-0004 independently records the historical recursive-randomness terminology for computable randomness;
- THM-0076 records only the source existence theorem and explicitly cautions that the finite-fibre scan conversion is P4-S011 programme mathematics.

## Mathematical construction checks

Let Y be the computably random wtt-autoreducible sequence and M its autoreduction.

1. Totality and computability.
   - At an epoch, the sentinel is the least unqueried coordinate.
   - A visible binary halt of M on the sentinel triggers a sentinel query.
   - Otherwise the scan queries the least fresh non-sentinel coordinate.
   - Therefore one fresh coordinate is produced at every stage even when the oracle computation diverges on a sibling.
   - The next query and finite simulation are computable from the finite transcript.

2. No-repeat and freshness.
   - Fillers are chosen outside the queried set and outside the current sentinel.
   - The sentinel is queried only after its prediction is visible.
   - Future sentinels are selected only from coordinates still unqueried after turnover.
   - Thus no genuine sentinel wager is pre-revealed.

3. Fair-coin preservation.
   - For any output string of length m, the adaptive query indices are pairwise distinct and determined by earlier output bits.
   - Its preimage fixes exactly m independent fair-coin source coordinates.
   - Therefore every length-m output cylinder has measure 2^{-m}, so F_*lambda=lambda.

4. Global k=2 fibre check.
   - If an epoch never triggers, its filler rule enumerates every coordinate except that epoch's sentinel; the fibre has exactly two points.
   - If every epoch triggers, the successive least-unqueried sentinels strictly increase and every source coordinate is eventually queried; the fibre is a singleton.
   - Hence every fibre has size at most two.

5. Source-randomness step.
   - On Y, M^Y(j) halts with output Y(j) and does not query j.
   - Its finite halting computation uses finitely many other oracle coordinates.
   - Persistent fillers eventually reveal all those coordinates, so every epoch triggers after finite time and predicts correctly.
   - Y is computably random by THM-0076 / SRC-0068 and lies on a singleton fibre.

6. Output martingale.
   - The martingale holds capital constant on filler outputs.
   - At a trigger it wagers all capital on the computably visible predicted sentinel bit.
   - The martingale equation is exact, the strategy is total computable, and on F(Y) capital doubles once per epoch.
   - Infinitely many target epochs complete, so the martingale is unbounded and F(Y) is not computably random.

Therefore P4-S011 gives an exact CAND-01 k=2 non-conservation witness.

## Failed positive alternative

The proposed generic argument that repeated c.e.-graph prediction constraints must yield one computable source martingale is invalid. The all-trigger correct-prediction graph constructed here contains the computably random source Y. A computable source martingale forced to succeed on every such spine would contradict Y's computable randomness.

The inspected source boundary is consistent with P4-S009/P4-S010: weak-truth-table autoreduction may be partial on sibling oracles, whereas the journal abstract contrasts it with the impossibility of rec-random truth-table autoreducibility.

## Synchronization checks

- authoritative/STATE.json parses and records P4-S011 as last completed, P4-S012 as next, Phase 4 OPEN and no active blocker;
- phase2/candidates.json parses and records the exact k=2 destroyer and negative forward-preservation result for CAND-01;
- catalog/sources.json parses with 68 records and unique IDs;
- catalog/theorems.json parses with 76 records and unique IDs;
- catalog/authors.json parses with 75 records and unique IDs;
- authoritative/SESSION_LEDGER.md records P4-S011, D-0033 and FL-059;
- authoritative/DECISION_LOG.md contains D-0033;
- docs/FAILURE_AND_LESSON_LEDGER.md contains FL-059;
- README.md, ROADMAP.md, AGENTS.md, authoritative/START_HERE.md and phase4/README.md are synchronized to the negative k=2 result;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded, runnable P4-S012 prompt restricted to the structural partial-predictor question at k=2.

This is manual mathematical/bookkeeping validation, not proof-assistant verification and not a novelty theorem.

Final remote main is verified after this validation commit, and the exact outgoing hash is reported in the session response.
