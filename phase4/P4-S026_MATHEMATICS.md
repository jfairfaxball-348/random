# P4-S026 — one-sided integer-boundary caps and the completeness collapse

Date: 2026-10-06
Session: P4-S026
Incoming checkpoint: d4e7bedb3cb150c33c0ba84d6053035799da7e39
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **ONE-SIDED INTEGER-BOUNDARY EFFECTIVE CAPS ARE GENUINELY WEAKER AS PRESENTATION DATA THAN A COMPLETE EFFECTIVE UPPER-SEMICONTINUITY BASIS, BUT THEY DO NOT DEFINE A NEW SEARCHABILITY LEVEL. THERE IS A COMPUTABLE GLOBALLY ADMISSIBLE k=2 (IN FACT EXHAUSTIVE) TICKET STREAM WHOSE BRANCH-LIMIT LOSS IS A NONCOMPUTABLE LEFT-c.e. CONSTANT BELOW 1, SO EVERY INTEGER BOUNDARY HAS A TRIVIAL EFFECTIVE ROOT CAP WHILE NO COMPLETE RATIONAL UPPER-CAP BASIS CAN EXIST. HOWEVER, ON ANY COMPUTABLE PRUNED BAD-CAPITAL TREE, EVERY c.e. SOUND LOCAL BOUNDARY-CAP / STRICT-SUBLEVEL CERTIFICATE SYSTEM THAT IS COMPLETE ON ALL BRANCHES WITH LIMIT LOSS BELOW THE QUERIED INTEGER COMPILES, UNDER SEMANTIC ANTI-ZENO, INTO A SEMIDECISION OF Bar(K,m). SINCE Reach(K,m) ALREADY HAS c.e. POSITIVE WITNESSES, EVERY SUCH BOUNDARY-COMPLETE EFFECTIVE CAP MECHANISM COLLAPSES TO DECIDABLE Reach AND HENCE TO THE P4-S020 WITNESS MODULUS. THERE IS THEREFORE NO GENUINELY INTERMEDIATE EFFECTIVE CLASS OF THIS c.e.-BOUNDARY-COMPLETE KIND.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work. Direct incoming-checkpoint checks found no phase4/P4-S026_MATHEMATICS.md, phase4/P4-S026_CLOSE.md or phase4/P4-S026_VALIDATION.md. The only incoming commit-search hit for P4-S026 was b414f43a7f32806939be940d007afc145f8ca51f, whose message is "P4-S025 schedule P4-S026" and whose only changed file is authoritative/NEXT_SESSION_PROMPT.md. Thus P4-S026 was unique.

P4-S001 through P4-S025 and the required CAND-01 authority were read. P4-S005 through P4-S025 are treated as settled. In particular P4-S011 and P4-S015 through P4-S025 are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. This session stays strictly at k=2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained bad-capital setting

Fix a globally admissible canonical full-ticket account in the settled sentinel-first completion. For a finite resolved history \(v\), write

\[
E(v)=\text{cumulative realized positive skipped gain},
\qquad
W^*(v)=\text{running maximum ticket capital}.
\]

For integer \(K\ge1\),

\[
B_K=\{v:W^*(v)<K\}.
\]

Under global admissibility, P4-S024 gives that \(B_K\) is a computable finitely branching pruned tree.

For \(X\in[B_K]\), put

\[
L_K(X)=\sup_s E(X\upharpoonright s)\in[0,\infty].
\]

No global finiteness assumption is needed for the definitions below. If \(L_K(X)<m\), then \(X\) lies strictly below the queried integer boundary \(m\).

Recall

\[
\operatorname{Reach}(K,m)
\iff
\exists v\in B_K\,[E(v)\ge m],
\]

and

\[
\operatorname{Bar}(K,m)
\iff
\forall v\in B_K\,[E(v)<m].
\]

Reach is uniformly c.e. because finite histories are computable.

P4-S020 established the equivalence, in the settled setting, between:

1. a computable loss-level witness modulus \(D(K,m)\);
2. decidability of Reach(K,m);
3. uniform positive semidecidability of true Bar(K,m).

