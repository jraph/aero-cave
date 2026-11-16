### PA-30 TWIN COMANCHE POH CORE — AV-CAVE
`L` limitation | `P` POH procedure | `N` POH note | `T` trap | `M` memory | `!` safety | `PERF` chart-dependent | Piper PA-30, normally aspirated, S/N 30-1 to 30-2000
`RELEASE:` `AIRCRAFT-REF` | `NOT FLIGHT AUTHORITY`
***
#### Source / status
<!-- id: pa30-sources | concepts: agk | kind: source | level: ME -->

- `SRC:` *Pilot's Operating Handbook and FAA Approved Airplane Flight Manual, Piper PA-30 Twin Comanche, 3600 lb gross weight, 1963–1969 (normally aspirated only), S/N 30-1 through 30-2000*, second issue (Aircraft Publications, 1993/1996; Section 2 rev. 1, 31 Dec 1996).
- `N:` compiled handbook: **only Section 2 (Limitations) is FAA approved**. This document or Piper Report 1269 or 1515 must be carried in the aircraft.
- `!:` STC supplements (e.g. higher gross weight, tip tanks, turbocharging, de-ice) change limitations, placards, procedures and performance. Supplement limitations are mandatory.
- `T:` the aircraft's own AFM, supplements, placards, equipment list, W&B and checklist prevail over this card.
***
#### Aircraft
<!-- id: pa30-identity-weights | concepts: agk-systems, me-train | level: ME -->

- Type certificate `A1EA` (5 Feb 1963), Normal category (CAR 3). 4 seats; optional 6 from S/N `30-902`.
- Engines: 2 × Lycoming `IO-320-B1A`, fuel-injected (Bendix RSA-5AD1), 4-cylinder, direct drive, `319.8 cu in`, `160 bhp @ 2700 rpm`, TBO `2000 h`.
- Propellers: Hartzell `HC-E2YL-2` hub / `7663-4` blades, 2-blade, constant speed, full feathering; diameter `72 in` (min `70`); pitch `12°` low, `78°` feathered.
- Weights: MTOW / MLW `3600 / 3600 lb`; with tip tanks `3725 lb`. Standard empty `2207 lb`; max useful load `1393 lb`.
- Wing: laminar flow NACA `64₂A215`, span `36.0 ft`, area `178 sq ft`, loading `20.2 lb/sq ft`; power loading `11.3 lb/bhp`.
***
#### Airspeed limitations
<!-- id: pa30-speeds | concepts: agk-vspeeds, me-vmc | level: ME -->

| Item | mph CAS | mph IAS | kt CAS | kt IAS | Meaning |
|---|---:|---:|---:|---:|---|
| `VNE` | `230` | `234` | `200` | `203` | never exceed |
| `VNO` | `194` | `197` | `169` | `171` | max structural cruise; smooth air only above |
| `VA @3600 lb` | `162` | `162` | `141` | `141` | manoeuvring / turbulent air penetration |
| `VA @2450 lb` | `135` | `134` | `117` | `116` | interpolate linearly between weights |
| `VLE` | `150` | `149` | `130` | `129` | max gear extended |
| `VLO` | `150` | `149` | `130` | `129` | max gear operating |
| `VFE` | `125` | `124` | `108` | `107` | max flap extended |
| `VMCA` | `90` | `88` | `78` | `76` | single-engine minimum control |
| `VS1` | `76` | `74` | `66` | `64` | stall, power off, clean |
| `VS0` | `69` | `69` | `60` | `60` | stall, power off, full flaps + gear down |

- `T:` the POH quotes speeds in **mph**; most ASIs on this type are marked in mph. Read the units on the aircraft's ASI.
- `T:` Section 4 and the emergency procedures quote single figures (e.g. `VMCA 90 mph / 78 kt`); these match the CAS column, while Section 2 gives IAS `88 mph / 76 kt` for VMCA. Do not mix the two.
- `L:` placards (CAS): VMC `90 mph`, VA `162 mph`, max gear down `150 mph`.
***
#### Airspeed-indicator markings
<!-- id: pa30-asi-markings | concepts: agk-vspeeds, agk-pitot, me-vmc | level: ME -->

