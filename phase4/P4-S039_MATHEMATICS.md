# P4-S039 — affine one-hole states, local autoreduction codes and the singleton-completion obstruction

Date: 2026-10-07
Session: P4-S039
Incoming checkpoint: ebf18e6ef13c1a684b0164811b7a13cc2bdf576c
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **ONE RAW HOLE IN THE DISPLAYED THREE-BIT BLOCK IS EXACTLY AN AFFINE ONE-BIT STATE \(u=a+h\,c_i\). EXACT SIMULATION OF A SINGLE VIRTUAL UNIT HOLE REQUIRES RESPECTIVELY 2, 2 OR 3 RAW HOLES, SO THE OLD VIRTUAL SENTINEL CANNOT BE ALGEBRAICALLY MIGRATED TO A FRESH RAW HOLE IN ANOTHER BLOCK. HOWEVER THE THREE COMMITTED AUTOREDUCTION EQUATIONS HAVE STRONGER SEMANTIC CONTENT: THEIR LOCALLY SELF-CONSISTENT THREE-BIT SOLUTIONS FORM A BINARY CODE OF MINIMUM HAMMING DISTANCE AT LEAST TWO, AND FOR THE DISPLAYED MATRIX EVERY SUCH CODE FIXES AT LEAST ONE RAW COORDINATE AFTER APPLYING \(A^{-1}\). THUS FINITE LOCAL SIBLING TOTALITY GIVES A POSITIVE SAME-SOURCE RAW ONE-HOLE SIMULATION THEOREM. THE ACTUAL P4-S011 WTT WITNESS DOES NOT SUPPLY THAT TOTALITY: FOR A PRESELECTED RAW TARGET THE ALTERNATE AFFINE HYPOTHESIS MAY BE FINITELY REJECTED, MAY ALSO BE FULLY SELF-CONSISTENT, OR MAY FAIL ONLY BY DIVERGENCE. THE LAST TWO ARMS ARE EXACTLY THE ONE-BIT CIRCULAR / C.E.-SINGLETON-COMPLETION OBSTRUCTION. NO TOTAL RAW ONE-HOLE DESTROYER FOR THE ACTUAL \(X\), NO \(X\in OH\), NO OH NON-INVARIANCE AND NO \(R_2\subsetneq OH\) CONCLUSION ARE OBTAINED.**

## Authority, uniqueness and scope

Immediately before the first P4-S039 write, live main was exactly

\[
\texttt{ebf18e6ef13c1a684b0164811b7a13cc2bdf576c},
\]

the committed P4-S038 outgoing checkpoint. Repository search found no P4-S039 mathematics record. The only P4-S039 repository hit was the P4-S038 forward prompt, so the session identifier was unused.

P4-S001 through P4-S038, the selected CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S038 were read. All validated mathematics through P4-S038 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence is not reopened.

Retain

\[
R_2=\{x\in CR:\text{every total computable fair-coin-preserving global-}k=2\text{ map sends }x\text{ to }CR\},
\]

\[
OH=\{x\in CR:\text{every total computable adaptive no-repeat one-hole scan sends }x\text{ to }CR\},
\]

and

\[
OH^{iso}=\{x\in CR:\text{every computable fair-coin-preserving homeomorphism }H\text{ sends }x\text{ into }OH\}.
\]

The retained inclusions remain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Let \(Y\) be the settled P4-S011 computably random wtt-autoreducible source, let \(M\) be its committed self-avoiding wtt autoreduction, let \(D\) be the P4-S011 one-hole destroyer, and retain

\[
X=H^{-1}(Y).
\]

Then

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

The missing source-side statement remains whether \(X\in OH\).

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Exact affine state of one omitted raw coordinate

Work in one block over \(\mathbb F_2\) with

\[
u=Ax,
\qquad
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix},
\]

so

\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2.
\]

The inverse is

\[
x_0=u_0\oplus u_1\oplus u_2,\qquad
x_1=u_0\oplus u_2,\qquad
x_2=u_1\oplus u_2.
\]

The raw-coordinate flip columns are

\[
c_0=Ae_0=(1,1,1)^T,
\qquad
c_1=Ae_1=(0,1,1)^T,
\qquad
c_2=Ae_2=(1,0,1)^T.
\]

Suppose the raw coordinate \(x_i\) is withheld while the other two raw bits of the block are known. Put \(h=x_i\). Then the whole virtual block has the exact form

