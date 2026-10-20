### CAP PLATE READING QRC — AV-CAVE v0.2
`SEPTEMBER CPAER REVIEW: retained reference, not freshly revalidated` | use exact aircraft/current operational sources
`P` procedure | `R` rule | `T` trap | `M` memory | `!` safety | `?` verify | Canada CAP / IFR / INRAT
`RELEASE:` `OPS/CYCLE-REF PROVISIONAL` | `CANONICAL SOURCE:` `cap_plate_reading_qrc_av_cave_v0_2.md` | `NOT FLIGHT AUTHORITY`
***
#### Current publication cycle

- Current `CAP/CAP GEN/CFS/AIP/DAH/charts` AIRAC cycle: effective `2026-07-09` through `2026-09-03`.
- These publications update every `56 days`; AIP SUP/AIC publish on a `14-day` cycle.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### Source / scope

- `SRC:` current CAP/CAP GEN/CFS/NOTAM/AIP SUP win. Current cycle: `2026-07-09` to `2026-09-03`.
- CAP contains IFR arrival/departure information: IAP, SID, STAR, visual approaches, noise abatement and aerodrome/ground charts.
- CAP is not intended for VFR operations and is regularly amended by NOTAM/AIP SUP.
- `T:` stale plate = no-go. Trigger NOTAM≠the amendment; retrieve referenced material.
***
#### 10-second plate scan

- `P:` title/effective→airport/runway/procedure→nav source/freq/course→plan view→profile→minima→missed→notes→lighting/runway→brief threats.
- `M:` `TITLE-NAV-PLAN-PROFILE-MIN-MISSED-NOTES-RWY`.
- `T:` don’t start with minima only. Plate errors usually come from source/fix/altitude/missed/notes.
***
#### Currency gate

- `G:` chart effective/current→procedure not cancelled/replaced→NOTAM reviewed→AIP SUP reviewed→NAVAIDs/runway/lights available→database current.
- AIP SUP may remain effective after its short-lived Trigger NOTAM disappears.
- `T:` a plate matching the current 56-day cycle can still be amended or unavailable.
***
#### Title block

- Check airport name/ICAO, procedure title, runway, amendment/effective date, page/cycle, units, notes.
- Procedure title tells primary nav basis: `ILS`, `LOC`, `RNAV (GNSS)`, `VOR`, `NDB`, `DME`, `RNP AR` etc.
- `T:` runway number/procedure variant matters; `ILS RWY 24` ≠ `LOC RWY 24` ≠ `RNAV (GNSS) RWY 24`.
***
#### Required equipment / approval

- Confirm aircraft and pilot authorized/equipped: NAV receiver, DME, ADF, GNSS/WAAS, Baro-VNAV, RNP AR, comms, transponder, database.
- `T:` if equipment/navaid/database not usable, that line/minima may be unavailable.
- `T:` GNSS overlay/direct-to does not make a non-GNSS procedure a GNSS approach unless authorized/published.
***
#### Frequencies / nav source

- `P:` set/identify nav aid; verify Morse/voice where applicable; set inbound course/front course; cross-check GPS/database.
- `T:` wrong CDI source is lethal: green needles vs magenta needles vs raw data.
- `T:` ILS front course set even when autopilot/GPS displays course automatically; know equipment.
***
#### Plan view

- Read IAF/IF/FAF/FAP, transitions, arcs, bearings/radials/tracks, distances, holds, MSA/Safe 100 NM/sector altitudes, terrain, restricted areas.
- `T:` plan view gives lateral path; profile gives vertical constraints. Need both.
- `T:` arc/radial orientation: VOR radials are FROM station; bearings to NDB are TO station.
***
#### MSA / Safe altitude / terrain

- MSA/sector altitude = emergency/sector obstacle clearance near reference point; not necessarily ATC minimum vectoring altitude.
- Check terrain symbols, obstacles, minimum sector altitude, procedure notes, cold-temp notes.
- `T:` MSA is not a clearance to descend on the procedure.
***
#### Initial / intermediate segment

- Identify crossing altitudes and restrictions before FAF/FAP.
- Stepdown fixes: confirm fix source and altitude. If fix cannot be identified, stepdown may be unusable.
- `T:` “at or above” altitude is a floor, not a target to duck under early.
***
#### PFAF depiction transition

- Current July 2026 cycle: use the symbols actually printed on the plate.
- From `2026-10-29`, NAV CANADA plans incremental use of a lightning-bolt symbol for the PFAF/glidepath-intercept altitude on vertically guided procedures.
- Future co-charted procedures may show both: Maltese cross for non-vertical FAF + lightning bolt for PFAF.
- `T:` this is a future incremental change, not a blanket reinterpretation of current plates.
***
#### FAF / FAP

