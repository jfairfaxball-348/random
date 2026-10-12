# P4-S107 — Canonical partner, ramification and failed exact-two surgery
2026-10-12; one owner-invoked CAND-01 Phase4 mathematics session. Live entry main 87191694a6fa58c8f088abfc7f80e55f10dd9e14, tree e9f03f8ee945928a5f654119498d5c688d7a9953, parent f0b4e71b0d32b47aa44b620a9ff35d473fc12f3e; S106 PR #3 merged. No novelty, Gate4 or publication work.

F2 comprises everywhere-total computable fair Cantor maps with one or two inverse points over EVERY output. DP2: every CR source x with an ACTUAL distinct partner x' satisfying G(x')=G(x) has CR output. CP2: every such G with EXACTLY two points over EVERY output preserves CR. Both unresolved at entry. S106 proves uniformly effective closed strata D_r of outputs with two preimages separated by input depth r, computable inverse charts conditional on r, preservation over Int(D_r), and dense-open safe output O_G=union_r Int(D_r) for everywhere-exactly-two G. Its meagreness conclusion does not exclude computably random inputs.

## Route A: computable approximations to the canonical partner

For G in F2 define J_G(x) as the distinct partner of x if there is one, and x otherwise. J_G is a set-theoretic involution.

**Theorem A1 (internally proved).** J_G is the pointwise limit of a UNIFORMLY COMPUTABLE sequence of continuous Cantor maps. Therefore J_G is Baire-one with meagre F-sigma discontinuity set. Every singleton-fibre x is a continuity point of J_G.

Proof. From S003/S007 take a computable monotone c(n)>=n such that the inverse image of any output cylinder of length c(n) meets at most two source n-cylinders. Compute L_n(x)={rho in 2^n: [rho] meets G^-1([G(x)|c(n)])}. It contains x|n and has at most two entries, decided by a finite clopen algorithm. Define P_n(x) to be the other n-prefix padded with zeroes when two exist, and x|n padded with zeroes otherwise. Each P_n is computable continuous. For a double point x with partner x', choose r separating their prefixes: for n>=r the two actual prefixes exhaust L_n(x), hence P_n(x)|n=x'|n. For singleton x, if an alternative in L_n(x) disagreed before fixed k for infinitely many n, choose witnesses v_n whose images share G(x)|c(n), with that early discrepancy. Compactness and c(n)->infinity give another actual preimage of G(x), impossible. Thus P_n(x)->J_G(x) in all cases. Classical Baire-one theorem gives the meagre F-sigma discontinuity locus. If x is singleton and x_i->x, every cluster point of J_G(x_i) maps to G(x), so is x; compactness forces J_G(x_i)->x. QED.

Caution: pointwise limits need no computable stabilization modulus. Continuity of J at an S083 destroyed SINGLETON is compatible with CR nonconservation. Baire meagreness is NOT a Schnorr-null certificate.

For an everywhere-EXACTLY-two G let Ram(G) be the source points with NO injective clopen source neighbourhood.

**Theorem A2 (internally proved).** For exact-two G, Ram(G)=Disc(J_G).
Proof. If J continuous at x, the distinct points x,J(x) have disjoint clopen U,V. Shrink U to clopen W with J(W) in V. A collision a,b in W would have b=J(a) in V, contradiction. Thus W is injective. Conversely if G is injective on clopen W containing x, any approaching x_i is eventually in W but J(x_i) stays outside W by exact two. Every limit of J(x_i) lies in G^-1(G(x))={x,J(x)} outside W, hence equals J(x). Compactness gives J(x_i)->J(x). QED. This converse is NOT asserted for mixed singleton/double maps: nearby singleton sources have J(u)=u. At singleton points J is continuous irrespective of local injectivity.

**Theorem A3 (internally proved, source-local DP2 constraint).** If x is CR, has a genuine partner x' and G(x) is non-CR, then for every n there exist DISTINCT a_n,b_n in [x|n] with G(a_n)=G(b_n). Both approach x. Let r separate x,x'. For n>=r, the common output of a_n,b_n does NOT lie in D_r because these two points exhaust its whole at-most-two fibre on the x-side. Their outputs approach G(x).
Proof. If G were locally injective at x, S106 A2 clopen source CR preservation would apply. The rest is compactness, the cap, and continuity. QED.

