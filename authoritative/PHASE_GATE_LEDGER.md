# Phase Gate Ledger

| Gate | Status | Meaning |
|---|---|---|
| Scaffold -> Phase 1 | AUTHORIZED | Owner explicitly authorized Phase 1 on 2026-10-03. |
| Phase 1 -> Phase 2 | PASS | P1-S014 formally reviewed Gate 1 and passed it. Phase 1 is complete for gate purposes and Phase 2 — Discovery is OPEN. The catalogue remains bounded/non-exhaustive and residual provenance gaps remain recorded. |
| Phase 2 -> Phase 3 | PASS | P2-S006 formally reviewed Gate 2 and passed it. Phase 2 is complete for gate purposes and Phase 3 — Novelty / Prior Art is OPEN. The PASS authorizes dedicated prior-art attack; it does not establish novelty or select a candidate. |
| Phase 3 -> Phase 4 | PASS | P3-S008 formally reviewed selected CAND-01 against every Gate-3 minimum-evidence requirement and passed Gate 3. Phase 3 is complete for gate purposes and Phase 4 — Mathematics is OPEN for CAND-01. PA-0001 remains unresolved under inspected evidence; PASS is not a novelty finding. |
| Phase 4 -> Phase 5 | CLOSED | Phase 4 is active; Gate 4 has not been reviewed, so Phase 5 remains unauthorized. |
| Phase 5 completion | CLOSED | No publication work is authorized. |

## Pre-review Gate-1 evidence status after P1-S013 (historical)

P1-S013 completed the coverage audit required by `docs/GATE_POLICY.md`. The result is **READY FOR FORMAL REVIEW**, not PASS.

Minimum evidence now assembled:

- documented 19-stratum coverage plan plus a completed per-stratum audit;
- stable-ID searchable source catalogue;
- definition/terminology index;
- theorem/characterization index;
- implication/equivalence/separation relationship map;
- status-question record with explicit provenance and later-status evidence;
- author/topic navigation;
- search/retrieval log;
- explicit source-access/uncertainty register in source records, coverage limitations, search log and failure/lesson ledger;
- no identified consequential unsourced claim in the authoritative research summary.

### Audit disposition

All 19 strata remain historically labelled `PARTIAL_...` because those labels record depth and provenance history, not gate outcomes. P1-S013 separately marks all 19 as `SUFFICIENT_FOR_GATE1_REVIEW`. There are **0 gate-critical remediation gaps**.

Residual gaps accepted for Gate-1 review include:

- original Schnorr/Kurtz internal statements where later statement-inspected primary literature supports the exact current definitions/relations;
- Jockusch/Kurtz genericity originals where later primary literature supplies exact syntax;
- the Demuth translation qualification, with the Russian original and modern primary normalization kept distinct;
- earliest standalone Martin-Löf no-randomness-from-nothing provenance;
- selected early Chaitin/Kolmogorov/Levin/Schnorr provenance;
- the uninspected Solovay draft and Schnorr 1973 internals;
- historical higher-randomness originals where later primary normalization is statement-inspected;
- Franklin-Greenberg-Miller-Ng internal statements, because no promoted theorem depends on the uninspected abstract;
- Kučera-Terwijn 1999 internals, because the current lowness/base equivalence package is statement-grounded elsewhere;
- abstract-level constructive-dimension and KL material, which must be upgraded before a future discovery claim materially relies on their exact formulations;
- the deliberately minimal COV-0016 resource-bounded-dimension/cryptography boundary.

P1-S013 found and corrected one catalogue-wide structural inconsistency: `coverage-plan.json` used `PARTIAL_P1_S010`, `PARTIAL_P1_S011` and `PARTIAL_P1_S012` in live records but omitted those values from its declared status vocabulary.

Current generic coverage counts remain: 19 partial, 0 started-core, 0 started-edge, 0 navigation-only, 0 not-started; 0 complete. These counts do not block review because Gate 1 requires a completed coverage audit and a discovery-ready library, not a claim that every literature stratum is exhaustive.

