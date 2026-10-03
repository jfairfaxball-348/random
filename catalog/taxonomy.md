# Phase-1 Catalogue Taxonomy

Status: **ACTIVE / evolving**  
Last refined: 2026-10-03 in `P1-S002`

This taxonomy is a retrieval vocabulary, not a claim that all listed areas are already covered. Use the controlled tag families below in structured records and add aliases/search terms where the literature uses competing terminology.

## 1. Object / domain

- `object:finite-binary-string`
- `object:infinite-binary-sequence`
- `object:subset-of-N`
- `object:real-number`
- `object:left-c.e.-real`
- `object:point-computable-metric-space`
- `object:computable-probability-space`
- `object:oracle`

The object tag matters: finite-string incompressibility is not itself an infinite-sequence randomness notion.

## 2. Ambient space / measure

- `space:cantor`
- `space:baire`
- `space:computable-metric`
- `measure:fair-coin`
- `measure:computable`
- `measure:biased`
- `measure:arbitrary-probability`
- `measure:effective-null`
- `measure:integral-test`

## 3. Core randomness notions encountered

- `notion:martin-lof`
- `notion:schnorr`
- `notion:computable-randomness`
- `notion:kurtz` — source-grounded as unqualified weak/weak-1 randomness
- `notion:weak-n` — weakly n-random / w-n-random / Kurtz n-random in SRC-0027
- `notion:weak-2` — distinct higher weak-n level, not an alias of unqualified Kurtz randomness
- `notion:kolmogorov-loveland`
- `notion:church-selection`
- `notion:demuth` — navigation only in P1-S001
- `notion:higher-randomness` — navigation only in P1-S001

Do not use a tag as evidence that a definition/relationship has been verified.

## 4. Test / small-set frameworks

- `framework:effective-null-test`
- `framework:martin-lof-test`
- `framework:schnorr-test`
- `framework:total-solovay-test`
- `framework:computably-graded-test`
- `framework:generalized-martin-lof-test`
- `framework:measure-one-test`
- `framework:uniform-test`
- `framework:effective-open-set`
- `framework:lower-semicomputable-integral-test`
- `framework:effective-category` — coverage pending

## 5. Betting / prediction / selection

- `framework:martingale`
- `framework:r.e.-martingale`
- `framework:computable-martingale`
- `framework:bounded-rate-martingale`
- `framework:lower-semicomputable-martingale`
- `framework:nonmonotonic-betting`
- `framework:place-selection`
- `framework:nonmonotonic-selection`
- `framework:stochasticity`
- `framework:typicality`

## 6. Complexity / information

- `complexity:plain-C`
- `complexity:prefix-free-K`
- `complexity:incompressibility`
- `complexity:program-size`
- `complexity:initial-segment`
- `complexity:algorithmic-information`

Future additions should distinguish monotone, a priori, process and resource-bounded complexities rather than folding them into `K`.

## 7. Dimension / graded randomness

- `dimension:constructive`
- `dimension:effective-hausdorff`
- `dimension:supergale`
- `dimension:finite-string`
- `dimension:resource-bounded` — boundary coverage pending

## 8. Computability resource / relativization

- `resource:computable`
- `resource:c.e.`
- `resource:lower-semicomputable`
- `resource:oracle-relative`
- `resource:arithmetical-level`
- `resource:higher-computability`
- `resource:bounded-time` — boundary coverage pending

## 9. Oracle/lowness structure

- `oracle:relative-randomness`
- `oracle:low-for-randomness`
- `oracle:k-trivial`
- `oracle:base-for-randomness`
- `oracle:traceability`
- `oracle:turing-reducibility`

## 10. Structural principles

- `principle:randomness-conservation`
- `principle:no-randomness-from-nothing`
- `principle:universal-test`
- `principle:measure-preserving-map`
- `principle:computable-isomorphism`
- `principle:ergodic-typicality`

## 11. Relation types

Use only when source-supported:

- `relation:implication`
- `relation:strict-implication`
- `relation:equivalence`
- `relation:incomparability`
- `relation:separation`
- `relation:relativized`
- `relation:characterization`
- `relation:property-holds`
- `relation:property-fails`

Never infer strictness from differing definitions.

## 12. Historical / foundational axis

- `history:borel-normality`
- `history:von-mises-collective`
- `history:church-selection`
- `history:kolmogorov-complexity`
- `history:martin-lof-tests`
- `history:schnorr-effectivity`
- `history:kurtz-weak-randomness`
- `history:demuth`

## 13. Interface areas

- `interface:probability`
- `interface:ergodic-theory`
- `interface:logic`
- `interface:computability`
- `interface:information-theory`
- `interface:computable-analysis`
- `interface:pseudorandomness` — boundary only
- `interface:derandomization` — boundary only
- `interface:genericity-category` — coverage pending

## 14. Evidence / access

Structured source records must use the repository access levels:

- `METADATA_ONLY`
- `ABSTRACT_INSPECTED`
- `STATEMENT_INSPECTED`
- `PROOF_INSPECTED`
- `SECONDARY_ONLY`
- `UNAVAILABLE`

Additionally use `inspected_material` and `pointers` to say what was actually seen. An author-hosted preprint statement may support a theorem statement when matched to the published bibliographic record; record that provenance explicitly.

## 15. Status-sensitive claims

Question records use exactly:

- `SOURCE-STATED OPEN`
- `SOURCE-STATED RESOLVED`
- `CURRENT STATUS UNKNOWN`
- `STATUS UNDER CHECK`

Every such record must identify the source/year stating the status and whether a later-status check has been done.

## 16. Retrieval aliases already observed

Important query aliases include:

- `1-random` / `Martin-Löf random`
- `recursive randomness` / `computable randomness`
- `KL-random` / `Kolmogorov-Loveland random`
- `base for randomness` / `basis for randomness`
- `randomness preservation` / `randomness conservation`
- `no randomness from nothing` / `no randomness ex nihilo`
- `constructive dimension` / `effective Hausdorff dimension`
- `place selection` / `selection rule`
- `collective` / `Kollektiv`
- `Kurtz random` / `weakly random` / `weakly 1-random`
- `weakly n-random` / `w-n-random` / `Kurtz n-random`

Do **not** collapse `weak 2-random` into unqualified `Kurtz random`: P1-S002 source inspection identifies them as different levels of the weak-n hierarchy. Aliases are search vocabulary, not automatic mathematical equivalences.
