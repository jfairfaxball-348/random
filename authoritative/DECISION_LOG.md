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



## D-0017 — Retire CAND-03: its exact oracle class is the existing Low-star(CR,CR) instance

On 2026-10-04, P3-S003 performed one bounded primary-source prior-art attack on CAND-03.

Kihara–Miyabe's SRC-0064 explicitly defines `Low^star(C,D)` as the oracles A such that every C-random is D-random uniformly relative to A, with uniform tests supplied by a total computable procedure valid across all oracle instances. With C=D=computable randomness and the exact uniform martingale-family convention of SRC-0032 / DEF-0025, CAND-03's `L_u` is the `Low^star(CR,CR)` instance at the definition level.

Decision: **REJECT_PRIOR_ART_REBRANDING** for CAND-03 as a candidate for a new named notion. Its formula and E3 alignment are unchanged; the literature classification changes from NOT_ASSESSED to **EQUIVALENT_OR_REBRANDED**.

This decision does **not** claim that the specific intrinsic characterization of `Low^star(CR,CR)` is known or open. No such characterization was located in the inspected statements, and no conclusion is inferred from absence. SRC-0009 / THM-0075 remains an ordinary-relativization contrast only; THM-0024/THM-0025 remain pairwise/existential; baseness remains existential.

Record: `phase3/P3-S003_PRIOR_ART.md`; structured finding: `PA-0003`.


## D-0018 — CAND-01 significance case provisionally survives, without novelty or selection

On 2026-10-04, P3-S004 assessed CAND-01's significance/usefulness and plausible interested communities without performing mathematics or a Gate-3 review.

Decision: **PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT**. The fixed global finite-fibre restriction is not treated as a cosmetic parameter: within the programme it is the surviving axis between known unrestricted total fair-coin-preserving non-conservation and positive invariance with explicit effective inverse data; adjacent primary literature also treats finite multiplicity as structural in uniformly finite-to-one endomorphisms and finite-to-one symbolic factor codes (SRC-0065, SRC-0066).

This is conditional significance evidence only. The adjacent sources impose stronger entropy, conditional-weight, shift or factor-code structure and do not transfer a computable-randomness theorem to CAND-01. PA-0001 therefore remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and CAND-01 remains `RETAIN_PROVISIONAL`, not selected.

Continued investment requires an explanatory future theorem package: exact preservation/failure, a mechanism or intrinsic characterization, sharp boundary against explicit inverse and unrestricted regimes, natural examples/subclasses, and any information/coding consequence only if proved under the exact effective hypotheses. A routine yes/no adaptation with no essential role for finite multiplicity remains a significance falsifier.

Record: `phase3/P3-S004_SIGNIFICANCE.md`.

## D-0019 — Retain CAND-02 for comparison, with elevated technical-slice risk

On 2026-10-04, P3-S005 completed the bounded significance/usefulness and likely-interested-community assessment on CAND-02.

Decision: **PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT WITH ELEVATED TECHNICAL-SLICE RISK.** The judgment is about significance only. PA-0002 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and no openness, novelty, equivalence, material-distinctness or theorem claim is added.

The positive case is source-backed. SRC-0058 explicitly treats weak-Birkhoff convergence as the appropriate nonergodic semantics and separates computable from lower-semicomputable observables. SRC-0062 independently treats c.e.-described analytic objects and Birkhoff convergence as a meaningful effectiveness axis. SRC-0063 shows that total computable Cantor dynamics with lower-semicomputable/effective observations occur in an established effective-dynamics framework.

The live significance risk is also explicit: no inspected evidence shows that CAND-02's everywhere-total restriction changes randomness content rather than excluding the a.e./possibly-partial witness representations used in the closest nonergodic sources. Continued investment therefore requires an exact characterization together with a structural totality result and an observable-boundary result. A routine totalization/collapse or a reduction that makes the effectively-open restriction inessential is a significance falsifier.

CAND-02 remains `RETAIN_PROVISIONAL`; its exact formula and E2 alignment are unchanged. CAND-01 is not re-assessed, retired CAND-03 stays retired, no final candidate is selected, Gate 3 is not reviewed and Phase 4 remains closed.

Record: `phase3/P3-S005_SIGNIFICANCE.md`.

## D-0020 — Phase-3 evidence is ready for a separate candidate-selection decision

On 2026-10-04, P3-S006 audited the committed Phase-3 evidence for surviving CAND-01 and CAND-02 against the preconditions needed for a later documented selection/NO-GO decision and eventual Gate-3 review.

Decision: **READY_FOR_SELECTION_DECISION**.

Both survivors have a dedicated primary-source prior-art attack, alternate-terminology/equivalent-formulation coverage, an explicit closest-known-work account, calibrated equivalence/rebranding risk, a significance/usefulness assessment, plausible interested communities, explicit remaining novelty uncertainty and a concrete future theorem package. No targeted Phase-3 evidence category is missing before selection.

The asymmetry is preserved rather than averaged away. CAND-01's finite-multiplicity axis is provisionally substantive but has no established computable-randomness consequence. CAND-02's effective-observation/nonergodic axis is provisionally substantive but carries **elevated technical-slice risk** because everywhere-totality may only exclude a.e./partial witness representations.

This readiness decision is **not** a candidate selection, a novelty finding or a Gate-3 PASS. CAND-01 and CAND-02 remain `UNRESOLVED_UNDER_INSPECTED_EVIDENCE`; CAND-03 remains retired. Gate 3 remains unreviewed and Phase 4 remains closed.

Next action: P3-S007 must make a separate documented choice among selecting CAND-01, selecting CAND-02, or NO-GO for both survivors. It must not combine selection with the formal Gate-3 review.

Record: `phase3/P3-S006_SELECTION_READINESS_AUDIT.md`.



## D-0021 — Select CAND-01 for separate Gate-3 review

On 2026-10-05, P3-S007 made the bounded Phase-3 candidate-selection / NO-GO decision over surviving CAND-01 and CAND-02.

Decision: **SELECT_CAND_01**.

CAND-01 is selected because its residual uncertainty is a direct mathematical-payoff question on a structurally meaningful finite-multiplicity axis. P3-S004 remains controlling: no computable-randomness consequence of the bare global finite cardinal fibre bound is established. The expected value lies in a sharp preservation/failure result plus an explanatory boundary between unrestricted total-map non-conservation, cardinal finite ambiguity and explicit effective inverse information.

