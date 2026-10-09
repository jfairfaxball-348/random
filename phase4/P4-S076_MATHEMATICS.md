# P4-S076 — Multistage joint-price financing with unbounded overlapping spoiled inventory

Date: 2026-10-09
Incoming independently pinned live main: f93ab90520175c51f1a36d3a903c8c1feedd6aff
Scope: Phase 4 mathematics ONLY, S071 supported two-coordinate XOR shears (all/even block support).
Disposition: VALIDATED EXPLICIT TOTAL MULTISTAGE FRESH-FILLER COMPILER, UNBOUNDED FINITE INVENTORY AND VANISHING INTERIM FLOOR. NOT H/SHEAR PRESERVATION IN GENERAL.

## 0. Authority and restrictions

Remote main equals the incoming SHA, parent of which is the S074 checkpoint. Tree contains exactly one of each S001–S075 mathematics, validation, close record and no S076 files. Reviewed all S001–S075 mathematics, S075 validation/close, CAND-01 / Gate-3 selection, both pivots and priority S008/S011/S012/S027/S032–S044/S052–S057/S065–S075. Nothing is reopened. Preserve MLR ⊆ R₂ ⊆ OH^iso ⊆ OH ⊊ CR; the ORIGINAL CR Y, unchanged syntactically self-avoiding globally use-clipped wtt M, repeated three-bit H, X=H⁻¹(Y), H(X)=Y notin OH. X in OH, supported-shear and H preservation, R₂=OH, R₂=OH^iso, and arbitrary homeomorphism invariance remain UNRESOLVED. S073 L F Π=d A and three-account estimate, S074 sharp fixed-q 3/16, S037 effective renewal/backward-price theorem and S075 savings mirrors are retained.

## 1. Finite multistage price lemma (all stages genuinely fresh)

Let K>0 be total computable from a finite already-raw-determined virtual-capital history h. Let m>=3, and let c_0,...,c_{m-1},r be DISTINCT real raw fair signs read IN THAT ORDER, each from an as-yet-unqueried source coordinate. Let B(r,c_0,...,c_{m-1})>0 be a total computable rational prospective terminal capital, computable as a full finite table before c_1, with

(A) 2^{-(m+1)} sum_{c,r} B(r,c)=K,

(B) 2^{-m} sum_{c_1,...,c_{m-1},r} B(r,c_0,c_1,...,c_{m-1})=K for BOTH c_0 signs.

Condition (B) means the first c_0 wager is identically 1, permitting h to become known only after that filler is read, as long as the entire table is computable before c_1. Define absolute backward prices
P_k(c_{<k})=2^{-(m-k+1)} sum_{r,c_k,...,c_{m-1}} B(r,c)
for 0<=k<=m, where P_m(c)= (B(-1,c)+B(1,c))/2.
Then P_0=P_1=K; all P_k>0; and
[P_{k+1}(c_{<k},-1)+P_{k+1}(c_{<k},+1)]/2=P_k(c_{<k}).
At the fresh c_k (k>=1) wager factor P_{k+1}/P_k, known BEFORE the bit; at c_0 wager 1. At the strictly later fresh raw r wager factor B(r,c)/P_m(c). Every pair of children has mean 1, and every factor is positive rational. Do NOT multiply separately betting martingales on overlapping coordinates: these are successive factors of ONE martingale e, holding at every other raw coordinate. Its entire group factor telescopes:
(∏_{k=0}^{m-1} P_{k+1}/P_k) · B/P_m = B/K.
The finite sums, prices and all wagers are total computable on EVERY finite reachable transcript. Normalization is a consequence of verified conditions (A) and (B), NOT an automatic property of an arbitrary speculative price table. There are NO future stakes, nonhalting certificates, or zero-time infinite searches.

For the S075 three-claim payoff B/K=∏_{j=0}²(1+q c_j r), q rational in (0,1), direct prices normalized by K satisfy
p_0=p_1=1,
p_2=1+q² c_0 c_1,
p_3=1+q²(c_0 c_1+c_0 c_2+c_1 c_2).
Thus c_1 carries p_2, c_2 carries p_3/p_2, and r carries G/p_3. At q=1/2 and c_0=c_1=+1, S075's invalid last-c factors (7/4,3/4) have mean 5/4; the CORRECT c_2 factors are (7/5,3/5), of mean 1, financed by c_1's earlier p_2=5/4. This specifically solves the S075 restricted one-slot obstruction, not every arbitrary bundle.

