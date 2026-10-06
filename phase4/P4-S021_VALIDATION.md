# P4-S021 validation

Date: 2026-10-06
Session: P4-S021
Incoming checkpoint: baf6f7be7dfe30f475465d43e677235abee66518
Pre-validation main: 041a49c5836cb31ed5f5b0eafc1eadf1fe9fa321
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 scale-tail / boundary-attainment effectivity
Validation result: **PASS**

## Authority and uniqueness

- Live main matched the requested incoming checkpoint \`baf6f7be7dfe30f475465d43e677235abee66518\` before substantive work.
- Incoming repository search returned no committed P4-S021 record, so the session identifier was unused.
- P4-S001 through P4-S020 were read as mathematical authority.
- Required CAND-01 selection/Gate-3 authority, PA-0001 and DEF-0020 were checked.
- P4-S005 through P4-S020 were treated as settled.
- P4-S011 and P4-S015 through P4-S020 were preserved.

## Mathematical validation

### 1. The two-scale positive theorem is correct

Fix \(\delta_n=2^{-n}\). The P4-S021 large-loss waiting condition is formulated on finite bad-capital continuations: whenever a \(\delta_n\)-large payout is reachable from a node while remaining in \(B_K\), the first such payout is reachable within \(R(K,n)\) controller epochs.

If \(E_{\ge n}\ge q\) is reachable, take a first-crossing history. Every counted payout is at least \(\delta_n\), so at most \(\lceil q/\delta_n\rceil\) counted payouts occur before the first crossing. Applying the waiting bound successively after each counted payout gives a computable finite depth bound for one coarse-scale witness. Exhaustive finite search therefore decides \(\operatorname{ScaleReach}(K,n,q)\).

Under loss-properness, \(E_{\ge n}\) is bounded for every fixed n. Hence, at a fixed computable scale such as n=1, searching integer q eventually finds a false coarse-scale reachability instance. Adding the supplied computable bound \(T(K,1)\) for \(E_{<1}\) gives a computable upper bound on total E in \(B_K\).

Thus the P4-S021 scale-tail hypothesis plus set-theoretic loss-properness really does imply effective loss-properness. The proof does not assume exact Reach(K,m) decidability.

### 2. The hypothesis does not restore absolute premium summability

The settled P4-S017/P4-S018 one-sided-trigger H=1 account has a computable linear relation between bad-capital E and W*. Therefore its small-loss contribution has a computable bound and fixed-scale large-loss opportunities have a computable waiting schedule.

Its all-trigger positive branch still has harmonic exact fair premiums

\[
\sum_r \pi_r=\frac12\sum_r\frac1{r+1}=\infty.
\]

So P4-S021 remains strictly below the P4-S016 absolute-premium certificate at the exhibited fixed ticket stream.

### 3. The shrinking-scale boundary construction is coherent

The Mode-B index ladder uses only settled rational fractional stakes. A successful one-sided ticket with realized positive skipped gain \(\ell\) has price \(\ell/2\), hence net ticket-account gain \(\ell/2\). Positive rational gains can be accumulated until a prescribed rational block total is approached and the final stake can be scaled to hit the total exactly. Therefore an advance block with total E increment 2 and ticket-capital increment 1 is available effectively.

After selecting e, the machine-tail stages are numbered \(t=0,1,\ldots\). On nonhalting progress, deterministic-trigger blocks have total losses \(2^{-t}\). Their sum is 2. Every finite nonhalting prefix therefore has machine-tail loss strictly below 2, while the tail converges effectively to 2.

If a halt is observed before the next ordinary block, the remaining residual is a positive computable rational. A finite scaled deterministic-trigger block can pay exactly that residual. Deterministic-trigger ticket price equals certain payout, so this correction does not change ticket-account capital.

All controls and deterministic stages consume their sentinels. A permanently nontriggering one-sided epoch is the only possible source of an omitted coordinate and omits exactly its current sentinel. Hence the settled least-fresh argument gives an everywhere-total computable no-repeat fair-coin-preserving scan with global fibre bound k=2.

The reserve calculation is also valid: successful one-sided tickets increase ticket capital; a positive-cost failed one-sided continuation is sent to a positive-ticket-inactive tail; deterministic tickets have zero net capital change. Reserve 1 therefore gives global admissibility.

### 4. The halting equivalence has no false witnesses

For \(K_e=e+2\) and \(m_e=2e+2\), the selected-e machine tail has \(W^*=1+e<K_e\).

- If \(\Phi_e\) diverges, every finite machine-tail prefix has total E strictly below \(m_e\).
- If \(\Phi_e\) halts, the finite correction block makes E exactly \(m_e\) while W* remains \(1+e\).
- Earlier selected indices j<e have total E at most \(2j+2\le2e<m_e\).
- Passing from index e to e+1 reaches E=\(m_e\) exactly when ticket capital reaches \(K_e\), and that node is excluded by the strict bad-capital condition \(W^*<K_e\).
- Mode A obeys the settled linear W*/E relation and cannot reach \(m_e\) below \(K_e\).

Therefore

\[
\operatorname{Reach}(K_e,m_e)\iff\Phi_e\downarrow.
\]

A computable P4-S020 witness modulus would decide Reach and hence the halting problem. The claimed non-searchability follows.

### 5. Strong scale-tail control survives in the boundary construction

For fixed K, only finitely many index advances are possible while W*<K. For fixed n, a machine-tail block after sufficiently large t has total size below \(2^{-n}\), so no individual payout in that block reaches \(2^{-n}\). Any halting correction after such a late t is also below that scale.

The finitely many earlier schedules have computable lengths. Therefore a computable global deadline exists after which no \(2^{-n}\)-large payout occurs anywhere in \(B_K\).

The remaining geometric mass after stage t is computably small. Combining that with the finite set of earlier positive rational payouts and the finite Mode-A/index-ladder behaviour below K gives a computable subscale bound with an effective modulus tending to zero as n grows.

The construction also has an explicit computable linear bad-capital loss bound, so it is effectively loss-proper. It therefore separates exact loss-level searchability from effectivity of loss-properness rather than repeating the P4-S019 obstruction.

### 6. P4-S011 check

Under global admissibility, the P4-S011 full-ticket account is a total nonnegative computable martingale on the sentinel-first completion of the computably random source Y, so its running capital is bounded there.

P4-S016 proves that the realized skipped-gain sum along that completion diverges. For the all-in correct-prediction stream after the P4-S015 savings wrapper, the successive positive skipped multiplicative gains are \(1/(r+1)\); the horizon-missed subseries still diverges.

For every fixed n, all sufficiently late terms of that divergent subseries are below \(2^{-n}\). Thus cumulative subscale loss below \(2^{-n}\) is unbounded while W* remains below one fixed K. No finite \(T(K,n)\) can exist.

Hence P4-S011 fails the P4-S021 scale-tail hypothesis under global admissibility. The already-settled stronger fact that it fails set-theoretic loss-properness is preserved. Bare admissibility remains unruled-out.

## Synchronization validation

Comparing incoming checkpoint \`baf6f7be7dfe30f475465d43e677235abee66518\` to pre-validation main \`041a49c5836cb31ed5f5b0eafc1eadf1fe9fa321\` is a 15-commit fast-forward with no commits behind and exactly 13 changed files:

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
- phase4/P4-S021_CLOSE.md
- phase4/P4-S021_MATHEMATICS.md
- phase4/README.md

The structured files parse successfully. \`authoritative/STATE.json\` records P4-S021 as last completed and P4-S022 as next. \`phase2/candidates.json\` records the P4-S021 scale-tail/boundary-attainment result while preserving CAND-01's unresolved prior-art/novelty disposition. \`authoritative/NEXT_SESSION_PROMPT.md\` names P4-S022 and stays strictly at k=2.

The \`phase3/prior-art.json\` blob SHA remains unchanged at:

\`6de1aebd5f1b6b22de9e6535a503f3e0fbafb90c\`

Therefore PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

The \`catalog/definitions.json\` blob SHA remains unchanged at:

\`d7052d72a82b5635634544c3f4eedd18383332e9\`

Therefore DEF-0020 is unchanged.

## Guards

- P4-S011 is preserved.
- P4-S015 is preserved.
- P4-S016 is preserved.
- P4-S017 is preserved.
- P4-S018 is preserved.
- P4-S019 is preserved.
- P4-S020 is preserved.
- P4-S005 through P4-S020 are not reopened.
- No k>2 claim is made.
- No novelty claim is made.
- Gate 4 is not reviewed.
- No publication or outreach work is performed.
- Phase 4 remains OPEN.
- Phase 5 remains CLOSED.
- Owner/external blocker: **NONE**.

## Validation disposition

**PASS.**

P4-S021 supplies a checked positive structural effectivization theorem from local scale-tail data, proves that it remains compatible with nonsummable absolute premiums, and isolates a strictly narrower negative obstruction: exact finite attainment of a loss boundary can remain noncomputable even when total bad-capital loss already has effective bounds and every fixed loss scale has computable tail control. The smallest next bounded task is P4-S022 as recorded in \`authoritative/NEXT_SESSION_PROMPT.md\`.
