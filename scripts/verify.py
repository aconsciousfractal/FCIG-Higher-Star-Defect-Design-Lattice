#!/usr/bin/env python3
"""Deterministic verifier for the finite controls of the higher-star defect paper.

Reproduces, from scratch (no external data), the self-contained finite
statements used in the paper:

  * SQS(8) = AG(3,2): the 3-(8,4,1) quadruple system has full incidence Smith
    form 1^4 2^3 4, hence Delta = (Z/2)^3 (a nonzero t=3 defect; d=2);
  * the same-parameter separation of two 2-(15,3,1) Steiner triple systems:
    PG(3,2) has Smith form 1^11 2^3 6 and Delta = (Z/2)^4, while the Bose system
    has Smith form 1^14 3 and Delta = 0;
  * the smallest finite Moebius plane M(2) = 3-(5,3,1): Smith form 1^4 3,
    Delta = 0 (the d=1 vanishing corollary).

Each Smith form is computed by python-flint; the binary and ternary generator
counts of the defect are cross-checked, and enforced, against an independent
modular-rank route (`rank_mod`). If a frozen certificate is present, the run
also asserts byte-identity against it. Output JSON is byte-identical under
`python` and `python -O`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from collections import Counter
from itertools import combinations
from pathlib import Path

from flint import fmpz_mat


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise RuntimeError(msg)


def smith_counts(rows: list[list[int]]) -> dict[str, int]:
    """Invariant-factor multiplicities via python-flint SNF (|factor| -> count),
    zeros omitted."""
    snf = fmpz_mat(rows).snf()
    n, m = snf.nrows(), snf.ncols()
    diag = [abs(int(snf[i, i])) for i in range(min(n, m))]
    return {str(v): c for v, c in sorted(Counter(d for d in diag if d).items())}


def rank_mod(rows: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in rows]
    rows_n, cols_n = len(a), len(a[0]) if a else 0
    r = 0
    for c in range(cols_n):
        piv = next((i for i in range(r, rows_n) if a[i][c] % p), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(rows_n):
            if i != r and a[i][c] % p:
                f = a[i][c]
                a[i] = [(x - f * y) % p for x, y in zip(a[i], a[r])]
        r += 1
    return r


def incidence(points: list, blocks: list[frozenset]) -> list[list[int]]:
    return [[1 if x in B else 0 for B in blocks] for x in points]


def pointed_presentation(points: list, blocks: list[frozenset]) -> list[list[int]]:
    """Delete the first point row and append the all-ones block row."""
    A = incidence(points, blocks)
    return A[1:] + [[1] * len(blocks)]


def counts_to_factor_list(counts: dict[str, int]) -> list[int]:
    out: list[int] = []
    for value, mult in sorted(counts.items(), key=lambda kv: int(kv[0])):
        out.extend([int(value)] * mult)
    return out


# ---- constructions -------------------------------------------------------

def sqs8() -> tuple[list, list[frozenset]]:
    """3-(8,4,1): points F_2^3, blocks = affine 2-flats (cosets of 2-subspaces)."""
    points = list(range(8))
    subspaces = set()
    for a in range(1, 8):
        for b in range(a + 1, 8):
            W = frozenset({0, a, b, a ^ b})
            if len(W) == 4:
                subspaces.add(W)
    blocks = set()
    for W in subspaces:
        for c in range(8):
            blocks.add(frozenset({c ^ w for w in W}))
    blocks = sorted(blocks, key=lambda B: sorted(B))
    require(len(blocks) == 14, "SQS(8) block count")
    return points, blocks


def pg32_lines() -> tuple[list, list[frozenset]]:
    """2-(15,3,1): points = nonzero F_2^4, lines = xor-zero triples."""
    points = list(range(1, 16))
    lines = sorted(
        {frozenset({x, y, x ^ y}) for x in points for y in points if x < y},
        key=lambda B: sorted(B),
    )
    require(len(lines) == 35, "PG(3,2) line count")
    return points, lines


def bose_sts15() -> tuple[list, list[frozenset]]:
    """2-(15,3,1) Bose system on Z_5 x Z_3 with idempotent commutative
    quasigroup x*y = 3(x+y) mod 5 on Z_5."""
    def star(x, y):
        return (3 * (x + y)) % 5
    points = [(x, i) for x in range(5) for i in range(3)]
    blocks = set()
    for x in range(5):  # verticals
        blocks.add(frozenset({(x, 0), (x, 1), (x, 2)}))
    for i in range(3):
        for x in range(5):
            for y in range(x + 1, 5):
                blocks.add(frozenset({(x, i), (y, i), (star(x, y), (i + 1) % 3)}))
    blocks = sorted(blocks, key=lambda B: sorted(B))
    require(len(blocks) == 35, "Bose STS(15) block count")
    # exact 2-(15,3,1) check
    pairs = Counter()
    for B in blocks:
        for u, v in combinations(sorted(B), 2):
            pairs[(u, v)] += 1
    require(len(pairs) == 105 and set(pairs.values()) == {1}, "Bose pair balance")
    return points, blocks


def moebius2() -> tuple[list, list[frozenset]]:
    """3-(5,3,1) = all triples of 5 points (the order-2 Miquelian plane)."""
    points = list(range(5))
    blocks = [frozenset(T) for T in combinations(points, 3)]
    require(len(blocks) == 10, "M(2) block count")
    return points, blocks


# ---- checks --------------------------------------------------------------

def check_design(points, blocks, expected_full, k, emit, name) -> dict:
    A = incidence(points, blocks)
    full = smith_counts(A)
    require(
        counts_to_factor_list(full) == expected_full,
        f"{name}: full Smith form {counts_to_factor_list(full)} != {expected_full}",
    )
    # Delta from the pointed presentation Delta = coker(C_x0).
    C = pointed_presentation(points, blocks)
    delta = smith_counts(C)
    # independent modular cross-check of the binary/ternary ranks of C
    v = len(points)
    r2 = rank_mod(C, 2)
    r3 = rank_mod(C, 3)
    delta_group = {kk: vv for kk, vv in delta.items() if kk != "1"}
    # Load-bearing independent cross-check: the number of 2- and 3-generators of
    # Delta (from the flint SNF) must equal the modular coranks v - rank_Fp(C_x0).
    gens2 = sum(m for f, m in delta_group.items() if int(f) % 2 == 0)
    gens3 = sum(m for f, m in delta_group.items() if int(f) % 3 == 0)
    require(
        v - r2 == gens2 and v - r3 == gens3,
        f"{name}: flint Delta disagrees with modular ranks "
        f"(2: {v - r2} vs {gens2}; 3: {v - r3} vs {gens3})",
    )
    emit(f"{name}: full Smith {counts_to_factor_list(full)}; "
         f"Delta={delta_group or 'trivial'}; rank_F2(C_x0)={r2}, rank_F3(C_x0)={r3}"
         f" (modular cross-check OK)")
    return {
        "name": name,
        "points": v,
        "blocks": len(blocks),
        "block_size": k,
        "full_smith_invariant_factors": counts_to_factor_list(full),
        "delta_invariant_factors": counts_to_factor_list(delta_group),
        "pointed_rank_F2": r2,
        "pointed_rank_F3": r3,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--log", required=True, type=Path)
    args = ap.parse_args()

    started = time.perf_counter()
    log: list[str] = []

    def emit(m: str) -> None:
        line = f"[{time.perf_counter()-started:7.3f}s] {m}"
        print(line, flush=True)
        log.append(line)

    results = {}

    p, b = sqs8()
    results["SQS8"] = check_design(p, b, [1, 1, 1, 1, 2, 2, 2, 4], 4, emit, "SQS(8)=AG(3,2)")
    require(results["SQS8"]["delta_invariant_factors"] == [2, 2, 2], "SQS(8) Delta")

    p, b = pg32_lines()
    results["PG32"] = check_design(
        p, b, [1]*11 + [2, 2, 2, 6], 3, emit, "PG(3,2) STS(15)")
    require(results["PG32"]["delta_invariant_factors"] == [2, 2, 2, 2], "PG(3,2) Delta")

    p, b = bose_sts15()
    results["Bose"] = check_design(p, b, [1]*14 + [3], 3, emit, "Bose STS(15)")
    require(results["Bose"]["delta_invariant_factors"] == [], "Bose Delta trivial")

    require(
        results["PG32"]["delta_invariant_factors"] != results["Bose"]["delta_invariant_factors"],
        "same-parameter separation failed",
    )
    emit("separation: PG(3,2) Delta=(Z/2)^4 vs Bose Delta=0 on the common 2-(15,3,1) row")

    p, b = moebius2()
    results["M2"] = check_design(p, b, [1, 1, 1, 1, 3], 3, emit, "Moebius M(2)=3-(5,3,1)")
    require(results["M2"]["delta_invariant_factors"] == [], "M(2) Delta trivial (d=1)")

    payload = {
        "schema": "FCIG-HIGHER-STAR-DEFECT-CONTROLS-v1",
        "status": "PASS",
        "terminal": "HIGHER_STAR_DEFECT_FINITE_CONTROLS_PASS",
        "claim_scope": "self-contained finite controls; no novelty or firstness claim",
        "controls": results,
        "separation_confirmed": True,
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    frozen = (
        Path(__file__).resolve().parent.parent
        / "certificates" / "expected_verification.json"
    )
    if frozen.exists():
        require(
            text.encode("utf-8") == frozen.read_bytes(),
            "output differs from certificates/expected_verification.json",
        )
        emit("self-check: output byte-identical to the frozen certificate")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.log.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8", newline="\n")
    emit(f"certificate_sha256={hashlib.sha256(text.encode()).hexdigest().upper()}")
    emit("PASS")
    args.log.write_text("\n".join(log) + "\n", encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