For arbitrary m with factors g_j=1+q c_j r (or g_0=1+q R_prev c_0 r), the DIRECT prices are
p_k(c_{<k}) = (∏_{j<k}(1+q a_j c_j)+∏_{j<k}(1-q a_j c_j))/2
where a_0=R_prev and a_j=1 for j>0. In particular p_1=1 for all c_0. The price may have high-degree even interactions and need not be paid by its last filler alone. p_k>0 because q<1.

## 2. Explicit unbounded-inventory rolling infinite scan

Choose m_i=i+3, N_0=0, N_{i+1}=N_i+m_i. Group i consists of ALL three virtual coordinates in source blocks with indices 2N_i,2N_i+1,...,2N_{i+1}-1; its m_i ACTIVE selected blocks are the even ones e_{i,k}=2(N_i+k), 0<=k<m_i. For both E=all and E=even, each e_{i,k} is shear-selected with virtual (u,v,w)=(a,b XOR c,c). In each group define C_{i,k}=2c_{e_{i,k}}-1, and let R_i=2a_{e_{i+1,0}}-1 be the genuine fresh next-group a-pivot. Put R_{-1}=+1 and q_i=1-2^{-(i+2)}.

The deterministic virtual permutation T first requests v_{e_{0,0}},...,v_{e_{0,m_0-1}}. Then for EVERY i in order:
1. request v_{e_{i+1,0}} (opening the next group early);
2. request u_{e_{i+1,0}} (the genuine later a pivot R_i);
3. request v_{e_{i+1,1}},...,v_{e_{i+1,m_{i+1}-1}} (later TRUE c funding fillers);
4. request w_{e_{i,0}},...,w_{e_{i,m_i-1}} (all selected spoiled w, SILENT on the raw evaluator);
5. exhaust every still-unused virtual u/v/w coordinate of all 2m_i blocks of group i, in fixed natural order, at zero virtual stake.

Each virtual coordinate occurs exactly once, every group is finished in finitely many explicit steps, and all blocks eventually get exhausted. This T is an everywhere-total computable exhaustive permutation independently of input. Apply the UNCHANGED S071 raw evaluator P_E,T. A selected v queries REAL fresh raw c first (zero-stake filler unless specified financing wager) then fresh raw b, and selected subsequent w is silent; u queries genuinely fresh raw a. The complement is queried once. By S071, P is everywhere total, exhaustive (zero-hole), computable, no-repeat and fair-coin preserving on EVERY transcript, for both supports. All non-financing filler/cleanup steps have zero raw stakes. No simulated virtual step changes the raw scan. At the pivot R_i all group-i c fillers are already known and every group-i w is still unqueried virtually. Before those old w claims retire, the next group's c's have been partly opened; its first c is read BEFORE R_i and its remaining c's AFTER R_i. Hence outstanding spoiled claim inventory at R_i is m_i→infinity, and groups overlap along an infinite chain.

Define a strictly positive normalized total computable rational virtual martingale d: zero stakes except at the m_i virtual w requests of group i. The first bets signed fractional stake q_i R_{i-1}R_i; every remaining one bets q_i R_i. All are determined by earlier virtual u queries; no stake depends on its own w. Each child is between 1-q_i and 1+q_i. With w signs C_{i,k}, the group gain is
G_i(R_i,C_i)=(1+q_i R_{i-1}R_i C_{i,0})∏_{k=1}^{m_i-1}(1+q_i R_i C_{i,k}).

Let h_i be the capital-and-stopping history of d through all prior groups' w settlements, omitting intervening zero-stake virtual bits. h_0 is empty with capital 1. At the first next-group c_{i,0} read, h_i may NOT be known because the previous R_{i-1} may not yet have been read, but the c_0 factor is 1. By the time the SECOND c_{i,1} is about to be read, the previous pivot R_{i-1} IS raw-known, and all earlier groups' c fillers and pivots are already raw-known; therefore their w factors and ENTIRE stopped-capital history h_i are computable, even if their virtual w queries are still pending. Nothing outside the w wagers affects d or its savings transform. At this pre-c_{i,1} moment, the finite table for every hypothetical r and all remaining c's is total computable and uses no future outcome. At group 0 the seed R_{-1}=1 and h_0 is known initially.

## 3. Effective savings mirror and success transfer

