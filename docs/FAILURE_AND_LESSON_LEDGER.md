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


## FL-063 — a horizon miss should be priced by the positive skipped gain, but its optimal future price may be noncomputable

Session: P4-S015
Status: PHASE-4 k=2 STAKE-WEIGHTED TAIL GUARD

P4-S014 deliberately charged one unit for every finite-horizon miss. That was enough for a clean theorem, but it can be grossly pessimistic when the deferred sentinel wager is small, losing, or never occurs.

P4-S015 identifies the exact local damage to the restart hedge: if a missed epoch later triggers and the prequeried sentinel wager would multiply output capital by g, skipping it only hurts when g>1, by positive multiplicative loss g-1. A finite leaf ticket can therefore be priced by a computable majorant of this positive gain rather than by unit miss mass.

This matters quantitatively. A two-control-bit least-fresh scan can retain a permanent avoiding sibling of probability 1/4 at every epoch, so no choice of finite horizons has a summable raw miss budget. Yet if sentinel j carries stake 2^{-(j+1)}, the leafwise fair weighted prices sum to at most 1/4.

The new trap is effectivity. The pointwise smallest future-loss envelope asks whether and with what stake a currently missed partial computation will ever halt. A c.e. noncomputable trigger family makes that exact optimum encode a noncomputable set. Do not silently treat the optimal stake-weighted envelope as computable.

Resolution: require a computable rational future-loss envelope, or stronger data that computes one. Under a finite pathwise budget on its fair ticket prices, weighted tickets plus the P4-S014 restart hedge transfer success. P4-S011 remains outside the positive regime because every target sentinel wager is all-in and correct, so each missed-then-triggered positive loss is exactly one.

Next lesson target: test whether advance envelopes can be replaced by incremental tickets bought only when larger postmiss stakes become finitely visible, without computing an infinite optional projection.


## FL-064 — do not replace a noncomputable future supremum by another advance approximation when a fresh last-chance bit remains

Session: P4-S016
Date: 2026-10-06

The P4-S015 pointwise minimal future skipped-loss envelope can encode noncomputable information, so trying to approximate that supremum more cleverly is the wrong local target.

After a horizon miss, the sentinel-first completion still has fresh filler bits. At each unresolved state, before the next filler is drawn, both next-child logical states are computable. The exact skipped-sentinel loss is therefore computable on any child that triggers immediately. Buying the corresponding one-step ticket at that moment removes the need to know any farther future supremum.

The remaining difficulty is quantitative rather than limit-computational: a single finite initial bankroll can fund all last-chance tickets only under an effective admissibility condition. P4-S016 uses a finite uniform pathwise sum bound on their exact fair premiums. The next refinement should attack that bankroll condition, not return to the noncomputable future envelope.

Guard: this is a lesson about the P4-S016 least-fresh transfer architecture only, not an impossibility result for other computable martingale transfers.

## FL-065 — solvency is not success: self-financed insurance needs a coercive surplus condition

Session: P4-S017
Date: 2026-10-06
Status: PHASE-4 k=2 SELF-FINANCING RESERVE GUARD

The tempting weakening of P4-S016 is to require only that earlier ticket winnings keep the insurance account from going bankrupt. That is not enough. No-overdraft makes the canonical full-ticket account a total nonnegative computable martingale, but says nothing about growth.

A certain-payout ticket exposes the failure: if both next filler children trigger the same positive skipped loss ell, the exact fair premium is ell and the ticket pays ell surely. The same reserve can be recycled forever. Along a path with harmonic skipped gains, realized loss diverges but insurance capital stays constant, while the restart hedge can lose reciprocal factors and remain bounded.

Resolution: the needed condition is **coercivity**, not merely solvency. The full-ticket account must be unbounded whenever cumulative realized positive skipped gain diverges. Finite realized loss is handled by the restart hedge. A computable unbounded reserve floor g(E) is a stronger easy certificate, but is not claimed necessary.

P4-S011 excludes every coercive certificate; bare admissibility alone is not ruled out.

Guard: this is a boundary for the P4-S016/P4-S017 ticket-plus-restart architecture, not an impossibility theorem for every computable transfer.

## FL-066 — semantic branchwise coercivity does not give a uniform loss-to-capital modulus

Session: P4-S018
Date: 2026-10-06
Status: PHASE-4 k=2 EFFECTIVE-COERCIVITY / CROSS-BRANCH GUARD

The tempting inference from P4-S017 is that if every individual completion run with divergent realized skipped loss makes the self-financing ticket account unbounded, compactness should yield a computable retained-surplus floor. That inference fails before computability enters.

For a capital target K, let B_K be the tree of finite ticket histories whose running maximum capital is still below K. Semantic coercivity only says that every infinite branch through B_K has bounded cumulative realized loss E. It does not say that E is uniformly bounded over all finite nodes of B_K.

A computable mode switch between the two settled P4-S017 gadgets makes the distinction exact. One mode is genuinely coercive on every E-divergent run. The other permits a unary-selected finite burst of certain-payout tickets: price equals payout, so capital stays 1 while the harmonic cumulative payout can be made arbitrarily large, after which positive tickets stop. Every individual burst branch still has finite E.

Resolution: use a computable running-maximum threshold h(K) only as a stronger sufficient certificate. The exact set-theoretic extra condition for a uniform threshold is loss-properness b(K)=sup{E(v):W*(v)<K}<infinity. Whether finite b(K) must be computably bounded is a separate question.

P4-S011 remains outside every effective-modulus regime. Bare no-overdraft is still not ruled out there.

Guard: this is a boundary inside the P4-S016/P4-S017 ticket-plus-restart architecture, not an impossibility theorem for arbitrary transfer martingales.

## FL-067 — finite bad-capital loss height is not an effective loss bar

Session: P4-S019
Date: 2026-10-06
Status: PHASE-4 k=2 LOSS-PROPERNESS EFFECTIVITY GUARD

P4-S018 isolated loss-properness b(K)<infinity as the exact set-theoretic condition restoring a uniform loss threshold at each fixed capital target. The tempting next inference is that a computable ticket tree should let one search for those finite bounds. That inference is false.

A computable controller can hide the halting time of machine e behind a finite ticket-capital ladder. After the ladder, zero-stake epochs wait for the machine. If it halts after t steps, a deterministic finite ticket burst records t in cumulative realized skipped loss without increasing ticket capital. For each fixed K only finitely many e remain below K, so b(K) is finite; but a computable majorant of b would bound every halting time and decide the halting problem.

The general lesson is that computability of finite histories gives lower semicomputable approximations to b(K), not effective upper bounds. Finiteness of a lower-semicomputable quantity is not a modulus.

Resolution: when the P4-S018 quantitative transfer is needed, require effective loss-properness — a computable bad-capital loss bound U(K) — or structural data from which such a bound can actually be searched. Do not silently turn set-theoretic loss-properness into an effective certificate.

P4-S011 is outside even the set-theoretic loss-proper regime whenever its full-ticket account is globally admissible. Bare admissibility remains unruled-out.

Guard: this is a boundary inside the P4-S016/P4-S017 full-ticket plus restart architecture, not an impossibility theorem for arbitrary martingale transfers.

## FL-068 — bounding the next positive loss is too coarse; control the reachable loss scale

Session: P4-S020
Date: 2026-10-06
Status: PHASE-4 k=2 LOSS-SCALE SEARCHABILITY GUARD

P4-S019 hid halting-time information behind arbitrarily long zero-loss waiting, suggesting that a computable waiting bound might repair effectivity. That diagnosis is too coarse.

The same obstruction survives after inserting summably small deterministic heartbeat losses. A branch which will later realize more positive skipped gain can be forced to realize some positive gain again within a fixed computable number of controller epochs, yet the total heartbeat contribution on a nonhalting branch remains bounded. A late halt still unlocks a finite effectively divergent burst, so a computable majorant of b(K) would still decide halting.

Lesson: event frequency does not control accumulated loss scale. The useful structural datum is a computable bound on where a **specified loss level** must first have a witness if it is reachable. Such a loss-level witness modulus makes the global loss-bar predicate searchable; with loss-properness it computes U(K).

Do not silently replace a loss-level reachability problem by a next-event waiting bound, especially when positive increments may shrink summably.

The searchable-loss-level condition remains weaker than branchwise amount-sensitive progress and is compatible with divergent absolute premium sums. P4-S011 fails before this boundary because global admissibility plus loss-properness is already impossible there.

Guard: this is a boundary inside the P4-S016/P4-S017 full-ticket plus restart architecture, not an impossibility theorem for arbitrary martingale transfers.


## FL-069 — effective loss mass does not decide boundary attainment

Session: P4-S021
Date: 2026-10-06
Status: PHASE-4 k=2 ANTI-ZENO / LOSS-BOUNDARY GUARD

P4-S020 isolated loss-scale reachability after next-positive-loss waiting proved too coarse. P4-S021 shows that a strong repair still has two logically different consequences.

If losses at a fixed positive scale have computably bounded local waiting and the total contribution below that scale has a computable bound, then set-theoretic loss-properness can be effectivized. One does not need exact loss-bar searchability for that conclusion.

But even global deadlines for every fixed scale plus an effectively vanishing small-loss tail do not decide whether an exact loss level is reached. A computable geometric tail can approach a rational boundary forever if a machine diverges and pay the remaining residual at once if the machine halts. Thus finite attainment versus limit approach can carry halting information while all bad-capital loss heights already have a computable majorant.

Resolution: distinguish **effective control of total loss mass** from **effective isolation of a queried boundary**. Do not silently upgrade a computable tail estimate into a P4-S020 witness modulus. Any next exact-Reach theorem needs an anti-Zeno / boundary-isolation ingredient or an equivalent finite-attainment certificate.

P4-S011 lies outside even the scale-tail regime under global admissibility: its divergent loss has an unbounded tail below every fixed positive scale.

Guard: this is a boundary inside the settled P4-S016/P4-S017 full-ticket plus restart architecture, not a general impossibility theorem for arbitrary martingale transfers.

## FL-070 — a vanishing tail bound is not a boundary gap; exact search needs strict separation

Session: P4-S022
Date: 2026-10-06
Status: PHASE-4 k=2 STRICT-BOUNDARY / ANTI-ZENO GUARD

P4-S021 already gives extremely strong control in its negative example: every fixed positive loss scale dies out by a computable deadline, the remaining small-loss tail tends effectively to zero, and total bad-capital loss has a computable bound. The tempting inference is that this should make exact integer loss levels decidable.

The missing detail is the sign of the residual gap. At an exhausted scale, a computable tail cap Q proves nonreachability only when (E+Q<m). In the P4-S021 nonhalting machine tail, the sharp computable remainder satisfies (E+Q=m) at every finite stage. If the machine halts, that same residual is paid by one finite correction. Equality therefore carries the halting bit.

Resolution: for exact Reach search, require or derive a **strict** residual-gap certificate on every genuinely unreachable boundary. Positive crossing witnesses need no extra certificate because they are already c.e. Once all false boundaries have searchable strict gaps, Reach is decidable and P4-S020's witness modulus can be recovered.

Guard: do not call such a condition strictly weaker than D in effective consequence. It is only a different, more local source of the same exact searchability. The next question is whether semantic exclusion of nonattaining boundary-Zeno paths plus effective compactness forces the strict gap automatically.

P4-S011 remains outside the scale-tail regime under global admissibility.


## FL-071 — incompatible near-boundary branches cannot beat compactness under a uniform vanishing tail

Session: P4-S023
Date: 2026-10-06
Status: PHASE-4 k=2 SEMANTIC ANTI-ZENO / EFFECTIVE-COMPACTNESS GUARD

