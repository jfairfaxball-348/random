# P1-S008 Close — Pseudorandomness, resource-bounded randomness and derandomization boundary

Date: 2026-10-04  
Status: **COMPLETED**  
Incoming checkpoint: `c0be7714c9a1d424575dd026a47b02c7a78b6044`

## Incoming authority and scope

Live `main` was pinned before substantive work and matched the expected incoming checkpoint exactly. `P1-S008` was unique in the incoming session ledger. Phase 1 was OPEN; Phases 2–5 were CLOSED; Gate 1 was CLOSED / NOT READY FOR REVIEW.

The incoming `authoritative/START_HERE.md` lagged the more specific `authoritative/STATE.json` and `authoritative/SESSION_LEDGER.md` by one session: it still named P1-S006 while the committed state/ledger correctly recorded P1-S007. The mismatch was reconciled without changing authorization and is recorded as FL-017.

## Bounded objective completed

P1-S008 consolidated COV-0016 only to the boundary depth required by the Fairfax-Ball catalogue. It did not become a general cryptography, complexity-theory or derandomization survey.

The session established the following object/resource distinctions:
- computational pseudorandomness is distributional: indexed probability ensembles on finite strings are judged relative to bounded statistical distinguishers/adversaries;
- a pseudorandom generator is a deterministic P-time stretching map on finite seeds; with a uniformly random seed it induces an output distribution that is compared with the uniform output ensemble;
- neither computational indistinguishability nor PRG output-distribution pseudorandomness is identified with Martin-Löf, Schnorr or computable randomness of an individual infinite sequence;
- Lutz-style Δ-randomness is again an individual infinite-sequence property, but its measure/tests/martingales retain an explicit complexity resource; for the polynomial-time specialization in SRC-0051, `p=p1`;
- complexity-theoretic languages enter the resource-bounded framework through characteristic sequences, which are a different object type from finite-string probability ensembles;
- derandomization is recorded only as the problem of replacing/simulating random choices in computation using generators that fool a stated bounded class, not as another unbounded individual-sequence randomness predicate.

No implication between p-randomness/resource-bounded randomness and the already catalogued unbounded randomness hierarchy was inferred.

## Primary-source changes

Added:
- `SRC-0048` — Andrew Chi-Chih Yao (1982), *Theory and Applications of Trapdoor Functions (Extended Abstract)*. Statement inspection recovered the explicit single-sequence-versus-pseudorandom-generation distinction, polynomial statistical tests and the source's perfect-source characterization.
- `SRC-0049` — Håstad–Impagliazzo–Levin–Luby (1999), *A Pseudorandom Generator from any One-way Function*. Statement inspection supplied exact probability-ensemble, computational-indistinguishability and P-time stretching PRG formulations.
- `SRC-0050` — Nisan–Wigderson (1994), *Hardness vs. Randomness*. Used only for the minimum hardness-versus-randomness / deterministic-simulation vocabulary; internal statement inspection used the authors' corresponding FOCS extended abstract, with journal metadata separately verified.
- `SRC-0051` — Jack H. Lutz (1992), *Almost Everywhere High Nonuniform Complexity*. Statement inspection supplied exact resource-class, Δ-randomness, martingale-success and Δ-randomness/martingale characterization statements.

## Stable records added

Added definitions `DEF-0046`–`DEF-0049`, theorems `THM-0049`–`THM-0050`, and relations `REL-0042`–`REL-0043`.

The principal catalogue split is:
- `DEF-0046` / `DEF-0047`: finite-string probability ensembles, bounded distinguishers and PRGs;
- `DEF-0048` / `DEF-0049`: individual infinite sequences, resource-bounded measure and Δ-computable martingales.

`THM-0050` records only the inspected equivalence: an infinite sequence is Δ-random iff no Δ-computable martingale succeeds on it. The resource parameter is substantive and is not dropped.

## Coverage and gate state

Catalogue close counts:
- 51 sources
- 49 definitions
- 50 theorem/characterization records
- 43 relations
- 1 status-sensitive question
- 58 author-navigation records
- 19 coverage records

Coverage: **0/19 complete** — 15 partial, 2 started-core, 1 started-edge, 1 navigation-only, 0 not-started.

`COV-0016` is now `PARTIAL_P1_S008`. It is no longer a not-started stratum, but it is not marked complete. Phase 1 remains OPEN; Gate 1 remains CLOSED / NOT READY FOR REVIEW; Phases 2–5 remain CLOSED.

## Retrieval failures / lessons

- `FL-015`: computational-pseudorandomness sources required mixed publisher/proceedings/author-hosted access routes; the inspected artefact and bibliographic publication are separately recorded.
- `FL-016`: “pseudorandom sequence” is a terminology collision between distributional pseudorandomness and Lutz-style resource-bounded individual-sequence randomness; the catalogue preserves the object/resource distinction.
- `FL-017`: the stale START_HERE session pointer was corrected while preserving the more specific committed STATE/session-ledger authority.

No inaccessible original or formulation gap was filled from a secondary summary.

## Validation

PASS before this close-record commit:
- all catalogue/state JSON parses;
- stable-ID syntax and uniqueness pass;
- catalogue count/list agreement passes;
- cross-file stable-ID references have zero unresolved references;
- `COV-0016` is exactly `PARTIAL_P1_S008`, covered by `SRC-0048`–`SRC-0051`;
- `DEF-0020` is byte-for-byte unchanged from the incoming checkpoint;
- authoritative coverage counts agree with the computed 19-record coverage plan;
- Phase 1 is OPEN, Phases 2–5 are CLOSED, and Gate 1 is `CLOSED_NOT_READY_FOR_REVIEW`;
- the incoming-to-pre-close diff touches only authoritative/catalogue/failure-ledger files and no `phase2/`, `phase3/`, `phase4/` or `phase5/` path.

The exact outgoing `main` hash is verified after this close-record write because a committed file cannot contain the hash of the commit that contains itself.

## Exclusions

No Fairfax-Ball candidate definition or selection; no Phase-2 research-target selection; no dedicated novelty audit; no original mathematics or proof search beyond understanding published statements; no resource-bounded-dimension survey; no general cryptography or derandomization survey; no Lean/Palomar work; no manuscript/publication preparation; no external outreach.

## Next recommended bounded session

`P1-S009`: primary-source consolidation of `COV-0011` higher randomness, because it remains the only navigation-only stratum and Gate 1 still explicitly lacks higher-randomness definitions/separations.

No P1-S009 work was begun in this session.
