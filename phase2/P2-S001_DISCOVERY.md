# P2-S001 — First bounded Discovery portfolio

Date: 2026-10-04
Incoming `main`: `f82b0162efd486783bfd921f1a9d1d0a8447e358`
Scope: Phase 2 Discovery only
Outcome: **three provisional directions retained; three redundant shapes rejected**
Novelty/current literature status of retained questions: **NOT ASSESSED / UNKNOWN**

## Authority, reconciliation and method

Live `main` was checked through Git and the GitHub ref endpoint before substantive work. Both matched the expected incoming checkpoint exactly. The clone was clean at that commit. The incoming session ledger contained no P2-S001 session entry; existing mentions only recommended it. No committed Phase-2 session or CAND record existed. P2-S001 is the first and unique Discovery session.

The required authority, P1-S014 review/close, catalogue overview, all structured catalogue indexes, taxonomy, retrieval log, and existing Phase-2 scaffold/template were inspected. The detailed catalogue was read through record projections retaining mathematical statements, hypotheses, resources, cautions, access levels and source pointers, with relevant definitions and relationships inspected in full. No external literature retrieval, candidate-specific prior-art search, proof search, experiment, Lean, Palomar, manuscript work or outreach was performed. Source access descriptions below are **inherited committed evidence**, not claims that this session independently re-inspected the papers.

Incoming posture confirmed:

- Gate 1 PASS; Phase 1 COMPLETED for gate purposes; Phase 2 OPEN; Phases 3–5 CLOSED.
- No final candidate selected and no definition of Fairfax-Ball Randomness established.
- P1-S014 performed no Discovery. The library is discovery-ready, bounded and non-exhaustive.
- Residual provenance/access gaps survive the gate; abstract-level KL/dimension records and the missing exact supergale definition cannot carry decisive distinctions.
- DEF-0020 retains the finite convention: n-random means ML-random relative to the (n−1)-st jump, for n≥1. All other Phase-1 conventions are preserved.

**Stale-surface reconciliation.** README.md, STATUS.md and phase-1-research/README.md still described the P1-S003-era posture; authoritative/NEXT_SESSION_PROMPT.md still requested P1-S004; phase-2-discovery/README.md still said CLOSED. These conflict with the later committed STATE, D-0008, gate/session ledgers, START_HERE, ROADMAP and P1-S014 review. The specific later gate decision controls. Synchronizing those surfaces does not make another gate decision. No historical Phase-1 session or catalogue record is rewritten. The existing Phase-2 scaffold requires a portfolio, not immediate selection; phase2/ now holds the requested session records, with a pointer from the old scaffold directory.

**Method and claim boundary.** Compare structural mechanisms in the committed map, formulate questions, and apply already catalogued results where they exactly dispose of a shape. A missing catalogue edge is not an open-problem claim. Syntactic differences are not separation results. Prospective theorem packages are requirements for future value, not conjectures certified plausible by a proof attempt. No new implication, separation or equivalence is promoted to the Phase-1 theorem graph. CAND IDs identify working directions, including retired ones; they do not name Fairfax-Ball Randomness.

## Shared notation and evidence discipline

Unless explicitly stated otherwise, the space is Cantor space 2^N with fair-coin measure λ. CR means DEF-0004; MLR means DEF-0002; W2R means DEF-0015. A total computable map means a single oracle procedure producing every output bit for every input sequence, with no exceptional undefined inputs. This explicit total-map convention is part of the provisional shapes, not an assertion that every cited source uses it.

The main working index is [candidates.json](candidates.json). Links below are stable IDs resolving in [catalogue.json](../catalog/catalogue.json) and its detailed files. Source pointers and access qualifications remain in [sources.json](../catalog/sources.json). Retained candidates have formulation/evidence tasks, not owner blockers. None uses KL, dimension or a supergale as a decisive premise.

## CAND-01 — Computable randomness under finite-ambiguity observations

**Disposition: RETAIN_PROVISIONAL.** A question about preservation first; a named randomness notion is not the required outcome.

