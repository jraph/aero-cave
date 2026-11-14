# Departure: takeoff minima, SID / ODP & climb gradient / Départ : minimums de décollage, SID / ODP et pente de montée
<!-- concept: ifr-dep | level: IR -->

[IFR index / Index IFR](README.md) · concept `ifr-dep` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Departure / takeoff minima
<!-- id: ifr-departure-takeoff-minima | from: 10 -->

- Check CAP aerodrome chart/SID/ODP/diverse departure, climb gradient, obstacle notes, RVR/visibility, lighting, engine-out capability if applicable.
- `R:` takeoff visibility precedence: use runway `RVR` when reported at/above the applicable minimum; use aerodrome `ground visibility` when RVR is below minimum, varies below/above minimum, or is not reported; use PIC-observed `runway visibility` only when neither RVR nor ground visibility is reported. `[CAR 602.126]`
- Applicable minimum comes from the AOC/special authorization, or the current CAP for other operations.
- `T:` takeoff visibility ≠ landing/approach visibility. Departure obstacle climb gradient may be more restrictive than weather.
- `T:` “standard takeoff minima” is not “safe to climb over obstacles”; compare required climb gradient vs aircraft performance.
***
#### SID / ODP / climb gradient
<!-- id: ifr-sid-odp-climb-gradient | from: 10 -->

- SID = published ATC/obstacle/departure routing; may include altitude/speed/climb gradient.
- Diverse departure assumes obstacle environment supports generic departure; if obstacle DP exists, use it unless ATC assigns otherwise.
- Climb gradient: `ft/NM`; required ROC ≈ `GS × ft/NM / 60`.
- Common 3.3% ≈ `200 ft/NM`. `F:` `ROC fpm = GS kt × gradient(ft/NM)/60`.
- `T:` climb gradient is ground-speed based; tailwind/high GS raises required fpm.
***
#### Takeoff visibility / RVR trap
<!-- id: ifr-takeoff-visibility-rvr-trap | from: 10 | also: ifr-minima -->

- RVR report can be below takeoff minimum but ground visibility at/above minimum may govern; inverse also possible.
- If both lowest RVR and ground visibility are below required minimum, takeoff not authorized.
- If only RVR below minimum and no governing ground visibility at/above minimum, takeoff not authorized.
- `T:` “variable RVR” and “observed on-the-hour vs now” wording can flip the answer.
***
