# P4-S074 — Effective rolling price escrow over an infinite shared-pivot dependency chain

Date: 2026-10-09
Incoming independently checked remote main: 71ad3437aa4a0c9f22b0567a9c12da8b07812409
Scope: Phase 4 Mathematics ONLY; selected CAND-01 and the fixed P4-S071 supported-shear evaluator
Disposition: **VALIDATED EFFECTIVE PRE-FINANCING OF A GENUINELY OVERLAPPING INFINITE TWO-CLAIM CHAIN; SHARP 3/16 SAME-SOURCE BOUND AT q=1/2; NO UNIVERSAL COMPILER OR H-PRESERVATION**

## 0. Authority, freeze and exact meaning

Live remote main matched the requested S073 outgoing SHA, whose parent is the S072 outgoing SHA 9394fc898b1f152666524d27c1e60d037f658e4a. No P4-S074 artifact existed. Read P4-S001–S073 mathematics (emphasizing S008/S011/S012/S027/S032–S044/S052–S057/S065–S073), the P3-S007 CAND-01 selection, P3-S008 Gate-3 PASS, both post-S031 and post-S069 pivots, and the S073 mathematics, validation and closeout. Retain every prior result and definition.

In particular retain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Keep the ORIGINAL computably random Y, unchanged syntactically self-avoiding globally use-clipped wtt autoreduction M, committed repeated three-bit fair-coin homeomorphism H and CR X=H^{-1}(Y) with H(X)=Y\notin OH. X in OH, H-preservation, R_2=OH, R_2=OH^{iso} and arbitrary homeomorphism invariance remain UNRESOLVED.

S073 gives, for a total pre-bit finite common-pivot registrar on the unchanged S071 raw one-hole scan P,
\[
LF\Pi=dA,\qquad h_2\ge\sqrt{dA/\Pi},\qquad
h_3\ge(dAQ/\Pi)^{1/3}
\]
with Q any additional total positive rational raw martingale. Here \(\Pi\) includes prices charged at **all** earlier credited bundle pivots (even if their claims have settled), whereas \(A\) contains only credited but **unsettled** virtual wagers. No new result below treats \(\Pi\) as a martingale.

## 1. One explicit, nonclosed, infinite rolling virtual schedule

Fix either computable shear support E=all blocks or E=even blocks, with selected-block recoding
\[
(u_j,v_j,w_j)=(a_j,b_j\oplus c_j,c_j).
\]
Choose an arbitrary fixed rational \(0<q<1\). Divide virtual blocks into groups \(B_i=\{4i,4i+1,4i+2,4i+3\}\), for \(i\ge0\), and let \(j=4i\). Begin the deterministic virtual scan T with \(v_0,v_2\). For every \(i=0,1,\ldots\), request, in this order,
\[
v_{j+4},\quad u_{j+4},\quad v_{j+6},\quad
w_j,\quad w_{j+2},
\tag{1}
\]
then finish the as-yet-unqueried coordinates of \(B_i\): request \(u_0\) additionally when \(i=0\), then \(u_{j+1},u_{j+2},u_{j+3}\), then \(v_{j+1},v_{j+3}\), then \(w_{j+1},w_{j+3}\). For \(i>0\), \(u_j\) was already queried as the preceding group's \(u_{j-4+4}\) pivot. Similarly \(v_j,v_{j+2}\) were already queried when the preceding group was processed. All complementary queries have zero virtual stake.

Consequently every virtual coordinate is queried exactly once, eventually: T is an everywhere-total exhaustive computable permutation, not a merely source-dependent scan. Its S071 raw evaluator P, for the stated E, takes REAL fresh c fillers before the b bits of selected v's and silently processes their later virtual w's. It is everywhere total, fair-coin preserving, no-repeat, and **globally zero-hole** (hence one-hole) on every transcript. Nothing in the following changes P, its genuine raw filler reads or its silent steps.

Put
\[
C_{i,0}=2c_{4i}-1,\quad C_{i,2}=2c_{4i+2}-1,\quad
R_i=2a_{4i+4}-1,\quad R_{-1}=1.
\tag{2}
\]
The sign \(R_i\) is a genuinely fresh real raw a pivot at the query of \(u_{4i+4}\). It is strictly later than both c fillers of \(B_i\), while the previous \(R_{i-1}\) is known before the real c filler at \(v_{4i+2}\) for \(i>0\).

