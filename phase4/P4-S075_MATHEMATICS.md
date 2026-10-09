# P4-S075 — Effective settlement-mirror escrow savings without a uniform inventory floor

Date: 2026-10-09
Incoming independently checked live remote main: \`9989c52b902492d73fbae2118c3de987703e74e4\`
Scope: Phase 4 mathematics ONLY; supported XOR shears under the unchanged S071 globally legal evaluator
Disposition: **VALIDATED EXPLICIT EFFECTIVE SAVINGS/ESCROW COMPILER FOR A VANISHING-FLOOR INFINITE ROLLING CHAIN; EXACT THREE-CLAIM ONE-SLOT FINANCING OBSTRUCTION; NO GENERAL SHEAR OR H PRESERVATION**

## 0. Authority and frozen hypotheses

The incoming SHA is the unique live \`main\` head, with S001–S074 mathematics/validation/close present and S075 absent. Prior CAND-01 selection, P3-S008 Gate-3 PASS, the pivots after S031 and S069, S034–S037, S070–S074 and the emphasized S008/S011/S012/S027/S032–S044/S052–S057/S065–S074 were reviewed. Freeze all earlier results.

Keep
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Preserve ORIGINAL CR source Y, unchanged syntactically self-avoiding globally use-clipped wtt autoreduction M, committed repeated three-bit homeomorphism H, and CR X=H^{-1}(Y) with H(X)=Y\notin OH. X in OH, H/supported-shear preservation, R_2=OH, R_2=OH^{iso} and arbitrary homeomorphism invariance remain unresolved.

Retain S073's \`LF\Pi=dA\`, \`h_3\ge(dAQ/\Pi)^{1/3}\` and the strict separation of **all credited joint prices** \(\Pi\), executable actual raw finance \(Q\), and **still-unsettled** credited factors \(A\). Neither \(\Pi\) nor a formal conditional price is automatically a fair computable martingale. The present explicit e=QF is legal only because its nontrivial Q and F raw wager coordinates are disjoint.

## 1. The exact rolling counterexample to a uniform floor

Keep, without changing a single query, S074's deterministic infinite exhaustive four-block virtual permutation T and S071 raw evaluator P_E for E=all blocks or E=even blocks. Each group i has j=4i and two selected spoiled coordinates w_j,w_{j+2}. The scan begins v_0,v_2 and then for each i requests v_{j+4},u_{j+4},v_{j+6},w_j,w_{j+2} and the zero-stake cleanup of B_i from S074. REAL c fillers at selected v queries precede their b bits; selected later w queries are SILENT. All raw queries are fresh and exhaustive on ALL transcripts. The raw evaluator is fair-coin preserving and globally zero-hole (hence one-hole); neither martingale below changes it.

Set
\[
q_i=1-2^{-(i+2)}\in(0,1),\qquad
C_{i,0}=2c_{4i}-1,\quad C_{i,2}=2c_{4i+2}-1,\quad
R_i=2a_{4i+4}-1,\quad R_{-1}=1.
\]
Define a total strictly positive rational virtual martingale d, initialized at 1, holding at ALL virtual bits except w_{4i} and w_{4i+2}. On these it stakes respectively q_i R_{i-1}R_i and q_i R_i (signed fair-coin fractional stakes; the corresponding u bits have already been queried VIRTUALLY). For old spoiled raw signs the two eventual factors and their joint pivot price are
\[
g_{i,0}(r)=1+q_i C_{i,0}R_{i-1}r,\quad
g_{i,2}(r)=1+q_i C_{i,2}r,\quad
G_i(r)=g_{i,0}(r)g_{i,2}(r),
\]
\[
\pi_i=1+q_i^2 C_{i,0}C_{i,2}R_{i-1}.
\]
All factors are positive rational but the possible minimum 1-q_i tends to zero. S074's original direct finance still works with q replaced by the computable group-specific q_i: at the genuinely fresh c_{4i+2} filler Q bets \(1+q_i^2 C_{i,0}R_{i-1}s\), and at the genuinely fresh a_{4i+4} pivot F bets \(G_i(r)/\pi_i\). They have disjoint wagering coordinates. Consequently e_0=QF is one total positive computable fair raw martingale, and at ALL virtual checkpoints the same S073 accounting identity holds:
\[
e_0=d\,A(Q/\Pi).
\]
Here Pi includes *settled* group prices, A only credited but UNSETTLED w factors; at most one price has been paid but not charged.

There is **NO source-independent positive floor** for \(A(Q/\Pi)\), even on a single suitable (not claimed random) raw path. After the current group's a pivot and next group's c_{4i+6} finance, but before either old w settles, S074's exact checkpoint table gives
\[
A(Q/\Pi)=G_i(R_i)\pi_{i+1}.
\]
At every even i choose the old two c signs to make both g factors \(1-q_i\), and choose the next group's two c signs so that \(\pi_{i+1}=1-q_{i+1}^2\). These requirements are compatible for every disjoint even/odd pair, whatever the fresh pivot signs. Thus along ONE infinite raw assignment, the displayed ratios at these infinitely many checkpoints equal
\[
(1-q_i)^2(1-q_{i+1}^2)\longrightarrow0.
\]
This is an all-transcript floor failure, NOT an assertion of CR/OH membership of that assignment. The nonempty spoiled frontier and infinite cross-group shared-pivot dependency from S074 persist. All individual retirements remain computably finite.

## 2. Effective settlement mirrors: a sufficient criterion

### Lemma 1 — computable persistent savings

For any total nonnegative computable rational virtual martingale d with d(empty)=1, let d^[k] stop when d first reaches \(2^k\), and define
\[
\widehat d=\sum_{k\ge1}2^{-k}d^{[k]}.
\]
As in S036–S037, this is one total normalized computable nonnegative rational martingale. On a finite virtual history, choose any K with \(2^K\) strictly larger than EVERY encountered d capital. Then compute EXACTLY
\[
\widehat d=\sum_{k=1}^{K}2^{-k}d^{[k]}+2^{-K}d.
\]
Every stopped component remains locked on all continuations. If d is unbounded along a virtual path, then for each integer N, \(\widehat d\ge N\) on every sufficiently late virtual prefix, including all sufficiently late designated completed-group prefixes. In our strictly positive d example, \(\widehat d>0\) on all finite histories.

### Theorem 2 — executable two-fresh-bit settlement-mirror criterion

Fix an everywhere-total exhaustive computable virtual/raw scan pair and a strictly positive computable rational virtual martingale D (possibly a computable savings transform). Suppose the process has computably indexed groups with:

1. two ordered **genuinely fresh RAW** signs \(s_i\) (funding bit) then \(r_i\) (settlement pivot), all distinct, occurring at boundedly describable finite stage on EVERY raw history, with all other raw wagers of the proposed compiler zero;
2. a finite *already-raw-known* virtual capital history \(H_i\) at the pre-\(s_i\) instant, giving \(K_i=D(H_i)>0\), even if earlier virtual spoiled steps have not actually been replayed yet; no unqueried future bit or negative nonhalting certificate is used;
3. a total computable strictly positive rational table
\[
W_i(r,s)=D(H_{i+1}(r,s))/K_i,
\]
computed BEFORE s_i from current finite raw data, where \(H_{i+1}(r,s)\) is the next group's virtual capital history after its actual scheduled spoiled settlements; all intermediate virtual events irrelevant to D have zero stake;
4. the **fair rectangular price equation**
\[
\frac14\sum_{r,s\in\{-1,+1\}}W_i(r,s)=1
\]
on EVERY reachable raw pre-funding state; and
5. on every infinite path, the realized histories \(H_i\) are cofinal among completed virtual groups, and D-success is persistent there: for every N, eventually \(D(H_i)\ge N\).

Then put
\[
p_i(s)=\frac12(W_i(-1,s)+W_i(+1,s)).
\]
At fresh funding bit \(s_i\), Q uses child factor \(p_i(s)\); at the distinct later fresh pivot \(r_i\), F uses \(W_i(r,s_i)/p_i(s_i)\). Both are strictly positive rational and known BEFORE their respective raw reads. Equation (4) makes the two Q children mean one, and the definition of p makes the two F children mean one. Their bets occur at disjoint raw coordinates, so the *literal product* e=QF is itself a SINGLE everywhere-total computable fair positive rational raw martingale. By multiplying realized group factors and telescoping,
\[
\boxed{e(\hbox{raw immediately after }r_i)
       =D(H_{i+1})/D(H_0)}
\]
when e and D are normalized with D(H_0)=1. The right-hand side eventually exceeds every N by condition 5. Hence virtual d success (when D is its persistent savings transform) transfers to the SAME raw source EVEN WHEN inf A(Q/Pi)=0.

**Quantifier guard.** This is conditional on an explicit TOTAL pre-bit finite table and a computably recurring settlement-mirror schedule for ALL raw inputs. It does not say arbitrary T,d admit such a table, does not assume prices are martingales, and does not infer the recurrence from eventual M^Y halting.

## 3. The variable-q chain meets the stronger savings criterion

Apply Lemma 1 to the d from section 1, taking D=\(\widehat d\). Write H_i for the virtual history through the TWO w settlements of groups <i (all intervening u,v and cleanup wagers are zero). At the REAL c_{4i+2} funding instant, the previous group's REAL a pivot and the previous group's c fillers have already been read; thus the values of its virtual w wagers, even if virtual replay is still pending, are RAW-KNOWN. The entire H_i capital history and every threshold crossed so far are computable then. Importantly the upcoming virtual v/u/cleanup steps have zero stakes, so the future b and v values cannot affect the prospective savings wager table.

Before reading c_{4i+2}, know C_{i,0}, R_{i-1} and H_i. For each hypothetical \(r,s\in\{-1,+1\}\), compute the exact two extensions
\[
d_1=d(H_i)(1+q_i R_{i-1}r C_{i,0}),\qquad
d_2=d_1(1+q_i r s),
\]
and use Lemma 1's finite rational formula to obtain
\[
W_i(r,s)=\widehat d(H_i;d_1,d_2)/\widehat d(H_i)>0.
\]
Every quantity is a total finite pre-bit computation. For fixed r, the second virtual w stake is fair in s, even under stopping and weighted summation, so
\[
\tfrac12\sum_s\widehat d(H_i;d_1,d_2)
=\widehat d(H_i;d_1).
\]
For fixed C_{i,0}, the FIRST virtual w's fractional wager is odd in the genuinely fresh r; the savings transformation is a positive linear combination of stopped virtual martingales and preserves that symmetric averaging:
\[
\tfrac12\sum_r\widehat d(H_i;d_1)=\widehat d(H_i).
\]
Together these give exactly the rectangular price equation. A positive child factor cannot be zero because every original wager multiplier is at least 1-q_i>0 and the stopped savings transform is positive.

Thus the preceding Q/F algorithm is TOTAL ON ALL RAW TRANSCRIPTS, uses genuine fresh c and a bits in precisely their legal order, and gives
\[
e(\text{after real }a_{4i+4})=\widehat d(H_{i+1})
\quad\text{for every raw source and every }i.
\]
For each source on which the original virtual d succeeds, \(\widehat d(H_i)\) tends to infinity by persistent savings, and e is unbounded on its raw scan. This is an explicit **single-raw-martingale effective savings compiler without ANY uniform positive all-checkpoint aggregate escrow floor**.

For this PARTICULAR two-claim chain the original e_0 also suffices without the wrapper: between completed-group virtual histories, at most two virtual multipliers occur, each at most 2, so \(d_m\le4d(H_i)\) during group i. Thus d unbounded already forces its completed-group capitals unbounded, and
\[
e_0(\text{after }a_{4i+4})=d(H_{i+1}).
\]
This direct bounded-upward-drawdown shortcut is **not** valid when an unbounded number of potentially profitable wagers can occur between mirror cuts. The savings construction gives the more robust effective success principle, provided its re-priced joint tables can still be computed.

## 4. A precise obstruction: one remaining filler need not price three claims

The rectangular price equation is a real restriction, NOT a consequence of each virtual w bet's individual fairness.

Take THREE selected spoiled w claims at coordinates j,j+2,j+4, with their distinct real c fillers read first, then a genuinely fresh shared raw a pivot r, and only afterwards the three virtual w queries. A deterministic exhaustive virtual permutation extending the finite order
\[
v_j,\ v_{j+2},\ v_{j+4},\ u_{j+1},\
w_j,\ w_{j+2},\ w_{j+4}
\]
and querying all unused coordinates with zero stakes gives a globally legal S071 raw evaluator for E=all/even. At each virtual w bet the fair signed fraction q r, for fixed rational 0<q<1. Let the first two already-raw-known spoiled signs be C_0,C_1, and the LAST genuine fresh c filler have hypothetical sign s. The group payoff and a-pivot joint price are
\[
G(r,s)=(1+q C_0r)(1+q C_1r)(1+q sr),
\]
\[
p(s)=\tfrac12\sum_rG(r,s)
 =1+q^2[C_0C_1+s(C_0+C_1)].
\]
Consequently
\[
\tfrac12(p(-1)+p(+1))=1+q^2C_0C_1\ne1.
\]
**Proposition 3 (single-last-filler obstruction).** A strategy whose ONLY earlier financing wager for this bundle is the exact factor p(s) at the LAST fresh c filler, followed by fair a-pivot factor G(r,s)/p(s), CANNOT be a normalized martingale strategy. Its funding child mean is not one on any reachable state, irrespective of how its capital was scaled previously. Example q=1/2, C_0=C_1=+1: p(+)=7/4, p(-)=3/4, mean 5/4.

This proves impossibility ONLY for the specified one-last-filler exact-price strategy. An earlier funding bit, multi-stage Doob financing, a different legitimate raw martingale or S037's effective-renewal compiler is NOT ruled out. The triple architecture is a local obstruction embedded in a globally legal exhaustive schedule, not an OH non-invariance witness.

## 5. Relation to S037, failed shortcuts, unresolved boundary

S037 already establishes broad positive preservation under effective fresh-frontier retirement, with persistent savings and computable backward prices, without positive ratio bounds. This S075 variable-q example itself HAS computably finite claim retirement; it therefore yields **NO newly enlarged preservation class** beyond S037. The added justified result is a completely executable *forward* joint-price cash-out compiler with explicitly computed positive two-bit tables, cofinal exact settlement mirrors, and a demonstrated vanishing A(Q/Pi) floor. Unlike S074 it has NO all-checkpoint linear lower ratio, yet still a SINGLE raw martingale transfers all virtual d success. Proposition 3 delineates exactly why the same single-last-filler formula is not automatic for three claims.

Failed or unjustified methods: (i) infer e success from a finite but vanishing lower escrow ratio; (ii) apply savings to d while retaining d's OLD pre-financing prices without recomputing the stopped joint tables; (iii) treat p as automatically fair at its own pivot or multiply contemporaneous claims without their joint normalization; (iv) extrapolate the two-bit rectangular price identity to arbitrary growing claim sets; (v) use retrospectively known halting or source-specific recurrence as prospective funding data.

The real unsolved boundary is whether a source-side total executable financing/stopping certificate can handle **non-effectively retiring** spoiled claims, genuinely growing overlapping inventories, or price factors requiring several earlier funding bits. The current finite two-claim construction and S037 do not imply one. No X-specific recurrence is proved. Do not resume S057–S069 controller work automatically; if indispensable, preserve exactly four paired globally clipped M traces, prospective deadlines, real fillers, zero-stake t/u timeout release, mandatory non-s sweep WITHOUT old sentinel reset, and seven 8/7 versus one ZERO payoffs.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claims. Owner/external blocker: NONE.
