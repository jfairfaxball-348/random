# P4-S033 validation

Date: 2026-10-06
Session: P4-S033
Incoming checkpoint: 1995951e38106e18effb79dcc44e4a96a77c3793
Scope: first one-hole normalization step
Status: **VALIDATED**

## Repository and scope checks

- Live `main` matched `1995951e38106e18effb79dcc44e4a96a77c3793` before substantive work and immediately before the first write.
- Repository search found no committed P4-S033 record before the session, so the identifier was unique.
- P4-S001 through P4-S032, the selected CAND-01 authority, `phase4/P4_RESEARCH_PIVOT_AFTER_S031.md`, and `phase4/P4-S032_MATHEMATICS.md` were read.
- All validated mathematics through P4-S032 is preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence was not reopened.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach work was performed.

## Mathematical validation

### 1. One-hole coordinate-locality

For a fixed scan transcript, every queried raw coordinate is fixed by the transcript. P4-S032 already identifies the fibre with arbitrary assignments to omitted coordinates. Therefore a two-point fibre of a one-hole scan has exactly one omitted coordinate and the two preimages differ there and nowhere else.

This is strictly stronger than the P4-S007 width-two statement. Width two bounds the number of compatible prefixes but does not bound their Hamming distance.

### 2. Homeomorphism invariance of (R_2)

For a computable fair-coin-preserving homeomorphism (H), composition (Fcirc H) remains total, computable and measure preserving. Since (H) is bijective, fibre cardinalities are unchanged. Applying the same argument to (H^{-1}) gives the equivalence (xin R_2iff H(x)in R_2).

P4-S001 supplies computability and CR invariance of the inverse pair; no stronger inverse assumption is imported.

### 3. (OH^{iso}) reduction

The definition

[
OH^{iso}={xin CR:(orall H) H(x)in OH}
]

immediately gives (OH^{iso}subseteq OH) via the identity. If (xin R_2), homeomorphism invariance gives (H(x)in R_2subseteq OH) for every (H), hence (R_2subseteq OH^{iso}).

If (xin OH) but (H(x)
otin OH), then (x
otin R_2), otherwise invariance of (R_2) would imply (H(x)in R_2subseteq OH). The claimed separation consequence is therefore exact.

### 4. Signed-permutation compilation

If a virtual scan asks coordinate (q) of (H_{pi,a}(x)), asking raw coordinate (pi(q)) reveals the needed virtual bit after XOR with the known (a(q)). A computable permutation preserves no-repeat and takes a virtual omitted set of size at most one to a raw omitted set of the same size.

The finite-transcript conversion is bijective stage by stage up to a known child swap, so (e(z)=d(v(z))) satisfies the martingale equality exactly and has identical capital along the target. This proves source-level normalization for the stated subclass.

### 5. Multi-coordinate output mixing example

For the left-shift scan followed by pairwise XOR postprocessing, the first output bit is (x_1oplus x_2). A scan's first output bit is necessarily the value of one fixed queried source coordinate, because no transcript information exists before its first query. Hence this composite is not literally a scan, while P4-S001 removes the output homeomorphism for randomness-normalization purposes.

### 6. Three-bit linear coded-hole homeomorphism

For each block the forward map is

[
u_0=x_0oplus x_2,quad
u_1=x_0oplus x_1,quad
u_2=x_0oplus x_1oplus x_2.
]

The proposed inverse satisfies

[
u_0oplus u_1oplus u_2=x_0,quad
u_0oplus u_2=x_1,quad
u_1oplus u_2=x_2.
]

Thus the block transform is bijective and its product over disjoint blocks is a computable fair-coin-preserving homeomorphism.

A unit flip of (u_0,u_1,u_2) changes respectively raw coordinate sets ({x_0,x_1}), ({x_0,x_2}), and ({x_0,x_1,x_2}). Their Hamming weights are (2,2,3).

### 7. Destructive conjugate

Let (D,Y) be the settled P4-S011 destroyer and vulnerable computably random source. With (F=Dcirc H) and (X=H^{-1}(Y)):

- (Xin CR) by P4-S001;
- total computability and fair-coin preservation compose;
- (F^{-1}(z)=H^{-1}(D^{-1}(z))), so the fibre bound remains two;
- (F(X)=D(Y)
otin CR);
- every double fibre of (D) differs in one virtual coordinate, and the inverse block transform spreads that unit difference to two or three raw coordinates.

Therefore every double fibre of (F) violates one-hole scan coordinate-locality. An output homeomorphism is bijective and cannot change source fibres, so no output-homeomorphic one-hole representation exists.

This proves failure of literal map-level normalization but does not imply (Xin OH); accordingly no separation (R_2subsetneq OH) is claimed.

### 8. Null ambiguity

Source precomposition by a bijection preserves the output fibre cardinality at each output, hence (A_F=A_D). Since the constructed (F) is destructive, P4-S032's null-ambiguity theorem forces this common ambiguity locus to have positive measure. The record does not promote ambiguity mass to an invariant.

## Selection validation

The next task follows the exact obstruction rather than returning to a local bankroll question. Testing homeomorphism invariance of (OH) is necessary for (R_2=OH), and the explicit three-bit linear map supplies the smallest concrete non-coordinate case not covered by the signed-permutation theorem.

## Validation outcome

**PASS.**

Owner/external blocker: **NONE**.
