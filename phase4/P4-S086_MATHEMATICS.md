# P4-S086 — Universal width-two filtrations or a genuinely R₂ non-MLR survivor

Date: 2026-10-10. Scope: Phase 4 mathematics ONLY; selected CAND-01.
Incoming independently pinned live GitHub main: 453439b56f4bcf44b8539974969f0bed1a59773f, exactly the P4-S085 outgoing commit.
P4-S086 mathematics, validation and close records and branch were absent on entry. Phase 4 OPEN, Gate 3 PASS.

**Disposition: GLOBAL IMPOSSIBILITY THEOREM FOR A SINGLE FAIR OBSERVER AND EVERY RANK-ONE CR-PRESERVING POSTPROCESSING FAMILY. R₂ versus MLR REMAINS UNRESOLVED.**
This is not a proof of a universal width-two pair, nor a global R₂ survivor, and is strictly different from S085's reformulation and entropy bound.

## 0. Authority, proof dependencies, and frozen results

Read cumulative P4-S001–S085 session/gate/decision/failure history, S085 mathematics/validation/closeout, S003–S008, S011/S012, S032/S033, S081–S084, selected CAND-01, post-S031 pivot and post-S069 strategic pivot. No prior claim is revoked. The proof below relies on three *already catalogued* statements:

- **THM-0002**, strict MLR ⊊ CR (SRC-0007 STATEMENT_INSPECTED; SRC-0028 STATEMENT_INSPECTED). S082 independently furnishes CR\MLR witnesses.
- **THM-0007**, computable-randomness *no randomness from nothing*, specialized to total computable fair Cantor maps (SRC-0015, STATEMENT_INSPECTED, Theorem 7). This means: if F_*λ=λ, then for **each** λ-computably random output y there is a λ-computably random input x with F(x)=y. No computable inverse selector is claimed.
- **THM-0035**, conservation of Martin-Löf randomness under total computable fair maps (SRC-0011, STATEMENT_INSPECTED). **THM-0038** (SRC-0015, STATEMENT_INSPECTED, Lemma 8) additionally makes every computable fair measure isomorphism CR-preserving in both directions.

The special access levels remain: SRC-0019 and SRC-0060 STATEMENT_INSPECTED; SRC-0069 STATEMENT_INSPECTED (preprint, Section 2 proof already read in S082); SRC-0070 and SRC-0072 ABSTRACT_INSPECTED; SRC-0071 STATEMENT_INSPECTED (preprint with previously recorded internal proof checks), 2021 journal version METADATA_ONLY. R_tot=MLR remains the programme deduction from the SRC-0071 preprint; no fresh journal or external access is implied.

Freeze, for k≥2, MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR, R₂⊊OH, MLR⊊OH, KLR⊆TKLR⊆OH. S084's predictable error stream, effective ML-null infinite-resolution locus, and balanced a.e. two-fibre map are untouched. S085's global computable c(n) width-two criterion is accepted without restatement as progress.

## 1. A global no-single-observer impossibility theorem

**Theorem 1 (strong pullback survivor; arbitrary fair maps, not only width two).**
For EVERY everywhere-total computable λ-preserving F:2^ω→2^ω and EVERY y∈CR\MLR, there exists x∈CR\MLR such that F(x)=y.

*Proof.* Fix such F and y. THM-0007 (no randomness from nothing for computable randomness) supplies x∈CR with F(x)=y, because y is CR for the computable pushforward F_*λ=λ. If x were MLR, THM-0035 would give F(x)=y∈MLR, contradiction. Thus x∈CR\MLR. The argument is global; it uses neither a source-specific almost-everywhere estimate nor a binary-fibre or inverse-sheet assumption. QED.

Note the quantifier strength: the SAME y can be chosen for every F, but **its CR non-MLR preimage x_F may depend on F**. No effective choice of x_F is asserted.

**Corollary 2 (single-filtration universalization is impossible).**
No SINGLE computable fair dyadic filtration C, regardless of its fibre cardinality, has the property that its output is non-computably random on every CR non-MLR source. Consequently it cannot catch every such source even if equipped with EVERY computable output martingale simultaneously, nor if equipped with a fixed finite/countable family of output computable martingales.

*Proof.* Its induced total fair map F=T_C satisfies Theorem 1. Choose x∈CR\MLR with F(x)∈CR. All total computable output martingales are bounded on F(x), contradicting any such covering property. This applies in particular to every globally width-two dyadic filtration from S085. QED.

This is a **non-tautological global impossibility theorem**, based on two independent conservation/nothing-from-nothing directions, not on a fibre count or a finite-depth toy example. It excludes *every* proposed one-observer universal strategy, including an observer with adaptive capital, provided winning means failure of ordinary output computable randomness. The existing SRC-0071 preprint introduction already observes the non-universality of one sequence-set strategy; this proof supplies a calibrated CR\MLR input formulation and does not claim novelty.

