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



## D-0011 — Retain CAND-01 unchanged after exact finite-fibre formulation alignment

On 2026-10-04, P2-S003 resolved E1 for CAND-01 without changing its predicate. CAND-01 continues to quantify over **everywhere-total computable fair-coin-preserving Cantor self-maps** with a **global finite cardinal fibre bound**, while explicitly assuming no effective inverse branches.

The catalogue comparison keeps three notions separate: THM-0037 is an existential no-randomness-from-nothing preimage theorem for a.e.-computable maps; THM-0038 gives computable-randomness invariance only for an a.e.-computable inverse pair; and THM-0035 is a Martin-Löf morphism/isomorphism result with explicit inverse data in the isomorphism case. THM-0008/THM-0039 are Martin-Löf maximality characterizations, not finite-to-one computable-randomness preservation theorems.

Decision: **RETAIN_PROVISIONAL, SHAPE UNCHANGED; E1 RESOLVED.** No finite-to-one preservation theorem was searched for or asserted. This is not target selection, novelty assessment, literature-openness assessment or a Gate-2 decision. Record: `phase2/P2-S003_FORMULATION_ALIGNMENT.md`.

## D-0012 — Retain CAND-03 unchanged after universal-lowness / global-family alignment

On 2026-10-04, P2-S004 resolved E3 for CAND-03 without changing its predicate. CAND-03 continues to define an **oracle class**

`L_u = {A : for every X in CR, X is computably random uniformly relative to A}`,

using DEF-0025's globally total uniform-family convention: one total computable family is defined on every oracle input and every oracle instance is a valid martingale. A procedure that is only total/valid at the chosen oracle A is outside this formulation.

THM-0024 remains a pairwise symmetric join characterization and THM-0025 remains an existential pairwise separation between uniform and ordinary relative computable randomness. Neither supplies the universal quantifier over all unrelativized computably random X required by L_u, nor a noncomputable member of L_u. The recorded Martin-Löf lowness/K-trivial/low-K equivalences and the base-for-randomness theorem retain their own universal-versus-existential quantifiers and cannot be transferred by relabelling. SRC-0009 Theorem 5.7 remains a contrast about ordinary computable-randomness lowness only.

Decision: **RETAIN_PROVISIONAL AS AUXILIARY, SHAPE UNCHANGED; E3 RESOLVED.** Future promotion requires an intrinsic oracle characterization independent of the defining preservation clause plus a concrete randomness/product-information consequence; mere renaming of a known lowness property is a falsifier. No noncomputable low oracle, novelty, openness, equivalence or separation is asserted. Record: `phase2/P2-S004_FORMULATION_ALIGNMENT.md`.

## D-0013 — Gate-2 minimum evidence is assembled for separate formal review

On 2026-10-04, P2-S005 audited the existing six-candidate Discovery portfolio against every Gate-2 minimum-evidence field in `docs/GATE_POLICY.md`.

CAND-01, CAND-02 and CAND-03 each have an exact search-ready formulation, mathematical motivation/potential value, explicit relationship to known notions, a prospective theorem/characterization package, falsifiers, dependencies/expected difficulty, and an explicit guard separating apparent interest from novelty. E1–E3 are resolved. CAND-04, CAND-05 and CAND-06 remain rejected exactly as recorded.

Decision: record **READY_FOR_FORMAL_GATE2_REVIEW** only. This is not Gate-2 PASS, does not open Phase 3, does not select a final candidate and does not establish novelty, openness or any new mathematical result. A separate formal Gate-2 review is required in P2-S006.


## D-0014 — Gate 2 passes; Phase 3 opens without a novelty finding

On 2026-10-04, P2-S006 formally reviewed the committed Phase-2 portfolio against every Gate-2 minimum-evidence requirement in `docs/GATE_POLICY.md`.

The review independently confirmed a bounded six-candidate portfolio. CAND-01, CAND-02 and CAND-03 each have a search-ready formulation, motivation/potential value, explicit relationships to known notions, a plausible future theorem/characterization package, falsifiers, dependencies/expected difficulty and an explicit novelty guard. E1–E3 remain resolved. CAND-04, CAND-05 and CAND-06 remain rejected in their exact recorded shapes.

Decision: **GATE 2 PASS**. Phase 2 is complete for gate purposes and Phase 3 — Novelty / Prior Art — is OPEN.

This PASS is a readiness decision only. It does not establish that any retained candidate is novel, open, distinct, nontrivial or publishable; it does not select a final candidate; and it does not define Fairfax-Ball Randomness. Candidate novelty/literature status remains NOT_ASSESSED until Phase-3 evidence is recorded. No Phase-3 substantive work was performed in P2-S006.

Record: `phase2/P2-S006_GATE2_REVIEW.md`.

## D-0015 — CAND-01 exact finite-fibre prior-art status remains unresolved after first primary attack

On 2026-10-04, P3-S001 performed the first dedicated primary-source prior-art attack on CAND-01.

Rute's SRC-0060 introduces **endomorphism randomness**, requiring computable-randomness preservation under every a.e.-computable measure-preserving endomorphism, and THM-0071 records that ordinary computable randomness is not preserved by that unrestricted class. Bienvenu–Porter's SRC-0061 / THM-0072 shows more sharply that an everywhere-total truth-table functional can induce fair-coin measure yet destroy computable randomness.

Decision: CAND-01 remains **RETAIN_PROVISIONAL** with prior-art disposition **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. Its exact formula and E1 alignment are unchanged. The fixed global finite-cardinality fibre bound with no assumed effective inverse branches remains the live unmatched hypothesis in the inspected evidence.

This is not a finding that the candidate is open, novel, materially distinct or publishable. It is also not classified as already known or equivalent/rebranded. The documented search establishes substantial framework overlap with endomorphism randomness and rules out totality plus fair-coin preservation alone as the distinguishing feature.

Record: `phase3/P3-S001_PRIOR_ART.md`; structured finding: `PA-0001`.

## D-0016 — CAND-02 exact total-map effective-open prior-art status remains unresolved after primary attack

On 2026-10-04, P3-S002 performed one dedicated primary-source prior-art attack on CAND-02.

Franklin–Towsner (SRC-0058 / THM-0063 / THM-0064) remain the closest nonergodic weak-Birkhoff framework, but use an a.e.-defined computable-transformation convention. Miyabe–Nies–Zhang (SRC-0062 / THM-0073) strengthen nonergodic convergence for lower-semicomputable observables to Oberwolfach-random points while explicitly not assuming the operator is total. Bienvenu et al. (SRC-0057 / THM-0059 / THM-0060) directly treat effectively-open indicators but require ergodicity and equality to expectation. Moriakov (SRC-0063 / THM-0074) supplies total computable Cantor maps and effectively-open indicators, but within ergodic automorphism actions with Følner averaging and expectation equality.

Decision: CAND-02 remains **RETAIN_PROVISIONAL** with prior-art disposition **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. Its exact formula and E2 alignment are unchanged. No inspected primary theorem matched the combined everywhere-total arbitrary self-map, effectively-open indicator, nonergodic convergence-only predicate.

This is not a finding that CAND-02 is open, novel, materially distinct or publishable, and it is not classified as already known or equivalent/rebranded. The documented attack records substantial overlap while preserving the unmatched hypothesis combination.

Record: `phase3/P3-S002_PRIOR_ART.md`; structured finding: `PA-0002`.