P4-S025 further established that a complete effective rational upper-cap basis is equivalent, by effective compactness, to a computable global uniform tail modulus. The present session asks whether integer-boundary-only upper information gives a genuinely weaker effective level.

## 2. The natural one-sided integer-boundary notion

The weakest local cap syntax relevant to a queried integer does not need arbitrary rational approximation of \(L_K\).

### Definition — c.e. strict-boundary cylinder certificates

A **boundary certificate system** is a uniformly c.e. relation

\[
\operatorname{BCert}(K,m,\sigma)
\]

on integers \(K,m\ge1\) and finite nodes \(\sigma\in B_K\), satisfying soundness:

\[
\operatorname{BCert}(K,m,\sigma)
\Longrightarrow
\forall X\in[B_K]\cap[\sigma]\quad L_K(X)<m.
\]

It is **boundary-complete** if whenever \(X\in[B_K]\) has \(L_K(X)<m\), some prefix \(\sigma\prec X\) satisfies \(\operatorname{BCert}(K,m,\sigma)\).

This is exactly effective openness of the strict integer sublevel

\[
\{X\in[B_K]:L_K(X)<m\},
\]

but only at the queried integer \(m\). It does not ask for caps below every rational \(r>L_K(X)\).

A concrete local-cap mechanism of the kind proposed in the session prompt is a special case: if an enumeration produces pairs \((\sigma,q)\) with \(q<m\) and soundness

\[
\forall X\in[B_K]\cap[\sigma]\quad L_K(X)\le q,
\]

then erase \(q\) and enumerate \(\operatorname{BCert}(K,m,\sigma)\).

### Oracle-functional form

A natural structural formulation is an oracle-uniform local boundary-clearance functional \(\Gamma\):

- if \(L_K(X)<m\), then \(\Gamma^X(K,m)\) halts;
- its finite computation outputs a prefix length \(n\) and a checkable sound cap below \(m\) valid on every bad-capital branch extending \(X\upharpoonright n\).

Finite-use halting traces of \(\Gamma\) uniformly enumerate a boundary certificate system. Thus every oracle-uniform one-sided boundary modulus of this form is covered by the abstract definition above.

This is weaker input syntax than P4-S025's complete rational upper-cap basis: it only distinguishes a branch from one integer boundary.

## 3. Representation-level separation from full effective upper-semicontinuity

The one-sided notion is not merely a notational restriction. It can hold while a complete rational upper-cap basis fails.

### Construction — a constant noncomputable branch-limit loss below the first integer

Fix a c.e. noncomputable set \(H\). Define

\[
\alpha=\sum_{e\in H}4^{-(e+2)}.
\]

Then

\[
0\le\alpha\le\sum_{e\ge0}4^{-(e+2)}=\frac1{12}<\frac14.
\]

The base-4 digits of \(\alpha\) are 0 or 1, so computability of \(\alpha\) would decide \(H\). Hence \(\alpha\) is a noncomputable left-c.e. real.

At controller stage \(s\), let

\[
a_s=\sum_{\substack{e\text{ enters }H\\\text{for the first time at stage }s}}4^{-(e+2)}.
\]

Each \(a_s\) is a computable nonnegative rational and \(\sum_s a_s=\alpha\).

Use the settled deterministic-trigger gadget to realize, at stage \(s\), certain ticket payout \(a_s\) with exact fair premium \(a_s\). Both fresh-filler children trigger and receive the same payout. The ticket-account capital therefore does not change.

All sentinels are consumed. The induced least-fresh scan is exhaustive, hence singleton-fibre and therefore inside the global k=2 class. It is everywhere total and fair-coin preserving. A finite reserve equal to the initial ticket capital funds the account globally because each deterministic premium is exactly returned by the certain payout.

For every completion branch \(X\),

\[
E(X\upharpoonright s)=\sum_{t<s}a_t,
\qquad
L_K(X)=\alpha
\]

whenever \(K\) is above the constant ticket capital.

Thus the branch-limit loss is the constant function \(\alpha\), and is classically continuous.

### Lemma 1 — every queried integer boundary has a trivial effective cap

For every integer \(m\ge1\),

\[
L_K(X)=\alpha<\frac14<m
\]

on every branch.

