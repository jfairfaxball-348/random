# P4-S080 — The committed z0 question is a universal question: admissible-model underspecification, GL(3,2) classification and the OH-certification gate

Date: 2026-10-09
Scope: Phase 4 Mathematics ONLY; selected CAND-01; pinned incoming live main `670bfaed2351827f8a1f6c57c42574c60f094dd0`.
Disposition: **PROVED that the committed record does not determine z0=R(X)∈OH. There is an admissible pair (Y1,M1), satisfying every hypothesis the record places on (Y,M), for which H⁻¹(Y1)∉OH, so the membership arm "z0∈OH against every legal raw scan" cannot be proved from the record. A derivation of X∉OH from the record is therefore exactly a proof of the universal proposition U(H): every computably random wtt-autoreducible Y has H⁻¹(Y)∉OH. U(H) is unresolved, so X∉OH is not established. U(K) is PROVED for every block matrix outside the 18-element no-unit-column double coset S₃AS₃, which is closed under inversion, so U(H)⇔U(H⁻¹). Any refutation of U(H), and any proof of R₂⊊OH, must establish that OH contains a non-MLR sequence; KLR⊆OH, so the route OH=MLR would answer QST-0001 affirmatively. U(H), X∈OH, fixed-S preservation, R₂=OH and R₂=OH^iso remain UNRESOLVED.**

## 0. Authority, uniqueness and frozen objects

Live remote `main` matched the pinned P4-S079 checkpoint exactly; the recursive tree had 79 consecutive mathematics/validation/close triplets and no P4-S080 file. Reviewed P4-S001–S079 through the phase summaries and the controlling detailed records (S011/S012, S027 §2, S032/S033, S037, S039–S049 summaries, S070–S079), S079 validation and close, selected CAND-01, the P3-S008 Gate-3 PASS, and both Phase-4 pivots. No discrepancy with the incoming prompt was found.

Retain MLR ⊆ R₂ ⊆ OH^iso ⊆ OH ⊊ CR. Preserve the ORIGINAL computably random Y, the unchanged syntactically self-avoiding globally use-clipped wtt autoreduction M, the repeated three-bit H with matrix A=[101;110;111] (rows; y₀=x₀⊕x₂, y₁=x₀⊕x₁, y₂=x₀⊕x₁⊕x₂), and X=H⁻¹(Y), with Y∉OH, X∉R₂, X∉OH^iso, and z₁,…,z₆∉OH from S079. Nothing below alters Y, M, H or X. The auxiliary pair (Y1,M1) of §2 is a *model of the record's hypotheses*, not a replacement for Y.

## 1. What the record actually fixes about Y

P4-S011 fixed Y existentially: "Fix a computably random sequence Y and an oracle machine M witnessing its wtt-autoreducibility", citing only the existence theorem SRC-0067/SRC-0068/THM-0076 (abstract- and statement-level access; no construction inspected). P4-S027 §2 calls the clipped M "a normal-form choice inside the settled existential P4-S011 witness". No later session added a hypothesis on Y that is not a consequence of these. Call a pair (Y,M) **admissible** if

* Y is computably random;
* M is an oracle machine with M^Y(q)=Y(q) for every q, which never queries q on input q on ANY oracle, and has a total computable use bound on Y;
* (normal form) M is globally use-clipped as in S027 §2. Every wtt autoreduction can be so clipped without changing its target behaviour, so this adds nothing.

