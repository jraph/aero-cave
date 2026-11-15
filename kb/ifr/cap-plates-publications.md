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

- AIC `013/2026`: lightning-bolt symbol for the PFAF/glidepath-intercept altitude on vertically guided procedures.
- Incremental implementation from `2026-10-29`. `?` not yet confirmed on a printed chart.
- Co-charted procedures may show both: Maltese cross for the non-vertical FAF + lightning bolt for the PFAF.
- Conversion is incremental: read the symbols printed on the chart in hand; do not assume either convention or reinterpret existing plates.
***
#### Publication-currency exam traps
<!-- id: ifr-publication-currency-exam-traps | from: 10 | also: nav-pubs | kind: trap -->

- Check effective date/cycle first, then NOTAM and AIP SUP: cycle, Trigger NOTAM and AIP SUP rules in `ref-current-publication-cycle-c01`; PFAF symbol in `ifr-cap-transition-watch`.
- `T:` wrong-cycle plate may produce a numerically correct but operationally invalid answer.
- `G:` chart effective/current→procedure not cancelled/replaced→NOTAM reviewed→AIP SUP reviewed→NAVAIDs/runway/lights available→database current.
- `T:` a plate matching the current 56-day cycle can still be amended or unavailable.
***
#### Source / scope
<!-- id: plate-source-scope | from: 11 | kind: source | level: IR -->

- `SRC:` current CAP/CAP GEN/CFS/NOTAM/AIP SUP win; cycle and Trigger NOTAM: see `ref-current-publication-cycle-c01`.
- CAP contains IFR arrival/departure information: IAP, SID, STAR, visual approaches, noise abatement and aerodrome/ground charts.
- CAP is not intended for VFR operations and is regularly amended by NOTAM/AIP SUP.
- `T:` stale plate = no-go (see `ifr-publication-currency-exam-traps`).
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
- `T:` arc/radial orientation: see `ifr-ils-loc-vor-ndb-dme`.
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

- CYCLE `cycle, preflight order, Trigger NOTAM/AIP SUP → ref-current-publication-cycle-c01 | stale plate = no-go`
- GATE `chart effective → procedure not cancelled → NOTAM → AIP SUP → NAVAIDs/RWY/lights → database current | current-cycle plate can still be amended/unavailable`
- PLATE `title/effective → airport/RWY/proc → nav source/freq/course → MSA → RASS/cold temp → fixes → stepdowns → minima → MAP → missed → lighting/RWY → notes | plan-view altitude not enough: profile and minima notes can modify it`
- T `wrong-cycle plate = numerically correct, operationally invalid | PFAF lightning-bolt (AIC 013/2026): incremental from 2026-10-29, vertically guided procedures; co-charted Maltese cross + bolt; use the symbols printed on the chart`
- TRAPS `category first | the note block can kill the approach | RASS adds to altitudes / may force circling | cold temp protects obstacle clearance | MAP timing uses GS | LPV≠ILS | LOC line≠ILS line | wrong CDI source kills | legal approach≠landing distance OK`
***
