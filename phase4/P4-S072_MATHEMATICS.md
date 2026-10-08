# P4-S072 — effective settlement of genuinely late spoiled shear wagers

Date: 2026-10-08
Incoming exact live remote main: \`3a588efd41939b1f2c193fd877bbdbab61e38bf0\`
Scope: Phase 4 Mathematics ONLY; selected CAND-01; computably supported XOR shears
Disposition: **VALIDATED CONDITIONAL ONLINE FAIR-SETTLEMENT / PENDING-INVENTORY THEOREM AND EARLY-FORECAST OBSTRUCTION; NO UNRESTRICTED PRESERVATION OR SEPARATION**

## 0. Authority, frozen mathematics and scope

The live remote main was independently queried and matched the requested SHA and its S071 commit parent. The tree contains P4-S001–S071 mathematics and no P4-S072 file. The P3-S007 CAND-01 selection, P3-S008 Gate-3 PASS, both Phase-4 pivots, P4-S001–S071 mathematics (emphasizing S008/S011/S012/S027/S032–S044/S052–S057/S065–S071), S071 validation/close and current authority were inspected. S034–S036's forecast/packet work is expressly NOT replaced by what follows.

Keep
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Keep the original computably random \(Y\), unchanged self-avoiding globally use-clipped wtt autoreduction \(M\), exact repeated three-bit homeomorphism \(H\), and \(X=H^{-1}(Y)\), with \(X\in CR\) and \(H(X)=Y\notin OH\). \(X\in OH\), preservation by \(H\), \(R_2=OH\), \(R_2=OH^{iso}\), \(OH^{iso}=OH\) and unrestricted homeomorphism invariance remain unresolved.

As in S070–S071 take any decidable block set \(E\), especially all blocks or alternating blocks, and the involutive shear \(S_E(a,b,c)=(a,b\oplus c,c)\) on selected blocks. Write its virtual coordinates \(u=a,v=b\oplus c,w=c\). Let \(T\) be an arbitrary TOTAL computable no-repeat virtual global one-hole scan, \(d\) a nonnegative rational computable virtual-output martingale normalized to one, and \(P=P_{E,T}\) the S071 raw evaluator: v first reads fresh c as a REAL raw filler, then fresh b for v; a later w request is silently supplied from c. This P is everywhere-total, globally one-hole, no-repeat and fair on **all** raw transcripts. The present work changes its betting rules, not its raw scan.

## 1. Online fair settlement certificates

Call a selected-block virtual w request *spoiled* when an earlier v request has already forced raw c to be read. A *prospective claim* is identified by its selected block after (or as) its raw c filler is entered and before its eventual virtual w request; a block has at most one such claim.

A **total computable online fair-settlement registrar** \(\mathcal C\) for \(P,T,d\) acts BEFORE each next real raw query \(p\), using only the finite raw transcript and the fully simulated virtual transcript so far. It may mark that query as the single *credit pivot* for one not-yet-credited prospective claim \(j\), and output rational child multipliers \(g_j(0),g_j(1)\) satisfying
\[
g_j(0),g_j(1)>0,\qquad g_j(0)+g_j(1)=2.
\tag{1}
\]
Otherwise it outputs no claim, and the multipliers are \(1,1\). A block receives at most one credit and a pivot credits at most one block; no zero-time/silent step is a credit pivot. The certificate can be attached to its original raw c filler (the early-forecast case), or to a LATER FRESH raw coordinate which fixes the delayed stake (the genuinely late-information case). A registrar is an effective algorithm on every finite raw transcript, **not** an oracle for the eventual stake.

For a raw source \(x\) on which the certificate is *faithful*, every nontrivial spoiled w-factor of \(d\) is credited at a real raw pivot no later than that virtual w request. If \(r_j\) is the pivot's actual outcome, the recorded factor
\[
g_j=g_j(r_j)>0
\]
equals the signed-fractional virtual martingale multiplier \(1+s(\tau_j)(2c_j-1)\) WHEN w is eventually requested. Every spoiled w without a credit has factor exactly \(1\). Every credited claim which has already had its w requested is thus settled, and every other credited claim remains pending. Faithfulness is a semantic hypothesis along \(x\), or may be required of every source; the compiler never assumes it can *decide* whether a future w will appear, and an omitted w simply leaves its credit pending.

Define, after the first \(m\) virtual requests have been fully processed, the finite set \(\mathcal O_m(x)\) of credited-but-not-yet-requested w claims and its strictly positive **inventory factor**
\[
A_m(x)=\prod_{j\in\mathcal O_m(x)}g_j.
\tag{2}
\]
This rational is effectively obtainable from the finite raw history, including claims awaiting a w that may never be queried. Empty product is 1. No effective upper bound on the future number or lifetime of pending claims is assumed.

## 2. The exact online fair-settlement theorem

**Theorem 1 (two-account same-source extraction).** Uniformly from decidable E, total T, rational d and a total computable registrar \(\mathcal C\) obeying the purely syntactic conditions (1), there are two total computable nonnegative rational martingales \(L,F\), and their average \(h=(L+F)/2\), on outputs of the SAME globally legal raw one-hole scan P, all normalized to one.

For every faithful source \(x\), at every completed virtual stage \(m\), with \(n(m)\) actual raw queries emitted by P, the following **exact identity** holds:
\[
\boxed{L_{n(m)}(x)\,F_{n(m)}(x)=d_m(T(S_E(x)))\,A_m(x).}
\tag{3}
\]
Consequently
\[
\boxed{h_{n(m)}(x)\geq \sqrt{d_m(T(S_E(x)))\,A_m(x)}.}
\tag{4}
\]
If \(\sup_m d_m A_m=\infty\), then the computable h succeeds on P(x). In particular, if \(\inf_m A_m>0\) and d succeeds on the virtual scan, h succeeds on the raw scan.

**Proof.** The S071 live-copy martingale L stakes zero on actual c fillers and copies exactly each virtual wager completed on a fresh raw bit; on v=b xor c it swaps the two b children according to the already known c. At a silently processed spoiled w it does nothing. S071 establishes total fair rational computation at EVERY raw prefix and global scan legality. Thus L is exactly the product of all *live* virtual factors already executed.

The second account F bets only on the registrar's designated real credit pivots: if the next raw bit p is marked with rational factors g_j(0),g_j(1), its capital children receive those multipliers. Their average is one by (1). At every other real query F holds. The registrar is total and sees no pivot outcome before choosing g_j, so F is a total computable rational nonnegative martingale on EVERY raw transcript. Its value after n(m) raw queries is exactly the product of all credits placed so far. On a faithful source, those credits partition into the already settled spoiled factors of d and the pending factors in (2); all uncredited spoiled factors are one. Multiplying by L gives (3), including a zero virtual-capital path (a zero live factor makes both sides zero; all credited factors are strictly positive). There is no need to multiply L and F to obtain a martingale: their product need not be a martingale when they wager on the same raw bit. Instead the AVERAGE h is a martingale, and AM–GM yields (4). All capital accounting is on genuine raw output stages; silent virtual w requests never masquerade as fresh raw queries. QED.

**Corollary 2 (bounded-inventory supported-shear preservation).** If \(z\in OH\), every faithful registrar must obey
\[
\sup_m d_m(T(S_E(z)))\,A_m(z)<\infty.
\tag{5}
\]
In particular, a virtual d with unbounded capital cannot be faithful to a registrar whose pending inventory satisfies \(\inf_m A_m(z)>0\). A checkable sufficient inventory criterion is: for some fixed computable rational \(0<\rho<1\), every credited multiplier lies in \([1-\rho,1+\rho]\), and at most K credited claims are pending at any time on the target. Then \(A_m\ge (1-\rho)^K\). More generally, a bound \(\sum_{j\in\mathcal O_m}[-\log g_j]_+\le C\) uniformly in m gives \(A_m\ge e^{-C}\), with no upper bound on the number of pending claims.

**Corollary 3 (sharpened necessary obstruction relative to a faithful registrar).** If \(z\in OH\) and d succeeds on \(T(S_E(z))\), then for every faithful strictly-positive fair-settlement registrar,
\[
\inf_m A_m(z)=0,\qquad
\log d_m\le C_z-\log A_m \quad(d_m>0)
\tag{6}
\]
for some finite \(C_z\). More precisely the small-inventory-product conclusion holds along a subsequence on which d is unbounded. This is IN ADDITION to the unconditional S071 necessity \(\sum_{\rm spoiled}|s|=\infty\). Without a faithful registrar, (6) is not asserted.

**Proof.** Since P is a legal global one-hole scan, \(h(P(z)\upharpoonright n)\) is bounded by some K on z in OH. From (4), \(d_m A_m\le K^2\); take \(C_z=2\log(\max(1,K))\). An unbounded d forces A_m arbitrarily close to zero along its capital peaks. The two stated inventory bounds are elementary product estimates. QED.

These are a genuine same-source TOTAL scan/martingale and a new *online pending-claim obstruction* special to the supported shear; they extend S035 pre-determination-pivot forecastability by allowing the credit pivot to be a LATER fresh coordinate. They do NOT assert that arbitrary T,d possess a registrar or a lower inventory bound; S035–S037 closed-packet and backward-price results stay authoritative.

## 3. Explicit genuinely late cross-block model: all and alternating shears

Partition the blocks into adjacent pairs \((2k,2k+1)\), and for each pair let T query virtual coordinates in the deterministic order
\[
v_{2k},\ u_{2k+1},\ w_{2k},\ u_{2k},\ v_{2k+1},\ w_{2k+1}.
\tag{7}
\]
Repeat forever. This is an everywhere-total computable **exhaustive** virtual scan, hence globally one-hole (indeed an effective permutation). It is valid for E=all blocks and E=even blocks (alternating support).

Let d place fractional stake \(q(2u_{2k+1}-1)\), with rational \(q=1/2\), on \(w_{2k}=c_{2k}\), and zero stake on every other virtual request. This is a globally total fair nonnegative rational output martingale: the deciding u has already been queried, and virtual w is fresh. When v_{2k} is requested, P REALLY reads raw c_{2k} before raw b_{2k}; at this stage u_{2k+1} is not yet known, and the w stake is NOT computable from this raw pre-c history.

At the later fresh raw pivot \(a_{2k+1}=u_{2k+1}\), c_{2k} is already known. Credit the old spoiled w claim on that pivot by
\[
g_{2k}(r)=1+q(2c_{2k}-1)(2r-1),\qquad r\in\{0,1\}.
\tag{8}
\]
The two rational factors are 1/2 and 3/2, with average exactly 1; on reading r=u_{2k+1}, (8) equals d's eventual spoiled-w factor. At most one credited factor is outstanding: w_{2k} is requested immediately after u_{2k+1}. If E=all, the later w_{2k+1} request can be spoiled by v_{2k+1}, but its d stake is zero; it needs no credit. Every other d stake is zero. Thus L=1, \(A_m\ge1/2\), and \(h_{n(m)}\ge\sqrt{d_m/2}\) on every source.

This is a concrete infinite family of GENUINELY late choices across blocks, normalized on the SAME raw one-hole observer, not a closed virtual packet that assumes oracle access to future stakes. It is NOT a counterexample: its virtual d need not and cannot win on an OH source under this normalization. The finite parity/fair-price audit over all 64 assignments of each two-block raw packet, for E=all and E=alternating, checked 128 cases without discrepancy; the proof is the identity (8), not that finite enumeration.

A simpler synchronous illustration uses T's v_j then w_j and stake \(q(2v_j-1)\) on w_j: after raw c_j, the F-account credits on fresh b_j with multiplier \(1+q(2b_j-1)\). Here the future stake also cannot be read before raw c_j, yet it can be fairly settled at b_j.

## 4. Structural impossibility of unrestricted early exact forecasting

**Proposition 4 (no universal pre-c exact stake forecaster).** For the T,d of (7), no procedure which has only the finite raw history BEFORE the raw c_{2k} filler can output the actual future fractional stake on w_{2k}, correctly on every continuation. In fact, two continuations identical through that history can assign opposite values to the subsequently queried u_{2k+1}, forcing stakes \(+q\) and \(-q\).

**Proof.** At the pre-c filler event the deterministic virtual transcript has not queried u_{2k+1}, nor has raw P read a_{2k+1}. Hold fixed the current raw finite history and choose two extensions differing only at this fresh a_{2k+1}. Their future virtual u values differ, so their future w stakes have opposite signs. One fixed rational forecast cannot equal both. The conclusion persists for all-block and alternating support. QED.

This disproves the NATURAL universal exact-preforecast method at the initial c pivot, NOT the possibility of later fair settlement: (8) succeeds using the later h pivot. It does not show that any source belongs to OH, and it does not revive a divergence-only Case-C negative certificate. In the general S039–S044 Case C, a partial sibling computation's failure to halt has no computable finite negative witness. A merely *eventually computed* or *retrospectively observed* stake does not supply a total registrar or its fair two-child price. Nor can one promise a uniformly positive pending inventory without a separate proof: infinitely many prepaid factors below one can multiply toward zero.

## 5. Exact limits and next global question

The present theorem adds **conditionally effective late-information settlement** and the open-inventory deficit (6) to the unconditional S071 cumulative spoiled exposure law. It neither proves that unrestricted infinite supported shears preserve OH nor exhibits a z in OH with S_E(z) outside OH. It does not decide H-preservation, classify committed X, or resolve \(R_2=OH\), \(R_2=OH^{iso}\) or general homeomorphism invariance. No inference is made from failed extraction to OH membership or from high-degree/measure-typical sources to actual X. S057–S069 controllers, hazards and finite closure-multiplicity tasks were NOT resumed.

P4-S073 (if no blocker): seek a computably priced *multi-claim* settlement theory beyond one-credit-per-fresh-pivot, with an effective bound on aggregate pending downside, or prove an explicit globally legal counter-architecture in which every natural total fair-settlement registrar has unbounded negative open-inventory pressure. Start with the simple (7) chain extended to overlapping shared decision pivots; distinguish failure of a proposed registrar from actual nonpreservation. Retain exactly the same-source, all-branch fair one-hole rules and the S071 B_m law; R_2=OH^iso stays separate.

PA-0001 **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claims. Owner/external blocker: NONE.
