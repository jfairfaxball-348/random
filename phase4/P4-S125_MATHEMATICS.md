# P4-S125 — Proper overlap with real erasure and asynchronous ghost FOLDs; local sharp partial inversion

13 October 2026. ONE newly owner-invoked Phase4 CAND-01 mathematics session. INTERNAL same-agent mathematical development, not external/formal/novelty certification.

## Authority and hostile inherited proof audit

Remote main at entry: 519520e019903811c578314e5a043901f5fa1952, S124's single atomic commit with SOLE parent ed9410b9da23807c9d1c44ab6738f9cd9fee5d2e, tree 686d974f63509254c727a1df4cbb38d3076c208a, merged PR #22 (head equals main); no S125 file, branch or open PR. No intervening newer main. Tree contains no .github workflow definition; hosted runs 0, check-runs 0, individual commit statuses 0 (the aggregate API says pending with zero actual contexts): ABSENT_NOT_PASS. Rulesets []; protection GET 403 UNKNOWN.

We independently re-derived S124: M_l(u)=2^{-l} sum_{|v|=l}d(vu) is root-one rational with fair child average and upper bound 2^{|u|} from the full nonnegative level sum. T_{k,l}(s)=1 up to k and M_l(s[k:]) after k is coherent at the switching node. With dyadic weights 2^{-k-1}2^{-l-1}, the k>=|s| tail is exactly 2^{-|s|}, and remaining l>=L error is bounded by 2^{|s|-L}; hence the real mixture has a uniform effective modulus. Child-difference approximations within 2^{-|s|-4} and root 2 make an exact rational nonnegative martingale within 1/8 of 1+mixture. Its fixed positive k,l summand transfers every output winner between streams having a common infinite suffix. Sigma(a u)=u cannot coincide with a fair homeomorphism on positive measure inside [a], since the first scales that set's image measure by two and the latter preserves it. These claims withstand this same-agent algebra audit. S121's G_U has true fibres {0y,1y} before/no release, and {c rho 0v,c rho 1v} after a release y=rho c v, with all off-path output prices correct; its fat nowhere-dense K supports no nonzero computable measure by diagonalization. S122's two XOR clocks and S123's two nonlinear invertible fair charts remain restricted compilers, not a general FOLD result.

## A125. An explicit fair exactly-two F with proper overlap and indefinite asynchronous finite-row FOLD clocks

For a in {0,1}, define computable bit permutations pi_0,pi_1:
  pi_0(2j)=2j+1; pi_0(2j+1)=2j;
  pi_1(0)=0; pi_1(2j+1)=2j+2; pi_1(2j+2)=2j+1.
Let P_a(v)_n=v_{pi_a(n)}. These are computable fair homeomorphisms and pi_a(n)<=n+1.

For every x=a b c v (three header bits and an infinite tail), define F(x) = h(a,b,c) P_a(v), with two-bit header
  h(0,0,c)=00, h(1,0,c)=11  (c REALLY ERASED);
  h(a,1,0)=01, h(a,1,1)=10 (a HIDDEN).

F is total computable. For output length m=1 its header requires at most 3=m+2 source bits; for m>=2 the tail of length n=m-2 requires at most n+1 source-tail bits and three header bits, hence <=m+2 source bits. So F has additive use <=2.

GLOBAL FAIRNESS: the headers 00,01,10,11 each have probability 1/4; conditional on any header the independent tail P_a(v), or the 50/50 mixture of P_0(v),P_1(v), is fair. Thus for ALL output tau of length m>=2, lambda(F^-1[tau])=2^{-m}; lengths zero and one follow by summing. Equivalently every length-m output cylinder contains EXACTLY four length-(m+2) source cylinders (for m>=2), including off-path cylinders.

COMPLETE INFINITE FIBRES: write w=P_a^{-1}(t), unique computably. Then
  F^-1(00t)={000w,001w};
  F^-1(11t)={100w,101w} with a=1 so w=P_1^{-1}(t);
  F^-1(01t)={010 P_0^{-1}(t),110 P_1^{-1}(t)};
  F^-1(10t)={011 P_0^{-1}(t),111 P_1^{-1}(t)}.
In the 00 formula w=P_0^{-1}(t). These are the WHOLE compact infinite fibres, always exactly two; there are no hidden third/fourth inverses or remaining finite ghosts.

Component ranges are I_0=[00] union [01] union [10], I_1=[01] union [10] union [11]. They are BOTH PROPER clopen subsets of Cantor space, with PROPER overlap [01] union [10] of fair measure 1/2; neither component is onto. On [00] and [11], c is irreversibly erased: each unique key component contributes BOTH actual inverse streams. On [01] and [10], each key component has ONE actual inverse, so the only two genuine alternatives differ at a. In the shared overlap the four length-(m+2) compatible rows split 2:2 between the keys. The spare tail-coordinate in each key cone is a finite ghost; pi_0's PERM/FOLD clock alternates opposite pi_1's, and both have infinitely many FOLD restarts. This is a fully legal overlap example with actual one-off erasure on exclusive cones and infinite ASYNCHRONOUS temporary ghosts on the overlap, not two continuing permanent erasures on the overlap.

