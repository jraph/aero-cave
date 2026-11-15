# Minima, visual reference, RVR & approach ban / Minimums, références visuelles, RVR et interdiction d’approche
<!-- concept: ifr-minima | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-minima` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### CAP definitions / minima
<!-- id: ifr-cap-definitions-minima | from: 10 | also: ifr-plates -->

| Item | Memory |
|---|---|
| `DA` | altitude where missed shall be initiated if visual ref not established |
| `DH` | height of DA above TDZE/threshold |
| `MDA` | no descent below until required visual ref |
| `HAA` | MDA above aerodrome elevation, circling |
| `HAT/HATh` | DA/MDA above TDZE/threshold, straight-in |
| `MSA` | min 1000 ft clearance in sector, standard temp/pressure |
| `RVR` | runway centreline visual range of markings/lights |
| `Vis` | advisory / approach-ban planning value, not DA/MDA itself |

- `T:` advisory visibility helps probability/ban logic; DA/MDA controls vertical descent.
***
#### Landing minima / visual reference
<!-- id: ifr-landing-minima-visual-reference | from: 09, 10 -->

- Do not continue below DH/DA or descend below MDA unless required visual reference established and maintained for safe landing.
- Visual refs include runway/markings/threshold/TDZ/approach lights/VGSI/RIL/threshold-end lights/edge/centreline/TDZL.
- Published landing visibilities are advisory only subject to approach ban; use to judge success probability.
- `!:` missed after MAP: obstacle clearance not assured.
- `T:` seeing “some lights” may not be enough if it doesn’t allow position/rate assessment for safe landing.
***
#### Approach ban / RVR
<!-- id: ifr-approach-ban-rvr-general-aviation | from: 09, 10 -->

- RVR = automated runway visual range for landing/takeoff direction. Use current approach-ban rules; category/operator-specific.
- GA NPA/APV/CAT I/II: governed by RVR values when runway served by RVR.
- General non-Part VII aeroplane rule: if both measured, below minimum when `RVR A <1200` **or** `RVR B <600`; if only one is measured, below minimum when it is `<1200`. `[CAR 602.129]`
- Exceptions include: below-min RVR received after FAF; training missed approach; RVR varying below/above; RVR below min but ground vis ≥`1/4 SM`; CAT III as applicable.
- `T:` if RVR unavailable/not reported, GA approach-ban criterion may not exist; still need DA/MDA visual reference to land.
- `T:` commercial approach-ban rules are stricter/different; don’t mix GA and 703/704/705 tables.
- `T:` advisory vis not same as approach-ban controlling visibility. CAP/CAR/operator ops spec wins.
***
#### RVR / visibility quick memory
<!-- id: ifr-rvr-visibility-quick-memory | from: 06 | kind: formula | level: IR -->

- `R non-Part VII aeroplane:` if both measured, below minimum when `RVR A <1200` **or** `RVR B <600`; if only A or B measured, below minimum when that RVR `<1200`. `[CAR 602.129]`
- Below-minimum RVR normally bars continuation beyond the applicable point, subject to listed exceptions: report received after FAF/final-course intercept, training no-landing, varying RVR, ground visibility ≥`1/4 SM`, or CAT III.
- Advisory visibility helps planning; DA/MDA visual reference controls descent/landing.
- `T:` this general rule excludes Part VII operations; ground visibility, runway visibility, RVR, advisory visibility and flight visibility are different.
***
#### Minima box scan
<!-- id: plate-minima-box-scan | from: 11 | also: ifr-plates | level: IR -->

- Read aircraft category first: `A/B/C/D/E` by final approach speed category.
- Identify line: `ILS/LOC/LNAV/LNAV-VNAV/LPV/VOR/NDB/circling`.
- Extract: `DA/DH` or `MDA`; `HAT/HATh/HAA`; advisory visibility; notes/lighting penalties; RASS/cold-temp impacts.
- `T:` wrong category = wrong protected area/minima. Faster circling speed can force higher category.
***
#### Straight-in vs circling
<!-- id: plate-straight-in-vs-circling | from: 11 | also: ifr-missed, ifr-plates | level: IR -->

- Straight-in minima require alignment/descent/visual environment adequate for landing on that runway.
- If runway not suitable/visual manoeuvre required, use circling minima unless procedure provides straight-in authorized minima.
- `T:` “approach to runway” does not guarantee straight-in landing is sensible.
***
#### Lighting / runway / visual aids
<!-- id: plate-lighting-runway-visual-aids | from: 11 | also: ifr-plates | level: IR -->

- Check ALS, runway lights, TDZ/centreline lights, PAPI/VASI, RIL, approach lighting penalties, runway length/LDA, slope, displaced threshold.
- `T:` lighting inoperative can increase minima or make procedure/runway unsuitable. NOTAM can change this.
***
#### Pebble
<!-- id: ifr-minima-visual-reference-pebble -->

- DEFINITIONS `DA = missed initiated if no visual ref | DH = DA above TDZE/threshold | MDA = no descent below without visual ref | HAA = MDA above aerodrome elevation, circling | HAT/HATh = above TDZE/threshold, straight-in`
- VISUAL REF `no descent below DA/DH/MDA unless required visual reference established AND maintained for safe landing | “some lights” may not be enough | published landing visibilities advisory, subject to approach ban | missed after MAP: obstacle clearance not assured`
- APPROACH BAN (GA, non-Part VII) CAR 602.129 `both measured: below minimum when RVR A <1200 OR RVR B <600 | one measured: <1200 | exceptions: after FAF, training missed approach, RVR varying, ground vis ≥¼ SM, CAT III as applicable | no RVR reported → criterion may not exist`
- T `commercial 703/704/705 rules differ: do not mix tables | advisory vis ≠ approach-ban controlling visibility`
***