At the end of P1-S013 Gate 1 remained **CLOSED** and ready for separate formal review. That historical posture was superseded by the P1-S014 formal review below; no Phase-2 discovery was performed in the review session.


## Gate-1 formal review — P1-S014

Formal outcome: **PASS**.

P1-S014 independently reviewed the committed Phase-1 library against every Gate-1 minimum-evidence requirement in `docs/GATE_POLICY.md`. It confirmed the structured catalogue, completed 19-stratum audit, stable-ID indexes, relationship map, status provenance, search/retrieval record and explicit uncertainty register are fit to support bounded Discovery.

The PASS does not erase residual gaps. Original Schnorr/Kurtz and Jockusch/Kurtz internals, Demuth translation qualification, earliest standalone ML-NRFN provenance, selected early Chaitin/Kolmogorov/Levin/Schnorr provenance, the Solovay draft, Schnorr 1973, historical higher-randomness originals, Franklin-Greenberg-Miller-Ng and Kučera-Terwijn 1999 remain recorded as provenance/access gaps. Abstract-level KL and constructive-dimension records remain cautioned and must be upgraded before a future Discovery claim relies on their exact formulations. COV-0016 remains deliberately bounded.

Gate-1 PASS means **discovery-ready, not exhaustive**. It does not select a candidate, establish novelty or authorize Phase 3.

Authorization after P1-S014:

- Phase 1: **COMPLETED**
- Phase 2 — Discovery: **OPEN**
- Phases 3–5: **CLOSED**
- candidate selected: **NO**
- Phase-2 substantive work performed in P1-S014: **NO**

Formal review record: `phase1/P1-S014_GATE1_REVIEW.md`

## Discovery checkpoint — P2-S001 (not a gate review)

The first bounded Discovery pass retains CAND-01, CAND-02 and CAND-03 provisionally and rejects CAND-04, CAND-05 and CAND-06 by exact already-catalogued characterizations/collapse. Records: `phase2/P2-S001_DISCOVERY.md` and `phase2/candidates.json`.

No candidate is selected and no Fairfax-Ball definition is established. Formulation tasks E1–E3 remain; next is P2-S002 on E2/CAND-02 only. No novelty assessment or original proof work was performed. The portfolio is not a Gate-2 PASS or readiness finding. Gate 1 and every later phase status remain unchanged. No owner/external blocker exists.

## Discovery checkpoint — P2-S002 (not a gate review)

P2-S002 resolved CAND-02 formulation task E2. The candidate remains **RETAIN_PROVISIONAL** with its everywhere-total map / effectively-open-indicator predicate unchanged. Local reinspection of already-catalogued SRC-0058 clarified that THM-0063/THM-0064 use a computable-transformation representation guaranteed defined/infinite outside a computable G_delta null set; the converse construction is explicitly ensured defined almost everywhere, not everywhere total. The source characterization therefore does not silently dispose of CAND-02's narrower total-map formulation.

This checkpoint makes no novelty, literature-openness, equivalence or separation claim and performs no Gate-2 review. The retained/rejected portfolio counts are unchanged. Gate 1 remains PASS; Phase 1 remains completed for gate purposes; Phase 2 remains OPEN; Gate 2 remains CLOSED / NOT REVIEWED; Phases 3–5 remain CLOSED. No owner/external blocker exists. Next scheduling is P2-S003 on CAND-01/E1 only.



## Discovery checkpoint — P2-S003 (not a gate review)

P2-S003 resolved CAND-01 formulation task E1. The candidate remains **RETAIN_PROVISIONAL** with its everywhere-total computable fair-coin-preserving / globally finite-fibre predicate unchanged and with no effective inverse branches assumed.

