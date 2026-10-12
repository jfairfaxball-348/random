# P4-S109 — One-bit lookahead: a normal form, saturated-fibre conservation, and the remaining binary frontier

2026-10-12. ONE owner-invoked CAND-01 Phase4 mathematics session. Live entry main 750a62d77efd2728c4db0dac224d0fb6d90f71cd, tree 6b78057da20ba25f433001b384e069635722f464. Incoming expanded S109 archived byte-identically. Claims are PROVED INTERNALLY unless explicitly marked otherwise; no external novelty, independent referee, formalisation or Gate4 claim. General DP2/CP2/EQ/SEP remain UNRESOLVED.

## 1. Research map and exact conventions

This session developed four interconnected fronts beyond the first conservation observation:
* CONSTRUCTION: classify all fair one-bit-lookahead maps by their complete finite transition tables, derive a computable homeomorphism/chronological-scan normal form, and construct non-tail-trivial exact-two examples.
* CONSERVATION: derive an ordinary total positive RATIONAL source-martingale compiler for saturated fibres, including actual ramified double sources.
* HIERARCHY/EQ: characterize robustness for the whole one-lookahead class, locate S083's SAME-source separation inside it, and test the new central reduction.
* HOSTILE EXTENSION/SURGERY: attack unsaturated two-bit buffers, refute the seductive blanket compiler extension with an exact-two map, and identify the genuinely new hybrid transition obstruction.

For c>=0, say G has additive lookahead c if G(x)|m is determined uniformly computably by x|(m+c), for EVERY m and EVERY source x. This is a bound on the ORIGINAL source coordinates, not just a computable use function or S003's inverse precision c(n). A smaller-use computation may be padded to m+c. Define g_m:2^(m+c)->2^m by this computation. g_0 is empty output. All maps below are everywhere total and fair.

Finite-source-price lemma: fairness implies EVERY output m-word has EXACTLY W=2^c preimage words of length m+c, because each such source cylinder has mass 2^(-m-c). Consistency gives g_(m+1)(sigma b)|m=g_m(sigma). Compactness then bounds every infinite fibre by W: W+1 distinct infinite inverses would have distinct prefixes at some common length, contradicting the finite count. These exact finite counts alone DO NOT supply W actual inverses.

DP2 and CP2 refer to ALL F2, with actual double fibres and everywhere-exact-two respectively; neither has a lookahead restriction in its original statement. EQ is R2=MLR. SEP is ONE nonMLR source protected against EVERY F2 map. The new restricted theorems below are not relabelled as those general conclusions.

## 2. Saturated-fibre conservation with a uniform rational compiler

**Theorem 2.1 (PROVED INTERNALLY).** Let G be fair with additive lookahead c. If a CR source x has |G^-1(G(x))|=2^c, then G(x) is CR. No local injectivity, continuous partner, computable stabilization modulus, or conditional stopping mass is assumed.

Proof. Write W=2^c and y=G(x). Choose r separating the W actual preimages. For every m with m+c>=r, the W source (m+c)-words over y|m are exactly their prefixes, by saturation of the finite-source-price lemma. At the next output step each actual inverse extends its own prefix to one distinct child over y|(m+1). Thus each of the W parent words has EXACTLY ONE child giving the actual next output bit. Since a parent has two source children, its other child gives the other output bit. In particular the source transition at x|(m+c) is permutive in its new source bit, at ALL sufficiently late times.

Here is the promised ordinary martingale, with no hidden oracle for r. Normalize an output martingale d to d(empty)=1; a successful nonnegative martingale has positive root. Replace d by p=(d+1)/2, a total positive rational computable martingale with the same success set. Set D(sigma)=1 for |sigma|<=c. For |sigma|=n>=c compute tau=g_(n-c)(sigma), and the two next bits b_0,b_1 from g_(n-c+1)(sigma 0), g_(n-c+1)(sigma 1).
If b_0!=b_1 put
    D(sigma i)=D(sigma) p(tau b_i)/p(tau).