P4-S022 left open a possible escape: every individual bad-capital branch might be non-Zeno while different incompatible branches come arbitrarily close to the same integer boundary, preventing a uniform strict gap.

That escape fails under the strong P4-S021 tail form. Global fixed-scale exhaustion and an effectively vanishing uniform subscale bound make cumulative loss uniformly Cauchy on compact branch space. Near-boundary nodes at finer frontiers therefore have a diagonal limit branch which inherits the boundary value.

Resolution: under strong uniform tail convergence, semantic anti-Zeno is enough. A false Reach instance must eventually expose a strict P4-S022 frontier certificate, so exact Reach is decidable and P4-S020's witness modulus follows.

Guard: the proof uses **uniform** effective tail convergence. P4-S023 does not show that pointwise or merely branchwise convergence suffices. P4-S011 remains outside the strong tail regime under global admissibility.

## FL-072 — pointwise effective convergence does not survive incompatible-branch limits

Session: P4-S024
Date: 2026-10-06
Status: PHASE-4 k=2 POINTWISE-TAIL / EFFECTIVE-TOPOLOGY GUARD

P4-S023 used uniform vanishing tails to transfer near-boundary loss from incompatible finite nodes to a compact diagonal limit branch. It is tempting to replace that by the statement that every individual bad-capital branch has an effective convergence modulus.

That is false if the moduli are genuinely nonuniform. P4-S024 builds a computable globally k=2 admissible comb in which every branch has only finitely many positive losses, so every branch is eventually constant and has some computable modulus. Yet later incompatible teeth end arbitrarily close to the queried integer boundary while their all-continue Cantor-limit spine stays a fixed distance below it. The branch-limit loss is discontinuous, and exact Reach still codes halting.

Resolution: distinguish **pointwise existence of computable moduli** from **one oracle-uniform branch-modulus functional**. The latter compactifies effectively to a global uniform modulus on the pruned bad-capital tree; the former does not.

Guard: semantic anti-Zeno is branchwise and does not by itself control discontinuity across branches. The next useful hypothesis should target effective upper-semicontinuity or an equivalent computable local tail-cap basis, not merely restate pointwise convergence. P4-S011 remains outside even the weak pointwise-tail regime under global admissibility.

## FL-073 — continuity is not an effective frontier certificate

Session: P4-S025
Date: 2026-10-06
Status: PHASE-4 k=2 EFFECTIVE-UPPER-SEMICONTINUITY / COMPACTNESS GUARD

P4-S024 isolated discontinuity of the branch-limit loss as the failure of genuinely nonuniform pointwise tails. It is tempting to conclude that restoring continuity should make semantic anti-Zeno computationally sufficient.

That inference is false. P4-S025's delayed-activation comb keeps the branch-limit loss continuous: on a nonhalting selected-e comb, tooth losses converge to the all-continue spine; if a halt is detected, every still-surviving branch receives the same finite correction. Every branch is eventually loss-constant and non-Zeno. Yet exact Reach still codes halting.

The missing datum is effective upper information. A complete c.e. local upper-cap basis is much stronger than semantic continuity: on the computable pruned bad-capital tree it compactifies to a computable global uniform tail modulus. Thus full effective upper-semicontinuity collapses back to the P4-S023 regime.

Resolution: distinguish ordinary continuity/usc from an effective upper-cap representation. Do not treat a set-theoretic compactness gap as searchable without effective upper neighborhoods. Boundary-specific effective caps are useful only when they supply the already-needed positive certificate for Bar(K,m).

P4-S011 remains outside even the finite branch-limit regime under global admissibility.

Guard: this is a boundary inside the settled k=2 ticket/restart architecture, not a necessity theorem for arbitrary martingale transfers.

## FL-074 — boundary-only effectivity may be weaker as data, but completeness is already the negative Reach search

Session: P4-S026
Date: 2026-10-06
Status: PHASE-4 k=2 ONE-SIDED-BOUNDARY / SEARCHABILITY GUARD

P4-S025 left a narrow apparent gap between full effective upper-semicontinuity and explicit searchable Bar. That gap is real only at the level of representation. Integer-boundary caps can exist without a complete rational upper-cap basis: a constant noncomputable left-c.e. loss below 1 has a trivial effective cap for every integer boundary but cannot admit arbitrary effective rational upper approximation.

The tempting mistake is to infer a new intermediate searchability notion from that representation weakening. If sound local exclusion certificates are c.e. and complete for every branch strictly below a queried integer boundary, then on a true Bar instance semantic anti-Zeno makes those cylinders cover the whole computable pruned bad-capital branch space. Effective compactness finds a finite subcover. This positively semidecides Bar; together with the already-c.e. positive Reach witnesses it decides Reach and recovers P4-S020's witness modulus.

Resolution: distinguish **weaker certificate language** from **weaker final effective consequence**. Any c.e. all-boundary-complete local-cap language is already the missing negative Reach search in topological form.

To remain strictly below P4-S020, a future boundary notion must give up either effective enumeration of sound local certificates or completeness for every false queried boundary; then it no longer yields searchable Bar by itself.

P4-S011 remains unchanged. Its divergent bad-capital branch is outside the full finite-limit regime, but it does not refute the weaker boundary-only notion because that branch reaches every integer boundary.

Guard: this is a searchability boundary inside the settled k=2 ticket/restart architecture, not a general necessity theorem for arbitrary martingale transfers.

## FL-075 — divergent premiums do not imply unbounded reserve demand

Session: P4-S027
Date: 2026-10-06
Status: **DURABLE LESSON**

Failed inference to avoid: from P4-S016's proof that every computable horizon has divergent last-chance premium sum on the P4-S011 target, infer that no finite reserve can buy all full tickets globally.

Why it fails: total expenditure and reserve demand are different when ticket payouts can be recycled. After globally clipping the P4-S011 wtt witness to its computable use frontier and choosing a horizon which exhausts that frontier, every positive postmiss ticket is deterministic. Its two child losses are equal, so its exact fair premium equals its certain payout. A unit reserve can therefore be spent and restored indefinitely even though the cumulative premium sum diverges.

Correct guard: to refute bare self-financing admissibility one needs a family of branches producing **net premium deficit before replenishment**, not merely infinitely many or divergent fair prices. In particular, future trigger dependence on genuinely unrevealed filler bits is the relevant source of one-sided ticket risk.

This lesson does not weaken P4-S016's absolute-budget theorem or P4-S017's coercivity theorem. It distinguishes absolute expenditure, solvency and success of the ticket martingale.


## FL-076 — no finite frontier is not yet a reserve lower bound; persistent one-sided deficit is

Session: P4-S028
Date: 2026-10-06
Status: **DURABLE LESSON**

P4-S027 showed that finite dependency exhaustion kills one-sided ticket risk: once later trigger data no longer depend on future filler values, both ticket children have the same skipped gain and a finite reserve can be recycled forever.

The converse inference must not be made automatically. The absence of a finite dependency frontier only says that arbitrarily late filler values can still matter. By itself it does not quantify the size or cumulative drawdown of the resulting one-sided tickets.

P4-S028's negative witness adds exactly the missing quantitative feature. In the first-1-search epoch, with stored sentinel bit 1, every unresolved post-horizon filler has loss vector (0,1). The fair premium is always 1/2. Following the 0-child repeatedly loses that premium and leaves the same one-sided opportunity available again, with no intervening payout. Hence the net deficit grows linearly and defeats every finite reserve.

Correct guard: to prove bare insolvency, exhibit unbounded **net premium deficit before replenishment**, not merely infinitely many value-sensitive future dependencies. Future no-frontier examples with effectively decaying skipped gains may still be globally solvent and must be analyzed separately.

P4-S011 is not affected: its P4-S027 frontier makes post-horizon tickets deterministic even though cumulative premiums diverge.


## FL-077 — no-frontier dependence is a geometry, not a bankroll lower bound

Session: P4-S029
Date: 2026-10-06

The failed inference is: “if an epoch has no finite dependency frontier and keeps arbitrarily late one-sided trigger opportunities, then a finite canonical full-ticket reserve must fail.”

P4-S029 refutes that inference using the exact P4-S028 first-1-search scan. The scan geometry is unchanged and still has no finite initial frontier, but scaling the possible skipped gain at first-1 depth n to (2^{-n}) changes the ticket from ((0,1)) to ((0,2^{-n})). The zero-payout sibling then pays only the summable premiums (2^{-(n+1)}), whose total is 1/4.

The durable lesson is to separate **dependency depth** from **exposure mass**. A finite frontier makes positive tickets deterministic and therefore recyclable, but genuinely unbounded value-sensitive dependence can also be solvent when the unreplenished premium deficit is bounded. In the fixed first-1-search family the exact boundary is summability of the one-sided premium tail.

This does not weaken any P4-S015 through P4-S028 transfer theorem and does not affect the P4-S011 destroyer.


## FL-078 — divergent one-sided premiums are compatible with solvency when renewal is paid for

Session: P4-S030
Date: 2026-10-06
Status: **DURABLE LESSON**

The tempting inference after P4-S029 is that divergent cumulative premiums must force a deterministic frontier before a finite reserve can survive. P4-S030 refutes that inference.

The relevant quantity is still purchase-time deficit, not gross expenditure. A genuinely one-sided ticket may renew the same no-frontier risk regime if its realized payout more than restores the premium just spent. P4-S030 arranges exactly that on the continuing branch: the early ticket costs a_r/2, pays a_r, and moves to the next active epoch. Repeating these wins yields a divergent harmonic premium sum while the reserve grows.

The global guard is on the losing or unreplenished siblings. Every active epoch has arbitrarily late one-sided opportunities, but once the first early ticket loses, the remaining late-ticket premium tail is summable; a late trigger or unfavorable sentinel terminalizes future positive ticket cost. Hence no completion can concatenate infinitely many unpaid bad tails.

Correct obstruction: if some completion has unbounded cumulative premium minus prior payouts — in particular a zero-payout continuation with divergent remaining premium mass — then no finite reserve is possible. P4-S028 has exactly that obstruction. P4-S030 avoids it without making tickets deterministic and without restoring P4-S016 absolute premium summability.

This does not alter any transfer theorem or the P4-S011 destroyer.

## FL-079 — terminalization is only the zero-budget endpoint of a renewal reserve potential

Session: P4-S031
Date: 2026-10-06
Status: **DURABLE LESSON**

The tempting inference after P4-S030 is that once a branch has traversed an unreplenished late one-sided tail, future positive ticket cost must be terminated; otherwise repeated late triggers will eventually exhaust every finite reserve.

P4-S031 shows that this is too strong. What must be controlled is the reserve budget of the renewed state, not whether renewal occurs at all. If an active state of scale c can incur at most 3c/4 premium drawdown before a late trigger, then starting with W>=c leaves at least c/4 even before crediting the trigger payout. Renewing at positive scale c/4 therefore closes the same reserve invariant. Repeated late triggers remain possible forever, but their worst unreplenished reserve demands contract geometrically.

At the same time, immediate favourable triggers can leave the scale unchanged because their one-sided payout exceeds the premium just spent. Along the all-immediate-favourable branch this produces the same divergent harmonic premium stream as P4-S030, funded by realized payouts.

Correct guard: terminalization is one sufficient way to set future reserve demand to zero. A strictly positive computable renewal potential is another. Insolvency still requires unbounded purchase-time premium deficit; mere repeatability of late triggers is not enough.

This does not establish that scale contraction is necessary. P4-S032 is reserved for whether the explicit contraction itself can be removed.


## FL-080 — final fibre size and ambiguity mass are not the resource; renewal can exist on a singleton target

