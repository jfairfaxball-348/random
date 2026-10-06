# P4-S021 — scale-tail effectivity versus shrinking-scale boundary attainment

Date: 2026-10-06
Session: P4-S021
Incoming checkpoint: baf6f7be7dfe30f475465d43e677235abee66518
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **A NATURAL TWO-SCALE LOCAL HYPOTHESIS DOES EFFECTIVIZE SET-THEORETIC LOSS-PROPERNESS WITHOUT RESTORING ABSOLUTE PREMIUM SUMMABILITY. IT IS ENOUGH TO HAVE COMPUTABLE WAITING BOUNDS FOR LOSSES AT LEAST 2^-n TOGETHER WITH A COMPUTABLE BOUND ON THE TOTAL CONTRIBUTION OF SMALLER LOSSES IN EACH BAD-CAPITAL TREE. HOWEVER THESE DATA DO NOT FORCE P4-S020'S EXACT LOSS-LEVEL WITNESS MODULUS OR DECIDABILITY OF Reach(K,m): HALTING INFORMATION CAN STILL BE ENCODED IN WHETHER A GEOMETRICALLY SHRINKING LOSS TAIL ATTAINS AN INTEGER BOUNDARY AT A FINITE HISTORY OR ONLY APPROACHES IT. P4-S011 VIOLATES THE SMALL-LOSS-TAIL CONDITION ON ITS COMPUTABLY RANDOM TARGET WHENEVER THE FULL-TICKET ACCOUNT IS GLOBALLY ADMISSIBLE.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint \`baf6f7be7dfe30f475465d43e677235abee66518\` exactly before substantive work. Repository search returned no committed P4-S021 record, so the session identifier was unused.

P4-S001 through P4-S020 and the required CAND-01 authority were read. P4-S005 through P4-S020 are treated as settled. In particular P4-S011's exact global-k=2 destroyer and P4-S015 through P4-S020 are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. This session stays strictly at k=2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained quantities and loss scales

Fix a globally admissible computable canonical full-ticket account in the settled sentinel-first completion. For a finite resolved ticket history v write

\[
E(v)=\sum_{i<|v|} e_i,
\]

where \(e_i\ge 0\) is the realized positive skipped-sentinel gain at ticket i, and let

\[
W^*(v)
\]

be the running maximum of ticket-account capital on resolved prefixes.

For integer \(K\ge 1\),

\[
B_K=\{v:W^*(v)<K\},
\qquad
b(K)=\sup\{E(v):v\in B_K\}.
\]

P4-S018/P4-S019 call the account loss-proper when \(b(K)<\infty\) for every K.

For \(n\ge 0\) put \(\delta_n=2^{-n}\). Split cumulative realized loss into

\[
E_{\ge n}(v)=\sum_{i<|v|,\ e_i\ge\delta_n} e_i,
\qquad
E_{<n}(v)=\sum_{i<|v|,\ 0<e_i<\delta_n} e_i.
\]

Then \(E=E_{\ge n}+E_{<n}\).

P4-S020 showed that merely bounding the waiting time to the next positive loss is too coarse because arbitrarily small heartbeat losses can carry no useful amount information. The question here is whether controlling a fixed positive scale and the tail below that scale is enough.

## 2. A local scale-tail hypothesis

### Definition — large-loss waiting modulus

A **large-loss waiting modulus** is a total computable function

\[
R(K,n)
\]

such that for every finite history \(v\in B_K\) and every infinite branch X through \(B_K\) extending v:

if X has any later ticket payout at least \(\delta_n\), then its first such later payout occurs within the next \(R(K,n)\) controller epochs.

This is a branchwise local condition. It says nothing about smaller losses and does not decide whether another large loss exists.

### Definition — computable subscale-tail bound

A **subscale-tail bound** is a total computable rational function

\[
T(K,n)<\infty
\]

such that for every finite \(v\in B_K\),

\[
E_{<n}(v)\le T(K,n).
\]

The positive theorem below only needs one computably chosen scale n for each K; requiring the data uniformly in all n is the natural scale-tail formulation. No convergence \(T(K,n)\to0\) is needed for that theorem.

This condition is not an absolute premium bound. It controls realized skipped-loss mass below a selected loss scale while ticket capital remains below K.

## 3. Large-scale reachability is effectively searchable

