# P4-S019 — finite loss-properness versus effective loss bars

Date: 2026-10-06
Session: P4-S019
Incoming checkpoint: b71f3fff7e128cafc6eb0e225f7b3f00ce8dc7cd
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **LOSS-PROPERNESS DOES NOT EFFECTIVIZE AUTOMATICALLY. THERE IS A COMPUTABLE GLOBALLY k=2, GLOBALLY ADMISSIBLE LAST-CHANCE TICKET STREAM FOR WHICH b(K)=sup{E(v):W*(v)<K} IS FINITE FOR EVERY INTEGER K, BUT NO TOTAL COMPUTABLE FUNCTION UNIFORMLY MAJORIZES b(K). THE OBSTRUCTION IS HALTING-TIME INFORMATION HIDDEN IN FINITE BAD-CAPITAL EXCURSIONS AFTER ARBITRARILY LONG ZERO-LOSS WAITING. A COMPUTABLE UPPER-BOUND FUNCTION FOR b(K), EQUIVALENTLY AN EFFECTIVE LOSS-PROPERNESS CERTIFICATE, IS EXACTLY THE EXTRA NUMERICAL EFFECTIVITY NEEDED TO RECOVER THE P4-S018 COERCIVITY MODULUS. P4-S011 CANNOT SATISFY EVEN SET-THEORETIC LOSS-PROPERNESS FOR ANY GLOBALLY ADMISSIBLE FULL-TICKET ACCOUNT.**

## Authority, uniqueness and scope

Live main matched the requested checkpoint b71f3fff7e128cafc6eb0e225f7b3f00ce8dc7cd exactly before substantive work, and it still matched immediately before the first P4-S019 write. Repository commit search returned no committed P4-S019 record on the incoming checkpoint, so P4-S019 was unused.

P4-S001 through P4-S018 and the required CAND-01 authority were read. P4-S005 through P4-S018 are treated as settled. In particular P4-S011's exact k=2 destroyer, P4-S015's weighted theorem, P4-S016's envelope-free last-chance theorem, P4-S017's coercive self-financing theorem, and P4-S018's running-maximum modulus/cross-branch boundary are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. This session stays strictly at k=2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained P4-S018 quantity

Fix a computable horizon/ticket stream and a finite computable reserve making the canonical full-ticket account globally admissible. For each finite resolved ticket history v let

E(v) = cumulative realized positive skipped gain,

W*(v) = maximum ticket-account capital attained on a resolved-ticket prefix of v.

For an integer K>=1 define the bad-capital set

B_K = {v : W*(v)<K}

and its loss height

b(K) = sup {E(v) : v in B_K}.

P4-S018 calls the account loss-proper when b(K)<infinity for every K.

A computable running-maximum coercivity modulus is a total computable threshold h such that

E(v)>=h(K)  implies  W*(v)>=K

for every finite history v.

The only question here is whether the computability of the k=2 ticket tree plus finiteness of every b(K) automatically produces such an h.

It does not.

## 2. What computability gives for free

### Lemma 1 — b(K) is uniformly lower semicomputable

For fixed K, finite ticket histories are effectively enumerable and E(v), W*(v) are computable rationals. Therefore one can enumerate the values E(v) for histories satisfying W*(v)<K and keep their running maximum.

This gives a uniformly computable increasing rational approximation to b(K).

So the ticket tree supplies lower information about b(K). Loss-properness says that this increasing approximation has a finite limit. It supplies no effective upper information about that limit.

### Lemma 2 — a computable majorant and a computable coercivity threshold are equivalent up to a harmless margin

Suppose U:N_{>=1}->Q_{>=0} is total computable and

b(K)<=U(K)

for every K. Then

h(K)=U(K)+1

is a computable P4-S018 threshold: if E(v)>=h(K), then v cannot lie in B_K.

Conversely, if h is a computable P4-S018 threshold, then every v in B_K has E(v)<h(K), so

b(K)<=h(K).

Thus, for the settled ticket/restart architecture, the remaining effectivity question is exactly whether the finite lower-semicomputable function K -> b(K) has a computable uniform majorant.

