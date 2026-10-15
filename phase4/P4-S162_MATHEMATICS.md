# P4-S162 — Effective phase-subsequence finance on the singular oscillator; an exact clopen-certificate barrier

15 October 2026. One fresh explicit owner-invoked Phase4 CAND-01 mathematics session, INTERNAL / SAME AGENT only. Independently pinned ENTRY main 8b47b642b96ad07cf34b775b6620b5f118b78d98, tree 98e033b11e527253cefecf9a6713183e68729600; predecessor S161 PR #61 merged 2026-10-15T11:30:12Z as its exact authored commit, sole parent 0cd8e83e7846b7a938f1682039f163e82a1e2ed4. No open PR or S162 branch; Actions runs, checks and individual statuses absent, NOT PASS; rulesets empty; branch-protection fetch 403 UNKNOWN. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. S101-S103, DEF-0020, PA-0001, Y/M/H/X and source grades frozen. No external originality, publication or proof certificate.

Notation. X=2^omega with fair product lambda; CR means ordinary total nonnegative exact-rational computable martingale randomness. F_k maps are EVERYWHERE TOTAL computable globally lambda-preserving and have <=k ACTUAL COMPLETE infinite inverse sequences above EACH output. R_k={x: for EVERY F in F_k, F(x) is CR}. Source rows of length m+2 are FINITE prefixes and are NEVER silently counted as complete preimages.

## A162.1 — two computable selector probability measures on S135's perfect singular tree (internally proved)

Fix precisely the previously established S135 GLOBAL legal additive-two F3 map G and T={y: y_(3j+1)=y_(3j+2)=0 for all j}. Its active rows R(tau), for tau compatible with T, always have tagged A/B counts (3,1) at output depths m=0,1 (mod 3), and (2,2) at m=2 (mod 3). Its global children partition all eight aligned source descendants; for y in T there are exactly TWO ACTUAL COMPLETE source inverses x_A(y), x_B(y), one in each initial tagged sector. For y outside T there are three. The T-supported measure mu_T gives each compatible output prefix tau of length m exact probability 2^(-a(m)), a(m)=ceil(m/3), and zero otherwise.

NEW EFFECTIVE CLAIM: x_A:T->X and x_B:T->X are uniformly computable continuous selector maps on the *represented computable closed space T*, with an explicit way to calculate every pushforward cylinder measure. In each active row at phase m=3j+1 the FIRST tagged A cell (length m+2) is the actual inverse x_A(y) prefix for every y in T extending tau. It survives the next forced step; at the following forced step its first child continues; subsequent free steps preserve the chosen output digit. These first-A cells are nested across consecutive phase-1 levels for fixed y. Similarly, at phase m=3j+2 the FIRST tagged B cell is the actual inverse x_B(y) prefix; B's first cell survives the next forced step, the next free step and subsequent forced split, nested across phase-2 levels. No oracle deciding y in T is required: the selector is a computable functional on the promised closed input subspace T. The full-space G is unchanged.

For any finite source string s, choose any phase-1 m>=|s|+4 and enumerate the finitely many T-compatible tau of length m. Define
  nu_A[s] = sum_{tau in T_m} 2^(-a(m)) 1{ FIRST_A(R(tau)) extends s }.
Similarly use any phase-2 m>=|s|+4 for nu_B. These are EXACT RATIONAL, uniformly computable numbers. Nested selector prefixes make the values independent of sufficiently large choice of phase level. The assignments nu_i[epsilon]=1, nu_i[s]=nu_i[s0]+nu_i[s1] are exact, so EACH nu_i is one computable projective source probability on ALL source cylinders. Their supports lie in G^-1(T); they are mutually separated by the original A/B root sectors. No noncanonical Borel regular conditional distribution or undecidable multiplicity mass was smuggled into their definition.

## B162.1 — effective three-phase limits and Cesaro projectivisation (internally proved)

Fix rational 0<delta<1 and S161's strictly positive rational winning output martingale D_delta=delta+(1-delta)*d_T. Its induced output probability is mu_delta=delta*lambda+(1-delta)*mu_T. Write
 eta_m[s]=integral_[s] D_delta(G(z) restricted to m) d lambda(z)
          =sum_{|tau|=m} mu_delta[tau] q_s(tau)
