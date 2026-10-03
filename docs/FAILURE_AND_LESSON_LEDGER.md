# Failure and Lesson Ledger

Every phase must preserve material dead ends, including candidate collapses, false conjectures, counterexamples, novelty failures, search strategies that miss terminology, formalisation/specification mismatches, publication-policy dead ends and corrected programme claims.

Use IDs `FL-###`. Do not delete an old failure because a later route succeeds.

## FL-001 — Foundational original-source retrieval gaps in P1-S001

Session: `P1-S001`  
Status: PARTIALLY RESOLVED IN P1-S002 / ORIGINAL-SOURCE GAP REMAINS / NOT A PROGRAMME BLOCKER

The first foundational pass did not obtain statement-level primary/original coverage for the foundational Schnorr formulation, Kurtz randomness, or Demuth's original randomness papers. Later primary papers, surveys and monographs were located, but P1-S001 deliberately did not promote uninspected originals into exact definition records.

Lesson: when an original is not available at statement level, record the gap and use the strongest actually inspected later source with its evidence level. Do not manufacture priority or theorem detail from citation trails.

P1-S002 follow-up: Schnorr's 1971 monograph/article are now anchored as SRC-0022/SRC-0023 but remain metadata-only internally; exact modern Schnorr statements are strengthened by statement-inspected primary SRC-0008, SRC-0024 and SRC-0028. Kurtz's 1981 thesis is now anchored as SRC-0025 but remains metadata-only; a source-grounded Kurtz definition and weak-n hierarchy are established from SRC-0026/SRC-0027/SRC-0029. Demuth originals were intentionally not pursued in that bounded weaker-randomness session.

P1-S004 follow-up: Demuth's 1982 original is now SRC-0034 and has been visually statement-inspected at the relevant historical definition pages. The Demuth portion of this retrieval gap is therefore closed at statement level, subject to the language/notation qualification in FL-006.

Remaining follow-up: if accessible, inspect the original Schnorr/Kurtz internal statements in a later Phase-1 retrieval pass; otherwise preserve those gaps rather than infer.

## FL-002 — Chaitin near-title metadata collision

Session: `P1-S001`  
Status: RESOLVED

Searches for *On the Length of Programs for Computing Finite Binary Sequences* surfaced both the 1966 JACM article and a distinct 1969 continuation with “Statistical considerations” and a different DOI.

Resolution: SRC-0004 was anchored to the 1966 record only after cross-checking year, volume, pages and DOI (`10.1145/321356.321363`).

Lesson: exact-title searching is insufficient when an author publishes near-identically titled sequels; verify DOI plus journal coordinates before assigning a stable source ID.

## FL-003 — Provisional stable-ID format defect

Session: `P1-S001`  
Status: RESOLVED BEFORE CLOSEOUT

The first KL-randomness definition draft used `DEF-0006A`, which violated the required `DEF-####` stable-ID convention. Referential validation also caught one lingering question-record link to that provisional ID.

Resolution: the permanent record is `DEF-0012`; source/theorem/question references were repaired and final cross-file validation passed with zero unresolved reference errors.

Lesson: run ID-pattern and referential-integrity validation before authoritative closeout, including status-question links.


## FL-004 — Schnorr test exact-measure convention ambiguity

Session: `P1-S002`  
Status: RESOLVED / CONVENTION DIFFERENCE PRESERVED

P1-S002 found that Downey–Griffiths 2002 uses `μ(U_n)≤2^-n` with computable `n↦μ(U_n)`, while later inspected primary papers use exact-measure normal forms. DEF-0003 now records computability of level measures as substantive and exact equality as a supported normalization.

Lesson: preserve source convention differences rather than presenting one normal form as the unique historical definition.


## FL-005 — van Lambalgen provenance and relativization-convention correction

Session: `P1-S003`  
Status: RESOLVED CORRECTION / RESIDUAL ACCESS GAPS PRESERVED

