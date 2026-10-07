# P4-S049 — square column shielding and finite-tenure escape obstruction

Date: 2026-10-07
Session: P4-S049
Incoming checkpoint: ab8136c67eb772821b1fcc40a17e3b877ad32119
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding

Result: **AT AN UNRESOLVED P4-S047 OLD-HOLE EPOCH, THE TWO CORNERS IN THE ACTUAL FUTURE-BIT COLUMN ARE THE TOTAL FIXED TARGET \(Y\) AND THE FALSE OLD COMPLETION \(Z\), WHICH IS A GLOBAL PARTIAL FIXED POINT. HENCE THAT ENTIRE COLUMN IS IMMUNE TO FINITE WRONG/NONBINARY REFUTATION. CONSEQUENTLY ONE FINITE REFUTATION ANYWHERE IN THE TWO-RAW-BIT SQUARE ALREADY IDENTIFIES THE WRONG FUTURE-BIT COLUMN AND POSITIVELY PREDICTS THE FUTURE RAW BIT, WITHOUT KNOWING THE OLD BIT AND WITHOUT REQUIRING A FOURTH-CORNER REJECTION. IN PARTICULAR, EVERY ACTUAL FUTURE CASE-\(A_j\) RAW-ADJACENT REJECTION IS SUCH A ONE-REFUTATION FUTURE-BIT CERTIFICATE EVEN IF THE FALSE FOURTH CORNER IS LOCALLY SELF-CONSISTENT OR DIVERGENCE-ONLY. A LOCALLY CASE-B FOURTH CORNER ALSO FORCES THE P4-S041 ROLE-SWITCH REFUTATIONS IN THE FALSE OLD ROW. HOWEVER THE PREMISE THAT THE OLD EPOCH IS GENUINELY UNRESOLVED IS SEMANTIC AND NOT POSITIVELY RECOGNIZABLE. WHILE THE OLD SENTINEL REMAINS OPEN, EVERY PROSPECTIVE FUTURE SENTINEL MUST THEREFORE BE ONLY TRANSIENTLY RESERVED ON A GLOBALLY LEGAL NO-EVENT BRANCH; ARBITRARILY LATE FINITE SQUARE REFUTATIONS CAN OUTRUN EVERY COMPUTABLE FINITE-TENURE POLICY. IF \(X\in OH\), THEN AT THE FIRST TRAPPED OLD EPOCH EVERY COMPUTABLE FINITE-TENURE SQUARE-RESERVATION POLICY CATCHES ONLY FINITELY MANY REFUTATIONS. A SQUARE WITH NO GLOBAL FINITE REFUTATION HAS ALL FOUR CORNERS AS GLOBAL PARTIAL FIXED POINTS. A SHARPER COMPUTABLE STRUCTURAL MODEL REALIZES RECURRENT FULL TWO-ROW RADIUS-ONE PARTIAL-FIXED STARS, SO SELF-AVOIDANCE AND PARTIAL FIXEDNESS ALONE DO NOT FORCE A SQUARE EVENT. NO COMPUTABLE INFINITE ESCAPE, NO \(X\in OH\) PROOF, AND NO SEPARATION IS OBTAINED.**

## Authority, uniqueness and frozen scope

Live main was pinned at

\[
\texttt{ab8136c67eb772821b1fcc40a17e3b877ad32119},
\]

the exact P4-S048 outgoing checkpoint. There was no mismatch. Direct path inspection showed that phase4/P4-S049_MATHEMATICS.md did not exist, so P4-S049 was unused.

P4-S001 through P4-S048, the required CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S048 were read at the pinned state, with special attention to P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S048.

All validated mathematics through P4-S048 is frozen. In particular, the ticket/reserve/frontier/recycling line, backward-price line, ordinary raw-martingale compilation, ambiguity mass, generic radius-one totalization, generic reverse-dependency closure, detached A/B/C enumeration, certificate-time bounding and same-block freshness-cost enumeration are not reopened.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR,
\]

and, for the displayed repeated block recoding \(H\),

\[
X=H^{-1}(Y)\in CR,\qquad H(X)=Y\notin OH.
\]

The statement \(X\in OH\) remains unresolved.

Fix the recoding columns

\[
c_0=111,\qquad c_1=011,\qquad c_2=101.
\]

At an unresolved P4-S047 global-refutation epoch let the old raw sentinel be

