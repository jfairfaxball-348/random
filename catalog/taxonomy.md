# Phase-1 Catalogue Taxonomy

Status: **ACTIVE / evolving**  
Last refined: 2026-10-03 in `P1-S006`

This taxonomy is a retrieval vocabulary, not a claim that all listed areas are already covered. Use the controlled tag families below in structured records and add aliases/search terms where the literature uses competing terminology.

## 1. Object / domain

- `object:finite-binary-string`
- `object:infinite-binary-sequence`
- `object:subset-of-N`
- `object:real-number`
- `object:left-c.e.-real`
- `object:point-computable-metric-space`
- `object:computable-probability-space`
- `object:probability-measure-name`
- `object:oracle`

The object tag matters: finite-string incompressibility is not itself an infinite-sequence randomness notion.

## 2. Ambient space / measure

- `space:cantor`
- `space:baire`
- `space:computable-metric`
- `space:computable-probability`
- `measure:fair-coin`
- `measure:computable`
- `measure:computable-cantor`
- `measure:measure-parameter`
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
- `notion:n-randomness` — Martin-Löf randomness relative to `∅^(n−1)` in P1-S003
- `notion:kolmogorov-loveland`
- `notion:church-selection`
- `notion:demuth` — source-grounded in P1-S004; moving components with computably bounded index changes and Solovay passing
- `notion:difference-randomness` — neighborhood-based d.r.e. tests; do not confuse with the source's naive n-r.e. string tests
- `notion:balanced-randomness` — weak-Demuth-style tests with O(2^n), equivalently exact 2^n, component-index changes
- `notion:oberwolfach-randomness` — coherent weak-Demuth moving-component tests
- `notion:higher-randomness` — navigation only in P1-S001
- `notion:1-genericity` — Σ^0_1/Cohen-style finite-extension genericity; category framework, not a randomness synonym
- `notion:weak-1-genericity` — meeting every dense c.e. set of strings; strictly implies Kurtz randomness by an inspected primary statement
- `notion:n-genericity` — meet-or-avoid every Σ^0_n set of strings
- `notion:weak-n-genericity` — meet every dense Σ^0_n set of strings; distinct from `notion:weak-n`

Do not use a tag as evidence that a definition/relationship has been verified.

## 4. Test / small-set frameworks

- `framework:effective-null-test`
- `framework:martin-lof-test`
- `framework:schnorr-test`
- `framework:total-solovay-test`
- `framework:computably-graded-test`
- `framework:generalized-martin-lof-test`
- `framework:moving-component-test`
- `framework:difference-test`
- `framework:coherent-test`
- `framework:measure-one-test`
- `framework:uniform-test`
- `framework:measure-parameter-uniform-test`
- `framework:effective-open-set`
- `framework:lower-semicomputable-integral-test`
- `framework:effective-category`
- `framework:effective-meagre-set`
- `framework:effective-meager-set` — American-spelling retrieval alias for the same category notion
- `framework:dense-c.e.-open`
- `framework:finite-extension-genericity`

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
- `resource:uniform-relativization` — uniform family selected by the oracle; distinct from ordinary oracle computation for Schnorr/computable randomness
- `resource:arithmetical-level`
- `resource:omega-c.e.-index`
- `resource:computably-bounded-mind-changes`
- `resource:exponential-mind-change-bound`
- `resource:higher-computability`
- `resource:bounded-time` — boundary coverage pending

## 9. Oracle/lowness structure

- `oracle:relative-randomness`
- `oracle:low-for-randomness`
- `oracle:k-trivial`
- `oracle:base-for-randomness`
- `oracle:traceability`
- `oracle:turing-reducibility`
- `oracle:jump-relativization`
- `oracle:uniform-relative-randomness`

P1-S003 convention guard: ordinary oracle relativization and uniform relativization are not interchangeable for Schnorr/computable randomness. The inspected van-Lambalgen records are fair-coin Cantor-space statements. Where `A⊕B` occurs in SRC-0032, it is even/odd interleaving.

## 10. Structural principles

- `principle:randomness-conservation`
- `principle:no-randomness-from-nothing`
- `principle:universal-test`
- `principle:measure-preserving-map`
- `principle:computable-isomorphism`
- `principle:ae-computable-map`
- `principle:binary-representation`
- `principle:atomless-lebesgue-isomorphism`
- `principle:ergodic-typicality`
- `principle:van-lambalgen`

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
- `interface:genericity-category` — statement-level P1-S006 coverage; retain category/measure separation

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
- `A-random` / `Martin-Löf random relative to A`
- `n-random` / `∅^(n−1)-random`
- `uniformly relative Schnorr randomness` / `truth-table Schnorr randomness`
- `uniformly relative computable randomness` / `truth-table reducible randomness`
- `difference random` / `d.r.e. random` — only after fixing the neighborhood/difference-test semantics of SRC-0035
- `balanced random` / `2^n-change weak Demuth normal form`
- `Oberwolfach random` / `coherent moving-component randomness`
- `Oberwolfach randomness` / `interval-test randomness` / `left-c.e.-bounded randomness` — equivalent source-specific normal forms in SRC-0037
- `NWAP` / `A_beta` — historical Demuth-era search terms, not context-free modern synonyms
- `effectively meager` / `effectively meagre`
- `1-generic` / `Σ^0_1-generic`
- `weakly 1-generic` / `weak 1-generic`
- `weakly n-generic` / `weak n-generic`
- `Cohen genericity` / `finite-extension genericity`

