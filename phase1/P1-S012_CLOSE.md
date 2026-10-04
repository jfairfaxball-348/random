# P1-S012 Close — Lowness notions and bases for randomness

Date: 2026-10-04  
Status: **COMPLETED**  
Incoming checkpoint: `f008ba90648b31d99eb7476dea984562fc849d0b`

## Incoming authority and scope

Live `main` was pinned before substantive work and matched the expected incoming checkpoint exactly. `P1-S012` was unused in the committed session ledger. Phase 1 was OPEN; Phases 2–5 were CLOSED; Gate 1 was CLOSED / NOT READY FOR REVIEW.

The bounded objective was COV-0009: consolidate the principal lowness/base equivalences needed to connect existing Martin-Löf, prefix-free-complexity and ordinary-relativization records, without opening a general computability-theory, degree-theory, traceability, cost-function or oracle-randomness survey.

## Bounded objective completed

P1-S012 establishes and separates the following source-grounded layers:

- **Low for Martin-Löf randomness:** A is low iff every unrelativized Martin-Löf random remains Martin-Löf random relative to A; equivalently SRC-0009 writes `MLR^A=MLR`.
- **K-triviality:** one constant b satisfies `K(A↾n)≤K(n)+b` for every n, using prefix-free K.
- **Low for K:** one constant c satisfies `K^A(σ)≥K(σ)-c` for every finite string σ.
- **Principal coincidence:** statement-inspected Nies 2005 gives the two directions needed for low-MLR ↔ low-K and K-trivial ↔ low-K, yielding the established low-MLR ↔ low-K ↔ K-trivial package without collapsing the definitions.
- **Base for randomness:** for a relativizable notion R, B is a base iff some Z≥_T B is R-random relative to B. Statement-inspected Hirschfeldt-Nies-Stephan 2007 establishes the base-for-1-randomness/K-trivial characterization.
- **Bounded contrast only:** Nies's theorem that every oracle low for computable randomness is computable was inspected but not expanded into a separate computable/Schnorr-lowness survey.

No closure in Turing degrees, cost-function theorem, traceability characterization or jump characterization was promoted.

## Source and stable-record changes

Sources remain 59. `SRC-0009` is upgraded from `ABSTRACT_INSPECTED` to `STATEMENT_INSPECTED` only for material actually inspected. `SRC-0010` is re-indexed with precise definition/theorem pointers. `SRC-0021` remains `ABSTRACT_INSPECTED` after failed internal-text retrieval.

Added definition: `DEF-0063` (low for prefix-free K).

Added theorem/characterization records:
- `THM-0069`: K-triviality iff low for K.
- `THM-0070`: low for Martin-Löf randomness iff low for K.

Updated `THM-0003` and `THM-0004` from their previous weaker pointers to exact statement-inspected primary support.

Added relations:
- `REL-0058`: low for K ↔ K-trivial.
- `REL-0059`: low for Martin-Löf randomness ↔ low for K.

No status-sensitive question was added or modified. No new author record was required; existing author-navigation topics were refined.

## Coverage and gate state

Catalogue close counts:

- 59 sources
- 63 definitions
- 70 theorem/characterization records
- 59 relations
- 1 status-sensitive question
- 66 author-navigation records
- 19 coverage records

Coverage: **0/19 complete** — 19 partial, 0 started-core, 0 started-edge, 0 navigation-only, 0 not-started.

`COV-0009` is now `PARTIAL_P1_S012`. All 19 strata being partial does **not** constitute Phase-1 completion or Gate-1 readiness.

Phase 1 remains OPEN; Gate 1 remains CLOSED / NOT READY FOR REVIEW; Phases 2–5 remain CLOSED.

## Retrieval failures / lessons

- `FL-027`: the principal low-MLR/K-trivial slogan is replaced by exact statement-level definition/theorem records, while distinct quantifier/resource structures are preserved.
- `FL-028`: Kučera-Terwijn 1999 remains internally uninspected; Cambridge did not expose usable full text and the ILLC archive route returned an unsupported gzip payload. No theorem syntax was reconstructed from secondary/later summaries.
- Publication identity is kept distinct from the copy actually inspected for SRC-0009 and SRC-0010.

## Validation

PASS before advancing `main`:

- all modified catalogue/state JSON parses;
- stable-ID syntax and uniqueness pass;
- catalogue count/list agreement passes;
- structured stable-ID references resolve;
- `COV-0009` is exactly `PARTIAL_P1_S012`;
- generic coverage counts equal 19 partial = 19 total;
- `DEF-0020` is byte-for-byte unchanged as a JSON record from the incoming checkpoint;
- generalized-measure records DEF-0005/DEF-0033 and P1-S011 DEF-0060/DEF-0061/DEF-0062 are unchanged;
- Phase 1 is OPEN, Phases 2–5 are CLOSED, Gate 1 is `CLOSED_NOT_READY_FOR_REVIEW`;
- no Phase-2/3/4/5 work or state transition is introduced.

The exact outgoing `main` hash is verified after this close-record write because a committed file cannot contain the hash of the commit that contains itself.

## Exclusions

No Fairfax-Ball candidate definition or selection; no Phase-2 research-target selection; no dedicated novelty audit; no general computability/degree/traceability/cost-function survey; no original mathematics or proof search beyond understanding published statements; no Lean/Palomar; no manuscript/publication preparation; no external outreach.

## Next recommended bounded session

`P1-S013`: a bounded Phase-1 completion/source-gap audit against Gate-1 criteria. Audit the 19 partial strata, provenance/access gaps, cross-cutting theorem graph and catalogue integrity to determine which gaps are gate-relevant and what bounded remediation remains. Do not automatically deepen any already-partial stratum and do not begin Phase 2.

No P1-S013 work was begun in this session.
