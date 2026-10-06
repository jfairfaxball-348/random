# P4-S031 validation

Date: 2026-10-06
Session: P4-S031
Incoming checkpoint: 3acf92913c8c89dc32b718832d7966ab5ba0f6bb
Scope: selected CAND-01; k=2 repeatable no-frontier self-financing boundary only
Status: **VALIDATED**

## Repository and scope checks

- Live main matched the requested incoming checkpoint exactly before substantive work and immediately before writes.
- Repository search returned no committed P4-S031 record, so the session identifier was unused.
- P4-S001 through P4-S030 and required CAND-01 authority were read.
- P4-S005 through P4-S030 remain settled.
- P4-S011 and P4-S015 through P4-S030 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. The contracting stake functional is computable and self-avoiding

The current active scale is c=4^{-l}, where l is the number of earlier late triggers. In a least-fresh scan, every coordinate used in a completed earlier epoch lies below the next sentinel, so l and c are reconstructible without querying the current sentinel.

Inside the current epoch the functional queries one dummy and then only fresh non-sentinel coordinates until the first 1. The exposed stake is a rational computable function of c and the finite first-1 depth.

### 2. The induced scan is exact global-k=2

If an epoch never triggers, the scan remains there and queries every coordinate except its sentinel, yielding a two-point fibre. If every reached epoch triggers finitely, each sentinel is consumed and the next least-unqueried sentinel moves strictly right; every coordinate is eventually queried and the fibre is singleton.

Every output query is fresh and adaptively determined by earlier output bits, so the usual fresh-coordinate induction gives fair-coin preservation.

### 3. No finite dependency frontier is reintroduced

After the dummy and any finite zero search prefix, the next unseen filler can still distinguish continuation from a trigger. The associated stake is c at depth 1 and c2^{-m}>0 at every later finite depth. After any finite number of late renewals c remains positive. Thus every reached epoch has arbitrarily late genuinely one-sided tickets and no finite P4-S028 frontier.

### 4. The arbitrary-wrapper ticket bound is correct

During one epoch q is flat on fillers. Write beta=R_risk/q, so 0<=beta<=1.

For stored sentinel 1, the depth-1 ticket is (0,beta c) with premium beta c/2. At depth m>=2 it is (0,beta c2^{-m}) with premium beta c2^{-(m+1)}. The late premium tail sums to beta c/4. Hence the entire possible one-epoch gross premium exposure is 3 beta c/4 <= 3c/4.

For stored sentinel 0 the positive skipped gain is zero, so all canonical premiums are zero.

### 5. The reserve potential closes globally

Use invariant W>=c at the start of every active epoch.

An immediate stored-sentinel-1 trigger costs beta c/2 and pays beta c, so W increases by beta c/2 and the next scale remains c. A stored-sentinel-0 immediate trigger costs zero.

If the first search answer is zero, the whole current epoch can cost at most 3c/4. Starting from W>=c leaves at least c/4 even before crediting any late-trigger payout. A late trigger sets c'=c/4, so W'>=c'. If no trigger ever occurs, every finite partial premium sum remains below the same bound and no next epoch is reached.

Therefore R=1 with c=1 initially makes every prescribed purchase affordable on every completion branch.

### 6. Every finite trigger renews active no-frontier risk

There is no dead mode. Immediate triggers renew at c; late triggers renew at c/4, regardless of sentinel outcome. Both scales are positive. Therefore even after an arbitrarily late finite trigger the next epoch again contains an unbounded first-1 search with positive one-sided stakes at every depth.

### 7. Premium divergence and recycling are exact

On the completion with sentinel 1 and immediate first search 1 at every epoch, no scale contraction occurs, so c=1 forever.

After r favourable all-in renewals the settled savings wrapper has savings r, active risk 1 and q=r+1. Hence beta=1/(r+1), premium is 1/(2(r+1)) and payout is 1/(r+1). The premium sum diverges harmonically, while each ticket increases the reserve account by 1/(2(r+1)).

Thus the construction genuinely uses self-financing payout recycling and is not covered by P4-S016 absolute premium summability.

### 8. Settled comparison points remain exact

- P4-S030: late triggers terminalize future cost; P4-S031 instead renews at positive contracted scale.
- P4-S029: finite reserve follows from global absolute premium summability; P4-S031 has a divergent-premium run.
- P4-S028: one unresolved epoch carries constant 1/2 zero-payout premiums and unbounded deficit; P4-S031 makes each epoch's late exposure summable and contracts repeatable late renewals.
- P4-S011/P4-S027: tickets become deterministic after a finite dependency frontier; P4-S031 remains no-frontier and genuinely one-sided.

## Synchronization validation

- STATE.json advances the completed session to P4-S031 and schedules P4-S032.
- CAND-01 authority records P4-S031 without changing its exact formulation or PA-0001 disposition.
- Decision D-0053 and lesson FL-079 record the durable repeatable-renewal bankroll boundary.
- Session ledger, START_HERE, phase4 index, AGENTS, project README and ROADMAP are synchronized.
- PHASE_GATE_LEDGER.md is intentionally unchanged because P4-S031 is not a gate review.
- No blocker is introduced.

## Validation outcome

**PASS.**

P4-S031 removes terminalization: every finite trigger renews active no-frontier risk, while reserve R=1 remains globally admissible and harmonic premiums diverge on an immediate-favourable completion.

Owner/external blocker: **NONE**.