CAND-02 is not selected for active Gate-3 investment. Its natural nonergodic/effective-observation axes remain acknowledged, but P3-S005/P3-S006's **elevated technical-slice / representation-artifact risk** remains decisive: everywhere-totality may merely exclude a.e./partial witness representations without defining a distinct randomness boundary.

NO-GO is not chosen because CAND-01 still clears the programme's investment threshold for an independent Gate-3 review. This selection is not a novelty, openness, truth or publishability finding. PA-0001 and PA-0002 remain **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

Gate 3 is not reviewed in P3-S007 and Phase 4 remains closed.

Record: `phase3/P3-S007_SELECTION_DECISION.md`.


## D-0022 — Gate 3 PASS opens Phase 4 for selected CAND-01

On 2026-10-05, P3-S008 independently reviewed selected CAND-01 against every Gate-3 minimum-evidence requirement in docs/GATE_POLICY.md.

Decision: **PASS**.

The committed record contains a dedicated primary-source prior-art attack, alternate-terminology/equivalent-formulation search, an explicit closest-known-work account, calibrated equivalence/rebranding risk, a significance/usefulness case, plausible interested communities, explicit remaining novelty uncertainty and a documented selection decision.

The PASS does not upgrade PA-0001. It remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No openness or novelty conclusion is inferred from search absence. The P3-S004/P3-S007 guard remains controlling: finite multiplicity is provisionally substantive, but no computable-randomness consequence of the bare global finite cardinal fibre bound is established.

Authorization effect: Phase 3 is complete for gate purposes; Phase 4 — Mathematics is OPEN for CAND-01; Phase 5 remains CLOSED. No Phase-4 mathematics was performed in P3-S008.

Record: phase3/P3-S008_GATE3_REVIEW.md.

## D-0023 — k=1 finite ambiguity collapses to the effective-isomorphism regime

On 2026-10-05, P4-S001 performed the first authorized original mathematics on selected CAND-01.

Decision/result: under the exact k=1 hypotheses, an everywhere-total computable fair-coin-preserving Cantor self-map with one-point fibres is necessarily a computable fair-coin-preserving homeomorphism with an everywhere-total computable inverse. The inverse can be computed by effectively separating the compact images of finite input cylinders. SRC-0015 / THM-0038 then yields computable-randomness invariance in both directions.

The effective inverse information is map-dependent: coordinate permutations show that no single fixed inverse-use bound works for the whole k=1 class.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status claim is made, and no result is inferred for k>=2 or arbitrary finite multiplicity. The Gate-3 guard remains accurate as the pre-Phase-4 baseline rather than as a post-P4-S001 statement about k=1.

Record: phase4/P4-S001_MATHEMATICS.md.

## D-0024 — k=2 does not force total effective inverse branches

On 2026-10-05, P4-S002 investigated the first genuinely non-injective CAND-01 case.

Decision/result: under the exact k=2 hypotheses, the inverse fibre F^{-1}(y) is uniformly represented by descending computable clopen sets F^{-1}([y↾m]); a particular point becomes computable from y when an isolating input prefix is supplied. But the bare cardinal bound does **not** force an everywhere-total computable selector or an everywhere-total computable two-branch enumeration.

The witness is an explicit computable fair-coin-preserving prefix-replacement map with exactly one double fibre. Unique inverses approaching the collision output converge along two subsequences to two different domain points, so every global selector/listing is discontinuous.

This obstruction does not decide computable-randomness preservation. The witness has an a.e.-computable measure-preserving inverse and hence preserves computable randomness by SRC-0015 / THM-0038. The exactly two-to-one shift independently preserves computable randomness by direct martingale lift. General k=2 preservation/failure therefore remains unresolved after P4-S002.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S002_MATHEMATICS.md.

## D-0025 — k=2 has forced finite two-prefix inverse lists, but the effective sheet-weight step remains unresolved

On 2026-10-05, P4-S003 continued selected CAND-01 strictly at k=2.

Decision/result: the bare k=2 hypotheses force, for every input precision, a computable list of at most two candidate input prefixes from sufficiently much output. They also force uniformly computable bounded conditional-weight martingales. If a computable clopen two-sheet injectivity split is supplied, those weighted components are enough to prove forward computable-randomness preservation via SRC-0015 / THM-0038 and DEF-0036.

The cardinal hypothesis itself does not force that global split. The marker-and-delete witness is total computable, fair-coin preserving and two-to-one off one singleton, yet no continuous two-colouring separates every double fibre. It still preserves computable randomness, so this is a sheet-structure boundary rather than a non-conservation witness.

General k=2 preservation/failure remains unresolved. The next mathematical target is effective control of conditional sheet weights along a computably random source, or an exact k=2 destruction construction exploiting failure of such control.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S003_MATHEMATICS.md.

## D-0026 — k=2 conditional weights reduce the remaining transfer problem to effective stopping

On 2026-10-05, P4-S004 continued selected CAND-01 strictly at k=2.

Decision/result: for every source cylinder [sigma], low values of the conditional martingale w_sigma pull back to uniformly effectively open source sets with fair-coin measure at most the weight threshold. Equivalently, the reciprocal weight is the likelihood-ratio supermartingale between fair coin and the pushforward of fair coin conditioned on [sigma]. This forces positive persistent weight for Martin-Löf-random sources, but does not by itself settle computably random sources; the missing datum is a computable hitting probability/stopped pullback or another computable-randomness-level test.

Every fixed stage of an output computable martingale also lifts exactly to a normalized computable source martingale. The obstruction is coherence across unbounded stages: a fixed mixture needs a growth rate, while adaptive stopping again needs effective hitting probabilities.

A new explicit asymmetric collision map F_thin is total computable, fair-coin preserving and globally k=2, yet one genuine double-fibre sheet has w_0(0^m)=2^{-m}->0. Its thin source point is computable and the map has an a.e.-computable inverse off the collision output, so it is not a randomness-destruction witness.

General k=2 preservation/failure remains unresolved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S004_MATHEMATICS.md.

## D-0027 — k=2 two-prefix lists do not force computable stopping probabilities

