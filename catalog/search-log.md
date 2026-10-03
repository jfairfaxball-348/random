# Phase-1 Search and Retrieval Log

## P1-S001 — 2026-10-03

Scope: foundational territory mapping and first corpus acquisition only. Searches were used to locate primary sources, authoritative monographs/surveys, exact metadata, accessible statements, and later-status evidence. Search failure is **never** treated as nonexistence.

### Productive locations

- Publisher/journal pages: Elsevier/ScienceDirect, ACM metadata, Oxford Academic, Springer, Cambridge Core, Wiley/Oxford journal pages.
- Stable scholarly metadata: DOI landing pages, Math-Net.Ru, DBLP.
- Open/preprint sources: arXiv, Dagstuhl LIPIcs, author-hosted University of Chicago PDFs/pages.
- Author pages were useful for matching preprints to final publication metadata.
- ResearchGate and generic metadata aggregators were used only as discovery/metadata cross-checks when stronger sources were unavailable; they were not allowed to settle priority by themselves.

### Query families that worked

- Exact-title + author + DOI queries for seminal papers.
- Notion + original author + year: `Martin-Löf 1966 random sequences`, `Church random sequence 1940`, `Schnorr randomness`.
- Relationship queries: `low for Martin-Löf randomness K-trivial`, `basis for randomness K-trivial`.
- Generalization queries: `Martin-Löf randomness computable metric space`, `Schnorr randomness computable probability spaces`.
- Structural-principle queries: `randomness conservation no randomness from nothing`.
- Status queries with recent-year terms: `Kolmogorov-Loveland Martin-Löf open problem 2025`.
- Dimension queries: `constructive Hausdorff dimension Kolmogorov complexity`.

### Citation-following routes

- SRC-0007 (Downey–Hirschfeldt survey) supplied terminology and citations for the three main paradigms: statistical tests, incompressibility, and betting.
- SRC-0009 and SRC-0010 were followed to establish the lowness/K-triviality/bases cluster without inferring equivalences from terminology.
- SRC-0011 led to the beyond-Cantor/computable-probability-space stratum.
- SRC-0018 led to a deliberate later-status check for QST-0001, resulting in SRC-0019 (2025).

### Retrieval/access limitations

1. **Original Schnorr source not yet statement-inspected.** Searches located later primary and survey sources, including SRC-0008, but P1-S001 did not complete a reliable original-source statement extraction for Schnorr's foundational test formulation. Result: DEF-0003 is supported by an inspected authoritative survey, with this provenance gap explicit.
2. **Kurtz primary definition not yet acquired.** Stuart Kurtz's thesis/work surfaced in citations/searching, but no primary definition statement was inspected. Result: no Kurtz DEF or relationship edge was created.
3. **Demuth original sources not yet acquired.** SRC-0016 gives a modern historical/technical map, but exact original definitions remain a later retrieval task.
4. **Higher-randomness chapter access is restricted.** SRC-0017's publisher summary is inspected, but the full Cambridge chapter was not available through open access in this session; no higher DEF record was promoted.
5. **Major monographs are partly paywalled.** SRC-0005 and SRC-0006 are important navigational anchors but chapter-level statements were not silently upgraded to `STATEMENT_INSPECTED`.
6. **Martin-Löf original paper not fully indexed.** Publisher abstract was inspected; primary internal definitions/theorems still need a dedicated pass despite accessible copies/mirrors.
7. **No proof inspections were claimed in P1-S001.** This session prioritized architecture and foundational breadth; exact proof-level checking remains future Phase-1 work where consequential.

### Meaningful search correction

A title-only search for Chaitin's *On the Length of Programs for Computing Finite Binary Sequences* can mix the 1966 JACM paper (13(4), 547–569, DOI 10.1145/321356.321363) with a distinct 1969 follow-up carrying “Statistical considerations” (16(1), 145–159, different DOI). P1-S001 cross-checked year, volume, pages and DOI before creating SRC-0004.

### Unsuccessful/incomplete searches to resume

- Exact original Schnorr publication(s) for the foundational test definition and their theorem numbering.
- Primary Kurtz definition source/full thesis text and exact modern normalization.
- Original Demuth papers relevant to Demuth randomness.
- Primary sources for weak n-randomness, difference randomness and other stronger notions beyond the survey-level mentions encountered.
- Dedicated sources for resource-bounded randomness/pseudorandomness boundary.
- Dedicated effective-category/genericity sources.
- Original sources for van Lambalgen's central relativization theorem; SRC-0020 was only abstract-inspected.

### Current terminology vocabulary for later searches

`Martin-Löf random`; `1-random`; `effective null test`; `Schnorr test`; `computably random`; `recursive random`; `Kurtz random`; `weak 2-random`; `Demuth random`; `Kolmogorov-Loveland`; `nonmonotonic betting`; `selection rule`; `Church stochastic`; `K-trivial`; `low for random`; `base for randomness`; `computable probability space`; `uniform randomness test`; `randomness conservation`; `no randomness from nothing`; `constructive dimension`; `effective Hausdorff dimension`; `higher randomness`; `Pi11 randomness`.