## 3. Halting-coded finite excursions

We build one computable exact k=2 ticket stream from the two P4-S017 gadgets plus zero-stake control epochs.

Fix a standard computable enumeration of partial machines Phi_e on empty input. Put

H_n = sum_{r<n} 1/(r+1)

and

P_n = 1 + H_n/2.

Use initial ticket reserve R=1. Let d hold its capital fixed on every control/wait epoch and make all-in wagers on bit 1 only at the productive sentinel epochs described below. Let q=Save(d), using the settled P4-S015 wrapper.

Along a run with r previous correct productive sentinel wagers, q has r units of saved capital plus one unit of active risk. Thus the next positive skipped gain on a correct sentinel is

ell_r = 1/(r+1).

All control and waiting epochs are zero-stake and consume their sentinels immediately.

### Mode selection

A first zero-stake control bit chooses between two modes.

**Mode A — infinite productive mode.**
Run the settled P4-S017 one-sided-trigger H=1 gadget forever. On a positive stored sentinel at productive stage r, the last-chance ticket has payouts {0,ell_r}, fair price ell_r/2, and the winning trigger child continues to the next productive stage. The nontrigger child ends future positive tickets.

This is exactly the settled coercive gadget, now started with reserve 1.

**Mode B — halting-coded finite-excursion mode.**
Read a unary index e by zero-stake consumed controls: 0^e1 chooses e. The all-zero control continuation remains zero-stake forever.

After choosing e, run e productive one-sided-trigger stages. Only the branch which triggers and has positive stored sentinel at each of those stages reaches the next part with active risk still equal to one. Along that branch,

E = H_e,
W = W* = P_e = 1+H_e/2.

A nontriggering productive stage is the settled permanent-avoidance child and has no later positive tickets. A losing sentinel kills the active risk, so it cannot create a larger future E.

Next simulate Phi_e one ordinary machine step per zero-stake consumed-sentinel epoch.

- If Phi_e never halts, continue zero-stake forever.
- If Phi_e halts after t simulation steps, run exactly t copies of the settled P4-S017 deterministic-trigger gadget and then use only zero-stake epochs forever.

On the all-positive sentinel branch of this finite burst, deterministic burst stage j has

L(0)=L(1)=ell_{e+j}=1/(e+j+1).

Hence its fair premium equals its certain payout. The ticket account stays exactly at P_e while E increases. At the end of the t-stage burst,

E = H_{e+t},
W* = P_e.

If a burst sentinel is 0, its positive skipped gain is zero and the active risk disappears, so again the all-positive branch maximizes E.

### Computability and k=2 check

The controller uses only finite computable state: mode, unary index, ladder counter, a finite step-by-step simulation of Phi_e, and finite burst counter after a halt is observed.

Every physical next query is therefore computable from the finite transcript.

The only potentially nonterminating productive epoch is the settled one-sided-trigger epoch. On its nontrigger continuation it omits exactly that current sentinel and enumerates every other source coordinate. All zero-stake controls, zero-stake waiting epochs and deterministic-trigger epochs consume their current sentinels.

Therefore every transcript either gets trapped in one settled nontrigger epoch and omits exactly one coordinate, or consumes every sentinel. The induced least-fresh scan remains everywhere total, no-repeat, fair-coin preserving and globally k=2.

This is a ticket-stream boundary construction, not a new randomness-destruction witness.

## 4. Global admissibility

### Lemma 3 — reserve 1 funds every prescribed ticket

On a one-sided productive stage, a positive-cost ticket has price ell_r/2.

- If it wins, it pays ell_r, so net ticket capital rises by ell_r/2.
- If it loses, capital falls by ell_r/2 and that epoch becomes permanently nontriggering, so no later positive premium is due.

Since ell_r<=1 and the account starts at 1, even a first losing ticket leaves nonnegative capital. Earlier wins only increase the available capital.

On a deterministic burst stage, price equals payout on both filler children, so ticket capital is unchanged.

Zero-stake epochs cost nothing.

Hence the canonical full-ticket account is globally admissible with reserve R=1.

