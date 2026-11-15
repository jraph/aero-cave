# CAP plate reading / Lecture des cartes CAP
<!-- concept: ifr-plates | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-plates` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### CAP plate read flow
<!-- id: ifr-cap-plate-read-flow | from: 10 -->

- `P:` title/effective→airport/runway/proc→nav source/freq/course→MSA/Safe100/terrain→RASS/cold temp→IAF/IF/FAF/FAP→stepdowns→DA/MDA/HAT/HAA/HATh/DH→advisory vis→MAP→missed→lighting/runway/LDA→notes.
- `T:` wrong frequency/source/course = common trap. Always verify CDI source and loaded procedure.
- `T:` plan view altitude is not enough; profile and minima notes can modify it.
- `M:` `TITLE-NAV-PLAN-PROFILE-MIN-MISSED-NOTES-RWY`.
- `T:` don’t start with minima only; plate errors usually come from source/fix/altitude/missed/notes.
***
#### CAP transition watch
<!-- id: ifr-cap-transition-watch | from: 09 | also: nav-pubs -->

- AIC `013/2026`: PFAF/glidepath-intercept depiction using a lightning-bolt symbol.
- Incremental implementation from `2026-10-29`, the cycle current at last review (14 Nov 2026). `?` not yet confirmed on a printed chart.
- Conversion is incremental: read the symbols printed on the chart in hand; do not assume either convention.
***
#### Publication cycle
<!-- id: ifr-current-publication-cycle | from: 09 | also: nav-pubs | kind: source -->

- AIRAC cycle at last review (14 Nov 2026) for `CAP/CAP GEN/CFS/AIP/DAH/charts`: effective `2026-10-29` through `2026-12-24`. `T:` this line ages every 56 days; read the effective dates printed on the product.
- These publications update every `56 days`; AIP SUP/AIC publish on a `14-day` cycle.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### Publication-currency exam traps
<!-- id: ifr-publication-currency-exam-traps | from: 10 | also: nav-pubs | kind: trap -->

- Check effective date/cycle first. Then NOTAM and AIP SUP; Trigger NOTAM only points to changed material.
- AIP SUP can remain active with no current Trigger NOTAM.
- PFAF lightning-bolt depiction is an incremental standard from `2026-10-29`; answer from the symbology printed on the chart given.
- `T:` wrong-cycle plate may produce a numerically correct but operationally invalid answer.
- `G:` chart effective/current→procedure not cancelled/replaced→NOTAM reviewed→AIP SUP reviewed→NAVAIDs/runway/lights available→database current.
- `T:` a plate matching the current 56-day cycle can still be amended or unavailable.
***
#### Source / scope
<!-- id: plate-source-scope | from: 11 | kind: source | level: IR -->

- `SRC:` current CAP/CAP GEN/CFS/NOTAM/AIP SUP win. Cycle at last review (14 Nov 2026): `2026-10-29` to `2026-12-24`.
- CAP contains IFR arrival/departure information: IAP, SID, STAR, visual approaches, noise abatement and aerodrome/ground charts.
- CAP is not intended for VFR operations and is regularly amended by NOTAM/AIP SUP.
- `T:` stale plate = no-go. Trigger NOTAM≠the amendment; retrieve referenced material.
***
#### Title block
<!-- id: plate-title-block | from: 11 | level: IR -->

- Check airport name/ICAO, procedure title, runway, amendment/effective date, page/cycle, units, notes.
- Procedure title tells primary nav basis: `ILS`, `LOC`, `RNAV (GNSS)`, `VOR`, `NDB`, `DME`, `RNP AR` etc.
- `T:` runway number/procedure variant matters; `ILS RWY 24` ≠ `LOC RWY 24` ≠ `RNAV (GNSS) RWY 24`.
***
#### Required equipment / approval
<!-- id: plate-required-equipment-approval | from: 11 | level: IR -->

- Confirm aircraft and pilot authorized/equipped: NAV receiver, DME, ADF, GNSS/WAAS, Baro-VNAV, RNP AR, comms, transponder, database.
- `T:` if equipment/navaid/database not usable, that line/minima may be unavailable.
- `T:` GNSS overlay/direct-to does not make a non-GNSS procedure a GNSS approach unless authorized/published.
***
#### Plan view
<!-- id: plate-plan-view | from: 11 | level: IR -->

- Read IAF/IF/FAF/FAP, transitions, arcs, bearings/radials/tracks, distances, holds, MSA/Safe 100 NM/sector altitudes, terrain, restricted areas.
- `T:` plan view gives lateral path; profile gives vertical constraints. Need both.
- `T:` arc/radial orientation: VOR radials are FROM station; bearings to NDB are TO station.
***
#### MSA / Safe altitude / terrain
<!-- id: plate-msa-safe-altitude-terrain | from: 11 | level: IR -->

- MSA/sector altitude = emergency/sector obstacle clearance near reference point; not necessarily ATC minimum vectoring altitude.
- Check terrain symbols, obstacles, minimum sector altitude, procedure notes, cold-temp notes.
- `T:` MSA is not a clearance to descend on the procedure.
***
#### Notes block
<!-- id: plate-notes-block | from: 11 | level: IR -->

- Read all notes: NA at night, procedure NA, GNSS required, DME required, circling restrictions, approach-angle notes, lighting notes, altimeter/RASS, temperature, missed-climb gradient.
- `T:` notes can override the attractive minima line.
- `M:` if a note starts with `NA`, `Use`, `When`, `Requires`, or `Circling`, slow down.
***
#### Real-flight plate method
<!-- id: plate-real-flight-plate-method | from: 11 | kind: trap | level: IR -->

- `1` current plate/NOTAM; `2` legal/equipped; `3` fuel/alternate; `4` terrain/icing/TS/wind; `5` setup/brief; `6` monitor stable approach; `7` miss early if doubt.
- `T:` legal minimums are not personal minimums. Low-vis approaches invite confirmation bias.
***
#### Pebble
<!-- id: ifr-cap-plates-publications-pebble -->

- CYCLE `publications every 56 days; AIP SUP/AIC every 14 days | cycle dates age: read the effective dates printed on the product | preflight: current publication → NOTAM → AIP SUP/AIC → airport/procedure page → ACFT data`
- TRIGGER NOTAM `only announces changed source material: open the referenced source | AIP SUP can remain active after the Trigger NOTAM expires`
- PLATE `title/effective → airport/RWY/proc → nav source/freq/course → MSA → RASS/cold temp → fixes → stepdowns → minima → MAP → missed → lighting/RWY → notes | plan-view altitude not enough: profile and minima notes can modify it`
- T `wrong-cycle plate = numerically correct, operationally invalid | PFAF lightning-bolt (AIC 013/2026): incremental from 2026-10-29, use the symbols printed on the chart`
- TRAPS `category first | the note block can kill the approach | RASS adds to altitudes / may force circling | cold temp protects obstacle clearance | MAP timing uses GS | LPV≠ILS | LOC line≠ILS line | wrong CDI source kills | legal approach≠landing distance OK`
***
