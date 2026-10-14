# P4-S148 — quantified claims and missing obligations

- A148.1 INTERNAL: ∀c∈N∀total computable additive-use-c G∀total nonnegative rational martingale d, letting p=d+1, ∃ONE total rational nonnegative ordinary source martingale e_(G,p), uniformly computed from G,c,p, such that ∀x∀n≥0 p(G(x)|n)/p(empty)=e(x|n+c)*F_n(x), where F_n is the product of p next-bit ratios over SOURCE-FORCED rows.
- A148.2 INTERNAL: ∀such G,d∀x∈CR, if d succeeds on G(x), then sup_n F_n(x)=∞; hence source-forced rows are infinite. Does not infer R2-specific destruction.
- B148 ALL-OUTPUT countercontrol: H adjacent-pair swap ∈F1⊆F2,F3, forced at every odd output index for every source; H preserves CR.
- Missing E-08: from ∀G legal additive-two F3 and ∀x∈R2 with bad image, obtain ONE total fair global F2/e acting on SAME x, every output ≤2 ACTUAL COMPLETE inverses, no oracle.
- E-00 OPEN: ∀G∈F3∀x∈R2 G(x)∈CR, unrestricted computable use.
- S-00 OPEN: ∃ONE legal G∈F3, ONE d, ONE x∈R2 destroyed by d∘G but protected against EVERY legal F2/e. 
- Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.