Write WAR for the class of computably random sequences admitting an admissible M. Every theorem the programme has proved about "the committed Y" is a theorem about every admissible pair. Say that a statement about the committed X=H⁻¹(Y) *follows from the record* if it holds for H⁻¹(Y') for every Y'∈WAR. Only such statements can be derived from the record; a statement is *established* once such a derivation has actually been given.

## 2. An admissible model on which the committed question has answer "not in OH"

*Cap normalization.* An admissible N is clipped by S027 with a computable cap U: on every oracle, N(i) never queries i and never queries beyond U(i) (it abandons instead). The running maximum U'(i)=max(i+1, max_{i'≤i}U(i')) is a computable nondecreasing cap with U'≥U, and N already respects it on every oracle, so no re-clipping and no change of target behaviour is needed. Whether the cap is read strictly or non-strictly is immaterial below. We therefore assume U nondecreasing with U(i)>i.

**Lemma 1 (chained-substitution spreading).** Let (W,N) be admissible, with N globally clipped by a computable nondecreasing cap U(i)>i: on every oracle, N(i) queries only coordinates below or equal to U(i) and never i, otherwise it abandons. Define a computable bijection τ:ℕ×{0,1,2}→ℕ greedily: at stage n let i_n be the least unused number, j_n the least unused number >U(i_n), k_n the least unused number >U(j_n); set τ(n,0)=i_n, τ(n,1)=j_n, τ(n,2)=k_n. Put V(3n+r)=W(τ(n,r)). Then V∈CR and V has an admissible autoreduction M_V that is **block-avoiding**: on every oracle Z and input 3n+r, M_V reads no coordinate of block n={3n,3n+1,3n+2}.

*Proof.* τ is computable and injective by construction. At each stage the current least unused number is consumed as i_n, so the least unused number strictly increases and every natural number is eventually used; τ is a computable bijection with computable inverse. Hence V is a computable coordinate permutation of W, an effective isomorphism, and V∈CR by S001.

Define M_V on input 3n+r with oracle Z. For m∉{i_n,j_n,k_n} answer a W-query at m by Z(τ⁻¹(m)), a coordinate outside block n. (1) Run N(i_n). Its queries are ≤U(i_n)<j_n<k_n and never i_n, so it never asks for j_n or k_n; let b_i be its output. (2) Run N(j_n), answering a query at i_n by b_i; its queries are ≤U(j_n)<k_n and never j_n; let b_j be its output. (3) Run N(k_n), answering i_n by b_i and j_n by b_j; let b_k be its output. Output b_r for r=0,1,2 respectively (stopping after the needed step); a nonbinary output or an abandonment makes M_V diverge. On every oracle M_V reads only Z(τ⁻¹(m)) with m∉{i_n,j_n,k_n}, i.e. only coordinates outside block n. Since U is nondecreasing, every query lies at some m≤U(k_n), so the use is bounded by 1+max{τ⁻¹(m): m≤U(k_n)}, computable, on every oracle. On Z=V every answered value equals the true W-value: step (1) is exactly the target computation N^W(i_n); by induction steps (2) and (3) are exactly N^W(j_n) and N^W(k_n), since the substituted values are correct. Hence M_V^V(3n+r)=W(τ(n,r))=V(3n+r). M_V is already globally capped on every oracle, so (V,M_V) is admissible without further clipping. ∎

The essential point is that the wtt cap orders each triple so that every in-block query can be answered by an already computed in-block prediction; no sibling halting, divergence certificate or decisiveness is used.

**Theorem 2 (admissible model with every block recoding outside OH).** Let (V,M_V) be as in Lemma 1 and let K be any computable family of bijections κ_n of {0,1}³ applied on block n (in particular the repeated linear H, H⁻¹, or any blockwise GL(3,F₂) recoding). Then K(V) is computably random and wtt-autoreducible by a block-avoiding autoreduction; hence K(V)∉OH. In particular, with Y1=V and M1=M_V,

  (Y1,M1) is admissible and X1:=H⁻¹(Y1) ∉ OH;

and every intermediate of S078's chain built from X1, including z₀¹:=R(X1), lies outside OH.

*Proof.* K is an effective isomorphism, so K(V)∈CR by S001. To predict K(V)(3n+r) from an oracle Z: for every block m≠n compute the V-block as κ_m⁻¹ of the Z-block m; run M_V on 3n, 3n+1, 3n+2 using only these (M_V is block-avoiding); output the r-th bit of κ_n applied to the three results. No coordinate of block n of Z is ever read, the use bound is computable, and on Z=K(V) every value is correct. So K(V) is CR and wtt-autoreducible, and the P4-S011 least-fresh scan (or S079 Theorem 1 with J=ℕ) is a total computable no-repeat fair-coin-preserving globally one-hole scan with a computable martingale succeeding on it; thus K(V)∉OH. For H⁻¹ take κ_n=A⁻¹. Each S078 intermediate built from H⁻¹(V) is K_i(V) for a fixed blockwise matrix K_i (a product of R, Q, S and A⁻¹), so Theorem 2 applies to it directly. ∎

**Corollary 3 (record-level status of the primary target).**

(a) *The membership arm is not derivable.* No argument that uses only the record's hypotheses on (Y,M) can prove z₀=R(X)∈OH, equivalently X∈OH: such an argument would apply verbatim to (Y1,M1), contradicting Theorem 2. In particular "prove z₀∈OH against every legal raw scan" is unattainable from the committed record as it stands.

(b) *The nonmembership arm is exactly a universal theorem.* Define

  **U(H):** for every Y'∈WAR, H⁻¹(Y')∉OH.