Session: P4-S032
Date: 2026-10-06
Status: **DURABLE FINITE-AMBIGUITY LESSON**

Two tempting explanations of the k=1 versus k=2 jump are now ruled out as complete invariants.

First failed explanation: the destroyer works because the vulnerable source leaves one bit permanently hidden in its inverse fibre. P4-S011 says the opposite on the winning path: every epoch triggers, every source coordinate is eventually queried and the final fibre is a singleton. In the adaptive no-repeat scan model, P4-S032 makes this exact: h permanently unqueried coordinates give 2^h preimages. The P4-S011 target has h=0.

Second failed explanation: the amount of output ambiguity controls destruction. P4-S032 proves that zero ambiguity measure is indeed safe — an a.e.-injective map has an a.e.-computable measure-preserving inverse. But there is no positive safety threshold: localizing P4-S011 inside a small clopen cylinder makes destructive k=2 maps with arbitrarily small positive ambiguity measure. At the opposite extreme, P4-S002's exactly-two-to-one left shift has ambiguity measure one and preserves CR.

The better candidate resource is **renewable counterfactual ambiguity**. A k=2 scan may withhold one fresh source coordinate while exposing others, use the exposed information to determine a wager on that withheld sentinel, then consume the sentinel and move the hole to a new fresh coordinate. Off-target avoiding siblings justify the global two-point fibre budget; the target itself can finish with no ambiguity at all.

Correct guard: do not infer preservation or destruction from final fibre cardinality along the target or from lambda(A_F) once it is positive. Future characterization work should test whether arbitrary k=2 destruction normalizes to renewable one-hole adaptive access, or identify the extra non-scan resource if it does not.

## P4-S033 lesson — binary inverse width is not coordinate locality

**Failed route:** infer a one-hole scan presentation directly from the P4-S007 coherent width-two inverse skeleton.

**Why it fails:** width two bounds the inverse state to one binary cohort, but the two candidate source points may differ in many raw coordinates. A one-hole scan has a stronger invariant: every double fibre differs at exactly one raw coordinate.

**Exact destructive witness:** precompose the P4-S011 scan destroyer with a computable fair-coin-preserving blockwise three-bit linear homeomorphism whose inverse maps a virtual unit-coordinate difference to raw Hamming weight 2, 2 or 3. The conjugate remains globally k=2 and destructive but cannot be a one-hole scan or an output-homeomorphic one-hole scan.

**Positive lesson:** source recoding is harmless for R_2 but not definitionally harmless for OH. OH is invariant under signed coordinate permutations; arbitrary homeomorphism invariance is the real first source-level normalization test.

**Do not overclaim:** the coded-hole map refutes literal map normalization only. It does not prove R_2 proper-subset OH because the recoded source may still be destroyed by a different one-hole scan.

Next bounded attack: P4-S034 on OH invariance under the explicit coded-hole homeomorphism.

## FL-081 — finite Boolean mixing is harmless; infinite delayed stake selection is the surviving coded-hole resource

Session: P4-S034
Date: 2026-10-06
Status: **DURABLE ONE-HOLE NORMALIZATION LESSON**

Two stronger-looking inferences from P4-S033 are now ruled out.

First failed inference: once a virtual coordinate hole spreads across several raw coordinates, source-side one-hole normalization should already fail. P4-S034 proves the opposite for every recoding supported on finitely many coordinates. One may read the whole finite mixed block, skip the finitely many affected virtual wagers, and copy all remaining wagers. Finite deletion changes target capital only by a fixed positive multiplicative factor. Thus OH is invariant under all finite-coordinate fair-coin recodings.

Second failed inference: the direct P4-S012 stake pullback should itself become an ordinary raw self-avoiding stake. It need not. For the displayed three-bit mixer, virtual avoidance becomes invariance under a multi-coordinate inverse flip vector. A stake may depend essentially on every individual raw coordinate while still avoiding the queried virtual parity.

The exact surviving obstruction is temporal. A canonical raw support evaluator copies a virtual wager whenever the requested parity still has a fresh raw pivot. For the displayed matrix that evaluator is exhaustive, so copied gain is bounded on every computably random raw source. Any destructive witness must accumulate unbounded gain on the complementary **spoiled** stages, where the parity was fixed by earlier raw queries but the virtual martingale chooses its stake only later.

Correct guard: do not call this OH non-invariance. It is an exact compiler obstruction, not a source separation. A strict \(R_2\subsetneq OH\) conclusion still requires an actual \(x\in OH\) with a homeomorphic image outside OH.

Next lesson to test: whether spoiled stakes already decided at raw determination time can always be moved back to the last raw pivot, leaving only genuinely late-decision dependence as the possible infinitary resource.

## FL-082 — bounded delay is not finite closure

Session: P4-S035
Date: 2026-10-06
Status: **DURABLE ONE-HOLE NORMALIZATION LESSON**

The P4-S034 phrase “late choice after raw determination” needs two refinements.

First, “stake known at determination time” is not enough if it means after the determining raw bit has been read. A fair raw wager must be fixed before that pivot. Same-pivot late choice has an exact fair-price correction; the residual is a multiplicative late-choice premium.

Second, finite local delay is not the real obstruction. Every late-decision mechanism confined to one closed finite block, or to a uniformly bounded closed packet of blocks, is harmless under every repeated invertible finite block recoding: finite Doob compression transfers the whole packet exactly.

The first surviving architecture is **decision nonclosure across infinitely many blocks**. A pending spoiled parity in block \(b\) may wait for stake information from block \(b+1\), which creates the next pending parity, and so on. Individual delays may remain uniformly bounded while no finite packet closes.

Correct guard: this is still only a compiler obstruction. It does not prove OH non-invariance or \(R_2\subsetneq OH\).

Next bounded attack: P4-S036 on the dependency graph and infinite rays.

## FL-083 — finite forward closure is not effective packet closure

Session: P4-S036
Date: 2026-10-06
Status: **DURABLE ONE-HOLE NORMALIZATION LESSON**

The P4-S035 uniform packet-size bound was not a real boundary. A standard threshold-stopping savings transform makes martingale success persist to packet exits, so every computably finite closed packet can be compressed exactly regardless of its size.

The tempting replacement “every dependency has a finite/well-founded forward closure” is still too weak for two different reasons. First, the fact that a finite closure is complete may hide negative information: a rank-one edge can appear exactly when a machine halts. Second, even uniformly computable finite forward closures can overlap into one infinite interaction component; the rank-one graph \(a_n\to c_n,c_{n+1}\) has no directed infinite ray but its symmetrization is one infinite chain.

Correct positive guard: what the current compiler needs is a **total computable finite closed packetizer** which knows the complete packet before its raw coordinates are opened. Rank and forward finiteness alone are not substitutes.

Correct negative guard: an infinite interaction component is still only a compiler obstruction. Every finite truncation has exact Doob compression, and the remaining issue is effective stabilization of the backward fair prices of the open boundary claims. Failure of such a compiler does not prove OH non-invariance.

For the recoded P4-S011 witness, P4-S036 proves only that no total computable finite closed packetizer exists. It does not prove the recoded source lies in \(OH\), nor even that the essential graph contains a directed infinite ray.



## FL-084 — infinite interaction is harmless when the frontier renews effectively

Session: P4-S037
Date: 2026-10-06
Status: **DURABLE ONE-HOLE NORMALIZATION LESSON**

P4-S036 correctly identified backward pricing as the next object, but the explicit P4-S035 infinite ray does not require an effective infinite-limit argument. Its carried claim is replaced by a new virtual coordinate which has not yet been queried. Conditional on the visible transition transcript, that new parity is still fair. Therefore every normalized next-frontier price vector has mean one and vanishes exactly from the previous backward step.

The same rolling cancellation handles the P4-S036 rank-one overlap realization. Thus neither a directed infinite ray nor an infinite symmetrized component is, by itself, the obstruction.

The tempting next inference — bounded open-claim width plus bounded positive prices should suffice — is also false. The recoded P4-S011 witness has active nonzero width one. A fixed half-stake sentinel martingale still succeeds while its local triggered price vector is always of ((3/2,1/2))-type, so the condition number is at most three.

The correct surviving distinction is **effective retirement/stabilization**. P4-S011 has finite per-claim value dependence from its wtt use bound, but after those values are exposed the open computation may still halt only after an arbitrarily long search, or never halt on a sibling. Finite dependence is therefore not effective closure of the claim's backward price.

Correct positive guard: effective fresh-frontier renewal is sufficient, and effective Cauchy stabilization of absolute persistent-savings prices is sufficient more generally.

Correct negative guard: compiler failure still does not prove OH non-invariance. The recoded source is only known to be computably random, not in (OH).


## FL-085 — one-jump retirement effectivity and positive hedge cost are different resources

Session: P4-S038
Date: 2026-10-07
Status: **DURABLE ONE-HOLE NORMALIZATION LESSON**

The P4-S037 phrase “non-effective retirement/backward-price stabilization” splits into two sharply different routes.

For the actual value-closed P4-S011 persistent claim, the half-stake normalized price is not a complicated limit. It is exactly \((1,1)\) until a binary halt appears and then jumps once to \((3/2,1/2)\) or its reversal. Because the jump has fixed positive size, a computable deadline, eventual-constancy modulus, Cauchy modulus, exact limiting price, or a second semidecision for permanent nonretirement all decide whether the jump ever occurs. The actual recoded witness cannot provide that decision uniformly: if it did, P4-S037 would compile its successful half-stake witness to a raw martingale on the settled computably random source.

The correct positive escape is not a weaker retirement oracle. It is **prepaid uncertainty**. An unresolved stake of magnitude \(r\) has two possible triggered price vectors, and the exact minimal positive orientation-free superhedge costs the factor \(1+r\). If the cumulative product of those factors has a computable finite bound, one can carry enough reserve through c.e.-only retirement and obtain a computable raw supermartingale, then a martingale cover.

For the pure correct-prediction sentinel mechanism this escape is unavailable exactly when it matters: its target capital grows by the same product \(\prod(1+r_e)\). Thus the positive hedge cost and the virtual winning resource coincide multiplicatively.

Correct guard: do not respond by shrinking stakes and hoping for a second-order error. The unresolved backward-price error is first order in \(r_e\).

Correct next move: the actual witness cannot be normalized by an ordinary raw martingale without contradicting \(X\in CR\). To advance the sustained \(R_2=OH\) target, test direct **raw one-hole** simulation of the coded persistent claims instead.

Compiler failure still does not prove \(X\in OH\) or OH non-invariance.

## FL-086 — exact coded-hole rank and same-source vulnerability are different questions

Session: P4-S039
Date: 2026-10-07
Status: **DURABLE ONE-HOLE NORMALIZATION LESSON**

A virtual unit sentinel under the displayed three-bit source recoding cannot be represented by one omitted raw coordinate. The exact raw support costs are \(2,2,3\), and a fresh raw hole in a later block cannot transport the old affine ambiguity.

That exact-simulation obstruction is not a vulnerability obstruction.

For the actual P4-S011 autoreduction \(M\), the simultaneous locally correct three-bit assignments form a c.e. binary code of minimum Hamming distance at least two. For the displayed matrix every such code fixes some raw coordinate after \(A^{-1}\). Thus the finite algebra is positively informative: if the local code can be completed, a raw bit is available.

The remaining trap is **c.e. singleton completion under a preselected raw target**. For the two affine hypotheses determined by withholding one raw coordinate, the alternate endpoint may be finitely rejected, fully self-consistent, or non-self-consistent only because a sibling computation diverges. A wtt use bound controls oracle locations but does not decide this last halting question.