The incoming relative-randomness coverage note associated the uninspected central van Lambalgen theorem with SRC-0020, the 1987 paper *Von Mises' Definition of Random Sequences Reconsidered*. Citation following and statement inspection showed that the original source relevant to the central product/relative-randomness theorem is van Lambalgen's 1990 paper *The Axiomatization of Randomness* (now SRC-0033).

P1-S003 also found a second convention hazard: for Schnorr and computable randomness, ordinary oracle relativization and uniform relativization are distinct. SRC-0032 uses the uniform notions to obtain van-Lambalgen-type results and gives a separation for computable randomness; therefore the catalogue must not use "relative" and "uniformly relative" as interchangeable labels.

Resolution: SRC-0020 is retained with corrected scope; SRC-0033 preserves the original paper's actual recursive-sequential-test/product-space statements; modern fair-coin join formulations are separately supported by SRC-0030/SRC-0032; DEF-0022/DEF-0024 and DEF-0021/DEF-0025 preserve the ordinary/uniform splits.

Lesson: identify the exact cited original before assigning theorem provenance, and treat oracle-resource placement/uniformity as part of a randomness definition rather than harmless notation.


## FL-006 — Original Demuth retrieval succeeded but modern normalization is not a verbatim translation

Session: `P1-S004`  
Status: PRIMARY SOURCE RECOVERED / LANGUAGE-NOTATION QUALIFICATION PRESERVED / NOT A PROGRAMME BLOCKER

P1-S004 recovered Demuth's 1982 paper (SRC-0034) and visually inspected the pages containing the bounded-change and measure conditions. The paper is in Russian, uses historical constructive notation and formulates its classes among arithmetical reals. No independent complete English translation was located in this bounded session.

Resolution: DEF-0026 uses the clean modern all-real Cantor-space statement supported independently by statement-inspected SRC-0016 and SRC-0035, while SRC-0034 is cited for original provenance and the underlying bounded-change/measure mechanism. The repository does not claim that the modern wording is a verbatim translation of the 1982 paper.

Lesson: original-source access does not erase a translation/notation boundary. Preserve the original domain and use a later inspected primary or authoritative source to normalize terminology rather than translating technical historical notation by inference.

## FL-007 — Stronger-test terminology and passing conventions collide

Session: `P1-S004`  
Status: RESOLVED AS CATALOGUE DISCIPLINE / CONVENTION DIFFERENCES PRESERVED

Two collision hazards were found. First, SRC-0035 uses `n-r.e.` for a naive hierarchy of sets of strings that gives 2-randomness for n≥2, and then introduces a neighborhood/difference hierarchy also called n-r.e. tests whose levels n≥2 collapse to difference randomness. Second, Demuth randomness uses Solovay passing (membership in finitely many final components), whereas the balanced and Oberwolfach notions inspected here sit in a weak-Demuth framework using ordinary escape from a component.

Resolution: DEF-0027 names the neighborhood/difference semantics explicitly; taxonomy/search notes preserve the naive-string collision. DEF-0026 versus DEF-0028/DEF-0029 state their distinct passing conditions rather than forcing all moving-component tests into one normal form.

Lesson: for moving or difference tests, the object being changed, the bound on changes and the definition of passing are all part of the mathematical notion. Similar-looking test syntax is not enough to identify notions.


## FL-008 — Cantor representation is not automatically fair-coin representation

Session: `P1-S005`  
Status: RESOLVED AS SCOPE CORRECTION / HYPOTHESES PRESERVED

The generalized-space navigation wording risked collapsing two different primary results. SRC-0011/SRC-0012 show that every computable probability space admits an effective Cantor-space representation with an **appropriate computable probability measure**. SRC-0012's stronger fixed nonatomic-model theorem requires the measure to have **no atoms** and concludes that the space is a computable Lebesgue space.

Resolution: THM-0033 and REL-0032 record the arbitrary computable-measure Cantor representation without calling it fair coin; THM-0034 and REL-0033 separately record the atomless Lebesgue-space result. Non-full support is allowed in the general machinery and the source's support qualification is retained.

Lesson: “isomorphic to Cantor space” does not determine the measure. Track the source measure, target measure, atomlessness and support hypotheses explicitly before using a representation theorem as a randomness-invariance bridge.

