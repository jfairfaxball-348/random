# P3-S001 — CAND-01 primary-source prior-art attack

Date: 2026-10-04  
Session: `P3-S001`  
Incoming checkpoint: `aa245847cb71116f9a8916277bab71a754e53414`  
Scope: Phase 3 — Novelty / Prior Art; CAND-01 only  
Disposition: **UNRESOLVED UNDER INSPECTED EVIDENCE**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly before substantive work. The incoming session ledger contained no P3-S001 entry and no committed P3-S001 record existed; forward recommendations were not treated as session use. P3-S001 was therefore unique.

Gate 1 and Gate 2 remain **PASS**. Phases 1–2 are completed for gate purposes. Phase 3 is **OPEN**. Gate 3 is not reviewed and Phase 4 remains closed. No final candidate is selected and Fairfax-Ball Randomness is not defined.

This session performs one bounded primary-source prior-art attack on CAND-01 only. It does not prove a preservation/failure theorem, construct witnesses as original mathematics, run experiments, use Lean/Palomar, investigate CAND-02/CAND-03, select a final candidate, review Gate 3, begin Phase 4, prepare publication material or contact third parties.

## Exact target retained

For each fixed integer (k\ge1), CAND-01 considers the everywhere-total computable fair-coin-preserving Cantor self-maps (F) satisfying the global cardinal condition

[
|F^{-1}(y)|\le k\qquad\text{for every }y\in2^\omega.
]

The candidate asks whether computable randomness is preserved forward by every such map. No effective inverse branch, fibre enumeration, selector or inverse map is assumed.

## Primary prior art inspected

### SRC-0060 — Rute, *Computable randomness and betting for computable probability spaces*

Statement-inspected at the source's morphism convention, Definition 10.1, Proposition 10.2, Theorem 10.4 and Corollary 10.7.

Rute defines an **endomorphism** as an a.e.-computable measure-preserving self-morphism and defines **endomorphism randomness** by requiring every endomorphism image to be computably random. Corollary 10.7 states that ordinary computable randomness is not preserved by unrestricted endomorphisms.

This is the closest named preservation framework found. It is broader than CAND-01 in map scope and contains no finite-fibre restriction.

### SRC-0061 — Bienvenu–Porter, *Strong reductions in effective randomness*

Statement-inspected at Definition 2.4 and Theorem 4.2.

Their terminology identifies a truth-table functional with a **total** Turing functional. Theorem 4.2 gives a truth-table functional that does not preserve computable randomness and explicitly says the example can induce fair-coin/Lebesgue measure.

Thus everywhere-totality plus fair-coin preservation is already known insufficient. The theorem does **not** state a finite/global bounded fibre hypothesis.

### Existing anchors retained

- **THM-0037 / SRC-0015:** random output implies existence of a computably random preimage for an a.e.-computable map to its pushforward. This is reverse-direction no-randomness-from-nothing.
- **THM-0038 / SRC-0015:** computable-randomness invariance for an a.e.-computable measure-preserving inverse pair. This has explicit effective inverse information absent from CAND-01.
- **THM-0035 / SRC-0011:** corresponding Martin-Löf morphism/isomorphism framework, not a finite-to-one computable-randomness theorem.

## Alternate terminology searched

Queries included `endomorphism randomness`, `endomorphism random`, `stable computable randomness`, `truth-table functional computable randomness`, `total Turing functional computable randomness`, `finite-to-one computable randomness`, `finite fibre computable randomness`, `bounded-to-one computable randomness`, `k-to-one computable randomness`, `n-to-one computable randomness`, `finite-to-one endomorphism algorithmic randomness`, `uniformly p-to-one endomorphism` and `finite-to-one factor computable randomness`.

Classical ergodic/symbolic-dynamics literature does use **uniformly p-to-one endomorphism**, **finite-to-one factor** and **bounded-to-one**. The located sources concern entropy, conjugacy or factor structure; they did not supply an algorithmic-randomness preservation theorem for the CAND-01 map class. These terms are retained as navigation vocabulary only.

## Exact hypothesis matrix

| Item | Totality | Fibre hypothesis | Effective inverse information | Direction / conclusion |
|---|---|---|---|---|
| **CAND-01** | everywhere total | global `<=k` cardinal fibres, every output | none assumed | asks forward CR conservation |
| **SRC-0060 / DEF-0064 / THM-0071** | a.e.-computable | none | none | unrestricted endomorphism CR conservation fails |
| **SRC-0061 / THM-0072** | everywhere total (tt-functional) | none stated | none | total fair-coin-preserving CR conservation fails |
| **SRC-0015 / THM-0037** | a.e.-computable | none | no inverse supplied; existential random preimage conclusion | reverse NRFN |
| **SRC-0015 / THM-0038** | a.e.-computable | no finite-fibre condition | explicit a.e.-computable inverse pair | forward invariance |

## Prior-art classification

**Disposition: UNRESOLVED_UNDER_INSPECTED_EVIDENCE.**

- **Already known:** not established for the exact CAND-01 restriction.
- **Equivalent/rebranded:** not established. There is substantial framework overlap with endomorphism randomness, but the quantification is over a strictly more restricted map class syntactically and no equivalence theorem was located.
- **Materially distinct:** not established. The finite-fibre restriction is an exact formulation difference, but this session does not elevate a syntactic difference into mathematical novelty or significance.
- **Unresolved:** yes, under the inspected evidence. No primary theorem located in this bounded search settles forward computable-randomness conservation for everywhere-total fair-coin-preserving Cantor self-maps with a fixed global finite cardinal fibre bound and no effective inverse branches.

This is **not** an assertion that the question is open, novel or publishable.

## Durable consequence

CAND-01 remains provisionally retained for Phase-3 purposes, with E1 still resolved and its formula unchanged. Its literature status is no longer NOT_ASSESSED: one dedicated primary-source attack has been performed, and the exact finite-fibre status remains unresolved under inspected evidence.

The closest-known-work narrative must now start from **endomorphism randomness** and the total truth-table non-conservation theorem rather than from isomorphism/NRFN alone.

DEF-0020 and all existing Phase-1/Phase-2 convention guards are unchanged.
