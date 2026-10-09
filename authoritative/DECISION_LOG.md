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

## D-0054 — freeze the local bankroll sequence and pivot Phase 4 to a theory of finite inverse ambiguity

Date: 2026-10-06
Type: programme-level research-direction decision after P4-S031

Decision: preserve all validated mathematics through P4-S031, but stop using the next unresolved ticket/reserve/frontier/recycling refinement as the automatic Phase-4 scheduler.

The new organising question is:

> What mathematical resource is exposed by the jump from injective observation to one binary degree of inverse ambiguity, and what else does that resource control?

Future sessions should treat P4-S001's k=1 preservation result and P4-S011's k=2 destruction result as base points of a broader mathematical theory. The main forward axes are:

- robustness classes R_k and source-side characterizations;
- structural conditions strictly between injective and bare finite-to-one observation;
- reverse/randomness-creation effects;
- selected comparisons across randomness notions;
- composition, factorisation and ambiguity budgets;
- identification of a structural resource deeper than fibre cardinality;
- systematic mutations of P4-S011;
- converse results from vulnerability to predictive/autoreductive source structure.

P4-S032 is therefore a reconnaissance/theorem-selection session, not a continuation of the stationary late-trigger reserve question scheduled before this decision. It should compare several routes with exact mathematical work and select the deepest theorem target for sustained multi-session pursuit.

The old strict-k=2 restriction was session-local to the previous trajectory. It is no longer the default when finite k>2, composition or factorisation is mathematically necessary for this finite-ambiguity theory. This decision itself asserts no k>2 theorem.

No settled result is reopened. The P4-S015–P4-S031 line remains available as machinery when a deeper theorem needs it.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, prior-art, Gate-4, publication or outreach claim is made.

Authority record: phase4/P4_RESEARCH_PIVOT_AFTER_S031.md.


## D-0055 — select one-hole normalization as the sustained finite-ambiguity theorem target

Session: P4-S032
Date: 2026-10-06
Type: Phase-4 mathematics theorem-selection decision

Decision/result: after exact reconnaissance across robustness, structural thresholds, composition and scan/source-side mechanisms, select **one-hole normalization** as the next sustained theorem programme.

P4-S032 first proves a structural preservation theorem. For an everywhere-total computable fair-coin-preserving F, let A_F be the outputs with at least two preimages. If lambda(A_F)=0, then the singleton-fibre locus supports a partial computable inverse whose domain is a full-measure constructive G_delta. The inverse is fair-coin preserving on that domain, so THM-0038 gives computable-randomness preservation. No finite global fibre bound and no effective-null presentation of A_F are needed.

The boundary cannot be promoted to an ambiguity-mass invariant. Localizing the P4-S011 destroyer inside a clopen cylinder gives exact global-k=2 destroyers with positive ambiguity measure below any prescribed epsilon. Conversely the P4-S002 left shift is exactly two-to-one everywhere and preserves computable randomness. Thus zero ambiguity mass is safe, but neither small positive nor full ambiguity mass determines behavior.

P4-S032 also proves the scan ambiguity-budget identity: an adaptive no-repeat transcript omitting h<infinity source coordinates has exactly 2^h preimages. Global k=2 is therefore exactly a one-hole constraint in the scan subclass. On the P4-S011 vulnerable target, however, no coordinate is omitted in the limit and the final fibre is singleton. The relevant resource is therefore **renewable counterfactual one-hole ambiguity**: a fresh bit can be withheld long enough to support a self-avoiding wager, consumed, and replaced by another withheld bit.

Define OH as the CR sources robust under every total computable one-hole adaptive no-repeat scan. Then R_2 subseteq OH, and P4-S011 plus P4-S012 makes OH a concrete source-side class with a stake-level failure mechanism.

Selected theorem target:

> Determine whether R_2=OH.

A positive result would normalize arbitrary binary-ambiguity destruction to the P4-S012 self-avoiding scan/stake mechanism. A negative result must construct a genuinely non-scan k=2 destroyer and identify the additional resource.

This target outranks direct R_2-versus-MLR classification because it first asks for the mechanism of arbitrary k=2 failure. It outranks ambiguity-mass refinement because that parameter has already been shown non-characterizing. It outranks binary factorisation because P4-S032 proves that factorisation alone does not propagate R_2 robustness through the intermediate image.

The bounded follow-up plan is P4-S033 through at most P4-S036 as warranted: first normalization from the effective width-two inverse skeleton; then non-coordinate mixing/homeomorphism conjugacy; then the strongest surviving structured subclass; only after that compare the resulting invariant with MLR or the finite-hole hierarchy.

P4-S005 through P4-S031 remain settled; the local ticket/reserve trajectory stays frozen. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, prior-art, Gate-4, publication or outreach claim is made.

Record: phase4/P4-S032_MATHEMATICS.md.

## P4-S033 — select homeomorphism invariance as the next normalization test

Date: 2026-10-06
Decision: **LITERAL SCAN NORMALIZATION IS TOO STRONG; TEST HOMEOMORPHISM INVARIANCE OF OH NEXT**

P4-S033 proves that the P4-S007 width-two inverse skeleton supplies one binary cohort but not a raw coordinate hole. One-hole scan double fibres differ at exactly one raw coordinate.

The session proves R_2 is invariant under every computable fair-coin-preserving homeomorphism and defines OH^iso with

R_2 subseteq OH^iso subseteq OH.

Thus R_2=OH requires OH to be homeomorphism-invariant. OH invariance is proved for signed coordinate permutations.

A blockwise three-bit linear precomposition of the P4-S011 destroyer preserves totality, fair coin, fibre bound two and destruction while spreading every scan double-fibre unit difference to raw Hamming weight 2 or 3. Hence the resulting map is not a one-hole scan and cannot be made one by an output homeomorphism. This exact destructive **coded-hole** architecture shows literal map-level normalization is false without deciding the source-class equation.

Decision for P4-S034: test OH invariance under the explicit three-bit homeomorphism at the P4-S012 stake level. Do not return to the frozen bankroll sequence.

Guards: PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged; no novelty, Gate-4, publication or outreach conclusion.

## D-0056 — treat late-decision spoiled gain as the next coded-hole obstruction

Session: P4-S034
Date: 2026-10-06
Type: Phase-4 mathematics theorem-selection refinement

Decision/result: finite source recoding is now on the positive side of the one-hole normalization boundary, while the repeated three-bit recoding is reduced to an infinitary delayed-stake problem.

P4-S034 proves that OH is invariant under every computable finite-coordinate fair-coin recoding. This strictly enlarges P4-S033's signed-coordinate-permutation class: a finite CNOT recoding is allowed. Hence every finite truncation of the explicit repeated three-bit mixer preserves OH.

At the P4-S012 level, direct pullback through the mixer yields vector-self-avoidance rather than raw-coordinate self-avoidance. A canonical support evaluator nevertheless turns every virtual one-hole scan for a repeated invertible binary block matrix into a raw one-hole scan. For the displayed matrix this evaluator is exhaustive. It copies all virtual wagers made while a fresh raw pivot remains and skips only **spoiled** wagers whose parity has already become determined in raw time.

Since the evaluator is an effective isomorphism, copied live-pivot wagers cannot give an unbounded computable martingale on a computably random raw source. Any surviving destruction must therefore carry unbounded multiplicative gain in the spoiled wagers.

Decision for P4-S035: formalize the determination-time versus stake-selection-time gap. First settle the early-decided case, where a spoiled stake is already known when its last raw pivot is exposed; then attack the genuinely late-decision case.

No OH non-invariance witness is established, so no strict \(R_2\subsetneq OH\) claim is made. \(OH^{iso}\) remains the comparison class.

The P4-S015–P4-S031 bankroll sequence remains frozen as the default route. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no novelty, prior-art, Gate-4, publication or outreach conclusion is made.

Record: phase4/P4-S034_MATHEMATICS.md.

## D-0057 — finite packet closure is safe; select infinite dependency closure

Session: P4-S035
Date: 2026-10-06
Type: Phase-4 mathematics theorem-selection refinement

Decision/result: the P4-S034 spoiled-stage obstruction is not caused by finite delayed choice inside a fixed region of the source.

For the displayed three-bit recoding, every spoiled stake uniformly determined before its raw determination pivot transfers exactly to a raw martingale. Same-pivot late choice reduces to an exact scalar late-choice premium.

More strongly, for every repeated invertible finite binary block recoding of block size at least two, every block-closed or uniformly bounded packet-closed one-hole witness preserves computable randomness. Finite packet behaviour is exactly compressible by raw Doob conditional expectations.

Bounded decision delay does not imply packet closure. There is an exact one-hole architecture with a pending spoiled parity in block \(b\) whose stake depends on information first exposed in block \(b+1\), recursively, producing an infinite dependency ray with no finite closed packet.

Decision for P4-S036: formalize the dependency graph and test finite/well-founded closure versus infinite rays. Do not infer OH non-invariance from the architecture alone.

The P4-S015–P4-S031 bankroll sequence remains frozen as the default route. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no novelty, prior-art, Gate-4, publication or outreach conclusion is made.

