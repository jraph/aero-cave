# Thunderstorms & convection / Orages et convection
<!-- concept: met-ts | level: PPL CPL IR -->

[Meteorology index / Index météo](README.md) · concept `met-ts` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Thunderstorms
<!-- id: wx-thunderstorms | from: 16, 05 -->

- Moisture + instability + lift.
- Stages:
  1. **Cumulus:** updrafts only.
  2. **Mature:** up + downdrafts; precip; maximum hazards.
  3. **Dissipating:** downdrafts dominate.
- Hazards: extreme turbulence, hail, lightning, heavy precip, icing, tornado, wind shear/microburst, instrument errors.
- `!:` avoid with large margin: cells/lines/embedded TS; never use a visual/radar “gap” to thread active cells.
- Assess SIGMET/GFA/TAF/PIREP/radar/lightning/satellite for movement/growth/line/escape. `T:` datalink delayed; attenuation hides cells.
***
#### Thunderstorm types, coverage, lightning detection
<!-- id: wx-thunderstorm-types-lightning-detection | also: ifr-wx | level: PPL CPL IR -->

- Types by lifting: **air mass** (surface heating, afternoon, isolated) · **frontal** (cold front lines, warm-front embedded) · **orographic** (forced over terrain) · **squall line** (line ahead of cold front, often most severe) · **nocturnal** (night, cloud-top cooling, Prairies).
- Coverage terms: `ISOL` ≤25 % · `OCNL` 26–50 % · `FRQ` >50 %. SIGMET TS implies severe icing + turbulence. [AIM MET 5.2, 6.2]
- Avoid severe storms by ≥**20 NM**; never under a storm; strong radar echoes ≤40 NM apart = no safe gap. [AIM AIR 2.7.1–2.7.2]
- Lightning detection: Canadian Lightning Detection Network (CLDN) data to FICs/ACCs; lightning imagery = supplementary product. AUTO stations outside CLDN cannot report TS. [MET 1.2.2, 1.2.3, 1.3.9.2]
- Airborne strike finders map electrical discharges (not precipitation); weather radar shows precipitation, not turbulence.
- `?:` type list and airborne detector line = general knowledge; not checked against a TC source.
***
#### Pebble
<!-- id: met-ts-pebble -->

- TS `MOISTURE + INSTABILITY + LIFT | cumulus = updrafts only → mature = up + downdrafts, precip, maximum hazards → dissipating = downdrafts dominate`
- HAZARDS `extreme turbulence | hail | lightning | icing | wind shear/microburst | tornado`
- AVOID `large margin: cells/lines/embedded TS | never thread a visual/radar gap | datalink delayed; attenuation hides cells`
- TS `ISOL ≤25 % · OCNL 26–50 % · FRQ >50 % | avoid severe ≥20 NM | strong echoes ≤40 NM apart = no gap | CLDN lightning to FIC/ACC`
***
