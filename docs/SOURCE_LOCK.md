# Sources and theorem-import boundary

The finite controls are constructed from scratch; no external dataset is
bundled or required. The general arguments use the mathematical inputs below.
Matrix conventions are point-by-block in this paper; a source using
block-by-point incidence must be transposed.

## Higher incidence and the universal group

- R. M. Wilson, *Incidence matrices of t-designs*, Linear Algebra Appl.
  **46** (1982), 73–82, [DOI](https://doi.org/10.1016/0024-3795(82)90027-1),
  owns the higher-incidence identity underlying the star-vector count.
  The original full text was not inspected. An accessible primary
  reproduction is M. Kiermaier and A. Wassermann, *Higher incidence matrices
  and tactical decomposition matrices*, Glasnik Mat. **58(78)** (2023),
  181–200, [DOI](https://doi.org/10.3336/gm.58.2.03),
  [published PDF](https://hrcak.srce.hr/en/file/450584), Section 2.2,
  printed p.184, equation (2.1), for `e+f<=t`. Specializing `e=1,f=j`
  gives the star identity used here. The integer Bezout combination of
  the star differences is proved in the paper.
- Wilson's *A diagonal form for the incidence matrices of t-subsets vs.
  k-subsets*, European J. Combin. **11** (1990), 609–615,
  [DOI](https://doi.org/10.1016/S0195-6698(13)80046-7), is a distinct
  complete-subset incidence result, cited for context; it is not the direct
  source of the selected-design star identity.
- A. Caggegi, G. Falcone and M. Pavone, *On the additivity of block
  designs*, J. Algebraic Combin. **45** (2017), 271–294,
  [DOI](https://doi.org/10.1007/s10801-016-0707-5),
  [institutional open postprint](https://iris.unipa.it/handle/10447/201793),
  Definition 2.1 and Theorem 2.2, define the universal group `coker(A)`
  and give the `t=2` point-difference relation. These portions of the
  postprint were inspected. Its embedding/additivity questions require
  point injectivity, which is not established by the bounds here.

## Bilinear forms and design obstructions

- C. T. C. Wall, *Quadratic forms on finite groups, and related topics*,
  Topology **2** (1963), 281–298,
  [DOI](https://doi.org/10.1016/0040-9383(63)90012-0), and V. V. Nikulin,
  *Integral symmetric bilinear forms and some of their applications*,
  Math. USSR-Izv. **14** (1980), 103–167,
  [DOI](https://doi.org/10.1070/IM1980v014n01ABEH001060),
  [source record](https://www.mathnet.ru/eng/im1677), supply the classical
  finite-form/discriminant framework. Their original full texts were not
  fully inspected. The paper uses bilinear saturation isotropy, not an
  even-lattice quadratic-isotropy import; its binary order lemma has an
  elementary proof.
- K.-U. Schmidt, *Symmetric bilinear forms over finite fields with
  applications to coding theory*, [primary PDF](https://arxiv.org/pdf/1410.7184),
  is the finite-field classification reference. J. H. Conway and
  N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed. (1999),
  is the local Jordan/type-I/type-II reference.
- R. M. Wilson, *Codes and modules associated with designs and t-uniform
  hypergraphs: Abstract and summary*,
  [lecture summary PDF](https://www.math.uniri.hr/NATO-ASI/abstracts/wilson.pdf),
  Sections 5–6, Theorems 5.2, 6.1 and 6.2, explicitly records the classical
  determinant/Witt criterion and earlier design applications of Lander and
  Calderbank. Those sections were inspected. The explicit pointed-Gram
  specialization in this paper does not introduce Witt theory to designs.

## Exact carriers, ranks, and realization

- H. Hanani, *On balanced incomplete block designs with blocks having five
  elements*, JCTA **12** (1972), 184–201,
  [DOI](https://doi.org/10.1016/0097-3165(72)90035-0), supplies the exact
  `S(2,5,v)` existence input. The original abstract, but not the original
  full proof, was inspected. An explicit primary reproduction is
  Y. Fujiwara et al., *Entanglement-assisted quantum low-density parity-check
  codes*, Phys. Rev. A **82** (2010), 042338,
  [PDF](https://arxiv.org/pdf/1008.4747), Appendix A, p.19, Theorem 50,
  reference [66]. The nontrivial conditions are `v>=21`, `v=1,5 mod20`;
  the size boundary is also explicit in M. Kiermaier et al.,
  [*Some new Steiner designs S(2,6,91)*](https://arxiv.org/pdf/2504.04293), p.2.
  Thus `v=5+60h`, `h>=1`, is covered. The extra restriction `3` not dividing
  `h` in the Witt application is a valuation condition, not an existence
  exception.
- D. Jungnickel and V. D. Tonchev, *Counting Steiner triple systems with
  classical parameters and prescribed rank*, JCTA **162** (2019), 10–33,
  [DOI](https://doi.org/10.1016/j.jcta.2018.09.009),
  [primary PDF](https://arxiv.org/pdf/1709.06044), Theorems 4.4 and 4.12
  (PDF pp.19–20 and 24), supply the ternary and binary exact-rank difference
  bounds, under `2<=t<=h-1` after renaming their `n` as `h`. These formulas
  were inspected. Appendix B proves their eventual positivity after
  `t=h-c` or `h-a`; the all-sufficiently-large-orders conclusion is not
  imported from the source abstract. Ternary selected dimension `c`
  corresponds to incidence rank `v-1-c`, with mandatory deficiency `c+1`.
- P. Keevash, *Counting designs*, JEMS **20** (2018), 903–927,
  [DOI](https://doi.org/10.4171/JEMS/779),
  [author PDF](https://people.maths.ox.ac.uk/keevash/papers/count-designs.pdf),
  Theorem 2.2 (PDF p.2), supplies the labeled STS asymptotic. This is
  distinct from *The existence of designs*, arXiv:1401.3665.
- A. Ferber, V. Jain and B. Sudakov, *Number of 1-factorizations of regular
  high-degree graphs*, Combinatorica **40** (2020), 315–344,
  [DOI](https://doi.org/10.1007/s00493-019-3970-y),
  [author-hosted published PDF](https://people.math.ethz.ch/~sudakovb/counting-1factors.pdf),
  Theorem 1.2 and the introduction, printed pp.316–318, supply the
  complete-graph one-factorization asymptotic and recall the permanent-bound
  Latin-square estimate. The stated portions of this source and Keevash's
  counting source were inspected. Factor-order conventions change the
  logarithms by only `O(q log q)` in Appendix B's comparison.
- J. Doyen, X. Hubaut and M. Vandensavel, *Ranks of incidence matrices of
  Steiner triple systems*, Math. Z. **163** (1978), 251–259,
  [DOI](https://doi.org/10.1007/BF01174898), gives the classical
  other-prime full-rank boundary (unnumbered theorem, p.252).
  M. Shi, **L. Xu** and D. S. Krotov, *The number of the non-full-rank
  Steiner triple systems*, J. Combin. Des. **27** (2019), 571–585,
  [DOI](https://doi.org/10.1002/jcd.21663),
  [primary PDF](https://arxiv.org/pdf/1806.00009), Theorem 5.1 in this
  version (PDF p.12), excludes simultaneous non-full binary and ternary
  ranks for `v>3`. The latter statement was inspected.

## Geometric Smith forms and finite spectra

| Input | Source and boundary |
|---|---|
| Projective/affine incidence invariant factors | D. B. Chandler, P. Sin and Q. Xiang, *TAMS* **358** (2006), 4935–4957, [DOI](https://doi.org/10.1090/S0002-9947-06-03859-1). Source-owned calibration. |
| Miquelian/even-order Möbius Smith forms | C. Ringe, *Über die Elementarteiler der Inzidenzmatrix des Ree-Unitals*, dissertation (2008), Chapter 8. The paper's general vanishing deduction is separately proved. |
| Hermitian unital Smith group | G. Hiss, *Indag. Math.* **15** (2004), 223–243, [DOI](https://doi.org/10.1016/S0019-3577(04)90016-X), [author PDF](https://www.math.rwth-aachen.de/~Gerhard.Hiss/Preprints/u3q.pdf), Conjecture 2.2 and unconditional Corollary 7.2, PDF pp.12–13; inspected with Sections 2, 5–7. Applies to the classical unital for prime-power `q`. The selected group here only removes one augmentation factor. |
| Explicit classical unital construction | J. D. Key, *J. Symbolic Comput.* **31** (2001), 37–53, [DOI](https://doi.org/10.1006/jsco.1999.1007). The construction and Smith row are not new computations of this paper. |
| STS(15) ranks and code/lattice classification | E. F. Assmus and J. D. Key, *TAMS* **330** (1992), 269–293, [DOI](https://doi.org/10.1090/S0002-9947-1992-1055565-6); V. D. Tonchev and R. S. Weishaar, *J. Statist. Plann. Inference* **58** (1997), 207–216; P. Solé, *Electron. J. Combin.* **4** (1997), R6, [DOI](https://doi.org/10.37236/1291). Imported finite rank/classification facts, translated to the selected group. |

The complete-carrier integral/null-design theory of Graver–Jurkat and
Graham–Li–Li is contextually distinct from a selected design's point-column
image. Later additive-design work of Buratti–Nakić and
Buratti–Merola–Nakić concerns zero-sum embeddings; its ambient groups are not
identified with the selected quotient by citation alone.

The access notes above identify checked statements, not full verification of
every source or every proof. Several originals and books were not read in
full, and the literature comparison is not exhaustive. The MIT license
covers the authors' code and documentation here, not the cited works.
