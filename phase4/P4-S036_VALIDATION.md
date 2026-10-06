# P4-S036 validation

Date: 2026-10-06
Session: P4-S036
Incoming checkpoint: de5905a3b32cb091f2d5ff906606dff891e0632b
Scope: finite dependency closure, packet savings normalization and infinite-component obstruction
Status: **VALIDATED**

## Repository and scope checks

- Immediately before the first P4-S036 write, live main was exactly de5905a3b32cb091f2d5ff906606dff891e0632b, the P4-S035 outgoing checkpoint with message “P4-S035 set P4-S036 dependency-closure prompt”.
- Direct lookup of phase4/P4-S036_MATHEMATICS.md returned no file before the first write, so P4-S036 was unique.
- P4-S001 through P4-S035 were read as committed mathematical authority.
- The selected CAND-01 record in phase2/candidates.json, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032/P4-S033/P4-S034/P4-S035 were read.
- All validated mathematics through P4-S035 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence was not reopened.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. Dependency relations are finitely witnessed

The essential stake edge \(B\to_d C\) is defined by two finite branch simulations from a common spoiled-claim state, both reaching the same pending wager, with the first differing information exposed in \(C\) and with different rational stakes at the wager.

All conditions in a proposed witness are decidable from finite simulation. Hence existing essential edges are uniformly c.e.; nonedges need not be decidable.

The conservative exposure edge \(B\leadsto C\) and block-return interaction are likewise finitely witnessed. The mathematics correctly separates the exact stake graph from the larger operational closure graph needed by packet compression.

### 2. The persistent-savings transform is exact and computable

Let \(d(\varnothing)=1\), let \(d^{[k]}\) stop \(d\) on first reaching \(2^k\), and put
\[
\widehat d=\sum_{k\ge1}2^{-k}d^{[k]}.
\]

At a finite string \(\sigma\), the maximum value of \(d\) on prefixes of \(\sigma\) is a computable rational. Once \(2^K\) exceeds this maximum, no threshold \(2^k\), \(k>K\), has yet been hit, so every corresponding stopped martingale still equals \(d(\sigma)\). The infinite tail is therefore one exact geometric rational tail. This makes \(\widehat d(\sigma)\) exactly computable, not merely lower semicomputable.

Each stopped component satisfies the martingale equality, and the same finite-plus-geometric representation verifies the equality for their weighted sum.

A nonnegative binary martingale can increase by at most factor \(2\) at one step. Therefore at first hitting \(2^k\), the stopped value lies in \([2^k,2^{k+1})\), so the weighted \(k\)-th component contributes at least \(1\) permanently. If \(d\) is unbounded, arbitrarily many thresholds are hit and \(\widehat d\to\infty\).

This validates Lemma 4.

### 3. Arbitrary computably finite closed packets normalize

For one finite packet \(P\), packet closure ensures that after entry the virtual scan completes its entire \(P\)-episode before leaving and never returns. Since \(P\) contains finitely many virtual coordinates and the scan is no-repeat, every complete packet assignment yields a finite simulation to packet exit.

The exit capital of \(\widehat d\) is therefore a computable finite payoff table on virtual assignments to \(P\). Repeated martingale averaging gives mean equal to the entry capital.

The repeated invertible block recoding is a bijection on the finite packet assignment space. Pulling back the payoff table preserves its uniform mean. Finite raw Doob conditional expectations therefore give a computable nonnegative raw martingale segment with exact entry and exit capitals.

Every packet contains at least one block of size \(n\ge2\). A one-hole scan cannot fail to enter a packet, because that would omit at least two virtual coordinates. Hence every packet is eventually processed and the raw evaluator that queries the whole packet is exhaustive.

The persistent-savings transform tends to infinity, so its values at sufficiently late packet exits are unbounded. Thus no uniform packet-size estimate is needed. This validates Theorem 5 and Corollary 6.

### 4. The online packetizer generalization is sound

Under Definition 7, the exact finite packet is computable at entry before any raw bit of that packet is opened. The closure promise holds on every continuation represented by the finite payoff table, and successive packets are disjoint.

The same finite Doob construction therefore applies verbatim. Any unassigned block must eventually be entered by the virtual one-hole scan, since omitting a whole \(n\ge2\) block is impossible. Hence every raw block is eventually assigned and queried.

This validates Theorem 8. The positive resource is effective finite closure known at packet entry, not a uniform numerical size bound.

