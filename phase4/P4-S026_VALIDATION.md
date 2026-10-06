# P4-S026 validation

Date: 2026-10-06
Session: P4-S026
Incoming checkpoint: \`d4e7bedb3cb150c33c0ba84d6053035799da7e39\`
Pre-validation checkpoint: \`3a3b95da74f11606cdd0cfeacca9b5923a7f3afe\`
Scope: selected CAND-01; k=2 one-sided integer-boundary cap / completeness-collapse boundary only
Status: **VALIDATED**

## Repository and scope checks

- Live \`main\` matched the requested incoming checkpoint exactly before substantive work.
- Direct incoming-checkpoint path checks found no \`phase4/P4-S026_MATHEMATICS.md\`, \`phase4/P4-S026_CLOSE.md\` or \`phase4/P4-S026_VALIDATION.md\`.
- The only incoming commit-search hit for P4-S026 was \`b414f43a7f32806939be940d007afc145f8ca51f\`, message \`P4-S025 schedule P4-S026\`, changing only \`authoritative/NEXT_SESSION_PROMPT.md\`. It was forward scheduling, not an S026 session record. P4-S026 was unique.
- P4-S001 through P4-S025 mathematics records and required CAND-01 authority were read before the conclusion was recorded.
- P4-S005 through P4-S025 remain treated as settled.
- P4-S011 and P4-S015 through P4-S025 are preserved.
- No result is claimed for k>2.
- No novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. The boundary-certificate abstraction is genuinely weaker in syntax than full effective upper-semicontinuity

P4-S026 defines a uniformly c.e. relation \(\operatorname{BCert}(K,m,\sigma)\) with:

1. soundness:
   \[
   \operatorname{BCert}(K,m,\sigma)
   \Longrightarrow
   \forall X\in[B_K]\cap[\sigma]\quad L_K(X)<m;
   \]
2. completeness:
   whenever \(L_K(X)<m\), some prefix \(\sigma\prec X\) is certified.

This is exactly a c.e. effective-open presentation of the strict integer sublevel \(\{L_K<m\}\), not a complete rational upper approximation to \(L_K\).

A local rational cap \(q<m\) is a special case. An oracle-uniform integer-clearance functional whose finite-use computation returns a sound local cap below \(m\) also yields such a c.e. certificate system by enumerating its finite halting traces.

The abstraction therefore captures the intended one-sided boundary-modulus question without assuming P4-S025's arbitrary-rational upper-cap completeness.

### 2. The constant-loss representation separation is correct

Fix a c.e. noncomputable set \(H\) and put

\[
\alpha=\sum_{e\in H}4^{-(e+2)}.
\]

The full possible sum is

\[
\sum_{e\ge0}4^{-(e+2)}
=
\frac{1/16}{1-1/4}
=
\frac1{12}
<
\frac14.
\]

The base-4 expansion uses only digits 0 and 1, so \(\alpha\) is noncomputable when \(H\) is noncomputable. Its finite enumeration-stage partial sums form a computable increasing rational approximation, hence \(\alpha\) is left-c.e.

At stage \(s\), the total weight of indices first entering \(H\) at that stage is a computable rational \(a_s\). The settled deterministic-trigger gadget realizes certain payout \(a_s\) at exact fair premium \(a_s\). Because the payout is certain and equals the premium, the ticket-account capital is unchanged.

All such epochs consume their sentinels. The induced least-fresh scan is exhaustive, hence singleton-fibre, and therefore lies inside the global k=2 class. It is everywhere total and fair-coin preserving by the settled least-fresh scan calculations. The ticket account is globally admissible from its finite starting capital because every deterministic premium is exactly returned.

Every completion branch has

\[
E(X\upharpoonright s)=\sum_{t<s}a_t
\]

and branch-limit loss

\[
L_K(X)=\alpha
\]

for every K above the constant ticket capital.

Thus the branch-limit loss is the constant continuous function \(\alpha\).

### 3. Every integer boundary has an effective cap in the example

For every integer \(m\ge1\),

\[
L_K(X)=\alpha<1/4<m
\]

for every branch.

Therefore the root cylinder with fixed rational cap \(1/4\) is a sound certificate for every queried integer boundary. Completeness is immediate.

So the one-sided integer-boundary presentation exists uniformly.

### 4. A complete rational upper-cap basis cannot exist in the example

Suppose, toward contradiction, that the P4-S025 complete rational upper-cap basis existed.

Because \(L_K\) is constantly \(\alpha\), every sound cap \(q\) on any nonempty bad-capital cylinder satisfies

\[
q\ge\alpha.
\]

Completeness says that for every rational \(r>\alpha\), some enumerated sound cap has

\[
q<r.
\]

Hence the global enumeration contains rational upper bounds cofinal downward to \(\alpha\). After the first enumerated cap, taking the running minimum gives a computable nonincreasing rational sequence converging to \(\alpha\). Therefore \(\alpha\) is right-c.e.

But \(\alpha\) is also left-c.e. from the computable partial sums. A real which is both left-c.e. and right-c.e. is computable. This contradicts the choice of \(H\).

Therefore the example really separates integer-boundary effective caps from full effective upper-semicontinuity.

This validates the claimed representation-level weakening.

### 5. Bar plus semantic anti-Zeno gives strict branchwise separation

Fix \(K,m\) and assume the semantic anti-Zeno promise:

> no branch through \(B_K\) stays below \(m\) at every finite prefix while its losses converge to \(m\).

Assume \(\operatorname{Bar}(K,m)\). Then every finite bad-capital history has \(E<m\).

For any branch X, monotonicity gives

\[
L_K(X)\le m.
\]

Indeed if \(L_K(X)>m\), some finite prefix would already have \(E\ge m\), contradicting Bar.

If \(L_K(X)=m\), then every finite prefix is below \(m\) and the monotone prefix losses converge to \(m\), exactly the forbidden nonattaining Zeno behavior.

Hence

\[
\forall X\in[B_K]\quad L_K(X)<m.
\]

This is the only role of semantic anti-Zeno in the collapse theorem.

### 6. Boundary completeness semidecides true Bar

Under global admissibility, settled P4-S024 gives that \(B_K\) is a computable, finitely branching, pruned tree.

Enumerate the certified cylinders from the c.e. boundary system. For any finite family of certificates, remove their cylinders from \(B_K\).

Whether the residual tree has an empty level is semidecidable: each level is finite and membership in \(B_K\) and in the removed cylinder union is computable.

Because the residual tree is finitely branching, it has no infinite path iff some finite level is empty.

If Bar is true, Section 5 gives \(L_K(X)<m\) for every branch. Boundary completeness therefore supplies a certified prefix on every branch, so the certified cylinders cover \([B_K]\).

Compactness gives a finite subcover. The empty-residual-level search eventually detects one.

Soundness makes such a finite cover a valid negative certificate. Because \(B_K\) is pruned, any finite bad-capital node with \(E\ge m\) would extend to a branch with branch-limit at least \(m\), contradicting the covering certificates.

Therefore true \(\operatorname{Bar}(K,m)\) is uniformly positively semidecidable.

### 7. Decidable Reach and the P4-S020 modulus follow

\(\operatorname{Reach}(K,m)\) is already uniformly c.e.: enumerate finite bad-capital histories until one has \(E\ge m\).

Dovetail:

1. the positive Reach witness search;
2. the finite-cover Bar certificate search.

If Reach is true, the first halts. If Reach is false, Bar is true and, under semantic anti-Zeno, the second halts. Soundness prevents both outcomes.

Thus Reach is decidable on the promised class.

By settled P4-S020, decidable Reach uniformly recovers a computable loss-level witness modulus \(D(K,m)\).

So every c.e. sound boundary-complete local cap mechanism collapses to the already-settled P4-S020 final effective strength.

### 8. The collapse does not depend on rational caps

The proof used only:

- computable finite branching and pruning of \(B_K\);
- c.e. sound local neighborhoods;
- completeness for every branch with \(L_K<m\);
- semantic anti-Zeno to turn true Bar into strict branchwise separation.

No numerical tail modulus, fixed-scale exhaustion, residual-loss formula, continuity modulus or rational upper-cap approximation was used.

Therefore the collapse applies equally to:

- local rational caps below \(m\);
- local residual-loss bounds;
- oracle-uniform integer-clearance functionals;
- c.e. presentations of the strict integer sublevel;
- any c.e. local witness language whose certified neighborhood excludes \(m\).

The recorded claim that there is no genuinely new **c.e. all-boundary-complete** searchability class is therefore correct.

### 9. The abstract converse is correct on the same promise

Suppose true Bar is uniformly positively semidecidable on the semantic anti-Zeno promised class.

When that semidecision halts, enumerate the root as a boundary certificate.

On the promised class, Bar plus anti-Zeno gives \(L_K<m\) on every branch by Section 5, so the root certificate is sound and complete.

Thus, relative to the same promise, abstract c.e. boundary completeness and positive semidecidability of Bar have the same effective content.

This does not say every explanatory local cap presentation is identical mathematically. It says no such complete c.e. presentation can be weaker in final exact-boundary searchability.

### 10. Sharp remaining logical alternatives

To stay strictly below P4-S020 while retaining a one-sided boundary flavor, a future notion must drop at least one ingredient of the collapse:

1. c.e. enumerability of sound local exclusion certificates; or
2. completeness for every false queried boundary.

Limit-computable candidate caps or certificates available only on a cofinal subset of safe boundaries are possible weaker representations, but by themselves they no longer positively semidecide every true Bar instance.

The stopping point is therefore logically sharp for the task posed in P4-S026.

### 11. P4-S011

Let Y be the settled P4-S011 computably random source. Fix any computable horizon selector and suppose a finite reserve makes the canonical full-ticket account globally admissible.

The settled P4-S016/P4-S019 analysis gives divergent realized skipped loss on the sentinel-first completion \(C(Y)\). Global admissibility makes the ticket account a total nonnegative computable martingale, so its capital is bounded on the computably random completion. Choose K above that bound.

Then the entire completion branch lies in \(B_K\) and

\[
E(C(Y)\upharpoonright s)\to\infty.
\]

Therefore P4-S011 remains outside every hypothesis requiring a finite branch-limit loss throughout \(B_K\), including the full P4-S025 effective-upper-semicontinuity regime.

The weaker P4-S026 boundary system requires certificates only on branches with \(L_K<m\). The divergent P4-S011 branch belongs to no such strict sublevel. For this K every integer m is eventually reached on that branch.

Accordingly the S026 record correctly avoids claiming that P4-S011 refutes every boundary-only certificate system. The settled conclusions remain exactly:

- P4-S011's exact global-k=2 randomness destroyer is unchanged;
- under global admissibility, set-theoretic loss-properness fails;
- bare no-overdraft admissibility remains unruled-out.

No stronger P4-S011 claim is made.

## Authority synchronization checks

Comparing the incoming checkpoint with the pre-validation checkpoint \`3a3b95da74f11606cdd0cfeacca9b5923a7f3afe\` gives:

- status: ahead;
- 13 commits ahead;
- 0 commits behind;
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
  - \`phase4/P4-S026_CLOSE.md\`
  - \`phase4/P4-S026_MATHEMATICS.md\`
  - \`phase4/README.md\`.

\`authoritative/STATE.json\` and \`phase2/candidates.json\` both parse successfully.

The synchronized state records:

- \`last_completed_session = P4-S026\`;
- \`recommended_next_session = P4-S027\`;
- Phase 4 remains OPEN;
- owner/external blocker: NONE;
- latest mathematics and close records point to P4-S026;
- the expected validation path is \`phase4/P4-S026_VALIDATION.md\`.

CAND-01 now points to \`phase4/P4-S026_MATHEMATICS.md\`, remains selected, and records both the integer-boundary representation separation and the boundary-completeness collapse.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No prior-art record changed relative to the incoming checkpoint.

No Phase-1 definition/catalogue file changed relative to the incoming checkpoint. The previously validated DEF-0020 record is therefore unchanged.

Durable decision: D-0048.

Failure/lesson guard: FL-074.

Owner/external blocker: **NONE**.

## Validation outcome

**PASS.**

P4-S026 is internally consistent with the settled authority, stays strictly at k=2, proves a genuine representation-level weakening from complete effective upper-semicontinuity to integer-boundary caps, proves that every c.e. sound boundary-complete mechanism collapses under semantic anti-Zeno to semidecidable Bar, decidable Reach and the P4-S020 witness modulus, explicitly preserves the exact scope of P4-S011, and synchronizes the next bounded task without making novelty, Gate-4, publication or outreach claims.
