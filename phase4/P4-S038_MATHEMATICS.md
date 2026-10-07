# P4-S038 — persistent retirement, one-jump prices and multiplicative uncertainty budgets

Date: 2026-10-07
Session: P4-S038
Incoming checkpoint: edae61899419825b2aa7610aa600e2804e9b8d1d
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **THE P4-S011 PERSISTENT FRONTIER HAS AN EXACT ONE-JUMP BACKWARD-PRICE PROCESS. AFTER THE WTT VALUE-USE FRONTIER IS EXHAUSTED, THE PRICE VECTOR IS \((1,1)\) UNTIL A BINARY HALT IS SEEN AND THEN JUMPS ONCE TO \((3/2,1/2)\) OR \((1/2,3/2)\). FOR A FIXED POSITIVE STAKE, COMPUTABLE RETIREMENT DEADLINES, EVENTUAL-CONSTANCY MODULI, CAUCHY MODULI, EXACT LIMIT PRICES AND TWO-SIDED RETIREMENT SEMIDECISIONS ALL COLLAPSE TO THE SAME TRIGGER/NONTRIGGER DECISION RESOURCE. THE ACTUAL RECODED P4-S011 FAMILY CANNOT SUPPLY THAT RESOURCE UNIFORMLY, NOR CAN ITS ABSOLUTE PERSISTENT-SAVINGS PRICES HAVE A UNIFORM COMPUTABLE CAUCHY MODULUS, ELSE P4-S037 WOULD COMPILE THE SETTLED VIRTUAL WIN INTO A RAW COMPUTABLE MARTINGALE ON THE COMPUTABLY RANDOM SOURCE. HOWEVER DECIDABLE RETIREMENT IS NOT NECESSARY: A COMPUTABLE FINITE MULTIPLICATIVE UNCERTAINTY BUDGET \(\prod_e(1+r_e)\le K\) PREPAYS EVERY POSSIBLE ORIENTATION AND GIVES A TOTAL COMPUTABLE RAW SUPERMARTINGALE, HENCE A MARTINGALE COVER, EVEN WHEN RETIREMENT IS ONLY C.E. THIS STRICTLY EXTENDS FRESH RENEWAL AS A COMPILER CONDITION. FOR PURE CORRECT-PREDICTION SENTINEL GAIN THE BOUNDARY IS SHARP: \(\prod_e(1+r_e)\) IS BOTH THE TARGET CAPITAL-GROWTH PRODUCT AND THE MINIMAL POSITIVE ORIENTATION-FREE HEDGE PRODUCT, SO STAKE DECAY CANNOT PRESERVE UNBOUNDED SENTINEL GAIN WHILE MAKING THE UNRESOLVED SOURCE-SIDE PRICE COST FINITE. NO \(X\in OH\) IS PROVED; NO OH NON-INVARIANCE OR \(R_2\subsetneq OH\) CONCLUSION IS AVAILABLE.**

## Authority, uniqueness and scope

Immediately before the first P4-S038 write, live main was exactly

\[
\texttt{edae61899419825b2aa7610aa600e2804e9b8d1d},
\]

the committed P4-S037 outgoing checkpoint. Repository search returned no P4-S038 record, so the session identifier was unused.

P4-S001 through P4-S037, the selected CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S037 were read. All validated mathematics through P4-S037 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence is not reopened.

Retain

\[
R_2=\{x\in CR:\text{ every total computable fair-coin-preserving global-}k=2\text{ map sends }x\text{ to }CR\},
\]

\[
OH=\{x\in CR:\text{ every total computable adaptive no-repeat one-hole scan sends }x\text{ to }CR\},
\]

and

\[
OH^{iso}=\{x\in CR:\text{ every computable fair-coin-preserving homeomorphism }H\text{ sends }x\text{ into }OH\}.
\]

The retained inclusions are

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

The repeated three-bit source recoding remains

\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Value closure is not retirement

Fix one P4-S011 epoch with sentinel \(j\). Let \(M\) be the committed wtt autoreduction and let \(u(j)\) be its computable use bound. Work after the scan has exposed the finite value frontier required to determine every oracle answer which \(M(j)\) can ever inspect.

Because \(M\) is an autoreduction, it never queries \(j\) while computing \(j\). Thus, after the use frontier has been exhausted:

1. every source value which can affect the fixed computation \(M(j)\) has been fixed;
2. the sentinel value itself has not been virtually queried;
3. under the displayed source recoding, the sentinel parity may already be determined by the raw history;
4. future filler values outside the finite use frontier cannot change any oracle answer seen by \(M(j)\);
5. nevertheless finite simulation may not yet have exposed a binary halt.

This separates two notions.

### Definition 1 — value-closed persistent frontier

A **value-closed persistent frontier state** \(s\) records only finite computable data:

- the sentinel index \(j\);
- the finite virtual transcript/controller state;
- the finite answers on the exhausted wtt use frontier;
- the current finite machine-simulation configuration / elapsed simulation budget;
- the finite raw block state needed by the displayed recoding;
- and, when already raw-determined, the sentinel sign \(z\in\{-1,+1\}\).

The state does **not** record whether the fixed computation eventually halts, diverges, or produces a nonbinary output.

A claim is **value-closed** at \(s\) when every future oracle value is irrelevant to the outcome of the fixed computation. It is **retired** only when a binary prediction has been exposed and the sentinel wager can be settled, or when permanent nontriggering is certified.

The first property is decidable from the wtt use bound and finite exposure. The second need not be decidable.

Let

\[
B_+(s)=\{\text{the fixed computation eventually exposes binary sign }+1\},
\]

\[
B_-(s)=\{\text{the fixed computation eventually exposes binary sign }-1\},
\]

and \(B(s)=B_+(s)\cup B_-(s)\).

Uniformly in reachable value-closed states, \(B_+\) and \(B_-\) are disjoint c.e. events and \(B\) is c.e. The no-binary-trigger event \(\neg B\) is co-c.e. A visible nonbinary halt belongs to the permanently nontriggering side for the P4-S011 scan convention.

No claim is made that this particular c.e. set is complete for the halting problem.

## 2. Exact half-stake finite-horizon price

Use the P4-S037 half-stake sentinel martingale. Before the sentinel is queried, its fractional stake is zero until a binary prediction is visible; once the prediction sign \(a\in\{-1,+1\}\) is visible, the virtual sentinel multiplier is

\[
1+\frac12az.
\]

Fix a value-closed state \(s\). Let \(h_s\in\mathbb N\cup\{\infty\}\) be the least additional simulation horizon at which a binary halt becomes visible, and let \(a_s\) be its sign when \(h_s<\infty\).

For finite simulation horizon \(N\), the normalized backward price is exactly

\[
P_N^s(z)=
\begin{cases}
1,&N<h_s\text{ or }h_s=\infty,\\[2mm]
1+\frac12 a_s z,&N\ge h_s.
\end{cases}
\]

Ordering the vector by \(z=+1,-1\),

\[
P_N^s=
(1,1)
\]

until the trigger is seen, and then it changes once to

\[
(3/2,1/2)
\]

when \(a_s=+1\), or to

\[
(1/2,3/2)
\]

when \(a_s=-1\).

There is no oscillation, no unbounded condition number, and no infinite sequence of price corrections. The only unresolved datum is whether the one jump ever occurs and, if it does, its orientation.

### Proposition 2 — exact effective complexity of the one-jump price

The limiting vector satisfies

\[
P_\infty^s(+1)
=
1+\frac12\mathbf 1_{B_+(s)}
-\frac12\mathbf 1_{B_-(s)},
\]

\[
P_\infty^s(-1)
=
1-\frac12\mathbf 1_{B_+(s)}
+\frac12\mathbf 1_{B_-(s)}.
\]

Consequently:

1. \(P_N^s\) is a computable rational approximation with at most one mind change.
2. \(B_+\) and \(B_-\) are c.e.; the trigger indicator \(\mathbf 1_B\) is left-c.e.; the no-trigger indicator is right-c.e.
3. The coordinate functions are differences of left-c.e. quantities. Uniformly over states they need not be left-c.e. or right-c.e. because one orientation raises a coordinate and the other lowers it.
4. If the eventual orientation \(a\) is fixed in advance, the matching coordinate is left-c.e. and the opposite coordinate is right-c.e.
5. The midpoint is computable:
   \[
   \frac{P_\infty^s(+1)+P_\infty^s(-1)}2=1.
   \]
6. The spread is
   \[
   |P_\infty^s(+1)-P_\infty^s(-1)|
   =
   \mathbf 1_{B(s)},
   \]
   so it is left-c.e.
7. A decision oracle for \(B\) computes the exact limiting vector: on a positive answer, simulate until the binary halt reveals its sign. Conversely the exact limiting vector decides \(B\), since it equals \((1,1)\) exactly on \(\neg B\).