CONSERVATION: for each actual input header (a,b,c), x=a b c v is CR iff v is CR (fixed finite prefix), while F(x)=h(a,b,c)P_a(v) is CR iff P_a(v) is CR; computable fair homeomorphism invariance makes these equivalent. Indeed F preserves CR in BOTH directions on every input, and each output y has two CR inverses iff y is CR. No Schnorr-random NONCR output with CR inverses exists here. A winning output martingale can be transferred by a single finite-header mixture of the effective fair homeomorphism and common-prefix martingales; this is a RESTRICTED certificate, not an all-c2 compiler.

Why this matters: proper image overlap + globally complete double fibres + real erasure elsewhere + two infinite, disjoint transient FOLD clocks still do NOT create the paired destroyer. Genuine repeated permanent loss must be located on an overlap BOUNDARY or else violate the fibre cap. Finite ghost folds and persistent information loss must not be conflated.

## A125 firewall: the all-F2 overlap multiplicity constraint

Let G be ANY total continuous globally cap-two map and I_a=G([a]). For every y in I_0 intersection I_1, there is at least one actual inverse in EACH disjoint input cone [0],[1]. Since total fibre size is <=2, there is EXACTLY one in each. In particular, two real erasures inside either cone at such y would force at least three actual inverses, impossible. This unconditional fibre-count firewall needs NO effective chart, fairness or additive-use bound. In a globally fair map (hence onto), two CR preimages over a nonCR output in the interior of the overlap are separately ruled out by S106/S118's effective clopen injective certificate; this latter stronger interior-conservation fact is INHERITED, not a new theorem. Any successful paired destruction therefore has to exploit the boundary, with divergent ghost replacements and no persistent double-per-cone actual fibre. The firewall does not by itself exclude an overlap-boundary example.

## C125. Local boundary criterion for the sharp 2/3 PARTIAL randomized inverse threshold

S124 used DENSE c.e.-open U. Density everywhere is unnecessary. Let U be ANY c.e.-open trigger set in the S120 G_U release/erase mechanism, K=2^omega minus U, and assume SOME computably random y belongs to K intersection closure(U). Define uniform unconditional success r as infimum over all CR output oracles z of coin probability that a partial randomized streaming algorithm emits a COMPLETE true inverse; nontermination counts as failure.

Then SUP_A r(A)=2/3. The lower bound is S124's probability 2/3 immediate fair key candidate C_a and 1/3 wait for release, whose success is 2/3 both on U and K. For the upper bound, put p=probability that A emits its FIRST source bit at the CR boundary y. Success(y)<=p. For each epsilon>0 choose finitely used oracle prefix rho of y and finite-time/measurable coin event E of mass >=p-epsilon on which the first bit has already been emitted; choose minority output-key c among these runs, with mass <=p/2. Since y is in closure U, a first-trigger cylinder inside U extends rho (as y is nonrelease); append release bit c and a CR continuation z. Every actual inverse of z begins with c, so success(z)<=p/2+1-(p-epsilon). Therefore r<=min(p,1-p/2+epsilon), and r<=2/3 on letting epsilon vanish. The proof uses ONLY the local boundary CR point, NOT global density or eventual termination. It makes no conditional-on-termination assertion.

This genuinely extends S124: take its dense fat c.e.-open V with complement containing CR w, and U=0V. Then U is NOT dense in Cantor space ([1] is disjoint), but y=0w is CR and lies in K intersection closure U. The same sharp 2/3 uniform optimum holds. In contrast if U is clopen, membership/first release can be decided from a bounded output prefix and there exists a TOTAL deterministic genuine inverse selector (success 1), selecting either key on K and the revealed key on U. Thus topology of the unresolved trigger, not mere finiteness of the hitting candidate list, controls this threshold in these two examples. S123's a.s.-total 1/2 ceiling and S122's no-all-CR deterministic true selector for dense U are retained with their separate quantifiers.

## B/D. Hostile failed counterexample and direct target accounting

An arbitrary fair additive-use-two cap-two G has four source (m+2)-cells above every m-output cell. Its q_s(tau) posterior lies on the 1/4-grid after the fixed s is resolved. On CR output paths each q_s eventually stabilizes (S121/S117 volatility martingale); on a target Schnorr-random NONCR output it may oscillate indefinitely, and using the CR stabilization result there is circular. Along two genuine inverses, finite ghost replacement can continue forever. A moving-horizon conditional expectation of d(G(X)|m) is NOT one coherent source martingale; the present F permits a compiler only through fixed prefix and computable homeomorphic tail charts. No general additive-two source compiler or legal c2 counterexample to that statement was obtained.

Global known S011 fair F2 CR destroyer is an UNBOUNDED-USE adaptive scan with a SINGLETON bad fibre; it is NOT a c=2 counterexample or an exact-double failure. S083 likewise cannot be silently repurposed as a same-source R_L1-minus-R2 witness. CP2/DP2 and the double-CR to NONCR witness remain unknown.

EQ: forall z in CR minus MLR, exists total globally fair cap-two G and total rational output d with unbounded d(G(z)|n). SEP: exists ONE z outside MLR such that forall legal G in F2, forall total rational d, d(G(z)|n) is bounded. No instance of either central quantifier is established by A125/C125. SAME-SOURCE requires z in R_L1 minus R2, not merely a source outside raw OH. Unrestricted F2(R2) subset R2 or its failure remains unproved: G2 o G1 may possess FOUR actual infinite inverse streams. This session does not generalize the conserving example to arbitrary maps.

No novelty or priority claim; Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. No Lean/Palomar/outside contact. S126 FUTURE ONLY.
