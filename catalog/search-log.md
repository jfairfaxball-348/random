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


## P1-S007 — 2026-10-03

Scope: primary-source consolidation of COV-0015, restricted to finite-string versus infinite-sequence incompressibility, left-c.e. (historical r.e.) reals, prefix-free/self-delimiting halting probabilities, Chaitin Ω-numbers, binary-real representation conventions, and exact links to already catalogued Martin-Löf randomness/prefix-free complexity. Search failure is not treated as nonexistence.

### Primary sources inspected or added
- SRC-0045: Chaitin, *A Theory of Program Size Formally Identical to Information Theory* (JACM 22(3), 1975, 329-340; DOI 10.1145/321892.321894). IBM/DOI metadata was cross-checked; statement inspection used the article reprinted in Chaitin's collected papers. Theorem 4.2 and the following definition/remark ground the finite-string versus infinite-string complexity distinction; the base-two-representation definition, halting-probability definition and Theorem 4.3 ground the original Ω construction used here.
- SRC-0046: Calude–Hertling–Khoussainov–Wang, *Recursively Enumerable Reals and Chaitin Ω Numbers* (TCS 255, 2001, 125-149; DOI 10.1016/S0304-3975(99)00159-0). Publisher metadata plus a coauthor-hosted publisher-version PDF were statement-inspected. Theorem 4.1 gives exact one-sided rational-approximation/lower-cut/prefix-free-code characterizations; Theorem 3.4 gives randomness of universal-machine Ω; Theorems 6.5-6.6 and the published added note record the Ω-like/Ω and random-r.e./Ω conclusions.
- SRC-0047: Kučera–Slaman, *Randomness and Recursive Enumerability* (SIAM J. Comput. 31(1), 2001, 199-211; DOI 10.1137/S0097539799357441). SIAM metadata plus the author-hosted full paper were statement-inspected. Definitions 1.1/1.4/1.6/1.8/1.10/1.12 and Theorems 1.9/1.11/1.15/2.1 provide the exact object, self-delimiting, Ω, r.e.-real and random-r.e.-real characterization chain.

### Exact convention reconciliation
1. `Σ*` / finite binary strings, `Σ^ω` / infinite binary sequences, and real numbers represented by binary expansions are kept as distinct domains. SRC-0047 explicitly calls its Martin-Löf tests “sequential” tests on infinite sequences to distinguish them from tests on finite strings.
2. Prefix-free complexity `K(σ)` remains a finite-string quantity. The infinite-sequence incompressibility characterization is the quantified condition over every prefix `X↾n` in THM-0001. Chaitin's 1975 finite-string discussion is not promoted to a new infinite-sequence notion.
3. “Recursively enumerable real” in the 2001 papers is normalized to the modern alias “left-c.e. real”: a computable nondecreasing rational approximation from below. Left-c.e. by itself is not randomness.
4. Every left-c.e. real in (0,1] is the halting probability of some prefix-free/self-delimiting machine (THM-0047). The machine need not be universal.
5. A Chaitin Ω-number is the halting probability of a universal self-delimiting/prefix-free machine. Every such Ω is left-c.e. and Martin-Löf random (THM-0046).
6. The exact converse is preserved: Martin-Löf-random left-c.e. reals are exactly the Ω-numbers (THM-0048). No arbitrary left-c.e. real is identified with this subclass.
7. Binary-expansion ambiguity is explicit. Chaitin 1975 selects the expansion with infinitely many 1s; the later sources note uniqueness for irrational reals. Since Ω is random, it is irrational, so Ω itself has no dyadic ambiguity.
8. DEF-0020's jump convention is unchanged. P1-S007 does not reopen relative Ω, generalized measures, stronger tests or effective category.

### Retrieval failures / provenance qualifications
- Direct publisher routes did not provide all historical Chaitin statement text in this pass. SRC-0045 is therefore statement-inspected through Chaitin's collected-paper reprint after bibliographic cross-checking, and that provenance is recorded rather than silently treating a reprint route as the publisher copy.
- FL-002 remains controlling for the Chaitin near-title collision: SRC-0004 is the 1966 JACM paper; the 1969 “Statistical Considerations” continuation is a distinct work. Neither is conflated with SRC-0045 (1975).
- Solovay's unpublished draft, repeatedly cited by the 2001 primary papers, was not independently recovered at statement level. No exact theorem record is created from citation trails alone.
- The historical term “r.e. real” is not silently rewritten in source quotations/provenance; catalogue records state the modern left-c.e. normalization explicitly.

