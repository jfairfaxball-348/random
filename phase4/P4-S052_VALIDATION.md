# P4-S052 Validation — escrow cash-out and shielded old epoch

Date: 2026-10-08
Session: P4-S052
Incoming checkpoint: a157f51f8c57b851a2f4bc3d32696109255df51b
Mathematics: phase4/P4-S052_MATHEMATICS.md
Disposition: **PASS — finite theorems and conditional capture only**

## Authority
P4-S052 absent on incoming main. Live main matched checkpoint; P4-S001–P4-S051 mathematics, required selected CAND-01 authority, research pivot and designated focus read. Y/M/H/X, inclusion chain and P4-S008/P4-S051 retained.

## Truth table and fair child capitals
For exclusions (s=a,t=beta), (s=1-a,u=gamma): (beta,gamma) excludes both s-values; (beta,1-gamma) forces s=1-a; (1-beta,gamma) forces s=a; (1-beta,1-gamma) permits both s-values. The future fair t capitals are 2C/3,4C/3; u capitals (0,4C/3) on t=beta and (4C/3,4C/3) otherwise. Fair old s children are (0,8C/3) on correctly oriented outcomes and (4C/3,4C/3) otherwise. Every actual surviving terminal payoff is 8C/3 or 4C/3; all conditional means equal parent capital. PASS.

## Positive certificates
Same-row same-target complementary refutations exclude one old row. An actual consumed future matching the refuted beta excludes that old row, even with late certificate, but never supports a retroactive future wager. A finite old-only wrong/nonbinary halt excludes its old hypothesis. Different-target same-row exclusions alone do not orient old s. No negative halt or timeout inference. PASS.

## Shielded-old proof
At a P4-S049 shielded old epoch Y is total M-fixed and opposite-old Z global partial fixed. The two corners with future bit equal actual g are exactly Y/Z and cannot be finitely wrong-halt refuted. Thus all positive beta differ from observed g, matching orientation fails, same-target complementary-beta old orientation fails, and old-only refutations fail. A caught opposed-row escrow therefore uses actual future tuple (1-beta,1-gamma), which does not orient s. The shield is semantic, not algorithmically detectable. PASS.

## Scan and martingale
Finite computable L(e,k), K(e,k), bounded symmetric simulations, support queues and suspended protected requests ensure each finite round halts. At most s,t,u protected; t/u released at a finite positive exit or mandatory timeout. Alternating least-unread sweep exhausts every nonpermanent source coordinate. Every old reset consumes least-unread s; infinitely many resets imply exhaustion, finitely many leave at most final s. Thus global fibres <=2, totality/no-repeat and fair-coin cylinder probability 2^-m. Correct future 4/3, certified 2x, and zero-stake child prices are rational exactly fair on every transcript. PASS.

## Quantifier and preservation guard
Infinitely many **executed completed** positive exits by a fixed controller would yield X not in OH; not established on X. P4-S008 disallows infinite successful escrows at one fixed permanently omitted s on a CR source. If every old sentinel is consumed after finite time on all continuations, the scan is an exhaustive computable bijection and preserves CR. Under hypothetical X in OH the fixed success-gated controller makes finitely many exits and has final persistent s, without implying absence of passive or late events. PASS.

## Governance
PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged, Gate 3 PASS, Phase 4 OPEN, Phase 5 CLOSED. No X in OH, X not in OH, R_2=OH, novelty, openness, prior-art, Gate-4, publication or outreach claim.
