# P4-S016 — incremental last-chance loss tickets

Date: 2026-10-06
Session: P4-S016
Incoming checkpoint: 66b77cf8fcb5c6c5feafeb54cd9ce003e2d9342c
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh stake subclass only

Result: **THE ADVANCE COMPUTABLE FUTURE-LOSS ENVELOPE OF P4-S015 CAN BE ELIMINATED UNDER A DIFFERENT EFFECTIVE BUDGET. AFTER A HORIZON MISS, THE EXACT POSITIVE LOSS THAT WOULD BE SKIPPED IF THE NEXT FRESH FILLER MAKES THE SENTINEL TRIGGER IS FINITELY COMPUTABLE BEFORE THAT FILLER IS DRAWN. BUYING THIS ONE-STEP LAST-CHANCE LOSS TICKET AT ITS EXACT FAIR PRICE AT EVERY UNRESOLVED POSTMISS NODE YIELDS ONE TRANSFER MARTINGALE WHEN THOSE AUTOMATIC FAIR PRICES HAVE ONE FINITE COMPUTABLE UNIFORM PATHWISE SUM BUDGET. NO FUTURE SUPREMUM, INFINITE OPTIONAL PROJECTION OR COMPUTABLE LOSS ENVELOPE IS USED. P4-S011 VIOLATES THE CONDITION ALREADY ON ITS COMPUTABLY RANDOM TARGET PATH.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work. The P4-S016 mathematics, close and validation records were absent on that checkpoint and repository search returned no committed P4-S016 record, so the session identifier was unused.

P4-S001 through P4-S015 and required CAND-01 authority were read. P4-S005 through P4-S015 are treated as settled. In particular:

- P4-S011's exact global-k=2 destroyer is preserved;
- P4-S012's target-winning self-avoiding stake boundary is preserved;
- P4-S013's reachable-sentinel-totality / finite-deadline theorem is preserved;
- P4-S014's computably budgeted raw-tail transfer is preserved;
- P4-S015's weighted theorem is preserved, including its savings wrapper and its proof that the pointwise minimal future-loss envelope need not be uniformly computable.

This session changes only the extra effectivity datum used after a P4-S014 horizon miss. It does not reopen crossing-measure, canonical-sheet, one-hole/coalescence, persistent-hole or capped-projection routes.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

## 1. Retained P4-S015 loss quantity

Fix the P4-S012/P4-S015 least-fresh scan and a nonnegative rational-valued computable output martingale d. Apply the settled P4-S015 savings wrapper and write q=Save(d).

If q(tau)>0, its signed fractional stake at logical transcript tau is

theta_q(tau) = (q(tau1)-q(tau0))/(2q(tau)).

For sentinel bit b, the positive multiplicative gain lost by skipping that logical sentinel wager is

ell_q(tau,b)
 = max(0, q(taub)/q(tau)-1)
 = max(0, theta_q(tau)(2b-1)),

with ell_q=0 when q(tau)=0. Thus 0<=ell_q<=1.

P4-S015 required, already at the finite horizon miss leaf, a computable rational majorant of every possible later ell_q. The exact least such future supremum need not be computable.

P4-S016 does not try to compute that supremum.

## 2. The postmiss last-chance loss is computable one step before it matters

Use the same globally exhaustive sentinel-first completion C as P4-S014/P4-S015. At each epoch, C physically queries the sentinel first and stores its bit b, while the logical least-fresh scan keeps that sentinel withheld.

Choose any total computable finite horizon H(s) at each reachable epoch state s and run the settled finite-horizon hedge through H(s). A horizon miss below means that after the H(s) fillers the epoch is still unresolved and its next logical query is another fresh filler. If the H-th filler makes the logical sentinel query become visible, that branch is counted as a good finite-horizon branch.

Fix an unresolved postmiss completion state v. The finite state determines the stored sentinel bit b, the current logical transcript tau_v, the next fresh filler coordinate k, and the fact that the logical next query is k rather than the sentinel.

Before physically querying k, consider each possible filler answer a in {0,1}. Simulate the total computable next-query procedure one further logical step using a.

If after appending a the next logical query is the sentinel, let tau_{v,a} be the resulting pre-sentinel transcript and put

L_v(a) = ell_q(tau_{v,a},b).

If the epoch remains unresolved after that filler, put L_v(a)=0.

### Lemma 1 — exact next-step loss and price are computable

Both L_v(0) and L_v(1) are computable rationals uniformly from v. Hence so is

pi(v) = (L_v(0)+L_v(1))/2.

Before the next fresh filler is drawn, buy a one-step ticket T_v whose child payoff on answer a is L_v(a). The fair martingale price of this ticket is exactly pi(v).

Proof. The least-fresh next-query function is total computable on finite transcripts. Thus for each hypothetical child a we can decide by finite computation whether that child makes the sentinel the next logical query. In the trigger case the finite pre-sentinel transcript is known, and q is a computable rational martingale, so ell_q is computable exactly.

