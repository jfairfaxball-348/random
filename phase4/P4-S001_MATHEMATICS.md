# P4-S001 — k=1 injective base case

Date: 2026-10-05
Session: P4-S001
Incoming checkpoint: d451cf0c65b9a508b8215ade9916c09fa239f7ad
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=1 injective base case
Result: **K1 FORCES EFFECTIVE ISOMORPHISM; COMPUTABLE RANDOMNESS IS PRESERVED**

## Authority, uniqueness and scope

Live main matched the incoming checkpoint exactly before substantive work. Repository code search returned no committed P4-S001 result, work, close or validation record, and the incoming session ledger contained no P4-S001 heading. Existing P4-S001 mentions were forward scheduling only. The session identifier was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 guard is preserved as a historical pre-Phase-4 fact: before this session, no computable-randomness consequence of the bare global finite-cardinality fibre bound had been established by the programme.

This session addresses only k=1. It does not claim any result for k>=2, general finite multiplicity, novelty, openness or publishability.

## Exact k=1 hypotheses

Let lambda be fair-coin measure on Cantor space. Let F:2^omega -> 2^omega be an everywhere-total computable Cantor self-map satisfying fair-coin preservation and one-point fibres. The latter is exactly injectivity. No inverse, selector, inverse branch or fibre enumeration is assumed.

## New mathematics

### Lemma 1 — effective uniform forward use

For every requested output length m, a finite input use u_F(m) can be computed from a Type-2 program for the everywhere-total computable map F such that agreement of x and z on their first u_F(m) bits implies agreement of F(x) and F(z) on their first m bits.

**Proof.** Search for a finite oracle-use bound u and stage at which all length-u binary oracle-answer strings make the machine produce m output bits without querying outside u. Totality on compact Cantor space gives a finite subcover of local uses, so this search halts. ∎

### Lemma 2 — fair-coin preservation upgrades injectivity to surjectivity

F is onto.

**Proof.** F is continuous, so its compact range is closed. If y were outside the range, some basic cylinder [tau] containing y would miss the range. Then F^{-1}([tau]) is empty, contradicting fair-coin preservation because lambda([tau])>0. ∎

### Lemma 3 — the inverse is computable, with a computable map-dependent use modulus

Let G=F^{-1}. Then G is everywhere-total computable. For each input-prefix length n one can effectively find an output-prefix length m_F(n) determining the first n bits of G(y).

**Proof.** For each sigma of length n, let K_sigma=F([sigma]). Injectivity makes these finitely many compact sets pairwise disjoint. For candidate output length m, Lemma 1 lets us compute exactly the finite set S_{sigma,m} of m-bit output prefixes attained on [sigma]. Pairwise disjoint compact K_sigma are separated by some finite output level, so eventually the finite sets S_{sigma,m} are pairwise disjoint; search for the first such m. Surjectivity then guarantees that each y-prefix of this length belongs to exactly one S_{sigma,m}, yielding the first n bits of G(y). ∎

The construction is uniform in a program for F in the semantic sense that the same effective procedure yields a correct total inverse program for every index that in fact denotes a valid k=1 map. No decision procedure for recognizing valid indices is claimed.

### Lemma 4 — the inverse is also fair-coin preserving

Since F is a homeomorphism, F(A) is Borel for Borel A. For G=F^{-1}, G^{-1}(A)=F(A), and preservation for F gives lambda(F(A))=lambda(A). Thus G also preserves fair coin. ∎

### Theorem — k=1 collapses to the effective-isomorphism regime

Every map in F_1 is an everywhere computable fair-coin-preserving homeomorphism whose inverse is also everywhere computable and fair-coin preserving. Conversely, every computable fair-coin-preserving homeomorphism belongs to F_1.

## Literature dependency and randomness consequence

The only literature theorem used for the randomness conclusion is the already-catalogued, statement-inspected **SRC-0015 / THM-0038**, which gives computable-randomness invariance under a.e.-computable measure-preserving inverse pairs.

The new lemmas establish stronger hypotheses here: F and G are everywhere computable, measure preserving and inverse everywhere. Therefore THM-0038 applies.

**Corollary.** If x is computably random and F is in F_1, then F(x) is computably random. In fact computable randomness is invariant in both directions under F.

Hence the k=1 part of CAND-01 does not produce a stricter robustness class than ordinary computable randomness.

## What is forced, and what is not

Forced at k=1: surjectivity; unique inverse points; an everywhere-total computable inverse; a computable map-dependent inverse-use modulus; inverse fair-coin preservation; and computable-randomness invariance.

There is no map-independent fixed inverse-use bound. For each j, let F_j swap coordinates 0 and j and fix the rest. Each F_j lies in F_1. Recovering the first input bit requires output coordinate j, so coordinate permutations make the inverse use arbitrarily large across the class.

No stronger complexity bound is claimed.

## Failed / abandoned approaches

1. Direct martingale transport was abandoned because it risks silently assuming effective control of image cylinders; the structural inverse theorem is stronger and lets THM-0038 handle preservation.
2. An attempted noncomputable-inverse counterexample fails because compactness plus injectivity makes finite image-cylinder separation effectively searchable.
3. Pure measure-theoretic a.e.-inverse reasoning is weaker than the exact situation: total continuity makes the range closed and fair-coin preservation forces onto-ness everywhere.

## Guards and stopping point

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No novelty or openness claim is made.
- The Gate-3 statement that finite multiplicity had no established computable-randomness consequence **before Phase 4** is preserved. P4-S001 is the first programme mathematics establishing such a consequence, only for k=1.
- No result is claimed for k>=2 or general finite multiplicity.
- DEF-0020 and all source/convention guards are unchanged.
- Catalogue source/definition/theorem/relation records are unchanged.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.

The smallest next question is the first genuinely non-injective case k=2: whether any effective finite-valued inverse information is forced.
