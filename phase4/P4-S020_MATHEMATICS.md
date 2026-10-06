# P4-S020 — zero-loss waiting versus searchable loss levels

Date: 2026-10-06
Session: P4-S020
Incoming checkpoint: 4beb36e69158e9badccb2a80a6292772c11c8ed4
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **A COMPUTABLE BOUND ON ZERO-LOSS WAITING, EVEN A FIXED CONSTANT BOUND ALONG EVERY BAD-CAPITAL BRANCH THAT WILL EVER REALIZE MORE POSITIVE LOSS, DOES NOT EFFECTIVIZE SET-THEORETIC LOSS-PROPERNESS. THE P4-S019 HALTING-TIME EXCURSION CAN BE HEARTBEATIZED BY SUMMABLY SMALL DETERMINISTIC LOSS TICKETS, SO POSITIVE LOSS KEEPS OCCURRING WHILE THE MACHINE IS SIMULATED, YET EVERY b(K) IS FINITE AND NO COMPUTABLE UNIFORM MAJORANT EXISTS. THE MISSING EFFECTIVITY IS LOSS-SCALE REACHABILITY, NOT EVENT REACHABILITY. A COMPUTABLE LOSS-LEVEL WITNESS MODULUS D(K,m), BOUNDING THE DEPTH OF SOME BAD-CAPITAL HISTORY WITH E>=m WHEN ONE EXISTS, MAKES LOSS BARS EFFECTIVELY SEARCHABLE; TOGETHER WITH LOSS-PROPERNESS IT COMPUTES A UNIFORM U(K) AND HENCE THE P4-S018 COERCIVITY MODULUS. THIS SEARCHABILITY DOES NOT RESTORE ABSOLUTE PREMIUM SUMMABILITY. P4-S011 REMAINS EXCLUDED ALREADY AT LOSS-PROPERNESS.**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work. Commit search returned no P4-S020 record, so the session identifier was unused.

P4-S001 through P4-S019 and the required CAND-01 authority were read. P4-S005 through P4-S019 are treated as settled. In particular P4-S011's exact global-k=2 destroyer, P4-S015's weighted theorem, P4-S016's envelope-free last-chance theorem, P4-S017's coercive self-financing theorem, P4-S018's effective-coercivity/loss-properness boundary, and P4-S019's finite-but-noncomputably-bounded loss-proper account are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. Nothing below concerns k>2, novelty, Gate 4, publication or outreach.

## 1. Retained quantities

Fix a globally admissible computable full-ticket account in the settled sentinel-first completion. For finite resolved history v write

E(v) = cumulative realized positive skipped gain,

W*(v) = maximum ticket-account capital attained on a resolved prefix.

For integer K>=1 put

B_K = {v : W*(v)<K}

and

b(K) = sup {E(v) : v in B_K}.

Loss-properness is b(K)<infinity for every K. P4-S019 proved that b is uniformly lower semicomputable but need not have any computable majorant.

The P4-S019 obstruction used arbitrarily long zero-loss machine waiting. The first question is whether forbidding that particular shape is enough.

## 2. Event-level zero-loss waiting is not enough

Use any fixed computable epoch coding of completion histories. Say an admissible account has a **zero-loss waiting modulus** when there is a total computable z(K) such that on every branch X through B_K and every prefix v of X:

if E increases at some later prefix of X while the branch remains in B_K, then E already increases within the next z(K) controller epochs.

This is deliberately strong: it is branchwise, not merely existential over sibling continuations.

### Theorem 1 — bounded zero-loss gaps do not effectivize loss-properness

There is a computable globally k=2, globally admissible ticket stream which is loss-proper, has a fixed zero-loss waiting bound, retains a branch with divergent absolute premium sum, and nevertheless has no computable uniform majorant of b(K).

### Construction — heartbeatize P4-S019

Start from the exact P4-S019 Mode-A / Mode-B construction.

Leave Mode A unchanged. It already retains the settled one-sided-trigger harmonic branch with divergent absolute premium sum.

In Mode B, replace every original zero-stake control or one-step machine-wait epoch by a short block:

1. run one scaled deterministic-trigger heartbeat at a fresh sentinel;
2. then perform the original control action or one simulation step of Phi_e.

At heartbeat number s choose, from the computable finite state, a positive rational fractional stake small enough that on the favourable sentinel the resulting savings-wrapped positive skipped gain epsilon_s satisfies

0 < epsilon_s <= 2^(-s-3).

The P4-S012 rational-stake freedom and the settled P4-S017 deterministic-trigger gadget give such a scaled ticket. On the favourable stored sentinel both fresh-filler children trigger, so its exact fair premium equals its certain payout epsilon_s and the ticket account capital is unchanged. On the unfavourable stored sentinel declare the controller permanently inactive for positive tickets and consume all later sentinels with zero stake.