The physical next filler is a fresh fair source bit. Therefore the unique fair price of the two-child payoff vector (L_v(0),L_v(1)) is its average. QED.

This is the crucial elimination of the P4-S015 envelope. No future trigger probability, future supremum or limit is computed. Insurance is bought only at the last fair moment, while one fresh filler bit remains unresolved.

## 3. Incremental premium budget

For a fixed computable horizon selector H, let V_H(x) be the sequence of all unresolved postmiss states v actually visited by the sentinel-first completion on source x, over all epochs. A state appears only after that epoch has missed its chosen horizon and before it later triggers or continues forever.

### Definition — computably budgeted incremental last-chance premiums

The pair (scan,q) has a computably budgeted incremental loss certificate for H if there is a computable rational B<infinity such that for every source run x,

sum_{v in V_H(x)} pi(v) <= B.

The local prices pi(v) require no certificate data: they are automatically computable from the finite scan state and q. The only extra hypothesis is the supplied finite uniform pathwise bound B.

This is the weakest condition established here for the exact one-step ticket construction. The word weakest is local to this architecture: at node v, any nonnegative one-step fair hedge whose two child payoffs dominate L_v(0),L_v(1) must start with capital at least pi(v), by the martingale equation. No absolute necessity claim is made across all possible multi-step transfer constructions.

## 4. The incremental insurance martingale

Start an insurance account J with reserve B.

Whenever an unresolved postmiss state v is reached, spend pi(v) units of reserve on T_v. Keep every resolved ticket payoff as cash. If the next filler does not trigger the sentinel, that ticket pays zero and the construction continues to the next unresolved state. If it does trigger, the ticket pays the exact positive skipped-gain loss ell_q at that sentinel.

### Lemma 2 — J is a total computable fair martingale

The pathwise premium budget prevents overdraft on every run. Every ticket is a finite one-step fair martingale and all unused reserve/cash is held constant. Hence J is a total nonnegative computable martingale on the completion stream.

After any finite set of resolved tickets,

J >= B - sum pi(v) + sum ell_r,

where ell_r ranges over the positive skipped gains of horizon-missed epochs that have subsequently triggered.

Consequently, if the realized skipped-gain sum diverges, J is unbounded.

No independence between epochs is used.

## 5. The restart hedge needs only the realized loss sum

Construct D exactly as in P4-S015 against q, except that no advance w-envelope is supplied.

- On an epoch triggering by H(s), the finite conditional-expectation hedge tracks the current positive scale of q exactly through sentinel consumption.
- After a horizon miss, D copies q on every later fresh filler.
- If that epoch never triggers, D copies q forever.
- If it later triggers, D skips the already-physically-revealed sentinel update and restarts at the next epoch.
- If q is zero at a restart state, freeze D on that branch as in P4-S015; such a branch cannot be one on which d succeeds.

Suppose a missed epoch later triggers at pre-sentinel transcript tau with actual bit b. Let

g = q(taub)/q(tau).

If g<=1, skipping the logical sentinel cannot decrease the scale of D relative to q. If g>1, then g=1+ell_q(tau,b), so the scale loses exactly the factor 1/(1+ell_q(tau,b)).

### Lemma 3 — finite realized skipped gain is harmless

If sum_r ell_r < infinity, then the restart scale remains bounded below by a positive constant:

product_r (1+ell_r)^(-1) >= exp(-sum_r ell_r) > 0.

Because q=Save(d) tends to infinity along all sufficiently late prefixes whenever d is unbounded, D succeeds on every d-success path with finite realized skipped-gain sum.

If a horizon-missed epoch never triggers, D copies q forever from its horizon onward and also succeeds whenever d does.

## 6. One-martingale transfer without an advance envelope

### Theorem 4 — incremental last-chance premium theorem

Fix d and q=Save(d). Suppose there are a total computable horizon selector H and a computable rational B which uniformly bounds the pathwise sum of the automatic last-chance fair prices pi(v) over all unresolved postmiss states.

Then there is one total computable source martingale which succeeds on every source x for which d succeeds on the logical least-fresh output.

Proof. On the sentinel-first completion take M=J+D.

If the realized skipped-gain sum diverges, J succeeds by Lemma 2.

If the realized skipped-gain sum is finite and d succeeds, D succeeds by Lemma 3.

If a missed epoch never triggers, D copies q forever after its horizon.

Thus M succeeds whenever d does.

The completion C is the settled P4-S014/P4-S015 everywhere-total computable adaptive permutation, hence a fair-coin effective isomorphism. P4-S001 transfers M to one computable martingale on the original source. QED.

The theorem computes no infinite optional projection.

## 7. What exactly has been eliminated?

P4-S015 needed a computable miss-leaf value w(s,b,rho) already at the horizon, majorizing every later positive sentinel gain. P4-S016 needs no such future majorant.

After the horizon miss, it waits. At each still-unresolved finite state it asks only a decidable one-step question: if the next fresh filler is 0 or 1, does that make the sentinel trigger, and if so what is q's exact positive sentinel gain? The corresponding ticket is bought immediately before that filler.