\[
u=a+h\,c_i
\]

for a known affine offset \(a\).

Thus the uncertainty is rank one, but it is generally not coordinate-local in virtual space.

### Lemma 1 — exact transcript information from one raw hole

With \(x_0\) omitted, no individual \(u_r\) is determined; all three change together with \(h\), while every pairwise XOR \(u_r\oplus u_s\) is known.

With \(x_1\) omitted, \(u_0\) is known while \(u_1,u_2\) share the same unresolved bit.

With \(x_2\) omitted, \(u_1\) is known while \(u_0,u_2\) share the same unresolved bit.

Equivalently, a virtual row \(u_r\) can be answered exactly without consuming the raw hole \(x_i\) if and only if

\[
A_{ri}=0.
\]

Therefore:

- an \(x_0\)-hole answers none of the three virtual rows;
- an \(x_1\)-hole answers only \(u_0\);
- an \(x_2\)-hole answers only \(u_1\).

If an exact virtual simulation requests a row with \(A_{ri}=1\), the actual value of that row determines \(h\), so the current raw hole must be closed.

This is the requested affine one-bit state, not merely a Hamming-distance observation.

## 2. Exact virtual unit holes need 2, 2 and 3 raw holes

A different question is how many raw coordinates must remain unresolved if the desired virtual ambiguity is exactly one unit coordinate.

The inverse images of the virtual unit vectors are

\[
A^{-1}e_0=(1,1,0)^T,
\qquad
A^{-1}e_1=(1,0,1)^T,
\qquad
A^{-1}e_2=(1,1,1)^T.
\]

Hence their raw Hamming weights are

\[
2,\qquad 2,\qquad 3.
\]

### Theorem 2 — local exact-simulation cut obstruction

Suppose two virtual completions of one block agree in every virtual coordinate except \(u_r\). Their raw preimages differ by \(A^{-1}e_r\).

Consequently any raw transcript which keeps those two completions simultaneously possible must leave unread every raw coordinate in the support of \(A^{-1}e_r\). In particular an exact virtual unit sentinel needs at least

\[
2,\ 2,\ 3
\]

raw unresolved coordinates for \(u_0,u_1,u_2\), respectively.

No one-raw-hole transcript can therefore reproduce the exact virtual state “all virtual filler bits known, exactly this virtual sentinel unknown”.

This recovers the P4-S033 fibre obstruction locally, but now identifies the exact affine cut dimension/support cost.

## 3. Pivot migration does not transport the old affine bit

The recoding is block diagonal. Let block \(B\) currently have affine state

\[
u^{(B)}=a+h\,c_i.
\]

Every raw coordinate outside \(B\) has coefficient zero in every virtual coordinate of \(B\). Therefore no observation in another block changes, reduces, or re-encodes the old variable \(h\).

### Lemma 3 — exact pivot migration is closure followed by independent reopening

If an exact virtual query in block \(B\) needs a row with coefficient one on \(h\), the only way to answer its actual value after the other two raw bits are known is to read the raw hole \(x_i^{(B)}\). At that moment the old affine line collapses to a point.

Withholding a fresh raw coordinate \(x_j^{(C)}\) in another block \(C\) then creates a new independent affine variable

\[
g=x_j^{(C)}
\]

supported only in block \(C\). It does not carry or replace the old \(h\).

Thus a raw one-hole process may operationally close one target and later choose another, but it cannot algebraically transfer an unresolved old virtual sentinel to a new raw coordinate.

The practical consequence is temporal. If the wager on the old virtual parity has not been fixed before the raw hole is consumed, a new raw hole cannot retroactively supply a fair pivot for that old wager. This is the same “spoiled” phenomenon isolated in P4-S034–P4-S038, now derived directly from the one-hole affine state.

This proves failure of exact transcript simulation. It does not yet rule out a different raw vulnerability process.

## 4. Use the actual committed autoreduction: local self-consistency codes

The preceding obstruction is too strong a target if one only wants to destroy \(X\) by some raw one-hole scan. The three virtual autoreduction computations may contain enough information to predict a different raw coordinate.

Fix a virtual block

\[
B=\{q_0,q_1,q_2\}.
\]

For \(v=(v_0,v_1,v_2)\in\mathbb F_2^3\), let \(Y[B\leftarrow v]\) be the oracle obtained by replacing only the three virtual bits in \(B\) by \(v\), leaving the actual \(Y\) unchanged outside \(B\).

