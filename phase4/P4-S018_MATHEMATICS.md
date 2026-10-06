# P4-S018 — effective coercivity modulus and cross-branch escape

Date: 2026-10-06
Session: P4-S018
Incoming checkpoint: 5b77d2f6b0d824c9f8a0213908e6fbd6efc245a9
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh stake subclass only

Result: **P4-S017 SEMANTIC COERCIVITY HAS A CLEAN EFFECTIVE SUFFICIENT REPLACEMENT, BUT NOT AN EQUIVALENT ONE. THE WEAKEST NATURAL LOCAL CERTIFICATE FOR THE SAME TICKET/RESTART PROOF IS A COMPUTABLE RUNNING-MAXIMUM COERCIVITY MODULUS: FOR EACH CAPITAL TARGET K, A COMPUTABLE LOSS THRESHOLD h(K) FORCES THE TICKET ACCOUNT TO HAVE ALREADY REACHED K ONCE REALIZED SKIPPED LOSS REACHES h(K). THIS MAY GROW ARBITRARILY SLOWLY AND DOES NOT RESTORE ABSOLUTE PREMIUM SUMMABILITY. HOWEVER SEMANTIC COERCIVITY DOES NOT IMPLY EVEN A NONCOMPUTABLE UNIFORM THRESHOLD: COMPUTABLE k=2 TICKET STREAMS CAN HAVE ARBITRARILY LARGE FINITE-LOSS SIDE EXCURSIONS WITH BOUNDED CAPITAL, WHILE EVERY ACTUALLY LOSS-DIVERGENT BRANCH IS COERCIVE. THE OBSTRUCTION IS CROSS-BRANCH NONUNIFORMITY. P4-S011 ADMITS NO SUCH EFFECTIVE MODULUS FOR ANY COMPUTABLE HORIZON SELECTOR.**

## Authority, uniqueness and scope

Live main matched the requested checkpoint `5b77d2f6b0d824c9f8a0213908e6fbd6efc245a9` exactly before substantive work. Repository search returned no committed P4-S018 record, so the session identifier was unused.

P4-S001 through P4-S017 and the required CAND-01 authority were read. P4-S005 through P4-S017 are treated as settled. In particular P4-S011's exact global-k=2 destroyer, P4-S015's weighted theorem and savings wrapper, P4-S016's envelope-free exact last-chance ticket theorem, and P4-S017's coercive self-financing reserve theorem are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No result is claimed for k>2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Retained P4-S017 account

Fix a nonnegative rational-valued computable output martingale d, its settled P4-S015 savings wrapper q=Save(d), a total computable horizon selector H, and the settled sentinel-first completion.

Along a completion run enumerate the exact P4-S016 postmiss last-chance tickets by i. Let

`pi_i=(L_i(0)+L_i(1))/2`

be the exact fair premium and let `e_i=L_i(a_i)` be the realized payout, equal to the positive multiplicative gain of the skipped sentinel wager when that wager becomes visible immediately.

For finite ticket history v put

`E(v)=sum e_i`

and let the canonical full-ticket account with computable rational reserve R have resolved capital

`W(v)=R+sum e_i-sum pi_i.`

P4-S017 admissibility says every prescribed full ticket is affordable on every run. Its semantic coercivity clause is

`E(X)=infinity => sup_n W(X↾n)=infinity`

for every completion run X.

The settled restart hedge succeeds on every d-success path with finite total E. Hence only the divergent-E case needs insurance success.

## 2. The weakest natural local effective certificate for this proof

For a finite history v define the running maximum

`W*(v)=max{W(u): u is a resolved-ticket prefix of v},`

including the initial reserve.

### Definition — computable running-maximum coercivity modulus

An admissible ticket account has an effective coercivity modulus if there is a total computable nondecreasing function

`h: N_{>=1} -> Q_{>=0}`

such that for every finite resolved ticket history v and every integer K>=1,

`E(v) >= h(K)  =>  W*(v) >= K.`

No prescribed rate is required. h may grow arbitrarily fast as a loss threshold, equivalently the guaranteed capital floor as a function of accumulated loss may grow arbitrarily slowly.

This is local in the relevant sense: E(v) and W*(v) are computed from the finite ticket history. No future supremum, infinite optional projection, tail probability or advance loss envelope is computed.

### Equivalent floor form

The threshold form is equivalent, up to routine integer rounding, to a total computable nondecreasing unbounded function g on nonnegative rationals satisfying