Hence any branch which will ever realize another positive skipped gain cannot take an unfavourable heartbeat. Along every such continuing branch the next heartbeat is favourable and E increases after at most the fixed heartbeat/control block length. Thus one may take a constant zero-loss waiting bound.

The total heartbeat contribution on any continuing branch is bounded by

sum_s epsilon_s <= 1/4.

Therefore a nonhalting machine branch still has finite total E. If Phi_e halts after t steps, the original finite deterministic post-halt burst is then run. The summably small heartbeat perturbation leaves the active savings risk in a computable positive interval and changes only fixed computable constants. The t-stage all-winning burst still has a computable effectively divergent harmonic lower bound in t. Concretely, for each chosen e there is a computable c_e>0 such that the post-halt burst contributes at least

c_e * sum_{j<t} 1/(e+j+1).

This lower bound diverges effectively with t.

All heartbeat and control sentinels are consumed. The only possible permanently omitted coordinate remains the current sentinel of a settled one-sided nontrigger epoch. Therefore the induced scan remains everywhere total, no-repeat, fair-coin preserving and globally k=2.

### Loss-properness survives

Fix K. As in P4-S019, only finitely many machine indices e can reach their waiting phase while W*<K. For a divergent Phi_e, its heartbeat contribution is at most 1/4 after the finite ladder. For a halting Phi_e, the heartbeat contribution plus the finite post-halt burst is finite.

Thus b(K)<infinity for every K.

### No computable majorant survives

Suppose U(K) computably majorized b(K). For a fixed e choose the same computable integer K_e above the post-ladder ticket capital.

If Phi_e halts after t steps, the all-favourable heartbeat/all-positive burst branch remains below K_e and has

E >= c_e * sum_{j<t} 1/(e+j+1)

up to an irrelevant fixed nonnegative prefix contribution.

From e and U(K_e), effective divergence of the displayed harmonic lower bound computes T such that a halt at t>=T would force E>U(K_e), impossible. Simulating Phi_e for T steps would decide halting.

Therefore no computable uniform majorant exists.

### Consequence

The P4-S019 nonuniformity is not fundamentally "nothing happens for a long time". Halting information can be hidden behind a computable stream of arbitrarily small positive losses whose total remains bounded on nonhalting branches. What matters is **how quickly a prescribed amount of loss can become reachable**, not how quickly the next positive loss occurs.

## 3. Amount-sensitive local progress is sufficient

The failed event-level condition suggests the correct strengthening.

### Definition — branchwise amount-sensitive progress modulus

A bad-capital tree has an amount-sensitive progress modulus if there is a total computable function R such that, for every K, every finite v in B_K and every positive rational q, on every branch X through B_K extending v:

if some later prefix w of X satisfies

E(w) >= E(v)+q,

then such a prefix occurs within R(K,v,q) further controller epochs.

This is stronger than needed, because it controls every branch separately. It is nevertheless a clean local sufficient condition.

Taking v to be the root and q=m gives a computable depth by which every branch that can accumulate m loss must do so. The next section isolates the strictly weaker root-level condition actually used.

## 4. Searchable loss-level witnesses

### Definition — loss-level witness modulus

A computable loss-level witness modulus is a total computable D(K,m), for integers K,m>=1, such that

if there exists v in B_K with E(v)>=m,

then there exists such a v of controller-epoch depth at most D(K,m).

D does not bound all branches. It only says that whenever the bad-capital tree reaches loss level m somewhere, one witness appears within a computably bounded finite search.

The amount-sensitive progress modulus implies a witness modulus by applying it at the root.

### Lemma 2 — a witness modulus decides loss-level reachability

For fixed K,m, exhaustively compute the finite bad-capital tree through depth D(K,m).

- If some node has E>=m, then the loss level is reachable.
- If none does, the defining property of D says no later witness exists.

Thus

Reach(K,m) := exists v in B_K with E(v)>=m

is decidable uniformly in K,m, and the loss-bar predicate

Bar(K,m) := every v in B_K has E(v)<m

is decidable as its complement.

### Theorem 3 — searchable loss levels plus loss-properness imply effective loss-properness

Assume b(K)<infinity for every K and a computable witness modulus D.

For fixed K, search m=1,2,3,... . For each m decide Reach(K,m) by Lemma 2. Loss-properness guarantees that eventually some integer m satisfies Bar(K,m).

Return the first such m as U(K).

Then U is total computable and

W*(v)<K implies E(v)<U(K)

for every finite v.

Hence the account is effectively loss-proper. By P4-S019/P4-S018, h(K)=U(K)+1 is a computable running-maximum coercivity modulus, so the settled ticket-plus-restart transfer theorem applies.

## 5. Exact searchability formulation

Because Reach(K,m) already has c.e. positive witnesses from the computable finite tree, the following are equivalent:

1. a computable loss-level witness modulus D(K,m);
2. uniform decidability of Reach(K,m);
3. uniform positive semidecidability of every true Bar(K,m).