where q_s(tau)=2^m lambda([s] intersect G^-1[tau]). Each eta_m is a total exact-rational projective source probability, but S161 shows eta_m[11] does NOT converge.

At an arbitrary active output level m, the most recent A-bottleneck (respectively B-bottleneck) is at most three levels back. Its chosen FIRST tagged cell is the only parent continuing to the active child at that bottleneck. All later tagged cells descend from it. Hence for EVERY finite source s and every sufficiently large m (m>=|s|+4 certainly suffices), every active A row cell shares the length-|s| prefix of x_A(y) and every active B row cell shares that of x_B(y), uniformly for y in T. In particular for tau in T_m and any y in T extending tau,
 q_s(tau)= [w_A(m) 1{x_A(y) extends s} + w_B(m) 1{x_B(y) extends s}]/4,
where (w_A,w_B)=(3,1) in phases 0,1 and (2,2) in phase 2. The indicator values already depend on tau alone once m>=|s|+4.

The fair lambda component of eta_m is EXACTLY delta*lambda[s] for all m, since G pushes lambda to lambda. Summing the supported T cylinders gives these EXACT, eventually constant, phase-specific source marginals for EACH s:
  eta_(3j)[s]=eta_(3j+1)[s]=delta*lambda[s]+(1-delta)*(3nu_A[s]+nu_B[s])/4;
  eta_(3j+2)[s]=delta*lambda[s]+(1-delta)*(nu_A[s]+nu_B[s])/2.
The equalities hold once the displayed levels exceed |s|+4. Thus each phase subsequence stabilises EFFECTIVELY even though the full sequence does not. The ordinary Cesaro means of eta_0,...,eta_(N-1), for EACH fixed s, therefore converge EFFECTIVELY (computable modulus from |s| and rational periodic averages) to the EXACT-RATIONAL projective source probability
  eta_bar[s]=delta*2^(-|s|)+(1-delta)*(2nu_A[s]/3+nu_B[s]/3).
For s=11, nu_A[11]=0,nu_B[11]=1, so eta_bar[11]=delta/4+(1-delta)/3. At delta=1/2 that is 7/24, exactly the Cesaro average of 1/4,1/4,3/8. This REPAIRS the SPECIFIC S161 nonconvergence route without falsely claiming that arbitrary singular tilts have computable Cesaro limits.

## C162.1 — ONE exact rational source martingale wins on both singular inverse selectors

Define zeta[s]=(eta_bar[s]+2^(-|s|))/2, a strictly positive EXACT RATIONAL computable projective probability on ALL source cylinders; fair mixing is optional because delta>0 already makes eta_bar positive. Let e(s)=2^|s| zeta[s]. Then e(epsilon)=1, e(s0)+e(s1)=2e(s), and every value is a rational computed in finite time. There is no nonconvergent stage choice and no unjustified passage of martingale identities through an arbitrary limit.

If y in T, choose m=3j+1 for A and tau=y restricted to m, s=x_A(y) restricted to (m+2). By the explicitly computable selector prefix, ALL T extensions of tau have x_A prefix s. Therefore nu_A[s]>=mu_T[tau]=2^(-ceil(m/3)), and
  e(s)>=(1-delta)/3 * 2^(m+2-ceil(m/3)).
For x_B(y), choose m=3j+2, tau=y restricted to m and s=x_B(y) restricted to (m+2), giving
  e(s)>=(1-delta)/6 * 2^(m+2-ceil(m/3)).
Both lower bounds diverge exponentially as j->infinity. It is ONE total rational e winning on BOTH ACTUAL COMPLETE inverses over EVERY y in T, not separate ad hoc martingales depending on the particular y. This is a genuine source-finance construction satisfying the source parent averages, built from phase-averaging rather than a nonexistent eta_m limit. It is also deliberately a NON-SEPARATOR: all those sources are already nonCR, and S135's different exact rational W independently defeats them via the effectively closed null G^-1(T). We claim no new class inclusion.

## D162.1 — effective small clopen output certificates cannot identify a bad CR image (internally proved)

