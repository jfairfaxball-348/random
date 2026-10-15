# P4-S151 — Information-refinement obstruction to SAME-SOURCE R2/R3 transfer

**Internal mathematical proof, one owner-invoked session 2026-10-15.** Entry live main 3c0b023b742b64ff8b4ec3b619ef1f8f44037a74; predecessor S150 PR #50, authored head 3c0b023b742b64ff8b4ec3b619ef1f8f44037a74, parent 249c81e5264ad2d96f134c3607991680c7a543f4, tree ed494d3f68c8f25549914d2e479cab3696df1bd3, 20 changed paths, direct expected-head non-force fast-forward. No competing S151 records or branch on main, no open PR. Hosted Actions runs 0, check runs 0 and individual statuses 0 (**ABSENT_NOT_PASS**), rulesets [], protection 403 **UNKNOWN_403**. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN/Phase5 CLOSED. Selected CAND-01. No Gate4, paper or originality claim.

Definitions from S149/S150: for total computable globally fair G:2^omega→2^omega, output n-word tau, m input bits determining the first n output bits, let P_tau be lambda conditioned on G(X)|n=tau; its mass denominator lambda(G^-1[tau])=2^-n. Let B(X)=1_{G(X)_n=1} and rho_m(X)=E[B|X|m, G(X)|n=tau]. This is computable rational on each compatible m-word (compute at a finite longer modulus for n+1). For positive rational output martingale p=d+1 and r_b=p(tau b)/p(tau)>0, r0+r1=2, put A_m=r0+(r1-r0)rho_m. No fibre assumption is needed.

## A151.1 Exact arbitrary-use refinement law (INTERNALLY PROVED)

