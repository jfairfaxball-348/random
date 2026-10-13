# P4-S117 — Posterior volatility, balanced paired reservoirs and priced injective certificates

2026-10-13. Exactly one owner-invoked Phase4 CAND-01 mathematics session. Entry main `1e0203f74334996474ad3aa007c0acb4b13f1415`, sole parent `e397fe406e4cc61f0276cd257314694743f27011`, tree `634c0d412a49bed1051f7745d2688f2428d0bf84`. S116 PR #14 is merged at that same atomic commit. S117 unused at entry; Phase4 OPEN. INTERNAL mathematical development and same-agent hostile validation, no external/formal/novelty certification.

The central targets remain unresolved. The main additional result is a useful dichotomy for a **two-CR-preimage** additive-two destroyer, together with an explicit posterior-volatility output martingale. This is weaker in source quantifiers than general DP2 (which assumes only one CR preimage). It does not assert conservation for all additive-two maps.

## 1. Definitions and hostile reconstruction

X=2^omega with fair product measure lambda. Ordinary martingales are total computable nonnegative rational functions d with d(tau0)+d(tau1)=2d(tau); success is unbounded limsup. F2 means total computable fair maps with at most two ACTUAL infinite preimages of EVERY output. R_k means survival of every globally fair total computable map of fibre cap k. Fixed additive use c means the first m output bits are determined by the first m+c input bits, uniformly over inputs. Padding smaller uses is legal. Fairness implies onto.

For S116 affine splitting, independently choose source-coordinate evaluations A whose restriction to the finite binary kernel K is bijective. If H(x)=(A(x),L(x)), injectivity follows by subtracting two solutions in K; onto follows by translating any L-preimage by the unique kernel element correcting A. Effective compact separation gives the inverse; translation by kernel elements fixes L and permutes tags transitively, giving each tag-output cylinder mass 2^(-dim K-m). The coordinate choice is finite and nonuniform in a program for L. It is not a proof for a source-dependent piecewise affine map. For q swapping 4^j and 2*4^j, all inverse coordinates are recovered from x_0 and cumulative XOR along q; precisely two streams exist at every output, with unbounded excess use. No finite price table is substituted for this recursion.

S115's safe-core residual is effectively closed null only under its supplied full-measure promise. Increasing inner and decreasing outer clopen bounds compute the mass by a terminating rational squeeze; the promise cannot be inferred from the search itself. S114's pair construction remembers early discrepancy even after controls coalesce and uses coherent infinite paired paths, not independent finite collisions. Finite undecided states each have a path to DEAD, yielding transient absorption and a rational linear system. S113's post-exit-bit cancellation pairs the two unread independent child bits; the special density N/2 cannot be exported to arbitrary nonlinear postmaps. Its R_k deletion proof retains the deleted finite tag in the test output. For all first-exit trees, boundary inverses are 0y,1y and exited inverses are c rho 0t,c rho 1t. Dead nodes and never-exit limit paths are included. No fatal gap was found in these restricted prior results.

S101–S103 A–C and source grades are retained: E-ISO's checked primary-proof dependency, SRC-0067 ABSTRACT_INSPECTED and SRC-0068 PROOF_INSPECTED are not upgraded by this session. Original Y/M/H/X, DEF-0020 and PA-0001 remain frozen.

## 2. Front B, first attack: turn the finite price floor into a volatility martingale

Fix ANY fair additive-c G, not necessarily F2, and a finite clopen source set B. Take m0 with m0+c at least the source precision defining B. For |tau|=m>=m0 put

    q(tau)=2^m lambda(B intersect G^-1[tau]).

**Theorem B117-1 (finite-grid posterior martingale and explicit volatility winner).** q is a total rational computable output martingale, 0<=q<=1, and q(tau) is a multiple of 2^-c for m>=m0. There is a total rational nonnegative output martingale M_B which succeeds at every y for which q(y|m) changes infinitely often. Consequently at every CR output y this posterior is eventually EXACTLY constant, not merely convergent. No effective final-constancy time is asserted.