\[
s=(b,i).
\]

For proof only write

\[
\alpha=X(s).
\]

The actual completion is \(Y\), while the false old completion \(Z\) is a global partial fixed point:

\[
M^Z(n)\downarrow\Longrightarrow M^Z(n)=Z(n)\in\{0,1\}
\qquad(\forall n).
\]

No live construction below uses \(\alpha\), the false old value, or any future actual bit as a program parameter.

## 1. The two-raw-bit square and generic pair elimination

Fix a future raw coordinate

\[
t=(c,j),\qquad c\ne b.
\]

For \(a,\beta\in\{0,1\}\), let

\[
W_{a,\beta}
=
H(X\text{ with }X(s)=a,\ X(t)=\beta),
\]

with every other raw coordinate left at its target value.

A **finite pair refutation** of \((a,\beta)\) is a finite computation

\[
M^{W_{a,\beta}}(n)\downarrow
\]

whose output is nonbinary or differs from \(W_{a,\beta}(n)\).

This is positive finite information. It is discoverable by symmetric simulation of the four pair hypotheses without querying either hypothesized raw coordinate.

### Lemma 1 — pair elimination

A finite pair refutation eliminates \((a,\beta)\) from being the actual raw pair.

#### Proof

For the actual pair \((X(s),X(t))\), the oracle is exactly \(Y\). Target correctness gives

\[
M^Y(n)\downarrow=Y(n)\in\{0,1\}
\]

for every \(n\). Hence a wrong or nonbinary halt under \(W_{a,\beta}\) proves that \(W_{a,\beta}\ne Y\), so the raw pair \((a,\beta)\) is impossible. ∎

### Corollary 2 — generic row/column elimination

Finite pair refutations give the exact positive square logic:

1. if both \((a,0)\) and \((a,1)\) are finitely refuted, then
   \[
   X(s)=1-a;
   \]
2. if both \((0,\beta)\) and \((1,\beta)\) are finitely refuted, then
   \[
   X(t)=1-\beta.
   \]

No absence of a halt is used.

The second arm is exactly the generic two-row CHU column-elimination picture anticipated in the P4-S049 prompt: an actual-row rejection and a false-row rejection of the same future value exclude that future value independently of the old bit.

The next theorem shows that at a genuinely trapped old epoch this two-refutation column test is stronger than necessary.

## 2. Actual-column shielding at an unresolved old epoch

For proof only let

\[
\gamma=X(t).
\]

Then the two corners in the actual future-bit column are

\[
W_{\alpha,\gamma}=Y
\]

and

\[
W_{1-\alpha,\gamma}=Z.
\]

The first is a total fixed point of \(M\). The second is a global partial fixed point.

### Theorem 3 — actual-column shielding

At an unresolved old-hole epoch, neither corner in the actual future-bit column admits a finite pair refutation.

Equivalently,

\[
\operatorname{Ref}(a,\beta)
\Longrightarrow
\beta\ne X(t)
\]

for every finite square refutation.

#### Proof

The corner \(Y\) has no wrong/nonbinary equation by target correctness.

The corner \(Z\) has no wrong/nonbinary defined equation by the P4-S047 partial-fixed-point theorem retained through P4-S048.

These are exactly the two old-bit rows in the column \(\beta=\gamma\). ∎

### Theorem 4 — one-refutation future-bit prediction

At an unresolved old-hole epoch, one finite pair refutation of \(W_{a,\beta}\), for either old hypothesis \(a\), positively determines the future raw bit:

\[
\boxed{X(t)=1-\beta.}
\]

The rule does not require knowing the actual old bit.

#### Proof

By Theorem 3 the actual future-bit column contains no finite refutation. Therefore any observed refutation lies in the other column. Since the two future values are binary, the actual value is \(1-\beta\). ∎

This is strictly sharper than generic column elimination. The second refutation in the other old row is unnecessary once the old epoch is semantically known to be trapped.

### Corollary 5 — row elimination cannot occur at the trap

At an unresolved old epoch no fixed old row can have both future values finitely refuted.

Indeed each row contains one corner in the actual future-bit column, and that corner is unrefutable by Theorem 3.

Thus old-bit prediction by a two-refutation row elimination is not the square mechanism available at a trapped epoch. The source-specific square resource is future-bit prediction from a single positive refutation.

