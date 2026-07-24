# Red-team summary

## Internal review provenance

The mathematics has undergone extensive internal adversarial review during
development, including:

- an end-to-end proof reconstruction of the whole spine (definitions through
  Pasch transport);
- a theorem-level primary-source audit that narrowed the contribution to the
  selected-design `Delta` package and demoted every classical ingredient to its
  attributed owner;
- a multi-lane package-level review (mathematics, source/prior-art, claim
  architecture) that found no central theorem error;
- independent reconstructions and exact certificates for the finite controls
  (the `SQS(8)` defect, the `PG(3,2)`/Bose separation, the valuation-two
  control, and the Steiner-triple spectrum).

## This package

`scripts/verify.py` reconstructs the self-contained finite controls from scratch
and computes the Smith forms with `python-flint`, cross-checking the binary and
ternary ranks by an independent modular route; the cross-check is **enforced**
(a disagreement aborts the run), and when the frozen certificate is present the
run also asserts byte-identity against it. The certificate is byte-identical
under `python` and `python -O`. The proofs of the general theorems (Sections
2–4, 6–7) use no finite census.

## Documentary review of the built package

A documentary red team of this built package (distinct from the internal
mathematics review above) was carried out across four lanes — proof text,
source/prior-art attribution, claim architecture, and packaging/reproducibility.
Its findings were remediated in place:

- **Proof text.** The `Delta`-sandwich proof (Theorem 2.1) was corrected to the
  `d k\,e_o \in L` step and the correct `(Z/d)^{v-1}` quotient mechanism; the
  omitted proofs of the good-prime decomposition, the exceptional-prime
  reduction (with the `D_{n-2}` root block), and the valuation-two formula were
  supplied; the residual `maxiso` equality was demoted to the one-sided bound
  actually used.
- **Attribution.** The bibliography was rebuilt and then **fully finalized**
  against primary sources (Wilson DOI; Tonchev–Weishaar JSPI 58; Key JSC 31; Hiss
  Indag. Math. 15; Solé EJC 4 #R6; Shi–Xu–Krotov JCD DOI; Jungnickel–Tonchev JCTA
  162; and Christian Ringe, *Über die Elementarteiler der Inzidenzmatrix des
  Ree-Unitals*, RWTH Aachen 2008). No `[to be finalized]` placeholders remain.
- **Packaging/reproducibility.** The PDF build was made timestamp-free and
  title-named; `MANIFEST_SHA256.txt` now pins the LaTeX source and verifier but
  neither the compiled PDF (TeX-toolchain-dependent) nor `results/`
  (regenerated); the verifier's modular cross-check and frozen-certificate
  self-check were made load-bearing; the divergent unused `refs.bib` was removed
  (the bibliography is inline).

## Open items

- The prior-art positioning is a **dated negative search**: no exact prior
  equivalent of the combined selected-design `Delta` package was located, but
  the original Wilson and Graver–Jurkat texts were not all inspected in full;
  this is recorded as a caveat, not a priority claim.
- A second external red team (2026-07-23) was adjudicated and remediated: the
  Cauchy–Binet square bound, the corrected exceptional base vector, the ternary
  augmentation-splitting proof (Prop A.2), the corrected Pasch statement (local
  four-block lattices; the `2m`-cycle generalization removed), the
  `binom(14,8)=3003` `SQS(8)` count, the `n`-vs-`w` symmetric-order disambiguation,
  the abstract's discriminant-form scoping, and the finalized Ringe reference.
  No bibliography placeholders remain; publish stays owner-gated.