Hence the root cylinder itself is a sound effective boundary certificate. Equivalently, the fixed rational cap \(q=1/4\) certifies every queried integer boundary.

So a complete one-sided integer-boundary cap system exists uniformly.

### Lemma 2 — no complete rational upper-cap basis exists

Suppose a P4-S025 complete effective upper-cap basis existed.

Every enumerated sound cap \(q\) on any nonempty cylinder would satisfy \(q\ge\alpha\), because every branch has limit loss \(\alpha\).

Completeness says that for every rational \(r>\alpha\), along any branch some enumerated cap satisfies \(q<r\).

Therefore the enumeration supplies a c.e. set of rational upper bounds cofinal down to \(\alpha\). Taking the running minimum gives a computable decreasing rational sequence converging to \(\alpha\). Thus \(\alpha\) would be right-c.e.

But \(\alpha\) is already left-c.e. from the partial sums \(\sum_{t<s}a_t\). A real which is both left-c.e. and right-c.e. is computable, contradicting the choice of \(H\).

Hence full effective upper-semicontinuity fails.

### Consequence

Integer-boundary upper information is genuinely weaker **as effective presentation data** than a complete rational upper-cap basis.

This does not yet produce a new searchability class: in the example every integer Bar instance is trivial. The next theorem shows that this is unavoidable once the boundary mechanism is complete enough to resolve all false Reach instances.

## 4. Compactness collapse for every boundary-complete c.e. cap mechanism

Fix \(K,m\) and assume semantic anti-Zeno at that boundary:

> there is no \(X\in[B_K]\) such that every finite prefix has loss below \(m\) while \(E(X\upharpoonright s)\to m\).

### Lemma 3 — Bar plus semantic anti-Zeno puts every branch in the strict sublevel

Assume \(\operatorname{Bar}(K,m)\).

Then every finite bad-capital prefix has \(E<m\).

For any branch \(X\in[B_K]\), monotonicity gives \(L_K(X)\le m\): if \(L_K(X)>m\), some finite prefix would already satisfy \(E\ge m\), contradicting Bar.

Equality \(L_K(X)=m\) would make \(X\) a nonattaining Zeno branch, again contradicting the semantic anti-Zeno promise.

Therefore

\[
\forall X\in[B_K]\quad L_K(X)<m.
\]

### Theorem 4 — boundary completeness semidecides Bar

Assume a c.e. sound boundary-complete certificate system.

Enumerate its certified cylinders \([\sigma]\cap[B_K]\).

For every finite family \(F\) of already-enumerated certificates, delete their cylinders from \(B_K\). The residual is a computable finitely branching tree.

The family \(F\) covers \([B_K]\) iff the residual tree has no infinite path. By König's lemma, this is equivalent to the residual tree having an empty finite level. Since levels are finite and computable, emptiness is semidecidable.

Run this finite-cover search over the growing certificate enumeration.

If Bar(K,m) is true, Lemma 3 puts every branch in the strict sublevel \(L_K<m\). Boundary completeness gives every branch a certified prefix, so the certified cylinders cover \([B_K]\). Compactness yields a finite subcover, and the effective empty-level search eventually finds it.

Soundness ensures that a discovered finite cover is a genuine negative certificate: every branch has \(L_K<m\), so in particular no finite bad-capital history can have \(E\ge m\).

Hence true Bar(K,m) is uniformly positively semidecidable.

### Corollary 5 — every boundary-complete c.e. cap mechanism collapses to decidable Reach

Run two searches in dovetail:

1. the ordinary c.e. positive search for a finite \(v\in B_K\) with \(E(v)\ge m\);
2. the boundary-certificate finite-cover search from Theorem 4.

If Reach is true, search 1 halts. If Reach is false, Bar is true and, under semantic anti-Zeno, search 2 halts. Soundness prevents both outcomes.

Therefore Reach(K,m) is decidable uniformly on the promised class.

By settled P4-S020, a computable witness modulus \(D(K,m)\) is recoverable.

So no boundary-complete c.e. cap mechanism can force searchable Bar for every queried integer while remaining below P4-S020 searchability in final effective strength.

## 5. The collapse is representation-independent

The proof did not use numerical caps, tail moduli, fixed-scale exhaustion, continuity moduli or the P4-S021 decomposition.