Thus the exact limit is uniformly equivalent to the local binary-trigger decision, not to a generic noncomputable martingale limit.

On the P4-S011 target, correctness gives \(a=z\), so the realized scalar price is \(1\to3/2\). That target-path monotonicity is not a total compiler resource: on sibling states the prediction sign can oppose the already raw-known sign.

### Corollary 3 — mean-one normalization does not remove the obstruction

Every finite and limiting vector has mean one. Therefore normalization by its fair mean leaves the vector unchanged. The price ratio is \(1\) before the jump and \(3\) after the half-stake jump. Hence neither normalization nor bounded ratio erases the trigger decision.

## 3. The standard one-jump effectivity hypotheses collapse

The previous section extends verbatim to any fixed rational stake \(r\in(0,1]\), with the two triggered vectors

\[
p^+=(1+r,1-r),\qquad p^-=(1-r,1+r).
\]

The sup-norm jump size from \((1,1)\) is exactly \(r\).

### Theorem 4 — retirement/stabilization collapse for a fixed positive jump

Uniformly over a computable family of value-closed one-jump states with fixed computable \(r>0\), the following resources are equivalent up to uniform computable conversion:

1. a decision procedure for whether the binary price jump ever occurs;
2. a computable deadline \(D(s)\) such that every jump, if it occurs, occurs by \(D(s)\);
3. a computable eventual-constancy modulus for \(P_N^s\);
4. a computable Cauchy modulus for \(P_N^s\);
5. a computable exact limiting price vector \(P_\infty^s\);
6. a semidecision procedure for permanent nontriggering in addition to the already available c.e. trigger semidecision.

**Proof.**

- A decision of \(B(s)\) returns immediately on the negative case. On the positive case, finite simulation eventually exposes the unique binary halt, giving a deadline, orientation and exact limiting vector.
- A deadline decides \(B\) by simulating through that deadline.
- An eventual-constancy modulus decides \(B\) in the same way.
- Given a Cauchy modulus, ask for tolerance \(<r/2\). If no jump has occurred by the returned stage, a later jump of size \(r\) would violate the modulus. Thus no later jump is possible.
- An exact computable limit, or an approximation to error \(<r/3\), distinguishes \((1,1)\) from either triggered vector.
- Since trigger is already c.e., a second semidecision for permanent nontriggering can be dovetailed with it to decide \(B\).

The converse implications then follow from the first bullet. ∎

This theorem is specific to the discrete one-jump geometry. It does not say that arbitrary effective Cauchy convergence problems collapse to decidable stabilization.

### Consequence

For this persistent claim, a one-sided exact optional projection does not evade the issue. Any total computable exact conditional price would decide whether the vector is \((1,1)\) or a distance \(r\) away from it.

## 4. The actual recoded P4-S011 witness cannot have uniform retirement effectivity

Return to the P4-S033 source \(X=H^{-1}(Y)\). Settled facts give

\[
X\in CR
\]

and the half-stake version of the P4-S011 martingale succeeds on

\[
D(H(X))=D(Y).
\]

### Proposition 5 — no uniform trigger decision on all reachable persistent states

There is no total computable procedure which, from every reachable value-closed persistent frontier state of the actual recoded P4-S011 family, decides whether the current binary sentinel trigger will ever appear.

**Proof.**
Suppose such a procedure existed.

If it answers “trigger”, finite simulation can be continued until the binary halt appears, the current claim is retired, and the finite wtt value frontier for the next epoch can be exposed.

If it answers “no trigger”, the current half-stake claim can be certified permanently inactive. For this virtual witness the scan has entered an absorbing zero-stake regime: it can continue through irrelevant fillers while the compiled raw evaluator is completed exhaustively.

Thus every old persistent claim has an effective finite retirement/absorption decision. This is exactly the missing information needed to turn the width-one frontier into an effective renewing/absorbing compiler of the P4-S037 type. Applying that compiler to the successful half-stake witness would produce one total computable raw martingale succeeding on \(X\), contradicting \(X\in CR\). ∎

No reduction from the full halting set has been used or proved.

### Corollary 6 — no standard local stabilization modulus exists

By Theorem 4, the actual family has no uniform computable:

- trigger deadline;
- eventual-constancy modulus for the one-jump normalized prices;
- Cauchy modulus for those prices;
- exact limiting-price procedure;
- or semidecision pair for trigger and permanent nontriggering.

This is an exact obstruction internal to the committed witness.

