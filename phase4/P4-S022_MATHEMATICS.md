# P4-S022 — anti-Zeno boundary isolation versus exact loss-level searchability

Date: 2026-10-06
Session: P4-S022
Incoming checkpoint: 2abc3b536272fd5c8f903d8087e0328212445d11
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **IN THE P4-S021 SCALE-TAIL SETTING, A LOCAL STRICT RESIDUAL-GAP CERTIFICATE AFTER COMPUTABLE EXHAUSTION OF EACH FIXED LOSS SCALE MAKES EXACT Reach(K,m) DECIDABLE. THE POSITIVE "MUST CROSS SOON" ARM IS NOT NEEDED: Reach ALREADY HAS C.E. FINITE WITNESSES, SO THE ONLY NEW EFFECTIVE CONTENT IS A SEARCHABLE CERTIFICATE THAT AN UNREACHABLE BOUNDARY IS STRICTLY SEPARATED FROM THE REMAINING SUBSCALE TAIL. HOWEVER ANY SUCH UNIFORM CERTIFICATE COMPILES BACK INTO A P4-S020 WITNESS MODULUS D(K,m), SO IT IS WEAKER ONLY AS PRIMITIVE LOCAL DATA, NOT IN FINAL COMPUTABILITY STRENGTH. P4-S021'S GEOMETRIC HALTING CONSTRUCTION IS SHARP: ON A NONHALTING BRANCH THE COMPUTABLE RESIDUAL TAIL EQUALS THE CURRENT GAP TO m AT EVERY SUFFICIENTLY FINE SCALE, WHILE HALTING REPLACES THAT TAIL BY A FINITE CORRECTION WHICH HITS m. THUS NONSTRICT BOUNDARY CONTROL DOES NOT DECIDE Reach. P4-S011 STILL FAILS BEFORE THIS BOUNDARY QUESTION, SINCE UNDER GLOBAL ADMISSIBILITY IT HAS UNBOUNDED SUBSCALE LOSS IN ONE BAD-CAPITAL TREE.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint `2abc3b536272fd5c8f903d8087e0328212445d11` exactly before substantive work. Repository commit search returned no P4-S022 session record; the only incoming P4-S022 hit was the P4-S021 forward-scheduling commit. Thus P4-S022 was unused.

P4-S001 through P4-S021 were read as mathematical authority. P4-S005 through P4-S021 are treated as settled. In particular P4-S011's exact global-k=2 destroyer, P4-S015's weighted theorem, P4-S016's envelope-free last-chance theorem, P4-S017's coercive self-financing theorem, P4-S018's effectivity-of-coercivity boundary, P4-S019's finite/noncomputable loss-properness boundary, P4-S020's searchable-loss-level theorem and P4-S021's scale-tail/boundary-attainment separation are preserved.

The required CAND-01 selection and Gate-3 authority was checked. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. This session stays strictly at k=2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained quantities

Use the settled canonical full-ticket account and the notation

[
E(v)=	ext{cumulative realized positive skipped gain},
qquad
W^*(v)=	ext{running maximum ticket capital},
]

[
B_K={v:W^*(v)<K},
qquad
operatorname{Reach}(K,m)iffexists vin B_K [E(v)ge m].
]

For (delta_n=2^{-n}), write (E_{ge n}) and (E_{<n}) for the parts of E contributed by ticket payouts at least (delta_n) and below (delta_n), respectively.

P4-S021 supplies two local data in the positive scale-tail setting:

1. a computable large-loss waiting modulus (R(K,n));
2. a computable subscale bound (T(K,n)) with (E_{<n}(v)le T(K,n)) for every (vin B_K).

Together with set-theoretic loss-properness, P4-S021 already computes a total bad-capital loss bound (U(K)). P4-S022 does not reopen that theorem. It asks only what further local information decides the exact integer predicate Reach.

## 2. Scale-tail data already give computable scale-exhaustion frontiers

