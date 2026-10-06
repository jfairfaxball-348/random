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


## FL-022 — The Schnorr/mixing slogan hid an atomlessness hypothesis and a generalized-space node

Session: `P1-S010`  
Status: RESOLVED CORRECTION / HYPOTHESES PRESERVED

The pre-P1-S010 THM-0006/REL-0006 summarized Gács-Hoyrup-Rojas as “Schnorr randomness iff typical for every mixing computable dynamics” without carrying the main theorem's assumption that the computable probability space has no atoms. REL-0006 also used the fair-coin Schnorr definition DEF-0003 even though the theorem is formulated for Schnorr randomness on a computable probability space.

Resolution: THM-0006 now states atomlessness, the exact T-typical and polynomial-mixing/independence resources, and the paper's separate atomic remarks. REL-0006 now starts from DEF-0034, the generalized computable-probability-space Schnorr notion.

Lesson: an abstract-level theorem slogan can suppress a structural measure hypothesis. For generalized effective dynamics, always inspect the theorem statement and attach the relation to the correct measure-space notion rather than a fair-coin specialization.

## FL-023 — Birkhoff convergence and equality to the space expectation separate in nonergodic systems

Session: `P1-S010`  
Status: RESOLVED AS THEOREM-SCOPE DISCIPLINE

V'yugin's theorem gives convergence at Martin-Löf-random points for computable measure-preserving transformations without assuming ergodicity, but only identifies the limit with E(f) when the transformation is ergodic. Franklin-Towsner explicitly distinguish weak Birkhoff points (convergence) from Birkhoff points (convergence to the integral) and use the weak notion for their nonergodic characterization.

Resolution: THM-0058, THM-0063 and THM-0064 preserve the convergence/equality split. The catalogue does not infer a global expectation value in the nonergodic setting.

Lesson: “satisfies Birkhoff's theorem” is not a sufficiently precise catalogue statement when ergodicity is absent. Record whether the conclusion is existence of a point-dependent limit or equality with the integral.

## FL-024 — Effective-ergodic publication identity and inspected-copy access diverged

Session: `P1-S010`  
Status: STATEMENTS RECOVERED WITH COPY QUALIFICATION / RESIDUAL ACCESS GAP PRESERVED / NOT A PROGRAMME BLOCKER

Franklin-Towsner's final journal identity is bibliographically clear, but its author-hosted final PDF timed out during the bounded pass. Exact promoted theorem statements therefore come from the inspected arXiv copy, whose numbering is not assumed to match the final PDF. Separately, Franklin-Greenberg-Miller-Ng (2012) was located and its abstract inspected, but a full primary copy was not obtained at statement level in this pass.

Resolution: SRC-0058 records the journal DOI separately from the inspected arXiv artefact and uses content/section pointers rather than pretending final theorem numbering was checked. No theorem record is promoted from the Franklin-Greenberg-Miller-Ng abstract.

Lesson: bibliographic publication identity, the exact copy inspected and theorem numbering are separate provenance facts. An abstract can guide retrieval but cannot fill a statement gap.


## FL-025 — Martin-Löf 1966 original recovered, but historical test syntax is not the modern shorthand

Session: `P1-S011`  
Status: ORIGINAL SOURCE RESOLVED AT STATEMENT LEVEL / FORMULATION HAZARDS PRESERVED

P1-S011 recovered a full scan of Martin-Löf's 1966 *The Definition of Random Sequences* and inspected the relevant internal statements. Publication identity and DOI were verified separately from the inspected UCI-hosted scan. The source does not literally present the now-standard one-line definition “uniformly effectively open U_n with μ(U_n)≤2^-n”: its fair-coin sequential tests are r.e. families of finite-string critical regions that are nested in significance and extension-closed, with an exact counting bound. Randomness is then finite critical level under a universal sequential test. The paper itself converts this to nested constructively open sets and proves that the nonrandoms form a maximal constructive null set.

Section IV creates a second hazard. Martin-Löf treats arbitrary computable sequential probability distributions, but his level bound uses a **strict** inequality because strict comparison of computable reals is semidecidable whereas non-strict comparison need not be. This historical construction is not silently identified with the later computable-measure/computable-probability-space machinery already recorded in DEF-0005/DEF-0033.

A third hazard is complexity notation: the 1966 finite-string critical-level theorem uses conditional plain program-size `K(x|l(x))`, not the later prefix-free/self-delimiting `K` of THM-0001.

Resolution: SRC-0001 is upgraded only to the material actually inspected; DEF-0060 and THM-0065/THM-0066 preserve the historical formulation; REL-0055 records formulation equivalence to the modern fair-coin notion with an explicit non-verbatim-syntax caution. Existing generalized-measure and prefix-free-complexity records are not overwritten.

Lesson: when normalizing a foundational definition, preserve the original representation, nesting/extension conditions, comparison effectivity and complexity convention. Mathematical equivalence does not make historical syntax interchangeable.

## FL-026 — Solovay and Schnorr original characterization provenance remains incomplete

Session: `P1-S011`  
Status: LATER PRIMARY STATEMENTS RECOVERED / ORIGINAL-PROVENANCE GAPS PRESERVED / NOT A PROGRAMME BLOCKER

The Solovay 1975 manuscript cited throughout later primary literature remains uninspected in the repository. P1-S011 therefore does not reconstruct its exact original theorem or priority details from citation trails. Instead, statement-inspected primary SRC-0059 explicitly gives the ordinary Solovay-test characterization needed here: a computable sequence of finite strings with finite/bounded Kraft sum, passed by only finitely many prefix hits. This condition is deliberately kept distinct from the computable-total-sum Schnorr convention in DEF-0017.

Schnorr's 1973 *Process Complexity and Effective Random Tests* was located at publisher/open-archive metadata level, but the direct full-text routes available in this bounded session did not provide reliable inspectable internal statements. P1-S011 therefore does not use it to settle historical process-complexity or Levin–Schnorr priority details. The prefix-free incompressibility characterization remains grounded in already statement-inspected primary Chaitin/Kučera-Slaman material, and the c.e.-martingale characterization is grounded in SRC-0059.

Lesson: an original citation target that cannot be inspected is not interchangeable with a later exact restatement. Preserve the provenance gap, and never upgrade a stronger effectivity condition (such as computable total measure) into the ordinary Solovay condition by terminology alone.