### Bounded exclusions
No Fairfax-Ball candidate was invented or selected; no Phase-2 target selection or dedicated novelty audit was performed; no original mathematics or proof search beyond understanding published statements was performed; no Lean/Palomar work, manuscript/publication preparation or external outreach was performed.

## P1-S008 — Pseudorandomness / resource-bounded / derandomization boundary

Date: 2026-10-04

Bounded objective: consolidate COV-0016 only deeply enough to prevent conflation of unbounded individual algorithmic randomness, finite-string distributional pseudorandomness, resource-bounded individual-sequence randomness, and algorithmic derandomization. No general cryptography/complexity survey was attempted.

### Primary-source searches and inspections

- **Yao 1982, _Theory and Applications of Trapdoor Functions_.** DOI/proceedings metadata were cross-checked and an accessible scan of the actual FOCS paper was inspected. The printed p. 84 passage explicitly separates “what is a random sequence?” (a property of a single sequence) from pseudorandom number generation. Definitions 10–14 give the source-ensemble / polynomial-statistical-test setup, and Theorem 3 gives the paper's perfect-source iff every-polynomial-test characterization. Promoted as `SRC-0048`, supporting `DEF-0046`, `DEF-0047`, and `THM-0049`.
- **Håstad–Impagliazzo–Levin–Luby 1999, _A Pseudorandom Generator from any One-way Function_.** SIAM bibliographic metadata/abstract were cross-checked; Håstad's author-hosted full paper was statement-inspected. Definitions 2.3.7–2.3.8 fix probability ensembles/P-samplability; Definitions 3.3.1–3.3.3 fix bounded-adversary computational indistinguishability and the P-time stretching PRG definition. Promoted as `SRC-0049`, supporting `DEF-0046`, `DEF-0047`, and `REL-0042`.
- **Nisan–Wigderson 1994, _Hardness vs. Randomness_.** JCSS metadata/abstract were checked. The authors' 1988 FOCS extended abstract corresponding to the later journal paper was inspected at the abstract/introduction: a short truly random seed is stretched into a longer string intended to fool algorithms from a stated complexity class, and deterministic simulation is described by trying all seeds. Promoted as `SRC-0050` only for the minimal derandomization boundary; exact journal theorem numbering was not reconstructed from the preliminary version.
- **Lutz 1992, _Almost Everywhere High Nonuniform Complexity_.** ScienceDirect metadata/abstract and the author-hosted full journal PDF were inspected. Paper pp. 8–9 define `p_i` resource classes and `p=p1`, with `G1` polynomially bounded; Definition 3.18 defines martingale success; Definition 6.1 defines Δ-tests/Δ-randomness; Theorem 6.2 gives Δ-random iff no Δ-computable martingale succeeds. Promoted as `SRC-0051`, supporting `DEF-0048`, `DEF-0049`, `THM-0050`, and `REL-0043`.

### Boundary distinctions fixed

- Yao/HILL computational pseudorandomness is **distributional**: indexed finite-string distributions/ensembles are compared by computationally bounded observers.
- A PRG's output randomness is the distribution induced by a uniformly random finite seed; no individual output string is thereby catalogued as Martin-Löf/Schnorr/computably random.
- Lutz Δ-randomness is an **individual infinite-sequence** property whose tests/martingales are resource bounded. For p-randomness the `p` resource is retained explicitly.
- Complexity-theoretic languages enter the resource-bounded framework through characteristic sequences; this representation is not the same object as a PRG output ensemble.
- Derandomization is recorded only as the algorithm-simulation problem supported by pseudorandom generators/hardness assumptions; it is not an additional infinite-sequence randomness predicate.
- No cross-hierarchy implication between p-randomness and the existing unbounded randomness notions was promoted.

### Retrieval failures / formulation hazards