### 5. Finite closure plus rank does not effectivize completion

In Proposition 9 the only possible edge is
\[
b_e\to c_e
\]
and it is enumerated iff machine \(e\) halts.

Every graph in the family is well-founded and rank at most one; the distinguished forward closure is always finite. If a total computable procedure returned that complete closure, membership of \(c_e\) would decide whether machine \(e\) halts. Thus no such uniform closure-completion procedure exists.

This validates the claimed nonuniformity obstruction. It is a compiler obstruction only; no randomness failure is inferred from it.

### 6. Even computable finite forward closures need not form finite packets

For
\[
a_n\to c_n,\qquad a_n\to c_{n+1},
\]
every forward closure is computable and has at most three vertices. There is no directed path of length more than one, so the graph has computable rank one and no infinite directed forward ray.

After symmetrization, however, the dependency edges connect
\[
c_0-a_0-c_1-a_1-c_2-a_2-\cdots.
\]
Any partition which puts the endpoints of every dependency edge into the same packet therefore has one infinite packet.

This validates Proposition 11 and proves that well-foundedness, rank, and uniformly finite directed closure are not equivalent to finite packetizability.

### 7. The raw-pivot obstruction is order-independent

For the displayed recoding,
\[
S(u_0)=\{x_0,x_2\},\qquad S(u_1)=\{x_0,x_1\}.
\]
Their union is all three raw coordinates of the block.

An exact raw-coordinate evaluator cannot determine a parity before every raw coordinate in its support is known. Hence any evaluator which has already produced both \(u_0\) and \(u_1\) has necessarily queried all three raw coordinates. The third parity \(u_2\) is then determined.

Thus no reordering inside the block can leave a fresh raw pivot for \(u_2\). This validates Lemma 12.

### 8. Finite truncations are exactly compressible

At every finite ray cut chosen after the finitely many claims internal to the cut have resolved, the terminal virtual capital is a computable function of finitely many virtual block assignments.

The finite block recoding is bijective, so finite Doob conditional expectations give an exact raw martingale for that terminal payoff.

Hence failure of the infinite compiler is not a failure of finite conditional expectation. Lemma 13 is sound.

### 9. Classical convergence does not supply an effective terminal payoff

The Lemma 14 construction activates, for machine \(e\), one fair mean-zero wager of size \(2^{-e-3}\) at its reserved coordinate exactly if a finite simulation verifies that \(e\) halts for the first time at the corresponding stage.

At any finite source string only finitely many reserved coordinates have been encountered, so the martingale value is an exactly computable rational. The sum of all possible wager magnitudes is at most \(1/4\), keeping the martingale bounded and positive.

On the computable all-1 path the limit is
\[
1+\sum_{e\in K}2^{-e-3}.
\]
The halting set is infinite and co-infinite, so this is a non-dyadic real whose binary expansion computes \(K\); it is therefore noncomputable.

Thus a bounded computable martingale can have a noncomputable pointwise limit. Classical boundedness/uniform integrability alone cannot provide the computable terminal-value functional or effective convergence modulus required to pass from all finite closures to one raw compiler.

### 10. The recoded P4-S011 corollary is valid

Let \(D,Y,H,X\) be the settled P4-S033 setup:
\[
X=H^{-1}(Y)\in CR,\qquad D(H(X))=D(Y)\notin CR.
\]

If the virtual P4-S011 witness admitted a total computable finite closed packetizer relative to the displayed repeated recoding, Theorem 8 would imply that every computably random raw source, in particular \(X\), has computably random virtual scan output. This contradicts the settled destruction.

Therefore the recoded P4-S011 witness has no such packetizer.

Its wtt use bound only shows that every individual sentinel computation has finite dependence. It does not decide whether the global obstruction contains a directed infinite ray or is an infinite overlap component assembled from finite closures.

### 11. Separation guard

No proof that
\[
X\in OH
\]
is obtained. The established source fact remains only \(X\in CR\).

Therefore the session does not prove OH non-invariance and does not prove
\[
R_2\subsetneq OH.
\]

The retained inclusions remain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains unchanged.

## Validation disposition

**PASS.**

P4-S036 removes the uniform packet-size hypothesis, identifies total computable finite closed packetization as a stronger exact positive criterion, proves that rank/well-foundedness/finite forward closure do not by themselves supply it, and sharpens the infinite-component obstruction to effective stabilization of finite-horizon backward prices. The sustained equation \(R_2=OH\) remains unresolved.