### Exact provisional shape

For each integer k≥1 let F_k consist of total computable maps F:2^N→2^N such that F_*λ=λ and every y has at most k preimages. The bound is global for the map, not an input-dependent finite-fibre condition. No computable inverse, effective list of preimages, or conditional-probability computation is assumed.

Define the working predicate

`R_fin(x) :⇔ x∈CR and for every k≥1 and every F∈F_k, F(x)∈CR.`

Question: **does every computably random x satisfy R_fin? If not, how can this preservation class be characterized by tests or betting resources?** The core target is the conservation question. No strictness, characterization, nontrivial witness, or difference between the k-levels is asserted. The explicit CR conjunct keeps the baseline clear.

### Motivation and catalogue anchors

This asks whether bounded ambiguity in an observation already suffices for computable randomness to behave as it does under effectively invertible observations. Counting preimages measures a concrete loss of distinguishability of inputs; it is not claimed to be a complete information-theoretic loss measure.

- DEF-0004 supplies the fair-coin computable-martingale baseline; DEF-0035 and DEF-0036 keep map and generalized-measure notions distinct.
- THM-0038 / REL-0029, from SRC-0015 Lemma 8, establish computable-randomness invariance with a.e.-computable inverse maps. They do not state a finite-fibre replacement for the inverse hypothesis.
- THM-0037 / REL-0028, from SRC-0015 Theorem 7, concern existence of random preimages. That direction must not be substituted for preservation of an arbitrary random input.
- THM-0035 / REL-0026 provide the ML conservation benchmark. THM-0008 / REL-0008 and THM-0039 / REL-0031 warn that an unrestricted largest-class conservation-plus-preimage proposal is already accounted for; see CAND-04.

### Structural comparison and prospective value

The changed resource is the observation map: bounded fibre cardinality in place of an effective inverse. The betting class remains ordinary CR. This differs in formulation from a direct test restriction and from an oracle-lowness condition. It has **not** been shown to produce a different class from CR or MLR.

A worthwhile future package would give a precise preservation theorem or an exact failure criterion for this map class; explain the role of finite ambiguity versus effective inverse information; and, only if a proper subclass arises, give a natural test/martingale characterization and supported placement. A clean preservation characterization could be valuable even if R_fin=CR, but would not justify naming a distinct randomness class.

### Collapse risks, falsifiers and dependencies

- High collapse risk: finite fibres may already permit a standard simulation/conservation argument. No attempt to prove or disprove that was made.
- A cardinal bound does not supply effective inverse branches by definition. Adding branch enumeration to make an argument work would change the candidate and could place it directly under known invariance machinery.
- Total maps and a.e.-computable maps are not interchangeable. Neither the unrestricted maximality theorem nor an a.e. counterexample decides the stated question without further evidence.
- Retire as a proposed distinct notion if it is CR, MLR or an already defined preservation class. Retire the direction entirely if the remaining theorem package is merely a routine instance of a catalogued result or the finite-ambiguity restriction has no useful explanatory role.
- Mathematical dependencies: effective measure-preserving maps, fibre representations and computable martingale resources. Expected difficulty: **high**; no constructive proof route has been assessed.
- Evidence weakness: the catalogue contains no theorem specifically evaluating bounded-fibre total maps. This is a library limitation, not evidence of novelty. Before using SRC-0015 beyond its recorded scope, check its exact map syntax and the inverse hypotheses locally; dedicated equivalent-definition searching belongs to Phase 3.

## CAND-02 — Nonergodic convergence for enumerable events

**Disposition: RETAIN_PROVISIONAL.** This is a characterization question about observational resources.

### Exact provisional shape

Let T range over total computable λ-preserving self-maps of 2^N. Let U range over effectively open subsets of 2^N, meaning unions of a computably enumerable set of cylinders. Put

`a_N(T,U,x) = (1/N) Σ_{i=0}^{N−1} 1_U(T^i(x)), for N≥1,`

and define