Proof. Fairness and the additive use imply precisely 2^c source (m+c)-cells over tau. Each B-cell contributes 2^-c to q. The two child cylinder measures sum to the parent cylinder measure; therefore q(tau0)+q(tau1)=2q(tau). Compute q also at shorter levels directly using a uniform use bound for G and the finite clopen B; granularity at those short levels is unnecessary.

For EVERY finite tau define delta(tau)=(q(tau0)-q(tau1))/2 and v(tau)=q(tau)(1-q(tau)). Direct expansion gives

    (v(tau0)+v(tau1))/2 = v(tau)-delta(tau)^2.

Set

    M_B(tau)=v(tau)+sum_{rho proper prefix tau} delta(rho)^2.

Each summand is a computable rational, the sum is finite, and M_B>=0. At the two children the accumulated sum gains the SAME delta(tau)^2, so the displayed identity proves the ordinary martingale equation. If the posterior changes at a sufficiently long step, the actual change equals +delta or -delta and its magnitude is at least 2^-c. Thus N long active steps contribute at least N*4^-c, while v remains between 0 and 1/4. Infinitely many changes give an explicit rational winner on the output. If M_B has root zero, nonnegativity and the martingale equation force it identically zero, so the infinite-change case cannot occur; normalizing a positive root is optional. QED.

This is an OUTPUT winner, not a SOURCE compiler. Inferring that its fair pullback is an ordinary source martingale is the first unsupported step in the attempted universal transfer. Pullbacks of its finite horizons can be priced exactly, but those are distinct source martingales and do not automatically form one coherent account.

## 3. Front B, second attack: isolate the balanced two-sheet bottleneck

Let p=d+1 for an arbitrary output winner d. Define a single total rational source martingale D, valid for any fair additive-c G. Give every source prefix of length at most c capital 1. At source word s of length n=m+c, G(s) has a well-defined length-m output tau. Compute the next output bits b0,b1 on s0,s1. If b0 != b1, multiply D(sb) by p(tau b_b)/p(tau); if b0=b1, keep D(sb)=D(s). At a permutive row the two factors average 1; at a constant row both factors are 1. All denominators are positive. Therefore this is a total ordinary rational nonnegative source martingale. This rederives S109's gated compiler without falsely claiming its general success.

**Lemma B117-2 (eventual one-cell sheet).** Suppose x is an actual inverse of y, x lies in a finite clopen B, and for all sufficiently long tau=y|m there is precisely ONE source (m+c)-cell above tau inside B. Then if any total rational d succeeds on y, the preceding D succeeds on x. In particular x cannot be CR when y is nonCR.

Proof. At sufficiently long n, membership of B is already decided by s=x|n. If its next-output row were constant with bit y_m, BOTH s0 and s1 would be B-candidates above y|(m+1), contradicting the one-cell hypothesis. Thus every eventual actual row is permutive. All D-values on this actual path are positive, because p>0 and earlier frozen factors are 1. From the first such depth onward the factors telescope to a positive fixed multiple of p(y|m). No computable first such depth is required to define D. QED.

**Theorem B117-3 (two-CR-preimage balanced-or-volatile obstruction at c=2).** Let G be fair additive-two and have precisely two actual preimages x0,x1 above y. Suppose BOTH x0 and x1 are CR and y is nonCR. For EVERY finite clopen B containing exactly one of x0,x1, its posterior q(y|m) must either change infinitely often or be eventually equal to 1/2.

Proof. Eventually both B and its complement contain their respective actual (m+2)-cell. Hence q is in {1/4,1/2,3/4} along all sufficiently long actual output prefixes. If q changes only finitely often, its final value is one of these three values. Final value 1/4 gives an eventual unique B-cell; B117-2 defeats the CR source in B. Final value 3/4 gives an eventual unique complement-cell; the same compiler defeats the CR source outside B. The only remaining final value is 1/2. QED.

