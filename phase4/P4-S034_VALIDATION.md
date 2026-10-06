# P4-S034 validation

Date: 2026-10-06
Session: P4-S034
Incoming checkpoint: 63a6e11565d19660ec5b711a8f53bb55f73d9040
Scope: homeomorphism invariance of one-hole robustness
Status: **VALIDATED**

## Repository and scope checks

- Live main matched 63a6e11565d19660ec5b711a8f53bb55f73d9040 before substantive work and immediately before the first write.
- The Phase-4 directory contained no P4-S034 record before the first write, so the identifier was unique.
- P4-S001 through P4-S033, the selected CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, phase4/P4-S032_MATHEMATICS.md, and phase4/P4-S033_MATHEMATICS.md were read.
- Phase 4 is OPEN and Phase 5 is CLOSED.
- All validated mathematics through P4-S033 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling line was not reopened.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. Pullback of P4-S012 self-avoidance

For the displayed three-bit matrix \(A\), the inverse images of the virtual unit vectors are
\[
v_0=(1,1,0),\quad v_1=(1,0,1),\quad v_2=(1,1,1).
\]
If a virtual stake avoids coordinate \(u_i\), toggling \(v_i\) changes only \(u_i\), so the pulled-back stake is invariant under that whole raw vector. This establishes coded/vector self-avoidance.

The example dependence on
\[
u_2=x_0\oplus x_1\oplus x_2
\]
shows why this need not be raw-coordinate self-avoidance: a legal stake at \(u_0\) can depend on a parity involving every raw coordinate in its block.

This proves failure of the direct induced-stake conversion only. It is not used as evidence of OH non-invariance.

### 2. Support evaluator totality

For a fixed finite invertible block matrix, a finite raw history touches finitely many blocks and therefore makes only finitely many virtual coordinates computable without a fresh raw query. Since the virtual scan is no-repeat and total, the evaluator cannot perform infinitely many internal spoiled steps before its next raw query. Hence the raw evaluator is total.

Every emitted raw query is fresh by construction, so it is no-repeat.

### 3. Support evaluator one-hole bound

The queried raw columns in a block are the union of supports of the virtual rows queried in that block.

- If no virtual row is omitted, invertibility rules out a zero column, so every raw column is queried.
- If row \(r\) is the unique omitted virtual coordinate, an omitted raw column must have support contained in \(\{r\}\). Since an invertible matrix has no zero column, that column must equal \(e_r\).
- Two omitted raw columns would then be identical columns \(e_r\), contradicting invertibility.

Thus the raw evaluator omits at most one raw coordinate globally.

### 4. Live-wager martingale

At a live virtual stage, after all but the last fresh raw support bit are known, the requested virtual bit is the last raw bit XOR a computable constant. Copying the virtual fractional stake to that last raw bit, with an optional child swap, preserves the martingale equation exactly. Holding on all other support fillers preserves it as well.

On the target of a succeeding nonnegative martingale, capital never reaches zero, so all realized fractional multiplicative factors are defined and positive. The live product is exactly the raw evaluator martingale's capital ratio.

### 5. Exhaustiveness for the displayed matrix

The displayed matrix has columns
\[
(1,1,1)^T,\quad(0,1,1)^T,\quad(1,0,1)^T,
\]
all of weight at least two. A one-hole virtual scan omits at most one row globally, so deleting that row leaves every column represented by a queried row. Therefore every raw coordinate is eventually queried.

The evaluator is consequently injective. Its scan map is total, computable and fair-coin preserving, so P4-S001 makes it an effective isomorphism and preserves computable randomness.

### 6. Spoiled-gain necessity

Let \(D_t\) be the target capital of the virtual martingale and \(E_t\) the target capital of the raw evaluator martingale after the corresponding simulated virtual stages. Then
\[
D_t/D_0=(E_t/E_0)P_t,
\]
where \(P_t\) is the product of realized multiplicative factors at spoiled virtual stages.

Because the raw evaluator image of a computably random source is computably random, \(E_t\) is bounded. If \(D_t\) is unbounded, \(P_t\) must be unbounded. No monotonicity of either product is assumed or needed.

### 7. Finite-coordinate invariance

For a finite-coordinate recoding supported on \(B\):

- outside \(B\), the raw and virtual bits coincide, so the virtual wager can be copied exactly;
- at the first virtual query in \(B\), reading all of finite \(B\) reveals the complete finite recoded block;
- all virtual wagers in \(B\) can then be skipped and all later outside-\(B\) wagers copied;
- if the virtual scan never enters \(B\), the one-hole condition forces \(|B|\le1\);
- if it does enter \(B\), the raw scan reads all of \(B\) and can omit only the at-most-one outside coordinate omitted virtually.

Thus the raw scan is total, no-repeat and one-hole. Only finitely many target multiplicative factors are deleted. Since a succeeding nonnegative martingale has positive realized factors on its target, their finite product is a fixed positive constant, so success is preserved. The inverse recoding has the same form, giving equivalence.

The two-bit CNOT example is invertible and fair-coin preserving but its first output depends on two raw bits, so it lies strictly beyond signed coordinate permutations.

### 8. Infinitary boundary

Each finite truncation \(H_N\) of the repeated three-bit map is a finite-coordinate recoding and therefore preserves OH. The full map repeats the mixer in infinitely many blocks, so finite deletion no longer applies. The spoiled-gain theorem shows exactly what can accumulate: an unbounded product of wagers selected after their virtual parity was already raw-determined.

This is a structural obstruction, not a separation theorem.

### 9. Separation guard

No \(x\in OH\) with \(H(x)\notin OH\) is established. Therefore P4-S033's implication from OH non-invariance to \(R_2\subsetneq OH\) is not activated.

The retained comparison remains
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

### 10. Null-ambiguity guard

P4-S032 null-ambiguity preservation is unchanged and remains available as a reduction. No ambiguity-mass characterization is asserted.

## Selection validation

P4-S034 produces both a real positive invariance theorem and an exact obstruction for the first infinite coded-hole recoding. The next unresolved datum is the timing of spoiled stakes: whether the stake is already known when the raw parity becomes determined, or is chosen only after later virtual information arrives. This is the narrowest bounded continuation of the sustained \(R_2=OH\) programme and does not return to the frozen bankroll line.

## Validation outcome

**PASS.**

Owner/external blocker: **NONE.**
