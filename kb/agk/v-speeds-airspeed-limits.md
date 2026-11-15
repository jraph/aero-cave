# V-speeds & airspeed limits / Vitesses caractéristiques et limites
<!-- concept: agk-vspeeds | level: CPL IR ME -->

[Index](README.md) · concept `agk-vspeeds` · unit IDs are stable: never rename one.

***
#### VREF / landing reference speed
<!-- id: agk-vref-landing-reference-speed | from: 06 | also: agk-perfcalc | kind: formula | level: CPL IR ME -->

- `Definition:` `VREF` is the landing reference speed. Use the POH/AFM value for the specified landing configuration; certification bases differ. In landing-distance certification it is maintained to the `50 ft` screen height.
- `F fallback:` when `VREF` is not specified, use `VREF = 1.3 × VSO`. Example: `VSO 50 KIAS → VREF 65 KIAS`.
- `F weight:` for the same configuration and speed basis, `VREF₂ ≈ VREF₁ × √(W₂/W₁)`. Use POH/AFM landing-weight data when published.
- `Approach category:` use published `VREF`, or `1.3 VSO` if none is specified, at **maximum certificated landing weight**. Do not lower the category because today’s landing weight is lower. `[TC AIM 2026-1 RAC 9.21]`
- `T:` a wind/gust additive changes the operational approach target (`VAPP`), not the underlying `VREF`. Aircraft procedures and limitations govern.
***
#### Landing gear speeds — VLO / VLE
<!-- id: agk-landing-gear-speeds-vlo-vle | level: PPL CPL ME -->

- `VLO` = maximum speed for **operating** the landing gear (extending or retracting). Some aircraft publish two: `VLO` extend and `VLO` retract.
- `VLE` = maximum speed with the gear **extended** and locked.
- `T:` `VLO ≤ VLE` usually: gear doors/mechanism in transit are the weak point. Values come from the AFM/POH limitations section.
- `?:` general knowledge; no TC text found for these definitions.

- Sources: AFM/POH limitations section.
***
#### Pebble
<!-- id: agk-v-speeds-airspeed-limits-pebble | level: CPL IR ME -->

- VREF `POH/AFM value; fallback 1.3 × VSO | weight: VREF₂ ≈ VREF₁ × √(W₂/W₁) | approach category at maximum certificated landing weight | gust additive changes VAPP, not VREF`
- GEAR SPEEDS `VLO operating (extend/retract, may differ) | VLE extended | VLO usually ≤ VLE | AFM/POH limitations`
***