| Marking | mph CAS | kt CAS | Meaning |
|---|---:|---:|---|
| red line | `230` | `200` | never exceed |
| yellow arc | `194–230` | `169–200` | caution, smooth air only |
| green arc | `76–194` | `66–169` | normal operating |
| white arc | `69–125` | `60–108` | flaps extended |
| red radial | `90` | `78` | `VMCA` |
| blue radial | `105` | `91` | `VYSE` (best single-engine rate of climb) |

- `N:` ASI colour markings are in **CAS**.
***
#### Engine / instrument limits
<!-- id: pa30-engine-instrument-limits | concepts: agk-engine, agk-inst | level: ME -->

| Instrument | Green | Caution | Red |
|---|---|---|---|
| tachometer | `500–2700 rpm` | — | `2700 rpm` max (takeoff and max continuous) |
| oil temperature | `120–245 °F` | yellow `60–120 °F` | `245 °F` max |
| oil pressure | `60–90 psi` | yellow `25–60` and `90–100 psi` | `25 psi` min, `100 psi` max |
| fuel flow | `0–16.0 gph` | — | `16.0 gph` (`7.0 psi`) max at sea level |
| cylinder head temperature | `200–500 °F` | — | `200 °F` min, `500 °F` max |
| instrument vacuum | `4.8–5.1 in Hg` | — | `4.8` min, `5.1` max |

- `L:` cowl flaps open on the ground and in climbs; never exceed `CHT 500 °F` or `oil 245 °F`.
- `N:` increasing or abnormally high fuel flow can indicate restricted injector lines or nozzles.
***
#### Weight / CG / baggage
<!-- id: pa30-handbook-limits | concepts: agk-wb | level: ME -->

| Weight | Forward limit | Aft limit |
|---:|---:|---:|
| `3600 lb` | `86.5 in` | `92.0 in` |
| `3200 lb` | `83.0 in` | `92.0 in` |
| `≤2450 lb` | `81.0 in` | `92.0 in` |

- `L:` straight-line variation between points. Datum `79 in` ahead of the wing leading edge (measured at station `65.5` / spanwise `97.0`).
- `L:` baggage `200 lb` (S/N 30-1 to 30-901 except 30-853); `250 lb` including seats in the baggage area (S/N 30-853 and 30-902 to 30-2000).
- `T:` baggage door is an emergency exit on later serials (placard: hold knob up, turn latch clockwise). Method and loading: `see agk-weight-balance`.
***
#### Manoeuvre / operational limits
<!-- id: pa30-manoeuvre-operational-limits | concepts: agk-load, agk-ops | level: ME -->

- `L:` Normal category: `+3.8 g` / `−1.52 g`. No inverted manoeuvres; aerobatics **including spins prohibited**.
- `L:` approved VFR and IFR, day and night, when equipped per the regulations.
- `L:` **flight into known icing prohibited** unless equipped with: wing and empennage boots (STC SA233EA), alcohol propeller anti-ice (STC SA184EA), heated windshield panel, heated pitot head and Piper antennas per the listed drawings.
- `L:` maximum altitude **FL200** (normally aspirated).
- `L:` flaps: takeoff `0–15°` (white arc on the flap indicator), landing `0–27°`.
- `L:` power-on stalls: do not exceed `2100 rpm`. Altitude loss in a power-off stall, gear and flaps up: `280 ft`. Practise stalls with at least `5000 ft` terrain clearance.
- `L:` stall warning is inoperative with the master switch off (placard).
- `T:` the green gear-down light dims with the instrument/navigation lights and may be invisible in daylight.
***
#### Fuel
<!-- id: pa30-traps | concepts: agk-fuel | level: ME -->

