# P4-S024 — pointwise tail convergence and the incompatible-branch comb

Date: 2026-10-06
Session: P4-S024
Incoming checkpoint: 4f0eef36aa6c2223528c1e48a8e300f0e9d29ec0
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **P4-S023 DOES NOT SURVIVE GENUINELY NONUNIFORM POINTWISE / BRANCHWISE EFFECTIVE TAIL CONVERGENCE. THERE IS AN EXACT COMPUTABLE GLOBALLY k=2, GLOBALLY ADMISSIBLE INCOMPATIBLE-BRANCH COMB WITH COMPUTABLE GLOBAL EXHAUSTION OF EVERY FIXED POSITIVE LOSS SCALE AND AN EXPLICIT COMPUTABLE BAD-CAPITAL LOSS BOUND, SUCH THAT EVERY INDIVIDUAL BAD-CAPITAL BRANCH HAS ONLY FINITELY MANY POSITIVE LOSSES AND IS THEREFORE SEMANTICALLY NON-ZENO WITH A BRANCH-SPECIFIC COMPUTABLE CONVERGENCE MODULUS, YET Reach(K_e,m_e) IS EQUIVALENT TO HALTING. THE NEAR-m_e LOSS MOVES TO LATER INCOMPATIBLE TEETH WHOSE LIMIT BRANCH STAYS A FIXED DISTANCE BELOW m_e, SO THE BRANCH-LIMIT LOSS IS DISCONTINUOUS AND NO SEARCHABLE STRICT FRONTIER GAP IS FORCED. BY CONTRAST, A SINGLE ORACLE-UNIFORM BRANCHWISE CONVERGENCE FUNCTIONAL TOTAL ON ALL BAD-CAPITAL BRANCHES EFFECTIVELY COMPACTIFIES TO A COMPUTABLE UNIFORM TAIL MODULUS, SO THAT VERSION IS NOT A GENUINE WEAKENING OF P4-S023.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint \`4f0eef36aa6c2223528c1e48a8e300f0e9d29ec0\` exactly before substantive work. The incoming checkpoint contained P4-S001 through P4-S023 and no P4-S024 mathematics, close or validation record; direct path checks returned no P4-S024 record. The session identifier was therefore unused.

P4-S001 through P4-S023 and the required CAND-01 selection/Gate-3 authority were read. P4-S005 through P4-S023 are treated as settled. P4-S011's exact global-k=2 destroyer and P4-S015 through P4-S023 are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. This session stays strictly at k=2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained P4-S023 question

Keep the settled notation

\[
B_K=\{v:W^*(v)<K\},
\qquad
\operatorname{Reach}(K,m)\iff \exists v\in B_K\,[E(v)\ge m].
\]

P4-S023 assumes a computable global fixed-scale exhaustion together with one computably and uniformly vanishing subscale-tail bound. This makes the branch-limit loss a continuous function on the compact path space \([B_K]\), and semantic anti-Zeno then forces a searchable strict P4-S022 frontier gap.

The present question is whether the same conclusion follows when convergence is only pointwise or branchwise effective.

There are two materially different meanings of "branchwise effective":

1. **oracle-uniform branchwise effectivity:** one Turing functional, using the branch as oracle, returns a correct tail/Cauchy modulus for every branch;
2. **genuinely nonuniform pointwise effectivity:** every branch has some ordinary computable modulus, but there is no single functional uniformly assigning such a modulus from the branch.

The first meaning compactifies back to uniform effectivity. The second does not.

## 2. Oracle-uniform branch moduli compactify

Assume the full-ticket account is globally admissible, so its capital process is a total nonnegative computable martingale. Then each bad-capital tree \(B_K\) is a computable pruned finitely branching tree.

### Lemma 1 — \(B_K\) is pruned

If \(v\in B_K\), choose at each subsequent fair binary martingale step a child whose ticket-account capital is no larger than the current capital. Such a child exists by the martingale equation. Along the resulting continuation capital never exceeds its current value, so the running maximum remains below K.

Thus every finite \(v\in B_K\) extends to some infinite \(X\in[B_K]\).

### Definition — oracle-uniform branchwise effective convergence

Suppose there is one Turing functional \(\Gamma\) such that for every K,n and every \(X\in[B_K]\),

\[
\Gamma^X(K,n)\downarrow=N
\]

and for all \(t\ge s\ge N\),

\[
0\le E(X\upharpoonright t)-E(X\upharpoonright s)\le 2^{-n}.
\]

No uniform running-time bound for \(\Gamma\) is assumed.

### Lemma 2 — one total oracle branch modulus yields a computable global modulus

For fixed K,n, enumerate halting computations of \(\Gamma^\sigma(K,n)\) whose use is contained in the finite oracle string \(\sigma\). Each gives a cylinder \([\sigma]\) on which the same output N is forced whenever a bad-capital branch extends \(\sigma\).

These cylinders form a c.e. open cover of \([B_K]\). Because \([B_K]\) is compact, a finite subcover exists.

That finite subcover is effectively searchable. For each finite family of enumerated cylinders, remove them from the computable finitely branching tree \(B_K\). The family covers \([B_K]\) exactly when the residual tree has no infinite path. By König's lemma this is equivalent to the residual tree having some empty finite level, which can be searched.

When a finite subcover is found, take the maximum of its finitely many returned moduli. This gives a total computable

\[
H(K,n)
\]

such that every \(X\in[B_K]\) has tail variation at most \(2^{-n}\) after H(K,n).

Because \(B_K\) is pruned, the same bound applies to every finite bad-capital continuation beyond H: any finite continuation extends to an infinite branch.

Thus a single oracle-uniform branchwise modulus is already a computable **uniform tree-tail modulus**.

### Corollary 3 — P4-S023 survives this apparent weakening

Use a monotone closure of H as the frontier depth. At a sufficiently fine frontier the sound negative certificate is simply

\[
E(v)+2^{-n}<m
\]

for every frontier node v, together with absence of an earlier crossing.

If Reach(K,m) is false and every such strict frontier failed, choose frontier nodes with loss at least \(m-2^{-n}\). The P4-S023 compactness argument, now using H in place of its original T/G package, produces an infinite bad-capital branch whose loss converges to m from below without finite attainment.

Semantic anti-Zeno forbids that branch. Therefore exact Reach is decidable under the semantic promise.

So oracle-uniform branchwise effective convergence is not a genuinely weaker regime: effective compactness turns it into the uniformity needed by P4-S023.

## 3. Genuinely pointwise effectivity is different

Now weaken the hypothesis to:

> For every \(X\in[B_K]\), the prefix-loss sequence along X converges effectively with some total computable modulus \(h_X\), but no single functional uniformly producing \(h_X\) from X is assumed.

This property alone does not make the branch-limit function continuous. In fact it does not even prevent every individual branch from becoming exactly constant after finitely many positive losses while the finite near-boundary nodes migrate across incompatible branches.

The following exact comb exploits that gap.

## 4. The incompatible-branch halting comb

Use only settled k=2 least-fresh components from P4-S017 through P4-S021: zero-stake consumed controls, the finite one-sided-trigger index-advance blocks, deterministic-trigger tickets, and rational scaling.

### Index ladder

Starting from ticket reserve 1, zero-stake consumed controls either select the current index e or advance to e+1.

Reuse the settled P4-S021 finite advance block: each successful advance contributes exactly

\[
\Delta E=2,\qquad \Delta W^*=1.
\]

If a required one-sided trigger is missed or unfavourable, future positive tickets stop.

After e successful advances and selection of index e,

\[
E=2e,\qquad W^*=1+e.
\]

Put

\[
K_e=e+2,\qquad m_e=2e+2.
\]

### The comb after selecting e

Run zero-stake consumed comb controls at stages \(t=0,1,2,\ldots\).

At stage t:

- **continue outcome:** consume the control sentinel and proceed to stage t+1 with no positive loss;
- **tooth outcome:** consume the control sentinel, simulate machine \(\Phi_e\) for exactly t steps, execute one finite deterministic-ticket block, and then stop all positive tickets while exhaustively revealing the remaining coordinates.

Let

\[
\delta_t=2^{-(t+3)},\qquad N_t=2^{t+4}.
\]

Every ticket in the tooth block has certain payout \(\delta_t\), hence exact fair price \(\delta_t\) and zero net change in ticket capital.

If \(\Phi_e\) has halted within t steps, execute \(N_t\) tickets. The tooth contributes total loss

\[
N_t\delta_t=2.
\]

If \(\Phi_e\) has not halted within t steps, execute \(N_t-4\) tickets. The tooth contributes

\[
(N_t-4)\delta_t
=
2-2^{-(t+1)}.
\]

The controller is total computable: only a finite t-step machine simulation and finite rational ticket block are used at each tooth.

Denote the all-continue branch by \(X_\infty\), and the branch taking its first tooth at t by \(X_t\). Then \(X_t\to X_\infty\) in Cantor topology.

## 5. Global k=2, fair-coin and admissibility checks

All comb controls and deterministic tooth stages consume their current sentinel. The only potentially permanently nontriggering stage is one of the already-settled one-sided index-advance stages; on such a branch exactly its current sentinel is omitted and every other source coordinate is subsequently exposed.

Therefore the induced least-fresh scan is everywhere total, no-repeat, fair-coin preserving and has every fibre of cardinality at most two by the same settled global-k=2 argument as P4-S017 through P4-S021.

Reserve 1 is globally sufficient:

- successful index advances raise ticket capital;
- a failed positive-cost one-sided advance stops future positive premiums;
- deterministic tooth tickets have price exactly equal to their certain payout;
- zero-stake controls cost nothing.

Thus the canonical full-ticket account is globally admissible.

No new randomness-destruction witness is claimed. This is a boundary construction for the ticket/restart effectivity analysis.

## 6. Every individual bad-capital branch is strongly non-Zeno

Fix K. A branch in \(B_K\) can make only finitely many successful index advances, because each raises running ticket capital by 1.

After an index is selected:

- a tooth branch executes one finite deterministic block and thereafter has no positive loss;
- the all-continue spine has no comb loss at all;
- a failed ladder branch has already stopped positive tickets.

Therefore **every infinite branch through \(B_K\) has only finitely many positive-loss events.** Its cumulative loss is eventually constant.

Consequently every branch is semantically anti-Zeno at every integer boundary. More strongly, for each fixed branch X there exists an ordinary computable convergence modulus: hard-code any finite stage after its last positive loss. This is genuine pointwise/branchwise effective convergence in the nonuniform sense.

What is absent is a uniform way to recover that last-loss stage from the branch.

## 7. Reach still codes halting

### Theorem 4 — exact reachability is undecidable under pointwise effective convergence

For every e,

\[
\operatorname{Reach}(K_e,m_e)
\quad\Longleftrightarrow\quad
\Phi_e\downarrow.
\]

Proof.

At selected index e, ticket capital remains \(1+e<K_e\) throughout the comb.

If \(\Phi_e\) diverges, every tooth t ends with

\[
E
=
2e+2-2^{-(t+1)}
<
m_e,
\]

and the all-continue spine stays at \(E=2e\). Thus no selected-e branch reaches \(m_e\).

If \(\Phi_e\) halts in s steps, any tooth \(t\ge s\) executes the full block and reaches

\[
E=2e+2=m_e
\]

at a finite bad-capital history.

No other index creates a false witness. If \(j<e\), its baseline plus a full tooth is at most \(2j+2\le 2e<m_e\). Passing from e to e+1 reaches total loss \(m_e\) only when ticket capital reaches \(e+2=K_e\), which is excluded by the strict definition \(W^*<K_e\). Later indices are therefore outside \(B_{K_e}\).

Hence Reach(K_e,m_e) is true exactly when machine e halts. ∎

So on divergence

\[
\operatorname{Bar}(K_e,m_e)
\]

is true but not uniformly semidecidable. If semantic anti-Zeno plus pointwise branchwise convergence forced searchable strict frontier gaps, the nonhalting set would be c.e.; combined with ordinary halting semidecidability this would decide the halting problem.

Therefore the P4-S023 conclusion fails in the genuinely nonuniform pointwise regime.

## 8. The obstruction really moves across incompatible branches

Assume \(\Phi_e\) diverges. Then

\[
L(X_t)=m_e-2^{-(t+1)}
\longrightarrow m_e,
\]

but

\[
L(X_\infty)=2e=m_e-2.
\]

Thus the branch-limit loss function L is discontinuous at the comb spine.

Every near-boundary branch \(X_t\) is individually harmless: after its tooth, its loss is constant strictly below m. The compact topological limit \(X_\infty\) is also harmless and stays a fixed distance below m.

This is exactly the incompatible-branch escape that P4-S023's uniform tail condition ruled out. Once uniform tail control is removed, near-boundary loss can be paid farther and farther out on mutually incompatible teeth and disappear at the limit branch.

Semantic anti-Zeno is a branchwise statement; it does not forbid this discontinuity.

## 9. Strong scale exhaustion can still be retained

The counterexample is not caused by uncontrolled large losses.

Fix K,n. In a tooth t every individual payout has size

\[
\delta_t=2^{-(t+3)}.
\]

A tooth can contain a payout at least \(2^{-n}\) only when \(t\le n-3\). Below K only computably finitely many ladder indices can be selected. The ladder blocks are finite computable blocks, and the finitely many relevant tooth blocks have computable lengths.

Hence there is a computable global depth

\[
G(K,n)
\]

after which no continuation in \(B_K\) can realize any payout at least \(2^{-n}\).

The construction also has an explicit computable bad-capital loss bound, for example after harmless rounding

\[
U(K)=2K+4.
\]

So it remains effectively loss-proper and preserves global fixed-scale exhaustion.

What fails is the P4-S023 **uniformly vanishing subscale tail**. For every sufficiently fine n choose a large tooth t with \(\delta_t<2^{-n}\). Almost the entire amount 2 is then realized through sub-\(2^{-n}\) payouts on that one tooth. Thus any global subscale bound valid over \(B_{K_e}\) remains bounded away from zero.

This isolates uniform vanishing, not fixed-scale exhaustion or loss-properness, as the missing compactness datum.

## 10. No oracle-uniform modulus exists for the comb

The preceding separation is genuinely nonuniform.

Suppose one oracle functional \(\Gamma\) produced a \(1/2\)-tail modulus on every branch of the divergent selected-e comb. Run it on the all-continue spine \(X_\infty\). Its halting computation reads only finitely many comb controls and outputs some N.

Choose a tooth t later than both that oracle use and N. The tooth branch \(X_t\) agrees with \(X_\infty\) on every bit consulted by the computation, so \(\Gamma^{X_t}\) returns the same N. But after N, \(X_t\) realizes a deterministic block of total loss greater than 1, contradicting the claimed \(1/2\)-tail modulus.

Thus the comb cannot satisfy the oracle-uniform branchwise hypothesis of Lemma 2. This exactly matches the positive compactification result.

## 11. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source and fix any computable horizon selector. Suppose a finite reserve makes the associated full-ticket account globally admissible.

P4-S016 gives divergent cumulative realized skipped gain along the sentinel-first completion \(C(Y)\). Global admissibility makes ticket capital a total nonnegative computable martingale, so it is bounded on the computably random completion \(C(Y)\). Choose K above that bound. Then the entire completion branch lies in \(B_K\) while

\[
E(C(Y)\upharpoonright s)\to\infty.
\]

Therefore P4-S011 fails even the weakest finite pointwise-tail convergence considered in this session. It certainly has no branch-specific finite Cauchy modulus on that bad-capital branch, and P4-S021 already shows its loss is unbounded below every fixed positive scale.

So P4-S024 does not weaken or disturb the exact P4-S011 destroyer. The stronger settled fact that global admissibility plus loss-properness is impossible there remains unchanged. Bare admissibility remains unruled-out.

## 12. Exact boundary after P4-S024

P4-S024 separates three levels.

1. **Strong uniform effective tail convergence** — P4-S023 applies.
2. **One oracle-uniform branchwise effective modulus functional** — effective compactness recovers a global computable uniform tail modulus, so P4-S023 still applies; this is not a genuine weakening.
3. **Genuinely nonuniform pointwise/branchwise effective convergence** — insufficient. The incompatible-branch comb has eventual constancy on every branch, semantic anti-Zeno on every branch, global fixed-scale exhaustion and effective loss-properness, yet exact Reach hides halting information.

The decisive topological failure is discontinuity of the branch-limit loss. P4-S023 needs enough uniform tail information to prevent near-boundary values from disappearing when incompatible branches converge to a limit branch.

## Successes and limits

Successful:

1. Distinguished oracle-uniform branchwise effectivity from genuinely nonuniform pointwise effectivity.
2. Proved that one total oracle branch-modulus functional compactifies effectively to a computable global tail modulus.
3. Constructed an exact computable globally k=2, globally admissible incompatible-branch comb.
4. Made every individual bad-capital branch eventually loss-constant, hence strongly non-Zeno and pointwise effectively convergent.
5. Preserved computable global exhaustion of every fixed positive loss scale.
6. Preserved an explicit computable bad-capital loss bound.
7. Proved \(\operatorname{Reach}(K_e,m_e)\iff\Phi_e\downarrow\).
8. Identified discontinuity of the branch-limit loss as the exact compactness failure.
9. Checked P4-S011 explicitly and preserved it.

Not claimed:

1. No necessity theorem is claimed for martingale-transfer architectures outside the settled full-ticket plus restart decomposition.
2. No new computable-randomness destruction witness is claimed.
3. No result is claimed for k>2.
4. No novelty, Gate-4, publication or outreach claim is made.
5. P4-S005 through P4-S023 are not reopened.

## Preserved boundaries

P4-S005 through P4-S023 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015 through P4-S023 are preserved exactly.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

## Next bounded question

The counterexample fails exactly by discontinuity of the branch-limit loss. The smallest next question is whether one can replace P4-S023's uniform effective tail convergence by an **effective upper-semicontinuity / local tail-cap basis** for the branch-limit loss, strictly weaker as primitive data but strong enough that semantic anti-Zeno makes every false integer boundary expose a searchable strict frontier gap. If not, isolate the sharpest effective-topological obstruction. Stay strictly at k=2 and recheck P4-S011.