The first useful observation is that the P4-S021 data can be compiled into a finite stage after which no payout at a fixed coarse scale remains possible anywhere in (B_K).

### Lemma 1 — computable exhaustion depth for one loss scale

Assume the P4-S021 hypotheses and let (U(K)) be the computable total-loss bound obtained there.

For fixed K,n, every history in (B_K) contains fewer than

[
N(K,n)=lceil 2^n U(K)ceil+1
]

payouts of size at least (2^{-n}). If another such payout is reachable after a prefix in (B_K), the waiting modulus places the first one within (R(K,n)) controller epochs.

Hence, after absorbing the fixed finite controller-encoding overhead, one can compute a depth

[
G(K,n)
]

such that every (vin B_K) of depth at least (G(K,n)) is **n-quiet**: no continuation through (B_K) extending v ever realizes another payout at least (2^{-n}).

Proof. If a branch had a large payout after the proposed repeated-waiting bound, successive applications of R would produce more than (N(K,n)) large payouts before that point. Their total alone would exceed U(K), contradicting the P4-S021 bad-capital bound. The bound is uniform over all branches. ∎

Thus P4-S021's local waiting hypothesis plus its already-proved effectivization theorem yields a computable finite **scale-exhaustion frontier**.

## 3. A computable residual subscale cap

At an n-quiet node v, every future positive loss is below (2^{-n}). Therefore the global P4-S021 subscale bound immediately gives a computable local residual cap

[
Q(K,n,v)
=
max{0,,T(K,n)-E_{<n}(v)}.
]

For every continuation (wsucceq v) staying in (B_K),

[
E(w)-E(v)le Q(K,n,v).
]

This Q need not be sharp. Any smaller computable valid local upper bound may be substituted. The geometric P4-S021 boundary construction in fact has a sharp computable local remainder.

For a queried boundary m, the strict inequality

[
E(v)+Q(K,n,v)<m
]

is therefore a finite, computable certificate that **no continuation of v inside (B_K) can reach m**.

The strict sign is the anti-Zeno ingredient.

## 4. Searchable strict boundary isolation is sufficient

### Definition — frontier separation certificate

For fixed K,m,n, let (F(K,n)) be the finite set of (B_K)-nodes at controller depth (G(K,n)).

Define (operatorname{SepCert}(K,m,n)) to hold when:

1. no node in (B_K) of depth at most (G(K,n)) has (Ege m); and
2. every (vin F(K,n)) satisfies
   [
   E(v)+Q(K,n,v)<m.
   ]

Because the tree through depth G is finite and all displayed quantities are computable rationals, SepCert is decidable uniformly in K,m,n.

It is sound:

[
operatorname{SepCert}(K,m,n)Longrightarrow 
egoperatorname{Reach}(K,m).
]

### Definition — effective boundary isolation

The account has **effective boundary isolation** if for every K,m with (
egoperatorname{Reach}(K,m)), some n satisfies

[
operatorname{SepCert}(K,m,n).
]

No modulus selecting such n is required. The certificate itself is finitely checkable, so n can be searched.

This is the smallest useful one-sided form of the proposed anti-Zeno condition: only genuinely unreachable boundaries need eventually acquire a strict residual gap.

### Theorem 2 — effective boundary isolation decides exact Reach

Assume the P4-S021 scale-tail hypotheses, loss-properness, and effective boundary isolation.

Then (operatorname{Reach}(K,m)) is decidable uniformly in K,m.

Proof. Run the following two searches in dovetail.

- Positive search: enumerate the computable finite bad-capital tree until a node with (Ege m) appears.
- Negative search: test (operatorname{SepCert}(K,m,n)) for (n=0,1,2,ldots).

If Reach is true, the positive search eventually finds a finite witness. If Reach is false, effective boundary isolation guarantees that the negative search eventually finds a valid SepCert. Soundness prevents both outcomes. ∎

