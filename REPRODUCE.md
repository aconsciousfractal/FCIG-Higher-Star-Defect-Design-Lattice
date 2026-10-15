# Reproducing the finite controls

## Requirements

- Python 3.10+
- `python-flint` (exact Smith/Hermite normal forms): `pip install -r requirements.txt`
- The independent modular-rank cross-check uses only the standard library.
- No external data is needed: every design is constructed from scratch.

## Run

```bash
python scripts/verify.py \
    --output results/verification.json \
    --log results/verification.log
```

## Expected result

The run prints progress and ends in `PASS` (well under a second). It verifies:

1. `SQS(8) = AG(3,2)`: full incidence Smith form `1^4 2^3 4`, so
   `Delta = (Z/2)^3` (a nonzero `t=3` defect; `d=2`);
2. the same-parameter separation of two `2-(15,3,1)` systems: `PG(3,2)` has
   form `1^11 2^3 6` and `Delta = (Z/2)^4`, the Bose system has form `1^14 3`
   and `Delta = 0`;
3. the smallest finite Moebius plane `M(2) = 3-(5,3,1)`: form `1^4 3`,
   `Delta = 0`.

Each Smith form is computed with `python-flint`; the binary and ternary ranks
of the pointed presentation are cross-checked, and enforced, by an independent
modular route. `results/verification.json` is byte-identical under `python` and
`python -O`; when the frozen `certificates/expected_verification.json` is
present, the run additionally asserts byte-identity against it and prints a
`self-check` line. The certificate SHA-256 is

```
13BBF7B95BD9404CB6190F686BDD2D5FE31F53426B42D0E86D502DAA612BCCAE
```

## Check the manifest

`MANIFEST_SHA256.txt` pins the exact shipped inventory except the manifest
itself, including the LaTeX source, verifier, frozen and replayed certificates,
documentation, and canonical compiled PDF. The package checker fails closed on
missing, unexpected, or changed files:

```bash
python scripts/verify_public_package.py
```

```bash
# Linux/macOS:
sha256sum -c MANIFEST_SHA256.txt
# or, cross-platform:
python -c "import hashlib; \
[print('OK' if hashlib.sha256(open(p.strip(),'rb').read()).hexdigest().upper()==h.upper() else 'MISMATCH', p.strip()) \
 for h,p in (l.split(None,1) for l in open('MANIFEST_SHA256.txt') if l.strip() and not l.startswith('#'))]"
```

## Build the paper

The manuscript is a multi-file LaTeX document: `paper/main.tex` inputs
`paper/macros.tex` and `paper/sections/01..11` (seven main sections plus four
appendices). The bibliography is an inline
`thebibliography`, so **no `bibtex`/`biber` pass is needed** — two `pdflatex`
passes resolve the cross-references (a third is harmless).
`main.tex` sets `\pdfinfoomitdate=1`, `\pdfsuppressptexinfo=-1`, and
`\pdftrailerid{}`, so the build is timestamp-free and the PDF bytes are stable
across rebuilds on a fixed TeX distribution. The current PDF is hash-pinned in
`MANIFEST_SHA256.txt`; a rebuild with another TeX distribution may be visually
equivalent without being byte-identical. Rebuild from `paper/` with the
title-named job target:

```bash
cd paper
job="The_Selected_Higher-Star_Defect_of_a_Design_Incidence_Lattice"
pdflatex -interaction=nonstopmode -halt-on-error -jobname="$job" main.tex
pdflatex -interaction=nonstopmode -halt-on-error -jobname="$job" main.tex
```

## What is imported rather than replayed

The verifier `scripts/verify.py` re-derives **only** the four self-contained
finite controls listed above, from scratch, with no external data. Everything
else the paper cites is imported, not recomputed here:

- the higher-incidence/star identities (Wilson 1982, reproduced by
  Kiermaier–Wassermann 2023), the distinct complete-subset diagonal form
  (Wilson 1990), and the
  universal additive/incidence group and its `t=2` case (Caggegi–Falcone–Pavone);
- the invariant factors of point/subspace incidence in `PG(n,q)`/`AG(n,q)`,
  including the `PG(2,4)` valuation-two calibration (Chandler–Sin–Xiang);
- the finite symmetric bilinear / discriminant-form theory (Wall; Nikulin;
  Conway–Sloane; Schmidt) used in the prime-by-prime analysis;
- the `S(2,5,v)` existence carriers (Hanani), the STS `p`-rank inputs
  (Doyen–Hubaut–Vandensavel; Assmus–Key; Tonchev–Weishaar; Shi–Xu–Krotov;
  Solé), the prescribed-rank carriers (Jungnickel–Tonchev) and counting
  asymptotics (Keevash; Ferber–Jain–Sudakov), and the Hermitian-unital incidence
  divisors (Hiss; Key).

These classical ingredients are attributed in the paper and in `docs/SOURCE_LOCK.md`;
no priority or firstness is claimed for them. Elementary supporting facts,
including the generic binary bilinear lemma, are proved in the manuscript. The
theorems of Sections 2–4 and 6–7 use no finite census at all.
