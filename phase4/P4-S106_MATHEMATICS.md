# P4-S106 — Effective double-fibre strata, local preservation and residual branch boundaries

2026-10-12. ONE owner-authorized Phase 4 mathematics session, CAND-01. Incoming live main f0b4e71b0d32b47aa44b620a9ff35d473fc12f3e (owner amendment, sole parent S105 commit 06480bea3053ea73268b94105bf88b1bcf2ccfa6; amendment tree 2b26eb1681957983e7854989d432c0f28806cf39). No S107 work. This is internal original proof development, NOT a prior-art novelty claim or independent certification.

## 1. Exact questions and established starting point

F2 = everywhere-total computable fair-coin-preserving Cantor endomorphisms G with 1 ≤ |G^-1(y)| ≤ 2 for EVERY output y. CR is defined using total rational computable martingales.

DP2: for all G in F2 and x in CR, |G^-1(G(x))|=2 implies G(x) in CR.
CP2: for all G in F2 with exactly two preimages at EVERY y, G maps CR into CR.

Both are **UNRESOLVED in S106**. CP2 follows from DP2; the converse is not established. Neither follows from S084's almost-everywhere balanced double fibres: S083's actual destroyed source lies on an exceptional singleton fibre. S003 already proves conservation with a global clopen injective two-sheet decomposition; S007 proves a uniform computable width-two inverse skeleton but not a uniform persistent selector. S004 gives an ACTUAL double fibre with vanishing conditional sheet weight, S005 invalidates computable hitting-measure inference even for clopen sheets. A–C of S101–S103, S105's finite ticket and bank, source access and Y/M/H/X are unchanged.

## 2. Architecture A: effective closed strata with computable two-branch charts

Fix G in F2. For r,m and an output y put
C_{r,m}(y) = {rho in 2^r: [rho] intersects G^-1([y|m])}.
These finite sets are computed uniformly from y|m, and decrease in m. By S003 there is a computable c(n) such that |C_{n,c(n)}(y)|≤2 for all y, with c nondecreasing (S007).

Define D_r = {y: |G^-1(y)| has two points with distinct length-r prefixes}.

**Theorem A1 (uniform effective closed decomposition, PROVED INTERNALLY).**
D_r = intersection over m of {y: |C_{r,m}(y)|≥2}. Consequently D_r is uniformly effectively closed, D_r⊆D_{r+1}, and the exact double-fibre locus D equals union over r≥1 of D_r. For y∈D_r and n≥r, C_{n,c(n)}(y) consists EXACTLY of the length-n prefixes of the two actual preimages. Ordering its two entries lexicographically gives uniformly computable partial inverse charts h_{r,0}, h_{r,1} on D_r, with a computable source-precision n -> output-use c(max(n,r)). On D_r their outputs are distinct, continuous, and G(h_{r,i}(y))=y. In particular the two preimages have the same Turing degree as y (and hence as each other), with a finite, nonuniform parameter r. This is source-equivalence, NOT computable conditional probability or preservation of CR.

Proof. The finite nonempty C_{r,m}(y) decrease. At least two elements persist at every m iff at least two distinct length-r cylinders each meet every nested compact preimage G^-1([y|m]); compactness then produces an actual preimage in each of those cylinders. Each predicate at finite m is computable clopen. The S003 cap |C_{n,c(n)}|≤2, together with two actual distinct r prefixes, leaves no room for any phantom entry at any n≥r. Lexicographic order is coherent under extension because the two branches already disagree by r; truncate length-r output for n<r. The finite clopen preimage calculation gives the claimed use. Conversely every actual preimage is a coherent path and is recovered. Output y is computable from either preimage by G. QED.

**Lemma A2 (local clopen injective slice, PROVED INTERNALLY; expands the application of S003).**
For ANY total computable fair G, finite clopen source set B with G|B injective, and CR x∈B, the image G(x) is CR. A global two-colouring of all fibres is not needed.

Proof. The normalized conditional lambda_B and mu_B=G_*lambda_B are computable measures; G|B is a computable compact injective map with a computable partial inverse on its compact image. Its computable measure isomorphism carries lambda_B-CR x to mu_B-CR G(x), using SRC-0015/THM-0038 precisely as in S003 Theorem 3. Membership x∈B transfers lambda-CR to lambda_B-CR via the fixed positive dyadic normalizer and eventual containment in B. Since mu_B(E)≤lambda(E)/lambda(B), failure of lambda-CR at y would, by DEF-0036 ratio characterization and a computable witnessing measure, imply failure of mu_B-CR. Contradiction. The normalizer is a positive rational; no arbitrary Π1 measure is assumed computable. QED.

**Theorem A3 (genuine-double local preservation, PROVED INTERNALLY).**
If y=G(x) belongs to the TOPOLOGICAL INTERIOR of some D_r, then EVERY CR source in G^-1(y) has CR output y.

Proof. Choose a finite output cylinder U=[tau] with y∈U⊆D_r. For each v∈U the finite list C_{r,c(r)}(v) has exactly the two actual r-prefixes. On the clopen set G^-1(U), classify source x by whether its r-prefix is lexicographically first or second in this list, computed from the finite output prefix G(x)|c(r). Both classes B_0,B_1 are computable clopen, each G|B_i is injective (exactly one source in each rank for EVERY v∈U). Apply Lemma A2 to the class containing x. QED.

