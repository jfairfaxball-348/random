# P4-S048 — partial-neighbour role kernels and recurrent divergence gates

Date: 2026-10-07
Session: P4-S048
Incoming checkpoint: caba6f96b665e067661750e40e08164fb959968c
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding

Result: **AT AN UNRESOLVED GLOBAL-REFUTATION EPOCH, THE FALSE RAW-RADIUS-ONE COMPLETION IS A PARTIAL FIXED POINT, SO FINITE WRONG-OUTPUT SENSITIVITY DISAPPEARS. EVERY DIVERGENCE-SENSITIVE FUTURE TARGET EQUATION HAS A FINITE TARGET-TRACE CONTACT WITH THE OLD CHANGED SUPPORT AND THEN ENTERS A SHARP TWO-ARM SUPPORT LASSO: LOCAL DIVERGENCE OR A CORRECT-HALTING OLD-SUPPORT CYCLE. FOR THE CANONICAL P4-S046 LOW-COST A CERTIFICATES, FALSE-BRANCH TARGET FIXEDNESS REDUCES TO THE FINITE ROLE LISTS \(F_0=\{q_0,q_1,q_2\}\), \(F_1=\{q_0\}\), \(F_2=\{q_1\}\), SEPARATE FROM THE FALSE-BRANCH RAW-ADJACENT REJECTION. TWO RECURRENT FINITE-USE SELF-AVOIDING STRUCTURAL FAMILIES SHOW THESE TWO REQUIREMENTS ARE INDEPENDENT EVEN WHEN THE FALSE NEIGHBOUR IS A GLOBAL PARTIAL FIXED POINT: ONE FIXED OLD ROW CAN MAKE A LISTED TARGET EQUATION DIVERGE FOREVER WHILE RAW-ADJACENT REJECTION SURVIVES, OR THE FALSE NEIGHBOUR CAN EVEN BE A TOTAL FIXED POINT WHILE EVERY FALSE-BRANCH RAW-ADJACENT FUTURE CANDIDATE DIVERGES. THEREFORE PARTIAL FIXEDNESS DOES NOT FORCE EFFECTIVE CHU ESCAPE. A TOTAL COMPUTABLE CANONICAL ESCAPE OPERATOR WOULD STILL YIELD AN INFINITE CHU PATH AND \(X\notin OH\); HYPOTHETICAL \(X\in OH\) FORCES EVERY SUCH OPERATOR TO FAIL ON A REACHED NODE. NO CHU PATH, NO \(X\in OH\) PROOF, AND NO SEPARATION IS OBTAINED.**

## Authority, uniqueness and frozen scope

Live `main` was pinned at

\[
\texttt{caba6f96b665e067661750e40e08164fb959968c},
\]

the exact P4-S047 outgoing checkpoint. There was no mismatch. Direct path inspection showed that `phase4/P4-S048_MATHEMATICS.md` did not exist, so P4-S048 was unused.

P4-S001 through P4-S047, the required CAND-01 authority, `phase4/P4_RESEARCH_PIVOT_AFTER_S031.md`, and P4-S032 through P4-S047 were read at the pinned state, with special attention to P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S047.

All validated mathematics through P4-S047 is frozen. The ticket/reserve/frontier/recycling sequence, backward-price route, ordinary raw-martingale compilation, ambiguity mass, generic radius-one totalization, generic reverse-dependency closure, and the previously closed local-enumeration/timing/same-block-cost routes are not reopened.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR,
\]

and, for the displayed repeated block recoding \(H\),

\[
X=H^{-1}(Y)\in CR,\qquad H(X)=Y\notin OH.
\]

The statement \(X\in OH\) remains unresolved.

## 1. The false partial neighbour

Fix an unresolved epoch of the P4-S047 global-refutation scan \(S_{\rm ref}\). Let the current raw sentinel be

\[
s=(b,i).
\]

For mathematical analysis only, let

\[
h_*=X(s),\qquad \bar h=1-h_*,
\]

and write

\[
Z=Y^{[\bar h]}.
\]

No live construction below uses \(h_*\) or \(\bar h\) as a program parameter. Live procedures still simulate both finite hole hypotheses symmetrically.

Let

\[
S_i=\{q_{b,r}:r\in\operatorname{Dep}(i)\}.
\]

Then \(Z\) and \(Y\) differ exactly on \(S_i\), with

\[
|S_0|=3,\qquad |S_1|=|S_2|=2.
\]

