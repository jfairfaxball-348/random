# P4-S019 close

Date: 2026-10-06
Session: P4-S019
Incoming checkpoint: b71f3fff7e128cafc6eb0e225f7b3f00ce8dc7cd
Scope: selected CAND-01; k=2 loss-properness effectivity boundary only
Status: **COMPLETED**

## Result

P4-S019 answers P4-S018's remaining effectivity question negatively.

For an admissible canonical full-ticket account, b(K)=sup{E(v):W*(v)<K} is uniformly lower semicomputable from the finite computable ticket tree. Mere loss-properness, b(K)<infinity for every K, does not provide a computable upper bound.

A computable exact k=2 construction combines only settled ingredients:

- zero-stake control epochs choose between a productive mode and a halting-coded finite-excursion mode;
- the productive mode is the P4-S017 one-sided-trigger gadget and retains divergent harmonic absolute premiums;
- in the finite-excursion mode, a unary index e is followed by e successful one-sided-trigger ladder stages, placing ticket capital at P_e=1+H_e/2;
- zero-stake epochs then simulate machine e one step at a time;
- if it halts after t steps, t deterministic-trigger tickets add realized loss up to H_{e+t} while ticket capital stays P_e; if it never halts, no later positive loss occurs.

The account is globally admissible with reserve 1 and the induced least-fresh scan remains everywhere total, fair-coin preserving and globally k=2.

For each fixed K, only finitely many indices e can reach their waiting/burst phase while P_e<K. Each of those finitely many halting machines has a finite halting time, so b(K) is finite. This proves set-theoretic loss-properness.

However no total computable function U can majorize all b(K). If such U existed, choose K_e>P_e. A halt of machine e after t steps creates a bad-capital history with E=H_{e+t}<=U(K_e). Effective divergence of harmonic sums then computes a finite T such that H_{e+T}>U(K_e), proving that e can halt only before T. Simulating e for T steps would decide the halting problem.

Therefore loss-properness does not force a computable coercivity modulus.

The exact numerical extra condition for the settled ticket/restart architecture is **effective loss-properness**: a total computable U(K) with W*(v)<K implying E(v)<=U(K). This is equivalent, up to a harmless rational margin, to the P4-S018 running-maximum coercivity modulus.

P4-S011 is excluded more strongly than before. P4-S016 gives E=infinity along its computably random sentinel-first completion. If a globally admissible full-ticket account were loss-proper, unbounded E would force unbounded W*, making that computable ticket martingale succeed on a computably random completion. Hence any admissible P4-S011 account must have b(K)=infinity for some K. Bare admissibility itself remains unruled-out.

P4-S005 through P4-S018 remain settled. P4-S011, P4-S015, P4-S016, P4-S017 and P4-S018 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S019_VALIDATION.md.

Recommended next bounded session: P4-S020, still at k=2, testing only whether a natural local bound on zero-loss waiting / positive-loss reachability, or a weaker effectively searchable loss-bar condition, turns set-theoretic loss-properness into effective loss-properness without restoring absolute premium summability.