## 3. Every actual future A rejection is already a square prediction

Fix a future block \(B_c\) and raw role \(j\). Let

\[
Y_j=Y\oplus c_j^{(c)}
\]

be the actual-old-row raw-adjacent candidate.

If role \(j\) is actual Case A, then by definition some local equation on \(Y_j\) has a finite wrong/nonbinary halt.

But

\[
Y_j=W_{\alpha,1-\gamma}.
\]

### Theorem 6 — actual A gives a one-refutation future certificate

At an unresolved old-hole epoch, every actual future \(A_j\) raw-adjacent rejection positively predicts the future raw bit \(X(c,j)\) by Theorem 4.

No finite rejection of the fourth corner

\[
Z_j=Z\oplus c_j^{(c)}
\]

is required for this one-shot future-bit prediction.

#### Proof

The actual \(A_j\) witness is a finite pair refutation in the actual-old row. By actual-column shielding it cannot lie in the actual future-bit column, so its future hypothesis is the wrong value. The opposite bit is therefore the target value. ∎

This changes the interpretation of the P4-S048 two-kernel boundary.

For the older CHU certificate architecture, one needed compatible finite rejection packages in both old-hole rows, including a false-row raw-adjacent rejection.

For **square prediction at a trapped old epoch**, the actual-row A rejection alone suffices. The fourth corner may be:

1. finitely refuted;
2. locally self-consistent;
3. divergence-only.

All three give the same one-refutation prediction once \(Y_j\) has been finitely refuted.

This does not yet produce a globally reusable scan. The semantic trap premise and one-hole legality are handled below.

## 4. Fourth-corner classification and full partial-fixed squares

The P4-S049 trichotomy remains useful for classifying the false fourth corner.

For a future actual \(A_j\) block, classify \(Z_j\) locally as:

1. **finite-refuted:** a required local equation halts wrong/nonbinary;
2. **locally self-consistent:** the full local block equations under consideration halt with the \(Z_j\)-assigned values;
3. **divergence-only:** no local finite refutation appears and at least one required local equation diverges.

Only case 1 is a second positive pair elimination. Cases 2 and 3 do not weaken Theorem 6, because its prediction already comes from the \(Y_j\) refutation.

For global square behavior there is a sharper semantic statement.

### Proposition 7 — no-refutation square is a full partial-fixed square

Suppose, at an unresolved old epoch and a fixed future \(t\), that none of the four corners \(W_{a,\beta}\) has any global finite wrong/nonbinary equation.

Then every square corner is a global partial fixed point:

\[
M^{W_{a,\beta}}(n)\downarrow
\Longrightarrow
M^{W_{a,\beta}}(n)=W_{a,\beta}(n)\in\{0,1\}
\]

for all \(a,\beta,n\).

The actual corner \(Y\) is total. The other three corners may be partial.

#### Proof

The displayed implication is exactly the negation of existence of a finite wrong/nonbinary equation, separately for each corner. ∎

This proposition is semantic only. Failure to discover a refutation is not a positive certificate that a corner is a partial fixed point.

In particular, an actual \(A_j\) square can never satisfy Proposition 7, because \(Y_j\) already has a finite refutation.

## 5. What paired partial fixedness really forces

Suppose two global partial fixed points \(P,Q\) differ only on one finite future virtual support \(T\).

For the square application, take

\[
P=Z,\qquad Q=Z_j,\qquad T=\operatorname{supp}(c_j)
\]

inside block \(B_c\).

Fix \(q\in T\). If both

\[
M^P(q)\downarrow,\qquad M^Q(q)\downarrow,
\]

partial fixedness gives the opposite correct values \(P(q)\ne Q(q)\).

Because the input-\(q\) computation syntactically avoids \(q\), the two deterministic computations cannot first distinguish the oracles at \(q\). Their first differing oracle answer must occur at another member of

\[
T\setminus\{q\}.
\]

### Theorem 8 — paired partial-fixed first-contact lasso

On the set of changed future coordinates on which both corner computations halt, draw from \(q\) to the first other changed coordinate at which the two computations receive different answers.

Starting at any such \(q\), iteration has exactly two possibilities:

1. it reaches a changed coordinate at which at least one of the two corner computations diverges, and the finite dependency walk stops;
2. every reached changed-coordinate computation halts on both corners, so the walk eventually enters a directed cycle inside \(T\).

