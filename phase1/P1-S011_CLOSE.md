# P1-S011 Close — Foundational Martin-Löf randomness and effective null tests

Date: 2026-10-04  
Status: **COMPLETED**  
Incoming checkpoint: `5af1bf425a4f85d5029d964d850a2d1218d1e93d`

## Incoming authority and scope

Live `main` was pinned before substantive work and matched the expected incoming checkpoint exactly. `P1-S011` was unused in the committed repository. Phase 1 was OPEN; Phases 2–5 were CLOSED; Gate 1 was CLOSED / NOT READY FOR REVIEW.

The bounded objective was COV-0003 only: foundational Martin-Löf randomness and effective null tests at primary-source depth, including the original 1966 formulation, universal tests, ordinary Solovay tests, one principal c.e.-martingale characterization, and the minimum complexity cross-check needed to connect the existing incompressibility record without reopening COV-0005/COV-0006 as general surveys.

## Bounded objective completed

P1-S011 establishes and separates the following source-grounded layers:

- **Original fair-coin formulation:** Martin-Löf 1966 uses r.e. nested, extension-closed sequential critical regions with the fair-coin counting bound. A universal sequential test exists and dominates every other test after a test-dependent additive shift of the significance index.
- **Infinite-sequence definition:** relative to a universal sequential test, an infinite binary sequence is random exactly when its critical level is finite. The definition is independent of the chosen universal test.
- **Constructive-null reformulation:** the universal test induces nested constructively open levels of measure at most `2^-m`; the nonrandoms are their intersection and form a maximal constructive null set containing every constructive null set.
- **Original generalized distribution section:** Martin-Löf separately treats arbitrary computable sequential probability distributions. Its test bound is strict because `<` for computable reals is effectively recognizable while `≤` need not be. This historical construction is not substituted for the modern generalized records DEF-0005/DEF-0033.
- **Ordinary Solovay tests:** a later statement-inspected primary paper gives the exact computable-string / finite-Kraft-sum / finite-prefix-hit formulation and states equivalence with Martin-Löf randomness.
- **c.e. martingales:** the same primary paper gives the exact lower-semicomputable martingale convention and success by capital tending to infinity, again characterizing Martin-Löf randomness.
- **Complexity guard:** THM-0001 remains the prefix-free/self-delimiting initial-segment characterization. Martin-Löf's 1966 conditional plain-complexity finite-string formula is recorded as historical source detail and is not conflated with it.

No Schnorr, Kurtz, relative, stronger-test, generalized-measure, category, Ω, pseudorandomness, higher-randomness or effective-ergodic theorem was generalized or reopened by analogy.

## Source and stable-record changes

Added source: `SRC-0059`.  
Upgraded source: `SRC-0001` from `ABSTRACT_INSPECTED` to `STATEMENT_INSPECTED` only for actually inspected material.

Added definitions: `DEF-0060`–`DEF-0062`.  
Added theorem/characterization records: `THM-0065`–`THM-0068`.  
Added relations: `REL-0055`–`REL-0057`.  
Added authors: `AUT-0065`–`AUT-0066`.

Updated `DEF-0002` and `THM-0001` only to attach the newly inspected foundational evidence and convention guards. Updated COV-0018 only because the new COV-0003 characterization edges directly extend the cross-cutting graph.

`DEF-0020` is unchanged.

No status-sensitive question was added or modified.

## Coverage and gate state

Catalogue close counts:

- 59 sources
- 62 definitions
- 68 theorem/characterization records
- 57 relations
- 1 status-sensitive question
- 66 author-navigation records
- 19 coverage records

Coverage: **0/19 complete** — 18 partial, 1 started-core, 0 started-edge, 0 navigation-only, 0 not-started.

`COV-0003` is now `PARTIAL_P1_S011`. It is not marked complete. `COV-0009` is the sole remaining STARTED_CORE stratum.

Phase 1 remains OPEN; Gate 1 remains CLOSED / NOT READY FOR REVIEW; Phases 2–5 remain CLOSED.

## Retrieval failures / lessons

- `FL-025`: the 1966 original is now statement-inspected, but its nested sequential syntax, arbitrary-computable-distribution strict inequality and conditional-plain-complexity notation are preserved instead of rewritten as modern conventions.
- `FL-026`: the Solovay 1975 draft remains uninspected, and Schnorr 1973 internal statements were not reliably retrieved in this bounded pass. Exact promoted Solovay/martingale formulations therefore come from later statement-inspected primary SRC-0059, without claiming direct original-source wording or priority.
- Published bibliographic identity is kept distinct from the copy actually inspected for both SRC-0001 and SRC-0059.

## Validation

PASS before advancing `main`:

- all modified catalogue/state JSON parses;
- stable-ID syntax and uniqueness pass;
- catalogue count/list agreement passes;
- stable-ID references in structured records resolve;
- `COV-0003` is exactly `PARTIAL_P1_S011`;
- generic coverage counts equal 18 partial + 1 started-core = 19 total;
- `DEF-0020` is byte-for-byte unchanged as a JSON record from the incoming checkpoint;
- existing generalized-measure definitions DEF-0005 and DEF-0033 remain unchanged;
- Phase 1 is OPEN, Phases 2–5 are CLOSED, Gate 1 is `CLOSED_NOT_READY_FOR_REVIEW`;
- no Phase-2/3/4/5 work or state transition is introduced.

The exact outgoing `main` hash is verified after this close-record write because a committed file cannot contain the hash of the commit that contains itself.

## Exclusions

No Fairfax-Ball candidate definition or selection; no Phase-2 research-target selection; no dedicated novelty audit; no general AIT/computability/martingale/complexity/history survey; no original mathematics or proof search beyond understanding published statements; no Lean/Palomar work; no manuscript/publication preparation; no external outreach.

## Next recommended bounded session

`P1-S012`: primary-source consolidation of `COV-0009` (lowness notions and bases for randomness). It is now the sole STARTED_CORE stratum and the highest-value remaining structural dependency before a broader Phase-1 completion/source-gap audit.

No P1-S012 work was begun in this session.
