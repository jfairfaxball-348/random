# P2-S004 — CAND-03 formulation alignment (E3)

Date: 2026-10-04  
Session: `P2-S004`  
Incoming checkpoint: `6b5bcc046cd1bd74dda33569565d593db9ba567d`  
Scope: Phase 2 Discovery only; CAND-03 formulation alignment only  
Disposition: **RETAIN_PROVISIONAL AS AUXILIARY — SHAPE UNCHANGED; E3 RESOLVED**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly. Repository search found no P2-S004 session record; existing mentions were forward recommendations only, so P2-S004 was unique.

Gate 1 remains **PASS**. Phase 1 is **COMPLETED for gate purposes**. Phase 2 — Discovery is **OPEN**. Gate 2 is **CLOSED / NOT REVIEWED**. Phases 3–5 remain **CLOSED**. No candidate is selected and Fairfax-Ball Randomness is not defined.

This session performs only E3 for CAND-03. It does not conduct a lowness/traceability prior-art survey, search for an equivalent prior definition, prove a new implication, construct a low oracle or other witness, perform experiments or original proof work, use Lean/Palomar, prepare publication/outreach, expand CAND-01 or CAND-02, review Gate 2, open later phases or begin P2-S005.

## Candidate shape retained

CAND-03 remains an **oracle-class** direction, not a new randomness predicate on sampled sequences. Using DEF-0025, write `X∈UCR^A` when no instance at A of a globally total computable uniform martingale family succeeds on X. Every oracle instance in the family must be a valid martingale.

The working class remains

`L_u = { A∈2^N : for every X∈CR, X∈UCR^A }.`

Thus A is fixed first, then the predicate quantifies over **every** unrelativized computably random X. No noncomputable member, degree closure or equivalence with another oracle class is assumed.

## Exact quantifier and convention comparison

| Item | Oracle/family quantifiers | Random-input quantifier | Recorded conclusion | E3 consequence |
|---|---|---|---|---|
| **CAND-03 / L_u** | Fix A; UCR^A uses DEF-0025 globally total families, valid at every oracle instance | **For every X∈CR** | asks which oracles preserve all CR inputs against the uniform-family resource | Candidate shape; universal lowness. |
| **DEF-0025 / SRC-0032 Definitions 5.1–5.2** | One total computable map Φ on the full oracle space codes a family; every oracle instance is a martingale; oracle A selects one instance | Pairwise definition for the given sequence/oracle | defines uniformly relative computable randomness | Confirms that A-only totality/validity is not the candidate convention. The global family requirement is retained unchanged. |
| **THM-0024 / SRC-0032 Theorem 5.3** | Two fixed reals A,B; each half is uniformly CR relative to the other | Pairwise mutual condition tied to A⊕B | A⊕B is CR iff both mutual uniform-relative conditions hold | A pairwise join characterization is not a universal lowness theorem over all X∈CR. |
| **THM-0025 / SRC-0032 Corollary 5.4** | Existentially chooses A,B | One pair witnesses a separation | some A is uniformly CR relative to B but not ordinarily CR relative to B | Does not provide any noncomputable oracle in L_u and does not answer the universal preservation clause. |
| **DEF-0007; THM-0003/THM-0069/THM-0070** | Fix oracle A under ordinary ML relativization | Universal preservation of unrelativized ML-random reals | ML lowness coincides with K-triviality/low-K under recorded hypotheses | Useful quantifier model only; labels/equivalences are not transferred to uniform CR. |
| **DEF-0009 / THM-0004** | Fix B but require existence of some Z≥_T B random relative to B | **Existential** witness Z | bases for 1-randomness are K-trivial | Baseness is not lowness by definition; existential syntax cannot replace CAND-03's universal clause. |
| **SRC-0009 Theorem 5.7** | Ordinary computable-randomness lowness | Universal ordinary-CR preservation | every oracle low for ordinary CR is computable | Retained only as a contrast. Its ordinary A-computable-martingale resource is not silently substituted for DEF-0025's global-family resource. |

## Evidence and access

The catalogue was used first and was sufficient. No source passage required reopening.

DEF-0025 and SRC-0032 already record the total-family/all-instance-validity convention at statement level; THM-0024 and THM-0025 already record their exact pairwise quantifiers. DEF-0007, DEF-0008, DEF-0063, DEF-0009 and THM-0003/THM-0069/THM-0070/THM-0004 preserve the relevant lowness/base distinctions. SRC-0009's source record explicitly contains the inspected Theorem 5.7 contrast. No source access level changes, new source, citation chase, equivalent-definition search or broader lowness survey occurred.

DEF-0020 and all Phase-1 evidence/convention guards remain untouched.

## Independent value criterion

E3 also requires a value criterion that does not assume a noncomputable low oracle exists. CAND-03 is worth future promotion only if later authorized work can produce an **intrinsic computability-theoretic characterization of L_u independent of merely restating its universal preservation definition**, together with a concrete consequence for randomness, products or oracle information.

Retire the direction if later evidence shows it is simply an established lowness class with no additional explanatory consequence, routinely collapses to ordinary computable lowness, or yields no meaningful randomness consequence. These are falsifiers/criteria, not claims that any outcome holds.

## Disposition

**Retain CAND-03 provisionally as an auxiliary direction, unchanged. Resolve E3.**

Reason: the exact recorded anchors preserve all three distinctions on which the candidate depends: global all-oracle family totality versus A-only procedures; pairwise relative randomness versus universal lowness over every CR input; and universal lowness versus existential baseness. None of the recorded theorems already states the CAND-03 lowness characterization.

This is a formulation finding only. It is **not** evidence that L_u is novel, open in the literature, nontrivial, contains a noncomputable oracle, equals K-triviality, or collapses to the computable oracles.

## Stopping point

CAND-01 remains provisionally retained with E1 resolved and is not expanded here. CAND-02 remains provisionally retained with E2 resolved and is not expanded here. CAND-04–CAND-06 remain rejected exactly as recorded. All three formulation tasks E1–E3 are now resolved. No final candidate is selected. Gate 2 remains not reviewed.
