# P4-S037 close

Date: 2026-10-06
Session: P4-S037
Incoming checkpoint: 6e6694a0439001933427f4e830b085da637100e1
Scope: sustained Phase-4 one-hole normalization; rolling finite-state/backward-price normalization
Status: **COMPLETED**

## Result

P4-S037 moves the positive boundary strictly beyond finite packetization.

The open boundary is represented by a finite computable frontier: active spoiled claims already raw-determined but not virtually closed, finite controller state, their known parity values, and the next unopened blocks. No eventual halt/divergence information is hidden in that state.

The new positive condition is **effective fresh-frontier renewal**. Uniformly from every frontier, a computably finite transition retires every old claim and reaches either a safe absorbing mode or a new frontier whose carried claims are still virtually unseen fair bits. Although those new parities may already be raw-known, the virtual controller and accumulated virtual capital do not depend on their values.

That fresh handoff gives an exact backward-price identity. Averaging any normalized next-frontier price vector over the new unseen fair parities gives one, so the continuation vector disappears completely from the previous backward step. For the explicit P4-S035 one-pending-parity ray, finite-horizon normalized prices therefore stabilize after one backward transition. There is no ineffective infinite-limit problem for that architecture.

Combining this identity with the P4-S036 persistent-savings transform produces one total computable raw martingale. Once (K) savings thresholds have been locked, the saved virtual capital is at least (K) on every continuation, so every later raw conditional price is also at least (K). Hence any virtual success transfers to raw success.

The same rolling argument handles the concrete P4-S036 rank-one overlap realization
[
a_n	o c_n,qquad a_n	o c_{n+1}.
]
Thus neither a directed infinite dependency ray nor an infinite symmetrized overlap component is by itself the obstruction.

The negative boundary is sharper. The recoded P4-S011 witness has only one active nonzero sentinel claim at a time and a finite computable frontier state, so bounded open-claim width and finite state are not sufficient. Replacing its all-in sentinel wager by fixed fractional stake (1/2) still succeeds on the target, while local triggered backward-price vectors remain in ([1/2,3/2]) with ratio at most (3). Therefore uniform positivity and bounded price ratios do not suffice either.

The surviving P4-S011 obstruction is **non-effective claim retirement / backward-price stabilization**. Its wtt use bound makes each sentinel's source-value dependence finite. But after those values are exposed, a sibling computation may still remain open through arbitrarily many irrelevant fillers because finite simulation cannot certify divergence. In the half-stake version the finite-horizon price remains ((1,1)) until a halt becomes visible and then jumps to a fixed nontrivial well-conditioned vector.

At event level the P4-S011 claim process is acyclic and has no recurrent claim cycle. The committed abstract autoreduction does not determine whether the coarse repeated-block quotient necessarily contains a directed infinite ray rather than overlapping finite closures; P4-S037 shows that this graph distinction is not the decisive one.

More generally, computable effective convergence of the absolute backward prices of the persistent-savings martingale is sufficient for a raw compiler. Fresh renewal is the structural case where stabilization is exact after one backward step.

No proof that the P4-S033 recoded source (X) belongs to (OH) is obtained. Consequently no OH non-invariance theorem and no
[
R_2subsetneq OH
]
conclusion is available.

The retained comparison is
[
MLRsubseteq R_2subseteq OH^{iso}subseteq OHsubsetneq CR.
]

P4-S032 null-ambiguity preservation remains unchanged. The P4-S015–P4-S031 bankroll/ticket/frontier/recycling sequence remains frozen as the default route.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## Next bounded target

P4-S038 should attack **persistent-frontier claim retirement and non-effective backward-price stabilization**.

The primary test case is the recoded P4-S011 epoch after its finite wtt value-use frontier has been exhausted but before the sentinel computation is known to halt or diverge. Determine the weakest effective condition which makes the limiting stopped backward price computable: a computable retirement modulus, an effectively summable unresolved-price tail, or another exact optional-projection criterion.

Test whether one-hole geometry plus the displayed three-bit recoding forces any such condition. If not, isolate the sharpest exact persistent-claim pricing obstruction inside the actual one-hole problem. Do not return to graph rank or infinite-component geometry merely because they are available.

Source-side separation remains guarded: do not claim OH non-invariance without independently proving (Xin OH).
