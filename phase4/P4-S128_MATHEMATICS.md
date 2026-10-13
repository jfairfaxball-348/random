# P4-S128 — Globally complete circulating surplus and finite-fibre hierarchy

ONE owner-invoked Phase4 CAND-01 mathematics session, 13 October 2026. Incoming live main b52437666f74a7ed3b5424f197dc875d3fb6b1c8, S127 commit merged by PR #26 as one atomic fast-forward with sole parent ddc6afe4e1a9678d949b772fb36a4728a041dea2, tree ad2daa762376afd88b6a37d659bc3afec4803c63. S128 unused at entry; Gate3 PASS, Phase4 OPEN. Claims here INTERNALLY argued only; separate adversarial audit.

Definitions: F_k is the class of total computable globally fair maps on 2^omega with at most k ACTUAL full inverse streams at EVERY output. R_k consists of CR sources whose images under ALL F_k observers are CR. R_fin=intersection over k of R_k, with UNIFORM finite cap for each observer. We use c fixed additive source-use overhead: the first m output bits are determined by m+c input bits.

## Theorem B128 — complete arbitrary computable-spine rotation

For every c>=2 put N=2^c, r=N-1. For ANY computable output stream z and computable tag sequence a_m from {0,...,r-1}, with a_0=0, there exists a total computable fair additive-c map G with EXACTLY r full infinite inverses above EVERY y, and whose N input cells at depth m+c above z|m are distributed among r tagged clopen source sectors as two in tag a_m and one in each other tag. In particular c=2 gives a complete F3 map with an indefinitely circulating fourth FINITE cell among three real streams. This map conserves CR and every R_j, so it is NOT a destroyer.

**Explicit algorithm on ALL output prefixes.** At depth zero assign the N source c-words to r tags, tag0 receiving two, each other tag one. Maintain for every output tau of length m EXACTLY N compatible distinct source m+c words. A distinguished MAIN node is tau=z|m, with tag counts (2,1,...,1); all other output nodes carry a SAFE state consisting of two PAIR words and N-2 SOLO words. All choices use lexicographic ordering and computable z(m),a_m.

At MAIN let old=a_m, new=a_(m+1), and b=z(m). Each compatible input word s has two children s0,s1. If new=old (HOLD), send BOTH children of the first old-tag word to output child b and BOTH children of the other old-tag word to 1-b. Split every other singleton, source child0 going to output0 and source child1 to output1. Main and sibling each receive N words: the main remains doubled in old tag; sibling becomes SAFE, with its two old-tag children marked PAIR and all remaining N-2 marked SOLO.

If new differs from old (SWITCH), from the first doubled old-tag word send source child0 to output b and source child1 to output 1-b; send BOTH children of the other old-tag word to sibling 1-b. Send BOTH children of the unique new-tag word to output b. Split all other tag singletons between output0 and output1. Main now has old1,new2,and each other tag1; sibling has old3,new0,other tags1. Crucially mark the ONE sibling child from the first old cell SOLO, the TWO sibling children of the second old cell PAIR, and all other sibling words SOLO. The sibling is therefore SAFE despite its (3,0,1) tag count for c2. Child counts: main 1+2+(r-2)=N, sibling 3+(r-2)=N.

At EVERY SAFE node choose its two PAIR source words p0<p1; send BOTH children of p0 to output child0 and BOTH children of p1 to output child1, all marked PAIR. Split each SOLO source word one child to output0 and one to output1, retaining SOLO. Each child receives precisely 2+(N-2)=N words, of which precisely two remain PAIR. This recursive algorithm defines the entire map, including ALL siblings and boundary outputs: no local rotation row is mistaken for a global map.