Record: phase4/P4-S035_MATHEMATICS.md.

## D-0058 — replace packet-size/rank criteria by effective closed packetization and backward-price stabilization

Session: P4-S036
Date: 2026-10-06
Type: Phase-4 mathematics theorem-selection refinement

Decision/result: the finite side of the coded-hole obstruction is now controlled by **effective closed packetization**, not by a uniform packet-size bound and not by dependency rank.

P4-S036 uses an exact persistent-savings transform to make every virtual martingale win persistently. This removes the only use of uniformly bounded packet cardinality in P4-S035. Every computably finite packet-closed witness, and more generally every witness admitting a total computable online finite closed packetizer, normalizes by finite Doob conditional expectations.

Finite forward closure / well-foundedness is not the same effective resource. Rank-one examples show both that closure completion can encode halting information and that uniformly computable finite forward closures can overlap into an infinite symmetrized interaction component even with no directed infinite ray.

For the explicit P4-S035 ray, raw coordinate reordering cannot retain a pivot after \(u_0,u_1\) are known. Yet every finite truncation has exact conditional-expectation compression. The selected obstruction is therefore the **effective stabilization of the finite-horizon backward fair-price vector of the open boundary claims**.

Decision for P4-S037: attack rolling finite-state normalization on infinite interaction components. Test bounded open-claim width, finite boundary-state dimension, telescoping/contraction and computable Cauchy/projective moduli. Compare the simple ray, the no-ray rank-one overlap architecture and the actual recoded P4-S011 schedule.

No OH non-invariance witness is established. The P4-S011 recoded source remains only known to be in \(CR\), not in \(OH\). The P4-S015–P4-S031 bankroll sequence remains frozen as the default route.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no novelty, prior-art, Gate-4, publication or outreach conclusion is made.

Record: phase4/P4-S036_MATHEMATICS.md.



## D-0059 — replace infinite-component geometry by effective claim retirement

Session: P4-S037
Date: 2026-10-06
Type: Phase-4 mathematics theorem-selection refinement

Decision/result: the infinite-component obstruction selected in P4-S036 splits into a positive rolling-renewal case and a sharper persistent-claim case.

A computable finite frontier transition which retires all old spoiled claims and hands off only to new virtually unseen fair parities gives exact backward-price cancellation. Persistent savings then transfers virtual success to one computable raw martingale.

This theorem normalizes both the explicit P4-S035 directed ray and the concrete P4-S036 rank-one overlap component. Therefore neither directed rays nor infinite weak interaction components are the decisive invariant.

The recoded P4-S011 witness rules out a simpler width/conditioning criterion. It has active nonzero frontier width one; with half-stake sentinel bets its local triggered price vectors have entries in ([1/2,3/2]) and ratio at most (3), yet destruction persists. Its wtt use frontier makes source-value dependence finite but does not make eventual claim retirement decidable.

Decision for P4-S038: attack non-effective retirement/backward-price stabilization in the actual P4-S011 persistent frontier. Test the weakest computable retirement, summable unresolved-price tail, or optional-projection condition sufficient for a raw compiler, and whether one-hole geometry forces it.

No OH non-invariance witness is established. (OH^{iso}) remains the comparison class. The P4-S015–P4-S031 bankroll sequence remains frozen.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no novelty, prior-art, Gate-4, publication or outreach conclusion is made.

Record: phase4/P4-S037_MATHEMATICS.md.


## D-0060 — close local persistent-price compilation and select same-source one-hole simulation

Session: P4-S038
Date: 2026-10-07
Type: Phase-4 mathematics theorem-selection refinement

Decision/result: the persistent single-claim obstruction selected by P4-S037 is now classified at the backward-price level.

After the P4-S011 wtt value-use frontier is exhausted, the claim is value-closed but may retire only c.e. The half-stake normalized price has exactly one possible nontrivial jump from \((1,1)\) to \((3/2,1/2)\) or its reversal.

For any fixed positive jump size, computable retirement deadlines, eventual-constancy/Cauchy moduli, exact limiting prices and two-sided retirement semidecisions all collapse to the trigger/nontrigger decision. The actual recoded P4-S011 family cannot have that uniform decision or an absolute persistent-savings Cauchy modulus, since P4-S037 would then contradict \(X\in CR\).

A distinct positive compiler condition is available: if unresolved stake magnitudes \(r_e\) have a computable finite multiplicative uncertainty budget \(\prod_{e<n}(1+r_e)\le K\), the worst possible orientation can be prepaid. Persistent savings plus this reserve gives a computable raw supermartingale and a computable martingale cover without deciding retirement.

This condition is sharp for the pure all-correct sentinel mechanism because the target gain is exactly the same product. Therefore stake decay cannot preserve unbounded sentinel gain while making the unresolved positive hedge cost finite.

Decision for P4-S039: stop tightening ordinary raw-martingale retirement/pricing criteria for the actual P4-S011 source. Attack the missing same-source statement directly by testing whether the c.e.-persistent virtual sentinel process on \(H(X)\) can be simulated by a total raw-coordinate one-hole scan/stake process on \(X\). Begin with the exact one-hole linear algebra of the displayed three-bit block recoding and cross-block transport of the unresolved parity state.

No \(X\in OH\) is established. No OH non-invariance or \(R_2\subsetneq OH\) conclusion is made. \(OH^{iso}\) remains the comparison class. The P4-S015–P4-S031 bankroll sequence remains frozen.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no novelty, prior-art, Gate-4, publication or outreach conclusion is made.

Record: phase4/P4-S038_MATHEMATICS.md.

## D-0061 — replace finite-rank simulation by the c.e. local-code completion target

Session: P4-S039
Date: 2026-10-07
Type: Phase-4 mathematics theorem-selection refinement

Decision/result: the direct three-bit source-side analysis separates exact virtual transcript simulation from same-source vulnerability.

With one omitted raw coordinate, the virtual block is an affine rank-one state \(u=a+hAe_i\). Exact simulation of a unit virtual sentinel requires \(2,2,3\) raw unresolved coordinates and cannot be migrated to another block through one raw hole.

However the three actual P4-S011 autoreduction equations define a local c.e. consistency code \(C_B\) with minimum Hamming distance at least two. For the displayed matrix every such code fixes at least one raw coordinate. Two visible consistent assignments already give a finite coordinate certificate.

For a preselected raw target, the exact alternatives are finite rejection, a second self-consistent raw endpoint, or divergence-only failure of the alternate endpoint. The first gives a raw self-avoiding predictor. The latter two isolate the remaining one-bit circular / c.e.-singleton-completion obstruction.

A positive theorem is retained: for the displayed matrix, and more generally every raw-hyperplane-coding invertible three-bit matrix, local sibling totality of the 24 finite perturbation computations yields a total raw one-hole destroyer on the same source.

Decision for P4-S040: attack online c.e. local-code completion and raw-adjacent companions under a preselected raw sentinel. Test whether the Case-B/Case-C arms can be bypassed while preserving a global one-hole scan; otherwise prove a precise stall invariant.

No actual raw destroyer for \(X\) is established and no \(X\in OH\) is established. No OH non-invariance or \(R_2\subsetneq OH\) conclusion is made. \(OH^{iso}\) remains the comparison class. The frozen P4-S015–P4-S031 bankroll sequence and the P4-S038 ordinary backward-price route remain closed as default directions.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no novelty, prior-art, Gate-4, publication or outreach conclusion is made.

Record: phase4/P4-S039_MATHEMATICS.md.

## D-0062 — replace full local sibling totality by raw-adjacent decisiveness

Session: P4-S040
Date: 2026-10-07
Type: Phase-4 mathematics theorem-selection refinement

Decision/result: the P4-S039 positive same-source theorem does not need completion of all 24 local sibling computations.

For a raw target direction \(i\), the raw-adjacent companion differs virtually by \(Ae_i\). Call it decisive when it is either locally self-consistent or finitely refuted by one wrong/nonbinary autoreduction halt.

If all three raw directions are decisive on every reached synchronized block, three raw one-hole scans suffice. Case A yields a correct all-in wager; Case B yields a zero-stake closure. The local minimum-distance-two code law prevents all three companions from being accepted, so every block supplies at least one Case-A wager across the three scans. Infinite pigeonhole gives one fixed successful scan.

This condition is materially weaker than full local sibling totality: a finitely refuted companion may have other divergent computations and unrelated local candidates may diverge.

The Case-B two-codeword certificate is not a prospective handoff resource. Raw-adjacent endpoints differ only at the current raw sentinel, so every raw coordinate they certify has already been queried.

Global one-hole geometry also forbids two permanent reservations: on a complete branch where the current sentinel is never queried, every other raw coordinate must eventually be queried.

The sharp surviving local obstruction is therefore divergence-only Case C. Extra outside \(M(n)\)-equations can only add c.e. finite refutations; the wtt use bound gives no computably finite reverse closure of all computations affected by the changed block.

