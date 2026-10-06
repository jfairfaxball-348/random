# P4-S025 — effective upper-semicontinuity and non-effective continuity obstruction

Date: 2026-10-06
Session: P4-S025
Incoming checkpoint: 2b6c46b63029c454cc5536cfc11d51786d0590a1
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **A NATURAL EFFECTIVE UPPER-SEMICONTINUITY / LOCAL UPPER-TAIL-CAP BASIS DOES FORCE SEARCHABLE STRICT FRONTIER GAPS WITH SEMANTIC ANTI-ZENO, BUT IT IS NOT A GENUINE WEAKENING OF P4-S023: ON THE COMPUTABLE PRUNED BAD-CAPITAL TREE, EFFECTIVE UPPER CAPS COMPACTIFY TO A COMPUTABLE GLOBAL UNIFORM TAIL MODULUS. CONVERSELY SUCH A UNIFORM MODULUS ENUMERATES AN EFFECTIVE UPPER-CAP BASIS. THE SHARP REMAINING OBSTRUCTION IS EFFECTIVITY, NOT SEMICONTINUITY ITSELF: THERE IS AN EXACT COMPUTABLE GLOBALLY k=2, GLOBALLY ADMISSIBLE DELAYED-ACTIVATION COMB WITH COMPUTABLE FIXED-SCALE EXHAUSTION, EFFECTIVE LOSS-PROPERNESS, EVENTUAL CONSTANCY AND SEMANTIC ANTI-ZENO ON EVERY BRANCH, AND A CONTINUOUS BRANCH-LIMIT LOSS, YET Reach(K_e,m_e) IS EQUIVALENT TO HALTING. ITS CONTINUITY MODULUS / UPPER-CAP BASIS IS NON-EFFECTIVE.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work. Direct incoming-checkpoint path checks returned no P4-S025 mathematics, close or validation record, and repository search returned no P4-S025 record. The session identifier was unused.

P4-S001 through P4-S024 and required CAND-01 authority were read. P4-S005 through P4-S024 are treated as settled. P4-S011 and P4-S015 through P4-S024 are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. This session stays strictly at k=2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained bad-capital setting

Fix a globally admissible canonical full-ticket account in the settled sentinel-first completion. For a finite resolved history \(v\), let

\[
E(v)=\text{cumulative realized positive skipped gain},
\qquad
W^*(v)=\text{running maximum ticket capital}.
\]

For an integer \(K\ge1\),

\[
B_K=\{v:W^*(v)<K\}.
\]

Under global admissibility the ticket-account capital is a total computable nonnegative martingale. The settled P4-S024 pruning argument therefore applies: \(B_K\) is a computable finitely branching pruned tree.

For \(X\in[B_K]\), when the monotone prefix losses are bounded, write

\[
L_K(X)=\lim_s E(X\upharpoonright s)=\sup_s E(X\upharpoonright s).
\]

Because \(E(v)\) is computable and monotone along extensions, \(L_K\) is automatically lower semicomputable on branch space in the following exact sense: for rational \(a\),

\[
\{X\in[B_K]:L_K(X)>a\}
\]

is effectively open, witnessed by a finite prefix with \(E>a\).

P4-S024 showed that pointwise effective convergence does not control the missing upper direction. The incompatible-branch comb made \(L_K\) discontinuous.

P4-S025 tests exactly that upper direction.

## 2. Effective upper-semicontinuity as a local tail-cap basis

The natural effective upper-semicontinuity representation for this monotone limit is a c.e. local upper-cap basis.

### Definition — effective local upper-cap basis

Uniformly in K, enumerate triples

\[
(\sigma,q),\qquad \sigma\in B_K,\ q\in\mathbb Q,
\]

with the following two properties.

**Soundness.** For every branch \(X\in[B_K]\) extending \(\sigma\),

\[
L_K(X)\le q.
\]