| Tanks | Capacity | Usable |
|---|---:|---:|
| main (inboard), 2 × 30 US gal | `60` | `54` (3 gal unusable each in critical attitudes) |
| auxiliary (outboard), 2 × 15 US gal | `30` | `30` |
| tip tanks (if installed), 2 × 15 US gal | `30` | `30` |

- `L:` minimum grade `91/96` (100LL).
- `P:` takeoff and landing: selectors **ON main (inboard) tanks**, electric fuel pumps **ON**. Cruise: main or auxiliary, pumps **OFF**.
- `L:` auxiliary and tip fuel **only in level cruise**; with tip tanks, use tip fuel first.
- `L:` placard: uncoordinated manoeuvres including slips of **≥30 s**, and fast taxi turns just before takeoff, can cause **power loss if the tanks in use are less than ¼ full**.
- `P:` strainers drain only the tank shown on the selector: drain about `5 s` per tank, each tank in turn.
- `P:` crossfeed (single-engine emergency, **level flight only**): inoperative side selector ON main or aux, operative side **CROSSFEED ON**. **Never both selectors on CROSSFEED.** Before landing: operative side ON its inboard main, inoperative side OFF, electric pump ON (operative side).
- `T:` fuel gauges show only the cells selected; bladders may not hold full rated capacity.
***
#### Oil
<!-- id: pa30-oil | concepts: agk-engine | level: ME -->

- `8 US qt` each engine; normal `6–7 qt`; minimum safe `2 qt`. Grade MIL-L-22851C. Typical consumption `0.40–0.50 qt/h`.
- `!:` on start, no oil pressure within `30 s` → stop engine and investigate.
***
#### Normal speeds — 3600 lb, sea level
<!-- id: pa30-normal-speeds | concepts: agk-vspeeds, me-oei | level: ME -->

| Operation | mph | kt |
|---|---:|---:|
| `VR` (flaps 0°) | `90` | `78` |
| `VX` | `90` | `78` |
| `VY` | `112` | `97` |
| best en-route climb | `130` | `113` |
| `VXSE` | `94` | `82` |
| `VYSE` (blue line) | `105` | `91` |
| `VSSE` (minimum intentional one-engine) | `97` | `84` |
| `VAPP` (flaps as required) | `95` | `83` |
| `VAPP` flaps 0° | `100` | `87` |
| `VAPP` IFR approach, clean | `120` | `104` |
| `VFE` recommended | `100` | `87` |
| `VLO` recommended | `125` | `108` |
| max range `VIMR` | `130` | `113` |
| max endurance `VIMD` | `100` | `87` |
| demonstrated crosswind | `20` | `17` |

- `N:` `VX` and `VY` decrease about `1 mph` per `100 lb` below gross. `VX` +`0.25 mph` and `VY` −`0.75 mph` per `1000 ft` density altitude; en-route climb speed −`0.75 mph` per `1000 ft`.
- `N:` demonstrated crosswind is not a limitation.
***
#### Run-up
<!-- id: pa30-run-up | concepts: agk-engine, agk-prop | level: ME -->

- `P:` warm-up `2–4 min` at `800–1200 rpm`. Above `5000 ft` density altitude, lean for takeoff only until roughness stops.
- `P:` at `2000 rpm`: cycle propeller (normal drop `300–400 rpm`). Do not exceed `2200 rpm` in a static test.
- `P:` feather check at `1000–1500 rpm`: in and out of feather **rapidly**, drop **≤500 rpm**.
- `P:` magnetos: max drop `175 rpm`, max difference `50 rpm`. Vacuum `5.0 in Hg` (+0.1 / −0.2). Alternator press-to-test outputs about equal.
***
#### Takeoff / climb
<!-- id: pa30-takeoff-climb | concepts: agk-perfcalc, agk-ops | level: ME -->