**Theorem.** For EVERY fair total computable G, EVERY n,tau, every two source-prefix lengths m'≥m for which the first n output bits are decided, write E_tau for P_tau-expectation. Then
(1) E_tau[rho_m]=E_tau[rho_m']=1/2;
(2) Var_tau(rho_m')-Var_tau(rho_m)=E_tau[(rho_m'-rho_m)^2]≥0;
(3) E_tau[A_m]=E_tau[A_m']=1; Var(A_m')-Var(A_m)=(r1-r0)^2 E_tau[(rho_m'-rho_m)^2];
(4) E_tau[log A_m']≤E_tau[log A_m], with strictness if r0≠r1 and rho_m' is not a.s. constant given m.

**Proof.** On the clopen G^-1[tau], the source m-prefix partition refines as m grows. Both random variables are versions of the conditional expectation of B, hence E[rho_m'|X|m,tau]=rho_m. Expand (rho_m'-1/2)^2 around rho_m and discard the zero conditional cross term. The same expansion applied to affine A proves (3); conditional Jensen of log gives (4). Each expectation is an explicit finite dyadic weighted sum: all compatible m-prefixes have the same conditional mass 2^(n-m), so there is no hidden noncomputable measure assumption. A chosen source path may have the opposite sign; this result NEVER selects x.

**Exact information interpretation.** For the N=2^(m-n) compatible m-cells set U_m(s)=1/N and Q_m(s)=A_m(s)/N. By (3), Q_m is a probability distribution. Under refinement m→m', the Q_m distribution is exactly the coarse marginal of Q_m', by the tower identity. Consequently D(U_m||Q_m)= -E_tau log A_m is monotone NONDECREASING, with the excess given by the usual finite conditional relative-entropy chain rule. This KL is one-step source-population reweighting under p, NOT a pathwise effective martingale or an R2 observer.

## B151.1 Universal over-reading saturation (INTERNALLY PROVED)

**Theorem.** Let h(n+1) be any computable use fixing the first n+1 output bits of a total computable fair G. At a stage n≥1 choose ANY compatible read length m≥h(n+1) (possibly enforced by a strictly increasing overread clock). Then rho_m(s)∈{0,1} for EVERY compatible source cell. Fairness makes exactly half the N cells have rho=0 and half rho=1. Hence FOR EVERY tau:
Var_tau(rho_m)=1/4 (maximum possible for a [0,1] variable of mean 1/2),
E_tau log A_m=(log r0+log r1)/2,
D(U_m||Q_m)= -1/2 log(r0*r1).
If r0≠r1, this KL is strictly positive everywhere. Choosing an overread clock sufficiently ahead is possible for EVERY total computable G and all n≥1 (u(0)=0 and later strictly increasing), even when G is a degree-one computable measure-preserving homeomorphism.

**Proof.** Knowing the next output bit makes B measurable at the source m-prefix. Its conditional expectation rho_m equals B. Half/half follows from lambda(G^-1[tau b])=2^-(n+1), while each compatible m-cylinder has equal fair source mass. Substitution gives the identities. **Therefore positive/large population variance, negative mean log A, and positive KL, even uniformly across ALL output prefixes and arbitrarily many levels, are not a valid SAME-SOURCE R2 detector.** A151.1 shows why the apparent "signal" grows under completely artificial extra knowledge of the next bit.

## B151.2 2,520 explicit globally legal cap-two conserving falsifiers (INTERNALLY PROVED)

Let f:{0,1}^3→{0,1}^2 take each of the four output words exactly twice; there are 8!/(2!)^4=2520 distinct f. Define F_f(a z)=f(a) z where a is the first three input bits and z the infinite remaining tail. For EVERY infinite output y exactly TWO complete inputs exist, namely a z where f(a)=y|2 and z=y after its first two bits. Hence F_f is total computable, globally fair ON ALL cylinders and has exactly two actual complete inverses over EVERY y; no finite-row extrapolation is used.

**Each F_f preserves EVERY CR source.** Given output total rational nonnegative martingale d, for each 3-bit source prefix a set source M(a)=1, and on [a] put M(a v)=d(f(a)v)/d(f(a)) if d(f(a))>0, otherwise 1; also set M=1 above source depth three. The child average is correct; if d wins on F_f(x), its capital at prefix f(a) cannot be zero and M wins on x. Thus ordinary source CR implies output CR. This is even stronger than required R2 conservation of CR.

At output length n=2, the legitimate shorter read m=3 has rho_m≡1/2 within each output cone (next output is FIRST tail bit), so KL=0. The strictly increasing overread clock u(0)=0, u(n)=n+2 for n≥1 already reads that next bit for all n≥2. Each tau has half rho=0 and half rho=1, giving the universal maximum KL regardless of f. Take a positive computable rational output martingale with fixed child ratios r0=3/2, r1=1/2 at every node (p itself; use d=p if desired). Then mean A=1, Var(A)=1/4, product of the four A over compatible u(2)-cells is 9/16, and mean log A=(1/2)log(3/4)≈-0.143841 per cone. The maximum per-cone information penalty coexists with complete CR conservation in all 2520 globally fair exact-cap-two full maps. This extends the S150 identity-overread control to a noninjective F2 family.

## C151.1 Unbounded adaptive / countable bank safety budget (INTERNALLY PROVED)

**Theorem (stopped two-branch budget).** Fix any source cylinder [s] and any event E decided by a finite source-level partition inside [s], with conditional fair measure α∈[0,1]. Let M be ANY nonnegative source martingale with initial M(s)=c; let T be a possibly unbounded stopping time on its fair extensions, finite a.s., and assume terminal capital M(X|T)≥a for almost every path in E and ≥b for almost every path outside E. Then α a+(1−α)b≤c. The same holds for a countable sum of nonnegative self-financing banks with finite total initial capital (whenever interpreted pointwise; no computability is assumed for that sum). If E selects t of four equiprobable grandchildren, c=1 gives t a+(4−t)b≤4. This includes delayed sentinels, bounded or unbounded stopped excursions, and adaptive reserves **only under the stated BOTH-SIDES terminal guarantee**.

**Proof.** For every K, optional stopping at bounded T∧K gives E[M_T∧K |s]=c; by Fatou E[M_T|s]≤c. Terminal floors give E[M_T|s]≥α a+(1−α)b. For sums of banks apply Tonelli to their nonnegative terminal values and finite initial capitals. This does NOT exclude a strategy that wins only along one exceptional path, different bank per path, non-a.s. stopping, or a global F2 detector using source information. It closes exactly the proposed "adaptive banks guarantee both floor increases" loophole beyond S150's fixed finite horizon and FINITE bank summation.

## D151 Hostile E/S proof attempts and first unsatisfied obligations

**Attempt 1 — KL/variance compiler:** REJECTED. A151+B151 show the statistic is monotone in artificial lookahead and saturates even under CR-conserving exact-F2 maps. A universal test using JUST those population statistics and successively increasing clock cannot certify same-source failure. A conditional-data plus genuine witness-specific branch mechanism is required. This is NOT a no-go against arbitrary F2 compilers.

**Attempt 2 — adaptive hedge and delayed sentinel:** The stopped budget still forbids simultaneous >1 target/fallback guarantees, even with countable finite-capital banks and unbounded a.s.-finite stops. It does not prohibit choosing a winning branch by information acquired later. That algorithm remains the missing E-08 construction; 3:1↔2:2 S135 and S141 benign folds defeat static chart-selection. At q_A=1→2→t, t=1,2,3, α=t/4 and the exact bound survives unaltered; same when exchanging A/B at q_B=1. The 178 finite rows do not certify a global selector.

**Attempt 3 — finite prices and arbitrary use:** rho_m is finite rational and KL is exact; neither supplies the infinite stopped-event source price demanded by S145–S147 nor turns an output martingale into a single total rational same-source F2 observer. S011 supplies a genuine legal F2 bad-image CR source so blanket CR preservation is false. S129's normalized degree-three additive-c2 R2 success remains scoped to its own hypotheses. E-08 at c2 degree-two, E-00 at arbitrary use and S-00 ONE globally legal three-inverse G/d with ONE x∈R2 are still OPEN. The conull R2 class cannot be intersected with the null success pullback without an explicit witness or forcing.

**Independent-in-method finite sanity:** Enumerated all 2520 balanced tables, four output cones per table, exact Fraction ratios/mean/variance/product; 93,240 assertions pass over 10,080 finite cone cases. The full-map fairness, cap-two and CR-conservation claims follow from the symbolic tail extension and explicit source martingale above, NOT the code. No proof assistant, independent person, hosted CI, external novelty review or Gate4. Frozen S101–S103 A–C, Y/M/H/X, DEF-0020, PA-0001 and source grades unchanged.

**Disposition:** exact general clock-refinement/relative-entropy mathematics and adaptive all-branch hedge barrier INTERNALLY PROVED; uniformly maximal population penalty completely non-diagnostic for R2/R3. No E-08/E-00/S-00 theorem, strict witness or central hierarchy headline.