# P3-S002 — CAND-02 primary-source prior-art attack

Date: 2026-10-04  
Session: `P3-S002`  
Incoming checkpoint: `f930afb534948833feb7e3fdcda840e5922af3cf`  
Scope: Phase 3 — Novelty / Prior Art; CAND-02 only  
Disposition: **UNRESOLVED UNDER INSPECTED EVIDENCE**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly before substantive work. The incoming session ledger contained no P3-S002 entry and no committed P3-S002 session record existed; forward recommendations were not treated as session use. P3-S002 was therefore unique.

Gate 1 and Gate 2 remain **PASS**. Phases 1–2 are completed for gate purposes. Phase 3 is **OPEN**. Gate 3 is not reviewed and Phase 4 remains closed. No final candidate is selected and Fairfax-Ball Randomness is not defined.

This session performs one bounded primary-source prior-art attack on CAND-02 only. It does not prove a new theorem, construct witnesses as original mathematics, run experiments, use Lean/Palomar, investigate CAND-01 or CAND-03, select a final candidate, review Gate 3, begin Phase 4, prepare publication material or contact third parties.

## Exact target retained

On fair-coin Cantor space, CAND-02 defines `B_open(x)` by requiring that for every **everywhere-total computable fair-coin-preserving Cantor self-map** `T` and every **effectively open** set `U`, the averages

[
\frac1N\sum_{i<N}\mathbf 1_U(T^i(x))
]

converge.

There is **no ergodicity assumption**, **no equality-to-expectation clause**, **no computability requirement on `lambda(U)`**, and **no convergence modulus or rate**.

## Primary prior art inspected

### SRC-0058 — Franklin and Towsner, *Randomness and Non-Ergodic Systems*

This remains the closest characterization framework. The source explicitly distinguishes **weak Birkhoff** points, for which averages merely converge, from Birkhoff points, where the limit must also equal the integral.

THM-0063 characterizes Martin-Löf randomness by weak-Birkhoff convergence for the source's computable measure-preserving transformations and computable observables; the converse witness uses a computable set/indicator. THM-0064 gives weak-2-randomness as a sufficient condition for nonergodic convergence for lower-semicomputable observables.

The transformation convention is the decisive mismatch: SRC-0058's induced transformations are guaranteed defined/infinite outside a computable `G_delta` null set, and the converse construction is explicitly only almost-everywhere defined. The source does not establish an everywhere-total converse witness.

### SRC-0062 — Miyabe, Nies and Zhang, *Using almost-everywhere theorems from analysis to study randomness*

Statement-inspected at Section 6, especially Theorem 6.1 and the immediately following totality note.

For a computable probability measure on Cantor space, every measure-relative Oberwolfach-random point has convergent Birkhoff averages for every computable measure-preserving operator and every nonnegative integrable lower-semicomputable observable.

This is a close nonergodic convergence-only benchmark, and its observable class contains bounded effectively-open indicators. However, the source explicitly states that the operator `T` is **not assumed total**; its domain is conull and `Pi^0_2`. The result is also one-way sufficiency, not a characterization of CAND-02.

### SRC-0057 — Bienvenu, Day, Hoyrup, Mezhirov and Shen, *A constructive version of Birkhoff's ergodic theorem for Martin-Löf random points*

The source directly treats effectively-open indicators and nonnegative lower-semicomputable observables. THM-0059 and THM-0060 require a computable a.e.-defined, measure-preserving **ergodic** transformation and conclude that the average equals the measure/integral.

These results match the event-effectivity axis but not CAND-02's nonergodic convergence-only semantics.

### SRC-0063 — Moriakov, *On Effective Birkhoff's Ergodic Theorem for Computable Actions of Amenable Groups*

Statement-inspected at the computable-map/action conventions and Lemma 3.1.

The source's Cantor mappings are everywhere-total maps `2^N -> 2^N`, and its effectively-open indicator theorem gives convergence to `mu(U)` for Martin-Löf-random points. But this occurs inside a computable **ergodic group action by automorphisms** and uses a computable tempered two-sided Følner sequence.

