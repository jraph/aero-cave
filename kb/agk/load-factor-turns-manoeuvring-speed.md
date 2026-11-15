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
#### Manoeuvring speed / stall-speed notation
<!-- id: agk-manoeuvring-speed-stall-speed-notation | from: 06 | also: agk-stall, agk-vspeeds | kind: formula | level: PPL CPL IR -->

- `VS` = generic stall speed in stated config; `VS1` = stall speed in specified config (**often clean**); `VS0` = stall speed in landing config. `VS` and `VS1` may denote the **same clean-config value** in context; do not substitute `VS0`.
- `F theoretical:` positive stall/limit-load intersection `VA_est ≈ VS(clean) × √n_limit`, using matching config/weight/speed basis; **not guaranteed published VA**.
- `M legacy normal:` `n_limit=+3.8` ⇒ `VA_est≈1.95×VS1` (mental shortcut `≈2×VS1`, **not a VA range**); e.g. `VS1=50 KIAS ⇒ ≈97.5 KIAS`.
- `F weight:` approximate `VA2≈VA1×√(W2/W1)` if same config/load-factor basis; lighter ⇒ lower speed.
- `T:` approved POH/AFM `VA` and weight schedule win; `VA` does **not** guarantee protection against multiple/abrupt control inputs or all turbulence.
***
#### Pebble
<!-- id: agk-load-factor-turns-manoeuvring-speed-pebble | level: PPL CPL IR -->

- RATE ONE `3°/s, 360° in 2 min | bank = atan(3·TAS/1091) ≈ TAS/10 + 7 (high by 1–2°) | 90 kt ≈ 14°, 120 kt ≈ 18° | higher TAS needs more bank`
- VA `VA_est ≈ VS(clean) × √n_limit; +3.8 g → ≈1.95 × VS1, not guaranteed published VA | lighter → lower VA | VS0 ≠ VS1 | VA does not protect against multiple/abrupt inputs`
***
