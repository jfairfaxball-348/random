# Next Session Prompt — P4-S042

Continue the Fairfax-Ball Randomness Research Programme in https://github.com/jfairfaxball-348/random.

Run only Phase 4 — Mathematics session P4-S042. Treat committed repository state as authoritative. Pin live main at the exact P4-S041 outgoing checkpoint reported by the preceding session, reconcile any mismatch, confirm P4-S042 is unique, and read P4-S001 through P4-S041, the required CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, phase4/P4-S032_MATHEMATICS.md through phase4/P4-S041_MATHEMATICS.md, with special attention to P4-S011, P4-S012, P4-S039, P4-S040 and P4-S041.

## Sustained Phase-4 target — one-hole normalization after coded recoding

Freeze all validated mathematics through P4-S041. Do not return to the P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, the P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation, or ambiguity mass unless the theorem below genuinely requires them.

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

The current inclusions remain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Retain the repeated three-bit recoding

\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2,
\]

with

\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix},
\]

and columns

\[
c_0=111,\qquad c_1=011,\qquad c_2=101.
\]

Let \(Y\) be the settled P4-S011 computably random wtt-autoreducible source, \(M\) its committed syntactically self-avoiding wtt autoreduction, \(D\) its one-hole destroyer, and

\[
X=H^{-1}(Y).
\]

Retain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

The missing source-side statement remains whether \(X\in OH\).

## P4-S041 boundary to retain

P4-S041 proves the finite-perturbation totality collapse:

> If \(M\) halts on every input for every finite perturbation of \(Y\), then the computable wtt use bound makes every finite answer pattern below the use halt, so \(M\) compiles to a truth-table autoreduction of \(Y\).

The retained P4-S011 source authority excludes computably random truth-table-autoreducibility. Therefore some finite perturbation of \(Y\) causes divergence.

Transporting finite perturbations through the invertible recoding defines the minimal raw divergence radius

\[
\rho=\min\{|F|:(\exists n)\ M^{Y^F}(n)\uparrow\}.
\]

P4-S041 proves

\[
\rho\ge2\Longrightarrow X\notin OH,
\]

because totality of every single-raw-bit companion implies P4-S040 raw-adjacent decisiveness everywhere.

Therefore

\[
X\in OH\Longrightarrow\rho=1.
\]

Do not reverse this implication.

Raw-radius-one divergence does not by itself give P4-S040 Case C. It may occur only at an outside equation \(M(n)\), or a companion may have a divergent equation while another local equation already gives a finite wrong/nonbinary refutation.

P4-S041 also proves the finite-difference dependency-cycle theorem. For genuine fixed-point companions, every changed coordinate depends on another changed coordinate. The raw-adjacent supports satisfy:

\[
011:\ q_1\leftrightarrow q_2,
\]

\[
101:\ q_0\leftrightarrow q_2,
\]

while \(111\) has a two-cycle with a tail or an oriented three-cycle as its canonical first-difference graph.

These are positive Case-B structures, not finite Case-C certificates.

Finally, if A/B/C denote the P4-S040 local status of raw directions,

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

Hence a block with no finite rejection is necessarily triple Case C, with shared local divergences at the pairwise single-difference equations. No finite stage certifies that triple-C outcome.

## P4-S042 bounded task — localize raw-radius-one divergence

Attack only the gap between “some equation diverges on a single-raw-bit companion” and “one of the three block equations is divergence-only Case C”.

Do not return to general totalization or ordinary martingale pricing.

### 1. Formalize remote versus local radius-one partiality

Fix one raw coordinate \(j=(B,i)\) and let

\[
Z=Y^{\{j\}}.
\]

Distinguish:

- **local partiality:** \(M^Z(q_r)\uparrow\) for some \(q_r\in B\);
- **remote partiality:** \(M^Z(n)\uparrow\) for some \(n\notin B\);
- **local Case C:** at least one local block equation diverges and every local equation which halts is correct for \(Z\);
- **decisive despite partiality:** some equation may diverge, but one local equation finitely refutes \(Z\), so P4-S040 still classifies the companion as Case A.

Do not conflate these.

### 2. Use the halting target trace of a divergent companion equation

Suppose

\[
M^Z(n)\uparrow,\qquad M^Y(n)\downarrow=Y(n).
\]

The target computation is finite and has a definite query trace.

Ask whether divergence after changing only the support

\[
S_i=\operatorname{supp}(c_i)
\]

forces the target trace to query at least one coordinate in \(S_i\).

Prove the exact statement. In particular, if the target computation never queries \(S_i\), the two computations see identical answers and must behave identically, contradicting divergence.

Then identify the first queried changed coordinate and what this says about the dependency of the remote divergence on the block.

### 3. Build a divergence dependency relation

For a radius-one raw companion \(Z\), define a relation from a divergent input \(n\) to changed coordinates or to further inputs only when the relation is justified by finite target traces.

Test whether one can follow a finite chain from any remote divergent equation back to one of the changed block inputs \(q_r\).

Do not assume a computably finite reverse dependency closure. The relation must be oriented using information actually supplied by halting target computations.

Determine whether minimality of \(n\), minimal wtt use, or minimal target-trace contact produces a well-founded descent.

If no well-founded measure exists, isolate the exact obstruction.

