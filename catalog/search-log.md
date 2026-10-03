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


## P1-S004 — 2026-10-03

Scope: primary-source consolidation of the stronger test-randomness stratum: Demuth, difference, balanced and Oberwolfach randomness, with only exact cross-links to the already-normalized 2-/n-random, weak-2 and Martin-Löf records. Search failure is not treated as nonexistence.

### Primary/strong sources inspected
- SRC-0034: Osvald Demuth's 1982 original Russian paper was recovered from DML-CZ and visually inspected at printed pp. 457-458. The moving limit-index, computable change-bound and 2^-k measure machinery is present in the original historical arithmetic-real formulation.
- SRC-0016 was upgraded to STATEMENT_INSPECTED. Its §4.4 gives the modern Demuth-test definition, identifies f≤wtt∅' with an ω-c.e. index having a computable bound on changes, and decodes the original 1982 notation and later WAP/NWAP terminology.
- SRC-0035 (Franklin–Ng) was statement-inspected from a coauthor-hosted copy matched to Proc. AMS metadata. Definition 2.3, Theorem 2.8, Proposition 2.10/Figure 1 and Theorem 3.1 ground difference randomness and its strict placement.
- SRC-0036 (Figueira–Hirschfeldt–Miller–Ng–Nies) was statement-inspected at Definition 14, Remarks 16-18 and Proposition 19 for balanced randomness and its O(2^m) / exact-2^m normal form.
- SRC-0037 (Bienvenu–Greenberg–Kučera–Nies–Turetsky) was statement-inspected from the EMS paper at Definitions 2.2-2.3 and Propositions 2.4, 2.5 and 2.15 for Oberwolfach coherence, strict placement and equivalent test normal forms.