The catalogue was sufficient: THM-0037 supplies existential random preimages under a.e.-computable maps, THM-0038 supplies computable-randomness invariance only under an a.e.-computable inverse pair, and THM-0035 supplies the corresponding Martin-Löf morphism/isomorphism framework. THM-0008 and THM-0039 remain Martin-Löf maximality results. None was promoted into a finite-to-one computable-randomness preservation theorem.

This checkpoint makes no novelty, literature-openness, equivalence, separation or finite-to-one preservation claim and performs no Gate-2 review. The retained/rejected portfolio counts are unchanged. Gate 1 remains PASS; Phase 1 remains completed for gate purposes; Phase 2 remains OPEN; Gate 2 remains CLOSED / NOT REVIEWED; Phases 3–5 remain CLOSED. No owner/external blocker exists. Next scheduling is P2-S004 on CAND-03/E3 only.

## Discovery checkpoint — P2-S004 (not a gate review)

P2-S004 resolved CAND-03 formulation task E3. The candidate remains **RETAIN_PROVISIONAL** as an auxiliary structural direction, with its universal oracle-lowness predicate and globally total/valid uniform-family convention unchanged.

The catalogue was sufficient. DEF-0025 / SRC-0032 require uniform martingale families to arise from a total computable map defined for every oracle instance, with every instance a valid martingale. THM-0024 is a pairwise symmetric join characterization and THM-0025 is an existential pairwise ordinary-vs-uniform separation; neither is a universal lowness theorem. DEF-0007/DEF-0009 and THM-0003/THM-0004/THM-0069/THM-0070 preserve the universal-lowness versus existential-base distinction, while SRC-0009 Theorem 5.7 remains an ordinary-computable-randomness lowness contrast.

This checkpoint makes no novelty, literature-openness, equivalence, separation or noncomputable-member claim and performs no Gate-2 review. The retained/rejected portfolio counts are unchanged. Gate 1 remains PASS; Phase 1 remains completed for gate purposes; Phase 2 remains OPEN; Gate 2 remains CLOSED / NOT REVIEWED; Phases 3–5 remain CLOSED. No owner/external blocker exists. Next scheduling is P2-S005, a bounded Gate-2 readiness audit only.

## Pre-review Gate-2 readiness status after P2-S005

P2-S005 completed a bounded readiness audit against the Gate-2 minimum evidence in `docs/GATE_POLICY.md`.

Result: **READY_FOR_FORMAL_GATE2_REVIEW — NO GATE DECISION**.

The existing portfolio remains six stable candidates: CAND-01, CAND-02 and CAND-03 provisionally retained; CAND-04, CAND-05 and CAND-06 rejected in their recorded shapes. E1–E3 are resolved. For each retained candidate the committed record now supports review of: a precise/search-ready formulation; motivation and potential value; relationship to known concepts; a prospective theorem/characterization package; falsifiers/failure conditions; dependencies and expected difficulty; and explicit separation of “appears interesting” from “is novel”.

Novelty and literature status remain **NOT_ASSESSED**. No prior-art search, equivalent-definition search, proof work, witness construction, experiment, candidate selection or later-phase work was performed. DEF-0020 and all Phase-1 evidence/convention guards remain unchanged.

Gate 2 remains **CLOSED / NOT FORMALLY REVIEWED** and Phase 3 remains CLOSED. The next bounded session is P2-S006, a separate formal Gate-2 review that may record PASS, FAIL or BACKTRACK without performing Phase-3 work in the same session.


## Gate-2 formal review — P2-S006

Formal outcome: **PASS**.

P2-S006 independently reviewed the committed six-candidate Discovery portfolio against every Gate-2 minimum-evidence requirement in `docs/GATE_POLICY.md`. The portfolio is bounded; CAND-01, CAND-02 and CAND-03 each have a search-ready formulation, mathematical motivation/potential value, relationships to known concepts, a plausible theorem/characterization target, falsifiers, dependencies/expected difficulty and explicit separation between apparent interest and novelty. E1–E3 remain resolved.

