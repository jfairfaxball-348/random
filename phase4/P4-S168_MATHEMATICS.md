# P4-S168 — ML-deficiency compiler attack and the exceptional-output fibre trap

Date 2026-10-15. INTERNAL same-agent mathematics; no independent or formal verification. ENTRY main 55a20bedb4adb11453dc595095aeee3838a6dcb6, tree 12a4b397c91323f2d21e72b10418eefd04b085e4, sole parent 75372ef69068f9c81c17d1bfd30de5562aa85314. S167 is the actual sole-parent authored commit, integrated unchanged in merged PR #68 (2026-10-15 16:36:34Z). Entry prompt blob 461ba9f06681bf145c33a4fde0cbc8d97aed9c2a. No open PR, no S168 record on main and no competing S168 active branch at entry. No Actions runs, check-runs, or status contexts (ABSENT_NOT_PASS); rulesets []; branch protection read returns 403 UNKNOWN_403.

## Definitions, H1 quantified goal

X=2^omega, lambda=fair coin. F_k = all TOTAL computable globally lambda-preserving X->X having <=k ACTUAL COMPLETE inverse streams above EVERY infinite output. R_k = {x in CR : G(x) in CR for all G in F_k}; R_fin = intersection_(k>=1)R_k. We need EITHER every x in CR\MLR admits one x-dependent finite k, one legal G in F_k, one total exact nonnegative rational output martingale d succeeding on G(x), OR a SINGLE x in CR\MLR surviving every legal finite k. MLR subset R_fin is baseline. This session proves neither direction.

## A168: finite-open-certificate exposure fails without an additional oracle principle

Fix a uniformly c.e. nested universal ML test U_n with lambda(U_n)<=2^-n and x in CR intersect_n U_n. A natural but invalid "compiler" scans source coordinates until it has witnessed x in U_n, then advertises that certificate as a prediction of an as-yet unseen fresh source bit j.

**Lemma A168.1 (no fresh bit from an observed open certificate).** Suppose a finite set S of coordinates and their values has been read, and these observations semidecide x in U_n by establishing a finite basic cylinder [sigma] subset U_n containing all observations used for that certificate. If j was NOT queried and j is not among the coordinates prescribed by sigma, both possible values of x(j) extend sigma and retain U_n-membership. If instead sigma prescribes j, establishing membership from genuinely observed source values has already required reading j, so j cannot still be a fresh wager. Thus the certificate alone supplies no pre-revelation prediction of an unqueried j.

Proof: by definition a cylinder restricts only finitely many input bits. Both j-extensions remain in it when j is free. A machine that has not read a prescribed j cannot certify the corresponding cylinder from its observations; it may guess correctly, but then its correctness is an additional assumption rather than a consequence of U_n-membership. For ordinary prefix cylinders sigma (the usual presentation) this holds verbatim; any finite-coordinate observation can be replaced by its finite union of compatible prefix cylinders. QED, scope: this PARTICULAR membership-certification scheme, NOT arbitrary partial oracle reductions using extra information.

Consequently a compiler must exploit a nontrivial partial sibling-divergent predictive relation in addition to naked ML-test membership. For a chronologically SOURCE-computable total predictor succeeding infinitely many times on a CR x, the exact rational source martingale that doubles on predicted next bits succeeds, contradiction. S011's wtt autoreduction exploits future source queries and partiality on siblings; it is not equivalent to a total chronological source predictor. We did not prove or disprove that each nonMLR CR x admits a suitable partial autoreduction. No uniform finite-k detector constructed.

**Finite-round product.** Any finite composition G_r∘...∘G_1 of F_(k_i) maps has global complete-fibre cap product_(i<=r)k_i. An unbounded sequence of rounds gives neither an infinite product cap nor, without independent proof, a total computable limit. Conversely S011 already shows infinitely many adaptive prediction epochs CAN coexist with cap2; the right invariant is ACTUAL unqueried coordinates over every output, not round count. A168.1 does not establish impossibility of clever adaptive ML-deficiency compilers.

## B168: exact fibre theorem for no-repeat adaptive scans

Let q(t,tau) be total computable on every t and tau in 2^t, such that q(t,tau) differs from every q(s,tau|s), s<t. For x define y=F_q(x) by y(t)=x(q(t,y|t)). A finite transcript determines the next query, so F_q is total and computable as a Cantor map, with no repeated source query. For each y define Q_y={q(t,y|t):t in N}.

**Theorem B168.1 (all-output complete-fibre formula).** For EACH infinite y, the FULL infinite inverse fibre is exactly
 F_q^-1{y}={x: for all t, x(q(t,y|t))=y(t)}.
Hence, if h_y = |N\Q_y| is finite, the actual cardinal is 2^(h_y); if N\Q_y is infinite the fibre has cardinal 2^aleph0. It is nonempty for EVERY y. Every output cylinder [tau] of length m has lambda-preimage 2^-m, regardless of the unqueried set on infinite paths. Thus F_q is globally fair.

Proof: the t coordinates are distinct, so the m prescribed independent input fair bits have probability 2^-m. Every assignment of remaining bits extends these constraints. By induction on t, running F_q on ANY such assignment emits y(t), since past emitted bits equal y|t and hence the query address is exactly q(t,y|t). Conversely any preimage necessarily satisfies each equality. The claimed cardinal follows from the independent free coordinates, including the infinite case. This counts COMPLETE streams rather than approximating cells. QED.

**Corollary B168.2.** F_q belongs to global F_k iff for EVERY y, |N\Q_y| <= floor(log_2 k). For any such no-repeat scan, global F2 and global F3 are the SAME subclass (at most one permanently omitted coordinate for every y). A scan never has exactly three full inverses. This is a theorem about the scan OBSERVER subfamily only, NOT R2=R3 in the unrestricted globally fair map class. It is structurally compatible with S011, the old one-hole results and S167's general-j multiplicity theorem; claim no unreviewed priority.