It used only:

1. a computable finitely branching pruned bad-capital tree;
2. a c.e. family of sound local neighborhoods;
3. completeness of those neighborhoods for every branch strictly below the queried boundary;
4. semantic anti-Zeno to convert true Bar into strict branchwise separation.

Therefore the same collapse applies to local rational caps \(q<m\), local residual-loss bounds, oracle-uniform branchwise integer-clearance functionals, c.e. basic-open presentations of the strict integer sublevel, and any c.e. local witness relation whose certified neighborhood soundly excludes the boundary.

Changing the shape of the certificate does not create a new intermediate level if its successful certificates are effectively enumerable and complete.

## 6. Converse on the anti-Zeno promise

The collapse is not merely one-way at the abstract certificate level.

Suppose true Bar(K,m) is uniformly positively semidecidable on the semantic anti-Zeno class.

When the Bar semidecision halts, enumerate the root as a boundary certificate.

On the promised class, Bar plus semantic anti-Zeno implies by Lemma 3 that every branch has \(L_K<m\). Hence this root certificate is sound and covers the whole branch space.

Thus, relative to the same promise, the existence of an abstract boundary-complete c.e. certificate system is equivalent in effective content to positive semidecidability of Bar.

A nondegenerate local cap presentation may be mathematically more explanatory, but it cannot be computationally weaker once it is complete.

This sharpens P4-S025: the collapse is not specific to rational tail caps. It holds for every c.e. boundary-complete local exclusion language.

## 7. What a genuinely weaker future notion would have to sacrifice

To remain strictly below P4-S020 searchability, a future one-sided boundary notion must fail at least one of the two properties used by Theorem 4:

1. **effective enumerability** of sound local exclusion certificates; or
2. **completeness for every false queried boundary**.

For example, limit-computable or finite-mind-change candidate caps are not automatically c.e. sound certificates; a mechanism certifying only some cofinal safe boundary per K need not decide every Reach(K,m); and purely semantic local separation with no effective way to enumerate sound neighborhoods gives no Bar semidecision.

But any such weakening also stops, by itself, from giving the requested searchable Bar(K,m) for every query. This is a logical boundary, not a missing compactness trick.

## 8. Relation to P4-S025

P4-S025 established that complete rational effective upper-semicontinuity compactifies to a global uniform tail modulus, and that boundary-specific caps covering every false integer boundary have the same final strength as searchable Bar.

P4-S026 sharpens both sides.

First, the constant-loss example proves a real representation separation: integer-boundary caps can be available while full effective upper-semicontinuity fails.

Second, Theorem 4 removes dependence on rational caps entirely. Any c.e. sound local language which is complete for strict integer sublevels compactifies only as far as needed to semidecide Bar, and that already forces the P4-S020 collapse.

So the precise conclusion is:

> boundary-only effective information can be genuinely weaker than full effective upper-semicontinuity, but not if one asks it to resolve every exact integer boundary while also remain below decidable Reach.

## 9. Explicit P4-S011 check

Let \(Y\) be the settled P4-S011 computably random source and fix any computable horizon selector. Suppose a finite reserve makes the associated canonical full-ticket account globally admissible.

By the settled P4-S016/P4-S019 analysis, on the sentinel-first completion \(C(Y)\) the realized skipped loss diverges while the ticket-account capital is bounded because \(C(Y)\) is computably random and the account is a total nonnegative computable martingale.

Choose an integer K above that bounded capital. Then

\[
C(Y)\in[B_K],
\qquad
E(C(Y)\upharpoonright s)\to\infty.
\]

Therefore P4-S011 remains outside every hypothesis requiring a finite branch-limit loss on all of \([B_K]\), including the full P4-S025 upper-semicontinuity regime.

The deliberately weaker P4-S026 boundary-certificate notion is different: it only requires certificates on branches with \(L_K<m\). The divergent P4-S011 branch lies in no such strict sublevel. In fact, for this K and every integer m, that branch eventually witnesses Reach(K,m).

Accordingly P4-S026 does **not** claim a new failure of every boundary-only certificate system for P4-S011. On the known divergent branch the negative Bar side is simply never invoked.

