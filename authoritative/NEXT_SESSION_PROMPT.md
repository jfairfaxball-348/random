# Next Session Prompt — P4-S040

Continue the Fairfax-Ball Randomness Research Programme in https://github.com/jfairfaxball-348/random.

Run only Phase 4 — Mathematics session P4-S040. Treat committed repository state as authoritative. Pin live main at the exact P4-S039 outgoing checkpoint reported by the preceding session, reconcile any mismatch, confirm P4-S040 is unique, and read P4-S001 through P4-S039, the required CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, phase4/P4-S032_MATHEMATICS.md, phase4/P4-S033_MATHEMATICS.md, phase4/P4-S034_MATHEMATICS.md, phase4/P4-S035_MATHEMATICS.md, phase4/P4-S036_MATHEMATICS.md, phase4/P4-S037_MATHEMATICS.md, phase4/P4-S038_MATHEMATICS.md, and phase4/P4-S039_MATHEMATICS.md.

## Sustained Phase-4 target — one-hole normalization after coded recoding

Freeze all validated mathematics through P4-S039. Do not return to the P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, the P4-S037/P4-S038 backward-price route, or ambiguity mass unless the theorem below genuinely requires them.

Retain

\[
R_2=\{x\in CR:\text{every total computable fair-coin-preserving global-}k=2\text{ map sends }x\text{ to }CR\},
\]

\[
OH=\{x\in CR:\text{every total computable adaptive no-repeat one-hole scan sends }x\text{ to }CR\},
\]

and

\[
OH^{iso}=\{x\in CR:\text{every computable fair-coin-preserving homeomorphism }H\text{ sends }x\text{ into }OH\}.
\]

The current inclusions remain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Retain the repeated three-bit recoding

\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2,
\]

with

\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix}
\]

and inverse

\[
x_0=u_0\oplus u_1\oplus u_2,\qquad
x_1=u_0\oplus u_2,\qquad
x_2=u_1\oplus u_2.
\]

Let \(Y\) be the settled P4-S011 computably random wtt-autoreducible source, \(M\) its committed self-avoiding wtt autoreduction, \(D\) its one-hole destroyer, and

\[
X=H^{-1}(Y).
\]

Retain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

The missing source-side statement remains whether \(X\in OH\).

## P4-S039 boundary to retain

P4-S039 replaces the crude “coded bits mix” obstruction by an exact affine/effective boundary.

1. With one raw coordinate \(x_i\) withheld, one block is exactly

\[
u=a+hAe_i.
\]

The raw flip columns are

\[
Ae_0=(1,1,1)^T,\qquad
Ae_1=(0,1,1)^T,\qquad
Ae_2=(1,0,1)^T.
\]

Thus an \(x_0\)-hole answers no virtual row, an \(x_1\)-hole answers only \(u_0\), and an \(x_2\)-hole answers only \(u_1\).

2. Exact simulation of a virtual unit sentinel needs raw support

\[
A^{-1}e_0=(1,1,0)^T,\qquad
A^{-1}e_1=(1,0,1)^T,\qquad
A^{-1}e_2=(1,1,1)^T,
\]

so the exact raw-hole costs are \(2,2,3\). A fresh hole in another block cannot algebraically transport the old unresolved virtual bit.

3. For one virtual block \(B=\{q_0,q_1,q_2\}\), define

\[
C_B=
\{v\in\mathbb F_2^3:
M^{Y[B\leftarrow v]}(q_r)\downarrow=v_r
\text{ for all }r=0,1,2\}.
\]

The actual block belongs to \(C_B\), and syntactic autoreduction self-avoidance implies

\[
d_H(C_B)\ge2.
\]

4. For the displayed \(A\), every nonempty length-three code of minimum distance at least two fixes at least one raw coordinate after \(A^{-1}\).

More generally the exact three-bit raw-hyperplane criterion is

\[
p^TA\text{ is a unit row},\qquad A^{-1}p\ne p,
\qquad p=(1,1,1)^T.
\]

5. Two distinct enumerated members of \(C_B\) already give a finite raw-coordinate certificate:

- distance two certifies the raw parity coordinate \(x_0\);
- distance three is an antipodal pair, admits no third codeword, and certifies the agreeing raw coordinates.