## C168: an almost-everywhere bijective fair map outside EVERY F_k

Define the explicit scan T by: while the emitted transcript contains no 1, at stage t query source coordinate 2t; once any 1 has appeared, query the LEAST source coordinate not yet queried. Emit the source bit read. Its next query is computable from the finite emitted transcript; every query is fresh. At stage t the query is <2t+1, giving a simple computable input-use upper bound 2m for m output bits.

**Theorem C168.1 (exact global structure).**
(1) T is everywhere total computable and lambda-preserving on EVERY output cylinder.
(2) If y=0^omega, Q_y={0,2,4,...}, so there are continuum many distinct COMPLETE inverses: all x with x(2t)=0 and arbitrary odd bits.
(3) If y contains at least one 1, its first such 1 at output index n caused queries 0,2,...,2n. All later queries enumerate N\{0,2,...,2n} in increasing order. Therefore Q_y=N, the full fibre is exactly ONE complete source sequence. Explicitly the source bits at positions 0,2,...,2n are y(0),...,y(n)=0,...,1, and the remaining source positions in increasing order are filled with y(n+1),y(n+2),... .
(4) lambda({y: |T^-1{y}|>1})=lambda({0^omega})=0; but T is not in F_k for ANY finite k, even F_count (the exceptional fibre is uncountable).
(5) T preserves computable randomness on EVERY CR input, hence is NOT a hierarchy separator.

Proof (1)-(4): B168.1 and the explicit query schedule. For (5), any x with all even-coordinate bits zero is nonCR: the total rational source martingale bets its entire current capital on a zero at each even coordinate and holds across odd positions; it doubles forever on that x. Thus a CR x has a LEAST n with x(2n)=1. For that n, T(x)=0^n 1 z, where z is the subsequence of x obtained by deleting just the FINITE coordinate set {0,2,...,2n} and retaining all other coordinates in increasing order. Deletion of finitely many known coordinates preserves CR (S113; alternatively any successful rational martingale after deletion can be lifted, with finite-bit-conditioned tagged accounts, to an ordinary total source martingale). Prefixing a fixed finite word preserves CR by the reciprocal prefix conditional construction. Hence T(x) is CR. QED.

All conditions include the exceptional output and its infinitely many actual missing coordinates. This map exposes the EXACT failure of the inference "lambda(E_(k+1))=0 => G∈F_k". It is stronger than S167's pointwise-finite variable erasure benchmark in the sense of a.e. degree ONE, but is INCOMPARABLE in exceptional fibre type (continuum here versus finite unbounded there). S167's conclusion only controls fibres at CR-source images, consistent with C168.

**Corollary C168.2 (no surgery changing only nonCR sources).** Suppose H:X->X is a TOTAL continuous map agreeing with T on ALL CR source inputs. CR is dense (indeed conull), so for any x, select CR x_i->x and use continuity to obtain H(x)=lim H(x_i)=lim T(x_i)=T(x). Therefore H=T everywhere and H cannot lie in any F_k. In particular a proposed repair that modifies T ONLY on nonCR inputs cannot yield a globally finite-fibre total computable observer. This does NOT prevent surgery changing some CR inputs, or an entirely different detector for a chosen x.

## D168: common same-source survivor attempt

List every valid (G,d) with G total computable fair of SOME finite global fibre cap and d a total rational output martingale. The union over these valid pairs of preimages of d-success is null; each pulled-back success event is null by global fairness, so R_fin is conull (as already known from MLR). The set intersection_n U_n of a nested universal ML test is null and includes nonMLR CR inputs, yet conullness gives NO witness in its intersection with R_fin.

An illustrative adversarial test of the false finite-stage selection argument is V_n=[0^n]. Every V_n is nonempty open with lambda(V_n)=2^-n and has positive-measure intersection with the complement of ANY countable union of null failure sets; however intersection_n V_n={0^omega}, which is nonCR. This V is NOT a universal ML test and does NOT replace U; it is a counterexample to the proposed GENERAL compactness inference from stagewise positive measure. Valid legal observer indices are not a decidable c.e. list, and a construction must force nonMLR and all legal preservation at the SAME x. No such forcing constructed.

## E168: literature boundary and H1-H5 verdict

Rute/Petrovic's published characterization (also described in "Randomness and invariance", Journal of Logic and Computation 35(8), 2025, section 3.4, Theorem 40; https://academic.oup.com/logcom/article/35/8/exae083/8377131 ) says preservation of CR under ALL lambda-a.e. computable globally fair maps characterizes MLR. This has DIFFERENT quantifiers and domain/fibre restrictions: it does NOT by itself supply an everywhere-total globally F_k witness for each nonMLR CR x. This is only an external-scope pointer, not a claim of unperformed detailed proof-prior-art audit. It suggests a specific conversion obligation for S169.

Primary H1 R_fin ?= MLR remains OPEN. H2 a fixed K remains OPEN. H3 every adjacent-level strictness remains OPEN. H4: new explicit observer T is a.e. one-to-one but has an uncountable exceptional fibre, so it lies in F_all but not F_count/F_pf/F_ub; previous F_pf\F_ub witness from S167 persists. No RANDOMNESS-CLASS separation. H5: scan-only powers-of-two degree phenomenon is rigorous restricted-family arithmetic; prime/composite/modular global classes, R_pi/prime-growth undefined and OPEN. R2=R3, E-08/E-00/S-00, S165/S166 A-source OPEN. Frozen Y/M/H/X, S101-S103 A-C, DEF-0020, PA-0001, prior source grades unchanged. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