CAND-04, CAND-05 and CAND-06 remain rejected exactly in their recorded P2-S001 shapes by THM-0008, THM-0026 and THM-0024 respectively. DEF-0020 and all Phase-1 evidence/convention guards are unchanged.

Residual risks are deliberately carried forward: all three retained candidates have high collapse/redundancy risk; CAND-02 retains its SRC-0058 copy qualification; CAND-03 retains the deliberately uncatalogued broader uniform-lowness/traceability exposure. These are Phase-3 attack targets, not missing Discovery fields.

Authorization after P2-S006:

- Phase 1: **COMPLETED**
- Phase 2 — Discovery: **COMPLETED**
- Phase 3 — Novelty / Prior Art: **OPEN**
- Phases 4–5: **CLOSED**
- candidate selected: **NO**
- Fairfax-Ball Randomness defined: **NO**
- Phase-3 substantive work performed in P2-S006: **NO**

Formal review record: `phase2/P2-S006_GATE2_REVIEW.md`.

## Novelty / prior-art checkpoint — P3-S001 (not a gate review)

P3-S001 performed one bounded primary-source prior-art attack on CAND-01 only. It located Rute's endomorphism-randomness framework (SRC-0060 / DEF-0064 / THM-0071) and Bienvenu-Porter's total truth-table non-conservation theorem (SRC-0061 / THM-0072).

Result: **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** for the exact CAND-01 restriction. Everywhere-totality plus fair-coin preservation is already known insufficient for computable-randomness conservation, while unrestricted endomorphism preservation is already a named framework. No inspected primary source matched CAND-01's fixed global finite cardinal fibre bound with no assumed effective inverse branches.

This is not an openness or novelty finding. CAND-01 remains provisional with its exact formulation unchanged; CAND-02 and CAND-03 remain unassessed in Phase 3. No final candidate is selected. Gate 3 is **NOT REVIEWED** and Phase 4 remains **CLOSED**. DEF-0020 and existing convention guards remain unchanged.

Record: `phase3/P3-S001_PRIOR_ART.md`; structured finding: `PA-0001` in `phase3/prior-art.json`.

## Novelty / prior-art checkpoint — P3-S002 (not a gate review)

P3-S002 performed one bounded primary-source prior-art attack on CAND-02 only. It retained Franklin–Towsner's nonergodic weak-Birkhoff framework (SRC-0058 / THM-0063 / THM-0064) and added two decision-relevant primary benchmarks: Miyabe–Nies–Zhang (SRC-0062 / THM-0073), where nonergodic lower-semicomputable convergence is proved without assuming totality, and Moriakov (SRC-0063 / THM-0074), where total computable Cantor maps and effectively-open indicators occur under ergodicity, automorphism group-action structure, Følner averaging and expectation equality.

Result: **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** for the exact CAND-02 predicate. No inspected primary theorem matched everywhere-total arbitrary fair-coin-preserving self-maps together with effectively-open indicators and nonergodic convergence-only semantics.

This is not an openness or novelty finding. CAND-02 remains provisional with its exact formulation and E2 alignment unchanged. CAND-01's P3-S001 disposition is unchanged; CAND-03 remains unassessed in Phase 3. No final candidate is selected. Gate 3 is **NOT REVIEWED** and Phase 4 remains **CLOSED**. DEF-0020 and existing convention guards remain unchanged.

Record: `phase3/P3-S002_PRIOR_ART.md`; structured finding: `PA-0002` in `phase3/prior-art.json`.



## Novelty / prior-art checkpoint — P3-S003 (not a gate review)

P3-S003 performed one bounded primary-source prior-art attack on CAND-03 only. It located Kihara–Miyabe's parameterized uniform-lowness framework (SRC-0064 / DEF-0065), which defines `Low^star(C,D)` by universal preservation of C-randoms under uniform D-relativization using total all-oracle test procedures.

Result: **EQUIVALENT_OR_REBRANDED at the definition level**. With C=D=computable randomness and SRC-0032 / DEF-0025 providing the exact globally total valid uniform-martingale convention, CAND-03 is the `Low^star(CR,CR)` instance. CAND-03 is therefore retired as a candidate for a new named notion.

