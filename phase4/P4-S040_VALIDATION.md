# P4-S040 validation

Date: 2026-10-07
Session: P4-S040
Incoming checkpoint: a2902d7aed904f0fcf36693cf7da6105a1f6ab34
Scope: online c.e. local-code extraction under one raw sentinel
Status: **VALIDATED**

## Repository and scope checks

- Immediately before the first P4-S040 write, live `main` was exactly `a2902d7aed904f0fcf36693cf7da6105a1f6ab34`, the final P4-S039 outgoing checkpoint.
- The comparison of that hash with live `main` was `identical`, with zero commits ahead or behind.
- No P4-S040 mathematics record existed. The only prior P4-S040 repository hit was the forward prompt written by P4-S039.
- P4-S001 through P4-S039, the selected CAND-01 authority, the sustained post-P4-S031 pivot, and the required P4-S032 through P4-S039 records were read.
- All validated mathematics through P4-S039 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence was not reopened.
- The P4-S037/P4-S038 backward-price route was not reopened.
- Ambiguity mass was not reinstated as an invariant.
- No ordinary raw-martingale compiler for the actual P4-S011 win was attempted.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. Raw-adjacent acceptance/refutation is positively visible and target-self-avoiding

Fix a block (B), raw target coordinate (i), and the two raw completions determined after the other two raw coordinates have been read.

Each completion gives a finite virtual assignment (winmathbb F_2^3).

For a candidate (w):

- acceptance is witnessed by the three finite correct halts
  [
  M^{Y[Bleftarrow w]}(q_r)downarrow=w_r;
  ]
- finite refutation is witnessed by one finite wrong or nonbinary halt.

Both are c.e. events.

The current raw sentinel is not queried in order to simulate them. Every virtual value inside (B) is supplied from the finite candidate assignment. Every requested virtual value outside (B) depends only on raw coordinates outside (B), because the recoding is a direct product of three-bit blocks. Those values can be exposed as zero-stake raw fillers.

Thus the status test is a genuine target-self-avoiding finite-information process.

The wtt use bound is used only correctly: each finite halt has finite oracle use. No halting-time or divergence bound is inferred.

### 2. The trichotomy is exhaustive

On the actual target block (v), all three computations halt correctly, so (v) is accepted.

For the raw-adjacent companion (v+c_i), exactly one of the following occurs:

1. some computation halts wrong/nonbinary — finite refutation;
2. all three halt correctly — acceptance;
3. neither occurs — at least one required computation diverges, while every finite halt seen is compatible.

These are precisely P4-S039 Cases A, B and C.

Raw-adjacent decisiveness means only that Case C is absent.

### 3. At least one Case-A direction is forced on every fully decisive block

The P4-S039 code law gives

[
d_H(C_B)ge2.
]

The raw flip columns are

[
c_0=111,qquad c_1=011,qquad c_2=101.
]

If all three companions were accepted, then both (v+c_0) and (v+c_1) would be in (C_B), yet

[
(v+c_0)+(v+c_1)=c_0+c_1=100,
]

whose Hamming weight is one. Contradiction.

Therefore at least one companion is not accepted. If all three directions are decisive, every nonaccepted companion is finitely refuted, so at least one direction is Case A.

No completion of the whole eight-word code is used.

### 4. The three scan constructions are total computable

Each scan performs only finite work between source queries:

1. advance a fixed dovetail of the 24 candidate simulations for a finite number of machine steps;
2. inspect the finite simulation state for newly visible acceptance/refutation events;
3. if its own pair has just resolved, query its still-fresh sentinel;
4. otherwise query the next deterministic fresh filler.

It never waits for a Turing computation to halt before producing its next source query.

Thus the next queried coordinate is a total computable function of the finite transcript.

All source queries are fresh by construction, so the scans are no-repeat.

### 5. The universal candidate dovetail really synchronizes the three target runs