### Corollary 7 — no computable Cauchy modulus for the absolute persistent-savings prices

The absolute backward prices of the P4-S036 persistent-savings transform cannot have a total computable Cauchy modulus uniformly over the reachable recoded P4-S011 frontiers.

**Proof.**
P4-S037 Theorem 9 proves that such a modulus, together with the finite consistency equations already present in the construction, yields one total computable raw martingale. Persistent savings preserves the virtual success. The resulting raw success on \(X\) would contradict \(X\in CR\). ∎

This is stronger than merely observing that finite-horizon prices can have noncomputable limits.

## 5. Why the obvious compiler repairs fail

The one-jump process is simple enough to test the requested repairs exactly.

### 5.1 Two-account orientation hedge

For stake \(r\), the two triggered normalized vectors are

\[
p^+=(1+r,1-r),\qquad
p^-=(1-r,1+r).
\]

The equal mixture is

\[
\frac{p^++p^-}{2}=(1,1),
\]

so a symmetric two-account hedge erases exactly the advantage it was meant to preserve.

An unequal mixture with weight \(q\) on \(p^+\) is

\[
(1+(2q-1)r,\;1-(2q-1)r),
\]

which merely precommits to one orientation.

Selecting the favourable orientation after the raw-known sign \(z\) is available gives the coordinatewise maximum

\[
(1+r,1+r),
\]

whose fair mean is \(1+r\), not \(1\).

### Lemma 8 — exact one-claim positive hedge cost

Every nonnegative vector which dominates both possible triggered orientations coordinatewise has fair mean at least \(1+r\). The constant vector \((1+r,1+r)\) attains this bound.

Thus \(1+r\) is the exact orientation-free positive superhedge factor for one unresolved claim.

### 5.2 Delayed commitment

After value closure, later filler values carry no information about the eventual prediction sign. When the c.e. halt finally reveals the sign, the sentinel parity \(z\) is already raw-known. Choosing the orientation then is retroactive from the raw-betting point of view. The exact cost of making that delayed choice safely is again the factor \(1+r\) from Lemma 8.

### 5.3 Upper and lower envelopes

The minimal coordinatewise upper envelope is \((1+r,1+r)\). The lower envelope \((1-r,1-r)\) does not dominate a triggered payoff. Hence envelope methods reduce to the same prepaid positive hedge.

### 5.4 Supermartingale-to-martingale conversion does exist, but it does not create reserve

There is a useful exact conversion under the repository's fair binary convention.

Let \(s\) be a total computable nonnegative rational supermartingale and define its defect by

\[
\delta(\sigma)
=
s(\sigma)-\frac{s(\sigma0)+s(\sigma1)}2
\ge0.
\]

Put \(A(\varnothing)=0\) and

\[
A(\sigma b)=A(\sigma)+\delta(\sigma),
\]

and define

\[
m(\sigma)=s(\sigma)+A(\sigma).
\]

Then

\[
\frac{m(\sigma0)+m(\sigma1)}2=m(\sigma),
\]

so \(m\) is a total computable nonnegative rational martingale and \(m\ge s\).

Therefore a successful computable supermartingale is enough for contradiction with computable randomness. But this conversion does not fund the factor \(1+r\) needed before an unresolved orientation is revealed.

### 5.5 Persistent savings does not shrink the relative jump

Persistent savings guarantees a source-side success transfer once the relevant conditional values are computable. It does not decide retirement and does not supply a Cauchy modulus. Corollary 7 rules out such a uniform modulus in the actual witness.

### 5.6 Rolling mixtures over finite simulation horizons

Let \((\lambda_n)\) be computable nonnegative mixture weights with computable sum one. If the trigger is first visible at simulation horizon \(h\), only the horizons \(n\ge h\) see the nontrivial vector. The mixed deviation from \(1\) is

\[
r\,a z\,L(h),
\qquad
L(h)=\sum_{n\ge h}\lambda_n.
\]

Since \(L(h)\to0\), arbitrarily late triggers receive arbitrarily small weight. To preserve unbounded gain across epochs one would need quantitative control such as

\[
\sum_e r_e L_e(h_e)=\infty
\]

along the target. The committed wtt use bound gives no computable control of the trigger times \(h_e\). Hence horizon mixing does not give a rate-free compiler for the actual family.

## 6. A positive theorem without decidable retirement

The failure of exact optional projection does not mean that all persistent claims require retirement decisions. One may instead prepay the worst possible orientation.

