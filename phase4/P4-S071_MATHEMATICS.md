# P4-S071 — supported-shear same-source scan extraction and spoiled-stake exposure

Date: 2026-10-08
Incoming exact live remote main: 303cbb1ce2d4fc202462901bc0071bcbf7cc8b7a
Scope: Phase 4 Mathematics ONLY; CAND-01; global supported two-coordinate XOR shear
Disposition: **VALIDATED GLOBAL QUANTITATIVE SAME-SOURCE EXTRACTION AND NECESSARY SPOILED-STAKE EXPOSURE; UNRESTRICTED SHEAR PRESERVATION AND SEPARATION NOT DECIDED**

## 0. Authority, uniqueness and frozen results

Immediately before the investigation the LIVE remote main equalled the exact requested post-S070 SHA. Its recursive tree contained complete P4-S001–S070 mathematics/validation/close records, the two Phase-4 pivots, and NO P4-S071 record. The selected P3-S007 CAND-01, P3-S008 Gate-3 PASS, both pivots, P4-S001–S070 mathematics, and S070 validation/close were inspected, emphasizing S008, S011, S012, S027, S032–S044, S052–S057 and S065–S070. P4-S034–S036's spoiled-stage support evaluator and effective packet criteria were also used as controlling earlier mathematics.

Retain exactly
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Keep the original computably random Y, syntactically self-avoiding globally use-clipped wtt autoreduction M, committed three-bit homeomorphism H with matrix A=[101;110;111], and X=H^{-1}(Y) in CR with H(X)=Y notin OH. X in OH, H-pres, R_2=OH, R_2=OH^{iso}, OH^{iso}=OH and general homeomorphism invariance are all UNRESOLVED. The S070 equivalence between H-preservation, ALL supported-shear preservation and ALL computable blockwise GL(3,2)-recoding preservation is frozen. No claim that this equivalence itself proves preservation.

A total computable adaptive no-repeat *one-hole* scan must omit at most one raw coordinate on EVERY infinite transcript, not only on the target. A rational computable nonnegative output martingale suffices to witness non-computable randomness.

## 1. Explicit supported shear, including the alternating-block test

Fix ANY decidable set E of three-bit block indices, independently of source oracle values. Let
\[
S_E(x)_{3j}=x_{3j},\quad
S_E(x)_{3j+1}=x_{3j+1}\oplus x_{3j+2},\quad
S_E(x)_{3j+2}=x_{3j+2}
\]
for j in E; on j outside E let S_E be the identity. It is an involutive computable fair-coin-preserving homeomorphism. The concrete initial test E=2N (alternating blocks) and the all-blocks E=N case are both included below; the proof actually works uniformly for all computable E.

Write, within a selected block, raw (a,b,c) and virtual (u,v,w)=(a,b xor c,c). Let T be ANY total computable adaptive no-repeat global one-hole scan of the *virtual* coordinates, and d ANY nonnegative computable rational martingale on its infinite virtual output, normalized so d(empty)=1.

A *spoiled w-request* is exactly a later T-request of virtual w=3j+2 after T previously requested v=3j+1 on some selected j in E. The raw value c needed for the earlier parity v was already read, so that later w is already known. No other virtual query is spoiled by the evaluator below. A block contributes at most one spoiled request. The event and its occurrence are recognizable effectively from the finite virtual/raw transcript; recognizing eventual omission or an unbounded future wager is NOT required.

## 2. Global raw one-hole evaluator — an unconditional map construction

**Lemma 1 (same-source raw evaluator).** Uniformly from E and T there exists an everywhere-total computable adaptive no-repeat raw scan P_E,T such that:

1. In a selected block, on T's request for u, query fresh raw a. On T's request for v, first query raw c as a zero-stake filler if not already read, then query fresh raw b, and reconstruct v=b xor c. On T's request for w, query raw c if still fresh; otherwise reconstruct w from the pre-read c without emitting a raw query. In unselected blocks, query the corresponding fresh raw bit.
2. The simulated virtual transcript is exactly T(S_E(x)), on EVERY raw source x.
3. P_E,T emits infinitely many REAL raw output bits, never repeats a coordinate, and omits at most one raw coordinate on EVERY infinite raw transcript. Consequently it is a legal global one-hole scan; its output is fair-coin distributed.

**Proof.** All requested operations and the finite scan state are computable. A requested u reads a. The only requested v reads fresh b and possibly a preceding fresh c. A requested w either reads fresh c or is silently reconstructed. No raw query is repeated. The virtual scan sees precisely the parity/coordinate value requested, so its adaptive state is simulated exactly.

A silent step can occur only for a w already pre-read at some earlier v in a selected block. At any finite raw prefix, only finitely many raw c's have been read, so only finitely many distinct such silent w-steps can occur before another fresh raw request. An infinite silent run is impossible: it would request infinitely many distinct virtual coordinates from a finite set of already determined w's. Since T requests infinitely many distinct virtual positions, P emits infinitely many raw queries. Thus the next raw coordinate is found in finite computable time at every finite raw transcript, including off-target transcripts.