The specific intrinsic characterization of `Low^star(CR,CR)` remains unresolved under the inspected evidence; no openness is inferred. Ordinary low-for-computable-randomness (SRC-0009 / THM-0075), pairwise uniform relativity and existential baseness remain separate.

CAND-01 and CAND-02 retain their prior dispositions. No final candidate is selected. Gate 3 is **NOT REVIEWED** and Phase 4 remains **CLOSED**. DEF-0020 and existing convention guards remain unchanged.

Record: `phase3/P3-S003_PRIOR_ART.md`; structured finding: `PA-0003`.


## Novelty / significance checkpoint — P3-S004 (not a gate review)

P3-S004 assessed CAND-01's significance/usefulness and plausible interested communities only.

Result: **PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT**. The exact fixed global finite-fibre restriction remains the live structural axis between known unrestricted total-map non-conservation and explicit-effective-inverse invariance. Adjacent primary sources SRC-0065 and SRC-0066 show that finite multiplicity is structurally meaningful in ergodic/symbolic dynamics and channel-style factor-code questions, but their stronger hypotheses do not transfer a computable-randomness result to CAND-01.

PA-0001's novelty disposition remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No candidate is selected, Gate 3 is **NOT REVIEWED**, Phase 4 remains **CLOSED**, and no original mathematics was performed. DEF-0020 and all existing convention/evidence guards remain unchanged.

Record: `phase3/P3-S004_SIGNIFICANCE.md`.

## Phase-3 candidate-selection readiness — P3-S006 (not a gate review)

P3-S006 recorded **READY_FOR_SELECTION_DECISION** for the surviving CAND-01/CAND-02 portfolio. This means the committed prior-art/significance evidence is sufficient for a separate documented selection/NO-GO decision; it is not a candidate selection and not a Gate-3 PASS.

CAND-01 retains its unresolved finite-multiplicity payoff risk. CAND-02 retains elevated totality/representation-artifact risk. Both remain `UNRESOLVED_UNDER_INSPECTED_EVIDENCE`; CAND-03 remains retired.

Authorization is unchanged: Phase 3 remains **OPEN**, Gate 3 remains **NOT REVIEWED / CLOSED**, Phase 4 remains **CLOSED**, and no candidate is selected. The next bounded session is P3-S007, selection/NO-GO only.



## Phase-3 candidate selection — P3-S007 (not a gate review)

P3-S007 recorded the single programme outcome **SELECT_CAND_01** after comparing the two surviving Phase-3 investment cases under the committed P3-S001 through P3-S006 evidence.

CAND-01 is selected for a separate formal Gate-3 review. Its P3-S004 qualification remains controlling: finite multiplicity is provisionally substantive as a research axis, but no computable-randomness consequence of the bare global finite cardinal fibre bound is established. The selection reflects the expected explanatory payoff of resolving the boundary between unrestricted total-map non-conservation, bare finite multiplicity and explicit effective inverse information.

CAND-02 is not selected for active Gate-3 investment. Its significance assessment is preserved, including the elevated risk that everywhere-totality is merely a representation slice excluding a.e./partial witnesses rather than changing randomness content.

PA-0001 and PA-0002 remain **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. CAND-03 remains retired. Selection is not a novelty, openness, theorem or publishability finding.

Authorization remains unchanged pending formal review: Phase 3 is **OPEN**, Gate 3 is **NOT REVIEWED**, Phase 4 is **CLOSED**, and mathematical investigation is unauthorized. The next bounded session is P3-S008, a separate formal Gate-3 review of selected CAND-01 only.


## Gate-3 formal review — P3-S008

Formal outcome: **PASS**.