Scope: this DOES NOT close DP2. A DP2 counterexample could have only ONE CR source and a nonCR partner. Even for two CR sources the balanced case permits two finite candidates per separated side but only one actual infinite path on each side; neither side is saturated. The volatile case supplies M_B as a ready-made TOTAL rational output winner if a globally legal two-CR-preimage example can be built. No such example has been produced.

For general c the same reasoning rules out a final posterior of 2^-c or 1-2^-c for such a two-CR-preimage bad output. At c=1 these are the only possible nontrivial values, independently recovering the two-CR version of the additive-one obstruction. The stronger S109 DP2 theorem for one CR source remains a separate retained theorem.

### Attempted repair through stabilized balanced populations

At q=1/2 with c=2, a separating B has two candidates forever on the actual tail. Because q is an output martingale, if the actual child retains value 1/2 then its SIBLING also has value 1/2. Thus every eventual actual node has 2:2 offspring balance inside B. An initial draft incorrectly allowed 1:3 splitting at such a node after final stabilization; the hostile algebra check corrected that inference before commit. Off-path descendants can still leave balance, and there is precisely ONE actual B inverse, so the saturated actual-double theorem does not apply.

**Theorem B117-4 (balanced chart reduction to a legal singleton L1 destroyer).** In the eventually balanced case of B117-3, each of the two CR preimages admits a finite conditional source normalization and a total fair additive-one map with singleton fibre over the normalized bad output. Its ordinary rational winning martingale is a restriction of any winner on the original output. This is a reduction to two synchronized singleton obstructions, not a contradiction or a construction of the paired map.

Proof. Choose an output prefix tau0 after stabilization and after B-membership is determined. Exactly two source words sigma0,sigma1 of length n0=|tau0|+2 lie in B above tau0. Normalize source z=i u to original sigma_i u, i in {0,1}. Conditional on this two-cylinder region the label i and tail are fair. For the actual x=sigma_i u, CR of x implies CR of u by fixed-prefix martingale restriction, and hence CR of i u by the same restriction in reverse.

Starting with candidate source labels 0,1, simulate the next-output rows of G on the two normalized candidate prefixes. At a node where its four source children split 2:2 between the next output bits, use those exact rows and update the two candidates above each output child. If a node fails this 2:2 test, permanently replace the output rule by fresh chronological tail-bit emission, retaining the current two candidates as a hidden label. The test is finite and depends only on the simulated output node and its two source candidate words. All decisions are total computable. The replacement is balanced. Inductively each j-bit output has precisely two (j+1)-bit source candidates, so the resulting map is fair and additive-one, hence globally cap two by the finite-prefix compactness argument of S109. The source new-bit order remains chronological in both modes.

Along the selected output y after tau0, all original B row splits are balanced at every subsequent node, including the sibling child counts, so no replacement occurs. EVERY inverse producing that same output follows this same output-controlled no-replacement sequence. Inverses are therefore exactly the normalized original B inverses above y, of which there is ONE. The actual normalized CR source is among them. If d wins on y, the total rational martingale e(eta)=d(tau0 eta) wins on its tail. Thus each side gives a genuine singleton L1 destruction certificate. QED.

This explains rather than resolves the obstruction: S083 already shows legal L1 singleton destruction on CR sources. The hard paired problem is to glue TWO such conditional charts into one globally fair additive-two F2 map while controlling every unbalanced off-path continuation. Simply summing two individually onto L1 maps creates up to four points, and A117-1 excludes bijective block repairs. The reduction does not normalize all CR nonMLR sources or certify any R_L1\R2 witness.

## 4. Front A: nonlinear variable-memory keyed exchanges, with a complete conserving certificate

We investigated arbitrary nonlinear block permutations, with block lengths depending on the hidden key and previously emitted output. This substantially enlarges a fixed two-bit compiler but still does not make a destroyer.