If b_0=b_1 put D(sigma 0)=D(sigma 1)=D(sigma).
These finite computations define a TOTAL POSITIVE RATIONAL computable martingale: in the first case the two ratios average to one, and in the second case both children equal the parent. Initial levels also satisfy the identity. No noncomputable limit or infinite mixture is computed.

On the actual saturated source, only finitely many freezes occur. After some N, ratios telescope:
    D(x|n)=D(x|N) p(y|(n-c))/p(y|(N-c)),  n>=N.
The positive prefactor cannot erase unbounded output capital. Thus output failure of CR gives source failure of CR, contradiction. QED.

**Corollary 2.2 (restricted DP2 and CP2, PROVED).** EVERY fair additive-one-lookahead map preserves CR at EVERY actual DOUBLE source. In particular EVERY everywhere-exactly-two fair additive-one-lookahead map preserves CR at ALL CR sources. This covers all S108 maps, including their large-measure ramified paired CR sources, and much more than their fixed-prefix tail formulas.

**Corollary 2.3 (necessary obstruction).** A genuine DP2 counterexample cannot have uniform original-coordinate output use m+1. A CP2 destroyer must leave that class. This is not a claim that every general F2 destroyer needs more lookahead: S083 already destroys a SINGLETON source within the class (Section 7).

For c=0, fairness makes every g_m a permutation of length-m words; consistency supplies a computable prefix-preserving fair homeomorphism. This is also the W=1 saturated case.

## 3. The complete two-prefix transition dichotomy

Specialize to c=1. Above any output word tau of length m there are exactly two input words sigma_0,sigma_1 of length m+1. Label them 0 and 1; labels may be propagated, not necessarily lexicographic. Their four source children split 2:2 among the next output bits.

There are exactly SIX possible Boolean assignments of these four children to the next output bit:
* BALANCED: each row sigma_j has one child for each output bit (four choices of the two row orientations).
* FOLD: both children of one row give 0 and both children of the other give 1 (two choices).

There is no hybrid case for two rows: if one row contributes two children to one output bit, fairness forces the other row to contribute zero. This elementary exhaustion is the leverage absent from general F2. The labels of an output child are updated as follows:
* At a balanced transition, its two source candidates retain their old row labels.
* At a fold, label its two source candidates by their newly appended source bit.

Starting with labels 0 and 1 on one-bit source words, the rule assigns exactly one candidate of each label at every output word, uniformly computably.

**Theorem 3.1 (fibre/fold classification, PROVED).** For EVERY fair one-lookahead map and EVERY infinite output y, its fibre has TWO points iff the transitions along y contain FINITELY MANY folds; its fibre has ONE point iff they contain INFINITELY MANY folds.

Proof, finite folds. After the final fold (or from the root if none), every transition is balanced. Each of the two current input candidates then has exactly one child over the selected next output bit forever. Their two coherent infinite paths are distinct and exhaust the fibre. Proof, infinite folds. A fold replaces both next candidates by children of ONE previous candidate. Given any fixed earlier source precision r, take a fold at a later stage; both surviving candidates then have the same r-prefix. Their later descendants keep it. The nested compact nonempty preimages therefore have exactly one infinite point. Alternatively two actual inverses separated at r forbid every later fold by Section 2. QED.

Important exceptional example: the IDENTITY map, when padded to m+1 use, folds at EVERY step; its fibre is singleton and it preserves CR. Thus infinite folds are neither a martingale win nor an effectively null locus. This hostile correction prevents a false nullness theorem.

Everywhere-exact-two is exactly the semantic requirement "every output path has only finitely many folds". It does not give a computable last-fold bound, a uniform fold count, or a continuous partner. S108's fat-boundary maps already refute those unjustified geometric inferences.

## 4. Computable normal form for ALL fair one-lookahead maps

A prefix-preserving fair homeomorphism (tree automorphism) A maps each length-n source word bijectively to a length-n word, consistently in n, and has a total computable inverse with the same prefix use. It preserves CR by the direct compiler d(A(sigma)); its inverse does likewise.