`W*(v) >= g(E(v))`

for every finite ticket history v.

The running maximum is essential for minimality. Requiring the current capital W(v) itself to dominate g(E(v)) is stronger than needed because martingale success only asks for an unbounded supremum.

### Theorem 1 — effective-modulus transfer

If the canonical full-ticket account is globally admissible and has a computable running-maximum coercivity modulus, then the P4-S017 conclusion holds: there is one total nonnegative computable source martingale succeeding whenever d succeeds on the logical least-fresh output.

#### Proof

If total realized skipped loss is finite, the settled restart hedge succeeds on every d-success path. If total realized skipped loss diverges, then for each integer K the finite history eventually satisfies E>=h(K), hence W*>=K. Therefore the ticket account is unbounded. The sum of ticket and restart accounts is one computable completion martingale, and the settled P4-S001 effective-isomorphism transfer gives one source martingale. QED.

Thus the effective modulus can replace semantic coercivity as a **sufficient certificate**, but the next sections show that it is not an equivalent reformulation.

## 3. It remains strictly weaker than absolute premium summability

Reuse the fixed-H one-sided trigger example settled in P4-S017 Section 6.

With H=1, on positive stored sentinels the stage-r ticket has possible payout 0 or

`ell_r=1/(r+1)`

and exact premium `ell_r/2`. A winning ticket reaches another epoch and increases ticket capital by `ell_r/2`; a losing positive-cost ticket ends all later positive premiums.

With reserve 1/2, on every finite history

`W*(v) >= 1/2 + E(v)/2.`

Hence, for example, `h(K)=max(0,2K-1)` after harmless rational/integer rounding is a computable coercivity modulus.

Along the all-trigger positive-sentinel run,

`sum pi_r=(1/2)sum 1/(r+1)=infinity.`

Therefore the effective-modulus condition does not restore P4-S016 absolute premium summability. The separation is, as in P4-S017, for the fixed horizon/ticket stream.

## 4. Exact cross-branch obstruction

Semantic coercivity quantifies only over **individual infinite runs with E=infinity**. A uniform modulus demands much more: a single finite loss threshold for each capital target must work simultaneously over all finite branches.

That extra uniformity can fail completely.

### Construction from the two settled P4-S017 gadgets

Use a computable zero-stake control prefix to choose between two modes. Control epochs carry no positive skipped loss and therefore no positive ticket premium.

**Mode A — productive coercive branch.**
Use the P4-S017 one-sided trigger gadget. On a positive stored sentinel the exact ticket has child losses `{0,ell_r}`, price `ell_r/2`, and the zero-payout nontrigger branch ends future positive tickets. With reserve R=1 this mode is admissible and whenever E diverges its ticket capital grows unboundedly. It also has an all-trigger positive-sentinel branch with divergent absolute premium sum.

**Mode B — finite deterministic bursts.**
Read a unary control code using zero-stake, always-consumed control epochs. If the first 1 occurs after N-1 zeros, run exactly N copies of the P4-S017 deterministic-trigger gadget and then hold forever. If the unary code is all zeros, remain zero-stake forever.

During the deterministic burst, on a positive stored sentinel both next-filler children carry the same positive loss

`L(0)=L(1)=ell_r=1/(r+1),`

so the exact fair premium equals the certain payout. Thus on the branch whose N stored sentinels are all positive,

`W(v)=1`

throughout the burst while

`E(v)=sum_{r<N}1/(r+1).`

After the N-th copy there are no further positive tickets.

The mode switch and both component gadgets use only computable finite state. They are concatenations of the settled adaptive no-repeat least-fresh constructions. Every nontriggering continuation omits at most its current sentinel, while the control and deterministic-burst epochs consume their sentinels. Hence the resulting scan remains everywhere total, fair-coin preserving and globally k=2. This is a ticket-stream boundary example, not a new randomness-destruction witness.

### Lemma 2 — semantic coercivity holds

Every Mode-B run has finite E: either no burst occurs or one finite burst occurs and then positive tickets stop. Hence Mode B contributes no E-divergent run.

Any E-divergent run must therefore lie in Mode A, where the settled one-sided-trigger account is coercive. Thus the combined account is semantically coercive.

### Lemma 3 — no uniform modulus exists, even noncomputably

Fix capital target K=2.

For every real threshold T choose N so large that the harmonic partial sum

`sum_{r<N}1/(r+1) >= T.`

Take the Mode-B finite branch with unary code N and N positive stored sentinels. At the end of its burst,