- `P:` before takeoff: selectors on mains, electric pumps ON, flaps `0–15°`, trim set (neutral for most operations), cowl flaps open.
- `P:` normal: rotate at `90 mph (78 kt)`, positive rate → tap brakes, gear up (amber light), climb at `VY 112 mph (97 kt)`. Reduced-power climb: full power to `1000 ft AGL`, then `25 in / 2500 rpm`, `130 mph (113 kt)`, CHT green.
- `P:` short field: flaps `15°`, partial power before brake release, rotate at `70–80 mph (61–70 kt)` depending on weight, `VX 90 mph (78 kt)` to clear the obstacle, then `VY`, gear and flaps up.
- `P:` soft field: flaps `15°`, full back pressure, keep moving, stay in ground effect to `VX`, gear up, positive rate, `VY`, flaps up.
- `P:` climb: mixtures adjusted with ascent; pumps OFF at altitude (check fuel flow); cowl flaps closed at altitude. Below `5000 ft MSL`, mixture full rich before increasing power.
- `!:` runway length should exceed accelerate-stop distance. Sluggish or rough engine early in the roll → abort.
***
#### Cruise / descent
<!-- id: pa30-cruise-descent | concepts: agk-engine, agk-ops | level: ME -->

- `P:` normal maximum cruise power `75 %`; set power from the Section 5 power table. Mixture by EGT: `100 °F` rich of peak at `75 %`, `50 °F` rich of peak at `65 %`.
- `P:` propellers synchronized (optional synchrophaser slaves right to left within `50 rpm`).
- `P:` descent: cruise rpm, `15–17 in` MP, keep CHT in the green, enrich with descent.
- `T:` the POH oxygen note (above `12,500 ft`) is US guidance; Canadian requirement: `see law-oxygen-oxyg-ne-car-605-31-32`.
***
#### Approach / landing / go-around
<!-- id: pa30-approach-landing | concepts: agk-ops, agk-perfcalc | level: ME -->

- `P:` approach: electric pumps ON, selectors on mains, gear down below `125 mph (108 kt)` recommended, flaps below `100 mph (87 kt)` recommended, cowl flaps open, propellers `2400 rpm`, GUMP check on final, `VAPP 95 mph (83 kt)`.
- `P:` crosswind component above `12 kt`: partial or no flaps, approach faster than normal.
- `P:` short field: `90 mph (78 kt)` on final, power until the flare, flaps up right after touchdown, full back pressure, heavy braking.
- `P:` soft field: `90 mph (78 kt)` on final, power until the flare, flaps left down, back pressure, minimum braking.
- `P:` go-around: propellers forward, throttles full, rotate, positive rate, move to the right of the runway, gear up, `VY 112 mph (97 kt)`, flaps up, reduce power above `1000 ft AGL`, `130 mph`.
- `P:` shutdown: idle until CHT drops, `1800 rpm` for `15–20 s` to clear plugs, `1200 rpm`, mixtures idle cut-off. Hot day: also press the throttle cut-off release button and pull throttles fully aft.
***
#### Engine failure — identify, takeoff, climb
<!-- id: pa30-engine-out | concepts: me-fail, emg-engine | level: ME -->

- `P:` identify: **dead foot, dead engine** (rudder needed on the good-engine side). Verify: partially retard the suspected throttle; no change in control pressure or sound = correct engine. MP and rpm read near normal: **do not use them to identify**.
- `P:` takeoff, below `90 mph IAS (78 kt)`: both throttles closed, maximum braking. Not enough runway: fuel selectors OFF, master OFF, straight ahead, avoiding obstacles.
- `P:` takeoff, `90–105 mph IAS (78–91 kt)`: **pilot decides** to abort or continue: runway left, weight, density altitude, obstacles, weather, ability.
- `P:` takeoff, at or above `105 mph IAS (91 kt)`: runway left → land straight ahead. Otherwise gear up, flaps up, hold `VYSE 105 mph (91 kt)`, then climb flow.
- `P:` climb: `VYSE 105 mph (91 kt)` → identify + verify → rudder toward live engine → **bank 5° into live engine**, ball **½ width toward live engine** → live engine full power → secure.
- `!:` in flight below `VMCA (90 mph)`: reduce power on **both** engines and lower the nose to regain control, accelerate to `105 mph`, then the same flow with power as required.
- Why 5° bank and ½ ball: `see me-zero-sideslip-best-oei-performance`.
***
#### Securing, air start
<!-- id: pa30-secure-restart | concepts: me-fail, agk-prop | level: ME -->