On 2026-10-05, P4-S005 continued selected CAND-01 strictly at k=2.

Decision/result: the forced two-prefix inverse lists do **not** make the P4-S004 low-weight crossing measures computable. An exact total computable fair-coin-preserving k=2 prefix-code map is constructed with a computable clopen partition [0],[1] into injective sheets, yet
[
\lambda(V_{0,1/3})=\frac18\sum_{e\in K}4^{-(e+1)}
]
for a fixed c.e. noncomputable set K. The base-4 coding makes this crossing measure noncomputable.

A natural branch-free alternative also fails uniformly: integrating inverse-point counts against fair coin yields a finite measure whose total mass is (2-\frac12\sum_{e\in K}4^{-(e+1)}), again noncomputable. Thus neither candidate-count information nor symmetric fibre counting supplies the desired computable stopped/pullback martingale by itself.

These are effectivity obstructions, not non-conservation results. The constructed map lies inside P4-S003's positive computable-clopen-sheet regime and therefore preserves computable randomness. No exact k=2 destroyer is obtained, and the SRC-0061 pre-revealed-bet obstruction remains unresolved.

General k=2 preservation/failure remains unresolved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S005_MATHEMATICS.md.



## D-0028 — canonical k=2 sheets are effective Borel/Baire-1 but do not uniformly yield computable transfer data

On 2026-10-05, P4-S006 continued selected CAND-01 strictly at k=2.

Decision/result: for every exact k=2 map, the collision relation is effectively closed. Assigning the lexicographic minimum of each fibre to the lower sheet and the nonminimum point of each double fibre to the upper sheet gives an effective G-delta lower sheet and effective F-sigma upper sheet; the double-fibre output set is effective F-sigma. The lexicographic minimum and maximum inverse selectors are effective Baire-1 limits of computable continuous approximants.

This does not close computable-randomness transfer. In the P4-S005 prefix-code map, used here only as a calibration example, the canonical sheet masses are noncomputable. Therefore the canonical split does not uniformly provide computable component measures, and the Baire-1 selector approximations have no forced computable stabilization modulus.

The attempted one-hole/rotating-mask completion of the SRC-0061 filler idea also remains invalid: revealing one genuine betting coordinate that was encoded in a shared two-way ambiguity identifies that ambiguity and pre-reveals every other coordinate in the same cohort. A more complex delayed-coalescence construction is not ruled out.

General k=2 preservation/failure remains unresolved. No exact k=2 destroyer is obtained. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S006_MATHEMATICS.md.

## D-0029 — delayed coalescence has a coherent width-two skeleton but leaves a freshness obstruction

On 2026-10-05, P4-S007 continued selected CAND-01 strictly at k=2.

Decision/result: for every exact k=2 map there is a computable monotone coalescence schedule c(n) such that the n-prefixes compatible with y↾c(n) form a coherent width-at-most-two inverse tree whose infinite paths are exactly F^{-1}(y). Double fibres become exact two persistent tracks after their true split; singleton phantoms can recur only with their disagreement moving outward. Fixed precision has a computable mind-change bound and at most one post-c(n) injury, but the last injury need not be computably recognizable.

This bounded inverse information is insufficient for the existing computable-randomness transfer routes because it does not compute branch persistence, conditional mass or stopping normalization. After c(n), all unresolved first-n information is one binary choice, so revealing one later coordinate that distinguishes the candidates determines every other differing coordinate below n. Thus any future scan-style k=2 counterexample must prove a global freshness condition relative to c(n).

SRC-0061 is not claimed to meet that condition and is not reused as a finite-fibre witness. General k=2 preservation/failure remains unresolved. No exact k=2 destroyer is obtained. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S007_MATHEMATICS.md.

## D-0030 — global k=2 scan destruction cannot use a persistent hole

On 2026-10-05, P4-S008 continued selected CAND-01 strictly at k=2 and analyzed only the scan-freshness question forced by P4-S007.

Decision/result: for a total adaptive no-repeat scan, P4-S007's schedule c(n) means that by stage c(n) every transcript has queried at least n-1 of the first n source coordinates. More importantly, any fixed coordinate j can be turned into a sentinel for a total computable adaptive permutation: query j first, follow the original scan while it avoids j, and if it requests j switch to enumerating all remaining coordinates. If it never requests j, the global k=2 fibre condition forces the original scan to query every other coordinate.

An output martingale can be copied along this permutation completion and frozen if the sentinel is consumed. Hence a computably random source on which the original output martingale succeeds cannot omit any coordinate. Any scan-based k=2 destroyer must therefore win on a singleton fibre, with the unique low-coordinate hole moving outward and eventually being consumed.

This does not yet prove scan preservation. On a singleton path every fixed sentinel is eventually consumed, c(n) gives no computable consumption deadline, and neither a static mixture nor a dynamic sentinel completion has been shown to retain the win without a computable growth/query-time relation. SRC-0061 is not reused.

General k=2 preservation/failure remains unresolved. No exact k=2 destroyer is obtained. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S008_MATHEMATICS.md.

## D-0031 — bounded moving-hole turnovers hedge exactly; only branchwise-avoidable sentinels remain hard

On 2026-10-05, P4-S009 continued selected CAND-01 strictly at k=2 and analyzed only the singleton moving-hole scan case isolated by P4-S008.

Decision/result: for a finite scan transcript tau and fresh coordinate j, the continuations on which T avoids j form a computable binary tree. If every continuation eventually queries j, compactness makes this tree finite and a uniform finite query deadline is computably searchable. If no such deadline exists, there is an infinite sibling continuation omitting j; global k=2 then forces that sibling to query every other coordinate.

A deferred sentinel wager with a verified finite deadline can be hedged exactly. Query the sentinel first, run the scan until its bounded consumption, and take the finite conditional expectation of d's post-consumption capital. The resulting completion-stream process is a computable fair martingale and reaches exactly the logical d-capital at turnover. Hence factor-two losses and savings are not intrinsic to bounded turnovers.

The unresolved case is therefore branchwise avoidable: the singleton target consumes the moving hole, but another continuation can keep it forever. Finite-horizon capital splits have tails tending to zero, so no rate-free infinite-turnover lower bound follows from unbounded output capital alone. A simple global k=2 singleton-spine comb has the right query-set geometry but its naive computable-control spine is not computably random.

