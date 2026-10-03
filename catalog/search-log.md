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