- FAF often Maltese-cross-like symbol on NPA; FAP for precision/APV intercept of final descent path.
- `P:` before FAF/FAP: correct nav source, approach mode, altimeter, brief complete, landing config plan, missed set, timer if required.
- `T:` after FAF, workload jumps; if not configured/briefed, go around or delay.
***
#### Profile view

- Read inbound course, crossing altitudes, stepdowns, descent angle, distance to threshold/MAP, MDA/DA relationship.
- For NPA: manage MDA, MAP, timing/DME/fix. For precision/APV: manage DA and vertical path.
- `T:` advisory descent angle/CDFA does not authorize descent below MDA without required visual reference.
***
#### Descent math

- `F 3°:` ROD≈`GS×5`.
- `F:` descent gradient fpm=`GS×ft/NM/60`.
- `F:` distance to lose altitude≈`altitude to lose/300` for 3°.
- `T:` use groundspeed. Stepdowns and level-offs change the simple 3° plan.
***
#### Minima box scan

- Read aircraft category first: `A/B/C/D/E` by final approach speed category.
- Identify line: `ILS/LOC/LNAV/LNAV-VNAV/LPV/VOR/NDB/circling`.
- Extract: `DA/DH` or `MDA`; `HAT/HATh/HAA`; advisory visibility; notes/lighting penalties; RASS/cold-temp impacts.
- `T:` wrong category = wrong protected area/minima. Faster circling speed can force higher category.
***
#### Minima definitions

| Item | Use |
|---|---|
| `DA` | decision altitude; missed if visual ref not established |
| `DH` | height above threshold/TDZE reference |
| `MDA` | minimum descent altitude; do not descend below until visual ref |
| `HAT/HATh` | height above touchdown/threshold, straight-in |
| `HAA` | height above aerodrome, circling |
| `Vis` | advisory / approach-ban planning value, not DA/MDA itself |

- `T:` DA/MDA controls vertical descent; RVR/vis controls approach-ban/planning/success probability.
***
#### Visual reference rule

- Do not continue below DH/DA or descend below MDA unless required visual reference is established and maintained for safe landing.
- Visual references may include runway/markings/threshold/TDZ/approach lights/VGSI/RIL/threshold-end lights/edge/centreline/TDZ lights.
- `T:` “I see glow/lights” may not be enough; must support safe continuation/landing.
***
#### Approach type memory

| Type | Vertical? | Minimum |
|---|---|---|
| `ILS` | precision vertical | `DA/DH` |
| `LOC` | lateral only | `MDA` |
| `LNAV` | lateral only | `MDA` |
| `LNAV/VNAV` | APV vertical | `DA` |
| `LPV` | APV vertical-like | `DA` |
| `VOR/NDB` | lateral/non-precision | `MDA` |
| `Circling` | visual manoeuvre | `MDA/HAA` |

- `T:` `LPV` is not ILS. `LNAV/VNAV` often temperature/Baro-VNAV limited.
***
#### RASS / altimeter source

- Read altimeter source line before minima. Approved altimeter setting source drives procedure protection.
- `Use CYXX`: procedure designed/minima already based on that source.
- `When using CYXX add N ft`: add correction to relevant intermediate/final/missed minimum altitudes.
- `When using CYXX add N ft; circling minima apply`: straight-in not usable under that remote setting case.
- `T:` RASS is not optional arithmetic decoration; it can invalidate straight-in minima.
***
#### Cold temperature

- Check CAP cold-temp notes / temperature limits / uncompensated Baro-VNAV restrictions.
- Apply required altitude corrections to procedure altitudes as applicable; ATC cleared altitude may need coordination if correction affects assigned altitude.
- `T:` cold correction protects obstacle clearance; it does not change aircraft altimeter reading.
***
#### Notes block

- Read all notes: NA at night, procedure NA, GNSS required, DME required, circling restrictions, approach-angle notes, lighting notes, altimeter/RASS, temperature, missed-climb gradient.
- `T:` notes can override the attractive minima line.
- `M:` if a note starts with `NA`, `Use`, `When`, `Requires`, or `Circling`, slow down.
***
#### Missed approach

- Brief before FAF: initial climb, turn direction/altitude, fix/hold, nav source, frequencies, climb gradient, special notes.
- At DA/MDA/MAP without required visual ref or unstable/unsafe: power→attitude→config→track missed.
- `T:` missed after MAP may not ensure obstacle clearance. Do not continue level past MAP hunting runway.
***
#### MAP identification