**Theorem A4 (internally proved).** With exact two everywhere, K_G=2^omega\(union_r Int(D_r)) satisfies
                    K_G=G(Ram(G))=G(Disc(J_G)).
J_G continuous everywhere iff D_r=2^omega for SOME finite r. In that case J_G is computable, G has a computable global clopen two-sheet split and preserves CR.
Proof. S106 A3 gives two clopen injective source sheets over an open output U within D_r, so G(Ram) is disjoint from O_G. Conversely, if both preimages of y have disjoint clopen injective neighbourhoods W0,W1, the compact image of their source complement avoids y. Choose clopen output U around y disjoint from that compact image. All two preimages of each v in U lie in W0 union W1 and there can be at most one in each. The disjoint clopen sets are separated by a common finite input prefix length r, so U subset D_r, placing y in O_G. Thus all y in K_G have some ramified preimage. Use A2. For global J continuity, compact graph of pairs (x,J(x)) avoids the diagonal; a finite uniform r separates all pairs. Hence D_r all. Conversely full D_r gives computable inverse charts (S106 A1) and global clopen decomposition (S106 A3). QED.

A1–A4 do NOT prove CP2/DP2. In particular no effective Schnorr cover of Ram was built.

## Route B: second partner on a destroying source

S083's destroyed source is SINGLETON, despite almost-everywhere double fibres. Attempting to append a second inverse via composition has a global obstruction.

**Theorem B1 (internally proved).** If G is onto, at most two-to-one and NONINJECTIVE, and H is any onto EXACTLY-two-to-one continuous map, neither G∘H nor H∘G has all-output fibre cap two.
Proof. Over a double G-fibre {a,b}, (G∘H)^-1(y) is the disjoint union H^-1(a) and H^-1(b), of size four. If every (H∘G)-fibre had size <=2, for every z whose H-fibre is {a,b}, |G^-1(a)|+|G^-1(b)|<=2. Both positive by onto, hence both one. Every a occurs in the H-fibre over H(a), so G is injective, contradiction. QED. This rules out ALL globally twofold pre/post padding, not an independently redesigned fair quotient.

Failed B2: grafting a partner only on a nowhere-dense closed support while keeping a continuous G unchanged on the dense complement is impossible by continuity. Successive neighbourhood-wide dyadic balancing remains conceivable, but no total computable fair global width-two repartition and actual partnered CR winner were built.

Failed B3: an exactly-two quotient with an exceptional thin branch and folding pairs has compatible topological shape, but no computable clopen tree with exact fair cell prices, all-output two-preimage certification, actual CR source, and total rational winning output martingale. S004 zero-weight genuine double branches and S005 noncomputable crossing masses defeat unpriced conditional transfer. A finite fold picture is NOT a counterexample.

## Route C: effective preservation attempt

Local clopen injectivity suffices for CR preservation at a source by S106 A2. For exact-two maps it is equivalent to partner continuity at the source. CONDITIONAL: if Ram(G) has a uniformly computable sequence of finite clopen covers E_n, covering Ram for every n, with effective rational measure <=2^-n and a valid Schnorr-test presentation, every CR source avoids Ram and CP2 follows. No such covers are known from our argument for arbitrary fair exact-two G, and Baire category or an ML-test is insufficient.

Calibration: fair computable marker-deletion maps 0^k1bt to 0^k1t and 0^omega to itself. Every output containing 1 has two inverses and zero-output has ONE. The partner flips the bit b after the marker and fixes all-zero, with J continuous at singleton zero despite unbounded separation length. 6096 finite n=2,...,10 prefix assertions passed in phase4/P4-S107_PARTNER_AUDIT.py, not an infinite proof.

## Classified outcome
INTERNALLY PROVED A1–A4 and B1; NOT externally verified or novelty certified. Two independent serious strategies developed and separately adversarially checked. No all-output exact-two fair CR-destroyer, ordinary conditional mass compiler, or effective universal Ram-cover. DP2=UNRESOLVED; CP2=UNRESOLVED; EQ R2=MLR=UNRESOLVED; SEP z in R2 outside MLR=UNRESOLVED; F2(R2) subset R2=UNRESOLVED. No gate, source-access, original Y/M/H/X, S101–S103 A–C or S105 historical NO-GO changes. Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED. S108 FUTURE.
