# Takeoff, climb, cruise, glide & landing performance / Performances : décollage, montée, croisière, plané, atterrissage
<!-- concept: agk-perfcalc | level: IR -->

[Index](README.md) · concept `agk-perfcalc` · unit IDs are stable: never rename one.

***
#### Performance factors
<!-- id: agk-performance-factors | from: 01, 03 | also: agk-perf, agk-vspeeds | level: PPL CPL -->

- Vx=altitude/distance. Vy=altitude/time. Best glide=max distance no power. Min sink=max time.
- Calculate, don’t guess. TO/LDG: weight/temp/pressure/elev/wind/slope/surface/config/technique.
- `M:` hot-high-heavy-humid-tailwind-soft-uphill TO = bad stack.
- Headwind helps; tailwind hurts big: small value, large distance penalty. grass/soft/wet/snow roll↑ braking↓.
***
#### Climb / descent gradient
<!-- id: agk-climb-descent-gradient | from: 06 | also: ifr-dep | kind: formula | level: IR -->

- `F:` `ft/NM = ROC(fpm) × 60 / GS`.
- `F:` `ROC/ROD(fpm)=GS × gradient(ft/NM)/60`.
- `M:` % conversions (`200 ft/NM ≈ 3.3%`): `see agk-percent-gradient`.
- `M:` at `90 kt`, `300 ft/NM` needs `450 fpm`; at `120 kt`, needs `600 fpm`.
- `T:` gradient uses groundspeed. Tailwind increases GS and required fpm.
***
#### Percent gradient
<!-- id: agk-percent-gradient | from: 06 | also: ifr-dep | kind: formula | level: IR -->

- `F:` `% gradient = ft/NM / 60.76`.
- `F:` `ft/NM ≈ % × 60.76`.
- `M:` `3° glidepath ≈ 318 ft/NM ≈ 5.2%`.
- `M:` `3.3% ≈ 200 ft/NM`.
- `T:` degrees and percent are not the same.
***
#### Descent planning
<!-- id: agk-descent-planning | from: 06 | also: ifr-app-fly | kind: formula | level: PPL CPL IR -->

- `F 3°:` `ROD ≈ GS × 5`.
- `F 3°:` descent distance NM ≈ `altitude to lose / 300`.
- `F:` time to descend = distance/GS×60.
- `M:` `90 kt` on 3° ⇒ `450 fpm`; `100 kt` ⇒ `500 fpm`; `120 kt` ⇒ `600 fpm`.
- `T:` add level-offs, stepdowns, tailwind, config, ATC restrictions.
***
#### Glide
<!-- id: agk-glide | from: 06 | kind: formula | level: PPL CPL IR -->

- `F:` glide distance `NM = height AGL(ft) × glide ratio / 6076`.
- Example: `9:1` glide ratio ⇒ `1000 ft AGL ≈ 1.48 NM` still-air.
- `F:` time aloft ≈ height to lose / descent rate.
- C150M POH glide data: `see c150-maximum-glide`.
- `T:` use height above terrain, not altitude ASL. Wind, configuration, propeller, speed and aircraft condition change actual range.
***
#### Runway / landing energy
<!-- id: agk-runway-landing-energy | from: 06 | kind: formula | level: PPL CPL IR -->

- `F:` kinetic energy ∝ `V²`.
- `F:` speed increase energy factor = `(actual/target)²`.
- `M:` `+10% speed` ⇒ `+21% energy`; `+20% speed` ⇒ `+44% energy`.
- `T:` fast final burns runway and brakes. Tailwind hurts more than it feels.
***
#### Runway / landing distance
<!-- id: plate-runway-landing-distance | from: 11 | also: ifr-plates | level: IR -->

- Use LDA/declared distances, slope, surface condition/RSC, wind, temperature, aircraft landing performance.
- `T:` approach legal does not mean landing distance acceptable.
***
#### Pebble
<!-- id: agk-takeoff-climb-cruise-glide-landing-performance-pebble | level: PPL CPL IR -->

- FACTORS `Vx = altitude/distance; Vy = altitude/time; best glide = max distance; min sink = max time | hot-high-heavy-humid-tailwind-soft-uphill = bad stack | calculate, don’t guess`
- GRADIENT `ft/NM = ROC × 60 / GS | fpm = GS × ft/NM / 60 | % = ft/NM / 60.76 | 200 ft/NM ≈ 3.3% | 3° ≈ 318 ft/NM ≈ 5.2% | uses groundspeed`
- DESCENT `3°: ROD ≈ GS × 5; distance NM ≈ altitude to lose / 300 | add level-offs, stepdowns, tailwind`
- GLIDE `NM = height AGL × glide ratio / 6076 | height above terrain, not ASL`
- ENERGY `KE ∝ V² | +10% speed = +21% energy; +20% = +44% | fast final burns runway`
***
