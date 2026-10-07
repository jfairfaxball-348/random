# P4-S039 validation

Date: 2026-10-07
Session: P4-S039
Incoming checkpoint: ebf18e6ef13c1a684b0164811b7a13cc2bdf576c
Scope: same-source one-hole simulation under the three-bit recoding
Status: **VALIDATED**

## Repository and scope checks

- Immediately before the first P4-S039 write, live main was exactly ebf18e6ef13c1a684b0164811b7a13cc2bdf576c, the P4-S038 outgoing checkpoint.
- No P4-S039 mathematics record existed on that checkpoint. The only P4-S039 hit was the forward prompt created by P4-S038.
- P4-S001 through P4-S038, the selected CAND-01 authority, the sustained pivot, and P4-S032 through P4-S038 were read.
- All validated mathematics through P4-S038 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling line was not reopened.
- No attempt was made to compile the actual P4-S011 win into an ordinary raw martingale on \(X\).
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. The affine one-hole formulas are exact

For

\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix},
\]

the columns are

\[
Ae_0=(1,1,1)^T,\quad
Ae_1=(0,1,1)^T,\quad
Ae_2=(1,0,1)^T.
\]

If only \(x_i\) is unresolved and \(h=x_i\), linearity gives

\[
u=a+hAe_i.
\]

Therefore:

- for \(i=0\), every virtual coordinate depends on \(h\);
- for \(i=1\), only \(u_0\) is independent of \(h\);
- for \(i=2\), only \(u_1\) is independent of \(h\).

This validates Lemma 1 and the answerable-query classification.

### 2. The exact unit-sentinel raw support costs are \(2,2,3\)

The recorded inverse equations give

\[
A^{-1}e_0=(1,1,0)^T,
\quad
A^{-1}e_1=(1,0,1)^T,
\quad
A^{-1}e_2=(1,1,1)^T.
\]

If two virtual completions differ only at \(u_r\), their raw preimages differ exactly by \(A^{-1}e_r\). Any raw coordinate on which those preimages differ must remain unread if both completions are to stay compatible with the same raw transcript.

Hence the minimum support sizes are exactly \(2,2,3\). Theorem 2 is a finite linear-algebra statement and does not infer failure of every alternative raw vulnerability process.

### 3. Cross-block pivot migration cannot carry the old ambiguity

The full source recoding is a direct block product. Raw coordinates in a different block have zero coefficient in every old-block virtual coordinate.

Thus once the old raw hole is queried, the old affine line collapses. A newly withheld raw coordinate creates a new independent affine direction in its own block. There is no linear relation by which the new hole can reintroduce uncertainty into the old virtual parity.

This validates the exact-transcript migration obstruction while preserving the distinction from vulnerability simulation.

### 4. The local consistency set really has minimum distance at least two

For one virtual block \(B=\{q_0,q_1,q_2\}\), define \(C_B\) by simultaneous correctness of the three computations \(M(q_r)\) on the finite block replacement.

Suppose \(v,w\in C_B\) differed only at coordinate \(r\).

The two candidate oracles then agree at every coordinate except \(q_r\). By the committed autoreduction convention, the input-\(q_r\) computation never queries \(q_r\). Therefore its complete oracle interaction is identical on the two candidates and it must have the same output.

Local consistency would require the two outputs to be \(v_r\) and \(w_r\), which are different. Contradiction.

Thus \(d_H(C_B)\ge2\).

The proof uses the actual self-avoiding machine \(M\), not an assumed generic predictor.

### 5. Every such code fixes a raw coordinate for the displayed matrix

A length-three binary code with minimum distance at least two has a simple classification.

If it contains an antipodal pair, no third word can be distance at least two from both endpoints. Thus it is exactly that pair. For the displayed matrix,

\[
A^{-1}(1,1,1)^T=(1,0,0)^T,
\]

so the raw pair differs only in \(x_0\), leaving \(x_1,x_2\) constant.

If the code contains no antipodal pair and has at least two words, all pair distances are two. Hence every word has the same parity. Since

\[
x_0=u_0\oplus u_1\oplus u_2,
\]

\(x_0\) is constant.

Singletons trivially fix every raw coordinate.

Theorem 5 is therefore valid.

### 6. Two enumerated local solutions already certify a coordinate

For a distance-three pair, the preceding argument proves there can be no third codeword, so the agreeing raw coordinates are final.

For a distance-two pair, any third word at distance at least two from both must have the same parity as the pair; otherwise it would be at odd distance from one endpoint, hence distance one or three, and distance three would make it antipodal to that endpoint and distance one from the other.

Thus parity, and hence raw \(x_0\), is already fixed.

No negative completion information is needed once two distinct consistent assignments are visible. The only local code-size case whose completion may require negative information is a singleton.

### 7. The general raw-hyperplane matrix criterion is exact in dimension three

Let \(p=(1,1,1)^T\).