X∉OH follows from the record's hypotheses if and only if U(H) holds; equivalently, a derivation of X∉OH from the record is exactly a proof of U(H). Since U(H) is unresolved, X∉OH is not currently established.

(c) *Failure of U(H) refutes H-preservation and gives R₂⊊OH and OH^iso⊊OH; R₂=OH^iso stays open.* If U(H) fails, choose Y2∈WAR with z:=H⁻¹(Y2)∈OH. Then H(z)=Y2∉OH by S011, so z∉R₂ by S033 Corollary 4, and R₂⊊OH; also z∉OH^iso by definition of OH^iso, so OH^iso⊊OH. Moreover OH is not H-invariant, so by S078 the fixed full shear S fails to preserve OH on some OH source. This does not decide R₂=OH^iso. In that case the record also admits both answers for the committed X (Y2 gives X∈OH, Y1 gives X∉OH), so X's membership is undetermined by the record.

(d) *Relation to fixed-S preservation.* Universal S-preservation implies H-preservation (S078 Theorem 2), which implies U(H) because WAR⊆CR∖OH. The converse implication is not claimed.

Thus the session's primary target is reformulated without loss: **decide U(H)**. A proof gives X∉OH for the committed Y (and for every admissible choice); a refutation gives R₂⊊OH but leaves the committed X undetermined by the record. The auxiliary model Y1 shows that the only other conceivable outcome, a proof of X∈OH from the record, is excluded.

## 3. The block-matrix landscape of the universal question

For K∈GL(3,F₂) acting on every block, write U(K) for: K⁻¹(Y')∉OH for every Y'∈WAR (here Y'=K(z)). So U(H) is U(A).

**Theorem 4 (classification of U(K) on GL(3,F₂)).**

1. If K has a unit column, U(K) holds.
2. U(PKQ)⇔U(K) for all 3×3 permutation matrices P,Q.
3. The invertible matrices with no unit column are exactly the double coset S₃AS₃; it has 18 elements and is closed under inversion. In particular A⁻¹∈S₃AS₃.

Consequently U holds on the 150 matrices outside S₃AS₃, is constant on S₃AS₃, and

  U(H) ⇔ U(H⁻¹), i.e. [∀Y'∈WAR: H⁻¹(Y')∉OH] ⇔ [∀Y'∈WAR: H(Y')∉OH].

*Proof.* (1) *Generalized unit-column lemma.* S079 Theorem 2 is stated for the committed (Y,M), but its proof uses only two facts: the autoreduction never queries q on input q on ANY oracle, and it halts correctly on the target at every row q(j), j∈J. It uses no use bound, clipping or sibling totality. Hence for every Y'∈WAR with admissible M', and every K with Y'=K(z) whose column t is the unit vector with its 1 in row q(t), the proof of S079 Theorem 2 with J={3k+t} and S079 Theorem 1 gives K⁻¹(Y')∉OH.

