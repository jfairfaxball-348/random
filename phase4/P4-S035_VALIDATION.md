# P4-S035 validation

Date: 2026-10-06
Session: P4-S035
Incoming checkpoint: 9751ab899736c606f47f137f78823318c72aa6e6
Scope: delayed spoiled-stake normalization after the P4-S034 coded-hole obstruction
Status: **VALIDATED**

## Repository and scope checks

- Live main matched 9751ab899736c606f47f137f78823318c72aa6e6 immediately before the first P4-S035 write.
- That hash is the P4-S034 synchronization tip, with message “P4-S034 synchronize START_HERE.md”.
- Repository search returned no P4-S035 record before the first write, so the session identifier was unique.
- P4-S001 through P4-S034 were read at the pinned P4-S034 checkpoint.
- The selected CAND-01 authority in phase2/candidates.json was read.
- phase4/P4_RESEARCH_PIVOT_AFTER_S031.md and P4-S032/P4-S033/P4-S034 were read.
- All validated mathematics through P4-S034 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence was not reopened.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. Raw determination and the pre-pivot guard

For a parity q, the first raw event completing its support has one fresh raw coordinate p. Before reading p, the parity is an affine/sign copy of p with orientation computable from the already queried support bits.

A fair raw wager on p must therefore be chosen from the pre-pivot history. A stake which is only computable after p is read cannot in general be moved back without a normalization factor. This validates the stronger “pre-pivot forecastability” hypothesis and rejects the weaker inclusive “at determination time” reading.

### 2. Separating schedule for the displayed matrix

For
\[
S_0=\{0,2\},\qquad S_1=\{0,1\},\qquad S_2=\{0,1,2\},
\]
the schedules

- first row 0: query 2,0;
- first row 1: query 1,0;
- first row 2: query 0,2,1

make at most one still-unrequested row newly determined at each raw query.

If row 0 or row 1 is first, one raw coordinate remains and the next live row determines at most the one remaining future row. If row 2 is first, row 0 is completed at the second raw query and row 1 only at the third, together with the current row 2.

Thus spoiled coordinates have distinct determination pivots under this evaluator.

### 3. Early-decision martingale transfer

At a spoiled determination event,
\[
Z_q=\varepsilon X_p
\]
with \(\varepsilon\) known pre-pivot. If the eventual fractional stake s is also known pre-pivot, the raw fractional stake \(s\varepsilon\) has multiplier
\[
1+sZ_q,
\]
exactly the virtual spoiled multiplier.

Because spoiled determination pivots are distinct, the raw martingale can multiply all spoiled factors exactly. On the target, P4-S008 makes the virtual scan exhaustive because H(x) is computably random and d succeeds, so no target spoiled factor is an extra wager on an ultimately omitted coordinate.

P4-S034 already proves the live product bounded and the spoiled product unbounded. Hence a determination-predictable destructive witness would give a computable martingale succeeding on an effective raw permutation, contradiction.

### 4. Synchronous late-choice premium

If the spoiled stake has branch values \(s_+,s_-\) after the determining pivot and \(Z_q=\theta X_p\), then the two desired factors are
\[
g(+)=1+\theta s_+,\qquad g(-)=1-\theta s_-.
\]
Their fair price is
\[
c=(g(+)+g(-))/2.
\]
When the target factor is positive, c is positive. Dividing by c gives a nonnegative mean-one two-child factor and therefore a legal raw martingale step.

Thus the exact residual for same-pivot late choice is the product of the c factors. The early-decision case has \(s_+=s_-\), hence c=1.

### 5. Closed-packet theorem

Fix a packet containing at most M blocks of an invertible n-bit recoding, \(n\ge2\). A packet-closed scan makes at most Mn virtual queries before leaving the packet.

For each complete virtual packet assignment, finite simulation computes d's exit capital. By finite optional stopping / repeated martingale averaging, the mean of this exit capital over the uniform virtual packet equals d's entry capital.

The repeated invertible block map is a bijection of finite packet assignments, so the same mean identity holds after pullback to raw packet assignments.

Finite Doob conditional expectations therefore produce an exact computable nonnegative raw martingale segment which begins with d's entry capital and ends with its exit capital.

Every packet contains at least two virtual coordinates. Since a one-hole scan omits at most one virtual coordinate globally, it must enter every packet. Querying the whole raw packet on entry therefore yields an exhaustive adaptive raw permutation.

Within one packet d's capital can grow by at most \(2^{Mn}\) relative to entry, because there are at most Mn nonnegative martingale bets and each multiplicative factor is at most 2. Hence unbounded d-capital forces unbounded packet-boundary capital, which the raw Doob martingale reproduces.

The theorem is therefore exact.

### 6. Infinite bounded-delay chain is one-hole

On the designated chain, block b has pending \(u_2^{(b)}\). The scan reads \(u_0^{(b+1)},u_1^{(b+1)}\), then either:

- trigger: consumes \(u_2^{(b)}\) and carries \(u_2^{(b+1)}\) as the next pending coordinate; or
- no trigger: omits \(u_2^{(b)}\) permanently and switches to an exhaustive fixed tail.

Thus every nontrigger transcript omits exactly one coordinate and the all-trigger transcript omits none. The scan is total, computable and one-hole.

After \(u_0^{(b)}\) and \(u_1^{(b)}\) are both produced, their support union is all three raw coordinates of block b. Therefore \(u_2^{(b)}\) is raw-determined independently of the raw support order. Any stake dependence on \(u_1^{(b+1)}\) is genuinely later and cross-block.

Any finite closed packet containing block b must include block b+1 to decide the pending stake, then block b+2 to close the pending stake created there, and so on. Hence no finite packet closes the all-trigger dependency ray.

This validates Theorem 10 as a compiler obstruction.

### 7. Separation guard

The chain architecture does not supply a computably random source in OH, nor a martingale known to succeed on its recoded image. It therefore cannot be used to claim OH non-invariance or \(R_2\subsetneq OH\).

The retained inclusions remain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains unchanged.

## Validation disposition

**PASS.**

P4-S035 establishes a real delayed-stake normalization theorem, a stronger finite-packet theorem, and a precise infinite cross-block temporal obstruction. It does not decide \(R_2=OH\).