No exact k=2 destroyer and no full scan-preservation theorem is obtained. SRC-0061 is not reused. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S009_MATHEMATICS.md.

## D-0032 — threshold capping does not compute branchwise-avoidable optional projections

On 2026-10-05, P4-S010 continued selected CAND-01 strictly at k=2 and analyzed only the branchwise-avoidable deferred-wager case isolated by P4-S009.

Decision/result: capping at an output-capital threshold does not by itself effectivize the missing stopping value. An exact global k=2 no-repeat scan was constructed in which sentinel 0 is consumed on a c.e.-open tail event of noncomputable measure alpha and omitted otherwise. A bounded computable martingale, already capped at 2, has eventual-consumption payoff whose exact conditional values after a fixed-sentinel completion reveals bit b are 1-alpha and 1+alpha. Hence the exact optional projection is noncomputable; finite-horizon projections have no computable convergence modulus.

A stronger adaptive singleton-spine comb was also checked. Withhold the least unqueried coordinate, let other fresh bits drive a c.e. trigger/prediction, consume the sentinel only after the prediction is fixed, and choose the next sentinel only afterwards from still-unqueried coordinates. This architecture is total, fair-coin preserving, globally k=2, singleton on every all-trigger path, and satisfies freshness/non-pre-revelation. The missing check is the existence of a computably random all-trigger winning source.

No exact k=2 destroyer and no full scan-preservation theorem is obtained. SRC-0061 is not reused. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S010_MATHEMATICS.md.

## D-0033 — k=2 already admits exact computable-randomness destruction

On 2026-10-05, P4-S011 used SRC-0067 / SRC-0068 / THM-0076 to fix a computably random weak-truth-table-autoreducible source Y and converted its partial autoreduction into a total adaptive no-repeat least-fresh-sentinel scan.

The induced map is fair-coin preserving and has every fibre of size at most two. A permanently nontriggering epoch omits exactly one sentinel; an all-trigger transcript queries every coordinate. On Y all predictions halt and are correct, so Y lies on a singleton fibre and one computable output martingale doubles at every sentinel.

Therefore the general k=2 forward-preservation question is settled negatively by an exact witness. The repeated graph-like trigger structure does not force a source martingale without stronger totality or uniformity.

This is programme mathematics, not a novelty finding. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. SRC-0061 is not reused. No k>2 result is asserted. Gate 4 is not reviewed and Phase 5 remains closed.

Record: phase4/P4-S011_MATHEMATICS.md.


## D-0034 — the k=2 scan mechanism is partial self-betting; the converse is exact at stake level

On 2026-10-06, P4-S012 continued selected CAND-01 strictly at k=2 and abstracted the P4-S011 destroyer without altering it.

Decision/result: the P4-S011 least-fresh conversion does not use the weak-truth-table use bound. It needs only target-visible self-avoiding partial predictions at the recursively generated sentinels; predictions at filler coordinates are irrelevant. More generally, a target-winning self-avoiding rational stake spine is sufficient.

Conversely, every global-k=2 adaptive no-repeat scan winning on a computably random source induces a partial self-avoiding stake functional total on that source. P4-S008 forces the winning transcript to be singleton; simulating the scan up to each coordinate without reading it and reading off the output martingale's signed stake reproduces the winning capital exactly in the scan's original order.

This does not establish an all-correct bit-autoreduction converse. Fractional success can survive infinitely many wrong favoured-bit predictions, although all-in wagers on a succeeding path must be correct. Reordering the induced stakes into a new least-fresh scan is not justified automatically.

The new live boundary is sibling totality: P4-S011 relies on a target-correct partial computation which may diverge on sibling oracles. P4-S013 should test whether total-on-all-oracles or a weaker effective uniform-totality/deadline condition forces preservation for the least-fresh subclass.

P4-S011's exact destroyer remains settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S012_MATHEMATICS.md.

## D-0035 — reachable-sentinel totality is the finite-deadline preservation boundary for the least-fresh mechanism

On 2026-10-06, P4-S013 continued selected CAND-01 strictly at k=2 and tested only the sibling-totality boundary left by P4-S012.

Decision/result: full totality of the self-avoiding predictor/stake functional on every oracle and every input is sufficient for preservation, but it is stronger than necessary. The weaker relevant condition is reachable-sentinel totality: whenever a least-fresh run reaches an epoch with sentinel j, the functional halts at j on that source.

At any reachable epoch, nontriggering sibling continuations form a computable finitely branching avoidance tree. Reachable-sentinel totality is equivalent to absence of an infinite path through that tree. By compactness the tree is then finite, and the first empty level is found by a computable search. Therefore a separate computable deadline modulus is not an additional hypothesis.

When this condition holds at every reachable epoch, every epoch ends on every source and the scan is exhaustive. It queries every coordinate exactly once, so the induced map has singleton fibres and a computable inverse. The least-fresh k=2 subclass has collapsed to the P4-S001 k=1 effective-isomorphism regime, and computable randomness is invariant.

The condition is strictly weaker than full oracle-totality because the functional may diverge on coordinates that are always consumed earlier as fillers and therefore never become sentinels.

This is a sufficient boundary for the exact compactness/finite-hedge transfer, not a necessary characterization of every preserving k=2 least-fresh scan. P4-S011 shows that target-only totality is insufficient and that branchwise avoidance can support exact destruction; it does not say every branchwise-avoidable scan destroys randomness.

P4-S011's exact destroyer and P4-S012's structural boundary are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty/open-status, k>2, Gate-4 or publication claim is made.

Record: phase4/P4-S013_MATHEMATICS.md.


## D-0036 — computably budgeted avoidance tails suffice below finite deadlines

Session: P4-S014
Date: 2026-10-06
Decision: **USE COMPUTABLY BUDGETED FINITE-HORIZON MISS PROBABILITIES AS THE NEXT POSITIVE PRESERVATION BOUNDARY INSIDE THE k=2 LEAST-FRESH STAKE SUBCLASS.**

For a reachable epoch state s and a total computable horizon H(s), let p(s) be the exact conditional probability that the sentinel is still avoided after H(s) fillers. It is sufficient that one finite computable budget bound the sum of p(s) over all reached epoch states on every run.