`B_open(x) :⇔ for every such T and U, lim_{N→∞} a_N(T,U,x) exists.`

Limits are finite, since the averages lie in [0,1]. Ergodicity, a computable value of λ(U), a convergence rate, and equality of the limit with λ(U) are **not** requirements. The question is: **which already catalogued randomness class, if any, is characterized by B_open? In particular, does this bounded observable class capture W2R, MLR, or a different class?** Those are alternatives for assessment, not an asserted sandwich or strict hierarchy.

### Motivation and catalogue anchors

An effectively open event can be positively recognized from a finite observation even when its complement cannot be decided. It is a concrete binary observable. Restricting to indicators isolates this recognition resource without introducing unbounded functions or integrability-tail conventions.

- DEF-0059 distinguishes convergence from equality to the expectation. DEF-0015 / DEF-0016 and THM-0018 / REL-0012 supply the weak-2 null-test benchmark.
- THM-0063 / REL-0052, from SRC-0058, characterize MLR by nonergodic computable Birkhoff convergence, with a computable-set witness in the converse. This already rules out merely renaming the computable-observable endpoint.
- THM-0064 / REL-0053, also SRC-0058, give the weak-2 sufficient condition for lower-semicomputable observables in the source's setting. Indicators of effectively open sets motivate a bounded observational slice; no new reverse implication is established here.
- THM-0059 and THM-0060 / REL-0050, from SRC-0057, give ML effective-set/lower-semicomputable conclusions **with ergodicity**. They do not settle the nonergodic question by dropping that hypothesis.
- THM-0006 / REL-0006 and DEF-0056 / DEF-0057, from SRC-0012, are a separate atomless Schnorr/mixing benchmark. Their effective mixing and typicality hypotheses cannot be imported into B_open.

### Structural comparison and prospective value

The varied resource is observability (decidable/computable versus positive semidecision), while the intended dynamics are nonergodic. This is distinct from CAND-01's fibre restriction and CAND-03's oracle uniformity. The catalogue's one-sided lower-semicomputable statement motivates asking for characterization at the indicator level; it does not establish that the question is unresolved in the literature.

A worthwhile future package would identify B_open exactly by effective tests, or establish a substantive obstruction to such a familiar characterization; specify the transformation representation; and explain whether the binary-event restriction loses information compared with the larger observable class. A strictness theorem would be required only if a different class is claimed. An already-known characterization or a routine restatement does not merit a new name.

### Collapse risks, falsifiers and dependencies

- High collapse/prior-definition risk: this may already be part of effective ergodic theory, or may coincide with MLR/W2R without a distinct new definition being warranted. No candidate-specific audit has been performed.
- The source convention for “computable transformation” must be matched to the explicitly **total** T here before using a converse witness from THM-0063. A theorem proved for a broader a.e.-defined class cannot simply furnish a witness in this narrower class.
- Do not assume the bounded-indicator restriction has the same characterization as all integrable lower-semicomputable functions. That is part of the question, not a source fact in the committed map.
- Retire if exact committed/source scope already characterizes this very class, or if the apparent gap is solely a total-versus-a.e. or convergence-versus-expectation mismatch. If formulation alignment requires widening T, record a versioned change instead of silently changing the quantifier.
- Dependencies: effective open events, computable measure-preserving dynamics, and effective Birkhoff statements. Expected difficulty: **high**; a converse would be substantial Phase-4 work and is not attempted.
- Evidence weakness: SRC-0058's inspected arXiv copy is not the timed-out final author PDF; theorem numbering remains copy-qualified. Its map convention is the first formulation check. The uninspected Franklin–Greenberg–Miller–Ng internals are not used. No arbitrary-measure or layerwise extension is asserted.

## CAND-03 — Oracle lowness for uniform computable randomness

**Disposition: RETAIN_PROVISIONAL as an auxiliary structural direction.** This defines a prospective **class of oracles**, not a new randomness predicate on the sampled sequence. Its relevance to the programme must be earned by a useful characterization rather than a name change.

### Exact provisional shape

