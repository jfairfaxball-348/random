# P2-S002 — CAND-02 formulation alignment (E2)

Date: 2026-10-04  
Session: `P2-S002`  
Incoming checkpoint: `f3fa72d57498dff34640c77400d8aa39cfc48968`  
Scope: Phase 2 Discovery only; CAND-02 formulation alignment only  
Disposition: **RETAIN_PROVISIONAL — SHAPE UNCHANGED; E2 RESOLVED**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly. The committed tree and session ledger contained no P2-S002 session record; existing uses of the identifier were forward recommendations and the formulation brief, so P2-S002 was unique.

Gate 1 remains **PASS**. Phase 1 is **COMPLETED for gate purposes**. Phase 2 — Discovery is **OPEN**. Gate 2 is **CLOSED / NOT REVIEWED**. Phases 3–5 remain **CLOSED**. No candidate is selected and Fairfax-Ball Randomness is not defined.

This session performs only E2 for CAND-02. It does not search for a converse or equivalent prior definition, prove an implication, construct a witness, run a novelty audit, make a novelty/open-status claim, perform experiments or original mathematics, use Lean/Palomar, prepare a manuscript/publication, contact anyone, review Gate 2, open a later phase or begin P2-S003. CAND-01 and CAND-03 are not expanded.

## Candidate shape retained

CAND-02 keeps the P2-S001 predicate unchanged. On fair-coin Cantor space, let T range over **everywhere-total computable** fair-coin-preserving self-maps and let U range over effectively open sets. For

[
a_N(T,U,x)=\frac1N\sum_{i<N}\mathbf 1_U(T^i(x)),
]

`B_open(x)` requires only that the limit exists for every such T and U.

There is no ergodicity requirement, no computability requirement on λ(U), no convergence modulus, and no requirement that the limit equal λ(U).

## Exact hypothesis comparison

| Item | Transformation convention | Observable convention | Ergodicity / conclusion | Alignment consequence |
|---|---|---|---|---|
| **CAND-02 / B_open** | Everywhere-total computable fair-coin-preserving Cantor self-map | 1_U for effectively open U; bounded in [0,1] | No ergodicity; convergence only | This remains the candidate definition shape. |
| **SRC-0058 / THM-0063** | SRC-0058 builds a computable transformation from finite-string approximations so that the induced map is defined and infinite outside a computable G_delta null set. In the converse construction the source explicitly ensures the transformation is defined **almost everywhere**. | Positive direction: computable observables. Converse witness: a computable set/indicator. | No ergodicity; weak-Birkhoff convergence only | The source converse witness is **not established everywhere total**, so it cannot silently settle the narrower total-map predicate. The computable-set witness does not repair that map mismatch. |
| **SRC-0058 / THM-0064** | Same source computable-transformation convention: a.e.-defined, not an everywhere-total convention | Lower semicomputable observable in the source's Section 5 setting, represented by increasing computable approximants. An effectively open indicator is a bounded lower-semicomputable special case. | No ergodicity; convergence only | THM-0064 is a sufficient-condition benchmark for a broader observable/map setting. It supplies no converse characterization of B_open. No new implication is promoted in this session. |
| **SRC-0057 / THM-0059–THM-0060** | Computable a.e.-defined, measure-preserving transformation | Effectively open/closed indicators (THM-0059); nonnegative lower semicomputable observable (THM-0060) | **Ergodic**; limit equals μ(U) or integral f | These results are retained only as the guard against accidentally dropping ergodicity when asserting equality to expectation. They do not settle the nonergodic total-map question. |

## Source evidence and access

The catalogue was used first. It already settled the fair-coin domain, observable classes, weak-Birkhoff/Birkhoff distinction and the ergodic hypotheses in SRC-0057. One directly blocking detail remained under-specified: whether SRC-0058's "computable transformation" meant an everywhere-total Cantor map.

Only the smallest necessary passages of the already-catalogued **SRC-0058** were reinspected, using the arXiv HTML copy corresponding to arXiv:1206.2682:

- Definition 1.4, for weak Birkhoff versus Birkhoff;
- Section 2, for the computable-transformation representation and its null exceptional domain;
- Section 4, for the converse construction's explicit almost-everywhere definition guarantee;
- Section 5, for the lower-semicomputable observable convention and weak-2 theorem.

Access remains **STATEMENT_INSPECTED**. The journal identity is unchanged. P1-S010's recorded limitation also remains: the final author-hosted PDF timed out, so internal statement inspection is copy-qualified to the arXiv version. No new source, citation chase, newer-result search, converse search or prior-art search was performed. SRC-0057 did not need renewed external access because its exact ergodic hypotheses were already statement-inspected and recorded.

## Disposition

**Retain CAND-02 provisionally, unchanged. Resolve E2.**

Reason: the exact source scope does not make the recorded predicate redundant. THM-0063 characterizes Martin-Löf randomness using SRC-0058's a.e.-defined computable transformations and therefore does not provide the everywhere-total converse witness needed to collapse the CAND-02 formulation. THM-0064 supplies only a one-way nonergodic convergence benchmark for lower-semicomputable observables in that same source transformation framework. The ergodic equality-to-expectation results remain separately scoped.

This is a formulation finding only. It is **not** evidence that B_open is novel, open in the literature, distinct from MLR/W2R, or mathematically nontrivial.

## What a worthwhile future theorem package would still require

Without answering the mathematics, a future authorized programme would need an exact characterization of the **everywhere-total-map / effectively-open-indicator** predicate, or a source-backed reason that this formulation should be retired; a clear account of whether restricting from the source's larger observable class to bounded event indicators loses characterization power; and, only if a genuinely different class survives later gates, supported placement/separation and a natural test or betting interpretation.

Those are requirements, not claims or conjectures established here.

## Stopping point

CAND-01 remains provisionally retained and unexpanded. CAND-03 remains provisionally retained as an auxiliary direction and unexpanded. CAND-04–CAND-06 remain rejected exactly as recorded. No final candidate is selected. Gate 2 remains not reviewed.
