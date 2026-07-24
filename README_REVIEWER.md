# Reviewer Quickstart

About fifteen minutes: a sub-second replay plus reading. This is a theory paper
with a small, self-contained reproducibility layer — no external data, no
randomness, no network.

1. **Read the paper**: `paper/The_Selected_Higher-Star_Defect_of_a_Design_Incidence_Lattice.pdf`.
   The spine is proved with **no** finite census: the sandwich and exact
   sequences (Thm 2.1, §2); the pointed presentation and parameter/discriminant
   envelope (Prop 3.1, §3, with the square bound by Cauchy–Binet); the
   prime-by-prime analysis (good-prime Prop 4.1, Witt Thm 4.2, exceptional-prime
   Thm 4.3, binary metabolicity Lem 4.4/Thm 4.5, §4); the valuation-two formula
   (Thm 5.1) and same-parameter separation (Thm 5.2, §5); Pasch transport
   (Thm 6.1, §6); Möbius/Hermitian applications (§7); and the appendices — the
   STS(15) spectrum with the ternary splitting (Thm A.1, Prop A.2), the
   realization theorem (Thm B.1), the worked SQS(8) example, and reproducibility.

2. **Replay the finite controls** (<1 s; Python 3.10+, `python-flint`):

   ```bash
   python scripts/verify.py \
       --output results/verification.json --log results/verification.log
   ```

   Constructed from scratch with no external data, it checks:
   - `SQS(8)`: full form `1^4 2^3 4`, `Delta = (Z/2)^3`;
   - `PG(3,2)` vs Bose `STS(15)`: forms `1^11 2^3 6` and `1^14 3`, defects
     `(Z/2)^4` vs `0` on the common `2-(15,3,1)` row (Thm 5.2);
   - `M(2) = 3-(5,3,1)`: form `1^4 3`, `Delta = 0` (the `d=1` corollary).

   It ends `PASS`, prints `certificate_sha256=13BBF7B9...`, enforces an
   independent modular cross-check, and prints a `self-check: output
   byte-identical to the frozen certificate` line. The output is byte-identical
   under `python` and `python -O`.

3. **Check the manifest**: compare all file hashes against `MANIFEST_SHA256.txt`
   (see `REPRODUCE.md`). The pinned object is the LaTeX source and the verifier,
   not the toolchain-dependent PDF or the regenerated `results/`.

4. **Boundary** (read before citing): `docs/PUBLIC_CLAIM_BOUNDARY.md` and
   `docs/CLAIM_LEDGER.md`.
   - What is equal / bounded concerns the image (column) lattice and the pointed
     cokernel `Delta = coker(C_x0)`; the relation kernels are not part of any
     claim.
   - Discriminant isotropy statements are **bilinear**; no quadratic (Arf)
     refinement is asserted, and the binary no-growth result is only for the
     discriminant-form obstruction (other binary obstructions are not excluded).
   - No realizability beyond the elementary `(Z/2)^a`/`(Z/3)^b` targets;
     nonsquarefree exponents and general realizability are out of scope.
   - **No priority or firstness** is claimed; dated negative searches are recorded
     as such.

   Every imported input is attributed in the bibliography and
   `docs/SOURCE_LOCK.md` (Wilson; Caggegi–Falcone–Pavone; Chandler–Sin–Xiang;
   Wall; Nikulin; Conway–Sloane; Schmidt; Hanani; Doyen–Hubaut–Vandensavel;
   Assmus–Key; Tonchev–Weishaar; Shi–Xu–Krotov; Solé; Jungnickel–Tonchev; Hiss;
   Key; and Christian Ringe for the Möbius Smith form).
