# Reviewer Quickstart

The finite replay is short; checking the general proofs is a separate task.
This is a theory paper
with a small, self-contained reproducibility layer — no external data, no
randomness, no network.

1. **Read the paper**: `paper/The_Selected_Higher-Star_Defect_of_a_Design_Incidence_Lattice.pdf`.
   Start with Sections 1.1–1.2 for the mathematical results, 1.3 for the
   relationship to prior work, and 1.4 for notation. Then follow the argument:

   | Location | Purpose |
   |---|---|
   | §§2–3 | Star bound, exact sequences and pointed Gram/discriminant presentation |
   | §§4.1–4.4 | Good primes, odd-prime Witt bound, exceptional reduction and the general binary order lemma |
   | §§5–7 | Fixed-parameter behavior, Pasch switches and geometric applications |
   | Appendices A–C | STS spectrum and augmentation splitting, infinite elementary realization, worked SQS(8) example |
   | Appendix D | Four finite controls, checks performed and imported data |

   The theorem numbering is unchanged. The general arguments are written
   proofs; the two-system comparison (Theorem 5.2) uses the stated finite
   computation. Keep this distinction when assessing the companion.

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

3. **Check the package**:

   ```bash
   python scripts/verify_public_package.py
   ```

   This fail-closed check verifies the exact shipped inventory and every hash
   in `MANIFEST_SHA256.txt`, including the canonical PDF and replay result. It
   also checks revision metadata, retired-path absence, and certificate byte
   identity (see `REPRODUCE.md`).

4. **Boundary** (read before citing): `docs/PUBLIC_CLAIM_BOUNDARY.md` and
   `docs/CLAIM_LEDGER.md`.
   - What is equal / bounded concerns the image (column) lattice and the pointed
     cokernel `Delta = coker(C_x0)`; the relation kernels are not part of any
     claim.
   - Discriminant isotropy statements are **bilinear**; no quadratic (Arf)
     refinement is asserted. The binary lemma concerns maximum subgroup order,
     not which abstract subgroup types admit isotropic embeddings.
   - No realizability beyond the elementary `(Z/2)^a`/`(Z/3)^b` targets;
     nonsquarefree exponents and general realizability are out of scope.
   - **No priority or firstness** is claimed; dated negative searches are recorded
     as such. The explicit selected-design deductions are distinguished from
     classical inputs in the introduction and claim ledger.

5. **Read the revision and AI disclosure**: `docs/REVISION_NOTES.md` and
   `AI_USE.md`. Revision 1.0.1 corrects the binary comparison and
   supplies the missing moving-parameter proof in Appendix B. AI review and
   finite replay are not independent specialist verification.

   Every imported input is attributed in the bibliography and
   `docs/SOURCE_LOCK.md` (Wilson; Caggegi–Falcone–Pavone; Chandler–Sin–Xiang;
   Wall; Nikulin; Conway–Sloane; Schmidt; Hanani; Doyen–Hubaut–Vandensavel;
   Assmus–Key; Tonchev–Weishaar; Shi–Xu–Krotov; Solé; Jungnickel–Tonchev; Hiss;
   Key; and Christian Ringe for the Möbius Smith form).
