# P4-S022 validation

Date: 2026-10-06
Session: P4-S022
Incoming checkpoint: 2abc3b536272fd5c8f903d8087e0328212445d11
Pre-validation main: e75b796409142c7d623fbf005fb8de3644097841
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 anti-Zeno / boundary-isolation searchability
Validation result: **PASS**

## Authority and uniqueness

- Live main matched the requested incoming checkpoint `2abc3b536272fd5c8f903d8087e0328212445d11` exactly before substantive work.
- The incoming repository commit search had no P4-S022 session record. Its only P4-S022 hit was the P4-S021 forward-scheduling commit, so the session identifier was unused.
- P4-S001 through P4-S021 were read as mathematical authority.
- Required CAND-01 selection/Gate-3 authority, PA-0001 and DEF-0020 were checked.
- P4-S005 through P4-S021 were treated as settled.
- P4-S011 and P4-S015 through P4-S021 were preserved.
- Work stayed strictly at k=2.

## Mathematical validation

### 1. The fixed-scale exhaustion frontier follows from P4-S021

P4-S021 already supplies, from its scale-tail hypotheses plus loss-properness, a computable total bad-capital loss bound (U(K)).

Fix (K,n), write (delta_n=2^{-n}), and let (R(K,n)) be the settled large-loss waiting modulus. Every payout counted at scale at least (delta_n) contributes at least (delta_n) to E. Therefore every bad-capital history contains a computably bounded number of such payouts, for example fewer than

[
N(K,n)=lceil 2^n U(K)ceil+1.
]

Whenever a later (delta_n)-large payout occurs on a bad-capital continuation, the P4-S021 waiting hypothesis places the first such payout after the current prefix within (R(K,n)) controller epochs. Iterating this along a branch shows that its j-th large payout, if present, occurs within a computable multiple of (jR(K,n)).

Consequently there is a computable global depth (G(K,n)) after which no node in (B_K) can have a future payout at least (2^{-n}). The fixed finite controller-encoding overhead can be absorbed into G exactly as in P4-S021's coarse-scale witness-depth argument.

Thus the P4-S022 scale-exhaustion lemma is correct.

### 2. The residual subscale cap is valid

Let v be an n-quiet bad-capital node at or beyond the scale-exhaustion frontier. Every future positive loss on a continuation through (B_K) is then below (2^{-n}).

P4-S021 supplies

[
E_{<n}(w)le T(K,n)
]

for every (win B_K). Since (E_{<n}) is monotone along histories, the additional future loss after v is at most

[
Q(K,n,v)
=
max{0,T(K,n)-E_{<n}(v)}.
]

Hence every bad-capital continuation (wsucceq v) satisfies

[
E(w)le E(v)+Q(K,n,v).
]

Therefore the strict inequality

[
E(v)+Q(K,n,v)<m
]

is a sound finite certificate that no continuation through v can reach the queried boundary m.

The strict inequality, rather than a nonstrict bound, is the only new anti-Zeno content used by the theorem.

### 3. Frontier separation decides false Reach instances

For fixed K,m,n, the finite tree through depth (G(K,n)) is computable. It is therefore decidable whether:

1. no node through that depth in (B_K) already has (Ege m); and
2. every bad-capital node v at the exhaustion frontier satisfies (E(v)+Q(K,n,v)<m).

If these conditions hold, every later bad-capital continuation passes through a frontier node and has total future loss bounded by that node's residual cap, so no later witness can reach m. The certificate is sound.

If every false (operatorname{Reach}(K,m)) instance eventually has such a finite scale n, then exact Reach is decidable by dovetailing:

- the ordinary c.e. search for a finite node with (Ege m); and
- the search over n for a valid strict frontier-separation certificate.

Exactly one search succeeds. The P4-S022 positive theorem is therefore correct.

### 4. The proposed bounded-crossing arm is redundant

A separate local clause saying that a reachable boundary must cross within a computable finite depth is stronger than the proof needs.

The positive predicate

[
operatorname{Reach}(K,m)
]

already has c.e. finite witnesses because the bad-capital ticket tree is computable. Thus the missing effective information after P4-S021 is only positive recognition of the negative predicate (operatorname{Bar}(K,m)).

The strict frontier-gap certificate supplies exactly that negative information. The P4-S022 reduction to a one-sided anti-Zeno certificate is valid.

### 5. No full Reach decision can remain strictly below the P4-S020 witness modulus in effective consequence

P4-S020 established the equivalence of:

1. a computable loss-level witness modulus (D(K,m));
2. uniform decidability of (operatorname{Reach}(K,m));
3. uniform positive semidecidability of true (operatorname{Bar}(K,m)).

P4-S022's effective boundary isolation supplies item 3, hence item 2. Once Reach is decidable, D is recovered uniformly: return any default value on false instances, and on true instances enumerate finite histories until the first witness appears and output its depth.

