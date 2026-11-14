# Meteorology — concept files / Météorologie — fiches par concept

One file per ontology concept (`explorer/ontology.json`). Each `####` section is a **unit** with a stable ID on the line under its heading. A unit lives in one file (its primary concept) and may list other concepts in `also:`; the [explorer](https://jraph.github.io/aero-cave/explorer.html) shows it under all of them, and under the TC guide items mapped in `explorer/syllabus.json`.

| Concept file | Concept | Units |
|---|---|---|
| [Atmosphere, altimetry & density altitude / Atmosphère, altimétrie et altitude-densité](atmosphere-altimetry.md) | `met-atmos` | 4 |
| [Temperature, moisture, stability & cloud / Température, humidité, stabilité et nuages](stability-clouds.md) | `met-stab` | 5 |
| [Fog & visibility / Brouillard et visibilité](fog-visibility.md) | `met-fog` | 2 |
| [Air masses, fronts, pressure systems & wind / Masses d’air, fronts, systèmes de pression et vent](air-masses-fronts-wind.md) | `met-systems` | 9 |
| [Icing / Givrage](icing.md) | `met-icing` | 4 |
| [Carburettor icing & induction / Givrage du carburateur et admission](carburettor-icing.md) | `carb-ice` | 2 |
| [Ground de-/anti-icing & clean aircraft / Dégivrage / antigivrage au sol et aéronef propre](ground-deicing.md) | `deice` | 1 |
| [Thunderstorms & convection / Orages et convection](thunderstorms.md) | `met-ts` | 2 |
| [Turbulence, wind shear & mountain wave / Turbulence, cisaillement et ondes orographiques](turbulence-wind-shear.md) | `met-turb` | 8 |
| [Weather products & decoding / Produits météo et décodage](weather-products.md) | `met-products` | 3 |
| [METAR / SPECI](metar.md) | `met-metar` | 7 |
| [TAF](taf.md) | `met-taf` | 2 |
| [GFA, SIGMET / AIRMET, PIREP & upper winds / GFA, SIGMET / AIRMET, PIREP et vents en altitude](gfa-sigmet-pirep-winds.md) | `met-gfa` | 3 |
| [Meteorology — exam traps & recall / Météorologie — pièges et rappel](recall.md) | `met` | 2 |

Go/no-go flows, gates and the personal weather matrix are procedures and stay in [card 05](../../cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md).

## Provenance / Provenance

Units were moved on 14 November 2026 from cards 16 and 05 with their text unchanged (`from:` on each unit). Overlapping units from the two cards now sit side by side and have **not** been merged. The original card headers still apply to their units:

- Card 16 (`from: 16`):
  - `K` knowledge | `M` memory | `T` trap | `!` hazard | `F` formula | Canada PPL/CPL/INRAT
  - `RELEASE:` `STUDY-REF PROVISIONAL` | `SRC:` TC AIM 2026-1 + standard aviation meteorology | use current MET products for flight
- Card 05 (`from: 05`):
  - `TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
  - `P` procedure | `R` rule | `F` formula | `T` trap | `M` memory | `!` safety | `?` verify | Canada PPL/CPL/INRAT/IR
  - `RELEASE:` `STUDY/OPS-REF PROVISIONAL` | `NOT FLIGHT AUTHORITY`

## Editing rules / Règles d’édition

- Unit comment: `<!-- id: wx-fog | from: 16 | also: met-decide | level: IR -->`. `id` is required; `also` and `level` are optional (`level` defaults to the file header).
- File header: `<!-- concept: met-fog | level: PPL CPL IR -->` directly under the title.
- Never rename or reuse an ID. To retire a unit, delete it and fix `explorer/syllabus.json`.
- After any edit run `python3 explorer/build_explorer.py` and bump the service-worker VERSION.
