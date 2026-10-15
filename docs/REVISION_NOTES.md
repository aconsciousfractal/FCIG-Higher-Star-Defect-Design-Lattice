# Manuscript revision 1.0.1, 2026-10-15

This revision follows the historical `v1.0.0` snapshot. Version numbers here
identify the companion package; archive deposits have their own identifiers.

1. **Binary bilinear comparison corrected.** The earlier statement that the
   plateau product equality could fail was false. A general elementary lemma
   now proves `maxiso(E)=2^floor(log2(|E|)/2)` for any nonsingular symmetric
   bilinear finite 2-group. The equality holds; there is no extra binary
   subgroup-order obstruction beyond square divisibility. Metabolicity is
   distinguished from hyperbolicity and from subgroup-type classification.
2. **Elementary realization proof completed.** Appendix B now displays the
   Jungnickel–Tonchev exact-rank difference bounds in the required moving
   regime and proves eventual positivity using the stated counting inputs.
   The ternary incidence deficiency is correctly `c+1` for selected defect
   `(Z/3)^c`. The earlier proof omitted this comparison and conflated these
   deficiencies; the final realization statement is retained.
3. **Attribution repaired.** The star identity is linked to Wilson 1982 and
   its checked reproduction, separately from Wilson's 1990 diagonal form.
   Counting-design and one-factorization inputs are cited explicitly; Li Xu's
   initial is corrected. Classical design applications of Witt theory are
   acknowledged.
4. **Proof and scope clarified.** The saturation pairing, inverse Gram matrix,
   and local Pasch exchange are explicit. The introduction distinguishes the
   selected-design deductions, elementary consequences, and imported examples.
   Reproducibility text distinguishes Smith computation from minor enumeration.
5. **AI disclosure added** in the manuscript and `AI_USE.md`. The fixed finite
   verifier and its expected certificate are unchanged. The manifest covers
   this revision, including the rebuilt PDF, rather than the historical PDF.

The review found no remaining actionable error in its inspected proof chain
after these corrections. It was AI-assisted and bounded, not independent
specialist or formal verification; the source record retains its access gaps.

## Reader-oriented restructuring

The same mathematical revision has been reorganized for reading. The contents
page is removed. The introduction now explains the quotient before presenting
its results, related work and notation in separate short sections. The local
prime cases and supporting appendices have clearer headings; the four finite
controls are collected in a table. A4 layout, Latin Modern fonts and microtype
match the recent manuscript format. The theorem sequence, proof obligations,
source boundaries and AI disclosure are preserved.

## Final proof reading and publication preparation

A further GPT-6 Astra review found no blocking error in the inspected proof
chain. Two elementary steps are now spelled out: the congruence of the Gram
matrix to the constant matrix at odd valuation-one primes, and the binary
generator bound from the common Pasch quotient. The theorem statements and
finite certificates are unchanged. The manuscript disclosure names the
revision reviewers separately from the original Codex assistance. The
manuscript is offered under CC BY 4.0, with the companion code under MIT;
see `LICENSE_SCOPE.md`.
