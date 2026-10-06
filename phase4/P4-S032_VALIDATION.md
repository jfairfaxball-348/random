# P4-S032 validation

Date: 2026-10-06
Session: P4-S032
Incoming checkpoint: 26c86b254410806dac04ddb57584d97b0da7da1c
Scope: sustained Phase-4 finite-ambiguity reconnaissance and theorem selection
Status: **VALIDATED**

## Repository and scope checks

- Live main matched 26c86b254410806dac04ddb57584d97b0da7da1c before substantive work and immediately before the first write.
- Repository search found no committed P4-S032 result before the session, so the identifier was unique.
- P4-S001 through P4-S031, CAND-01 authority and phase4/P4_RESEARCH_PIVOT_AFTER_S031.md were read.
- P4-S005 through P4-S031 remain settled; P4-S011 and P4-S015 through P4-S031 are preserved.
- The P4-S015–P4-S031 bankroll sequence was not reopened.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. R_k consequences

R_1=CR is exactly P4-S001. Monotonicity follows because F_k subseteq F_{k+1}. The P4-S011 k=2 destroyer lies in every F_k for k>=2, so every R_k with k>=2 and R_fin is a proper subclass of CR.

THM-0035 applies to every total computable fair-coin-preserving map as a morphism, so MLR subseteq R_fin. No equality or strictness beyond the settled/proved inclusions is asserted.

### 2. Schnorr comparison

CR implies Schnorr by THM-0002 and THM-0036 conserves Schnorr randomness under every computable-probability-space morphism. Therefore a total computable fair-coin-preserving map cannot send a CR source outside Schnorr randomness. In particular the P4-S011 image is Schnorr but non-CR. This uses no finite-fibre assumption and makes no new literature claim.

### 3. Null-ambiguity inverse algorithm

For each output prefix tau, effective total continuity supplies a finite input use and therefore an exact finite clopen representation of F^{-1}([tau]).

For oracle y and precision n, the inverse search asks for an m such that this clopen preimage is contained in one n-cylinder. The containment test is finite and decidable after refining the clopen representation to a common input length.

On a singleton fibre {x}, compactness forces such an m for every n. On a non-singleton fibre, an n separating two preimages prevents success forever. Hence the partial inverse domain is exactly the singleton-fibre locus, a constructive G_delta.

If the ambiguity locus is null, this domain and its source preimage have measure one. On them the inverse identities are exact. For every input cylinder [sigma], the inverse preimage C satisfies F^{-1}(C)=[sigma] intersect X_0, so lambda(C)=2^{-|sigma|}. Thus the inverse is a.e.-computable and measure preserving, and THM-0038 applies.

### 4. Arbitrarily small positive ambiguity witness

Block-localizing the P4-S011 destroyer D on a clopen cylinder [a] preserves total computability, fair coin and the global fibre bound two. The ambiguity locus scales by 2^{-|a|}. The null-ambiguity theorem forces the original D ambiguity locus to have positive measure, so the localized ambiguity measure is positive and can be made below any epsilon.

Finite prefixing preserves CR/non-CR by shifting a martingale past a fixed prefix, so the localized vulnerable source remains valid.

### 5. Composition algebra

A j-bounded fibre followed by a k-bounded fibre has at most jk preimages. The transport rule F_j(R_jk) subseteq R_k follows by composing an arbitrary second-stage G in F_k with the first-stage F.

The record correctly treats binary factorisation as insufficient *by itself* for R_2 hierarchy collapse; it does not claim a separation of R_2 and R_4.

### 6. Scan hole count

P4-S008 identifies a scan fibre with arbitrary assignments to never-queried coordinates. h finite holes therefore give exactly 2^h preimages; infinitely many holes give continuum many. Hence the scan global-k condition is h<=floor(log_2 k).

P4-S011's winning target has h=0 by its settled all-trigger/exhaustive property. The conclusion that final hidden inverse information is not the resource is therefore exact for that witness.

### 7. Selection discipline

Four routes received exact mathematical tests. The selected next target is not the smallest leftover bankroll lemma. One-hole normalization directly tests whether the strongest currently understood source-side mechanism is a normal form for arbitrary k=2 failure. Both a proof and a counterexample would sharpen the finite-ambiguity theory.

## Synchronization validation

The P4-S032 mathematics, close and validation records are committed. Phase-4 state, CAND-01 authority, next-session prompt, phase4 index, decision/session/start ledgers, failure/lesson ledger, AGENTS, project README and ROADMAP are synchronized to the selected P4-S033 one-hole-normalization target.

PHASE_GATE_LEDGER.md is intentionally unchanged because P4-S032 is not a gate review.

## Validation outcome

**PASS.**

Owner/external blocker: **NONE**.