A CHRONOLOGICAL ONE-HOLE scan S has, at transcript length m, read exactly [0,m+1) except one held coordinate h<=m. Initially h=0. From its output transcript alone it either:
* FILL: output source coordinate m+1 and retain h; or
* RESOLVE: output coordinate h and replace the hold by m+1.
The choice is total computable. Queries never repeat, all outputs have at most one permanently unread coordinate, and prefix prices are fair by fresh-bit induction. This is a specific subclass of the programme's total one-hole scans; NO identification of it with the full OH scan family is asserted.

**Theorem 4.1 (normal form, PROVED).** Uniformly from a total fair one-lookahead G, construct prefix-preserving computable fair homeomorphisms K,H and a chronological one-hole scan S such that
                         G = H composed with S composed with K.
The scan resolves exactly at the FOLD transitions in Section 3. The equality holds at every source, including all exceptional infinite paths.

Full construction. Let ell_m(x|(m+1)) be its propagated candidate label above tau=G(x)|m. Initially ell_0=x_0. At a balanced transition, let
    K(x)_(m+1)=G(x)_m;
at a fold, let
    K(x)_(m+1)=x_(m+1).
In the balanced case the output bit is a permutation of the NEW input bit for each fixed input prefix; in the fold case it is the new input bit itself. Together with K(x)_0=x_0 this gives a triangular bijection of every finite source level, hence a total computable tree automorphism with computable triangular inverse.

At a fold above tau let a_tau be the output bit belonging to candidate label 0. The output bit is ell_m XOR a_tau. At a balanced step the label is retained, and at a fold the new label is the new input bit. Inductively ell_m is exactly the as-yet-unread held bit of K(x).

Define H and S simultaneously from a normalized transcript s. Given H(s)|m=tau, compute its transition type and, for a fold, a_tau. At a balanced transition, S fills coordinate m+1 and H prints the emitted bit unchanged. At a fold, S resolves h, sets h=m+1, and H prints the emitted bit XOR a_tau. This defines S's decision from its transcript alone. H's next bit is either the new transcript bit or its complement, with the choice determined by the already reconstructed tau. Thus H and its inverse are total computable tree automorphisms.

Induction on m proves the read-set invariant, ell_m=held K-bit, and H(S(K(x)))|m=G(x)|m. The source K-bit at m+1 is not queried when a fold resolves: it becomes the new hole, so the construction never peeks illegally. Prefix equality for all m proves the infinite equality. QED.

Converse: EVERY H S K with H,K such tree automorphisms and S a chronological one-hole scan is a total fair one-lookahead map. Use is m+1, fairness is preserved by composition, and Section 1 forces the all-output cap two. Thus this is an exact CLASSIFICATION, not just a selected example.

An independent conservation proof now exists: on a double fibre S has finitely many resolutions. After its last resolution its output shares a fixed tail with K(x), shifted by one position. CR passes through K, the fixed-tail relation and H. This cross-check uses finite-prefix martingale restriction rather than the ratio compiler.

## 5. Genuine constructions beyond S108's finite-prefix equivalence