Let the total positive computable rational virtual martingale d start at 1, hold at every other virtual bit, and bet signed fractional stake \(qR_{i-1}R_i\) at \(w_{4i}\), and \(qR_i\) at \(w_{4i+2}\). Both stakes are known from PREVIOUS virtual u queries before their corresponding virtual w queries. Each child pair sums to two, and every factor lies in \([1-q,1+q]\).

The two spoiled w claims for group i have prospective multiplier functions at their SHARED genuine later fresh raw a pivot:
\[
g_{i,0}(r)=1+q C_{i,0}R_{i-1}r,\qquad
g_{i,2}(r)=1+q C_{i,2}r,
\tag{3}
\]
\[
G_i(r)=g_{i,0}(r)g_{i,2}(r),\qquad
\pi_i=\tfrac12(G_i(-1)+G_i(+1))
 =1+q^2 C_{i,0}C_{i,2}R_{i-1}.
\tag{4}
\]
All input data for (3)–(4) are already available before the pivot \(R_i\). The registrar there is total and outputs exactly two distinct positive rational claims, to be credited once each and settled later at their corresponding virtual w steps.

**Nonclosed overlap.** The next group is started by \(v_{4i+4}\) before the old group's common a pivot; the next group's second v (and its c-filler price transaction) occurs AFTER that pivot but BEFORE either old spoiled w claim settles. Consequently, after \(v_0\), every subsequent virtual cut has at least one raw-determined selected w claim still awaiting its virtual request: there are no subsequent empty-spoiled-frontier cuts and no partition into consecutive finite closed episodes. Moreover, \(R_i\) essentially enters BOTH group-i settlement factors and the next group's first factor and fair price \(\pi_{i+1}\). Thus the block-group essential-dependency graph contains the entire infinite chain \(B_0-B_1-B_2-\cdots\), so no finite *block-aligned disjoint dependency-closed packetization* exists. This specifies the non-packetizable sense used here; it does not assert a no-go for arbitrary noncontiguous reorganizations or other compilers. Individual old claims nonetheless retire in finitely and computably many steps. The example is compatible with, and a sharpened aggregate-price instance of, the S037 positive effective-renewal boundary.

## 2. A TOTAL genuine-filler financing martingale

At the REAL fresh raw \(c_{4i+2}\) filler, prior to seeing its value, the raw state already knows \(C_{i,0}\) and \(R_{i-1}\) (the latter seeded by 1 for i=0). Define a financing wager Q with two-child multiplier
\[
q_i(s)=1+q^2 C_{i,0}R_{i-1}s,\qquad s\in\{-1,+1\}.
\tag{5}
\]
The two children have mean one, are rational, and lie in \([1-q^2,1+q^2]\). At the realized c sign \(C_{i,2}\) its factor is EXACTLY \(\pi_i\). Q holds at all other genuine raw queries. It is therefore a SINGLE, total computable normalized strictly positive rational raw martingale on every raw transcript. These are genuine pre-fresh-bit c bets, not fictional virtual wagers or after-the-fact knowledge of a future u outcome.

At the later REAL fresh raw \(a_{4i+4}\) pivot bet the positive normalized bundle factor
\[
f_i(r)=G_i(r)/\pi_i.
\tag{6}
\]
Both g functions and \(\pi_i\) are known at this permitted time; \(f_i(-1)+f_i(+1)=2\). Their sequence gives the total normalized positive rational raw martingale F of S073. Q and F have **disjoint nontrivial RAW wager coordinates**: Q wagers only at c_{4i+2}, F only at a_{4i+4}. Thus their literal product
\[
e=QF
\tag{7}
\]
is in THIS CONSTRUCTION itself one total normalized positive computable rational raw martingale: at any raw step exactly one factor can have a nontrivial fair wager, while the other holds. This disjoint-wager argument would NOT justify multiplying arbitrary martingales or two factors at one pivot. The live copier is \(L\equiv1\), since d wagers only at spoiled w steps; all live virtual wagers have stake zero.