c2 schematic:
 MAIN (A,A,B,C), SWITCH A->B towards output0:
   child0 MAIN (A,B,B,C) [2 in B]
   child1 SAFE (A_s,A_p,A_p,C_s) [3 finite in A, only 2 actual A]
 SAFE (A_s,A_p,A_p,C_s) on each next output bit:
   one A_s child + TWO A_p children of a SINGLE prior A_p parent + one C_s child.
 Subscripts s and p mean SOLO and PAIR finite words, not separate full inverse streams.

**Proof of totality and use:** Every source word at depth m+c belongs to exactly one compatible output m-cylinder by induction; its two child words are each assigned exactly once to the two output child cylinders by the rule above. Hence every infinite input determines a unique consistent output at all m, computably from its first m+c input bits. Every input maps somewhere, and use is uniformly additive c.

**Proof of fair prices at EVERY cylinder:** At output depth 0 there are N=2^c source c-words. The HOLD, SWITCH and SAFE arithmetic above yields EXACT N compatible input words of length m+c at EVERY output tau length m. Therefore lambda(G^-1[tau])=N/2^(m+c)=2^-m. Thus G is globally measure preserving. Not merely a proof for z.

**Proof of ALL actual inverse counts:** For every output y either (i) y=z, or (ii) it has a unique FIRST departure from z and then remains forever SAFE. In SAFE, each of N-2 SOLO source words yields exactly one full inverse above every continuation (split 0/1 uniquely at each step). The PAIR contributes exactly ONE full inverse: on each output bit one of the two old PAIR words is completely rejected and the other contributes two children forming the new PAIR. Two distinct infinite inverses in the PAIR would eventually occupy both distinct old words and could not both survive the next output step. Nonempty nested finite compatible words yield existence. Thus SAFE produces (N-2)+1=N-1 full inverse paths, even at a SWITCH sibling with three same-tag finite cells.

For y=z, every initial tag has 1 or 2 compatible cells at every m, so finite-branching compactness gives at least one path per tag. If a tag has TWO at some MAIN m, both HOLD and SWITCH discard all main-branch descendants of one of the two at m+1; if it has ONE, it has only one candidate. Two distinct infinite paths of a tag would remain distinct at arbitrarily large depth, impossible. Thus exactly one genuine infinite inverse in EACH of r initial tag cones. There is NEVER a fourth actual inverse at c2 z or any sibling. At each aligned level N finite compatible words but r actual inverses: precisely ONE transient ghost.

**Source randomness boundary:** z and schedule are computable. Its r inverse paths are computable: at depth m, use main m+1 to decide which old cell survives if the tag was doubled; the source prefix stabilizes effectively. No such source is CR. Every other output departs at some finite stage, then its SOLO or PAIR source/output tails coincide up to a fixed finite prefix and fixed one-bit offset (PAIR outputs source bit identifying which old pair member survived). By S113/S127 finite-prefix invariance, CR and every R_j are preserved along these branches. Hence all CR sources map to CR, and G(R_j) subset R_j for all j. This is a SAFE class despite infinite rational output-posterior volatility along computable z. It does not decide universal F3 behaviour.

Schedule I: c2 z=000... and a_m=A,B,A,B,..., giving alternating occupancies (2,1,1),(1,2,1). Every SWITCH sibling has 3 old cells = SOLO1+PAIR2, plus third tag SOLO1.

Schedule II: c2 z=010101..., a_m repeating A,A,C,B,B,A, with distinct holds and switches, rotating among all three tags. At both output bit orientations and any FIRST departure the same SAFE proof applies.

General c: c3,r7, z_m=floor(m/2) mod2 and a_m=m mod7 illustrates full cycling among 7 cones. Any c>=2 and arbitrary computable schedule were proved by the identical counts. In S127 notation, q_tag(tau)=number compatible tag words / 2^c is a computable rational output martingale; along schedule I q_A(z|m) alternates 2/4 and 1/4. The rational volatility martingale from S127 wins on computable z, which DOES NOT yield a source-capital obstruction on a Schnorr-random NONCR target.

## A128 — attempted destruction and quantifier audit