Define the local simultaneous consistency set

\[
C_B=
\left\{
v\in\mathbb F_2^3:
M^{Y[B\leftarrow v]}(q_r)\downarrow=v_r
\text{ for }r=0,1,2
\right\}.
\]

The committed autoreduction convention is syntactic self-avoidance: while computing input \(q_r\), \(M\) never queries coordinate \(q_r\). The actual block

\[
Y\upharpoonright B
\]

belongs to \(C_B\).

Membership in \(C_B\) is c.e. from the outside-block oracle data: a positive witness consists of three finite correct halting computations. The wtt use bound makes every positive witness depend on only finitely many source coordinates. It does not decide nonmembership, because a sibling computation may diverge.

### Lemma 4 — the local consistency set is a one-error-detecting code

No two distinct elements of \(C_B\) have Hamming distance one.

**Proof.**
Suppose \(v,w\in C_B\) differed only at coordinate \(r\). Then the two candidate oracles \(Y[B\leftarrow v]\) and \(Y[B\leftarrow w]\) agree everywhere except \(q_r\).

The computation \(M(q_r)\) never queries \(q_r\), so its entire oracle computation is identical on the two candidates. It must therefore return the same bit on both. But local consistency requires it to return \(v_r\) on one and \(w_r\ne v_r\) on the other, a contradiction. ∎

Thus

\[
d_H(C_B)\ge2.
\]

This statement uses the actual three committed autoreduction computations in the block; it is not a generic predictor assumption.

## 5. The three equations semantically fix a raw coordinate

The displayed matrix has a special interaction with every length-three binary code of minimum distance at least two.

### Theorem 5 — local code-to-raw-hyperplane lemma

Let \(C\subseteq\mathbb F_2^3\) be nonempty and suppose every two distinct elements of \(C\) have Hamming distance at least two. Then there are a raw coordinate \(i\in\{0,1,2\}\) and a bit \(b\) such that

\[
(A^{-1}v)_i=b
\]

for every \(v\in C\).

In words: after pulling back by the displayed recoding, every such local self-consistency code lies in a raw coordinate hyperplane.

**Proof.**

If \(C\) is a singleton, the conclusion is immediate.

Suppose \(C\) has at least two elements.

If \(C\) contains an antipodal pair \(v,v+(1,1,1)\), no third word can be distance at least two from both endpoints: a third word has some Hamming weight \(k\) relative to the first endpoint, so its distances to the two endpoints are \(k\) and \(3-k\), one of which is at most one.

Hence \(C\) is exactly that pair. Since

\[
A^{-1}(1,1,1)^T=(1,0,0)^T,
\]

the two raw preimages differ only in \(x_0\); therefore \(x_1\) and \(x_2\) are both constant on \(A^{-1}C\).

Otherwise \(C\) has no antipodal pair. Since distance one is forbidden, every pair of distinct codewords has distance two. All codewords therefore have the same parity. But

\[
x_0=u_0\oplus u_1\oplus u_2,
\]

so \(x_0\) is constant on \(A^{-1}C\). ∎

### Corollary 6 — semantic raw prediction from the three committed predictors

For every block \(B\), the full simultaneous consistency set \(C_B\) semantically determines at least one raw coordinate of \(X\upharpoonright B\).

This is a positive algebraic result. The three virtual autoreductions are not merely circular equations with no raw content.

The difficulty is that \(C_B\) is c.e., not uniformly decidable.

### Corollary 7 — two positive local solutions already give a finite certificate

If two distinct members \(v,w\) of \(C_B\) have been enumerated, then a raw coordinate fixed by every possible future member of \(C_B\) can already be identified without waiting for negative information.

- If \(d_H(v,w)=2\), any further codeword compatible with minimum distance two has the same parity as \(v,w\). Hence \(x_0\) is already certified.
- If \(d_H(v,w)=3\), no third codeword is possible. Hence the raw coordinates on which \(A^{-1}v\) and \(A^{-1}w\) agree are certified.

So the hard local case is not multiple algebraic solutions. Multiple solutions become positively visible and already expose a safe raw coordinate.

The hard case is an apparently singleton c.e. solution set: the actual candidate is eventually visible, but there may be no finite certificate that no second candidate will ever appear.

## 6. A larger three-bit linear class

The preceding code lemma is not peculiar to one matrix entry-by-entry.

Let

\[
p=(1,1,1)^T.
\]