The proof does not compute the eventual trigger probability. A globally exhaustive sentinel-first completion supports two computable martingales: a fair unit miss-ticket martingale, funded by the finite tail budget and unbounded on infinitely many misses; and a finite-horizon conditional-expectation hedge which tracks the output martingale exactly on good epochs, copies filler bets after a miss, skips only the already-revealed sentinel wager if that epoch later triggers, and restarts. Their sum succeeds whenever the output martingale succeeds. P4-S001 transfers that completion win to one computable source martingale.

The condition is strictly weaker than P4-S013 finite deadlines. The zero-stake wait-for-next-1 functional has a genuine all-zero infinite avoiding sibling at every reached epoch, while horizons H_r=r+2 have total miss budget at most 1/2.

P4-S011 necessarily violates this condition: otherwise its successful output martingale would transfer to a computable martingale succeeding on its computably random source.

This is a sufficient boundary, not an absolute necessity result. A stake-weighted weakening remains open. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S014_MATHEMATICS.md.


## D-0037 — charge finite-horizon misses by possible positive skipped-sentinel gain, not by unit mass

Session: P4-S015
Date: 2026-10-06
Decision: **USE A COMPUTABLE LEAF-DEPENDENT POSITIVE SKIPPED-GAIN PRICE AS THE NEXT POSITIVE TRANSFER BOUNDARY INSIDE THE k=2 LEAST-FRESH STAKE SUBCLASS.**

For a given computable output martingale, apply a savings wrapper that preserves or reduces fractional stake sizes and tends to infinity along all late prefixes whenever the original martingale succeeds.

At reachable epoch state s and finite horizon H(s), a miss leaf consists of the prequeried sentinel bit b and a filler string rho in the avoidance tree. Let w(s,b,rho) be a computable rational majorant of the positive multiplicative gain of any later sentinel wager that would be skipped from that leaf. The exact finite fair ticket price is
c(s)=2^{-(H(s)+1)} sum_rho(w(s,0,rho)+w(s,1,rho)).
A single finite computable pathwise budget on the sum of c(s) is sufficient.

Weighted tickets succeed when realized miss weights diverge. Otherwise the P4-S014 restart hedge loses at most factors 1+w and keeps a positive scale against the savings-wrapped output martingale. Thus one completion martingale, and hence one source martingale via P4-S001, succeeds whenever the certified output martingale succeeds.

The coarser condition sum p(s)a(s)<infinity follows when a computable epoch weight a(s) uniformly bounds possible positive post-horizon sentinel gain. Raw miss probabilities may be nonsummable.

The boundary is strictly below P4-S014: an explicit two-control-bit scan has permanent avoidance probability 1/4 at every epoch, excluding every raw-tail certificate, while small sentinel stakes have total weighted price at most 1/4.

The exact pointwise minimal envelope need not be computable, so an effective envelope or stronger computable data is a real hypothesis. P4-S011's all-in correct-prediction destroyer has no finite certificate of this form.

This is programme mathematics, not a novelty finding or an absolute necessity theorem. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. DEF-0020 is unchanged. No k>2, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S015_MATHEMATICS.md.


## D-0038 — advance future-loss envelopes can be replaced by last-chance one-step insurance

Session: P4-S016
Date: 2026-10-06

Decision/result: inside the k=2 least-fresh stake architecture, P4-S015's advance computable future-loss envelope is not required if the exact fair prices of automatically computed last-chance loss tickets have one finite computable uniform pathwise sum budget.

After a horizon miss, at each unresolved state simulate both possible answers to the next fresh filler. If a child makes the sentinel trigger, compute the savings martingale's exact positive skipped-sentinel gain on that child; otherwise use zero. The one-step fair ticket price is the average of the two losses. This price is automatic and is locally minimal for any one-step hedge covering both child losses.

A reserve funded by the uniform premium budget buys all such tickets. Divergent realized skipped loss makes the insurance account succeed; finite realized loss preserves a positive multiplicative scale for the P4-S015 restart hedge. Their sum transfers every output win through the settled sentinel-first effective isomorphism.

This eliminates the future-envelope effectivity datum but introduces a different conditional pathwise premium budget. No global ordering of the S015 and S016 numerical certificates is claimed.

For the settled P4-S011 destroyer, every computable horizon selector yields divergent realized skipped loss on the computably random target, and the last pre-trigger fair premium is at least half the corresponding realized loss. Hence the S016 premium sum diverges on the target itself.

P4-S011 through P4-S015 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S016_MATHEMATICS.md.

## D-0039 — allow exact last-chance insurance to self-finance, but require coercivity

Session: P4-S017
Date: 2026-10-06

Decision/result: inside the k=2 least-fresh stake architecture, replace P4-S016's absolute pathwise sum bound on last-chance fair premiums, for a fixed horizon/ticket stream, by a **coercive self-financing full-ticket reserve**.

Earlier payouts may fund later premiums. A finite computable initial reserve must make every full-ticket purchase without overdraft on every run. Divergent cumulative realized positive skipped gain must also make the ticket account unbounded. The settled restart hedge handles finite realized loss; their sum transfers success through the sentinel-first effective isomorphism.

P4-S016 implies this condition. Bare solvency does not. A fixed-H separation shows harmonic premiums can be funded by earlier ticket winnings. This does not rule out an old P4-S016 certificate after choosing another horizon.

P4-S011 has no coercive certificate for any computable horizon selector. Bare admissibility alone is not excluded.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S017_MATHEMATICS.md.

## D-0040 — effective coercivity requires uniform bad-capital loss control; semantic coercivity alone does not provide it

Session: P4-S018
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, use a **computable running-maximum coercivity modulus** as the natural effective sufficient certificate: for every integer K, a computable threshold h(K) must ensure that any finite history with realized skipped loss E>=h(K) has already reached ticket capital K.

This certificate may be arbitrarily slow and does not imply absolute premium summability. It is nevertheless strictly stronger than P4-S017 semantic coercivity. Cross-branch finite-loss excursions can be arbitrarily large while every individual infinite bad-capital branch has bounded loss. The exact set-theoretic strengthening is loss-properness b(K)=sup{E(v):W*(v)<K}<infinity.

