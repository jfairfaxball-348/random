# P4-S041 validation

Date: 2026-10-07
Session: P4-S041
Incoming checkpoint: c7735bca90102348d6a52afed16eb20ca8d3e2e1
Scope: finite-perturbation refutability and raw-radius-one partiality
Status: **VALIDATED**

## Repository and scope checks

- Live main immediately before the first P4-S041 write was exactly c7735bca90102348d6a52afed16eb20ca8d3e2e1, the final P4-S040 outgoing checkpoint.
- The phase4 directory contained P4-S001 through P4-S040 and no P4-S041 mathematics, close or validation file.
- P4-S001 through P4-S040 were read.
- The selected CAND-01 authority, P3-S007 selection, P3-S008 Gate-3 review, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md and P4-S032 through P4-S040 were checked.
- P4-S011 and P4-S012 were reread in detail.
- The retained source authority was checked at SRC-0067/SRC-0068/THM-0076. SRC-0067 records both the computably random wtt-autoreducible existence result and the contrast that no rec-random set is truth-table autoreducible.
- All validated mathematics through P4-S040 is preserved.
- The P4-S015–P4-S031 bankroll sequence, P4-S037/P4-S038 backward-price route and ambiguity mass were not reopened.
- No ordinary raw-martingale compilation was attempted.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. Finite-perturbation totality collapse uses the wtt bound correctly

For fixed input \(n\), let \(u(n)\) bound every oracle query.

Every binary answer pattern below \(u(n)\) is realized by changing only those finitely many target coordinates on which the pattern differs from \(Y\).

Therefore the hypothesis that \(M\) halts on all finite perturbations implies that the input-\(n\) simulation halts for every finite answer pattern in the use window.

There are only finitely many patterns. Dovetailing all of them until completion is a terminating computable procedure.

This produces a total finite truth table uniformly in \(n\).

The proof does not assume a halting-time bound in advance.

### 2. Nonbinary off-target outputs do not block the collapse

Truth-table autoreducibility of \(Y\) requires target-correct binary output, not preservation of arbitrary off-target nonbinary values.

After the finite table has been computed, any nonbinary entry may be replaced by \(0\).

The target entry is already binary and correct.

Hence the collapse theorem remains valid under the repository's P4-S040 convention allowing nonbinary finite refutation off target.

### 3. Self-avoidance is preserved

The committed program syntactically avoids coordinate \(n\) when computing input \(n\).

The compiled finite answer table therefore has no need to consult the current bit.

Thus the result is a truth-table **autoreduction**, not merely a total truth-table computation of some unrelated function.

### 4. The retained source authority supports the contradiction used

SRC-0067 records:

- existence of a rec-random weak-truth-table-autoreducible set; and
- the contrast with the known impossibility of rec-random truth-table autoreducibility.

SRC-0068/THM-0076 fixes the wtt use and self-avoidance conventions for the committed P4-S011 source.

Therefore the finite-perturbation totality hypothesis is incompatible with the retained authority for this \(Y\).

The conclusion is exactly that **some** finite perturbation causes divergence.

No radius-one conclusion is inferred at this stage.

### 5. Finite virtual perturbations and finite raw perturbations correspond

The three-bit recoding is blockwise invertible over \(\mathbb F_2\).

A finite virtual difference changes finitely many blocks and has a unique finite raw preimage difference.

Hence the set of raw finite perturbations producing divergence is nonempty.

The minimum cardinality \(\rho\) is therefore well-defined and positive.

### 6. The radius dichotomy is exact

If \(\rho\ge2\), every radius-one raw perturbation is total on every input.

Fixing a raw-adjacent companion, the three P4-S040 local equations therefore all halt.

Either all three halt correctly, giving Case B, or at least one halt is wrong/nonbinary, giving Case A.

Thus all three directions are decisive on every block.

This is stronger than the exact P4-S040 hypothesis, so its validated three-scan theorem applies and gives

\[
X\notin OH.
\]

Therefore

\[
X\in OH\Rightarrow\rho=1.
\]

No converse is asserted.

### 7. Radius-one divergence is weaker than local Case C

A radius-one perturbation may make some outside equation diverge while all three block equations are decisive.

It may also contain a divergent block equation but already have a different wrong local halt, making the companion Case A.