For each a in {0,1}, supply total computable functions ell_a(tau)>=1 and pi_(a,tau), a permutation of binary words of length ell_a(tau). On source tail u, at a completed output prefix tau read the next ell_a(tau) unread source bits w and append pi_(a,tau)(w). Repeat indefinitely. Call the result P_a(u). Lengths may be unbounded and nonlinear tables may vary at every output node; no finite-state or additive-use bound is imposed. Finite table bijectivity and positivity of ell are genuine promises.

**Theorem A117-1 (all infinite fibres, exact prices and adaptive-block compiler).** F(a u)=P_a(u) is total computable, fair and EVERYWHERE EXACTLY TWO. It preserves all R_k. It also has an explicit ordinary rational CR compiler that handles unbounded block lengths, including output wins occurring only inside blocks.

Proof of infinite legality. Given a,y, the boundary lengths are computed successively from the decoded output prefix. At each boundary invert pi_(a,tau) on the next output block. This gives one and only one infinite u because every block has positive length and the total decoded length tends to infinity. Hence above EVERY y the full inverse set is {0P_0^-1(y),1P_1^-1(y)}. There is no extra compact limit branch. Forward computation and inverse computation of any finite prefix require only finitely many total table calls. Conditioned on any completed history, a block is uniform and its permutation is uniform; a prefix of the permuted block of length h has probability 2^-h. Induction handles cylinders ending INSIDE blocks as well as boundary cylinders. Thus each P_a is a fair computable homeomorphism and F is fair with two actual points at all outputs. The map H(a u)=a P_a(u) is a computable fair homeomorphism with the stated inverse. F deletes its initial output tag; S113 therefore gives all R_k preservation.

Explicit source compiler. First use S101's total rational savings wrapper to replace d by p with nonnegative capital and drawdown less than 2: later p-values exceed earlier p-values minus 2, and original unboundedness implies p unbounded. Fix the actual key a as a finite parameter. At a source block boundary v whose completed output is tau, put E_a(v)=p(tau). At an intermediate source prefix v w, |w|=h<ell=ell_a(tau), put

    E_a(vw)=2^(-(ell-h)) sum_{z in 2^(ell-h)}
                         p(tau pi_(a,tau)(wz)).

This is a finite rational computation at EVERY input prefix. Intermediate averaging gives the binary martingale equation. At a boundary, the average of all block endpoints is p(tau), because pi is a permutation and p is an ordinary martingale. Initial tail capital is p(empty); extend to the full source with both key-child values p(empty), the chosen-key branch following E_a and the other branch constant. If p has arbitrarily large values inside output blocks, the next block endpoint has value greater than each such peak minus 2. There are infinitely many completed boundaries and each finite block has finitely many prefixes. Therefore boundary values are unbounded, so E_a wins. Using d instead of savings here would be WRONG for unbounded blocks: capital could peak high and return to a bounded value before every sampled endpoint. QED.

Nonlinearity is real: on any three-bit block (b0,b1,b2), use (b0,b1,b2 xor b0*b1), the binary Toffoli permutation. Its third coordinate has a nonzero quadratic mixed difference, so it is not affine. For instance ell_a(tau)=3*(|tau|+1) allows unbounded memory/use with products applied within each triple. Every table and inverse remains computable. This is an explicit nonlinear nonhomeomorphic F2 map, but it has clopen key sheets and cannot produce a bad CR image. Two CR sources above a CR y follow from inverse homeomorphic preservation and fixed-prefix CR equivalence; above a nonCR y the compiler rules out a CR source on either key.

