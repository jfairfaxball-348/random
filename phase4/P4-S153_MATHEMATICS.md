# P4-S153 — Two-sided finite-table density and the coherent inverse firewall

15 October 2026. Internal one-session original mathematics, SAME-AGENT audit only. Entry LIVE main 16f66bceb70431777cc39cfae95eebf8822205d0, tree 41413aa73edf683d4da7112ce22732e6bc76d495; S152 PR #52 merged by direct expected-head non-force fast-forward, sole parent de64170106f9cb27599a616e2431cf7df4b4ecf0. No open PRs/competing S153, Actions runs/check-runs/statuses ZERO = ABSENT_NOT_PASS; rulesets []; branch protection 403 = UNKNOWN_403. Frozen S101–S103 A–C and Y/M/H/X, DEF-0020, PA-0001 untouched.

Let X=2^ω, λ fair product measure, F_k total computable globally fair X→X maps with at most k ACTUAL COMPLETE inverse points above EVERY infinite output, CR computable randomness and R_k the sources surviving EVERY legal F_k output test.

## A153.1 — UNIVERSAL LOCALISED DESTROYING COMPLETION (INTERNALLY PROVED)

**Theorem.** Fix the S011 globally fair total F∈F₂ and one CR source Y with F(Y)∉CR. For EVERY globally fair total computable G, finite N≥0, source word t and positive rational ε, one can uniformly from a program for G,N,t,ε and a fixed program for F construct a globally fair computable D∈F₂ and a fair computable homeomorphism H with:
(i) ∀x D(x)↾N=H(x)↾N=G(x)↾N, including identical intrinsic minimum common input-prefix use for every n≤N;
(ii) D differs from H only inside ONE source cylinder C=[s]⊆[t] with λ(C)<ε, and all different outputs belong to ONE output cylinder V of the same dyadic measure;
(iii) EVERY infinite output has one or two ACTUAL COMPLETE D-inverses;
(iv) ∃x=sY∈C∩CR such that D(x)∉CR.
For ε_N→0 and N→∞ these D_N converge EFFECTIVELY UNIFORMLY to G. The witness sY is NOT asserted R₂ (in fact D itself kills it).

**Entire algorithm.** By total computability plus effective Cantor compactness, find an integer u≥max(N+1,|t|) so that the first N output bits of G depend on the first u input bits, and increase u until 2^-u<ε. Put a(v)=G(v0^ω)↾N for every v∈2^u. Fairness says each τ∈2^N has EXACTLY 2^(u-N) u-words in its a-preimage. Enumerate those words in lexicographic order; for v of rank i(v), set b(v)=a(v) concatenated with the (u-N)-bit binary encoding of i(v). Then b is a computable PERMUTATION of ALL 2^u words. Choose any u-word s extending t and define ON ALL INFINITE INPUTS
    H(vz)=b(v) z;
    D(vz)=b(v) F(z) if v=s; D(vz)=b(v) z if v≠s.
No oracle for Y, no chosen output path, and no future sheet membership is queried; the programme for F is globally total.

**ALL cylinder fairness and actual fibres.** For output words τ of length m≤u, the u-output tag b(v) is a permutation, so exactly 2^(u-m) equally weighted input u-cells produce τ and λ(D^-1[τ])=2^-m. For m>u, an output word τ has one UNIQUE first-u tag b(v). Conditional on the corresponding source v-cell, its remaining output prefix is from either fair F or identity; therefore λ(D^-1[τ])=2^-u·2^-(m-u)=2^-m. These are ALL finite output cylinders, including off-spine siblings. Since fair total maps from compact Cantor space are onto, for EVERY infinite y=b(v)w,
    D^-1{y}={vz:z∈F^-1{w}} if v=s,
             ={vw} otherwise.
Hence there are precisely 1 or 2 ACTUAL COMPLETE inverses above EVERY output, without a compact-limit guess. D=H off [s], and outputs on [s] lie in [b(s)]; the latter has equal dyadic mass and is fully covered by H and D.

**Actual destruction.** Fixed finite-prefix insertion/deletion preserves computable randomness (standard total rational martingale restriction), so sY∈CR. Since F(Y) is not CR, b(s)F(Y) is not CR. This equals D(sY). It is impossible to advertise x=sY as R₂: D itself is a legal F₂ map defeating x. Even if G has additive-use TWO, D may not have it, because F=S011 uses an unbounded adaptive scan. Identical FIRST N intrinsic moduli do NOT imply a uniform infinite additive-use promise. QED.

## B153.1 — BOTH CLASSIFICATIONS DENSE/CO-DENSE IN F₂ (INTERNALLY PROVED)

Let P⊆F₂ contain all maps conserving CR on EVERY CR input, and Q=F₂\P the CR destroyers. S152 constructs for EVERY fair total G and N a globally EXACTLY-two-inverse CR-conserving K_N agreeing with G first N bits on ALL x, and converging effectively uniformly to G. A153.1 constructs a global F₂ CR-destroying D_N with the same prefix agreement and effective convergence. Applying both to ANY F₂ G shows P and Q are BOTH dense in F₂ for the uniform finite-prefix topology and BOTH have EMPTY INTERIOR. Neither subset is closed: K_N→S011 F∈Q, whereas D_N→identity∈P. In particular neither is open.