(2) (PKQ)⁻¹(Y')=Q⁻¹(K⁻¹(P⁻¹Y')). The blockwise coordinate permutation P⁻¹ is a computable permutation π of ℕ. It maps WAR onto WAR: translate the queries of M' through π; self-avoidance and target correctness are preserved, the new cap n↦max{π⁻¹(m): m≤U(π(n))} is computable (normalize it as in §2), and computable randomness is preserved by S001. Q⁻¹ preserves both OH and CR∖OH by S033 Theorem 5. As P⁻¹ is a bijection of WAR, U(PKQ)⇔U(K).

(3) Columns of weight at least two are 011, 101, 110, 111. The three weight-two vectors sum to zero, so an invertible matrix with all column weights at least two has columns 111 and two distinct weight-two vectors: 3 choices of the pair times 3! column orders gives 18 matrices. Row permutations act transitively on the weight-two vectors, so all 18 lie in S₃AS₃, and S₃AS₃ has no unit columns since permutations preserve column weights. A⁻¹ has rows [111;101;011], i.e. columns 110, 101, 111, so A⁻¹∈S₃AS₃, and (PAQ)⁻¹=Q⁻¹A⁻¹P⁻¹ gives closure under inversion. The coset is also closed under transposition, so the statement does not depend on the row/column convention; part (1) is stated for Y'=K(z) with column vectors. The exhaustive audit (§6) confirms these counts. ∎

Hence the whole remaining blockwise-linear question on WAR is concentrated in one 18-element double coset, and its two orientations (pulling back by H, pushing forward by H) are equivalent. This strengthens S079: the unit-column method is not merely sufficient for six intermediates of one word but decides the universal question on every coset except S₃AS₃.

## 4. What a counterexample to U(H) must look like, universally over autoreductions

Fix an admissible (Y',M'), X'=H⁻¹(Y') and a block b. Hiding raw x_{3b+r} leaves exactly two candidate Y'-blocks, v and v⊕a_r, where a_r is column r of A: a₀=111, a₁=011, a₂=101. Both candidates are computable from the other raw bits.

**Proposition 5 (target-only role refutation).** Say block b is *r-good for M'* if some q∈supp(a_r) has a target computation M'^{Y'}(3b+q) that queries no other coordinate of 3b+supp(a_r). Explicitly:

* 0-good: some in-block equation queries neither in-block mate on target;
* 1-good: M'^{Y'}(3b+1) does not query 3b+2, or M'^{Y'}(3b+2) does not query 3b+1;
* 2-good: M'^{Y'}(3b) does not query 3b+2, or M'^{Y'}(3b+2) does not query 3b.

If for some r all but finitely many blocks are r-good for M', then X'∉OH.

*Proof.* On an oracle Z, the predictor P(3b+r) forms the two candidate Y'-blocks from Z without reading raw 3b+r, runs the three block equations M'(3b+q) on the two candidate Y'-oracles, and halts as soon as one candidate receives a binary output different from its own q-th bit, outputting raw bit r of the other candidate. It never reads raw 3b+r on any oracle. On X' the true candidate is never refuted because M' is correct on Y'. If b is r-good with witness q, the false oracle Y'⊕a_r agrees with Y' on every coordinate the target computation at 3b+q reads, so that computation reproduces y'_{3b+q} while the false candidate claims its complement: a finite wrong-output refutation, hence a correct halt. For a cofinite set of r-good blocks, J={3b+r: b≥b₀} is infinite and decidable, and S079 Theorem 1 yields a globally legal winning raw one-hole scan. ∎

