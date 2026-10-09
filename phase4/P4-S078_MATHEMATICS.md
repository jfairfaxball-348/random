# P4-S078 — Single infinite-support shear criterion and three-step committed-X witness reduction

Date: 2026-10-09
Session: P4-S078; Phase 4 Mathematics ONLY; selected CAND-01.
Incoming live remote main: `178948859e2cf6853a90bbb36fcb8837bf59292b` (independently verified at start).
Disposition: **PROVED a new global equivalence reducing all computable infinite supported shears / H-preservation to ONE fixed all-block shear, and an exact three-candidate reduction for the committed X. Neither the fixed shear's preservation nor nonpreservation is determined; X in OH and R₂=OH remain unresolved.**

## 0. Authority and incoming reconciliation

Live `main` exactly matched the P4-S077 outgoing checkpoint; recursive tree showed precisely 77 consecutive mathematics/validation/close triplets and NO S078 record. Reviewed the mathematics results in P4-S001–S077, S077 validation/close, selected P3-S007 CAND-01, P3-S008 Gate-3 PASS and both active Phase-4 pivots. Emphasized S011/S012, S032–S044, S057, S069–S077, particularly S033's OH signed-permutation invariance and R₂ homeomorphism invariance, S037's effective retirement bound, S070's support-family equivalence, S071's arbitrary spoiled-wager exposure, and S077's all-observer finite-support transfer. No previous proof is revised.

Retain `MLR ⊆ R₂ ⊆ OH^iso ⊆ OH ⊊ CR`. Preserve ORIGINAL CR `Y`, exact syntactically self-avoiding globally use-clipped wtt autoreduction `M`, repeated three-bit `H` (matrix `A=[101;110;111]`), and `X=H⁻¹(Y)` with `H(X)=Y∉OH`. Previously established `X∉R₂` and `X∉OH^iso` remain frozen. Membership `X∈OH` is NOT established. `R₂=OH^iso` remains a logically separate question.

## 1. Main new global algebraic bridge: a single infinite shear suffices

Use S070's exact definitions on each block `B_j={3j,3j+1,3j+2}`. Let `S=S_ℕ` be the ONE fixed computable all-block shear `(a,b,c)↦(a,b xor c,c)`. For any decidable block set `E`, let `Q_E` swap raw coordinates `3j+1` and `3j+2` exactly in blocks in `E`, and fix all other coordinates. Each `Q_E` is a computable coordinate permutation, hence an OH-automorphism by S033. All these maps preserve fair coin and have computable inverses.

**Theorem 1 (two-copy supported-shear identity, all Cantor sources).** For every computable `E`,

    S_E = Q_E ∘ S ∘ Q_E ∘ S ∘ Q_E.                      (1)

Proof. On an unselected block `Q_E=I`, so the right-hand side is `S²=I`, as required. On a selected block restrict to the coordinates `(b,c)` and write

    s = [[1,1],[0,1]],    q = [[0,1],[1,0]]   over F₂.

Direct exact multiplication gives `q s q s q = s`. The first coordinate `a` is fixed throughout. Thus (1) holds independently on every block, including arbitrary infinite computable E. The word has exactly two copies of the same global infinite-support S and three computable coordinate-permutation factors, with NO truncation, limiting process, infinite product of bets, or computable modulus requirement. QED.

**Theorem 2 (ONE-FIXED-MAP OH preservation criterion).** The following are equivalent:

(i) `∀z∈OH, S(z)∈OH` for the single fixed all-block shear S;
(ii) `∀E⊆ℕ decidable ∀z∈OH, S_E(z)∈OH`;
(iii) `∀z∈OH, H(z)∈OH` for the exact committed H;
(iv) OH is preserved by all computable blockwise `GL(3,F₂)` recodings.

Proof. (i) implies (ii) by (1): each Q_E preserves OH and two uses of the hypothesized S-preservation suffice. (ii) implies (i) by choosing E=ℕ. S070 Theorem 3 already proves the equivalence of (ii), (iii), and (iv); its algebraic premises and direction of implication are preserved. Because S is an involution, one-way preservation in (i) also gives invariance of OH under S. There is NO extension to arbitrary computable homeomorphisms or proof of (i). QED.

**Corollary 3 (two explicit full-shear counterexample candidates).** Suppose an actual computably random `z∈OH` and decidable E satisfy `S_E(z)∉OH`. Put `z0=Q_E(z)` and `z2=Q_E(S(z0))`. If `S(z0)∉OH`, then `(z0,S(z0))` witnesses failure of (i). Otherwise `S(z0)∈OH`, so `z2∈OH`, while equation (1) yields `Q_E(S(z2))=S_E(z)∉OH`. Since Q_E preserves OH both ways, `S(z2)∉OH`; hence `(z2,S(z2))` witnesses failure of (i). All candidate sources are CR because Q_E and S preserve CR. This is a finite existential extraction; deciding which candidate belongs to OH is not asserted computable.

