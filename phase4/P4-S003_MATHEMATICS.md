# P4-S003 — k=2 weighted-sheet and martingale-transfer boundary

Date: 2026-10-05
Session: P4-S003
Incoming checkpoint: 4ccf7a1f9993a38ed15d8ba59207bde2ee1ecdee
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **K2 FORCES UNIFORM TWO-PREFIX INVERSE LISTS; EFFECTIVE WEIGHTED SHEETS SUFFICE WHEN AVAILABLE, BUT GLOBAL SHEET COLOURING IS NOT FORCED; GENERAL COMPUTABLE-RANDOMNESS PRESERVATION/FAILURE REMAINS UNRESOLVED**

## Authority, uniqueness and scope

Live main matched the incoming checkpoint exactly before substantive work. The committed phase4 directory contained only P4-S001 and P4-S002 records, repository code search returned no P4-S003 record, and authoritative state named P4-S003 only as the next session. P4-S003 was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 guard remains historical: before Phase 4 no computable-randomness consequence of the bare global finite-cardinality fibre bound had been established.

P4-S001 and P4-S002 are preserved exactly. This session stays at k=2. It makes no claim for k>2, novelty, openness, Gate 4, publication or outreach. DEF-0020 is unchanged.

## Exact k=2 hypotheses

Let lambda be fair-coin measure on Cantor space. Let F:2^omega -> 2^omega be everywhere-total computable, lambda-preserving, and satisfy |F^{-1}(y)| <= 2 for every y. No selector, inverse branch, disintegration, sheet colouring or conditional weight is assumed.

P4-S002 already gives, uniformly in y, the nested computable clopen fibre approximants

A_m(y)=F^{-1}([y↾m]),

with intersection equal to F^{-1}(y).

## Lemma 1 — k=2 forces a uniform two-prefix inverse list at every requested precision

For every input length n one can computably find an output length m_F(n) such that for every tau in 2^{m_F(n)}, the clopen set F^{-1}([tau]) meets at most two cylinders of length n.

Equivalently, from y↾m_F(n) one can compute a list L_n(y) of at most two strings of length n, and every x in F^{-1}(y) has x↾n in L_n(y).

**Proof.** For fixed n and candidate m, compute F^{-1}([tau]) for every tau of length m using the effective forward-use construction from P4-S001/P4-S002, and decide which of the finitely many length-n cylinders it meets. Thus the property “every tau has at most two length-n candidates” is decidable, so it is enough to prove that some m works.

Suppose not. Call tau bad when F^{-1}([tau]) meets at least three length-n cylinders. Badness is inherited by prefixes. If bad strings existed at every length, the finitely-branching bad-string tree would have an infinite path y. The finite sets

N_m(y)={sigma in 2^n : [sigma] meets F^{-1}([y↾m])}

would then be nested and have cardinality at least three at every m. Their intersection would therefore contain at least three distinct length-n strings. For each such sigma, the nested compact sets F^{-1}([y↾m])∩[sigma] are nonempty, so their intersection contains a point mapped to y. This gives at least three preimages of y, contradiction. Search therefore halts. ∎

This is strictly stronger effective inverse information than the raw descending-clopen name from P4-S002: at every finite input precision there is a computable bounded list of at most two candidates. It still does not coherently label the candidates as two persistent branches.

## Lemma 2 — computable conditional cylinder weights are bounded martingales

For a finite input string sigma and an output string tau define

w_sigma(tau)=2^{|tau|} lambda([sigma] ∩ F^{-1}([tau])).

Then w_sigma is a uniformly computable rational-valued fair martingale on output strings and 0<=w_sigma<=1.

**Proof.** F^{-1}([tau]) is computable clopen, so the displayed measure is computable rational. Since the two child preimages partition the parent preimage,

(w_sigma(tau0)+w_sigma(tau1))/2 = w_sigma(tau).

Also [sigma]∩F^{-1}([tau]) is contained in F^{-1}([tau]), whose lambda-measure is 2^{-|tau|}; hence the bound. ∎

For a fixed y, if the fibre misses [sigma], then w_sigma(y↾m) is eventually 0. If the whole fibre lies inside [sigma], it is eventually 1. The only genuinely unresolved behaviour occurs when [sigma] separates the two points of a double fibre: then w_sigma records the relative conditional mass carried by one sheet and need not be effectively stabilized by the information proved so far.

