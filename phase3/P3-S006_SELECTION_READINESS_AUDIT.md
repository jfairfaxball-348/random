# P3-S006 — Candidate-selection readiness audit

Date: 2026-10-04  
Session: `P3-S006`  
Incoming checkpoint: `d8e017893870fac451c8d555105b9295df86d05e`  
Scope: Phase 3 — Novelty / Prior Art; comparative readiness audit over surviving CAND-01 and CAND-02 only  
Outcome: **READY_FOR_SELECTION_DECISION**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly before substantive work. The incoming session ledger contained no `P3-S006` session heading and repository commit search found only the P3-S005 forward-scheduling mention of P3-S006. The session identifier was therefore unique.

Gate 1 and Gate 2 remain **PASS**. Phases 1–2 remain completed for gate purposes. Phase 3 remains **OPEN**. Gate 3 is **NOT REVIEWED** and Phase 4 remains **CLOSED**. No final candidate is selected and Fairfax-Ball Randomness is not defined.

This session audits whether the committed Phase-3 evidence is mature enough for a separate documented selection/NO-GO decision. It does **not** select a candidate, review Gate 3, prove mathematics, construct witnesses, run experiments, use Lean/Palomar, reopen retired CAND-03, perform a broad literature survey, begin Phase 4, prepare publication material or contact third parties.

No new external literature was required. The audit uses the committed P3-S001 through P3-S005 prior-art/significance, close and validation records; `phase3/prior-art.json`; `phase2/candidates.json`; the P2-S002/P2-S003 formulation alignments; and existing authority.

## Readiness standard

The audit checks whether each survivor has enough committed evidence for a later selection/NO-GO decision and, if selected, for a separate Gate-3 review to assess the Gate-3 minimum evidence. The required comparison dimensions are: dedicated prior-art attack; alternate terminology/equivalent-formulation coverage; closest-known-work clarity; equivalence/rebranding risk; significance/usefulness; likely interested communities; remaining novelty uncertainty; future theorem-package quality; and candidate-specific technical-artifact risk.

Readiness here means **decision-ready under explicit uncertainty**. It does not mean novel, open, mathematically correct, selected, or Gate-3-ready by automatic consequence.

## Comparative audit

| Dimension | CAND-01 | CAND-02 | Readiness finding |
|---|---|---|---|
| Dedicated prior-art attack | P3-S001 complete | P3-S002 complete | **SATISFIED** |
| Alternate terminology / equivalent-formulation search | finite-to-one, bounded-to-one, k/n-to-one, endomorphism randomness, total/tt-map terminology tracked | weak Birkhoff, c.e./effectively-open, lower-semicomputable observable, total/non-total operator terminology tracked | **SATISFIED** |
| Closest-known-work clarity | unrestricted endomorphism non-conservation, total fair-coin non-conservation, explicit-inverse invariance separated by hypothesis | nonergodic a.e./non-total convergence results separated from total+effectively-open ergodic/Følner benchmarks | **SATISFIED** |
| Equivalence / rebranding risk | not established either way; exact finite cardinal fibre restriction remains unmatched under inspected evidence | not established either way; exact total/effectively-open/nonergodic conjunction remains unmatched under inspected evidence | **EXPLICIT, NOT RESOLVED** |
| Significance / usefulness | P3-S004: **PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT** | P3-S005: **PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT WITH ELEVATED TECHNICAL-SLICE RISK** | **SATISFIED WITH DIFFERENT RISK LEVELS** |
| Interested communities | algorithmic randomness/computability core; computable analysis/effective probability adjacent; dynamics/information audiences conditional on real structural consequences | algorithmic randomness/computability core; effective ergodic theory/computable dynamics and computable analysis adjacent; classical ergodic interest conditional | **SATISFIED** |
| Remaining novelty uncertainty | exact restricted preservation status unresolved; no openness/novelty claim | exact characterization unresolved; no openness/novelty claim | **EXPLICIT** |
| Future theorem package | sharp preservation/failure + mechanism/characterization + boundary/sharpness + natural examples; optional information consequence only if earned | exact characterization + totality mechanism + observable-boundary theorem + placement/sharpness + natural total nonergodic examples | **SUFFICIENTLY CONCRETE FOR SELECTION** |
| Candidate-specific technical-artifact risk | **material but ordinary research risk:** finite cardinal multiplicity may have no computable-randomness effect or may collapse by known-style machinery; however the parameter itself is structurally meaningful in adjacent mathematics | **elevated representation-slice risk:** everywhere-totality may merely exclude a.e./partial witnesses, leaving a syntactically unmatched but mathematically uninformative slice | **EXPLICIT AND COMPARABLE** |

