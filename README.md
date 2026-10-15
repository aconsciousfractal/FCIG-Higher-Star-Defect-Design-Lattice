# The Selected Higher-Star Defect of a Design Incidence Lattice

Companion package for the paper

> **The Selected Higher-Star Defect of a Design Incidence Lattice**
> Oleksiy Babanskyy, 2026.

PDF: [`paper/The_Selected_Higher-Star_Defect_of_a_Design_Incidence_Lattice.pdf`](paper/The_Selected_Higher-Star_Defect_of_a_Design_Incidence_Lattice.pdf)
(built from `paper/main.tex` + `paper/sections/`; see
[`REPRODUCE.md`](REPRODUCE.md)). This tree contains the **2026-10-15
manuscript revision** (`1.0.1`); see
[`docs/REVISION_NOTES.md`](docs/REVISION_NOTES.md). The earlier
[`v1.0.0`](https://github.com/aconsciousfractal/FCIG-Higher-Star-Defect-Design-Lattice/releases/tag/v1.0.0)
snapshot is historical and does not contain these corrections. The current
13-page manuscript uses the revised reader structure: no contents page, a
short introduction organized by results and prior work, separate local-prime
cases, and a table of finite controls.

## What the paper proves

For a `t`-design `D` with point-by-block incidence matrix `A` and block size
`k`, the **selected higher-star defect** is
`Delta(D) = H_k / im_Z(A)`, where `H_k = { z in Z^P : sum(z) = 0 mod k }`.
Writing `d = gcd{ lambda_j - lambda_{j+1} }` over the star vector:

- **Finiteness and bounds.** `d·H_k <= im_Z(A) <= H_k`, so `Delta(D)` is finite,
  killed by `d`, on at most `v-1` generators, of order dividing `d^(v-1)`; it is
  the torsion of the retained-apex cokernel and fits
  `0 -> Delta(D) -> coker(A) -> Z/k -> 0`.
- **Presentation and Gram matrix.** A pointed presentation gives
  `Delta(D) = coker(C_x0)`; the Gram matrix `C_x0 C_x0^T` depends only on the
  ordinary parameters, giving a square-order bound and a bilinear discriminant
  form into which the dual defect embeds isotropically.
- **Prime-by-prime obstruction.** A good-prime decomposition; an odd
  valuation-one **Witt obstruction** that strictly beats square divisibility on
  an infinite `S(2,5,v)` family; an exceptional-prime rank-three reduction; and,
  at the prime two, an elementary **general bilinear lemma** showing that
  isotropy gives no additional subgroup-order bound beyond rounded square
  divisibility. This does not classify isotropically embeddable subgroup types.
- **Fixed-parameter phenomena.** A valuation-two formula; a **same-parameter
  separation** of two `2-(15,3,1)` Steiner triple systems (`Delta = (Z/2)^4` for
  `PG(3,2)` vs `0` for the Bose system); and the complete `STS(15)` spectrum.
- **Operations and realization.** A Pasch transport law; every elementary
  `(Z/2)^a` and `(Z/3)^b` realized by infinitely many STS.
- **Applications.** Finite Moebius planes (`Delta = 0`, form `1^(q^2)(q+1)`),
  `SQS(8)` (`Delta = (Z/2)^3`), and Hermitian unitals
  (`Delta(H(q)) = (Z/(q+1))^(q^2-q)`).

## What is and is not claimed

The classical ingredients are attributed in the paper — Wilson (higher-incidence
identities, 1982; distinct complete-subset diagonal form, 1990), Caggegi–Falcone–Pavone
(universal group, `t=2`), Chandler–Sin–
Xiang (projective/affine Smith forms), Ringe (Moebius forms), Wall / Nikulin
(finite/discriminant forms), Hanani (`S(2,5,v)` carriers), Hiss (Hermitian
divisors), Assmus–Key (order-16 ranks), Solé (`STS(15)` code/lattice), and
Jungnickel–Tonchev with Keevash and Ferber–Jain–Sudakov (rank counts and counting
asymptotics).

The deductions developed here include the explicit pointed Gram analysis,
the determinant-class-`k` bound, the exceptional rank-three block, the Pasch
quotient law, and the moving-parameter comparison for elementary realization.
The star gcd argument is elementary, the binary order lemma is a general
bilinear fact, and the geometric applications use known Smith forms. No
priority certification or resolution of an externally posed open question is
claimed. See the [claim boundary](docs/PUBLIC_CLAIM_BOUNDARY.md) and
[source record](docs/SOURCE_LOCK.md).

The work involved substantial mathematical, coding, and writing assistance
from OpenAI Codex. The manuscript and [`AI_USE.md`](AI_USE.md) disclose the
role and limits of this assistance. The general proofs have not received
independent specialist or formal verification.

## How to verify

`scripts/verify.py` reproduces the self-contained finite controls from scratch
(no external data): `SQS(8)`, the `PG(3,2)`/Bose separation, and `M(2)`. See
[`REPRODUCE.md`](REPRODUCE.md).

## Layout

```text
paper/         main.tex, macros.tex, sections/01..11 (7 main + 4 appendix), <title>.pdf
scripts/       verify.py (finite controls; python-flint + independent modular ranks)
               verify_public_package.py (fail-closed inventory/metadata checker)
certificates/  frozen expected certificate
results/       verification.json (produced by verify.py)
docs/          CLAIM_LEDGER.md, PUBLIC_CLAIM_BOUNDARY.md, SOURCE_LOCK.md, REVISION_NOTES.md
LICENSE (MIT), LICENSE_MANUSCRIPT.md (CC BY 4.0), LICENSE_SCOPE.md
CITATION.cff, MANIFEST_SHA256.txt, requirements.txt
```

`LICENSE_SCOPE.md` records the manuscript/code license map and the citation-only
third-party boundary; this package embeds no external source or data.

The bibliography is an inline `thebibliography` in `main.tex` (no `bibtex`
pass). `MANIFEST_SHA256.txt` pins the exact shipped inventory, including the
compiled PDF and replay result. Run `python scripts/verify_public_package.py`
to check every hash, revision metadata, retired-path absence, and certificate
byte identity.
