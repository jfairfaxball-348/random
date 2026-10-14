# P4-S138 — Effective inverse-decoding firewall and precise factorisation boundary

**14 October 2026. INTERNAL MATHEMATICS ONLY.** Owner explicitly authorized an extended multi-front P4-S138 beyond any one-object stopping rule. Entry LIVE main `df7628aea370f795a4fb45c78e22e4fbbdd1e6f0` (S137 authored commit, sole parent 3e4e46a1cf1b0d3d40d40125a70f33fc64beb47f; tree `7a77d23bbaf876f5f3132d6e6dd685aa9b2b0add`; merged PR #36; 18 paths). Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. No S139 work. This dossier uses the original S136 all-output four-cell G rows and S137's uniform synchronizers; frozen A–C/S101–S103, Y/M/H/X, DEF-0020 and PA-0001 unchanged.

## A. THE remaining S137 singleton leakage obligation — SOLVED for G

Let X=2^ω with λ fair coin. G is the specific globally fair, total computable additive-use-two F3 map of S136: for every output word τ of length n its clopen preimage is the union of FOUR distinct input cylinders of length n+2, listed by computable row R_G(τ). S137 established that SAFE001001 synchronizes the ancestry of all four cells. Every output state reaches SAFE and then completes that word with a prescribed extension of at most eight bits. Thus from any output history, each consecutive aligned eight-bit block has conditional probability ≥1/256 of containing a completed synchronizer; probability of t successive misses is ≤(255/256)^t.

### Lemma A138.1 — effective prefix decoding with explicit ambiguity bound

For input precision m and output depth n≥m, mark an output n-cylinder [τ] **labelled s**, |s|=m, if ALL FOUR input row cells in R_G(τ) extend s. Two different labels cannot occur. Call the union of unlabelled n-cylinders U_{m,n}. Labels are algorithmic from τ and m. Once a cylinder is labelled, every later output extension retains its label, by the source-child ancestry partition.

Choose block index N(m)=ceil(m/8)+2. A successful synchronizer block at index ≥N(m) makes all later compatible source cells descend from ONE source ancestor of length at least m. Therefore for n≥8(N(m)+t),

 λ(U_{m,n}) ≤ (255/256)^t.                                             (1)

This is an explicit, uniform computable modulus in both m and desired error; no independence of block events is assumed. Let E be the outputs that have successful synchronizers in infinitely many blocks. Then λ(E)=1; for every y∈E and every m, a sufficiently late τ≺y is labelled with the first m bits of its UNIQUE full preimage. Consequently the partial inverse J:E→X is computable on this effective conull domain: to output m bits, search successive G rows for the first common m-prefix. For each y∈E, G(J(y))=y; for each x with G(x)∈E, J(G(x))=x. Fairness gives λ(G^{-1}(E))=1.

Note: neither mere singleton fibres nor an abstract a.e. inverse gives (1). The quantitative bound is essential for the constructive rational transfer below.

### Lemma A138.2 — pull back EVERY bounded output martingale to a computable source measure

Take an arbitrary unit total nonnegative rational output martingale d. For integer k≥1 define d^{(k)}(τ) by stopping and freezing d at the FIRST prefix where its capital reaches or exceeds 2^k. This is a unit rational martingale. Since every child stake is at most twice its parent, 0≤d^{(k)}≤2^{k+1} at all nodes. It induces a computable output probability measure μ_k([τ])=2^{-|τ|}d^{(k)}(τ) satisfying

 μ_k(A)≤2^{k+1} λ(A)                                                   (2)

for all measurable A. In particular μ_k(E)=1.

Fix a source word s of length m. At output depth n, let B_{s,n} be the finite union of cylinders [τ], |τ|=n, with ALL four G-row cells extending s. This is computable clopen. B_{s,n} increases in n. By (1),(2), the quantities

 b_{k,s,n}=μ_k(B_{s,n})=Σ_{τ labelled s}2^{-n}d^{(k)}(τ)

are exact computable rationals, monotone in n, with an explicit error bound

 0 ≤ ν_k([s])−b_{k,s,n} ≤ 2^{k+1}(255/256)^t                          (3)

whenever n≥8(N(m)+t). Define ν_k([s]) as the limit. Equation (3) proves UNIFORM computability as a real number (at any requested rational precision), not merely lower semicomputability. Because μ_k(E)=1 and the unique inverse prefix labels exhaust all m-words on E, ν_k([s])=ν_k([s0])+ν_k([s1]), ν_k([empty])=1. Thus ν_k is a computable source probability measure and

 m_k(s)=2^{|s|}ν_k([s])

is a TOTAL nonnegative computable-REAL λ-source martingale, m_k(empty)=1, with m_k(s)≤2^{|s|}. No noncomputable limiting posterior or division by a vanishing conditional mass has been used.

For every finite output word τ on which d^{(k)} has stopped at capital C≥2^k, its value equals C on every extension of τ. On G^{-1}([τ]), ν_k=Cλ: indeed G is fair, its inverse on E is one-to-one modulo λ-null exceptions, and μ_k agrees with Cλ on [τ]. The equality holds for all source clopen subsets of G^{-1}([τ]) by the conull inverse and fairness. For any x with d(G(x)|τ) first reaching 2^k, continuity of G gives SOME source prefix s≺x with [s]⊆G^{-1}([τ]); hence

 m_k(s)=C≥2^k.                                                          (4)

This is an explicit SAME-SOURCE winning transfer for every level k; it does NOT assume that output capital evaluated on G(x) is itself a source martingale.

### Theorem A138.3 — ONE ordinary rational source martingale handles all levels

Set
 M(s)=(1/3)Σ_{k≥1}(3/4)^k m_k(s).

The weights sum to one. The series is a uniformly computable real at each finite s because m_k(s)≤2^{|s|}; its tail beyond K is at most (4/3)2^{|s|}(3/4)^{K+1}. Therefore M is a total unit nonnegative computable-REAL source martingale. If d(G(x)|n) is unbounded and y=G(x)∈E, for each k an s_k≺x has m_k(s_k)≥2^k, whence M(s_k)≥(1/3)(3/2)^k, unbounded.

Convert M into a *single TOTAL RATIONAL nonnegative martingale* without relying on uncomputable exact values: set r(empty)=2. For each input s choose effectively a rational q_s within 2^{-(|s|+4)} of M(s0)−M(s), and define
 r(s0)=r(s)+q_s, r(s1)=r(s)−q_s.
Induction yields exact fair averaging, all values rational, and
 |r(s)−(1+M(s))| < Σ_{j≥0}2^{-(j+4)}=1/8.
Thus r(s)>7/8 everywhere, and r/2 is a total unit nonnegative RATIONAL source martingale that succeeds whenever M does.

If y∉E, it has only finitely many completed synchronizer blocks; hence y∈E_N for some N in S137. S137's already constructed ONE ordinary rational source martingale W_* succeeds on G^{-1}(∪_N E_N) — that proof works for ALL finite-success outputs, not only those later proved degree≥2. Therefore
 D_d(s)=[(r(s)/2)+W_*(s)]/2
is one total unit nonnegative rational SOURCE martingale succeeding on every x for which the original d succeeds on G(x), including the exceptional no-infinite-synchronizer case.

**CONCLUSION (INTERNALLY PROVED):**
  ∀x∈CR, G(x)∈CR. Equivalently, G^{-1}(nonCR)⊆nonCR.
This closes S137's specific singleton-fibre leakage obligation. It yields NO separation R2\R3, because every R2 source is CR. It DOES NOT claim G maps R2 into R2 or prove any equality of the universal classes.

### Corollary A138.4 — effective decoding firewall beyond bounded fibres

The same argument works for any total computable globally λ-fair T with decidable finite source-prefix compatibility such that the λ-probability A_m(n) of disagreement between compatible n-output source prefixes at source precision m admits a UNIFORM COMPUTABLE modulus →0. There need be no uniform bound on T's actual fibre sizes, provided this effective a.e. inverse-decoding property and exact finite-cylinder computability hold. Such maps preserve CR. This is a sufficient condition, not claimed necessary or novel, and it does NOT cover arbitrary finite-fibre fair maps lacking a computable ambiguity-decay rate. It can be viewed as a constructive instance of known computable-randomness invariance under effective a.e. isomorphisms, but the rational compiler here has been written out rather than assumed.

## B. Genuine fair F2 with precisely the dense null H-double locus required by a hypothetical factor of G

Construct an additive-one fair map H using TWO distinct input words at each output n-row, of length n+1. Root row (0,1), state SAFE. For SAFE row (a,b), output0 row (a0,b0) has state PENDING; output1 row (a1,b1) has state SAFE. For PENDING row (a,b), output0 row (a0,a1) has state SAFE; output1 row (b0,b1) has state SAFE. Every row's four input children occur exactly once across its output siblings. Therefore H is total computable, all output cylinders have exactly two input cells, λ-fair, onto, and has at most TWO actual full preimages for all outputs.

If y has infinitely many zeros, it triggers infinitely many PENDING transitions (SAFE0 initiates one; a PENDING step returns SAFE). Each PENDING transition maps both new input slots to ONE previous input parent, so every fixed ancestral source-prefix level eventually collapses to rank one. Compactness gives exactly one full inverse. If y is eventually all ones, there is a last PENDING transition (or none); thereafter SAFE1 perpetually keeps one distinct descendant from each of the two current slots, giving exactly two full inverses. Hence

 |H^{-1}(y)| = 2 iff y is eventually all ones; else 1.                 (5)

In particular the H-double locus is countable, dense and λ-null; the H-singleton locus is comeagre of measure one. This CONSTRUCTIVELY refutes the attempted inference that a fair F2 outer map cannot have S137's necessary dense-null-double profile. It does **not** factor G: the inner F would have to be constructed and proven fair with cap two.

This H itself also has effective inverse decoding through repeated PENDING synchronizations (which occur with geometric tail under λ), so the A138 firewall proves H preserves CR. It is NOT a hierarchy separator.

## C. Stronger, still SCOPED factorisation obstruction: no additive-one plus additive-one factors

Assume G=H∘F and BOTH F,H are total globally fair maps of additive use at most ONE (first n outputs from first n+1 inputs). Fairness then makes exactly TWO aligned source (n+1)-cells per H output n-cell, and exactly TWO aligned original (n+2)-cells per F target (n+1)-cell. Thus the four G-row cells at output τ are partitioned into two unordered PAIRS, one pair for each H compatible input cell. Let p_i∈{0,1} label their H parent, with precisely two 0s and two 1s.

At any G SAFE row, the numbers of children sent to output0 by its four ordered input parent cells are (2,1,1,0); the output1 ancestor tuple is u=(3,3,1,2). Each H parent contributes four source grandchildren via its two original G cells. An additive-one fair H has only two possible sorts of one-bit splitting: (SPLIT) each of its two current cells contributes one child to EACH output branch, or (SYNC) one current cell sends BOTH its children to output0 and the other sends both to output1. The SYNC case would force an original G two-cell pair to contribute FOUR of the output0 grandchildren and the other pair ZERO. With weights (2,1,1,0), this is IMPOSSIBLE (no pair sums to 0 or 4). Thus H must SPLIT at every G SAFE node.

For SPLIT, each original G two-cell pair must contribute exactly TWO output0 children. The UNIQUE possible unordered partition is {0,3}|{1,2}. Along G SAFE output1 the next row's original parent-index tuple is (3,3,1,2); hence its H-parent labels are (h,h,k,k), h≠k. But that next G row is again SAFE. Its obligatory partition {0,3}|{1,2} is violated: indices 0 and 3 have opposite H labels, as do 1 and 2. Contradiction after only TWO consecutive SAFE1 transitions.

**Scoped result:** NO factorization G=H∘F exists with BOTH factors fair and use ≤n+1. This genuinely extends the earlier outer-shift/clopen-half-tag no-go, but an arbitrary F2 factor may have longer or unbounded use. There is NO proof of arbitrary F2∘F2 nonfactorability, nor any R2/R3 separation from this combinatorial restriction.

## D. R_fin / arbitrary F3: extended attempts and honest limits

The broad A138 effective-decoding theorem excludes as destructive candidates even genuinely coupled, non-patchwise, unbounded-fibre observers **if** they have the computable output-ambiguity decay stated there. The fat-boundary patch models of S130–S137 do not automatically meet this hypothesis: their identity-on-C part and inner components must be analysed separately, and composition may destroy effective decoding. A proposed coupling without a complete all-cylinder fairness proof and an every-output FINITE actual-fibre proof cannot be promoted to a legal R_fin observer.

A possible noncomputable-rate ambiguity mechanism remains viable, even for singleton fibres, but we did not construct a globally fair explicit F3 with an R2 surviving bad-image source, nor prove a universal rate for arbitrary F3. An F2 source winner after one map does not imply that image stays in R2; F2(R2)⊆R2 is open. R_fin requires one x satisfying ALL finite k, not separately chosen x_k. In particular a negative theorem about ONE specific G cannot settle the universal hierarchy.

## E. Comprehensive finite sanity versus infinite proof

Independent-in-method but SAME-AGENT checks replayed the S136 row recursion and new H row recursion through output depth12: at each depth every input prefix at the aligned level occurred exactly once, G had four compatible cells for every output cylinder, H had two. At depth12 G had 1519 SAFE and 2577 ACTIVE rows; H had 2731 SAFE and 1365 PENDING rows. For G, the fraction of output cylinders whose four input cells disagree on first two input bits decreased across depths8,10,12 as 3/8, 61/256, 341/2048. This does NOT establish an infinite rate; (1) is proved by the uniform synchronizer argument. The H exact-fibre assertion follows from repeated PENDING contraction/SAFE1 separation, not finite rows. C no-go uses only the exact parent weights and coherent F,H row requirements, not an exhaustive finite search.

S137 return maps u=(3,3,1,2), a=(0,0,1,1), b=(0,2,2,2), c=(0,0,0,0) and examples 1^ω degree3, 0^ω degree2, (001)^ω degree1, (0101)^ω degree2 remain unchanged. S136 ACTIVE limiting snapshot mass5/8 ≠ persistent D mass0. S135 U_j exact price2^-4j, S129 one-surplus hypotheses and S132–S135 restricted factorization were reviewed without overextension. SAME-AGENT verification and finite Fraction audits are SANITY ONLY; no independent referee, Lean, Palomar, novelty promotion or Gate4.

**FIRST INVALID INFERENCES:** a.e. singleton ⇒ CR preservation (needs effective inverse/transfer); limit of computable clopen probabilities ⇒ computable measure (needs explicit modulus (3)); bounded μ_k implies arbitrary d bounded (must STOP separately at EACH k); μ_k pulled-back success ⇒ rational martingale automatically (requires computable mixture and increment rationalization); dense-null H-double contradicts fairness (false, B construction); use1+use1 impossibility ⇒ arbitrary F2∘F2 impossibility (false inference); CR source ⇒ R2 source (false); several x_k ⇒ one R_fin x (false).

**FULL CENTRAL STATUS:** R2=R3, R2=MLR, R3=MLR, R2/R4, F2(R2) closure, arbitrary F3 source compiler, arbitrary F2-factorization, and a coupled nonpatchwise R_fin bad-image witness remain OPEN.