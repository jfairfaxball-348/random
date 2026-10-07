# P4-S041 close

Date: 2026-10-07
Session: P4-S041
Incoming checkpoint: c7735bca90102348d6a52afed16eb20ca8d3e2e1
Scope: finite-perturbation refutability and raw-radius-one partiality
Status: **COMPLETED**

## Result

P4-S041 proves the intended finite-perturbation collapse exactly.

Let \(M\) be the committed syntactically self-avoiding wtt autoreduction of the P4-S011 computably random source \(Y\), with computable use bound \(u(n)\).

If \(M\) halted on every input for every oracle differing from \(Y\) on finitely many coordinates, then for each \(n\) every answer pattern below \(u(n)\) would be realized by a finite perturbation of \(Y\). All finitely many pattern simulations would therefore halt. Dovetailing them produces a finite total truth table; nonbinary off-target outputs can be normalized without changing the target value. Self-avoidance removes the current input coordinate. Thus \(Y\) would be truth-table autoreducible.

The retained P4-S011 source authority records the opposite boundary for computable randomness. Therefore some finite perturbation of \(Y\) must make some \(M(n)\) diverge.

Transporting finite perturbations through the invertible three-bit recoding gives a minimal raw divergence radius

\[
\rho\ge1.
\]

The key new dichotomy is

\[
\rho\ge2\Longrightarrow X\notin OH.
\]

Indeed if no single raw flip causes any divergence, every raw-adjacent companion is total on the three local block equations. It is then either accepted or finitely refuted, so P4-S040 decisiveness holds on every block and the validated three-scan theorem destroys \(X\).

Hence

\[
X\in OH\Longrightarrow \rho=1.
\]

This does not identify local Case C: radius-one divergence may occur only at an outside equation, or a locally wrong halt may already make the companion decisive.

P4-S041 also proves a finite-difference dependency theorem. If \(Y\) and a finite perturbation \(Z\) are both fixed points, every changed output coordinate must obtain its changed value by querying another changed coordinate. The canonical first-difference graph has minimum out-degree one and therefore a directed cycle.

For the raw-adjacent supports:

\[
\operatorname{supp}(011)=\{q_1,q_2\}
\]

forces

\[
q_1\leftrightarrow q_2,
\]

\[
\operatorname{supp}(101)=\{q_0,q_2\}
\]

forces

\[
q_0\leftrightarrow q_2,
\]

and

\[
\operatorname{supp}(111)=\{q_0,q_1,q_2\}
\]

has exactly a two-cycle with a tail or an oriented three-cycle as its canonical witness graph.

These are positive Case-B certificates, not finite Case-C refutations.

There is also a sharper pairwise law. The direction-0 and direction-1 companions differ only at \(q_0\), so their \(M(q_0)\) computations are identical while their expected values are opposite. Likewise directions 0 and 2 share the same \(M(q_1)\) computation with opposite expectations. Therefore

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

If no direction has a finite rejection, all three directions are forced into Case C, with shared divergence at the displayed equations.

The requested target-equivalent normal-form operations do not remove the obstruction from the committed data. Extra equations add only c.e. refutation witnesses. The wtt use bound gives no finite reverse dependency closure. Closing a finite use window would require deciding which answer patterns never halt, and the compiler is not allowed to use the noncomputable target \(Y\) as a parameter.

No unconditional raw destroyer for \(X\) is obtained and no proof of \(X\in OH\) is obtained.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## Next bounded target

P4-S042 should localize radius-one divergence.

Given a single-raw-bit perturbation \(Z=Y^{\{j\}}\) and an outside input \(n\) with \(M^Z(n)\uparrow\), test whether the target computation \(M^Y(n)\) and the finite support \(Ae_i\) force a dependency chain back to one of the three block equations, yielding local Case C or a finite refutation.

The exact alternatives are:

- remote radius-one divergence can always be converted into a raw-adjacent local Case-C witness;
- remote divergence can coexist with local decisiveness, in which case P4-S040 may still eliminate the source;
- or a target-equivalent self-avoiding presentation can relocate the divergence into or out of the local block family.

Do not return to ordinary raw-martingale compilation, the frozen bankroll line, backward-price normalization or ambiguity mass.
