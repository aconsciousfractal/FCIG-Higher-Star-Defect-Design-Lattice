# Claim Ledger

This self-contained ledger maps each shipped claim to its evidence and scope.
The authoritative scope statement is `docs/PUBLIC_CLAIM_BOUNDARY.md`. The object
is the selected higher-star defect `Delta(D) = H_k / im_Z(A)` of a `t`-design
`D` with block size `k`.

Evidence is stated directly: **paper proof** means a proof in the cited
section, **imported theorem** means a classical result attributed in the paper
and `docs/SOURCE_LOCK.md`, and **exact finite replay** means a control produced
by `scripts/verify.py` and frozen in the certificate with SHA-256 prefix
`13BBF7B9`.

| ID | Evidence | Claim | Pointer | Scope caveat |
|---|---|---|---|---|
| HS | Paper proof; imported theorem | `d H_k <= im_Z(A) <= H_k`; `Delta` is finite, killed by `d`, has at most `v-1` generators, and has order dividing `d^(v-1)`; `0 -> Delta -> coker(A) -> Z/k -> 0`; `Delta = Tor coker(A+)` | Paper §2, Thm 2.1 | The star mechanism is Wilson's; the universal group and `t=2` case are Caggegi–Falcone–Pavone's. |
| GP | Paper proof; classical framework | `Delta = coker(C_x0)`; the parameter Gram matrix is `C_x0 C_x0^T`, with `det = alpha^(v-1) r/k`; `|Delta|^2` divides the determinant; the dual defect is isotropic in the bilinear discriminant form | Paper §3, Prop 3.1 | Explicit pairing and saturation proof; bilinear only. The overlattice framework is classical. |
| DP/WI | Paper proof; imported theorem | Good-prime decomposition; odd valuation-one Witt bound `mu(Delta_p) <= m` (or `m-1` when `n=v-1` is even); strict on the infinite `S(2,5,5+60t)` family | Paper §4, Prop 4.1 and Thm 4.2 | Witt classification is classical; the existence carriers are Hanani's. |
| XD | Paper proof; imported theorem | Exceptional-prime `alpha D_(n-2)` plus explicit rank-three `C_p`; binary valuation-one case is symplectic | Paper §4, Thm 4.3 | Jordan theory is classical (Conway–Sloane). |
| XI | Elementary paper proof | For every nonsingular symmetric bilinear finite 2-group `E`, `maxiso(E)=2^floor(log2(|E|)/2)`. Applied to the pointed group, binary isotropy gives no further subgroup-order bound; the plateau product equality holds exactly. | Paper §4, Lem 4.4 and Cor 4.5 | General bilinear fact, not a design-specific novelty claim; no classification of embeddable subgroup types or quadratic refinements. Metabolic need not mean hyperbolic. |
| V2 | Paper proof; imported theorem | In the symmetric case with `v_p(k-lambda)=2`, `Delta_p = (Z/p)^(v+1-2rho) + (Z/p^2)^(rho-1)` | Paper §5, Thm 5.1; `PG(2,4)` calibration | The `PG(2,p^2)` calibration is Chandler–Sin–Xiang's. |
| SEP | Paper proof; exact finite replay | `PG(3,2)` and the Bose `STS(15)` share parameters `2-(15,3,1)` but have defects `(Z/2)^4` and `0` | Paper §5, Thm 5.2; `scripts/verify.py` | The binary-rank landscape is classical. |
| STS15 | Paper proof; imported theorem | Complete `STS(15)` spectrum `Delta = (Z/2)^a`, `0 <= a <= 4`; every STS defect is pure-2, pure-3, or zero; ternary augmentation splits | Appendix A, Thm A.1 and Prop A.2 | Ranks are imported from Assmus–Key; the code/lattice classification is Solé's. |
| PT | Paper proof | Under a Pasch switch, local four-block lattices have index two; odd-primary `Delta` is preserved, the order ratio lies in `{1/2,1,2}`, and binary generator counts differ by at most one | Paper §6, Thm 6.1 | Uses the classical switching operation. |
| ER | Paper proof; imported bounds and asymptotics | Every fixed `(Z/2)^a` and `(Z/3)^c` occurs for every sufficiently large exponent in orders `2^h-1` and `3^h` respectively | Appendix B, Thm B.1 | JT exact-rank bounds plus Keevash/Ferber–Jain–Sudakov counting inputs. The moving-parameter positivity comparison is supplied here. Ternary incidence deficiency is `c+1`; threshold not effective. |
| HU | Paper proof; imported theorem | `Delta(H(q)) = (Z/(q+1))^(q^2-q)`; in particular `Delta(H(4)) = (Z/5)^12` | Paper §7 | The Smith row is Hiss's; the construction is Key's. |

## Non-claims

- The deductions proved here are identified separately from imported results;
  the source search establishes no priority or firstness certificate.
- No externally posed open question is claimed to be solved.
- Only bilinear discriminant isotropy is asserted; no `2`-adic quadratic
  (Arf/oddity) refinement is claimed.
- No nonsquarefree-exponent or general defect-group realizability claim is made.
- The relation kernels `ker_Z(A)` are outside the scope of every claim.