- `P:` before securing: fuel selector to a tank with fuel (crossfeed as required), electric pump ON, ignition ON, mixture full rich, alternate air ON, check gauges for cause. Power back → pump OFF, alternate air OFF.
- `P:` cannot restore: mixture idle cut-off → fuel selector OFF → electric pump OFF → magnetos OFF → cowl flap closed → **propeller FEATHER** → generator/alternator OFF → reduce load. Land at the nearest suitable airport.
- `T:` Section 2 (approved) orders the feather sequence: live engine throttle to hold altitude and **>97 mph** → dead throttle closed → mixture idle cut-off → prop feather → ignition OFF → pumps OFF → fuel OFF. Section 3 lists the same items in another order: follow the aircraft's checklist.
- `N:` feathering by dry nitrogen, about `3 s`, prop control fully aft through the low-rpm range.
- `P:` air start: magnetos ON, mixture rich, fuel ON, pump ON, throttle `¼ in` open, prop forward to cruise, starter until windmilling; when running: adjust controls, oil pressure check, pump OFF, cowl flap as required, alternator ON; warm at about `2000 rpm / 15 in`.
***
#### Single-engine landing, go-around, training
<!-- id: pa30-se-landing-goaround-training | concepts: me-fail, me-oei, me-train | level: ME -->

- `P:` single-engine landing, once the field is assured: gear down, flaps `15°`, blue line `105 mph (91 kt)`.
- `P:` single-engine go-around: full power, rudder toward live engine, 5° bank, ½ ball, gear up, flaps up, `VYSE 105 mph (91 kt)`.
- `!:` **the aircraft will not climb with gear and flaps extended** on one engine.
- `P:` simulated engine failure: below `125 mph (109 kt)`, at least `5000 ft` terrain clearance, experienced ME instructor. Never fail an engine below `VSSE 97 mph (84 kt)`; on one engine, do not let speed fall below blue line `105 mph`.
- `N:` wings level with ball centred can raise VMCA by up to `20 kt` and cut single-engine climb by up to `300 ft/min`.
***
#### Power-off landing — both engines
<!-- id: pa30-power-off-landing | concepts: emg-engine | level: ME -->

- `P:` best glide `110 mph (96 kt)` at gross weight, propellers **feathered**; endurance glide `90 mph (78 kt)`. `121.5 MHz`, transponder `7700`, MAYDAY if time permits.
- `P:` gear-down landing: ELT on, throttles closed, fuel selectors OFF, mixtures idle cut-off, ignition OFF, harness tight, door block open, flaps as required; **gear down just before touchdown** (extension about `7 s`; glide ratio drops sharply), master OFF, touch down at the slowest possible speed.
- `P:` gear-up landing only if the surface is too soft or rough, the field is too short, or ditching: flaps up, then the same shut-off items.
***
#### Fires
<!-- id: pa30-fires | concepts: emg-fire | level: ME -->

- `P:` engine fire on start: keep cranking, mixture idle cut-off, throttle open, pump OFF, fuel selector OFF; still burning → extinguish with best means, radio for help.
- `P:` electrical fire / smoke: master OFF, vents open, door open as an exhaust if needed, cabin heater OFF, oxygen as required. Land as soon as possible **without flaps**, `VAPP 100 mph (87 kt)`, manual gear extension.
- `P:` engine fire in flight: throttle closed, mixture idle cut-off, fuel selector OFF, pump OFF; then the engine power-loss flow (feather).
***
#### Electrical failures
<!-- id: pa30-electrical-failure | concepts: agk-elec, emg-sys | level: ME -->

