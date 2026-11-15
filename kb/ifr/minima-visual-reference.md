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
- Categories by approach speed: **A** ≤90 kt · **B** 91–120 · **C** 121–140 · **D** 141–165 · **E** >165. Faster than your category → use the higher one; never a lower category. [CAP GEN Minima]
***
#### Landing minima / visual reference
<!-- id: ifr-landing-minima-visual-reference | from: 09, 10 -->

- Do not continue below DH/DA or descend below MDA unless required visual reference established and maintained for safe landing.
- Visual refs include runway/markings/threshold/TDZ/approach lights/VGSI/RIL/threshold-end lights/edge/centreline/TDZL.
- Published landing visibilities are advisory only subject to approach ban; use to judge success probability.
- `!:` missed after MAP: obstacle clearance not assured (see `ifr-missed-approach`).
- `T:` seeing “some lights” may not be enough if it doesn’t allow position/rate assessment for safe landing.
***
#### Approach ban / RVR
<!-- id: ifr-approach-ban-rvr-general-aviation | from: 09, 10 -->

- RVR = automated runway visual range for landing/takeoff direction. Use current approach-ban rules; category/operator-specific.
- GA NPA/APV/CAT I/II: governed by RVR values when runway served by RVR.
- General non-Part VII aeroplane rule: if both measured, below minimum when `RVR A <1200` **or** `RVR B <600`; if only one is measured, below minimum when it is `<1200`. `[CAR 602.129]`
- Below-minimum RVR bars continuation beyond the FAF (or, with no FAF, the point where the final approach course is intercepted), subject to exceptions: below-min RVR received after that point; training missed approach (no landing); RVR varying below/above; RVR below min but ground vis ≥`1/4 SM`; CAT III as applicable.
- `T:` if RVR unavailable/not reported, GA approach-ban criterion may not exist; still need DA/MDA visual reference to land.
- `T:` commercial approach-ban rules are stricter/different; don’t mix GA and 703/704/705 tables.
- `T:` advisory vis not same as approach-ban controlling visibility; ground visibility, runway visibility, RVR, advisory visibility and flight visibility are different. CAP/CAR/operator ops spec wins.
***
#### Minima box scan
<!-- id: plate-minima-box-scan | from: 11 | also: ifr-plates | level: IR -->

- Read aircraft category first: `A/B/C/D/E` by final approach speed category.
- Identify line: `ILS/LOC/LNAV/LNAV-VNAV/LPV/VOR/NDB/circling`.
- Extract: `DA/DH` or `MDA`; `HAT/HATh/HAA`; advisory visibility; notes/lighting penalties; RASS/cold-temp impacts.
- `T:` wrong category = wrong protected area/minima; speed vs category rule: see `ifr-cap-definitions-minima`.
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
#### Reduced and low visibility operations
<!-- id: ifr-reduced-low-visibility-operations | also: law-atc | level: IR -->

- **RVO** = below RVR 2600 down to RVR 1200; **LVO** = below RVR 1200 down to RVR 600. Arrivals/departures below RVR 600 not authorized. [CAP GEN Operating minima]
- RVR 2600 imminent → procedures restrict movement area; ATIS: "LOW / REDUCED VISIBILITY PROCEDURES IN EFFECT". [CAP GEN]
- LVP in effect → no NPA, APV, CAT I or CAT II approach may be commenced (CAT III ops only). [CAP GEN; CAR 602.129]
- CAP aerodrome chart shows each runway's level of service (`RVR 1200`, `¼ SM`, `RVR 600`). Below CFS level of service = taxi/landing "below published aerodrome operating visibility" (exceptions: already past FAF, started taxi, ATC-authorized per procedures). [CAP GEN]
- Start/push: wait for RVR ≥1000 for 1200 take-off minima; ≥600 for 600 minima. "Follow me" on request below RVR 2600. [CAP GEN]
- `M:` `2600 RVO · 1200 LVO · 600 floor`.
***
#### Pebble
<!-- id: ifr-minima-visual-reference-pebble -->

- DEFINITIONS `DA = missed initiated if no visual ref | DH = DA above TDZE/threshold | MDA = no descent below without visual ref | HAA = MDA above aerodrome elevation, circling | HAT/HATh = above TDZE/threshold, straight-in`
- VISUAL REF `no descent below DA/DH/MDA unless required visual reference established AND maintained for safe landing | “some lights” may not be enough | published landing visibilities advisory, subject to approach ban | missed after MAP: obstacle clearance not assured`
- APPROACH BAN (GA, non-Part VII) CAR 602.129 `both measured: below minimum when RVR A <1200 OR RVR B <600 | one measured: <1200 | exceptions: after FAF, training missed approach, RVR varying, ground vis ≥¼ SM, CAT III as applicable | no RVR reported → criterion may not exist`
- T `commercial 703/704/705 rules differ: do not mix tables | advisory vis ≠ approach-ban controlling visibility`
- RVO/LVO `RVO <2600–1200 · LVO <1200–600 · <600 not authorized | LVP in effect → no NPA/APV/CAT I/II start | categories A≤90 B≤120 C≤140 D≤165`
***
