# P2-S003 — CAND-01 formulation alignment (E1)

Date: 2026-10-04  
Session: `P2-S003`  
Incoming checkpoint: `f15cbc0f08493c0ce8993096d0a67fda904fe610`  
Scope: Phase 2 Discovery only; CAND-01 formulation alignment only  
Disposition: **RETAIN_PROVISIONAL — SHAPE UNCHANGED; E1 RESOLVED**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly. Repository search found no P2-S003 session record; existing mentions were forward recommendations only, so P2-S003 was unique.

Gate 1 remains **PASS**. Phase 1 is **COMPLETED for gate purposes**. Phase 2 — Discovery is **OPEN**. Gate 2 is **CLOSED / NOT REVIEWED**. Phases 3–5 remain **CLOSED**. No candidate is selected and Fairfax-Ball Randomness is not defined.

This session performs only E1 for CAND-01. It does not search for a finite-to-one preservation theorem, construct a witness, prove a new implication, search for a converse or equivalent prior definition, conduct novelty/prior-art work, make novelty claims, perform experiments or original proof work, use Lean/Palomar, prepare publication/outreach, expand CAND-02 or CAND-03, review Gate 2, open later phases or begin P2-S004.

## Candidate shape retained

For each integer k≥1, let `F_k` contain the **everywhere-total computable fair-coin-preserving Cantor self-maps** F satisfying the global cardinal fibre bound

[
|F^{-1}(y)|le kquad	ext{for every }yin 2^omega.
]

CAND-01 keeps

[
R_{mathrm{fin}}(x)iff x	ext{ is computably random and }F(x)	ext{ is computably random for every }kge1	ext{ and every }Fin F_k.
]

The finite-fibre condition is retained exactly as a cardinal bound. No effective inverse branches, fibre enumeration, selector or inverse map are assumed.

## Exact hypothesis comparison

| Item | Map convention | Inverse / preimage convention | Randomness conclusion | E1 consequence |
|---|---|---|---|---|
| **CAND-01 / R_fin** | Everywhere-total computable fair-coin-preserving Cantor self-map; global `|F^{-1}(y)|≤k` | No effective inverse branches assumed | asks forward preservation of computable randomness for this restricted map class | Candidate shape. |
| **SRC-0011 / THM-0035 / DEF-0035** | Morphism is a.e.-computable on a constructive full-measure domain and measure-preserving | Isomorphism supplies morphisms in both directions with inverse identities on full-measure domains | Martin-Löf randomness conservation; isomorphism invariance | Explicit inverse-map data in the isomorphism framework is not the same recorded hypothesis as CAND-01's cardinal fibre bound. This theorem concerns Martin-Löf randomness. |
| **SRC-0015 / THM-0037** | μ-a.e.-computable Cantor map; output measure is the computable pushforward μ_T | For each μ_T-computably-random output y, there **exists** a μ-computably-random x with T(x)=y | no-randomness-from-nothing for computable randomness | This is a reverse-direction existential preimage theorem. It does not state forward preservation of computable randomness, and it has no finite-fibre hypothesis. |
| **SRC-0015 / THM-0038** | a.e.-computable measure-preserving maps F and G | F and G are inverse almost everywhere; inverse identities hold on random points | computable-randomness invariance | The theorem's inverse pair is explicit effective structure not assumed by CAND-01. No equivalence between global finite fibres and that structure is recorded. |
| **SRC-0015 / THM-0008** | a.e.-computable fair-coin-preserving self-maps | closure under conservation plus no-randomness-from-nothing | Martin-Löf maximality | A Martin-Löf property characterization, not a finite-to-one computable-randomness preservation result. |
| **SRC-0015 / THM-0039** | a.e.-computable maps across all computable Cantor-space measures | closure under conservation plus no-randomness-from-nothing | Martin-Löf point/measure maximality | Different randomness notion and ambient class; no finite-fibre conclusion for CAND-01. |

## Evidence and access

The catalogue was used first and was sufficient. No source passage required reopening.

Relevant records were already statement-inspected: SRC-0011 and SRC-0015, with exact map/inverse/preimage hypotheses preserved in DEF-0035, DEF-0036, THM-0035, THM-0037, THM-0038, THM-0008 and THM-0039. No source access level changes, new source, citation chase, theorem search, converse search or prior-art search occurred.

DEF-0020 and all Phase-1 evidence/convention guards remain untouched.

## Disposition

**Retain CAND-01 provisionally, unchanged. Resolve E1.**

Reason: the exact catalogue comparison does not identify CAND-01's map class with an already-recorded computable-randomness invariance hypothesis. The closest computable-randomness records separate existential random-preimage existence (THM-0037) from invariance under an explicit a.e.-computable inverse pair (THM-0038). The candidate's global finite cardinal fibre bound remains a distinct recorded restriction with no effective inverse information added by definition.

This is a formulation finding only. It is **not** evidence that R_fin is novel, open in the literature, distinct from computable randomness, or mathematically nontrivial. It does not assert any finite-to-one preservation or failure theorem.

## Stopping point

CAND-02 remains provisionally retained with E2 resolved and is not expanded here. CAND-03 remains provisionally retained as an auxiliary direction with E3 unresolved and is not expanded here. CAND-04–CAND-06 remain rejected exactly as recorded. No final candidate is selected. Gate 2 remains not reviewed.
