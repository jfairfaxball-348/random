# P4-S070 — global coded-hole robustness: blockwise linear amplification theorem

Date: 2026-10-08
Incoming pinned remote main: 32b4fce1400cf5f38d23732bc24d32d71bb213ca
Scope: Phase 4 Mathematics ONLY, owner-directed strategic pivot after S069
Disposition: **VALIDATED GLOBAL EQUIVALENCE REDUCING H-PRESERVATION TO COMPUTABLY SELECTED TWO-COORDINATE XOR SHEARS; NEITHER H-PRESERVATION NOR NONPRESERVATION DECIDED**

## 0. Authority and unchanged definitions

The pinned remote main agreed exactly with the requested post-S069 strategic-pivot checkpoint. The tree contained P4-S001–S069 mathematics/close/validation records and no P4-S070 record. The selected P3-S007 CAND-01, P3-S008 Gate-3 PASS, both post-S031 and post-S069 pivots, all P4-S001–S069 mathematics, and current governance/ledger files were inspected, with emphasis on S008/S011/S012/S027/S032/S033/S039–S044/S052–S057/S065–S069. No previous mathematical assertion or object is revised.

Retain, with the exact previously committed meanings,
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Here OH consists of computably random sources whose images are computably random under every total computable adaptive no-repeat scan omitting at most one raw coordinate on **every** transcript. The class R_2 tests all total computable fair-coin-preserving global-fibre-at-most-two maps; OH^{iso} tests OH after **every** computable fair-coin-preserving homeomorphism. By S033, OH is invariant under computable signed coordinate permutations, and R_2 is invariant under all computable fair-coin-preserving homeomorphisms.

Fix exactly the committed block matrix, over the field with two elements:
\[
A=\begin{pmatrix}1&0&1\\1&1&0\\1&1&1\end{pmatrix},\qquad
H(x)\upharpoonright B_b=A(x\upharpoonright B_b),
\quad B_b=\{3b,3b+1,3b+2\}.
\]
The unchanged S011/S027 self-avoiding globally use-clipped M, computably random Y, and X=H^{-1}(Y) are preserved. X is computably random and H(X)=Y is NOT in OH. X in OH is not decided.

## 1. New globally quantified algebraic normal form

For each computable (decidable) set of block indices E subseteq natural numbers, let Q_E be the signed coordinate permutation which **swaps raw positions 3b+1 and 3b+2** for b in E and fixes all other coordinates. Thus Q_E is a computable fair-coin homeomorphism, and S033 proves that it preserves OH in both directions.

Define the block-supported XOR shear S_E by
\[
S_E(a,b,c)=
\begin{cases}
(a,b\oplus c,c),&\text{on block }B_j,\ j\in E,\\
(a,b,c),&j\notin E.
\end{cases}
\tag{1}
\]
This is an involutive, computable fair-coin-preserving homeomorphism. It is NOT in general a signed coordinate permutation, since the output middle bit mixes two raw coordinates.

**Lemma 1 (exact supported-shear conjugation).** On all of Cantor space, for every computable E,
\[
\boxed{S_E=H^{-1}\circ Q_E\circ H.}\tag{2}
\]
Moreover H has finite order seven: H^7=id and H^{-1}=H^6.

**Proof.** In one block put
\[
Q=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix},
\quad A^{-1}=\begin{pmatrix}1&1&1\\1&0&1\\0&1&1\end{pmatrix}.
\]
Direct binary matrix multiplication gives
\[
A^{-1}QA=\begin{pmatrix}1&0&0\\0&1&1\\0&0&1\end{pmatrix}=:E_{12}.
\]
On a block outside E, Q_E is the identity and hence so is A^{-1}I A; on a block inside E the action is E_{12}. This proves (2) uniformly for arbitrary computable E. Direct multiplication gives A^7=I, hence the two order identities on the infinite block product. No extraction, inverse-limit approximation, or pointwise convergence is used. QED.

