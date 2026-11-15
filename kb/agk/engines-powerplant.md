# Engines & powerplant / Moteurs et groupe motopropulseur
<!-- concept: agk-engine | level: PPL CPL -->

[Index](README.md) · concept `agk-engine` · unit IDs are stable: never rename one.

***
#### Engine essentials
<!-- id: sys-engine-essentials | from: 08 | level: PPL CPL -->

- Piston engine needs: air + fuel + ignition + compression + correct timing.
- Power-loss / roughness scan flow: `see sys-engine-roughness-generic-flow`.
- `M:` `AIR-FUEL-SPARK-COMPRESSION`.
- `T:` partial power may be temporary. Keep a landing area continuously available.
***
#### Magnetos / ignition
<!-- id: sys-magnetos-ignition | from: 08 | level: PPL CPL -->

- Mags are battery/alternator-independent; dual mags/plugs add redundancy/efficiency. Engine running with master OFF is normal.
- One-mag roughness: plug fouling, mag/lead or mixture. `!:` bad P-lead can leave mag live—moving prop may start engine.
- `T:` electrical failure may spare engine but remove radios/lights/flaps/gear/instruments.
***
#### Mixture
<!-- id: sys-mixture | from: 08 | level: PPL CPL -->

- Too rich: rough/fouling/high burn/power loss aloft; too lean: rough/power loss/high temps/detonation risk at high power.
- Lean by POH RPM/EGT/monitor method. `T:` full rich may be over-rich for high-DA TKOF.
***
#### Oil pressure / temperature
<!-- id: sys-oil-pressure-temperature | from: 08 | level: PPL CPL -->

| Indication | Likely concern | Action memory |
|---|---|---|
| low oil pressure + high temp | lubrication loss / impending seizure | reduce power, land ASAP |
| low pressure + normal temp | gauge/sender or early failure | treat seriously, monitor, land |
| high temp + normal pressure | cooling, low oil, prolonged climb | enrich/increase airflow/reduce power |
| pressure fluctuation | low quantity, aeration, sensor, manoeuvre | stabilize, assess, land |

- `T:` “gauge fault” is a diagnosis of exclusion. Plan for engine stoppage.
- `!:` abnormal noise/vibration + oil indication = immediate landing priority.
***
#### Powerplant / PROP · L4 CAVE
<!-- id: sys-powerplant-prop-l4-cave | from: 08 | also: agk-prop | level: CPL ME -->

| Key | Recall |
|---|---|
| `R` Cycle | Gas turbine: **INTAKE→COMPRESS→continuous COMBUST→TURBINE→EXHAUST**; turbine drives compressor; remaining energy → thrust/shaft. Piston: intermittent combustion. |
| `M` Turbojet | Core airflow → exhaust jet = principal thrust; no bypass fan. |
| `M` Turbofan | Fan + core; bypass air adds thrust; **BPR = bypass mass flow ÷ core mass flow** (5:1 = 5 bypass/1 core; **≠ thrust ratio**). |
| `M` Turboprop | Gas turbine → power shaft + reduction gearbox → **PROP** principal thrust (e.g. ATR); exhaust contributes some thrust. |
| `M` Turboshaft | Turbine → output shaft → rotor/accessory load; output not principally jet thrust. |
| `T` AFR ≠ BPR | **AFR = air mass ÷ fuel mass** (fuel mixture); **BPR = bypass/core airflow** (turbofan). |
| `R` Compressor | **Axial** successive rotor/stator rows; **centrifugal** impeller→radial diffuser. |
| `T` STAGE ≠ SPOOL | Compressor STAGE≈rotor+stator; turbine STAGE≈stator/nozzle+rotor. SPOOL=compressor+shaft+driving turbine; multi-stage spool ≠ multi-spool. |
| `R` N1/N2 | Typical two-spool turbofan: **N1 LP/fan**, **N2 HP/core** speeds; exact indications/configuration ACFT-specific. Free power turbine mechanically independent of gas-generator compressor spool. |
| `R` Pitch | Blade angle ↑ → **COARSE/HIGH** → PROP load ↑, RPM tendency ↓; angle ↓ → **FINE/LOW** → load ↓, RPM tendency ↑ (**given comparable power/airspeed**). Pitch≠blade AOA. |
| `R` Types | Fixed: no FLT pitch control; ground-adjustable: ground only; pilot variable: selectable angle; **constant-speed governor varies pitch to hold selected RPM** within stops; full-feathering or reversible only if installed. |
| `P` CS PROP | Typical piston: throttle→power/MP; PROP lever→governed RPM; lever FWD→high RPM/fine, AFT→lower RPM/coarse; pitch stops may prevent RPM hold. |
| `R` Feather | Near edge-on to airflow→**windmilling drag↓** after ENG failure; **≠ reverse**. |
| `R` ALPHA | Turboprop flight range: PROP governor varies blade angle to maintain selected RPM. |
| `R` BETA | Ground range aft of FLT idle: power lever schedules PROP blade angle (outside normal RPM governing). |
| `R` GROUND FINE | Low blade angle→low/near-zero forward thrust for taxi. |
| `R` REVERSE | Further BETA→negative blade angle→reverse thrust for ground deceleration; **BETA ≠ REVERSE** (reverse ⊂ beta, on equipped ACFT). |
| `!` BETA LIMIT | Normally **ground only**; observe FLT-idle gate and AFM limits; in-FLT BETA may cause loss of control/overspeed. |
| `T` SE vs ME | **Typical piston** SE non-feathering: governor oil P↑→pitch↑/RPM↓; **typical piston** ME full-feathering: oil P↑→pitch↓/RPM↑; oil P loss→counterweights/springs drive feather. **Not universal**; POH/AFM wins. |
| `!` OEI | Windmilling unfeathered failed PROP→large drag / climb loss; never feather unverified ENG. Flow + feather hardware: `see me-engine-failure-flow-generic`, `me-prop-governor-feather-l4-cross-ref`. |

