# P4-S015 — stake-weighted skipped-wager loss budgets

Date: 2026-10-06
Session: P4-S015
Incoming checkpoint: 7c47680ab22d21e9fd21cb1d276165f0406bc0e8
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh stake subclass only

Result: **RAW HORIZON-MISS PROBABILITIES NEED NOT BE SUMMABLE. A COMPUTABLE FINITE-HORIZON FAIR PRICE FOR THE POSSIBLE POSITIVE MULTIPLICATIVE GAIN OF THE DEFERRED SENTINEL WAGER THAT WOULD BE SKIPPED AFTER A MISS IS SUFFICIENT WHEN THOSE PRICES HAVE ONE FINITE UNIFORM PATHWISE BUDGET. A SAVINGS WRAPPER, WEIGHTED MISS TICKETS AND THE P4-S014 TRUNCATED/RESTART HEDGE GIVE ONE TOTAL TRANSFER MARTINGALE. THE CONDITION IS STRICTLY WEAKER THAN P4-S014 AT THE SCAN/MARTINGALE CERTIFICATE LEVEL. THE EXACT POINTWISE MINIMAL FUTURE-LOSS ENVELOPE NEED NOT BE UNIFORMLY COMPUTABLE. P4-S011 NECESSARILY VIOLATES EVERY SUCH FINITE WEIGHTED CERTIFICATE.**

## Authority, uniqueness and scope

Live main matched the P4-S014 outgoing checkpoint 7c47680ab22d21e9fd21cb1d276165f0406bc0e8 exactly before substantive work. The P4-S015 mathematics, close and validation records were absent on that checkpoint, and repository search returned no committed P4-S015 record, so the session identifier was unused.

P4-S001 through P4-S014 and the required CAND-01 authority were read. P4-S005 through P4-S014 are treated as settled. In particular P4-S011's exact global-k=2 destroyer, P4-S012's stake-level boundary, P4-S013's reachable-sentinel-totality / finite-deadline theorem and P4-S014's computably budgeted raw-tail theorem are preserved.

This session changes only the quantitative budget charged after a P4-S014 horizon miss. It does not reopen crossing-measure, canonical-sheet, one-hole/coalescence, persistent-hole or capped-projection routes.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

## 1. Exact loss from skipping one deferred sentinel wager

Fix the P4-S012/P4-S014 least-fresh scan and a nonnegative rational-valued computable martingale d on its logical output. Normalize d(empty)=1.

For a transcript tau with d(tau)>0, write

theta_d(tau) = (d(tau1)-d(tau0))/(2 d(tau)).

Then theta_d(tau) is in [-1,1] and

d(taub) = d(tau) (1 + theta_d(tau)(2b-1)).

At zero capital put theta_d=0; nonnegativity makes zero absorbing.

After a P4-S014 horizon miss, if the same epoch later triggers then the sentinel has already been physically revealed by the sentinel-first completion. The restart hedge skips exactly this one logical sentinel update. Only a positive logical gain can damage the comparison.

Define

ell_d(tau,b)
 = max(0, d(taub)/d(tau) - 1)
 = max(0, theta_d(tau)(2b-1))

when d(tau)>0, and put ell_d=0 at zero capital. Thus 0<=ell_d<=1.

A losing or flat sentinel wager has loss zero: skipping it cannot decrease completion capital relative to d. This is the multiplicative quantity that the unit P4-S014 miss ticket overcharged.

## 2. Savings wrapper

The P4-S014 finite-miss proof only needed exact tracking after the last miss. With infinitely many small weighted misses, output success must remain visible at restart/epoch boundaries.

### Lemma 1 — computable savings transform with no larger fractional stakes

From d compute a nonnegative rational martingale q=Save(d) such that:

1. if d is unbounded on a path, q tends to infinity along all sufficiently long prefixes of that path;
2. the absolute fractional stake of q is never larger than that of d, so ell_q(tau,b)<=ell_d(tau,b).

#### Construction

Maintain cash savings S and active risk R. Initially S=0 and R=1. At tau, risk R uses theta_d(tau). On child b set

R* = R (1 + theta_d(tau)(2b-1)).

If R*>=2, transfer one unit to savings: S'=S+1 and R'=R*-1. Otherwise S'=S and R'=R*. Put q=S+R.

The total child capital is always S+R*, so q is a computable rational martingale. Its one-step change is

q(taub)-q(tau)=R theta_d(tau)(2b-1),