Thus multiple local solutions are positively visible. The difficult completion case is a c.e. singleton.

6. For a preselected raw target \(x_i\), after the other two raw bits are known the two affine hypotheses have the exact trichotomy:

- **A — finite rejection:** the alternate hypothesis has a wrong/nonbinary finite halt; this gives a target-visible raw self-avoiding predictor;
- **B — second self-consistent endpoint:** both raw values satisfy all three local equations; the designated target remains a genuine one-bit circular pair;
- **C — divergence-only singleton:** the alternate endpoint is not self-consistent, but its failure is witnessed only by divergence, so semantic uniqueness has no finite completion certificate.

The wtt use bound does not remove B or C.

7. A positive same-source theorem is available. If the finite 24-computation local sibling family is total at every reached fresh block, then the complete \(C_B\) can be computed, and three synchronized raw one-hole scans suffice to ensure that one coordinate type is correctly wagered infinitely often. Hence local sibling totality implies

\[
X\notin OH.
\]

8. The committed P4-S011 authority does **not** establish local sibling totality or classify the alternate affine hypotheses block by block. It supplies target correctness, self-avoidance, a computable use bound, and permits sibling divergence.

9. No actual raw one-hole destroyer for \(X\) was obtained. No proof of \(X\in OH\) was obtained. Therefore no OH non-invariance or \(R_2\subsetneq OH\) conclusion is available.

## P4-S040 bounded task — online c.e. local-code extraction under one raw sentinel

Attack only the remaining source-side completion problem for the displayed recoding and the actual committed \(M\).

Do not return to ordinary raw-martingale compilation. A positive result must be an actual raw one-hole scan/stake witness on \(X\), or an exact target-visible self-avoiding stake functional from which P4-S012 yields such a witness.

### 1. Formalize raw-adjacent companions

For a raw target \(j=(B,i)\), write

\[
X^{\langle j\rangle}=X\oplus e_j.
\]

Then

\[
H(X^{\langle j\rangle})
=
Y\oplus Ae_i
\]

inside block \(B\) and agrees with \(Y\) elsewhere.

Track the three local \(M\)-computations simultaneously on the actual and companion hypotheses.

Distinguish exactly:

- finite rejection of the companion;
- local self-consistency of both endpoints;
- divergence-only failure of the companion.

Do not replace this with a generic “partial predictor” statement.

### 2. Globalize the finite-rejection arm if possible

P4-S039 Case A gives a correct raw target predictor once the alternate endpoint is finitely rejected.

Test whether there is a total computable fresh-target scheduling rule such that on the actual \(X\):

- every epoch eventually reaches finite rejection or a computably harmless zero-stake exit;
- infinitely many epochs yield nonzero correct raw wagers;
- no target bit is queried before its stake is fixed;
- every sibling transcript which stalls eventually queries every raw coordinate except its current sentinel.

If such a schedule exists, apply the P4-S012 conversion and construct the raw one-hole destroyer explicitly.

Do not assume a computable rejection-time bound.

### 3. Test whether the two-solution arm can hand off the sentinel

When both affine endpoints are locally self-consistent, the current raw target is not determined by the three equations.

But the pair may certify a different raw coordinate.

Test whether that positive certificate can be used **prospectively**, not retroactively:

- can the current sentinel be closed at zero stake while a still-unread certified raw coordinate becomes the next sentinel;
- can one reserve a prospective block long enough to see two codewords without creating a complete transcript with more than one omitted raw coordinate;
- can a two-block or finite-window baton pass keep exactly one eventual hole on every branch;
- can a finite family of scans with different target-coordinate policies guarantee that one of them wins by pigeonhole without assuming negative singleton information.

If no such handoff is possible, state the exact no-handoff invariant.

### 4. Attack divergence-only singleton completion directly

Case C is the sharpest surviving effectivity problem.

The actual candidate is eventually positively visible, but there may be no finite evidence that the alternate candidate will never become self-consistent.

Test source-side mechanisms which do not require deciding that negative fact:

- races between actual and alternate acceptance;
- finite families of waiting policies;
- dovetailed prospective targets;
- zero-stake abandonment followed by a fresh sentinel;
- use of additional \(M(n)\) computations outside the current block when their finite behaviour can reject the companion;
- any exact c.e. certification which remains target-self-avoiding.

