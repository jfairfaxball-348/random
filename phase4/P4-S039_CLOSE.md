# P4-S039 close

Date: 2026-10-07
Session: P4-S039
Incoming checkpoint: ebf18e6ef13c1a684b0164811b7a13cc2bdf576c
Scope: same-source raw one-hole simulation under the displayed three-bit recoding
Status: **COMPLETED**

## Result

P4-S039 separates exact transcript simulation from same-source vulnerability simulation.

For the displayed block map

\[
u=Ax,\qquad
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix},
\]

with one raw coordinate \(x_i\) omitted, the virtual block is exactly an affine one-bit state

\[
u=a+h\,Ae_i.
\]

The three raw flip columns are

\[
(1,1,1)^T,\qquad(0,1,1)^T,\qquad(1,0,1)^T.
\]

Hence an \(x_0\)-hole leaves all three virtual bits unresolved; an \(x_1\)-hole leaves only \(u_0\) known; an \(x_2\)-hole leaves only \(u_1\) known.

Exact simulation of a virtual unit sentinel is strictly more expensive. Since

\[
A^{-1}e_0=(1,1,0)^T,\qquad
A^{-1}e_1=(1,0,1)^T,\qquad
A^{-1}e_2=(1,1,1)^T,
\]

the three virtual unit holes require respectively two, two and three raw unresolved coordinates. A one-raw-hole process cannot transport such a unit sentinel across blocks: closing the old raw hole collapses the old affine state, and a new raw hole in another block creates an independent ambiguity.

That does not settle same-source vulnerability. Using the actual P4-S011 autoreduction \(M\), define for each virtual block \(B\) the set \(C_B\) of three-bit assignments on which all three local computations \(M(q_0),M(q_1),M(q_2)\) halt with the assigned bits.

Self-avoidance implies

\[
d_H(C_B)\ge2.
\]

For the displayed \(A\), every nonempty length-three binary code of minimum distance at least two pulls back under \(A^{-1}\) into a raw coordinate hyperplane. Thus the full local consistency set always semantically fixes at least one raw coordinate.

This has a finite positive form. Once two distinct members of \(C_B\) are seen, a fixed raw coordinate is already certified: a distance-two pair certifies \(x_0\) via parity, while a distance-three pair is antipodal, admits no third codeword, and certifies \(x_1,x_2\).

The obstruction is therefore effective, not purely algebraic. For a preselected raw target \(x_i\), the two affine hypotheses have an exact trichotomy:

1. the alternate hypothesis is finitely rejected, giving a target-visible raw self-avoiding predictor;
2. the alternate hypothesis is also self-consistent, giving a genuine one-bit circular pair;
3. the alternate hypothesis fails only because a sibling computation diverges, leaving semantic uniqueness without a finite completion certificate.

The wtt use bound does not eliminate the third case.

A positive same-source theorem is obtained. For every repeated invertible three-bit matrix with the raw-hyperplane coding property, if all 24 local sibling computations halt at every reached target block, three synchronized raw one-hole scans can compute each \(C_B\); at least one of the three raw coordinate types is certified infinitely often, and the corresponding computable martingale doubles infinitely often. Hence under local sibling totality,

\[
X\notin OH.
\]

The displayed matrix satisfies the exact raw-hyperplane criterion

\[
(1,1,1)A\text{ is a unit row},
\qquad
A^{-1}(1,1,1)^T\ne(1,1,1)^T.
\]

The committed P4-S011 witness does not provide local sibling totality or a blockwise classification of the alternate raw hypotheses. Its authority gives target correctness, self-avoidance, a computable wtt use bound, and permission for sibling divergence. Therefore no actual raw one-hole destroyer is justified in this session.

No proof of

\[
X\in OH
\]

is obtained either. Thus no OH non-invariance theorem and no

\[
R_2\subsetneq OH
\]

claim is available. Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## Next bounded target

P4-S040 should globalize the new c.e. local-code boundary.

Test whether a raw one-hole protocol can progress without a negative singleton-completion certificate by exploiting finitely visible pairs of locally consistent assignments or finite rejection of raw-adjacent companions. If not, isolate an exact stall invariant for the Case-B/Case-C arms.

The central object should be the raw-adjacent companion relation \(X\leftrightarrow X\oplus e_j\), translated to the virtual difference \(Ae_j\), together with the c.e. enumeration of simultaneous \(M\)-consistent local candidates.

Do not return to backward-price normalization, the frozen P4-S015–P4-S031 bankroll line, or ambiguity mass.