## FL-027 — Principal lowness equivalences require distinct definitions even when the classes coincide

Session: `P1-S012`  
Status: RESOLVED AT STATEMENT LEVEL / FORMULATION GUARDS PRESERVED

Before P1-S012, SRC-0009 supported the slogan “low for Martin-Löf randomness iff K-trivial” only at publisher-abstract level. The full primary paper was recovered from the author's site and matched to the published Advances in Mathematics identity. Its internal statements distinguish three notions: K-triviality by `K(A↾n)≤K(n)+O(1)`; low for Martin-Löf randomness by `MLR^A=MLR`; and low for K by the finite-string oracle inequality `K(σ)≤K^A(σ)+O(1)`. Corollary 5.3 and Theorem 6.2, together with the explicit inclusions after Definition 2.6, establish the principal coincidence package. SRC-0010 independently restates the definitions and supplies the base-for-1-randomness theorem package.

Resolution: DEF-0007, DEF-0008 and new DEF-0063 remain separate. THM-0003, THM-0069 and THM-0070 carry the exact equivalences. DEF-0009 remains an existential base definition, with THM-0004 linking bases for 1-randomness to K-triviality. No definition is rewritten as a synonym merely because the source proves class equality.

Lesson: preserve the resource and quantifier structure of lowness, complexity and base notions. A theorem-level coincidence is a relation between definitions, not permission to collapse their syntax.

## FL-028 — Kučera-Terwijn 1999 internal statements remain inaccessible in the available retrieval path

Session: `P1-S012`  
Status: ORIGINAL-PROVENANCE GAP PRESERVED / NOT A PROGRAMME BLOCKER

The foundational Kučera-Terwijn paper SRC-0021 remains abstract-inspected. The Cambridge route exposed metadata/abstract but not usable full internal text. The ILLC technical-report index advertises a full-text object, but the available retrieval route returned it as an unsupported `application/x-gzip` payload, so no internal definition/theorem statement was inspected.

Resolution: SRC-0021 remains `ABSTRACT_INSPECTED`. Exact low-for-random/K-trivial theorem syntax is grounded instead in statement-inspected primary SRC-0009 and SRC-0010. The catalogue records Kučera-Terwijn's abstract-level historical fact—existence of nonrecursive low-for-RAND sets—without reconstructing its internal proof or theorem numbering.

Lesson: an archive listing “full text” is not statement access if the actual payload cannot be inspected. Later primary restatements may support current theorem syntax, but they do not erase the original-source provenance gap.

## FL-029 — Coverage depth labels are not Gate-1 outcomes

Session: `P1-S013`  
Status: RESOLVED AUDIT-DISCIPLINE CLARIFICATION

At the P1-S012 checkpoint every coverage record was labelled `PARTIAL`, which correctly described literature depth but did not answer the Gate-1 question. `docs/GATE_POLICY.md` requires a completed coverage audit and a library fit to support discovery; it does not require every stratum to be declared exhaustive or `COMPLETE`.

Resolution: P1-S013 leaves all 19 historical `PARTIAL_...` labels intact and adds a separate per-stratum audit disposition. All 19 are judged `SUFFICIENT_FOR_GATE1_REVIEW`; 0 require gate-critical remediation. Residual source-access and depth gaps remain explicit and do not disappear merely because the library is ready to be reviewed.

Lesson: catalogue depth/provenance status and phase-gate readiness are separate dimensions. Never manufacture `COMPLETE` labels merely to satisfy a gate, and never treat `PARTIAL` as automatic gate failure when the gate policy asks for bounded discovery readiness rather than exhaustive literature closure.

## FL-030 — Coverage-plan status vocabulary lagged live record values

Session: `P1-S013`  
Status: RESOLVED STRUCTURAL CONSISTENCY CORRECTION

The P1-S013 structural audit found that `catalog/coverage-plan.json` contained live records with `PARTIAL_P1_S010`, `PARTIAL_P1_S011` and `PARTIAL_P1_S012`, but its declared `status_vocabulary` stopped at `PARTIAL_P1_S009`.

Resolution: the missing already-used values were added to the declared vocabulary. No coverage record's substantive status was changed.

Lesson: validate enumerated vocabularies against values actually used in records, not only JSON syntax and ID references. An aggregate schema can drift even when all individual records are internally coherent.


## FL-031 — Gate-1 PASS does not promote weak-access records or erase provenance gaps

Session: `P1-S014`  
Status: FORMAL REVIEW DISCIPLINE / GATE PASSED WITH RESIDUALS PRESERVED

The formal Gate-1 review confirmed that discovery readiness and source exhaustiveness are different standards. A bounded research library can pass Gate 1 while retaining explicit original-source gaps and deliberately bounded omissions, provided consequential discovery-enabling claims are adequately grounded and uncertainty is visible.

The review specifically rechecked the weak-access dependency graph. `DEF-0012` and `THM-0011` (Kolmogorov-Loveland material), `THM-0009`/`THM-0010` and `REL-0005` (constructive dimension) remain abstract-level; no exact supergale definition is present. These records are suitable navigation for Discovery but must be upgraded before any Phase-2 comparison materially relies on their exact formulation. Original Schnorr/Kurtz, Jockusch/Kurtz, Solovay/Schnorr historical, Kučera-Terwijn and other named provenance gaps likewise remain recorded rather than being relabelled by the PASS.

Lesson: a phase-gate PASS changes authorization, not evidence granularity. Never upgrade `METADATA_ONLY`/`ABSTRACT_INSPECTED` material, close a provenance gap, infer novelty, or manufacture exhaustive coverage merely because the containing phase has passed.

## FL-032 — Scaffold status surfaces lagged Gate-1 PASS

Session: `P2-S001`
Status: RESOLVED AUTHORITY-SYNCHRONIZATION CORRECTION

At the exact expected incoming checkpoint, README.md, STATUS.md and phase-1-research/README.md still described P1-S003-era Phase-1 work; authoritative/NEXT_SESSION_PROMPT.md still asked for P1-S004; phase-2-discovery/README.md said CLOSED. The later committed STATE, D-0008, gate/session ledgers, START_HERE, ROADMAP and P1-S014 review agreed on Gate-1 PASS and Phase-2 OPEN.

