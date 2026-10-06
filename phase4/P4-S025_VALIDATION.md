# P4-S025 validation

Date: 2026-10-06
Session: P4-S025
Incoming checkpoint: \`2b6c46b63029c454cc5536cfc11d51786d0590a1\`
Pre-validation checkpoint: \`0aac1bae9bb5d0ff3e674533b18c973e9e4e5170\`
Scope: selected CAND-01; k=2 effective upper-semicontinuity / local tail-cap boundary only
Status: **VALIDATED**

## Repository and scope checks

- Live \`main\` matched the requested incoming checkpoint exactly before substantive work.
- Direct incoming-checkpoint path checks found no \`phase4/P4-S025_MATHEMATICS.md\`, \`phase4/P4-S025_CLOSE.md\` or \`phase4/P4-S025_VALIDATION.md\`; repository search found no incoming P4-S025 record. P4-S025 was unique.
- P4-S001 through P4-S024 mathematics records and required CAND-01 authority were read before the P4-S025 conclusion was committed.
- P4-S005 through P4-S024 remain treated as settled.
- P4-S011 and P4-S015 through P4-S024 are preserved.
- No result is claimed for k>2.
- No novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. Effective upper-cap basis really gives a uniform tail modulus

The proposed effective upper-semicontinuity representation is a c.e. basis of sound local upper caps \((\sigma,q)\) for the monotone branch-limit loss \(L_K\), complete in the sense that every branch and every rational \(r>L_K(X)\) eventually receives a cap \(q<r\) on some prefix.

For fixed \(\varepsilon=2^{-n}\), close each cap under extensions and retain finite nodes \(\tau\) satisfying

\[
q-E(\tau)<\varepsilon.
\]

Soundness gives, on every branch extending such a \(\tau\),

\[
0\le L_K(X)-E(\tau)\le q-E(\tau)<\varepsilon.
\]

These tight cylinders cover the whole bad-capital branch space. Indeed, along any branch X, ordinary monotone convergence gives a prefix whose current loss is within \(\varepsilon/2\) of \(L_K(X)\); local completeness then supplies a cap below a rational lying between \(L_K(X)\) and current loss plus \(\varepsilon\). Extending the two prefixes produces a tight cylinder.

Under global admissibility \(B_K\) is computable, finitely branching and pruned by the settled P4-S024 argument. Coverage of its compact path space by a finite family of cylinders is semidecidable by searching for an empty level in the residual tree. Effective compactness therefore finds a finite subcover. The maximum prefix length is a total computable uniform tail depth \(H(K,n)\).

Monotonicity then extends the bound from each covering prefix to every deeper prefix. The claimed compactification to a global uniform tail modulus is correct.

### 2. Converse upper-cap construction is correct

Given a computable global tail modulus \(H(K,n)\), every bad-capital node \(\sigma\) of depth at least \(H(K,n)\) has the sound cap

\[
q=E(\sigma)+2^{-n}.
\]

For any branch X and rational \(r>L_K(X)\), choose n with \(2^{-n}<r-L_K(X)\). The cap on X at depth \(H(K,n)\) is below r. Hence the complete effective upper-cap basis and computable global uniform tail convergence are equivalent here, up to harmless strict/non-strict rational margins.

This validates the key conclusion that complete effective upper-semicontinuity is not a genuine weakening of the P4-S023 tail regime.

### 3. Semantic anti-Zeno then yields searchable strict frontiers

With the recovered uniform tail modulus, false Reach(K,m) leaves every finite bad-capital loss below m.

If no strict frontier existed, for each n there would be a frontier node with

\[
E(v)+2^{-n}\ge m.
\]

A finitely branching diagonal argument, together with the uniform \(2^{-n}\) tail control, gives an infinite bad-capital branch whose limit loss is m. False Reach keeps every finite prefix strictly below m. This is exactly the forbidden semantic Zeno branch.

Therefore some finite strict frontier is found. Dovetailing its search with the ordinary c.e. positive witness search decides Reach(K,m), and the settled P4-S020 equivalence recovers a witness modulus D(K,m).

### 4. Delayed-activation comb arithmetic

After e successful index advances the selected-index branch has

\[
E=2e,\qquad W^*=1+e.
\]

The calibration block adds exactly 1 loss at zero net ticket-capital change, so the comb starts at

\[
E=2e+1,\qquad W^*=1+e.
\]

Set

\[
K_e=e+2,\qquad m_e=2e+2.
\]

At comb stage t,

\[
\delta_t=2^{-(t+3)},\qquad M_t=2^{t+3}.
\]

If a halt is visible, the full deterministic correction has total loss

\[
M_t\delta_t=1,
\]

so a surviving selected-e branch reaches \(m_e\) finitely while staying at ticket capital \(1+e<K_e\).

If no halt is visible and the tooth is taken, four deterministic tickets add

\[
4\delta_t=2^{-(t+1)},
\]

giving final loss

\[
m_e-1+2^{-(t+1)}<m_e.
\]

The all-continue divergent branch remains at \(m_e-1\).

Earlier selected indices \(j<e\) contribute at most \(2j+2\le2e<m_e\). Advancing beyond e first reaches ladder loss \(m_e\) when ticket capital reaches \(K_e\), outside the strict bad-capital set. Thus

\[
\operatorname{Reach}(K_e,m_e)\iff\Phi_e\downarrow.
\]

### 5. Continuity and semantic anti-Zeno checks

On a divergent selected-e comb, tooth-t branch limits are

\[
m_e-1+2^{-(t+1)}
\longrightarrow
m_e-1,
\]

which is exactly the all-continue spine limit. Hence the branch-limit loss is continuous at the comb accumulation branch.

If \(\Phi_e\) halts at stage s, only finitely many teeth \(t<s\) terminate below the boundary. Every branch surviving to stage s receives the same finite correction and then stops positive loss, so no discontinuity is introduced at the surviving component.

Below fixed K only finitely many ladder indices are possible. Failed ladder branches and all comb branches are eventually loss-constant. Therefore the branch-limit loss is continuous on the whole compact bad-capital path space, and every branch is semantically anti-Zeno at every integer boundary.

The construction therefore separates ordinary continuity from effective upper-semicontinuity exactly as claimed.

### 6. Fixed-scale exhaustion and effective loss-properness

Every stage-t comb payout has size \(2^{-(t+3)}\). Thus a payout at least \(2^{-n}\) can occur only for computably bounded t. Late halting corrections are split into many small deterministic tickets rather than one large ticket, so late halting does not violate fixed-scale exhaustion.

Below fixed K only computably finitely many ladder indices occur. The finite ladder/calibration pieces and finitely many coarse comb stages therefore admit a computable global fixed-scale exhaustion depth \(G(K,n)\).

A coarse linear total-loss bound such as \(U(K)=2K+4\) remains safe. The obstruction is not loss-properness or fixed-scale event effectivity.

### 7. Why no effective upper-cap basis exists for the comb

If a complete effective upper-cap basis existed uniformly for this construction, the validated compactification lemma would yield a computable global uniform tail modulus.

Combined with the already-verified semantic anti-Zeno property, the strict-frontier algorithm would decide every \(\operatorname{Reach}(K_e,m_e)\), hence decide whether \(\Phi_e\) halts.

Therefore the continuity of the branch-limit loss is necessarily non-effective in precisely the upper-cap/modulus direction. This validates the recorded obstruction.

### 8. Boundary-specific caps

If one supplies only sound local caps for the queried integer boundary and guarantees a finite cover whenever Reach(K,m) is false, effective compactness semidecides true Bar(K,m).

By settled P4-S020/P4-S022, this is exactly the missing negative semidecision needed for decidable Reach and recovery of the witness modulus. The claim that this is a weaker primitive syntax but not a new weaker final effective strength is correct.

### 9. P4-S011

Under global admissibility, the settled P4-S011 sentinel-first completion of its computably random source has bounded total computable ticket-martingale capital but divergent realized skipped gain. Choosing K above the capital bound puts the whole completion branch in \(B_K\) while

\[
E(C(Y)\upharpoonright s)\to\infty.
\]

Hence no finite branch-limit loss exists on that branch. P4-S011 therefore fails before the P4-S025 upper-semicontinuity question is reached. Its exact k=2 destroyer remains unchanged; bare admissibility remains unruled-out.

## Authority synchronization checks

Before this validation commit, comparing the incoming checkpoint with \`0aac1bae9bb5d0ff3e674533b18c973e9e4e5170\` gave:

- status: ahead;
- 13 commits ahead;
- exactly 13 changed files:
  - \`AGENTS.md\`
  - \`README.md\`
  - \`ROADMAP.md\`
  - \`authoritative/DECISION_LOG.md\`
  - \`authoritative/NEXT_SESSION_PROMPT.md\`
  - \`authoritative/SESSION_LEDGER.md\`
  - \`authoritative/START_HERE.md\`
  - \`authoritative/STATE.json\`
  - \`docs/FAILURE_AND_LESSON_LEDGER.md\`
  - \`phase2/candidates.json\`
  - \`phase4/P4-S025_CLOSE.md\`
  - \`phase4/P4-S025_MATHEMATICS.md\`
  - \`phase4/README.md\`.

\`authoritative/STATE.json\` and \`phase2/candidates.json\` both parsed successfully and identify P4-S025 as the completed session and P4-S026 as the next bounded task.

CAND-01 now points to \`phase4/P4-S025_MATHEMATICS.md\` and records the effective-upper-cap/uniform-tail equivalence plus the continuous delayed-activation obstruction.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The prior-art file blob remains \`6de1aebd5f1b6b22de9e6535a503f3e0fbafb90c\`, unchanged from the incoming checkpoint.

No Phase-1 definition/catalogue file changed relative to the incoming checkpoint. The previously validated DEF-0020 definition record is therefore unchanged.

Durable decision: D-0047.
Failure/lesson guard: FL-073.
Owner/external blocker: **NONE**.

## Validation outcome

**PASS.**

P4-S025 is internally consistent with the settled authority, stays strictly at k=2, proves that complete effective upper-semicontinuity compactifies back to P4-S023-level uniform tails, supplies an exact continuous-but-non-effectively-upper-semicontinuous halting obstruction, explicitly preserves P4-S011, and synchronizes the next bounded task without making novelty, Gate-4, publication or outreach claims.
