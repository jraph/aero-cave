# Pitot-static instruments / Instruments anémobarométriques
<!-- concept: agk-pitot | level: PPL CPL IR -->

[Index](README.md) · concept `agk-pitot` · unit IDs are stable: never rename one.

***
#### Pitot / static
<!-- id: sys-pitot-static | from: 08 | level: PPL CPL IR -->

- Pitot→ASI; static→ASI/ALT/VSI. Pitot heat normally does not heat static ports; preflight for covers/bugs/water/ice/tape.

| Failure | ASI | ALT | VSI |
|---|---|---|---|
| pitot blocked, drain open | →`0` | normal | normal |
| pitot+drain blocked | climb high/descent low | normal | normal |
| static blocked | climb low/descent high | frozen | →`0` |
| alternate static | often ASI/ALT higher | aircraft-specific | momentary/specific |

- `P:` heat→alternate static per POH→attitude/power/GPS trend→ATC→land. Exact errors vary.
***
#### Pitot-static instruments — principles
<!-- id: agk-pitot-static-instrument-principles | also: ifr-emerg | level: PPL CPL IR -->

| Instrument | Senses | Principle |
|---|---|---|
| ASI | pitot + static | diaphragm fed pitot pressure, case vented static → IAS |
| Altimeter | static | sealed aneroid in case vented to static expands as altitude increases; subscale = pressure datum |
| VSI | static | calibrated leak between case and static → rate of change; rate lags, settles 6–9 s after level-off |

- Altimeter lags in climb/descent: lead level-off by ~10 % of vertical speed. IVSI adds accelerometers → near-zero lag. [TP 2076 2.1.2 F]
- Altimeter calibrated ±20 ft at sea level; ground check ±50 ft of known elevation. [AIM AIR 1.5.1–1.5.2]
- Setting too high → reads too high. Cold → true lower: ~4 % per 11 °C below ISA. Mountain wave + cold → overread up to 3 000 ft. [AIR 1.5.3–1.5.8]
- Blockage patterns: `sys-pitot-static`.
***