Decision for P4-S041: attack **finite-perturbation refutability** for the actual wtt-autoreduction presentation. Test whether a target-equivalent self-avoiding wtt normal form can make every raw-adjacent finite perturbation either another fixed point or finitely refutable without imposing full sibling totality.

The actual P4-S011 machine is not known to satisfy the new decisiveness condition. No actual raw destroyer for \(X\), no \(X\in OH\), no OH non-invariance and no \(R_2\subsetneq OH\) conclusion is made. \(OH^{iso}\) remains the comparison class.

The P4-S015–P4-S031 bankroll sequence and P4-S037/P4-S038 backward-price route remain frozen as default directions. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 is unchanged; no novelty, prior-art, Gate-4, publication or outreach conclusion is made.

Record: phase4/P4-S040_MATHEMATICS.md.
## P4-S041 — finite-perturbation partiality is forced; only raw-radius-one partiality can remain relevant

Date: 2026-10-07
Decision type: Phase-4 mathematics checkpoint
Status: **VALIDATED**

The P4-S040 divergence-only boundary is sharpened.

For the committed syntactically self-avoiding wtt autoreduction \(M\) of the P4-S011 computably random source \(Y\), totality on every finite perturbation of \(Y\) would make every finite answer pattern below the computable use halt. The finitely many patterns can then be dovetailed into a total truth table, yielding a truth-table autoreduction of \(Y\). The retained source authority excludes this. Therefore some finite perturbation necessarily makes some \(M(n)\) diverge.

Under the repeated invertible three-bit recoding define \(\rho\) to be the least number of raw coordinates whose simultaneous flip causes any divergence. Then
\[
\rho\ge2\Longrightarrow X\notin OH.
\]
Reason: totality on every radius-one raw companion makes all three local block computations halt, hence every companion is P4-S040-decisive, and the validated three-scan theorem applies. Consequently any still-possible branch \(X\in OH\) requires \(\rho=1\).

Do not identify \(\rho=1\) with P4-S040 Case C. Radius-one divergence may be remote from the block equations or may coexist with a finite local wrong halt.

If a finite perturbation is genuinely fixed on its changed coordinates, self-avoidance forces a directed dependency cycle among those changed coordinates. For the displayed raw-adjacent supports, \(011\) and \(101\) force two-cycles; \(111\) gives a two-cycle with a tail or an oriented three-cycle. These cycles classify positive Case B and do not certify Case C.

The pairwise raw-adjacent identity further yields
\[
B_0\Rightarrow A_1,A_2,\qquad B_1\Rightarrow A_0,\qquad B_2\Rightarrow A_0.
\]
Therefore a block with no finite-refutation direction is necessarily triple Case C.

No uniform target-equivalent totalization is licensed by the wtt use bound: the finite use table has only a c.e. halting domain and a compiler cannot use \(Y\) as a noncomputable parameter.

Decision: keep the present source alive only on the narrower raw-radius-one localization question. Run P4-S042 on whether remote radius-one divergence must propagate into the local block family or can coexist with local decisiveness.