Let \(\mathcal L_3\) be the group of **all computable blockwise invertible binary linear recodings**: choose a uniformly computable sequence \((L_b)_{b\in\mathbb N}\) in \(GL(3,\mathbb F_2)\), and define \(L(x)\upharpoonright B_b=L_b(x\upharpoonright B_b)\). Every such L is a computable fair-coin-preserving homeomorphism with computable inverse.

**Lemma 2 (effective finite-generator closure).** Each L in \(\mathcal L_3\) is a finite composition of (i) computable block-dependent coordinate permutations and (ii) computably supported shears of the form (1), conjugated by computable block-dependent coordinate permutations. The **number of global composition stages can be bounded independently of b and of L**.

**Proof.** Over \(\mathbb F_2\), Gaussian elimination reduces every invertible 3-by-3 matrix to the identity using row swaps and elementary row additions \(E_{ij}=I+e_i e_j^T\), i neq j. Every E_{ij} is a conjugate of E_{12} by a permutation matrix. There are only
\[
|GL(3,\mathbb F_2)|=(2^3-1)(2^3-2)(2^3-2^2)=168
\]
possible matrices. Fix a canonical finite row-reduction word for each; their lengths have a common finite maximum N. For an arbitrary computable b-to-L_b assignment, its canonical word is computable from b; pad shorter words by identities to length N. At each of the N slots, partition the blocks computably according to the finitely many possible elementary operations, apply that operation on its decidable block subset and identity elsewhere, and compose the finitely many supported actions. The selected coordinate permutations are S033-safe; each supported row-addition is a conjugate of S_E. This gives a finite global computable decomposition of L. QED.

## 2. Global theorem and exact implications

Write (H-pres) for
\[
(\forall z\in CR)\ [z\in OH\ \Longrightarrow\ H(z)\in OH].
\]

**Theorem 3 (global blockwise linear amplification).** The following are equivalent:

(A) (H-pres).

(B) For **every computable set E** and every z in OH, S_E(z) belongs to OH.

(C) For **every L in \(\mathcal L_3\)** and every z in OH, L(z) belongs to OH.

(D) OH is invariant under the entire group \(\mathcal L_3\).

**Proof.** Assume (A). Because H^7=id, repeated application of (A) shows invariance of OH under H and H^{-1}=H^6; every intermediate source is computably random because computable fair-coin homeomorphisms preserve CR by S001. For every computable E, Q_E preserves OH by S033. Equation (2) therefore makes S_E a composition of three OH-preserving operations. This proves (B). By Lemma 2 and S033, (B) gives (C). Inverses of elements of \(\mathcal L_3\) lie in the same group, so (C) implies the two-sided invariance (D). Finally H itself belongs to \(\mathcal L_3\), and (D) implies (A). QED.

Define the new structural intermediate class only as notation, not a selected randomness definition:
\[
OH^{lin3}=\{z\in CR:(\forall L\in\mathcal L_3)\ L(z)\in OH\}.
\]
Then
\[
R_2\subseteq OH^{iso}\subseteq OH^{lin3}\subseteq OH,
\tag{3}
\]
and the theorem yields the **exact equivalence**
\[
\boxed{(H\text{-pres})\quad\Longleftrightarrow\quad OH^{lin3}=OH
\quad\Longleftrightarrow\quad
(\forall \text{ computable }E)\ S_E[OH]\subseteq OH.}
\tag{4}
\]
This does not assert that any of the inclusions in (3) is strict.

**Corollary 4 (witness localization, existential not algorithmic).** If (H-pres) fails, then there exist a computable E and a source w in OH with S_E(w) not in OH. Conversely, any such supported-shear counterexample implies failure of (H-pres) and hence R_2 is a **proper** subclass of OH. The witness w in the shear reduction need not be X or the original counterexample to H-pres.

**Proof.** If every S_E preserved OH, Theorem 3 would force (H-pres). This proves existence by contraposition; alternatively expand H into the finite supported-shear/permutation word in Lemma 2 and select the first step at which OH fails. Conversely (H-pres) implies preservation of every S_E, so its failure is incompatible with such a w. Since R_2 is invariant under every computable fair-coin homeomorphism and is included in OH (S033), a source w with S_E(w) outside OH cannot belong to R_2. As w is in OH, R_2 is properly included in OH. No effective first-failure recognition is asserted: OH membership is not decidable. QED.

