# P4-S030 validation

Date: 2026-10-06
Session: P4-S030
Incoming checkpoint: 45b0a3b0d5b2715f2b9886e826803aa2994dcd2f
Scope: selected CAND-01; k=2 no-frontier divergent-premium self-financing boundary only
Status: **VALIDATED**

## Repository and scope checks

- Live main matched the requested incoming checkpoint exactly before substantive work and immediately before writes.
- The incoming tree contained P4-S001 through P4-S029 and no P4-S030 result files.
- Commit search returned no P4-S030 commit, so the session identifier was unused.
- P4-S001 through P4-S029 and required CAND-01 authority were read.
- P4-S005 through P4-S029 remain settled.
- P4-S011 and P4-S015 through P4-S029 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. The stake functional is self-avoiding and computable

At a reached sentinel j, all earlier epoch coordinates lie below j because each least-fresh epoch consumes a contiguous block consisting of its sentinel and the fillers exposed before it. Therefore the active/dead history can be reconstructed from oracle bits below j without querying j.

In the current active epoch the functional queries only fresh non-sentinel coordinates: one ignored dummy, then an unbounded first-1 search. Its visible stake is rational and computable from the first-1 depth. Dead mode returns stake 0 immediately.

### 2. The induced scan is exact global-k=2

Every output step queries one fresh coordinate. If an active epoch never triggers, the scan remains there forever and queries every coordinate except its sentinel, giving a two-point fibre. If all reached active epochs trigger, every sentinel is consumed; after any late or unfavorable trigger the scan enters dead mode and consumes all later coordinates immediately. Hence all-trigger fibres are singleton and every fibre has size at most two.

Fresh-coordinate induction gives fair-coin preservation exactly as in P4-S011/P4-S012.

### 3. No finite frontier has been reintroduced

H=1 reveals only the ignored dummy filler. After any finite string of zero search fillers, a later fresh filler can still change the next-query behavior from “continue filling” to “trigger the sentinel”, and the associated stake remains positive at every depth m. Thus every active epoch has no finite P4-S028 dependency frontier and has arbitrarily late genuinely one-sided tickets.

### 4. The savings-wrapper gain calculation is exact

After r early favorable renewals, each earlier all-in favorable sentinel update took active risk 1 to 2 and caused exactly one unit to be saved, resetting active risk to 1. Thus q=r+1 with active risk 1.

The early fractional stake of q is therefore 1/(r+1)=a_r. A late output stake 2^{-m} gives q fractional stake a_r2^{-m}. These are exactly the positive skipped multiplicative gains on stored sentinel bit 1. Stored sentinel bit 0 gives positive skipped gain zero.

### 5. The ticket premiums and tail sum are exact

At depth 1 the ticket vector is (0,a_r), hence premium a_r/2.

For m>=2 it is (0,a_r2^{-m}), hence premium a_r2^{-(m+1)}. Therefore

[
sum_{m=2}^{infty}a_r2^{-(m+1)}=a_r/4,
]

and the whole zero-payout active-epoch exposure is 3a_r/4<=3/4.

### 6. Reserve 3/4 covers every completion

At the start of every renewed active epoch the ticket account has at least its initial 3/4. The early favorable branch pays net +a_r/2 and moves to the next active epoch.

If the early ticket loses, every later premium in that epoch has total remaining mass a_r/4. A late trigger only adds a payout before entering dead mode; an infinite zero continuation never leaves the epoch. Stored sentinel 0 and dead mode have zero positive-loss premiums.

Thus no branch can concatenate two unpaid full late tails, and every finite prescribed purchase satisfies the no-overdraft inequality.

### 7. Absolute premiums really diverge on one run

On the completion with stored sentinel 1 and immediate post-horizon filler 1 at every active epoch,

[
pi_r=1/(2(r+1)),qquad e_r=1/(r+1).
]

The premium sum is harmonic and diverges, so there is no P4-S016 finite absolute premium budget for H=1. Yet each ticket increases the bank by 1/(2(r+1)), proving that later purchases are genuinely financed by realized payouts.

### 8. Settled comparison points remain exact

- P4-S029: finite reserve comes from absolute summability; no recycling is needed.
- P4-S028: a zero-payout sibling carries constant premium 1/2 forever and forces unbounded deficit.
- P4-S011/P4-S027: finite-frontier tickets are deterministic and repay premium surely.
- P4-S030: tickets remain one-sided and no frontier exists; only the favorable renewing branch repays enough to continue, while every unreplenished tail has bounded total exposure.

## Synchronization validation

- STATE.json advances the completed session to P4-S030 and schedules P4-S031.
- CAND-01 authority records P4-S030 without changing its exact formulation or PA-0001 disposition.
- Decision D-0052 and lesson FL-078 record the durable bankroll boundary.
- Session ledger, START_HERE, phase4 index, AGENTS, project README and ROADMAP are synchronized.
- PHASE_GATE_LEDGER.md is intentionally unchanged because P4-S030 is not a gate review.
- No blocker is introduced.

## Validation outcome

**PASS.**

P4-S030 establishes an exact no-frontier global-k=2 bare-admissible ticket stream with arbitrarily late one-sided risk and divergent premiums funded by payout recycling.

Owner/external blocker: **NONE**.