The scans initially read different pairs of raw coordinates in the current target block, but the 24 simulations range over **all eight** finite block assignments.

Therefore the simulation schedule itself does not depend on knowing the withheld bit or on choosing the actual block assignment.

Outside (B), all three scans see the same target raw source. They use the same deterministic outside-filler order. Hence after the same number of outside-filler rounds they have supplied exactly the same outside virtual oracle values to all 24 simulations.

The positive status of every finite candidate is therefore visible after the same outside-filler round in all three scans.

One scan can close its sentinel earlier than another. That adds one query inside (B) but does not alter the outside oracle values or the outside-round count.

Once all three target pairs have classified, every scan has closed its own sentinel and hence knows the whole block. Their outside queried sets are identical. The finite prefix-restoration sweep is therefore identical, and the next fresh block is common.

This validates the synchronization claim.

### 6. Every complete transcript has at most one hole

Fix one scan (S^i).

**Own pair never resolves.**  
The sentinel (x_i^{(B)}) remains unread. The other two raw coordinates of (B) were already queried. The scan continues enumerating every fresh coordinate outside (B). Hence the complete transcript omits exactly the sentinel.

**Own pair resolves, but synchronization never finishes.**  
The sentinel is consumed. The scan continues enumerating all remaining fresh fillers. Hence the transcript is exhaustive.

**Infinitely many epochs finish.**  
After each finite epoch the prefix-restoration sweep produces a larger completely queried initial segment and chooses the next block beyond it. The queried prefix tends to infinity, so the transcript is exhaustive.

Thus the global one-hole condition is verified on all branches, including branches on which some local search never completes.

### 7. Fair-coin preservation is exact

At each output stage the scan queries one fresh source coordinate, and its identity is a computable function of earlier output bits.

For any output word (	au) of length (m), the induced query sequence consists of (m) distinct source coordinates. The preimage of ([	au]) imposes exactly (m) independent fair-bit equations.

Hence its measure is (2^{-m}).

Every constructed scan is therefore fair-coin preserving.

### 8. The target martingales succeed

On (X), the actual raw endpoint is accepted.

In Case A, the alternate endpoint is finitely refuted, so the accepted endpoint is the actual one. The all-in sentinel wager is correct.

In Case B, the martingale wagers zero.

Every target block has at least one Case-A direction by the code argument. Therefore across the three scans there are infinitely many correct nonzero wagers in total. By the infinite pigeonhole principle, one fixed coordinate type receives infinitely many of them.

That scan's computable martingale holds on all fillers and Case-B sentinels and doubles on every Case-A sentinel. It never loses and doubles infinitely often.

Thus under raw-adjacent decisiveness,

[
X
otin OH.
]

### 9. Raw-adjacent decisiveness is genuinely weaker as a local halting requirement

P4-S039 local sibling totality requires all 24 computations to halt.

The P4-S040 condition permits divergence in rejected companions and in all irrelevant candidates.

A concrete self-avoiding local partial table shows the logical separation.

Let the actual block be (000). Write the three local partial output functions as functions of the two *other* bits, which enforces self-avoidance.

Choose:

[
f_0(0,0)=0,quad f_0(0,1)=0,quad f_0(1,1)=0,
]

with (f_0(1,0)) undefined;

[
f_1(0,0)=0,quad f_1(0,1)=0,
]

with the remaining values optional/undefined; and

[
f_2(0,0)=0,
]

with, in particular, (f_2(1,1)) undefined.

Then (000) is accepted.

The raw-adjacent companions are:

- (111): (f_0(1,1)=0
e1), so it is finitely refuted;
- (011): (f_1(0,1)=0
e1), so it is finitely refuted;
- (101): (f_0(0,1)=0
e1), so it is finitely refuted.

All three directions are decisive, while the (q_2)-computation on the (111) candidate diverges. Hence local sibling totality fails.

This validates that Theorem 5 uses materially weaker local completion data.