- The IEEE landing route for Yao's original was access-limited; statement inspection therefore used an accessible proceedings scan after DOI/title/page cross-checking. No publisher-only internal claim was inferred.
- The SIAM landing page for HILL exposes metadata/abstract but not the full internal text in this environment; the exact definitions were inspected in the author-hosted journal paper matched to the SIAM record.
- For Nisan–Wigderson, the exact journal article metadata and abstract were available, while statement inspection used the authors' FOCS extended abstract. The catalogue does not claim journal theorem-number inspection.
- **Terminology collision:** Lutz calls time/space-bounded Δ-random individual infinite sequences “pseudorandom sequences,” while Yao/HILL pseudorandomness is an ensemble/generator notion. The collision is recorded rather than normalized.
- **Historical terminology warning:** Lutz's discussion of `rec`-randomness uses historical Schnorr/weak-randomness terminology. P1-S008 did not promote a fresh edge into the repository's modern weaker-randomness hierarchy from that prose; only the Δ-martingale theorem needed for COV-0016 was recorded.

### Deliberate exclusions

No cryptographic primitive survey beyond the PRG definition; no one-way-function catalogue expansion; no resource-bounded dimension survey; no hardness-amplification survey; no extractor/sampler survey; no BPP landscape audit; no transfer from generalized measure, genericity, Ω/left-c.e. or oracle randomness; no Fairfax-Ball candidate definition/selection; no novelty audit; no original mathematics; no formalization/manuscript/outreach work.

Result: `COV-0016` becomes `PARTIAL_P1_S008`. Boundary depth is sufficient for this bounded session, but the stratum is not marked complete and Gate 1 is unchanged.


## P1-S009 — Higher randomness and higher computability

Date: 2026-10-04

Bounded objective: consolidate COV-0011 at primary-source statement level, restricted to the principal Δ1^1/Π1^1 notions, their exact test/definability resources, the minimum higher weak-2/difference hierarchy needed to locate them, and higher-computability distinctions necessary to prevent false ordinary-relativization analogies.

### Primary sources inspected or added

- **SRC-0052 — Chong, Nies, Yu (2008), _Lowness of Higher Randomness Notions_.** Journal/DOI metadata were cross-checked against the authors' full preprint, whose title is _Higher Randomness Notions and Their Lowness Properties_. Section 3 was statement-inspected. Definition 3.1 separates Γ-randomness from Γ-Martin-Löf randomness; Lemma 3.2/Theorem 3.3 give Δ1^1-random = Δ1^1-ML-random; Theorem 3.4 gives a largest null Π1^1 set; Theorem 3.12 supplies the strict Π1^1-random → Π1^1-ML-random → Δ1^1-random = Δ1^1-ML-random subchain used here. The theorem's stronger Δ1^1(O)-random leading edge was deliberately not promoted because P1-S009 does not reopen a general oracle-higher-randomness survey.
- **SRC-0053 — Hjorth–Nies (2007), _Randomness via effective descriptive set theory_.** Publisher metadata were matched to the author-hosted full paper. Section 3.4 was inspected for the Π1^1 version of Martin-Löf tests; Theorem 5.2 and Definition 5.3 were inspected for the largest null Π1^1 class and Π1^1-randomness. The source-local unqualified “ML-random” label and its note that Sacks used “Σ1^1-random” for the null-Π1^1-class notion are recorded as terminology provenance rather than normalized away.
- **SRC-0054 — Bienvenu–Greenberg–Monin (2017), _Continuous higher randomness_.** DOI/arXiv metadata and the authors' full journal-version PDF were inspected. Definitions 1.1/1.3 fix continuous higher Turing/enumeration resources; Theorem 1.7 gives the higher-difference/Kleene-O characterization; Section 5 defines higher weak 2-tests and separates Π1^1-randomness from higher weak 2-randomness; the later hierarchy discussion locates higher weak 2 above higher difference randomness.
- **SRC-0055 — Greenberg–Monin (2017), _Higher randomness and genericity_.** Cambridge's open journal PDF was inspected only for its higher-randomness material. Theorem 2.1 supplies the Π1^1-random = Δ1^1-random + Church-Kleene-ordinal-preservation characterization; Section 5 identifies higher weak 2-randomness with Π^ck_2-randomness and places it strictly between Δ1^1-randomness and Π1^1-randomness.

### Exact convention reconciliation