**Local completeness.** For every \(X\in[B_K]\) and every rational \(r>L_K(X)\), some enumerated pair \((\sigma,q)\) has

\[
\sigma\prec X,\qquad q<r.
\]

We may computably close the enumeration under extensions: if \((\sigma,q)\) is enumerated and \(\tau\in B_K\) extends \(\sigma\), enumerate \((\tau,q)\).

Equivalently, for each rational r the sublevel set

\[
\{X\in[B_K]:L_K(X)<r\}
\]

is effectively open relative to \([B_K]\). This is the standard upper-semicomputable / effectively upper-semicontinuous direction specialized to the present compact tree.

The basis is local. It does not explicitly provide a global tail depth.

## 3. Effective upper caps compactify to a uniform tail modulus

The local appearance is deceptive.

### Theorem 1 — effective upper caps imply computable uniform tail convergence

Assume an effective local upper-cap basis. Then there is a total computable function

\[
H(K,n)
\]

such that for every \(X\in[B_K]\) and every \(s\ge H(K,n)\),

\[
0\le L_K(X)-E(X\upharpoonright s)<2^{-n}.
\]

Hence the convergence of prefix loss to branch-limit loss is computably uniform over the whole bad-capital branch space.

### Proof

Fix K,n and put \(\varepsilon=2^{-n}\).

Enumerate every upper-cap pair \((\sigma,q)\), close it under extensions \(\tau\in B_K\), and retain those extensions satisfying

\[
q-E(\tau)<\varepsilon.
\]

Each retained cylinder \([\tau]\cap[B_K]\) is soundly \(\varepsilon\)-tight: every branch X through it satisfies

\[
0\le L_K(X)-E(\tau)\le q-E(\tau)<\varepsilon.
\]

These tight cylinders cover \([B_K]\). To see this, fix X and let \(L=L_K(X)\). Pointwise convergence gives a prefix \(\rho\prec X\) with

\[
L-E(\rho)<\varepsilon/2.
\]

Choose a rational r with

\[
L<r<E(\rho)+\varepsilon.
\]

Local completeness gives an upper-cap pair \((\sigma,q)\) along X with \(q<r\). Extend both \(\rho\) and \(\sigma\) along X to one longer prefix \(\tau\). Then

\[
q-E(\tau)\le q-E(\rho)<r-E(\rho)<\varepsilon.
\]

So X lies in an enumerated tight cylinder.

Now use effective compactness. For any finite family of enumerated cylinders, whether it covers \([B_K]\) is semidecidable: delete the cylinders from the computable finitely branching tree \(B_K\) and search for an empty residual level. Compactness guarantees that some finite family of tight cylinders covers, so this search eventually finds one.

Let H(K,n) be the maximum length of the finitely many covering prefixes. If \(s\ge H(K,n)\), every X extends one covering prefix \(\tau\), and monotonicity gives

\[
L_K(X)-E(X\upharpoonright s)
\le L_K(X)-E(\tau)
<2^{-n}.
\]

The construction is uniform in K,n. ∎

This is an effective Dini-type compactness step specialized to the monotone computable prefix-loss process.

### Consequence

A full effective upper-semicontinuity representation is **not** genuinely weaker than the uniform-tail datum needed in P4-S023. It reconstructs a computable global uniform tail modulus.

The reconstructed H need not reproduce P4-S021's separate fixed-scale exhaustion \(G\) and subscale bound \(T\). It directly supplies the stronger net statement actually used in the P4-S023 compactness proof: all future bad-capital loss after H is uniformly small.

## 4. The converse: a uniform tail modulus gives effective upper caps

The collapse is two-sided.

### Lemma 2 — uniform tails enumerate a local upper-cap basis

Suppose H(K,n) is a computable uniform tail modulus:

\[
s\ge H(K,n)
\Longrightarrow
L_K(X)-E(X\upharpoonright s)\le 2^{-n}
\]

for every bad-capital branch X.