## Candidate-specific readiness judgments

### CAND-01

**READY AS A SELECTION OPTION.**

P3-S004's significance judgment is preserved exactly: finite multiplicity is provisionally substantive as a research axis, but no established evidence shows that the bare global cardinal fibre bound has any computable-randomness consequence. The exact prior-art status remains `UNRESOLVED_UNDER_INSPECTED_EVIDENCE`.

Its principal investment risk is therefore mathematical payoff rather than a missing literature category: the eventual result may show that finite multiplicity is irrelevant, routine, or insufficient. That risk is already explicit enough to compare against CAND-02 in a selection decision.

### CAND-02

**READY AS A SELECTION OPTION, WITH ELEVATED TECHNICAL-SLICE RISK.**

P3-S005's judgment is preserved exactly: nonergodic convergence-only semantics and c.e./lower-semicomputable observation complexity are independently substantive, but no inspected evidence shows that everywhere-totality changes the randomness requirement rather than merely removing a.e./partial witness representations. The exact prior-art status remains `UNRESOLVED_UNDER_INSPECTED_EVIDENCE`.

That unresolved totality issue is serious, but it is a known candidate risk rather than an unfilled readiness category. A later selection decision can legitimately reject CAND-02 because of this risk, select it despite the risk, or select neither survivor.

## Why no targeted Phase-3 session is required first

No concrete committed-reference inconsistency blocks comparison, no Gate-3 minimum-evidence category is absent at the readiness level, and no additional narrow literature question has been identified whose answer is necessary merely to choose whether either survivor merits the cost of mathematics.

Requiring Phase 3 to resolve CAND-01's finite-fibre mathematical effect or CAND-02's totality mechanism before selection would cross from prior-art/significance readiness into the mathematical questions that a selected Phase-4 programme would exist to investigate. Conversely, the selection session must not treat these uncertainties as harmless: they are the central comparative risks.

A small metadata inconsistency was found in `phase2/candidates.json`: its top-level `last_updated_session` and forward-recommendation fields lag behind the already-committed P3-S005 CAND-02 significance content. This is a synchronization defect only, not a candidate-evidence defect, and is corrected during P3-S006 closeout without changing any formulation or substantive judgment.

## Readiness outcome

**READY_FOR_SELECTION_DECISION.**

The committed evidence is sufficient for a separate Phase-3 selection/NO-GO session. This outcome makes no preference and performs no selection.

A separate selection session must compare the two surviving investment cases and record one documented programme decision:

- select **CAND-01** for subsequent Gate-3 consideration;
- select **CAND-02** for subsequent Gate-3 consideration; or
- record **NO-GO** for both survivors and specify the required backtrack/termination disposition.

That selection session must preserve the unresolved novelty language, CAND-01's lack of an established finite-fibre randomness consequence, and CAND-02's elevated totality/representation-artifact risk. It must not combine candidate selection with the formal Gate-3 review.

## Guards preserved

- CAND-01 and CAND-02 exact formulas and E1/E2 alignments remain unchanged.
- CAND-03 remains retired as `REJECT_PRIOR_ART_REBRANDING` and is not reopened.
- DEF-0020 and all Phase-1/Phase-2 evidence and convention guards remain unchanged.
- No openness, novelty, equivalence, separation, mathematical theorem, publishability or community-endorsement claim is added.
- No original mathematics or external outreach occurred.