1. The object domain in the promoted records remains an individual real / infinite binary sequence in Cantor space. No finite-string PRG or resource-bounded object from P1-S008 is imported.
2. Δ1^1-randomness is null-Δ1^1-class avoidance; Δ1^1-Martin-Löf randomness is test-based. They are identified only because the inspected theorem proves equivalence.
3. Π1^1-Martin-Löf randomness and Π1^1-randomness are distinct. The inspected chain is strict: Π1^1-random → Π1^1-ML-random → Δ1^1-random = Δ1^1-ML-random.
4. Hjorth–Nies's source-local “ML-random” means the higher Π1^1-ML notion in that section, not ordinary Martin-Löf randomness. Their note on Sacks's “Σ1^1-random” names the null-Π1^1-class notion now catalogued as Π1^1-randomness.
5. Higher weak 2-randomness is a higher Π^ck_2/null-higher-Π^0_2 notion and is not ordinary weak 2-randomness DEF-0015. The source-stated placement Π1^1-random > higher weak 2 > Δ1^1-random is recorded without extrapolating the finite weak-n hierarchy.
6. Higher difference randomness is recorded only from SRC-0054's continuous-higher test/reducibility formulation. No lower difference-randomness definition or implication from P1-S004 is transferred by analogy.
7. DEF-0020 is unchanged: repository n-randomness remains finite jump-relativized Martin-Löf randomness relative to ∅^(n−1).
8. SRC-0054 explicitly shows why ordinary-looking oracle constructions can fail higher up, including failure of a uniform universal higher oracle test. Continuous higher relativization is therefore treated as a separate resource, not a synonym for ordinary Turing-oracle relativization.

### Retrieval failures / provenance qualifications