For rational \(q>0\), define

\[
\operatorname{ScaleReach}(K,n,q)
\iff
\exists v\in B_K\ [E_{\ge n}(v)\ge q].
\]

### Lemma 1 — scale waiting gives a computable witness depth for ScaleReach

Assume a large-loss waiting modulus R. If \(\operatorname{ScaleReach}(K,n,q)\) is true, then it has a witness by a computable depth depending only on \(K,n,q\).

Proof. Every term counted in \(E_{\ge n}\) is at least \(\delta_n\). A witness with total at least q can be shortened at the first crossing, which contains at most

\[
N=\lceil q/\delta_n\rceil=\lceil q2^n\rceil
\]

large-loss events. Along the finite branch leading to this first-crossing witness, after each prefix preceding the next such event there is a later \(\delta_n\)-large payout. The waiting modulus therefore places the next event within \(R(K,n)\) controller epochs.

Hence a witness exists within at most \(N R(K,n)\), up to the fixed computable finite epoch encoding overhead of the settled controller. Absorbing that overhead into a computable bound gives the result. ∎

### Corollary 2 — ScaleReach is decidable

Exhaustively search the finite completion tree through the bound from Lemma 1. If a node in \(B_K\) has \(E_{\ge n}\ge q\), answer yes; otherwise answer no.

The crucial point is that this decides **coarse-scale accumulated loss**, not the exact total-loss predicate Reach(K,m) from P4-S020.

## 4. Scale-tail data plus loss-properness implies effective loss-properness

### Theorem 3 — two-scale effectivization

Assume:

1. the full-ticket account is loss-proper, \(b(K)<\infty\) for every K;
2. a computable large-loss waiting modulus R is supplied;
3. a computable subscale-tail bound T is supplied.

Then the account is effectively loss-proper: one can compute a total rational \(U(K)\) with

\[
W^*(v)<K\Longrightarrow E(v)<U(K).
\]

Consequently the P4-S018 computable running-maximum coercivity modulus exists and the settled ticket/restart transfer applies.

Proof. Fix K and choose the single computable scale n=1; any other fixed computable choice works.

Because \(E_{\ge1}(v)\le E(v)\) and \(b(K)<\infty\), the large-scale quantity is uniformly bounded over \(B_K\). Search integers \(q=1,2,3,\ldots\). By Corollary 2, \(\operatorname{ScaleReach}(K,1,q)\) is decidable. Loss-properness guarantees that eventually the answer is no.

Let q be the first false instance. Then every \(v\in B_K\) satisfies

\[
E_{\ge1}(v)<q.
\]

By the subscale-tail bound,

\[
E_{<1}(v)\le T(K,1).
\]

Therefore

\[
E(v)<q+T(K,1).
\]

Return, for example,

\[
U(K)=q+T(K,1)+1.
\]

This is total computable and uniformly bounds bad-capital realized loss. P4-S019/P4-S018 then give a computable coercivity threshold. ∎

### What this theorem does and does not say

The theorem does **not** need to decide exact integer total-loss reachability. It first bounds the contribution from a fixed coarse loss scale by searchable large-loss events, then adds a computable bound for everything smaller.

Thus the scale-tail hypothesis gives a structural route to effective loss-properness that is genuinely different from simply postulating P4-S020's loss-bar searchability.

It is stronger in one direction and weaker in another:

- it imposes quantitative control on the entire subscale tail;
- it need not make \(\operatorname{Reach}(K,m)\) decidable for exact total-loss thresholds.

The latter separation is established below.

## 5. Absolute premium summability is still not restored

Reuse the settled P4-S017/P4-S018 one-sided-trigger example with H=1.

On its continuing positive branch,

\[
W^*(v)\ge \frac12+\frac12E(v).
\]

Hence every \(B_K\) has the explicit computable total-loss bound \(E(v)<2K\). In particular one may take

\[
T(K,n)=2K
\]

for every n.

The controller reaches each next one-sided trigger opportunity after a fixed finite number of filler/control epochs, so a computable \(R(K,n)\) exists.

Nevertheless the exact fair premiums on the all-trigger positive branch satisfy

\[
\sum_r\pi_r
=
\frac12\sum_r\frac1{r+1}
=
\infty.
\]

