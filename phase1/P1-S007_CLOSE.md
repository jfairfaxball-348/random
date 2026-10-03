# P1-S007 Close — Finite strings, left-c.e. reals and Ω

Date: 2026-10-03  
Status: **COMPLETED**  
Incoming checkpoint: `173af3fe90eb6dc1cbddf20eab9e17ee7c9cd713`

## Bounded objective completed

P1-S007 consolidated COV-0015 at statement-level primary-source depth while preserving the repository's object and convention boundaries.

The session:
- kept finite binary strings distinct from infinite binary sequences and from real numbers represented in base two;
- strengthened the primary self-delimiting-complexity link without creating a standalone finite-string notion of infinite-sequence randomness;
- normalized historical “recursively enumerable real” to the modern alias “left-c.e. real” while keeping the source terminology visible;
- separated halting probabilities of arbitrary prefix-free/self-delimiting machines from Chaitin Ω-numbers of universal machines;
- preserved binary-expansion ambiguity/convention data;
- recorded that universal-machine Ω is left-c.e. and Martin-Löf random;
- recorded the exact characterization that Martin-Löf-random left-c.e. reals are precisely the Ω-numbers;
- made no transfer from generalized-measure, relative/oracle, stronger-test or category results.

## Primary-source changes

Added:
- `SRC-0045` — Chaitin (1975), *A Theory of Program Size Formally Identical to Information Theory*.
- `SRC-0046` — Calude–Hertling–Khoussainov–Wang (2001), *Recursively Enumerable Reals and Chaitin Ω Numbers*.
- `SRC-0047` — Kučera–Slaman (2001), *Randomness and Recursive Enumerability*.

The Chaitin source is statement-inspected through its collected-paper reprint with IBM/DOI bibliographic cross-checking. SRC-0004 remains at its actual ABSTRACT_INSPECTED level; FL-002's 1966/1969 near-title distinction is preserved.

## Stable records added / strengthened

Added definitions `DEF-0042`–`DEF-0045`, theorems `THM-0045`–`THM-0048`, and relations `REL-0038`–`REL-0041`. Existing `DEF-0002`, `DEF-0011` and `THM-0001` gained statement-level support/cautions where the newly inspected primary paper explicitly supports them.

The principal distinction is:

- left-c.e. real ↔ halting probability of **some** prefix-free machine (`THM-0047`);
- Martin-Löf-random left-c.e. real ↔ halting probability of a **universal** prefix-free machine / Ω-number (`THM-0048`).

## Coverage and gate state

Catalogue close counts:
- 47 sources
- 45 definitions
- 48 theorems/characterizations
- 41 relations
- 1 status-sensitive question
- 51 authors
- 19 coverage records

Coverage: **0/19 complete** — 14 partial, 2 started-core, 1 started-edge, 1 navigation-only, 1 not-started.

`COV-0015` is `PARTIAL_P1_S007`. `COV-0006` and `COV-0018` are refreshed through P1-S007. Phase 1 remains OPEN; Gate 1 remains CLOSED / NOT READY FOR REVIEW; Phases 2–5 remain CLOSED.

## Retrieval failures / lessons

- `FL-013`: Chaitin statement inspection used a collected-paper reprint after exact DOI/journal cross-checking; near-title provenance is kept explicit.
- `FL-014`: historical r.e.-real versus modern left-c.e. terminology, universality of Ω, and real/binary-sequence representation are kept separate.
- The Solovay manuscript cited by the inspected papers was not independently statement-inspected and is not reconstructed from secondary citation trails.

## Validation

PASS before commit:
- JSON parsing: all modified catalogue/state JSON valid.
- Stable-ID syntax and uniqueness: PASS.
- Catalogue count and ID-list agreement: PASS.
- Cross-file stable-ID references: zero unresolved references.
- Phase/gate invariants: Phase 1 OPEN; Phases 2–5 CLOSED; Gate 1 NOT READY FOR REVIEW.
- P1-S007 uniqueness: confirmed against incoming committed state before work.

## Exclusions

No Fairfax-Ball candidate definition or selection; no Phase-2 target selection; no dedicated novelty audit; no original mathematics/proof search; no Lean/Palomar; no manuscript/publication preparation; no external outreach.

## Next recommended bounded session

`P1-S008`: COV-0016 boundary consolidation — pseudorandomness, resource-bounded randomness and derandomization — using a small primary-source corpus sufficient to establish exact object/resource distinctions and vocabulary without turning Phase 1 into a general complexity-theory survey.

No P1-S008 work was begun in this session.