hence its fractional stake is (R/q)theta_d(tau), proving the stake domination.

If only finitely many savings transfers occurred on a path, then after the last transfer R would evolve by exactly the same multiplicative factors as d with a fixed positive ratio to d. Unbounded d would eventually force R>=2 and another transfer, contradiction. Hence unbounded d causes infinitely many one-unit savings transfers, so S and therefore q tend to infinity. QED.

## 3. Leaf-dependent skipped-loss envelopes and exact fair cost

At a reachable epoch state s, let j be the withheld sentinel and A_s the computable avoidance tree from P4-S013. Choose a total computable finite horizon H(s) and put

R_s = A_s intersect 2^{H(s)}.

These are the finite filler-answer leaves on which the horizon is missed.

The sentinel-first completion physically reveals the sentinel bit b before the fillers. For every finite miss leaf (b,rho), assume a computable rational

w(s,b,rho) in [0,1]

with this future-loss envelope property:

For every continuation of that miss leaf on which the same logical epoch later triggers at a pre-sentinel transcript tau,

ell_q(tau,b) <= w(s,b,rho).

If the epoch never later triggers, there is no skipped sentinel wager and the true loss is zero. The envelope need not decide that case exactly.

Define the finite-ticket price

c(s)
 = 2^{-(H(s)+1)}
   sum_{rho in R_s} ( w(s,0,rho) + w(s,1,rho) ).

Because H(s) is finite and A_s is computable, c(s) is a computable rational.

This is exactly the fair price of a finite terminal ticket which pays w(s,b,rho) on the corresponding horizon-miss leaf and zero if the epoch triggers by the horizon. The fresh sentinel and H(s) fresh fillers give each miss leaf probability 2^{-(H(s)+1)}.

P4-S014 is the special case w=1 on every miss leaf, where c(s)=p(s).

A simpler sufficient form is a computable a(s) in [0,1] dominating every possible post-horizon positive sentinel gain from s. Taking w=a(s) gives

c(s)=p(s)a(s).

Hence a finite pathwise budget on sum p(s)a(s) is sufficient even when sum p(s) diverges.

## 4. Main weighted-transfer theorem

### Definition — computably budgeted positive skipped-gain tails for d

For q=Save(d), require:

1. a total computable finite horizon selector H(s);
2. a total computable rational leaf envelope w(s,b,rho) satisfying the domination property;
3. a computable rational C_0<infinity;

such that on every source run, for successive reached epoch states s_0,s_1,...,

sum_r c(s_r) <= C_0,

with the sum stopping if some epoch never ends.

This condition is martingale-relative. A map-wide preservation theorem would need such a certificate for every output martingale, or a stronger uniform condition implying it.

### Theorem 2 — weighted budgets suffice for one source transfer martingale

If the above certificate exists for d, then there is one total computable source martingale succeeding on every source x on which d succeeds on the logical least-fresh output.

#### Proof

Use the globally exhaustive sentinel-first completion C from P4-S014. It is a computable adaptive permutation and hence a fair-coin effective isomorphism by P4-S001.

Construct two computable martingales on the completion stream.

### Weighted ticket martingale J

Start with reserve C_0. At each reached epoch s, buy the finite miss-leaf ticket for price c(s), and keep resolved payouts as cash.

The pathwise budget prevents overdraft. After any finite collection of resolved tickets,

J >= C_0 - sum c(s_r)
     + sum_{actual horizon misses r} w(s_r,b_r,rho_r).

Therefore if the sum of realized miss weights diverges, J is unbounded. No independence is used.

### Truncated/restart martingale D

Run the P4-S014 finite-horizon conditional-expectation hedge against q. If q is zero at a restart state, freeze D forever on that branch. Zero is absorbing for q, so such a branch cannot be one on which d succeeds. This makes the construction total without affecting the success implication.

On a good epoch triggering by H(s), D tracks one fixed positive multiple of q exactly through sentinel consumption. After a horizon miss, D copies q on later fresh fillers. If that epoch never triggers, D copies q forever. If it later triggers, D skips the already-revealed sentinel update and restarts at the next epoch.

Suppose a missed epoch later triggers at pre-sentinel transcript tau with actual sentinel bit b. Put

g = q(taub)/q(tau).

If immediately before the logical sentinel D=alpha q(tau), then after skipping that zero-physical-time logical update the new scale is alpha/g.