For every \(n\) and every \(\sigma\in B_K\) with \(|\sigma|\ge H(K,n)\), enumerate the cap

\[
q=E(\sigma)+2^{-n}.
\]

It is sound on every branch extending \(\sigma\).

For local completeness, fix X and rational \(r>L_K(X)\). Choose n with

\[
2^{-n}<r-L_K(X).
\]

At depth at least H(K,n), the enumerated cap q along X satisfies

\[
q\le L_K(X)+2^{-n}<r.
\]

Thus the natural effective upper-cap basis and a computable global uniform tail modulus are equivalent, up to harmless strict/non-strict rational margins, in the present monotone compact-tree setting.

## 5. Semantic anti-Zeno then decides exact Reach

Fix an integer m and assume semantic anti-Zeno at \((K,m)\): no infinite branch through \(B_K\) has every finite prefix below m while its cumulative loss converges to m.

Assume an effective upper-cap basis, hence the computable uniform tail modulus H from Theorem 1.

### Theorem 3 — searchable strict frontier separation

If

\[
\neg\operatorname{Reach}(K,m),
\]

then for some n every bad-capital node v at depth H(K,n) satisfies

\[
E(v)+2^{-n}<m.
\]

There is also no earlier node with E at least m.

### Proof

False Reach keeps every finite bad-capital prefix below m.

If the displayed strict frontier failed for every n, choose a depth-H(K,n) node \(v_n\) with

\[
E(v_n)+2^{-n}\ge m.
\]

By finite branching choose a diagonal subsequence converging to a branch X through \(B_K\). The uniform tail bound transfers the near-m values to X and gives

\[
L_K(X)=m.
\]

Every finite prefix remains below m because Reach is false. This is a forbidden nonattaining Zeno branch. ∎

The certificate is finitely checkable. Dovetail:

1. the ordinary c.e. search for a finite witness with \(E\ge m\); and
2. the search over n for the finite strict frontier above.

If Reach is true, the first search halts. If Reach is false, Theorem 3 makes the second halt. Therefore Reach(K,m) is decidable under the semantic anti-Zeno promise.

By settled P4-S020, the witness modulus D(K,m) is recoverable.

So effective upper-semicontinuity does answer the positive part of the P4-S025 question, but only because it has already restored P4-S023-level uniform tail effectivity.

## 6. Boundary-specific caps do not create a new intermediate effective class

One could weaken the local data by asking only for c.e. sound cylinders proving

\[
L_K<m
\]

for the particular queried integer boundary m, and require those cylinders to cover \([B_K]\) whenever Reach(K,m) is false under anti-Zeno.

Effective compactness would then find a finite subcover and semidecide true Bar(K,m).

But this is exactly the missing negative half of Reach searchability. By P4-S020/P4-S022, uniform positive semidecidability of true Bar instances is equivalent in final computability strength to decidable Reach and hence to a loss-level witness modulus.

Thus:

- a complete rational upper-cap basis is full effective upper-semicontinuity and collapses to a uniform tail modulus;
- a boundary-only cap basis can be weaker as primitive syntax, but if it is guaranteed to cover precisely all false integer Reach instances, it is just the already-settled searchable-Bar mechanism in topological form.

No genuinely new intermediate effective consequence is obtained that decides all exact boundaries while remaining below P4-S020 searchability.

## 7. Semantic upper-semicontinuity is not enough effectively

The positive result above uses **effective** upper caps. Ordinary upper-semicontinuity is a different matter.

Because \(L_K\) is already lower semicontinuous as a supremum of finite-prefix losses, ordinary upper-semicontinuity makes it continuous. On compact \([B_K]\), false Reach plus semantic anti-Zeno then gives a set-theoretic strict gap below m.

The gap need not be computably searchable.

The following exact delayed-activation comb proves that this remaining effectivity obstruction is real.

## 8. Delayed-activation continuous halting comb