`E(v)>=T`

but

`W*(v)=1<2.`

Therefore there is no finite threshold h(2) satisfying

`E(v)>=h(2) => W*(v)>=2`

uniformly over finite histories.

This defeats not only computable h but **every** uniform loss-to-capital threshold. Equivalently there is no nondecreasing unbounded floor g with `W*(v)>=g(E(v))` on all finite histories.

So semantic coercivity is strictly weaker than every uniform reserve-floor / retained-surplus modulus of this natural kind.

## 5. Sharp formulation of the obstruction

For integer K define the bad-capital tree

`B_K={v : W*(v)<K}.`

Semantic coercivity says:

> every infinite branch through B_K has bounded total realized skipped loss E.

A uniform coercivity modulus at K says the stronger statement:

> E is uniformly bounded over **all finite nodes** of B_K.

The construction above has, for K=2,

- every infinite branch through B_2 of finite E;
- but `sup{E(v):v in B_2}=infinity`.

Large finite-loss excursions occur on side branches which peel away later and later. Their limiting control branch has E=0. This is the exact cross-branch nonuniformity: branchwise boundedness does not imply a uniform bound over the bad-capital tree.

No computability issue is needed for the separation; uniform boundedness itself fails.

### Boundary consequence

If one adds the set-theoretic **loss-properness** condition

`b(K)=sup{E(v):W*(v)<K}<infinity`

for every K, then semantic coercivity upgrades to a uniform, possibly noncomputable threshold modulus by taking any h(K)>b(K).

If, stronger still, computable rational upper bounds for b(K) are available uniformly in K, one gets the effective modulus of Theorem 1.

P4-S018 does not prove that finite b(K) automatically has a computable bound in a computable k=2 ticket tree. That is the remaining effectivity layer.

## 6. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source, d its successful output martingale, H any total computable horizon selector, and J the associated P4-S016/P4-S017 full-ticket account.

P4-S016 already proves that along the sentinel-first completion C(Y),

`E(C(Y))=infinity.`

If J had a computable running-maximum coercivity modulus h, then for every integer K the completion prefix would eventually satisfy E>=h(K), forcing W*>=K. Thus J would be a total nonnegative computable martingale succeeding on C(Y).

But C is the settled P4-S001 effective isomorphism, so C(Y) is computably random. Contradiction.

Therefore P4-S011 admits no effective coercivity modulus for any computable horizon selector.

Indeed P4-S017 already rules out semantic coercivity itself, so every sufficient reserve-floor modulus fails a fortiori. As before, bare no-overdraft admissibility is not ruled out.

## 7. Successes and limits

Successful:

1. Identified the weakest natural local quantitative certificate for the existing proof: a running-maximum loss-to-capital modulus.
2. Proved that such a computable modulus suffices for the same one-martingale transfer.
3. Showed that it may be arbitrarily slow and remains strictly weaker than absolute premium summability.
4. Proved semantic coercivity does not imply even a noncomputable uniform modulus.
5. Isolated the exact cross-branch obstruction as unbounded finite E on the bad-capital tree despite bounded E on each infinite bad-capital branch.
6. Identified loss-properness `b(K)<infinity` as the exact set-theoretic condition restoring a uniform threshold.
7. Checked P4-S011 explicitly: it fails every effective modulus for every computable H.

Not claimed:

1. No computable bound is derived from mere finiteness of b(K).
2. No necessity theorem is claimed for transfer architectures other than the settled full-ticket plus restart decomposition.
3. The mode-switch example is a boundary example, not a new randomness-destruction witness.
4. No settled P4-S005 through P4-S017 result is reopened.
5. No result for k>2.
6. No novelty, Gate-4, publication or outreach claim.

## Preserved boundaries

P4-S011's exact k=2 destroyer is unchanged.
P4-S015's weighted theorem and savings wrapper are unchanged.
P4-S016's envelope-free last-chance-ticket theorem is unchanged.
P4-S017's semantic coercive self-financing reserve theorem is unchanged; P4-S018 shows only that a uniform effective modulus is a strictly stronger sufficient certificate.
PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
DEF-0020 is unchanged.

## Next bounded question

The remaining effectivity layer is narrower. Assuming the new loss-properness condition `b(K)<infinity` for every K, determine whether the computable k=2 ticket tree forces a computable upper bound on b(K), or whether finite but noncomputably bounded bad-capital loss can occur. This is the natural bounded P4-S019 question.
