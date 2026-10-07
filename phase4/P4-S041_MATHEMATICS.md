# P4-S041 — finite-perturbation collapse, raw-radius-one partiality and finite dependency cycles

Date: 2026-10-07
Session: P4-S041
Incoming checkpoint: c7735bca90102348d6a52afed16eb20ca8d3e2e1
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **FINITE-PERTURBATION TOTALITY OF THE COMMITTED SELF-AVOIDING WTT AUTOREDUCTION WOULD COLLAPSE TO A TRUTH-TABLE AUTOREDUCTION, CONTRADICTING THE RETAINED P4-S011 SOURCE AUTHORITY. HENCE SOME FINITE PERTURBATION OF Y FORCES DIVERGENCE. AFTER TRANSPORT THROUGH THE THREE-BIT HOMEOMORPHISM THERE IS A WELL-DEFINED MINIMAL RAW DIVERGENCE RADIUS. IF THAT RADIUS EXCEEDS ONE, EVERY SINGLE-RAW-BIT COMPANION IS TOTAL ON ALL INPUTS, SO P4-S040 RAW-ADJACENT DECISIVENESS HOLDS EVERYWHERE AND X IS NOT IN OH. THEREFORE ANY SURVIVING POSSIBILITY X IN OH FORCES RAW-RADIUS-ONE PARTIALITY, BUT RADIUS-ONE PARTIALITY ALONE DOES NOT FORCE LOCAL CASE C. GENUINE FINITE-DIFFERENCE FIXED-POINT COMPANIONS CARRY A DIRECTED DEPENDENCY CYCLE: THE 011 AND 101 SUPPORTS FORCE TWO-CYCLES, WHILE THE 111 SUPPORT HAS EXACTLY A TWO-CYCLE-WITH-TAIL OR AN ORIENTED THREE-CYCLE AS ITS CANONICAL FIRST-DIFFERENCE GRAPH. THESE CYCLES ARE POSITIVE CASE-B STRUCTURE, NOT FINITE CASE-C REFUTATIONS. NO TARGET-EQUIVALENT RADIUS-ONE TOTALIZATION OR FINITE COMPLETE OUTSIDE-WITNESS SET FOLLOWS FROM THE COMMITTED WTT DATA.**

## Authority, uniqueness and scope

Immediately before the first P4-S041 write, live main was exactly

\[
\texttt{c7735bca90102348d6a52afed16eb20ca8d3e2e1},
\]

the final P4-S040 outgoing checkpoint after its notation-repair commits.

The phase4 directory contained P4-S001 through P4-S040 and no P4-S041 mathematics, close or validation record. The only P4-S041 material was the forward prompt in authoritative/NEXT_SESSION_PROMPT.md. Hence P4-S041 was unused.

P4-S001 through P4-S040 were read, together with the selected CAND-01 authority, the P4-S031 pivot, and P4-S032 through P4-S040 with special attention to P4-S011, P4-S012, P4-S039 and P4-S040.

All validated mathematics through P4-S040 is frozen.

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

The retained inclusions remain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Let \(Y\) be the P4-S011 computably random wtt-autoreducible source, let \(M\) be its committed syntactically self-avoiding wtt autoreduction, and let

\[
X=H^{-1}(Y)
\]

under the repeated three-bit recoding

\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix}.
\]

Retain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

The missing source-side statement remains whether \(X\in OH\).

The selected CAND-01 formulation is unchanged. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Four distinct finite-perturbation notions

For a finite raw set \(F\subseteq\omega\), write

\[
X^F=X\oplus\chi_F,\qquad Y^F=H(X^F).
\]

A raw radius-one perturbation is \(F=\{j\}\).

Inside one raw block \(B\), flipping raw coordinate \(i\) changes the corresponding virtual block by

\[
c_i=Ae_i,
\]

where

\[
c_0=111,\qquad c_1=011,\qquad c_2=101.
\]

The following notions must remain distinct.

### Target correctness

\[
M^Y(n)\downarrow=Y(n)\qquad\text{for every }n.
\]

This is the committed autoreduction property.

### Local block acceptance

For a candidate virtual block value \(v\in\mathbb F_2^3\),

\[
M^{Y[B\leftarrow v]}(q_r)\downarrow=v_r
\qquad(r=0,1,2).
\]