No \(X\in OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.

## P4-S042 — remote divergence does not localize per witness; OH survival forces recurrent local Case C

Date: 2026-10-07
Decision type: Phase-4 mathematics checkpoint
Status: **VALIDATED**

The P4-S041 raw-radius-one boundary is sharpened.

If a radius-one companion diverges at any input while the target computation halts, the finite target trace must query the changed support. Iterating this finite first-contact information inside the support yields a lasso whose semantic endpoints are: finite local refutation, local divergence, or a correct local dependency cycle.

The third endpoint cannot be removed by minimal-use reasoning. A computable finite-use self-avoiding countermodel has remote divergence in all three raw directions with local status vector
\[
(A_0,B_1,B_2).
\]
Thus remote partiality can remain genuinely remote while P4-S040 local decisiveness survives.

The programme therefore does not adopt a target-equivalent localization normal form.

A separate tail argument gives the source-side recurrence requirement:
\[
X\in OH\Longrightarrow
\text{infinitely many local Case-C block-direction pairs}.
\]
By finite pigeonhole, some fixed raw direction is Case C on infinitely many blocks. Otherwise one can start the P4-S040 construction after the final Case-C block and obtain a raw one-hole destroyer.

Decision: keep the current source candidate alive only through the recurrent fixed-direction Case-C regime. P4-S043 should test whether nontriple recurrent Case-C blocks can still be exploited asynchronously, potentially sharpening the necessary obstruction to recurrent triple Case C.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.
## P4-S043 — asynchronous progress is local; the surviving obstruction is online selection/reachability

Date: 2026-10-07
Decision type: Phase-4 mathematics checkpoint
Status: **VALIDATED**

P4-S043 removes one artifact of P4-S040: a scan does not need all three raw-adjacent statuses to become visible before restarting. One selected role can close on its own A/B certificate and move to a fresh block. This is a strict positive extension of the raw one-hole extraction theorem.

The fixed-C status patterns are now completely classified. The P4-S041 implications are the full local finite-table law, with exactly 14 realizable A/B/C triples. Every nontriple recurrent fixed-C block contains visible Case A.

The programme does **not** infer recurrent triple Case C. The missing step is global and online: a computable role must be chosen before its positive status certificate appears, a selected C is absorbing, and the scan's support queries determine which blocks remain fresh. Ambient recurrence therefore does not imply scan-reachable recurrence.

A guaranteed finite abandonment policy is rejected as a destroyer mechanism because it makes the scan exhaustive and returns to the k=1 preservation regime. A finite family of pure wait policies is also insufficient from the current abstract data: a computable structural countermodel on \(0^\omega\) can trap every prescribed member using only nontriple patterns.

Decision: keep the current source candidate alive only through the online selector / fresh-block reachability problem. Run P4-S044 on the actual wtt use horizon and whether it supplies a finite fresh-lane or transient-race selector theorem.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.

## P4-S044 — use horizons close source-value dependence but not certificate-time reachability

Date: 2026-10-07
Decision type: Phase-4 mathematics checkpoint
Status: **VALIDATED**

The P4-S043 online-selector obstruction is sharpened using the actual wtt resource.

For each three-bit block \(B_b\), the strict computable wtt cap gives a uniform raw source-value horizon
\[
V(b)=\max_{r<3}U(3b+r),\qquad
h(b)=\max\{b+1,\lceil V(b)/3\rceil\}.
\]
All six raw-adjacent endpoint computations are source-value closed below this horizon, including divergent computations.

Decision: do **not** treat this as a fresh-target horizon. After source-value closure, positive A/B evidence can still appear after arbitrarily long internal computation. If the current unresolved sentinel and a fixed future sentinel were both protected until that event, a no-event continuation would have two permanent holes. One must be consumed at finite time. Moving reservations preserve global one-hole legality but make the next target depend on certificate time.

The interval family \(I_b=[b,h(b))\) has a finite computable lane cover exactly under uniformly bounded overlap. A bare computable wtt use function does not force this condition, and a countable lane cover is not enough to invoke infinite pigeonhole.

The programme also does not adopt finite transient races as a solution: on the all-C continuation all but at most one prospective sentinel must be consumed, creating finite abandonment times that arbitrarily late finite A certificates can miss.

A computable finite-use structural \(0^\omega\) model with genuine horizon \(h(b)=2b+2\), recurrent nontriple \(C_0\) and visible A witnesses shows these failures are realizable from the abstract machine data.

Decision: move P4-S045 to source-specific **certificate-time selector thickness**. Test whether computable randomness and target-total wtt autoreducibility constrain delayed sibling A certificates enough to defeat every moving-reservation evasion pattern.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.

## P4-S045 — move from certificate-time thickness to live certification access

Date: 2026-10-07

Decision: adopt **faithful moving-reservation selector** as the precise version of the P4-S044 architecture. The selector keeps the current sentinel until its own A/B event, cycles through transient future blocks, and freezes the block active when the event appears. The ambient A set, reservation stream and event-selected targets remain separate.

Decision: use **event-time selector thickness** as the exact positive condition. A C-free A-cofinite computable lane is sufficient, as is finite possible-index coverage coupled to certificate-time domination. Do not treat bounded gaps, positive density, finite-union lane concentration or recurrence on computable subsequences as substitutes without a theorem connecting them to the actual selected indices.

Decision: do not infer a computable-randomness contradiction merely from late certificates. After P4-S044 value closure, the finite certificate clock is determined by already exposed source data and internal computation and has no syntactic dependence on later reservation-block bits. A betting contradiction needs an additional coupling to an unread bit.

Decision: retain the new structural theorem. Any prescribed uniformly computable countable family of faithful moving-reservation selector schemes can be trapped by one computable finite-use self-avoiding \(0^\omega\) model using \(CCA/CAC\), visible A, no triple C, and genuine \(h(b)=2b+2\).

Decision: do **not** promote that theorem to all computable selectors. On a computable target, finite A certificates are c.e. after construction. A new computable selector can enumerate certified A targets and, using their computable target certificate times, reserve each next target only through the required finite window. Thus universal computable-target evasion with infinitely many visible A witnesses is impossible.

Decision: the sustained source-side obstruction is now **live-source certification access**. For the committed noncomputable \(X\), prospective A evidence requires finite source values that a live scan must query. Future work should test whether those values can be obtained without consuming or indefinitely protecting the prospective raw target.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.

Next: P4-S046, future A-certificate access cost.

## P4-S046 — move from target-block access to current-hole-uniform certification

Date: 2026-10-07

Decision: adopt **slice certificate freshness cost** as the exact local measure for future Case-A evidence. Count only live raw coordinates inside the prospective target block; track outside raw support separately.

Decision: retain the automatic self-avoidance theorem. For \(d_r=A^{-1}e_r\), the candidate differs from \(Y\) only at virtual input \(q_r\); syntactic self-avoidance therefore reuses the correct target computation as a finite rejection.

Decision: record the sharp local bound
\[
A_0:\kappa=0,\qquad A_1:\kappa\le1,\qquad A_2:\kappa\le1.
\]
Do not continue treating two non-sentinel raw bits as intrinsically necessary for Case-A certification under this recoding.

Decision: use raw \(011\) / virtual \(110\) as the exact remaining block-free obstruction for \(A_1/A_2\) in the finite positive slice-certificate system.

Decision: retain the \(CAC/CCA\) exact-cost-one gadgets only as structural sharpness witnesses. Their computable target does not transfer selector failure to the committed source.

Decision: do not identify block-free certification with global one-hole compatibility. A future certificate can still depend through outside support on the current open sentinel.

Decision: move P4-S047 to **current-hole-uniform future A certification**: branch prospective evidence over both values of the current sentinel and test whether usable collision-free certification edges can be selected infinitely often.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.


## P4-S047 — old-hole uniformity is a branch-stability resource, not a local-cost consequence

Date: 2026-10-07
Decision type: Phase-4 mathematics checkpoint
Status: **VALIDATED**

P4-S047 formalizes the unresolved current sentinel as exactly two finite counterfactual raw completions. For the displayed recoding the safe old-block virtual rows are

\[
\operatorname{Safe}(0)=\varnothing,\qquad
\operatorname{Safe}(1)=\{u_0\},\qquad
\operatorname{Safe}(2)=\{u_1\}.
\]

Decision: distinguish syntactic old-hole independence from branch uniformity. A finite future rejection trace which avoids the hole-dependent old rows is automatically valid in both old-hole branches, but a trace may touch those rows and still be harmless if both finite branch simulations give compatible evidence.

Decision: adopt **two-branch future fixedness** as a second exact sufficient resource. If the three future target computations halt with the same target-correct values under both old-hole completions, syntactic self-avoidance restores the P4-S046 automatic \(A^{-1}e_r\) rejections in both branches. The P4-S046 local costs \(0,1,1\) then remain available provided the raw-adjacent A rejection itself also survives both branches.

Decision: do not infer two-branch fixedness from target correctness. The counterfactual old-hole completion is a raw-radius-one perturbation, and the retained P4-S041/P4-S042 theory explicitly permits partiality and remote dependence there.

Decision: retain the structural old-row-gating theorem. For every current raw role and every future A role, a computable finite-use syntactically self-avoiding \(0^\omega\) model can gate all future local computations through one old hole-dependent virtual row. The actual branch retains visible \(A_0\), \(A_1\), or \(A_2\) with the P4-S046 local cost, while the alternate old-hole branch diverges before any finite rejection. The patterns \(ACB,CAC,CCA\) suffice.

Therefore no nonempty role-only current-hole-uniform transition matrix, and no infinite collision-escape recurrence, follows from target correctness, self-avoidance, finite use, recurrent nontriple C and the P4-S046 local-cost theorem alone.

Decision: do not treat branch nonuniformity as a prediction of the old sentinel. Both \(h=0,1\) simulations are counterfactual computations from the same observed data. A source-bit prediction requires finite elimination of one current completion itself.

An infinite computable path of current-hole-uniform usable edges would still yield \(X\notin OH\), but no such path is obtained for the committed source.

Next: **P4-S048**, persistent old-hole sensitivity of future A-certificate computations on the actual source. Test whether one current raw-radius-one perturbation can remain semantically essential for infinitely many later A witnesses without exposing the current bit, or whether its influence is effectively escapable into CHU usable edges.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.


### P4-S047 strengthening — finite branch refutation is harvestable

The two-branch formalism yields a stronger source-side necessary condition.

For any current raw completion \(h\), a finite wrong/nonbinary equation
\[
M^{Y^{[h]}}(n)\downarrow\ne Y^{[h]}(n)
\]
eliminates that completion, because the actual branch is total and target-correct. The event is positively discoverable without reading the current raw sentinel: old-block oracle values are supplied by the finite hypothesis and all other raw support is live outside the hole.

Decision: adopt the canonical global-refutation scan which dovetails all \(M\)-equations under both hole hypotheses while sweeping every other raw coordinate. If a false completion is finitely refuted, the scan bets correctly on the current sentinel and restarts. If every epoch resolved, the martingale would double infinitely often.

Therefore
\[
X\in OH
\Longrightarrow
\text{the canonical scan eventually reaches a false raw-radius-one partial fixed point of }M.
\]

At that trap every defined equation is correct; only divergence can hide the false completion.

This sharpens, rather than retracts, the earlier guard: **mere CHU nonuniformity** does not expose the old bit, but an actual finite equation refuting one old-hole completion does.

## P4-S048 — partial fixedness splits canonical future A certification into two independent kernels

Date: 2026-10-07
Decision type: Phase-4 mathematics checkpoint
Status: **VALIDATED**

At an unresolved P4-S047 global-refutation epoch, the false raw-radius-one completion \(Z\) is a partial fixed point. Therefore future target equations have only three source-side types: trace-safe, trace-sensitive but value-fixed, or divergence-sensitive. A divergence-sensitive target trace must contact the old changed support.

Decision: sharpen the P4-S042 support lasso. Under partial fixedness the finite-refutation arm disappears; after first old-support contact the walk reaches either old-support divergence or a correct-halting dependency cycle.

Decision: adopt the canonical false-neighbour role lists
\[
F_0=\{q_0,q_1,q_2\},\qquad
F_1=\{q_0\},\qquad
F_2=\{q_1\}.
\]
These are exactly the target equations needed for the P4-S046 cost-\(0,1,1\) automatic unit-flip traces.

Decision: keep the false-branch raw-adjacent rejection as a separate finite kernel. It lives on the doubly perturbed oracle and is not controlled by partial fixedness of \(Z\).

Decision: retain both P4-S048 structural families. Family F makes one listed equation diverge recurrently through one fixed old row while the false raw-adjacent rejection survives. Family R makes \(Z\) a total fixed point while every false raw-adjacent future candidate diverges; each such doubly perturbed oracle is itself a global partial fixed point. Hence partial fixedness, even total fixedness of \(Z\), does not force CHU escape.

Decision: an actual total computable canonical partial-neighbour escape operator would yield an infinite computable CHU path and \(X\notin OH\). Under hypothetical \(X\in OH\), only the algorithm-relative contrapositive is retained.

Next: **P4-S049**, analyze the two-raw-bit square / partial-fixed-point star and test whether the actual committed source forces a positive finite relation between the false-neighbour target equations and the doubly perturbed raw-adjacent branch.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.
## P4-S049 — trapped square refutations predict the future column

Date: 2026-10-07
Decision type: Phase-4 mathematics checkpoint
Status: **VALIDATED**

At an unresolved P4-S047 global-refutation epoch, the actual-future column of every two-raw-bit square consists of \(Y\) and the false old completion \(Z\). The former is a total fixed point and the latter is a global partial fixed point.

Decision: adopt **actual-column shielding**. Neither corner in the actual-future column can have a finite wrong/nonbinary equation.

Decision: therefore adopt the source-specific one-refutation rule
\[
\boxed{\text{finite refutation of }W_{a,\beta}\Longrightarrow X(t)=1-\beta}
\]
at a genuinely trapped old epoch. The old row label is irrelevant.

Decision: an actual future Case-\(A_j\) raw-adjacent rejection is already one such square refutation. A false fourth-corner rejection is therefore not logically required for one-shot future-bit prediction, although it remains relevant to the older two-row CHU package and to square classification.

Decision: use paired partial-fixed dependency cycles only when the required computations halt on both corners. Divergence terminates the lasso and supplies no edge.

Decision: a genuine false-row local Case B activates the retained P4-S041 role-switch law and hence supplies finite refutations—and future-bit predictions—in alternate raw roles.

Decision: the new effective obstruction is **finite-tenure capture**. With the old sentinel left permanently open, every future target must be transient on a globally legal no-event branch. If a computable finite-tenure policy catches infinitely many square refutations at one trapped old sentinel, it yields a computable one-hole destroyer and \(X\notin OH\).

Decision: under hypothetical \(X\in OH\), every computable finite-tenure square-reservation policy catches only finitely many refutations at the first trapped old epoch. Retain this only algorithm-relatively; do not infer semantic infinitude of no-refutation squares or a computable eventual bound.

Decision: retain the P4-S049 structural full-star model showing that both old rows can have all three future raw-adjacent neighbours globally partial fixed, with total row bases. The model is structural on \(0^\omega\), is not a randomness witness, and lacks the actual-A premise.

Next: **P4-S050**, attack effective activation of the one-refutation square theorem without a semantic trap oracle, using only positive finite square events and globally legal one-hole fallback.

No \(X\in OH\), unconditional \(X\notin OH\), OH non-invariance, \(R_2\subsetneq OH\), novelty, openness, Gate-4, publication or outreach conclusion is made.


## P4-S050 — finite positive pair-hedge activation

Decision: a finite square refutation is a one-pair exclusion **on every old epoch**. Two-bit conditional-expectation betting provides a fair computable exact 4/3 terminal gain on the other three pairs without an old-trap oracle.

Decision: use globally one-hole-safe finite-tenure square exits. A caught pair refutation triggers s-then-t queries and resets the old sentinel; a timeout consumes t but retains s. Optionally combine finite old-branch refutation exits with correct doubled wagers.

Decision: infinite *executed* captured pair exits or infinite combined positive exits under a single computable legal scan imply X not in OH. Do not confuse with passive repeated events sharing a permanent unread old s.

Decision: a single forbidden pair cannot guarantee a strict one-bit gain without further positive information; consuming s to realize the unconditional hedge incurs a reset cost.

Decision: under hypothetical X in OH, every fixed computable combined policy makes finitely many positive exits and eventually persists at a policy-dependent old s with no finite old-branch refutation and no timely square captures. Do not infer semantic absence of later A blocks, a uniform capture clock, or X in OH.

Next: **P4-S051**, test positive multi-square escrow and repeated captures after reset. Preserve R_2 subseteq OH^iso subseteq OH and all unsettled separation guards.


## P4-S051 — opposite-row escrow and turnover boundary

Decision: adopt the future-only rule: two finite positive raw-square refutations against opposite old values at distinct unread future targets exclude a joint future tuple. Fair two-target hedging guarantees 4/3 without reading old s. No semantic trap oracle is used.

Decision: opposite-row same-target exclusions at one future value predict that future bit. Generally a target-only universal strict hedge exists exactly when some future tuple has no compatible old-bit completion; all certificates confined to one old row are insufficient.

Decision: finite multi-square escrow windows can be globally one-hole safe even while s,t,u are temporarily protected, provided each transient future is consumed by execution or a computable timeout. Use bounded simulations and fresh zero-stake support/sweep queries.

Decision: by P4-S008, a computably random source cannot sustain infinite successful reset-free escrows while a single fixed old sentinel stays permanently omitted. Thus the committed X still requires effective unbounded old-sentinel turnover for any same-source destroyer. Infinite timely opposed-row captures and certified turnovers have not been established.

Next **P4-S052**: finite escrow gain coupled to old-sentinel cash-out and repeated effective turnover. Retain PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged, X in OH and R_2=OH unresolved. No novelty, openness, prior-art, Gate-4, publication or outreach finding.


## P4-S052 — old-sentinel cash-out and effective turnover guard

Decision: two opposite-old-row, different-target exclusions support 4/3 future escrow. Exactly two surviving future tuples positively orient the old s and support an additional fair double (combined 8/3); the double nonmatch leaves both old rows possible (4/3 with zero-stake old consumption).

Decision: old-value evidence must be a finite positive same-row/same-target complementary refutation, an observed target matching a refuted value, a finite old-only wrong halt, or an independently proved equivalent. A late witness can orient a still-unread s but not retrospectively stake an observed t/u.

Decision: at a semantically shielded old epoch, Y/Z prohibit all positive square refutations of actual-future-value corners. No matching old orientation survives; every actual opposed-row escrow takes the unorientable outcome. No semantic shielding oracle is available to the controller.

Decision: mandatory transient-future timeout with old s retained is globally one-hole legal. Old s may be consumed at zero stake **after a positive escrow**; automatically resetting old s on every timeout on all continuations instead gives exhaustive computable isomorphism. Infinite *executed* profitable turnovers would establish X not in OH, but they remain unproved. Under hypothetical X in OH each fixed success-gated controller has finitely many exits and final s; passive late witnesses may remain.

Next P4-S053, effective branchwise-avoidable pre-consumption certificate capture. No separation, novelty, openness, Gate-4, publication or outreach conclusions.


## P4-S053 — prompt escrow arrival versus all-transcript reset bars

Decision: adopt the explicit finite-execution-trace promptness condition, quantified over both certificate discovery and actual unconsumed fresh supports, as a conditional sufficient criterion for infinitely many profitable cross-epoch old turnovers. An adaptive computable finite timeout remains finite on every reached transcript; it does NOT certify the condition on the committed X.

Decision: an eventual positive-turnover event on every continuation of a reached prefix is an effective finite bar, with a computably searchable uniform common deadline. Eventual old consumption at every reachable epoch on all continuations gives an exhaustive computable isomorphism, even without a prescribed reset clock. Genuine branchwise avoidance remains necessary for a potentially destroying success-gated controller.

Decision: escrow does not beat the P4-S050 first-refutation reset in earliest LOCAL positive 4/3 payoff. It can alter future epoch support, so no global dominance is asserted. The shielded old epoch permits only the unoriented 4/3 escrow cash-out, not the 8/3 old orientation.

Decision: an abstract computable c.e. delayed-publication model can provide two opposite-old-row sound wrong-future exclusions AFTER the release of every spent prospective target and thereby defeat timely capture on a computable reference input. This is NOT a construction or no-go theorem for the committed M/Y/X. No actual-source infinite promptness, X in OH, X not in OH, R_2=OH or OH non-invariance established.

Next P4-S054 on an actual-M finite-stage promptness invariant or stronger necessary arrival law. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach finding.


## P4-S054 — actual autoreduction cube certificate and partial clock

Decision: retain the exact H recoding. Flipping future raw x0 and x1 in one fresh block changes ONLY virtual q=3b. The target-correct syntactically self-avoiding M^Y(q) therefore finitely refutes the corresponding virtual-unit-flip completion, EVEN in the presence of a distinct old unread s held at its actual value. This is an actual-M/X forced positive finite witness, unlike an arbitrary c.e. publication calendar.

Decision: expose the third block bit and every source value in the computable raw wtt use frontier except protected s,t,u, then symmetrically test all eight synthetic cube corners. The first wrong-output clock sigma(p) is partial computable from the exposed finite p and finite on every X-derived state. Its domain is NOT all sibling transcripts and it has no established total computable bound or effective deadline.

Decision: a verified forbidden raw 3-bit corner justifies the exact sequential fair (s,t,u) terminal table 0 on the corner and 8/7 everywhere else. The gain consumes s. This does NOT give opposed-old-row squares, a reset-free 4/3 escrow, or a generic one-bit future prediction.

Decision: a fully computable finite-window controller mandatorily releases t,u, keeps s after timeout, and resets s only on a witnessed profitable 8/7 cube; it is globally total, no-repeat, fair-coin preserving and at most one-hole. Profitable exit at p is exactly sigma(p)<=L(p), and infinite executed old resets would witness X not in OH, conditionally. Under hypothetical X in OH every total computable controller in this cube family has a final old s with every later witnessed positive sigma(p) finite but strictly L(p)<sigma(p). This is a sharper actual-source necessary latency law, NOT a proof of X in OH or of R_2=OH.

Next P4-S055: test whether source-reached partial clock totalization is possible under globally legal, genuinely branchwise-avoidable fresh-coordinate tenure, or derive a sharper non-domination obstruction. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach decision.


## P4-S055 — paired clock, target-runtime non-domination, and source-selected slow blocks

Decision: the P4-S054 eight counterfactual cubes form four exact M(q)-trace pairs because jointly flipping raw t,u changes ONLY virtual q and the clipped M(q) syntactically avoids q. A halt in any pair gives a positive wrong-output certificate at one mate. Hence sigma equals the min ordinary halting clock over four representatives, still PARTIAL away from X.

Decision: T_Y(q), the halting time of M^Y(q), is total Y-computable and not eventually dominated by any total computable function, since such domination would yield a forbidden tt-autoreduction of CR Y. This source-runtime obstruction does NOT imply any corresponding sigma non-domination: an off-source representative may halt early.

Decision: the explicit four-run finite-window scan remains globally fair, total, no-repeat and one-hole, using compulsory temporary releases and exactly fair 8/7 old-reset payoffs. Under hypothetical X in OH, every computable q-only tenure b has a final old sentinel and infinitely many source-selected distinct q_k with max(1,b(q_k))<sigma(p_k)<=T_Y(q_k). Neither infinite capture nor X in OH nor R_2=OH is established.

Next P4-S056: test actual source-reached minimum-clock frequent promptness under legally changing fresh-block supports. Freeze P4-S008, P4-S052, P4-S053 and earlier mathematics. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach finding.


## P4-S056 — exact compulsory-reset four-run latency law

Decision: retain the P4-S055 equality sigma=minimum ordinary halting time of four representative clipped M(q) traces and the finite actual-X certificate law 0<sigma(p)<=T_Y(q). The full target runtime's hyperimmunity does not transfer to sigma by pointwise comparison.

Decision: choose one entirely fresh raw block for each epoch, complete the finite wtt value support while keeping s,t,u unread, compute any total L(e,p), and simulate four traces only to that finite deadline. On a positive wrong/nonbinary halt, execute the exact fair 8/7 forbidden-triple hedge. On timeout, consume s,t,u all at zero stake rather than retaining s. All branches terminate; the least-unread s is consumed each epoch, so the scan is a computable fair-coin-preserving homeomorphism.

Decision: on the committed computably random X, this **compulsory-reset** controller can have only finitely many executed profitable cube captures; otherwise its total computable fair output martingale wins on a computably random computable-isomorphic image. Hence ANY total computable positive L eventually falls STRICTLY below sigma on every subsequent X-derived value-closed epoch of its own forced-reset schedule, at distinct fresh q_e. This is an actual-source result **without X in OH**; it is not a source-independent universal sigma dominance statement.

Decision: a bounded all-valuation four-run BAR(r) is decidable for supplied finite r, but a globally total computable renewable fresh-block certified-BAR provider on every forced-reset X epoch cannot exist. C.e. positive proof search does not itself give a total prospective tenure.

Decision: success-gated timeout retains s and is not in the isomorphism regime. The new anti-promptness result MUST NOT be transferred to it. P4-S008, P4-S052 and P4-S053 preserved. X in OH and R_2=OH remain unresolved.

Next P4-S057 on the gap between compulsory-reset and success-gated renewal, not more forced-reset thickness. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach claim.

## P4-S057 — no computable prospective miss-budget bound on hypothetical infinite success

Decision: preserve the true success-gated L-clock controller, with mandatory temporary t/u releases, least-unread non-s sweep, and no old reset at timeout. On CR X, any hypothetical infinite winning epoch sequence has W_e >= B(e,p_e) at infinitely many epochs for EACH total computable epoch-start B. Proved by a finite-prefix compulsory-reset effective-isomorphism shadow, never by misapplying P4-S056 to actual T_L. No infinite success proved.

## P4-S058 — effective finite winning cylinders and no closed safety supplier for CR

Decision: distinguish positive M wrong-output certificates from completed WINNING 8/7 exit leaves on arbitrary inputs. The raw finite winning-level G_n is uniformly c.e. open with fair-coin bound lambda(G_n)<=(7/8)^n. Every finite raw prefix has an infinite extension avoiding sufficiently many winning resets; no algorithm to find that extension is supplied. The actual infinite-winning class is effective Pi^0_2 and null; a computably random source can in principle belong to such a class. No effective closed, or effective F-sigma, subcondition sufficient for infinite gains can contain CR X: each effectively closed subset is null and has a computable-martingale defeat. This is a safety-style obstruction not a success-gated timing bound or an existence theorem. Preserve P4-S057, P4-S056, P4-S053, P4-S052 and P4-S008; X in OH and R_2=OH unresolved. No Gate-4 or prior-art decision.


## Mathematics checkpoint — P4-S059 (NOT a gate review)

Decision: retain the genuine Pi^0_2 four-run winning question, but record a stronger source-specific anti-promptness theorem. Uniformly decidable clopen C_{n,m} of n winning exits within m output bits obey lambda(C_{n,m})<=(7/8)^n. Every computably random raw source has only finitely many C_{n,h(n)} for each total computable h; conditional infinite winning-time function eventually dominates all total computable functions. The P4-S011 original Y all-trigger scan already supplies a dominating function, so the committed X/Y highness is not a contradiction or positive certification. Preserve P4-S057/P4-S058 and all frozen mathematics; X in OH and R_2=OH unresolved. Gate 3 PASS, Phase 4 OPEN, Phase 5 CLOSED; PA-0001 and DEF-0020 unchanged; no Gate-4, novelty, prior-art or publication disposition.

## P4-S060 — conditional dominant cumulative missed reservations (mathematics, NOT Gate 4)

Decision: in genuine success-gated T_L each legal total prospective finite reservation necessarily completes (positive hedge or mandatory zero-stake t/u plus non-s release, keeping s unread). Finite branching yields computable b(m) bounding bits for m complete reservations. Hence D_{n,m} is clopen and lambda(D_{n,m})<=(7/8)^n.
Decision: on CR X every computable reservation horizon h(n) is attained for n completed 8/7 wins at only finitely many n. Under HYPOTHETICAL infinite actual wins, A_n=n+sum_{e<n}W_e and so cumulative real misses S_n=sum_{e<n}W_e eventually dominate every total computable f(n). This is an operational P4-S059 corollary via b, not an independent theorem proving or excluding infinite renewal. P4-S057 individual adaptive W_e budgets remain separate.
Decision: preserve three distinctions: eventual M^Y(q) halting; total prospective pre-consumption protection/release; infinitely many ACTUALLY executed profits. Only first two verified. X in OH and R_2=OH unresolved; frozen guards P4-S008/P4-S052/P4-S053/P4-S056–P4-S059, class hierarchy and Y/M/H/X unchanged. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged. Gate 3 PASS; Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach. Next P4-S061; no blocker.

## P4-S061 — local prompt-block source martingale; mathematics, NOT Gate 4

Decision: for each total computable prospective B and each valid epoch-start output history h, truncate the following k epochs with a finite compulsory-old-reset SHADOW solely to define a decidable clopen test requiring k genuinely winning B-prompt old exits. The test has measure <=2^(-|h|)(7/8)^k; a computably summable mixture over ALL h and k produces one computable source martingale. Consequently CR X, CONDITIONAL on infinitely many actual wins, must have an overbudget completed W_j in every sufficiently late window of 64ceil(log_2(m_e+2)) epochs after reached epoch e. This is a further local W-profile necessity; it is NOT actual winning, pointwise W domination, all-continuation compulsory reset or a global nth-win horizon relabelling. Frozen mathematics, Y/M/H/X, exact fair terminal table and governance unchanged; no novelty/open-status/Gate-4/publication/outreach decision. Next P4-S062; no blocker.

## P4-S062 — near-critical single-length audit, NOT Gate 4

Decision: retain the genuine P4-S057 success-gated four-run machine and P4-S061 finite E^B_(h,k) tests, but audit only k(m)=ceil(26ceil(log_2(m+2))/5) prompt wins at each epoch-start OUTPUT length m. Sum finite clopen length-selected tests using weights ceil(log_2(m+2))+1. The EXACT arithmetic 2^5*7^26<8^26 makes the source-martingale sum effectively convergent, yielding a CONDITIONAL individual-W overrun in every sufficiently late 5.2-log-length actual epoch window if infinitely many profits occur. Abstract disjoint fair triple events show why the mass bound alone gives no subcritical-log inference; they are not a legal one-hole scan or a source progress certificate. No proof of infinitely many actual X exits, X in OH, R_2=OH, novelty, openness, Gate-4, publication or outreach. All earlier authority and gates frozen. Next P4-S063; no blocker.

## P4-S063 — frozen old-sentinel reflection and marked finite-renewal kernel (2026-10-08)

**Mathematics checkpoint, NOT a gate or novelty decision.** On the unchanged actual success-gated T_L, flipping the unread old sentinel leaves the entire pre-reset trace, first positive gate and real completed timeout count unchanged. Every finite prospective epoch gate has an EXACT computable rational reachability weight g. At its pre-consumption protected triple, one atom is forbidden zero, one is a fragile old-bit-sensitive 8/7 win, and six are robust old-bit-insensitive 8/7 wins; the marked probabilities are respectively g/8,g/8,3g/4. Fixed marked k-win words have finite clopen mass <=2^-m(1/8)^f(3/4)^r.

CONDITIONAL on infinitely many ACTUAL profitable old resets on committed CR X, for each total computable prospective B, every sufficiently late 2J(m_e)-epoch window (J=ceil(log_2(m+2))) either has W_j>=B(j,p_j) or strictly more than J(m_e) robust exits. The proof uses an effective finite-clopen portfolio bounded by sum_j(j+1)(3/4)^j. One-J all-fragile B-prompt windows are likewise excluded eventually. These MARKED laws do not replace the P4-S062 W-only K_62 law, and no infinitely executed profitable renewal is verified. All exact fresh-block, paired-trace, clipped, pre-consumption, timeout no-old-reset, fair ledger, global one-hole and earlier frozen theorem guards stand. X in OH and R_2=OH unresolved. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED; no Gate-4 or novelty/publication claim. No blocker; next P4-S064.

## P4-S064 — first-gate deficit / executed-timeout dependence, NOT Gate 4 (2026-10-08)

Decision: retain the actual P4-S057–P4-S063 four-run T_L with old-sentinel retention on timeout; use exact P4-S063 finite gate weights g_h^B to define the complementary source-reached clopen B-timeout event of rational conditional mass delta=1-g. On any CR source, effectively summably rare completed B-timeout events cannot recur infinitely often; for r(m)=(m+2)^-3 every sufficiently late actually reached B-overrun has computed deficit delta>(m+2)^-3. Combine ONLY CONDITIONALLY on infinite actual profitable renewal with P4-S062's W-only K_62 law to tag one real overrun and gate deficit in every eventual K_62 window, and with P4-S063 to tag its marked overrun arms. The complementary gate law is NOT an infinite progress supplier; no actual repeated gates are verified. All mathematics, Y/M/H/X, X in OH/R_2=OH uncertainty, PA-0001, DEF-0020, Phase 4 OPEN / Phase 5 CLOSED and no Gate-4/novelty/publication guards preserved. Next P4-S065, no blocker.

## P4-S065 — permanent-old transition hazard obstruction, NOT Gate 4 (2026-10-08)

Decision: preserve all frozen mathematics and real success-gated T_L. Adopt actual nested no-gate timeout survival q_n and rational frontier-averaged hazards c_n=1-q_(n+1)/q_n. A genuinely forever-stalled CR source requires positive-mass effectively closed F_h and summable hazards, plus positive all-B no-gate deficit floor; zero-survival at all actually reached X epoch starts would ensure infinitely many real correct 8/7 old resets, but is NOT VERIFIED. No equality R_2=OH, separation, or X in OH decision. PA-0001, DEF-0020, Y/M/H/X, Gate 3 PASS, Phase 4 OPEN, Phase 5 CLOSED and no Gate-4/novelty/openness/prior-art/publication/outreach preserved. Next P4-S066; no blocker.


## P4-S066 — mathematics-only checkpoint (2026-10-08)

No policy or Gate-4 decision in P4-S066; validated mathematics-only necessary pathwise-hazard obstruction, with source-X recurrence unresolved. Prior decisions and CAND-01 selection unchanged.

## P4-S067 — mathematics-only local gate-leaf capacity (2026-10-08)

No new policy/gate decision. Retain all earlier decisions. The actual controller's finite first-gate leaf-depth capacity law is a necessary obstruction on hypothetical CR permanent stalls; no committed-X hazard divergence/recurrence verified. A padded alternative-program clock countermodel is NOT a modification of committed M. Gate 3 PASS; Phase 4 OPEN; Phase 5 CLOSED; PA-0001/DEF-0020 unchanged. Next P4-S068; no blocker.


## P4-S068 — mathematics-only closure-gate multiplicity (2026-10-08)

No policy, candidate-selection or gate decision. For the unchanged P4-S057 controller, after the c-bit finite use closure, filler-bit values are inert for certificate decisions, so gamma(p)=a(p)/2^c(p) where a counts genuinely timely positive closure assignments. Every CR permanent stall has sum_n a(p_n)/2^c(p_n)<infinity; no committed X recurrence/lower bound or repeated actual gate established. Preserve Y/M/H/X, all Phase-4 results, PA-0001 and DEF-0020. Gate 3 PASS, Phase 4 OPEN, Gate 4 NOT REVIEWED and Phase 5 CLOSED. No novelty/openness/prior-art/publication/outreach inference. Next P4-S069; blocker NONE.


## P4-S069 — mathematics-only eventual/late closure certificate separation (2026-10-08)

Decision: no gate, policy, candidate selection, prior-art or publication change. Record fixed ORIGINAL M/T_L certificate partition a=b-d_L; retain actual-X lateness on every true timeout, the CR permanent-stall bounded-closure complete-lateness necessity, and the null/meagre exact-original-M autoreduction target locus and generic CR survivor warning. Do not infer real X hazard divergence from b, c, sibling potentials, null-locus measure, or retrospective halts. Every frozen P4-S001–S068 theorem, Y/M/H/X, t/u ZERO timeout release plus non-s sweep WITHOUT old reset, and exact 8/7/zero one-hole fair scan remain unchanged. X in OH, X not in OH and R_2=OH unresolved. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/prior-art/publication/outreach claim. No blocker; next P4-S070.


## Inter-session owner direction after P4-S069 — prioritize global same-source coded-hole obstruction (2026-10-08)

**RESEARCH STRATEGY ONLY; NOT A MATHEMATICS SESSION OR NEW THEOREM.** Owner chose a global structural pivot before running P4-S070. Record \`phase4/P4_STRATEGIC_PIVOT_AFTER_S069.md\` as the controlling research priority, consistent with the historical P4_RESEARCH_PIVOT_AFTER_S031.md. Freeze P4-S001–S069 and retain the central R_2 versus OH and OH^iso questions. Primary new bounded test: whether the explicit H preserves OH on all CR raw sources; a proof would force committed X notin OH, while a counterexample z in OH, H(z) notin OH would prove R_2 proper-subset OH (not necessarily classify X). Secondary separate target R_2=OH^iso. Prefer a global same-source normalization or rigorous structural obstruction over further finite timely-certificate/timeout/hazard estimates. Original M, Y, H, X and ALL success-gated t/u ZERO releases, non-s sweeps without old reset, four paired traces, seven 8/7 and one ZERO remain unchanged. No new mathematical conclusion or resolved classification. PA-0001/DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED; Phase 4 OPEN, Phase 5 CLOSED; no novelty/openness/prior-art/publication/outreach claim; no blocker. Next P4-S070 has not run.


## P4-S070 — mathematics-only global reduction, no gate decision (2026-10-08)

Disposition: VALIDATED Phase-4 mathematical result only. H preserves OH iff all computably supported two-bit XOR shears preserve OH iff all computable blockwise GL(3,F_2) recodings preserve OH. No preservation/separation decision. Strategic pivot after S069 remains governing; next P4-S071 targets supported-shear same-source normalization. Gate 3 PASS, Gate 4 NOT REVIEWED, PA-0001 unchanged, Phase 4 OPEN, Phase 5 CLOSED. No external blocker and no novelty/prior-art/publication decision.


## P4-S071 — mathematics-only supported-shear exposure normalization, no gate decision (2026-10-08)

Disposition: accept validated conditional global same-source criterion e_{n(m)}>=d_m exp(-B_m) for every computable supported shear, with an explicit globally legal raw one-hole scan. Any putative OH shear separator needs unbounded total absolute late spoiled-w stake; this is only a necessary obstruction, NOT a proof of full preservation or a CR-in-OH counterexample. P4-S034–S036 earlier general spoiled-wager results remain authoritative. Frozen Y/M/H/X and entire S057 controller unchanged. No selection, prior-art, novelty or Gate-4 decision. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; PA-0001/DEF-0020 unchanged. No owner/external blocker; next P4-S072.


## P4-S072 — conditional online late-shear pricing, no gate decision (2026-10-08)

Disposition: validated mathematics only. S071 global raw scan plus a total computable positive rational fair credit registrar produces two source martingales L,F, with L*F=d*A (unsettled-credit product A) and single martingale h=(L+F)/2>=sqrt(d*A). A faithful registrar with pending downside bounded cannot witness supported-shear destruction of OH; otherwise small open inventory is necessary. Genuine future-bit stake dependence prevents an exact pre-c stake forecast but can admit later fair settlement. This does NOT decide H/shear invariance, X in OH, R_2=OH or R_2=OH^iso. All prior mathematics frozen. Gate 3 PASS, Gate 4 NOT REVIEWED, PA-0001/DEF-0020 unchanged, Phase 4 OPEN, Phase 5 CLOSED; no novelty/prior-art/publication decision. Blocker NONE; next P4-S073.


## P4-S073 — joint-price fair settlement, no gate or external decision (2026-10-08)

Disposition: validated Phase-4 conditional mathematics ONLY. For total effective finite multi-claim credits, fair price pi=(G(0)+G(1))/2 yields L F Pi=d A and a single h_2>=sqrt(d A/Pi); an additional total computable martingale Q yields h_3>=(d A Q/Pi)^(1/3). Two common-pivot individually fair wagers cannot generally be multiplied as a fair wager; a priced finite four-block shared-pivot example nevertheless pre-funds pi at a genuine raw c filler and obtains a globally fair e>=d/4. Neither a general infinite-overlap financier nor OH separation/H-preservation is proved. All frozen objects/results unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED, PA-0001/DEF-0020 unchanged, Phase 4 OPEN, Phase 5 CLOSED, no novelty/prior-art/publication/outreach decision. Blocker NONE; P4-S074 next.


## P4-S074 — rolling infinite escrow theorem; no gate decision (2026-10-09)

Disposition: Phase-4 VALIDATED conditional mathematics ONLY. In an explicitly nonclosed infinite all/even supported-shear chain, two spoiled w claims share each later fresh a pivot; next groups start and pre-finance before older claims settle, with successive conditional prices depending on earlier pivots. An actual earlier fresh c-filler fair Q wager realizes each nontrivial pi_i; a later fresh a F wager realizes G_i/pi_i. Because Q,F use DISJOINT raw betting coordinates, e=QF is a single globally legal total martingale, and e=d A(Q/Pi)>=(1-q)²(1-q²)d (sharp e>=3d/16 at half stake) on ALL virtual checkpoints. Disjoint finite closed block packets do not describe the source-scan dependency chain; effective S037 renewal remains consistent. Strongest new lesson: cumulative settled prices may be arbitrary while matched by truly executed Q, and pending downside A is an independent cost. No general financer or X/H/R2 result. Prior S001–S073 and Y/M/H/X unchanged; S057 not resumed. Gate 3 PASS, Gate 4 NOT REVIEWED, PA-0001/DEF-0020 unchanged, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/prior-art/publication/outreach decision. Blocker NONE; P4-S075 next.


## P4-S075 — conditional mathematics, no new candidate/gate decision (2026-10-09)

Accept the effective two-fresh-bit settlement-mirror pricing/savings theorem on S074's nonclosed rolling chain with q_i->1 and vanishing all-checkpoint escrow floor, and the precise three-claim single-last-filler financing obstruction. This is NOT a new preservation class beyond S037 effective fresh renewal for the computably retiring example, nor any H/supported-shear theorem or actual-X classification. Original Y/M/H/X, S073/S074, exact S057 controller all frozen. Gate 3 PASS, Gate 4 NOT REVIEWED; Phase 4 OPEN, Phase 5 CLOSED. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged. No novelty, openness, prior-art, publication or outreach decision. No owner/external blocker; P4-S076 is next.


## P4-S076 — conditional multistage pricing, no gate/candidate decision (2026-10-09)

Accept only a total positive sequential fair pre-fresh-c Doob financing and later genuine fresh a settlement for specified all/even S071 shared-pivot spoiled w bundles (m_i=i+3 rolling, with cofinal S036 savings mirrors and no uniform direct interim floor). S075 last-c-only obstruction remains correct. S037 effective renewal is not strengthened to genuinely non-effectively retiring claims. No X∈OH, H/shear invariance, R₂=OH, R₂=OH^iso or unrestricted homeomorphism conclusion. All previous results and original Y/M/H/X, S057 exact controller frozen. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/prior-art/publication/outreach decision. No blocker; P4-S077 next.


## P4-S077 — mathematics-only finite-support OH invariance (2026-10-09)

Accept global all-scan/all-martingale finite-support homeomorphism transfer with a single everywhere-total fair one-hole raw scan and D_m≤2^|F|e after finite F preloading. No effective retirement required, even with partial target-dependent virtual computations. Finite supported S_E preserve OH and supported-shear invariance status is insensitive to finite symmetric differences of computable block supports. Finite truncations provide NO passage to all-block H; no X membership, H-preservation, R₂=OH or R₂=OH^iso resolution. Retain S001–S076 and original Y/M/H/X; no S057 resumption. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; PA-0001/DEF-0020 unchanged; no novelty/openness/prior-art/publication/outreach decision. Blocker NONE; next P4-S078 globally infinite-support only.

## P4-S078 — mathematics-only global shear reduction (2026-10-09)

P4-S078 (2026-10-09): GLOBAL single-shear criterion. Writing S=S_N (a,b,c)->(a,b xor c,c) on EVERY three-bit block and Q_E the computable within-block b/c swap on decidable E, the exact full-Cantor identity S_E=Q_E S Q_E S Q_E proves all computable-support shear preservation iff preservation under the ONE FIXED infinite-support S; by S070 this is equivalent to committed H-preservation and all computable GL(3,2)-block recoding preservation. Independently, the exact committed H factors as S R Q S R Q S R (right-to-left; R swaps a/b globally, Q swaps b/c), giving THREE explicit all-shear witness-transition candidates on the fixed X->Y chain IF X lies in OH. This is only a global algebraic quantifier reduction, NOT S-preservation, not nonpreservation, not X membership and not R2=OH; R2=OH^iso stays separate. All 65536 four-block support/source identities and 168 GL3 generator states passed with zero discrepancies. S037/S073–S077, exact S057 controller and ORIGINAL Y/M/H/X preserved; no finite truncation limit, effective-retirement assumption or new raw compiler. Gate 3 PASS, Gate 4 NOT REVIEWED; Phase 4 OPEN, Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. No novelty, openness, prior-art, publication or outreach claim. Blocker NONE. Next P4-S079: prove or disprove preservation under this fixed S with an actual OH source, or classify committed X directly.

## P4-S079 — direct global unit-column one-hole extraction (2026-10-09)

P4-S079 proved a globally legal restricted-sentinel destroyer: for a target-correct self-avoiding partial predictor on ANY infinite decidable raw-coordinate family, choose least fresh sentinel in that family, fill least-fresh non-sentinel coordinates while running bounded checks, place a genuine prediction wager, and after EVERY successful sentinel query one genuine zero-stake least-unread sweep. On nontriggering branches exactly one sentinel remains unread; on all-trigger branches infinitely many sweeps exhaust ALL raw indices. This yields total fair no-repeat globally one-hole winning scans, without sibling totality or advance wagers. Apply unchanged M^Y via the exact remaining block matrices Y=B_i(z_i) in S078's R,S,Q,R,S,Q,R,S path: B_i has a unit column for EVERY i=1,...,6, so z1,...,z6 are UNCONDITIONALLY in CR minus OH. The first source z0=R(X) has NO unit-column certificate and remains unclassified. If X in OH, the FIRST shear pair (z0,z1) is a real fixed-S failure and R2 proper-subset OH; it is not proved that X in OH. Therefore universal fixed-S preservation, R2=OH, R2=OH^iso and original X membership remain unresolved. Exact 8-input F2 algebra/column independence audit passed; infinite-scan correctness proved separately. Original Y/M/H/X, S001–S078, S037/S057/S073–S078 retained. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; no novelty/open/prior-art/publication/outreach claim. Owner/external blocker NONE. Next P4-S080 targets z0=X up to signed permutation, not further residue tables. Files: phase4/P4-S079_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _UNIT_COLUMN_AUDIT.py.


## P4-S080 — record-level universal reformulation of the z0 question (2026-10-09)

P4-S080 (2026-10-09): RECORD-LEVEL DECISION OF THE PRIMARY TARGET'S FORM. The record fixes Y only existentially (P4-S011 'Fix a computably random sequence Y and an oracle machine M'; P4-S027 'settled existential witness'), so an admissible pair is any CR Y with a self-avoiding clipped wtt autoreduction M (class WAR). Chained-substitution spreading: from any admissible (W,N) with nondecreasing cap U, the greedy computable bijection tau(n)=(i_n, least unused >U(i_n), least unused >U(j_n)) gives V=W o tau in CR with a BLOCK-AVOIDING autoreduction (later in-block queries answered by earlier in-block predictions). Then EVERY computable blockwise recoding of V, including H^{-1}(V), is wtt-autoreducible and outside OH. Hence (Y1,M1)=(V,M_V) satisfies every record hypothesis while H^{-1}(Y1) notin OH: z0=R(X) in OH is NOT derivable from the record, and X notin OH is established exactly when U(H): H^{-1}(Y') notin OH for every Y' in WAR. Failure of U(H) gives R2 proper-subset OH (and record-independence of X); universal fixed-S preservation implies U(H). GL(3,2) classification: U(K) holds for every K with a unit column (S079 Thm 2 for arbitrary admissible pairs) and U(PKQ)<=>U(K) for permutation matrices; the no-unit-column matrices are exactly the 18-element double coset S3 A S3, closed under inversion, so U(H)<=>U(H^{-1}). Any U(H) counterexample needs, for EVERY autoreduction, infinitely many target in-block two-cycles {1<->2} and {0<->2} (target-only role refutation). Calibration: KLR subset OH; every element of OH minus R2 (any separation, any U(H) refutation) is non-MLR, and the programme has no OH certificate beyond MLR; OH=MLR would decide R2=OH but give KLR=MLR (QST-0001, SOURCE-STATED OPEN in the catalogue; no new openness claim). Exact finite audit PASS (GL(3,2) coset, tau bijection, toy substitution model, 1408 role cases). U(H), committed X in OH, fixed-S preservation, R2=OH, R2=OH^iso, OH=MLR UNRESOLVED. Original Y/M/H/X unaltered; S001–S079, S037, S057 (not invoked), S070–S079 frozen. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; no novelty/open/prior-art/publication/outreach claim. Owner/external blocker NONE. Next P4-S081: OH-certification gate (non-MLR OH member or exact obstruction), then test against R2/H-images; a proof of U(H) is acceptable. Files: phase4/P4-S080_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _ADMISSIBILITY_AUDIT.py.

## Owner direction — closeout must merge to main and carry the next prompt (2026-10-09)

Owner instruction given at the end of P4-S080 and standing for all future sessions: closeout must commit, push the session branch, merge into `main` (fast-forward when possible, never rewriting `main` history), push `main`, and independently verify the remote `main` SHA. The session close record and the final report must contain the full copy-ready next-session prompt unless an owner/external blocker exists. Recorded in `docs/SESSION_PROTOCOL.md` (Closeout steps 3–5) and `AGENTS.md` (Sessions and blockers). This is a process decision only; no mathematical, gate, prior-art or definition disposition changes.
