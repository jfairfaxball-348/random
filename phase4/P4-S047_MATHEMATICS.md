# P4-S047 — current-hole branching, uniform certificates and old-row-gated nonuniformity

Date: 2026-10-07
Session: P4-S047
Incoming checkpoint: 751ce6dbf35c2ea4e34e02280e31ddeaab8871d1
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding

Result: **CURRENT-HOLE BRANCHING IS FINITE AND EFFECTIVE: THE UNREAD OLD SENTINEL GIVES EXACTLY TWO COUNTERFACTUAL SOURCE COMPLETIONS, WITH SAFE CURRENT VIRTUAL ROWS \(\varnothing,\{u_0\},\{u_1\}\) FOR RAW ROLES \(0,1,2\). A FUTURE SLICE CERTIFICATE IS AUTOMATICALLY CURRENT-HOLE-UNIFORM WHEN ITS FINITE REJECTION TRACES AVOID THE HOLE-DEPENDENT OLD ROWS. MORE GENERALLY, TWO-BRANCH FUTURE FIXEDNESS RESTORES THE P4-S046 AUTOMATIC UNIT-FLIP REJECTIONS IN BOTH OLD-HOLE BRANCHES, SO \(A_0,A_1,A_2\) RETAIN LOCAL COST \(0,1,1\) UNDER A PRECISE BRANCH-FIXEDNESS HYPOTHESIS. SELF-AVOIDANCE ALONE DOES NOT FORCE THIS. FOR EVERY CURRENT RAW ROLE AND EVERY FUTURE A ROLE THERE IS A COMPUTABLE FINITE-USE SYNTACTICALLY SELF-AVOIDING STRUCTURAL \(0^\omega\) MODEL WHICH GATES THE FUTURE A WITNESS THROUGH ONE OLD HOLE-DEPENDENT VIRTUAL ROW: THE TRUE BRANCH HAS THE SAME VISIBLE A AND THE SAME P4-S046 LOCAL COST, WHILE THE ALTERNATE OLD-HOLE BRANCH MAKES EVERY RELEVANT FUTURE LOCAL COMPUTATION DIVERGE. THUS LOW LOCAL COST CAN COEXIST WITH UNAVOIDABLE OLD-HOLE DEPENDENCE, NO ROLE-ONLY CURRENT-HOLE-UNIFORM TRANSITION MATRIX IS FORCED, AND FINITE USE DOES NOT FORCE INFINITELY MANY FUTURE A CANDIDATES OUTSIDE THE OLD-HOLE COLLISION SET. AN INFINITE COMPUTABLE PATH OF CURRENT-HOLE-UNIFORM USABLE EDGES WOULD STILL GIVE \(X\notin OH\), BUT NO SUCH PATH IS FORCED FOR THE COMMITTED SOURCE. MERE FAILURE OF UNIFORMITY DOES NOT ITSELF EXPOSE THE CURRENT BIT OR PROVE \(X\in OH\). HOWEVER ANY FINITE WRONG/NONBINARY EQUATION UNDER ONE OLD-HOLE COMPLETION ELIMINATES THAT COMPLETION. A CANONICAL GLOBAL-REFUTATION ONE-HOLE SCAN THEREFORE SHOWS THAT HYPOTHETICAL \(X\in OH\) MUST EVENTUALLY REACH A FALSE RAW-RADIUS-ONE COMPLETION WHICH IS A PARTIAL FIXED POINT OF \(M\): EVERY HALT IS CORRECT AND ONLY DIVERGENCE CAN HIDE THE FALSE BRANCH.**

## Authority, uniqueness and frozen scope

Immediately before substantive work and again before the first write, live main was exactly

\[
\texttt{751ce6dbf35c2ea4e34e02280e31ddeaab8871d1},
\]

the P4-S046 outgoing checkpoint which installs the present bounded task. Direct path inspection found no P4-S047 mathematics record, so P4-S047 was unused.

P4-S001 through P4-S046, the selected CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S046 were read at the pinned state, with special attention to P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S046.

All validated mathematics through P4-S046 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation, ambiguity mass, general radius-one totalization, one-off remote-divergence localization, local A/B/C enumeration, generic certificate-time bounding and another generic same-block freshness-cost enumeration are not reopened.

Retain

\[
R_2=\{x\in CR:\text{every total computable fair-coin-preserving global-}k=2\text{ map sends }x\text{ to }CR\},
\]

\[
OH=\{x\in CR:\text{every total computable adaptive no-repeat one-hole scan sends }x\text{ to }CR\},
\]