Consequently the remaining supported-shear invariance problem has a single fixed infinite E=ℕ. Finite/coinfinite support distinctions and support search are not needed for the universal claim. This genuinely strengthens S070's equivalence with a UNIVERSAL family; S077's finite-support theorem alone cannot give (1) or preservation of S. The fixed S still has infinitely many potentially spoiled w wagers, so S071's exposure gap remains.

## 2. An explicit three-shear factorization of committed H

Let `R` swap coordinates `(a,b)` in EVERY three-bit block, `Q` swap `(b,c)` in EVERY block, and let S be the fixed all-block shear above. R and Q are computable signed coordinate permutations, thus OH-automorphisms by S033.

**Lemma 4 (exact eight-factor word).** With operations read chronologically LEFT TO RIGHT,

    R → S → Q → R → S → Q → R → S

has composite exactly H. Equivalently, under the standard right-to-left convention,

    H = S ∘ R ∘ Q ∘ S ∘ R ∘ Q ∘ S ∘ R.             (2)

Proof. On the coordinate column `(a,b,c)^T`, matrices of R, Q and S have row encodings respectively `[010;100;001]`, `[100;001;010]`, `[100;011;001]`. Successive left multiplication from the identity in the chronological order in (2) gives the row matrices:

    010/100/001, 010/101/001, 010/001/101,
    001/010/101, 001/111/101, 001/101/111,
    101/001/111, 101/110/111.

The last is exactly the unchanged committed `A=[101;110;111]`. Blockwise repetition proves (2) on all infinite sources. QED.

**Corollary 5 (THREE explicitly specified possible full-shear witnesses from X).** Define a fixed chain on the original committed X:

    z0=R(X); z1=S(z0); z2=Q(z1); z3=R(z2);
    z4=S(z3); z5=Q(z4); z6=R(z5); z7=S(z6)=Y.

If `X∈OH`, then at least one of the THREE concrete pairs `(z0,z1)`, `(z3,z4)`, `(z6,z7)` witnesses a source in OH sent outside OH by the SAME fixed S. Proof: `z0∈OH` by S033; each of Q,R preserves OH; `z7=Y∉OH`. Take the first transition in this finite chain that exits OH. It cannot be Q or R; it must be one of the three S transitions. This does NOT show X∈OH and does NOT choose an OH witness without that missing premise.

Conversely if (i) holds, (2) gives H-preservation, whence the settled Y=H(X)∉OH implies `X∉OH`. Neither implication settles `R₂=OH`; failure of (i) WITH AN ACTUAL OH SOURCE does settle `R₂⊊OH` by S033 R₂ homeomorphism invariance.

## 3. Direct-route assessment and missing infinitary lemma

**Central-target progress:** the full S070 universal shear/H-preservation problem is EQUIVALENT to preservation under one concrete computable involution S, with an explicit two-application reduction for any E and only three S calls on the exact X→Y chain. This is a global all-OH-source assertion and a substantive quantifier reduction, not merely a restriction on a compiler, finite financial arithmetic or a negative method result.

**Still missing global implication:** prove or refute `∀z∈OH S(z)∈OH`, namely: for every computably random source robust against ALL globally legal raw one-hole scans, applying the single all-block shear remains robust against ALL such scans. A proof must handle arbitrarily late spoiled virtual wagers with partial computation and infinite cumulative exposure, or use a different global invariance argument. A refutation must exhibit an actual `z∈OH` and one globally legal scan/martingale destroying `S(z)`; such a witness proves `R₂⊊OH`. Alternatively prove X membership directly; Corollary 5 then localizes the witness.

**Approaches rejected as insufficient:** (a) limit S077's finite-support theorem as the number of blocks grows; its `2^|F|` loss is unbounded and no single raw witness is produced; (b) treat algebraic equivalence as proving either direction of preservation; (c) claim the failed S071 spoiled-stake compiler shows no other global raw scan exists; (d) use computably retiring S037/S072–S076 examples to infer arbitrary non-effectively retiring cases; (e) use target-only halting/nonhalting knowledge, two permanent raw holes or an assumed source recurrence. No raw scan or martingale compiler is claimed by the algebraic proof.

## 4. Validation and disposition

Algebraic 2x2 calculation `q s q s q=s` and `s²=I` is exact, not experimental. Independently exhaustive exact audit: 16 support patterns × 4096 raw assignments on four triples = 65,536 comparisons of both sides of (1), ZERO discrepancies. Breadth-first generation by the three local matrices S,Q,R reaches all 168 elements of `GL(3,F₂)`, and shortest-word extraction gives the exact eight-factor word (2); its eight intermediate row matrices were checked directly. Computational checks supplement the finite proofs and DO NOT test OH membership, global scan legality, infinite support analytically, or an actual source witness.

Freeze all P4-S001–S077 mathematics, including S037 renewal, S073 `LFΠ=dA`, S074 sharp 3/16, S075 savings mirrors, S076 multistage financing, S077 finite-support invariance; original Y/M/H/X and exact S057 four paired clipped traces, prospective deadlines, real fillers, t/u ZERO timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 vs one ZERO terminal payoffs are unchanged; S057 was NOT invoked.

PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker NONE. Next P4-S079 should attack the **single fixed S=S_ℕ** directly, rather than searching E or restarting finite pricing.