Ramified extension tested: precompose any S108 G_T by a nonlinear fair homeomorphism, or apply a fixed-key P_a after G_T. Pointwise all R_k preservation still follows from S113 and homeomorphic invariance, independently of lambda(D_r). If the chosen P_a do not satisfy S112's relative compatibility, exact-two/fairness of the keyed postcomposition must be checked separately; A117-1 DOES NOT supply that check for arbitrary T. A common postmap P after G_T is legal and exact-two, including fat ramified CR sources, but is in the already-conserving orbit family. A key duplicated singleton destroyer gives four points on regular double outputs. None of these constructions meets the requested two-CR-preimage bad-image certificate.

## 5. Front C: priced injective submeasures, a sufficient theorem beyond a bare orbit argument

The proposed measure-free universal transfer was not proved. A positive price floor does not yield a computable submeasure. The following explicit certificate instead avoids requiring the canonical stratum's lambda-mass to be computable.

**Theorem C117-1 (priced injective certificate).** Let G be total computable fair. Suppose B is an effectively closed source set on which G is injective, and beta is a nonzero finite COMPUTABLE Borel measure with beta<=lambda, beta(X\B)=0. For a source x in B suppose there is a fixed epsilon>0 with

    beta([x|n]) >= epsilon * lambda([x|n]) for every n.

Then lambda-CR of x implies lambda-CR of G(x). The floor may equivalently hold for all sufficiently large n; the finitely many earlier positive cylinder ratios have a positive minimum. No computability of lambda(B), lambda(D_r), a partner selector outside B, or epsilon is assumed. Computability of beta's cylinder masses IS mandatory.

Proof. We use the computable-measure likelihood-ratio characterization and effective-isomorphism theorem E-ISO in the precise scope already declared in S101/S102 and S112. Normalize beta by its positive computable total if a probability measure is required. For any computable finite test measure mu, along x,

    mu([x|n])/lambda([x|n])
      = (mu([x|n])/beta([x|n]))
        * (beta([x|n])/lambda([x|n])).

All beta cylinders at x are positive by the floor. If the first quotient is unbounded, the left-hand quotient is unbounded. The left-hand function is a computable real ordinary lambda-martingale; S101's positive-factor rationalization turns it into a total rational winner. Thus lambda-CR implies beta-CR at x. This step is pointwise and does not silently infer a density lower bound from beta<=lambda (which gives only an upper bound).

Put nu=G_*beta. Its cylinders are computable: G^-1[tau] is an effectively finite clopen union, so beta computes their sum. Also nu<=lambda by beta<=lambda and fair G. The restriction G:B->G(B) has a partial computable inverse on its effective compact range. To obtain n source bits, effectively separate images of the finitely many disjoint compact pieces B intersect [s], |s|=n, by finite output prefixes; injectivity and compactness guarantee termination. This inverse is defined on G(B), has inverse identities there, and pushes nu back to beta. These are full-beta/full-nu supports. E-ISO sends beta-CR x to nu-CR y=G(x); no total inverse outside the support is asserted.

If a total rational lambda-output martingale d succeeds at y, let mu_d([tau])=2^-|tau| d(tau), a computable finite Borel measure. Every cylinder at a nu-CR y has positive nu mass (otherwise it belongs to an effectively null cylinder for nu). Along y,

    mu_d([y|m])/nu([y|m]) >= d(y|m),

because nu<=lambda. This is an unbounded computable-measure likelihood-ratio test and contradicts nu-CR. Hence no lambda d wins. The uses of measure-relative CR here are through E-ISO and its recorded ratio convention, not a claim that an arbitrary rational output function pulls back literally as a rational source martingale. QED.

Comparison: S112 takes beta=lambda restricted to a computable-mass closed sheet. C117-1 accepts any supplied computable dominated measure with pointwise lower density, which may be supported on a proper subset of B. It does not compute lambda(B). Example of compatibility with the awkward noncomputable-mass stratum: in S112's halting tree K, [0] subset K because every forbidden p_e begins with 1. For source B=0K under G_T, take beta=lambda restricted to [00]. This is computable, supported on B, dominated by lambda, and has cylinder density 1 eventually at every source in [00]. Yet lambda(B)=lambda(K)/2 is noncomputable. This is a demonstration of the hypothesis distinction, not a new conservation result for that example (the tree switch already conserves all R_k pointwise).

