# Takeoff, climb, cruise, glide & landing performance / Performances : décollage, montée, croisière, plané, atterrissage
<!-- concept: agk-perfcalc | level: IR -->

[Index](README.md) · concept `agk-perfcalc` · unit IDs are stable: never rename one.

***
#### Climb / descent gradient
<!-- id: agk-climb-descent-gradient | from: 06 | also: ifr-dep, study-formulas | level: IR -->

- `F:` `ft/NM = ROC(fpm) × 60 / GS`.
- `F:` `ROC/ROD(fpm)=GS × gradient(ft/NM)/60`.
- `M:` `200 ft/NM ≈ 3.3%`.
- `M:` at `90 kt`, `300 ft/NM` needs `450 fpm`; at `120 kt`, needs `600 fpm`.
- `T:` gradient uses groundspeed. Tailwind increases GS and required fpm.
***
#### Percent gradient
<!-- id: agk-percent-gradient | from: 06 | also: ifr-dep, study-formulas | level: IR -->

- `F:` `% gradient = ft/NM / 60.76`.
- `F:` `ft/NM ≈ % × 60.76`.
- `M:` `3° glidepath ≈ 318 ft/NM ≈ 5.2%`.
- `M:` `3.3% ≈ 200 ft/NM`.
- `T:` degrees and percent are not the same.
***
#### Descent planning
<!-- id: agk-descent-planning | from: 06 | also: ifr-app-fly, study-formulas | level: PPL CPL IR -->

- `F 3°:` `ROD ≈ GS × 5`.
- `F 3°:` descent distance NM ≈ `altitude to lose / 300`.
- `F:` time to descend = distance/GS×60.
- `M:` `90 kt` on 3° ⇒ `450 fpm`; `100 kt` ⇒ `500 fpm`; `120 kt` ⇒ `600 fpm`.
- `T:` add level-offs, stepdowns, tailwind, config, ATC restrictions.
***
#### Glide
<!-- id: agk-glide | from: 06 | also: study-formulas | level: PPL CPL IR -->

- `F:` glide distance `NM = height AGL(ft) × glide ratio / 6076`.
- Example: `9:1` glide ratio ⇒ `1000 ft AGL ≈ 1.48 NM` still-air.
- `F:` time aloft ≈ height to lose / descent rate.
- `M C150M:` POH Fig. 3-1 shows approx `6000 ft AGL → 10 NM`; therefore `1000 ft ≈ 1.67 NM` at `60 KIAS`, flaps UP, prop windmilling, zero wind. `[C150M POH 1977 Fig. 3-1]`
- `T:` use height above terrain, not altitude ASL. Wind, configuration, propeller, speed and aircraft condition change actual range.
***
#### Runway / landing energy
<!-- id: agk-runway-landing-energy | from: 06 | also: study-formulas | level: PPL CPL IR -->

- `F:` kinetic energy ∝ `V²`.
- `F:` speed increase energy factor = `(actual/target)²`.
- `M:` `+10% speed` ⇒ `+21% energy`; `+20% speed` ⇒ `+44% energy`.
- `T:` fast final burns runway and brakes. Tailwind hurts more than it feels.
***
