# TAF
<!-- concept: met-taf | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-taf` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### TAF scan / groups
<!-- id: wxp-taf | from: 05 -->

- `P:` ID→issue/valid→prevailing→`FM/BECMG/TEMPO/PROB` timeline covering DEP/ETA/ALT ETA + delay; do not average groups.
- `FM` permanent from minute | `BECMG` gradual permanent | `TEMPO` each `<1 h`, combined `≤½` of the TEMPO window [TC AIM 2026-2, MET 7.3, p. 158] | `PROB30/40` probability.
- `FM` begins a new self-contained forecast period. With `BECMG/TEMPO`, unchanged groups may carry forward, but a changed cloud group gives the complete new cloud picture; visibility/weather/obscuration form another related group. Do not retain an old cloud layer merely because it is absent after a change. `[AIM MET 7.4]`
***
#### TAF alternate / risk
<!-- id: wxp-taf-alternate | from: 05 | also: ifr-alt | level: IR -->

- Alternate TAF rule (`BECMG` end/start, `TEMPO`≥alternate, `PROB`≥landing): `ifr-taf-alternate-logic`.
- `T:` alternate≠landing≠approach-ban minima. `TEMPO` near ETA and `PROB30/40` high-consequence `TS/FZRA/low vis` require fuel/options; many short groups reduce confidence.
***
#### Pebble
<!-- id: met-taf-pebble -->

- TAF `FM = permanent from the minute, new self-contained period | BECMG = gradual permanent | TEMPO = each <1 h, combined ≤½ TEMPO window | PROB30/40 | do not average groups`
- ALTERNATE `rule: ifr-taf-alternate-logic | alternate ≠ landing ≠ approach-ban minima | TEMPO near ETA / PROB30/40 TS-FZRA-low vis → fuel + options`
***
