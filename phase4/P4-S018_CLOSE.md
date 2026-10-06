# P4-S018 close

Date: 2026-10-06
Session: P4-S018
Incoming checkpoint: 5b77d2f6b0d824c9f8a0213908e6fbd6efc245a9
Scope: selected CAND-01; k=2 effectivity-of-coercivity boundary only
Status: **COMPLETED**

## Result

P4-S018 separates P4-S017 semantic coercivity from uniform effective reserve-floor certificates.

For the canonical full-ticket account, let E(v) be cumulative realized skipped loss and W*(v) the running maximum of ticket capital along a finite history. A clean local sufficient certificate is a total computable threshold modulus h such that, for every integer capital target K,

`E(v)>=h(K) => W*(v)>=K`

on every finite ticket history. This is equivalent to a computable nondecreasing unbounded running-maximum floor g(E), up to routine rounding. It is weaker than requiring a floor on current capital and exactly matches the fact that martingale success is an unbounded-supremum property.

The modulus suffices for the same P4-S017 ticket/restart transfer. It does **not** restore P4-S016 absolute premium summability: the fixed-H one-sided-trigger example from P4-S017 has a linear retained-surplus modulus while its harmonic premium sum diverges.

However semantic coercivity does not imply such a modulus. A computable mode switch between the two settled P4-S017 gadgets gives an exact k=2 ticket stream with two behaviours:

- a productive one-sided-trigger mode on which every divergent-E run makes ticket capital unbounded;
- finite deterministic bursts, selected by arbitrarily long unary control codes, in which price equals certain payout and the account remains at capital 1 while harmonic realized loss becomes arbitrarily large before positive tickets stop.

Every actual finite-burst run has finite E, so the combined account is semantically coercive. Yet for K=2 and every threshold T there is a finite burst history with E>=T and W*=1. Thus no uniform threshold exists even noncomputably.

The sharp obstruction is cross-branch nonuniformity. For the bad-capital tree `B_K={v:W*(v)<K}`, semantic coercivity only says every infinite branch of B_K has bounded E. A uniform modulus requires E to be uniformly bounded over all finite nodes of B_K. These are different.

The exact set-theoretic strengthening is loss-properness:

`b(K)=sup{E(v):W*(v)<K}<infinity.`

A computable uniform upper bound on b(K) yields the effective modulus. P4-S018 does not settle whether mere finiteness of b(K) in a computable k=2 ticket tree forces such a computable upper bound.

P4-S011 fails every effective modulus for every computable horizon selector: its settled target has E=infinity, so any such modulus would make the total ticket martingale succeed on the computably random sentinel-first completion, contradicting P4-S001.

P4-S005 through P4-S017 remain settled. P4-S011, P4-S015, P4-S016 and P4-S017 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S018_VALIDATION.md.

Recommended next bounded session: P4-S019, still at k=2, testing only whether finite bad-capital loss bounds b(K) are automatically computably bounded or can be finite but noncomputable.