*Remark (relation to S040–S043).* r-goodness is a sufficient criterion for local Case A_r of S040: the false raw-adjacent companion is finitely refuted by a wrong-output halt of a local equation. The converse fails, since a companion can be refuted through a computation that does read the other support coordinates. The contact argument behind r-good ⇒ A_r is the contrapositive of S041 Theorem 4 (first-difference contact of a correctly halting companion computation) combined with S042 Theorem 1 (first changed-coordinate contact of a divergent one). The destruction step, cofinitely many A_r blocks ⇒ X'∉OH, was already available from S043 Theorem 2 with the constant role policy r, or S042 Theorem 5 with a delayed start. Because every theorem about the committed (Y,M) holds for every admissible pair (§1), those results already range over all admissible autoreductions. What is new in Proposition 5 is only a purely target-trace (query-graph) sufficient criterion for A_r.

**Corollary 5′ (necessary structure of a U(H) counterexample).** If Y2∈WAR and H⁻¹(Y2)∈OH, then for EVERY admissible autoreduction M2 of Y2 and each role r there are infinitely many blocks that are not local Case A_r (by the remark). Since non-A_r implies non-r-good, there are in particular infinitely many blocks with the target two-cycle {1↔2}, infinitely many with the target two-cycle {0↔2}, and infinitely many in which every block equation queries an in-block mate on target. Here a target two-cycle means that each of the two target computations queries the other coordinate somewhere in its trace; this differs from S041's first-difference graph, which is defined from companion computations.

The two-cycle statements are the target-observable consequence of the non-A_r condition. Every block-direction pair (b,r) of local status B or C, including the trapped old-hole blocks of S047–S049, is non-r-good, so its target traces on supp(a_r) contain a cycle. Remote radius-one divergence at locally decisive blocks (for example the (A₀,B₁,B₂) model of S042 Theorem 4) is not tied to a target cycle. None of this decides U(H).

## 5. The certification gate and its calibration

**Proposition 6 (KLR ⊆ OH).** Every Kolmogorov–Loveland random sequence (DEF-0012) lies in OH.

*Proof.* KLR⊆CR, since monotone strategies are non-monotonic strategies. If T is a total computable adaptive no-repeat one-hole scan and d a computable martingale succeeding on T(z), then "query the coordinate T chooses next and stake as d does" is a total computable non-monotonic betting strategy succeeding on z (replace d by an equivalent rational-valued computable martingale if rational stakes are required). ∎

DEF-0012 does not specify whether strategies are partial or total. The proof produces a total strategy, so the class of sequences random against all *total* computable non-monotonic strategies is already contained in OH, and so is KLR under either reading.

**Corollary 7 (where each outcome must come from).**

(a) Since MLR⊆R₂ (S032), every element of OH∖R₂ is outside MLR. Hence any proof of R₂⊊OH, and in particular any refutation of U(H) (Corollary 3(c)), must establish that OH contains a computably random non-MLR sequence; for a refutation of U(H) the non-MLR status is immediate, since Y2∉OH⊇MLR and H⁻¹ preserves MLR. Proposition 6 adds KLR⊆OH, but this yields no known non-MLR member: exhibiting an element of KLR∖MLR would itself answer QST-0001 negatively. Apart from that, the programme has no way to show that a given sequence is in OH beyond MLR⊆R₂⊆OH.

(b) If OH=MLR, then MLR=R₂=OH^iso=OH and U(H) holds: every Y'∈WAR lies outside OH by S011, hence outside MLR⊆OH, and H⁻¹ preserves MLR in both directions (THM-0035), so H⁻¹(Y')∉MLR=OH. But OH=MLR together with Proposition 6 would give KLR⊆MLR. The reverse inclusion MLR⊆KLR holds because the capital of any computable (possibly partial) non-monotonic strategy is a fair-coin martingale in the revealed-bit filtration. Here capital starts at 1, is indexed by the number of bets, stays nonnegative because stakes never exceed capital, and is frozen once the strategy diverges or would repeat a query; each next query position is a function of the revealed history and is fresh. By Ville's inequality the sets where the capital exceeds 2ⁿ are uniformly c.e. unions of cylinders of measure at most 2⁻ⁿ, a Martin-Löf test. This covers partial strategies, hence total ones too. So OH=MLR would give KLR=MLR under either reading of DEF-0012, i.e. an affirmative answer to QST-0001. The catalogue records QST-0001 as SOURCE-STATED OPEN (SRC-0018, with the SRC-0019 2025 status note). This is a programme deduction about difficulty calibration; P4-S080 makes no openness claim of its own.