The finance is online even though prices interact across groups: the old \(R_i\) is used to finance \(\pi_{i+1}\) at the next group's c filler, and is never forecast before its own genuine fresh read. At the pivot \(R_i\), the EXACT SETTLEMENT \(G_i(R_i)\) is delivered by the already-paid price \(\pi_i\) and normalized wager \(G_i/\pi_i\).

## 3. Exact global inventory identity and sharp all-stage bound

Let \(\Pi\) be the product of prices of all previously CREDITED groups at their a pivots, including retired groups. Let \(A\) be the product of realized factors of those credited w claims which are still UNSETTLED. Write \(n(m)\) for the number of REAL raw reads completed by virtual checkpoint m. Then S073's exact identity becomes, on EVERY source,
\[
F_{n(m)}\Pi_m=d_m A_m,\qquad
\boxed{\ e_{n(m)}=d_m\,A_m\frac{Q_{n(m)}}{\Pi_m}\ }.
\tag{8}
\]
In the rolling schedule, no second group has a credited pivot before the previous group's two w claims have retired. Hence \(A_m\) is 1, a two-factor \(G_i(R_i)\), or its one-factor remainder \(g_{i,2}(R_i)\), so
\[
A_m\ge(1-q)^2.
\tag{9}
\]
The Q account pays each \(\pi_i\) at an earlier c filler, while \(\Pi\) charges that \(\pi_i\) only at its later a pivot. There is at most ONE paid-but-not-yet-charged price at any raw or completed virtual checkpoint, so
\[
Q_{n(m)}/\Pi_m\in\{1,\pi_i:i\ge0\},\qquad
Q_{n(m)}/\Pi_m\ge1-q^2.
\tag{10}
\]
This is an exact CASH/PRICE distinction: a cumulative settled premium \(\prod_{k<i}\pi_k\), which may grow without bound, is matched by Q; only an at-most-one-group forward escrow remains in Q/Pi. Pending spoiled-w downside appears separately in A.

Combining (8)–(10) proves the all-source, all-virtual-checkpoint estimate
\[
\boxed{\ e_{n(m)}\ge(1-q)^2(1-q^2)\,d_m\ }.
\tag{11}
\]
This transfers any unbounded success of this particular virtual d on S_E(z) into success of one globally legal raw e on P(z), and therefore this **rolling-chain witness** cannot distinguish an OH source from its E-shear.

For \(q=1/2\), (11) is the sharp bound
\[
\boxed{\ e_{n(m)}\ge \tfrac{3}{16}d_m\quad\text{for all }m.\ }
\tag{12}
\]
To see sharpness, take group i with \(g_{i,0}(R_i)=g_{i,2}(R_i)=1/2\) and next group with \(\pi_{i+1}=3/4\). The conditions are compatible because the next c-pair can be chosen independently given the known \(R_i\). After the next-group price filler but before the first old w settlement, \(e/d=G_i(R_i)\pi_{i+1}=3/16\).

More explicitly the relative e/d ratios during the i-th rolling step, after the initial c-pair is prefunded, are
\[
\pi_i\ \xrightarrow{\ v_{4i+4}\ }\ \pi_i\
\xrightarrow{\ u_{4i+4}\ }\ G_i(R_i)\
\xrightarrow{\ v_{4i+6}\ }\ G_i(R_i)\pi_{i+1}\
\xrightarrow{\ w_{4i}\ }\ g_{i,2}(R_i)\pi_{i+1}\
\xrightarrow{\ w_{4i+2}\ }\ \pi_{i+1}.
\tag{13}
\]
The zero-stake cleanup steps do not change the ratio; the initial two v queries and every unshown prefix satisfy the same bound. This exact table shows why the rolling chain does NOT return to equality at finite group boundaries, unlike S073's closed four-block packets.

For a branch with \(C_{i,0}C_{i,2}R_{i-1}=1\) at every group, every settled \(\pi_i=1+q^2\), and so \(\Pi\) is exponentially unbounded along that branch. Yet \(Q/\Pi\) remains between \(1-q^2\) and \(1+q^2\) on ALL branches. The branch is a mathematical price-growth calibration, NOT a claim of OH/CR membership.

