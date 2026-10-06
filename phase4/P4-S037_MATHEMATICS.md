# P4-S037 — rolling frontier renewal and effective backward pricing

Date: 2026-10-06
Session: P4-S037
Incoming checkpoint: 6e6694a0439001933427f4e830b085da637100e1
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **THE SIMPLE P4-S035 INFINITE RAY AND THE P4-S036 RANK-ONE INFINITE OVERLAP COMPONENT BOTH NORMALIZE BY A ROLLING BACKWARD-PRICE COMPILER. THE KEY POSITIVE RESOURCE IS EFFECTIVE FRESH-FRONTIER RENEWAL: OLD SPOILED CLAIMS RETIRE IN A COMPUTABLY FINITE TRANSITION AND THE NEW OPEN CLAIMS ARE VIRTUALLY UNSEEN FAIR BITS. THEIR NORMALIZED BACKWARD PRICE HAS CONDITIONAL MEAN ONE, SO THE NEXT-BOUNDARY VECTOR DISAPPEARS EXACTLY FROM THE PREVIOUS BACKWARD STEP. THRESHOLD-STOPPING THEN REMOVES ALL BOUNDARY DISTORTION WITHOUT A POSITIVITY OR RATIO BOUND. BOUNDED OPEN-CLAIM WIDTH, FINITE COMPUTABLE FRONTIER STATE, UNIFORM POSITIVITY AND BOUNDED PRICE RATIOS ARE NOT SUFFICIENT IN GENERAL: THE RECODED P4-S011 WITNESS HAS ACTIVE WIDTH ONE, AND A HALF-STAKE VERSION STILL DESTROYS WHILE ITS LOCAL TRIGGER-price ratios are at most three. THE SURVIVING OBSTRUCTION IS NON-EFFECTIVE CLAIM RETIREMENT / BACKWARD-PRICE STABILIZATION, NOT A DIRECTED RAY OR AN INFINITE WEAK COMPONENT BY ITSELF. NO OH NON-INVARIANCE WITNESS IS PROVED.**

## Authority, uniqueness and scope

Live `main` matched the exact P4-S036 outgoing checkpoint
[
6e6694a0439001933427f4e830b085da637100e1
]
before substantive work and again immediately before the first write. The committed tree contained no P4-S037 record, so P4-S037 was unused.

P4-S001 through P4-S036, the selected CAND-01 authority in `phase2/candidates.json` and `phase2/P2-S001_DISCOVERY.md`, `phase4/P4_RESEARCH_PIVOT_AFTER_S031.md`, and P4-S032 through P4-S036 were read. All validated mathematics through P4-S036 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence is not reopened.

Retain
[
R_2={xin CR:(orall Finmathcal F_2) F(x)in CR},
]
[
OH={xin CR:(orallhbox{ one-hole scans }T) S_T(x)in CR},
]
and
[
OH^{iso}={xin CR:(orall Hinmathcal H) H(x)in OH}.
]
The retained inclusions are
[
MLRsubseteq R_2subseteq OH^{iso}subseteq OHsubsetneq CR.
]

The repeated three-bit source recoding remains
[
u_0=x_0oplus x_2,qquad
u_1=x_0oplus x_1,qquad
u_2=x_0oplus x_1oplus x_2.
]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Open-claim frontiers

Fix a total computable one-hole virtual scan (T), a computable nonnegative rational martingale (d), and a repeated invertible finite binary block recoding.

At a finite raw/virtual cut, an **open spoiled claim** is a virtual coordinate (q) such that:

1. its parity value is already determined by the raw history;
2. (T) has not yet queried (q);
3. the eventual (d)-wager on (q), if (q) is queried, is not yet closed by the currently exposed virtual information.

A finite **frontier state** records only finite computable data:

- the finite set (Q) of active open spoiled claims;
- the current finite virtual controller/transcript state;
- the raw-known parity values (zin{pm1}^{Q});
- the finite description of the first as-yet-unopened blocks which the controller may expose next.