Therefore the scale-tail theorem does not restore P4-S016 absolute premium summability.

## 6. Strong scale-tail control does not imply P4-S020 witness searchability

The positive theorem computes U(K), but it would be stronger to conclude that every exact predicate

\[
\operatorname{Reach}(K,m)
\iff
\exists v\,[W^*(v)<K\ \&\ E(v)\ge m]
\]

is decidable, equivalently that a P4-S020 witness modulus D(K,m) exists.

That conclusion is false even under scale-tail data stronger than Theorem 3 needs.

### Construction — finite attainment versus geometric approach

Use only settled components: zero-stake consumed controls, P4-S017 one-sided-trigger productive stages, deterministic-trigger tickets, and the P4-S012 permission to scale rational stakes.

Keep a disjoint Mode A equal to the settled P4-S017 one-sided-trigger harmonic gadget. This preserves an infinite branch with divergent absolute premium sum.

Mode B builds a computable index ladder.

#### Index ladder

Starting with ticket reserve 1, a zero-stake consumed control either selects the current index e or asks to advance to e+1.

An advance block consists of finitely many favourable one-sided-trigger productive stages whose total realized skipped gain is exactly 2 and whose total ticket-account net gain is exactly 1. Such a finite block is computable: take positive rationally scaled favourable stakes, never exceeding the remaining target, and trim the final rational stake to hit the target exactly. The settled P4-S012 fractional-stake freedom gives the final trim; the one-sided ticket charges half its possible positive payout, so a favourable trigger contributes half that payout as net ticket capital.

If a nontrigger or unfavourable branch occurs, positive tickets stop as in the settled gadget.

After e successful advance blocks the selected-index branch has

\[
E=2e,\qquad W^*=1+e.
\]

#### Geometric machine tail

After selecting e, simulate \(\Phi_e\) one ordinary step at a time.

The remaining target loss is initially 2. If the machine has not halted by machine stage t, append a finite deterministic-trigger block whose total realized positive loss is

\[
2^{-t}
\]

and whose ticket-account net change is zero. Then simulate the next machine step.

Thus on a nonhalting machine the cumulative tail approaches 2 from below.

If a halt is detected before the next ordinary half-residual block, append instead one finite deterministic correction block whose total realized loss equals the entire remaining rational residual. Then stop positive tickets.

Every deterministic-trigger block is exactly fair with price equal to certain payout, so throughout the machine tail

\[
W^*=1+e.
\]

Each finite prescribed rational block can be implemented by finitely many scaled deterministic-trigger stages with each individual payout no larger than the block total and with the last stake trimmed rationally to make the sum exact.

The controller is computable because it only performs finite arithmetic, finite-state scheduling and step-by-step simulation of \(\Phi_e\).

### k=2 and admissibility checks

All zero-stake controls and deterministic-trigger stages consume their current sentinels. The only possible permanently nontriggering epoch is a settled one-sided-trigger stage in the index ladder or Mode A, whose nontrigger branch omits exactly its current sentinel and then exposes every other source coordinate.

Therefore the induced least-fresh scan remains everywhere total, no-repeat, fair-coin preserving and globally k=2 by the same settled scan argument used in P4-S017 through P4-S020.

Reserve 1 is globally sufficient:

- a successful one-sided index-ladder ticket increases capital by half its payout;
- a failed positive-cost one-sided ticket stops future positive premiums;
- deterministic-tail tickets have price exactly equal to their certain payout;
- zero-stake controls cost nothing.

Thus the canonical full-ticket account is globally admissible.

### Lemma 4 — exact total-loss reachability codes halting

Put

\[
K_e=e+2,\qquad m_e=2e+2.
\]

Then

\[
\operatorname{Reach}(K_e,m_e)
\quad\Longleftrightarrow\quad
\Phi_e\downarrow.
\]

Proof.

For the selected index e, ticket capital during the entire machine tail is \(1+e<K_e\).

If \(\Phi_e\) diverges, every finite tail prefix has cumulative tail loss strictly below 2, hence total E is strictly below \(2e+2=m_e\).

If \(\Phi_e\) halts, the correction block pays the exact remaining residual, producing a finite history with

\[
E=2e+2=m_e,\qquad W^*=1+e<K_e.
\]

No other mode creates a false witness.