Call an invertible \(3\times3\) binary matrix \(A\) **raw-hyperplane coding** when every nonempty \(C\subseteq\mathbb F_2^3\) of minimum distance at least two is carried by \(A^{-1}\) into some raw coordinate hyperplane.

### Proposition 8 — exact matrix criterion in dimension three

An invertible \(3\times3\) binary matrix \(A\) is raw-hyperplane coding exactly when

\[
p^T A
\]

is a unit row vector and

\[
A^{-1}p\ne p.
\]

**Proof.**

Every minimum-distance-two code in length three is of one of two types:

1. it contains no antipodal pair, in which case all of its words have the same parity and it lies in a parity coset;
2. it contains an antipodal pair, in which case it consists of exactly that pair.

A parity coset pulls back to a raw coordinate hyperplane exactly when the parity functional

\[
p^TAx
\]

is one raw coordinate, i.e. \(p^TA\) is a unit row.

An antipodal pair has raw difference \(A^{-1}p\). It fixes at least one raw coordinate exactly when this difference has a zero coordinate, i.e. \(A^{-1}p\ne p\). ∎

For the displayed matrix,

\[
p^TA=(1,0,0)
\]

and

\[
A^{-1}p=(1,0,0)^T,
\]

so it lies in this larger class.

This enlarges the algebraic theorem beyond the single displayed recoding without making any claim about all finite linear recodings.

## 7. Per-target raw self-avoidance: the exact two-hypothesis trichotomy

The previous theorem chooses some raw coordinate after seeing the completed local code. A P4-S012 one-hole predictor has a stricter operational requirement: its target raw coordinate is already designated and may not be queried.

Fix a block \(B\), a raw target coordinate \(x_i\), and suppose the other two raw bits of the block have been exposed. There are exactly two raw hypotheses

\[
h=0,\qquad h=1.
\]

Their virtual blocks are

\[
u(h)=a+h\,c_i.
\]

Using the candidate block \(u(h)\), simulate the three computations

\[
M(q_0),\qquad M(q_1),\qquad M(q_2)
\]

while obtaining every outside-block oracle answer from the raw oracle and never querying the target \(x_i\).

The actual hypothesis \(h=X_i\) eventually makes all three computations halt with the correct candidate bits.

The alternate hypothesis has exactly three possible statuses.

### Case A — finite rejection

At least one alternate computation halts with a nonbinary output or with a binary output different from its candidate bit.

This is positively visible. Wait until:

1. the actual hypothesis has all three correct halts; and
2. the alternate hypothesis has a finite rejection.

Then output the actual value of \(h\).

This is a genuine target-visible raw self-avoiding partial predictor. It uses no \(x_i\), and the wtt use bound gives a finite oracle-use bound for every visible computation. No halting-time bound is required.

### Case B — a second self-consistent endpoint

All three alternate computations halt with their candidate bits. Then both endpoints of the affine raw line are in \(C_B\).

The three local autoreduction equations are exactly compatible with both raw values of \(x_i\). They contain no finite algebraic elimination of that designated raw target.

This is a genuine one-bit circular local system. It does **not** have ambiguity rank two: the unresolved raw state is still exactly one bit. What failed is coordinate determination for the preselected target.

### Case C — semantic uniqueness hidden by divergence

The alternate hypothesis is not in \(C_B\), but no finite rejection is ever seen because at least one required alternate computation diverges.

Then the actual raw target is semantically unique among the two hypotheses, yet the tested finite-elimination procedure has no finite certificate of that uniqueness.

This is the source-side analogue of the P4-S038 distinction between value closure and effective retirement. Here the unresolved negative fact is not a limiting price; it is completion of a c.e. local fixed-point code.

### Theorem 9 — exact local target trichotomy

For every block and every designated raw target coordinate, the three actual committed virtual autoreduction computations reduce the raw prediction problem to exactly Cases A, B and C above.

Case A yields a P4-S012-style raw self-avoiding correct predictor at that target.

Case B is an exact one-bit fixed-point circularity.

Case C is a c.e.-singleton-completion obstruction caused by sibling partiality.

The committed wtt use bound removes no arm of this trichotomy. It bounds which oracle values can be queried, but it does not force sibling halting.

## 8. Same-block dependency graph: the direct predictor test

The trichotomy can also be read at the target computation level.

For a raw hole \(x_i\), let

\[
I_i=\{r:A_{ri}=1\}.
\]

Thus

