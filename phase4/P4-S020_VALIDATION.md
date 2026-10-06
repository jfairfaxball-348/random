# P4-S020 validation

Date: 2026-10-06
Session: P4-S020
Incoming checkpoint: 4beb36e69158e9badccb2a80a6292772c11c8ed4
Pre-validation main: 1359421f4434379f8607e32171763651287651f8
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 loss-properness local-searchability boundary
Validation result: **PASS**

## Authority and uniqueness

- Live main matched the requested incoming checkpoint 4beb36e69158e9badccb2a80a6292772c11c8ed4 before substantive work.
- Incoming repository commit search returned no committed P4-S020 record, so the session identifier was unused.
- P4-S001 through P4-S019 were read as mathematical authority.
- Required CAND-01 selection/Gate-3 authority, PA-0001 and DEF-0020 were checked.
- P4-S005 through P4-S019 were treated as settled.

## Mathematical validation

### 1. The zero-loss-waiting negative result is well-formed

P4-S020 strengthens the P4-S019 machine-wait region by inserting scaled deterministic-trigger heartbeat tickets.

The scaling is available inside the settled architecture. P4-S012 permits computable rational fractional stakes. At a finite state with positive active savings risk, choose a positive rational stake small enough that the next favourable sentinel has positive skipped gain epsilon_s<=2^(-s-3). The deterministic-trigger gadget makes both next-filler children trigger once that favourable sentinel is stored, so the exact fair ticket price equals the certain payout epsilon_s. Ticket-account capital is therefore unchanged by a favourable heartbeat.

If the heartbeat sentinel is unfavourable, its positive skipped gain is zero. P4-S020 sends that continuation to a permanently positive-ticket-inactive tail. Hence a branch which will realize any later positive skipped gain cannot pass through an unfavourable heartbeat. Along every such continuing branch a favourable heartbeat occurs once per fixed heartbeat/control block, giving the stated fixed zero-loss waiting bound.

The sum of the heartbeat gains is at most 1/4, so a nonhalting machine branch still has finite total realized skipped gain.

### 2. Heartbeats do not remove the P4-S019 halting obstruction

On the all-favourable heartbeat continuation, the savings active risk is never decreased by a heartbeat. The total heartbeat multiplicative distortion is bounded by the computable product of (1+epsilon_s), with sum epsilon_s<=1/4. Consequently the original positive ladder and post-halt all-positive deterministic burst retain computable harmonic comparisons up to positive computable constants.

In particular:

- post-ladder bad-capital ticket capital still grows computably without bound with the unary machine index, so for fixed K only finitely many machine indices can reach their machine-simulation region while W*<K;
- a divergent machine adds only the bounded heartbeat tail after its finite ladder;
- if Phi_e halts after t steps, an all-favourable finite history below a computable capital threshold K_e acquires skipped gain bounded below by c_e sum_{j<t}1/(e+j+1) for a computable c_e>0.

Therefore every b(K) remains finite.

If U computably majorized all b(K), effective divergence of that harmonic lower bound would compute, from e and U(K_e), a finite T after which Phi_e could not halt. Simulating Phi_e for T steps would decide the halting problem. Thus the heartbeatized account has no computable uniform majorant.

The negative conclusion is therefore sharper than P4-S019's literal zero-loss-waiting presentation: bounded next-positive-loss waiting does not suffice.

### 3. The loss-level witness theorem is correct

Let

Reach(K,m) := exists v [ W*(v)<K and E(v)>=m ].

Finite histories, E(v), and W*(v) are computable, so Reach is uniformly c.e.

Assume a total computable D(K,m) such that whenever Reach(K,m) is true, some witness occurs by depth D(K,m). Exhaustive finite search through that depth decides Reach.

If the account is loss-proper, b(K)<infinity. Hence for every fixed K there is an integer m with Reach(K,m) false. Searching m=1,2,... and deciding Reach at each m therefore terminates. The first false m is a computable U(K) satisfying

W*(v)<K => E(v)<U(K).

Thus loss-properness plus the witness modulus gives effective loss-properness and, by P4-S019/P4-S018, a computable running-maximum coercivity threshold.

