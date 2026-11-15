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