- Precision/APV: DA/DH on glidepath is decision point.
- NPA: MAP may be timing, DME, waypoint, station passage, runway threshold, or defined fix.
- `T:` if timer/DME/GPS not set before FAF, MAP identification can fail under workload.
***
#### Timing

- Timing required if MAP based on time or as backup when published.
- `F:` time(min)=distance/GS×60.
- `T:` use ground speed, not IAS. Wind change on final can make timing inaccurate; use primary MAP if available.
***
#### Circling

- Check circling minima/category, prohibited sectors, day/night restrictions, runway lighting, terrain/obstacles, weather/wind.
- If visual reference lost: initiate circling missed; generally turn toward landing runway then intercept published missed unless procedure/SOP says otherwise.
- `T:` circling area depends category/speed. Faster than category = higher category.
***
#### Straight-in vs circling

- Straight-in minima require alignment/descent/visual environment adequate for landing on that runway.
- If runway not suitable/visual manoeuvre required, use circling minima unless procedure provides straight-in authorized minima.
- `T:` “approach to runway” does not guarantee straight-in landing is sensible.
***
#### Lighting / runway / visual aids

- Check ALS, runway lights, TDZ/centreline lights, PAPI/VASI, RIL, approach lighting penalties, runway length/LDA, slope, displaced threshold.
- `T:` lighting inoperative can increase minima or make procedure/runway unsuitable. NOTAM can change this.
***
#### Runway / landing distance

- Use LDA/declared distances, slope, surface condition/RSC, wind, temperature, aircraft landing performance.
- `T:` approach legal does not mean landing distance acceptable.
***
#### GNSS / RNAV plate traps

- Verify database current, correct airport/runway/procedure/transition, approach mode armed/active, RAIM/WAAS, CDI sensitivity, OBS/SUSP.
- Do not use expired database for IFR approach unless explicitly permitted/verified by approved procedure and data.
- `T:` `Direct-To FAF` can destroy sequencing; missed approach may not auto-sequence until SUSP cancelled correctly.
***
#### ILS / LOC traps

- Identify LOC frequency, set front course, intercept from below glidepath, verify GS alive/captured, monitor raw data.
- LOC-only approach uses LOC minima and MDA, not ILS DA.
- `T:` false glideslope if intercept from above; back-course/reverse sensing depends equipment and procedure.
***
#### VOR / NDB / DME traps

- VOR radials are FROM; NDB bearing is TO; DME is slant range.
- DME arc: lead radial/turn anticipation; station passage/DME switch can confuse.
- `T:` unserviceable navaid or no identification = no approach using that navaid.
***
#### Approach briefing compact script

- `P:` “This is [procedure/runway] at [airport], plate current. Nav [source/freq/course], minima [line/category/DA-MDA/vis], altimeter/RASS [source/correction], FAF [fix/alt], MAP [fix/time/DME], missed [climb/turn/fix/hold], runway [LDA/lights], threats [wx/terrain/wind/icing/NOTAM].”
- `M:` `PROC-NAV-MIN-RASS-FAF-MAP-MISSED-RWY-THREATS`.
***
#### Before FAF / final gate

- `P:` altimeter set/cross-check → nav source active → course set → approach armed/active → missed loaded/briefed → landing checklist → speed/config plan → timer if needed → minimums bugged.
- `T:` if not stable/briefed/configured, request vectors/hold or go missed.
***
#### INRAT plate question method

- `1` identify procedure/minima line; `2` check category; `3` read notes/RASS/cold; `4` check altimeter source; `5` apply lighting/runway/NOTAM; `6` compare weather/RVR; `7` determine legal/safe action.
- `T:` exam distractors often ignore a note or use wrong category/minima line.
***
#### Real-flight plate method

- `1` current plate/NOTAM; `2` legal/equipped; `3` fuel/alternate; `4` terrain/icing/TS/wind; `5` setup/brief; `6` monitor stable approach; `7` miss early if doubt.
- `T:` legal minimums are not personal minimums. Low-vis approaches invite confirmation bias.
***
#### Pebble

- scan `TITLE-NAV-PLAN-PROFILE-MIN-MISSED-NOTES-RWY` | current CAP/NOTAM wins | category first | note block can kill approach | DA/MDA require visual refs | RASS add to altitudes / may force circling | cold temp protects obstacle clearance | brief missed before FAF | MAP timing uses GS | LPV≠ILS | LOC line≠ILS line | wrong CDI source kills | circling lost visual→missed | legal approach≠landing distance OK.

***
#### Sources & review status

See the [separate review record](../CONTENT_REVIEW.md#historical-source-review-notes) for source editions, check dates and earlier validation notes.