This is P4-S039/P4-S040 local consistency. It says nothing about equations outside the three block coordinates.

### Global fixed point

An oracle \(Z\) is a global fixed point of \(M\) when

\[
M^Z(n)\downarrow=Z(n)
\qquad\text{for every }n.
\]

Local acceptance does not imply this.

### Finite refutation and divergence-only failure

A candidate is finitely refuted as soon as one tested equation halts with a nonbinary value or with a binary value different from the candidate bit.

A candidate has divergence-only failure relative to a tested equation family when every halt seen is correct but at least one required computation diverges.

P4-S040 Case C is exactly the local three-equation version of this last phenomenon.

## 2. Finite-perturbation totality collapses to truth-table autoreducibility

Let \(u(n)\) be the committed computable wtt use bound. Use the harmless convention that every oracle query in the input-\(n\) computation is below \(u(n)\).

### Theorem 1 — finite-perturbation totality collapse

Suppose

\[
\forall F\subseteq_{\mathrm{fin}}\omega\ \forall n\quad
M^{Y\oplus\chi_F}(n)\downarrow.
\]

Then \(Y\) is truth-table autoreducible.

#### Proof

Fix \(n\).

For every binary string

\[
\sigma\in2^{u(n)}
\]

choose the finite set

\[
F_\sigma=\{k<u(n):\sigma(k)\ne Y(k)\}.
\]

Then the finite perturbation

\[
Z_\sigma=Y\oplus\chi_{F_\sigma}
\]

has prefix \(\sigma\) below the entire use window.

By hypothesis \(M^{Z_\sigma}(n)\) halts.

Because the input-\(n\) computation never queries outside the use window, the same finite simulation halts for every oracle whose answers below \(u(n)\) are \(\sigma\).

Thus every one of the finitely many answer patterns \(\sigma\in2^{u(n)}\) gives a halting computation.

Uniformly in \(n\), dovetail the finitely many simulations until all have halted. This search terminates. Record the resulting finite answer table.

If an off-target halt is nonbinary, replace that table entry by \(0\). This normalization does not alter the target value, since

\[
M^Y(n)=Y(n)\in\{0,1\}.
\]

The syntactic self-avoidance of the original program means the finite table does not need the \(n\)-th oracle bit.

Hence these uniformly computable finite tables define a total truth-table autoreduction of \(Y\). ∎

### Corollary 2 — some finite perturbation forces divergence

The retained P4-S011 source authority explicitly records the boundary that no computably random set is truth-table autoreducible, while a computably random weak-truth-table-autoreducible set exists.

Therefore Theorem 1 cannot hold for the committed \(Y,M\).

Hence there exist a finite perturbation \(F\) and an input \(n\) such that

\[
M^{Y\oplus\chi_F}(n)\uparrow.
\]

This conclusion is only finite-perturbation partiality. It does not yet locate the divergence at raw radius one.

## 3. Transport to raw perturbations and define the minimal radius

Because the repeated block map \(H\) is an invertible computable linear homeomorphism, a finite virtual perturbation of \(Y\) has a unique finite raw preimage perturbation of \(X\), block by block.

Therefore Corollary 2 implies that the set

\[
\mathcal P=
\{F\subseteq_{\mathrm{fin}}\omega:
(\exists n)\ M^{Y^F}(n)\uparrow\}
\]

is nonempty.

Define the **minimal raw divergence radius**

\[
\rho=\min\{|F|:F\in\mathcal P\}.
\]

Since \(M^Y\) is total,

\[
1\le \rho<\infty.
\]

### Theorem 3 — radius dichotomy

If

\[
\rho\ge2,
\]

then

\[
X\notin OH.
\]

Equivalently,

\[
X\in OH\quad\Longrightarrow\quad \rho=1.
\]

#### Proof

Assume \(\rho\ge2\).

Then for every single raw coordinate \(j\) and every input \(n\),

\[
M^{Y^{\{j\}}}(n)\downarrow.
\]

Fix any fresh block \(B\) and any raw direction \(i\). Its raw-adjacent companion is exactly one such radius-one perturbation.

In particular all three local computations

\[
M^{Y^{\{j\}}}(q_r),\qquad r=0,1,2,
\]

halt.

