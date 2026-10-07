# P4-S046 — one-bit future-A certification cost

Date: 2026-10-07
Session: P4-S046
Incoming checkpoint: 99b628d62895fb3c98e7c31545b818580b0b884d
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding

Result: **Target correctness plus syntactic self-avoidance collapse every actual Case-A same-block access cost to at most one raw bit for the displayed three-bit recoding. \(A_0\) is block-free; \(A_1\) needs at most \(x_2\); \(A_2\) needs at most \(x_1\). The three differences \(A^{-1}e_r\) are automatically finitely refuted, and the only extra obstruction to block-free \(A_1/A_2\) certification is the common raw diagonal \(011\), virtual difference \(110\). Block-local \(CAC/CCA\) gadgets show cost one is sharp. Block-free still need not be one-hole-safe because outside certificate support may hit the current open sentinel. No raw destroyer for \(X\) and no proof \(X\in OH\) are obtained.**

## Authority and frozen scope

Live main was exactly 99b628d62895fb3c98e7c31545b818580b0b884d, the P4-S045 prompt-setting outgoing checkpoint. There was no mismatch. P4-S046 was unused: Phase 4 contained exactly P4-S001 through P4-S045 mathematics records.

P4-S001 through P4-S045, CAND-01 authority, the post-S031 pivot, and P4-S032 through P4-S045 were read at the pinned state, with special attention to P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S045. All validated mathematics through P4-S045 is frozen. The excluded bankroll, backward-price, ordinary martingale-compilation, ambiguity-mass, generic totalization, remote-divergence, local-enumeration and runtime-modulus routes are not reopened.

Retain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR,
\qquad
X\in CR,\quad H(X)=Y\notin OH,
\]
with \(X\in OH\) unresolved.

## 1. Certificate support and freshness cost

For a raw block \(B_b\), write its actual raw word \(x\in\mathbb F_2^3\), virtual word \(v=Ax\), and
\[
A=\begin{pmatrix}1&0&1\\1&1&0\\1&1&1\end{pmatrix}.
\]

For a raw hypothesis \(z\), simulate the three local \(M\)-computations on the oracle equal to \(Y\) outside the block and with virtual block \(Az\). A finite wrong/nonbinary halt is a **rejection trace**.

Same-block oracle answers come from the finite hypothesis, not live raw bits. Outside answers come from \(X\) via the recoding; the finite raw coordinates thereby read form \(S_{\rm out}\). By the retained strict use cap,
\[
S_{\rm out}\subseteq\bigcup_{\substack{d<h(b)\\d\ne b}}B_d,\qquad
h(b)=\max\{b+1,\lceil V(b)/3\rceil\}.
\]

For prospective sentinel role \(i\), let \(E\subseteq\{0,1,2\}\setminus\{i\}\). After exposing \(x\upharpoonright E\), an **\(E\)-slice certificate** for \(x_i=\beta\) is finite evidence rejecting every \(z\) with
\[
z|E=x|E,\qquad z_i=1-\beta.
\]
Target correctness makes this sound because the actual block is never rejected.

Define \(\kappa_b(i)\) as the least \(|E|\) supporting such a certificate for an actual Case-A role. Thus \(\kappa=0\) is block-free; \(\kappa=1\) exposes one non-sentinel raw bit; \(\kappa=2\) is the old two-non-sentinel endpoint test. Reading the sentinel consumes the target and is not useful pre-certification.

## 2. Automatic rejections from self-avoidance

Direct calculation gives
\[
A^{-1}=\begin{pmatrix}1&1&1\\1&0&1\\0&1&1\end{pmatrix}.
\]
Let \(d_r=A^{-1}e_r\). Then
\[
d_0=110,\qquad d_1=101,\qquad d_2=111,\qquad Ad_r=e_r.
\]

### Theorem 1 — automatic unit-flip rejection

For every block and \(r<3\), raw candidate \(x+d_r\) is finitely rejected.

Its virtual oracle differs from \(Y\) only at \(q_r\). Syntactic self-avoidance makes the input-\(q_r\) computation identical to \(M^Y(q_r)\), which target correctness makes halt with actual bit \(v_r\). The candidate expects \(v_r\oplus1\), so the same finite halt rejects it.

No noncomputable source value is hard-coded: a live procedure dovetails all eight finite raw hypotheses.

## 3. Every Case A costs at most one block bit

Case \(A_i\) means raw-adjacent candidate \(x+e_i\) is finitely rejected.

### Theorem 2 — one-bit local access bound

\[
A_0\Rightarrow\kappa_b(0)=0,
\]
\[
A_1\Rightarrow\kappa_b(1)\le1\quad\text{using only }x_2,
\]
\[
A_2\Rightarrow\kappa_b(2)\le1\quad\text{using only }x_1.
\]

For role 0, the four differences which flip \(x_0\) are
\[
100,110,101,111=e_0,d_0,d_1,d_2.
\]
Case \(A_0\) rejects \(e_0\), and Theorem 1 rejects the other three. Hence the entire wrong-\(x_0\) slice is rejected without reading \(B_b\).

For role 1, after reading only \(x_2\), the two differences flipping \(x_1\) are
\[
010,110=e_1,d_0.
\]
For role 2, after reading only \(x_1\), they are
\[
001,101=e_2,d_1.
\]
In each case the raw-adjacent candidate is rejected by A and the other automatically.