All previously settled P4-S011 conclusions are preserved:

- its exact global-k=2 randomness destroyer is unchanged;
- under global admissibility, set-theoretic loss-properness fails;
- bare no-overdraft admissibility itself remains unruled-out.

No stronger P4-S011 claim is made here.

## 10. Exact boundary after P4-S026

The upper-information hierarchy is now separated cleanly.

1. **Complete rational effective upper-semicontinuity.** P4-S025: equivalent to a computable global uniform tail modulus.
2. **Boundary-only c.e. effective strict-sublevel information.** P4-S026: strictly weaker as presentation data; the constant noncomputable-loss example separates it from full effective upper-semicontinuity.
3. **Boundary completeness for every false Reach instance.** P4-S026: enough, under semantic anti-Zeno, to semidecide Bar by effective compactness; hence it collapses to decidable Reach and P4-S020's witness modulus.
4. **Pure semantic continuity / upper-semicontinuity.** P4-S025: too weak; the delayed-activation comb keeps exact Reach undecidable.

There is therefore no missing c.e. local-cap notion between "complete enough to resolve every exact integer boundary" and P4-S020 searchability. The only remaining ways to weaken boundary information are to give up effective sound-certificate enumeration or to give up completeness for every query.

## 11. Successes and limits

Successful:

1. Formalized the weakest natural c.e. one-sided integer-boundary certificate system used by local-cap proposals.
2. Showed that oracle-uniform branchwise boundary-clearance functionals compile into that system.
3. Built a computable globally admissible exhaustive k=2 ticket stream with constant noncomputable left-c.e. branch-limit loss below 1.
4. Proved that all integer boundary caps are trivial in that example while no complete rational upper-cap basis exists.
5. Thus established a genuine representation-level weakening from full effective upper-semicontinuity to integer-boundary caps.
6. Proved the general boundary-completeness collapse theorem for arbitrary c.e. sound local exclusion certificates.
7. Derived positive semidecidability of Bar, decidable Reach and recovery of the P4-S020 witness modulus.
8. Proved the abstract converse on the semantic anti-Zeno promise: Bar semidecision yields a degenerate root boundary basis.
9. Identified exactly what any strictly weaker future notion must sacrifice: c.e. soundness or all-boundary completeness.
10. Checked P4-S011 without strengthening any unsettled admissibility claim.

Limits:

1. No claim is made that limit-computable or non-c.e. boundary approximations suffice for searchable Bar.
2. No necessity theorem is claimed for martingale-transfer architectures outside the settled full-ticket plus restart decomposition.
3. No new randomness-destruction witness is claimed; the constant-loss construction is only an effectivity-separation example.
4. Bare admissibility for the P4-S011 canonical full-ticket account remains unresolved.
5. No result is claimed for k>2.
6. PA-0001 remains unresolved under inspected evidence.
7. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S011's exact k=2 destroyer is unchanged.

P4-S015's weighted theorem, P4-S016's envelope-free last-chance-ticket theorem, P4-S017's self-financing/coercivity theorem, P4-S018's running-maximum modulus boundary, P4-S019's loss-properness non-effectivity, P4-S020's searchability equivalence, P4-S021's scale-tail effectivization, P4-S022's strict boundary-isolation theorem, P4-S023's semantic anti-Zeno/uniform-tail theorem, P4-S024's pointwise incompatible-branch obstruction and P4-S025's effective-upper-semicontinuity equivalence/continuous obstruction all remain unchanged.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## Next bounded question

The c.e. all-boundary cap route is now closed: any such complete mechanism is already P4-S020 searchability in another presentation.

The smallest repeatedly preserved unresolved local question is the bare bankroll issue for the P4-S011 ticket stream.

A bounded P4-S027 should stay strictly at k=2 and test only whether there exist a computable horizon selector H and a finite reserve R making the canonical P4-S016/P4-S017 full-ticket account for the settled P4-S011 destroyer globally admissible on every completion branch, without assuming coercivity or loss-properness. If not, isolate an exact sibling family forcing arbitrarily large premium deficit / reserve demand. Preserve all P4-S015 through P4-S026 transfer boundaries and make no stronger randomness claim.
