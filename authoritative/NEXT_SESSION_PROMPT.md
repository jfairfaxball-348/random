# Next Session Prompt — P4-S034

Continue the Fairfax-Ball Randomness Research Programme in https://github.com/jfairfaxball-348/random.

Run only Phase 4 — Mathematics session P4-S034. Treat committed repository state as authoritative. Pin live main at the exact P4-S033 outgoing checkpoint reported by the preceding session, reconcile any mismatch, confirm P4-S034 is unique, and read P4-S001 through P4-S033, the required CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, phase4/P4-S032_MATHEMATICS.md, and phase4/P4-S033_MATHEMATICS.md.

## Sustained Phase-4 target — homeomorphism invariance of one-hole robustness

Freeze all validated mathematics through P4-S033. Do not return to the P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence unless it becomes necessary for the theorem below.

Retain

R_2 = {x in CR : every total computable fair-coin-preserving global-k=2 map sends x to CR},

OH = {x in CR : every total computable adaptive no-repeat scan whose every transcript omits at most one source coordinate sends x to CR},

and the P4-S033 homeomorphism closure

OH^iso = {x in CR : H(x) is in OH for every computable fair-coin-preserving homeomorphism H}.

P4-S033 establishes

MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR.

It proves R_2 is invariant under every computable fair-coin-preserving homeomorphism, and therefore R_2=OH can hold only if OH has the same invariance. It also proves OH invariance under signed coordinate permutations, but not under arbitrary computable fair-coin homeomorphisms.

P4-S033 further shows that literal map-level scan normalization is false: precomposing the P4-S011 destroyer with an explicit blockwise invertible three-bit linear homeomorphism yields an exact destructive global-k=2 map whose double fibres differ in at least two raw coordinates, so it is not a one-hole scan and cannot become one by output-homeomorphic postprocessing. This does not yet separate R_2 and OH because the recoded source may still admit a different one-hole destroyer.

The explicit three-bit homeomorphism is, blockwise,

u0 = x0 xor x2,
u1 = x0 xor x1,
u2 = x0 xor x1 xor x2,

with inverse

x0 = u0 xor u1 xor u2,
x1 = u0 xor u2,
x2 = u1 xor u2.

A unit virtual-coordinate ambiguity therefore becomes a raw ambiguity of Hamming weight 2, 2 or 3.

## P4-S034 bounded task

Attack **only** the homeomorphism-invariance obstruction exposed by P4-S033.

1. Start with the explicit three-bit linear H above. Let x be computably random, let T be a total computable one-hole adaptive no-repeat scan, and let d be a computable martingale succeeding on T(H(x)). Test whether this data can always be compiled, on the same raw source x, into a total computable one-hole scan S and computable martingale e succeeding on S(x).

2. Work first at the P4-S012 self-avoiding stake level. Pull the T/d witness back through H and determine exactly what kind of raw-coordinate stake functional results. Track whether a wager on one virtual coordinate can be implemented while avoiding the raw coordinate currently being wagered on, when that virtual bit is a parity of several raw bits.

3. Prove the strongest exact positive invariance theorem available beyond P4-S033 signed permutations. Natural candidates include finite block homeomorphisms with a triangular/fresh-coordinate elimination order, bounded-depth reversible Boolean circuits admitting one raw fresh pivot for every queried virtual bit, or another explicitly checkable class. State whether the condition is genuinely weaker than coordinate permutation/bit flip.

4. In parallel, search for a genuine obstruction for the displayed three-bit H. Distinguish carefully:
   - failure to conjugate the *same scan*;
   - failure to convert the induced P4-S012 stake witness;
   - actual existence of x in OH with H(x) not in OH.
   Only the third is a separation witness.

5. If a computably random x in OH and H(x) not in OH can be proved, record the immediate consequence R_2 proper-subset OH using P4-S033 homeomorphism invariance of R_2. Do not claim separation from a candidate architecture alone.

6. If invariance survives the three-bit H, formulate the exact structural reason and determine whether it extends to all finite-block computable fair-coin homeomorphisms. If a finite-block theorem is proved, identify the next minimal homeomorphism class not covered.

7. Keep P4-S032 null-ambiguity preservation in force as a reduction for arbitrary destructive k=2 maps, but do not return to ambiguity mass as an invariant.

8. Do not fall back to a local bankroll lemma. The output of P4-S034 should be a real invariance theorem, a rigorous non-invariance witness, or the sharpest exact coded-hole obstruction that determines the next bounded attack.

## Selection guard for the next session

The sustained question remains whether R_2=OH. P4-S034 should decide whether the first coded-hole recoding can be absorbed by raw one-hole access, or isolate exactly why not. If the correct source-side normal form is larger than OH, preserve OH^iso as the current comparison class rather than forcing a scan presentation.

Preserve PA-0001 as **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 unchanged. Make no novelty, openness, prior-art, Gate-4, publication or outreach claim. Continue original mathematics only.

Record, validate and synchronize useful work, commit it, verify remote main, report the exact outgoing hash, and provide the next prompt if no blocker exists.