If every changed-coordinate computation halts on both corners, then:

- for \(c_1=011\) the cycle is the forced two-cycle on \(\{q_1,q_2\}\);
- for \(c_2=101\) the cycle is the forced two-cycle on \(\{q_0,q_2\}\);
- for \(c_0=111\) the canonical first-difference graph is a two-cycle with tail or an oriented three-cycle.

#### Proof

The first-difference edge exists exactly when both endpoint computations halt with opposite correct values. It has no loop by syntactic self-avoidance. If the next changed coordinate does not have two halting corner computations, iteration stops. Otherwise continue. A walk which never stops lies in the finite set \(T\) and therefore repeats.

The exact cycle shapes are the retained P4-S041 finite-difference classification. ∎

The theorem deliberately does **not** assign an edge at a divergent changed coordinate. Partiality can remain the terminal obstruction.

Thus paired partial fixedness gives no stronger closure than P4-S041 unless the needed two-corner halts are positively available.

## 6. A locally Case-B fourth corner forces a role switch

For the same future block, write the three false-old-row raw neighbours as

\[
Z_r=Z\oplus c_r^{(c)},\qquad r=0,1,2.
\]

Suppose one of these companions is genuinely **local Case B**, meaning all three local equations halt correctly with that companion's assigned values. This is stronger than merely seeing no finite refutation.

The P4-S041 pairwise law applies inside the false old row:

\[
B_0\Longrightarrow A_1,A_2,
\]

\[
B_1\Longrightarrow A_0,
\]

\[
B_2\Longrightarrow A_0.
\]

### Corollary 9 — square role-switch prediction

At an unresolved old epoch:

- local \(B_0\) of \(Z_0\) gives finite false-row refutations of \(Z_1\) and \(Z_2\), hence one-refutation predictions of raw future coordinates \(1\) and \(2\);
- local \(B_1\) of \(Z_1\) gives a finite false-row refutation of \(Z_0\), hence a prediction of raw future coordinate \(0\);
- local \(B_2\) of \(Z_2\) gives a finite false-row refutation of \(Z_0\), hence a prediction of raw future coordinate \(0\).

For the P4-S046 low-cost geometry this role switch is compatible with the already retained same-block access pattern:

- from role \(0\), the future block may still be wholly fresh;
- from role \(1\), only future \(x_2\) need have been read, so \(x_0\) can remain available;
- from role \(2\), only future \(x_1\) need have been read, so \(x_0\) can remain available.

This is a genuine square-local consequence of a positive B certificate. It does not say that a B certificate appears, and it does not by itself establish the outside-support/fallback conditions for a live handoff.

## 7. Why the one-refutation theorem is not yet an effective infinite escape

Theorem 4 has a semantic premise: the current old epoch is one of the unresolved P4-S047 epochs whose false completion is a global partial fixed point.

That premise is not positively recognizable at finite time. An epoch is unresolved precisely because no future finite old-branch refutation ever appears.

A live program may simulate all four pair hypotheses symmetrically, but before the trap premise is known, one refutation of \(W_{a,\beta}\) need only eliminate one pair. It need not identify the future column.

Thus Theorem 4 cannot simply be applied at every finite stage of the canonical global-refutation scan.

There is a second, independent legality issue. While the old sentinel \(s\) is still open, a future raw target \(t\) cannot also be left permanently unread on a no-event branch.

### Definition 10 — finite-tenure square reservation policy

At a fixed old sentinel \(s\), a finite-tenure square reservation policy is a total computable one-hole-safe protocol which repeatedly:

1. chooses a fresh prospective future raw target \(t_k\);
2. keeps \(t_k\) unread only for a finite computably determined tenure;
3. during that tenure symmetrically dovetails finite computations for the four pair hypotheses \(W_{a,\beta}\), acquiring all needed support outside \(s,t_k\);
4. if a finite pair refutation appears during the tenure, uses the square rule available at the trapped epoch, wagers on \(t_k\), and reads it;
5. if no such event appears in time, reads \(t_k\) at zero stake;
6. continues a background no-repeat sweep so that every raw coordinate other than \(s\) is eventually consumed unless it is the currently transient reservation.

On a complete no-event continuation every \(t_k\) is consumed at finite time. Hence only \(s\) can remain permanently unread.