Mode A also retains the P4-S017 separation from absolute premium summability: on its all-trigger positive-sentinel branch,

sum pi_r = (1/2) sum 1/(r+1) = infinity.

So the new boundary does not restore the P4-S016 absolute premium budget.

## 5. Every b(K) is finite

### Theorem 4 — the construction is loss-proper

Fix an integer K.

For K<=1, B_K is empty because the initial reserve is 1.

Now suppose K>1. Since H_n diverges computably, choose n_K least such that

P_{n_K} = 1+H_{n_K}/2 >= K.

In Mode A, every continuing positive productive stage satisfies W=1+E/2. Therefore any Mode-A history in B_K has

E < 2(K-1),

apart from a final losing ticket which does not increase E.

Consider Mode B. A history can reach the machine-wait/burst part for index e only after e successful positive productive ladder stages, at which point W*=P_e.

If e>=n_K, then P_e>=K, so no history after that ladder belongs to B_K.

Thus only the finitely many indices e<n_K can contribute machine-wait/burst histories to B_K.

For each such e:

- if Phi_e diverges, its post-ladder E stays H_e forever;
- if Phi_e halts after t_e steps, its burst is finite and its largest possible E is H_{e+t_e}.

The remaining histories are control prefixes or incomplete/failed ladder prefixes, whose E is bounded by H_{n_K}.

There are only finitely many relevant e<n_K and every halting t_e is a finite natural number. Hence the set of possible bad-capital E values has a finite supremum.

Therefore

b(K)<infinity

for every K.

The proof is deliberately non-effective at one point: it takes the maximum of finitely many actual halting times without providing a way to know which of those machines halt.

## 6. No computable uniform upper bound exists

### Theorem 5 — loss-properness does not force an effective modulus

Assume toward contradiction that there is a total computable rational function U such that

b(K)<=U(K)

for every integer K.

Fix an index e. The rational P_e=1+H_e/2 is computable. Let

K_e = floor(P_e)+1,

so K_e is an integer and P_e<K_e.

If Phi_e halts after t steps, take the Mode-B branch which:

1. chooses index e;
2. wins all e ladder stages with positive sentinels; and
3. has positive sentinels through the entire t-stage deterministic burst.

At the end of that finite burst,

W* = P_e < K_e,
E = H_{e+t}.

Therefore

H_{e+t} <= b(K_e) <= U(K_e).

Because harmonic partial sums diverge effectively, from e and the computable rational U(K_e) one can search for T with

H_{e+T} > U(K_e).

If Phi_e were to halt at some t>=T, the previous inequality would be impossible. Thus, if Phi_e halts at all, it halts before T.

Simulate Phi_e for T steps. If it halts, answer yes; if it has not halted by then, answer no.

This would decide the halting problem, contradiction.

Hence no total computable function uniformly majorizes the finite values b(K).

By Lemma 2 there is therefore no computable P4-S018 running-maximum coercivity modulus for this loss-proper account.

## 7. Exact obstruction

P4-S018's obstruction was cross-branch nonuniformity strong enough to destroy even set-theoretic loss-properness. P4-S019 moves one layer deeper.

Here each fixed bad-capital tree B_K has a finite E-height. The problem is that those finite heights are not effectively bounded as K varies.

The construction hides the halting time of Phi_e in a finite deterministic excursion which is reachable only after the ticket account has climbed to P_e. For any fixed K only finitely many such indices remain below K, so the supremum is finite. But obtaining a uniform upper bound would have to know how long every halting computation among those finitely many indices runs.

Equivalently:

- computability of the ticket tree makes b(K) uniformly lower semicomputable;
- loss-properness says these lower approximations converge to finite values;
- neither fact supplies an effective upper approximation or computable majorant;
- the missing information can have halting-time strength.

This is an effectivity obstruction, not a failure of set-theoretic uniformity at each K.

## 8. Weakest effective extra condition established

### Definition — effective loss-properness

Call the admissible account effectively loss-proper when there is a total computable rational function U such that for every K and every finite history v,

W*(v)<K  implies  E(v)<=U(K).