Resolution: the specific later gate decision controlled. P2-S001 synchronized those live navigation surfaces and linked the old Phase-2 scaffold to phase2/. Historical session and catalogue records are unchanged. This is reconciliation of stale prose, not another authorization decision.

Lesson: validate all live entry/status/handover surfaces at close, while preserving historical statements in dated records.

## FL-033 — Unrestricted structural axioms already have a maximal-class answer

Session: `P2-S001`
Status: CAND-04 REJECTED BY CATALOGUED CHARACTERIZATION

The largest fair-coin class closed under conservation and no-randomness-from-nothing for all a.e.-computable measure-preserving self-maps is already MLR by THM-0008 / REL-0008 (SRC-0015). The proposed axiomatic shape cannot justify a separate definition. The theorem is a largest-class statement, not a claim that every smaller class satisfying the axioms equals MLR.

Lesson: before retaining an intrinsic-looking definition, check the exact quantified characterization already in the map. Restricting the map class is a different question, not a rescue of the unrestricted shape. See CAND-01 and CAND-04 in phase2/P2-S001_DISCOVERY.md.

## FL-034 — More syntax did not produce more randomness classes

Session: `P2-S001`
Status: CAND-05 AND CAND-06 REJECTED BY CATALOGUED RESULTS

The neighbourhood-based n-r.e. test levels for n≥2 already collapse to difference randomness (THM-0026, SRC-0035); mutual uniformly relative computable randomness of the interleaved halves already characterizes CR (THM-0024, SRC-0032). Those exact shapes were rejected. A brief additional screen rejected merely varying the fixed constant in balanced-test change bounds, already normalized in DEF-0028 / SRC-0036 Remark 18.

Lesson: preserve these negative Discovery findings. Different syntax, more finite alternations or two-sided phrasing is not evidence of a different class. Never switch neighbourhood/string-test semantics or remove symmetry to conceal the known result.

## FL-035 — A missing catalogue arrow and a pairwise witness do not settle candidate status

Session: `P2-S001`
Status: FORMULATION RISKS PRESERVED; NO NEW THEOREM CLAIMED

CAND-02's proposed total-map/indicator quantifiers are not silently identified with every source use of computable dynamics or lower-semicomputable observables. Its next task E2 is exact formulation alignment, not a search for the missing converse. For CAND-03, THM-0025 gives an existential ordinary/uniform separation pair; it does not establish a noncomputable oracle preserving every CR sequence uniformly.

Lesson: distinguish library omissions from unresolved literature questions, and existential separation from universal lowness. Future theorem packages remain questions until authorized mathematics; novelty remains a separate Phase-3 question.

## FL-036 — Franklin–Towsner computable dynamics are not an everywhere-total map convention

Session: `P2-S002`  
Status: RESOLVED FORMULATION CORRECTION / CANDIDATE RETAINED PROVISIONALLY

The P2-S001 catalogue summary of THM-0063/THM-0064 used the phrase "computable measure-preserving transformation" without recording the exact domain convention needed by CAND-02. Local reinspection of the already-catalogued SRC-0058 shows that its finite-string representation requires the induced transformation to be defined and infinite outside a computable G_delta null set. The Section 4 converse construction explicitly ensures definition almost everywhere. This is weaker than CAND-02's deliberate requirement that T be total on every Cantor input.

Resolution: SRC-0058, THM-0063, THM-0064, REL-0052 and REL-0053 now state the a.e.-defined convention explicitly. CAND-02 is retained unchanged because the source converse witness is not established everywhere total. The lower-semicomputable theorem remains a sufficient benchmark only, and the ergodic equality-to-expectation results remain separately scoped.

Lesson: "computable transformation" is not a complete type signature. Before transferring an effective-ergodic characterization to a candidate, record whether the source map is total, partial/a.e.-defined or layerwise computable, and keep that axis separate from observable effectivity and ergodicity.



## FL-037 — Cardinal finite fibres, effective inverse data and random-preimage existence are distinct hypotheses

Session: `P2-S003`  
Status: RESOLVED AS FORMULATION DISCIPLINE / NO NEW THEOREM CLAIMED

CAND-01 uses a global set-theoretic fibre bound on an everywhere-total computable fair-coin-preserving map and explicitly assumes no effective inverse branches. The nearby catalogue records use different resources: THM-0037 gives existence of a computably random preimage under an a.e.-computable map, while THM-0038's computable-randomness invariance assumes a pair of a.e.-computable measure-preserving maps with inverse identities almost everywhere. THM-0035 similarly builds inverse data into the probability-space isomorphism notion for Martin-Löf randomness.

Resolution: E1 preserves these as distinct recorded formulations. P2-S003 does not infer an effective inverse from a finite fibre bound, does not turn existential no-randomness-from-nothing into forward conservation, and does not search for a theorem connecting the two.

Lesson: when comparing randomness under observations, track separately (i) total versus a.e.-defined maps, (ii) cardinal fibre bounds, (iii) effective inverse/branch information, and (iv) the direction of a conservation versus preimage-existence theorem.

## FL-038 — Pairwise uniform relativity does not witness universal uniform lowness

Session: `P2-S004`  
Status: RESOLVED AS FORMULATION DISCIPLINE / NO NEW LOWNESS THEOREM CLAIMED

CAND-03 has three separate quantifier layers: fix an oracle A; quantify over every unrelativized computably random X; and evaluate X against instances at A of uniform martingale families generated by a total computable map that is defined on every oracle input and whose every oracle instance is a valid martingale. An A-specific partial/total procedure is not a DEF-0025 uniform family.

The nearby recorded theorems have different quantifiers. THM-0024 is a pairwise symmetric join equivalence, and THM-0025 asserts existence of a pair A,B separating uniform from ordinary relative computable randomness. Neither theorem supplies a noncomputable A satisfying the universal preservation clause. Likewise DEF-0009 baseness is existential in a random Z above the oracle, whereas DEF-0007 lowness is universal over unrelativized random reals.

Resolution: E3 keeps CAND-03's predicate unchanged and treats SRC-0009 Theorem 5.7 only as a contrast for ordinary computable-randomness lowness. No conclusion about membership, noncomputable members, equivalence to K-triviality or collapse to computable oracles is inferred.