A noncomputable Schnorr-random but noncomputably random target y cannot simply be substituted for the hardwired computable spine z: a transducer then requires uncomputable y bits to choose its transition. The first failed line is "read y(m) effectively." A decidable branching tree supporting infinitely many such y and compatible with global cap3/fairness is NOT constructed. Our computable-spine sources over z are themselves computable; offspine sources are finite-tail-safe. Therefore no triple CR inverse streams above an output with a rational winning martingale, no SAME-SOURCE x in R2\R3, no R2=R3 or R3=MLR, and no universal R2=MLR theorem. Output q volatility cannot be applied to prove CR source failure without a source compiler. All these targets OPEN.

## C128 — factorization and iteration

Necessary degree-three factorization invariant: suppose G=H∘F with G everywhere EXACTLY three-to-one, H,F each fair total cap2. Both F,H are surjective (compact image plus fair full-support measure). For every y, 3=|G^-1(y)|=sum over u in H^-1(y) of |F^-1(u)|. Each summand is 1 or 2. Therefore H must be everywhere EXACT TWO, and its two actual inverse points over each y must consist of ONE F-single point and ONE F-double point. Thus the double locus of F is a set-theoretic selector of one point in each H-fibre. This is NECESSARY, not sufficient and not an invariant forbidding all factorization. Indeed T3 from S127 factors: F(0u)=0u, F(10u)=F(11u)=1u; H deletes first bit. F is fair cap2, H fair exact2, H∘F=T3. Two everywhere-double factors would produce four inverses, not three.

S127 still gives F_b(R_ab) subset R_a; the product of two F2 observers can be genuinely F4, not F2. No F2(R2) closure, general F3/F4 factorization or SAME SOURCE R2\R4 is proven.

## D128 — all finite: pointwise finite versus uniform cap

Let tau_n=0^n1 for n>=0. These disjoint clopen cylinders partition X except 0^infty. With S127's T_k complete-prefix-code tail deletion (T1=identity), define U(tau_n u)=tau_n T_(n+1)(u), U(0^infty)=0^infty. U is total computable: an output prefix of length m can emit m zeros without discovering a 1, or else learn finite n and run total T_(n+1) on the suffix. It is continuous at 0^infty and every cone tau_n maps onto itself with normalized fair conditional law. The boundary singleton has measure zero. Hence U is globally fair. Every y in [tau_n] has EXACT n+1 actual inverse streams, y=0^infty has EXACT one, and no other fibres occur. Fibre size is finite for EACH y but unbounded across y, so U belongs to NO uniformly capped F_k. Yet for each finite cone input/output tails differ by only finite prefixes, so U preserves all R_j and CR; the isolated zero input is computable.

Thus uniformly finite observer and pointwise-finite observer classes are not equal, but no DIFFERENCE IN RANDOMNESS CLASSES follows. R_fin=MLR, finite threshold versus nonthreshold, a single x in R_fin\MLR, and stronger pointwise-finite preservation remain OPEN. Existence of an x_k for each k would not imply a single universal x.

## E128 — generality and exact scorecard

A: strict R2/R3, equality, R3=MLR, triple CR inverse NONCR: OPEN.
B: arbitrary computable-spine perpetual surplus with **all-output F3 exact-three**: INTERNALLY PROVED; c general N-1 streams, not destructive.
C: one-of-two factorization selector NECESSITY: INTERNALLY PROVED; no general nonfactorization or iteration.
D: pointwise finite UNBOUNDED fair observer: INTERNALLY PROVED, but all-R_j safe and no R_fin result.
E: general c rotating r=2^c-1 theorem and rational q posterior explicitly checked; no universal F_k normal form.

Grades: internal mathematical arguments only, same-agent hostile methods; finite Python sanity not proof, no novelty campaign. Historical Y/M/H/X, DEF-0020/PA-0001, frozen S101–S103 A–C, original prior-art/source access grades, Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED unchanged.