The policy may use increasing tenures and arbitrary computable adaptation to the finite transcript. It may not reserve one future coordinate forever while leaving \(s\) open.

### Theorem 11 — infinite caught square refutations destroy \(X\)

Fix a genuinely unresolved old epoch. If some computable finite-tenure square reservation policy catches finite square refutations for infinitely many of its active future targets, then there is a total computable adaptive no-repeat one-hole scan whose output has a succeeding computable martingale.

Hence

\[
X\notin OH.
\]

#### Proof

Keep the trapped old sentinel \(s\) permanently unread. By Definition 10 every future reservation is transient, so the complete transcript omits at most \(s\).

Whenever a square refutation is caught while \(t_k\) is still unread, Theorem 4 supplies the correct value of \(X(t_k)\). Bet all current capital on that bit and then query \(t_k\). On timeouts query \(t_k\) with zero stake. Make zero-stake support and background queries elsewhere.

Every nonzero wager is correct. Infinitely many caught events therefore double capital infinitely often. The query protocol is total, computable and no-repeat and has at most one permanent hole. ∎

This theorem uses no CHU handoff: one old trapped hole can be kept forever while transient future targets supply the wagers.

The missing resource is now **effective capture of finite square-refutation times**.

P4-S044/P4-S045 already showed why a finite-use value horizon does not provide a certificate-time modulus. A finite refutation may exist but occur after every tenure chosen for that target.

Semantic abundance of finitely refutable squares therefore does not imply a successful finite-tenure policy.

## 8. Necessary square-timing obstruction under hypothetical \(X\in OH\)

Assume hypothetically

\[
X\in OH.
\]

Run the canonical P4-S047 global-refutation scan. By the retained theorem it has a first target epoch \(e_*\) which never resolves; let \(s_*\) be its old sentinel. The false completion at that epoch is a global partial fixed point.

The natural number \(e_*\) need not be computably discoverable from \(X\). For a contradiction argument, however, a fixed finite integer may be hard-coded into a computable scan.

### Theorem 12 — algorithm-relative finite-tenure obstruction

Under hypothetical \(X\in OH\), at the first trapped old epoch \(e_*\), every total computable finite-tenure square reservation policy catches only finitely many finite square refutations on \(X\).

#### Proof

Suppose a computable policy \(P\) caught infinitely many.

Define a computable one-hole scan which follows the canonical P4-S047 global-refutation scan through its first \(e_*\) resolved epochs and then, at the next sentinel, runs \(P\) while keeping that sentinel open.

The finite integer \(e_*\) is built into the program; the program does not need to decide at runtime that the epoch is trapped.

Before \(e_*\), every branch-refutation wager of the canonical scan is correct. At the trapped epoch, Theorem 11 makes every caught-square wager correct and gives infinitely many doublings. The combined scan is globally one-hole and succeeds on \(X\), contradicting \(X\in OH\). ∎

This is deliberately algorithm-relative.

It does **not** imply:

- infinitely many future squares have no finite refutation;
- every actual future A square has a divergence-only fourth corner;
- there is a computable bound beyond the last caught event;
- the square-refutation times dominate every computable function in a single semantic ordering;
- or the first trapped epoch is computably identifiable.

One fixed computable policy may fail because the finite refutations it targets always appear after its chosen tenures.

Theorem 12 is therefore the exact source-side obstruction obtained in P4-S049.

## 9. A sharper structural full-star countermodel

P4-S048 Family R had a total false neighbour \(Z_*\) and infinitely many false-row raw-adjacent partial-fixed neighbours, while the corresponding actual-row A candidates remained finitely refuted.

The following structural model shows a stronger abstract non-implication when the actual-A premise is removed: both old rows can support the whole radius-one future partial-fixed star.

### Theorem 13 — recurrent full two-row partial-fixed star

Fix any old raw role \(i\). There is a computable finite-use syntactically self-avoiding partial functional \(N\), target

\[
Y_*=0^\omega,
\]

and old false neighbour

\[
Z_*=Y_*\oplus\chi_{S_i}
\]

such that:

1. \(N^{Y_*}\) is total and correct;
2. \(N^{Z_*}\) is total and correct;
3. on every designated future block \(B_c\) and every raw direction \(j=0,1,2\),
   \[
   Y_{*,c,j}=Y_*\oplus c_j^{(c)}
   \]
   is a global partial fixed point;