- `N:` 12 V system: two 50 A generators or two 70 A non-paralleling alternators. Generators give no output below `1200 rpm`.
- `P:` alternators: ammeter shows battery charge; press-to-test shows each alternator. One reads zero → shed load until charging; tripped breaker → minimum load, wait `2–5 min`, reset **once**.
- `P:` both zero: minimum load → voltage regulator selector **AUX** → reset regulator breakers. Not restored: selector back to MAIN, both alternator breakers OFF, reset the overvoltage relay (master OFF ≥`6 s`, then ON), bring alternators back one at a time to find the faulty one.
- `!:` alternator breakers and regulator selector are not operated with engines running except in an emergency.
- `P:` battery depleted: land **without flaps**, `VAPP 100 mph (87 kt)`, manual gear extension. Gear lights and warning horn are lost with electrical power.
***
#### Engine abnormals
<!-- id: pa30-engine-abnormal | concepts: agk-engine, emg-engine | level: ME -->

- `P:` high oil temperature / CHT: cowl flaps open, enrich, reduce power if needed, keep above `130 mph (113 kt)`; land as soon as possible, prepare for engine failure.
- `P:` loss of oil pressure: land as soon as possible, prepare for engine failure.
- `P:` loss of fuel pressure (most often fuel exhaustion from mismanagement): selector to a tank with fuel, pump ON, enrich; not regained → pump OFF, engine-failure flow.
- `P:` induction icing (first sign: **fuel-flow drop**, then roughness): alternate air full ON, throttle full open, mixture for smoothness; when clear → alternate air OFF, cruise power, lean by EGT.
- `P:` engine roughness: alternate air ON; after `1 min` still rough → alternate air OFF, then mixture for smoothness, pump ON, switch tanks, gauges, magnetos L / R / both. Runs on one magneto → reduced power to the nearest airport.
- `P:` propeller overspeed: prop control aft, throttle back, slow down, stay below `2700 rpm`, feather if needed; land as soon as possible.
- `N:` the induction air door opens automatically if the filter blocks; ALT AIR operates it manually.
***
#### Vacuum, open door, manual gear extension
<!-- id: pa30-vacuum-door-gear | concepts: agk-gyro, agk-systems, emg-sys | level: ME -->

- `N:` dual vacuum pumps; an indicator shows the failed side and the other pump carries the load.
- `P:` suction below `4.8 in Hg`: rpm `2700`, descend to keep `4.8`; cross-check the gyros with the electric turn coordinator and compass; else partial panel.
- `P:` open door: below `100 mph (87 kt)`, vents closed, storm window open, slip with the door into the wind, latch. Not dangerous; if it won't close, land at about `+10 mph`.
- `P:` gear won't extend: check master ON and gear breakers. Below `100 mph (87 kt)`: selector DOWN LOCKED (two-position) or centre OFF (three-position); disengage the motor release arm and push it fully forward; extension handle per the placard, rotate **fully forward** until locked; green light ON.
- `!:` **do not re-engage the gear motor in flight**; do not retract with the handle in its socket; after landing avoid crosswind and fast taxi turns.
- `P:` gear works but no green light: navigation lights OFF (dimming), replace the bulb.
***
#### Spin recovery, emergency descent
<!-- id: pa30-spin-descent | concepts: emg-ua, agk-stall | level: ME -->

- `P:` spin (intentional spins prohibited): throttles idle → ailerons neutral → **full rudder opposite** the rotation → wheel **briskly full forward** → rudder neutral when rotation stops → smooth back pressure, without exceeding VA or the load limit. Aileron against the rotation can speed recovery.
- `P:` emergency descent: harness secure, throttles back, propellers full forward, gear down below `150 mph (130 kt)`, keep below `150 mph`; `2000–3000 ft/min` limits engine and passenger stress. Recover by `10,000 ft MSL` or `2000 ft AGL`. When getting down fast outweighs everything (uncontrolled fire): spiral at `40–45°` bank.
***
#### Systems
<!-- id: pa30-systems | concepts: agk-systems, agk-fuel | level: ME -->