## FL-009 — “Uniform randomness test” has two unrelated uniformity axes

Session: `P1-S005`  
Status: RESOLVED AS TERMINOLOGY DISCIPLINE

SRC-0038/SRC-0011 use **uniform test** for a test lower-semicomputable jointly in a point and a represented probability measure. P1-S003's SRC-0032 uses **uniformly relative** Schnorr/computable randomness for a single computable family selected by an oracle. These are not the same construction and neither is an alias for the other.

Resolution: DEF-0006 is rewritten as measure-parameter uniformity and taxonomy now uses `framework:measure-parameter-uniform-test`; P1-S003's `resource:uniform-relativization` remains unchanged.

Lesson: always name the parameter with respect to which uniformity is required. “Uniform” alone is not enough to identify a randomness notion or theorem.

## FL-010 — Historical Martin-Löf no-randomness-from-nothing antecedent remains provenance-incomplete

Session: `P1-S005`  
Status: MODERN PRIMARY STATEMENTS INSPECTED / EARLIEST STANDALONE PROVENANCE NOT RECOVERED / NOT A PROGRAMME BLOCKER

SRC-0015 attributes the Martin-Löf no-randomness-from-nothing result to Shen and treats the conservation/NRFN background as known. P1-S005 inspected exact modern primary statements that use these principles, including the all-computable-measure and fair-coin maximality theorems, but did not recover an earlier standalone Shen source containing the exact original theorem statement.

Resolution: the catalogue records only the exact statement-inspected modern theorems and keeps the historical attribution qualified. It does not invent a source ID or priority claim for an uninspected original.

Lesson: folklore attribution and exact theorem provenance are separate evidence questions. A later primary theorem can support the mathematical statement while an earlier-priority gap remains explicit.


## FL-011 — Category/null smallness and “weak n” terminology cannot be transferred by analogy

Session: `P1-S006`  
Status: RESOLVED AS CATALOGUE DISCIPLINE / FRAMEWORK DISTINCTION PRESERVED

P1-S006 encountered two closely named but mathematically different axes. Effective category uses effectively meagre sets built from uniformly Π^0_1 nowhere-dense components, while measure-based randomness uses null/measure-one tests. Separately, “weakly n-generic” indexes dense Σ^0_n genericity requirements, whereas the existing “weak n-random” records index measure-one arithmetical randomness classes.

Resolution: DEF-0037–DEF-0041 and the P1-S006 taxonomy guard keep these resources separate. The direct weakly-1-generic → Kurtz-random comparison is recorded only because SRC-0041 states it, and its non-converse is preserved; no other category/measure edge is inferred.

Lesson: shared words such as “weak”, “typical”, “small”, or a visual analogy between null and meagre sets do not establish a theorem. Track the ambient topology, measure (if any), definability level, density/nowhere-dense quantifiers and exact source statement before drawing a cross-framework relation.

## FL-012 — Foundational genericity originals remain partly inaccessible internally

Session: `P1-S006`  
Status: LATER PRIMARY STATEMENTS INSPECTED / ORIGINAL INTERNAL-STATEMENT GAPS PRESERVED / NOT A PROGRAMME BLOCKER

The bounded retrieval pass verified Jockusch's 1980 *Degrees of Generic Sets* bibliographically but did not obtain statement-level internal text, so SRC-0039 remains METADATA_ONLY. Kurtz's 1983 *Notions of weak genericity* was available through a publisher extract confirming scope and hierarchy, but not full statement text, so SRC-0040 remains ABSTRACT_INSPECTED. Kurtz's 1981 thesis SRC-0025 also remains METADATA_ONLY.

Resolution: exact definitions and hierarchy statements are grounded in later statement-inspected primary papers SRC-0042/SRC-0044, while SRC-0039/SRC-0040/SRC-0025 are used only for calibrated historical provenance.

Lesson: an original-source citation trail is not statement inspection. Preserve access-level gaps and use later primary statements for exact quantifiers rather than reconstructing unavailable originals from summaries.