Lesson: in oracle-randomness comparisons, track separately (i) totality/validity of the whole family across all oracle parameters, (ii) the fixed oracle parameter, (iii) universal versus existential quantification over random inputs, and (iv) whether a theorem is pairwise, lowness-level or baseness-level before transferring a characterization.

## FL-039 — Discovery readiness is not novelty evidence or a gate decision

Session: `P2-S005`  
Status: READINESS/GATE-SEPARATION GUARD

A candidate can be precise, motivated, related to known notions, equipped with a plausible future theorem package, falsifiers and difficulty estimates, yet still have completely unassessed novelty and literature status. Gate-2 readiness asks whether the Discovery record is mature enough for a formal gate decision and subsequent dedicated prior-art attack; it does not itself establish that any candidate is new, open, nontrivial or worth naming.

Resolution: P2-S005 records **READY_FOR_FORMAL_GATE2_REVIEW** only. Candidate-level novelty/literature fields remain NOT_ASSESSED, CAND-04–CAND-06 remain rejected exactly as recorded, and no final candidate is selected. Gate 2 remains unreviewed until a separate formal review.

Lesson: keep three claims distinct in durable records: (i) a direction appears mathematically interesting enough to examine, (ii) its Discovery evidence is sufficient for gate review, and (iii) it is novel after prior-art attack. Only the first two are in scope before Phase 3, and neither entails the third.


## FL-040 — Gate-2 PASS authorizes prior-art attack, not novelty language

Session: `P2-S006`  
Status: FORMAL REVIEW DISCIPLINE / GATE PASSED WITH NOVELTY UNASSESSED

Gate 2 asks whether Discovery has produced a bounded, precise and motivated portfolio that is mature enough for a dedicated prior-art attack. It does not ask Phase 2 to settle the very novelty questions reserved for Phase 3.

Resolution: P2-S006 records **PASS** because the committed portfolio satisfies every Gate-2 minimum-evidence field and at least three retained directions are search-ready. The same review preserves their high collapse/redundancy risks, CAND-02's source-copy qualification and CAND-03's broader lowness/traceability exposure. Candidate-level novelty/literature fields remain NOT_ASSESSED; no candidate is selected.

Lesson: a Gate-2 PASS changes authorization, not epistemic status. Opening Phase 3 is permission to try to kill candidates with prior art, not evidence that they survived that attack.

## FL-041 — Totality, bounded fibres and effective inverse information remain separate prior-art axes

Session: `P3-S001`  
Status: PRIOR-ART HYPOTHESIS-DISCIPLINE GUARD

The first CAND-01 prior-art attack located two nearby but nonidentical negative preservation results. Rute's endomorphism framework permits a.e.-computable measure-preserving self-maps with no fibre bound. Bienvenu–Porter reaches everywhere-total truth-table functionals and can preserve fair-coin measure, but the inspected theorem states no finite or bounded fibre property. By contrast, the known positive invariance result THM-0038 assumes explicit effective inverse-pair data.

Resolution: do not treat "total", "finite-to-one", "bounded-to-one", "invertible" and "effectively invertible" as interchangeable. Likewise, do not turn THM-0037's reverse existential random-preimage statement into forward conservation. CAND-01's exact finite-cardinality fibre restriction remains unresolved under the inspected evidence.

Lesson: when attacking observation-map randomness claims, maintain a four-axis matrix: domain totality, cardinal fibre size, effective inverse information and implication direction. A source matching three axes does not settle the fourth, and failure to locate the fourth is not an openness proof.

## FL-042 — Effective-Birkhoff prior art requires independent totality, observable, ergodicity and conclusion axes

Session: `P3-S002`  
Status: PRIOR-ART HYPOTHESIS-DISCIPLINE GUARD

The CAND-02 prior-art attack found several sources that are very close while differing on a single decisive axis. Franklin–Towsner and Miyabe–Nies–Zhang provide nonergodic convergence-only results but allow a.e./non-total operators. Bienvenu et al. directly cover effectively-open indicators but require ergodicity and identify the limit with the expectation. Moriakov reaches total computable Cantor maps and effectively-open indicators but only within an ergodic automorphism group action with Følner averaging.

Resolution: do not treat `computable transformation` as a uniform totality convention across sources; do not replace an effectively-open indicator class by a broader lower-semicomputable class in a converse without evidence; do not drop ergodicity from equality-to-expectation results; and do not identify arbitrary one-sided self-map iterates with group-action Følner averages.

Lesson: effective-Birkhoff prior-art comparisons should track at least map totality/structure, observable effectivity, ergodicity and exact conclusion strength, with averaging scheme added when the source changes it. Matching several axes does not settle the remaining one, and failure to find an exact match is not an openness proof.



## FL-043 — Search parameterized Low-star lowness before treating a universal uniform-relative class as new

Session: `P3-S003`  
Status: PRIOR-ART TERMINOLOGY / QUANTIFIER GUARD

CAND-03 survived formulation alignment because the committed pairwise anchors did not state its universal low-oracle class. A dedicated prior-art search located a broader parameterized framework that does: SRC-0064 defines `Low^star(C,D)` using the same universal preservation pattern and a total uniform-test procedure across all oracle instances. Instantiating C=D=computable randomness, with DEF-0025 providing the exact martingale-family realization, reproduces CAND-03 at the definition level.

Resolution: retire CAND-03 as a candidate for a new named notion, while keeping the specific characterization of `Low^star(CR,CR)` unresolved under the inspected evidence. Keep ordinary `Low(CR,CR)`, pairwise uniform relativity and existential baseness separate.

Lesson: when a candidate is a universal lowness predicate, search not only its object-level randomness terminology but also **parameterized lowness schemas** such as `Low(C,D)` and `Low^star(C,D)`. Pairwise sources can fail to dispose of a candidate even though a higher-level universal schema already names it.


## FL-044 — Finite multiplicity is a significance signal, not a preservation theorem

Session: `P3-S004`  
Status: SIGNIFICANCE / TRANSFER-DISCIPLINE GUARD

Adjacent primary literature makes finite multiplicity mathematically substantive: uniformly finite-to-one endomorphisms support entropy/conjugacy structure (SRC-0065), and finite-to-one symbolic factor codes support degree/encoding and channel questions (SRC-0066). It would nevertheless be an invalid transfer to conclude that CAND-01's bare global cardinal fibre bound preserves computable randomness, supplies effective inverse branches, controls randomness deficiency, or inherits an entropy/channel theorem.