### Definition and terminology reconciliation
1. Demuth tests use moving c.e.-open components with an ω-c.e. (equivalently, in SRC-0016, weak-truth-table-∅') index whose mind changes are computably bounded by the level. The modern levels satisfy μ(U_m)≤2^-m.
2. Demuth randomness uses Solovay passing: a real lies in only finitely many final test components. This is not the same pass condition as the weak-Demuth framework used for balanced/Oberwolfach randomness, where escaping a component suffices.
3. Balanced tests impose an O(2^m) bound on changes of the m-th component index; SRC-0036 states that exact 2^m changes is an equivalent normal form.
4. Oberwolfach tests are weak Demuth tests with coherence across levels: while level n stays fixed over an interval of stages, level n+1 changes at most once.
5. SRC-0035 has a genuine n-r.e. terminology collision. Its naive n-r.e. tests of strings yield 2-randomness for n≥2; its neighborhood/difference n-r.e. tests collapse for n≥2 to difference randomness. The catalogue records only the latter as DEF-0027 and keeps the collision explicit.
6. Where SRC-0035 says 2-randomness, P1-S004 reads it through DEF-0020's existing convention: Martin-Löf randomness relative to ∅'. No new oracle survey was opened.

### Source-supported relationship additions
- 2-randomness strictly implies both Demuth randomness and weak 2-randomness.
- Demuth randomness and weak 2-randomness are incomparable.
- Each of Demuth and weak 2-randomness strictly implies difference randomness, which strictly implies Martin-Löf randomness.
- Balanced randomness strictly implies Oberwolfach randomness, which strictly implies difference randomness.
- SRC-0036 independently supplies the direct strict balanced-to-difference edge.
- Difference randomness is exactly Martin-Löf randomness plus Turing incompleteness.
- Oberwolfach, interval-test and left-c.e.-bounded randomness coincide in SRC-0037's fair-coin setting.

### Retrieval failures and access qualifications
- The original Demuth paper is accessible but in Russian and in historical constructive notation. No independent complete English translation was located in this bounded pass; modern normalization is cross-checked with SRC-0016/SRC-0035 rather than supplied by guesswork.
- A direct Franklin-hosted PDF route timed out during retrieval; the same primary paper was successfully obtained from coauthor Keng Meng Ng's site and matched against Proc. AMS metadata.
- No generalized-measure, oracle-relative or higher analogues of the four stronger notions were inferred from the fair-coin sources.

### Bounded exclusions
No Fairfax-Ball candidate was invented or selected; no Phase-2 target selection or novelty audit was performed; no original mathematics/proof search, Lean/Palomar work, manuscript work, publication preparation or external outreach was performed.


## P1-S005 — 2026-10-03

Scope: primary-source consolidation of computable measures, computable probability spaces, generalized-measure Martin-Löf/Schnorr randomness, and only the exact representation/invariance/conservation/no-randomness-from-nothing links needed to connect COV-0001, COV-0012 and COV-0013. Search failure is not treated as nonexistence.

### Primary sources inspected or upgraded
- SRC-0011 (Hoyrup–Rojas 2009) was re-inspected at statement level for computable metric spaces and canonical Cauchy representations; computable Borel probability measures and equivalent valuation criteria; binary representations of computable probability spaces; uniform integral tests; morphism conservation; and isomorphism invariance on Martin-Löf random points.
- SRC-0012 (Gács–Hoyrup–Rojas 2011) was upgraded from abstract-only to STATEMENT_INSPECTED. Exact statements now support the computable-probability-space definition, a.e.-computable measure-preserving morphisms/isomorphisms, general Martin-Löf and Schnorr tests, Cantor representation with an appropriate computable measure, the atomless computable-Lebesgue-space theorem, and Schnorr conservation under morphisms.
- SRC-0015 (Rute 2016) was upgraded from abstract-only to STATEMENT_INSPECTED. Definition 2/6, Theorem 7, Lemma 8, Theorem 25/Corollary 26 and Theorems 33/36 now ground exact computable-measure Cantor-space randomness, a.e.-computable map hypotheses, computable-randomness NRFN/isomorphism invariance, Schnorr NRFN failure, and distinct all-measure versus fair-coin maximality statements.
- SRC-0038 (Bienvenu–Gács–Hoyrup–Rojas–Shen 2011) was added at STATEMENT_INSPECTED for computable Cantor-space measures, Martin-Löf P-tests, explicit Bernoulli/non-symmetric-coin class tests, arbitrary-measure uniform tests, and the fixed-P/uniform-test correspondence.

### Exact convention reconciliation
1. A computable metric space, a computable probability measure, and a computable probability space are separate records (DEF-0030/0031/0032). The inspected general-space theory is metric/Cauchy-representation based; no theorem for arbitrary represented spaces is inferred.
2. Generalized Martin-Löf randomness (DEF-0033) uses uniformly effective open levels with μ(A_n)≤2^-n. Generalized Schnorr randomness (DEF-0034) adds uniform computability of the real level measures μ(A_n). The exact-equality fair-coin normal form from some P1-S002 sources is not silently transplanted.
3. Uniformity has two distinct meanings in the repository: measure-parameter uniform tests (DEF-0006/SRC-0038) versus uniform oracle relativization (DEF-0024/DEF-0025). They are not aliases.
4. Every computable probability space has a Cantor representation with an appropriate computable measure. This is not automatically fair coin. The stronger reduction to a fixed Lebesgue/nonatomic model requires atomlessness (THM-0034).
5. Atoms are allowed in the basic computable-probability-space machinery. Non-full support is also allowed; source-specific support qualifications are retained for representation-domain density.

### Conservation / no-randomness-from-nothing scope
- ML randomness: SRC-0011 gives conservation under computable-probability-space morphisms and isomorphism invariance; SRC-0015 Theorem 33 gives the all-computable-Cantor-measure maximality of ML under conservation + NRFN, while Theorem 36 separately gives the fair-coin self-map form.
- Schnorr randomness: SRC-0012 Proposition 3.27 gives conservation under computable-probability-space morphisms. SRC-0015 Theorem 25/Corollary 26 shows NRFN fails for the broader a.e.-computable Cantor-space map class. These are different properties and map formulations.
- Computable randomness: SRC-0015 Theorem 7 gives NRFN for arbitrary computable Cantor-space source measures and their pushforwards; Lemma 8 gives invariance for a.e.-computable measure-preserving isomorphisms. The fair-coin martingale definition DEF-0004 is not used as a substitute for the μ-random definition DEF-0036.

### Retrieval failures / qualifications
- The historical standalone Shen antecedent for Martin-Löf no-randomness-from-nothing was not independently recovered as an original source in this bounded session. Exact modern primary statements are retained from inspected papers rather than reconstructing the folklore attribution.
- No bounded primary source for a fully general arbitrary represented-space probability formalism was added. The repository therefore says “computable metric/probability space” where that is what the sources prove, rather than silently broadening to every represented space.
- Rute's proposed fully uniform-relativized computable-randomness NRFN extension appears as Conjecture 21 in the inspected paper; it is not promoted to a theorem.
- No generalized-measure version of Demuth, difference, balanced or Oberwolfach randomness was searched into the catalogue merely by analogy; their P1-S004 records remain fair-coin-only.

### Bounded exclusions
No Fairfax-Ball candidate was invented or selected; no Phase-2 target selection or dedicated novelty audit was performed; no original mathematics/proof search, Lean/Palomar work, manuscript/publication work or external outreach was performed.


## P1-S006 — 2026-10-03

Scope: primary-source consolidation of COV-0019, restricted to effective category/meagreness, the principal computability-theoretic genericity notions needed to separate weak/1/higher levels, and exact inspected comparison links to already catalogued randomness notions. Search failure is not treated as nonexistence.

### Primary sources inspected or anchored
- SRC-0039 (Jockusch 1980, *Degrees of Generic Sets*) was added as the foundational n-genericity provenance anchor at METADATA_ONLY. Cambridge metadata was verified, but the chapter's internal statements were not available for statement-level inspection in this bounded pass.
- SRC-0040 (Kurtz 1983, *Notions of weak genericity*) was added at ABSTRACT_INSPECTED from the Cambridge publisher extract. The extract confirms that the paper defines weakly n-generic classes for n≥1 and proves their interleaving with n-genericity, but exact syntax was not reconstructed from the unavailable full text.
- SRC-0041 (Stephan–Yu 2006) was statement-inspected from author-uploaded/indexed full text cross-checked with the NUS repository and Springer metadata. It explicitly contrasts dense Σ^0_1 classes with measure-one Σ^0_1 classes and states weakly 1-generic ⇒ Kurtz-random with non-converse.
- SRC-0042 (Kuyper–Terwijn 2014) was visually and textually statement-inspected. Definition 2.1 fixes Cantor-space 1-genericity via c.e. sets of strings dense along x; Corollary 2.3 gives the Π^0_1-boundary characterization.
- SRC-0043 (Brendle–Brooke-Taylor–Ng–Nies 2015 / arXiv:1404.2839) was visually and textually statement-inspected. §3.1 defines effective F_sigma classes and effectively meagre sets using uniformly Π^0_1 nowhere-dense components; §3.1.1 connects avoidance of all effectively meagre sets to weak 1-genericity. Its introduction explicitly says the meagre/null relationship is an analogy and that corresponding results may differ.
- SRC-0044 (Csima–Downey–Greenberg–Hirschfeldt–Miller 2006) was visually and textually inspected from an author-hosted copy matched to JSL metadata. The introduction gives exact Σ^0_n string-set formulations for n-genericity and weak n-genericity and records Kurtz's strict interleaving hierarchy.
- Existing SRC-0031 was re-inspected only far enough to confirm its separate 1-generic/weak-1-generic terminology; P1-S006 did not reopen the general oracle-relativization survey.

### Exact convention reconciliation
1. Effective meagreness is category-theoretic smallness: containment in a uniform effective F_sigma union of nowhere-dense Π^0_1 classes. It has no measure bound.
2. Weak 1-genericity meets every globally dense c.e. set of strings. 1-genericity instead meets every c.e. set dense along the given real, equivalently avoids Π^0_1 boundaries. These are not one definition with different wording.
3. Higher genericity has two interleaving hierarchies. Weakly n-generic meets every dense Σ^0_n set of strings; n-generic meets or avoids every Σ^0_n set. The inspected hierarchy is n-generic ⊋ weakly (n+1)-generic ⊋ (n+1)-generic.
4. “Weakly n-generic” and repository “weak n-random” are unrelated naming axes. DEF-0014/DEF-0015 are unchanged.
5. The only direct measure/category comparison promoted in this pass is the source-stated strict implication weakly 1-generic ⇒ Kurtz-random. No Martin-Löf/Schnorr/higher or generalized-measure edge is inferred by analogy.
6. DEF-0020's jump convention is unchanged. Although SRC-0044 discusses standard relative formulations, P1-S006 does not create a new oracle-genericity survey.

### Retrieval failures / access qualifications
- Jockusch's 1980 chapter could be verified bibliographically but not inspected internally; SRC-0039 is therefore METADATA_ONLY.
- Kurtz's 1983 paper was available through a publisher extract but not full statement text; SRC-0040 is therefore ABSTRACT_INSPECTED.
- Kurtz's 1981 thesis SRC-0025 remains METADATA_ONLY; P1-S006 did not upgrade it from citation trails.
- Direct publisher routes for some otherwise recovered papers were access-limited, so statement inspection used author-hosted/arXiv/NUS copies whose bibliographic identity was cross-checked.
- No inaccessible-original gap was filled from a secondary summary.

### Bounded exclusions
No Fairfax-Ball candidate was invented or selected; no Phase-2 research target or dedicated novelty audit was performed; no original mathematics or proof search beyond understanding published statements was performed; no Lean/Palomar work, manuscript/publication preparation or external outreach was performed.