Use only settled k=2 least-fresh components: zero-stake consumed controls, the P4-S021/P4-S024 index ladder, deterministic-trigger tickets with rational scaling, and finite exhaustive tails.

### Index ladder

Reuse the settled advance block. After e successful advances and selection of index e,

\[
E=2e,\qquad W^*=1+e.
\]

Put

\[
K_e=e+2,\qquad m_e=2e+2.
\]

Immediately after selection, execute a finite deterministic calibration block of total realized loss 1. Its fair premium equals its certain payout, so ticket capital does not change. The comb therefore starts from

\[
E=2e+1=m_e-1,\qquad W^*=1+e<K_e.
\]

### Comb stages

At stage \(t=0,1,2,\ldots\), consume one zero-stake control sentinel. The control chooses either a tooth now or continuation to the next comb stage.

Let

\[
\delta_t=2^{-(t+3)},\qquad M_t=2^{t+3}.
\]

Simulate \(\Phi_e\) for exactly t steps.

If a halt is visible by stage t, then regardless of the control outcome execute \(M_t\) deterministic tickets, each with certain payout \(\delta_t\), and stop all later positive tickets. Their total loss is

\[
M_t\delta_t=1.
\]

Thus the selected-e branch reaches \(m_e\) finitely.

If no halt is visible by stage t:

- on the tooth outcome, execute exactly four deterministic tickets of payout \(\delta_t\), for total added loss
  \[
  4\delta_t=2^{-(t+1)},
  \]
  then stop all later positive tickets;
- on the continue outcome, add no positive loss and proceed to stage t+1.

The controller is computable: every machine simulation is finite, every ticket block is finite, and every next query is given by settled least-fresh finite state.

## 9. k=2, fair-coin and admissibility checks

The index ladder is the settled global-k=2 component.

All calibration tickets, comb controls and comb ticket blocks consume their sentinels. A failed one-sided ladder advance is the only possible permanently nontriggering component; as settled, it omits exactly its current sentinel and exposes every other source coordinate.

Therefore the complete scan remains everywhere total, computable, no-repeat, fair-coin preserving and globally fibre-bounded by two.

Reserve 1 remains globally sufficient:

- successful ladder advances increase ticket capital;
- a failed positive-cost one-sided ladder stage stops future positive premiums;
- every deterministic calibration/comb ticket has price equal to certain payout;
- zero-stake controls cost nothing.

This is another ticket/restart boundary example, not a new computable-randomness destroyer.

## 10. Reach still codes halting

### Theorem 4

For every e,

\[
\operatorname{Reach}(K_e,m_e)
\iff
\Phi_e\downarrow.
\]

### Proof

At selected index e, the ticket account remains at \(1+e<K_e\) throughout the calibration and comb.

If \(\Phi_e\) diverges, a tooth at stage t ends at

\[
E=m_e-1+2^{-(t+1)}<m_e,
\]

while the all-continue spine stays at \(m_e-1\). Hence the selected-e comb never reaches m_e.

If \(\Phi_e\) halts in s steps, any surviving branch reaching comb stage s sees the halt and executes the full correction of total 1, reaching \(m_e\) at a finite bad-capital history.

As in P4-S021/P4-S024, no other selected index creates a false witness:

- every earlier \(j<e\) has total selected-index loss at most \(2j+2\le2e<m_e\);
- advancing from e to e+1 first reaches total ladder loss \(2e+2=m_e\) exactly when ticket capital reaches \(e+2=K_e\), outside the strict bad-capital set;
- later indices therefore cannot contribute inside \(B_{K_e}\).

Thus Reach is equivalent to halting. ∎

## 11. Every branch is anti-Zeno and the branch-limit loss is continuous

Every bad-capital branch has only finitely many positive-loss events.

For a divergent machine:

- the all-continue branch has limit \(m_e-1\);
- the tooth-t branch has limit
  \[
  m_e-1+2^{-(t+1)};
  \]
