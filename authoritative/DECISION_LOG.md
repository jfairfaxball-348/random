# Decision Log

## D-0001 — Five gated phases

The programme uses five sequential phases: Research/Catalogue; Discovery; Novelty/Prior Art; Mathematics; Publication. Phase boundaries are hard gates.

## D-0002 — Name is earned, not assumed

"Fairfax-Ball Randomness" is the intended public name only if a genuinely distinct, natural and worthwhile notion survives the research, novelty and mathematics gates.

## D-0003 — Repository authority

Committed repository records supersede conversational memory for project state.

## D-0004 — Catalogue rather than paper archive

External papers/articles normally remain external. The repository stores stable bibliographic metadata, links, access status, theorem/definition records, derived notes and cross-references. Copyrighted source texts are not copied merely for convenience.

## D-0005 — Agent-searchable knowledge architecture

Phase-1 records use stable IDs, structured metadata, normalized terms, compact summaries and cross-links so future agents can retrieve relevant knowledge without rereading the whole corpus.

## D-0006 — Scaffold does not open research

Bootstrap creates only architecture. All research phases remain closed pending explicit owner authorization.

## D-0007 — Owner opens Phase 1

On 2026-10-03 the owner explicitly authorized opening Phase 1 — Research / Catalogue — and P1-S001. Phase 1 may perform bounded literature mapping and catalogue construction. Phases 2–5 remain CLOSED. Candidate invention/selection, dedicated novelty audits, original mathematics, formalisation, publication work and external outreach remain unauthorized. This authorization does not constitute a PASS of the Phase 1 -> Phase 2 gate.


## D-0008 — Gate 1 PASS opens Phase 2 Discovery

On 2026-10-04, bounded review session `P1-S014` formally recorded **PASS** for Gate 1 — Research/Catalogue -> Discovery.

The decision is based on the Gate-1 standard in `docs/GATE_POLICY.md`: the committed library is fit to support discovery, not that all literature has been found. The 19 historical coverage records remain partial-depth records; their P1-S013 audit dispositions remain 19/19 sufficient for review with 0 gate-critical remediation gaps.

Residual provenance/access gaps remain live. In particular, abstract-level Kolmogorov-Loveland and constructive-dimension material must be upgraded before a Phase-2 claim materially relies on exact formulations, and the deliberately minimal COV-0016 boundary remains deliberate.

Effect: Phase 1 is complete for gate purposes; Phase 2 — Discovery is OPEN; Phases 3–5 remain CLOSED. P1-S014 performed no Phase-2 discovery, selected no candidate and made no novelty claim.

## D-0009 — Preserve a provisional portfolio and retire three redundant shapes

On 2026-10-04, P2-S001 retained CAND-01 (finite-ambiguity observations), CAND-02 (nonergodic convergence for enumerable events) and CAND-03 (uniform-computable-lowness, as an auxiliary direction) for further bounded formulation work. None is selected as the programme target or asserted novel, open in the literature, or mathematically distinct.

CAND-04, CAND-05 and CAND-06 are rejected in their exact recorded shapes because THM-0008, THM-0026 and THM-0024 respectively already supply the desired characterization or collapse. Their stable records remain addressable; reformulating a rejected shape would require an explicit changed question, not erasure of the rejection.

Decision record: `phase2/P2-S001_DISCOVERY.md`; machine index: `phase2/candidates.json`. No gate is passed. Next scheduling is P2-S002, CAND-02 formulation alignment only, to resolve a concrete map/observable convention dependency. The Phase-1 catalogue remains unchanged; Phases 3–5 remain CLOSED.

## D-0010 — Retain CAND-02 unchanged after exact formulation alignment

On 2026-10-04, P2-S002 resolved E2 for CAND-02 without changing its predicate. CAND-02 continues to quantify over **everywhere-total** computable fair-coin-preserving Cantor self-maps and effectively open event indicators, asking only for convergence.

The decisive formulation clarification is that SRC-0058's computable-transformation representation is a.e.-defined: the induced transformation is guaranteed defined/infinite outside a computable G_delta null set, and the Section 4 converse construction explicitly ensures definition almost everywhere. THM-0063 therefore does not provide the everywhere-total converse witness needed to dispose of the recorded CAND-02 shape. THM-0064 remains a one-way lower-semicomputable-observable benchmark; THM-0059/THM-0060 retain ergodicity for equality to expectation.

Decision: **RETAIN_PROVISIONAL, SHAPE UNCHANGED; E2 RESOLVED.** This is not target selection, novelty assessment, literature-openness assessment or a Gate-2 decision. Record: `phase2/P2-S002_FORMULATION_ALIGNMENT.md`.