### 4. Test localization by minimal use

Let \(u(n)\) be the computable wtt use bound.

Among all divergent inputs for a fixed radius-one companion, choose one with minimal use \(u(n)\), if this helps.

The target trace must contact a changed coordinate.

Ask whether the contacted changed coordinate \(q_r\) can itself diverge under \(Z\), or whether its companion computation may halt correctly and pass the perturbation onward through another queried changed coordinate.

Use the P4-S041 finite dependency-cycle theorem when the local computation halts correctly.

The goal is to decide whether a minimal-use remote divergence can terminate only in:

- a local Case-C divergence;
- a finite local refutation;
- or a genuine cycle of correct local halts that leaves divergence remote.

### 5. Exploit the exact support sizes

Treat separately:

\[
S_1=\{q_1,q_2\},\qquad
S_2=\{q_0,q_2\},\qquad
S_0=\{q_0,q_1,q_2\}.
\]

For the two-coordinate supports, accepted local companions force a two-cycle.

Ask whether this rigid cycle makes remote divergence impossible, or merely means the outside divergent computation can depend on the already-closed two-cycle.

For the three-coordinate support, compare the two-cycle-with-tail and three-cycle cases.

Do not infer global fixed-pointhood from local cycle acceptance.

### 6. Use the pairwise raw-adjacent law aggressively

Retain

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

Try to strengthen it when a direction has remote divergence.

Examples to test:

- can remote partiality in direction 1 coexist with \(B_1\), hence force \(A_0\);
- can remote partiality occur in all three directions while some directions remain A or B locally;
- does absence of any A still force explicit shared local divergence exactly as in P4-S041;
- can one obtain a finite rejection in one direction from a remote divergence trace in another without negative information?

Any strengthened status law should be exact and finite-evidence based.

### 7. Test target-equivalent localization normal forms, not totalization

The normal-form goal is now weaker.

Do not try to make every radius-one companion total.

Ask whether \(M\) can be replaced uniformly by a target-equivalent syntactically self-avoiding wtt \(M'\) such that any radius-one divergence affecting \(M'\) is localized to a changed block equation, while finite local rejections remain allowed.

Potential operations:

- duplicate an outside equation into a changed block equation without querying that block input itself;
- redirect finite target traces through a block coordinate;
- use tagged compositions which preserve syntactic self-avoidance;
- choose a canonical lowest-use divergent dependency if such a choice can be made positively;
- or prove that any localization compiler would still require negative divergence information.

Any \(M'\) must be computable uniformly from committed data. Do not use \(Y\) as a noncomputable program parameter.

### 8. Test whether remote partiality is harmless for P4-S040

P4-S040 needs only local decisiveness.

It is possible in principle that \(M\) has unavoidable radius-one divergence somewhere but every raw-adjacent companion is still locally A or B.

If this can be proved for the committed mechanism, apply P4-S040 fully and conclude

\[
X\notin OH.
\]

Do not stop at the observation that remote divergence exists.

Conversely, if remote divergence can coexist with local Case C, state exactly what additional hypothesis is needed to force persistent Case C on reached synchronized blocks.

### 9. Separate one witness from enough witnesses

A theorem that some single raw perturbation has local Case C is not enough by itself to defeat the P4-S040 three-scan theorem on infinitely many reached blocks.

Distinguish:

- one radius-one divergent perturbation;
- one local Case-C direction;
- a Case-C direction on infinitely many fresh blocks;
- enough Case-C directions to block every finite-family synchronized raw scan;
- persistent Case C for every target-equivalent presentation.

Do not infer stronger recurrence from a single witness.

### 10. Preserve the source-side separation guard

An OH non-invariance theorem still requires

\[
X\in OH,\qquad H(X)=Y\notin OH.
\]

Only the second statement is settled.

If P4-S042 obtains local decisiveness everywhere, invoke P4-S040 and conclude only

\[
X\notin OH,
\]

eliminating this source as a separation candidate.

If P4-S042 localizes some divergence to Case C, \(X\in OH\) still does not follow unless all one-hole destroyers are excluded.

### 11. Required session outcome

The output should be one of:

- a theorem that every raw-radius-one divergent companion necessarily has local Case C or finite local refutation, with the exact branch classification;
- a theorem that radius-one divergence can remain genuinely remote while all three local block equations are decisive, followed by P4-S040 if this holds for the committed source;
- a target-equivalent self-avoiding wtt localization normal form;
- a well-founded/minimal-use dependency theorem sharply reducing remote divergence to the block support;
- a construction/obstruction showing why remote divergence cannot be localized from the committed data;
- or, only if it follows directly, an actual proof of \(X\notin OH\) or \(X\in OH\).

The sustained question remains

\[
R_2=OH\;?
\]

If no OH non-invariance witness is proved, preserve \(OH^{iso}\) as the comparison class and state separation status explicitly.

P4-S032 null-ambiguity preservation remains available. Do not return to ambiguity mass as an invariant.

Preserve PA-0001 as **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 unchanged. Make no novelty, openness, prior-art, Gate-4, publication or outreach claim. Continue original mathematics only.

Record, validate and synchronize useful work, commit it, verify remote main, report the exact outgoing hash, and provide the next prompt if no blocker exists.
