# P4-S073 — Multi-claim fair settlement and aggregate pending-inventory pricing

Date: 2026-10-08
Incoming independently verified live main: \`9394fc898b1f152666524d27c1e60d037f658e4a\`
Scope: Phase 4 Mathematics ONLY; selected CAND-01; computably supported two-coordinate XOR shears
Disposition: **VALIDATED CONDITIONAL JOINT-PRICE / FINANCED-ESCROW THEOREMS, EXACT UNFUNDED-PAIR OBSTRUCTION AND FULLY FUNDED SHARED-PIVOT EXAMPLE; NO UNRESTRICTED SHEAR PRESERVATION OR SEPARATION**

## 0. Authority and fixed objects

The live GitHub main matched the requested S072 outgoing commit exactly. The parent is the S071 outgoing commit; at the pinned phase4 listing S001–S072 are present and S073 is absent. Reviewed mathematics across S001–S072, highlighting S008/S011/S012/S027/S032–S044/S052–S057/S065–S072; separately inspected S072 mathematics/validation/close, S034–S037, S070–S071, both research pivots, CAND-01 P3-S007 selection, P3-S008 Gate-3 PASS and authority ledgers. No earlier proof is reopened.

Retain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Keep the ORIGINAL computably random Y, unchanged syntactically self-avoiding globally use-clipped wtt autoreduction M, committed repeated three-bit fair-coin homeomorphism H, and X=H^{-1}(Y) in CR with H(X)=Y notin OH. The questions X in OH, H preservation of OH, R_2=OH, R_2=OH^{iso}, and unrestricted homeomorphism invariance all remain UNRESOLVED.

For decidable E (in particular all blocks or even blocks), S_E(a,b,c)=(a,b xor c,c) on selected blocks; write virtual u=a,v=b xor c,w=c. Retain the EXACT S071 raw scan P_{E,T}, which on selected v reads real fresh c filler then fresh b, uses c to decode v, and silently handles a later spoiled w; on all other requests it queries fresh raw coordinates. It is total, computable, no-repeat, fair and globally one-hole on ALL transcripts, not merely the intended source. The following betting constructions do not change this scan.

## 1. Finite bundles at a common fresh pivot

Fix any total computable virtual one-hole scan T and normalized nonnegative rational output martingale d. A **total online bundle registrar** is a total algorithm on EVERY finite raw evaluator state, acting BEFORE the next fresh raw bit p. It either declares no credit or outputs a finite, explicitly terminated list J of distinct prospective spoiled-w claims, not previously credited, with positive rational two-child multipliers g_j(0),g_j(1). This list and every g_j(r) must be computed without the next raw bit or any future eventual stake. A claim is credited at most once, but ANY FINITE NUMBER of different claims may share p; credits occur only at real fresh raw queries, before the respective virtual spoiled-w requests. No bound on number/lifetime of outstanding claims is assumed. Unlike S072's single-credit rule, the individual g_j need not be fair; only their joint bundle will be normalized.

At the actual pivot outcome r define
\[
G_p(r)=\prod_{j\in J_p}g_j(r)>0,\quad
\pi_p={G_p(0)+G_p(1)\over2}>0,\quad
f_p(r)=G_p(r)/\pi_p.
\tag{1}
\]
Empty bundle gives G=pi=f=1. Each quantity is computable positive rational at the permitted time, and f_p(0)+f_p(1)=2. Faithfulness on a source x means each nontrivial spoiled virtual w multiplier is credited before its virtual request and equals its registered g_j(r) at the realized pivot, and every uncredited spoiled factor is 1. A credited claim which is NEVER queried simply stays pending; no negative nonhalting certificate is assumed.

After m completed virtual steps let n(m) be the number of ACTUAL raw queries, A_m the product of realized g_j(r_j) for credited claims whose virtual w has not yet occurred, and
\[
\Pi_m=\prod_{\text{nonempty bundle pivots }p\le n(m)}\pi_p.
\tag{2}
\]
All are computable positive rationals from the finite raw history, with empty products 1. Pi includes prices of groups long since settled; it is NOT just a pending-inventory factor.

### Theorem 1 — exact aggregate joint-price identity

For any total bundle registrar satisfying the syntactic online rules, there exist total computable normalized nonnegative rational raw martingales L,F, and their single average h_2=(L+F)/2, all acting on the SAME legal P, such that on every faithful source at ALL virtual checkpoints
\[
\boxed{L_{n(m)}F_{n(m)}\Pi_m=d_m A_m},\qquad
\boxed{h_{2,n(m)}\ge\sqrt{d_m A_m/\Pi_m}}.
\tag{3}
\]

**Proof.** L is S071's live-wager copier, holding at real c fillers and silently skipping already known spoiled w factors. F bets f_p at real bundle pivots and holds elsewhere. A total registrar supplies f before seeing the raw pivot; f(0)+f(1)=2, so F is a computable rational positive martingale on EVERY raw transcript. L is the already-validated total raw martingale. F equals product over all realized G_p divided by the product Pi. On a faithful path the credited g factors partition into settled virtual spoiled factors and unsettled factors in A; uncredited spoiled factors equal one. Therefore L F Pi=d A even if d has hit zero at a live wager. The product L*F is an ACCOUNTING equality, not generally a martingale; the arithmetic mean h_2 is a martingale, and AM–GM gives (3). Neither hypothetical future queries nor virtual silent steps count as raw bets. QED.

### Corollary 2 — aggregate burden, necessary and sufficient within this certificate

For a faithful registrar on a source z in OH,
\[
\sup_m\frac{d_m A_m}{\Pi_m}<\infty.
\tag{4}
\]
If d succeeds on the virtual output, the ratio A_m/Pi_m must approach zero along some unbounded-d capital subsequence. Conversely d success and inf_m(A_m/Pi_m)>0 imply the raw h_2 succeeds, so cannot occur for z in OH.

Define the computable rational aggregate downside B^{agg}_m=Pi_m/A_m. A sufficient effective lower-ratio certificate is B^{agg}_m<=C for all m on the target, for a fixed rational C. One stronger log bound is
\[
\sum_{p\le n(m)}[\log\pi_p]_+
 +\sum_{j\text{ pending at }m}[-\log g_j(r_j)]_+\le C',
\tag{5}
\]
which implies A_m/Pi_m>=exp(-C'). This permits unbounded numbers of claims only when their aggregate downside is controlled; at most K pending, with g_j>=1-rho, bounds the second sum but does NOT bound positive price premiums from settled groups. Positive prices can accumulate indefinitely.

## 2. Exact two-claim obstruction to naive multiplication

For two individually fair positive child factors g_1(r)=1+alpha r, g_2(r)=1+beta r on the SAME fresh sign bit r in {-1,+1}, where alpha,beta are rational and |alpha|,|beta|<1 and known before r,
\[
\frac{g_1(+1)g_2(+1)+g_1(-1)g_2(-1)}2
 =1+\alpha\beta.
\tag{6}
\]
Thus the literal product can be the one-step factor of a normalized fair RAW martingale with no prior financing iff alpha beta=0. This is a **structural impossibility for the natural unfunded exact-product method**, NOT for arbitrary multi-step compilers. Its uniquely normalized positive fair joint factor is g_1(r)g_2(r)/(1+alpha beta). Correlation determines a real price: aligned claims have premium >1, opposite signs discount <1. With alpha=beta=1/2, product children 9/4 and 1/4 average 5/4, while normalized children are 9/5 and 1/5. With alpha=-beta=1/2, the product is constantly 3/4 and its normalized children are both 1.

The one-pivot algebra cannot on its own bound Pi: repeating a packet with both pre-known c signs equal gives pi=5/4 every packet and Pi=(5/4)^N, while no more than two claims need be pending and each realized factor is >=1/2. This is a valid ALL-TRANSCRIPT obstacle to a uniform price bound, not an OH or CR source. In particular S072's bounded pending inventory criterion cannot be extended to multiply individually fair credits on the same pivot without financing or an aggregate-price hypothesis.

## 3. Third-account financing criterion

### Theorem 3 — computable price-escrow extraction

Under Theorem 1, let Q be ANY additional total computable normalized strictly positive rational raw martingale on P, with no restriction that its wagers occur at different pivots from L or F. Define its computable **financing ratio** at virtual checkpoints
\[
\Gamma_m=Q_{n(m)}/\Pi_m>0.
\tag{7}
\]
Then the SINGLE normalized raw martingale h_3=(L+F+Q)/3 satisfies on every faithful source
\[
\boxed{h_{3,n(m)}\ge (d_m A_m\Gamma_m)^{1/3}}.
\tag{8}
\]
In particular virtual success transfers if inf_m(A_m Gamma_m)>0. If z in OH and d succeeds through a faithful registrar, every such Q has A_m Gamma_m arbitrarily small along high virtual-capital stages.

**Proof.** L,F,Q are each fair total raw martingales, so their average is one too, regardless of overlapping betting coordinates. Identity (3) gives L F Q=d A(Q/Pi)=d A Gamma. Three-term AM–GM proves (8). A computably random raw P(z) bounds h_3, giving the converse. Q must be a genuinely constructible raw martingale BEFORE its respective wagers: Pi alone is NOT automatically a martingale or a prepayable premium. Q=1 recovers only the less flexible aggregate burden; this theorem asserts no universal Q and does not presume nonhalting status decidable. QED.

## 4. Globally legal TWO spoiled w claims at one genuinely later raw pivot

Use deterministic exhaustive virtual scans in disjoint FOUR-block packets (j=4k). The exact virtual query order in a packet is
\[
v_j,\ v_{j+2},\ u_{j+1},\ w_j,\ w_{j+2},\
u_j,\ u_{j+2},\ v_{j+1},\ w_{j+1},\
u_{j+3},\ v_{j+3},\ w_{j+3}.
\tag{9}
\]
All 12 virtual coordinates are requested once, for every continuation; T is a computable permutation, hence a globally one-hole virtual scan. Use E=all blocks or E=even blocks. In either case j,j+2 are selected; the S071 raw P first queries REAL c_j and REAL c_{j+2} fillers, and their respective b bits, before it reaches the still-FRESH raw pivot a_{j+1}=u_{j+1}. Later virtual w_j,w_{j+2} are BOTH silent. Other potential spoiled w claims have zero virtual stake.

Let q=1/2. The only nonzero d bets in each packet occur at w_j and w_{j+2}, with common signed stake q(2u_{j+1}-1). This is a total fair rational virtual martingale because u_{j+1} has ALREADY been queried virtually when each fresh virtual w is wagered on. Set C_0=2c_j-1, C_2=2c_{j+2}-1 and R=2a_{j+1}-1. The two eventual virtual factors are
\[
g_0(R)=1+q C_0R,\quad g_2(R)=1+q C_2R,\quad
G(R)=g_0(R)g_2(R).
\tag{10}
\]
No pre-c stake forecast is possible on all continuations, because the deciding a_{j+1} is genuinely later. After both c fillers, however, the joint price is computable:
\[
\pi={G(+1)+G(-1)\over2}=1+q^2 C_0C_2
\ \in\ \{5/4,3/4\}.
\tag{11}
\]
At the SECOND genuine raw c filler c_{j+2}, with c_j already known, wager the fair two-child factor
\[
Q\text{-factor}=1+q^2 C_0(2c_{j+2}-1)=\pi.
\tag{12}
\]
Its children sum to 2, lie in [3/4,5/4], and are determined by the prior raw state BEFORE c_{j+2} is read. At the later REAL fresh raw a_{j+1} pivot, wager
\[
F\text{-factor}=G(R)/\pi.
\tag{13}
\]
Because both c signs are now already known, the two children in (13) average exactly 1; they are positive rational. All other RAW wagers hold. Define e to use these successive wagers, directly, in every four-block packet. The underlying raw P is unchanged and exhaustive on ALL transcripts since T is exhaustive; e is a SINGLE globally total nonnegative normalized computable rational martingale. On the raw a_{j+1} event e's capital for this packet has multiplied by pi*(G/pi)=G. This is a true finite fair pre-finance, not multiplication of two contemporaneous unfair gambles.

At each completed virtual stage m in a packet, the ratio of current e to d (relative to matching capitals at the preceding packet end) is one of
\[
1,\quad \pi,\quad G(R),\quad g_2(R),\quad 1.
\tag{14}
\]
Before the first w request, G>=1/4; pi>=3/4; between w_j and w_{j+2}, g_2>=1/2. Therefore on EVERY raw source, at ALL completed virtual stages,
\[
\boxed{e_{n(m)}\ge\tfrac14 d_m.}
\tag{15}
\]
At each four-block packet end e=d EXACTLY; no accumulation of packet pricing discounts is needed. This is a strict later-decision/shared-pivot SAME-SOURCE normalization instance for both E=all and E=even. It is consistent with S035–S036 finite closed-packet compression, and does not prove that an arbitrary virtual one-hole observer is compressible into such packets.

The finite four-block audit ran all 2^12=4096 raw assignments for each E (8192 cases total). It found zero discrepancies for (11)–(15), child fair sums, or the 1/4 bound; all two-claim combinations occurred. This enumeration checks finite arithmetic only. Global scan legality, fair betting before fresh bits, and the infinite bound follow from the displayed construction and disjoint repeated packets.

## 5. Infinite-inventory limit, excluded methods and exact status

Unbounded groups can make a joint price arbitrarily large or small even with individual stakes bounded. For arbitrary virtual T,d, the effective ability to construct future claims or finance Pi is NOT forced; a computably finite group at one pivot does not imply computable future stake values or a uniform total registrar. Nor does bounded maximum OPEN claim count control the accumulated Pi from already retired groups. Theorem 3 specifies the missing *computable self-financing escrow* Q, rather than assuming that a formal conditional expectation is executable. S036 and S037 show finite packet and special rolling-ray methods, but do not turn all nonclosed infinitely overlapping sources into this example. Case C divergence still has no computable finite negative certificate; retrospective halting, high-degree or measure-typical sources cannot supply current raw bets.

Frozen S057 controller was NOT invoked. If later essential, preserve exactly four paired globally clipped M traces, prospective deadlines and REAL fillers, zero-stake t/u timeout release, mandatory non-s sweep WITHOUT old-sentinel reset, and seven 8/7 versus one ZERO terminal payoffs. No S057–S069 renewal/hazard/closure-multiplicity line was resumed.

S071 unconditional unbounded spoiled-stake exposure remains necessary for any hypothetical OH shear separator. S072 single-credit fair registrar is recovered when every bundle is singleton fair (pi=1). For a multi-claim faithful registrar the new necessary obstruction on a hypothetical z in OH is A_m/Pi_m arbitrarily small at d peaks, and even with price-financing martingale Q the product A_m(Q/Pi_m) must become arbitrarily small. Neither direction gives a universal registrar, OH non-invariance witness, H preservation, X in OH or any R_2 equality.

Governance: PA-0001 **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED; Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claims. Owner/external blocker **NONE**.

Suggested bounded P4-S074: test *online price-escrow renewal for non-packetizable overlapping claims*. Give a precise total computable price-financing construction for an unbounded rolling overlap (or an explicit impossibility for a specified naive escrow), tracking Q/Pi and pending A jointly; do NOT automatically return to S057 controllers or infer any actual-X recurrence. R_2=OH^{iso} remains separate.