Resolution: P3-S004 records only a conditional significance judgment. CAND-01's novelty status remains unresolved, and no mathematical consequence is inferred from the adjacent literature. The future value test requires an exact theorem plus explanatory structure under CAND-01's own hypotheses.

Lesson: use adjacent structural literature to justify why a parameter is worth investigating, but never use it to smuggle in stronger hypotheses or mathematical conclusions. Keep cardinal multiplicity, effective inverse information, dynamical uniformity and quantitative information bounds separate.

## FL-045 — An unmatched conjunction of hypotheses is not yet a significance case

Context: P3-S005 assessed CAND-02 after P3-S002 had already shown that no inspected theorem matched its exact conjunction of everywhere-total maps, effectively-open indicators and nonergodic convergence-only semantics.

Lesson: a syntactically unmatched intersection can still be a technical slice. Significance requires independent mathematical motivation for the component axes **and** evidence or a future theorem showing that their interaction matters. In effective dynamics, total versus a.e./partial representation is especially dangerous: excluding a known witness class may create an apparent gap without creating a new randomness phenomenon.

Operational guard: keep three questions separate in later work. (1) Are the component notions natural? (2) Does the exact interaction change the mathematics? (3) Is the resulting predicate novel? A positive answer to (1) does not settle (2), and neither settles (3). For CAND-02, totality remains the principal structural-risk item until a theorem or decisive source addresses it.

## FL-046 — Selection readiness does not require eliminating the research risk

Session: `P3-S006`  
Status: PHASE-3 READINESS / DECISION-SEPARATION GUARD

A candidate can be ready for a selection/NO-GO decision while still carrying the central uncertainty that later mathematics would have to resolve. Demanding that Phase 3 first prove that CAND-01's finite-fibre restriction changes computable-randomness behaviour, or that CAND-02's totality restriction is not a representation artifact, would turn a readiness audit into unauthorized proof work.

Resolution: P3-S006 records **READY_FOR_SELECTION_DECISION** because the missing items are not undocumented evidence categories; they are explicit comparative research risks. CAND-01 remains provisionally substantive with no established finite-fibre randomness consequence. CAND-02 remains provisionally substantive with elevated totality/technical-slice risk. A later selection session must weigh those risks rather than pretending they are resolved.

Lesson: distinguish an **evidence gap that prevents an informed programme decision** from an **open mathematical risk that is the reason to fund or reject the next phase**. Readiness requires the former to be closed or explicit enough to decide; it does not require the latter to be mathematically settled.



## FL-047 — Candidate selection is investment prioritization, not a novelty theorem

Session: `P3-S007`  
Status: PHASE-3 SELECTION / CLAIM-DISCIPLINE GUARD

P3-S007 selected CAND-01 over CAND-02 under explicit uncertainty. The choice rests on comparative expected mathematical payoff and technical-artifact risk, not on proof that CAND-01 is open, novel, distinct or true.

Resolution: preserve PA-0001 and PA-0002 as **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. Preserve CAND-01's lack of any established computable-randomness consequence of bare finite multiplicity and CAND-02's elevated totality/representation-artifact risk. Do not use the selection label as evidence in a later novelty claim or as a substitute for the formal Gate-3 review.

Lesson: a programme may rationally choose which uncertainty to investigate without resolving that uncertainty. Selection answers “which research risk is worth reviewing/investing in next?”, not “which candidate has already been shown novel or mathematically correct?”


## FL-048 — Gate-3 PASS authorizes mathematics; it does not certify novelty

Session: P3-S008  
Status: GATE / NOVELTY-SEPARATION GUARD

Gate 3 asks whether the selected candidate has survived enough dedicated prior-art and significance scrutiny to justify mathematical investment. It does not require search absence to be converted into an openness claim, and it does not require the central Phase-4 theorem to be known in advance.

Resolution: P3-S008 records **PASS** because every Gate-3 minimum-evidence category is present and the remaining risks are explicit. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The finite-fibre axis remains provisionally substantive, but no computable-randomness consequence of the bare cardinal bound is smuggled into the gate decision.

Lesson: a gate can authorize the next kind of work without upgrading epistemic status. Phase 4 begins with a research question under explicit uncertainty, not with a certified new notion.

## FL-049 — Singleton fibres can force effective inversion, but not a class-wide inverse-use bound

Session: P4-S001
Status: PHASE-4 MATHEMATICAL BOUNDARY / NON-EXTRAPOLATION GUARD

An attempted k=1 counterexample strategy was to make an injective total computable fair-coin-preserving map whose inverse hides noncomputable information. In the exact Cantor setting this fails: total computability gives effective finite forward-use bounds; injectivity makes the compact images of same-level input cylinders disjoint; those images can therefore be effectively separated at some finite output level. Fair-coin preservation additionally forces the closed range to be all of Cantor space. The inverse is consequently computable.

What remains unbounded is the amount of output needed for inversion. Coordinate permutations can move an early input bit arbitrarily far out, so no single fixed inverse-use modulus works for the entire k=1 class.

Resolution: treat k=1 as an effective-isomorphism collapse, but do not extrapolate the separation argument to k>=2. Once fibres can contain two points, image cylinders can overlap through different preimages, and the exact effective fibre-enumeration problem must be analysed separately.

Lesson: distinguish “an inverse is computable for each valid map” from “there is a map-independent quantitative inverse bound,” and distinguish both from the genuinely multivalued inverse-branch problem that begins at k=2.

## FL-050 — Two-point fibres give effective negative information without continuous sheet selection

Session: P4-S002
Status: PHASE-4 INVERSE-INFORMATION / RANDOMNESS-TRANSFER GUARD

At k=2, total computability still makes F^{-1}([y↾m]) a uniformly computable descending clopen approximation to the fibre. What fails from k=1 is disjointness of same-level cylinder images. A concrete prefix-replacement map can have only one double fibre and nevertheless force the unique inverse off the collision point to approach two different domain limits. No global continuous selector, and hence no total computable selector or two-function fibre enumeration, can exist.

Resolution: never replace the bare cardinal condition |F^{-1}(y)|<=2 by global effective inverse branches. The forced information is a negative compact fibre name plus local recovery after an isolating prefix is known.