\[
OH^{iso}=\{x\in CR:\text{every computable fair-coin-preserving homeomorphism }H\text{ sends }x\text{ into }OH\},
\]

and

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Let \(Y\) be the settled P4-S011 computably random wtt-autoreducible source, \(M\) its committed syntactically self-avoiding wtt autoreduction, \(D\) its one-hole destroyer, and

\[
X=H^{-1}(Y).
\]

Retain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

The missing source-side statement remains whether

\[
X\in OH.
\]

Use throughout

\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix},
\qquad
c_0=111,\quad c_1=011,\quad c_2=101,
\]

and the strict block horizon

\[
V(b)=\max_{r<3}U(3b+r),
\qquad
h(b)=\max\{b+1,\lceil V(b)/3\rceil\}.
\]

The P4-S046 facts remain

\[
A^{-1}e_0=110,\qquad A^{-1}e_1=101,\qquad A^{-1}e_2=111,
\]

\[
A_0\Rightarrow\kappa=0,\qquad
A_1\Rightarrow\kappa\le1\text{ using }x_2,\qquad
A_2\Rightarrow\kappa\le1\text{ using }x_1.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## 1. Exact two-branch source completion at the current hole

Let the current protected raw sentinel be

\[
s=(b,i)
\]

and suppose every raw coordinate of the current block \(B_b\) except \(x_i^{(b)}\) has already been read.

For \(h\in\{0,1\}\), define the finite counterfactual raw completion \(X^{[h]}\) by

\[
X^{[h]}(s)=h
\]

and

\[
X^{[h]}(n)=X(n)\qquad(n\ne s).
\]

This notation is semantic. A live scan never reads the actual \(X(s)\) in order to choose one branch.

Operationally, whenever a finite simulation asks for current-block virtual row \(u_r^{(b)}\), branch \(h\) supplies

\[
u_r^{[h]}
=
\bigoplus_{k\ne i}A_{rk}x_k^{(b)}
\oplus A_{ri}h.
\]

Every term on the right is either already read or is the explicit finite hypothesis \(h\). Thus both branches are uniformly computable from the finite scan state without using the noncomputable actual hole value as a program parameter.

Write

\[
Y^{[h]}=H(X^{[h]})
\]

only as shorthand for these finite simulations. Outside \(B_b\), the two candidate sources agree.

For a future target block \(B_c\), \(c\ne b\), same-block candidate values are supplied from the finite future raw hypothesis exactly as in P4-S046. Outside \(B_b\cup B_c\), required oracle values are acquired live from \(X\). The current block is the only place where the two old-hole simulations differ.

## 2. Safe current rows

Changing the current raw hole value changes its virtual block by

\[
c_i=Ae_i.
\]

Define

\[
\operatorname{Dep}(i)=\{r<3:A_{ri}=1\},
\qquad
\operatorname{Safe}(i)=\{0,1,2\}\setminus\operatorname{Dep}(i).
\]

Directly from the columns of \(A\),

\[
\operatorname{Dep}(0)=\{0,1,2\},
\qquad
\operatorname{Safe}(0)=\varnothing,
\]

\[
\operatorname{Dep}(1)=\{1,2\},
\qquad
\operatorname{Safe}(1)=\{0\},
\]

\[
\operatorname{Dep}(2)=\{0,2\},
\qquad
\operatorname{Safe}(2)=\{1\}.
\]

Thus:

- an old \(x_0\)-hole changes all three current virtual rows;
- an old \(x_1\)-hole leaves only \(u_0\) invariant;
- an old \(x_2\)-hole leaves only \(u_1\) invariant.

A finite future trace is **syntactically current-hole-independent** when every current-block virtual query it makes lies in \(\operatorname{Safe}(i)\).

This is stronger than being current-hole-uniform. A trace may query a row in \(\operatorname{Dep}(i)\), yet the two explicit branch simulations may still produce compatible finite evidence. Such a query is a syntactic collision, not automatically a fatal one-hole collision.

## 3. Current-hole-uniform finite slice certificates

Fix a prospective future target

\[
t=(c,j),\qquad c\ne b,
\]

and a P4-S046 same-block slice choice

\[
E\subseteq\{0,1,2\}\setminus\{j\}.
\]

The intended cases are:

\[
A_0:E=\varnothing,
\qquad
A_1:E=\{2\},
\qquad
A_2:E=\{1\},
\]

with the last two used only when the block-free diagonal certificate is unavailable.

### Definition 1 — current-hole-uniform slice certificate

A **current-hole-uniform**, or CHU, finite slice certificate for future sentinel value \(x_j^{(c)}=\beta\) consists of finite positive data such that:

1. for each \(h\in\{0,1\}\), every future raw hypothesis \(z\) satisfying
   \[
   z|E=x^{(c)}|E,\qquad z_j=1-\beta
   \]
   receives a finite wrong/nonbinary rejection trace in the \(h\)-branch simulation;
2. both \(h\)-branches certify the same future sentinel value \(\beta\);
3. no live raw query reads the current sentinel \(s\);
4. no live raw query reads the future sentinel \(t\);
5. the allowed P4-S046 same-block access \(E\) is the only live access inside the future target block before handoff;
6. the finite transition comes with a total computable no-event continuation which preserves the global one-hole condition.

The rejection trace used for one wrong future hypothesis is allowed to differ between \(h=0\) and \(h=1\). Uniformity is a statement about the finite conclusion and legal live access, not literal trace equality.

### Three effectivity levels

Keep separate:

1. **semantic CHU existence** — there exists a pair of compatible finite witnesses and a semantically legal fallback;
2. **positive CHU discovery** — the finite witnesses and a syntactically certified fallback protocol can be recognized by finite computation from the current finite state;
3. **computable indefinite selection** — one total computable scan can repeatedly choose positively certified CHU edges and continue forever on the target.

Finite positive rejection is c.e. once all live support values used by that particular witness have been legally acquired. Semantic totality of an arbitrary fallback is not automatically c.e. Therefore positive edge discovery includes a fallback drawn from a protocol whose total one-hole legality is known effectively; it is not inferred from semantic existence alone.

## 4. Trace avoidance gives automatic old-hole uniformity

### Theorem 2 — safe-trace criterion

Suppose a finite P4-S046 future slice certificate has rejection traces which, whenever they query the current block, query only rows in \(\operatorname{Safe}(i)\).

Then the same finite rejection traces are valid under both current-hole hypotheses.

Consequently, if the certificate predicts one future sentinel value and its future-target access and fallback satisfy Definition 1, it is CHU.

#### Proof

The two candidate sources \(X^{[0]},X^{[1]}\) agree outside \(s\). Their virtual images agree outside \(B_b\), and inside \(B_b\) they agree exactly on the safe rows.

By hypothesis every oracle answer read by each finite rejection trace is therefore identical in the two branch simulations. Determinism gives identical machine traces and outputs. The finite wrong/nonbinary halt which rejects a candidate in one branch rejects the same candidate in the other. ∎

This is the simplest positive source-specific criterion. It does not require any certificate-time modulus.

For a future \(A_0\), all four wrong-\(x_0\) rejections from P4-S046 are CHU whenever their chosen finite traces avoid \(\operatorname{Dep}(i)\).

For future \(A_1\) and \(A_2\), the extra local raw reads \(x_2^{(c)}\) and \(x_1^{(c)}\) occur in the future block, not the old block, so they do not themselves interact with the old-hole branch. Only the outside computation traces can create old-hole dependence.

## 5. Two-branch future fixedness restores the P4-S046 automatic theorem

Trace avoidance is sufficient but not necessary. There is a stronger semantic condition under which self-avoidance again becomes decisive.

### Definition 3 — two-branch future fixedness

A future block \(B_c=\{q_{c,0},q_{c,1},q_{c,2}\}\) is **two-branch fixed relative to the current hole** when, for both \(h=0,1\),

\[
M^{Y^{[h]}}(q_{c,r})\downarrow
=
Y(q_{c,r})
\qquad(r<3).
\]

The right-hand side is the same in both branches because changing the old sentinel changes only block \(B_b\), not the future block.

Target correctness supplies this for the actual old-hole branch. It does not supply it for the counterfactual branch.

### Theorem 4 — branch-fixed automatic unit-flip rejection

Assume two-branch future fixedness at \(B_c\).

For every \(r<3\) and every \(h\in\{0,1\}\), the future raw candidate

\[
x^{(c)}+A^{-1}e_r
\]

is finitely rejected in the \(h\)-branch.

#### Proof

Relative to \(Y^{[h]}\), the candidate changes only virtual coordinate \(q_{c,r}\). The input-\(q_{c,r}\) computation syntactically avoids that coordinate, so the candidate computation is literally the same computation as

\[
M^{Y^{[h]}}(q_{c,r}).
\]

By two-branch future fixedness this halts with the unchanged future target bit. The candidate expects the opposite bit, so that finite halt rejects it. ∎

Thus the P4-S046 automatic candidates

\[
110,\qquad101,\qquad111
\]

remain automatic under both old-hole hypotheses once future fixedness is known in both branches.

### Corollary 5 — low-cost CHU theorem under two-branch fixedness

Under two-branch future fixedness:

- a future \(A_0\) certificate is CHU and block-free whenever the raw-adjacent \(e_0\) candidate is finitely rejected under both old-hole hypotheses with the same future \(x_0\) prediction;
- a future \(A_1\) certificate is CHU after reading only future \(x_2\) whenever the raw-adjacent \(e_1\) candidate is finitely rejected under both old-hole hypotheses with the same future \(x_1\) prediction;
- a future \(A_2\) certificate is CHU after reading only future \(x_1\) whenever the raw-adjacent \(e_2\) candidate is finitely rejected under both old-hole hypotheses with the same future \(x_2\) prediction.

The remaining wrong-slice candidate in each case is one of the branch-fixed automatic unit-flip candidates.

Therefore the P4-S046 local access costs

\[
0,\ 1,\ 1
\]

are compatible with an older open hole. The new resource is not extra target-block access. It is stability of the relevant finite evidence under the counterfactual old-hole completion.

## 6. Why self-avoidance alone does not give two-branch fixedness

P4-S046 used a special alignment: the candidate perturbation changed exactly the virtual coordinate equal to the input of the rejecting computation. Syntactic self-avoidance then removed the perturbation from that trace.

An old raw hole in a different block changes every row in

\[
\operatorname{Dep}(i)
\]

of \(B_b\). For a future input \(q_{c,r}\), none of those old coordinates is the simulated input \(q_{c,r}\).

Therefore syntactic self-avoidance at the future input imposes no prohibition on querying the old hole-dependent rows.

If the future trace avoids them, Theorem 2 applies.

If it queries them but both branches still halt with compatible rejecting evidence, branching is harmless.

If one branch changes output, turns a wrong halt into a correct halt, or diverges, target correctness gives no repair: it controls only the actual source \(Y\), not the counterfactual radius-one raw perturbation \(Y^{[1-X(s)]}\).

This is consistent with P4-S041/P4-S042: radius-one perturbations can cause partiality, and finite-use target traces do not force that partiality to localize or disappear.

## 7. Exact interaction with the three low-cost future roles

The local and old-hole resources now separate cleanly.

### Future \(A_0\)

Local cost is zero. The four wrong-\(x_0\) candidates are rejected on the actual source by the raw-adjacent A witness and the three automatic unit-flip rejections.

Old-hole uniformity is a different question. Every one of those finite computations may use outside source values, including hole-dependent current rows. If the relevant traces are safe, Theorem 2 applies; if the future block is two-branch fixed and the raw-adjacent rejection also survives both branches, Corollary 5 applies.

Thus block-free does not imply CHU.

### Future \(A_1\)

Local cost is at most one by reading future \(x_2\).

That read is unchanged when the old sentinel hypothesis changes. It neither helps nor hurts old-hole uniformity by itself.

The old-hole issue lies in the two finite rejection computations for the wrong-\(x_1\) slice: the raw-adjacent \(e_1\) rejection and the automatic \(110\) rejection. Two-branch fixedness makes the latter automatic in both branches; the former still requires compatible positive rejection in both branches.

### Future \(A_2\)

Symmetrically, the local read of future \(x_1\) is independent of the old-hole branch. Two-branch fixedness makes the \(101\) automatic rejection uniform, while the raw-adjacent \(e_2\) rejection must survive both branches.

Hence the crossed local rules retained from P4-S046,

\[
A_1:\text{ read future }x_2,
\qquad
A_2:\text{ read future }x_1,
\]

do not create a new old-hole obstruction. They also do not remove one.

Keep distinct:

1. future-target local access;
2. old-hole branch sensitivity of outside traces;
3. certificate time after the finite source values are supplied;
4. the global total one-hole fallback.

P4-S047 addresses item 2 only.

## 8. Current-hole collision sets

Fix the current sentinel \(s=(b,i)\).

### Definition 6 — witness collision

A finite future certificate witness has a **syntactic old-hole collision** when at least one of its oracle traces queries a current-block row in \(\operatorname{Dep}(i)\).

The collision is:

- **avoidable** if another finite witness for the same future slice conclusion avoids \(\operatorname{Dep}(i)\);
- **unavoidable for that witness language** if every positive witness for the same conclusion has a syntactic collision;
- **branch-harmless** if colliding traces nevertheless produce compatible finite rejection families under both \(h=0,1\);
- **genuinely nonuniform** if no compatible pair of finite branch certificates with the same future prediction is obtained — for example one required rejection is positively visible in one branch but remains divergence-only in the other.

Let

\[
\operatorname{Coll}(s)
\]

be the set of prospective future slice certificates for which every available positive witness has a syntactic old-hole collision, and let

\[
\operatorname{NUnif}(s)\subseteq\operatorname{Coll}(s)
\]

denote genuine branch nonuniformity.

The strict use horizon gives only a finite location bound for each individual witness. It does not state that infinitely many future A blocks lie outside \(\operatorname{Coll}(s)\), nor that a colliding trace is branch-harmless.

The next theorem shows this failure is structural, not merely a logical possibility.

## 9. Sharp old-row-gated structural countermodel

The retained abstract resources do not force any role-to-role CHU transition.

### Theorem 7 — every current-role/future-role pair can be made nonuniform

Fix:

- a current raw role \(i\in\{0,1,2\}\);
- a hole-dependent current virtual row
  \[
  p\in\operatorname{Dep}(i);
  \]
- a future A role \(j\in\{0,1,2\}\).

There is a computable syntactically self-avoiding finite-use functional \(N\) with computable target

\[
Y_*=0^\omega
\]

such that:

1. \(N^{Y_*}(n)=Y_*(n)=0\) for every input;
2. on every designated future block, the actual branch has a visible Case-A witness in role \(j\);
3. its P4-S046 local target-block cost is exactly the retained cost:
   - \(j=0\): cost \(0\);
   - \(j=1\): cost \(1\) may be forced;
   - \(j=2\): cost \(1\) may be forced;
4. the finite A witness is gated through the single old row \(p\);
5. under the alternate old raw-hole hypothesis, row \(p\) flips and every relevant future local computation diverges before producing a rejection;
6. hence no designated future A witness is CHU;
7. use remains finite and computable;
8. for \(j=1,2\), recurrent nontriple \(C_0\) and visible A are retained using only the validated \(CAC/CCA\) gadgets.

#### Construction

Use raw target \(X_*=0^\omega\), so \(Y_*=H(X_*)=0^\omega\).

Choose one old block \(B_b\) and leave raw role \(i\) as its hypothetical current sentinel. Because \(p\in\operatorname{Dep}(i)\), changing the old raw completion from \(h=0\) to \(h=1\) flips virtual row \(p\).

On each later designated block \(B_c\), every local input first queries the old virtual coordinate \(p\).

- If that answer is \(1\), diverge forever.
- If that answer is \(0\), continue with a fixed block-local syntactically self-avoiding table.

For future role \(j=1\), use the validated P4-S046 \(CAC\) table

\[
\begin{array}{c|cccc}
&00&01&10&11\\ \hline
f_0&0&1&1&1\\
f_1&0&1&1&\uparrow\\
f_2&0&1&1&\uparrow
\end{array}.
\]

Its target block \(000\) is correct, the unique visible A is \(A_1\), the status is \(CAC\), the diagonal \(110\) is divergence-only, and \(\kappa(1)=1\).

For future role \(j=2\), use the validated \(CCA\) table

\[
\begin{array}{c|cccc}
&00&01&10&11\\ \hline
f_0&0&1&1&\uparrow\\
f_1&0&1&1&1\\
f_2&0&1&1&\uparrow
\end{array}.
\]

Its unique visible A is \(A_2\), the status is \(CCA\), the same diagonal is divergence-only, and \(\kappa(2)=1\).

For future role \(j=0\), use the following block-local \(ACB\) table:

\[
\begin{array}{c|cccc}
&00&01&10&11\\ \hline
f_0&0&1&0&0\\
f_1&0&1&0&0\\
f_2&0&\uparrow&1&0
\end{array}.
\]

Here \(f_0\) is indexed by \((u_1,u_2)\), \(f_1\) by \((u_0,u_2)\), and \(f_2\) by \((u_0,u_1)\).

At \(000\) all three outputs are \(0\).

At raw companion \(111\), input \(q_0\) sees \(11\) and outputs \(0\) against expected \(1\), so direction \(0\) is \(A_0\).

At \(011\), the traces are \(f_0(11)=0\), \(f_1(01)=1\), \(f_2(01)=\uparrow\), so direction \(1\) is \(C_1\).

At \(101\), the traces are \(f_0(01)=1\), \(f_1(11)=0\), \(f_2(10)=1\), so direction \(2\) is \(B_2\).

Thus the status is \(ACB\), and P4-S046 gives \(\kappa(0)=0\).

The preliminary old-row query is to a coordinate in a different block from every future input, so it does not violate syntactic self-avoidance. The local table then avoids its own input by construction. Every computation makes at most one old-row query plus finitely many same-block queries, so there is a computable finite use bound.

On the target old-hole branch \(h=0\), row \(p=0\), so all future gadgets behave exactly as above.

On the alternate branch \(h=1\), row \(p=1\), so all relevant future local computations diverge at the gate. The finite wrong-slice rejection family needed by P4-S046 therefore does not exist in that branch.

Define every other input to output \(0\) without querying the future block. Such outside equations supply no alternative finite rejection of a future wrong slice.

Hence every designated visible future A witness is genuinely old-hole-nonuniform.

∎

### Corollary 8 — no role-only transition matrix is forced

For every pair of raw roles

\[
i\to j
\]

there is a structural finite-use self-avoiding model satisfying the retained local-cost theorem in which that role transition has no CHU certificate.

Therefore target correctness, syntactic self-avoidance, finite use, recurrent nontriple C and the P4-S046 local-cost theorem do not force any nonempty universal role-to-role CHU transition matrix.

In particular the crossed \(A_1/A_2\) rules do not, by themselves, force a recurrent \(C_0\) chain.

### Corollary 9 — finite use does not force collision escape

In the same model every later designated A witness is gated through the same old hole-dependent row.

Thus there need not be infinitely many future A candidates outside \(\operatorname{Coll}(s)\), even though:

- each individual use is finite;
- the local A evidence is visible on the target;
- the local freshness cost is \(0\) or \(1\);
- recurrent nontriple C is present.

This closes the bare finite-use route to automatic current-hole-uniform recurrence.

The model is **structural only**. Its target is \(0^\omega\), not computably random. It is not a counterexample for the committed \(Y,M,X\).

## 10. Failure of uniformity does not itself reveal the old hole

Both old-hole simulations are run by the same computable program from the same observed live raw data, with \(h=0\) and \(h=1\) supplied as finite hypotheses.

Suppose one branch produces a future A rejection and the other branch diverges.

That fact does **not** by itself say which branch is the actual source. The successful branch computation can be run and observed regardless of the actual value \(X(s)\), because its current-block oracle answers were supplied from the hypothesis rather than read from \(s\).

The old-row-gated countermodel makes this explicit: the \(h=0\) simulation always sees the visible A witness and the \(h=1\) simulation always stalls, but this asymmetry is built into the two counterfactual simulations and does not observe the actual raw sentinel.

A computable prediction of the current hole would require additional finite evidence eliminating one current completion itself. For example, if one \(h\)-completion receives a finite wrong/nonbinary refutation of an equation which target correctness guarantees for the actual source, then that completion is impossible and the other hole bit is predicted.

That is a genuine current-sentinel finite-refutation resource of the P4-S039/P4-S043 type.

No such elimination follows from the mere statement

\[
\text{future certificate uniformity fails}.
\]

Therefore P4-S047 obtains no direct computable-randomness contradiction from branch nonuniformity and does not reopen a generic martingale compiler.


## 10A. Global branch refutation predicts the current sentinel

The preceding guard can be sharpened into a source-side extraction theorem.

### Definition 10A — partial fixed-point completion

For a current raw completion \(h\), call \(Y^{[h]}\) a **partial fixed point** of \(M\) when, for every input \(n\),

\[
M^{Y^{[h]}}(n)\downarrow
\quad\Longrightarrow\quad
M^{Y^{[h]}}(n)=Y^{[h]}(n)\in\{0,1\}.
\]

Thus every defined equation is correct. Divergence is allowed.

The actual completion is a total fixed point because \(M^Y(n)=Y(n)\) for every \(n\).

### Lemma 10B — finite branch refutation exposes the old bit

Suppose, while raw sentinel \(s=(b,i)\) is unread, there are \(h\in\{0,1\}\) and an input \(n\) such that

\[
M^{Y^{[h]}}(n)\downarrow
\]

with either a nonbinary output or an output different from \(Y^{[h]}(n)\).

Then \(h\) is not the actual current raw bit. Hence

\[
X(s)=1-h.
\]

Moreover this conclusion is positively discoverable without querying \(s\).

#### Proof

The actual branch is \(Y\), and target correctness gives

\[
M^Y(n)\downarrow=Y(n)\in\{0,1\}.
\]

Therefore an \(h\)-branch wrong/nonbinary halt proves that branch cannot be the actual source completion.

To discover the event, dovetail the two candidate computations. When a simulation queries the old block, answer from the finite \(h\)-hypothesis. Every other virtual oracle value can be obtained from raw coordinates outside \(s\). The expected bit \(Y^{[h]}(n)\) is also computable from the same legal data: if \(n\) lies in the old block use the finite completion; otherwise its raw support is disjoint from \(s\).

Thus no live query of the current sentinel is required. ∎

This is strictly stronger than observing that one future A-certificate search succeeds and another diverges. The latter may contain no wrong equation for either current completion.

### Theorem 10C — canonical global-refutation one-hole scan

There is a total computable adaptive no-repeat one-hole scan \(S_{\rm ref}\) with the following target behavior.

At each epoch:

1. choose the least fresh raw coordinate \(s\) as the current sentinel;
2. query no value of \(s\);
3. dovetail, for both \(h=0,1\) and all inputs \(n\), the computations
   \[
   M^{Y^{[h]}}(n);
   \]
4. answer old-block virtual queries from the finite \(h\)-hypothesis and acquire every other required raw value live;
5. simultaneously perform a least-fresh zero-stake sweep of all raw coordinates other than \(s\);
6. if Lemma 10B produces a finite refutation of branch \(h\), bet all current capital on
   \[
   X(s)=1-h,
   \]
   query \(s\), and start the next epoch at the least fresh coordinate.

If no branch refutation ever appears, the current epoch continues forever and the sweep queries every raw coordinate except \(s\).

Hence every complete transcript omits at most one raw coordinate.

On the actual \(X\), at most the false branch can be finitely refuted. Every wager made by \(S_{\rm ref}\) is therefore correct.

If every target epoch resolves, the associated computable output martingale doubles once per epoch and succeeds.

Consequently

\[
X\in OH
\Longrightarrow
\text{the target run of }S_{\rm ref}\text{ eventually reaches an unresolved epoch}.
\]

At that unresolved epoch the false raw-radius-one completion is a partial fixed point of \(M\).

#### Proof

Computability and no-repeat follow by caching every queried raw coordinate and interleaving the universal dovetail with the least-fresh sweep.

If an epoch never resolves, the sweep eventually consumes every raw coordinate other than the sentinel, so the resulting complete transcript has exactly one hole.

If an epoch resolves, the sentinel is consumed and the least-fresh choice ensures progress. On an infinite sequence of resolved epochs every coordinate is eventually queried.

Fair-coin preservation is the settled no-repeat scan fact: every output cylinder fixes the same number of distinct fair source bits.

Lemma 10B makes every nonzero wager correct. If all epochs resolve, capital doubles infinitely often. Therefore a source in \(OH\) cannot have all epochs resolve.

At the first unresolved target epoch, neither \(h\)-completion has any finite wrong/nonbinary equation. The actual completion is total correct. Hence the other, false completion is a partial fixed point. ∎

### Corollary 10D — the surviving old-hole sensitivity is divergence-only at the global equation level

Along the canonical refutation scan, a hypothetical

\[
X\in OH
\]

forces a current raw-radius-one neighbour \(Z\) of \(Y\) such that

\[
M^Z(n)\downarrow\Longrightarrow M^Z(n)=Z(n)
\]

for every \(n\), while \(M^Z\) may be partial.

Thus finite wrong-halt sensitivity is harvestable. The genuinely surviving source-side obstruction is a false completion which is globally self-consistent wherever defined and can differ from the actual source only through divergence / nontermination of equations.

This does not prove \(X\in OH\). It gives a sharper necessary obstruction under that hypothesis.


## 11. The current-hole-uniform certification graph

Refine the P4-S046 usable certification graph.

A node records a prospective raw sentinel role together with the finite legal scan state at which it is the sole protected current hole.

A directed edge

\[
s\longrightarrow t
\]

is a **CHU usable edge** when a positively discovered certificate of the form in Definition 1:

1. predicts the future sentinel \(t\) with the same value under both current-hole hypotheses;
2. never reads \(s\);
3. preserves \(t\);
4. legally acquires every other finite raw support value;
5. closes the old sentinel after the positive event with the certified correct wager;
6. has a total one-hole fallback on all no-event continuations;
7. restores the finite state required to begin the next node with \(t\) as the unique protected sentinel.

Keep separate:

- semantic edge existence;
- finite positive edge discovery;
- a computable outgoing-edge selector which is itself globally one-hole legal;
- an infinite computable CHU usable path.

Positive c.e. discovery of individual candidate edges does not automatically yield a legal dovetail of all candidates: running many unresolved future-sentinel searches in parallel can itself recreate the multiple-protected-hole problem.

### Theorem 10 — CHU path theorem

If there is one computable infinite CHU usable path for the actual \(X\), then

\[
X\notin OH.
\]

#### Proof

Concatenate the certified edge protocols.

At each completed edge the scan keeps exactly the current sentinel unresolved until the positive uniform certificate is obtained. The certificate predicts the same future raw bit under both old-hole hypotheses, so the program never needs to read the old sentinel in order to know the wager or validate the future handoff.

The old sentinel is then queried with a certified correct wager or otherwise legally closed as specified by the edge protocol, while the future sentinel remains fresh and becomes the unique next protected hole.

The fallback clause makes the concatenated scan total and globally one-hole even on branches where the next positive event never appears. No coordinate is repeated.

A computable output martingale holds on zero-stake support queries and makes the certified correct positive wagers supplied by the usable path. By the definition of an infinite usable path, these wagers occur indefinitely with the success schedule encoded in the path, so the martingale is unbounded.

Hence the resulting total computable adaptive no-repeat one-hole scan destroys computable randomness of \(X\), proving \(X\notin OH\). ∎

The theorem is one-way. A source-relative infinite graph, infinitely many semantic CHU edges, finite out-degree, or a c.e. edge relation without a legal computable selector does not supply such a path.

## 12. What the committed source does and does not force

For the actual committed \(M,Y,X\), P4-S047 has two positive sufficient mechanisms:

1. safe-trace CHU certification;
2. two-branch future fixedness plus two-branch raw-adjacent rejection.

The retained authority does not establish either mechanism infinitely often.

The alternate current-hole completion is a raw-radius-one perturbation of \(X\), hence its virtual image is one of the finite perturbations already known from P4-S041/P4-S042 to permit partiality and remote dependence.

The wtt use bound controls the finite coordinates a future computation may read. It does not force those coordinates to avoid the old block, does not force the counterfactual computation to halt, and does not force its output to agree with the actual-source computation.

Theorem 7 shows that these missing properties cannot be recovered from the abstract machine hypotheses alone.

Therefore P4-S047 does **not** prove:

\[
X\notin OH,
\]

because no infinite computable CHU usable path is constructed.

It also does **not** prove:

\[
X\in OH.
\]

Failure of current-hole-uniform certification is an obstruction to this extraction mechanism, not a membership certificate.

No OH non-invariance witness is obtained and no strict

\[
R_2\subsetneq OH
\]

conclusion is available.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains available but ambiguity mass is not reinstated as an invariant.

## 13. Exact new boundary

P4-S046 showed that the future target block itself costs at most one raw bit.

P4-S047 shows that the older open hole introduces an independent branch-stability problem.

The positive boundary is:

\[
\boxed{
\text{safe old-row traces}
\quad\text{or}\quad
\text{two-branch future fixedness}
}
\]

together with compatible raw-adjacent rejection and a total one-hole handoff.

The negative structural boundary is:

\[
\boxed{
\text{one old hole-dependent virtual row can gate every later low-cost A witness}
}
\]

without violating target correctness, syntactic self-avoidance or finite use.

Thus the remaining actual-source resource is not merely current-hole collision. It is the **persistence and effective escape of old-hole sensitivity through future A-certificate computations**.

A hypothetical \(X\in OH\) can survive this line only if every computable attempt to build a CHU path is eventually blocked by old-hole sensitivity, future-target/fallback failure, or lack of effective edge choice. This is a necessary obstruction, not a proof of membership.

## 14. Next bounded target

P4-S048 should attack **persistent partial-fixed-point old-hole sensitivity on the actual committed source**, not repeat generic support enumeration.

For a current sentinel \(s\), classify future A computations according to whether the two old-hole completions:

1. have identical finite traces on all required equations;
2. both halt with the same target-correct future values;
3. both produce compatible A rejection evidence despite different traces;
4. disagree finitely;
5. or exhibit branch partiality/divergence.

The central question is whether one fixed raw-radius-one perturbation can remain an essential gate for infinitely many later A certificates on the actual computably random wtt-autoreducible source without itself yielding a finite prediction of the current raw sentinel.

Useful targets include:

- a theorem that old-hole sensitivity has only finitely many future A consequences, or is computably escapable, which would feed the CHU graph and potentially give \(X\notin OH\);
- a theorem that hypothetical \(X\in OH\) forces a persistent old-hole sensitivity pattern along every computable usable attempt;
- an exact finite target-trace characterization of when a future computation really depends on the old hole, distinguishing syntactic fan-out from semantic influence;
- or a structural model showing persistent semantic influence can coexist with all retained source-side local laws without exposing the old bit.

Do not return to a generic reverse-dependency closure theorem. The object is specifically the branch sensitivity of future A-certificate computations to one currently open raw coordinate.

## Guards

All validated mathematics through P4-S046 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

Phase 4 remains OPEN. Phase 5 remains CLOSED.

No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.
