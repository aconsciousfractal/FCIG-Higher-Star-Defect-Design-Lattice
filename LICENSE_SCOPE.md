# License scope

Everything authored in this repository is released under the single MIT
`LICENSE`:

| Paths | License |
|---|---|
| `paper/**`, `scripts/**`, `docs/**`, `certificates/**`, `results/**` | MIT |
| `README.md`, `README_REVIEWER.md`, `REPRODUCE.md`, `CITATION.cff` | MIT |
| `MANIFEST_SHA256.txt`, `requirements.txt`, `.gitignore`, `.gitattributes` | MIT |

Copyright (c) 2026 Oleksiy Babanskyy.

## Third-party boundary

This package embeds **no third-party source, data, or bytes**: `scripts/verify.py`
constructs every design from scratch with no external input. The classical
theorems the paper builds on are used only by **citation** and remain the work
of their respective authors (Wilson; Caggegi–Falcone–Pavone; Chandler–Sin–Xiang;
Ringe; Wall; Nikulin; Conway–Sloane; Schmidt; Hanani; Doyen–Hubaut–Vandensavel;
Assmus–Key; Tonchev–Weishaar; Shi–Xu–Krotov; Solé; Jungnickel–Tonchev;
Graver–Jurkat; Graham–Li–Li; Keevash; Ferber–Jain–Sudakov; Hiss; Key); see
`docs/SOURCE_LOCK.md`. The MIT grant above covers only the original code and
prose of this repository, not those cited results.
