# P4-S047 Validation

Date: 2026-10-07
Session: P4-S047
Incoming checkpoint: 751ce6dbf35c2ea4e34e02280e31ddeaab8871d1
Mathematics record: phase4/P4-S047_MATHEMATICS.md
Disposition: **PASS**

## Authority and scope

- Live main matched the exact P4-S046 outgoing checkpoint before substantive work.
- Direct path inspection showed P4-S047 was unused.
- P4-S001 through P4-S046, CAND-01 authority, the post-S031 pivot and P4-S032 through P4-S046 were read at the pinned state.
- Special attention was given to P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S046.
- Frozen bankroll, backward-price, ordinary martingale, ambiguity-mass, generic totalization, remote-divergence, local-enumeration, certificate-time and same-block-cost routes were not reopened.

**Status: VALID.**

## 1. Current-hole completions and safe rows

For current raw sentinel \(s=(b,i)\), the two finite counterfactual completions differ only at that raw coordinate. Current-block virtual row \(r\) changes exactly when \(A_{ri}=1\).

For

\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix},
\]

the columns give

\[
\operatorname{Safe}(0)=\varnothing,\qquad
\operatorname{Safe}(1)=\{0\},\qquad
\operatorname{Safe}(2)=\{1\}.
\]

The branch oracle answers are computed from the already read non-sentinel raw bits plus the explicit finite hypothesis \(h\); the actual hole is never queried.

**Status: VALID.**

## 2. CHU certificate definition

The record requires finite positive rejection families under both old-hole hypotheses, a common future sentinel prediction, preservation of both current and future sentinels during certification, and a total one-hole fallback.

It explicitly separates semantic existence, positive finite discovery and computable indefinite selection. It does not infer c.e. fallback totality from semantic totality.

**Status: VALID.**

## 3. Safe-trace theorem

The two counterfactual virtual sources agree:

- at every coordinate outside the old block; and
- on exactly the safe rows inside the old block.

Therefore a finite deterministic rejection trace which queries no hole-dependent old row receives identical oracle answers in both branch simulations. The same wrong/nonbinary halt rejects the same future hypothesis in both branches.

No certificate-time bound or negative divergence information is used.

**Status: VALID.**

## 4. Two-branch future fixedness theorem

Assume for a future block \(B_c\) that, for both \(h\),

\[
M^{Y^{[h]}}(q_{c,r})\downarrow=Y(q_{c,r})
\]

for all \(r<3\).

Changing the future raw candidate by \(A^{-1}e_r\) changes only virtual coordinate \(q_{c,r}\) relative to \(Y^{[h]}\). Syntactic self-avoidance makes the candidate input-\(q_{c,r}\) trace identical to the branch-fixed trace. Its output is the unchanged future bit, opposite the candidate expectation. Thus the candidate is finitely rejected in both branches.

This correctly extends the P4-S046 automatic theorem under an explicit extra hypothesis. Target correctness alone supplies the hypothesis only on the actual branch and is not overextended to the counterfactual branch.

**Status: VALID.**

## 5. Low-cost roles under an old open hole

The P4-S046 local wrong-slice calculations remain exact:

- \(A_0\): wrong differences \(e_0,110,101,111\);
- \(A_1\) after future \(x_2\): \(e_1,110\);
- \(A_2\) after future \(x_1\): \(e_2,101\).

The future cross-read for \(A_1/A_2\) lies in \(B_c\), so changing an older raw coordinate in \(B_b\) does not alter that raw value.

The record therefore correctly isolates old-hole branch sensitivity in the computation traces rather than in the future local access itself.

**Status: VALID.**

## 6. Structural old-row gate

For every current role \(i\), \(\operatorname{Dep}(i)\) is nonempty. Choose \(p\in\operatorname{Dep}(i)\). On target \(0^\omega\), changing the current raw completion flips virtual row \(p\).

Every future local input first queries \(p\):