Therefore P4-S022 correctly distinguishes two senses of “weaker”:

- the strict-gap condition is more local and weaker as **primitive structural certificate data** than directly postulating D;
- it is **not** strictly weaker in final computability strength, because exact Reach decidability necessarily compiles back into D.

This logical limitation is essential and is synchronized into the decision/lesson records.

### 6. P4-S021 is the exact sharpness example for strictness

For the settled geometric machine-tail construction, fix

[
K_e=e+2,qquad m_e=2e+2.
]

On the selected-e nonhalting branch, every finite machine-tail prefix has loss below (m_e), while the exact remaining geometric mass is a positive computable rational (q_t) with

[
E(v_t)+q_t=m_e.
]

The residual tends effectively to zero and every fixed positive loss scale is exhausted by a computable deadline, but no strict gap ever appears.

If (Phi_e) halts, the settled finite correction block pays exactly the remaining residual and reaches (m_e).

Thus the weaker nonstrict information

[
E(v)+Q(v)le m
]

cannot decide finite attainment: the equality case carries the halting information. No additional construction is needed for P4-S022's negative sharpness statement.

### 7. Boundary isolation remains compatible with nonsummable absolute premiums

The settled P4-S017/P4-S018 one-sided-trigger harmonic example has a computable linear relation between E and (W^*). For fixed K, only computably finitely many positive trigger ranks can remain in (B_K) before the linear relation forces exit.

One can therefore choose a sufficiently fine computable loss scale below every positive payout still possible in (B_K). After its scale-exhaustion frontier the residual cap is zero, so every unreachable integer boundary has a strict frontier certificate.

Nevertheless its all-trigger absolute fair-premium sum remains harmonic and divergent. Hence P4-S022 does not restore the P4-S016 absolute-premium hypothesis.

### 8. Explicit P4-S011 check

Assume, exactly as in P4-S019 through P4-S021, that a finite reserve makes the canonical full-ticket account globally admissible for a computable horizon selector on the settled P4-S011 destroyer.

P4-S016 gives divergent realized skipped gain along the sentinel-first completion of the computably random source. Global admissibility makes the full-ticket account a total nonnegative computable martingale, so its capital is bounded on that computably random completion. Choose one K above the bound.

P4-S021 then proves that, for every n, cumulative realized loss from gains below (2^{-n}) is unbounded along prefixes in (B_K). Hence no finite (T(K,n)) exists.

Therefore P4-S011 fails before the P4-S022 boundary-isolation hypothesis is reached. The stronger settled failure of set-theoretic loss-properness is preserved. Bare admissibility remains unruled-out.

## Synchronization validation

Comparing incoming checkpoint `2abc3b536272fd5c8f903d8087e0328212445d11` to pre-validation main `e75b796409142c7d623fbf005fb8de3644097841` is a 13-commit fast-forward with no commits behind and exactly 13 changed files:

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
- phase4/P4-S022_CLOSE.md
- phase4/P4-S022_MATHEMATICS.md
- phase4/README.md

The structured state files parse successfully. `authoritative/STATE.json` records P4-S022 as last completed and P4-S023 as next. `phase2/candidates.json` records the P4-S022 boundary-isolation result while preserving CAND-01's unresolved prior-art/novelty disposition. `authoritative/NEXT_SESSION_PROMPT.md` names P4-S023 and remains strictly at k=2.

The `phase3/prior-art.json` blob SHA remains unchanged at:

`6de1aebd5f1b6b22de9e6535a503f3e0fbafb90c`

Its PA-0001 record remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

The `catalog/definitions.json` blob SHA remains unchanged at:

`d7052d72a82b5635634544c3f4eedd18383332e9`

DEF-0020 is unchanged.

## Guards

- P4-S011 is preserved.
- P4-S015 is preserved.
- P4-S016 is preserved.
- P4-S017 is preserved.
- P4-S018 is preserved.
- P4-S019 is preserved.
- P4-S020 is preserved.
- P4-S021 is preserved.
- P4-S005 through P4-S021 are not reopened.
- No k>2 claim is made.
- No novelty claim is made.
- Gate 4 is not reviewed.
- No publication or outreach work is performed.
- Phase 4 remains OPEN.
- Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Validation disposition

**PASS.**

P4-S022 identifies the exact first anti-Zeno certificate needed for exact boundary search: after computable fixed-scale exhaustion, a false loss boundary must eventually be **strictly** separated from a computable residual tail. This makes Bar positively searchable and hence Reach decidable. Because P4-S020 already characterizes exact searchability, the resulting decision procedure necessarily recovers a witness modulus; the gain is structural locality, not weaker final computability.

The settled P4-S021 geometric tail shows strictness is sharp, and P4-S011 remains outside the scale-tail regime under global admissibility.

The smallest next bounded task is P4-S023 as recorded in `authoritative/NEXT_SESSION_PROMPT.md`.