The maximal same-parity code is the parity hyperplane

\[
p^Tu=0.
\]

Under \(u=Ax\), its pullback is

\[
p^TAx=0.
\]

This two-dimensional subspace is a raw coordinate hyperplane exactly when \(p^TA\) is a unit row.

The other irreducible code type is an antipodal pair, whose raw difference is \(A^{-1}p\). Such a pair fixes a raw coordinate exactly when this difference has at least one zero coordinate. Since \(A^{-1}p\ne0\), the unique failure is \(A^{-1}p=p\).

Therefore Proposition 8 gives both necessary and sufficient conditions.

For the displayed \(A\),

\[
p^TA=(1,0,0),
\qquad
A^{-1}p=(1,0,0)^T,
\]

so the criterion holds.

### 8. The raw-target trichotomy is exhaustive

Fix a raw target \(x_i\) and reveal the other two raw bits. There are exactly two affine hypotheses.

The actual hypothesis makes all three \(M\)-computations halt correctly.

For the alternate hypothesis:

- if any computation halts incorrectly or nonbinary, finite rejection is visible;
- if all three halt correctly, the alternate endpoint is a second member of \(C_B\);
- if neither of those happens, at least one required computation diverges.

There is no fourth case.

In the finite-rejection arm, waiting for the actual three correct halts and one alternate rejection gives a partial raw predictor which never queries \(x_i\). All oracle answers outside the target can be supplied from raw data, and same-block virtual queries are supplied from the finite hypothesis. The wtt use bound gives finite oracle use, though not a halting-time modulus.

The other two arms therefore isolate respectively algebraic one-bit circularity and c.e. singleton-completion failure.

### 9. The local-totality one-hole theorem is globally sound

Under local sibling totality, all 24 finite candidate computations halt on each reached target block, so the complete \(C_B\) becomes known after finite time.

For each local raw index \(i\), define a scan \(S^i\):

1. designate \(x_i\) in the current block as sentinel;
2. query the other two raw bits of the block;
3. enumerate fresh outside-block fillers while simulating the 24 computations;
4. if all halt, compute \(C_B\);
5. wager all capital on the sentinel only if \(C_B\) fixes raw coordinate \(i\), otherwise wager zero;
6. query the sentinel and start the next epoch.

The candidate simulations never need the sentinel: all virtual coordinates in the current block are supplied from the finite candidate assignment.

If the simulations never all halt on a non-target branch, step 3 continues forever and queries every raw coordinate except the sentinel. Hence that complete transcript has exactly one hole.

If epochs keep completing, the filler order is chosen from the least fresh coordinates outside the sentinel. The three scans can be synchronized because, after their two local filler queries, they expose the same outside-block filler sequence and run the same candidate simulations. After the sentinel is finally consumed, all three have the same queried set. Choosing the next completely fresh block above the common queried prefix preserves synchronization and makes the prefix tend to infinity.

Thus every complete transcript of every \(S^i\) omits at most one raw coordinate.

On \(X\), the actual virtual assignment belongs to \(C_B\), so every nonzero wager is correct. Every completed block fixes at least one raw coordinate. Among three indices, one is fixed on infinitely many blocks. Its scan's martingale doubles infinitely often and never loses.

Therefore Theorem 11 validly concludes \(X\notin OH\) under the stated local sibling-totality hypothesis.

### 10. The hypothesis is not licensed for the actual P4-S011 machine

P4-S011 supplies:

- target totality and correctness on \(Y\);
- syntactic self-avoidance;
- a computable wtt use bound;
- no sibling totality guarantee.

P4-S038 already exploited precisely the difference between finite value use and nondecidable future halting.

A finite wtt use bound does not imply that the 24 local perturbation computations halt. Therefore Theorem 11 cannot be applied to the actual source without an additional proof.

Likewise, no committed machine trace proves that Case A occurs on enough targets to make a raw scan succeed.

The session correctly stops at this boundary.

### 11. Separation guard is preserved

The settled facts remain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

P4-S039 proves neither

\[
X\notin OH
\]

for the actual committed witness nor

\[
X\in OH.
\]

Therefore no OH non-invariance and no strict \(R_2\subsetneq OH\) conclusion follows.

## Validation disposition

**PASS.**

P4-S039 produces a genuine source-side advance.

Pure finite linear algebra is no longer the unresolved obstacle: the three local self-predictions semantically determine a raw coordinate for the displayed recoding, and under local sibling totality this yields an actual raw one-hole destroyer.

The exact surviving obstruction is effective and online: a preselected raw sentinel may face a second locally consistent endpoint or a divergence-only alternate endpoint, so the c.e. local consistency code need not have a finitely recognizable singleton completion.

The sustained equation

\[
R_2=OH\ ?
\]

remains unresolved.

P4-S040 should attack this c.e. local-code completion / raw-adjacent companion boundary directly, not return to ordinary raw-martingale pricing.
