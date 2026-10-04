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


## FL-013 — Chaitin Ω source-access and near-title provenance guard

Session: `P1-S007`  
Status: RESOLVED AT STATEMENT LEVEL WITH REPRINT-PROVENANCE QUALIFICATION / HISTORICAL TITLE GUARD RETAINED

P1-S007 needed statement-level access to Chaitin's original self-delimiting Ω construction. Publisher/IBM metadata fixed the 1975 JACM article *A Theory of Program Size Formally Identical to Information Theory* (DOI `10.1145/321892.321894`), while full statement inspection was obtained from the article as reprinted in Chaitin's collected papers. The catalogue records both facts rather than presenting the reprint route as the publisher copy.

The earlier FL-002 collision remains controlling: SRC-0004 is the 1966 *On the Length of Programs for Computing Finite Binary Sequences* (DOI `10.1145/321356.321363`), and the 1969 “Statistical Considerations” continuation is a different work. P1-S007 does not duplicate or merge either with the 1975 source.

Lesson: for Chaitin's tightly related early titles, identify the work by year, journal coordinates and DOI before promoting internal statements; when statement inspection uses a reprint, record that provenance explicitly.

## FL-014 — r.e.-real / left-c.e.-real and Ω universality convention hazard

Session: `P1-S007`  
Status: RESOLVED CONVENTION / SOLOVAY ORIGINAL ACCESS GAP PRESERVED

The inspected 2001 primary sources use “recursively enumerable real” for a real approximable from below by a computable nondecreasing rational sequence. Modern literature commonly calls the same notion “left-c.e. real.” A second hazard is more serious: every left-c.e. real in (0,1] can be a halting probability of some prefix-free machine, but only the Martin-Löf-random left-c.e. reals are halting probabilities of universal prefix-free machines (Chaitin Ω-numbers).

Resolution: DEF-0042 records the historical/modern terminology equivalence; DEF-0043 and DEF-0044 separate arbitrary prefix-free halting probability from universal-machine Ω; THM-0047 and THM-0048 record the two different equivalences. Binary-expansion conventions are recorded separately in DEF-0045.

The Solovay manuscript cited by the primary papers was not independently statement-inspected in this bounded pass. Its detailed claims are not reconstructed from secondary citation trails.

Lesson: never infer randomness from left-c.e.-ness alone, never drop universality from an Ω-randomness theorem, and never move between a real and a binary sequence without preserving the source's representation convention.

## FL-015 — Computational-pseudorandomness originals required mixed publisher/author-hosted access routes

Session: `P1-S008`  
Status: STATEMENTS RECOVERED WITH PROVENANCE QUALIFICATIONS / NOT A PROGRAMME BLOCKER

The bounded COV-0016 pass found that bibliographic landing pages and full statement access did not coincide uniformly. Yao 1982 was statement-inspected from an accessible proceedings scan after DOI/title/page verification because the IEEE route was access-limited. Håstad–Impagliazzo–Levin–Luby 1999 was statement-inspected from Håstad's author-hosted journal paper after SIAM metadata/abstract cross-checking. Nisan–Wigderson journal metadata/abstract were available, while the inspected internal statements came from the authors' corresponding 1988 FOCS extended abstract.

Resolution: `SRC-0048`–`SRC-0050` say exactly which artefact was inspected. No access level is upgraded on the strength of a publisher abstract alone, and no journal theorem numbering is reconstructed from a preliminary version.

Lesson: source identity, bibliographic publication status and the copy actually statement-inspected are distinct provenance fields. Record all three when publisher access is incomplete.

## FL-016 — “Pseudorandom sequence” names different object types across foundational sources

Session: `P1-S008`  
Status: RESOLVED AS OBJECT/RESOURCE DISCIPLINE

Yao/HILL computational pseudorandomness compares probability ensembles on finite strings with bounded statistical distinguishers; a PRG induces such an ensemble from a uniformly sampled finite seed. Lutz 1992, by contrast, explicitly uses “pseudorandom sequences” for Δ-random **individual infinite binary sequences** defined through resource-bounded measure/martingales. His polynomial-time specialization retains the exact `p=p1` resource convention.

Resolution: `DEF-0046`/`DEF-0047` and `DEF-0048`/`DEF-0049` are separate records with separate object domains. `THM-0050` records only the inspected Δ-random/martingale equivalence. No implication to or from Martin-Löf, Schnorr or computable randomness is inferred for p-randomness, and a fixed PRG output is not relabelled algorithmically random.

Lesson: the word “pseudorandom” is not a stable mathematical type signature. Before normalizing terminology, identify whether the object is a distribution ensemble, finite generator output, language/characteristic sequence, or individual infinite sequence, and retain the resource bound on the observer/test/strategy.

