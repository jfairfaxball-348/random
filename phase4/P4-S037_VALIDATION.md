# P4-S037 validation

Date: 2026-10-06
Session: P4-S037
Incoming checkpoint: 6e6694a0439001933427f4e830b085da637100e1
Scope: rolling finite-state normalization and effective backward pricing
Status: **VALIDATED**

## Repository and scope checks

- Live `main` was exactly `6e6694a0439001933427f4e830b085da637100e1`, the P4-S036 outgoing checkpoint, before substantive work and immediately before the first P4-S037 write.
- The pinned committed tree contained no P4-S037 mathematics, close or validation record, so P4-S037 was unique.
- P4-S001 through P4-S036 were read as committed mathematical authority.
- The selected CAND-01 authority in `phase2/candidates.json` and `phase2/P2-S001_DISCOVERY.md`, the sustained pivot record, and P4-S032 through P4-S036 were read.
- All validated mathematics through P4-S036 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence was not reopened.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. The frontier state contains only finite computable data

The P4-S037 frontier records the finite active claim set, finite virtual controller state, already raw-known parity values and a finite description of the next unopened blocks.

It deliberately excludes eventual halt/divergence facts and limiting prices. Every recorded field is recoverable by finite simulation from the current raw/virtual history.

Thus the state definition does not hide the very non-effective information under investigation.

### 2. Fresh renewal gives exact conditional mean one

At a renewing transition, all old claims retire in a computably finite decision tree. The new frontier coordinates have not been virtually queried during that transition.

Because the repeated block recoding is a finite measure-preserving bijection, unqueried virtual coordinates remain independent fair bits conditional on the visible virtual transcript. The new virtual controller state and the stopped virtual capital at the new boundary cannot depend on their unseen values.

Hence every normalized continuation price vector has conditional mean one over the new frontier vector. Averaging over that fresh vector removes the continuation price exactly.

This validates Lemma 2. It is an equality, not an asymptotic contraction argument.

### 3. The explicit P4-S035 ray has one-step price stabilization

For one carried parity (z=u_2^{(b)}), the next visible pair
[
v=(u_0^{(b+1)},u_1^{(b+1)})
]
is uniform. Conditional on that pair, the carried next parity (w=u_2^{(b+1)}) remains fair and has not been virtually queried.

The old-claim multiplier is
[
L_h(v)(1+s_h(v)z).
]
Therefore the local price
[
p_h(z)=rac14sum_vL_h(v)(1+s_h(v)z)
]
is exactly the backward price regardless of the normalized continuation vector placed at the next frontier.

The two old-parity prices average to one by finite martingale fairness. Thus all finite-horizon normalized ray prices agree after the first backward renewal step.

This validates Corollary 3. No Cauchy modulus or limiting projective direction is needed for the P4-S035 ray.

### 4. Persistent savings supplies one successful raw martingale

P4-S036 already validated
[
widehat d=sum_{kge1}2^{-k}d^{[k]}
]
as an exactly computable rational martingale tending to infinity whenever (d) is unbounded.

If thresholds (2,ldots,2^K) have been hit, their first (K) stopped components each contribute at least one forever on every continuation of the present virtual transcript. Hence (widehat dge K) uniformly on all later virtual continuations.

At each renewal transition the next boundary price table is finite and rational. Finite raw Doob expectations therefore give a computable nonnegative raw martingale segment. Lemma 2 makes adjacent segments consistent at their shared frontier values, so they concatenate to one total raw martingale.

Once (K) savings components are locked, every leaf of every later renewal transition has value at least (K). Every conditional price, and therefore the raw martingale at every later renewal boundary, is at least (K).

Thus the raw martingale is unbounded whenever the virtual martingale succeeds. This validates Lemma 4 and Theorem 5 without any positivity or condition-number hypothesis on normalized prices.

### 5. The raw evaluator is legitimate

Definition 1 requires successive transitions to use disjoint newly opened raw blocks and the induced evaluator to be exhaustive.

A computable exhaustive no-repeat raw scan is an effective permutation/isomorphism under the settled k=1 result. Therefore a successful computable raw martingale on its transcript contradicts computable randomness of the source.

The startup segment before the first frontier is finite and is handled by the same finite Doob construction.

### 6. The rank-one overlap realization satisfies renewal

In the concrete P4-S036 realization, the transition which eventually closes (q_n) exposes only finitely many deciding blocks, while (q_{n+1}) is the carried next claim and remains virtually unqueried at the rolling boundary.

Its value is therefore a fresh fair coordinate relative to the virtual controller even though the raw evaluator already knows it. The next boundary normalized price averages to one over that coordinate and disappears in the previous backward step.