If g<=1, skipping cannot decrease the scale. If g>1, then

g-1 = ell_q(tau,b) <= w

for the realized miss leaf, so

alpha/g >= alpha/(1+w).

Across missed-and-later-triggered epochs,

alpha_new >= alpha_old product_misses (1+w_r)^{-1}
          >= alpha_old exp(-sum_misses w_r),

because log(1+w)<=w.

If the realized miss-weight sum is finite, the scale therefore has a positive lower bound. If infinitely many epochs continue and d succeeds, q tends to infinity at the successive epoch-start prefixes, so D succeeds. If some missed epoch never triggers, D copies q forever after its horizon and again succeeds whenever d does.

Thus divergent realized miss weight is handled by J, while finite realized miss weight plus output success is handled by D. Their sum M=J+D is one computable completion martingale succeeding whenever d succeeds.

Finally C is the settled P4-S014/P4-S001 effective isomorphism, so M transfers to one computable martingale on the original source. QED.

No infinite-horizon trigger probability, convergence modulus or exact optional projection is computed.

## 5. Strict separation from P4-S014 raw budgets

Define a self-avoiding partial stake functional as follows. At an epoch with sentinel j:

1. inspect coordinate j+1;
2. if it is 1, halt with positive stake a_j=2^{-(j+1)};
3. if it is 0, inspect coordinate j+2;
4. if that second bit is 1, halt with the same stake a_j;
5. if the first two bits are 00, diverge forever.

The computation never queries j.

In the least-fresh scan, induction shows that at every new epoch no coordinate at or above the current sentinel has yet been queried. Thus j+1 and, when needed, j+2 are exactly the first two fresh fillers.

If the controls are 1, the epoch triggers after one filler. If they are 01, it triggers after two. If they are 00, it never triggers and the scan eventually queries every coordinate except j. The settled P4-S011/P4-S012 calculation therefore gives totality, no-repeat, fair-coin preservation and global fibres of size at most two.

### No P4-S014 raw certificate exists

At every reachable epoch, controls 00 give a permanent avoiding sibling of conditional probability 1/4. Therefore every finite horizon selector has

p(s,H(s)) >= 1/4.

There are infinite all-trigger runs, for example those taking first control bit 1 at every epoch. Along such a run infinitely many epochs are reached, so the raw sum diverges for every horizon selector. This scan has no P4-S014 finite uniform raw-tail certificate.

### A P4-S015 weighted certificate exists for its sentinel martingale

Let the associated output martingale hold on fillers and use stake +a_j at the triggered sentinel. Choose constant horizon H=1.

The unique miss filler is rho=0, with raw probability 1/2. A later 01 trigger can create a positive skipped gain only when the sentinel bit is b=1, and that gain is exactly a_j. On b=0 the skipped wager would lose; on 00 no sentinel wager ever occurs. Take

w(s,1,0)=a_j,
w(s,0,0)=0.

Then

c(s)=a_j/4.

Successive sentinels are strictly increasing, so on every run

sum_r c(s_r)
 <= (1/4) sum_{j>=0} 2^{-(j+1)}
 = 1/4.

Thus the weighted certificate has a finite computable pathwise budget although no P4-S014 raw-tail certificate exists.

This is a strict separation of transfer certificates for this scan/martingale pair. The small-stake martingale is not asserted to succeed, and the example is not a new randomness-destroying witness or a map-wide preservation theorem.

## 6. Sharp effectivity obstruction: the exact minimal envelope may be noncomputable

Pointwise, the mathematically smallest leaf weight is

w_min(s,b,rho)
 = sup { ell_q(tau,b) :
         tau is a later pre-sentinel trigger extending the miss leaf },

with supremum zero if no later trigger exists.

This pointwise optimum is not uniformly computable from arbitrary partial stake data.

### Proposition 3

Fix a c.e. noncomputable set K. Uniformly in e, define a self-avoiding one-epoch stake functional which first requires one non-sentinel filler to be revealed and then searches the enumeration of K for e.

If e is eventually enumerated, halt with all-in stake +1. If e is never enumerated, diverge forever.

Take horizon H=1 and a martingale flat on the filler and all-in on sentinel bit 1 if the trigger appears. For the miss leaf and b=1, the exact minimal future positive-loss envelope is

w_min=1 iff e is in K,

and is zero otherwise.