Correct guard: do not infer \(X\in OH\) from the \(2,2,3\) exact-simulation cost, and do not infer a raw destroyer merely because the full local code semantically fixes a coordinate. A one-hole stake must choose its raw target before reading it and must have a finite positive reason to progress.

Positive boundary: local sibling totality of the finite 24-computation block family makes the consistency code computable and yields a genuine same-source raw one-hole destroyer.

Correct next move: study online extraction from the c.e. local code / raw-adjacent companion relation, not another raw-martingale pricing compiler.

## P4-S040 lesson — positive pairs are visible, but divergence-only companions block online completion

**Successful weakening:** full local sibling totality is unnecessary. It is enough that each raw-adjacent companion be positively decisive: either locally self-consistent or finitely refuted by one wrong/nonbinary halt. Under this condition three synchronized raw one-hole scans yield a same-source destroyer.

**Why:** the P4-S039 minimum-distance-two local code law prevents all three raw-adjacent companions from being self-consistent. Thus every fully decisive block has at least one finite-rejection direction, and one fixed raw coordinate policy wins infinitely often by pigeonhole.

**Failed handoff route:** use the positive two-solution certificate in Case B to nominate a fresh same-block sentinel.

**Why it fails:** a raw-adjacent pair differs exactly at the current raw sentinel. Every raw coordinate it certifies is one of the other two coordinates, already read before classification. The certificate is therefore retroactive, not prospective.

**Global handoff guard:** while a current sentinel remains permanently unresolved, a globally one-hole scan must eventually query every other raw coordinate. A second prospective sentinel cannot also remain permanently reserved on that branch.

**Sharp surviving obstruction:** Case C. Once the actual endpoint is positively accepted, an unresolved companion can still later be finitely rejected, later become accepted, or diverge forever. No finite stage certifies the divergence-only alternative.

**Outside-equation lesson:** additional \(M(n)\)-equations can produce more c.e. rejection witnesses, but the wtt use bound is forward per-input information. It does not make the reverse dependency set of all inputs that may inspect the changed block computably finite.

**Guard:** failure of these online Case-C compilers does not prove \(X\in OH\). The actual P4-S011 machine is not known to satisfy raw-adjacent decisiveness, so no actual raw destroyer, OH non-invariance or \(R_2\subsetneq OH\) conclusion is available.

Next session: **P4-S041**, test finite-perturbation refutability / raw-adjacent decisiveness normal forms for the actual wtt autoreduction. Do not return to backward-price normalization, the frozen P4-S015–P4-S031 bankroll line, or ambiguity mass.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED.
## FL-087 — finite-perturbation partiality is forced, but the location of divergence is the real resource

Session: P4-S041
Date: 2026-10-07
Status: **DURABLE ONE-HOLE NORMALIZATION LESSON**

A self-avoiding wtt autoreduction of the P4-S011 computably random source cannot remain total on every finite perturbation. The computable use bound would otherwise make every finite answer pattern total and hence compile the machine into a truth-table autoreduction, contradicting the retained source boundary.

The important correction is that this does **not** force P4-S040 Case C at raw radius one.

Under the invertible three-bit recoding there is a minimal raw divergence radius \(\rho\). If \(\rho\ge2\), every single-raw-bit companion is total and therefore P4-S040-decisive; the existing three-scan theorem then gives \(X\notin OH\). Thus a surviving \(X\in OH\) branch must have \(\rho=1\).

But \(\rho=1\) only says that some equation diverges on some single-raw-bit companion. It may be an outside equation, or another local equation may already halt wrongly and finitely refute that companion. Do not equate radius-one partiality with local divergence-only Case C.

Finite-difference dependency cycles characterize the opposite, positive arm. If a finite companion is genuinely fixed on its changed coordinates, each changed output must depend on another changed coordinate. The \(011\) and \(101\) raw-adjacent supports force two-cycles; \(111\) gives a two-cycle-with-tail or an oriented three-cycle. The cycles become visible only after the relevant halts and therefore do not certify divergence.

A further local identity gives
\[
B_0\Rightarrow A_1,A_2,\qquad B_1\Rightarrow A_0,\qquad B_2\Rightarrow A_0.
\]
Hence a block with no finite rejection is necessarily triple Case C, but finite simulation still cannot certify that situation in advance.

Correct next move: localize single-raw-bit divergence. Determine whether remote divergent equations must propagate back to the three changed block equations, or whether radius-one divergence can remain remote while all local companions stay decisive.

Correct guard: failure to totalize the finite use table is a negative-information obstruction, not a proof of \(X\in OH\), OH non-invariance or \(R_2\subsetneq OH\).

## P4-S042 — remote-divergence localization failures and lessons

### Failed route: target-trace contact implies local Case C

A divergent radius-one companion equation does force the halting target trace to query the changed support. This finite contact is not enough to force a divergent local equation.

**Lesson:** after contact, a correctly halting changed-coordinate equation can pass dependence to another changed coordinate and close into a P4-S041 dependency cycle.

### Failed route: minimal wtt use gives a well-founded descent

Choosing a divergent input of minimal use does not force the contacted local coordinate to have smaller use. The first-contact fact is about the queried coordinate lying below the original computation's use, not about the use of that coordinate's own computation.

**Lesson:** forward use bounds do not orient the reverse dependency graph well-foundedly.

### Exact counterexample to per-witness localization

A computable finite-use self-avoiding functional on target \(0^\omega\) has one remote equation diverging under all three raw-adjacent perturbations while the three local statuses are
\[
(A_0,B_1,B_2).
\]

**Lesson:** remote partiality can coexist with full P4-S040 local decisiveness. Any theorem for the committed source must use more than self-avoidance, finite use and the three support shapes.

### Failed strengthening: remote traces force a finite rejection elsewhere

The target trace supplies dependency contact but no wrong/nonbinary output. It therefore yields no new finite cross-direction rejection law beyond P4-S041.

**Lesson:** preserve
\[
B_0\Rightarrow A_1,A_2,\quad B_1\Rightarrow A_0,\quad B_2\Rightarrow A_0
\]
as the exact finite-evidence law currently justified.

### New positive lesson: recurrence is the real surviving obligation

A single remote divergence, a single local divergence or a single Case-C block is too weak to support \(X\in OH\). If Case C disappeared after a finite cutoff, delayed-start P4-S040 scans would destroy \(X\).

**Lesson:** any surviving \(X\in OH\) branch must have arbitrarily late local Case C, with a fixed direction recurring infinitely often. Future work should attack recurrence/interleaving, not one-off localization.
## P4-S043 — recurrent nontriple-C harvesting failures and lessons

### Failed route: remove all-three synchronization and recurrence automatically becomes harvestable

A selected A/B direction can indeed close and restart without waiting for the other directions. But a selected C has no positive completion event and is absorbing.

**Lesson:** local asynchronous progress is solved; role selection is not.

### Failed route: infinitely many ambient A blocks give infinitely many A wagers for a fixed role scan

The local wtt simulations may consume raw coordinates in later blocks before the current sentinel closes. The next completely fresh target is therefore endogenous to the scan's own evaluation footprint.

**Lesson:** ambient raw-block recurrence is not scan-reachable recurrence.

### Failed route: add finite timeouts to skip C blocks

If every unresolved sentinel is guaranteed to close after finite interaction and prefix restoration follows, every coordinate is eventually queried. The scan becomes an effective adaptive permutation.

**Lesson:** guaranteed finite abandonment avoids C only by surrendering the one-hole resource and returning to k=1 preservation.

### Failed route: a finite family of pure wait policies must cover the visible A direction

For each fixed recurrent C direction, legal nontriple patterns can alternately expose A in one role while making another role C. A computable structural model can trap every member of any prescribed finite family after finitely many epochs.

**Lesson:** finite-family role switching does not force recurrent triple C from the current local laws.

### New positive lesson: the exact next resource is an online selector/fresh-lane theorem

The P4-S041 pairwise law is complete and P4-S040 synchronization is no longer the issue.

**Lesson:** future work should use the actual computable wtt horizon to test whether recurrent A witnesses can be placed on a computable fresh lane or reached by a transient one-hole-compatible race. Failure of such selectors remains an obstruction, not a proof of \(X\in OH\).

## P4-S044 — value-horizon selector failures and lessons

### Failed route: finite wtt use gives a fixed next fresh block

The use bound does close all source-value dependence for a local A/B/C test, but it does not bound the time at which a finite A/B certificate appears.

**Lesson:** a wtt value horizon is not a certificate-time horizon.

### Failed route: protect one future block while waiting forever on the current sentinel

On a no-event continuation, protecting the current sentinel and a different future sentinel forever would leave at least two holes.

**Lesson:** either the current role or the fixed future target must be abandoned at finite time. Moving reservations are legal, but they make the next target event-time dependent.

### Failed route: finite use implies finitely many fresh lanes

For \(I_b=[b,h(b))\), finitely many lanes exist exactly when interval-overlap depth is uniformly bounded. Each \(h(b)\) being finite does not imply this.

**Lesson:** \(h(b)=2b+2\) is already a computable finite-use unbounded-overlap geometry. Do not infer a finite coloring from pointwise finiteness.

### Failed route: countably many lanes recover recurrence

A computable countable lane decomposition always exists, but an infinite recurrent set may meet each lane only finitely often.

**Lesson:** countable pigeonhole is invalid here. A real concentration/thickness hypothesis is needed.

### Failed route: burn support at zero stake but preserve it as a later target

A legal local computation may request a future \(u_2\) value, which on a fresh raw block can require all three raw coordinates.

**Lesson:** support reuse is opportunistic, not forced by the use cap.

### Failed route: transient two- or three-sentinel races beat Case C without a time bound

On the all-C continuation, all but at most one candidate must eventually be consumed. Those finite consumption times can be outrun by arbitrarily delayed finite A certificates using the same bounded oracle values.

**Lesson:** temporary extra unread coordinates do not supply a rate-free selector theorem.

### Structural sharpness

A computable finite-use self-avoiding model on \(0^\omega\) can prepend ignored far \(u_2\) queries to the P4-S043 nontriple \(C_0\) gadgets. This makes the genuine horizon \(h(b)=2b+2\) while preserving visible A witnesses and finite-family trapping.

**Lesson:** finite use, self-avoidance, recurrent nontriple C and visible A do not by themselves force a fresh-lane selector.

### New positive lesson: the remaining issue is certificate-time selector thickness

The value footprint is no longer the mystery.

**Lesson:** future work must use source-specific structure—especially computable randomness and target-total wtt autoreducibility—to ask whether late sibling A certificates can systematically evade every computable moving-reservation selector. Failure to prove such thickness remains an obstruction, not a proof of \(X\in OH\).

## P4-S045 — selector-thickness and live-certification failures and lessons

### Failed route: cofinite or dense ambient A automatically makes moving reservations succeed

A faithful selector does not choose a generic member of the ambient A set. It chooses the reservation active at the current certificate time.

One early C exception on an otherwise A-cofinite lane can trap the scan. Bounded gaps or positive density can also be missed forever if certificate times repeatedly land on complementary reservation indices.

**Lesson:** the correct property is event-time selector thickness. Ambient density requires a clock-coupling theorem before it is useful.

### Failed route: recurrence on every computable subsequence controls the actual selected targets

The target subsequence of a computable scan need not be computable independently of the source. It can depend on finite source values and partial-computation halting times.

**Lesson:** prove source-independent computability of the selected sequence before applying any theorem that quantifies only over computable subsequences.

### Failed route: systematic late A certificates contradict computable randomness directly

After the P4-S044 value horizon is closed, finite certificate timing depends only on already exposed finite source data and internal computation. It does not query later reservation-block bits.