This gives a precise weighted form of the remaining problem.

## Theorem 3 — a computable clopen two-sheet decomposition is sufficient for forward computable-randomness preservation

Assume, in addition to the exact k=2 hypotheses, that there is a computable clopen partition D_0,D_1 of Cantor space such that each restriction F|D_i is injective. Empty sheets may be discarded. Then F preserves computable randomness forward.

**Proof.** Let p_i=lambda(D_i)>0 and let lambda_i be lambda conditioned on D_i:

lambda_i(B)=lambda(B∩D_i)/p_i.

This is a computable probability measure. Let mu_i=F_*lambda_i, also a computable probability measure because F is total computable and cylinder preimages are computable clopen.

On the compact clopen set D_i, the restriction F|D_i is injective. The P4-S001 finite-separation argument relativizes to this compact domain: its inverse on the compact image F(D_i) is computable. Hence F and that partial inverse form an a.e.-computable measure isomorphism between (2^omega,lambda_i) and (2^omega,mu_i), with the measures supported on D_i and F(D_i). SRC-0015 / THM-0038 therefore transfers lambda_i-computable randomness to mu_i-computable randomness.

If x is lambda-computably random and x∈D_i, then x is lambda_i-computably random. Indeed, after a sufficiently long prefix of x is contained in D_i, lambda_i(x↾n)=lambda(x↾n)/p_i; the ratio characterization in DEF-0036 converts any lambda_i-randomness failure into a lambda-randomness failure.

Finally, lambda=p_0 mu_0+p_1 mu_1 because F preserves lambda and D_0,D_1 partition the source. Thus mu_i(B)<=lambda(B)/p_i for every Borel B. If y were not lambda-computably random, DEF-0036 would give a computable probability measure nu with liminf_n nu(y↾n)/lambda(y↾n)=infinity. Along a mu_i-random y all mu_i(y↾n)>0, and

nu(y↾n)/mu_i(y↾n) >= p_i nu(y↾n)/lambda(y↾n),

contradicting mu_i-computable randomness. Therefore F(x) is lambda-computably random. ∎

This theorem unifies the positive intuition behind effective weighted sheets: the component output measures need not equal fair coin separately; finite mixture domination by fair coin is enough once each sheet has effective inverse information.

It does **not** show that such a partition is forced.

## Theorem 4 — k=2 does not force a global continuous/clopen two-sheet colouring

There is an everywhere-total computable fair-coin-preserving map H with fibres of size at most two such that no continuous two-colouring of the domain separates the two points in every double fibre. Consequently H admits no computable clopen partition into two sets on each of which H is injective.

Let a=0^omega. Every x!=a has a unique form

x=0^n 1 b z

where n>=0, b∈{0,1}, and z∈2^omega. Define

H(a)=a,
H(0^n 1 b z)=0^n 1 z.

Thus, on each cylinder Q_n=[0^n1], H is a one-bit left shift after the marker 0^n1.

**Checks.**

1. **Everywhere total computable.** To determine m output bits, inspect at most m+1 input bits. If no 1 has appeared before the relevant output position, the output prefix is all 0s; once the first 1 appears, delete exactly the following bit and copy the remaining tail.
2. **Fair-coin preserving.** The cylinders Q_n partition Cantor space except for the null singleton {a}. On each Q_n, the map is the fair-coin one-bit shift on the local tail and hence preserves the normalized fair-coin measure of Q_n. Therefore H preserves lambda globally.
3. **Fibres.** H^{-1}(a)={a}. For y=0^n1z, the fibre is exactly {0^n10z,0^n11z}.
4. **No continuous two-colouring.** If c:2^omega->{0,1} made the two members of every double fibre receive different colours, consider y_n=0^n1 0^omega with preimages x_n^0=0^n10 0^omega and x_n^1=0^n11 0^omega. Both x_n^0 and x_n^1 converge to a. Continuity of c at a makes both colours eventually equal to c(a), contradicting the required separation.

So the sufficient clopen-sheet hypothesis in Theorem 3 is genuinely additional.