Thus this source supplies a useful **total-map + effectively-open-event** benchmark, but it adds ergodicity, expectation equality, invertible group-action structure and a different averaging scheme. It is not an exact theorem about arbitrary one-sided iterates of a total measure-preserving self-map.

## Alternate terminology searched

Queries included `weak Birkhoff`, `weakly Birkhoff`, `Birkhoff point`, `effectively open Birkhoff`, `c.e. open Birkhoff`, `Sigma^0_1 Birkhoff`, `enumerable event ergodic average`, `lower semicomputable observable`, `computable measure-preserving operator`, `computable measure-preserving transformation`, `total computable transformation`, `nonergodic Birkhoff convergence`, `Oberwolfach random Birkhoff` and `weak 2 random Birkhoff`.

A terminology hazard is material here: inspected primary sources do not use **computable transformation/operator** uniformly with respect to totality. Some allow a conull effective domain; others explicitly use total maps and separately name a.e.-computability. CAND-02's everywhere-total requirement therefore remains an explicit hypothesis, not a terminological normalization.

## Exact hypothesis matrix

| Item | Totality / map structure | Observable | Ergodicity | Conclusion / averaging |
|---|---|---|---|---|
| **CAND-02** | everywhere-total arbitrary computable fair-coin-preserving self-map | effectively-open indicator | none | one-sided iterates; convergence only; no equality or modulus |
| **SRC-0058 / THM-0063** | a.e.-defined computable measure-preserving transformation | computable observables; computable set in converse | none | characterization of ML by convergence only |
| **SRC-0058 / THM-0064** | same a.e.-defined convention | lower semicomputable observable, hence broader than open indicators | none | weak-2 sufficiency for convergence only |
| **SRC-0062 / THM-0073** | computable measure-preserving operator explicitly not assumed total | nonnegative integrable lower semicomputable observable | none | Oberwolfach-random sufficiency for convergence only |
| **SRC-0057 / THM-0059–0060** | computable a.e.-defined measure-preserving transformation | effectively-open indicator / lower semicomputable observable | **required** | one-sided averages equal measure/integral |
| **SRC-0063 / THM-0074** | total computable Cantor maps inside an action by automorphisms | effectively-open indicator | **required** | Følner averages equal measure |

## Prior-art classification

**Disposition: UNRESOLVED_UNDER_INSPECTED_EVIDENCE.**

- **Already known:** not established for the exact CAND-02 predicate.
- **Equivalent/rebranded:** not established. The candidate substantially overlaps the established weak-Birkhoff/effective ergodic literature, but no inspected equivalence theorem transfers the a.e.-defined transformation characterizations to the everywhere-total predicate.
- **Materially distinct:** not established. The exact hypothesis combination differs from the inspected theorems, but this session does not elevate a syntactic/hypothesis difference into mathematical novelty or significance.
- **Unresolved:** yes, under the inspected evidence. No primary theorem located in this bounded attack states the exact combination of everywhere-total arbitrary fair-coin-preserving Cantor self-maps, effectively-open indicators, nonergodic convergence-only semantics, no equality clause and no modulus.

This is **not** an assertion that the question is open, novel or publishable.

## Durable consequence

CAND-02 remains provisionally retained for Phase-3 purposes, with E2 still resolved and its exact formulation unchanged. Its literature status is no longer NOT_ASSESSED: one dedicated primary-source attack has been performed, and its exact total-map/effectively-open/nonergodic status remains unresolved under inspected evidence.

The closest-known-work narrative must now distinguish at least four axes—map totality/structure, observable effectivity, ergodicity and conclusion strength—and must not infer equivalence merely because a source matches three of them.

CAND-01 and CAND-03 were not substantively investigated in this session. DEF-0020 and all existing Phase-1/Phase-2 convention/evidence guards are unchanged.