**Theorem A4 (Baire boundary confinement, PROVED INTERNALLY).**
For arbitrary F2 map, every double-fibre counterexample to DP2 must have output in the meagre F-sigma set union_r boundary(D_r). In fact y on a double fibre but outside all interiors D_r lies in boundary(D_r) for every sufficiently large r. When G has EXACTLY TWO preimages at EVERY y, the union O_G=union_r interior(D_r) is dense open, and all its CR preimages are preserved. Thus CP2 can fail ONLY over the closed nowhere-dense set K_G=2^omega\O_G.

Proof. Each D_r is closed, so boundary(D_r)=D_r\interior(D_r) is closed and nowhere dense. Every double-fibre y belongs to D_r eventually, and if y is outside all interiors it belongs to all subsequent boundaries. For exactly-two G, union D_r=2^omega. If an open cylinder missed union interiors, the closed D_r would each be nowhere dense relative to that cylinder, contradicting the Baire theorem for the cylinder. Then O_G is dense open. Apply A3. QED.

**EFFECTIVITY WARNING.** D_r is effectively closed, but its interior need NOT be effectively enumerable and K_G need not be effectively null or even effectively closed from an index of G. This is a topological comeagreness theorem, NOT an almost-everywhere measure theorem, and does not exclude CR output in K_G. Nor does the chart compute conditional sheet weights: S004/S005 obstruct the naive transfer. In particular A4 neither proves DP2 nor CP2; the potentially exceptional set can contain CR points.

## 3. Architecture B: attempt to retain a genuine partner in the known destroyer

B1. Revisit S083 G*=F_T* composed with Dprime and S084: almost every output has two balanced preimages, but the actual CR-nonCR source is on an infinitely resolving singleton fibre. Thus G* is NOT a DP2 refutation. S084 error-stream theorem excludes turning infinitely resolving predictable guesses into finitely many errors on a CR output; neither capital growth nor an actual second point was obtained by perturbing the scan.

B2. Universal padding does NOT repair it. If pi deletes the first bit, then (G* composed with pi)^-1(y) has size 2|G*^-1(y)|, which is four at regular two-point fibres. On outputs where both points of pi^-1(y) are regular for G*, pi composed with G* also has four preimages. Both violate the ALL-output F2 cap. Finite explicit deletion and marker-deletion cases in the audit exhibit this 4:1 multiplication; they are not constructive refutations of CP2.

B3. A pointwise null-set graft is NOT a continuous fix. If two continuous Cantor maps agree off a nowhere-dense closed set, they agree on the dense complement and hence everywhere. Therefore one cannot change only an isolated/witness or closed nowhere-dense collection of inputs to add a partner while retaining the old map literally on every other input. This does NOT forbid a globally reorganized, everywhere-computable tiny-neighbourhood surgery.

B4. Tested the more ambitious possibility of an exactly-two quotient with pairs folding into one source limit as y approaches a boundary while its second inverse at the limit comes from elsewhere. A1 permits this topologically; no computable fair finite partition and infinite source-martingale win with such a boundary was constructed. There is no DP2/CP2 counterexample.

## 4. Architecture C: repeated binary observations and precise limits

**Lemma C1 (composition transport, PROVED).** For positive finite integers j,k,
F_j(R_{jk}) ⊆ R_k.
Here R_j denotes robustness under EVERY globally valid F_j map, including the identity, and F_j(S)={G(x): G∈F_j,x∈S}. Proof: for each H∈F_k and G∈F_j, H∘G is total computable and fair, with all fibres bounded by jk. Thus H(G(x)) is CR for all x∈R_{jk}. QED. Special case F2(R4)⊆R2. A mere R2 hypothesis cannot supply R4, so F2(R2)⊆R2 remains UNRESOLVED, and a failure would imply a same-source R2\MLR witness only under the established R_tot=MLR inclusion; no shortcut is asserted.

Theorem A1 also supplies a finite-input-information interpretation: double fibres permit a genuine persistent branch label with finite nonuniform split advice, but that label is not an effective measure disintegration and is not a computable martingale win on the source. C1's multiplicative fibre capacity contrasts with the exact-two local single-branch charts of A3.

## 5. Dispositions and dependencies

PROVED INTERNALLY: A1 effective Π1 double strata, two partial computable inverse charts and finite parameter Turing equivalence; A2 local clopen injective preservation from the S003 proof; A3 interior-stratum preservation; A4 meagre boundary confinement and the dense-open safe locus for exactly-two maps; C1 composition transport; elementary no-graft/no-naive-duplication objections. These are new to the programme as assembled, NOT checked for external novelty.

REFUTED as strategies: treating a.e. double status of S083 as a double-fibre witness, universal input duplication keeping width two, arbitrary continuous single-point graft. The measure-inference from a compact chart, computable interior enumeration, and meagreness⇒CR exclusion are REJECTED as unjustified (not asserted mathematical theorems to be disproved).

UNRESOLVED: DP2, CP2, an exact-double CR destroyer, a uniform effective null description of exceptional K_G, arbitrary conditional sheet stabilization, F2(R2)⊆R2, R2=MLR, and a z∈R2\MLR. A CP2 solution would not itself settle DP2. Even a double boundary chart failure is not a CR destruction witness without an actual source, valid map and winning rational martingale.

Dependencies: compactness and effective preimages from S002/S003; width-two c(n) from S003/S007; computable measure-isomorphism preservation THM-0038/SRC-0015 and ratio DEF-0036 used only at the already recorded source access level; Baire category on Cantor space; S004/S005 measure obstructions; S083/S084 exceptional singleton construction and predictable-error stream; S105 NO-GO allocation. No new source claims. CAND-01, Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN and Phase5 CLOSED preserved. No Lean/Palomar/publication, novelty or Gate4 work.