\[
I_0=\{0,1,2\},\qquad
I_1=\{1,2\},\qquad
I_2=\{0,2\}.
\]

If, for some \(r\in I_i\), the actual computation \(M^Y(q_r)\) can be evaluated without asking any other ambiguous same-block coordinate in \(I_i\), then its output \(u_r\) immediately determines the raw bit \(h=x_i\), because

\[
u_r=a_r+h.
\]

Concretely:

- for \(x_0\), any one of the three computations that avoids the other ambiguous block bits gives a direct raw prediction;
- for \(x_1\), \(M(u_1)\) avoiding \(u_2\), or \(M(u_2)\) avoiding \(u_1\), suffices;
- for \(x_2\), \(M(u_0)\) avoiding \(u_2\), or \(M(u_2)\) avoiding \(u_0\), suffices.

If every direct computation depends on another ambiguous same-block value, the finite same-block dependency graph contains a directed cycle. Theorem 5 shows that simultaneous equations can still semantically break such cycles; Theorem 9 shows exactly where effectivity can nevertheless fail.

Ordinary query edges should not be confused with essential dependence: a machine may query and ignore a bit. The simultaneous-consistency formulation is invariant under such inessential extra queries.

## 9. Positive same-source theorem under local sibling totality

The code theorem becomes an actual one-hole vulnerability theorem once the c.e. local code can be completed positively.

### Definition 10 — local three-bit sibling totality along a block

A block \(B\) has **local sibling totality** for \(M\) over \(Y\) if, for every one of the eight block assignments

\[
v\in\mathbb F_2^3
\]

and every \(r=0,1,2\), the computation

\[
M^{Y[B\leftarrow v]}(q_r)
\]

halts. The output may be right, wrong or nonbinary.

This is only a finite family of 24 computations at one block. It is much weaker than totality of \(M\) on every oracle and every input.

### Theorem 11 — local-totality raw one-hole simulation

Let \(A\) be any raw-hyperplane-coding invertible \(3\times3\) matrix, repeated blockwise. Let \(Y=H_A(X)\), and suppose \(M\) is a self-avoiding autoreduction of \(Y\).

Assume there is an infinite target run of fresh blocks on which local sibling totality holds at every reached block.

Then one of three total computable raw one-hole scans has a computable output martingale succeeding on \(X\).

In particular,

\[
X\notin OH.
\]

**Construction and proof.**

Construct three scans \(S^0,S^1,S^2\), one for each local raw coordinate \(i\).

At a fresh block \(B\), \(S^i\) designates raw coordinate \(x_i^{(B)}\) as its sentinel.

It first exposes the other two raw coordinates of \(B\). Thereafter, while withholding only the sentinel, it keeps querying fresh outside-block raw fillers and in parallel simulates all 24 candidate computations defining \(C_B\). Candidate virtual bits inside \(B\) are supplied from the finite hypothesis \(v\), not from the withheld raw sentinel.

If all 24 computations halt, \(C_B\) is now exactly known. By the raw-hyperplane property, it fixes at least one raw coordinate. If it fixes coordinate \(i\), the scan records the fixed bit as a full prediction; otherwise it records zero stake. It then queries its sentinel and starts a new fresh block.

The three scans can be synchronized on the target: outside the current block they use the same filler order and the candidate simulations depend on the same outside virtual data. After a successful epoch each has consumed all three raw coordinates of the current block and exactly the same outside-block filler prefix. The next target block is chosen as the first completely fresh block above that common queried prefix. Filler enumeration always resumes from the least fresh coordinate outside the designated sentinel. Hence the three target runs remain synchronized, and if every epoch triggers then the common queried prefix tends to infinity, so every raw coordinate is eventually consumed.

If local sibling totality fails on a sibling source, the scan does not cease producing output. It simply continues enumerating every raw coordinate other than its current sentinel. Hence any nontriggering transcript omits exactly that one sentinel. Every \(S^i\) is therefore an everywhere-total computable adaptive no-repeat one-hole scan.

On the actual \(X\), local sibling totality makes every epoch finish. The actual virtual block belongs to \(C_B\), so every nonzero predicted raw bit is correct.

At every completed block at least one of the three raw coordinates is fixed by \(C_B\). By the infinite pigeonhole principle, some fixed index \(i\) is certified on infinitely many target blocks. The martingale for \(S^i\) holds on all filler bits and on its zero-stake sentinel epochs, and bets all capital on the certified sentinel value whenever coordinate \(i\) is fixed. It therefore doubles infinitely often and never loses on \(X\).

