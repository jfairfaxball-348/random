# P4-S028 validation

Date: 2026-10-06
Session: P4-S028
Incoming checkpoint: e94ff739fc2fbc77f519ce0afb0458624ebfc673
Scope: selected CAND-01; k=2 dependency-frontier / reserve-demand boundary only
Status: **VALIDATED**

## Repository and scope checks

- Live main matched the requested incoming checkpoint exactly before substantive work.
- The incoming tree contained P4-S001 through P4-S027 and no P4-S028 mathematics, close or validation file; commit search returned no P4-S028 commit.
- P4-S001 through P4-S027 and required CAND-01 authority were read.
- P4-S005 through P4-S027 remain settled.
- P4-S011 and P4-S015 through P4-S027 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. The frontier hypothesis is strictly structural

The positive theorem assumes only a finite set D(s), computable from the reached epoch state, after whose exhaustion later trigger/no-trigger decisions and trigger values no longer depend on future filler values.

It does not assume a wtt use bound depending only on the sentinel input, off-target totality, a trigger deadline, or decidable eventual halting.

This is exactly the part of the P4-S027 use cap used by its bankroll proof.

### 2. The horizon really exhausts the frontier

Let m be the maximum of D(s) together with the sentinel. The least-fresh filler rule must expose every missing non-sentinel coordinate at most m after finitely many filler queries.

Counting those missing coordinates, plus one harmless extra filler, gives a total computable horizon. If the epoch misses it, D(s) is exhausted.

### 3. Equal trigger data give equal child losses

After frontier exhaustion, the next filler value cannot change whether the predictor/stake triggers next or its visible stake/prediction value.

The P4-S012 output martingale is flat on fillers, and the P4-S015 savings wrapper therefore remains flat there too. Hence the two filler children have identical pre-sentinel q-capital.

So each unresolved postmiss node has either loss vector (0,0) or (ell,ell). The exact fair premium is respectively 0 or ell.

### 4. Reserve one is sufficient

P4-S015 gives 0<=ell<=1. A positive deterministic ticket costs ell and pays ell on either child. Starting from reserve one, the purchase never overdraws and its resolution restores capital to one.

Induction proves global admissibility on every sentinel-first completion branch.

### 5. The first-1-search scan is exact global k=2

At the first epoch, sentinel 0 is withheld and coordinates 1,2,... are queried until the first 1 appears.

If no 1 appears, the scan queries every positive coordinate and omits only 0, so the fibre has exactly two points.

If a 1 appears, sentinel 0 is consumed. Every later predictor halts immediately and every later least-unqueried coordinate is consumed, so the scan is exhaustive and the fibre is a singleton.

Every query is fresh and selected from previous transcript data, so the usual P4-S011/P4-S012 fresh-coordinate induction gives fair-coin preservation.

### 6. No finite dependency frontier exists at the first epoch

After any finite collection of revealed zeros, a later unseen filler can still switch the future behavior: value 1 causes the prediction to become visible, while value 0 allows continued avoidance.

For any finite proposed frontier, choose a later coordinate outside it. Two completions agreeing on the frontier but differing at that coordinate have different trigger behavior. Thus the frontier condition fails.

### 7. The reserve lower bound is exact

On the sentinel-first branch with stored sentinel bit 1 and all filler bits 0, q remains at capital one.

After any finite horizon miss, at every unresolved node next filler 1 would cause an all-in winning sentinel trigger, giving positive skipped gain 1; next filler 0 leaves the epoch unresolved. Hence
\[
(L_v(0),L_v(1))=(0,1),\qquad \pi(v)=1/2.
\]

The actual all-zero branch receives payout 0 each time. After N tickets its net deficit is N/2. For every finite reserve R choose N>2R. A prescribed purchase then overdraws.

Therefore no finite reserve is globally admissible for any finite horizon selector.

### 8. P4-S011 remains consistent

P4-S027's global use clipping gives P4-S011 a computable finite frontier at every epoch. The positive theorem therefore recovers its R=1 account.

Its target still has divergent premiums and payouts with constant ticket capital. Nothing in P4-S028 restores coercivity, loss-properness or any P4-S020–P4-S026 transfer/searchability hypothesis.

## Validation outcome

**PASS.**

P4-S028 identifies finite dependency exhaustion as a sufficient structural explanation for P4-S027 bare solvency, proves that P4-S012 does not force it, and supplies an exact global-k=2 no-frontier witness with unbounded reserve demand after every finite horizon.

Owner/external blocker: **NONE**.