Do not revive backward-price averaging or horizon mixtures merely under a new name.

### 5. Enlarge the consistency test beyond the three local equations only when finite

A raw companion \(X\oplus e_j\) changes two or three virtual bits. The same \(M\) may reveal inconsistency at inputs outside the block whose computations query those changed bits.

Test whether a computably finite closure of affected \(M\)-computations can reject a raw-adjacent companion while still avoiding \(x_j\).

If finite closure is not available, identify why. Do not silently quantify over infinitely many oracle computations and then claim a finite target-visible predictor.

### 6. Use the wtt use bound correctly

The use bound supplies a computable finite **oracle-coordinate** frontier for every fixed \(M(n)\).

It does not supply a halting-time bound.

When constructing a raw predictor, separate:

- finite source-value acquisition;
- c.e. observation of halts;
- negative claims of divergence.

Any step relying on “all relevant sibling computations have finished” must justify why completion is positively visible.

### 7. Test a finite-family / pigeonhole theorem

OH failure requires only one scan, not a uniform selector naming the successful scan in advance.

Exploit this existential freedom carefully.

For example, test whether finitely many scans corresponding to the three local raw coordinates and finitely many waiting/handoff policies can be arranged so that on every actual block one member progresses and, over infinitely many blocks, at least one fixed scan receives infinitely many certified correct wagers.

A valid theorem must ensure that each individual scan remains total and globally one-hole on **all** transcripts, including the branches on which its local search never completes.

### 8. If a raw destroyer emerges, verify the full global map

Do not stop at a local predictor.

Prove that the resulting raw scan is:

- total computable;
- adaptive and no-repeat;
- fair-coin preserving;
- globally one-hole on every complete transcript;
- target-exhaustive on the actual \(X\) when required;
- coupled to a computable output martingale that succeeds on the transcript of \(X\).

Then conclude only

\[
X\notin OH.
\]

This eliminates the current source as an OH non-invariance candidate but does not prove \(R_2=OH\).

### 9. If the online extraction fails, prove the narrowest exact obstruction

A negative result must be stronger than “the second solution might arrive late”.

Candidate structural outcomes include:

- every globally one-hole target protocol must eventually precommit to a raw coordinate before it can know which coordinate the c.e. code fixes;
- a raw-adjacent self-consistent companion can make the two target values observationally identical to every finite equation-based test avoiding the target;
- divergence-only singleton completion produces a genuine noncompactness / no-finite-certificate obstruction for any finite handoff protocol;
- any attempt to reserve multiple prospective target coordinates creates a branch with two or more permanent raw holes;
- or another exact online invariant derived from the committed \(M\).

Do not infer \(X\in OH\) from failure of this compiler.

### 10. Preserve the source-side separation guard

An OH non-invariance theorem still requires

\[
X\in OH,\qquad H(X)=Y\notin OH.
\]

Only the second statement is settled.

If P4-S040 constructs a raw one-hole destroyer on \(X\), the present source is eliminated as a separation candidate.

If it proves only that the current local-code extraction schemes fail, \(X\in OH\) remains unproved.

### 11. Required session outcome

The output should be one of:

- a total raw one-hole destroyer for the actual recoded P4-S011 source \(X\);
- a same-source extraction theorem turning a materially weaker condition than full local sibling totality into a raw one-hole destroyer;
- a rigorous online c.e.-code / raw-adjacent-companion obstruction for the actual tested mechanisms;
- or, only if it follows directly, a genuine proof that \(X\in OH\).

The sustained question remains

\[
R_2=OH\;?
\]

If no OH non-invariance witness is proved, preserve \(OH^{iso}\) as the comparison class and state separation status explicitly.

P4-S032 null-ambiguity preservation remains available. Do not return to ambiguity mass as an invariant.

Preserve PA-0001 as **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 unchanged. Make no novelty, openness, prior-art, Gate-4, publication or outreach claim. Continue original mathematics only.

Record, validate and synchronize useful work, commit it, verify remote main, report the exact outgoing hash, and provide the next prompt if no blocker exists.
