# P4-S104 — Separate adversarial validation

2026-10-12. Incoming main 8e57d9994ba21c219e3d94ffe31024d1ce175bac; written adversarial proof review of the new one-mechanism dossier, not referee, Lean, Palomar or hosted CI.

| Challenge | Finding |
|---|---|
| Unqualified CR source vs test witness | The test index e is computable, chosen a is a finite existential number; map program cannot access z as an oracle. |
| Read ahead / invertibility | Odd trigger depends ONLY on raw prefix preceding the current block; decode recursively from recovered preceding blocks, so K^{-1} is total. |
| Conditional fairness | Each fresh 2-bit block is sent by a bijection conditional on every preceding raw prefix; hence exact global fair distribution. |
| Unbounded fibres at unreachable outputs | F has global cap two by S083, K is global bijection. All-output cap inherited without target-only substitution. |
| Inverse lists mistaken for orientation | m(n) computed by finite clopen overlap/König; no computable inverse sheet selector claimed. |
| Tail-pair incompatibility | At every sufficiently late forced even block, raw difference (1,1) maps to (0,1); a tail complement has eventually (1,1), contradiction. Applies to *all* distinct F pairs as recorded S083 §4.3. |
| Rank-one factor proof | Fair injective total T has computable homeomorphic inverse; Q0 CR preservation would make F CR-preserving, contradict S083. Only this specified factor notion excluded. |
| Hidden deletion or output recoding | Fixed coordinate deletion after a fair computable homeo is CR-preserving (S003); transported S083 x demonstrates G destroys CR. |
| False universalization of source-specific gain | x_{e,a} varies with e,a; d* is a special-witness win. NO all-z proof. |
| Finite hitting times / totality | g is assumed total only in the REFUTED bridge; its maximal event is finite clopen, exact rational mass. Unbounded repair explicitly has no computable clock. |
| Martingale maximal pricing | Threshold 2^{n+2}d0 implies <=2^{-n-2}; fair preimage retains mass. Schnorr measure is *computable* because events are clopen, not because original test measures are computable. |
| Eventual-vs-every-level | Hard-code alleged finite N and reindex tail (A_{N+k}); eventual coverage still contradicts CR. |
| Source whole-error stream | S084 error-stream CR law prevents claiming eventually correct infinitely many guesses on CR output. No restart gain derived for generic z. |
| Competing partners | K^{-1}J_qK preserves MLR; two partners can both fail universal ML test; entry race unproved. |
| Padding | Every cylinder is replaced by finitely many longer cylinders at each j, with identical union but no emitted length<=2j. Uniform c.e. effectivity retained; no measure computation assumed. |
| External/gate scope | S101–S103 A–C and SRC distinctions frozen. No Gate4, Phase5, novelty or external review. |

**Separate local finite sanity audit:** exhaustive 8-bit triangular block shear for 2^8 inputs under a toy computable prefix predicate; each of 256 inputs had distinct 8-bit output, inverse recovered every input, and all 2^k prefixes (0<=k<=8) had exactly 2^{8-k} preimages. These are finite checks of the block algebra ONLY, not verification of infinite map F or EQ/SEP. The infinite global claims above rely on written proofs.

CI/protection evidence on entry: repo tree has NO .github/workflows, Actions workflow runs=0 (therefore jobs=0), check-runs=0, status contexts=0 with combined state pending; rulesets=[], administrative protection 403/inaccessible. No hosted validation passed. No open/recent PR; no competing S104 file/branch found. Finite review PASS only at stated scope; central goal FAIL/UNRESOLVED, as described in mathematics. S104 counts 1 of at most 2 speculative sessions; S105 review mandatory.