## FL-017 — Authoritative entry-point session pointer lagged committed state

Session: `P1-S008`  
Status: RESOLVED AUTHORITY-SYNCHRONIZATION CORRECTION

At the incoming checkpoint, `authoritative/STATE.json` and `authoritative/SESSION_LEDGER.md` correctly recorded P1-S007 as the latest completed session, but `authoritative/START_HERE.md` still named P1-S006 and omitted P1-S007 from its completed-session sentence.

Resolution: P1-S008 treated the more specific committed state/ledger plus the verified incoming hash as controlling, did not widen authorization, and synchronized `START_HERE.md` during closeout. Phase 1 remained OPEN and Phases 2–5 remained CLOSED throughout.

Lesson: entry-point prose can lag machine-readable/session-ledger state even within an otherwise consistent checkpoint. Pin `main`, reconcile the specific mismatch, and correct the entry point rather than using stale prose to roll back completed work.


## FL-018 — Higher-randomness terminology does not have one stable label

Session: `P1-S009`  
Status: RESOLVED AS CATALOGUE TERMINOLOGY DISCIPLINE

The primary higher-randomness sources use labels that collide across eras and levels. Hjorth–Nies locally call their Π1^1 version of Martin-Löf randomness simply “ML-random”, while the same paper reports that Sacks used “Σ1^1-random” for what Hjorth–Nies define as avoidance of null Π1^1 classes. Chong–Nies–Yu separately distinguish Π1^1-Martin-Löf randomness from Π1^1-randomness and prove a strict separation.

Resolution: `DEF-0052` is explicitly named Π1^1-Martin-Löf randomness / higher ML-randomness; `DEF-0053` is Π1^1-randomness. Sacks's “Σ1^1-random” is retained only as historical provenance. Ordinary Martin-Löf randomness remains `DEF-0002`.

Lesson: in higher randomness, pointclass symbols and the words “ML-random” or “random” are not interchangeable labels. Preserve the source's test/null-class resource before normalizing terminology.

## FL-019 — Higher computability is not ordinary oracle relativization carried to a transfinite index

Session: `P1-S009`  
Status: RESOLVED AS RESOURCE/RELATIVIZATION DISCIPLINE

The incoming finite convention `DEF-0020` defines n-randomness for finite n≥1 by Martin-Löf randomness relative to `∅^(n−1)`. The inspected higher sources instead use lightface Δ1^1/Π1^1 definability and, for continuous higher relativization, Π1^1 functionals and enumeration functionals. Bienvenu–Greenberg–Monin explicitly explain that a classical uniform universal oracle-test construction fails in the higher setting.

Resolution: `DEF-0020` is unchanged. New higher records `DEF-0050`–`DEF-0055` state their own resources, and `SRC-0054` is cited wherever continuous higher relativization matters.

Lesson: a visual analogy between the finite arithmetical hierarchy and the higher/projective notation is not a definition or theorem. Do not manufacture a transfinite n-random hierarchy or replace continuous higher reducibility by ordinary Turing-oracle relativization.

## FL-020 — Higher primary-source access required explicit copy/title provenance

Session: `P1-S009`  
Status: STATEMENTS RECOVERED WITH PROVENANCE QUALIFICATIONS / NOT A PROGRAMME BLOCKER

The existing Monin 2020 chapter `SRC-0017` remained inaccessible at statement level and therefore stayed ABSTRACT_INSPECTED. Chong–Nies–Yu's journal publication and accessible author preprint have different titles; Hjorth–Nies statement inspection used an author-hosted copy after publisher metadata cross-checking.

Resolution: exact definitions/theorems are grounded in `SRC-0052`–`SRC-0055`, with the actually inspected copy and title variation recorded. `SRC-0017` is retained only as the navigation anchor it was before P1-S009.

Lesson: publication metadata, the copy actually inspected, and historical provenance are separate evidence fields. Do not upgrade an inaccessible navigation source because a later paper discusses the same notion.

## FL-021 — Aggregate catalogue summary lagged P1-S008 records

Session: `P1-S009`  
Status: RESOLVED MAINTENANCE CORRECTION

At the incoming P1-S008 checkpoint, the underlying catalogue files, authoritative state and session ledger had P1-S008 counts and COV-0016=`PARTIAL_P1_S008`, but `catalog/catalogue.json` still had `last_completed_session: P1-S007` and a P1-S007-era coverage summary calling the pseudorandomness/resource-bounded boundary not started.

Resolution: P1-S009 treats the detailed committed records and authoritative state as controlling and synchronizes the aggregate catalogue metadata while adding the higher-randomness records. Authorization was unaffected.

Lesson: aggregate index prose can lag its underlying stable-ID files. Validate aggregate session pointers and coverage summaries as part of every catalogue closeout.
