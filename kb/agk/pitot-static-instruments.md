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
| ASI | pitot (total) − static | dynamic pressure → IAS |
| Altimeter | static | aneroid capsule expands as pressure falls; subscale = pressure datum |
| VSI | static | capsule vs calibrated leak: rate of pressure change → trend + rate, with lag |

- Altimeter calibrated to ISA true altitude, ±20 ft at sea level; ground check ±50 ft of field elevation. [AIM AIR 1.5.1–1.5.2]
- Setting too high → reads too high. Cold → true lower: ~4 % per 11 °C below ISA. [AIR 1.5.3–1.5.4]
- Errors: ASI position, compressibility, density; VSI lag; blockage patterns in `sys-pitot-static`.
- `?:` instrument mechanics = general knowledge; not checked against a TC source.
***
