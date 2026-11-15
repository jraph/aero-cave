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

- Types by trigger: **air mass** (surface heating, afternoon, isolated) · **frontal** (cold air undercuts warm air) · **lake-breeze** (cool lake air meets hot humid air inland) · **upslope / orographic** (forced over terrain; early-day storms on east slopes of the Rockies) · organized lines and systems (**squall line**, MCS) often along fronts. [ECCC *Severe Weather in Canada* ch. 4; NAV CANADA AvMet reference, thunderstorm]
- Coverage terms: GFA `ISOL` ≤25 % · `OCNL` 26–50 % · `FRQ` >50 % [MET 4.11, same in AIRMET 5.2] · high-level SigWx `ISOL` <50 % · `OCNL` 50–75 % · `FRQ` >75 % [MET 12.2]. SIGMET TS implies severe icing + turbulence [MET 6.2].
- `T:` same word, different % on GFA vs high-level SigWx.
- Avoid severe storms (or intense echoes, incl. anvil) by ≥**20 NM**; strong echoes ≤40 NM apart = no safe gap; tops ≥35 000 ft = severe; never under a storm. [AIM AIR 2.7.1–2.7.2]
- Radar shows precipitation; stronger return → generally worse turbulence; light echoes ≠ light storm. [AIR 2.7.1–2.7.2]
- Lightning detection: Canadian Lightning Detection Network (CLDN) data to FICs/ACCs; AUTO stations outside CLDN cannot report TS. [MET 1.2.2, 1.2.3, 1.3.9.2; CFS]
- 703/704 ops: passengers in IMC with forecast TS need thunderstorm detection equipment or weather radar. [CAR 703.65, 704.64]
- `?:` airborne strike finders map electrical discharges, not precipitation: no TC source found.
***
#### Pebble
<!-- id: met-ts-pebble -->

- TS `MOISTURE + INSTABILITY + LIFT | cumulus = updrafts only → mature = up + downdrafts, precip, maximum hazards → dissipating = downdrafts dominate`
- HAZARDS `extreme turbulence | hail | lightning | icing | wind shear/microburst | tornado`
- AVOID `large margin: cells/lines/embedded TS | never thread a visual/radar gap | datalink delayed; attenuation hides cells`
- TS `GFA ISOL ≤25 · OCNL 26–50 · FRQ >50 % | hi SigWx ISOL <50 · OCNL 50–75 · FRQ >75 % | avoid severe ≥20 NM | strong echoes ≤40 NM apart = no gap | CLDN lightning to FIC/ACC`
***