## 4. Exact failed escrow methods and preservation boundary

1. **Premium charged at its own pivot.** Immediately before \(a_{4i+4}\), \(\pi_i\) is already determined by old c and R values. A literal factor \(\pi_i\) on BOTH children of that raw pivot has conditional mean \(\pi_i\neq1\) on reachable histories with \(\pi_i=1\pm q^2\). It is not a martingale wager. Earlier truly fresh c financing in (5) is essential to this construction.
2. **Naive shared-pivot product.** The factors in (3) are individually fair as functions of the same raw sign r, but their product's conditional mean is \(\pi_i=1+q^2 C_{i,0}C_{i,2}R_{i-1}\), generally not one. S073's obstruction persists unchanged.
3. **Bound \(\Pi\) alone, or count only pending claims.** At most two credited w claims are pending, but prices of long-retired groups can accumulate exponentially. Counting claims without pricing is insufficient; measuring only \(\Pi\) misses the executable earlier c escrow Q.
4. **Forecast a future stake, claim a nonhalting certificate, or posit a limiting price.** None is used. The current group has a total prospective two-claim registrar from prior finite bits, and its finance has an actual pre-bit fair price transaction. This **does not** construct a registrar or financer for arbitrary virtual T,d, nonlinear stake choices, persistent undecidable retirement, or the original X-specific M.

A sharply scoped sufficient **effective one-step escrow rule** illustrated here is: a total online registrar of positive bounded common-pivot claims, a computable earlier genuine fresh funding-bit wager whose two children are the desired fair price with mean one, a uniformly bounded number of prepaid-but-uncharged prices with positive lower factors, and a uniform positive floor on the product of credited unsettled claims. For disjoint nontrivial F and Q wager coordinates and zero live stakes, the product e=FQ transfers success linearly. Without disjointness one must use S073's safe three-account average and condition on A(Q/Pi), not multiply arbitrary martingales. This is a **sufficient architecture rule**, not an assertion that the rule can be met for all spoiling patterns.

S035–S037 effective finite/rolling normalization is preserved and not claimed as superseded; this proof specifically handles interacting, variable priced TWO-claim common pivots with the exact executable escrow Q and its quantitative 3/16 inventory bound. The S057–S069 certificate/hazard/closure line is NOT reactivated. If ever used, preserve precisely four paired globally clipped M traces, prospective deadlines, genuine fillers, zero-stake t/u timeout release, mandatory non-s sweep WITHOUT old-sentinel reset, and seven 8/7 vs one ZERO. No X-specific recurrence is inferred.

## 5. Validation and disposition

An executable exact-Fraction finite audit checked three successive settled groups plus a fourth prefunded group, all \(2^{11}=2048\) relevant sign assignments for EACH of E=all and E=even, 4096 sign assignments and **159,744 completed virtual checkpoints**. It checked global source-independent request uniqueness on every tested prefix, real c filler timing, silent selected w processing, pre-bit Q and F child fairness, source-by-source \(F\Pi=dA\), \(e=dA(Q/\Pi)\), \(A\ge1/4\), \(Q/\Pi\ge3/4\), and \(e/d\ge3/16\). There were zero discrepancies; the exact minimum was 3/16, attained at 1536 checked checkpoints. The audit tests arithmetic, not a universal infinite theorem; the formal all-stage proof is (1)–(13) and exhaustive recurrence.

Result is a **positive globally legal online aggregate price-escrow construction for one infinite overlapping nonclosed family**, stronger than a finite closed packet example and explicitly bounded in inventory and net price. It is NOT universal shear/H preservation, OH membership of X, \(R_2=OH\), \(R_2=OH^{iso}\), or unrestricted homeomorphism invariance. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker: NONE.

Next mathematical axis, if authorized in P4-S075: determine whether **finite executable price-escrow renewal without a priori uniform pending/downside floors** can be upgraded to a computable savings or stopping compiler on infinite overlaps, or give an explicit impossibility theorem for a precisely specified online escrow strategy. Do not infer universal preservation from the present engineered example.