For ANY total computable globally fair G with arbitrary computable common use, suppose a UNIFORMLY computable family of clopen output events V_j, j>=1, is supplied with exact rational measure lambda(V_j)<=2^(-4j). Then no CR source x can satisfy G(x) in V_j for EVERY j. Proof without a Borel conditional kernel: U_j=G^-1(V_j) is a uniformly computable SOURCE clopen set (use totality plus the finite output-cylinder description), lambda(U_j)=lambda(V_j) exactly. For source prefix s put q_j(s)=lambda(U_j intersect [s])/lambda[s]; this is an exact rational and has q_j(s0)+q_j(s1)=2q_j(s). At every source word a of length j, q_j(a)<=2^j lambda(U_j)<=2^(-3j). Define M_j(s)=1 at |s|<=j; below source cone a=s restricted to j, use q_j(s)/q_j(a) if q_j(a)>0, and hold at 1 if its price is zero. Then M_j is a total rational source martingale with root 1 (at the activation boundary M_j(a)=1), including zero-price cones. Put
  W(s)=sum_(1<=j<=|s|) 2^(-j) M_j(s)+2^(-|s|).
The last term represents the still-unactivated components exactly: W is ONE total rational computable martingale with W(epsilon)=1. For any x mapping into all V_j, each U_j contains x; once the source prefix resolves U_j, q_j(x restricted to n)=1 and M_j(x restricted to n)>=2^(3j), giving W>=2^(2j). Contradiction to x in CR. In fact no R2 is needed, and no fibre cap, bounded use, L1 density or posterior stability is assumed.

This cleanly rules out a proposed class of effectively priced output clopen ribbons as a way to locate a bad image at a CR (hence R2) source. It DOES NOT rule out all open-event or singular martingale certificates: arbitrary nonCR outputs can be Schnorr random, and S011 supplies a CR source Y with bad fair F2 image. Such a y cannot lie in all V_j of a family as above. S161's no-effective-L1+floor barrier remains separate and intact.

## E162 — central and hierarchy attacks; precise first failures

Start with hypothetical globally fair additive-two G in F3, x in R2, y=G(x) not CR, exactly TWO ACTUAL COMPLETE inverse streams at y. To prove equality we need one G-dependent but total globally fair cap-TWO F that defeats THIS x via a single rational output martingale, or equivalently another contradiction to x in R2. The special selectors J_A,J_B above live ONLY on S135's effectively null T. Their pushforwards define a source bettor, but no non-CR output of that G has a CR preimage, much less an R2 one; thus they do not transfer to an arbitrary candidate y or construct F. E-08 remains OPEN.

Weighted stopping: S161's exact tilted output conditional odds 5/6,9/10,17/18,33/34,... and mu_delta(A_N)>=1-delta show strong biased output selection on T. They do NOT by themselves satisfy source parent averages. C162 supplies a legal rational source finance only because J_A,J_B form computably projective pushforward measures, with effectively bounded common prefixes. When those hypotheses are missing, summing tilted finite odds is not a licensed source bettor. S135 is a complete GLOBAL legal countermodel to the general claim that tilted posterior eta_m necessarily converges; S011+S160 legally refute a universal UI+floor output-winner replacement. No universal weighted-stopping transfer follows from our scoped construction.

A second independent hidden input bit added to S158's EXACT-two first-one release normally yields FOUR actual complete inverses over some output: cannot use a 2x2 finite table as an F3 proof. S117 paired reservoirs lack the needed computable selector/projective probabilities; S141's positive internal-folding control can hold even at MLR sources but preserve CR; S155's noncomputable degree-two locus mass does not itself cause destruction. S011's Y is CR but NOT R2 because its F2 image is bad. None yields a coupled x in R2 with a legal F3 destroyer. Neither finite table counts nor noncomputability proves the universal R2 quantifier; the arbitrary-use E-00 gap also persists.

## Disposition

INTERNALLY PROVED A162.1 (computable T selector measures), B162.1 (effective exact three-phase source distribution limits and computable Cesaro), C162.1 (one rational source martingale wins BOTH T inverse branches) and D162.1 (arbitrary-use fair clopen-ribbon source test). All are scoped/derived from S135 and elementary martingale arithmetic; no priority claim. Same-agent hostile validation and 672 exact-rational finite sanity checks only. No Lean/Palomar/external referee and no hosted CI. E-08/E-00/S-00, R2=R3 equality/strictness, R2=MLR and Gate4 remain OPEN. S163 future only.