- tooth branches converge in Cantor topology to the all-continue branch, and their limit losses converge to the same value.

So \(L_K\) is continuous at the comb spine.

If the machine halts at stage s, only the finitely many pre-s teeth can terminate below m_e. Every branch which survives to stage s receives the full correction and then stops positive loss. The corresponding terminal component has constant branch-limit m_e. Continuity is immediate.

Below a fixed K only finitely many selected indices can occur because every successful ladder advance raises ticket capital by one. The remaining failed-ladder components are settled eventually constant pieces. Hence \(L_K\) is continuous on the entire compact bad-capital branch space.

Since every branch is eventually loss-constant, semantic anti-Zeno holds at every integer boundary.

This restores exactly the topological property missing from P4-S024.

## 12. Strong ancillary effectivity survives

The example still retains substantial effective structure.

### Computable fixed-scale exhaustion

Every comb payout at stage t has size \(\delta_t=2^{-(t+3)}\). A payout at least \(2^{-n}\) can therefore occur only at comb stages \(t\le n-3\).

Even when a machine halts very late, its total correction 1 is split into \(M_t\) payouts of the tiny size \(\delta_t\). Thus late halting does not reintroduce a large payout.

Below fixed K only computably finitely many ladder indices are relevant. Taking the maximum controller depth of the finitely many ladder/calibration blocks and comb blocks with \(t\le n-3\) gives a computable global fixed-scale exhaustion depth \(G(K,n)\).

### Effective loss-properness

Below K, only finitely many index advances occur, each contributing the settled constant loss amount, and every selected comb contributes at most 2 after its \(2e\) ladder baseline. A coarse computable linear bound such as

\[
U(K)=2K+4
\]

remains valid.

Thus the obstruction is not loss-properness and is not failure of fixed-scale exhaustion.

## 13. What fails is effective upper-semicontinuity

For every fixed actual machine behavior the branch-limit loss is continuous, so compactness gives an ordinary uniform tail modulus and, on a false Reach instance, an ordinary strict gap.

But there is no uniform computable local upper-cap basis of the kind in Section 2.

If there were, Theorem 1 would compute a global uniform tail modulus. Theorem 3, together with the already-verified semantic anti-Zeno property, would decide every Reach(K_e,m_e). Theorem 4 would then decide the halting problem.

Equivalently, when \(\Phi_e\) has not yet halted, no sound effective neighborhood of the surviving comb spine can certify that the extra future loss stays below 1: a sufficiently late halt would activate the full correction inside that neighborhood. If \(\Phi_e\) never halts, such a strict upper neighborhood exists semantically, but its validity is not effectively recognizable.

This is the sharp effective-topological obstruction:

> compact continuity gives a strict gap; effective upper neighborhoods are what make the gap searchable.

The missing datum is not branchwise convergence, not ordinary continuity, and not fixed-scale exhaustion. It is effective upper information about the limit function.

## 14. Relation to P4-S024

P4-S024 used a divergent-machine comb with

\[
L(X_t)\to m_e,\qquad L(X_\infty)=m_e-2,
\]

so \(L\) was discontinuous. P4-S025 shows that discontinuity itself is not the final effectivity boundary.

The delayed-activation comb modifies the teeth so that on nonhalting behavior

\[
L(X_t)=m_e-1+2^{-(t+1)}
\to
m_e-1
=
L(X_\infty).
\]

If a halt is eventually detected, every still-surviving branch receives a finite full correction, preserving continuity.

Thus semantic continuity can coexist with undecidable exact Reach. What fails is a **uniform effective presentation of that continuity from above**.

## 15. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source and fix any computable horizon selector. Suppose a finite reserve makes the associated canonical full-ticket account globally admissible.

P4-S016 gives

\[
E(C(Y)\upharpoonright s)\to\infty
\]

