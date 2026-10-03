# P1-S005 Close — Computable measures and computable probability spaces

Date: 2026-10-03

## Authority and scope

Incoming live `main` was pinned at `10b6dbc073a15dbd7387488798dd7e77cc8a1510`, exactly matching the expected checkpoint. P1-S005 was unique and Phase 1 was OPEN. Phases 2–5 remained CLOSED throughout.

This session was limited to the computable-measure / computable-probability-space stratum and the exact invariance, conservation and no-randomness-from-nothing links needed for COV-0001, COV-0012 and COV-0013. No candidate invention, Phase-2 selection, novelty audit, original mathematics, Lean/Palomar, publication work or outreach was performed.

## Primary-source consolidation

- `SRC-0011` (Hoyrup–Rojas) now carries statement-level pointers for computable metric spaces and canonical fast-Cauchy representations, computable Borel probability measures and valuation criteria, binary representations, uniform integral tests, morphism conservation and isomorphism invariance for Martin-Löf random points.
- `SRC-0012` (Gács–Hoyrup–Rojas) was upgraded from ABSTRACT_INSPECTED to STATEMENT_INSPECTED for computable probability spaces, morphisms/isomorphisms, generalized Martin-Löf/Schnorr tests, Cantor representation, atomless computable-Lebesgue spaces and Schnorr conservation.
- `SRC-0015` (Rute) was upgraded from ABSTRACT_INSPECTED to STATEMENT_INSPECTED for computable-measure Cantor-space randomness, μ-a.e.-computable maps, computable-randomness NRFN/isomorphism invariance, Schnorr NRFN failure, and the separate all-computable-measure versus fair-coin Martin-Löf maximality theorems.
- `SRC-0038` (Bienvenu–Gács–Hoyrup–Rojas–Shen) was added at STATEMENT_INSPECTED for computable Cantor measures, Martin-Löf P-tests, explicit Bernoulli/non-symmetric-coin class tests, arbitrary-measure uniform tests and fixed-P uniformization.

## Definitions and theorem graph

Added `DEF-0030`–`DEF-0036` for the computable metric/probability-space machinery, generalized Martin-Löf/Schnorr randomness, effective measure-preserving morphisms/isomorphisms, and μ-computable randomness on Cantor space. `DEF-0005` and `DEF-0006` were corrected/strengthened rather than treated as fair-coin templates.

Added `THM-0032`–`THM-0040` and `REL-0026`–`REL-0033`. The key scope distinctions are:

- every computable probability space has a Cantor representation with an **appropriate computable measure**, not automatically fair coin;
- the stronger fixed nonatomic/Lebesgue isomorphism requires **atomlessness**;
- Martin-Löf and Schnorr randomness are conserved by the inspected computable-probability-space morphisms;
- computable randomness satisfies no-randomness-from-nothing for the inspected a.e.-computable Cantor-space map class and is invariant under the corresponding measure isomorphisms;
- Schnorr randomness fails no-randomness-from-nothing for that broader a.e.-computable Cantor-space class even though the inspected computable-probability-space morphism result gives Schnorr conservation;
- fair-coin Martin-Löf maximality and all-computable-Cantor-measure Martin-Löf maximality are separate source statements.

P1-S004 Demuth/difference/balanced/Oberwolfach records remain fair-coin-only. P1-S003 ordinary versus uniform oracle relativization remains unchanged. Rute's uniform-relativized extension is a conjecture in the inspected paper and was not promoted to a theorem.

## Retrieval and terminology corrections

`FL-008` records the Cantor-measure versus fair-coin/isomorphism correction. `FL-009` records the collision between measure-parameter uniform tests and uniform oracle relativization. `FL-010` records that the earliest standalone Shen provenance for Martin-Löf no-randomness-from-nothing was not independently recovered, although exact modern primary statements were inspected.

No arbitrary represented-space theorem beyond the inspected computable-metric-space frameworks was inferred by analogy. Atoms and non-full support are not excluded from the basic computable probability-space machinery; atomlessness/support hypotheses are stated only where the inspected theorem uses them.

## Coverage and validation

Catalogue close counts: 38 sources; 36 definitions; 40 theorems; 33 relations; 1 question; 42 authors; 19 coverage records.

Coverage: 0/19 complete; 12 partial; 2 started-core; 1 started-edge; 1 early-navigation-only; 1 navigation-only; 2 not-started. COV-0001, COV-0012, COV-0013 and COV-0018 are now `PARTIAL_P1_S005`.

Validation passed: every JSON file parsed; stable IDs were unique and syntactically valid; catalogue counts and ID lists matched the record files; cross-file stable-ID scanning found zero unresolved references.

## Programme state

Phase 1 remains OPEN. Gate 1 remains CLOSED / NOT READY FOR REVIEW. Phases 2–5 remain CLOSED. No owner/external blocker exists.

Recommended next bounded session: `P1-S006`, primary-source consolidation of effective category/genericity (COV-0019), with exact effective-meagreness/genericity definitions and only inspected comparison links to measure-based randomness.

The exact outgoing remote `main` hash is reported after this close record and all synchronization writes are committed and remote `main` is re-read.