Write `X∈UCR^A` for DEF-0025: no total computable uniform family of martingales has an A-instance succeeding on X. Every oracle instance in such a family must be a valid martingale; a procedure total only at A is insufficient. Define the working oracle class

`L_u = {A∈2^N : for every X∈CR, X∈UCR^A}.`

Question: **what is an intrinsic computability-theoretic characterization of L_u, and does it coincide with the computable oracles, K-triviality (DEF-0008), or another already catalogued class?** No noncomputable member, degree closure, or equivalence is asserted.

### Motivation and catalogue anchors

Uniform families constrain how an oracle can select an observer. Lowness asks whether that constrained side information can help against any ordinarily computably random input. The question tests whether a known distinction in relativization matters after universal preservation is imposed.

- DEF-0021 versus DEF-0025, THM-0025 and SRC-0032 Corollary 5.4 establish the ordinary/uniform distinction for some pairs. THM-0024 supplies the mutual-uniform product benchmark.
- DEF-0007, DEF-0008 and DEF-0063; THM-0003 / THM-0069 / THM-0070; REL-0003 / REL-0058 / REL-0059 record the ML-lowness/K-trivial/low-K coincidence. It cannot be transferred to uniform CR by replacing labels.
- SRC-0009, Theorem 5.7, is explicitly recorded at statement level in its `inspected_claims`: every oracle low for ordinary computable randomness is computable. It is used as a contrast, even though Phase 1 did not create a separate THM node for it.
- DEF-0009 / THM-0004 / REL-0004 distinguish existential bases from universal lowness. L_u uses the universal quantifier and is not a base notion.

### Structural comparison and prospective value

The mathematical object changes to the oracle A; the resource changes from arbitrary A-computable strategies to instances of globally total computable families. A pairwise uniform/ordinary separation does **not** imply that any noncomputable A lies in L_u. This is the principal quantifier trap.

A worthwhile future package would characterize L_u independently of its defining universal preservation clause, relate it to ordinary CR-lowness and the existing ML-lowness benchmarks with checked hypotheses, and explain a concrete consequence for oracle information or product randomness. Without that package the direction is auxiliary and cannot justify a randomness name. No traceability or cost-function definition is invented to fill the missing characterization.

### Collapse risks, falsifiers and dependencies

- High risk that universal quantification eliminates the pairwise distinction, or that an established lowness class already answers the question. The catalogue's omission of a uniform-lowness theorem is not a literature gap claim.
- Changing which oracle instances must be valid/total would change the predicate. Measure-parameter uniformity (DEF-0006) is a different axis and is excluded.
- Reject as a distinct programme contribution if this is an established lowness definition with its standard characterization, if it reduces routinely to ordinary computable lowness, or if no natural consequence for randomness emerges.
- Dependencies: exact DEF-0025 family coding, ordinary lowness, quantified comparison of oracle classes. Expected difficulty: **high**, with additional significance risk because the outcome concerns oracles rather than a randomness notion.
- Evidence weakness: COV-0009 deliberately did not catalogue the broader traceability/lowness landscape. That missing material is future Phase-3 exposure, not a reason to search it early. SRC-0021 remains abstract-only and is not needed for the decisive present motivation.

## CAND-04 — Largest class with unrestricted conservation and random preimages

**Disposition: REJECT_CATALOGUED_CHARACTERIZATION.**

**Exact shape.** On fair-coin Cantor space, ask for the largest set R such that every a.e.-computable λ-preserving self-map F is defined on R, maps R into R, and every y∈R has a preimage x∈R with F(x)=y. This is a class-level closure property, not a pointwise conjunction of slogans.

**Motivation/links.** Intrinsic invariance under processing and recoverability of random outputs are attractive structural axioms. However THM-0008 / REL-0008 (SRC-0015, Theorem 36) state exactly that MLR is the largest such set. DEF-0002 is the existing class. THM-0039 / REL-0031 state the separately scoped all-computable-measure analogue.