- Flight controls: stabilator with anti-servo tab; rudder–aileron interconnect (cable and spring); rudder trim is a bungee to the nose-gear steering; electric Fowler flaps `0–27°`, any position. The right flap locks only when up (step).
- Landing gear: electric motor, all three legs mechanically linked; nose steering `40°` arc, disconnected on retraction; squat switch on the left main; selector shaped like a wheel, guarded, pull aft to select UP.
- Gear warnings: horn if gear not down and locked with MP below about `12 in` on both engines (and on the ground with UP selected); amber gear-up light flashes when one engine is below `12 in`; green = all three down and locked.
- Brakes: toe brakes or hand lever; one reservoir; parking brake T-handle needs brake pressure to set.
- Fuel: rubber bladders, NACA anti-icing vents; engine-driven pump plus electric pump (start, takeoff, landing, tank changes, engine-driven pump failure).
***
#### Performance — headline specifications
<!-- id: pa30-performance | concepts: agk-perfcalc, me-oei | level: ME -->

| Item (3600 lb, standard day, sea level) | Value |
|---|---|
| max speed | `205 mph / 178 kt` |
| cruise 75 % @ 8000 ft | `194 mph / 169 kt` (`17.2 gph` total) |
| cruise 65 % @ 12,000 ft | `186 mph / 162 kt` (`15.2 gph`) |
| cruise 55 % @ 16,000 ft | `172 mph / 149 kt` (`13.4 gph`) |
| rate of climb, both engines / one engine | `1460 / 260 ft/min` |
| climb gradient, both / one engine | `903 / 171 ft/NM` |
| takeoff, flaps 15°: ground run / over 50 ft | `1250 / 2160 ft` |
| landing, full flaps: ground roll / over 50 ft | `700 / 2100 ft` |
| accelerate-stop, flaps 15° (VMCA 90 mph) | `3000 ft` |
| service ceiling, both / one engine | `18,600 / 5800 ft` |
| absolute ceiling, both / one engine | `20,000 / 7100 ft` |

- `PERF:` charts are unfactored, ICAO standard day; grass, slope and winds aloft are not included. Range and endurance figures include start, taxi, climb, descent and `45 min` reserve, best-economy mixture.
- `T:` single-engine service ceiling `5800 ft` at gross: a hot day or high field can leave no single-engine climb at all.
***
#### Pebble
<!-- id: pa30-pebble | concepts: agk | kind: pebble | level: ME -->

- `3600 lb` (tips `3725`) | CG `86.5–92.0 @3600`, `81.0 @≤2450` | `+3.8 / −1.52 g` | FL200 | no spins, no known icing unless equipped
- speeds mph CAS/IAS: `VNE 230/234` | `VNO 194/197` | `VA 162 @3600` | `VLE/VLO 150/149` | `VFE 125/124` | `VMCA 90/88` | `VS1 76/74` | `VS0 69`
- `VR 90` | `VX 90` | `VY 112` | `VXSE 94` | `VYSE 105` blue | `VSSE 97` | `VAPP 95` (flaps 0 `100`) | glide `110` feathered
- engines `IO-320-B1A 160 hp @2700` | oil `8 / 6–7 / min 2 qt` | oil `25–100 psi`, `≤245 °F` | CHT `≤500 °F` | fuel `54` usable mains + `30` aux (+`30` tips)
- fuel `TKOF/LDG mains + pumps ON | aux/tip level cruise only | <¼ tank + slip ≥30 s = power loss | crossfeed level flight, never both`
- EFATO `<90 abort | 90–105 decide | ≥105 gear/flaps up, 105, identify-verify-feather` | climb `5° bank + ½ ball to live engine`
- SE `will not climb gear + flaps down` | SE landing `flaps 15°, 105` | SE ceiling `5800 ft`
- manual gear `<100 mph, motor released, handle full forward, never re-engage motor`
- spin `IDLE-AIL NEUT-OPP RUD-FWD-NEUT-RECOVER`