**Lesson:** delay alone provides no fresh bit prediction. A direct martingale argument needs an additional computable coupling from the clock to an unread source coordinate.

### Failed route: the P4-S044 finite-family countermodel cannot scale beyond finitely many selectors

For a prescribed uniformly computable countable family of faithful selector schemes, requirements can be handled sequentially. Each family member either is already C-trapped in the finite assigned prefix or eventually reaches an unassigned target, where \(CCA\) or \(CAC\) traps its preselected role.

**Lesson:** the finite-family bound was not the sharp structural limit. Prescribed countable families can be diagonalized while preserving finite use, self-avoidance, visible A and \(h(b)=2b+2\).

### Failed strengthening: diagonalize against every computable selector on the same computable target

After the structural model is built, finite A certificates on a computable target are c.e. A post-construction selector can enumerate increasing certified A blocks and use the computable target certificate times to keep each future block reserved only for a finite known window.

**Lesson:** a computable-target model with infinitely many visible A witnesses cannot defeat every computable selector. The escaping selector is endogenous to the completed model.

### Failed route: two interleaved selectors automatically harvest recurrent nontriple \(C_0\)

The patterns \(CAC\) and \(CCA\) can remain indistinguishable through any finite interaction while delaying their respective A witness. One role is A and the other C, but global one-hole fallback forces finite abandonment of at least one protected sentinel.

**Lesson:** the exact obstruction is role alternation + certificate delay + global one-hole fallback. Support consumption is not needed.

### Failed route: the visible B arm synchronizes the \(A_0\) clock

In \(ACB\) or \(ABC\), finite internal dummy delays can move the A0 wrong halt arbitrarily later than the B certificate, or vice versa, without changing use, queries, outputs or status.

**Lesson:** B visibility does not generically control A0 timing. Any useful coupling must be a special property of the actual committed autoreduction.

### New positive lesson: the actual-source gap is certification access

The structural post-construction escape works because \(0^\omega\) supplies all finite source values off-line.

**Lesson:** the next task should ask where prospective A evidence must be read on the noncomputable \(X\). A future target is useful only if its A certificate can be learned without consuming or indefinitely protecting the coordinates needed to keep that block fresh.

## P4-S046 — certification-access failures and lessons

### Failed assumption: a Case-A certificate intrinsically needs both non-sentinel raw bits

For this recoding, self-avoidance supplies three automatic finite rejections \(A^{-1}e_r\). Combining them with the actual raw-adjacent A witness reduces every A certificate to same-block cost at most one.

**Lesson:** distinguish finite hypothesis branching from live block access. The naive endpoint implementation can overstate the freshness cost.

### Failed strengthening: every visible A can be certified without opening its block

Roles 1 and 2 share one extra candidate: raw \(011\), virtual \(110\). If it is accepted or divergence-only, the wrong sentinel slice cannot be completely finitely rejected without one cross-role raw value.

Explicit \(CAC/CCA\) local gadgets realize this exact cost-one case.

**Lesson:** support-only A is not forced by finite use, self-avoidance, target correctness and recurrent visible A.

### Failed route: the B arm supplies missing local information for \(A_0\)

Theorem 2 already makes every \(A_0\) block-free.

**Lesson:** \(ACB/ABC\) cannot improve the local information cost below zero. Any useful B-assisted theorem must act on outside-support compatibility or transition structure, not on missing target-block data.

### Failed inference: block-free means usable while another sentinel is open

A cost-zero future certificate may still query a virtual value whose raw support contains the current protected sentinel.

**Lesson:** track two independent freshness objects: local target-block cost and collision with the already open hole.

### Failed route: one-bit access itself contradicts computable randomness

Knowing which coordinate must be read does not predict its value before the read.

**Lesson:** access structure is dependency information, not a source martingale. A randomness contradiction needs an additional coupling to an unread bit.

### New positive lesson

The target-block information problem is now small:
\[
A_0:\kappa=0,\qquad A_1,A_2:\kappa\le1.
\]

The next obstruction is sharper: can future finite A evidence be made **uniform over both values of the current open sentinel** while preserving the future sentinel and a total one-hole fallback?


## P4-S047 — current-hole uniformity failures and lessons

### Failed assumption: block-free future A is automatically safe around the old hole

P4-S046 removed same-block access for \(A_0\), and reduced \(A_1,A_2\) to one future non-sentinel bit. This does not control the outside traces of the rejecting computations.

**Lesson:** future-target freshness cost and old-hole branch sensitivity are independent resources. Even \(\kappa=0\) may fail current-hole uniformity.

### Positive lesson: safe old-row traces are automatically uniform

For current raw role \(i\), only the rows in
\[
\operatorname{Dep}(i)=\{r:A_{ri}=1\}
\]
change with the unread old bit.

If all finite rejection traces avoid those rows, the two old-hole simulations receive identical oracle answers and the same finite witness works in both branches.

**Lesson:** syntactic old-hole support avoidance is a clean sufficient condition requiring no runtime modulus.

### Positive lesson: two-branch future fixedness restores the automatic unit-flip theorem

If every future target-coordinate computation is target-correct under both old-hole completions, changing the future raw candidate by \(A^{-1}e_r\) still changes only the computation's own input coordinate. Self-avoidance then gives the same finite rejection in both branches.

**Lesson:** the P4-S046 \(0,1,1\) local costs survive an older open hole under an explicit branch-stability condition. Target correctness supplies that condition only on the actual branch.

### Failed route: self-avoidance alone neutralizes an older raw hole

The old hole changes rows in a different block from the future computation input. Syntactic self-avoidance says nothing about querying those old rows.

**Lesson:** the alignment used by P4-S046 is special. Old-hole perturbations are ordinary off-input oracle perturbations for future computations.

### Structural sharpness: one old row can gate every later low-cost A

For any current raw role choose one virtual row which depends on it. Make every future local computation query that old row first, run a validated \(ACB\), \(CAC\), or \(CCA\) table when the answer is \(0\), and diverge when it is \(1\).

On target \(0^\omega\) the future A witness and its P4-S046 cost remain visible. Under the alternate old-hole hypothesis every relevant future local computation diverges.

**Lesson:** target correctness, finite use, self-avoidance, recurrent nontriple C and low local cost do not force any role-to-role current-hole-uniform edge. Pointwise finite use also does not force infinitely many future A witnesses outside the collision set.

The model is structural only; its target is not computably random.

### Failed route: asymmetric two-branch behavior reveals the current sentinel

Both branch simulations are run from finite hypotheses. Seeing the \(h=0\) simulation halt and the \(h=1\) simulation diverge does not tell which hypothesis is actual.

**Lesson:** nonuniformity is dependency information, not automatically source information. A direct raw-bit prediction needs finite evidence eliminating one current completion itself.

### Failed route: c.e. edge existence automatically gives a computable path

Individual finite CHU witnesses may be positively discoverable, but searching many prospective future sentinels in parallel can itself recreate the multiple-protected-hole problem.

**Lesson:** retain the four levels: semantic edge, finite positive discovery, globally legal computable outgoing selection, infinite computable usable path.

### New positive lesson: persistent old-hole sensitivity is the next exact source-side resource

The structural countermodel can use one old row as a permanent gate. The committed source may have more rigidity, but none is yet proved.

**Lesson:** P4-S048 should study semantic influence of one current raw-radius-one perturbation on later A-certificate computations, not return to generic support enumeration or reverse-dependency closure.


### P4-S047 strengthening: finite wrong equations are not a surviving obstruction

A universal dovetail over both current-hole completions can test every autoreduction equation while keeping the raw sentinel unread. If one completion ever produces a wrong/nonbinary halt, target correctness eliminates it and the sentinel is predicted.

**Lesson:** finite branch refutability is harvestable by a total one-hole scan. Under hypothetical \(X\in OH\), the canonical search must eventually be trapped by a false raw-radius-one **partial fixed point**: every halt is correct and the only remaining source of branch distinction is divergence.

This narrows the next problem from arbitrary old-hole sensitivity to persistent divergence-only sensitivity of partial fixed-point neighbours.

## P4-S048 — partial-neighbour divergence lessons

### Failed route: partial fixedness forces eventual future fixedness

It does not. Family F closes the old changed support into a correct dependency cycle while one fixed old row remains the first-contact gate for a required listed future equation on every designated block.

**Lesson:** correctness wherever defined supplies no well-founded descent and no bound on recurrent divergence.

### Positive reduction: the canonical target-equation burden is finite and role-specific

The P4-S046 low-cost packages need only
\[
F_0=\{q_0,q_1,q_2\},\qquad
F_1=\{q_0\},\qquad
F_2=\{q_1\}.
\]

**Lesson:** full three-equation two-branch fixedness is stronger than necessary for \(A_1,A_2\).

### Failed route: totality of the false neighbour forces the false raw-adjacent rejection

Family R makes the false neighbour a total global fixed point, so every automatic unit-flip rejection survives, while the doubly perturbed raw-adjacent candidate makes every local computation diverge.

**Lesson:** target-equation fixedness and raw-adjacent rejection are independent kernels. The fourth corner of the two-raw-bit square is not controlled by the \(Z\)-corner.

### Stronger structural lesson: a partial-fixed-point star is possible

In Family R each false raw-adjacent doubly perturbed oracle is itself a global partial fixed point. Infinitely many such future perturbations can surround one false total fixed neighbour while the corresponding actual-branch candidates are finitely rejected.

**Lesson:** even an infinite local web of partial fixed points is structurally compatible with the retained finite-use/self-avoidance data.

### Failed route: persistent divergence directly predicts the old bit

Divergence is not c.e. Seeing one branch halt leaves open that the other is merely slower.

**Lesson:** retain the P4-S047 positive-information guard. Only finite elimination of a completion predicts the current bit.

### Failed route: semantic finiteness of bad candidates gives effective escape

A finite source-relative divergence set need not come with a computable last-bad bound or one-hole-safe way to select beyond it.

**Lesson:** effective escape must be supplied by a terminating computable procedure returning a legal CHU edge, not by semantic cofinality.


## P4-S050 — passive square capture versus completed fair hedge

### Blocked inference: one forbidden atom predicts the future bit on an arbitrary old epoch

A finite wrong/nonbinary square witness eliminates only the pair (a,beta). Without a trapped-epoch shield or a second same-column refutation, the other old row leaves both future values possible.

**Lesson:** unconditional exploitation is via a *two-bit* conditional-expectation hedge, terminal multiplier 4/3, not by an unjustified individual-bit prediction.

### Blocked inference: a single pair exclusion can finance infinitely many bets while old s remains unread

If s=1-a, both t=0 and t=1 remain allowed. A fair t-only wager cannot guarantee a strict gain on both. The valid two-bit hedge consumes s, so an executed capture resets the old epoch. An arbitrary passive scan collecting infinitely many square refutations against one unopened s is not the same as a scan executing infinitely many pair hedges.

**Lesson:** the new capture problem is *cross-epoch* and retains the certificate-time obstruction. Theorem P4-S050-5 applies only to active, executed, globally one-hole-safe square exits.

### Blocked inference: finite wtt use or infinitely many actual A blocks forces successful capture

Value horizons bound which bits a computation may request, not when its finite wrong halt is discovered relative to timeout. After each successful pair hedge the protected old coordinate changes.

**Lesson:** no X in OH, X not in OH or R_2/ OH separation conclusion follows from the absence of a known capture policy.


## P4-S051 — joint future hedge without old consumption, and permanent-hole limitation

Blocked inference refined: one forbidden square atom cannot produce a universal gain from only its future bit. But two positively excluded atoms against opposite values of a common unread old s at *distinct* unread future targets t,u do exclude one future-only tuple, yielding a fair 4/3 hedge without querying s.