By the P4-S047 global-refutation theorem,

\[
M^Z(n)\downarrow\Longrightarrow M^Z(n)=Z(n)\in\{0,1\}
\qquad(\forall n).
\]

Thus \(Z\) is a global partial fixed point. The target \(Y\) is total and correct.

This removes exactly one of the three P4-S042 support-lasso arms: a finite wrong/nonbinary halt on \(Z\) is impossible.

## 2. Exact future-equation sensitivity trichotomy

Fix \(n\notin B_b\). Then

\[
Y(n)=Z(n).
\]

Let \(T_Y(n)\) be the finite target trace of

\[
M^Y(n)\downarrow=Y(n).
\]

Exactly one of the following occurs.

### Type I — trace-safe

The target trace does not query \(S_i\).

Then \(Y\) and \(Z\) give the same answer to every query made by the target computation. Hence

\[
M^Z(n)\downarrow=Y(n)=Z(n)
\]

with the identical finite trace.

### Type II — trace-sensitive but value-fixed

The target trace queries \(S_i\), and

\[
M^Z(n)\downarrow.
\]

Partial fixedness forces

\[
M^Z(n)=Z(n)=Y(n).
\]

The two computations may take different finite paths after the first changed-row answer, but both halt with the same correct value.

### Type III — divergence-sensitive

\[
M^Y(n)\downarrow=Y(n),
\qquad
M^Z(n)\uparrow.
\]

By the P4-S042 first-contact theorem, \(T_Y(n)\) must query at least one member of \(S_i\). If \(p\in S_i\) is the first such query, the \(Y\)- and \(Z\)-computations have identical states, queries and answers up to that query, and first receive different oracle answers at \(p\).

There is no fourth finite wrong-output type at an unresolved epoch, because any such halt would have refuted the false completion already.

This keeps distinct:

- **syntactic fan-out:** the target trace queries \(S_i\);
- **semantic sensitivity:** the \(Z\)-computation does not have the identical trace;
- **divergence sensitivity:** the target halts but \(Z\) diverges.

Only the last is the surviving target-equation obstruction.

## 3. Partial fixedness sharpens the support lasso

The P4-S042 support-lasso theorem allowed three outcomes after entering the old changed support: finite local refutation, local divergence, or a correct-halting cycle.

Partial fixedness deletes the first arm.

### Theorem 1 — partial-fixed-point lasso dichotomy

Suppose \(n\notin B_b\) is divergence-sensitive:

\[
M^Y(n)\downarrow,\qquad M^Z(n)\uparrow.
\]

Then the target trace reaches \(S_i\) in one finite first-contact step. Thereafter, following target-trace first differences on inputs in \(S_i\), exactly one of the following occurs.

1. **Old-support divergence.** For some reached \(q\in S_i\),
   \[
   M^Z(q)\uparrow.
   \]
2. **Correct-halting old-support cycle.** Every reached \(q\in S_i\) halts correctly on \(Z\); the finite first-difference walk therefore repeats and enters a directed cycle inside \(S_i\).

No finite-refutation arm is possible.

#### Proof

Let \(q\in S_i\) be reached. If \(M^Z(q)\uparrow\), arm 1 holds.

Otherwise partial fixedness gives

\[
M^Z(q)=Z(q).
\]

Since \(q\in S_i\),

\[
Z(q)=1-Y(q),
\]

while

\[
M^Y(q)=Y(q).
\]

The two correct computations therefore halt with different outputs. Syntactic self-avoidance forbids either computation from querying its own input \(q\). Hence the target computation must query another changed coordinate in

\[
S_i\setminus\{q\}
\]

before the two computations can differ. Draw the corresponding first-difference edge and iterate.

If arm 1 never occurs, the walk is infinite on the finite set \(S_i\), hence repeats and enters a directed cycle. ∎

For \(i=1\) and \(i=2\), if both old changed-coordinate computations halt, the cycle is the forced two-cycle already identified in P4-S041. For \(i=0\), the correct-halting geometry is the P4-S041 two-cycle-with-tail or oriented three-cycle.

Thus partial fixedness gives a sharper lasso, but not a descent. Remote divergence may remain attached to a closed correct old-support cycle.

## 4. The exact finite role lists for canonical low-cost A certification

Keep the P4-S046 notation

\[
d_0=A^{-1}e_0=110,\qquad
d_1=A^{-1}e_1=101,\qquad
d_2=A^{-1}e_2=111.
\]

For a future block