- SRC-0017 (Monin's 2020 Cambridge chapter) remains ABSTRACT_INSPECTED/navigation-only as a source record because full statement-level chapter text was not obtained in this session. No definition or theorem was promoted from it.
- SRC-0052 has a publication-title/preprint-title variation. The journal identity was fixed by DOI/volume/pages before statement inspection of the author-hosted preprint; the two titles are recorded as one source, not duplicated.
- SRC-0053 statement inspection used an author-hosted full paper after publisher metadata cross-checking. The catalogue does not imply that publisher full text was directly inspected.
- The earliest Martin-Löf/Sacks higher formulations were not independently recovered at statement level. Their historical labels are recorded only where the later inspected primary sources explicitly report them; unavailable wording is not reconstructed from secondary summaries.

### Bounded exclusions

No general admissible-set/descriptive-set-theory survey; no transfinite-recursion survey; no general higher-lowness programme; no broad higher-stronger-test hierarchy; no finite-level implication imported without an inspected higher theorem; no generalized-measure/category/Ω/resource-bounded transfer; no Fairfax-Ball candidate invention or selection; no Phase-2 target selection; no novelty audit; no original mathematics or proof search beyond understanding published statements; no Lean/Palomar; no manuscript/publication preparation; no outreach.

Result: COV-0011 becomes `PARTIAL_P1_S009`. It is no longer the catalogue's sole navigation-only stratum, but it is not marked complete and Gate 1 remains unchanged.


## P1-S010 — 2026-10-04

Scope: bounded primary-source consolidation of COV-0014, limited to effective/computable measure-preserving dynamics, exact effective Birkhoff/typicality theorems, direct randomness links, necessary recurrence, and minimal shift/frequency orientation. This was not a general ergodic-theory, dynamical-systems, computable-analysis or probability survey.

### Primary sources inspected / re-inspected

- SRC-0012 (Gács-Hoyrup-Rojas): re-inspected the full primary text around T-typicality, correlation functions, polynomial mixing/independence, Theorem 3.3.1 and the atomic remark. This corrected the previous catalogue's missing **no-atoms** hypothesis and its fair-coin relation node.
- SRC-0056 (V. V. V'yugin): SIAM publication identity/DOI was cross-checked; a full author-uploaded English translation was inspected at Theorem 2 and the surrounding computable-measure/transformation setup. The theorem was recorded as convergence for general computable measure-preserving T, with equality to expectation only in the ergodic case.
- SRC-0057 (Bienvenu-Day-Hoyrup-Mezhirov-Shen): publisher metadata plus arXiv v2/full primary text were inspected for effective recurrence, effective Birkhoff statements for effectively open/closed sets and lower semicomputable observables, μ-layerwise computability, and the explicit computable-probability-space extension.
- SRC-0058 (Franklin-Towsner): MathNet/journal identity and DOI were cross-checked; the arXiv primary copy was inspected for Definition 1.4, the non-Martin-Löf-random converse construction, the positive computable-observable convergence theorem and the weak-2/lower-semicomputable convergence result.

### Exact convention / hypothesis reconciliation

1. The main Gács-Hoyrup-Rojas Schnorr/mixing theorem assumes the computable probability space is **atomless**. Atomic mixing/ergodic cases are separate source remarks.
2. Generalized Schnorr randomness is DEF-0034, not fair-coin DEF-0003, in that theorem.
3. V'yugin works on binary-sequence Cantor space with an arbitrary computable probability measure; fair coin is not assumed.
4. In nonergodic systems, convergence of Birkhoff averages does not imply the limit equals the space expectation. Franklin-Towsner's weak-Birkhoff/Birkhoff distinction and V'yugin's ergodic clause are recorded separately.
5. Bienvenu et al.'s general-space extension uses computable probability spaces and μ-layerwise computable, measure-preserving, ergodic maps. This is neither ordinary oracle relativization nor an arbitrary represented-space theorem.
6. Franklin-Towsner's inspected nonergodic converse and weak-2 results remain fair-coin Cantor-space statements.

### Retrieval failures / provenance qualifications

- The final author-hosted Franklin-Towsner PDF timed out during retrieval. The publication identity is verified independently, but exact promoted statements/theorem pointers use the inspected arXiv copy; final theorem numbering is not asserted.
- Franklin-Greenberg-Miller-Ng, _Martin-Löf random points satisfy Birkhoff's ergodic theorem for effectively closed sets_ (Proc. AMS 140(10), 2012; DOI 10.1090/S0002-9939-2012-11179-7), was located at publisher/JSTOR abstract level, but a full primary copy was not statement-inspected in this pass. Its detailed theorem is therefore not promoted into the stable theorem graph.
- No unavailable statement was filled from a textbook, survey, abstract or citation summary.

### Bounded exclusions

No Fairfax-Ball candidate was invented or selected; no Phase-2 target was selected; no dedicated novelty audit; no original mathematics or proof search beyond understanding published statements; no general recurrence/mixing/dynamical-systems survey; no Lean/Palomar; no manuscript/publication work; no outreach.


## P1-S011 — 2026-10-04

Scope: bounded primary-source consolidation of COV-0003 only — Martin-Löf's original effective-test formulation, universal tests, exact ordinary Solovay and c.e.-martingale characterizations, and the minimum incompressibility cross-check needed to keep the foundational record coherent. This was not a general algorithmic-information, martingale, computability or historical survey.

### Primary sources inspected / re-inspected

- **SRC-0001 — Martin-Löf 1966, _The Definition of Random Sequences_.** ScienceDirect metadata/DOI fixed the publication identity; statement inspection used a full UCI-hosted scan. Section III, printed pp. 609-612, was inspected for the fair-coin sequential-test definition, effective enumeration of all tests, universal-test theorem, finite critical-level randomness definition, constructively open levels and maximal constructive-null-set reformulation. Section IV, printed pp. 612-614, was inspected for arbitrary computable sequential probability distributions and the strict level inequality.
- **SRC-0059 — Barmpalias and Lewis-Pye, _Computing halting probabilities from other halting probabilities_.** Published identity was cross-checked as Theoretical Computer Science 660 (2017), 16-22, DOI `10.1016/j.tcs.2016.11.013`; exact statements were inspected in arXiv:`1602.06395v2`, §2 pp. 3-4. The source explicitly states the ordinary Solovay-test characterization and the c.e.-martingale characterization with the needed effectivity and passing/success conventions.
- **SRC-0045 / SRC-0047** remain the already statement-inspected primary anchors for the self-delimiting/prefix-free incompressibility characterization and its finite/infinite object guard. They were used only to reconcile the COV-0003 complexity edge; no broader Ω tranche was reopened.

### Exact formulation reconciliation

1. Martin-Löf's original fair-coin sequential tests are not written in the modern one-line open-set syntax. The source uses an r.e. `U⊆N×2^{<ω}`, significance-level nesting, extension closure, and the counting bound corresponding to fair-coin measure `≤2^-m`.
2. The universal-test theorem is a level-shift domination theorem: for every sequential test `V`, `V_{m+c}⊆U_m` for all `m≥1`, with `c` depending on the test.
3. Original infinite randomness is finite critical level for a universal sequential test. The paper itself converts the universal levels to nested constructively open sets and proves that the nonrandom class is maximal among constructive null sets.
4. In the original arbitrary-computable-distribution section, the level bound is strict `<2^-m`. The source explicitly explains this by the semidecidability of strict comparison for computable reals. This historical convention was not imported into P1-S005's modern generalized-measure records.
5. Ordinary Solovay tests in SRC-0059 require a computable string sequence with a finite/bounded Kraft sum and are passed by finitely many prefix hits. **No computability of the total sum is required.** That condition is therefore not the total-Solovay/Schnorr convention DEF-0017.
6. The martingale characterization uses c.e./uniformly lower-semicomputable martingale values and success by capital tending to infinity. It is not the computable-martingale resource used for computable randomness.
7. The existing prefix-free `K(X↾n)≥n-O(1)` characterization remains distinct from Martin-Löf 1966's conditional plain-complexity finite-string formula. No plain/prefix-free notation collapse was made.

### Retrieval failures / provenance qualifications

- **Solovay 1975 draft:** still not independently statement-inspected. SRC-0059 explicitly attributes the ordinary Solovay characterization to Solovay, but P1-S011 does not reconstruct original theorem wording, numbering or priority from that citation.
- **Schnorr 1973, _Process Complexity and Effective Random Tests_:** publisher/open-archive metadata and abstract were located, but available direct full-text retrieval was not reliable enough for statement promotion in this bounded pass. No internal theorem was filled from the abstract or an aggregator.
- The original Martin-Löf publication identity and the copy actually inspected are different provenance facts: the DOI/publisher record establishes the article; the UCI-hosted scan supplied internal statements. The catalogue records both.
- No unavailable statement was filled from a textbook, survey, secondary summary or abstract.

### Bounded exclusions

No Schnorr/computable/Kurtz tranche was reopened; no ordinary/uniform oracle relativization; no stronger-test hierarchy; no generalized-measure rewrite; no category, Ω/left-c.e., pseudorandomness, higher-randomness or effective-ergodic expansion beyond direct cross-links already present. No Fairfax-Ball candidate invention/selection, no Phase-2 target selection, no novelty audit, no original mathematics/proof search, no Lean/Palomar, no manuscript/publication work, and no outreach.

## P1-S012 — Lowness notions and bases for randomness

Date: 2026-10-04

Scope: bounded primary-source consolidation of COV-0009, restricted to the principal low-for-Martin-Löf / K-trivial / low-for-K coincidence and the base-for-1-randomness characterization. No general traceability, cost-function, degree, jump or oracle-randomness survey was opened.

### Primary sources inspected / re-inspected

- **SRC-0009 — Nies (2005), _Lowness properties and randomness_.** Publisher/DOI metadata fixed the publication identity; statement inspection used the full author-hosted article matched to the published paper. Definition 2.1 gives K-triviality as `K(A↾n)≤K(n)+b` for all n. Definition 2.5 gives low for random as `MLR^A=MLR`. Definition 2.6 gives low for K by `K(y)≤K^A(y)+O(1)` for every finite string y. The paper immediately records low-for-K ⇒ low-for-MLR and low-for-K ⇒ K-trivial; Corollary 5.3 gives low-for-MLR ⇒ low-for-K; Theorem 6.2 gives K-trivial ⇒ low-for-K. Theorem 5.7 (low for computable randomness implies computable) was inspected only as a bounded contrast and was not used to open a separate lowness hierarchy.
- **SRC-0010 — Hirschfeldt, Nies, Stephan (2007), _Using random sets as oracles_.** The author-hosted full paper was re-inspected against journal metadata. Definition 1.2 gives the exact base-for-R definition: B is a base if some Z≥_T B is R-random relative to B. Definition 1.8 gives K-triviality. The surrounding text fixes low-for-R and low-for-K. Section 2/Theorem 2.1 supplies base-for-1-random ⇒ K-trivial, with the section/introduction recording the converse package; Corollary 3.1 gives low-for-1-random ⇒ K-trivial.
- **SRC-0021 — Kučera, Terwijn (1999), _Lowness for the class of random sets_.** Upgrade attempt failed. Cambridge exposed abstract/metadata only in the available route. The ILLC report index advertised full text, but the linked object was returned as unsupported `application/x-gzip`; internal statements were therefore not promoted.

### Exact formulation reconciliation

1. Low for Martin-Löf randomness quantifies over **all unrelativized Martin-Löf random reals** and requires each to remain random relative to oracle A; in SRC-0009 this is `MLR^A=MLR`, using the ordinary oracle-relative notion DEF-0019.
2. K-triviality quantifies over **all initial-segment lengths n** and compares prefix-free complexity of A's initial segment with prefix-free complexity of n using one additive constant.
3. Low for K quantifies over **all finite strings σ** and compares `K^A(σ)` with `K(σ)` up to one additive constant. This is a finite-string oracle-complexity resource, not an infinite-sequence randomness predicate.
4. Base for R-randomness is existential: **some** R-random-relative-to-B real Z computes B. It is not the universal preservation condition defining low for R.
5. The equivalences low-MLR ↔ low-K ↔ K-trivial and base-for-1-random ↔ K-trivial are promoted only because inspected primary statements support them.
6. P1-S003's ordinary/uniform relativization distinction is unchanged; no Schnorr/computable uniform-relative convention is imported.
7. No downward/upward Turing-degree closure is inferred. Nies contains degree/traceability consequences, but they are outside this bounded structural pass.

### Retrieval/provenance and scope hazards

- Publication identity and inspected copy are recorded separately for SRC-0009/SRC-0010.
- SRC-0021 remains abstract-only despite an archive full-text listing because its payload could not be inspected.
- Cost functions, traceability and jump characterizations were not promoted merely because they are adjacent to K-triviality in the literature.
- No status-sensitive question arose.
- No Phase-2 candidate, novelty audit or original mathematics was introduced.

Result: `COV-0009` becomes `PARTIAL_P1_S012`. All 19 coverage strata are now partial, but none is complete and Gate 1 remains not ready for review. The next recommended session is a bounded Phase-1 completion/source-gap audit.

## P1-S013 — 2026-10-04 — Gate-1 completion/source-gap audit

Scope: repository-wide Phase-1 audit against the Gate-1 minimum evidence. This session did not run another broad subject survey and did not treat a missing original source as automatically blocking.

### Audit method

- Compared all 19 committed coverage records with their required depth, dependencies, source-access limitations and the gate policy.
- Checked source-access levels catalogue-wide: 42 `STATEMENT_INSPECTED`, 11 `ABSTRACT_INSPECTED`, 6 `METADATA_ONLY`.
- Checked whether definition/theorem records relied only on weak access. The remaining notable weak-evidence records are explicit: `DEF-0012` (KL randomness) is abstract-inspected; `THM-0009` and `THM-0010` (constructive dimension) are abstract-inspected; `THM-0011` (KL dense-subsequence result) is abstract-inspected.
- Verified that these weak-evidence records do not silently settle a Gate-1 transition, an equivalence, a converse, priority, or openness claim beyond their documented source granularity.
- Reassessed the named residual provenance gaps from P1-S012 against whether exact current catalogue claims depend on them.

### Residual-gap disposition

No gate-critical source gap remains. Original Schnorr/Kurtz internals, Jockusch/Kurtz originals, the Demuth translation qualification, earliest standalone ML-NRFN provenance, selected Chaitin originals, the Solovay draft, Schnorr 1973, historical higher-randomness originals, Franklin-Greenberg-Miller-Ng and Kučera-Terwijn 1999 are retained as nonblocking provenance/history gaps because current exact theorem/definition syntax is either supported elsewhere or no theorem is promoted from the inaccessible source.

COV-0016's omitted resource-bounded dimension material is accepted as a deliberately bounded omission: P1-S008's purpose was to establish the object/resource boundary, not to survey complexity theory.

Constructive dimension and KL material remain explicit weak-evidence cautions. If Phase 2 develops a candidate or comparison that materially turns on exact supergale, dimension, or KL strategy syntax, those records must be upgraded before being used as decisive mathematical evidence.

### Retrieval decision

No external primary-source retrieval was performed in P1-S013 because the audit found no gate-critical gap that a small retrieval would need to settle. Launching source searches merely to reduce every provenance gap would have violated the bounded audit objective.

### Structural validation finding

`coverage-plan.json` used `PARTIAL_P1_S010`, `PARTIAL_P1_S011` and `PARTIAL_P1_S012` in records while omitting them from `status_vocabulary`. P1-S013 corrected this declared-vocabulary drift without changing substantive coverage statuses.

## P3-S001 — 2026-10-04 — CAND-01 primary-source prior-art attack

Scope: one bounded Phase-3 prior-art attack on CAND-01 only. Exact target: forward preservation of fair-coin computable randomness under everywhere-total computable fair-coin-preserving Cantor self-maps with a fixed global cardinal bound |F^{-1}(y)|<=k for every y, with no effective inverse branches, selectors or fibre enumerations assumed.

### Primary sources located / inspected

- **SRC-0060 — Rute, _Computable randomness and betting for computable probability spaces_ (2016).** Statement-inspected at the a.e.-computable morphism definition, Definition 10.1, Proposition 10.2, Theorem 10.4 and Corollary 10.7. This introduces **endomorphism randomness**: preservation of computable randomness under every a.e.-computable measure-preserving self-morphism. Computable randomness is not preserved by that unrestricted endomorphism class.
- **SRC-0061 — Bienvenu and Porter, _Strong reductions in effective randomness_ (2012).** Statement-inspected at Definition 2.4 and Theorem 4.2. A truth-table functional is total in the paper's convention; Theorem 4.2 gives a total functional that can induce fair-coin measure yet destroy computable randomness. The theorem states no finite or bounded fibre property.
- Existing **SRC-0015 / THM-0037 / THM-0038** were retained as direction/inverse guards: THM-0037 is reverse-direction existence of a computably random preimage; THM-0038 gives forward invariance only with an explicit a.e.-computable inverse pair.

### Alternate terminology / formulation queries

Search vocabulary included: `endomorphism randomness`, `endomorphism random`, `stable computable randomness`, `truth-table functional computable randomness`, `total Turing functional computable randomness`, `finite-to-one computable randomness`, `finite fibre computable randomness`, `bounded-to-one computable randomness`, `k-to-one computable randomness`, `n-to-one computable randomness`, `finite-to-one endomorphism algorithmic randomness`, `uniformly p-to-one endomorphism`, and `finite-to-one factor computable randomness`.

Classical ergodic/symbolic-dynamics literature uses terms such as **uniformly p-to-one endomorphism**, **finite-to-one factor** and **bounded-to-one**. The located examples concern measure-theoretic conjugacy, entropy or factor structure, not preservation of computable randomness. They are navigation vocabulary, not an exact prior-art match.

### Hypothesis reconciliation

1. **Everywhere totality is not the live novelty discriminator by itself.** SRC-0061 already gives a total truth-table functional inducing fair-coin measure that can destroy computable randomness.
2. **Unrestricted endomorphism preservation is already a named prior-art framework.** SRC-0060's endomorphism randomness is structurally broader than CAND-01 because it quantifies over a.e.-computable measure-preserving endomorphisms without a finite-fibre restriction.
3. **The global cardinal fibre bound remains unmatched in the inspected primary evidence.** Neither SRC-0060 nor SRC-0061 states `|F^{-1}(y)|<=k` or supplies an equivalent bounded-multiplicity hypothesis.
4. **Cardinal fibres are not effective inverse data.** No selector, fibre enumeration or inverse branch is imported. THM-0038 remains stronger on inverse information.
5. **Direction matters.** THM-0037 is no-randomness-from-nothing (random output -> existence of a random preimage), not the forward conservation required by CAND-01.

### P3-S001 disposition

**UNRESOLVED_UNDER_INSPECTED_EVIDENCE.** CAND-01 is not shown already known, equivalent/rebranded, or materially distinct by this bounded search. It has substantial framework overlap with known endomorphism randomness, and total fair-coin-preserving maps are already known not to conserve computable randomness in general. The exact globally bounded finite-fibre restriction remains the live point not matched by the inspected primary sources.

This is not an openness claim and not novelty evidence from absence. No theorem about finite-to-one preservation or failure is inferred or proved.