**Example 5.1.** Put P(x)_0=x_0 and P(x)_i=x_i XOR x_(i-1) for i>=1 (the programme's Dprime). This is a tree automorphism: its inverse is the running parity. For ANY S108 decidable tree T, set Q_T=G_T composed with P.
* Finite use is m+1.
* Every output has exactly two inverse points, P^-1 applied to the two explicit S108 inverses.
* Every output m-cylinder has exactly two source (m+1)-cylinders, since P permutes that level.
* Q_T is exactly fair.
* Ram(Q_T)=P^-1(Ram(G_T)); hence for the fat trees its measure is at least 47/48 and can approach one. Local injectivity is invariant under the source homeomorphism.
* All actual CR sources, including ramified paired sources, are preserved by Corollary 2.2.

On a fat-tree output y and source x=P^-1(a y), the output is y while x is its running-parity coding with initial state a. The change is infinite, not a finite-prefix replacement in the original source. More precisely at CR sources equality of x_(j+1) and y_j=P(x)_(j+1) holds exactly when x_j=0; a CR source has infinitely many x_j=1, so the naturally aligned tails disagree infinitely. This example illustrates the larger theorem; it is not claimed to refute every imaginable computable tail recoding.

The general six-transition recipe in Section 3 realizes ANY total computable choice of balanced orientations or fold orientations at each output word. Computing output uses the current input prefix and the finite table only. Fairness follows inductively from its 2:2 splitting; every output fibre is at most two. If every output has finitely many marked fold transitions the map is everywhere exact-two. Arbitrarily many source-dependent nonlinear balanced orientations may occur, so the class need not be tail-trivial even after all folds have stopped.

Construction attempt toward destruction: infinite delayed folds in this recipe can reproduce chronological one-hole reading after K. But an actual distinct partner forces the folds to stop. No choice of the six legal tables can turn a CR double source into a nonCR output. This is a class-wide impossibility theorem, not merely failure of one tree-switch variant.

## 6. Saturated finite-loss algebra

Let Sat_c be all fair additive-c-lookahead maps with exactly 2^c inverse points over EVERY output. Theorem 2.1 proves Sat_c(CR) subset CR.

**Proposition 6.1.** Sat_a composed with Sat_b is contained in Sat_(a+b). Source use adds; inverse cardinalities multiply EXACTLY because every output of the outer map has exactly 2^a preimages and each of these has exactly 2^b preimages under the inner map. Their disjoint union has 2^(a+b) points; composition is fair. Therefore every finite tower of these saturated quotients preserves CR.

This is a derived algebra of the NEW restricted conserving classes. It does NOT prove F2(R2) subset R2; it is not the old tautological F_j(R_jk) subset R_k. In particular a tower of exact-two one-lookahead maps has degree 2^t and lookahead t. Its preservation follows for ALL CR inputs from saturation, but it generally leaves F2 after the first step. Trying to use it as a partnered F2 destroyer violates the cardinality requirement.

## 7. A new exact restricted robustness characterization and a sharp threshold

Let L1 be ALL fair total additive-one-lookahead maps. By Section 1 these are automatically in F2. Let C be the set of sources whose image is CR under EVERY chronological one-hole scan, and define
    R_L1 = {x: for every G in L1, G(x) is CR}.
Identity is in both classes, so these robustness notions already imply source CR.

**Theorem 7.1 (PROVED).**
    R_L1 = intersection over computable tree automorphisms K of K^-1(C).
Proof. For every S,K the map S composed with K is in L1, giving the forward inclusion. Conversely factor any G in L1 as H S K by Theorem 4.1. If all K(x) are in C then S(K(x)) is CR, and H preserves CR. QED.

This gives an exact forward-coordinate structural characterization without universal finite-fibre selector or conditional-disintegration hypotheses. It is a programme auxiliary notion, not a proposed name or a change to CAND-01.

**Theorem 7.2 (PROVED using frozen S101-S103 package C).**
    R2 subset R_L1 STRICTLY SUBSET C subset CR.
Moreover OH subset C, but OH is NOT contained in R_L1.
Use the SAME S083 source z, not a fresh existential witness. The established package has z in OH^blk subset OH, hence in C, and CR; its destroyer is G=F_Tstar composed with P. The S083 scan state is exactly [0,M) except q, with q=0,M=1 initially. Each output increases M by one. It either queries M (fill) or q and sets q=M (resolve). Thus after m outputs M=m+1; F_Tstar has original-coordinate use m+1. P has prefix use m, so G is in L1. The frozen successful rational dstar defeats G(z); hence z is not in R_L1. Its fibre is SINGLETON by infinite resolutions. All maps, exact prices, source CR and martingale certificates are the established package, with this new explicit use calculation. R2 subset R_L1 follows from L1 subset F2. No strictness of that first inclusion is established.

The class R_L1 is invariant under every computable tree automorphism: composing a one-lookahead map with K or K^-1 stays one-lookahead. C is not invariant under them: z is in C but P(z) is not, witnessed by the chronological S083 scan. This sharpens the scope of the source-coordinate obstruction; it does not supply an R2 survivor.

**Minimal-use threshold.** Additive-zero fair maps all preserve CR. Additive-one fair maps already fail forward CR preservation on actual singleton fibres (S083), but ALWAYS preserve it on actual double fibres (Corollary 2.2). Any partnered destroyer therefore needs more original-coordinate use than one; whether two suffice is unresolved.

## 8. Serious EQ/SEP attack through the normal form — exact finishing gap

A concrete sufficient equality theorem would now be:
    for EVERY z in CR minus MLR there exist a computable tree automorphism K,
    a total chronological one-hole scan S, and a total rational computable d
    succeeding on S(K(z)).
This is exactly R_L1=MLR and would imply R2=MLR, since MLR subset R2 subset R_L1. It is stronger than the original equality target: arbitrary F2 might defeat a point that all L1 maps preserve. No converse reduction is claimed.

Attempt E1: use a universal ML test to mark folds and orient the current candidate label. At a fold its two candidate rows represent two full transformed source completions. A test covers the nonMLR actual row, but also covers its computable partner completion. Mere separate coverage or later entry does not decide which label to wager on. Enumerating the test is not an ordinary successful betting strategy. The normal form exposes this as repeated label-resolution betting rather than removes it. The S092-S105 coverage/race/partial-domain obstacles remain real.

Attempt E2: preserve both labels until one becomes distinguishable. If all outputs are required to remain double, Section 3 forces only finitely many folds along the actual output and the compiler proves conservation; thus EXACT-two L1 maps cannot be an EQ mechanism. Allowing singleton outputs reopens unbounded label replacements but again needs a success criterion for EVERY nonMLR source, not just the S083 specially built source. No such criterion was proved.

Attempt S1: diagonalize against the normalized S K family rather than all F2. The normal form provides effective code-level objects under PROMISED validity; it does not computably decide everywhere totality or all-map validity, nor construct a nonMLR protected point. Even a z in R_L1 minus MLR would leave the OTHER F2 maps unprotected. S105's effective protection bank and non-effective survivor construction do not fill either gap. Both EQ and SEP remain UNRESOLVED.

## 9. Hostile extension: exact-two with two-bit use breaks the easy compiler

The tempting stronger lemma "an actual double fibre forces eventual permutive single-input-bit transitions under every FIXED finite lookahead" is FALSE.

**Countermodel 9.1 (PROVED).** Let pi delete the initial source bit a; let V swap adjacent bits of the resulting tail u:
    Q(a u)_2j=u_(2j+1),  Q(a u)_(2j+1)=u_(2j).
Q is total computable fair and EXACTLY TWO over every output, with global injective clopen sheets [0],[1]. It has additive use two. At a source prefix of length n, the next output bit at index n-2 is independent of the newly appended source bit whenever n-2 is odd. Thus infinitely many transitions freeze in the Section 2 compiler run with c=2, on EVERY source, despite genuine partners.

Take the ordinary output martingale d that bets all-in on 0 at odd output positions and bets nothing at even positions; use positive p=(d+1)/2 in the compiler. On output 0^omega, d diverges, while the compiler D stays exactly ONE: every profitable step is frozen and every executed step has ratio one. The corresponding source is nonCR. This is a counterexample to the claimed compiler extension, NOT to DP2 or CP2. Q itself preserves CR, because fixed adjacent permutation and initial deletion have ordinary computable CR transfers; one can instead group two output bits and transfer the four equally priced source possibilities.

This repair works for the specified fixed permutation. It does NOT justify grouping at a computably chosen block length for arbitrary two-lookahead F2 maps: ghost candidates can persist for unbounded output delays, and no uniform source-local injective block was established.

## 10. Four-state constructive offensive and the new unsaturated obstruction

For lookahead two, each output prefix has FOUR source candidates, but an exact-two output may have only TWO actual infinite inverses. Two are transient; the saturation argument cannot spend them.

At a transition there are eight source children, four assigned to each output bit. There are choose(8,4)=70 Boolean tables:
* 16: all four rows permutive (one child to each bit).
* 6: two rows constant 0, two constant 1.
* 48: TWO permutive rows, one constant-0 row and one constant-1 row.

The 48 hybrid tables are impossible with two rows, and the exact first failure of the one-bit normal form. For example, with state (s,t) and new bit b, output b if s=0, and output t if s=1. It is exactly balanced, but whether the output reveals a new bit or old stored information depends on a HIDDEN source state, not only the known output transcript. An output-driven single-hole scan cannot simply choose fill versus resolve from tau for this table.

Actual construction route tested: assign a computable bijection from the eight (old state,new bit) pairs to (output bit,new state) pairs. Any one of the 70 balanced output assignments can be completed this way. Start with the first two source bits as the four-state reservoir. Iteration is an everywhere-total fair lookahead-two map with four equally priced finite candidates and all infinite fibres <=4. This establishes a legal design framework, but NOT an F2 or exact-two counterexample: exact finite prices do not prevent three or four persistent inverses, and prescribing a selected two-path diagram is not an all-output proof.

Attempted repair: keep a permanent partner track while using the other two prefix slots to carry a moving fold on the actual branch. At each proposed repeated fold, certify elimination of all unintended infinite tracks, preserve four cell prices, and keep both intended tracks alive for EVERY output. Neither the row table nor a local elimination schedule proves those infinite obligations. If separate partner duplication is used, regular double fibres instead become four by S107's composition obstruction. The fixed-permutation Countermodel 9.1 demonstrates legitimate transient cells without destruction; it does not supply self-reading bets. No actual paired CR source with nonCR output was obtained.

This is a materially sharper next construction frontier: four-state HYBRID conditional information release with only two persistent inverses. It is not a claim of a new mathematical impossibility for all such reservoirs.

## 11. Cross-front synthesis and claim status

What changed beyond S108:
1. A uniform ordinary rational compiler proves conservation for ALL saturated finite-lookahead fibres; minimal-lookahead DP2/CP2 are CLOSED as RESTRICTED theorems, even at positive-measure ramification.
2. ALL fair one-lookahead maps have an explicit H S K normal form. Genuine double versus singleton fibres correspond exactly to finite versus infinite fold histories.
3. The whole one-lookahead robustness class has an exact triangular chronological-scan characterization, is tree-automorphism invariant, and is strictly smaller than raw chronological-scan robustness using the established SAME S083 source.
4. Minimal one-bit lookahead supports CR destruction only on singleton fibres; larger paired destruction needs new structure.
5. The two-bit extension of the naive compiler is explicitly REFUTED inside globally exact-two maps; hybrid four-state transitions isolate the new unsaturated problem.

PROVED INTERNALLY: Sections 1-7, Countermodel 9.1, 70-table counting and legal <=4 reservoir framework.
REFUTED: finite lookahead plus an actual partner implies eventual single-bit permutivity; the corresponding blanket gated compiler; infinite fold locus must be null/nonCR; all finite two-cell prices require continuous partner (historically refuted, retained).
UNRESOLVED: GENERAL DP2, CP2, EQ, SEP; R2 versus R_L1; R_L1 versus MLR; C versus full OH; four-state exact-two destruction/conservation; factorization of arbitrary F2 into this normal form; F2(R2) subset R2.

No claim requires new source retrieval: new proofs use finite combinatorics, compactness and explicit rational martingales. The restricted strictness theorem additionally uses the frozen S101-S103 A-C/S083 package. Original Y/M/H/X, DEF-0020, PA-0001 and primary-source access levels are unchanged. Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED. No S110 mathematics, Lean, Palomar, novelty campaign, manuscripts, correspondence or publication.