4. simultaneously
   \[
   Z_{*,c,j}=Z_*\oplus c_j^{(c)}
   \]
   is a global partial fixed point;
5. none of these future raw-adjacent corners has a finite wrong/nonbinary equation.

Hence every designated future block carries three two-raw-bit squares whose four corners are all global partial fixed points, with the two unperturbed row bases \(Y_*,Z_*\) total.

#### Construction

On the old changed support \(S_i\):

- if \(|S_i|=2\), let the two changed inputs query and copy each other;
- if \(|S_i|=3\), orient a three-cycle and let each changed input query and copy the next changed coordinate.

Every unchanged old-block input outputs \(0\).

Thus both all-zero \(Y_*\) and the all-one changed support of \(Z_*\) satisfy the old equations.

On every designated future block, for input \(q_{c,r}\), query only the other two coordinates of that same future virtual block. If both queried bits are \(0\), output \(0\); otherwise diverge.

Every other input outputs \(0\).

On the unperturbed future block \(000\), all three local equations halt with \(0\), so both \(Y_*\) and \(Z_*\) are total and correct there.

For each

\[
c_0=111,\qquad c_1=011,\qquad c_2=101,
\]

every local input on the perturbed block sees at least one \(1\) among its other two coordinates. Hence all three local computations diverge. Outside that future block the oracle is unchanged except possibly on the old support already handled by the copy cycle. Therefore every actual-row and false-row future neighbour is a global partial fixed point.

Every query avoids its own input and lies in a computably bounded finite block. ∎

This model is structural only. Its target is computable, not computably random.

It also deliberately lacks the actual \(A_j\) premise. Therefore it does not contradict Theorem 6. Its purpose is narrower: no theorem from syntactic self-avoidance, finite use, total fixedness of the two row bases, and recurrent partial-fixed future stars alone can force a finite square refutation.

## 10. What P4-S049 changes

The P4-S048 question asked whether the actual source could force a positive finite constraint on the fourth corner \(Z_j\).

The strongest source-specific fact found is different:

\[
\boxed{
\text{at a trapped old epoch, the fourth corner is unnecessary for one-shot prediction.}
}
\]

The actual-future column consists of \(Y\) and \(Z\), and both are immune to finite refutation. Therefore

\[
\boxed{
\text{one finite square refutation}
\Longrightarrow
\text{future-bit prediction}.
}
\]

For an actual \(A_j\) candidate, the needed finite refutation already exists at \(Y_j\).

The fourth corner still matters for:

- the older two-row CHU package;
- local Case-B role switches;
- partial-fixed dependency geometry;
- deciding whether a square has a second positive refutation;
- and structural star obstructions.

But it is not the missing logical condition for predicting the future bit at a genuinely trapped old hole.

The new missing resource is operational:

\[
\boxed{
\text{activate the trapped-epoch rule effectively while respecting one-hole fallback,}
\]

or equivalently, capture enough finite square-refutation events before transient future reservations expire.

## 11. Separation status and guards

P4-S049 does not construct an infinite computable finite-tenure policy catching square refutations on the committed source.

It therefore proves neither

\[
X\notin OH
\]

nor

\[
X\in OH.
\]

No OH non-invariance theorem and no strict

\[
R_2\subsetneq OH
\]

conclusion is claimed.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

The sustained question remains

\[
R_2=OH\;?
\]

P4-S032 null-ambiguity preservation remains available. Ambiguity mass is not reinstated as an invariant.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. Phase 4 remains OPEN; Phase 5 remains CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## Next bounded question

P4-S050 should attack the **activation problem for the one-refutation square theorem**.

The central issue is no longer whether the false fourth corner must itself be rejected. It is whether one can exploit finite square refutations in one globally computable one-hole scan **without knowing which P4-S047 epoch is the semantically trapped one** and without keeping a future target permanently open beside an unresolved old sentinel.

The next session should test exact positive-information mechanisms only: safe escrow of a square refutation before the old branch status resolves, pair-elimination combinations which remain correct without a trap oracle, finite-injury activation of the trapped rule, or an effective square-refutation timing condition strong enough to beat the finite-tenure obstruction.

If none works, sharpen the algorithm-relative timing obstruction or build a structural model that defeats the proposed activation mechanism. Do not return to generic certificate-time bounding or the frozen bankroll/pricing routes.
