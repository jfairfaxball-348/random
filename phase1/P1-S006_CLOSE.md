# P1-S006 Close — Effective category and genericity

Date: 2026-10-03

## Authority and scope

Incoming live `main` was pinned at `6078ad22f18d214938ae6c0b4fd49cb605909c63`, exactly matching the expected checkpoint. Repository search found no prior `P1-S006` session record, so the session identifier was unique. Phase 1 was OPEN and Phases 2–5 remained CLOSED throughout.

This session was limited to COV-0019: effective category/meagreness, the principal computability-theoretic genericity notions needed to separate weak/1/higher levels, and exact inspected comparison links to already catalogued randomness notions. No candidate invention or selection, Phase-2 research-target selection, dedicated novelty audit, original mathematics/proof search, Lean/Palomar work, manuscript/publication preparation or external outreach was performed.

## Primary-source consolidation

- `SRC-0039` records Jockusch's 1980 *Degrees of Generic Sets* as the foundational n-genericity provenance anchor at `METADATA_ONLY`. The chapter was not upgraded beyond material actually inspected.
- `SRC-0040` records Kurtz's 1983 *Notions of weak genericity* at `ABSTRACT_INSPECTED` from the publisher extract. The extract confirms the weak-n-generic classes and their interleaving hierarchy, but exact internal statements were not reconstructed.
- `SRC-0041` (Stephan–Yu) was statement-inspected for the direct weak-1-generic/Kurtz comparison.
- `SRC-0042` (Kuyper–Terwijn) was visually and textually statement-inspected for the Cantor-space 1-generic definition and the `Pi^0_1`-boundary characterization.
- `SRC-0043` (Brendle–Brooke-Taylor–Ng–Nies) was visually and textually statement-inspected for effective `F_sigma` meagreness and its weak-1-generic avoidance formulation, as well as its explicit warning that meagre/null correspondences are analogy rather than identity.
- `SRC-0044` (Csima–Downey–Greenberg–Hirschfeldt–Miller) was visually and textually statement-inspected for exact n-generic/weak-n-generic syntax and the strict interleaving hierarchy.
- Existing `SRC-0031` was re-inspected only to confirm its separate 1-generic/weak-1-generic terminology; the general oracle/relative-randomness survey was not reopened.

## Definitions and theorem graph

Added `DEF-0037`–`DEF-0041`:

- effective meagreness on Cantor space;
- weak 1-genericity;
- 1-genericity;
- weak n-genericity;
- n-genericity.

Added `THM-0041`–`THM-0044`:

- the `Pi^0_1)-boundary characterization of 1-genericity;
- the strict interleaving `n-generic ⊋ weakly (n+1)-generic ⊋ (n+1)-generic`;
- the strict implication weakly 1-generic → Kurtz-random;
- weak 1-genericity as avoidance of all effectively meagre sets.

Added `REL-0034`–`REL-0037`. The category-to-measure comparison is deliberately only the exact source-stated weak-1-generic → Kurtz-random edge. No Martin-Löf, Schnorr, higher weak-randomness, generalized-measure or stronger-test result was transferred by analogy.

## Convention discipline

Effective meagreness is topological/category smallness: containment in an effective `F_sigma` union of uniformly `Pi^0_1` nowhere-dense classes. It has no probability-measure condition.

Weak 1-genericity meets every globally dense c.e. set of strings. The inspected 1-generic definition instead uses c.e. sets dense along the given real, equivalently avoidance of `Pi^0_1` boundaries. These quantifier patterns were not collapsed.

Weakly n-genericity and weak n-randomness remain different hierarchies despite the shared adjective. `DEF-0014`, `DEF-0015` and `DEF-0020` are unchanged. No new oracle-genericity normalization was introduced.

## Retrieval and correction lessons

`FL-011` records the category/null and weak-generic/weak-random convention collision and the rule that cross-framework edges require exact source statements.

`FL-012` records that Jockusch 1980, Kurtz 1983 and the already catalogued Kurtz 1981 thesis remain partly inaccessible at statement level. Exact definitions are therefore grounded in later statement-inspected primary papers rather than reconstructed from secondary summaries.

No inaccessible-original gap was filled by upgrading access levels beyond inspected material.

## Coverage and validation

Catalogue close counts: 44 sources; 41 definitions; 44 theorem/characterization records; 37 relation records; 1 status-sensitive question; 47 author-navigation records; 19 coverage records.

Coverage: 0/19 complete; 13 partial; 2 started-core; 1 started-edge; 1 early-navigation-only; 1 navigation-only; 1 not-started. `COV-0019` is now `PARTIAL_P1_S006`.

Validation passed on the committed catalogue state: every JSON file parsed; stable IDs were unique and syntactically valid; catalogue counts and ID sets matched the record files; and cross-file stable-ID scanning found zero unresolved references. Pre-existing definition-record ordering differs from the sorted catalogue index, but the ID sets agree exactly.

## Programme state

Phase 1 remains OPEN. Gate 1 remains CLOSED / NOT READY FOR REVIEW. Phases 2–5 remain CLOSED. No owner/external blocker exists.

Recommended next bounded session: `P1-S007`, primary-source consolidation of `COV-0015` (finite strings, random reals, left-c.e. reals and Ω), prioritizing exact object/domain distinctions and source-backed Chaitin/Ω/left-c.e.-random equivalences without reopening generalized-measure, oracle or stronger-test surveys.

The exact outgoing remote `main` hash is reported after this close record and all synchronization writes are committed and remote `main` is re-read.