A second guard is equally important: failure of total branch selection is not itself failure of computable-randomness conservation. The branch-collision witness has an a.e.-computable measure-preserving inverse and therefore falls under THM-0038. Conversely, the exactly two-to-one shift preserves computable randomness by a direct martingale lift even though no single selector gives an a.e. inverse identity.

Lesson: the remaining k=2 problem is not “are total branches computable?” but whether the forced finite-fibre information always supports some weaker a.e./weighted decomposition or direct betting transfer, or whether a genuine bounded-fibre non-conservation construction exists.

## FL-051 — Bounded inverse lists are not yet effective weighted sheets

Session: P4-S003
Status: PHASE-4 k=2 WEIGHTED-TRANSFER / COUNTEREXAMPLE GUARD

The global fibre bound |F^{-1}(y)|<=2 has a stronger effective consequence than P4-S002 recorded: for every requested input precision, sufficiently much output gives a computable list of at most two candidate input prefixes. What remains missing is coherent branch identity and branch weight.

For each input cylinder [sigma], the quantities w_sigma(tau)=2^{|tau|}lambda([sigma]∩F^{-1}([tau])) form a uniformly computable bounded fair martingale. On a genuine double-fibre split these values encode the relative conditional mass of a sheet. A supplied computable clopen partition into two injective sheets makes those weights manageable and yields computable-randomness preservation, but k=2 alone does not force such a global partition: shrinking two-point fibres can defeat every continuous two-colouring.

The obvious attempt to turn SRC-0061's nonmonotonic-scan counterexample into a k=2 map also has a precise failure. Filling unqueried coordinates can reveal a coordinate before the original nonmonotonic strategy later bets on it; an ordinary output martingale cannot retroactively make that bet. Filler schedules triggered only by observed success do not satisfy the global fibre bound on all inputs.

Resolution: do not equate “at most two candidate prefixes at each precision” with “two computable persistent sheets,” and do not claim a k=2 counterexample from a scan completion until the pre-revealed-bet problem is solved globally.

Lesson: the next k=2 target is conditional weight, not cardinality. Either source computable randomness forces enough effective stabilization/positive weight for martingale transfer, or a genuine counterexample must exploit the failure while keeping every fibre globally of size at most two.

## FL-052 — Conditional-weight smallness is an effective stopping problem, not a cardinality problem

Session: P4-S004
Status: PHASE-4 k=2 CONDITIONAL-WEIGHT / STOPPING GUARD

For a source cylinder [sigma], conditioning fair coin on [sigma] and pushing it through F turns 2^{-|sigma|}/w_sigma into the likelihood-ratio supermartingale of fair coin against the conditioned pushforward. Therefore the source points whose sheet weight ever drops below epsilon form a uniformly c.e.-open set of fair-coin measure at most epsilon.

That estimate is strong enough at the Martin-Löf level but not automatically at the computable-randomness level. The forced two-prefix lists bound candidate count, yet they do not compute the hitting probability of the low-weight event. Likewise, every fixed output betting stage lifts exactly to a computable source martingale, but choosing/stopping those stages coherently requires precisely the missing hitting-time effectivity.

An asymmetric k=2 collision example confirms that the structural issue is real: one actual sheet can have weight tending to zero even though F is total, fair-coin preserving and has at most two preimages everywhere. The example does not destroy computable randomness because its thin point is computable and the map is a.e.-invertible.

Resolution: do not promote the Ville/ML estimate to a computable-randomness transfer theorem without a computable stopping measure, and do not infer positive sheet weight from the two-prefix list alone. Conversely, vanishing weight at a non-random source point is not a non-conservation witness. The next exact question is whether k=2 makes these special hitting sets Schnorr/computable-randomness null, or whether a computably random point can occupy a genuinely thin sheet.

## FL-053 — Two-prefix inverse lists do not compute stopping probabilities

Session: P4-S005
Status: PHASE-4 k=2 STOPPING-EFFECTIVITY / NON-CONSERVATION-SEPARATION GUARD

The P4-S004 crossing sets are special c.e.-open sets arising from conditional sheet-weight martingales, but their measure need not be computable even at k=2. A halting-triggered prefix-code construction gives a total computable fair-coin-preserving map with at most two preimages everywhere and, more strongly, a computable clopen partition into two injective sheets, while the measure of V_{0,1/3} encodes a c.e. noncomputable set in base 4.

The same example blocks a second natural branch-free shortcut: the finite measure obtained by integrating inverse-point counts can have noncomputable total mass. Hence neither “at most two current candidates” nor “count both inverse points symmetrically” automatically supplies computable stopping data.

Resolution: do not infer Schnorr-effectivity from the two-prefix list alone, and do not revisit the direct crossing-measure-computability route as though P4-S005 had left it open. Equally, do not infer non-conservation from noncomputable hitting probability: the example has an explicit computable clopen injective-sheet split and therefore lies in P4-S003's positive preservation regime.

Lesson: the remaining k=2 problem is about effective coherence of genuinely non-clopen/moving sheets, not merely the numerical computability of the P4-S004 crossing probability.


## FL-054 — Canonical Borel branch assignment is not computable branch control

Session: P4-S006
Status: PHASE-4 k=2 EFFECTIVE-BOREL / MOVING-SHEET GUARD

The compact collision relation admits a natural lexicographic decomposition: the nonminimum/upper source sheet is effective F-sigma, the lower sheet is effective G-delta, and the lexicographic minimum/maximum inverse selectors are effective Baire-1 pointwise limits of computable continuous approximants. This is genuine effective structure, but it is weaker than the computable sheet data used in P4-S003.

The distinction is substantive. In the P4-S005 prefix-code map, the canonical upper and lower sheet masses encode a noncomputable base-4 real, even though that same map has a different computable clopen injective-sheet split and preserves computable randomness. Thus a canonical definable sheet need not have computable mass, and a Baire-1 selector need not supply a computable stabilization modulus.

A second failure concerns the most direct moving-one-hole repair of SRC-0061. If a set of filler coordinates is encoded by one shared two-way ambiguity, later revealing any one of those coordinates to place a genuine bet identifies the ambiguity and exposes every other differing coordinate in the same cohort. Rotating to a fresh hole cannot make already exposed old coordinates unknown again.

