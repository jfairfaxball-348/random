# P2-S004 close — CAND-03 formulation alignment

Date: 2026-10-04  
Status: **COMPLETED**  
Incoming checkpoint: `6b5bcc046cd1bd74dda33569565d593db9ba567d`

## Result

P2-S004 resolved formulation task E3 for CAND-03 and **retains the candidate provisionally as an auxiliary structural direction with its exact P2-S001 shape unchanged**.

The catalogue was sufficient. DEF-0025 / SRC-0032 already require a globally total computable uniform family whose every oracle instance is a valid martingale. CAND-03 therefore continues to exclude procedures that are only total or valid at the chosen oracle A. Its class `L_u` keeps the universal requirement that every unrelativized computably random X remain uniformly computably random relative to A.

THM-0024 remains a pairwise symmetric join characterization and THM-0025 remains an existential pairwise ordinary-vs-uniform separation. Neither supplies universal lowness or a noncomputable member of `L_u`. The recorded Martin-Löf lowness/K-trivial/low-K equivalences and base-for-randomness theorem retain their own universal/existential quantifiers; SRC-0009 Theorem 5.7 is used only as a contrast for ordinary computable-randomness lowness.

Full formulation record: [P2-S004_FORMULATION_ALIGNMENT.md](P2-S004_FORMULATION_ALIGNMENT.md).

## Evidence and catalogue synchronization

No external source passage was inspected. Existing statement-inspected catalogue records were enough to resolve E3, so no source, definition, theorem or relation record changed and no access limitation was added.

DEF-0020 and every Phase-1 evidence/convention guard remain untouched. Meaningful formulation guard: FL-038. Durable Discovery decision: D-0012.

The independent value criterion is now explicit: future promotion requires an intrinsic characterization of `L_u` independent of its defining universal preservation clause plus a concrete consequence for randomness/product information. Mere renaming of an established lowness class, a routine reduction to ordinary computable lowness, or no meaningful randomness consequence remains a falsifier.

## Authority after close

- Gate 1: **PASS**
- Phase 1 — Research / Catalogue: **COMPLETED for gate purposes**
- Phase 2 — Discovery: **OPEN**
- Gate 2: **CLOSED / NOT REVIEWED**
- Phases 3–5: **CLOSED**
- final candidate selected: **NO**
- Fairfax-Ball Randomness defined: **NO**
- CAND-01: **RETAIN_PROVISIONAL**, E1 resolved
- CAND-02: **RETAIN_PROVISIONAL**, E2 resolved
- CAND-03: **RETAIN_PROVISIONAL AS AUXILIARY**, shape unchanged, E3 resolved
- owner/external blocker: **NONE**

No lowness/traceability prior-art survey, equivalent-definition search, witness construction, new implication proof, novelty/prior-art audit, novelty claim, experiment, original proof work, Lean/Palomar work, manuscript/publication preparation or outreach was performed. P2-S005 was not begun.

## Validation

See [P2-S004_VALIDATION.md](P2-S004_VALIDATION.md). Changed JSON parses; six CAND IDs remain unique; status counts remain three provisionally retained and three rejected; all E1–E3 tasks are resolved; no candidate is selected; catalogue stable IDs/counts are unchanged; DEF-0020 is untouched; authority flags remain coherent.

## Next bounded task

No owner/external blocker exists. The smallest runnable next task is **P2-S005 — Gate-2 readiness audit only**: audit the existing portfolio against the Gate-2 minimum-evidence fields without making a Gate-2 decision, doing novelty/prior-art work, selecting a target or starting proof work.

The exact outgoing remote-main hash is reported after the publication commit is created; it cannot be self-embedded in this file.