Hence the infinite symmetrized component normalizes despite having no finite packet partition. Corollary 7 is valid.

This establishes that finite packetizability is not necessary and that an infinite weak component is not itself the obstruction.

### 7. Bounded active width is not sufficient

The P4-S011 scan has one active sentinel epoch at a time. Its standard destroying martingale holds on filler coordinates and wagers only at the sentinel.

After zero-stake claims are discarded, there is therefore at most one active nonzero spoiled claim at a time after recoding. Its finite scan/simulation/frontier data are computable.

P4-S033 nevertheless gives a computably random raw source (X) on which the recoded virtual witness destroys computable randomness. Consequently no theorem using only bounded active width and finite computable frontier dimension can guarantee a raw compiler.

This validates the width-one negative boundary.

### 8. Uniform positivity and bounded local ratios are also insufficient

Replace the P4-S011 all-in sentinel wager by fractional stake (1/2) on the same predicted bit.

On the target every sentinel prediction is correct, so every completed epoch multiplies capital by (3/2). Infinitely many target epochs complete, hence this modified martingale still succeeds.

Before a trigger is visible, the local sentinel price vector is ((1,1)). When a prediction with sign (a) becomes visible, it is
[
(1+a/2,1-a/2),
]
up to coordinate order. Thus all entries lie between (1/2) and (3/2), and the ratio is at most (3).

The destructive source/map geometry is unchanged. Therefore uniform positivity and bounded price ratios do not repair the width-one obstruction. Proposition 8 is valid.

### 9. The P4-S011 obstruction is retirement, not value dependence

The wtt use bound gives a computable finite set of possible source-value dependencies for each sentinel computation. After that finite value frontier has been exposed, later fresh filler values do not alter the fixed computation represented by those answers.

But finite simulation need not decide that this fixed computation will never halt. The sentinel claim may remain open through arbitrarily many irrelevant filler queries before a halt becomes visible, or forever on a sibling continuation.

For the half-stake version, finite-horizon prices therefore remain ((1,1)) until the trigger is seen and then jump to a uniformly well-conditioned nontrivial vector. The missing datum is effective retirement/eventual stabilization, not price magnitude.

This is a claim-pricing obstruction specific to the actual P4-S011 mechanism, not merely the generic fact from P4-S036 that computable martingales can have noncomputable limits.

### 10. Cyclic dependence is excluded, but the coarse ray question is not forced by the committed witness

At the event level the P4-S011 scan never reuses a source coordinate and never reopens a retired sentinel claim. Successive epoch sentinels advance through fresh coordinates. Hence the temporal claim-dependency relation is acyclic and has no recurrent claim cycle.

Each individual sentinel has finite source-value dependence by the wtt use bound.

However the committed existence theorem supplies an abstract wtt autoreduction, not a complete classification of how all of its finite use sets align with the repeated three-bit block boundaries on sibling runs. Therefore the committed data do not justify asserting that the coarse block quotient must contain a directed infinite ray rather than overlapping finite closures.

P4-S037 does not need that undecided coarse classification: both the explicit directed ray and explicit no-ray overlap component normalize when renewal is effective, while the actual P4-S011 witness remains obstructed by non-effective retirement.

### 11. Effective limiting prices are a sufficient analytic hypothesis

If the absolute finite-horizon backward prices of the persistent-savings martingale converge with a total computable Cauchy modulus to computable limiting vectors satisfying the finite-step consistency equations, those limits are exactly computable conditional values.

Using them as terminal values in successive raw Doob steps produces one total computable nonnegative raw martingale.

Persistent savings is essential for the success transfer: after (K) thresholds have been locked, the terminal payoff on every continuation is at least (K), so every conditional limit is at least (K). The raw martingale is therefore unbounded.

This validates Theorem 9.

### 12. Separation guard

No proof that
[
Xin OH
]
is obtained. Hence there is no OH non-invariance theorem and no strict
[
R_2subsetneq OH
]
conclusion.

The retained comparison is
[
MLRsubseteq R_2subseteq OH^{iso}subseteq OHsubsetneq CR.
]

P4-S032 null-ambiguity preservation remains unchanged.

## Validation disposition

**PASS.**

P4-S037 proves a rolling finite-state/backward-price normalization theorem materially beyond finite packetization: both the P4-S035 infinite directed ray and the P4-S036 rank-one infinite overlap component normalize by fresh-frontier renewal. It also isolates the sharper negative boundary: bounded active width, finite state, positive prices and bounded ratios do not suffice because the recoded P4-S011 witness can keep one claim persistently open without an effective retirement/stabilization modulus.

The sustained equation (R_2=OH) remains unresolved.