Zero-stake claims may be deleted from (Q). No eventual halt/nonhalt fact, limiting price, or other noncomputable terminal information is stored in the state.

For a fixed finite horizon (N), continue the finite virtual simulation for (N) renewal transitions, stop at the resulting boundary, and take the terminal value of the chosen stopped martingale. Pulling this finite payoff through the finite block bijections and averaging over the still-unread raw bits gives a finite rational **backward fair-price vector**
[
P_N(s,z)
]
indexed by the finite frontier state (s) and the already raw-known open-claim values (z).

Every (P_N) is computable. P4-S036 showed that this finite computability alone does not give an infinite compiler.

## 2. Effective fresh-frontier renewal

The missing structural condition is stronger than bounded width but weaker than finite packet closure.

### Definition 1 — effective fresh-frontier renewal

A rolling frontier is **effectively fresh-renewing** if, uniformly from every reachable frontier state (s), a total computable finite decision tree over finitely many as-yet-unopened blocks is available such that on every leaf:

1. every old claim in (Q(s)) is retired — queried with its wager settled, or permanently abandoned;
2. the scan reaches either an absorbing already-safe mode or a new finite frontier (s');
3. every claim in (Q(s')) is a virtual coordinate not queried during the transition;
4. conditional on the visible virtual transition transcript, the vector of new claim values (win{pm1}^{Q(s')}) is uniform, and the virtual controller state at the new boundary is independent of (w);
5. the stopped virtual capital accumulated before the new boundary depends only on the visible transition transcript and the old claim values, not on (w);
6. successive transitions expose disjoint new raw blocks, and the induced raw evaluator is exhaustive.

The frontier width may be bounded or unbounded; the theorem below only requires each individual frontier to be finite and effectively represented. A computable uniform width bound is therefore more than is needed for the algebra.

The condition does **not** require a finite closed packet. The new claims may lie in blocks already raw-opened by the very transition which creates them.

## 3. One-step backward-price collapse

Fix a stopped martingale (d^*). At a frontier (s), write the old raw-known claim vector as (z). Let (v) denote the visible finite transition outcome, and let
[
A_s(v,z)
]
be the multiplicative change in (d^*) from the old boundary through retirement of the old claims and all visible bets before the new boundary.

If the leaf has new frontier state (s'=s'(v,z)) with fresh unseen claim vector (w), let (R_{s'}(w)) be any nonnegative normalized continuation price satisfying
[
2^{-|Q(s')|}sum_w R_{s'}(w)=1.
]

### Lemma 2 — renewal annihilates the future boundary vector

For every old frontier state,
[
mathcal T_sR(z)
=
mathbb E_{v,w}!left[A_s(v,z)R_{s'(v,z)}(w)ight]
=
mathbb E_v A_s(v,z).
]

**Proof.**
By Definition 1, conditional on (v,z), the new frontier values (w) are still uniformly distributed virtual-unseen fair bits, the new controller state does not depend on (w), and (A_s(v,z)) does not depend on (w). Therefore
[
mathbb E_w R_{s'}(w)=1
]
and the displayed identity follows. ∎

Thus the backward transfer operator loses all dependence on the next normalized price vector in one renewal step. There is no limiting projective direction to compute. In projective/log-ratio language the continuation direction is killed exactly, rather than merely contracted.

Put
[
p_s(z)=mathbb E_v A_s(v,z).
]
Because (d^*) is a fair martingale and the old open virtual coordinates are themselves unseen at the point before their raw determination,
[
2^{-|Q(s)|}sum_z p_s(z)=1.
]
Hence (p_s) is itself the normalized fair boundary price.

No uniform positive lower bound for (p_s), and no bounded condition number, is assumed.

## 4. The P4-S035 ray telescopes exactly

For the explicit ray
[
B_0	o B_1	o B_2	ocdots
]
there is one pending old parity (z=u_2^{(b)}).

At stage (b), let
[
v=(u_0^{(b+1)},u_1^{(b+1)})in{pm1}^2.
]
Let (L_h(v)) be the stopped-martingale multiplier on the two visible coordinates, including any intervening visible bets, and let (s_h(v)in[-1,1]) be the signed fractional wager on the old pending parity on the trigger branch, with (s_h(v)=0) on a branch which abandons it.

Then the exact old-boundary price is
[
p_h(z)=rac14sum_{vin{pm1}^2}L_h(v)igl(1+s_h(v)zigr).
]
Its two coordinates satisfy
[
rac{p_h(+1)+p_h(-1)}2=1.
]

On a trigger leaf, (u_2^{(b+1)}) becomes the new pending parity (w). Although it is raw-known after the block has been opened, it has not been virtually queried. Conditional on (v), (w) remains a fair bit. Therefore for every normalized next-boundary vector (r_{h'}(w)),
[
mathbb E_{v,w}
left[
L_h(v)(1+s_h(v)z)r_{h'}(w)
ight]
=
p_h(z).
]

### Corollary 3 — the finite-horizon ray prices stabilize after one backward step

Every finite-horizon normalized backward price vector at a P4-S035 ray boundary is exactly (p_h), independently of how many later ray stages are appended.

So the P4-S036 concern about an ineffective limit does not occur for this explicit ray. Its fresh carried parity supplies an exact telescoping handoff.

## 5. A single computable raw compiler

Finite approximants are not enough. The persistent-savings transform already proved in P4-S036 supplies the correct success-preserving normalization.

Normalize (d(\varnothing)=1), let (d^{[k]}) be (d) stopped on first reaching (2^k), and put
[
\widehat d=\sum_{k\ge1}2^{-k}d^{[k]}.
]
P4-S036 proved that (\widehat d) is an exactly computable nonnegative rational martingale and
[
d	ext{ unbounded}quad\Longrightarrowquad \widehat d_t\to\infty.
]

It has a stronger persistence property useful here. Once (d) has reached thresholds (2,4,\ldots,2^K) along a virtual transcript, the first (K) stopped summands each contribute at least (1) on **every** continuation of that transcript. Hence
[
\widehat d\ge K
]
on every later virtual continuation, not merely on the target path.

For a frontier state (s,z), define the **absolute rolling price**
[
V_s(z)
]
to be the fair conditional value of (\widehat d) at the end of the next computably finite renewal transition, with the old frontier retired. Equivalently, compute it by the finite decision tree from Definition 1.

At the next frontier (s',w), use (V_{s'}(w)) as the terminal raw value of the current transition. The average of (V_{s'}(w)) over the fresh virtually unseen vector (w) is exactly the current virtual capital (\widehat d) at that new boundary: this is just finite martingale averaging through the next renewal episode. Therefore Lemma 2 gives
[
\mathbb E[,V_{s'}(w)mid s,z,]=V_s(z).
]

Query the finitely many fresh raw coordinates of the current transition and use finite raw Doob conditional expectations of the terminal table (V_{s'}(w)). Concatenating these finite pieces gives one total computable nonnegative rational raw martingale (e). A finite startup piece connects the empty raw history to the first frontier. The raw evaluator is exhaustive by Definition 1.

### Lemma 4 — persistent savings defeat arbitrary boundary distortion

If the first (K) savings thresholds have been locked before a renewal boundary, then
[
V_s(z)ge K
]
for every frontier value (z) compatible with the current raw history.

**Proof.**
Every virtual continuation from that transcript has (\widehat d\ge K). In particular every leaf value at the end of the next finite renewal transition is at least (K). Its fair conditional expectation is therefore at least (K). ∎

### Theorem 5 — effective fresh-frontier renewal normalizes infinite components

Under Definition 1, if (x\in CR), no computable nonnegative rational martingale can succeed on the recoded one-hole scan output.

**Proof.**
Suppose (d) succeeds. Then (\widehat d\to\infty), and for every (K) there is a virtual stage after which the first (K) stopped savings components are permanently locked.

At every sufficiently late renewal boundary, Lemma 4 gives
[
e\ge K.
]
Thus (e) is unbounded on the exhaustive computable raw evaluator. By the settled k=1/effective-permutation invariance this contradicts (x\in CR). ∎

This construction uses one computable raw martingale, not a sequence of finite approximants. It needs no finite packet, no uniform positive lower bound on normalized prices and no bounded condition number.

### Corollary 6 — the P4-S035 infinite ray is harmless

The explicit one-pending-parity ray of P4-S035 satisfies effective fresh-frontier renewal. Therefore it cannot witness failure of OH invariance for the displayed three-bit recoding.

## 6. Infinite overlap without a directed ray also normalizes

Return to the P4-S036 rank-one architecture
[
a_n	o c_n,qquad a_n	o c_{n+1},
]
whose symmetrization is one infinite component but whose directed graph has rank one.

Use the concrete P4-S036 realization: leave (q_n) pending, expose the deciding data in (C_n), open (q_{n+1}), expose the deciding data in (C_{n+1}), and then retire (q_n). At the corresponding rolling cut, (q_{n+1}) is the fresh virtually unseen carried claim. The finite transition which retires (q_n) is computable, and its stopped virtual capital is independent of the unqueried value of (q_{n+1}).

Thus the same conditional-mean-one cancellation applies.

### Corollary 7 — the P4-S036 rank-one overlap component is harmless under its rolling realization

Failure of finite packetizability in the rank-one overlap example does not obstruct rolling normalization. An infinite weak/symmetrized interaction component, even without a directed ray, is not by itself the randomness resource.

Combined with Corollary 6, neither **directed ray** nor **infinite overlap component** is the correct obstruction in isolation.

## 7. Bounded width and bounded price ratios are not enough

The positive theorem used effective retirement of the old frontier, not merely a small frontier.

Consider the recoded P4-S011 witness (D,H,X) from P4-S033. Its virtual scan has only one active epoch/sentinel at a time. The standard output martingale holds on filler coordinates and wagers only when the sentinel is finally queried. Therefore, after deleting zero-stake claims, the active spoiled open-claim width is at most one.

Its frontier data are finite and computable: the sentinel index, finite scan transcript, finite simulation state, and any already raw-known sentinel parity.

Nevertheless
[
Xin CR,qquad D(H(X))
otin CR.
]
Hence bounded open-claim width plus a finite computable frontier representation cannot be sufficient for a universal raw compiler.

The same conclusion survives strong local price conditioning. Replace the all-in sentinel wager by the fixed fractional wager (r=1/2) on the predicted sentinel bit. Along the P4-S011 target every prediction is correct and infinitely many epochs close, so the capital still grows by a factor (3/2) at every sentinel and succeeds.

Once the sentinel parity has become raw-known, a finite horizon which has not yet witnessed the trigger has local price vector
[
(1,1).
]
When the trigger becomes visible with predicted sign (a), the corresponding price vector is
[
left(1+rac a2, 1-rac a2ight),
]
up to ordering of the two parity values. Thus every coordinate lies in
[
[1/2,3/2]
]
and every nontrivial local condition number is at most (3).

### Proposition 8 — positivity and bounded ratios do not replace effective stabilization

There is a recoded P4-S011 destructive witness with active open-claim width one and uniformly positive locally triggered price vectors of ratio at most (3). Therefore bounded width, finite state, uniform positivity and bounded price ratios, separately or together, do not force normalization.

The surviving issue is whether the price jump ever occurs, not how badly conditioned the two prices are.

## 8. What fails in the recoded P4-S011 schedule

The wtt use bound remains only finite per-claim dependency data.

For one epoch, once all source coordinates below the computable use frontier relevant to the sentinel computation have been exposed, future filler **values** cannot change the eventual computation. But a finite partial simulation does not in general decide that the computation will never halt. The scan can therefore keep emitting fresh irrelevant fillers while the same sentinel claim remains open, and a later finite simulation may still reveal the halt.

For the half-stake martingale, the finite-horizon price vector on such a branch remains ((1,1)) until the halt becomes visible and then jumps to the fixed ((3/2,1/2))-type vector. Thus a total computable modulus of eventual constancy for these price vectors would decide, uniformly on the corresponding reachable frontier states, whether the sentinel computation will ever return.

The committed P4-S011 data do not supply such a modulus. P4-S036 already shows that the actual recoded witness has no total computable finite closed packetizer. P4-S037 now identifies the more local reason relevant to rolling pricing: **value dependence may already be finite while claim retirement remains only semidecidable**.

At the event level the scan is temporally acyclic: source coordinates are never queried twice, sentinels advance through fresh coordinates, and an individual sentinel claim is never reopened after retirement. Hence recurrent/cyclic claim dependence is not the source of the obstruction.

The committed abstract wtt-autoreduction does not specify enough sibling-halting geometry to decide whether the coarse block-level essential dependency quotient contains a genuine infinite directed ray rather than an infinite chain of overlapping finite closures. That distinction is no longer decisive for the normalization theorem: both graph shapes are harmless when fresh renewal is effective, while the P4-S011 obstruction persists at width one because retirement is not effectively settled.

## 9. General effective-price criterion

The rolling theorem has a direct analytic formulation.

### Theorem 9 — effective backward-price stabilization is sufficient

Apply the P4-S036 persistent-savings transform first, obtaining (\widehat d).

Suppose every reachable finite frontier state has finite-horizon **absolute** backward prices for (\widehat d) which converge uniformly effectively, with a total computable Cauchy modulus and a computable limiting price vector, and suppose the limiting vectors satisfy the one-step Doob consistency equations along the computable raw evaluator.

Then those limiting conditional values form one total computable nonnegative raw martingale. If (d) succeeds, the persistent-savings floor is eventually at least (K) on every continuation of the current virtual transcript for each (K). Every limiting conditional price from that point is therefore at least (K), so the raw martingale succeeds.

Effective fresh-frontier renewal is a structural sufficient condition for Theorem 9 in which no limiting computation is required at all: the normalized continuation vector is annihilated after one backward renewal step.

This is the weakest exact positive hypothesis isolated in this session. Bounded width, graph rank, positivity and bounded price ratios do not imply it.

## 10. Separation status

No proof of
[
Xin OH
]
for the P4-S033 recoded P4-S011 source is obtained.

Therefore P4-S037 proves neither OH non-invariance nor
[
R_2subsetneq OH.
]

The retained comparison remains
[
MLRsubseteq R_2subseteq OH^{iso}subseteq OHsubsetneq CR.
]

P4-S032 null-ambiguity preservation remains unchanged. Ambiguity mass is not reinstated as an invariant.

## 11. Exact next target

P4-S038 should attack **persistent-frontier claim retirement and non-effective backward-price stabilization**, not infinite-component geometry by itself.

The sharp test case is the recoded P4-S011 epoch after its finite wtt value-use frontier has been exhausted but before the sentinel computation is known to halt or diverge. The local price vector is well conditioned; the unresolved datum is the c.e. future price jump.

Determine the weakest effective retirement hypothesis which makes the limiting stopped price computable — for example a computable retirement modulus, an effectively summable unresolved-price tail, or another exact optional-projection criterion — and test whether it follows from one-hole geometry under the displayed recoding. If it does not, isolate an exact persistent-claim pricing obstruction inside the actual one-hole problem.

Do not return to the frozen P4-S015–P4-S031 bankroll sequence unless this retirement analysis genuinely requires it.

## Guards

All mathematics through P4-S036 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 remains OPEN; Phase 5 remains CLOSED.