Therefore
\[
\boxed{\kappa\in\{0,1\}\text{ for every actual A witness}.}
\]

Cost two is never needed merely to obtain a positive Case-A raw-bit prediction for this recoding.

## 4. Exact block-free obstruction for roles 1 and 2

Let
\[
\delta=e_1+e_2=011,\qquad A\delta=110.
\]

For \(A_1\), the full wrong-\(x_1\) slice is
\[
\{e_1,d_0,d_2,\delta\};
\]
for \(A_2\), the full wrong-\(x_2\) slice is
\[
\{e_2,d_1,d_2,\delta\}.
\]

All members except \(\delta\) are already rejected.

### Proposition 3 — common diagonal criterion

Within this finite positive slice-certificate system,
\[
A_1:\ \kappa_b(1)=0\iff x+\delta\text{ is finitely rejected},
\]
\[
A_2:\ \kappa_b(2)=0\iff x+\delta\text{ is finitely rejected}.
\]

If virtual candidate \(v+110\) is accepted or divergence-only, it remains compatible with every finite local trace, so one cross-role live bit is necessary for this certificate language.

## 5. Cost one is structurally sharp

On target \(0^\omega\), use block-local self-avoiding tables \(f_0(u_1,u_2),f_1(u_0,u_2),f_2(u_0,u_1)\).

A \(CAC\) gadget is
\[
\begin{array}{c|cccc}
&00&01&10&11\\ \hline
f_0&0&1&1&1\\
f_1&0&1&1&\uparrow\\
f_2&0&1&1&\uparrow
\end{array}
\]
and a \(CCA\) gadget is
\[
\begin{array}{c|cccc}
&00&01&10&11\\ \hline
f_0&0&1&1&\uparrow\\
f_1&0&1&1&1\\
f_2&0&1&1&\uparrow
\end{array}.
\]

In both gadgets the diagonal \(110\) has trace \((1,1,\uparrow)\), so it is not finitely rejected. The unique visible A has exact cost one: \(A_1\) in \(CAC\), \(A_2\) in \(CCA\).

Repeating or alternating the gadgets gives a computable finite-use syntactically self-avoiding structural model with recurrent nontriple \(C_0\), visible A on every block, and no support-only A certificate in this local finite-evidence system.

This is structural only. Its target is computable, so it is not an actual-source selector countermodel.

## 6. Same-block access is independent of timing

Retain
\[
CAA,\qquad CAC,\qquad CCA.
\]

When the diagonal is not finitely rejected,
\[
A_1:\ \text{read }x_2\text{ to preserve sentinel }x_1,
\]
while
\[
A_2:\ \text{read }x_1\text{ to preserve sentinel }x_2.
\]

The two gadgets realize both arms with block-local use and no delayed-certificate mechanism. Hence same-block certification access is an additional obstruction independent of the P4-S045 timing obstruction.

For
\[
C_1\wedge B_2\Rightarrow(A,C,B),\qquad
C_2\wedge B_1\Rightarrow(A,B,C),
\]
the accompanying \(A_0\) already has local cost \(0\). Thus B cannot reduce its same-block cost; any remaining role-0 problem lies in outside support or global fallback.

## 7. Block-free is not one-hole-safe

Let \(s\) be the current unread sentinel and \((c,j)\) a prospective future target.

Call a future certificate **open-hole-safe** if it preserves the future sentinel, its outside support avoids \(s\), and its transition protocol has a total no-event continuation leaving only \(s\) permanently unread before handoff.

Theorem 2 does not force this. Even a block-free certificate can have
\[
s\in S_{\rm out}.
\]
The use cap controls where support lies, not whether it intersects the current hole.

This is the exact live-source gap.

## 8. Certification graph and source-side guard

Use prospective roles \((b,i)\) as nodes. A usable edge
\[
(b,i)\to(c,j)
\]
means that while keeping the current sentinel, a finite positive protocol obtains an open-hole-safe A certificate for \((c,j)\), retains its sentinel, and has a total one-hole fallback.

Separate semantic edge existence, positive edge discovery, computable outgoing selection, and an infinite computable usable path.

### Theorem 4 — usable path theorem

An infinite computable usable path on \(X\) yields a total computable no-repeat one-hole scan which bets correctly at every completed target, hence
\[
X\notin OH.
\]

P4-S046 does not produce such a path. Low same-block cost does not imply support compatibility or effective path choice.

Cost-one access also gives no direct computable-randomness contradiction: it says which bit must be read, not what that bit is.

## 9. Exact boundary

The same-block layer is now
\[
A_0:\kappa=0,\qquad A_1:\kappa\le1,\qquad A_2:\kappa\le1,
\]
with one common \(011/110\) diagonal controlling block-free \(A_1/A_2\).

The next missing resource is
\[
\boxed{\text{current-hole-uniform future A certification}},
\]
meaning future-A evidence which can be acquired uniformly over both values of the current open sentinel, without reading it, while keeping the future sentinel usable.

No raw destroyer for \(X\) is constructed. No proof \(X\in OH\) is obtained. No OH non-invariance witness or \(R_2\subsetneq OH\) separation is claimed.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.
