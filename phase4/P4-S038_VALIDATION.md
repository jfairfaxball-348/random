# P4-S038 validation

Date: 2026-10-07
Session: P4-S038
Incoming checkpoint: edae61899419825b2aa7610aa600e2804e9b8d1d
Scope: persistent-frontier retirement and the c.e. price jump
Status: **VALIDATED**

## Repository and scope checks

- Immediately before the first P4-S038 write, live main was exactly edae61899419825b2aa7610aa600e2804e9b8d1d, the P4-S037 outgoing checkpoint.
- Repository search returned no P4-S038 record before the write, so P4-S038 was unique.
- P4-S001 through P4-S037 were fetched/read as committed mathematical authority.
- The selected CAND-01 authority, the sustained pivot, and P4-S032 through P4-S037 were read.
- All validated mathematics through P4-S037 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling line was not reopened.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. Value closure and retirement are genuinely different

The committed P4-S011 machine is a wtt autoreduction. Its use bound gives a computable finite oracle-value frontier for each sentinel computation, and the autoreduction never queries the sentinel itself.

After that finite frontier is exposed, every future oracle answer used by the fixed computation is already determined. Later filler values therefore cannot alter the computation.

But a finite simulation may still fail to decide whether the fixed computation eventually produces a binary halt. Continuing the simulation can reveal a halt after arbitrarily many later filler stages, while divergence has no finite witness.

Thus the P4-S038 persistent state contains only finite computable data and does not smuggle in the trigger/nontrigger answer. “Value-closed” is effective; “retired” need not be.

### 2. The half-stake price really is one jump

Before a binary prediction is visible, the half-stake virtual martingale holds on the sentinel, so its normalized multiplier is one.

If prediction sign \(a\in\{-1,+1\}\) appears and the already raw-known sentinel sign is \(z\), the fractional half-stake multiplier is

\[
1+\frac12az.
\]

Hence the two-coordinate normalized price is exactly \((1,1)\) before the trigger and then exactly one of

\[
(3/2,1/2),\qquad(1/2,3/2).
\]

The fixed computation can expose at most one first binary halt, so there is at most one price jump. A visible nonbinary halt is permanently nontriggering under the settled P4-S011 convention and leaves the price at \((1,1)\).

This validates the finite-horizon formula.

### 3. The semicomputability classification is exact

Binary positive-sign and negative-sign trigger events are separately c.e. by finite simulation. Their union is c.e.; its complement is co-c.e.

The limiting coordinates are

\[
1+\tfrac12\mathbf 1_{B_+}-\tfrac12\mathbf 1_{B_-}
\]

and its sign-reversed companion. They therefore have computable one-change approximations and are differences of left-c.e. quantities.

Uniformly over states, a coordinate is not forced to be one-sided semicomputable because one c.e. trigger orientation raises it and the other lowers it.

The mean of the two coordinates is always one. The spread is zero on nontriggering states and one on binary-triggering states, so the spread is left-c.e.

An oracle deciding the local trigger event computes the exact vector: if positive, finite simulation eventually gives the sign. Conversely the exact vector decides whether the trigger occurred because the two possible triggered vectors are separated from \((1,1)\).

No equivalence with the full halting set is asserted.

### 4. Fixed positive jump makes the effective hypotheses collapse

For general fixed computable \(r>0\), any future trigger changes the vector by sup norm exactly \(r\).

Therefore:

- a deadline decides trigger by finite simulation;
- an eventual-constancy modulus does the same;
- a Cauchy modulus at tolerance \(<r/2\) rules out any later unseen jump;
- an exact limit approximation finer than \(r/3\) separates the no-jump vector from either triggered vector;
- a semidecision for nontriggering, combined with the existing c.e. trigger semidecision, decides the event.

Conversely, a trigger decision gives all of these data by simulating to the halt when the answer is positive.

Theorem 4 is therefore valid for this discrete one-jump process.

### 5. A uniform trigger decision would contradict the settled recoded witness

Assume a computable trigger/nontrigger decision existed uniformly on all reachable value-closed P4-S011 frontiers.

On a positive state one can simulate until the binary halt and retire the claim. On a negative state the half-stake witness has no future nonzero wager in that stuck epoch; the state can be treated as absorbing for the capital while an exhaustive raw evaluator continues through irrelevant coordinates.

This supplies the missing effective retirement/absorption transition required by the P4-S037 rolling compiler.

The half-stake martingale succeeds on \(H(X)=Y\), while \(X\in CR\) is settled. A successful total computable raw martingale would be impossible.

Hence the uniform trigger decision cannot exist. The same argument transfers through Theorem 4 to deadlines and normalized-price moduli.

This is a contradiction argument internal to the committed witness, not a halting-set reduction.

### 6. Absolute persistent-savings prices cannot have a computable Cauchy modulus

P4-S037 Theorem 9 already states that a computable Cauchy modulus for the absolute backward prices of the P4-S036 persistent-savings martingale makes their limits computable and yields one consistent total raw martingale.

Applying it to the actual recoded P4-S011 target would transfer the successful virtual witness to the computably random source \(X\).

Therefore no such uniform modulus can exist. Corollary 7 follows directly from settled P4-S037 mathematics.

### 7. The two-orientation hedge cost is exactly \(1+r\)

The two possible triggered normalized vectors are

\[
(1+r,1-r),\quad(1-r,1+r).
\]

Any coordinatewise nonnegative superhedge covering both must have each coordinate at least \(1+r\). Its fair mean is therefore at least \(1+r\).