Let D=hat d be the frozen S036 threshold-stopping savings martingale:
D(h)=∑_{k>=1}2^{-k}d^[k](h).
At every finite history, if 2^K exceeds every prior capital, the tail is exactly 2^{-K} times the current d capital. This computes D as a positive rational on ALL finite histories; if d succeeds, D is eventually larger than every bound on ALL later virtual prefixes.

For fixed h_i define B_i(r,c)=D(h_i followed by the m_i ordered virtual w outcomes c using the prospective stakes with R_i=r). For fixed r, the successive c outcomes represent fair virtual w children, so averaging all c returns K_i=D(h_i). Similarly averaging c_1,...,c_{m_i-1} and r after fixing c_0 returns K_i: first w averages at each fixed r and then all remaining w average. Thus B_i satisfies exact conditions (A),(B). It is strictly positive, because d factors and D are positive. At pre-c_{i,1} calculate all absolute prices P_{i,k} as in §1 and use successive genuinely fresh c factors and the later a-pivot factor, holding at all other raw steps. The initial c_{i,0} factor is ALWAYS 1, so no unknown h_i is required then. Each wager is computed BEFORE its actual fresh read. This defines ONE total strictly positive normalized computable rational fair raw martingale e on P_E,T, for all raw transcripts. No unsupported same-coordinate product is used.

Induction using exact telescoping and the chosen group schedule proves, at the raw instant just after genuine pivot a_{e_{i+1,0}} and BEFORE next-group c_{i+1,1} funding,
e = D(h_{i+1})
for every raw source and every i, since D(h_0)=e(empty)=1. A prefetched next-group c_{i+1,0} has trivial factor 1. Each virtual group finishes in finite computable time, so these settled histories are cofinal. If d is unbounded on the virtual scan output, persistent savings ensures D(h_i)→∞; hence e is unbounded on the SAME raw P output. This is a success compiler for this EXPLICIT infinite family; it neither classifies X nor handles arbitrary persistent non-effectively retiring claims.

The DIRECT d version also works via the closed-form p_k formula and mirrors d at every pivot. Crucially at the pivot BEFORE old virtual w settlement the virtual d still equals d(h_i), whereas direct e=d(h_i)G_i. Along the ONE compatible infinite source with all R_i=+1 and all selected C_{i,k}=-1, the exact interim ratio is
e/d=(1-q_i)^{m_i}→0.
Thus no source-independent all-virtual-checkpoint positive ratio floor exists. This does not assert that this deliberately specified source is CR or OH; savings-mirror success needs no such floor. The inventory size m_i is unbounded, q_i→1, and all factors remain >0 at each finite stage.

## 4. Limits, failed methods, preserved boundaries

* Last-filler exact price G averaged over r is NOT generally fair in the last c; the missing fair denominator is the prior conditional price p_{m-1}. For m=3 this is S075's strict obstruction.
* Charging the complete known p_m at r, or multiplying the m individual same-r fair wagers, is not fair unless its conditional expectation happens to be one. The recursive ratios MUST use real earlier c bits.
* The first c must wager 1; retrospectively inserting a nontrivial bet before h_i is known is invalid. Our exact P_1=P_0 identity makes the rolling schedule executable.
* Arbitrary S071 scans/martingales need NOT satisfy the finite prospective-table or c-first equal-price hypothesis; no universal fair conditional prices follow.
* Each individual old claim retires at a computably specified finite stage; this example does NOT breach the S037 effective-retirement boundary or prove a new general H/shear preservation class. Unbounded width alone is not the non-effective infinite persistence obstruction.
* A virtual success argument on original committed X, or a negative halting certificate for its M, is NOT supplied. S057 controller is NOT invoked; its four paired globally clipped M traces, prospective deadlines, real fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, and seven 8/7 versus one ZERO payoffs remain frozen.
* No R₂=OH, R₂=OH^iso, H/supported-shear invariance, general homeomorphism invariance, or X in OH follows. Retain S073 cash/price/pending-account distinctions and S074 3/16 sharp fixed-q estimate unaltered.

Exact-rational audit: m=3,3,4,5,6 and q=1/2,3/4,7/8,15/16,31/32, both previous signs and two prior histories, direct and savings; 2048 prospective settled-endpoint checks, zero discrepancies. Finite raw scan simulation for 3+4+5+6 consecutive groups produced 108 distinct/exhaustive real raw reads for each E=all/even, with 36/18 respectively silent selected w steps and zero holes; see validation. Finite checks supplement, never replace the proof.

PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker: NONE.
