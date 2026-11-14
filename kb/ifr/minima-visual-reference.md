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

- `T:` advisory visibility helps probability/ban logic; DA/MDA controls vertical descent.
***
#### Landing minima / visual reference
<!-- id: ifr-landing-minima-visual-reference | from: 09 -->

- Do not continue below DH/DA or descend below MDA unless required visual reference established and maintained for safe landing.
- Visual refs include runway/markings/threshold/TDZ/approach lights/VGSI/RIL/threshold-end lights/edge/centreline/TDZL.
- Published landing visibilities are advisory only subject to approach ban; use to judge success probability.
- `!:` missed after MAP: obstacle clearance not assured.
***
#### Landing minima / visual reference · INRAT
<!-- id: ifr-landing-minima-visual-reference-inrat | from: 10 -->

- Do not continue below DA/DH or descend below MDA unless required visual reference is established and maintained for safe landing.
- Required visual refs include runway/markings/threshold/TDZ/approach lights/VGSI/RIL/threshold-end lights/edge/centreline/TDZL.
- `T:` seeing “some lights” may not be enough if it doesn’t allow position/rate assessment for safe landing.
***
#### RVR / approach ban
<!-- id: ifr-rvr-approach-ban | from: 09 -->

- RVR = automated runway visual range for landing/takeoff direction. Use current approach-ban rules; category/operator-specific.
- `T:` advisory vis not same as approach-ban controlling visibility. CAP/CAR/operator ops spec wins.
***
#### Approach ban / RVR — general aviation
<!-- id: ifr-approach-ban-rvr-general-aviation | from: 10 -->

- GA NPA/APV/CAT I/II: governed by RVR values when runway served by RVR.
- General non-Part VII aeroplane rule: if both measured, below minimum when `RVR A <1200` **or** `RVR B <600`; if only one is measured, below minimum when it is `<1200`. `[CAR 602.129]`
- Exceptions include: below-min RVR received after FAF; training missed approach; RVR varying below/above; RVR below min but ground vis ≥`1/4 SM`; CAT III as applicable.
- `T:` if RVR unavailable/not reported, GA approach-ban criterion may not exist; still need DA/MDA visual reference to land.
- `T:` commercial approach-ban rules are stricter/different; don’t mix GA and 703/704/705 tables.
***
