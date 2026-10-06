# P4-S036 close

Date: 2026-10-06
Session: P4-S036
Incoming checkpoint: de5905a3b32cb091f2d5ff906606dff891e0632b
Scope: sustained Phase-4 one-hole normalization programme; finite dependency closure versus infinite interaction components
Status: **COMPLETED**

## Result

P4-S036 materially strengthens P4-S035 without deciding \(R_2=OH\) and without proving OH non-invariance.

First, P4-S035's uniform packet-size hypothesis is unnecessary. Given any successful computable nonnegative rational virtual martingale \(d\), the threshold-stopping savings transform
\[
\widehat d=\sum_{k\ge1}2^{-k}d^{[k]}
\]
is itself an exactly computable rational martingale and tends to infinity whenever \(d\) is unbounded. Success therefore persists to arbitrarily late packet boundaries. The finite Doob-compression proof can then be run on packets of arbitrary computable finite size.

Consequently, for every repeated invertible finite binary block recoding of block size at least two, every one-hole witness closed with respect to a computable finite packet partition is harmless, with no uniform packet-cardinality bound. The same holds under the more general total computable **closed packetizer** hypothesis, where each exact finite packet is computed online at its entry state and is closed on every continuation.

Second, finite dependency closure and well-foundedness are weaker than effective packet closure. A rank-one halting-coded family has finite forward closures but no total computable procedure can know the complete closure. Even uniformly computable finite forward closures and computable rank one do not imply finite packetization: the computable graph
\[
a_n\to c_n,\qquad a_n\to c_{n+1}
\]
has no directed infinite ray and closures of size at most three, while its symmetrized interaction component is the infinite chain
\[
c_0-a_0-c_1-a_1-\cdots.
\]

Third, the P4-S035 ray cannot be repaired by reordering raw coordinates inside a block. Exact determination of both \(u_0^{(b)}\) and \(u_1^{(b)}\) consumes the union of their raw supports, which is all of \(B_b\), so \(u_2^{(b)}\) is already raw-determined.

Every finite ray truncation nevertheless has an exact finite conditional-expectation compiler. The surviving obstruction is effective passage to the infinite limit. Classical boundedness or uniform integrability is insufficient: bounded computable martingales can have noncomputable pointwise limits. The sharper object is therefore the finite-horizon backward fair-price vector of the open boundary claims and whether those prices stabilize effectively.

Finally, applying the new theorem to the recoded P4-S011 destroyer gives a concrete structural consequence: that witness cannot admit any total computable finite closed packetizer, or else its destruction of the computably random source would contradict the packetizer normalization theorem. This does not prove that its essential dependency graph has a directed infinite ray; overlapping finite wtt closures may already create the infinite interaction component.

No computably random \(X\in OH\) with \(H(X)\notin OH\) is proved. For the P4-S033 recoded P4-S011 source, only \(X\in CR\) is established; the missing source-side statement remains \(X\in OH\).

The retained comparison is
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains unchanged. The P4-S015–P4-S031 bankroll/ticket/frontier/recycling sequence remains frozen as the default route.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## Next bounded target

P4-S037 should attack **rolling finite-state normalization on an infinite interaction component**.

The primary object should be the finite-horizon backward fair-price vector carried by the open boundary state. Test the simple P4-S035 ray, the rank-one overlap architecture, and the actual recoded P4-S011 schedule. Determine whether bounded open-claim width, finite boundary-state dimension, telescoping, contraction of price ratios, or a computable Cauchy/projective modulus gives a single raw martingale compiler.

If normalization fails, isolate an exact computable architecture whose finite-horizon price vectors fail effective convergence or develop unbounded boundary distortion. For the recoded P4-S011 witness, decide whether its obstruction contains a genuine directed ray or consists only of overlapping finite wtt closures.

No source-side separation may be claimed without proving \(X\in OH\).