\[
B_c=\{q_{c,0},q_{c,1},q_{c,2}\},
\]

write \(q_r=q_{c,r}\) when the block is clear.

For the false old-hole branch, let

\[
R_j^Z(c)
\]

denote the positive event that the future raw-adjacent candidate \(x^{(c)}+e_j\) receives a finite wrong/nonbinary local rejection when the old block is completed as \(Z\).

This event concerns the doubly perturbed oracle: the false old completion plus the future raw-adjacent perturbation. It is not a statement about \(M^Z\) itself.

### Lemma 2 — exact automatic-trace criterion under a partial neighbour

For each \(r<3\), consider the future candidate \(x^{(c)}+d_r\) in the false old-hole branch.

Its virtual oracle differs from \(Z\) only at \(q_r\). Because the input-\(q_r\) computation syntactically avoids \(q_r\), the canonical rejecting computation on that candidate is literally

\[
M^Z(q_r).
\]

Therefore

\[
M^Z(q_r)\downarrow
\]

is equivalent to existence of the **canonical P4-S046 automatic \(q_r\)-rejection trace** in the false branch.

When it halts, partial fixedness gives

\[
M^Z(q_r)=Z(q_r)=Y(q_r),
\]

which is opposite the unit-flipped candidate bit, so the candidate is rejected.

If it diverges, that canonical automatic trace is absent.

This is an equivalence only for the canonical self-avoidance trace. Another local equation could in principle reject the same candidate by a different witness; no global uniqueness claim is made.

### Definition 3 — canonical fixedness lists

Define

\[
F_0(c)=\{q_0,q_1,q_2\},
\]

\[
F_1(c)=\{q_0\},
\]

\[
F_2(c)=\{q_1\}.
\]

These are exactly the false-neighbour target equations needed by the P4-S046 **cost \(0,1,1\)** canonical slice packages:

- \(A_0\): wrong differences
  \[
  e_0,d_0,d_1,d_2;
  \]
- \(A_1\), after reading future \(x_2\): wrong differences
  \[
  e_1,d_0;
  \]
- \(A_2\), after reading future \(x_1\): wrong differences
  \[
  e_2,d_1.
  \]

### Theorem 4 — finite partial-neighbour role kernel

Fix a future actual \(A_j\) block \(B_c\).

Assume:

1. the false old-hole branch has the finite raw-adjacent rejection
   \[
   R_j^Z(c);
   \]
2. every equation in the role list halts:
   \[
   M^Z(q)\downarrow\qquad(q\in F_j(c)).
   \]

Then the false branch has the entire canonical P4-S046 low-cost rejection family for that role.

The target branch already has the corresponding canonical family by target correctness and the actual \(A_j\) witness.

Hence, if the live outside support, allowed future cross-read and total fallback/handoff also satisfy the P4-S047 CHU legality conditions, the block yields a CHU usable edge with the retained local cost

\[
A_0:0,\qquad A_1:1,\qquad A_2:1.
\]

#### Proof

The raw-adjacent wrong-slice candidate is rejected by assumption 1.

Every remaining wrong-slice candidate is one of the \(d_r\) listed above. Lemma 2 turns each halt in \(F_j(c)\) into its canonical false-branch automatic rejection. The target branch has the same automatic rejections by P4-S046.

The future raw target bit is unchanged by the old-hole completion, so both branch packages certify the same future sentinel value. The remaining requirements are exactly the already separated live-support/fallback requirements of CHU. ∎

### Exact boundary of the theorem

Within this canonical witness package, once \(R_j^Z(c)\) is positively available, failure of the fixedness part is exactly divergence of at least one member of \(F_j(c)\).

This does **not** say:

- every CHU certificate must use these traces;
- failure of one listed halt rules out every alternative rejection trace;
- partial fixedness of \(Z\) forces \(R_j^Z(c)\).

The last point is the next structural boundary.

## 5. Persistent sensitivity set for future A

Define the source-specific canonical fixedness-sensitivity set at the current sentinel by

\[
\operatorname{Sens}^{\rm fix}_A(s)
=
\{(c,j,q):
q\in F_j(c),\
B_c\text{ is a prospective actual }A_j\text{ target},\
M^Z(q)\uparrow
\}.
\]

Because \(M^Y(q)\downarrow\), every member is a genuine Type-III divergence-sensitive future target equation.

This set is deliberately narrower than all inputs of \(M\).

Also keep separate:

