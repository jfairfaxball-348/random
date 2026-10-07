# P4-S038 close

Date: 2026-10-07
Session: P4-S038
Incoming checkpoint: edae61899419825b2aa7610aa600e2804e9b8d1d
Scope: persistent-frontier retirement and the c.e. backward-price jump
Status: **COMPLETED**

## Result

P4-S038 isolates the persistent P4-S011 obstruction exactly.

After the computable wtt value-use frontier of one sentinel computation is exhausted, all future oracle **values** are irrelevant, but finite simulation may still reveal a binary halt at an arbitrarily late stage. The claim is therefore value-closed while its retirement remains only c.e.

For the half-stake sentinel martingale the finite-horizon normalized backward price is exactly

\[
(1,1)
\]

until a binary halt is witnessed, and then changes once to

\[
(3/2,1/2)
\quad\text{or}\quad
(1/2,3/2).
\]

The trigger set is c.e.; nontriggering is co-c.e.; the full vector has a computable one-mind-change approximation. Its midpoint is always one, while its nonzero spread detects the trigger.

For any fixed positive stake, a computable retirement deadline, eventual-constancy modulus, Cauchy modulus, exact limiting price and a semidecision for permanent nonretirement all collapse to the same trigger/nontrigger decision resource. No halting-set completeness claim is made.

The actual recoded P4-S011 witness cannot possess that resource uniformly. Otherwise the width-one persistent frontier would become effectively retiring/absorbing and the P4-S037 compiler would turn the successful virtual half-stake witness into one total computable raw martingale succeeding on the settled computably random source. The same contradiction shows that the absolute P4-S036 persistent-savings backward prices have no uniform computable Cauchy modulus on this family.

The obvious repairs fail sharply. Mixing the two possible triggered orientations symmetrically returns \((1,1)\); selecting the favourable orientation after the halt costs the exact factor \(1+r\); delayed commitment is therefore retroactive unless that factor was prepaid. A rolling mixture of finite simulation horizons discounts arbitrarily late triggers by the mixture tail and has no rate-free success guarantee.

A new positive theorem survives. If unresolved fractional stakes \(r_e\) have a computable finite multiplicative uncertainty budget

\[
\prod_{e<n}(1+r_e)\le K
\]

for all \(n\), then after the P4-S036 persistent-savings transform one may prepay the worst possible orientation. With

\[
A_e=\frac{K}{\prod_{i<e}(1+r_i)},
\]

the reserve \(A_ec\) never has to increase when a trigger is finally exposed, because its multiplier is at most \(1+r_e\). This gives a total computable raw supermartingale even when retirement is only c.e.; the standard computable defect-compensation construction turns it into a martingale cover. No computable retirement decision or effective tail modulus is required.

For the pure all-correct sentinel mechanism this boundary is exact. Target capital grows by

\[
\prod_e(1+r_e),
\]

and the minimal orientation-free positive hedge costs the same product. Hence shrinking \(r_e\to0\) cannot preserve unbounded pure sentinel gain while making unresolved source-side pricing cost finite. For \(0\le r_e\le1\), both thresholds are equivalent to divergence/convergence of \(\sum_e r_e\).

The fixed half-stake P4-S011 witness has cumulative factor \((3/2)^n\), so it lies outside both P4-S037 fresh renewal and the new finite-uncertainty-budget theorem.

No proof of

\[
X\in OH
\]

is obtained. Thus no OH non-invariance theorem and no

\[
R_2\subsetneq OH
\]

claim is available. Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## Next bounded target

P4-S039 should stop trying to compile the actual coded P4-S011 win into an ordinary raw martingale: that would contradict the settled \(X\in CR\).

Instead attack the missing **same-source one-hole** question directly. Starting from the c.e.-persistent sentinel process on \(H(X)\), determine whether a total raw-coordinate one-hole scan/stake process can reproduce enough of the correct-prediction gain on \(X\).

Begin with the exact finite linear algebra of one omitted raw coordinate in one three-bit recoding block and track how the resulting unresolved parity state can or cannot be transported across block boundaries.

A positive simulation for the actual source proves \(X\notin OH\) and removes this source as an OH non-invariance candidate. A negative simulation theorem is only an obstruction; it does not by itself prove \(X\in OH\).

Do not return to P4-S015–P4-S031 or to ambiguity mass.