- answer \(0\): run the stated block-local table;
- answer \(1\): diverge.

Because \(p\) is in an older block, this preliminary query is never the future input itself. The local tables are self-avoiding. Hence the composite functional remains syntactically self-avoiding.

The actual \(h=0\) branch reproduces the stated local tables. The alternate \(h=1\) branch diverges before any local rejection.

The \(CAC\) and \(CCA\) tables are the already validated P4-S046 exact-cost-one gadgets.

For the new \(ACB\) table:

\[
f_0=(0,1,0,0),\quad
f_1=(0,1,0,0),\quad
f_2=(0,\uparrow,1,0)
\]

in the displayed input order \(00,01,10,11\).

Direct checking gives:

- target \(000\): all outputs \(0\);
- \(111\): \(f_0(11)=0\ne1\), hence \(A_0\);
- \(011\): \((f_0(11),f_1(01),f_2(01))=(0,1,\uparrow)\), hence \(C_1\);
- \(101\): \((f_0(01),f_1(11),f_2(10))=(1,0,1)\), hence \(B_2\).

Thus the pattern is \(ACB\) and P4-S046 makes \(A_0\) block-free.

Defining all other inputs to output \(0\) gives no alternative outside wrong-halt refutation. Use is finite and computably bounded.

Therefore, for every current-role/future-role pair, the retained abstract hypotheses permit visible low-cost A on the target together with complete failure of the corresponding two-branch finite slice rejection on the alternate old-hole completion.

The model target is \(0^\omega\), so it is correctly labelled structural only.

**Status: VALID.**

## 7. Role-transition and finite-use conclusions

Since the old-row gate works for every pair \(i\to j\), no nonempty universal role-only CHU transition matrix follows from target correctness, self-avoidance, finite use, recurrent nontriple C and the P4-S046 local-cost theorem.

Because every later designated A witness can query the same old hole-dependent row, pointwise finite use does not force infinitely many future A witnesses outside the current-hole collision set.

These are structural non-implication results, not claims about the actual committed \(M\).

**Status: VALID.**

## 8. Computable-randomness guard

The two \(h\)-simulations are counterfactual programs whose current-block oracle values are supplied by hypotheses. A finite halt in one branch and divergence in the other can be observed as a difference between simulations without observing which branch equals the actual source.

Therefore branch nonuniformity alone does not predict the current sentinel.

A genuine current-bit prediction would require finite evidence eliminating one current completion itself, for example a wrong/nonbinary target-equation halt which target correctness forbids on the actual completion.

The session correctly obtains no direct computable-randomness contradiction from nonuniformity alone.

**Status: VALID.**

## 9. CHU certification graph

The CHU usable-edge definition includes:

- common two-branch prediction;
- old-hole avoidance;
- future sentinel preservation;
- legal support acquisition;
- a total one-hole fallback;
- a legal handoff to the next unique sentinel.

Concatenating an already computable infinite sequence of such edges gives the same kind of raw one-hole destroyer as P4-S046, now with explicit old-hole uniformity.

The record does not infer a path from semantic edge existence, finite out-degree or c.e. discovery. It also notes that parallel edge searches may themselves recreate the multiple-protected-hole problem.

**Status: VALID.**

## 10. Separation and programme guards

No infinite CHU usable path is established for the committed \(M,Y,X\).

Accordingly P4-S047 proves neither

\[
X\notin OH
\]

nor

\[
X\in OH.
\]

No OH non-invariance theorem and no strict \(R_2\subsetneq OH\) conclusion are claimed.

The retained comparison remains

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. Phase 4 remains OPEN; Phase 5 remains CLOSED.

**Status: VALID.**

## Final disposition

**PASS.**

P4-S047 isolates branch stability relative to the old open hole, proves two precise sufficient uniformity criteria, and supplies a sharp structural old-row-gating countermodel showing that the retained abstract hypotheses do not force current-hole-uniform recurrence.