If all three are binary and equal the companion bits, the companion is P4-S040 Case B.

Otherwise one of the three halts gives a wrong or nonbinary finite witness, so the companion is Case A.

Thus every raw-adjacent companion on every block and in every direction is decisive.

The hypotheses of the validated P4-S040 three-scan theorem hold globally. Therefore

\[
X\notin OH.
\]

The contrapositive gives the second statement. ∎

### Interpretation

The unavoidable finite perturbation partiality can be hidden at radius two or larger only at the cost of making all radius-one companions total. For this recoded source that is already enough to trigger P4-S040 and eliminate \(X\) as an \(OH\) separation candidate.

Hence the only branch on which \(X\in OH\) can still be true is one in which some single raw-bit perturbation causes divergence.

This does **not** say that every radius-one divergent perturbation is P4-S040 Case C. The divergence may occur only at an outside equation, or the same companion may already have a different local wrong halt and hence still be decisive.

## 4. Radius-one decisiveness does not follow from radius-one totality failure

The hierarchy is now exact:

1. \(\rho=1\) means there are \(j,n\) with
   \[
   M^{Y^{\{j\}}}(n)\uparrow.
   \]
2. P4-S040 Case C at \((B,i)\) means at least one of the three block equations diverges and every block equation which halts is correct for that raw-adjacent companion.
3. Failure of the P4-S040 positive theorem requires a reached block/direction of type 2.

Therefore statement 1 is necessary for the still-open branch \(X\in OH\), but it is not sufficient to defeat P4-S040.

This is the precise gap left after Theorem 3.

## 5. Finite-difference dependency graph for genuine fixed points

Now let

\[
Z=Y\oplus\chi_S
\]

for a nonempty finite virtual support \(S\), and assume both \(Y\) and \(Z\) are global fixed points of the same syntactically self-avoiding \(M\).

For \(n\in S\),

\[
M^Y(n)=Y(n),\qquad
M^Z(n)=Z(n)=1-Y(n).
\]

Both computations halt and their outputs differ.

Because \(M(n)\) never queries coordinate \(n\), the two deterministic computations cannot distinguish the oracles at \(n\).

Before their computation histories first diverge, they are in the same machine state and make the same next oracle query. Since the eventual outputs differ, at some first such query the two oracle answers differ. That queried coordinate lies in

\[
S\setminus\{n\}.
\]

### Theorem 4 — finite dependency cycle

For every \(n\in S\), choose the first changed coordinate \(k\in S\setminus\{n\}\) queried before the two input-\(n\) computations diverge, and draw the edge

\[
n\to k.
\]

This gives a finite directed graph on \(S\) with out-degree exactly one at every vertex and no loops.

Consequently it contains a directed cycle of length at least two.

In particular no two global fixed points of a syntactically self-avoiding functional can differ in exactly one coordinate.

The same proof applies to the changed coordinates of a locally accepted raw-adjacent companion, because the target and companion computations at those changed block inputs both halt with opposite correct outputs.

## 6. Exact cycle shapes for the three recoding columns

For a raw-adjacent companion in direction \(i\), the changed virtual support is

\[
S_i=\operatorname{supp}(c_i).
\]

### Direction \(i=1\)

\[
S_1=\{q_1,q_2\}.
\]

If the companion is locally accepted, then the canonical first-difference graph is forced to be

\[
q_1\leftrightarrow q_2.
\]

There is no other loop-free out-degree-one graph on two vertices.

### Direction \(i=2\)

\[
S_2=\{q_0,q_2\}.
\]

Local acceptance forces

\[
q_0\leftrightarrow q_2.
\]

### Direction \(i=0\)

\[
S_0=\{q_0,q_1,q_2\}.
\]

Each changed coordinate points to one of the other two.

The canonical graph therefore has exactly one of the following forms:

- a two-cycle \(q_a\leftrightarrow q_b\) and the third vertex points to \(q_a\) or \(q_b\); or
- one of the two oriented three-cycles.

Thus there are six labelled two-cycle-with-tail patterns and two labelled oriented three-cycles.

### Corollary 5 — cycles are Case-B certificates, not Case-C refutations

Once all required companion computations have halted correctly, the finite traces positively exhibit one of the cycle patterns above.

But if a required computation diverges, failure to see the missing edge is not a finite certificate that no such edge will ever appear.