The constant vector \((1+r,1+r)\) attains that lower bound.

Thus \(1+r\) is the exact positive orientation-free cost. Equal mixing of the two fair vectors gives \((1,1)\) and loses the advantage; unequal mixing just commits to a sign.

This validates the upper-envelope, two-account and delayed-commitment analysis.

### 8. Computable supermartingales have computable martingale covers here

For a computable rational supermartingale \(s\), define

\[
\delta(\sigma)=s(\sigma)-\frac{s(\sigma0)+s(\sigma1)}2\ge0.
\]

Accumulating the defect equally on both children and setting \(m=s+A\) gives

\[
\frac{m(\sigma0)+m(\sigma1)}2=m(\sigma).
\]

All values remain nonnegative computable rationals and \(m\ge s\).

Therefore a successful total computable rational supermartingale suffices to contradict computable randomness under the repository convention.

This conversion is algebraically exact and does not itself supply the reserve required by an unresolved orientation.

### 9. The multiplicative uncertainty budget theorem is sound

Apply the P4-S036 persistent-savings transform before the budget construction.

A stopped summand wagers zero after stopping; an active summand has the same fractional wager as the original martingale. In the weighted sum, the aggregate fractional wager is a capital-weighted average diluted by stopped capital, so its magnitude is no larger than the original \(r_e\). The uncertainty budget therefore survives the transform.

Let

\[
P_e=\prod_{i<e}(1+r_i),\qquad A_e=K/P_e.
\]

Then \(A_e\ge1\) and \(A_e=(1+r_e)A_{e+1}\).

At an unresolved persistent frontier with persistent-savings capital \(c\), reserve \(A_ec\). While only irrelevant fillers are read, keep that reserve unchanged.

When a trigger is exposed, its realized multiplier satisfies

\[
m_e=1+r_ea_ez_e\le1+r_e.
\]

Therefore

\[
A_{e+1}cm_e\le A_ec.
\]

After value closure, the finite simulation fact is independent of the new filler bit values, so the reserve decrease can be made equally on both raw children at the stage where the halt becomes visible. This is a legitimate supermartingale move.

Finite nonpersistent transitions are handled by the already validated finite Doob pieces from P4-S037.

If no trigger appears, the reserve remains constant and totality is preserved. Since \(A_e\ge1\), the raw reserve dominates the persistent-savings capital at every persistent frontier. Persistent savings makes successful capital survive arbitrarily long waiting intervals and tend through arbitrarily large locked floors.

Hence the raw supermartingale succeeds, and §8 converts it into a raw martingale.

Theorem 10 is therefore valid.

### 10. The budget does not secretly contain a retirement modulus

A computable rational upper bound on

\[
\sum_e r_e
\]

gives a computable rational product bound because

\[
\prod_e(1+r_e)\le \exp\!\left(\sum_e r_e\right).
\]

No computable tail modulus follows merely from knowing a finite upper bound.

Conversely, for \(0\le r\le1\),

\[
r/2\le\log(1+r)\le r,
\]

so a finite product bound implies a finite sum bound up to a computable coarse rational majorant.

A computable summable sequence such as \(r_e=2^{-e-2}\) can be attached to a c.e. trigger family with undecidable nontriggering. Thus the multiplicative-budget compiler is strictly weaker in retirement information than decidable stabilization.

### 11. Stake decay has the claimed sharp threshold for pure sentinel gain

On an all-correct target, the \(e\)-th sentinel multiplies capital by \(1+r_e\), so target capital is

\[
d_0\prod_{e<n}(1+r_e).
\]

For \(r_e\in[0,1]\), the logarithmic inequalities above show that this product diverges exactly when \(\sum_e r_e\) diverges.

The exact orientation-free positive hedge factor for the same claim is also \(1+r_e\). Its cumulative cost is the same product.

Therefore no shrinking stake sequence can make the pure correct-prediction sentinel capital unbounded while keeping the universal positive unresolved-orientation hedge finite.

This validates Theorem 12. It is a backward-price statement, not a reuse of the P4-S015–P4-S031 bankroll accounting.

### 12. The actual half-stake witness is outside both positive compiler classes

For the actual witness \(r_e=1/2\) at every completed target epoch.

The target growth and minimal orientation-free hedge factor are both \((3/2)^n\), hence unbounded. The witness therefore fails the finite multiplicative uncertainty budget.

It also fails effective fresh renewal / stabilization by the contradiction arguments above.

This exactly locates the actual recoded P4-S011 witness beyond both current positive theorems.

### 13. Separation guard

No proof of

\[
X\in OH
\]

is obtained.

The available fact is \(H(X)=Y\notin OH\). Therefore there is still no OH non-invariance theorem and no strict \(R_2\subsetneq OH\) conclusion.

The retained comparison is

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation is unchanged.

## Validation disposition

**PASS.**

P4-S038 gives both a strict positive extension of the P4-S037 compiler boundary and an exact negative diagnosis of the actual recoded P4-S011 persistent claim.

The positive extension is the computable finite multiplicative uncertainty budget, which handles genuinely non-effectively retiring claims by prepaying their exact worst-case orientation cost.

The negative diagnosis is sharp for the pure correct-prediction sentinel mechanism: that cost product is exactly the same product which drives virtual success, so stake decay cannot separate gain from unresolved pricing cost.

The sustained equation \(R_2=OH\) remains unresolved. The next useful attack is source-side one-hole simulation under the displayed three-bit recoding, not another ordinary raw-martingale compiler refinement.