P3-S008 independently reviewed selected CAND-01 against every Gate-3 minimum-evidence requirement in docs/GATE_POLICY.md. The dedicated primary-source prior-art attack, alternate terminology/equivalent-formulation search, closest-known-work account, equivalence/rebranding risk, significance/usefulness case, interested-community assessment, explicit remaining novelty uncertainty and documented selection decision are all present.

The PASS preserves the controlling guard: finite multiplicity is provisionally substantive but no computable-randomness consequence of the bare global finite cardinal fibre bound is established. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; no openness or novelty inference is made.

Authorization after P3-S008:

- Phase 3: **COMPLETED FOR GATE PURPOSES**
- Phase 4 — Mathematics: **OPEN for CAND-01**
- Phase 5 — Publication: **CLOSED**
- Phase-4 mathematics performed in P3-S008: **NO**

Formal review record: phase3/P3-S008_GATE3_REVIEW.md

## Mathematics checkpoint — P4-S001 (not a gate review)

P4-S001 completed the first bounded Phase-4 investigation on selected CAND-01, restricted to k=1.

Result: every everywhere-total computable fair-coin-preserving injective Cantor self-map is forced to be a computable fair-coin-preserving homeomorphism with an everywhere-total computable inverse. Total computability supplies effective finite forward-use bounds; injectivity effectively separates the images of fixed-level input cylinders; fair-coin preservation forces surjectivity because a missing point would have a positive-measure cylinder with empty preimage.

Applying the already-catalogued SRC-0015 / THM-0038 therefore gives computable-randomness invariance for the entire k=1 class. A map-dependent computable inverse-use modulus is forced, but no single fixed class-wide use bound exists; coordinate permutations witness arbitrarily delayed inverse use.

This is Phase-4 programme mathematics, not a Gate-4 decision and not a novelty finding. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 no-consequence guard is preserved as the pre-Phase-4 baseline; P4-S001 resolves only k=1 and makes no claim for k>=2 or general finite multiplicity. Phase 4 remains OPEN, Gate 4 is not reviewed, and Phase 5 remains CLOSED.

Record: phase4/P4-S001_MATHEMATICS.md.

## Mathematics checkpoint — P4-S002 (not a gate review)

P4-S002 completed one bounded k=2 structural investigation for selected CAND-01.

Result: k=2 forces a uniform descending computable-clopen name for every one- or two-point fibre, but does not force a total computable selector or total two-branch fibre enumeration. A concrete total computable fair-coin-preserving map with exactly one double fibre makes every global selector discontinuous.

The counterexample mechanism concerns global inverse information, not randomness destruction. That map has an a.e.-computable measure-preserving inverse, so SRC-0015 / THM-0038 gives computable-randomness invariance for it. The exactly two-to-one left shift supplies a separate direct martingale-preservation example. General k=2 preservation/failure remains unresolved.

This is not a Gate-4 decision and not a novelty finding. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; the pre-Phase-4 Gate-3 guard and exact P4-S001 result are preserved; no claim is made for k>2. Phase 4 remains OPEN and Phase 5 CLOSED.

Record: phase4/P4-S002_MATHEMATICS.md.

## Mathematics checkpoint — P4-S003 (not a gate review)

P4-S003 completed one bounded k=2 weighted-sheet / martingale-transfer investigation for selected CAND-01.

Result: k=2 forces a computable two-prefix inverse list at every requested input precision. Computable conditional sheet weights are bounded fair martingales. An explicitly supplied computable clopen split into two injective sheets suffices for forward computable-randomness preservation, but a concrete marker-and-delete k=2 map shows that no global continuous/clopen sheet colouring is forced.

The general k=2 preservation/failure question remains unresolved. The attempted SRC-0061 scan completion does not produce a valid destroyer because filler queries may pre-reveal later betting positions.

This is not a Gate-4 decision and not a novelty finding. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; the pre-Phase-4 Gate-3 guard, P4-S001, P4-S002 and DEF-0020 are preserved; no claim is made for k>2. Phase 4 remains OPEN and Phase 5 CLOSED.

Record: phase4/P4-S003_MATHEMATICS.md.

