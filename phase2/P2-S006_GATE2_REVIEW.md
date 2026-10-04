# P2-S006 — Formal Gate-2 Review

Date: 2026-10-04  
Session: `P2-S006`  
Incoming checkpoint: `8590d713f145ecddb1aba0dfddfc120664cf5171`  
Scope: formal Gate 2 — Discovery -> Novelty / Prior Art review only  
Formal outcome: **PASS**

## Authority and session uniqueness

Live `main` was pinned before substantive review and matched the expected incoming checkpoint exactly. The committed `phase2/` directory contained records only through P2-S005, and the incoming session ledger contained no `## P2-S006` session entry. Existing P2-S006 mentions were forward scheduling only, so the session identifier was unused.

Incoming posture was confirmed from committed authority: Gate 1 PASS; Phase 1 completed for gate purposes; Phase 2 OPEN; P2-S005 = READY_FOR_FORMAL_GATE2_REVIEW only; Gate 2 not yet formally reviewed/passed; Phases 3–5 CLOSED; no final candidate selected; Fairfax-Ball Randomness not defined.

This session uses committed records only. It performs no novelty/prior-art search, equivalent-definition search, proof, witness construction, experiment, original mathematics, Lean/Palomar work, candidate selection or Phase-3 substantive work.

## Independent Gate-2 evidence review

The P2-S005 readiness conclusion was not treated as dispositive. The P2-S001 portfolio, current `phase2/candidates.json`, P2-S002 through P2-S004 formulation/close/validation records, and the complete P2-S005 audit/close/validation records were independently checked against `docs/GATE_POLICY.md`.

| Gate-2 minimum evidence | P2-S006 finding |
|---|---|
| bounded candidate portfolio | **SATISFIED.** Six stable candidates are recorded: three retained provisionally and three rejected in preserved shapes. |
| each live candidate stated precisely enough to search for prior art | **SATISFIED.** CAND-01 fixes total fair-coin-preserving maps plus a global finite cardinal fibre bound; CAND-02 fixes total fair-coin-preserving dynamics plus effectively-open indicators and convergence-only semantics; CAND-03 fixes universal oracle lowness using DEF-0025 globally total/valid uniform families. |
| motivation and potential mathematical value | **SATISFIED.** Each retained direction states a structural motivation and a useful outcome even if it collapses. |
| relationship to known concepts | **SATISFIED.** Each retained direction is anchored to stable DEF/THM/REL records with the relevant convention distinctions explicit. |
| plausible theorem package or characterization target | **SATISFIED.** Each retained candidate has an exact future characterization/preservation target. |
| falsifiers/failure conditions | **SATISFIED.** All three state collapse, rebranding or routine-instance conditions that would retire or demote the direction. |
| dependencies and expected difficulty | **SATISFIED.** Dependencies are explicit and all three are high difficulty; CAND-03 also records significance risk. |
| explicit separation between “appears interesting” and “is novel” | **SATISFIED.** Candidate novelty/literature status remains NOT_ASSESSED and every formulation record disclaims novelty inferences. |

## Candidate-by-candidate review

### CAND-01

**PASS for Gate-2 maturity.** The exact `R_fin` predicate is search-ready. E1 is resolved without converting a cardinal finite-fibre bound into effective inverse data or turning THM-0037's existential random-preimage theorem into forward conservation. The direction has a clear explanatory motivation, plausible preservation/failure package, explicit falsifiers and high expected difficulty.

Residual risk: it may be a routine known finite-to-one preservation fact, may collapse to CR, or may have no explanatory value. That is a Phase-3 prior-art target and later mathematical risk, not missing Discovery evidence.

### CAND-02

**PASS for Gate-2 maturity.** The `B_open` predicate fixes everywhere-total computable fair-coin-preserving maps, effectively open event indicators, nonergodic convergence only, no equality-to-expectation clause and no modulus. E2 is resolved: SRC-0058's converse map is only established almost everywhere, while CAND-02 deliberately requires totality.

Residual risk: the exact predicate may already be characterized under other terminology or the apparent distinction may be a representation artifact. The arXiv-copy qualification for SRC-0058 remains live. These are Phase-3 exposure, not Gate-2 blockers.

### CAND-03

**PASS for Gate-2 maturity as an auxiliary structural direction.** The class `L_u` is precisely quantified; E3 preserves the global all-oracle family convention and separates pairwise relative randomness, universal lowness and existential baseness. Its value criterion requires an intrinsic characterization plus a concrete randomness/product-information consequence.

Residual risk: an established lowness/traceability class may already characterize it, universal quantification may collapse the distinction, or the oracle-class result may lack programme significance. The broader lowness/traceability landscape is a Phase-3 exposure, not a missing Gate-2 field.

## Rejected shapes and formulation tasks

E1, E2 and E3 remain resolved.

CAND-04, CAND-05 and CAND-06 remain rejected exactly in their recorded shapes: CAND-04 by THM-0008; CAND-05 by THM-0026 with DEF-0020 unchanged; CAND-06 by THM-0024. No rejected shape is revived, weakened or reformulated.

## Residual weaknesses carried forward

The retained candidates all have high collapse/redundancy risk. CAND-03 additionally carries significance risk. The Phase-1 catalogue remains bounded/non-exhaustive and all provenance/access cautions remain authoritative. None prevents an honest Phase-3 prior-art attack; they define what that attack must stress-test.

## Formal decision

**Gate 2 outcome: PASS.**

Reason: the Discovery portfolio is bounded, internally coherent, and contains multiple candidates precise and motivated enough for dedicated prior-art attack, with explicit theorem targets, falsifiers, dependencies/difficulty and novelty guards. This satisfies every Gate-2 minimum-evidence requirement in `docs/GATE_POLICY.md`.

PASS does **not** mean any candidate is novel, open, distinct or nontrivial; that the catalogue is exhaustive; that any candidate has survived prior art; that a final candidate is selected; or that Fairfax-Ball Randomness has been defined.

## Authorization effect

This PASS completes Phase 2 for gate purposes and opens Phase 3 — Novelty / Prior Art. Phases 4–5 remain CLOSED. Candidate selection remains unset.

No Phase-3 substantive work was performed in P2-S006. The smallest next task is P3-S001, a dedicated primary-source prior-art attack on CAND-01 only.

No owner/external blocker exists.