## 2. A global rank-one family obstruction

Call a family (F_i)_{i∈I} a **CR-preserving output-factor family** when there is ONE everywhere-total computable λ-preserving F and maps Q_i such that F_i=Q_i∘F, with Q_i(y)∈CR for every y∈CR. To remain Route-A candidates the F_i themselves must be total computable fair maps with global ≤2 fibres; the theorem does not need those extra restrictions. The index set I can be arbitrary: the argument is pointwise, with no effective index selection.

**Theorem 3 (simultaneous non-MLR CR survivor for any rank-one family).**
For every CR-preserving output-factor family there is ONE x∈CR\MLR such that F_i(x)∈CR for ALL i∈I. In particular, NO SUCH FAMILY can be universal against CR\MLR, even if it is countably infinite or has arbitrarily many computable output martingales per observer.

*Proof.* Fix any y∈CR\MLR. Theorem 1 applied once to the common F gives x∈CR\MLR with F(x)=y. For every i simultaneously, F_i(x)=Q_i(y)∈CR by the assumed forward CR preservation. Hence no output martingale succeeds on any F_i(x). QED.

**Corollary 4 (arbitrary fair output homeomorphic recodings collapse to one vulnerability class).**
If F has global fibres of size ≤2 and the Q_i are arbitrary computable fair-coin-preserving homeomorphisms, each F_i=Q_i∘F is also total, fair, and globally ≤2-to-1; in fact its fibres have the same cardinalities as F's. By THM-0038, for every input x,

    F_i(x)∈CR  if and only if  F(x)∈CR.

Thus ALL these observers have exactly the SAME CR-destruction set, and by Theorem 1 this common set omits some x∈CR\MLR. Not even infinitely many output recodings of a single width-two observer provide a universal family.

*Proof.* Each Q_i is a fair effective isomorphism with computable inverse. It preserves CR in both directions by THM-0038, and its bijectivity preserves F's fibres. Apply Theorem 1. QED.

This strengthens S085's observation that output homeomorphisms cannot repair unbounded fibres: **even starting from a genuine global width-two F**, output-homeomorphic recoding and rebetting cannot turn it into a universal family. A successful finite pair would have to involve genuinely different source-side partitions/observation mechanisms, not merely two CR-preserving re-encodings of the same output. This is a *necessary design condition*, not a sufficient criterion for success.

## 3. Exact discrimination between the remaining alternatives

**Route A, R₂=MLR.** Theorems 1–3 eliminate one-map universality and all rank-one CR-preserving-output-factor families as candidate certificates. In particular choosing one global width-two C and a universal computable list of martingales on its output cannot decide R₂=MLR. This does NOT refute a pair of width-two maps whose observations are genuinely different (nor an arbitrary countable family not factoring through one CR-preserving observation). A finite universal pair remains sufficient but not known necessary.

**Route B, MLR⊊R₂.** Theorem 1 proves ∀F∈F₂ ∃x_F∈CR\MLR with F(x_F)∈CR. The definition of a genuine survivor requires ∃x∈CR\MLR ∀F∈F₂, F(x)∈CR. These quantifiers do NOT commute; choosing a fixed CR non-MLR output y does not make the varying preimages x_F agree. Therefore Theorems 1–3 are not a construction of z∈R₂\MLR. In particular no requirement for S083 T* and its homeomorphic recodings has been fulfilled for one common input. S084's infinite-resolution prediction-error condition still applies to any actual survivor.

**Substantive limitations.** Theorem 3 needs each Q_i to preserve ordinary computable randomness on EVERY CR input. A computable fair Q_i can fail this property (S011), even if Q_i has ≤2 fibres. Consequently an arbitrary pair F_0,F_1 need not admit the prohibited factorization and this argument cannot be misused to forbid general width-two pairs. No output-only entropy bound, global sheet selector, or computable uniform preimage is assumed.

Neither equality R₂=MLR nor strict inclusion MLR⊊R₂ follows. The open separate comparisons R₂ vs OH^iso, U(H), X∈OH and fixed-S preservation are untouched.

## 4. Preservation and status

Original computably random Y; syntactically self-avoiding globally use-clipped wtt M; repeated three-bit H with A=[101;110;111]; X=H⁻¹(Y); and every S001–S085 result are UNCHANGED. No S057 usage and no escrow, hazards, residues, unit columns, record-only z0 or multi-hole work. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, priority, publication or outreach inference. Owner/external blocker: NONE.

**P4-S087 target:** genuine two-observer width-two covering (or a simultaneously surviving CR non-MLR source); otherwise a strictly stronger genuinely two-observer impossibility theorem.
