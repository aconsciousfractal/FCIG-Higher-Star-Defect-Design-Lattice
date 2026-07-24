# The Selected Higher-Star Defect of a Design Incidence Lattice

Companion package for the paper

> **The Selected Higher-Star Defect of a Design Incidence Lattice**
> Oleksiy Babanskyy, 2026.

PDF: [`paper/`](paper/) (title-named, built from `paper/main.tex` +
`paper/sections/`; see [`REPRODUCE.md`](REPRODUCE.md)).

## What the paper proves

For a `t`-design `D` with point-by-block incidence matrix `A` and block size
`k`, the **selected higher-star defect** is
`Delta(D) = H_k / im_Z(A)`, where `H_k = { z in Z^P : sum(z) = 0 mod k }`.
Writing `d = gcd{ lambda_r - lambda_{r+1} }` over the star vector:

- **Finiteness and bounds.** `d·H_k <= im_Z(A) <= H_k`, so `Delta(D)` is finite,
  killed by `d`, on at most `v-1` generators, of order dividing `d^(v-1)`; it is
  the torsion of the retained-apex cokernel and fits
  `0 -> Delta(D) -> coker(A) -> Z/k -> 0`.
- **Presentation and envelope.** A pointed presentation gives
  `Delta(D) = coker(C_x0)`; the Gram matrix `C_x0 C_x0^T` depends only on the
  ordinary parameters, giving a square-order bound and a bilinear discriminant
  form into which the dual defect embeds isotropically.
- **Prime-by-prime obstruction.** A good-prime decomposition; an odd
  valuation-one **Witt obstruction** that strictly beats square divisibility on
  an infinite `S(2,5,v)` family; an exceptional-prime rank-three reduction; and,
  at the prime two in higher valuation, a **metabolicity theorem** — the growing
  constituent is always split, so no binary analogue of the odd-prime
  obstruction grows with `v`.
- **Fixed-parameter phenomena.** A valuation-two formula; a **same-parameter
  separation** of two `2-(15,3,1)` Steiner triple systems (`Delta = (Z/2)^4` for
  `PG(3,2)` vs `0` for the Bose system); and the complete `STS(15)` spectrum.
- **Operations and realization.** A Pasch transport law; every elementary
  `(Z/2)^a` and `(Z/3)^b` realized by infinitely many STS.
- **Applications.** Finite Moebius planes (`Delta = 0`, form `1^(q^2)(q+1)`),
  `SQS(8)` (`Delta = (Z/2)^3`), and Hermitian unitals
  (`Delta(H(q)) = (Z/(q+1))^(q^2-q)`).

## What is and is not claimed

The classical ingredients are attributed in the paper — Wilson (the higher-star
diagonal form), Caggegi–Falcone–Pavone (universal group, `t=2`), Chandler–Sin–
Xiang (projective/affine Smith forms), Ringe (Moebius forms), Wall / Nikulin
(finite/discriminant forms), Hanani (`S(2,5,v)` carriers), Hiss (Hermitian
divisors), Assmus–Key (order-16 ranks), Solé (`STS(15)` code/lattice). **No
priority or firstness is claimed;** the contribution is the selected-design
`Delta` package assembled on top of these.

## How to verify

`scripts/verify.py` reproduces the self-contained finite controls from scratch
(no external data): `SQS(8)`, the `PG(3,2)`/Bose separation, and `M(2)`. See
[`REPRODUCE.md`](REPRODUCE.md).

## Layout

```text
paper/         main.tex, macros.tex, sections/01..11 (7 main + 4 appendix), <title>.pdf
scripts/       verify.py (finite controls; python-flint + independent modular ranks)
certificates/  frozen expected certificate
results/       verification.json (produced by verify.py)
docs/          CLAIM_LEDGER.md, PUBLIC_CLAIM_BOUNDARY.md, SOURCE_LOCK.md,
               RED_TEAM_REPORT.md, GATE_HISTORY.md
LICENSE (MIT), LICENSE_SCOPE.md, CITATION.cff, MANIFEST_SHA256.txt, requirements.txt
```

`LICENSE_SCOPE.md` records the (single-MIT) license map and the citation-only
third-party boundary; this package embeds no external source or data.

The bibliography is an inline `thebibliography` in `main.tex` (no `bibtex`
pass). `MANIFEST_SHA256.txt` pins the LaTeX source and the verifier, but not the
compiled PDF (TeX-toolchain-dependent) or `results/` (regenerated on replay).
