# P4-S084 — Predictable errors and the balanced two-sheet tail-coded destroyer

Date: 2026-10-10. Phase 4 Mathematics only, CAND-01.
Incoming main: 4cb2a8b5b6a3a8b527704c3ee89b3a49c9d191ad (P4-S083 outgoing).
Outcome: PROVED structural theorems; R2 versus MLR UNRESOLVED.

## Authority and scope

P4-S084 is absent from the incoming tree and branch search. Reviewed mathematics P4-S001–S083 through the cumulative phase/authority records, with detailed checks of S004, S007–S008, S011–S012, S032–S033, S081 Theorem A, S082 §§2–7, S083 §§1–8 and its validation/closeout. CAND-01, Gate-3 PASS, both Phase-4 pivots and all prior results are frozen. No external literature retrieval: SRC-0019/SRC-0060 remain STATEMENT_INSPECTED; SRC-0069 proof inspected as recorded; SRC-0070/SRC-0072 ABSTRACT_INSPECTED; SRC-0071 preprint STATEMENT_INSPECTED, journal METADATA_ONLY. MLR=R_tot is an S083 programme deduction conditional on that preprint.

## Theorem 1: predictable extraction of computable randomness

Let y be computably random, and at each finite prefix u let a total computable rule either skip the next bit or select it with predicted bit p(u). If infinitely many bits are selected along y, the error sequence e_j=y(t_j) xor p(y prefix t_j) is computably random. In particular, the limiting frequency of errors is 1/2.

Proof. For any nonnegative rational computable martingale d on error strings, define a martingale D on all finite y-prefixes. At a skip set D(ub)=D(u). At a selected step set D(ub)=d(e(u) concatenated with (b xor p(u))), where e(u) is the error string already selected. Inductively D(u)=d(e(u)); the fair-child identity holds because b xor p permutes {0,1}. This total rational computable D succeeds on y whenever d succeeds on the infinite selected stream, contradiction. Its limiting 1-frequency is 1/2 by the standard computable fixed-fraction martingale strong-law proof. Global infinitude of selections is NOT required for totality of D.

Corollary 2. If z is in R2, y=G(z) with G=F_T* composed with Dprime from S083, and T* resolves infinitely on Dprime(z), then the resolution prediction-error stream is computably random and has limiting error frequency 1/2. The resolution flag and prediction are computable from the preceding virtual scan transcript (S083 Lemma 3.3), and G is total computable fair with fibres at most 2. In particular, if z were in S083's null class S AND R2, then by S083 Lemma 3.6 it would require frequency 1/2 wrong resolutions, each with S083 Lemma 3.4's anti-consistency certificate on r(q,m)=q+2m+4 positions. One fooling event is not enough.

## Theorem 3: the infinite-resolution input locus is effectively null

For q and nonempty guessed run epsilon of length m, let B(q,epsilon) be the S083 anti-consistency cylinder (empty unless the run finishes and has the required r(q,m) positions). Define E_Q as the union of B(q,epsilon) for all q>=Q and all epsilon.

Lemma 3.1. E_Q is uniformly effectively open, and measure(E_Q) <= sum over q>=Q,m>=1 of 2^m 2^(-q-2m-4) = 2^(-Q-3). Moreover, on each S083 true-run cylinder [sigma*_j], its relative measure is at most 2^(-Q-3). Proof: dovetail finite run completions; each cylinder has measure 2^-r; apply the geometric series and S083 Lemma 3.2's fixed-coordinate compatibility dichotomy.

Lemma 3.2. There is a total rational computable output martingale d_restart succeeding on every transcript with infinitely many T* resolutions and only finitely many incorrect predictions. For each output-time j let M_j start with 1 at time j, bet zero on fillers and all-in on T*'s predicted bit at resolutions after j. Define d_restart(u) = sum_{j=0}^{|u|} 2^(-j-1) M_j(u) + 2^(-|u|-1), where the last term is the exact tail of not-yet-started accounts. This is a computable rational martingale with initial capital 1. If mistakes stop after time t0, an account with j>t0 doubles at infinitely many subsequent resolutions.

Theorem 3. Let I={z: T* resolves infinitely on Dprime(z)}. Set
V_n = E_n union G^-1{y: exists t, d_restart(y prefix t) >= 2^(n+1)}.
Both parts are uniformly effectively open because G is total computable. By the fair pushforward property and the martingale maximal inequality,
measure(V_n) <= (1/8+1/2)*2^(-n) < 2^(-n).
If z in I has infinitely many mistakes, its strictly increasing hold coordinates q tend to infinity, and S083 Lemma 3.4 gives z in every E_n. Otherwise d_restart succeeds, putting z in the second part of every V_n. So I is contained in the Martin-Lof test intersection_n V_n. Thus every ML-random input has only finitely many T* resolutions.

## Corollary 4: a.e. balanced double fibres, exceptional singleton destruction

The UNCHANGED S083 map G=F_T* composed with Dprime has exactly two preimages for almost every output y, with conditional weights 1/2 and 1/2, despite the exceptional computably random non-MLR z of S083 Theorem 3.8 lying on a singleton fibre with G(z) non-CR.

Proof. Since G is fair and I has measure 0, almost every output transcript has finitely many resolutions. It then has precisely one permanently unread virtual coordinate q and determines every other virtual bit. The two virtual preimages differ only at q; applying Dprime inverse gives two raw preimages differing by the tail-complement involution J_q(z)=z xor 1_[q,infinity). Given any finite adaptive scan transcript, each unread fair source bit is conditionally unbiased, and its value never affects future queries until queried. Taking the conditional limit gives weights 1/2,1/2 on the two preimages. Conversely if resolutions are infinite the scan reads every virtual coordinate and the fibre is a singleton. S083's witness lies in this exceptional null set and is still destroyed.

Thus asymmetric conditional sheet weights from S004 are NOT needed for the already established strictness R2 proper-subset OH. Nothing is claimed for arbitrary k=2 maps or for R2=MLR.

## Direct attack and limitations

Attempted R2\MLR through S083's fooling set W: membership in W alone allows only one wrong prediction, while Theorem 1 forces an ENTIRE computably random error stream, with error frequency 1/2, on any infinitely resolving R2 candidate in S. No construction met these simultaneous requirements for T* and every other globally bounded-fibre map.

Attempted R2=MLR through a universal ML test and tail-pair orientation: the two raw completions J_q(z) are related by a computable fair homeomorphism, so both fail a universal ML test whenever z does. Merely being in all levels of that test cannot choose an orientation; finite-stage timings could still be useful. No uniform bounded-fibre implementation of Petrović's sequence-set strategy was obtained.

Exact counting potentials and the no-computable-modulus barrier from S082 remain open. R2 versus MLR, R2 versus OH^iso, OH^iso versus MLR, R_fin versus R2, U(H), X in OH, fixed-S preservation, block-H invariance, TKLR\MLR and QST-0001 are UNRESOLVED.

Finite check: 8,201 rational/integer checks passed using the P4-S084 extraction audit, covering a toy no-repeat scan, lifted predictable martingales, and geometric bounds. This is not an infinitary proof. No novelty, openness, prior-art, publication or outreach claims. Original Y/M/H/X, P4-S001–S083, S037, S057, PA-0001, DEF-0020, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN and Phase 5 CLOSED are frozen.

Next: P4-S085, focus exclusively on bounded-fibre universality or a high-entropy R2 survivor.