- In Mode A, the settled linear relation \(W^*\ge 1+E/2\), after harmless reserve normalization, forces \(E<m_e\) whenever \(W^*<K_e\).
- Any earlier selected index j<e has total machine-tail loss at most \(2j+2\le 2e<m_e\).
- To pass from index e to e+1 in the ladder, the next successful advance block reaches total \(E=m_e\) exactly when ticket capital reaches \(e+2=K_e\). Because \(B_{K_e}\) requires the strict inequality \(W^*<K_e\), that boundary node and all later indices are excluded.

Therefore Reach(K_e,m_e) is true exactly when machine e halts. ∎

### Corollary 5 — no P4-S020 witness modulus exists

If a computable D(K,m) bounded a witness depth whenever Reach(K,m) were true, then Reach would be decidable by P4-S020's bounded search. Lemma 4 would decide the halting problem.

Hence this account has no loss-level witness modulus and exact Reach is not decidable.

The obstruction is not a long wait to the next positive event. It is **finite attainment versus limit approach at a loss boundary**.

## 7. The same construction has very strong scale-tail data

The preceding account is not a counterexample to Theorem 3. It is effectively loss-proper and has scale control much stronger than required.

### Lemma 6 — computable global deadlines for every fixed loss scale

Fix K and n.

Only finitely many index-ladder levels e can be entered while \(W^*<K\), because each successful advance block raises ticket capital by exactly 1. Mode A likewise has only computably many payouts of size at least \(2^{-n}\) below K.

In a selected machine tail, the prescribed block total at machine stage t is \(2^{-t}\), and every individual payout in that block is no larger than \(2^{-t}\). Therefore no machine-tail payout of size at least \(2^{-n}\) can occur after a computably bounded stage \(t>n+O(1)\).

For the finitely many relevant e and finitely many relevant block stages, the controller schedule and each finite block length are computable. Taking their maximum gives a computable global deadline

\[
G(K,n)
\]

after which no payout at least \(2^{-n}\) occurs anywhere in \(B_K\).

This is strictly stronger than a branchwise waiting modulus R.

### Lemma 7 — the small-scale tail has computable effective control

For fixed K, only finitely many index levels are possible below K. The machine-tail block totals form a geometric series with computable remainder.

Given a rational \(\varepsilon>0\), choose a computable machine stage t so that the remaining geometric mass is below \(\varepsilon/2\). Before that stage there are only finitely many positive rational payouts in the finitely many relevant controller blocks. Compute their positive minimum \(\eta\) (ignoring zero payouts), and choose n with \(2^{-n}<\eta\).

Then every sub-\(2^{-n}\) contribution from the finite initial part is zero, while the entire later machine tail contributes less than \(\varepsilon/2\). The Mode-A and finite-ladder pieces below K have computable total-loss bounds and their payout scales decrease effectively, so the same finite search supplies their tail contribution.

Hence one can compute a bound \(T(K,n)\) for \(E_{<n}\), uniformly in K,n, with an effective modulus witnessing

\[
T(K,n)\longrightarrow 0
\]

as \(n\to\infty\).

In particular the weaker finite subscale-tail condition of Theorem 3 holds.

### Consequence

Even **global scale deadlines plus an effectively vanishing small-loss tail** do not imply P4-S020's exact witness modulus.

Halting information can survive only in the question whether a computable shrinking tail reaches its limiting boundary at a finite stage.

This is the sharp remaining scale obstruction isolated by P4-S021.

## 8. Effective loss-properness of the boundary construction

The construction has an explicit computable bad-capital loss bound.

Below capital K, at most \(K-1\) successful index advances can occur, contributing at most \(2(K-1)\) loss, and a selected machine tail contributes at most 2 more. Mode A already has a computable linear loss/capital bound.

Thus, after harmless rounding, one may take a computable linear U(K), for example

\[
U(K)=2K+4.
\]

So the account is not another P4-S019 non-effectivity counterexample. Its purpose is narrower: it separates **effective loss-properness** from **decidable exact loss-level reachability**.

This matches P4-S020's explicit warning that a witness modulus is sufficient but not necessary for effective loss-properness.

## 9. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source and d its successful all-trigger output martingale. Fix any computable horizon selector H and suppose a finite reserve makes the associated canonical full-ticket account globally admissible.