**Comparison and value.** No structural difference survives at the stated maximality level; the hoped-for characterization is already catalogued. “Largest” must not be omitted: the theorem does not say every smaller class satisfying both axioms equals MLR.

**Failure/dependencies/difficulty.** The exact known characterization is the falsifier. Access is STATEMENT_INSPECTED in the committed source record; historical earliest standalone ML-preimage provenance remains unresolved but does not weaken this rejection. No new mathematics is needed for this disposition. Restricting the map class is a different question (CAND-01), not a rescue of this exact shape.

## CAND-05 — A randomness hierarchy from additional finite differences

**Disposition: REJECT_CATALOGUED_COLLAPSE.**

**Exact shape.** For a fixed n≥3, require escape from every neighbourhood-based n-r.e. test of SRC-0035 Definition 2.3, with recursive component indices and level measures ≤2^-i, as in DEF-0027. Ask whether increasing n beyond 2 yields a distinct randomness class.

**Motivation/links.** Allowing more alternations of enumerable open information looks like a change of observational power. THM-0026 (SRC-0035, Theorem 2.8) already identifies all these levels for n≥2 with difference randomness. THM-0028 characterizes that class as ML randomness plus Turing incompleteness; REL-0020 places it above MLR.

**Comparison and value.** The hoped-for strict hierarchy is already ruled out at precisely the proposed syntax. It cannot supply a separate definition or theorem package. The paper's naive n-r.e. **string** tests instead yield 2-randomness; switching to that convention does not vindicate the original direction. DEF-0020 is not changed.

**Failure/dependencies/difficulty.** The source-stated collapse is the falsifier. STATEMENT_INSPECTED SRC-0035 suffices for rejection; no weak-access material is central. No additional proof or broader moving-test investigation is warranted by this shape.

## CAND-06 — Mutual uniform randomness of the two halves

**Disposition: REJECT_CATALOGUED_CHARACTERIZATION.**

**Exact shape.** Write X=A⊕B with even/odd interleaving and require both A∈UCR^B and B∈UCR^A, using DEF-0025. Ask whether this supplies a separate randomness class for X.

**Motivation/links.** Symmetric resistance to prediction from the other half is a natural independence-inspired formulation. THM-0024 (SRC-0032, Theorem 5.3) already states that this is exactly computable randomness of A⊕B, DEF-0004. THM-0025 explains why the uniform/ordinary distinction must nevertheless be preserved. THM-0023 and REL-0016 give separately scoped Schnorr and ML product benchmarks.

**Comparison and value.** The apparent two-sided characterization is already in the catalogue. Renaming it supplies no mathematical distinction or additional theorem package. The symmetric theorem must not be rewritten as an asymmetric one by analogy with ML.

**Failure/dependencies/difficulty.** The exact known equivalence is decisive. Its committed evidence is STATEMENT_INSPECTED. Broader oracle-relative results are unnecessary for rejecting this exact shape; no original proof is attempted. CAND-03 changes the quantified object to a lowness class and must face its own risks.

## Deferred navigation and screened-out cosmetic variations

- **KL/access-order direction: DEFERRED_BEFORE_FORMULATION.** DEF-0012, THM-0011, SRC-0018 and SRC-0019 provide abstract-level navigation only. No bounded-lookahead, query-schedule or density definition is manufactured from those abstracts. QST-0001 remains source-stated open on its recorded 2025 evidence, not a freshly verified 2026 status claim. Exact strategy/success syntax would be required before developing or distinguishing a candidate. No source upgrade was necessary for the surviving portfolio.
- **Dimension/graded-information direction: DEFERRED_BEFORE_FORMULATION.** SRC-0013/SRC-0014, THM-0009/THM-0010 and REL-0005 remain abstract-level, with no exact supergale definition. No candidate relies on a dimension-one/nonrandom separation, rate formula or supergale mechanism. A future Discovery session would need an explicitly bounded formulation upgrade before such reliance.
- **Balanced-test constant changes: SCREENED OUT AS COSMETIC.** DEF-0028 and SRC-0036 Remark 18 already normalize O(2^m), exact 2^m and fixed positive rational multiples. Merely changing that constant does not generate an additional candidate. This was a brief source-defined screen, not a seventh developed direction.