- \(\operatorname{Fan}_A(s)\): listed target traces which merely contact \(S_i\);
- \(\operatorname{Sens}^{\rm fix}_A(s)\): listed target equations which actually diverge on \(Z\);
- **raw-adjacent branch sensitivity:** failure or divergence in the false-branch computations witnessing \(R_j^Z(c)\);
- **canonical certificate-essential sensitivity:** a listed divergence for which the raw-adjacent rejection, every other listed halt, support acquisition and fallback have already positively resolved, so that this one divergence is the sole missing item in the canonical role kernel.

The last notion is relative to the canonical P4-S046 package. It is not identified with semantic essentiality among every conceivable CHU witness language.

By Theorem 1, every member of \(\operatorname{Sens}^{\rm fix}_A(s)\) has a finite target-trace first contact with \(S_i\). That positive contact does not positively certify the divergence.

## 6. The two finite obstructions are independent

Partial fixedness controls the listed target equations \(M^Z(q)\). It does not control the raw-adjacent candidate oracle used in \(R_j^Z(c)\).

This distinction is sharp.

### Theorem 5 — recurrent partial-fixed-point countermodels

Fix:

- a current raw role \(i\);
- one old changed virtual row
  \[
  p\in\operatorname{Dep}(i);
  \]
- a future A role \(j\in\{0,1,2\}\).

There are computable syntactically self-avoiding finite-use functionals on target

\[
Y_*=0^\omega
\]

with raw target \(X_*=0^\omega\) and false raw-radius-one neighbour

\[
Z_*=Y_*\oplus\chi_{S_i}
\]

having the following two recurrent behaviours on every designated future block.

#### Family F — fixedness divergence only

1. \(N^{Y_*}\) is total and correct.
2. \(Z_*\) is a global partial fixed point:
   \[
   N^{Z_*}(n)\downarrow\Longrightarrow N^{Z_*}(n)=Z_*(n).
   \]
3. The target branch has recurrent visible \(A_j\) with the retained P4-S046 local cost
   \[
   0,1,1
   \]
   for \(j=0,1,2\), using \(ACB,CAC,CCA\) respectively.
4. The false-branch raw-adjacent rejection \(R_j^{Z_*}(c)\) is finite and positive.
5. Exactly one required listed target equation is made divergence-sensitive: choose
   \[
   r_0=0,\qquad r_1=0,\qquad r_2=1,
   \]
   so
   \[
   q_{c,r_j}\in F_j(c)
   \]
   and
   \[
   N^{Z_*}(q_{c,r_j})\uparrow.
   \]
6. The target trace of that equation queries the same fixed old row \(p\) first on every future block.
7. The old changed support itself closes into a correct P4-S041 dependency cycle.

Thus one fixed old row can remain the first-contact divergence gate for infinitely many canonical future A kernels while the raw-adjacent rejection remains available.

#### Family R — raw-adjacent divergence only

1. \(N^{Y_*}\) is total and correct.
2. The false neighbour \(Z_*\) is in fact a **total global fixed point**.
3. Every listed target equation in every \(F_j(c)\) halts correctly on \(Z_*\), so every canonical automatic unit-flip rejection survives.
4. The target branch still has recurrent visible \(A_j\) with local cost \(0,1,1\).
5. On the false old-hole branch, every local computation on the future raw-adjacent candidate \(x^{(c)}+e_j\) diverges.
6. Hence \(R_j^{Z_*}(c)\) fails purely by candidate-level divergence on every designated future block.

Therefore two-branch fixedness of the false neighbour does not force compatible two-branch raw-adjacent A rejection.

#### Construction

Use one old block \(B_b\). Since

\[
S_i=\operatorname{supp}(c_i)
\]

has size two or three, define the old-block equations so that both \(Y_*\) and \(Z_*\) are correct fixed points there.

- If \(|S_i|=2\), let the two changed inputs query and copy each other.
- If \(|S_i|=3\), orient a three-cycle and let each changed input query and copy the next changed coordinate.
- Every unchanged old-block input outputs \(0\).

This is syntactically self-avoiding. On \(Y_*\), all copied bits are \(0\); on \(Z_*\), all changed bits are \(1\). Thus every old-block halt is correct in both oracles and the old support supplies the required correct dependency cycle.

On each future designated block, first query the fixed old row \(p\).

If the answer is \(0\), run the validated target gadget:

- \(ACB\) for \(j=0\);
- \(CAC\) for \(j=1\);
- \(CCA\) for \(j=2\).