Thus \(\rho=1\) does not imply P4-S040 failure.

The validation preserves this distinction.

### 8. The finite-difference dependency-cycle theorem is correct

Let \(Y,Z\) be fixed points differing on finite \(S\).

For \(n\in S\), the input-\(n\) computations halt with opposite outputs.

They cannot distinguish \(Y\) and \(Z\) by querying \(n\), because \(M\) syntactically avoids its current input.

Before the deterministic computation histories first separate, they make the same query. The first answer on which they differ must therefore be at a coordinate in \(S\setminus\{n\}\).

Choosing that coordinate gives one outgoing edge from each changed vertex, no loops.

Every finite directed graph with minimum out-degree one contains a directed cycle.

The argument does not assume both computations halt until that fact has been explicitly included in the fixed-point hypothesis.

### 9. The two-bit support classifications are forced

For support \(\{q_1,q_2\}\), each vertex must point to the other, so the graph is the unique two-cycle.

The same holds for \(\{q_0,q_2\}\).

For three vertices, a loop-free functional digraph contains either:

- one two-cycle, with the remaining vertex feeding one member of that cycle; or
- a three-cycle.

This yields the stated six labelled two-cycle-with-tail patterns and two oriented three-cycles.

### 10. The cycle theorem also applies to local Case B

For a locally accepted raw-adjacent companion, every changed block coordinate has:

- a halting target computation with target output; and
- a halting companion computation with the opposite correct output.

That is exactly the data needed for the first-difference argument on changed coordinates.

No global fixed-pointhood of outside equations is silently assumed.

### 11. Cycles do not refute Case C

A Case-B cycle becomes visible only after the relevant companion computations halt.

If one required computation diverges, the missing edge has no finite negative certificate.

Therefore the cycle theorem is a positive structural classification of Case B, not a completion procedure for Case C.

### 12. The pairwise raw-adjacent status law is correct

The companions \(Z_0,Z_1\) differ only at \(q_0\).

Because input \(q_0\) never queries coordinate \(q_0\), the two oracle computations are identical.

Their expected fixed-point values at \(q_0\) are opposite.

Thus a binary halt accepts at most one and refutes the other; a nonbinary halt refutes both; absence of refutation at that equation forces common divergence.

The identical argument applies to \(Z_0,Z_2\) at input \(q_1\).

Therefore

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

If no A-status exists, no B-status can exist, so all three companions are Case C.

The two shared divergences stated in the mathematics record follow directly.

### 13. The reverse-closure guard is preserved

A wtt use bound gives a computable finite oracle window for each fixed input.

It does not bound the number of input indices whose computations may inspect a fixed changed coordinate.

Therefore no computably finite complete set of outside equations follows from wtt alone.

The finite-difference cycle theorem does not change this direction of information.

### 14. The normal-form obstruction is stated at the correct strength

The session does **not** prove that no special target-equivalent presentation of the actual \(Y\) can improve radius-one decisiveness.

It proves that the tested totalization does not follow uniformly from the committed wtt data.

The finite use table has a c.e. halting domain. Filling an as-yet-unseen pattern safely requires knowing it will never halt or knowing the actual target pattern. Neither resource is supplied.

The abstract finite-table lemma correctly demonstrates that a uniform total extension preserving all eventual values would decide halting.

### 15. Source-side separation guard is preserved

The settled facts remain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

P4-S041 does not prove

\[
X\in OH.
\]

It also does not unconditionally prove

\[
X\notin OH,
\]

because the radius \(\rho\) is not determined.

No OH non-invariance theorem and no strict

\[
R_2\subsetneq OH
\]

conclusion follows.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

## Validation disposition

**PASS.**

P4-S041 materially narrows the finite-perturbation boundary.

Finite-perturbation divergence is unavoidable. If it first appears only beyond raw radius one, the existing P4-S040 theorem already destroys the recoded source. Thus any surviving proof of \(X\in OH\) must confront genuine raw-radius-one partiality.

The finite dependency-cycle theorem and pairwise adjacency law sharply classify the visible fixed-point arm, but neither provides a finite certificate of divergence.

The next exact problem is to localize radius-one divergence: determine whether a divergent outside equation can be forced back into the three local block equations as Case C, or can remain remote while all local companions stay decisive.