For any infinite virtual transcript let O be the set of omitted virtual indices, with |O|<=1 by T's GLOBAL hypothesis. Outside E, a missing raw bit corresponds exactly to the same missing virtual coordinate. Inside E, a can be missing only if u is omitted; b only if v is omitted; and c can be missing only if BOTH v and w are omitted. The last alternative is impossible when |O|<=1. Hence at most one raw coordinate is missing, on every transcript. Every raw transcript determines an infinite simulated virtual transcript by the preceding progress argument, so the fibre bound is global. Finally each REAL query reads a fresh fair bit selected from the prior raw transcript; therefore every length-n output cylinder has measure 2^{-n}. QED.

The pre-read c filler is an ACTUAL zero-stake query; no virtual step is falsely counted as a raw query. This does not reserve two raw sentinels, retrospectively set a deadline, or use c.e. negative information.

## 3. Uniform computable martingale compiler with exact exposure discount

For virtual prefix tau with d(tau)>0 define its signed fractional stake
\[
s(\tau)=\frac{d(\tau1)-d(\tau0)}{2d(\tau)}\in[-1,1].
\]
The factor on next virtual outcome b in {0,1} is
\[
m(\tau,b)=1+s(\tau)(2b-1)\in[0,2].
\]
At nodes with zero d-capital use zero stake; such a node cannot lie on a virtual d-success path.

**Theorem 2 (uniform same-source quantitative extraction).** Uniformly in E,T,d one can construct a nonnegative rational computable martingale e on the output of the GLOBAL one-hole raw scan P_E,T. For every raw x, after the first m virtual requests have been processed, let n(m) be the number of actual raw queries emitted, and let J_m be the set of spoiled w-requests among those m virtual requests. Define the computably accumulated nonnegative *exposure*
\[
B_m(x)=\sum_{t\in J_m}|s(\tau_t)|,
\]
where tau_t is the virtual output prefix immediately before request t. Then for EVERY x and m,
\[
\boxed{e(P_{E,T}(x)\upharpoonright n(m))
\ \ge\ d(T(S_E(x))\upharpoonright m)\,\exp(-B_m(x)).}
\tag{1}
\]
In particular, if the virtual d has unbounded capital and
\[
\sup_m d(T(S_E(x))\upharpoonright m)\exp(-B_m(x))=\infty,
\tag{2}
\]
the raw e succeeds on P_E,T(x). A fortiori (2) holds when d succeeds and B_m is bounded, for example when only finitely many nonzero spoiled wagers occur along x or the total spoiled absolute fractional stake is summable.

**Proof.** At every raw c filler before a parity v, stake zero. At a fresh raw bit implementing a virtual request, use the virtual fractional stake s(tau), swapping its two children if the requested virtual parity is the complement of the fresh raw bit conditional on previously queried c. This is a legal fair rational stake: the two child multipliers add to two, and the pre-query information (including c) is known. At a spoiled virtual w request, update the simulated T,d state using the ALREADY KNOWN c but make NO raw query and NO raw wager. Every next raw query and its stake is computable from the finite raw transcript: the preceding proof bounds silent processing by finitely many already determined w's. On nodes where virtual d is zero, use zero future stakes. These instructions define e as a globally total computable rational nonnegative martingale on every finite raw output transcript.

At a live virtual request, e and d receive exactly the same multiplicative capital factor; at a spoiled request e holds while d receives a factor m_t in [0,2]. Along a virtual d-success path all these factors are positive and
\[
d_m=e_{n(m)}\prod_{t\in J_m}m_t
\le e_{n(m)}\prod_{t\in J_m}(1+|s(\tau_t)|)
\le e_{n(m)}\exp(B_m).
\]
When virtual d has hit zero the desired inequality is trivial. This proves (1) for every x. Condition (2) makes e unbounded at raw stages n(m), which are unbounded by the total-progress part of Lemma 1. QED.

No probabilistic source-specific transfer and no conditional expectation over a noncomputable future are hidden here: all fresh wagers are implemented on genuine fresh bits, all spoiled wagers are knowingly forfeited, and the entire loss is charged in (1).

## 4. Global preservation criterion and necessary obstruction

**Corollary 3 (positive restricted shear preservation).** Let z belong to OH, E be computable, and y=S_E(z). For EVERY virtual one-hole T and rational computable d as above,
\[
\sup_m d(T(y)\upharpoonright m)e^{-B_m(z)}<\infty.
\tag{3}
\]
Therefore no such d can succeed on T(y) if its spoiled exposure is bounded on z. In particular, for every E (including E=2N and E=N), the entire class of virtual T,d witnesses with finitely many nonzero spoiled wagers, or absolutely summable spoiled fractions on z, is harmless on ALL z in OH.

