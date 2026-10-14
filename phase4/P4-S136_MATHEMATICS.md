# P4-S136 — Dense restarts escape a *single* effective-null tree, not the source-randomness obstruction

14 October 2026. Owner-invoked ONE Phase4/CAND-01 mathematics session. Live entry main \`547269229ae7a370e18f186d826e23c9abbf2e39\`; prior S135 was authored atomically with sole parent \`be7655c2d7120a7649a65cdc6dfe44cb8ce92099\`, tree \`45f7296c87d3e53c63f93b8d94e1966bbce56d0d\`, and PR #34 closed/merged by fast-forward to the authored SHA. No S136 branch/record and no open PR on entry. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. All results here are INTERNAL mathematics, not external referee or novelty claims.

## A136. Complete computable dense-restarting F3 observer

Write X=2^omega, λ for fair measure. A total fair F3 observer has at most three **actual infinite** preimages over *each* y, not merely a finite aligned-cell cap. For additive use two, associate to every output τ of length m exactly four distinct input words of length m+2. Each source child appears in exactly one of the two rows of its output parent. This specifies a total computable map G, by reading m+2 source bits for m output bits, and immediately gives λ(G^-1[τ])=4·2^-(m+2)=2^-m for **all** τ.

NEW root row (all four length-two source cells):
 \`SAFE: [(P,00),(P,01),(S,10),(T,11)]\`.
A SAFE row has ordered cells \`[(P,p),(P,q),(S,s),(T,t)]\`. Its 0 child **ACTIVATES**, as
 \`ACTIVE r=0: [(A,p0),(A,p1),(A,q0),(B,s0)]\`;
its 1 child is again SAFE, with
 \`[(P,t0),(P,t1),(S,q1),(T,s1)]\`.
Thus every SAFE parent supplies each of its eight input children exactly once. The P-pair need not consist of sibling source cells; we do not assume this.

An ACTIVE row has relative age r since its most recent activation and is of shape A3/B1 when r≡0 or 1 (mod3), A2/B2 when r≡2 (mod3). Use S135's fully specified FREE/FORCED transitions but **reset forbidden siblings to the new SAFE(P2,S1,T1) form**:
* If r≡0 (FREE), send each of the four parents' 0 source children to output 0 and 1 source children to output 1. Both output rows stay ACTIVE, age r+1, preserving A3/B1.
* If r≡1 (FORCED) and row \`[(A,a),(A,b),(A,c),(B,d)]\`, child 0 is ACTIVE r+1 with \`[(A,a0),(A,a1),(B,d0),(B,d1)]\`; child 1 is SAFE \`[(P,b0),(P,b1),(S,c0),(T,c1)]\`.
* If r≡2 (FORCED) and row \`[(A,a),(A,b),(B,c),(B,d)]\`, child 0 is ACTIVE r+1 with \`[(A,a0),(A,a1),(A,b0),(B,c0)]\`; child 1 is SAFE \`[(P,b1),(P,c1),(S,d0),(T,d1)]\`.

In each case the two output children have exactly four cells each and together are EXACTLY the eight distinct children of the four source parents. By simultaneous induction over all output rows, they partition the entire source tree at every level (not a selected output spine). Their labels may change at SAFE restarts but true source-prefix words never collide. This proves computability, totality, full-support onto property and global λ-fairness.

Define D={y: from some finite stage onwards the row on y is ACTIVE at every later stage}. Entry into a permanent ACTIVE episode is followed by an arbitrary FREE bit and two forced zero bits, cyclically. Hence D is a countable union over computable finite activation prefixes ρ of closed sets \`[ρ]∩{tail after ρ has forced digits 0 at relative ages 1,2 mod3}\`. Each component is effectively closed, perfect relative to [ρ], and λ-null with tail mass 4^-j after j full cycles. Consequently λ(D)=0.

**D is dense:** any finite output prefix τ either currently is ACTIVE (continue with all forced zero digits forever) or is SAFE (choose its 0 child to activate, then continue forever in ACTIVE). Therefore every cylinder meets D. In particular D is contained in NO proper closed subset of X, and hence in NO *single* effectively closed null class. This is a genuine escape from S135's one computable perfect null tree; it is *not* a positive-measure persistent exceptional class.

**Exactly two actual inverses for every y∈D.** At the permanent ACTIVE entry the A and B sectors are nonempty disjoint source cones. At every subsequent level A and B remain nonempty; compactness gives at least one full path in each. At cofinally many relative r≡1 forced steps, only descendants of the FIRST A parent persist to the chosen active child; at cofinally many r≡2 forced steps only descendants of the FIRST B parent persist. Any two distinct full paths of the same label would separate at some finite level and then be incompatible with a later single-parent reset. Thus exactly one A and one B full inverse exist, i.e. degree exactly 2, on every y∈D. Occupancy endlessly cycles 3:1 -> 3:1 -> 2:2 -> 3:1.

**GLOBAL genuine cap at most three.** Let y∉D. Its row is SAFE infinitely often, since otherwise it would eventually be permanently ACTIVE. On *either* SAFE successor choice, at least one of the four compatible SOURCE parent cells is killed entirely: choose output0 and old T-parent disappears; choose output1 and the first old P-parent disappears. Suppose y had four distinct full inverse points. From some large level all four compatible source cells would belong to four distinct inverse paths. No subsequent child could ever kill any of those four parent cells, contradiction with the infinitely many SAFE visits. Every y has at least one inverse by compactness/onto-ness; therefore **1≤|G^-1(y)|≤3** for ALL y. Exact 1/2/3-degree stratification outside D is NOT claimed or proved. One must not infer every non-D output has degree 3.

**Positive-measure ACTIVE prefixes, null immortal paths.** Under fair y, the row-state distribution (S,A0,A1,A2) evolves by \`S->(S,A0)/2\`, \`A0->A1\`, \`A1->(A2,S)/2\`, \`A2->(A0,S)/2\`. This finite-state chain is irreducible and aperiodic and has stationary distribution (3/8,1/4,1/4,1/8). Therefore the measure of length-m ACTIVE output cylinders tends to **5/8**, even though λ(D)=0. Positive-measure ACTIVE snapshot ≠ positive-measure permanent oscillation.

## A136'. The dense exceptional set still has ONE computable rational SOURCE destroyer

Each component C_ρ of D is effectively closed null with an explicit clopen output approximation V_(ρ,j) that confines the tail to 2j forced zeros after 3j active positions; λ(V_(ρ,j))≤2^-2j times a fixed clopen-prefix price. Use 6j active tail positions to obtain λ(V_(ρ,j))≤2^-4j. Since G is total computable and globally fair, U_(ρ,j)=G^-1(V_(ρ,j)) is effectively clopen with exactly computable dyadic λ(U_(ρ,j))≤2^-4j. For length-j source word a, conditional fraction q_(ρ,j)(a)=λ(U_(ρ,j)∩[a])/λ[a]≤2^j λ(U_(ρ,j))≤2^-3j. All U_j are decided by some computable finite source precision; the additive-two modulus makes that explicit.

Set q_(ρ,j)(s)=λ(U_(ρ,j)∩[s])/λ[s], computable rational. Define M_(ρ,j)(s)=1 until depth j, and below length-j cone [a] let M=q(s)/q(a) when q(a)>0, else hold exactly 1. This is a unit TOTAL nonnegative RATIONAL source martingale, including zero-denominator guards. Along any x∈G^-1(C_ρ), the numerator becomes 1 after the deciding depth, so M_(ρ,j)≥2^3j. The ONE delayed rational mixture \`W_ρ(s)=sum_{1≤j≤|s|}2^-j M_(ρ,j)(s)+2^-|s|\` succeeds along every such x; the delayed tail is EXACTLY 2^-|s| and preserves the martingale equation.

Moreover enumerate all finite activation prefixes ρ_e and delay W_(ρ_e) at source depth e+1 by normalizing within each source length-(e+1) cone: V_e(s)=1 until e+1, then V_e(s)=W_(ρ_e)(s)/W_(ρ_e)(s|e+1). Denominator is strictly positive because W_ρ includes its positive rational delayed tail. V_e is a total unit rational martingale and still wins whenever W_ρ does. Then \`W_*(s)=sum_{e<|s|}2^-(e+1)V_e(s)+2^-|s|\` is ONE total ordinary rational source martingale that succeeds on **every** x with G(x)∈D. (Use indexing e=0,1,... and delay each account through depth e+1; unstarted accounts =1.) Hence G^-1(D) contains NO CR source and NO R2 source. Noncomputable outputs inside D do not change that.

## B136. Arbitrary outer factorization — both degree-drop types attacked, not resolved

For any globally fair F,H in F2, both are onto X (compact image plus fair full support). If G=H∘F, full fibres satisfy \`|G^-1(y)|=Σ_(z∈H^-1(y)) |F^-1(z)|\`, a sum of *actual full inverse* multiplicities, never a count of aligned prefixes. In S135, every off-T y has degree3 and forces exactly two H-inverses with inner multiplicities (1,2); on-T degree2 permits either H singleton / F-double, or H-double / two F-singletons. Both possibilities remain consistent with λ(H^-1[τ])=λ[τ] and λ(F^-1[σ])=λ[σ] at the cylinder level; pointwise degree algebra alone has not produced a contradiction. In the dense-restart G, the same alternatives hold for each y∈D, while a degree1 output outside D would additionally force singleton/singleton; the full outside-D degree distribution is not settled.

An attempted **first false inference** is: 'D is dense, so an outer singleton locus or two-singleton locus is too large for fairness.' False: density gives no positive λ-price; λ(D)=0. Likewise 'no globally clopen half-tag' excludes only an outer *shift* with a clopen first-bit selector (S134/S135), not an arbitrary continuous fair H. No arbitrary-H nonfactorability OR valid factorization was obtained.

## C136. Central hierarchy — tests and failures

Candidate G is legal in F3 but its explicit new degree-two exceptional paths are defeated by W_* on the SAME source. For x∈R2, no G(x)∈D. Outside D, G may have infinite restarts and degree at most three, but we neither constructed a nonCR output of an R2 input nor proved a general source compiler there.

* To prove R2≠R3, one must display **one** x surviving **every** legal F2 and every rational martingale, and one legal F3 plus an output winner. Membership in CR or noncomputability is insufficient; our D candidates fail already at CR.
* To prove R2=R3, one needs an arbitrary-F3 reduction to F2 tests, not merely an additive-two example or a one-surplus fibre lemma. S129 covers exact N-1 fibres, NOT our degree-two points.
* To prove R2=MLR or R3=MLR, the reverse implication must eliminate every nonMLR survivor through the relevant universal tests. No such result here.
* A composition H∘F of two F2 maps has up to four actual inverses; x∈R2 implies only F(x)∈CR, not F(x)∈R2. Hence F2(R2)⊆R2 and the R2/R4 equality or strictness remain unproved.
* R_fin is an intersection of universal ALL-k tests; \`∀k∃x_k\` would not yield \`∃x∀k\`. No such survivor is claimed.

## D136. Pointwise finite, nonuniform test, without an advertised witness

Take S130/S131's computable closed fat boundary C_t (measure≥1-2^-t) with decidable pairwise disjoint complementary cylinders [ρ_n]. Set Q(x)=x on C_t, and on [ρ_n] put \`Q(ρ_n u)=ρ_n(T_(n+1)∘G)(u)\`, where T_(n+1) is the S127 fair finite-prefix exact-(n+1)-fibred observer and G is the new dense-restart F3. Each patch is total, fair and has at most 3(n+1) true inverses per point; distinct patches and C_t cannot collide, so Q is globally fair and pointwise finite, with no uniform finite bound. Increasing patch-prefix length ensures effective continuity at C_t. It is nonhomeomorphic. Unlike S135's CR-safe patch, CR preservation of the NEW dense-restart core outside D has not been established, so the statement 'Q conserves CR' is NOT justified. Conversely no R_fin source with bad Q-image is exhibited. This is still piecewise and does NOT meet the ambitious beyond-piecewise boundary-interaction target.

## E136. Replay and precision limits

S135 original FREE/forced/SAFE rows rechecked: 3:1 at r0,1; 2:2 at r2; both forced siblings receive four distinct source cells; SAFE P2/S2 rows can begin non-sibling and remain fair. At 6j output bits, λ(T_6j)=2^-4j, and source U_j=G135^-1(T_6j) has the same price. The conditional bound at depth j is 2^-3j, with q=0 held at1. The one delayed mixture W has rational finite expression and arbitrarily large 2^2j gain on a source over T. **Independent-in-method SAME-AGENT finite sanity only**, not an infinite proof: at j=1 U_1 has 16 source cylinders at input depth8, price1/16; at j=2 U_2 has64 at input depth14, price1/256; exact conditional martingale guards tested.

S129's rational one-surplus rotation assumes degree \`2^c-1=3\` at c=2, inapplicable to present degree2 outputs. S131 permits the 3:1↔2:2 sequence but says nothing about global source winning. S132/S133 factorization covers clopen onto-sheet models; S134/S135 no-half-tag only applies to shift-outer. These restrictions cannot be silently promoted.

New row algorithm finite audit (Fraction/exact integer identities; file P4-S136_FINITE_AUDIT.py) checked m=0..12: **8,191** output cylinders, **32,764** source occurrences, and all **16,384** input prefixes at final depth14 assigned exactly once; 5,130 ACTIVE / 3,061 SAFE cumulative rows. (At output depth13 after the loop: 5,109 ACTIVE, 3,083 SAFE.) All sibling partitions and tag patterns PASS SANITY. The finite calculation cannot prove the infinite-fibre, dense/null or Markov convergence claims; those rely on the preceding induction, compactness, measure and finite-state arguments.

No external validation, new prior-art assessment, novelty promotion, Gate4, Lean, Palomar or publication. All frozen S101–S103 A–C, Y/M/H/X, DEF-0020, PA-0001 and grades remain intact.