Therefore the dependency-cycle theorem classifies genuine Case B. It does not eliminate divergence-only Case C.

## 7. A sharper pairwise law among the three raw-adjacent companions

Fix one block and write

\[
Z_i=Y[B\leftarrow Y(B)+c_i].
\]

The recoding columns satisfy

\[
c_0+c_1=100,\qquad
c_0+c_2=010.
\]

Hence \(Z_0\) and \(Z_1\) differ only at virtual coordinate \(q_0\).

Since \(M(q_0)\) syntactically avoids \(q_0\),

\[
M^{Z_0}(q_0)
\]

and

\[
M^{Z_1}(q_0)
\]

are literally the same oracle computation: same queries, same answers, same halting behaviour and same output if they halt.

But the fixed-point values demanded by \(Z_0\) and \(Z_1\) at \(q_0\) are opposite.

Therefore:

- if the shared computation halts binary, it accepts at most one endpoint and finitely refutes the other;
- if it halts nonbinary, it finitely refutes both;
- if neither endpoint is finitely refuted at this equation, the shared computation diverges on both.

Similarly \(Z_0\) and \(Z_2\) differ only at \(q_1\), so

\[
M^{Z_0}(q_1)=M^{Z_2}(q_1)
\]

as computations, while the two expected values are opposite.

### Proposition 6 — status constraints

With A/B/C denoting the P4-S040 local status of a raw direction:

\[
B_0\Longrightarrow A_1\text{ and }A_2,
\]

\[
B_1\Longrightarrow A_0,
\]

and

\[
B_2\Longrightarrow A_0.
\]

Consequently, if none of the three raw-adjacent companions has a finite-refutation witness, then none can be Case B.

Hence

\[
\neg A_0\wedge\neg A_1\wedge\neg A_2
\Longrightarrow
C_0\wedge C_1\wedge C_2.
\]

Moreover in that triple-C situation,

\[
M^{Z_0}(q_0)=M^{Z_1}(q_0)\uparrow
\]

and

\[
M^{Z_0}(q_1)=M^{Z_2}(q_1)\uparrow.
\]

This is a sharper local form of the surviving obstruction: a block with no finite rejection is not a harmless mixture of visible second solutions and divergence. It is forced into a triple divergence-only regime.

The proposition still does not provide a finite certificate that the shared computations diverge.

## 8. Why the wtt use bound gives no finite complete outside witness set

A finite perturbation changes only finitely many oracle coordinates. For each fixed outside input \(n\), its wtt use is finite, so the companion computation can be simulated from finitely many source values.

If it halts wrong or nonbinary, this is a valid finite refutation.

However the use map is forward information:

\[
n\mapsto u(n).
\]

It does not give a finite bound on the reverse set

\[
\{n:\text{the input-}n\text{ computation may inspect one of the changed coordinates}\}.
\]

That reverse set may be infinite.

The finite-difference cycle theorem does not alter this. It constrains a companion **after** the relevant changed-coordinate computations are known to halt correctly. It does not produce a computably finite family of outside equations guaranteed to catch every non-fixed companion.

Therefore no finite outside witness set is forced by the committed wtt data.

## 9. Target-equivalent normal-form tests

The requested normal-form operations were tested against the same effectivity boundary.

### Dovetail several target-correct computations

Dovetailing is useful only when every candidate computation used for output is already known to be target-correct.

Running altered-oracle variants in parallel does not provide such a guarantee. A variant can halt earlier with the wrong target value.

Waiting for agreement reintroduces the divergence problem.

### Add redundant equations

Additional self-avoiding target-correct equations can only add c.e. wrong-halt certificates.

They cannot turn the absence of such a certificate into a positive finite fact.

### Duplicate local checks

Duplication changes no domain information. A divergent local answer pattern remains divergent.

### Compose autoreduction equations

Composition need not preserve syntactic self-avoidance: an input-\(n\) computation may call an autoreduction at another coordinate whose computation queries \(n\).

The finite dependency closure can also be infinite, exactly as the earlier recoding sessions warned.

### Close a finite wtt use window

For fixed \(n\), the finite set of answer patterns below \(u(n)\) is explicit.

The halting subset of that finite cube is c.e.

