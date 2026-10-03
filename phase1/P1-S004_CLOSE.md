# P1-S004 Close — Stronger test-randomness primary-source consolidation

Date: 2026-10-03

## Authority and scope

Incoming live `main` was pinned at `93390ebd21e06d26e3b9ba4d80fe5a87ddd9341a`, exactly matching the expected checkpoint. `P1-S004` was absent from the repository before work began and Phase 1 was OPEN. Phases 2–5 remained CLOSED throughout.

This session performed only the authorized stronger-randomness catalogue tranche. It did not invent or select a Fairfax-Ball candidate, perform a novelty audit, conduct original mathematics, use Lean/Palomar, draft a manuscript, prepare publication, or contact third parties.

## Source work completed

- Recovered and visually statement-inspected Osvald Demuth's original 1982 paper (SRC-0034), including the historical bounded-change and measure-control machinery.
- Upgraded SRC-0016 to statement-inspected and used it to normalize the original notation into the modern ω-c.e./weak-truth-table-∅' test-index convention without claiming a verbatim translation.
- Added statement-inspected primary SRC-0035 for difference randomness, including the exact neighborhood-based d.r.e./n-r.e. tests, the n≥2 collapse, strict stronger-randomness placement, and the Martin-Löf-plus-Turing-incomplete characterization.
- Added statement-inspected primary SRC-0036 for balanced randomness, including the O(2^m) change bound and exact-2^m normal form.
- Added statement-inspected primary SRC-0037 for Oberwolfach randomness, including coherent component changes, strict balanced/Oberwolfach/difference placement, and interval/left-c.e.-bounded equivalent forms.

## New durable records

Definitions: DEF-0026 through DEF-0029.

Theorems/characterizations: THM-0026 through THM-0031.

Relations: REL-0017 through REL-0025.

Sources: SRC-0034 through SRC-0037; SRC-0016 upgraded.

Authors: AUT-0036 through AUT-0041 plus relevant existing author indexes updated.

## Convention corrections preserved

1. Demuth randomness uses Solovay passing: membership in only finitely many final components.
2. Balanced and Oberwolfach randomness use the weak-Demuth/ordinary escape convention in the inspected sources.
3. SRC-0035's naive n-r.e. string-test hierarchy and its neighborhood/difference n-r.e. hierarchy are different; the former yields 2-randomness for n≥2 and the latter yields difference randomness for n≥2.
4. Every occurrence of 2-randomness in the new cross-links is read as the n=2 instance of DEF-0020: Martin-Löf randomness relative to ∅'.
5. All new definition/relation records are limited to the inspected fair-coin Cantor-space setting; no arbitrary-measure or oracle generalization was inferred.

## Relationship graph added

Source-inspected statements support:
- 2-random → Demuth and 2-random → weak 2, both strict;
- Demuth and weak 2 incomparable;
- Demuth → difference and weak 2 → difference, both strict;
- difference → Martin-Löf, strict;
- balanced → Oberwolfach → difference, both strict;
- balanced → difference directly, strict;
- difference random iff Martin-Löf random and Turing incomplete;
- Oberwolfach = interval-test = left-c.e.-bounded randomness in SRC-0037's normal forms.

No missing edge was supplied merely by comparing definitions.

## Retrieval limitations and lessons

FL-006 records that the Demuth original was recovered but remains subject to a Russian-language/historical-notation boundary. FL-007 records the n-r.e. terminology collision and passing-convention distinction. A Franklin-hosted PDF route failed, but the same primary paper was recovered from the coauthor site and matched to official metadata; this is not an active blocker.

## Validation and coverage

Validation PASS:
- all changed JSON parses;
- stable IDs satisfy the required prefix/4-digit syntax and are unique within record families;
- catalogue counts agree with record files;
- all stable-ID references resolve;
- no duplicate new IDs were introduced.

Close counts:
- 37 sources
- 29 definitions
- 31 theorem/characterization records
- 25 relation records
- 1 status-sensitive question
- 41 author-navigation records
- 19 coverage records

Coverage remains 0/19 complete: 4 started-core, 10 partial, 1 started-edge, 1 early-navigation-only, 1 navigation-only and 2 not-started. COV-0010 and COV-0018 remain PARTIAL_P1_S004. Gate 1 is NOT READY FOR REVIEW.

## State and next bounded task

Phase 1 remains OPEN; Phases 2–5 remain CLOSED. No owner/external blocker exists.

Recommended next session: P1-S005, a bounded primary-source consolidation of computable measures/probability spaces and generalized-measure randomness, because the committed catalogue repeatedly marks current fair-coin-only results and COV-0001/COV-0013/generalized-measure relation coverage as a consequential remaining gap.

The exact outgoing `main` hash is verified after commit and is intentionally not embedded here because a commit cannot contain its own hash.