This example is **not** a randomness-destruction witness. Away from a it has the evident a.e.-computable two-sheet structure: after locating the first 1, the deleted bit labels the sheet. More directly, for any computably random x=0^n1bz, removing the finite prefix 0^n1 and then applying the one-bit-shift martingale argument from P4-S002 preserves computable randomness of z; restoring the finite prefix 0^n1 preserves computable randomness of H(x)=0^n1z. Thus H preserves computable randomness.

## Why the forced two-prefix lists do not yet give a direct martingale transfer

Lemma 1 controls the **number** of coarse candidate input prefixes but not the measure carried by each candidate or the output precision required before the list contracts to size two.

At input precision n, the first searchable witness m_F(n) can be much later than n. The preimage of one output m-cylinder has total measure 2^{-m}; merely knowing that this mass lies in at most two length-n cylinders does not give a uniform lower bound on the share carried by the particular persistent branch. A naive transfer that splits output capital among the two coarse candidates can therefore lose an arbitrarily large factor tied to the resolution delay and the unknown conditional weights.

Lemma 2 identifies the missing datum exactly: effective control of the relevant w_sigma along a persistent sheet. P4-S003 proves neither that those weights are effectively available on all relevant points nor that they are unnecessary.

## Exact scan-functional counterexample route and its failure point

The proof of already-catalogued SRC-0061 / THM-0072 was rechecked only for its recorded mechanism. It starts with a computably random x defeated by a total computable nonmonotonic betting strategy S and maps an input z to the sequence of bits exposed by S; that total map induces fair coin but has no recorded finite-fibre bound.

For any total adaptive scan T that never queries an input coordinate twice, the output transcript y determines the queried coordinate sequence. Hence the fibre over y consists exactly of the assignments to coordinates never queried by that transcript. In particular, such a scan map has fibres of size at most two exactly when every transcript leaves at most one input coordinate unqueried.

This makes a tempting k=2 construction precise: complete the SRC-0061 scan by inserting filler queries until all but at most one coordinate is queried.

The completion attempt fails at a specific point. A filler query can expose a coordinate that S would later choose as a genuine betting position. When that later S-step is reached, an ordinary output martingale has already seen the bit and cannot retroactively place the bet that S would have placed before seeing it. Making filler queries conditional on observed success avoids stealing some important bets but then paths on which the condition fails can leave infinitely many coordinates unread, violating the **global** k=2 fibre requirement. Sparse unconditional fillers do not solve the issue: a successful nonmonotonic strategy may concentrate all decisive gains on an arbitrarily sparse set of future positions.

Therefore this bounded session does not produce an exact k=2 computable-randomness-destroying map.

## Successful and failed mechanisms

Successful in P4-S003:

1. **Uniform bounded-list inverse information:** for every input precision n, a computable output precision gives at most two candidate n-prefixes.
2. **Conditional-weight martingales:** the relative mass of any input cylinder inside output-cylinder preimages is a uniformly computable bounded martingale.
3. **Weighted-sheet preservation under an explicit effective split:** a computable clopen partition into two injective sheets suffices for forward computable-randomness preservation.
4. **Sharp topological boundary:** k=2 alone does not force such a global continuous/clopen sheet split.

Failed or incomplete:

1. **Coherently label the two-prefix lists.** The finite lists need not provide a computable persistent colouring.
2. **Split martingale capital equally between current candidates.** Candidate count alone does not control branch mass or resolution delay.
3. **Infer a general a.e. weighted decomposition from cardinality two.** No proof of that effectivization is obtained.
4. **Complete the SRC-0061 nonmonotonic scan by filler queries.** Fillers can pre-reveal later betting positions; conditioning fillers on success breaks the global fibre bound.
5. **Produce an exact k=2 destruction witness.** No such witness is established here.

## Proof dependencies and guards

New programme mathematics uses elementary effective compactness on Cantor space, computable clopen preimages, fair-coin measure, DEF-0004 and DEF-0036. The positive weighted-sheet theorem uses the already statement-inspected SRC-0015 / THM-0038 after its effective inverse hypotheses are established. SRC-0061 / THM-0072 is used only to inspect the known unrestricted scan-counterexample mechanism; no finite-fibre conclusion is imported from it.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001 is unchanged exactly.
- P4-S002 is unchanged exactly.
- General k=2 forward computable-randomness preservation/failure remains unresolved after this session.
- No result is claimed for k>2.
- DEF-0020 and all source/convention guards are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