Resolution: do not equate effective F-sigma/G-delta or Baire-1 inverse information with computable conditional measures, and do not treat a single hidden/rotating bit as a solution to the filler pre-revelation problem. Any future negative construction must allow richer finite-prefix ambiguity and delay its coalescence while still proving that complete fibres have size at most two.

Lesson: the remaining k=2 boundary has moved from canonical branch definability to **when** ambiguity coalesces. Large finite-prefix inverse trees may still collapse to two final points; whether that delayed coalescence forces a computable transfer or enables a genuine destroyer is the next exact question.

## FL-055 — Raw delayed ambiguity collapses to one binary cohort at each fixed precision

Session: P4-S007
Status: PHASE-4 k=2 DELAYED-COALESCENCE / FRESHNESS GUARD

The raw clopen inverse approximants may contain many source-prefix candidates before they die, but this does not produce arbitrarily many independent persistent ambiguities. The P4-S003 finite search can be diagonalized to a computable monotone c(n) for which the compatible n-prefixes form a coherent width-two skeleton. On a double fibre the two nodes are exactly the two true branch prefixes after their first split. On a singleton fibre there is at most one phantom, and any recurring phantom must move its disagreement farther out.

A fixed-precision finite-injury bound is therefore forced, including at most one deletion after c(n). The failed inference is to treat that as a computable stabilization time. The last allowed deletion can occur after an unbounded, noncomputably recognizable delay; a uniform persistence test would recover selector information excluded by the earlier k=2 boundary.

The same skeleton sharpens the filler problem. After c(n), every unresolved first-n coordinate is encoded by the same binary choice between two prefixes. Revealing one coordinate on which they differ chooses the entire n-prefix and therefore exposes every other differing coordinate below n. This generalizes the P4-S006 one-hole collapse beyond XOR or any particular mask representation.

Resolution: future scan-based non-conservation work must prove a **freshness invariant** relative to c(n), not merely retain many raw finite-stage candidates. It must ensure that coalescence below n does not place two still-important future betting positions into the same binary cohort. SRC-0061 currently supplies no such guarantee.

Lesson: delayed coalescence narrows the negative route rather than solving it. The remaining question is whether a globally k=2 completion can keep enough nonmonotonic bets fresh despite the computable coalescence schedule, or whether that constraint forces preservation.

## FL-056 — a persistent scan hole collapses to a computable permutation; only a moving singleton hole survives

Session: P4-S008
Status: PHASE-4 k=2 SCAN-FRESHNESS / SINGLETON-MOVING-HOLE GUARD

For a global k=2 no-repeat scan, a permanently omitted coordinate cannot support a computable-randomness counterexample. Fixing an omitted coordinate j allows a total adaptive permutation completion: query j first, follow the scan while it avoids j, and switch to exhaustive fillers if the scan ever requests j. If it never does, global k=2 forces every other coordinate to be queried. A winning output martingale therefore transfers to a k=1 permutation image, contradicting P4-S001 on a computably random source.

The failed inference is to extend this fixed-sentinel argument automatically to singleton fibres. On a singleton winning path every coordinate is eventually queried, so each fixed-sentinel completion eventually freezes. P4-S007's c(n) says that at most one low coordinate remains fresh at the sampled stage, but gives no computable deadline for when that moving hole is consumed. A weighted family of fixed sentinels has no proved success-rate compensation, while replacing consumed sentinels dynamically can pre-reveal later genuine betting coordinates.

Resolution: any future scan-based k=2 destroyer must be singleton-fibre at its winning source and must maintain an outward-moving freshness hole. Do not reuse a persistent-hole/double-fibre story, and do not claim that the fixed-sentinel family already yields one computable martingale.

Lesson: the scan problem is now narrower than P4-S007's general freshness formulation. The remaining issue is not whether one coordinate can stay hidden forever—it cannot on a winning computably random source—but whether infinitely many successively consumed holes can be managed without either a computable growth-rate assumption or pre-revelation.

## FL-057 — bounded deferred wagers are exactly hedgeable; unbounded delay means a sibling can keep the hole forever

Session: P4-S009
Status: PHASE-4 k=2 SINGLETON-MOVING-HOLE / DEFERRED-WAGER GUARD

A moving sentinel is not intrinsically costly. From a finite scan state, the continuations avoiding a proposed sentinel form a computable binary tree. If every continuation eventually consumes the sentinel, finite branching makes the tree finite and its first empty level gives a computably searchable deadline. Once that deadline is known, the future logical wager on the already-seen sentinel bit can be prepaid exactly: the finite conditional expectation of the post-consumption output-martingale capital is a computable fair martingale on the completion bits.

The failed inference is that savings/restart can therefore handle the singleton case automatically. The genuinely hard turnover is precisely one where the target eventually consumes the sentinel but some sibling continuation can omit it forever. Then no finite terminal depth is certified. Splitting capital among finite horizon guesses gives tail weights tending to zero; across infinitely many such turnovers no lower bound follows from unbounded output capital unless delay is related effectively to capital growth.

A simple k=2 singleton-spine comb confirms that infinitely many avoidable-but-consumed holes are compatible with the global fibre bound, but fixing the spine by a computable set of control bits destroys source computable randomness. Making the controls adaptive without pre-revealing future decisive bets is the unresolved construction problem.

Resolution: do not charge an automatic factor-two penalty to bounded sentinel turnovers, and do not claim that generic savings removes the unbounded stopping-value problem. Future work should analyze the capped deferred-wager value on branchwise-avoidable sentinels, or construct an adaptive singleton spine with every global check proved.

## FL-058 — a bounded cap removes integrability trouble, not noncomputable branch mass

Session: P4-S010
Status: PHASE-4 k=2 BRANCHWISE-AVOIDABLE OPTIONAL-PROJECTION GUARD

The failed inference is that once the deferred output martingale is stopped below a fixed threshold, bounded martingale convergence makes the prequeried-sentinel conditional value computable. P4-S010 gives an exact counterexample: sentinel consumption is a c.e.-open event with noncomputable measure alpha, while the bounded terminal payoff is 2b on consumption and 1 on avoidance. After revealing sentinel bit b early, the exact projected capital is 1+(2b-1)alpha.

Finite truncations are computable, but a computable convergence modulus would compute alpha. Thus boundedness supplies existence and integrability, not effective tail control.