Thus a local anti-Zeno certificate does make exact Reach decidable.

## 5. The proposed "must cross within finite depth" arm is redundant

One can formulate a stronger two-arm local condition at a scale-exhaustion frontier:

- either a node is strictly separated from m by a computable residual-tail cap;
- or, if m is reachable through that node, a computable local depth bounds a crossing witness.

This also decides Reach by a finite search.

But the second arm adds no essential effective information. Reach is already c.e. from the computable ticket tree. What was missing after P4-S021 was a positive certificate for **Bar(K,m)**, the negative case.

Therefore the minimal new boundary datum is one-sided: every true Bar instance must eventually expose a finitely checkable strict residual gap.

This is exactly the anti-Zeno role of strict boundary isolation.

## 6. It cannot be strictly weaker in final effective strength than P4-S020 searchability

P4-S020 proved that the following are equivalent:

1. a computable loss-level witness modulus (D(K,m));
2. uniform decidability of Reach(K,m);
3. uniform positive semidecidability of true Bar(K,m).

Theorem 2 puts effective boundary isolation into item 3. Consequently it automatically compiles into D:

- decide Reach using Theorem 2;
- if false, output any default depth;
- if true, enumerate finite histories until a witness appears and output its depth.

Hence the local strict-gap condition is **weaker as primitive certificate data**—it does not assume a root-level witness depth and is phrased only after fixed-scale exhaustion—but it is not strictly weaker in the resulting computability content. Once it decides every exact loss boundary, a P4-S020 witness modulus can be recovered.

This is an unavoidable logical limit on the P4-S022 search: no uniform hypothesis can make exact Reach decidable while remaining strictly below D in effective consequence.

## 7. Sharpness: the P4-S021 geometric tail fails exactly at strictness

No new construction is needed. The settled P4-S021 Mode-B machine tail already gives the exact anti-Zeno obstruction.

Fix e and

[
K_e=e+2,qquad m_e=2e+2.
]

After the index ladder, the selected-e branch has (E=2e) and (W^*=1+e<K_e).

On nonhalting progress, the machine-tail blocks have totals

[
1,rac12,rac14,ldots
]

with total 2. At every finite stage t, the current loss is strictly below (m_e), while the exact remaining geometric mass is a positive computable rational (q_t) satisfying

[
E(v_t)+q_t=m_e.
]

For every fixed scale, all larger losses are exhausted after computable finite depth, and (q_t	o0) effectively.

If (Phi_e) halts, the controller replaces the future geometric tail by one finite deterministic correction of exactly the remaining residual. Then (m_e) is reached at a finite bad-capital history.

If (Phi_e) diverges, the equality

[
E(v_t)+q_t=m_e
]

persists at every finite stage and m is never reached.

Therefore:

- strict separation (E+Q<m) never appears on the divergent selected-e branch when Q is taken to be the sharp geometric remainder;
- the weaker nonstrict estimate (E+Qle m) holds perfectly but does not distinguish divergence from later finite attainment;
- any uniform rule forcing a crossing depth from the equality case would decide whether (Phi_e) halts.

Thus the remaining obstruction is exactly **effective strictness at the boundary**, not frequency of losses, not their total mass, and not the availability of an effective tail modulus.

This is the sharpest shrinking-scale halting obstruction needed for P4-S022.

## 8. Boundary isolation does not restore absolute premium summability

Reuse the settled P4-S017/P4-S018 one-sided-trigger H=1 account.

For each fixed bad-capital level K, only computably finitely much positive-loss activity can occur before the linear relation between E and (W^*) forces exit from (B_K). Consequently one can choose n so fine that no further positive payout below (2^{-n}) is possible in (B_K), giving a trivial strict residual cap Q=0 at the corresponding scale-exhaustion frontier. Unreachable integer boundaries then have SepCerts.

Nevertheless on the unbounded all-trigger branch the exact fair premiums satisfy

