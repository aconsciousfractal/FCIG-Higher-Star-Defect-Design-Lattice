# Claim Ledger (public package)

One row per claim shipped with this package, with its verification pointer and
scope caveat. (Formatted for uniformity with the sibling FCIG notes; the
authoritative scope statement remains `docs/PUBLIC_CLAIM_BOUNDARY.md`.) The
object is the selected higher-star defect `Delta(D) = H_k / im_Z(A)` of a
`t`-design `D` with block size `k`.

Level column uses the official PAPP taxonomy
(Gate-Disciplined-Computational-Mathematics/docs/CLAIM_LEVELS.md): CL5 =
internal proof, CL4 = imported classical theorem, CL3 = exact finite
certificate. The *Verified by* column names the discharging route: a proof in
the numbered paper section, and/or a control in `scripts/verify.py` (frozen
certificate `13BBF7B9…`), and/or an imported source carried in
`docs/SOURCE_LOCK.md`.

| ID | Level | Claim | Verified by | Scope caveat |
|---|---|---|---|---|
| A-HS | CL5 | `d H_k <= im_Z(A) <= H_k`; `Delta` finite, killed by `d`, `<= v-1` gens, order `\| d^(v-1)`; `0 -> Delta -> coker(A) -> Z/k -> 0`; `Delta = Tor coker(A+)` | proof, paper §2 (Thm 2.1) | star mechanism is Wilson's; universal group / `t=2` is CFP's |
| A-GP | CL5 | `Delta = coker(C_x0)`; parameter Gram `C_x0 C_x0^T`, `det = alpha^(v-1) r/k`; `\|Delta\|^2 \| det` (Cauchy–Binet); dual defect isotropic in the bilinear discriminant form | proof, paper §3 (Prop 3.1) | bilinear isotropy only; overlattice duality is Nikulin's |
| A-DP/A-WI | CL5 + CL4 | good-prime decomposition; odd valuation-one Witt bound `mu(Delta_p) <= m` (or `m-1`, `n=v-1` even); strict on the infinite `S(2,5,5+60t)` family | proofs, paper §4 (Prop 4.1, Thm 4.2) | Witt classification classical; carriers are Hanani's |
| A-XD | CL5 | exceptional-prime `alpha D_(n-2)` + explicit rank-three `C_p`; binary valuation-one symplectic | proof, paper §4 (Thm 4.3) | Jordan theory classical (Conway–Sloane) |
| A-XI | CL5 | type-II `2^A`-modular planes metabolic (`A>=1`); binary higher-valuation isotropy defect confined to the rank-`<=3` residual, bounded independently of `v`; no `v`-growing binary discriminant-form obstruction | proofs, paper §4 (Lem 4.4, Thm 4.5) | finite-form theory is Wall's; other binary obstructions not excluded |
| A-V2 | CL5 | symmetric `v_p(k-lambda)=2`: `Delta_p = (Z/p)^(v+1-2rho) + (Z/p^2)^(rho-1)` | proof, paper §5 (Thm 5.1); `PG(2,4)` calibration | `PG(2,p^2)` calibration is CSX's |
| A-SEP | CL5 + CL3 | `PG(3,2)` and Bose `STS(15)`: same `2-(15,3,1)` parameters, `Delta = (Z/2)^4` vs `0` | proof, paper §5 (Thm 5.2) + `verify.py` cert | binary-rank landscape classical |
| A-STS15 | CL5 + CL4 | complete `STS(15)` spectrum `Delta = (Z/2)^a`, `0 <= a <= 4`; every STS defect pure-2 / pure-3 / zero; ternary augmentation splits | proof, App. A (Thm A.1, Prop A.2) + imported ranks | ranks imported (Assmus–Key); code/lattice classification is Solé's |
| A-PT | CL5 | Pasch switch: local four-block lattices index two; odd-primary `Delta` preserved, order ratio in `{1/2,1,2}`, binary generators differ `<= 1` | proof, paper §6 (Thm 6.1) | classical switching |
| A-ER | CL5 + CL4 | every `(Z/2)^a`, `(Z/3)^b` realized by infinitely many STS | proof, App. B (Thm B.1) + source-owned prescribed-rank counts | carriers/counts are Jungnickel–Tonchev (JCTA 162, 2019) |
| A-HU | CL4 + CL5 | `Delta(H(q)) = (Z/(q+1))^(q^2-q)`; `Delta(H(4)) = (Z/5)^12` | paper §7 + imported Smith row (Hiss) | Hiss owns the Smith row; Key owns the construction |

## Non-claims (standing)

- No priority, novelty, or firstness for any statement; dated negative searches
  are recorded as such, not as certificates.
- Bilinear discriminant isotropy only; no `2`-adic quadratic (Arf/oddity)
  refinement.
- No nonsquarefree-exponent or general defect-group realizability claim.
- The relation kernels `ker_Z(A)` are not part of any claim.