By Lemma 2 this is equivalent, up to adding a harmless rational margin, to the P4-S018 computable coercivity modulus.

Therefore effective loss-properness is the exact numerical extra condition needed by the settled ticket/restart proof. Mere finiteness of b(K) is strictly weaker.

A natural stronger presentation is to require the loss-bar predicate

Bar(K,m): every finite v with W*(v)<K has E(v)<m

to have uniformly semidecidable positive certificates, with at least one certified m for every K. Then a search finds such an m and computes U(K).

Without extra structure, Bar(K,m) is only a global no-counterexample assertion over the computable tree. A violating finite history is semidecidable; validity of the bar need not be.

No claim is made that every possible transfer architecture must receive its effectivity in this numerical form.

## 9. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source, d its successful output martingale, H any total computable horizon selector, and q=Save(d).

P4-S016 establishes that along the sentinel-first completion C(Y), cumulative realized skipped gain satisfies

E(C(Y))=infinity.

Now suppose some finite reserve made the canonical full-ticket account globally admissible and loss-proper.

If its running maximum W* were bounded on C(Y), choose an integer K above that bound. Every resolved prefix of C(Y) would then belong to B_K while E along those prefixes is unbounded, giving

b(K)=infinity,

contrary to loss-properness.

Thus loss-properness would force W* to be unbounded on C(Y). Global admissibility makes the ticket account a total nonnegative computable martingale, so it would succeed on C(Y).

But C is the settled P4-S001 effective isomorphism and Y is computably random. Therefore C(Y) is computably random. Contradiction.

Consequently, for every computable horizon selector H:

- if no finite reserve makes the full-ticket account globally admissible, the certificate already fails at admissibility;
- if some finite reserve does make it globally admissible, that account cannot be loss-proper: for some K, b(K)=infinity.

This strengthens the previous P4-S018 check. P4-S011 is not merely outside every effective-modulus regime; under admissibility it is outside the set-theoretic loss-proper regime itself.

As before, bare admissibility alone is not ruled out.

## 10. Successes and limits

Successful:

1. Proved that b(K) is uniformly lower semicomputable from the computable finite ticket tree.
2. Identified a computable majorant of b(K) as exactly the remaining numerical content of a computable P4-S018 modulus.
3. Built a computable globally k=2, globally admissible ticket stream with b(K)<infinity for every K.
4. Proved that no total computable function majorizes those finite b(K).
5. Kept a Mode-A branch with divergent harmonic absolute premiums, so the obstruction does not collapse back to P4-S016.
6. Isolated the obstruction as halting-time information hidden in finite bad-capital excursions after zero-loss waiting.
7. Identified effective loss-properness, i.e. a computable uniform bad-capital loss bound, as the exact numerical extra condition for this proof architecture.
8. Strengthened the P4-S011 exclusion: any globally admissible full-ticket account for its ticket stream must fail set-theoretic loss-properness at some K.

Not claimed:

1. No necessity theorem is claimed for transfer architectures other than the settled full-ticket plus restart decomposition.
2. No claim is made that the halting-coded boundary construction is a new randomness-destruction witness.
3. No settled P4-S005 through P4-S018 result is reopened.
4. No result is claimed for k>2.
5. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S011's exact k=2 destroyer is unchanged.
P4-S015's weighted theorem and savings wrapper are unchanged.
P4-S016's envelope-free last-chance-ticket theorem is unchanged.
P4-S017's coercive self-financing theorem is unchanged.
P4-S018's computable running-maximum modulus theorem and cross-branch obstruction are unchanged.
PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
DEF-0020 is unchanged.

## Next bounded question

The remaining positive issue is structural rather than numerical: identify a natural local condition that makes finite bad-capital loss bars effectively searchable, without simply supplying U(K) as extra data and without restoring absolute premium summability.

A bounded P4-S020 should test only whether a computable bound on zero-loss waiting / positive-loss reachability inside each bad-capital tree, or an exactly identified weaker local searchability condition, turns set-theoretic loss-properness into effective loss-properness. If not, isolate the next nonuniformity obstruction and check P4-S011 explicitly.