**Precisely scoped no-go:** An EXTENSIONAL detector that decides by finitely many source-output prefix-function observations (a finite set of arbitrary source/output cylinder queries) cannot positively CERTIFY either conservation or destruction under only the total-fair-F₂ promise: each finite observation transcript has a globally legal opposite-type completion. A code-INTENSIONAL proof that a particular given algorithm (such as identity) conserves CR is not refuted. Neither does this rule out an infinite effective search on the FULL code nor a class-specific E-08 transfer. S152 alone proved the conserving half; the destroying half and two-sided topological classification are the S153 advance.

This also gives an EXACT source-local result: even if a full-map finite table, its q transitions, all intrinsic shortest prefix uses, and every finite chart count through an arbitrary finite N are fixed, destruction can be hidden entirely in a future tail WITHIN an arbitrarily small prescribed cylinder, yet all output fibres remain capped globally. No FINITE chart-resurrection statistic can settle the question in either direction.

## C153.1 — AN ACTUAL INFINITE COHERENCE FIREWALL (INTERNALLY PROVED)

Let (H_j) be a uniformly computable family of globally fair total computable homeomorphisms converging EFFECTIVELY UNIFORMLY to a total computable G. Assume a SINGLE total computable function h(k) such that FOR ALL j,k,a,b,
  H_j(a)↾h(k)=H_j(b)↾h(k)  ⇒  a↾k=b↾k.
(Unlike individually computable inverse moduli h_j, the SAME h works across ALL stages.)

**Conclusion:** G is a fair computable homeomorphism with a computable inverse and preserves CR.

**Proof.** Fix output τ; effective uniform convergence gives an index j after which H_j^-1[τ]=G^-1[τ]. Thus G remains fair, and compactness plus full-support output measure makes G onto. For any a,b with G(a)=G(b), use uniform convergence to make H_j(a),H_j(b) agree on h(k) output bits; the uniform inverse-use promise forces a↾k=b↾k. All k yield injectivity. For effective inversion, given y↾h(k), take j with H_j and G equal on first h(k) output bits on ALL sources. Use ANY computable extension y' of that output prefix and compute H_j^-1(y')↾k. The uniform inverse-use condition makes this independent of the extension. If x=G^-1(y), then H_j(x) has the same h(k) prefix as y', so H_j^-1(y')↾k=x↾k. Hence this computes G^-1(y)↾k from y↾h(k), uniformly. Standard fair computable-homeomorphism martingale transport (S001/S102, SRC-0015) proves G(CR)⊆CR. QED.

The hypothesis is a genuinely INFINITE cross-approximation effective datum. It already FORCES degree one; it is NOT a two-sheet F₂ compiler and does not decide E-08. Any S152 approximating homeomorphisms to S011's destroyer necessarily FAIL to share such a computable uniform inverse modulus. This last consequence does not assert an effective inverse selector for a degree-two G.

## A. Failed infinite chart-resurrection attack — exact obstruction

At S129's normalized two-cell chart, test the four children for 2:2 output balance; when that holds, original G rows can be copied, and when it fails an always-total chronological-tail fallback constructs a globally fair cap-two map (S117/S129). But resurrecting after q=1→2→t or q=3→2→t demands realignment of TWO true inverse reservoirs without knowing the eventual selected branch. At a four-cell split with t target grandchildren and 4-t sibling grandchildren, simultaneous promised payoffs a,b obey t*a+(4-t)*b≤4; target-only gain 4/t assumes advance knowledge of continuation. S135's global oscillator supplies infinitely many legal 3:1↔2:2 changes. No effective deterministic state machine with proven EVERY-output cap and unbounded SAME-x rational capital has been found for persistent oscillation. S141's positive self-folding pockets show positive fold density is not automatically destructive. A153/B153 establish only a finite-observation no-go; no infinite-stage E-08 impossibility theorem is claimed.

## B. Rival pathwise obstruction and one-source separation — attempted, OPEN

C153 supplies a genuine tail/coherence invariant, but only with a very strong common inverse modulus leading to injectivity. Its two-sheet counterpart would require an effective conditional sheet-price/disintegration and an online total cap-two bank. A source x=sY delivered by A153 is computably random but already defeated by D∈F₂, so x∉R₂. A proof of ∀F₂∃x_F surviving does not give ONE ∃x∀F₂ survivor. There is no globally legal F₃, ordinary winning d, and SAME x∈R₂ constructed. S139 S-00 remains OPEN. The S145–S147 priced-open-set criterion is not triggered by merely converging finite event measures: infinite stopping probabilities may be noncomputable/nonconvergent (S144). This also blocks extrapolation of arbitrary-use E-00.

## C. Arbitrary-use E-00 separately — not closed

A153.1 uses an arbitrary fair G and a COMPUTABLE effective prefix modulus; this does not yield a rational martingale witnessing G(x) nonCR on a fixed x∈R₂. Nor does replacing G by D_N transfer an infinite winner to the same x: ∀N∃D_N is not ∃D∀N. Identity, finite-block bijections, adjacent swap, S011 destroyer, S135 oscillator, S141 pocket map and S145–S151 source-price/entropy firewalls are consistent controls. No infinite stopped-event mass was inferred from exact finite dyadic cylinders.

**Final:** A153.1, B153.1 and C153.1 internally proved symbolically, no claim of independent review or literature novelty. E-08/E-00/S-00, R₂=R₃ and R₂≠R₃ remain OPEN; Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