[
sum_rpi_r
=
rac12sum_rrac1{r+1}
=
infty.
]

So the anti-Zeno boundary certificate does not collapse the theory back to P4-S016 absolute premium summability.

## 9. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source and suppose, as in P4-S019 through P4-S021, that a finite reserve makes the canonical full-ticket account globally admissible for a computable horizon selector.

P4-S016 gives divergent realized skipped gain along the sentinel-first completion (C(Y)). Global admissibility makes the ticket account a total nonnegative computable martingale, hence its capital is bounded on the computably random completion. Choose K above that bound.

P4-S021 then shows more: for every n, the sub-(2^{-n}) realized loss along prefixes of (C(Y)) is unbounded while those prefixes remain in (B_K). Therefore no finite subscale bound (T(K,n)) exists.

Hence P4-S011 fails before the P4-S022 boundary-isolation question is even reached. It cannot satisfy the P4-S021 scale-tail hypotheses, so it cannot have the derived scale-exhaustion/residual-gap certificate under global admissibility.

The stronger settled fact that it fails set-theoretic loss-properness is preserved. Bare admissibility remains unruled-out exactly as before.

## 10. Exact boundary after P4-S022

P4-S022 closes the first anti-Zeno formulation.

Positive result:

- P4-S021 data plus loss-properness give computable scale-exhaustion frontiers.
- At an exhausted scale, the remaining subscale mass gives a computable local residual cap.
- If every genuinely unreachable integer boundary eventually has a finitely checkable **strict** residual gap, exact Reach is decidable.
- No separate finite-depth crossing arm is needed.

Limitation:

- because Reach is c.e., any uniform local condition that supplies the missing negative certificates is automatically equivalent in effective consequence to P4-S020 loss-bar searchability and hence yields a witness modulus D.
- P4-S021's nonhalting geometric branch shows that replacing strict separation by equality/nonstrict control leaves halting information intact.

The next genuinely narrower question is therefore whether the explicit effective strict-gap certificate can itself be forced by a **semantic anti-Zeno condition** together with the strong P4-S021 effective tail convergence, rather than supplied as certificate data. The possible obstruction would have to move near-boundary mass across incompatible branches rather than along one geometric Zeno branch.

## Successes and limits

Successful:

1. Derived a computable global exhaustion depth (G(K,n)) for every fixed loss scale from the settled P4-S021 data.
2. Isolated the computable residual future-loss cap at an n-quiet frontier.
3. Formulated a finitely checkable strict boundary-separation certificate.
4. Proved that eventual certificates for all false Reach instances decide exact Reach.
5. Showed the proposed local finite-depth crossing arm is unnecessary.
6. Proved that any such uniform decision procedure necessarily compiles to the P4-S020 witness modulus, so there is no strictly weaker final effective searchability notion.
7. Identified the exact sharpness witness already present in P4-S021: equality of current gap and computable shrinking residual tail.
8. Preserved divergent absolute premium sums.
9. Checked P4-S011 explicitly.

Not claimed:

1. No theorem is proved here that semantic absence of a nonattaining boundary path automatically yields a strict-gap certificate.
2. No claim is made about incompatible-branch compactness beyond the finite frontier argument above.
3. No new randomness-destruction witness is claimed.
4. No settled P4-S005 through P4-S021 result is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S005 through P4-S021 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015 through P4-S021 are preserved exactly.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## Next bounded question

P4-S023 should remain strictly at k=2 and test only whether, under P4-S021's strong global scale deadlines and an effectively vanishing subscale tail, the **semantic anti-Zeno condition**

> no bad-capital branch has cumulative loss converging to an integer boundary m from below without reaching m at a finite history

already forces a searchable strict frontier gap by effective compactness, and hence decidable Reach. If not, isolate an exact incompatible-branch shrinking-scale construction in which every individual branch is non-Zeno but near-boundary mass moves across branches so that Bar(K,m) still hides halting information. Check P4-S011 explicitly.
