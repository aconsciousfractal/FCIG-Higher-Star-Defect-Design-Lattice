# License scope

The original manuscript and its companion have the following scopes:

| Paths | License |
|---|---|
| `paper/**` | CC BY 4.0, in `LICENSE_MANUSCRIPT.md` |
| `scripts/**`, `docs/**`, `certificates/**`, `results/**` | MIT |
| `README.md`, `README_REVIEWER.md`, `REPRODUCE.md`, `CITATION.cff` | MIT |
| `MANIFEST_SHA256.txt`, `requirements.txt`, `.gitignore`, `.gitattributes` | MIT |

Copyright (c) 2026 Oleksiy Babanskyy.

The historical manuscript versions were distributed under MIT; this scope
update does not revoke those existing permissions. The top-level MIT license
and `CITATION.cff` software license refer to the original companion.

## Third-party boundary

This package embeds **no third-party source, data, or bytes**: `scripts/verify.py`
constructs every design from scratch with no external input. The classical
theorems the paper builds on are used only by **citation** and remain the work
of their respective authors (Wilson; Caggegi–Falcone–Pavone; Chandler–Sin–Xiang;
Ringe; Wall; Nikulin; Conway–Sloane; Schmidt; Hanani; Doyen–Hubaut–Vandensavel;
Assmus–Key; Tonchev–Weishaar; Shi–Xu–Krotov; Solé; Jungnickel–Tonchev;
Graver–Jurkat; Graham–Li–Li; Keevash; Ferber–Jain–Sudakov; Hiss; Key); see
`docs/SOURCE_LOCK.md`. The grants above cover only the author's original
material, not the cited works or their third-party content.
