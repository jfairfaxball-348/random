# P4-S019 validation

Date: 2026-10-06
Session: P4-S019
Incoming checkpoint: b71f3fff7e128cafc6eb0e225f7b3f00ce8dc7cd
Pre-validation main: 41242c63cfcd69281d06acf8aef8741be71d022b
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 loss-properness effectivity boundary
Validation result: **PASS**

## Authority and uniqueness

- Live main matched the requested incoming checkpoint b71f3fff7e128cafc6eb0e225f7b3f00ce8dc7cd before substantive work.
- A second main check immediately before the first P4-S019 write still matched that checkpoint.
- Incoming repository commit search returned no committed P4-S019 record, so the session identifier was unused.
- P4-S001 through P4-S018 were read as mathematical authority.
- Required CAND-01 selection/Gate-3 authority, PA-0001 and DEF-0020 were checked.
- P4-S005 through P4-S018 were treated as settled.

## Mathematical validation

### 1. General effectivity calculation

For each integer K, finite ticket histories are computably enumerable and E(v), W*(v) are computable rationals. Enumerating E(v) over W*(v)<K therefore gives a uniformly increasing computable rational approximation to b(K). Hence b is uniformly lower semicomputable.

A total computable upper bound U(K)>=b(K) yields the P4-S018 threshold h(K)=U(K)+1. Conversely any computable P4-S018 threshold h bounds b(K) by h(K). The equivalence claimed in P4-S019 is therefore correct up to the stated harmless margin.

### 2. Counterexample remains inside the settled k=2 architecture

The construction uses only:

- immediate zero-stake consumed-sentinel controls and waits;
- the settled P4-S017 one-sided-trigger gadget;
- the settled P4-S017 deterministic-trigger gadget;
- the settled P4-S015 savings wrapper.

The controller has finite computable state. A nontriggering one-sided epoch omits exactly its sentinel and then enumerates every other source coordinate. All control, waiting and deterministic-trigger epochs consume their sentinels. Hence every transcript has either one permanently omitted coordinate or no omitted coordinate.

Therefore the induced least-fresh scan is everywhere total, computable, no-repeat, fair-coin preserving and globally k=2, exactly as claimed.

### 3. Global ticket admissibility

With reserve R=1, a positive-cost one-sided ticket has price ell_r/2<=1/2. A win nets +ell_r/2 and continues; a loss costs ell_r/2 and enters a branch with no later positive premiums. Deterministic tickets have price equal to payout and hence zero net cost. Zero-stake epochs cost zero.

Thus no run overdraws the account.

The Mode-A all-positive continuing branch has sum pi_r=(1/2)sum_r 1/(r+1)=infinity, confirming that P4-S019 does not restore absolute premium summability.

### 4. Loss-properness

Let H_n=sum_{r<n}1/(r+1) and P_n=1+H_n/2. For K>1 choose n_K least with P_{n_K}>=K.

Mode A bad-capital histories have E<2(K-1), apart from a final losing ticket which does not increase E.

A Mode-B machine index e can reach its waiting/burst phase below K only when e<n_K. There are finitely many such indices. A divergent Phi_e contributes only E=H_e; a halting Phi_e contributes at most H_{e+t_e} for its finite halting time t_e. Control and partial-ladder histories have uniformly bounded E.

Therefore b(K)<infinity for every K. For K<=1 the bad-capital set is empty because initial reserve is 1.

### 5. No computable uniform majorant

For each e, let K_e=floor(P_e)+1, so P_e<K_e.

If Phi_e halts after t steps, the all-positive Mode-B finite history after the t-stage deterministic burst has W*=P_e<K_e and E=H_{e+t}. Thus any putative computable majorant U must satisfy H_{e+t}<=U(K_e).

Because harmonic partial sums diverge effectively, from e and U(K_e) one can compute T with H_{e+T}>U(K_e). A halting time t>=T is then impossible. Simulating Phi_e for T steps decides whether Phi_e halts, contradicting undecidability of the halting problem.

Therefore no total computable uniform upper bound on b(K) exists.

### 6. P4-S011 check

P4-S016 already gives cumulative realized skipped gain E=infinity along the sentinel-first completion C(Y) of the settled P4-S011 computably random source Y for every computable horizon selector.

If a globally admissible full-ticket account were loss-proper and W* stayed bounded on C(Y), an integer K above that bound would have finite b(K) but prefixes with unbounded E, contradiction. Hence loss-properness would force the ticket martingale unbounded on C(Y).

Global admissibility makes that account a total nonnegative computable martingale, while P4-S001 preserves computable randomness from Y to C(Y). Contradiction.

Thus every globally admissible P4-S011 full-ticket account fails loss-properness at some K. Bare admissibility alone remains unruled-out.

## Synchronization validation

Before this validation commit, comparing incoming checkpoint b71f3fff7e128cafc6eb0e225f7b3f00ce8dc7cd to pre-validation main 41242c63cfcd69281d06acf8aef8741be71d022b showed exactly 13 changed files:

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
- phase4/P4-S019_CLOSE.md
- phase4/P4-S019_MATHEMATICS.md
- phase4/README.md

The structured files parsed successfully. authoritative/STATE.json records P4-S019 as last completed and P4-S020 as next. phase2/candidates.json records the new P4-S019 loss-properness effectivity boundary while preserving CAND-01's unresolved prior-art/novelty disposition. authoritative/NEXT_SESSION_PROMPT.md names P4-S020 and stays strictly at k=2.

The incoming and pre-validation blob SHA for phase3/prior-art.json is unchanged at:

6de1aebd5f1b6b22de9e6535a503f3e0fbafb90c

Therefore PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

The incoming and pre-validation blob SHA for catalog/definitions.json is unchanged at:

d7052d72a82b5635634544c3f4eedd18383332e9

Therefore DEF-0020 is unchanged.

## Guards

- P4-S011 is preserved.
- P4-S015 is preserved.
- P4-S016 is preserved.
- P4-S017 is preserved.
- P4-S018 is preserved.
- P4-S005 through P4-S018 are not reopened.
- No k>2 claim is made.
- No novelty claim is made.
- Gate 4 is not reviewed.
- No publication or outreach work is performed.
- Phase 4 remains OPEN.
- Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Validation disposition

**PASS.**

P4-S019 has a checked negative answer to the automatic-effectivization question, a precise halting-time obstruction, an exact numerical effective strengthening, and an explicit P4-S011 check. The smallest next bounded task is P4-S020 as recorded in authoritative/NEXT_SESSION_PROMPT.md.