If the actual target answer pattern were supplied as a finite parameter, one could of course hard-code arbitrary behaviour on selected neighboring patterns while preserving the target entry.

But the compiler is not allowed to use \(Y\) as a noncomputable parameter.

Uniformly from the index of \(M\), there is no computable stage at which an as-yet-unseen halt can be certified never to occur. Assigning a fallback value to such a pattern can overwrite an arbitrarily late target-correct halt.

This is the exact global-uniformity obstruction.

### Lemma 7 — no uniform finite-table total extension principle

There is no computable procedure which, from an arbitrary index for a partial computable function on a finite domain, uniformly outputs a total extension agreeing with every value that the original partial function eventually defines.

#### Proof sketch

On a two-point domain, let the first point halt immediately with \(0\), while the second point halts with \(1\) exactly if a chosen Turing machine halts.

A uniform total extension preserving every eventual defined value would, when evaluated at the second point, decide whether the chosen machine halts. ∎

The wtt local-table problem is a structured instance of this general negative-information obstacle.

This lemma does not prove that the particular committed \(M\) has no special target-equivalent improvement. It proves that the use bound alone cannot supply one uniformly.

## 10. What has and has not been obtained

### Obtained

1. Exact finite-perturbation totality collapse to truth-table autoreducibility.
2. Therefore some finite perturbation of the committed \(Y\) causes divergence.
3. A well-defined minimal raw divergence radius \(\rho\).
4. The sharp conditional theorem
   \[
   \rho\ge2\Longrightarrow X\notin OH,
   \]
   hence
   \[
   X\in OH\Longrightarrow\rho=1.
   \]
5. A finite-difference dependency-cycle theorem.
6. Exact two-cycle / three-cycle classifications for \(011,101,111\).
7. A stronger pairwise raw-adjacent status law, including triple-C collapse when no finite rejection exists.
8. A precise explanation of why wtt forward use does not provide finite reverse refutation closure.
9. A precise uniformity obstruction to the tested target-equivalent totalization schemes.

### Not obtained

No target-equivalent self-avoiding wtt presentation \(M'\) has been proved to make every actual raw-radius-one companion decisive.

No actual P4-S040 raw destroyer for \(X\) has therefore been obtained unconditionally.

No proof of

\[
X\in OH
\]

has been obtained.

No OH non-invariance theorem and no

\[
R_2\subsetneq OH
\]

conclusion is claimed.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

## 11. New exact boundary

The remaining source-side question is narrower than at the start of the session.

Arbitrary finite-perturbation partiality is no longer the issue: it is forced.

Higher-radius-only partiality is also no longer a viable obstruction to P4-S040: if all raw radius-one perturbations are total, then \(X\notin OH\).

Therefore the surviving branch is **raw-radius-one partiality**, and the remaining gap is to decide whether that partiality can be forced into the three local block equations as divergence-only Case C, or whether every radius-one divergence can be accompanied by a finite local refutation that leaves P4-S040 decisiveness intact.

The finite dependency cycles describe the positive fixed-point arm. They do not decide this local-partiality placement question.

## 12. Next bounded target

P4-S042 should attack **localization of radius-one divergence**.

For a radius-one raw perturbation \(Z=Y^{\{j\}}\) with some divergent equation \(M^Z(n)\), use the halting target computation \(M^Y(n)\) and the finite changed virtual support \(Ae_i\) to ask:

- must the target trace query a changed block coordinate before the two computations separate;
- can a minimal divergent outside input be converted into divergence or finite refutation at one of the block equations \(q_r\);
- can dependency chains be followed back to the changed support without requiring a computably finite reverse closure;
- can divergence remain permanently remote while all three local block equations are decisive;
- and can a target-equivalent self-avoiding presentation relocate remote radius-one divergence into the local block family without negative divergence information?

A positive localization theorem producing raw-adjacent Case C would sharply characterize the only possible surviving OH branch.

A theorem that radius-one divergence may remain remote while local decisiveness always holds would instead trigger P4-S040 and eliminate the present source.

Do not return to ordinary raw-martingale pricing, the P4-S015–P4-S031 bankroll line, P4-S037/P4-S038 backward prices, or ambiguity mass.

## Guards

All validated mathematics through P4-S040 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

Phase 4 remains OPEN. Phase 5 remains CLOSED.

No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.