P1-S004 convention guard: Demuth randomness uses **Solovay passing** (membership in only finitely many final components), whereas the inspected balanced and Oberwolfach weak-Demuth tests use ordinary escape from a component. SRC-0035 also uses `n-r.e.` in two different test semantics: its naive string-test hierarchy yields 2-randomness for n≥2, while its neighborhood/difference hierarchy yields difference randomness for n≥2. Preserve the test semantics before normalizing terminology.

Do **not** collapse `weak 2-random` into unqualified `Kurtz random`: P1-S002 source inspection identifies them as different levels of the weak-n hierarchy. Aliases are search vocabulary, not automatic mathematical equivalences.

## P1-S005 generalized-measure convention guard

The inspected generalized-space sources use **computable metric spaces** with a canonical fast-Cauchy representation of points and rational ideal balls as the effective basis. A **computable probability measure** is a computable point of the induced metric space of Borel probabilities; on Cantor space this specializes to uniform computability of cylinder measures. A **computable probability space** is the pair of such a space and such a measure. These terms are related but are not interchangeable.

`framework:measure-parameter-uniform-test` is also distinct from P1-S003's `resource:uniform-relativization`. In SRC-0038/DEF-0006 the measure itself is a represented input to a jointly lower-semicomputable test; in DEF-0024/DEF-0025 an oracle selects a uniform family of tests or martingales. Do not normalize these as one notion of “uniform randomness.”

Every inspected computable probability space has a Cantor-space representation with an **appropriate computable measure** (THM-0033). This is not a fair-coin reduction. The stronger fixed nonatomic/Lebesgue isomorphism in THM-0034 assumes **atomlessness**. Non-full support is permitted in the general machinery; support qualifications must be retained in density/representation statements.

Generalized Martin-Löf and Schnorr randomness are DEF-0033 and DEF-0034. DEF-0002 and DEF-0003 remain fair-coin Cantor-space records. No Demuth/difference/balanced/Oberwolfach result from P1-S004 is transferred to arbitrary measures or spaces without a separately inspected primary statement.


## P1-S006 category/genericity convention guard

Category and measure are two different smallness frameworks. In the inspected effective-category source, an effectively meagre set is covered by an effective (F_\sigma) union of uniformly (Pi^0_1) nowhere-dense classes; no probability value occurs in that definition. The same source explicitly presents meagre/null correspondences as an **analogy** whose results may differ. Do not translate a null-set theorem into a meagre-set theorem, or conversely, without a separately inspected statement.

For (X\in2^\omega), weak 1-genericity means meeting every **globally dense c.e.** set of strings. By contrast, the inspected 1-generic definition asks (X) to meet every c.e. set that is **dense along (X)**, equivalently to avoid (V\setminus\operatorname{Int}(V)) for every (Pi^0_1) class (V). These quantifier patterns are not interchangeable.

The higher hierarchy is likewise indexed separately: weakly (n)-generic means meeting every dense (Sigma^0_n) set of strings, while (n)-generic means meeting or avoiding every (Sigma^0_n) set of strings. The inspected primary hierarchy is
[
n\text{-generic} \supsetneq \text{weakly }(n+1)\text{-generic} \supsetneq (n+1)\text{-generic}.
]
This indexing is unrelated to `notion:weak-n` randomness. Never read “weakly n-generic” as “weakly n-random”.

The one direct P1-S006 category-to-measure bridge is source-stated: every weakly 1-generic real is Kurtz random, and the converse fails. It is recorded as `THM-0043` / `REL-0037`; it does not identify the frameworks or license extrapolation to Martin-Löf, Schnorr, higher weak randomness, or generalized measures.

`SRC-0039` (Jockusch 1980) remains `METADATA_ONLY`, `SRC-0040` (Kurtz 1983) remains `ABSTRACT_INSPECTED` via its publisher extract, and `SRC-0025` (Kurtz 1981 thesis) remains `METADATA_ONLY`. Exact genericity syntax in this pass is therefore supported by later statement-inspected primary sources rather than inferred from inaccessible originals.