Thus \(S^i\) destroys \(X\). ∎

### Corollary 12 — what the actual witness must still decide

For the displayed recoding, a proof that the committed \(M\) has local sibling totality along the synchronized fresh-block run would immediately eliminate the current \(X\) as an OH non-invariance candidate.

No such totality fact is present in P4-S011. The construction was selected precisely because wtt autoreducibility permits sibling divergence.

Thus the positive theorem is available, but its hypothesis is not licensed for the actual witness.

## 10. Why the committed data do not choose among the hard arms

The repository does not contain an explicit machine index together with a block-by-block table of all finite-perturbation sibling computations. The mathematical authority for \(M\) records only the properties supplied by the wtt-autoreducibility theorem and used by P4-S011:

1. \(M^Y(n)\downarrow=Y(n)\) for every \(n\);
2. the input-\(n\) computation never queries \(n\);
3. a computable use bound exists;
4. sibling computations may diverge.

Those facts are enough for Lemma 4 and Theorems 5, 9 and 11. They do not determine whether, on the actual fresh blocks:

- an alternate raw hypothesis is finitely rejected;
- both raw endpoints are locally self-consistent;
- or the alternate endpoint fails only by divergence.

In particular, the wtt use bound makes the relevant source-value table finite but does not make the finite family of sibling computations total. This is the same precise distinction exploited by the P4-S011 construction itself.

Therefore it would be an unsupported strengthening to claim that the actual \(M\) falls in Case A infinitely often, satisfies local sibling totality, or has a persistent raw-adjacent companion on every block.

## 11. Exact transcript simulation versus vulnerability simulation

The session now separates three levels.

### Level 1 — exact transcript simulation

Impossible with one raw hole for a virtual unit sentinel. The local support costs are \(2,2,3\), and blockwise pivot migration cannot transfer the unresolved old bit.

### Level 2 — finite simultaneous vulnerability extraction

Positive algebraically. The three autoreduction equations form a minimum-distance-two local code, and for the displayed matrix that code always fixes some raw coordinate.

If local sibling computations can be completed effectively, Theorem 11 converts this into a different raw one-hole destroyer. Literal reproduction of \(D\circ H\) is unnecessary.

### Level 3 — the actual c.e.-partial witness

Still unresolved. For a preselected raw sentinel, the alternate affine hypothesis may survive as a second self-consistent endpoint or may fail only through divergence. Neither outcome is excluded by the committed wtt facts.

This is strictly stronger than the P4-S033 observation that the fibres have the wrong Hamming shape. It identifies the remaining same-source resource as **effective completion of a c.e. local autoreduction code under a preselected raw hole**.

## 12. Separation status

No total raw one-hole destroyer for the actual recoded P4-S011 source \(X\) is obtained.

Equally, failure of the tested compiler does not prove

\[
X\in OH.
\]

Therefore no OH non-invariance theorem is proved and no strict inclusion

\[
R_2\subsetneq OH
\]

is claimed.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains unchanged. Ambiguity mass is not reinstated as an invariant.

## 13. Exact next target

P4-S039 removes pure finite linear algebra as the main obstacle.

The displayed recoding has a surprisingly strong positive property: once the full local consistency code is effectively known, the three virtual self-predictions always determine a raw coordinate, and local sibling totality yields a raw one-hole destroyer.

The unresolved issue is now the online/c.e. completion problem with a preselected raw sentinel.

P4-S040 should therefore test whether the Case-B/Case-C obstruction can itself be globalized or defeated:

- build a raw one-hole protocol that can progress through blocks without needing a negative singleton-completion certificate, perhaps by exploiting finitely visible pairs of local solutions or finite rejection of raw-adjacent companions; or
- prove an exact obstruction showing that every such protocol can be forced to stall on a locally self-consistent or divergence-only raw-adjacent sibling while still respecting the actual P4-S011 target.

The central finite object should be the raw-adjacent companion relation

\[
X\longleftrightarrow X\oplus e_j
\]

translated to the virtual difference \(Ae_j\), together with the c.e. enumeration of simultaneous \(M\)-consistent local candidates.

Do not return to backward-price normalization, the frozen P4-S015–P4-S031 bankroll line, or ambiguity mass unless the new source-side theorem genuinely requires them.

## Guards

All validated mathematics through P4-S038 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 remains OPEN; Phase 5 remains CLOSED.