P4-S016 proves that on the sentinel-first completion C(Y),

\[
\sum_i e_i=\infty.
\]

Because C is a computable fair-coin effective isomorphism and Y is computably random, C(Y) is computably random. A globally admissible full-ticket account is a total nonnegative computable martingale, so its running capital is bounded on C(Y). Choose an integer K above that bound. Then every finite prefix of C(Y) lies in \(B_K\).

For P4-S011's all-in correct-prediction stream, after r correct sentinel wins the P4-S015 savings wrapper has r units of saved capital and one active-risk unit. The positive multiplicative skipped gain of the next correct sentinel is therefore

\[
\frac1{r+1}.
\]

The subsequence contributed by horizon-missed epochs still has divergent sum by P4-S016.

Fix n. Since \(1/(r+1)\to0\), all sufficiently late terms of that divergent subseries are strictly below \(2^{-n}\). Therefore

\[
E_{<n}(C(Y)\upharpoonright s)
\]

is unbounded as s grows through prefixes in \(B_K\).

Hence no finite subscale-tail bound \(T(K,n)\) can exist — indeed it fails for every n.

So P4-S011 violates the P4-S021 scale-tail hypothesis more strongly than merely failing set-theoretic loss-properness. This is conditional only on global admissibility, exactly as in P4-S019/P4-S020; bare admissibility itself remains unruled-out.

## 10. Exact boundary after P4-S021

P4-S021 establishes two distinct facts.

### Positive effectivization boundary

A computable large-loss waiting modulus plus a computable bound on all smaller realized loss inside each bad-capital tree turns set-theoretic loss-properness into effective loss-properness. This uses only coarse-scale reachability and does not restore absolute premium summability.

### Negative searchability boundary

Those scale-tail data do **not** force P4-S020's stronger searchable-loss-level property. Exact Reach(K,m) may remain undecidable because computable shrinking increments can approach m from below on a nonhalting branch and hit m exactly only when a machine halts.

The missing datum is therefore no longer control of loss frequency or loss mass. It is an **anti-Zeno / boundary-isolation effectivity condition** separating finite attainment of a target loss level from arbitrarily close approach by smaller-scale tails.

## 11. Successes and limits

Successful:

1. Identified a local two-scale structural hypothesis weaker than explicit loss-bar searchability that suffices, with loss-properness, for effective loss-properness.
2. Proved coarse-scale accumulated-loss reachability decidable from a large-loss waiting modulus.
3. Combined that coarse bound with a computable subscale-tail bound to compute U(K).
4. Kept divergent absolute premium sums in the settled harmonic example.
5. Built an exact computable globally k=2, globally admissible shrinking-scale construction with strong global scale deadlines and effectively vanishing small-loss tails.
6. Proved exact Reach(K_e,m_e) in that construction is equivalent to machine-e halting.
7. Therefore separated effective loss-properness and strong scale-tail control from P4-S020's exact witness modulus.
8. Checked P4-S011 explicitly: under global admissibility, its computably random target has divergent loss entirely in arbitrarily small scales, so every finite subscale-tail certificate fails.

Not claimed:

1. No anti-Zeno condition is proved necessary or sufficient here.
2. No necessity theorem is claimed for martingale-transfer architectures outside the settled full-ticket plus restart decomposition.
3. The shrinking-scale account is a boundary example, not a new randomness-destruction witness.
4. No settled P4-S005 through P4-S020 result is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S005 through P4-S020 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015's weighted theorem, P4-S016's envelope-free last-chance theorem, P4-S017's coercive self-financing theorem, P4-S018's running-maximum modulus boundary, P4-S019's finite/noncomputable loss-properness boundary and P4-S020's searchable-loss-level theorem are unchanged.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

## Next bounded question

The scale-tail gap is now narrower. A bounded P4-S022 should stay strictly at k=2 and test only an **anti-Zeno / boundary-isolation** condition weaker than an explicit P4-S020 witness modulus: for example, a computable modulus ensuring that once all losses at scale at least \(2^{-n}\) have been exhausted, the remaining smaller-loss tail is either provably too small to reach a queried integer level m or is forced to cross it within a computable finite search. Determine whether such local boundary separation makes exact Reach(K,m) decidable, or whether halting information can survive another level of shrinking-scale coding. Check P4-S011 explicitly.