Deferred navigation is not part of the surviving portfolio and has no CAND identifier. It is neither a negative theorem nor a finding of mathematical uninterest. Unexamined category, higher-randomness, Ω and cryptographic directions are not declared exhausted.

## Comparison and bounded disposition

These are qualitative Discovery judgments, not scores measuring novelty or probabilities of success.

| ID | Mathematical motivation | Structural axis | Prospective theorem value | Collapse / redundancy risk | Expected difficulty | Disposition |
|---|---|---|---|---|---|---|
| CAND-01 | Explain stability under bounded input ambiguity | Observation-map fibres and effective inverse resources | Preservation/failure characterization; test form if justified | High; may simply preserve CR, or fall under known map theory | High; effective preimage control | Retain provisionally |
| CAND-02 | Explain convergence for positively recognizable events | Observable effectivity in nonergodic dynamics | Exact randomness characterization at bounded indicator level | High; known endpoint or map-convention artifact | High; converse/dynamical characterization | Retain provisionally |
| CAND-03 | Explain which side information helps a uniformly selected bettor | Oracle class and universal lowness quantifier | Intrinsic oracle characterization with product/information consequence | High; standard lowness class or universal-quantifier collapse | High, plus programme-relevance risk | Retain as auxiliary direction |
| CAND-04 | Conservation plus existence of random preimages | Largest class under unrestricted maps | Already THM-0008 | Realized: MLR characterization | No further work warranted | Reject |
| CAND-05 | More finite alternations in tests | Fixed finite difference depth | Already THM-0026 | Realized: difference-randomness collapse | No further work warranted | Reject |
| CAND-06 | Mutual unpredictability of two components | Two-sided uniform relativization of a join | Already THM-0024 | Realized: CR characterization | No further work warranted | Reject |

The three surviving axes are not numerical variants of the same test. That supports a bounded portfolio, not a conclusion that three different mathematical classes exist. Their motivation is sufficient for a further formulation pass, **not** for asserting novelty, literature openness, nontriviality or eventual publishability. No final candidate is selected. No Fairfax-Ball definition is established.

## Evidence tasks before further promotion

| Task | Candidate | Smallest necessary clarification | Boundary |
|---|---|---|---|
| E1 | CAND-01 | Match total maps, global finite fibres and effective inverse assumptions against the exact recorded map framework | Do not search for a finite-to-one preservation theorem or construct a witness in Phase 2 |
| E2 | CAND-02 | Match SRC-0058's computable-map convention and observable domain to the explicit total-map/indicator shape | A local formulation check only; no search for the candidate's converse or newer equivalents |
| E3 | CAND-03 | Keep globally valid total families separate from A-only totality; formulate an independent value criterion without assuming a noncomputable low oracle | No lowness/traceability prior-art survey or attempt to build such an oracle |

All three have future novelty exposure. Only Phase 3, after Gate 2 PASS, can conduct the dedicated primary-source attack. Mathematical answers require Phase 4 authorization after Gate 3. No presently needed task requires an owner decision, communication or external account action.

## Session stopping point and next task

P2-S001 stops with these six dispositioned records. It does not run Gate 2, P2-S002 or any later phase. Gate 2 remains CLOSED / NOT REVIEWED; Phases 3–5 remain CLOSED. The Phase-1 catalogue, including DEF-0020 and all access/provenance records, is unchanged.

The smallest next bounded session is **P2-S002: CAND-02 formulation alignment only (E2)**. Confirm what the committed/source transformation and observable conventions actually support, clarify the comparison questions without proving them, then retain, revise with explicit history, defer or retire CAND-02. This ordering resolves a concrete uncertainty; it is not selection of CAND-02 as the programme target. Other candidates remain recorded without being expanded. See [the next-session prompt](../authoritative/NEXT_SESSION_PROMPT.md).
