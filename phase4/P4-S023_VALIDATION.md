# P4-S023 validation

Date: 2026-10-06
Session: P4-S023
Incoming checkpoint: 6cae7e038730450463293da2559a0a31ead04daf
Pre-validation main: 1a5c91712dfc79d9939d2c036886e0e165110cfa
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 semantic anti-Zeno / effective-compactness boundary
Validation result: **PASS**

## Authority and uniqueness

- Live main matched the requested incoming checkpoint exactly before substantive work.
- The incoming tree contained P4-S001 through P4-S022 and no P4-S023 mathematics/close/validation record; repository search found no committed P4-S023 record.
- P4-S001 through P4-S022 were read as mathematical authority.
- Required CAND-01 selection/Gate-3 authority was checked.
- P4-S005 through P4-S022 were treated as settled.
- P4-S011 and P4-S015 through P4-S022 were preserved.
- Work stayed strictly at k=2.

## Mathematical validation

### 1. The strong tail hypothesis gives uniform Cauchy control

P4-S023 uses the strong P4-S021 form recorded by P4-S021/P4-S022: for fixed K and every n, a computable global depth exhausts all payouts of size at least 2^-n, and a computable bound T(K,n) controls the total sub-2^-n realized loss in B_K, with T(K,n) tending effectively to zero.

After taking a monotone closure of the exhaustion depths, every continuation of an n-quiet node can add at most the P4-S022 residual cap Q(K,n,v), and Q<=T(K,n).

Therefore along every infinite branch through B_K the monotone prefix-loss sequence converges, and the convergence is uniform with effective error bound T(K,n) after the n-th quiet frontier.

### 2. The branch-limit loss is continuous

At a fixed finite controller depth, prefix loss depends only on that finite history, hence is locally constant on branch space.

The branch-limit loss is a uniform limit of these finite-prefix functions. It is therefore continuous on the compact path space [B_K]. This is the correct compactness mechanism; no computable maximizer or direct effective maximum theorem is assumed.

### 3. False Reach plus semantic anti-Zeno gives a strict branch-level gap

If Reach(K,m) is false, every finite bad-capital history has E<m. A monotone branch limit cannot exceed m without producing a finite crossing.

Semantic anti-Zeno rules out equality at m for any infinite bad-capital branch. Thus every branch limit is strictly below m.

Classical compactness then implies a uniform strict gap at the branch-limit level. P4-S023 does not rely on this nonconstructive gap as an oracle; it proves that the finite P4-S022 certificate search must eventually discover one.

### 4. Failure of all finite strict frontiers would create a forbidden Zeno branch

Suppose false Reach holds but every fine-scale P4-S022 strict frontier certificate fails.

At each monotone quiet frontier choose a bad-capital node v_n with E(v_n)+Q(K,n,v_n)>=m. Since Q<=T(K,n),

m-T(K,n) <= E(v_n) < m.

The frontier depths tend to infinity. By finite branching, a diagonal subsequence of the v_n converges to an infinite branch X through B_K.

Fix an older quiet scale r. Sufficiently late selected nodes extend the limiting r-frontier prefix of X. Uniform tail control at scale r bounds the loss gained after that prefix by T(K,r). Combining this with the near-m lower bound on E(v_n), then letting n tend to infinity, gives

E(X at the r-frontier) >= m-T(K,r).

Letting r tend to infinity yields branch-limit loss at least m. False Reach yields at most m and keeps every finite prefix below m. Hence X converges to m from below without finite attainment, contradicting semantic anti-Zeno.

This validates the key theorem.

### 5. Incompatible branches do not evade the proof

The chosen near-boundary nodes may lie on mutually incompatible branches. The diagonal argument does not require them to be nested initially.

Uniform tail convergence is the essential extra fact: once two histories share an old quiet prefix, neither can acquire more than the old tail bound after that prefix. Therefore near-boundary mass cannot keep moving to late incompatible side branches while avoiding transfer to a compact limit branch.

The requested incompatible-branch halting construction is consequently impossible under the full P4-S023 hypotheses.

### 6. Reach is decidable and the witness modulus is recoverable

Reach(K,m) already has c.e. positive finite witnesses.

For the negative side, enumerate scales and test the finite P4-S022 strict frontier certificate. Under false Reach and semantic anti-Zeno, the compactness theorem guarantees that one test eventually succeeds.

Dovetailing the positive and negative searches decides Reach uniformly under the semantic promise.

P4-S020 already proved that decidable Reach yields a computable witness modulus D(K,m), so P4-S023 correctly recovers rather than circumvents that final effective strength.

### 7. The P4-S021 geometric example is excluded at exactly the right hypothesis

On the nonhalting selected-e branch of P4-S021, loss approaches m_e from below and never reaches it. That branch is a direct violation of semantic anti-Zeno.

Thus P4-S023 does not contradict P4-S021's halting-coded nonsearchability result. It adds exactly the semantic hypothesis that P4-S021's negative example fails.

### 8. Absolute premium summability is not restored

The settled one-sided-trigger harmonic account remains compatible with the P4-S023 bad-capital boundary behavior while retaining a divergent absolute premium sum on its unbounded all-trigger run.

Therefore the new semantic/effective compactness theorem does not collapse back to P4-S016 absolute premium summability.

### 9. Explicit P4-S011 check

Under global admissibility, the settled P4-S011 target completion has bounded ticket capital but divergent realized skipped gain. P4-S021 already shows that for every n, the contribution from gains below 2^-n is unbounded in one B_K.

Hence no finite strong-tail bound T(K,n) exists for P4-S011 under global admissibility. The P4-S023 theorem does not apply, and P4-S011's exact k=2 destroyer remains untouched. Bare admissibility remains unruled-out.

## Synchronization validation

Comparing incoming checkpoint 6cae7e038730450463293da2559a0a31ead04daf to pre-validation main 1a5c91712dfc79d9939d2c036886e0e165110cfa is a 13-commit fast-forward with no commits behind and exactly 13 changed files:

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
- phase4/P4-S023_CLOSE.md
- phase4/P4-S023_MATHEMATICS.md
- phase4/README.md

The structured files parse successfully. authoritative/STATE.json records P4-S023 as last completed and P4-S024 as next. phase2/candidates.json records the P4-S023 semantic anti-Zeno/effective-compactness result while preserving CAND-01's unresolved prior-art/novelty disposition. authoritative/NEXT_SESSION_PROMPT.md names P4-S024 and remains strictly at k=2.

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
- P4-S020 is preserved.
- P4-S021 is preserved.
- P4-S022 is preserved.
- P4-S005 through P4-S022 are not reopened.
- No k>2 claim is made.
- No novelty claim is made.
- Gate 4 is not reviewed.
- No publication or outreach work is performed.
- Phase 4 remains OPEN.
- Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Validation disposition

**PASS.**

P4-S023 establishes the promised semantic-to-effective compactness step under strong uniform tail convergence. The smallest next bounded task is P4-S024 as recorded in authoritative/NEXT_SESSION_PROMPT.md.