Consider a sequential persistent-frontier architecture of the P4-S011 type. The \(e\)-th open claim has computable fractional magnitude

\[
0\le r_e\le1.
\]

While it is unresolved, the virtual witness places no other nonzero wager in that persistent claim. If a binary trigger is exposed, the claim multiplier is

\[
1+r_e a_e z_e\le1+r_e
\]

and the process proceeds to the next persistent claim. If no trigger ever appears, that claim may remain open forever.

### Definition 9 — computable multiplicative uncertainty budget

The persistent claim sequence has a **computable finite multiplicative uncertainty budget** if there is a computable rational \(K\ge1\) such that for every \(n\),

\[
\prod_{e<n}(1+r_e)\le K.
\]

No retirement deadline, trigger decision, convergence modulus or tail modulus is included in this definition.

### Theorem 10 — multiplicative-budget persistent-frontier normalization

Assume the finite raw/virtual transitions outside the persistent claims are computable as in the P4-S037 frontier construction, and assume Definition 9. Apply the P4-S036 persistent-savings transform first. If the original unresolved fractional stake at claim \(e\) has magnitude at most \(r_e\), the transformed stake has magnitude at most \(r_e\) as well: stopped summands wager zero and active summands retain the original fractional wager, so the aggregate fraction is a capital-weighted contraction.

Then every successful computable virtual martingale in this class yields one total computable raw supermartingale, and therefore one total computable raw martingale, which succeeds on the same raw source.

In particular, persistent retirement may remain only c.e.

**Proof.**
Write \(c\) for the persistent-savings capital. It tends to infinity after sufficiently late stages on every path where the original martingale is unbounded, and once a savings threshold is locked it stays locked through all later continuations.

Let

\[
P_e=\prod_{i<e}(1+r_i),
\qquad
A_e=\frac K{P_e}.
\]

Then \(A_e\ge1\) and

\[
A_e=(1+r_e)A_{e+1}.
\]

At the \(e\)-th persistent frontier, if the current virtual capital is \(c\), assign raw reserve

\[
S=A_ec.
\]

While the claim remains unresolved, keep \(S\) constant through the irrelevant filler extensions.

If the trigger eventually appears with realized multiplier

\[
m_e=1+r_ea_ez_e\le1+r_e,
\]

the desired reserve for the next frontier is

\[
A_{e+1}cm_e
\le
A_{e+1}c(1+r_e)
=
A_ec.
\]

After value closure the trigger time is independent of future filler values, so this drop is made equally on the two children of the raw filler node at which the new simulation fact becomes visible. Thus it is a legal computable supermartingale decrease. The finite computable transition into the next frontier is handled by the same finite conditional-expectation pieces used in P4-S037.

If the trigger never appears, the reserve stays constant forever and totality is unaffected.

Since \(A_e\ge1\), every target frontier satisfies

\[
S\ge c.
\]

Persistent savings makes \(c\to\infty\) along a successful target and makes the locked capital survive any arbitrarily long persistent waiting interval. Hence \(S\) is unbounded (indeed tends through arbitrarily large permanent floors) at the persistent frontiers and during unresolved waits. The exact supermartingale-to-martingale conversion of §5.4 gives one total computable nonnegative rational raw martingale which also succeeds. ∎

This strictly extends P4-S037 fresh renewal as a compiler hypothesis: retirement need not be decidable or occur in a computably finite transition.

### Proposition 11 — a computable sum bound is sufficient, but an effective tail is unnecessary

If a computable rational \(C\) is known with

\[
\sum_e r_e\le C,
\]

then a computable rational \(K\) satisfying Definition 9 is available, for example any explicit rational bound above \(e^C\).

Conversely, for \(0\le r\le1\),

\[
\frac r2\le\log(1+r)\le r.
\]

Hence a finite product bound implies a finite sum bound up to a computable coarse constant.

The presentation strengths differ: a known total bound on the sum or product does not by itself provide a computable tail modulus. Therefore an “effectively summable unresolved-error tail” is stronger than Theorem 10 needs.

A halting-coded family with, for example, \(r_e=2^{-e-2}\) can have undecidable retirement while satisfying a trivial finite uncertainty budget. Thus Theorem 10 is genuinely independent of retirement decidability.

## 7. Stake decay versus persistent uncertainty

P4-S037 used fixed half-stakes only to show that bounded ratios are insufficient. We can now locate the exact threshold for the pure correct-prediction sentinel mechanism.