(c) Consequently the question **OH = MLR?** inside CR is a one-sided gate for the north star. A non-MLR element of OH is necessary for any separation, but its existence does not by itself decide R₂=OH (R₂=OH could hold with MLR⊊R₂), and it does not resolve QST-0001. OH=MLR is a sufficient, not necessary, route to R₂=OH, of QST-0001 strength.

## 6. Validation of the finite components

`phase4/P4-S080_ADMISSIBILITY_AUDIT.py` verifies, exactly and exhaustively where finite: (1) |GL(3,F₂)|=168, the no-unit-column matrices equal S₃AS₃ (18 elements), closed under inversion, and every matrix outside it has a unit column; (2) the greedy τ is injective, exhausts initial segments, and satisfies j>U(i), k>U(j) for four caps over 400 blocks; (3) a toy finite model with synthetic adaptive, capped, self-avoiding, sometimes-divergent predictors N in which M_V never reads its own V-block on random oracles and is correct on V, and the derived raw predictor for X1=H⁻¹(V) never reads its own raw block and is correct (4 caps × 25 trials × 40 blocks); (4) 1408 role-refutation cases of Proposition 5. All pass. These checks support the finite algebra and the substitution logic only; computable randomness, wtt-autoreducibility on infinite sequences, OH membership and global one-hole legality are proved in §§2–5.

## 7. Failed or rejected routes

* Proving z₀∈OH from properties of the committed (Y,M): impossible by Corollary 3(a). A proof of X∈OH for the committed Y is impossible without a new commitment that pins Y down beyond the existential record, and such a commitment can make X∈OH true only if U(H) fails.
* Reading S041–S079's conditional results ("if X∈OH then …") as evidence about the committed X specifically: they are valid necessary conditions for every admissible pair and hence for any counterexample to U(H); they carry no evidence that X∈OH.
* Using absence of a unit column as an OH-membership argument (excluded, as instructed); Theorem 4 shows it only isolates the coset S₃AS₃.
* Limiting finite-support transfers (S077) or resuming finite price/escrow/hazard work: not used.

## 8. Disposition

Strict progress on the primary target: the question "is z₀=R(X) in OH?" is decided at the level of the record: it is not derivable that z₀∈OH, and z₀∉OH follows from the record exactly when U(H) holds, so deriving it means proving U(H). U(H) itself is unresolved, so z₀∉OH is not established. On GL(3,F₂) the universal question is settled everywhere except one 18-element coset, closed under inversion. The separation side of the north star requires establishing that OH contains a non-MLR sequence; the strongest equality route, OH=MLR, would answer the source-stated open QST-0001 affirmatively.

Unresolved: U(H), X∈OH (for the committed Y), universal fixed-S preservation, R₂=OH, R₂=OH^iso, OH=MLR.

Freeze all P4-S001–S079 results, including S011/S012, S027 clipping, S033, S037, S057 (exact four paired clipped traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 versus one ZERO; NOT invoked), S070–S079, and the original Y/M/H/X. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. No owner or external blocker.

Next: **P4-S081**, the OH-certification gate: construct a computably random non-MLR sequence in OH (a certification technique beyond MLR⊆R₂), or isolate an exact obstruction; if a certificate is found, test it for membership in R₂ or for H-image robustness, aiming at a refutation of U(H). A proof of U(H) remains an acceptable alternative outcome.