- `SRC:` [FAA AFH Ch 15 · Alpha/Beta](https://www.faa.gov/sites/faa.gov/files/regulations_policies/handbooks_manuals/aviation/airplane_handbook/16_afh_ch15.pdf) · [FAA PHAK · engines/PROP](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/faa-h-8083-25c.pdf) · [FAA AFH · ME governor/feather](https://www.faasafety.gov/files/events/SO/SO15/2022/SO15118118/TransitionToMultiengineAirplanes.pdf) · [FAA AMT Powerplant · PROP](https://www.faa.gov/sites/faa.gov/files/09_amtp_ch7.pdf); aircraft POH/AFM controls.

***
#### Manifold pressure · MP — L4
<!-- id: sys-manifold-pressure-mp-l4 | from: 08 | also: agk-prop | level: CPL ME -->

| Key | Recall |
|---|---|
| `R` MP | **Absolute** intake-manifold P, **inHg**; **MP ≠ MAP** (missed approach point). |
| `M` OFF→IDLE | ENG OFF: **MP≈ambient P** (29.92 inHg at standard SL) → IDLE: throttle nearly closed + intake pumping → **MP↓↓** (typically ~10–15 inHg; ACFT-specific). |
| `R` POWER | Throttle↑→MP↑; constant-speed PROP lever→selected RPM; power depends on **MP+RPM+mixture/conditions**. |
| `R` ALT / TURBO | Naturally aspirated ALT↑→max MP↓; turbocharged ENG may maintain commanded MP up to critical ALT, within limits. |
| `S` ICE | Carb ice: fixed-pitch **RPM↓**; constant-speed **MP↓**, RPM initially governed. |
| `T` SQUARE / BOOST | **Over-square:** MP(inHg) > RPM/100 (25 inHg / 2300 RPM → 25>23); numerical only, often permitted. **Overboost:** MP above approved limit **for operating conditions / RPM** (may occur below redline); damaging. POH/AFM MP–RPM limits + sequence win. |

- `SRC:` [FAA PHAK · manifold pressure / constant-speed PROP](https://www.faa.gov/sites/faa.gov/files/pilot_handbook_1.pdf) · POH/AFM governs.

***
#### Diesel engines, FADEC, oil system venting
<!-- id: agk-diesel-fadec-oil-venting | level: CPL -->

- **Diesel (compression ignition)**: high compression heats air; injected fuel ignites without spark plugs. Usually Jet-A / diesel, turbocharged, single power lever, FADEC-controlled. No mixture, no magnetos, no carb ice.
- **FADEC** (full authority digital engine control): computer meters fuel, timing and (if equipped) prop for a single power lever setting; redundant channels + backup battery; failure → reverts to backup channel/mode per AFM.
- **Oil system venting** (breather): vents crankcase pressure (blow-by) overboard; blocked breather → pressure → oil forced out / seal failure; in cold, breather can **freeze** (moisture).
- `?:` general knowledge; no free TC or NAV CANADA text found. Check against a TC-recognized text (e.g. *From the Ground Up*, TC Flight Training Manual) in the fact-check pass.


***
#### Pebble
<!-- id: agk-engines-powerplant-pebble | level: PPL CPL ME -->

- ENGINE `AIR-FUEL-SPARK-COMPRESSION + timing | partial power may be temporary: keep a landing area | mags independent of master; bad P-lead = live mag | too rich: rough/fouling; too lean: high temps/detonation at high power; full rich may be over-rich at high DA`
- OIL `low P + high T → reduce power, land ASAP | gauge fault = diagnosis of exclusion | noise/vibration + oil indication = land now`
- POWERPLANT `JET exhaust | FAN bypass + core; BPR = bypass/core ≠ AFR = air/fuel | T-PROP gearbox → PROP | T-SHAFT shaft | STAGE ≠ SPOOL | FINE angle↓/RPM↑; COARSE angle↑/RPM↓ | CS governor holds RPM within stops | FEATHER drag↓ ≠ REVERSE | ALPHA governed RPM; BETA ground blade-angle lever; REVERSE ⊂ BETA; AFM limits | typical piston SE oil→coarse, ME oil→fine, oil loss→feather; POH wins | verify ENG before feather`
- MP `absolute inHg; MP ≠ MAP | OFF ≈ ambient → IDLE↓↓ | throttle↑ MP↑ | non-turbo ALT↑ → MPmax↓; turbo holds MP to critical ALT | carb ice: CS MP↓ / fixed RPM↓ | over-square = MP > RPM/100 (may be OK) | overboost = MP > approved limit (RPM-dependent)`
- DIESEL `compression ignition, Jet-A, FADEC single lever: no mixture, mags or carb ice | blocked/frozen breather → oil forced out`
***