Suppose every target sentinel prediction is correct and the \(e\)-th fractional stake is \(r_e\in[0,1]\). After \(n\) completed target epochs, capital is

\[
d_n
=
d_0\prod_{e<n}(1+r_e).
\]

Using

\[
\frac{r_e}{2}\le \log(1+r_e)\le r_e,
\]

we obtain

\[
d_n\to\infty
\quad\Longleftrightarrow\quad
\sum_e r_e=\infty.
\]

But Lemma 8 shows that the exact positive orientation-free hedge factor for the same unresolved claim is \(1+r_e\). Therefore the cumulative minimal hedge factor through \(n\) claims is exactly

\[
\prod_{e<n}(1+r_e),
\]

the same product as the all-correct target gain.

### Theorem 12 — gain/cost identity for persistent correct-prediction claims

For the pure sequential sentinel mechanism:

- unbounded virtual success from the uncertain sentinel claims occurs exactly when
  \[
  \prod_e(1+r_e)=\infty,
  \]
  equivalently \(\sum_e r_e=\infty\);
- finite multiplicative orientation-free uncertainty cost occurs exactly when
  \[
  \prod_e(1+r_e)<\infty,
  \]
  equivalently \(\sum_e r_e<\infty\).

Hence shrinking \(r_e\to0\) cannot simultaneously preserve unbounded pure sentinel gain and make the unresolved positive source-side pricing cost finite.

In particular there is no second-order \(r_e^2\) escape: the sound unresolved price error is first order in \(r_e\).

This is not the P4-S015–P4-S031 skipped-wager bankroll calculation. It is an identity between the local backward-price superhedge factor and the target's multiplicative correct-prediction gain.

## 8. Exact position of the recoded P4-S011 witness

The actual recoded witness has:

1. computably finite source-value dependence for each sentinel, from the wtt use bound;
2. only c.e. detection of a future binary trigger after that value frontier is fixed;
3. no uniform trigger/nontrigger decision, deadline, eventual-constancy modulus or local Cauchy modulus, by Proposition 5 and Corollary 6;
4. no uniform computable Cauchy modulus for the absolute persistent-savings backward prices, by Corollary 7;
5. fixed \(r_e=1/2\), hence cumulative target gain and minimal orientation-free hedge factor
   \[
   (3/2)^n,
   \]
   which is unbounded.

Therefore the actual witness lies strictly beyond both positive mechanisms now established:

- P4-S037 effective fresh-frontier renewal;
- P4-S038 finite multiplicative uncertainty budget.

This is the exact persistent-pricing obstruction selected by the session. It does not imply that the recoded source belongs to \(OH\).

## 9. Separation status

For the P4-S033 recoded source,

\[
X\in CR
\]

is settled, and

\[
H(X)=Y\notin OH
\]

is available from the P4-S011 destroying scan.

The missing statement remains

\[
X\in OH.
\]

Nothing in the present pricing analysis proves it. Consequently P4-S038 proves neither OH non-invariance nor

\[
R_2\subsetneq OH.
\]

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains unchanged. Ambiguity mass is not reinstated as an invariant.

## 10. What the session selects next

P4-S038 closes the most direct persistent-price variants.

For a fixed positive one-jump claim, exact price computation and effective stabilization collapse to trigger/nontrigger decision. The actual P4-S011 family cannot possess that uniform resource. Positive superhedging avoids the decision only by paying the exact factor \(1+r_e\), and the cumulative price of that protection is exactly the all-correct target gain product.

Therefore another round of local retirement-modulus or stake-decay refinement would not attack the missing source-side question.

P4-S039 should move from **raw martingale compilation** to **same-source raw one-hole simulation** under the displayed three-bit recoding.

The bounded target is: starting from the c.e.-persistent P4-S011 virtual sentinel process on \(H(X)\), determine whether a total raw-coordinate one-hole scan/stake process can reproduce enough of the persistent correct-prediction gain directly on \(X\). The first object should be the finite linear-algebraic state of one raw hole inside a three-bit block and how that hole transports the three virtual parities across block boundaries.

A positive same-source simulation for the actual coded witness would prove only that this \(X\notin OH\), eliminating it as an OH non-invariance candidate. A negative simulation theorem would still not prove \(X\in OH\), but it could expose the next intrinsic source-side invariant.

Do not return to P4-S015–P4-S031 or to ambiguity mass.

## Guards

All validated mathematics through P4-S037 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 remains OPEN; Phase 5 remains CLOSED.