**Proof.** P_E,T is a legal GLOBAL one-hole scan, so P_E,T(z) belongs to CR by z in OH. Hence its computable martingale e has bounded capital on that transcript. Inequality (1) proves (3). QED.

**Corollary 4 (quantitative necessary condition for a separation).** Suppose a computably random z in OH satisfies S_E(z) notin OH, witnessed by a one-hole T and a normalized rational computable martingale d succeeding on T(S_E(z)). Then along that exact source
\[
\sum_{\substack{\text{spoiled w requests}\\\text{on selected blocks}}}|s(\tau_t)|=\infty.
\tag{4}
\]
More precisely, there is a finite source-and-observer-dependent C such that for every m with positive d-capital,
\[
\log d(T(S_E(z))\upharpoonright m)\le C+B_m(z).
\tag{5}
\]
Thus a supported-shear counterexample MUST have infinitely many nonzero spoiled w-wagers with unbounded cumulative absolute stake; the spoiling events arise from virtual v-before-w inversions on selected blocks, not from arbitrary raw-coordinate pre-revelations.

**Proof.** Let K bound e along the raw scan of z. Equation (1) yields d_m<=K exp(B_m). Set C=log(max(1,K)). A successful d is unbounded, so B_m cannot remain bounded; a bounded sum (or finitely many positive terms) would contradict success. QED.

These are genuine global quantified statements about an arbitrary computable E and arbitrary virtual T,d, not only about a particular local tableau. They specialize P4-S034's general live/spoiled evaluator to a *single explicit* two-coordinate site and quantify the possible lost capital by computable fractional stakes. They do NOT imply that B_m is bounded, nor that a d with unbounded exposure can be normalized by another raw scan.

## 5. Why the gap is real

A virtual scan can query v before w in infinitely many selected blocks and later bet with fixed nonzero fraction on each w. For example a computable deterministic virtual order v,w,u block by block, with a rational martingale betting fraction 1/2 on every w, has B_m tending to infinity on all sources when E is infinite, even though that martingale does NOT succeed on a computably random virtual sequence by itself. Thus computable randomness alone does not bound this exposure and there is no claim that this toy is a CR-in-OH separator.

The real risk is a LATE stake whose magnitude/sign is chosen after c has been used for the earlier parity v. Betting on the now-known c is no longer a fresh fair wager. Trying to bet on c at its initial filler step would require predicting a later virtual stake which may depend on subsequent cross-block data and on partial computations. P4-S035–S036 already demonstrate why mere determination or finite local delay is not a generally available online price. Divergence-only S039–S044 Case C supplies no finite negative certificate permitting safe abandonment or foreknowledge. The present compiler deliberately does NOT pretend otherwise.

The opposite tempting inference also fails: the literal map-level virtual w-hole has raw Hamming cost two, but Lemma 1 gives a legitimate raw ONE-hole observer for the SAME SOURCE by selectively making genuine zero-stake reads and forfeiting later w wagers. Thus failure of exact factorization is not impossibility of a same-source extraction. The remaining problem is exactly whether the potential *unbounded* discounted capital can be recovered with a different legal total fair no-repeat one-hole observer, or whether a genuine z in OH can realize it.

This does not use P4-S057–S069 clock, gate, finite closure or renewal machinery. If reactivated later the unchanged exact P4-S057 controller has four paired globally use-clipped M traces, prospective deadlines, real filler steps, mandatory zero-stake t/u timeout release and non-s sweep WITHOUT resetting the old sentinel, global fair no-repeat one-hole fibres, and seven 8/7 plus one ZERO terminal outcomes.

## 6. Validation, nonresults and P4-S072 selection

Proof checks: total next-query computation on EVERY raw transcript; no raw repeats; one-hole bound on EVERY infinite branch; actual zero-stake c fillers; parity betting on fresh b after c; silent virtual w steps terminate; rational fair martingale at EVERY raw node; exact loss inequality and finite/summable-exposure corollaries. Finite adversarial audit of six virtual coordinates (two blocks), all one-hole omissions, all virtual query orders, all 64 raw assignments and E=empty/even/all found 0 violations across 276,480 enumerated cases. Finite enumeration is a sanity check, not the proof of the infinite case.

There is NO proof that ANY nontrivial infinite E universally preserves OH, NO z in OH with S_E(z) notin OH, NO classification of committed X, NO R_2=OH or R_2=OH^{iso} result. The assumption z in OH in Corollaries 3–4 is essential; failure of an extraction algorithm never proves OH membership. Universal finite exposure is not derived from Case C, sibling certificates or measure-typical CR sources.

Next bounded global target P4-S072 (no owner/external blocker): analyze whether a late spoiled w-wager can be *pre-priced at the initial raw c query* under a genuinely computable effective late-stake measurability/forecast condition, or prove a sharper obstruction to such pre-pricing, strictly for supported shears. Preserve the all-transcript one-hole rule and the quantitative B_m necessity. Do not return automatically to the finite controller and do not infer X membership. R_2=OH^{iso} stays a separate secondary problem.

PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claims.