Hence the \(Y_*\)-branch has exactly the retained visible A role and local cost.

For Family F, if \(p=1\):

- input \(q_{c,r_j}\) diverges;
- every other future target input outputs \(0\).

Choose a different local input \(a_j\in\operatorname{supp}(c_j)\) with

\[
a_0=1,\qquad a_1=1,\qquad a_2=0.
\]

On the false-branch raw-adjacent candidate, that input still outputs \(0\), while the candidate expects \(1\) at \(q_{c,a_j}\). Hence the raw-adjacent candidate is finitely rejected even though the designated listed target equation diverges.

For Family R, if \(p=1\), each future local input queries the other two coordinates of its own future virtual block. If both are \(0\), output \(0\); otherwise diverge.

On the false neighbour \(Z_*\), every future target block is \(000\), so every local equation halts correctly with \(0\).

For a unit virtual flip at \(q_{c,r}\), the input-\(q_{c,r}\) computation does not read its own flipped bit and still sees the other two bits as \(00\); it outputs \(0\), giving the automatic rejection.

For the raw-adjacent perturbations

\[
c_0=111,\qquad c_1=011,\qquad c_2=101,
\]

every local input sees at least one \(1\) among its other two block coordinates. Hence every local computation diverges and no raw-adjacent finite rejection appears.

Every other input outputs \(0\). All uses are finite and computably bounded. ∎

### Corollary 6 — no abstract persistent-sensitivity escape

Target correctness, syntactic self-avoidance, computable finite use, global partial fixedness of the false raw-radius-one neighbour, the P4-S041 dependency-cycle law, recurrent nontriple C, and the P4-S046 local-cost theorem do not force:

- eventual totality of the finite role lists;
- eventual false-branch raw-adjacent rejection;
- finitely many divergence-sensitive future A kernels;
- a computable bound beyond the last such kernel;
- or a computable CHU escape.

Family F shows that one fixed old changed row may gate infinitely many listed target equations while the old support itself is already closed into a correct cycle.

Family R shows something strictly different: even a false neighbour which is a total global fixed point need not preserve the raw-adjacent future A rejection.

Both models are structural only. Their target is computable, not computably random. They do not settle the committed source.

## 7. What the actual computably random source adds — and does not yet add

For the committed source, a finite wrong/nonbinary halt under one current completion is already harvestable by P4-S047 and cannot survive at an unresolved epoch.

A divergence-sensitive equation gives no analogous positive event.

Suppose for a future \(n\) that semantically

\[
M^Y(n)\downarrow,\qquad M^Z(n)\uparrow.
\]

A live symmetric simulation can eventually observe the halt in the actual branch. At that finite time, however, the other branch may merely be slower. Its absence of a halt is not c.e.

Therefore the event

\[
M^Z(n)\uparrow
\]

does not itself supply a finite elimination of the false completion.

The same applies to the absence of \(R_j^Z(c)\): a raw-adjacent false-branch rejection may be delayed forever, but failure to see it does not distinguish acceptance from divergence.

No contradiction with computable randomness follows merely from:

- infinitely many target traces contacting the old support;
- infinitely many semantically divergent false-branch equations;
- or one fixed old row being queried on infinitely many target traces.

A concrete positive finite prediction/test would still be required.

The P4-S041 truth-table collapse also does not apply here. It required totality on **every** finite perturbation. A single false radius-one partial fixed point with an infinite divergence set is fully compatible with failure of that premise.

## 8. Exact effective escape criterion

The finite role kernels do give a clean conditional positive theorem.

### Definition 7 — canonical partial-neighbour escape operator

A **canonical partial-neighbour escape operator** is one total computable one-hole-safe procedure which, from every reached current-sentinel state, returns a future role \((c,j)\) together with finite positive data establishing:

1. the same future raw sentinel prediction in both old-hole branches;
2. the false- and true-branch raw-adjacent rejections required by the role;
3. halting of every listed target equation in
   \[
   F_j(c)
   \]
   in both old-hole branch simulations;
4. the allowed P4-S046 future cross-read only: no read for \(A_0\), future \(x_2\) for \(A_1\), future \(x_1\) for \(A_2\);
5. no live read of the current or future sentinel;
6. a syntactically certified total one-hole fallback and legal handoff.

The operator must actually terminate on every reached target state. Semantic existence of a suitable later block is not enough.

### Theorem 8 — effective escape gives a CHU path

