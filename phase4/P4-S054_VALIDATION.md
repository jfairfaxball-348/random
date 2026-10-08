# P4-S054 Validation — source-specific forced cube certificates and finite-window clocks

Date: 2026-10-08
Session: P4-S054
Incoming main: 66da740a0132fd376d7d367e1dd26fb80cfa5e06
Mathematics: phase4/P4-S054_MATHEMATICS.md
Disposition: **PASS — source-specific finite positive witness and conditional/necessary timing law; NO X classification**

## Authority and uniqueness audit
The live GitHub main branch equalled the supplied P4-S053 SHA; P4-S054 mathematics/validation/close did not exist. P4-S001–P4-S053 mathematics, CAND-01 authority, pivot and late records were read with stated emphasis. Earlier mathematics frozen; Gate 3 PASS; Phase 4 OPEN; Phase 5 CLOSED.

## Raw/virtual algebra check — PASS
The actual H sends (x0,x1,x2) to (x0 xor x2,x0 xor x1,x0 xor x1 xor x2). Flipping x0,x1 jointly changes (u0,u1,u2) by (1,0,0) EXACTLY. The inverse column H^{-1}(1,0,0) is raw (1,1,0); it is not a one-raw-bit flip. An old s in another block cannot affect the future virtual q directly.

## Forced wrong halt audit — PASS
The true old s corner with both future bits flipped yields Y xor e_q. Syntactic avoidance of q makes the entire M(q) target run identical, returning Y(q) while the candidate's q-bit is 1-Y(q). The target halt is finite and uses no clipped-out coordinates. Value closure reads the third block bit and every as-yet-unread raw coordinate below 3 ceil(U(q)/3) except s,t,u, so every permitted virtual query is answered from actual already queried bits and synthetic cube answers. All eight simulations become pure finite-input partial computations. One wrong halt is guaranteed ONLY for actual X-derived p, with no uniform total runtime.

## Clock/timeout audit — PASS
Sigma(p) is partial computable, since eight fixed clipped computations are dovetailed with a finite known oracle table. Sigma(p)<infinity at all actual X value-closed states; it need not halt on arbitrary p. The closure sweep itself terminates with computable finite length. A tenure L is total computable from observed p and enters only AFTER closure. Simulating r steps of every corner at each r=1,...,L makes sigma<=L equivalent to a detected positive event strictly before future release. No negative inference from timeout or late halt is made.

## Fair capital audit — PASS
The three-bit payoffs are 0 at one forbidden atom, 8C/7 at seven others, with mean C. Exact sequential children: s=(6C/7,8C/7); after matching s, t=(4C/7,8C/7); after matching s,t, u=(0,8C/7); all other branches stay at 8C/7. Every pair averages to the parent. The actual X atom is not the forbidden corner. The hedge consumes s,t,u; no reset-free gain is claimed.

## Global scan/fibre audit — PASS
Each value-closure query and normal sweep query is fresh and outside protected {s,t,u}; each simulation is finite. Every temporary t,u is consumed on successful hedge or forced finite timeout, and v is exposed before simulation. The least-unread sweep exhausts all nonfinal-s coordinates; successful resets consume the least-unread old s. Thus every infinite transcript omits at most one raw coordinate, and its fibre size is <=2. Adaptive fresh fair-bit queries give output cylinders measure 2^-m. The martingale remains fair on arbitrary off-target sources even if it loses there.

## Conditional/necessary inference audit — PASS
If every renewed epoch has a timely cube exit, capital grows (8/7)^m and the scan witnesses X not in OH; this is NOT proved. Under hypothetical X in OH, each fixed total L scan makes finitely many exits and eventually reaches a last s; every subsequent finite reservation on X has a forced finite sigma but timeout with L<sigma. This does NOT show X in OH or that every conceivable one-hole scan has this schedule.

## Guards
No general old-row square refutation, all-transcript clock, two-row escrow, uniform total extension of sigma, numerical halting bound, or explicit M index is asserted. Preserve the P4-S008 and P4-S052 bounds, all P4-S001–P4-S053 results, MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR, and Y/M/H/X. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim. Phase 4 OPEN; Phase 5 CLOSED.