P4-S011 has no effective modulus for any computable horizon selector. Bare admissibility remains unruled-out there.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S018_MATHEMATICS.md.

## D-0041 — finite loss-properness need not have any computable uniform bound

Session: P4-S019
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, do **not** infer a computable running-maximum coercivity modulus from the set-theoretic condition b(K)=sup{E(v):W*(v)<K}<infinity for every K.

For a computable admissible ticket tree, K -> b(K) is uniformly lower semicomputable. A halting-coded construction using only zero-stake controls and the two settled P4-S017 gadgets has every b(K) finite while no total computable function majorizes them. The finite bad-capital loss heights can therefore encode noncomputable halting-time information.

The exact numerical strengthening sufficient for the P4-S018 proof is effective loss-properness: a total computable U(K) uniformly bounding E on histories with W*<K. This is equivalent, up to a harmless margin, to a computable P4-S018 coercivity threshold.

P4-S011 cannot satisfy set-theoretic loss-properness for any globally admissible full-ticket account; bare admissibility itself remains unruled-out.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S019_MATHEMATICS.md.

## D-0042 — event-level waiting does not effectivize loss-properness; searchable loss levels do

Session: P4-S020
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, do **not** infer effective loss-properness from a computable zero-loss-waiting or next-positive-loss bound. P4-S019 can be heartbeatized with summably small deterministic positive-loss tickets, so positive loss occurs at a fixed computable cadence on every branch that will later realize more loss, while all b(K) remain finite and no computable majorant exists.

Use **loss-level searchability** as the structural positive boundary. A total computable D(K,m) such that every reachable bad-capital loss level m has some witness by depth D(K,m) makes Reach(K,m) decidable. Under loss-properness, the first unreachable integer loss level gives a computable U(K), equivalently the P4-S018 running-maximum coercivity threshold.

This does not restore absolute premium summability. P4-S011 remains outside the set-theoretic loss-proper regime whenever the full-ticket account is globally admissible; bare admissibility remains unruled-out.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S020_MATHEMATICS.md.


## D-0043 — scale-tail data effectivize loss-properness but do not decide exact loss-level reachability

Session: P4-S021
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, a computable local waiting bound for reachable losses at least \(2^{-n}\), together with a computable bound on the cumulative contribution of smaller realized losses in \(B_K\), is a structural sufficient condition for converting set-theoretic loss-properness into effective loss-properness. Coarse-scale accumulated loss is finitely searchable; an unreachable coarse amount plus the subscale bound computes U(K).

Do **not** infer from these scale-tail data that P4-S020's exact predicate Reach(K,m) is decidable. A computable globally k=2, globally admissible construction with global fixed-scale deadlines, effectively vanishing small-loss tails and an explicit linear U(K) can encode halting in whether a shrinking geometric tail attains an integer loss boundary at a finite node or only approaches it.

The next effectivity boundary is anti-Zeno / boundary isolation. Absolute premium summability is not restored.

P4-S011 violates the scale-tail hypothesis under global admissibility because its divergent missed-epoch gains eventually lie below every fixed positive scale. Bare admissibility remains unruled-out.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S021_MATHEMATICS.md.

## D-0044 — exact boundary search needs a strict residual-gap certificate; any full decision compiles to the P4-S020 witness modulus

Session: P4-S022
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, P4-S021 scale-tail data plus loss-properness yield computable fixed-scale exhaustion frontiers. Once losses at scale at least (2^{-n}) are exhausted, a computable residual subscale cap Q gives a finite local nonreachability certificate whenever (E+Q<m).

If every false Reach(K,m) instance eventually receives such a strict frontier certificate, exact Reach is decidable by dovetailing certificate search with the ordinary c.e. finite witness search. No separate bounded-crossing arm is needed.

Do **not** claim this is strictly weaker than P4-S020 in final effective strength. Decidable Reach is already equivalent to a computable witness modulus D(K,m), so the local strict-gap condition only changes the primitive structural data from which D is derived.

The strict inequality is essential. P4-S021's geometric halting construction has an exact computable residual tail equal to the current boundary gap on every divergent finite prefix; a halt pays that residual finitely. Hence nonstrict boundary control leaves halting information intact.

P4-S011 fails the underlying P4-S021 scale-tail hypothesis under global admissibility and so remains outside this boundary-isolation regime.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S022_MATHEMATICS.md.


## D-0045 — strong uniform effective tails turn semantic anti-Zeno into searchable boundary separation

Session: P4-S023
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, computable fixed-scale exhaustion plus a uniformly/effectively vanishing subscale tail makes semantic anti-Zeno sufficient for the P4-S022 strict frontier certificate.

If false Reach(K,m) had no strict certificate, finer frontier nodes would have E arbitrarily close to m. Uniform tail convergence prevents substantial late loss after common prefixes, so compactness turns a diagonal subsequence into an infinite bad-capital branch with limit loss exactly m. False Reach keeps every finite prefix below m, contradicting semantic anti-Zeno.

Therefore exact Reach is decidable under the promise and P4-S020's witness modulus is recoverable. Do not claim an incompatible-branch counterexample under the strong uniform-tail hypothesis.

P4-S011 fails the strong tail hypothesis under global admissibility. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S023_MATHEMATICS.md.

## D-0046 — nonuniform pointwise tail convergence permits an incompatible-branch halting comb

Session: P4-S024
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, distinguish two meanings of branchwise effective tail convergence.

A **single oracle-uniform branch-modulus functional** total on every bad-capital branch is not genuinely weaker than P4-S023's uniform tail regime. The bad-capital tree is computable, finitely branching and pruned under global admissibility. Halting cylinders for the functional form a c.e. open cover of its compact path space; an effective finite-subcover search gives one computable global tail modulus. Semantic anti-Zeno therefore still yields searchable strict frontier gaps and decidable Reach.

By contrast, **genuinely nonuniform pointwise/branchwise effectivity** is insufficient. The P4-S024 incompatible-branch comb is globally k=2, globally admissible, effectively loss-proper and has computable exhaustion of every fixed positive loss scale. Every individual bad-capital branch is eventually loss-constant and semantically non-Zeno. Nevertheless Reach(e+2,2e+2) is equivalent to halting: near-boundary loss moves to later incompatible teeth, while their Cantor-limit spine stays two units below the boundary.