If a canonical partial-neighbour escape operator exists for every node reached from the current construction, then its successive outputs form an infinite computable CHU usable path.

Hence

\[
X\notin OH.
\]

#### Proof

At each node, items 2 and 3 complete the finite role kernel of Theorem 4 under both old-hole hypotheses. Items 1 and 4–6 are exactly the remaining CHU legality and handoff conditions.

Thus every returned transition is a positively certified CHU usable edge. Total computable termination at every reached node makes the edge sequence computable and infinite. Apply the retained P4-S047 CHU usable-path theorem. ∎

### Corollary 9 — exact algorithm-relative obstruction under hypothetical \(X\in OH\)

Assume hypothetically

\[
X\in OH.
\]

Then no total canonical partial-neighbour escape operator can succeed at every reached node.

More narrowly, fix any globally one-hole-legal computable attempt whose only possible permanent wait, after the raw-adjacent rejection and fallback conditions have positively resolved, is waiting for the finite role-list equations. If the attempt is permanently captured at a future role \((c,j)\), then

\[
M^Z(q)\uparrow
\]

for at least one

\[
q\in F_j(c).
\]

This is an algorithm-relative necessary obstruction.

It does **not** imply that \(\operatorname{Sens}^{\rm fix}_A(s)\) is semantically infinite. One permanently divergence-sensitive proposed block can trap one computable attempt forever.

Likewise, even if \(\operatorname{Sens}^{\rm fix}_A(s)\) were semantically finite, no effective escape follows without a computable procedure which finds a candidate beyond it while preserving the one-hole constraints.

Finiteness alone does not reveal the last bad candidate.

## 9. Certification-graph refinement

At an unresolved partial-fixed-point node, a canonical CHU edge now has two separately visible finite kernels:

\[
\boxed{\text{raw-adjacent two-branch rejection}}
\]

and

\[
\boxed{\text{finite false-neighbour target-equation list }F_j}.
\]

The second kernel has exact role sizes

\[
|F_0|=3,\qquad |F_1|=|F_2|=1.
\]

This is strictly sharper than requiring full three-equation two-branch fixedness for every role.

But the two structural families show that neither kernel forces the other.

Therefore a source-relative graph may have infinitely many semantic candidate edges while still lacking a computable outgoing selector. No computable path is inferred from:

- semantic cofinality;
- finite branching;
- c.e. positive pieces;
- finiteness of the bad set without a computable bound;
- or partial fixedness of the false neighbour.

## 10. Separation status and exact boundary

P4-S048 proves a genuine sharpening of the P4-S047 boundary:

\[
\boxed{
\text{partial fixedness removes finite refutation from target equations,}
}
\]

but

\[
\boxed{
\text{it does not remove recurrent divergence gating.}
}
\]

For the canonical low-cost roles, the false-neighbour fixedness burden is now exactly

\[
A_0:\{q_0,q_1,q_2\},
\qquad
A_1:\{q_0\},
\qquad
A_2:\{q_1\},
\]

plus the logically separate false-branch raw-adjacent rejection.

One fixed old changed row can remain the first target-trace contact for recurrent listed divergence while the old support closes into a correct local dependency cycle.

Conversely, even total fixedness of the false neighbour does not force the raw-adjacent rejection on the two-bit-perturbed future candidate.

No infinite computable CHU usable path is constructed for the committed source.

Therefore P4-S048 proves neither

\[
X\notin OH
\]

nor

\[
X\in OH.
\]

No OH non-invariance theorem and no strict \(R_2\subsetneq OH\) conclusion are claimed. The sustained target remains

\[
R_2=OH\;?
\]

Retain \(OH^{iso}\) as the comparison class.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. Phase 4 remains OPEN; Phase 5 remains CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## Next bounded question

The new irreducible finite object is the **two-raw-bit square** formed by:

- the actual target \(Y\);
- the false old partial neighbour \(Z\);
- a future raw-adjacent A candidate on the actual branch;
- the same future raw perturbation applied to \(Z\).

P4-S049 should attack whether the committed source imposes any positive finite constraint on this square beyond P4-S048's two independent kernels, and in particular whether persistent failure of the false-branch raw-adjacent rejection can be converted into a new partial-fixed-point web, a finite branch refutation, a computable old-bit prediction, or an effective CHU escape.

Do not infer such a constraint from partial fixedness alone: Family R shows that the false old neighbour may be a total fixed point while the doubly perturbed raw-adjacent branch remains divergence-only.