No claim is made that this table is the actual P4-S011 machine.

### 10. The Case-B same-block handoff obstruction is exact

Two raw-adjacent endpoints differ by exactly (e_i) in raw coordinates.

Therefore they agree exactly on the other two raw coordinates, and those were already read before classification.

For the displayed matrix this matches the virtual pair certificates:

- (c_0=111): the pair certifies (x_1,x_2);
- (c_1=011): the pair certifies (x_0,x_2);
- (c_2=101): the pair certifies (x_0,x_1).

No positively certified raw coordinate from the pair is still unread.

Thus the P4-S039 two-codeword certificate cannot by itself become the next prospective same-block sentinel.

### 11. The global no-double-reservation lemma is exact and appropriately limited

If one complete scan transcript leaves sentinel (j) unread forever and another coordinate (k
e j) were also never queried, that transcript would omit at least two raw coordinates.

The scan fibre would then contain at least four raw sources, contradicting global one-hole.

Therefore every prospective second sentinel must eventually be consumed on a branch where the first sentinel remains permanently open.

This proves the claimed obstruction to two **permanent** reservations. The session correctly does not claim that all adaptive finite-window handoff schemes are impossible.

### 12. Case C has no finite negative certificate

Once the actual endpoint is accepted, an unresolved companion can still later:

- be refuted by a wrong/nonbinary halt;
- become accepted after enough correct halts;
- remain unresolved forever through divergence.

No finite simulation stage distinguishes the third outcome from sufficiently late instances of the first two.

Thus a pure c.e. race cannot positively certify Case C.

The session's finite-waiting-policy discussion is kept at the correct level: without a certificate-time modulus, the committed data give no rate-free guarantee. It does not assert that the actual P4-S011 machine realizes a diagonal delay pattern.

### 13. Additional outside equations do not have a computably finite complete closure

For any **fixed finite** set of input indices, additional companion computations can be simulated target-self-avoidingly and can yield extra finite refutations.

But a wtt use bound is forward information:

[
nmapsto u(n).
]

It bounds the oracle coordinates used by each fixed (M(n)).

It does not bound the set of all inputs (n) whose computations may inspect one of the finitely changed block coordinates. Infinitely many (n) may have use extending beyond that block.

Therefore the record supplies no computably finite reverse dependency closure whose total verification would settle global companion consistency.

This validates Proposition 10.

### 14. The actual-source guard is preserved

The committed P4-S011 authority supplies target correctness, syntactic self-avoidance and a computable use bound, while permitting sibling divergence.

It does not say that every raw-adjacent companion is either accepted or finitely refuted on the P4-S040 synchronized blocks.

Therefore Theorem 5 cannot be applied unconditionally to the actual (X).

The settled facts remain

[
Xin CR,qquad H(X)=Y
otin OH.
]

P4-S040 proves neither

[
X
otin OH
]

for the actual committed witness nor

[
Xin OH.
]

No OH non-invariance and no strict (R_2subsetneq OH) conclusion follows.

## Validation disposition

**PASS.**

P4-S040 delivers the requested same-source extraction theorem under a materially weaker condition than P4-S039 local sibling totality.

The new positive boundary is **raw-adjacent decisiveness**: every raw-adjacent non-solution need only have one finite refutation witness, while accepted companions need the three local correct halts.

The precise surviving obstruction is divergence-only raw-adjacent partiality. Case B is positively visible and can be closed at zero stake under synchronized progress, but its certificate is retroactive and cannot itself hand off to a fresh same-block sentinel. Case C has no finite negative certificate, and global one-hole geometry prevents keeping a second permanent raw target open while waiting forever.

The sustained equation

[
R_2=OH;?
]

remains unresolved.

P4-S041 should attack finite-perturbation refutability / raw-adjacent decisiveness for the actual wtt-autoreduction mechanism, rather than return to pricing, bankrolls or ambiguity mass.
