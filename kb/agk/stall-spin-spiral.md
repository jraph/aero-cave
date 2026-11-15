# Stall, spin & spiral / Décrochage, vrille et spirale
<!-- concept: agk-stall | level: PPL CPL IR -->

[Index](README.md) · concept `agk-stall` · unit IDs are stable: never rename one.

***
#### Load factor / accelerated stall
<!-- id: agk-load-factor-accelerated-stall | from: 06 | also: agk-load | kind: formula | level: PPL CPL IR -->

- `F:` in a coordinated, constant-altitude turn, `n = 1 / cos(bank)`. The bank-only equation does not apply to every manoeuvre.
- `F:` `Vs_bank = Vs × √n`.
- `M:` `45°` bank ≈ `1.41g`, stall ×`1.19`; `60°` bank = `2g`, stall ×`1.41`.
- `T:` accelerated stall depends load factor/AoA, not just bank; POH chart wins.
***
#### Manoeuvring speed / stall-speed notation
<!-- id: agk-manoeuvring-speed-stall-speed-notation | from: 06 | also: agk-load, agk-vspeeds | kind: formula | level: PPL CPL IR -->

- `VS` = generic stall speed in stated config; `VS1` = stall speed in specified config (**often clean**); `VS0` = stall speed in landing config. `VS` and `VS1` may denote the **same clean-config value** in context; do not substitute `VS0`.
- `F theoretical:` positive stall/limit-load intersection `VA_est ≈ VS(clean) × √n_limit`, using matching config/weight/speed basis; **not guaranteed published VA**.
- `M legacy normal:` `n_limit=+3.8` ⇒ `VA_est≈1.95×VS1` (mental shortcut `≈2×VS1`, **not a VA range**); e.g. `VS1=50 KIAS ⇒ ≈97.5 KIAS`.
- `F weight:` approximate `VA2≈VA1×√(W2/W1)` if same config/load-factor basis; lighter ⇒ lower speed.
- `T:` approved POH/AFM `VA` and weight schedule win; `VA` does **not** guarantee protection against multiple/abrupt control inputs or all turbulence.
***
#### Pebble
<!-- id: agk-stall-spin-spiral-pebble | level: PPL CPL IR -->

- LOAD FACTOR `coordinated level turn n = 1/cos(bank) | Vs_bank = Vs × √n | 45° ≈ 1.41 g, stall ×1.19 | 60° = 2 g, stall ×1.41`
- VA `VA_est ≈ VS(clean) × √n_limit; +3.8 g → ≈1.95 × VS1, not guaranteed published VA | lighter → lower VA | VS0 ≠ VS1 | VA does not protect against multiple/abrupt inputs`
***