The exact failure is discontinuity of the branch-limit loss. Do not infer searchable Bar from semantic anti-Zeno plus branchwise convergence unless the branchwise tail information has enough effective uniform/topological structure to survive compact limits.

P4-S011 remains outside even the weak pointwise-tail regime under global admissibility. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S024_MATHEMATICS.md.

## D-0047 — effective upper caps compactify; semantic continuity need not effectivize the gap

Session: P4-S025
Date: 2026-10-06

Decision/result: inside the k=2 least-fresh ticket/restart architecture, a complete effective upper-semicontinuity presentation of the bad-capital branch-limit loss is sufficient with semantic anti-Zeno, but it is not a genuine weakening of P4-S023's computable global tail modulus.

A c.e. sound local upper-cap basis can be refined to cylinders on which the cap lies within \(2^{-n}\) of the current finite-prefix loss. Pointwise convergence makes those cylinders cover the computable pruned bad-capital branch space. Effective compactness finds a finite subcover, yielding a computable global uniform tail modulus. Conversely, a computable uniform tail modulus enumerates such an upper-cap basis. Semantic anti-Zeno then gives the P4-S023 strict frontier certificate and decidable Reach.

Ordinary upper-semicontinuity is not enough effectively. A delayed-activation exact global-k=2 admissible comb has continuous branch-limit loss, eventual constancy and semantic anti-Zeno on every bad-capital branch, computable fixed-scale exhaustion and effective loss-properness, yet Reach(e+2,2e+2) is equivalent to machine-e halting. The missing information is the effective upper-cap / continuity modulus.

Boundary-specific effective caps can be weaker as primitive syntax, but if they uniformly cover every false integer Reach instance they are exactly a topological presentation of semidecidable Bar(K,m), hence recover P4-S020 searchability.

P4-S011 remains outside even the semantic finite-limit regime under global admissibility. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S025_MATHEMATICS.md.

## D-0048 — integer-boundary caps separate from full effective usc, but boundary completeness collapses to Reach searchability

Session: P4-S026
Date: 2026-10-06

Decision/result: inside the settled k=2 last-chance-ticket/restart architecture, distinguish representation strength from final searchability strength.

One-sided integer-boundary upper information is genuinely weaker as presentation data than P4-S025's complete effective rational upper-cap basis. A computable globally admissible exhaustive ticket stream can have constant branch-limit loss
\[
\alpha=\sum_{e\in H}4^{-(e+2)}<1/4
\]
for a c.e. noncomputable set \(H\). Every integer boundary \(m\ge1\) then has the trivial root cap \(1/4\), while a complete rational upper-cap basis would make \(\alpha\) right-c.e.; together with its left-c.e. approximation this would make \(\alpha\) computable.

However, any uniformly c.e. sound local boundary-certificate system which is complete for all branches with \(L_K<m\) collapses, under semantic anti-Zeno, to the already-settled P4-S020 searchability level. If Bar(K,m) is true, anti-Zeno makes every bad-capital branch strictly sub-boundary; the certified cylinders cover the computable pruned branch space, and effective compactness finds a finite subcover. Thus true Bar is positively semidecidable. Since Reach already has c.e. finite witnesses, Reach is decidable and the P4-S020 witness modulus is recoverable.

This collapse is independent of the certificate syntax: rational caps, residual bounds, oracle-uniform integer-clearance functionals and arbitrary c.e. local strict-sublevel certificates all behave the same once they are sound and boundary-complete.

P4-S011 is preserved exactly. Under global admissibility it still has a bounded-capital branch with divergent realized skipped loss, so it lies outside the full finite-limit P4-S025 regime. The weaker P4-S026 boundary-only notion need not fail on that branch, because every integer boundary is eventually reached there. Bare admissibility remains unruled-out.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S026_MATHEMATICS.md.

## D-0049 — a use-exhausting horizon makes the P4-S011 full-ticket account globally solvent

Session: P4-S027
Date: 2026-10-06

Decision/result: the settled P4-S011 wtt destroyer may be put in a globally use-clipped normal form without changing its computably random target or its exact global-k=2 scan argument. The wtt use bound, although unnecessary for the destroyer conversion itself, then yields a computable finite dependency frontier at every sentinel epoch.

Choose the P4-S016 horizon only after all still-unqueried non-sentinel coordinates inside that frontier have been exposed. If the epoch is still unresolved, later halting visibility may depend on more simulation time but cannot depend on any future filler value.

Therefore at every unresolved postmiss node both next-filler children either remain unresolved or trigger with the same prediction and the same positive skipped gain (ell). The exact P4-S016 fair ticket has payoff vector ((ell,ell)), so its premium is (ell) and it repays that amount surely. Because (0leellle1), reserve R=1 makes the canonical full-ticket account globally admissible and its resolved capital remains exactly one.

Do not infer transfer or preservation. On the P4-S011 target, cumulative realized skipped gain and cumulative premium both diverge while ticket capital is bounded, so coercivity and loss-properness fail maximally. This is fully consistent with P4-S016 through P4-S026.

The result is stated for the harmless globally use-clipped representative of the wtt witness. No claim is made for every arbitrary unnormalized off-target implementation of the same reduction.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: `phase4/P4-S027_MATHEMATICS.md`.


## D-0050 — finite dependency exhaustion, not wtt syntax, is the bare-solvency mechanism

Session: P4-S028
Date: 2026-10-06

Decision/result: inside the settled k=2 P4-S012 / P4-S016–P4-S017 least-fresh architecture, P4-S027's wtt use bound is stronger than the bankroll proof needs.

It is sufficient to have a computable finite dependency frontier D(s) at every reachable epoch state s such that, once D(s) is exhausted, all later trigger data for the current sentinel are independent of future filler values. A computable least-fresh horizon can exhaust D(s). After that horizon, both next-filler children have identical trigger data and, because the canonical output martingale and its savings wrapper are flat on fillers, identical positive skipped gain. Every positive last-chance ticket is deterministic. Its fair premium equals its certain payout and is at most one, so reserve R=1 is globally admissible.

