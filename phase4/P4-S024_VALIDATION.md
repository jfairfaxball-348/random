# P4-S024 validation

Date: 2026-10-06
Session: P4-S024
Incoming checkpoint: \`4f0eef36aa6c2223528c1e48a8e300f0e9d29ec0\`
Pre-validation checkpoint: \`723eeca089b794ff01d531bb4ce7433f48efbe73\`
Scope: selected CAND-01; k=2 pointwise/branchwise tail sharpness only
Status: **VALIDATED**

## Repository and scope checks

- Live \`main\` matched the requested incoming checkpoint exactly before substantive work.
- Direct incoming-checkpoint path checks found no \`phase4/P4-S024_MATHEMATICS.md\`, \`phase4/P4-S024_CLOSE.md\` or \`phase4/P4-S024_VALIDATION.md\`; P4-S024 was unique.
- P4-S001 through P4-S023 mathematics records and required CAND-01 authority were read before the P4-S024 conclusion was committed.
- P4-S005 through P4-S023 remain treated as settled.
- P4-S011 and P4-S015 through P4-S023 are preserved.
- No result is claimed for k>2.
- No novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. Oracle-uniform branchwise effectivity

The positive lemma was checked against the exact bad-capital setup.

Under global admissibility the full-ticket capital process is a total computable nonnegative martingale, so \(B_K=\{v:W^*(v)<K\}\) is a computable finitely branching tree. It is pruned: from any node below K, recursively choose a child whose next martingale capital does not exceed the current value.

If one oracle functional returns a correct tail modulus on every \(X\in[B_K]\), its finite-use halting computations enumerate cylinders covering \([B_K]\). For any finite candidate family, coverage is semidecidable by searching for an empty level in the residual computable finitely branching tree. Compactness guarantees that some finite family covers. Taking the maximum of the finitely many returned moduli therefore yields a total computable global tail modulus.

Because \(B_K\) is pruned, the resulting branch bound applies to every finite bad-capital continuation beyond the frontier. The P4-S023 compactness/semantic anti-Zeno proof then applies. Thus the claimed oracle-uniform "weakening" is correctly identified as non-genuine.

### 2. Incompatible-branch comb arithmetic

For the selected index e the settled ladder gives

\[
E=2e,\qquad W^*=1+e,
\]

and the query is

\[
K_e=e+2,\qquad m_e=2e+2.
\]

At tooth t,

\[
\delta_t=2^{-(t+3)},\qquad N_t=2^{t+4}.
\]

A detected halt executes \(N_t\) deterministic tickets and adds exactly

\[
N_t\delta_t=2.
\]

No detected halt executes \(N_t-4\) tickets and adds

\[
(N_t-4)\delta_t
=2-4\cdot2^{-(t+3)}
=2-2^{-(t+1)}.
\]

Thus on divergence the selected-e tooth t ends strictly below \(m_e\), while on a halt at stage s every tooth \(t\ge s\) reaches \(m_e\) finitely.

Earlier indices j<e have total loss at most \(2j+2\le2e<m_e\). Advancing past e first reaches \(E=m_e\) exactly when ticket capital reaches \(K_e\), outside the strict bad-capital set. Therefore

\[
\operatorname{Reach}(K_e,m_e)\iff\Phi_e\downarrow.
\]

### 3. k=2 and admissibility checks

The construction uses only settled least-fresh components:

- zero-stake controls consume their sentinels;
- deterministic tooth tickets consume their sentinels and have exact price equal to certain payout;
- successful ladder advances increase ticket capital;
- a failed one-sided ladder stage stops future positive premiums and can omit only its current sentinel while exposing all others.

Hence the scan remains everywhere total, no-repeat, fair-coin preserving and globally fibre-bounded by two. Reserve 1 remains globally sufficient.

The construction is a ticket/restart boundary example, not a new computable-randomness destroyer.

### 4. Pointwise effectiveness and semantic anti-Zeno

For each fixed bad-capital K, only finitely many successful ladder advances can occur. After selection, a tooth executes one finite deterministic block and then stops positive tickets; the all-continue spine has no comb loss.

Therefore every infinite branch through \(B_K\) has finitely many positive-loss events and is eventually loss-constant. Each branch has an ordinary computable modulus obtained by hard-coding a stage after its last positive loss. No branch can converge to an integer boundary from below without finite attainment.

On a divergent machine,

\[
L(X_t)=m_e-2^{-(t+1)}\to m_e,
\qquad
L(X_\infty)=m_e-2.
\]

So the branch-limit loss is discontinuous at the all-continue spine. This verifies that the obstruction is genuinely cross-branch rather than a hidden one-branch Zeno tail.

### 5. Fixed-scale exhaustion and loss-properness

Individual tooth payouts have size \(2^{-(t+3)}\). For fixed n, only teeth with \(t\le n-3\) can contain payouts at least \(2^{-n}\). Below fixed K only computably finitely many ladder indices can be selected. Hence a computable global fixed-scale exhaustion depth \(G(K,n)\) exists.

The selected-index baseline plus one tooth adds at most a constant 2 beyond the settled linear ladder loss. The recorded coarse bound \(U(K)=2K+4\) is therefore safe. The example remains effectively loss-proper.

Uniformly vanishing subscale control fails as required: for arbitrarily fine n, a sufficiently late tooth realizes almost 2 total loss using only payouts below \(2^{-n}\).

### 6. No oracle-uniform modulus for the comb

On a divergent selected-e all-continue spine, any purported oracle-uniform \(1/2\)-tail-modulus computation uses only finitely many comb controls and returns a finite N. A later tooth agrees on all queried oracle bits but realizes more than 1 additional loss after N. Hence the same returned modulus is false on that tooth branch. This validates the strict separation between nonuniform pointwise moduli and a single oracle-uniform branch functional.

### 7. P4-S011

Under global admissibility, the settled P4-S011 sentinel-first completion of its computably random source has bounded total computable ticket-martingale capital but divergent realized skipped gain. Choosing K above the bounded capital puts the whole completion branch in \(B_K\) while \(E\to\infty\).

Thus P4-S011 fails even finite pointwise tail convergence on that bad-capital branch. Its exact k=2 destroyer is preserved; bare admissibility remains unruled-out.

## Authority synchronization checks

Before this validation commit, comparing the incoming checkpoint with \`723eeca089b794ff01d531bb4ce7433f48efbe73\` gave:

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
  - \`phase4/P4-S024_CLOSE.md\`
  - \`phase4/P4-S024_MATHEMATICS.md\`
  - \`phase4/README.md\`.

\`authoritative/STATE.json\` and \`phase2/candidates.json\` both parsed successfully and identify P4-S024 as the completed session and P4-S025 as the next bounded task.

CAND-01 now points to \`phase4/P4-S024_MATHEMATICS.md\` and records the oracle-uniform/nonuniform pointwise-tail split.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. Its prior-art file blob remains \`6de1aebd5f1b6b22de9e6535a503f3e0fbafb90c\`, unchanged from the incoming checkpoint.

DEF-0020 remains unchanged. Its definitions file blob remains \`d7052d72a82b5635634544c3f4eedd18383332e9\`, unchanged from the incoming checkpoint.

Durable decision: D-0046.
Failure/lesson guard: FL-072.
Owner/external blocker: **NONE**.

## Validation outcome

**PASS.**

P4-S024 is internally consistent with the settled authority, stays strictly at k=2, supplies the requested exact incompatible-branch obstruction for genuinely nonuniform pointwise convergence, records the stronger oracle-uniform positive boundary, explicitly preserves P4-S011, and synchronizes the next bounded task without making novelty, Gate-4, publication or outreach claims.