For S108 fat nowhere-dense ramification, source B_i are closed sheets over a computable-mass K_L, and beta=lambda|B_i recovers the old S112 certificate; positive-measure boundary is harmless under those proven prices. For an arbitrary noncomputable K there is NO supplied beta with a density floor at every CR source in its sheets. Both noncomputable D1 and fat ramification are therefore accounted for without an invalid universal nullness or computable-mass claim.

Failed universalization: choosing beta=lambda|B for arbitrary Pi01 B yields only upper semicomputable cylinder values and may have noncomputable total. Choosing beta as a limit of granular q(tau) likewise requires effectivity and consistency not supplied by B117-1. Pointwise lower sheet weights are not names for a computable dominated measure. These are the first unsupported steps, not counterexamples to C117-1.

## 6. Front D: sustained central and hierarchy attacks, with exact failures

EQ attempt: feed the universal ML test into the variable-length block tables and choose increasingly long nonlinear permutations to encode test discoveries. A117-1 proves every total bijective block version, however adaptive its legal tables, conserves ALL CR; it cannot cover even one CR nonMLR source. Allowing the tables to be nonbijective breaks the conditional fair permutation proof. To escape, one must prove all-output fibre cap and fair cylinder prices separately and make two transient reservoir candidates do useful betting work. B117-3 gives an actual balanced-or-volatile target for TWO CR inverse sources, but does not orient or destroy EVERY CR nonMLR source. ML-test enumeration supplies neither orientation nor a general source-price compiler.

SEP attempt: protect a nonMLR source against the countable volatility martingales M_B, variable-block maps, and all priced injective certificates. Such protection is only against these families. Even listing beta certificates does not capture every legal F2 observer, and requiring eventual posterior stabilization does not put a source in R2. The all-map bank of S105 still needs an effective ordinary ML-null coding of a common protected point. Selecting a point outside integrable capital exceedances alone can select MLR. Thus neither ONE all-F2 nonMLR source nor EQ is obtained.

SAME-source R2 versus R_L1: the additive-two balanced reservoir frontier suggests maps outside L1, but a conserving nonlinear block quotient does not separate robustness. S083's known z lies outside R_L1, so cannot witness R_L1\R2. A valid separation needs ONE z in R_L1 and a legal F2 map with a total rational winner, and its full R_L1 survival certificate. None is constructed.

Unrestricted iteration: A117-1's explicit tag-retaining homeomorphism plus deletion preserves every R_k, hence in particular its F2(R2) outputs are R2; common-homeomorphism tree-switch compositions also preserve R2. This does not prove closure for EVERY F2. For arbitrary G,H in F2 the composed fibre can have four points. C117-1 supplies ordinary CR preservation at certified sources, not all-observer R2 survival; applying it twice does not turn an R2 source into an R4 source. No legal cap-two iteration failure or unrestricted inclusion is established.

## 7. Disposition

INTERNALLY PROVED: finite-grid posterior volatility martingale; eventual exact constancy at CR outputs; explicit eventual-one-cell source compiler; two-CR additive-two balanced-or-volatile necessity and balanced-chart reduction to singleton L1 destruction; complete nonlinear variable-memory keyed block family with all infinite inverse and cylinder proofs; savings-based rational compiler for unbounded blocks; all-R_k preservation for that family; conditional priced injective-submeasure conservation with its noncomputable-mass compatibility example.

NOT PROVED: a fair cap-two bad output with two actual CR preimages; general additive-two CR compiler or its counterexample; general measure-free conservation; DP2/CP2; EQ/SEP; R2 versus R_L1; unrestricted F2(R2) subset R2. No falsely reported theorem refutation from a finite table. Finite sanity supports algebra and finite prefix pricing only. Gates: Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. Future S118 is prepared separately and NOT executed.