Thus the noncomputable pointwise future supremum from P4-S015 never appears.

The price is a different budget hypothesis. P4-S015 charges an ex-ante finite fair price at the horizon using an advance envelope, while P4-S016 charges conditional one-step premiums along the realized postmiss continuation. These certificate notions are not claimed to be ordered. In particular, a very rare horizon miss may be cheap ex ante for P4-S015 while the conditional premium sum along an exceptional infinite avoiding continuation can be large. P4-S016 is therefore an effectivity weakening — removal of the future envelope — not a claimed strict weakening of the complete P4-S015 numerical hypothesis.

## 8. Sharp local minimality of the premium

At an unresolved postmiss state v, suppose an alternative one-step nonnegative fair ticket has child payouts P_0,P_1 with P_a>=L_v(a) for a=0,1.

Its current price must be

(P_0+P_1)/2 >= (L_v(0)+L_v(1))/2 = pi(v).

Therefore pi(v) is the exact least fair capital needed at that node by any one-step ticket which fully covers the possible next-step skipped gain.

This identifies the sharp local incremental cost. It does not show that a more global multi-step hedge cannot share capital more efficiently across nodes.

## 9. Explicit check of P4-S011

Let Y be the settled P4-S011 computably random source and d its successful all-trigger output martingale. Fix any total computable horizon selector H and form q=Save(d).

Every epoch on Y eventually triggers. Consider the P4-S015/P4-S016 restart hedge D with no insurance.

If the sum of the positive skipped gains ell_r over horizon-missed epochs on Y were finite, Lemma 3 would make D succeed on the sentinel-first completion of Y. That completion is a computable fair-coin effective isomorphism, so P4-S001 would yield a computable source martingale succeeding on Y, contradicting P4-S011.

Hence for every total computable H,

sum_r ell_r = infinity

along Y, where the sum ranges over the horizon-missed epochs.

For each such missed epoch, look at the final unresolved postmiss state v immediately before the fresh filler whose actual answer makes the sentinel trigger. If the actual answer is a, then L_v(a)=ell_r. Since the other child loss is nonnegative,

pi(v) = (L_v(0)+L_v(1))/2 >= ell_r/2.

Therefore sum_{v in V_H(Y)} pi(v) = infinity.

So P4-S011 violates the P4-S016 premium condition on the computably random target path itself, not merely somewhere among sibling runs. In particular, no finite uniform pathwise premium budget can exist for P4-S011 for any computable horizon selector.

This argument does not need to assert that the savings-wrapped stake remains all-in.

## 10. Relation to the requested larger-visible-stakes formulation

One could try to enumerate a growing approximation to the P4-S015 future supremum and buy tickets whenever the approximation increases. That is unnecessary.

The last-chance construction is more local: a loss is insured only once a concrete one-step trigger branch and its exact gain are finitely visible, but still before the fresh filler selecting that branch is known. The fair premium is then exact and computable.

This avoids both the noncomputable future supremum and any need to decide whether a larger stake will ever appear farther out.

## 11. Successes and limits

Successful:

1. The advance computable future-loss envelope from P4-S015 is removed.
2. Exact one-step skipped-gain payoffs are uniformly computable at every unresolved postmiss state.
3. Their exact fair prices are automatic computable rationals.
4. A finite computable uniform pathwise budget on the sum of those prices funds one total incremental insurance martingale.
5. Divergent realized skipped gain is caught by insurance; finite realized skipped gain leaves the restart hedge at positive scale.
6. Their sum gives one completion martingale, and P4-S001 gives one source martingale.
7. No infinite optional projection, future-loss supremum or convergence modulus is computed.
8. The local fair premium is minimal among one-step tickets covering both next-bit losses.
9. P4-S011 necessarily has divergent incremental premium sum on its target Y for every computable horizon selector.

Not claimed:

1. The P4-S016 premium condition is not claimed numerically weaker than every P4-S015 certificate; the two budget placements can be incomparable.
2. No absolute necessity theorem is claimed for all martingale transfers.
3. No self-financing scheme with unbounded total premiums is established.
4. No settled P4-S005 through P4-S015 route is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S011's exact k=2 destroyer is unchanged.
P4-S012's stake-level structural boundary is unchanged.
P4-S013's reachable-sentinel-totality / finite-deadline theorem is unchanged.
P4-S014's computably budgeted raw-tail theorem is unchanged.
P4-S015's weighted advance-envelope theorem is unchanged.
PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
DEF-0020 is unchanged.

## Next bounded question

The remaining extra datum in P4-S016 is no longer a future-loss envelope; it is the finite uniform absolute budget B on cumulative last-chance fair premiums.

The smallest next question is whether this absolute premium-sum budget can be weakened to a computable self-financing reserve condition, allowing later premiums to be paid from earlier ticket winnings while keeping one nonnegative total martingale, and whether P4-S011 necessarily defeats every such reserve condition.