**Lesson:** the exact effective finite-information target-only condition is a forbidden projected future tuple A(v)=empty, not a forced single future bit. Multiple refutations confined to the same old row do not suffice.

Blocked inference: infinitely many reset-free escrow opportunities at one permanently omitted s would prove new nonconservation on a CR source. P4-S008 already rules this out: any computably random source's winning one-hole scan must query every raw coordinate eventually.

**Lesson:** a valid finite fair escrow payoff, a timely positive *executed* capture, and a computable infinite series of certified old-sentinel turnovers are distinct requirements. Finite windows do not bridge the certificate-time gap by themselves.


## P4-S052 — finite cash-out is not executable infinite renewal

Blocked inference: two opposed-row future refutations always certify the value of old s after a successful 4/3 escrow. In the double-nonmatch surviving future outcome both old rows remain possible, so fair old betting cannot guarantee gain; it can only consume s at zero stake, absent new positive evidence.

**Lesson:** the exact finite cash-out multipliers are 8/3,8/3,4/3, not uniformly 8/3.

Blocked inference: the semantically shielded old branch will eventually yield a *matching* refuted future value or old-only wrong-output certificate. Both actual-future square corners are Y/Z fixed/partial-fixed, so no refutation can occur in that future column; at such an epoch actual escrow success always lands in the unoriented double nonmatch.

**Lesson:** profitable finite future-only escrow and certified positive old orientation are distinct, even where passive positive square witnesses are abundant.

Blocked inference: force old s to reset at every timeout in order to guarantee renewed captures. Such uniformly exhaustive least-unread scans are computable measure-preserving isomorphisms and cannot destroy CR.

**Lesson:** only branchwise-avoidable, timely executed successful turnovers could help; zero-stake consumption after an executed gain does not ensure the next gain. Late witnesses are not captured profits.


## P4-S056 — compelled old reset blocks effective four-run thickness on X

### Blocked inference: source-specific finite sigma forces frequent promptness even with compulsory old release

The actual target M^Y(q) halts and guarantees at least one of the four synthetic representatives halts on every X-derived value-closed cube. Nevertheless any total computable pre-consumption clock on a controller which consumes old s at **every** epoch, including timeouts, produces only finitely many timely cube certificates on X. Otherwise infinitely many sound 8/7 hedges would yield a computable martingale win on a computable isomorphic image of CR X.

**Lesson:** the problem is not merely finding a computable timeout; even transcript-dependent total timeouts are eventually outpaced on their OWN compulsory-reset X schedules. This is an unconditional source-specific anti-promptness law, not hyperimmunity of sigma on a fixed q list.

### Blocked inference: the unconditional law also prohibits success-gated renewal

A success-gated controller does NOT consume old s when future t,u expire. Its sibling branches can omit s forever; it is only globally one-hole, not a computable isomorphism. P4-S008 excludes infinite profits with one persistently omitted s on CR X, but does not imply the compulsory-reset theorem for a moving successfully consumed sentinel.

**Lesson:** any genuine success-gated obstruction must retain its branchwise avoidability, and any positive theorem must show infinitely many actual executed pre-consumption reset wagers. Finite BAR(r) decidability or retrospective eventual halts alone is not a renewal mechanism.

## P4-S057 — renewal gaps cannot be prospectively capped on an infinite-winning CR tail

Blocked inference: retaining old s after each timeout makes increasing finite windows enough to guarantee eventually bounded misses. For the actual success-gated T_L, a hypothetical eventually bounded W_e under any total computable epoch-start B creates an effective compulsory-reset shadow after a hard-coded finite prefix, whose infinitely profitable isomorphic image contradicts CR X. The shadow alone consumes s on the budget exhaustion; actual missed reservations retain s.

**Lesson:** if infinite success occurs, missed-reservation counts defeat every prospective computable epoch-start budget infinitely often; this does not show that success occurs.

## P4-S058 — finite safety certificates do not force unlimited renewal on CR X

Blocked inference: a positive wrong-output certificate is an actual winning terminal payoff on every sibling. Only the SEVEN winning hedge leaves count; the forbidden leaf pays 0. Counting raw positive discoveries alone invalidates the 8/7 probability estimate.

Blocked inference: a raw finite prefix, or effectively closed (even countably unioned) source safety class, can force infinitely many profitable 8/7 turnovers on CR X. The uniformly c.e. open event G_n of n completed winning exits has probability at most (7/8)^n, so no finite cylinder forces all gains. An effectively closed class included in all G_n is null and excludes every CR source; likewise effective F-sigma suppliers.

**Lesson:** any actual-X renewal supplier must use genuine infinitary progress beyond effective F-sigma safety, with concrete timely source-reached witnesses. Effective G-delta syntax alone does not establish membership of X, and no computably selectable avoiding sibling follows from the measure argument.


## P4-S059 — no computably scheduled finite-output-horizon infinite progress on CR X

Blocked inference: arbitrarily late but finite source-specific correct certificates imply the nth genuine completed 8/7 old turnover occurs promptly along some total computable global output schedule infinitely often. For every computable h(n), the finite clopen event C_{n,h(n)} has measure <=(7/8)^n and its infinitely-often occurrence on CR X would be defeated by a computable rational source martingale. Hence even infinitely-often computable OUTPUT-horizon promptness is impossible, and any hypothetical infinite n-th winning-time function dominates every computable function eventually.

Lesson: finite operational Pi^0_2 progress has no effective rate on the committed CR source; its membership cannot be inferred from eventual M halting, high Turing degree, or P4-S057 unbounded missed reservations. The original P4-S011 Y all-trigger scan already has a dominant time function, so this new obstruction is compatible with the retained source; actual infinite T_L gains remain unproved.

## P4-S060 — long computation alone cannot explain a bounded number of complete reservations

Blocked inference: P4-S059's noncomputably slow nth winning OUTPUT time could arise with only computably few completed finite-tenure reservations, provided each has huge raw closure or simulation time. But every actual T_L reservation ends on ALL sibling oracles at a finite total computable deadline or positive certificate. A complete m-reservation decision tree gives a computable uniform output length b(m). Therefore conditional infinite wins on CR X imply the ACTUALLY EXECUTED cumulative missed-reservation count S_n=sum_{e<n}W_e eventually dominates every computable f(n).

Lesson: distinguishing complete reservations from P4-S011's possibly unending c.e.-trigger epochs is essential. Dominance of cumulative W_e is an operational corollary of P4-S059, not independently stronger than output-time escape, and never verifies actual X's Pi^0_2 winning membership. P4-S057's individual prospective adaptive budgets remain unchanged.

## P4-S061 — fast success bursts cannot recur arbitrarily long after any start prefix

Blocked inference: P4-S057's infinitely-often overbudget epochs can be separated by locally arbitrarily long (relative to their emitted epoch-start prefix length) runs of budget-prompt profitable epochs on CR X. An effectively weighted portfolio over EVERY valid finite epoch-start history h and finite B-truncated k-success SHADOW detects runs of length K(m)=64ceil(log_2(m+2)). The fair surviving-atom cost (7/8)^k and a computable h,k sum yield a single computable rational source martingale that would succeed if such runs occurred infinitely often.

Lesson: conditional infinite actual gains impose a local logarithmic spacing law on individual ACTUAL missed-reservation budget overruns, not just cumulative S_n domination. The proof uses clopen historical-prefix tests; it does not show infinite gains or turn the shadow compulsory reset into the actual success-gated rule. No assumption of highness or pointwise total future capture is sufficient.

## P4-S062 — mass-only local-spacing sharpness, without a legitimate infinite-renewal source

Blocked inference: from the isolated fair surviving-atom inequality lambda(F_m)<=(7/8)^k(m), infer that subcritical-log k(m)-long historically B-prompt winning windows cannot recur on CR sources. Uniform independent disjoint fair-triple cylinder events satisfy this exact numerical mass bound but recur infinitely often with fair-coin probability one at subcritical logarithmic scales; some CR sequences witness the recurrence. These abstract tests are NOT a legal success-gated one-hole scanning process.

Lesson: the length-selected computable source-martingale method gives a strong sharp quantitative improvement: using 2^5*7^26<8^26, an individual actual W_j overbudget event must occur in the next ceil(26ceil(log_2(m_e+2))/5) epochs, CONDITIONALLY on infinitely many completed real profits. Further mass-only constant tuning is no substitute for a structural committed T_L dependence theorem or source-verified infinitary progress. Zero-stake timeout releases do not reset old s; eventual M^Y halts do not give prospective deadlines. X/OH and R_2/OH equality remain unresolved.

## P4-S063 — frozen old-sentinel reflection and marked finite-renewal kernel (2026-10-08)

**Mathematics checkpoint, NOT a gate or novelty decision.** On the unchanged actual success-gated T_L, flipping the unread old sentinel leaves the entire pre-reset trace, first positive gate and real completed timeout count unchanged. Every finite prospective epoch gate has an EXACT computable rational reachability weight g. At its pre-consumption protected triple, one atom is forbidden zero, one is a fragile old-bit-sensitive 8/7 win, and six are robust old-bit-insensitive 8/7 wins; the marked probabilities are respectively g/8,g/8,3g/4. Fixed marked k-win words have finite clopen mass <=2^-m(1/8)^f(3/4)^r.

CONDITIONAL on infinitely many ACTUAL profitable old resets on committed CR X, for each total computable prospective B, every sufficiently late 2J(m_e)-epoch window (J=ceil(log_2(m+2))) either has W_j>=B(j,p_j) or strictly more than J(m_e) robust exits. The proof uses an effective finite-clopen portfolio bounded by sum_j(j+1)(3/4)^j. One-J all-fragile B-prompt windows are likewise excluded eventually. These MARKED laws do not replace the P4-S062 W-only K_62 law, and no infinitely executed profitable renewal is verified. All exact fresh-block, paired-trace, clipped, pre-consumption, timeout no-old-reset, fair ledger, global one-hole and earlier frozen theorem guards stand. X in OH and R_2=OH unresolved. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED; no Gate-4 or novelty/publication claim. No blocker; next P4-S064.

## P4-S064 — gate conditional weights measure reachability; they do not cause infinite renewal

Blocked inference: a large exact computable first-gate probability g_h^B supplies the next timely positive certificate on committed X or proves infinitely many source-reached profitable resets. The old-bit flip leaves all B-pre-gate actions identical, and at finite h with 0<g<1 both first-gate and no-gate branches exist. The actual next outcome is not selected by its rational conditional probability.

Positive mathematical consequence: an actually reached length-m epoch which completes B real t/u zero-stake releases and non-s sweeps without old reset lies in the clopen complementary no-gate event of exact conditional mass delta=1-g. A computably summable portfolio forbids infinitely many such events on CR X when delta<=(m+2)^-3. Thus, ONLY conditional on genuinely infinite profitable renewals, every sufficiently late P4-S062 K_62 window has a completed W-overrun at a source-reached epoch with computably measured delta>(m+2)^-3.

Lesson: this is an exact finite-gate dependence/deficit obstruction with a source martingale, not a source-verified renewal certificate. Do not upgrade the computational ability to audit delta or the eventual finite M^Y halt to an infinite actual executed 8/7 profit assertion; preserve every preconsumption, timeout-without-old-reset and global one-hole guard.

## P4-S065 — survival-frontier averaging is not a source-X gate certificate

Blocked inference: a non-summable *purported* gate series, finite conditional g or P4-S064 delta, highness, abstract Pi^0_2 membership, or retrospective M^Y runtime yields an ACTUAL positive future gate. Only the exact finite-tree RAW no-gate survival q_n determines the controller-specific frontier-averaged c_n; the average integrates over ALL off-X histories and is not a pathwise X probability.