The witness-side lesson is separate. An adaptive least-unqueried-sentinel comb can satisfy totality, fair-coin, global k=2, singleton-spine, freshness and non-pre-revelation checks. The unresolved burden is source randomness: noncomputable trigger normalization blocks the immediate source-martingale mirror but does not prove that a computably random sequence lies on an infinite correct-prediction spine.

Resolution: do not infer computable optional projection from a capital cap, and do not infer a counterexample merely from noncomputable projection values. Future work should attack the computably-random-source question for the c.e.-trigger singleton spine directly.

## FL-059 — partial autoreduction realizes the hard sibling-avoidable turnover on a computably random source

Session: P4-S011
Status: PHASE-4 k=2 EXACT NON-CONSERVATION / PARTIAL-PREDICTION BOUNDARY

The failed positive inference was that infinitely many graph-like correct-prediction triggers might automatically combine into a computable source martingale even when one-turnover normalization is noncomputable.

SRC-0067 / SRC-0068 / THM-0076 block that inference: a computably random weak-truth-table-autoreducible sequence exists. Its autoreduction predicts each target bit without reading that bit, but unlike a truth-table reduction it need not halt on every sibling oracle.

Embedding that partial predictor into the least-fresh-sentinel comb gives exactly the P4-S009/P4-S010 hard geometry. On the target each sentinel is eventually consumed and correctly predicted. On a sibling where one prediction never halts, the total scan continues forever through every other coordinate and leaves exactly that sentinel omitted. Thus fibres remain globally of size at most two without a uniform turnover deadline.

Resolution: the branchwise-avoidable case supports an exact k=2 computable-randomness destroyer. Any positive theorem for a narrower subclass must add enough totality or uniformity to exclude this partial-autoreduction mechanism.

Lesson: distinguish a predictor that halts correctly on the target from one that is total on every oracle.


## FL-060 — martingale success yields self-avoiding stakes, not automatically an error-free autoreduction

Session: P4-S012
Status: PHASE-4 k=2 PARTIAL-PREDICTOR / CONVERSE GUARD

The P4-S011 witness was stated using a computably random weak-truth-table-autoreducible source, but the scan conversion never uses the computable use bound. It only waits until the current sentinel has a finite visible computation which avoids that sentinel and is correct on the target. Even prediction at filler coordinates is unnecessary. A still weaker rational stake output suffices if the target stake capital is unbounded.

The converse has a similarly precise level. Once P4-S008 forces a winning computably random scan source to be singleton, one can simulate the scan up to coordinate j while withholding j and read off the winning martingale's signed fractional stake. This gives a self-avoiding partial stake functional total on the target and reproduces the martingale exactly in the original scan order.

The failed inference is to promote this automatically to an all-correct bit autoreduction. A fractional martingale can grow despite infinitely many wrong favoured-bit wagers; only all-in wagers are forced to be correct on a succeeding path. Moreover the induced stake functional is order-sensitive: success in the original scan order need not survive a different least-fresh ordering.

Resolution: use “partial self-betting” as the structural level justified by an arbitrary singleton winning scan. Treat all-correct partial prediction as the stronger full-wager special case exemplified by P4-S011. Do not infer a strict separation between these source properties without a separate theorem.

Lesson: the next positive boundary is not bounded use. It is enough effective sibling totality to rule out the branchwise-divergent turnover that powers P4-S011.

## FL-061 — totality is needed only where a coordinate actually becomes a sentinel

Session: P4-S013
Status: PHASE-4 k=2 SIBLING-TOTALITY / FINITE-DEADLINE GUARD

The overstrong inference is that excluding the P4-S011 mechanism requires a predictor or stake functional which halts on every oracle at every input. P4-S013 shows that the least-fresh scan never consults many such input/oracle pairs. What matters is only the pair encountered when an epoch actually withholds a coordinate as its sentinel.

At a reachable epoch, the nontriggering continuations form a computable finitely branching tree. If every compatible continuation eventually triggers, the tree has no infinite path, is finite by König compactness, and has a computably searchable empty level. Thus qualitative sibling totality automatically supplies the finite deadline needed for the P4-S009 hedge; an extra modulus is not necessary.

The boundary is sharp for this transfer architecture. Target-only halting is too weak because P4-S011 has it on the computably random winning source while a sibling can diverge forever. But full oracle-totality is too strong because a functional may diverge on a coordinate that the scan always consumes as a filler before that coordinate can ever become a sentinel.

Resolution: formulate the positive hypothesis as reachable-sentinel totality, equivalently finite avoidance trees or computably searchable finite deadlines at every reachable epoch. Under it the scan is globally exhaustive and falls back into the P4-S001 effective-isomorphism regime.

Do not promote this to a necessary characterization of all preserving k=2 least-fresh scans. Branchwise avoidance merely reopens the destruction mechanism; it does not by itself prove failure.


## FL-062 — do not approximate the infinite stopping value when a miss ticket can absorb the tail

Session: P4-S014
Status: PHASE-4 k=2 COMPUTABLY BUDGETED TAIL GUARD

The failed framing from earlier turnover attempts was that every branchwise-avoidable deferred sentinel requires a computable approximation to its eventual conditional value. P4-S010 shows that such exact bounded projections can encode noncomputable probabilities.

P4-S014 avoids that target. Fix only a finite horizon. Up to that horizon the P4-S009 finite hedge is exact. If the horizon is missed, keep copying the output martingale on fresh fillers and deliberately skip the one sentinel wager whose bit was revealed early. Restart at the next epoch.

This alone is vulnerable to infinitely many misses. The repair is orthogonal: buy a fair unit ticket for each horizon-miss event. If the exact conditional ticket prices have one finite pathwise budget, infinitely many misses themselves make the ticket martingale succeed. If misses are finite, the restarted hedge eventually tracks a fixed positive multiple of the output martingale. Their sum therefore covers both cases without computing any infinite-horizon projection.

Lesson: under effective tail control, spend computability on a finite miss-event ticket rather than on the noncomputable stopping value. The exact summability condition established here is a finite uniform pathwise budget on the conditional horizon-miss probabilities. It is strictly weaker than finite deadlines but still excludes P4-S011.

Do not infer absolute necessity: a stake-weighted loss budget may be weaker and remains for a separate session.
