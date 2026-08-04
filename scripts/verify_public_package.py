#!/usr/bin/env python3
"""Fail-closed checker for the v1.0.0 public package."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "MANIFEST_SHA256.txt"
CANONICAL_PDF = "paper/The_Selected_Higher-Star_Defect_of_a_Design_Incidence_Lattice.pdf"
EXPECTED_RELEASE = "v1.0.0"
EXPECTED_CERTIFICATE_SHA256 = (
    "13BBF7B95BD9404CB6190F686BDD2D5FE31F53426B42D0E86D502DAA612BCCAE"
)
RETIRED_PATHS = {"docs/GATE_HISTORY.md", "docs/RED_TEAM_REPORT.md"}
IGNORED_DIRS = {".git", "tmp", "__pycache__"}
IGNORED_SUFFIXES = {
    ".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out",
    ".pyc", ".pyo", ".synctex.gz", ".toc",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def ignored(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if any(part in IGNORED_DIRS for part in relative.parts):
        return True
    name = relative.as_posix()
    if name == "results/verification.log":
        return True
    return any(name.endswith(suffix) for suffix in IGNORED_SUFFIXES)


def package_files() -> list[str]:
    return sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and not ignored(path)
    )


def manifest_entries() -> dict[str, str]:
    entries: dict[str, str] = {}
    for number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"([0-9A-Fa-f]{64})  (.+)", line)
        if not match:
            raise RuntimeError(f"malformed manifest line {number}")
        digest, name = match.groups()
        if name in entries:
            raise RuntimeError(f"duplicate manifest entry: {name}")
        entries[name] = digest.upper()
    return entries


def write_manifest() -> None:
    names = [name for name in package_files() if name != "MANIFEST_SHA256.txt"]
    lines = [
        "# SHA-256 manifest for the Higher-Star-Defect public package v1.0.0",
        "# Generated 2026-08-04; exact inventory except this manifest file.",
    ]
    lines.extend(f"{sha256(ROOT / name).lower()}  {name}" for name in names)
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def check_public_residue() -> None:
    markers = (
        "Gate-Disciplined-" + "Computational-Mathematics",
        "docs/" + "GATE_HISTORY.md",
        "docs/" + "RED_TEAM_REPORT.md",
        "owner-" + "gated",
        "P" + "APP taxonomy",
    )
    text_suffixes = {".cff", ".md", ".py", ".tex", ".txt"}
    offenders: list[str] = []
    for name in package_files():
        path = ROOT / name
        if path.suffix.lower() not in text_suffixes or path in {MANIFEST, Path(__file__).resolve()}:
            continue
        content = path.read_text(encoding="utf-8")
        if any(marker in content for marker in markers):
            offenders.append(name)
    if offenders:
        raise RuntimeError(f"retired public-process residue: {offenders}")


def verify() -> None:
    entries = manifest_entries()
    expected = set(entries) | {"MANIFEST_SHA256.txt"}
    actual = set(package_files())
    if expected != actual:
        raise RuntimeError(
            f"inventory mismatch; missing={sorted(expected - actual)}, "
            f"unexpected={sorted(actual - expected)}"
        )
    for name, expected_hash in entries.items():
        if sha256(ROOT / name) != expected_hash:
            raise RuntimeError(f"hash mismatch: {name}")

    if RETIRED_PATHS & actual:
        raise RuntimeError(f"retired paths present: {sorted(RETIRED_PATHS & actual)}")
    if CANONICAL_PDF not in entries:
        raise RuntimeError("canonical PDF is not pinned")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if 'version: "1.0.0"' not in citation or 'date-released: "2026-08-04"' not in citation:
        raise RuntimeError("release metadata mismatch")
    if EXPECTED_RELEASE not in readme:
        raise RuntimeError("README release link missing")

    frozen = ROOT / "certificates/expected_verification.json"
    result = ROOT / "results/verification.json"
    if sha256(frozen) != EXPECTED_CERTIFICATE_SHA256 or frozen.read_bytes() != result.read_bytes():
        raise RuntimeError("frozen/result certificate mismatch")
    payload = json.loads(frozen.read_text(encoding="utf-8"))
    if payload.get("status") != "PASS":
        raise RuntimeError("frozen certificate is not PASS")

    check_public_residue()
    print("PUBLIC_PACKAGE_VERIFY_PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    if args.write_manifest:
        write_manifest()
        print("MANIFEST_WRITTEN")
    else:
        verify()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