## P1-S002 — 2026-10-03

Scope: primary-source consolidation of Schnorr randomness, computable/recursive randomness, Kurtz randomness, weak n-randomness and weak 2-randomness. Search failure is not treated as nonexistence.

### Primary/strong sources inspected
- Schnorr originals were located bibliographically as SRC-0022/SRC-0023; internal statements remain uninspected.
- SRC-0008 was upgraded to statement-inspected from its full 2002 paper.
- SRC-0024 supplied primary computable-martingale and computably-graded-test statements.
- Kurtz's 1981 thesis (SRC-0025) was bibliographically anchored but remains metadata-only internally.
- SRC-0026 supplies the primary abstract-level Kurtz definition.
- SRC-0027 supplies statement-level weak-n, weak-2 and generalized-ML-test definitions/relations.
- SRC-0028 supplies statement-level martingale formulations and strictness witnesses.
- SRC-0029 supplies statement-level Kurtz test/martingale formulations and the strict Schnorr→Kurtz edge.

### Definition/convention reconciliation
1. Schnorr: SRC-0008 uses `μ(U_n)≤2^-n` plus computable level measures; SRC-0024/SRC-0028 use exact `μ(U_n)=2^-n` normal forms.
2. Computable randomness: primary sources confirm no computable/recursive martingale succeeds; SRC-0024 also gives the computably graded-test characterization.
3. Unqualified Kurtz/weak randomness is weak-1; weak 2-randomness is a distinct higher weak-n level.
4. Weak-2 generalized tests require measures tending to zero without a computable convergence rate.

### Relationship evidence added
Primary statements now support the local strict chain `weak 2 → Martin-Löf → computable/recursive → Schnorr → Kurtz`, plus total-Solovay, computably-graded and generalized-ML test characterizations.

### Remaining access gaps
- No statement-level copy of Schnorr's 1971 original book/article was reliably inspected.
- No statement-level copy of Kurtz's 1981 thesis was obtained.
- Demuth originals and other stronger notions were intentionally outside this bounded session.


## P1-S003 — 2026-10-03

Scope: primary-source consolidation of relative/oracle randomness, exact relativization conventions, van Lambalgen statements, and the n-random/weak-n bridge. Search failure is not treated as nonexistence.

### Primary/strong sources inspected
- SRC-0030 (Downey–Hirschfeldt–Miller–Nies) supplies an exact fair-coin A-Martin-Löf-test definition, the convention n-random = Martin-Löf random relative to ∅^(n−1), and a two-part van Lambalgen statement.
- SRC-0010 was upgraded within its existing record: Definition 1.7 and the following paragraph give the exact A-computable-martingale definition of computable randomness relative to A and the general low-for-R convention.
- SRC-0031 (Franklin–Stephan–Yu) gives statement-level martingale/rate formulations of Schnorr and Kurtz randomness relative to A.
- SRC-0032 (Miyabe–Rute) defines uniformly relative Schnorr/computable randomness and proves the exact uniform-relative van-Lambalgen statements recorded in THM-0023/THM-0024; Corollary 5.4 separates uniform from ordinary relative computable randomness.
- SRC-0033 is van Lambalgen's 1990 *The Axiomatization of Randomness*. Its Section 5 was visually statement-inspected at Definitions/Theorems 5.3, 5.9 and 5.10.

### Convention reconciliation
1. Martin-Löf: ordinary oracle relativization uses uniformly A-c.e. test components; SRC-0032 states its uniform-relative variant coincides with ordinary relative ML randomness.
2. n-randomness: the inspected convention is ML-randomness relative to ∅^(n−1). This is now explicit in DEF-0020 and is the convention used to read the n-random side of the P1-S002 weak-n sandwich.
3. Schnorr/computable: ordinary oracle relativization must not be collapsed with Miyabe–Rute uniform relativization. The latter uses a single total computable family whose oracle instance supplies the test/martingale.
4. van Lambalgen: THM-0021 is recorded only in fair-coin Cantor space. SRC-0032 uses even/odd interleaving for `A⊕B`. The uniform Schnorr theorem is asymmetric like the ML theorem; the computable-randomness theorem inspected here is the weaker symmetric mutual-relative form.
5. Kurtz: SRC-0031 supplies an ordinary oracle martingale/rate formulation. No generalized-measure oracle-Kurtz normalization is inferred.

### Retrieval/provenance correction
The P1-S002 coverage note treated the already catalogued 1987 SRC-0020 as if it were the uninspected source of the central van Lambalgen relativization theorem. Exact citation following showed that the original source used by the later theorem literature is the 1990 SRC-0033. The 1987 record remains valid for its own selection-rule/statistical-test topic but is no longer used as the theorem anchor.

### Remaining access gaps
- The original Merkle et al. counterexample paper behind failure of the naive forward van-Lambalgen direction for ordinary Schnorr/computable randomness was not separately statement-inspected; SRC-0032's explicit report is retained without manufacturing a new strictness record from definitions.
- Arbitrary computable measures/spaces were outside this bounded fair-coin relativization pass.
- Broader lowness/base/traceability families were intentionally not surveyed beyond exact cross-links needed here.
