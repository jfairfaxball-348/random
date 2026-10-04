# P1-S010 Close — Probability and ergodic-theory interfaces

Date: 2026-10-04  
Status: **COMPLETED**  
Incoming checkpoint: `20c8bda3b5b1f4f3be7a6f531aaf1e29b58e3dd0`

## Incoming authority and scope

Live `main` was pinned before substantive work and matched the expected incoming checkpoint exactly. `P1-S010` was unused in the committed repository. Phase 1 was OPEN; Phases 2–5 were CLOSED; Gate 1 was CLOSED / NOT READY FOR REVIEW.

The bounded objective was COV-0014 only: exact primary-source interfaces among computable probability, effective measure-preserving dynamics, Birkhoff typicality/convergence and already-catalogued individual randomness notions. No general ergodic-theory, dynamical-systems, probability or computable-analysis survey was opened.

## Bounded objective completed

P1-S010 establishes and separates the following primary-source regimes:

- **Schnorr / computable probability spaces:** Gács-Hoyrup-Rojas's principal characterization is corrected to its exact atomless hypothesis. T-typicality, polynomial effective mixing and independence are separately normalized.
- **Martin-Löf / computable Cantor measures:** V'yugin proves Birkhoff convergence for computable measure-preserving transformations and computable observables at every random point; ergodicity is additionally needed to identify the limit with the expectation.
- **Martin-Löf / effective ergodic observables and general spaces:** Bienvenu-Day-Hoyrup-Mezhirov-Shen give effective recurrence and Birkhoff results for effectively open/closed sets and lower semicomputable observables, then explicitly extend them to computable probability spaces with μ-layerwise computable, measure-preserving, ergodic transformations.
- **Martin-Löf and weak 2 / nonergodic fair-coin systems:** Franklin-Towsner distinguish weak Birkhoff convergence from equality to the integral, give the fair-coin converse characterization of Martin-Löf randomness for computable measure-preserving transformations/computable observables, and prove weak 2-randomness suffices for lower semicomputable-observable convergence.

No classical almost-everywhere result is promoted into an effective randomness characterization without an inspected primary theorem. No generalized-measure theorem is silently reduced to fair coin, and no fair-coin result is generalized by analogy.

## Source and stable-record changes

Added sources: `SRC-0056`–`SRC-0058`.  
Added definitions: `DEF-0056`–`DEF-0059`.  
Added theorem/characterization records: `THM-0058`–`THM-0064`.  
Added relations: `REL-0050`–`REL-0054`.  
Added authors: `AUT-0061`–`AUT-0064`.

Updated `SRC-0012`, `THM-0006` and `REL-0006` to preserve the atomlessness and generalized-space hypotheses that were previously too coarse.

`DEF-0020` is unchanged.

No status-sensitive question was added.

## Coverage and gate state

Catalogue close counts:

- 58 sources
- 59 definitions
- 64 theorem/characterization records
- 54 relations
- 1 status-sensitive question
- 64 author-navigation records
- 19 coverage records

Coverage: **0/19 complete** — 17 partial, 2 started-core, 0 started-edge, 0 navigation-only, 0 not-started.

`COV-0014` is now `PARTIAL_P1_S010`. It is not marked complete. Phase 1 remains OPEN; Gate 1 remains CLOSED / NOT READY FOR REVIEW; Phases 2–5 remain CLOSED.

The two remaining non-partial strata are `COV-0003` and `COV-0009`, both STARTED_CORE.

## Retrieval failures / lessons

- `FL-022`: corrected the missing atomlessness hypothesis and generalized-Schnorr node in the pre-existing Schnorr/mixing record.
- `FL-023`: preserved the nonergodic convergence versus ergodic equality-to-expectation distinction.
- `FL-024`: preserved publication-versus-inspected-copy provenance for Franklin-Towsner and did not promote the Franklin-Greenberg-Miller-Ng theorem beyond abstract-level access.

## Validation

PASS before advancing `main`:

- all modified catalogue/state JSON parses;
- stable-ID syntax and uniqueness pass;
- catalogue count/list agreement passes;
- stable-ID references in modified structured records resolve;
- `COV-0014` is exactly `PARTIAL_P1_S010`;
- `DEF-0020` is byte-for-byte unchanged as a JSON record from the incoming checkpoint;
- authoritative coverage counts equal 17 partial + 2 started-core = 19 total;
- Phase 1 is OPEN, Phases 2–5 are CLOSED, Gate 1 is `CLOSED_NOT_READY_FOR_REVIEW`;
- no Phase-2/3/4/5 work or state transition is introduced.

The exact outgoing `main` hash is verified after this close-record write because a committed file cannot contain the hash of the commit that contains itself.

## Exclusions

No Fairfax-Ball candidate definition or selection; no Phase-2 research-target selection; no dedicated novelty audit; no original mathematics or proof search beyond understanding published statements; no general ergodic/dynamical/computable-analysis survey; no Lean/Palomar work; no manuscript/publication preparation; no external outreach.

## Next recommended bounded session

`P1-S011`: primary-source consolidation of `COV-0003` (foundational Martin-Löf randomness). After P1-S010 the only non-partial strata are COV-0003 and COV-0009 at STARTED_CORE; the foundational Martin-Löf stratum is the higher-value dependency for the catalogue-wide definition/theorem/relation graph.

No P1-S011 work was begun in this session.