For K at or below the initial running maximum, B_K is empty and any default witness depth works; this harmless edge case does not affect the argument.

### 4. The searchability equivalences are valid

A witness modulus D decides Reach by bounded search.

Conversely, if Reach is decidable, then on a true instance one enumerates finite histories until a witness appears and returns its depth; on a false instance return any default depth. Hence a total witness modulus is computable.

If true Bar(K,m)=not Reach(K,m) instances are uniformly semidecidable, dovetail that bar procedure with the ordinary c.e. search for a violating history. Exactly one side succeeds, so Reach is decidable.

Therefore the recorded equivalence between witness modulus, decidable Reach, and uniform positive semidecidability of true loss bars is correct.

The weaker cofinal certificate relation described in P4-S020 is sufficient but is only a repackaging of effective loss-properness: a computable U supplies certificates above U(K), and one sound certified bar per K computes a majorant by search.

### 5. The condition remains below absolute premium summability

The settled P4-S017/P4-S018 one-sided-trigger H=1 account has an explicit linear relation W*>=1/2+E/2. Reachable integer loss levels therefore have computably searchable finite harmonic witnesses, while on the all-trigger positive branch

sum pi_r = (1/2) sum_r 1/(r+1) = infinity.

So the new searchability condition does not restore the P4-S016 absolute premium-sum hypothesis.

### 6. P4-S011 check

P4-S019 already proves the stronger exclusion. For the settled P4-S011 computably random source and any computable horizon selector, if a finite reserve makes the canonical full-ticket account globally admissible, that account cannot be set-theoretically loss-proper at every K.

Therefore P4-S011 cannot satisfy the hypotheses of the P4-S020 positive theorem. Bare admissibility alone remains unruled-out.

## Synchronization validation

Comparing incoming checkpoint 4beb36e69158e9badccb2a80a6292772c11c8ed4 to pre-validation main 1359421f4434379f8607e32171763651287651f8 shows exactly 13 changed files:

- AGENTS.md
- README.md
- ROADMAP.md
- authoritative/DECISION_LOG.md
- authoritative/NEXT_SESSION_PROMPT.md
- authoritative/SESSION_LEDGER.md
- authoritative/START_HERE.md
- authoritative/STATE.json
- docs/FAILURE_AND_LESSON_LEDGER.md
- phase2/candidates.json
- phase4/P4-S020_CLOSE.md
- phase4/P4-S020_MATHEMATICS.md
- phase4/README.md

The compare is a 13-commit fast-forward with no commits behind.

The structured files parse successfully. authoritative/STATE.json records P4-S020 as last completed and P4-S021 as next. phase2/candidates.json records the P4-S020 zero-loss-waiting/searchable-loss-level boundary while preserving CAND-01's unresolved prior-art/novelty disposition. authoritative/NEXT_SESSION_PROMPT.md names P4-S021 and stays strictly at k=2.

The phase3/prior-art.json blob SHA remains unchanged at:

6de1aebd5f1b6b22de9e6535a503f3e0fbafb90c

Therefore PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

The catalog/definitions.json blob SHA remains unchanged at:

d7052d72a82b5635634544c3f4eedd18383332e9

Therefore DEF-0020 is unchanged.

## Guards

- P4-S011 is preserved.
- P4-S015 is preserved.
- P4-S016 is preserved.
- P4-S017 is preserved.
- P4-S018 is preserved.
- P4-S019 is preserved.
- P4-S005 through P4-S019 are not reopened.
- No k>2 claim is made.
- No novelty claim is made.
- Gate 4 is not reviewed.
- No publication or outreach work is performed.
- Phase 4 remains OPEN.
- Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Validation disposition

**PASS.**

P4-S020 gives a checked negative answer for ordinary zero-loss/next-positive-loss waiting bounds, isolates loss-scale nonuniformity as the sharper obstruction, and gives a sufficient structural effectivization theorem via searchable reachable loss levels. The smallest next bounded task is P4-S021 as recorded in authoritative/NEXT_SESSION_PROMPT.md.