Positive obstruction: forever-stalled CR source at h lies in effectively closed F_h, forcing q_infty>0 and summable c_n by P4-S058; all B deficits then have a positive (not necessarily computable) floor. Zero q_infty at every X-reached h would force infinite real gates but was NOT proved. Preserve true timeout zero-stake t/u release, non-s sweep, NO old reset, prospective deadlines and sound pre-consumption certificates.

## P4-S066 — frontier averaging cannot replace individual CR-stall conditional hazards

Blocked inference: P4-S065 convergent surviving-frontier averaged c_n identifies the committed source trajectory's gate probabilities or implies actual progress. In fact a computable transcript-local gamma(p) is needed; a general martingale on nonmonotonic output is NOT automatically a source martingale. Positive exact law: a fixed forever-unread old s invokes P4-S008's computable permutation completion and permits one fair timeout martingale transfer; consequently CR permanent stalls have sum gamma(p_n)<infinity. An abstract mixture separates averages from an exceptional nonrandom survivor, not from committed M/Y/X. Nothing proves gamma divergence on X or infinite actual 8/7 exits. Timeout remains ZERO stake t/u release and non-s sweep WITHOUT old reset.

## P4-S067 — short certificate depth is not gate recurrence

Blocked inference: eventual M^Y halting, globally clipped finite use, or a computable finite deadline proves a positive actual next-reservation gate hazard, a bounded-depth recurring sibling gate certificate or summably large gamma on X. A valid alternative program can insert K+1 silent steps without changing its partial wtt autoreduction functionality; the legitimate L=K controller then has gamma=0 at every reservation. This is an **alternative M**, not the committed M. Positive finite-tree law: gamma is the dyadic measure of prefix-free gate-decision leaves. The P4-S066 source-local hazard budget forces a global C*2^K count bound on shallow certificates along every CR permanent stall. Increasing minimum leaf depth alone is not sufficient when gate leaves multiply. Neither condition proves actual infinite executed 8/7 gains.


## P4-S068 — finite value-closure multiplicity versus fictitious source-gate recurrence (2026-10-08)

**Validated mathematical lesson.** The unchanged success-gated four-run controller tests four clipped M(q) computations on a finite closure. Post-closure simulation filler bits are **value-inert** (although actual steps still occur); counting their lengths in first-gate output leaves obscures the stronger exact gate-cylinder formula gamma(p)=a(p)/2^c(p), with a(p) the number of timely positive closure assignments and c(p) the number of new informative closure bits. The P4-S066 fixed-hole martingale therefore constrains sum_n a(p_n)/2^c(p_n) on *every actual CR permanent stall*. It is INVALID to deduce from this necessary inequality that the fixed Y/M/X produces divergent weights, infinitely repeated resets, or that a potential sibling cylinder was actually traversed. A true timeout has a negative finite-clock decision at the actually seen eta even though target M^Y ultimately halts. The witness M is mathematically fixed via S011/S027 but no explicit executable index and computable oracle data were given for numeric actual-X trace measurement. No separate alternative padded-program inference about fixed M is made. Freeze all mathematics and P4-S057 controller invariants, including mandatory zero-stake t/u releases and non-s sweeps WITHOUT old reset. PA-0001 and DEF-0020 unchanged; Gate 3 PASS, Phase 4 OPEN, Phase 5 CLOSED, Gate 4 NOT REVIEWED. No novelty/openness/prior-art/publication/outreach claim. Next P4-S069; no blocker.


## P4-S070 — literal shear-hole geometry is not a global OH counterexample (2026-10-08)

**Blocked inference:** because the virtual third-coordinate omission under (a,b,c)->(a,b xor c,c) corresponds to raw Hamming difference (0,1,1), a one-hole observer cannot literally reproduce that exact two-hole virtual ambiguity; this does NOT prove that any CR raw source belongs to OH, nor that its recoded image lies outside OH. A divergence-only Case-C sibling cannot be declared negative after a finite timeout. Replacing exact scan simulation by general same-source destruction requires a globally total fair no-repeat scan with at most one permanently omitted raw coordinate on EVERY transcript and a genuinely successful computable output martingale.

**Positive global lesson:** the original H-preservation property is equivalent to OH preservation under every computably supported two-coordinate XOR shear and under all computable blockwise GL(3,2) recodings. This follows from H^7=identity, selective swap conjugation, S033 signed-permutation invariance, and uniformly finite elimination words. The theorem narrows the global obstruction to a two-coordinate mechanism; it is not a decision of H-preservation, X in OH, R_2=OH, or R_2=OH^{iso}. No renewal/hazard assertion about the fixed S057 controller was changed.


## P4-S071 — the zero-stake shear evaluator forfeits genuinely late spoiled wagers (2026-10-08)

Blocked inference: because a supported XOR shear uses only two raw bits, one can copy EVERY virtual one-hole wager on the same raw sequence. In fact a virtual request for v=b xor c must consume c before b to copy that parity bet; a later virtual request for w=c has then been pre-revealed and cannot be wagered on as fresh. Betting on c at the earlier filler time with the LATER w stake is not computably legitimate when that stake depends on later virtual information or a Case-C partial sibling computation. Literal virtual w-hole geometry is not a reason to infer OH membership either.

Positive controlled result: an everywhere-total globally one-hole raw evaluator exists, and the exact discounted-capital lower bound is e_{n(m)}>=d_m exp(-sum_spoiled|s_t|). Therefore any true separator from OH must realize infinite non-summable late spoiled-w exposure; finitely many/absolutely summable spoiled wagers cannot destroy an OH source through ANY computable supported shear. A deterministic virtual v,w,u order with constant 1/2 wagers on w has unbounded exposure without itself furnishing a CR destroyer, showing why finiteness cannot simply be assumed. This is a quantified refinement of S034, not a solution to S035–S044 future-stake effectivity. All S057 controller and source-X guards retained; no mathematical/policy gate transition.


## P4-S072 — an unavailable early stake need not mean an unpriceable late wager (2026-10-08)

Blocked inference A: read the future signed fractional stake on virtual w at the INITIAL raw c filler. In the explicit all/alternating pair schedule v_even,u_odd,w_even,u_even,v_odd,w_odd, the w_even stake is ±1/2 based on future u_odd. Identical pre-c raw prefixes have opposite future stakes; no total pre-c exact forecaster can be correct on both. That is a limitation of this method, not an impossibility of later same-source extraction.

Positive repair: at the later **fresh raw** u_odd pivot, c_even is known and the virtual factor is a fair 1/2-versus-3/2 child multiplier on u_odd. A total computable fair-credit registrar yields martingale F, while S071's live-copy L is another martingale. One must NOT claim the product L*F is a martingale; the mean h=(L+F)/2 is. For faithful claims L*F=d_m A_m, and h>=sqrt(d_m A_m). The exact remaining barrier for this certificate architecture is arbitrarily low product A_m of OPEN credits; retrospective eventual halting or finite-size dependency alone does not bound A_m, and Case-C nonhalting cannot be used as an online negative certificate. Shared-pivot clusters may fail to have fair price 1 and need independent analysis in P4-S073. No OH membership/noninvariance conclusion from registrar failure. All frozen governance and S057 controller untouched.


## P4-S073 — same raw pivot is NOT two independent fair wagers (2026-10-08)

**Blocked method:** multiplying individually fair spoiled-w factors (1+alpha r)(1+beta r) as though the result were itself a fair raw single-bit stake. Its mean is 1+alpha beta, not 1. Bounded number of pending claims cannot bound accumulated prices of ALREADY SETTLED bundles: repeated aligned packets have Pi=(5/4)^N on a possible raw branch, despite at most two outstanding claims. This is only a failure of naive unfinanced pricing; it is not an OH counterexample or a proof that all joint price hedges fail.

**Positive correction:** register each finite real-pivot bundle with computable joint price pi=(G(0)+G(1))/2>0 and wager G/pi before the raw bit. Preserve pending A separately from accumulated Pi: L F Pi=d A. If a separately TOTAL computable raw martingale Q provides price escrow, the sum-of-three inequality h_3>=(d A Q/Pi)^(1/3) gives a precisely conditional transfer. In an exhaustive four-block all/even XOR shear, the two c bits are revealed as REAL fillers before their shared later fresh u decision; at second c, fair children (3/4,5/4) pre-fund price, then fair G/pi on u yields e>=d/4 on every source, with equal packet-boundary capital. 8192 finite checks passed. That finite packet does not solve the genuinely infinite nonclosed dependency gap. Keep Case-C nonhalting, all-source scan legality, S057 exact controller and all governance guards unchanged.


## FL — P4-S074 rolling multi-claim escrow: real pre-finance and nonclosed boundary (2026-10-09)

**Validated positive lesson:** The S073 joint-price identity L F Pi=d A can support an unbounded, temporally overlapping infinite claim graph even when finite disjoint block-closed packets do not exist. In the explicit all/even-shear four-block chain, old pivot R_i also enters the NEXT claim/price, so adjacent groups are linked. Exact pre-bit finance at a genuine fresh c_{4i+2} with child multipliers 1+q² C_i0 R_{i-1}s is fair; at a genuinely later fresh a pivot normalized G_i/pi_i is fair. Here Q,F bet at distinct REAL coordinates, so e=QF is fair, and bounded pending downside A and the ONE prepaid-but-uncharged price give e>= (1-q)²(1-q²)d. Sharp 3/16 at q=1/2; 4096 finite assignments, 159744 checkpoints, zero discrepancies. This is compatible with S037 effective fresh renewal, not a universal theorem.

**Failed strategies retained:** (i) Multiply two individually fair wagers at the same fresh bit without dividing by their joint price; their product has conditional mean pi_i, generally not 1. (ii) Wager pi_i at its own a pivot after it is already determined; equal-child multiplier pi_i is not fair unless pi_i=1. (iii) Bound only the number of pending claims and ignore settled premiums in Pi, or bound only Pi and discard an executable Q; either conflates different burdens. (iv) Treat formal conditional expectation or future unknown stakes as total computable finance; no such effectiveness follows. S074 avoids these failures only through engineered earlier REAL price-betting and finite effective claim retirement. Neither OH membership nor non-invariance follows from failure of a compiler. Keep original X/Y/M/H, S057 exact controller, PA-0001/DEF-0020 and gate states unchanged.


## P4-S075 — explicit escrow-funding limitations despite effective savings (2026-10-09)

**Failed unconditional all-checkpoint floor extrapolation:** with computable q_i=1-2^{-(i+2)}, spoiled pending multipliers and pre-funded residual prices remain strictly positive yet A(Q/Pi) becomes arbitrarily small along a single compatible infinite raw input. Fixed-q S074 lower factors do NOT extend uniformly. Success nevertheless transfers through exact computably cofinal settlement mirrors, not a worst-checkpoint ratio.

**Failed reuse of OLD escrow after savings:** applying the persistent-stopped virtual martingale changes its effective wagers and joint payoff table; multiplying the original d's Q/F finance does not establish the required hat d identity. Recompute the entire finite 2x2 table for hat d BEFORE the genuine funding bit.

**Three-claim structural impossibility (narrow):** two already raw-known spoiled c signs C0,C1, a final real fresh c sign s, and a later fresh a pivot r give G(r,s)=(1+q C0 r)(1+q C1 r)(1+q s r). Its proposed last-c-filler exact price p(s)=E_r G=1+q²[C0C1+s(C0+C1)] has E_s p=1+q² C0C1 != 1. Thus a single last-filler wager with factors p(s) CANNOT be fair, regardless of the earlier capital scale. At q=1/2,C0=C1=+1 the two factors are 7/4 and 3/4, average 5/4. Earlier multi-filler finance, other raw compilers and S037 are NOT ruled out.