along the sentinel-first completion \(C(Y)\). Global admissibility makes the full-ticket account a total nonnegative computable martingale, hence its capital is bounded on the computably random completion. Choose K above that bound. Then the entire completion branch lies in \(B_K\) while its cumulative realized loss diverges.

Therefore a finite branch-limit value \(L_K(C(Y))\) does not exist. In particular:

- there is no finite effective upper-cap basis for that bad-capital branch;
- there is no semantic finite upper-semicontinuous branch-limit loss there;
- no uniform tail modulus exists.

So P4-S011 remains excluded before the P4-S025 upper-semicontinuity boundary is reached. Its exact k=2 destroyer is unchanged. The stronger settled failure of loss-properness under global admissibility is preserved. Bare admissibility remains unruled-out.

## 16. Exact boundary after P4-S025

P4-S025 separates three levels.

1. **Effective upper-semicontinuity / complete computable local tail caps.**  
   Sufficient with semantic anti-Zeno, but not genuinely weaker than P4-S023. Effective compactness converts the local caps into a computable global uniform tail modulus.

2. **Ordinary upper-semicontinuity / continuity.**  
   Together with semantic anti-Zeno it gives a strict gap set-theoretically, but not a searchable one. The delayed-activation comb is continuous, branchwise eventually constant, fixed-scale effective and loss-proper, yet exact Reach hides halting.

3. **Boundary-specific effective caps.**  
   If supplied only for false integer boundaries they suffice, but they are exactly a topological encoding of the already-settled positive semidecidability of Bar(K,m), hence recover P4-S020 searchability rather than defining a new weaker effective level.

The sharp unresolved direction is therefore no longer “usc versus continuity.” Full effective usc has collapsed to uniform tails, while semantic usc is too weak computationally. Any genuinely new weakening would have to provide less than a complete effective upper-cap basis yet more than semantic continuity, without merely restating Bar searchability.

## Successes and limits

Successful:

1. Formalized a natural effective upper-semicontinuity / local tail-cap basis for branch-limit loss.
2. Proved that the basis effectively compactifies to one computable global uniform tail modulus on every bad-capital tree.
3. Proved the converse: a computable uniform tail modulus enumerates such a basis.
4. Therefore effective usc plus semantic anti-Zeno forces searchable strict frontier gaps and decidable Reach, but is not a genuine weakening of P4-S023.
5. Isolated boundary-specific cap data as equivalent in final strength to the settled searchable-Bar / decidable-Reach mechanism.
6. Built an exact computable globally k=2, globally admissible delayed-activation comb with continuous branch-limit loss, eventual constancy and semantic anti-Zeno on every branch.
7. Preserved computable fixed-scale exhaustion and an explicit computable bad-capital loss bound in that obstruction.
8. Proved Reach(e+2,2e+2) is still equivalent to halting.
9. Identified the sharp obstruction as non-effective upper information / noncomputable continuity modulus rather than discontinuity itself.
10. Checked P4-S011 explicitly and preserved it.

Not claimed:

1. No necessity theorem is claimed for martingale-transfer architectures outside the settled full-ticket plus restart decomposition.
2. No new computable-randomness destroyer is claimed.
3. No result is claimed for k>2.
4. No novelty, Gate-4, publication or outreach claim is made.
5. P4-S005 through P4-S024 are not reopened.

## Preserved boundaries

P4-S005 through P4-S024 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015 through P4-S024 are preserved exactly.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

## Next bounded question

P4-S026 should remain strictly at k=2 and test only the narrow intermediate effectivity gap isolated here: whether a one-sided **effective boundary-modulus** weaker than a complete upper-semicontinuity basis — for example, a computable local cap mechanism only when the limit is separated from a queried integer boundary, without arbitrary rational upper approximation — can be derived from a natural structural hypothesis and force searchable Bar(K,m) without already being equivalent to P4-S020 searchability. Otherwise prove that every such boundary-complete effective cap mechanism collapses to decidable Reach. Recheck P4-S011.
