# Load factor, turns & manoeuvring speed / Facteur de charge, virages et vitesse de manœuvre
<!-- concept: agk-load | level: PPL CPL IR -->

[Index](README.md) · concept `agk-load` · unit IDs are stable: never rename one.

***
#### Rate-one turn / turn geometry
<!-- id: agk-rate-one-turn-turn-geometry | from: 06 | kind: formula | level: PPL CPL IR -->

- `F:` standard-rate turn = `3°/sec`; 360° in `2 min`.
- `F:` exact rate-one bank = `atan(3 × TAS / 1091)` (TAS kt).
- `F rough:` bank for rate-one ≈ `TAS/10 + 7` (overestimates ~1–2° at light-aircraft speeds).
- `F:` turn radius `ft ≈ TAS² / (11.26 × tan(bank))`; radius `NM ≈ TAS² / (68,420 × tan(bank))`. `[DERIVED; TAS kt]`
- `M:` exact: `90 kt` ≈ `14°`, `100 kt` ≈ `15°`, `120 kt` ≈ `18°` (rough rule gives 16° / 17° / 19°).
- `T:` high TAS needs more bank for standard rate.
***
#### Pebble
<!-- id: agk-load-factor-turns-manoeuvring-speed-pebble | level: PPL CPL IR -->

- RATE ONE `3°/s, 360° in 2 min | bank = atan(3·TAS/1091) ≈ TAS/10 + 7 (high by 1–2°) | 90 kt ≈ 14°, 120 kt ≈ 18° | higher TAS needs more bank`
***