**Corollary 5 (conditional classification of the committed witness).** If ANY of the equivalent conditions of Theorem 3 is proved, the established Y=H(X) notin OH gives X notin OH. This would not establish R_2=OH. If instead a supported-shear counterexample is found, it establishes R_2 proper-subset OH but does not determine whether X belongs to OH.

## 3. Why the simplification remains a genuine global one-hole question

For the shear on one block, y=(a,b xor c,c), so its inverse is x=(y_0,y_1 xor y_2,y_2). A virtual unit omission of y_2 therefore corresponds to the raw difference vector (0,1,1), which requires **two** unqueried raw coordinates for exact simultaneous compatibility. A virtual omission of y_0 or y_1 has raw Hamming cost one. Thus even the reduced two-coordinate shear retains a coded-hole obstruction: an exact virtual y_2 sentinel is not a legal raw one-hole sentinel. Inverting the shear or moving to another block does not itself create a legal total globally one-hole raw observer.

This is a **map-information statement**, not a theorem that the same raw source cannot be destroyed by some other total one-hole scan. The divergence-only S039–S044 Case C still prevents treating failure to see a positive sibling refutation as computable negative information. Any same-source winning scan must emit infinitely many real output bits, query without repetition, and leave at most one permanent hole on EVERY branch. One cannot protect a second indefinitely fresh sentinel while waiting for an unbounded partial computation. These inherited obstructions are unchanged.

The new theorem is global rather than a repeated local certificate/deadline law: it universally quantifies over all computable block selections E and all OH sources, then amplifies to all computable GL(3,2)-valued block maps. It replaces the algebraically complicated three-bit H test by an **equivalent** family of two-bit shears, but neither supplies a scan/martingale compiler nor constructs a new OH witness.

## 4. Boundaries, validation and next mathematical task

The following tempting inferences are invalid:
- S033's impossibility of literal factorization of D composed with H is not same-source nonpreservation.
- Showing a virtual shear sentinel needs two raw holes is NOT evidence that a source is in OH; another legal raw scan may succeed.
- A counterexample to the abstract matrix-class criterion requires a COMPUTABLY RANDOM source IN OH; finite sibling configurations, Case-C divergence patterns, or measure-typical CR sources alone do not provide it.
- The group \(\mathcal L_3\) is much smaller than the group of arbitrary computable fair-coin homeomorphisms; invariance under H or \(\mathcal L_3\) would not prove OH^{iso}=OH or R_2=OH^{iso}.
- The equivalence does not determine the answer for any particular z, especially the exceptional committed X; none of the S057–S069 actual-X clock/hazard problems is reactivated.

Validation: the matrix identities A^7=I, A^6 A=I, A^{-1} Q A=E_{12}, and generation of all 168 matrices by two adjacent coordinate swaps and E_{12} were independently checked by finite exact binary matrix enumeration; the proof above also gives a standalone Gaussian-elimination argument. Every quantifier is global and computable-set-relative, not relative to an oracle z. No material gap has been found in the algebraic equivalence.

**P4-S071 bounded target:** test preservation/nonpreservation of OH under the involutive supported shears S_E, starting with a completely explicit computable E (such as all or alternating blocks) and a legal one-hole scan/martingale transfer or a genuine CR-in-OH counterexample. The Case-C partiality/no-two-holes problem must be handled globally, not hidden in finite certificates. Keep R_2=OH^{iso} secondary and separate.

All validated P4-S001–S069 mathematics, the committed Y/M/H/X, and the exact success-gated S057 controller (four paired clipped traces, prospective deadlines, real filler steps, timeouts releasing t/u at ZERO and sweeping non-s WITHOUT resetting old s, fair total no-repeat one-hole fibres, one ZERO and seven 8/7 terminal outcomes) remain frozen. PA-0001=UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker NONE.