A uniform algorithm for the exact pointwise minimal envelope would therefore decide K. So the computable rational envelope in Theorem 2 is genuine extra effective certificate data. This is a narrow effectivity fact about the weighted route; the settled P4-S010 capped-projection route is not reopened.

## 7. P4-S011 necessarily violates every finite weighted certificate

P4-S011's winning output martingale is all-in and correct at every target sentinel. Whenever a chosen horizon is missed on its computably random target Y and that epoch later triggers, the skipped logical sentinel multiplier is 2, so ell=1.

Any valid P4-S015 envelope on that realized miss leaf must therefore have w=1.

Suppose P4-S011 admitted a finite P4-S015 certificate. By Theorem 2:

- if infinitely many horizons are missed along Y, the realized weights are all one and the weighted ticket martingale succeeds;
- if only finitely many horizons are missed, the truncated/restart martingale eventually tracks a fixed positive multiple of the savings-wrapped all-in martingale and succeeds.

The sentinel-first completion would then have a computable martingale succeeding on the image of Y, and P4-S001 would transfer it to a computable martingale succeeding on Y. This contradicts P4-S011's computable randomness of Y.

Therefore the exact P4-S011 destroyer admits no finite weighted-loss certificate of the P4-S015 form, for any total computable horizon selector and any computable envelope satisfying the required domination.

For the coarser p(s)a(s) condition, all-in wagers force a(s)=1 whenever a post-horizon trigger with the favoured bit remains possible, so small stake weights cannot hide P4-S011's full-wager losses.

## 8. Exact established boundary

The sharpest sufficient cost established here inside the finite-horizon ticket/restart architecture is

c(s)
 = 2^{-(H(s)+1)}
   sum_{rho in A_s intersect 2^{H(s)}}
       (w(s,0,rho)+w(s,1,rho)),

where w is any computable leafwise majorant of the positive multiplicative gain of a later skipped sentinel wager.

It improves on raw p(s) because it charges only positive skipped gain, can distinguish the two sentinel bits, and can distinguish different finite miss leaves, including harmless leaves.

The coarser computable bound a(s) gives the simple condition sum p(s)a(s)<infinity.

The pointwise mathematical minimum w_min is not uniformly computable, so no theorem is claimed without an effective envelope or stronger data from which one can be computed.

No claim is made that this is absolutely weakest among all possible martingale-transfer methods.

## 9. Successes and failures

Successful:

1. Raw finite-horizon miss probabilities may be nonsummable while a computable stake-weighted skipped-loss budget is summable.
2. The finite-ticket cost is the fair expectation of a computable leaf-dependent majorant of the positive multiplicative sentinel gain that would be skipped.
3. A savings wrapper makes arbitrary output-martingale success persistent at late restart points without increasing stake magnitudes.
4. Weighted miss tickets handle divergent realized skipped-loss weights.
5. The P4-S014 truncated/restart hedge handles finite realized skipped-loss weight even across infinitely many horizon misses.
6. Their sum gives one completion martingale, and P4-S001 gives one source martingale.
7. The two-control-bit scan has no P4-S014 raw-tail certificate for any horizon selector but has a finite P4-S015 weighted certificate for its small-stake sentinel martingale.
8. The exact minimal future-loss envelope need not be uniformly computable.
9. P4-S011 necessarily violates every finite P4-S015 certificate.

Failed or deliberately not claimed:

1. No automatic procedure extracts the exact minimal future-loss envelope from an arbitrary partial stake functional.
2. No map-wide preservation theorem follows because one particular output martingale has a weighted certificate.
3. No absolute necessity of the weighted condition is claimed.
4. No settled P4-S005 through P4-S014 route is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S011's exact k=2 destroyer is unchanged.
P4-S012's stake-level structural boundary is unchanged.
P4-S013's reachable-sentinel-totality / finite-deadline theorem is unchanged.
P4-S014's raw miss-probability theorem is unchanged and is recovered by the unit envelope w=1.
PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
DEF-0020 is unchanged.

## Next bounded question

The extra effective datum is now precise: a computable majorant of future positive skipped-sentinel gain on each finite miss leaf. The pointwise optimal majorant need not be computable.

The smallest next question is whether this advance envelope can be eliminated without returning to an infinite optional projection: can one buy computable incremental loss tickets only when larger postmiss stakes become finitely visible, under a computably budgeted sum of those increments, and still obtain one transfer martingale? Any such result must again be checked against the P4-S011 all-in destroyer.