For 3=>2, dovetail the ordinary search for a violating finite history with the positive Bar certificate. Exactly one side eventually appears. Once Reach is decided true, enumerate until a witness appears and take its depth; if false, output any default depth. This computes D.

This is the clean effectively searchable loss-bar condition.

A weaker "cofinal certificate" relation is enough for Theorem 3: it suffices to have a c.e. sound relation Cert(K,m) with Cert(K,m) implying Bar(K,m), and with at least one certified m for every K. Searching the enumeration computes a majorant U directly. Conversely a computable U gives such certificates by certifying every m>U(K). Thus that weakest certificate form is equivalent in strength to effective loss-properness itself and is not a new structural explanation.

The witness-modulus / decidable-Reach form is stronger, but it is a genuine structural searchability condition rather than merely supplying U under another name.

## 6. The witness condition is weaker than branchwise progress

A witness modulus only asks for one prompt witness when a loss level is reachable. It does not constrain how long other branches may wait.

A settled-gadget separation is immediate. Use a zero-stake control to split into:

- a fast branch which realizes one deterministic positive loss immediately and then stops positive tickets;
- slow branches indexed by a unary delay N which wait N zero-stake consumed-sentinel epochs before realizing the same one deterministic loss and then stop.

The reachable loss levels have a fixed short witness on the fast branch, so D is computable. But no uniform branchwise waiting/progress bound can control the slow branches as N grows.

The construction uses only consumed controls and deterministic-trigger epochs and therefore stays within the global-k=2 least-fresh architecture. A disjoint Mode-A one-sided-trigger component may be added to retain divergent harmonic absolute premiums.

So the root-level searchability condition is strictly weaker than an all-branch amount-sensitive progress modulus.

## 7. Absolute premium summability is still not restored

Reuse the settled P4-S017/P4-S018 one-sided-trigger H=1 account. On its continuing positive branch,

W*(v) >= 1/2 + E(v)/2,

so b(K) has an explicit computable linear bound.

Moreover, for any integer loss level m which is reachable below K, a finite all-positive witness is found by computably searching the harmonic partial sums. Hence this example has a computable loss-level witness modulus.

Nevertheless along the all-trigger positive branch

sum pi_r = (1/2) sum_r 1/(r+1) = infinity.

Therefore searchable loss levels do not collapse back to the P4-S016 absolute premium-summability hypothesis.

## 8. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source, H any total computable horizon selector, and J a canonical full-ticket account.

P4-S019 already proves the stronger fact needed here: if a finite reserve makes J globally admissible, then J cannot be set-theoretically loss-proper. Otherwise the divergent realized skipped gain on the sentinel-first completion C(Y) would force W* unbounded, making J a total nonnegative computable martingale succeeding on the computably random completion.

Therefore P4-S011 cannot satisfy the hypotheses of Theorem 3. It fails before loss-level searchability matters: for some K, b(K)=infinity.

Bare admissibility alone remains unruled-out exactly as in P4-S019.

## 9. Successes and limits

Successes:

1. Tested the proposed zero-loss-waiting route and showed it is insufficient, even with a fixed branchwise waiting bound.
2. Isolated the sharper obstruction: halting-time information can be carried across loss scales by summably small heartbeat losses.
3. Identified an amount-sensitive local progress modulus that is sufficient.
4. Isolated the weaker root-level condition actually used: a computable witness depth for reachable bad-capital loss levels.
5. Proved that this makes loss bars decidable and, with loss-properness, computes a uniform U(K).
6. Characterized full loss-bar searchability equivalently by decidable loss-level reachability.
7. Showed the searchability condition remains compatible with divergent absolute premium sums.
8. Preserved the stronger P4-S011 exclusion from set-theoretic loss-properness.

Limits:

1. No claim is made that the witness-modulus condition is necessary for effective loss-properness; a computable majorant U can exist even when lower loss levels are not decidable.
2. No universal necessity theorem is claimed outside the settled full-ticket plus restart architecture.
3. No new randomness-destruction witness is claimed.
4. Bare admissibility for P4-S011 remains unruled-out.

## Preserved boundaries

P4-S005 through P4-S019 remain settled.

P4-S011's exact k=2 destroyer is unchanged.

P4-S015's weighted theorem, P4-S016's envelope-free last-chance theorem, P4-S017's coercive self-financing theorem, P4-S018's running-maximum modulus boundary and P4-S019's finite/noncomputable loss-properness boundary are unchanged.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

## Next bounded question

The heartbeat counterexample shows that event frequency is too coarse; the relevant issue is loss scale.

A bounded P4-S021 should test whether the loss-level witness modulus can be forced by a more local two-scale hypothesis which does not simply restate bar searchability: for example, a computable waiting bound for losses of size at least 2^-n together with a computable bound on the cumulative contribution of smaller losses while W*<K. Determine whether such scale-tail data imply searchable loss levels, or whether halting information can still move across infinitely many shrinking scales. Check P4-S011 explicitly and remain strictly at k=2.
