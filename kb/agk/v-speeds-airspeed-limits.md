# V-speeds & airspeed limits / Vitesses caractéristiques et limites
<!-- concept: agk-vspeeds | level: CPL IR ME -->

[Index](README.md) · concept `agk-vspeeds` · unit IDs are stable: never rename one.

***
#### VREF / landing reference speed
<!-- id: agk-vref-landing-reference-speed | from: 06 | also: agk-perfcalc, study-formulas | level: CPL IR ME -->

- `Definition:` `VREF` is the landing reference speed. Use the POH/AFM value for the specified landing configuration; certification bases differ. In landing-distance certification it is maintained to the `50 ft` screen height.
- `F fallback:` when `VREF` is not specified, use `VREF = 1.3 × VSO`. Example: `VSO 50 KIAS → VREF 65 KIAS`.
- `F weight:` for the same configuration and speed basis, `VREF₂ ≈ VREF₁ × √(W₂/W₁)`. Use POH/AFM landing-weight data when published.
- `Approach category:` use published `VREF`, or `1.3 VSO` if none is specified, at **maximum certificated landing weight**. Do not lower the category because today’s landing weight is lower. `[TC AIM 2026-1 RAC 9.21]`
- `T:` a wind/gust additive changes the operational approach target (`VAPP`), not the underlying `VREF`. Aircraft procedures and limitations govern.
***