This finite-frontier condition is not forced by P4-S012. A self-avoiding first-1-search predictor gives an exact total fair-coin-preserving global-k=2 scan whose first epoch has no finite dependency frontier. On the sentinel-first sibling with stored sentinel bit 1 and every later filler 0, after any finite horizon every next filler still offers a one-sided all-in trigger: the loss vector is (0,1), the fair premium is 1/2, and the actual payout is 0. Repeating this produces deficit N/2 after N tickets, so no finite reserve is globally admissible for any finite horizon selector.

Do not promote this to a necessity theorem. P4-S028 shows that finite frontiers are a clean sufficient structural mechanism and that the broader P4-S012 class contains exact opposite reserve behavior. It does not show that every no-frontier predictor is insolvent; decaying one-sided skipped gains remain a live separation question.

P4-S011 remains unchanged and lies on the positive side because P4-S027's globally use-clipped witness supplies exactly such a finite frontier. P4-S015 through P4-S027 remain settled.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S028_MATHEMATICS.md.


## D-0051 — finite dependency frontiers are sufficient but not necessary for bare solvency

Session: P4-S029
Date: 2026-10-06

Decision/result: inside the settled k=2 P4-S012 / P4-S016–P4-S017 least-fresh architecture, reject finite dependency frontiers as a necessary condition for bare canonical full-ticket admissibility.

Reuse the exact P4-S028 first-1-search scan. Its initial epoch still has no finite dependency frontier: after every finite zero filler prefix, a later unseen bit can still decide whether the sentinel triggers. The scan remains total, no-repeat, fair-coin preserving and globally k=2.

Change only the output martingale. If the first 1 occurs at filler n, make one fractional sentinel wager of size (2^{-n}) on bit 1 and freeze thereafter. With H=1, on the stored-sentinel-1 branch the postmiss last-chance tickets are ((0,2^{-n})) and cost (2^{-(n+1)}), for every n>=2. These one-sided opportunities persist arbitrarily late, but the whole premium tail sums to 1/4. Therefore reserve R=1/4 is globally admissible.

More generally, in this same no-frontier geometry a positive stake sequence (alpha_n) gives premium (alpha_n/2) on the all-zero avoiding sibling. Summable tails give finite reserve; divergent tails give unbounded zero-payout deficit. P4-S028 is the constant (alpha_n=1) case. P4-S011/P4-S027 is different: frontier exhaustion makes tickets deterministic, so certain payouts recycle reserve even with divergent premium sums.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S029_MATHEMATICS.md.


## D-0052 — no-frontier one-sided tickets can recycle a finite reserve across divergent premiums

Session: P4-S030
Date: 2026-10-06

Decision/result: inside the settled k=2 P4-S012 / P4-S016–P4-S017 least-fresh architecture, divergent cumulative canonical premiums are compatible with bare global admissibility even when every active epoch has no finite dependency frontier and genuinely one-sided trigger opportunities remain at arbitrarily late fillers.

Use an active/dead least-fresh stake functional. In every active epoch, one dummy filler is ignored and H=1 is missed. Thereafter search fresh fillers for the first 1. If it appears immediately, stake 1 on the sentinel being 1; if it first appears at later post-horizon depth m>=2, stake 2^{-m}; if no 1 appears, diverge. An immediate favorable trigger renews another active epoch. Any late trigger or unfavorable sentinel sends all later epochs to zero-stake dead mode.

After r immediate favorable renewals, the P4-S015 savings wrapper has savings r, active risk 1 and total capital r+1. Thus the immediate positive skipped gain is a_r=1/(r+1), while the depth-m late gain is a_r 2^{-m}. The one-sided ticket premiums are a_r/2 at depth 1 and a_r 2^{-(m+1)} at m>=2. The entire unreplenished premium exposure of one active epoch is therefore 3a_r/4 <= 3/4.

Reserve R=3/4 is globally admissible. An immediate favorable ticket costs a_r/2, pays a_r and renews the process, so the account gains a_r/2. A 0-child exposes only the summable late tail; a later trigger or nontriggering continuation ends all future positive ticket cost. On the all-immediate-favorable completion, premiums are 1/(2(r+1)) and diverge harmonically, while payouts fund later premiums and the ticket bank grows.

This is genuine one-sided P4-S017 recycling, unlike P4-S011/P4-S027 deterministic-ticket recycling and unlike P4-S029 absolute premium summability. P4-S028's obstruction remains exact: a zero-payout sibling with divergent remaining premium deficit still defeats every finite reserve.

P4-S005 through P4-S029 remain settled. P4-S011 and P4-S015 through P4-S029 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S030_MATHEMATICS.md.

## D-0053 — terminalization is not necessary; a positive renewal reserve potential can fund repeatable late triggers

Session: P4-S031
Date: 2026-10-06

Decision/result: inside the settled k=2 P4-S012 / P4-S016–P4-S017 least-fresh architecture, reject P4-S030's late-trigger terminalization as a necessary condition for bare global full-ticket admissibility.

Use active epochs with a positive dyadic scale c. After one ignored dummy filler, search for the first 1. An immediate trigger uses fractional stake c and renews the next active epoch at the same scale. A later trigger at depth m>=2 uses stake c2^{-m} and renews the next active epoch at scale c/4. No finite trigger enters dead mode.

For any P4-S015 savings-wrapper state, if beta is active risk divided by total capital, the depth-1 premium is beta c/2 and the complete later premium tail is beta c/4. Thus one active epoch can draw down at most 3c/4. The invariant W>=c closes with initial reserve R=1: immediate positive triggers are self-financing, and after a late trigger at least c/4 remains even if its payout is ignored, exactly matching the next active scale c/4.

Every renewed scale is positive, so every finite trigger — including arbitrarily late triggers and either sentinel outcome — starts another epoch with no finite dependency frontier and arbitrarily late genuinely one-sided ticket opportunities.

On the all-immediate-favourable completion the scale stays one. The savings wrapper has active-risk ratio 1/(r+1), so premiums 1/(2(r+1)) diverge harmonically and payouts 1/(r+1) genuinely finance later tickets.

The new structural lesson is a renewal reserve potential: terminalization sets the next exposure budget to zero, while P4-S031 leaves it positive but contracts it enough to fit inside the residual bankroll. This is sufficient, not claimed necessary.

P4-S005 through P4-S030 remain settled. P4-S011 and P4-S015 through P4-S030 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S031_MATHEMATICS.md.