**Effective-knowledge guard:** settled joint prices Pi are cumulative and need not be bounded; A measures only unsettled claims; Q is actual financed capital and Pi itself is NOT automatically a martingale. Do not assume unknown future virtual stakes, nonhalting certificates, source-specific recurrence or a price convergence modulus. S075's cofinal mirrors are an explicitly engineered computable schedule; S037 already covers effective retirement here, and actual X remains unresolved.


## P4-S077 — finite truncations cannot be promoted to an infinite recoding without a new global argument (2026-10-09)

Global exact result: finite F preloading gives universal all-one-hole-observer same-source preservation with deterministic capital-loss ≤2^|F| and NO effective-retirement assumption, even for arbitrarily late or permanently absent virtual F requests. FAILED inference: apply this for F_n increasing to all blocks and take n→∞; the loss constant diverges, both raw scans and martingales vary with n, and computable randomness / OH membership is not known to be closed under that limit. This does NOT prove infinite-support impossibility. S037 price assumptions and S071 spoiled exposure remain the unresolved full-support obstacle. Do not continue S072–S076 price calculations without a proved bridge to H-preservation, X classification or R₂/ OH separation.

## P4-S078 — single-shear equivalence does not certify OH invariance (2026-10-09)

P4-S078 (2026-10-09): GLOBAL single-shear criterion. Writing S=S_N (a,b,c)->(a,b xor c,c) on EVERY three-bit block and Q_E the computable within-block b/c swap on decidable E, the exact full-Cantor identity S_E=Q_E S Q_E S Q_E proves all computable-support shear preservation iff preservation under the ONE FIXED infinite-support S; by S070 this is equivalent to committed H-preservation and all computable GL(3,2)-block recoding preservation. Independently, the exact committed H factors as S R Q S R Q S R (right-to-left; R swaps a/b globally, Q swaps b/c), giving THREE explicit all-shear witness-transition candidates on the fixed X->Y chain IF X lies in OH. This is only a global algebraic quantifier reduction, NOT S-preservation, not nonpreservation, not X membership and not R2=OH; R2=OH^iso stays separate. All 65536 four-block support/source identities and 168 GL3 generator states passed with zero discrepancies. S037/S073–S077, exact S057 controller and ORIGINAL Y/M/H/X preserved; no finite truncation limit, effective-retirement assumption or new raw compiler. Gate 3 PASS, Gate 4 NOT REVIEWED; Phase 4 OPEN, Phase 5 CLOSED; PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. No novelty, openness, prior-art, publication or outreach claim. Blocker NONE. Next P4-S079: prove or disprove preservation under this fixed S with an actual OH source, or classify committed X directly.

## P4-S079 — sparse sentinel families require a global sweep (2026-10-09)

A correct self-avoiding predictor on infinitely many computably chosen coordinates does NOT by itself make the naive restricted least-fresh comb globally one-hole: infinitely many all-trigger epochs could leave infinitely many non-sentinel coordinates unread. The proved repair is a GENUINE zero-stake least-unread raw sweep after EACH successful sentinel; a permanent stalled epoch exhausts the complement of its one sentinel, while infinitely many successful sweeps exhaust all coordinates. This constructs globally legal winning scans on z1,...,z6 via fixed Y and M. Do not interpret B0's absence of unit columns as proof z0=R(X) belongs to OH: a sufficient vulnerability criterion failing says nothing about other legal raw tests. The fixed S and R2=OH remain unresolved; no general preservation or impossibility theorem is inferred.


## P4-S080 — an existentially fixed object cannot carry a membership proof (2026-10-09)

Lesson: before attacking a property of a committed object, check what the record actually fixes. Y was fixed only existentially, so 'z0=R(X) in OH' for the committed Y is a theorem only if it holds for every admissible (Y,M). P4-S080 exhibits an admissible pair (chained-substitution spreading, block-avoiding autoreduction) with H^{-1}(Y1) notin OH; hence the membership arm pursued implicitly since S039 cannot be proved from the record, and the nonmembership arm is exactly the universal statement U(H). S039–S079 conditional results ('if X in OH then ...') remain valid as necessary conditions for any U(H) counterexample but are not evidence that X is in OH. Do not infer OH membership from failure of a sufficient vulnerability test. Separation work needs an OH certificate for a non-MLR sequence, which the programme does not yet have; proving OH=MLR instead would imply KLR=MLR (QST-0001).


## P4-S081 — bounded hole budgets are free; certification needs a genuinely unbounded-width or timing obstruction (2026-10-09)

Lesson 1: before designing a non-MLR OH candidate whose non-randomness is visible only to strategies that hold two or more coordinates (for example c.e. test components closed under single-coordinate flips), check Theorem A. Any strategy that postpones uniformly boundedly many coordinates reduces to a one-hole strategy: colour the held intervals online and split the log-capital. Such candidates are therefore not in OH. The flip-closed idea failed for exactly this reason: a 2-hole strategy reads the enumeration's structure, for example the centre of a Hamming ball.

Lesson 2: the certification construction (sparse windows with late-revealed c.e.-family content, placed away from held coordinates) failed at two exact points. (i) Choosing window positions from the random background leaks information about held coordinates. (ii) Strategies place blind fill bets on window content before revelation, and controlling them needs a content-selection rule compatible with a small c.e. family and with qualifying late stages the construction does not control. Recorded as the exact obstruction for P4-S082, not as a refutation.

Lesson 3: left-c.e. CR non-MLR reals give only one-sided c.e. certificates (bit value 1). This yields neither OH exploitation nor OH certification.

Lesson 4: an audit check placed one step too early (before the scan's own pulls) produced a false failure. Check invariants at the point of the construction where they are claimed.


## P4-S082 — control the expected capital over all completions, not the placement of hidden windows (2026-10-10)

Lesson 1: the S081 §7 obstruction came from the design, not from OH. Building a non-ML-random member against an independent random background forced the two problems (independence; blind bets). Fixing sparse bits so that a consistency potential (the capital-weighted mass of transcripts still consistent with the fixed bits) never increases, and then selecting the sequence by compactness, avoids both problems. Before declaring a construction obstruction intrinsic, try the expected-martingale/compactness template from the literature on restricted non-monotonic randomness (SRC-0069).

Lesson 2: in such potential arguments, isolate the single place where the strategy class matters. Here it is the split-weight (cost) bound, Lemmas 3.1–3.2. The monotonicity, domination and refinement lemmas hold for every total computable fair map. This shows exactly which extensions are open: unbounded width (Example E1), non-block homeomorphisms (Example E3) and globally ≤2-to-1 maps (Proposition 6.2 gap).

Lesson 3: a construction controlled against blockwise recodings as well produces witnesses robust under those recodings (Theorem 5.1). A separation witness for R₂⊊OH must therefore come from structure that the potential does not control, not from sparse fixing alone.

Lesson 4: when an induction invariant has the form Φ < 2−2^{−i}, check the base case: the initial value equals 2−2^{1}, so the invariant must be non-strict before each stage.


## P4-S083 — a hole that covers every candidate cannot be avoided by candidate choice (2026-10-10)

Lesson 1: S082's construction defeats every raw one-hole scan because it can always fix a coordinate outside the held one, and the potential then chooses the value adversarially. A scan whose single held bit is coded over an entire raw tail (one-hole scan of the prefix-difference homeomorphism D′) is never avoided. It does not need to predict the value: it waits until the construction has chosen and reads the choice off a simulated run. When a potential argument handles a class only through candidate avoidance, test the class against holes whose difference sets contain every admissible candidate.

Lesson 2: in a separation, the adversary is the analyst's ally, not an opponent. To show OH ⊄ R₂ it was enough to keep the S082 guarantees against raw scans and to make one specific coded-hole scan win. The only new difficulty was fooling by spurious guessed runs. Disjoint position classes per guess made each fooling event a fresh cylinder of measure 2^{−r}, which compactness can exclude.

Lesson 3: before attacking a "bounded resource vs MLR" question, calibrate against the unbounded version in the literature. Petrović's universal pair of sequence-set strategies shows R_tot = MLR, so fibre-boundedness is exactly the resource at stake in R₂ versus MLR.

Lesson 4: exact fixing-martingales (the savings potential β; the counting potential Π_∞ for ≤2-to-1 maps) exist for every total fair map. The difficulty of such constructions is never "cost" in the true potential, only the computability of the choices. Guessing a left-c.e. potential to precision 2^{−ℓ} costs about ℓ bits, which cancels the compression of ℓ fixed bits.

## P4-S084 — predictable T* errors and balanced a.e. two-sheet destruction (2026-10-10)

Phase 4 mathematics ONLY. Proved: predictable selection of infinitely many output bits of a computably random sequence yields a computably random prediction-error stream (frequency of mistakes 1/2). Hence a putative R₂ survivor with infinitely many S083 T* resolutions needs an entire CR error stream, not one wrong guess. Anti-consistency cylinders give λ(E_Q)≤2^(−Q−3); an exact restart martingale shows infinitely many T* resolutions occur only on an effectively ML-null input class. Consequently S083's UNCHANGED k=2 fair destroyer G=F_T*∘D′ has exactly two equal-conditional-weight preimages for almost every output, while still destroying an exceptional computably random singleton-fibre z∈OH^blk∖MLR. This refines the existing proof R₂⊊OH, NOT the still-unresolved R₂=MLR versus MLR⊊R₂. Finite sanity audit 8,201 checks, no infinitary computational claim. All original Y/M/H/X, P4-S001–S083, S037/S057, Gate-3 PASS, PA-0001, DEF-0020 frozen; Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No new literature access, novelty, openness or publication assertions. Next P4-S085: bounded-fibre universality or high-entropy R₂ survivor. Records in phase4/P4-S084_MATHEMATICS.md, _VALIDATION.md, _CLOSE.md, _EXTRACTION_AUDIT.py.

## P4-S085 — universality compilation limitation (2026-10-10)

Route A failed to turn the SRC-0071 unbounded-fibre universal strategies into globally ≤2-to-1 maps: changing only the computable output martingale or conjugating with input/output homeomorphisms cannot change fibre cardinality. The correct global test is the uniformly effective c(n) two-prefix width condition at EVERY output cell, not just near a selected non-MLR sequence. Route B failed to exhibit a non-MLR x avoiding all global width-two filtration/martingale pairs; a computably random resolution-error stream at S083 T* is only a necessary condition. The exact equivalence in S085 is an honest reduction and does not decide R₂ vs MLR or rule out all universal bounded-width strategies.

## P4-S086 — single-observer and common-output-factor dead ends (2026-10-10)

Failure A: A putative universal width-two filtration cannot be repaired just by adding a universal list of output martingales. By THM-0007 and THM-0035, every total computable fair F has some CR\MLR preimage of each prescribed CR\MLR output; every output computable martingale remains bounded there.

Failure B: Multiple distinct-looking observations F_i=Q_i∘F do not overcome this when each Q_i preserves CR. One non-MLR CR preimage of a fixed CR non-MLR output through F survives the ENTIRE family; for computable fair output homeomorphisms their vulnerability sets coincide exactly.

Lesson: source-side partition incompatibility is necessary for any universal finite pair, not sufficient; output relabelling is inadequate even when the original observer already has global two-fibre width. Avoid the quantifier error ∀F∃x_F => ∃x∀F. The genuine R₂=MLR versus MLR⊊R₂ problem remains. Existing prior-art observation of non-universality of one sequence-set strategy in SRC-0071's inspected preprint is respected; no novelty/prior-art claim. All guards intact.
