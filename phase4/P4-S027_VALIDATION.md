# P4-S027 validation

Date: 2026-10-06
Session: P4-S027
Incoming checkpoint: `4bd698d8b0402bb03d5beabe01766d263476eb31`
Scope: selected CAND-01; k=2 bare-bankroll question for P4-S011 only
Status: **VALIDATED**

## Repository and scope checks

- Live `main` matched the requested incoming checkpoint exactly before substantive work.
- The incoming tree contained P4-S001 through P4-S026 and no P4-S027 mathematics, close or validation file. P4-S027 was unique.
- P4-S001 through P4-S026 and required CAND-01 authority were read.
- P4-S005 through P4-S026 remain settled.
- P4-S011 and P4-S015 through P4-S026 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. Use clipping is a harmless normalization of the P4-S011 witness

The committed SRC-0068 / THM-0076 record gives a wtt autoreduction with a computable use bound, and P4-S011 explicitly notes that the use bound is available although unnecessary for the destroyer conversion.

Given a target use bound u(j), modify the witness program to abandon a prediction if it attempts to query j or any coordinate outside a strict computable cap U(j)>u(j). The target Y never takes that abort because its wtt autoreduction computation stays within the use and avoids j. Hence all P4-S011 target predictions and the successful output martingale are unchanged.

On siblings an aborted computation is simply another permanently nontriggering epoch. The scan itself still emits fresh non-sentinel fillers forever, so the settled totality and global fibre-at-most-two argument remains valid.

Thus the normalization adds no totality assumption and does not promote wtt autoreducibility to truth-table autoreducibility.

### 2. The horizon is total and computable

For epoch state s with sentinel j and already queried set R_s, the count of still-unqueried non-sentinel coordinates below U(j) is finite and computable from s. Taking one plus this count gives a total computable finite horizon.

Because fillers are queried least-fresh first, this horizon exposes every coordinate the clipped predictor can inspect before the horizon is declared missed.

### 3. Later filler values cannot affect a trigger

After a miss, the clipped computation may still become visibly halting after more finite simulation time, but all oracle bits it can ever read are already fixed.

At any unresolved postmiss node, the two possible next filler children therefore have identical trigger status and, if triggering, identical prediction and identical deferred sentinel gain.

Hence (L_v(0)=L_v(1)).

### 4. Exact fair price equals exact payout

If neither child triggers, both losses and the premium are zero.

If both trigger, let their common positive skipped gain be (ell_v). Then
[
L_v(0)=L_v(1)=ell_v,qquad
pi(v)=ell_v.
]
The ticket pays (ell_v) on either child.

P4-S015 stake domination gives (0leell_vle1).

### 5. Reserve one proves global admissibility

Starting from R=1, every zero ticket does nothing. A positive ticket costs at most 1, so it is affordable; its certain equal payout restores the resolved account to 1.

By induction the canonical full-ticket account is nonnegative at every prescribed purchase on every sentinel-first completion branch and has resolved capital exactly 1.

This answers the P4-S027 existence question positively.

### 6. The target-path exclusions remain intact

P4-S016 proved that for every computable horizon selector, including this one, realized skipped gain diverges along the settled P4-S011 completion C(Y).

For the use-exhausting horizon, every positive premium equals the realized payout. Therefore both cumulative premium and cumulative payout diverge while ticket capital remains constant.

So:

- P4-S016 absolute premium summability still fails;
- P4-S017 coercivity still fails;
- P4-S018/P4-S019 loss-properness fails for every K>1 on this branch;
- none of the P4-S020 through P4-S026 transfer/searchability hypotheses is recovered;
- the ticket account does not succeed on the computably random completion, so P4-S011 is not contradicted.

### 7. Representation boundary is stated correctly

P4-S027 proves the positive bankroll result for a globally use-clipped representative of the wtt witness, available without changing target behavior. It does not claim that an arbitrary unnormalized off-target program representing the same wtt reduction must have the property.

That remaining distinction motivates the next bounded structural question rather than silently strengthening P4-S011.

## Validation outcome

**PASS.**

P4-S027 gives a globally admissible finite-reserve full-ticket account for the normalized P4-S011 destroyer, isolates the mechanism as effective exhaustion of a finite dependency frontier, and remains fully consistent with every settled negative transfer result.

Owner/external blocker: **NONE**.
