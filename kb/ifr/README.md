# IFR & INRAT — concept files / IFR et INRAT — fiches par concept

One file per ontology concept (`explorer/ontology.json`), same format as [`kb/met/`](../met/README.md): each `####` section is a unit with a permanent ID; `also:` lists its other concepts.

| Concept file | Concept | Units |
|---|---|---|
| [Alternate minima / Minimums de dégagement](alternate-minima.md) | `ifr-alt` | 4 |
| [Approach types, briefing & flying the approach / Types d’approche, exposé et exécution](approaches.md) | `ifr-app-fly` | 6 |
| [CAP plate reading / Lecture des cartes CAP](cap-plates-publications.md) | `ifr-plates` | 5 |
| [Departure: takeoff minima, SID / ODP & climb gradient / Départ : minimums de décollage, SID / ODP et pente de montée](departure.md) | `ifr-dep` | 4 |
| [IFR emergencies & instrument failures / Urgences IFR et pannes d’instruments](emergencies-instrument-failures.md) | `ifr-emerg` | 3 |
| [Enroute: clearances, altitudes & reports / En route : autorisations, altitudes et comptes rendus](enroute.md) | `ifr-enr` | 5 |
| [Holding / Attente](holding.md) | `ifr-hold` | 3 |
| [IFR weather / Météo IFR](ifr-weather.md) | `ifr-wx` | 3 |
| [Lost communications / NORDO / Panne de communications / NORDO](lost-comms.md) | `emg-comms` | 3 |
| [Minima, visual reference, RVR & approach ban / Minimums, références visuelles, RVR et interdiction d’approche](minima-visual-reference.md) | `ifr-minima` | 5 |
| [Missed approach & circling / Approche interrompue et approche indirecte](missed-approach-circling.md) | `ifr-missed` | 3 |
| [Radio navigation (VOR / ADF / DME / ILS) / Radionavigation (VOR / ADF / DME / ILS)](navaid-checks.md) | `nav-radio` | 3 |
| [IFR planning, fuel & alternates / Planification IFR, carburant et dégagement](planning-fuel.md) | `ifr-plan` | 4 |
| [RASS / remote altimeter setting / RASS / calage altimétrique éloigné](rass.md) | `ifr-rass` | 2 |
| [IFR — exam method & traps / IFR — méthode d’examen et pièges](recall.md) | `ifr` | 5 |
| [IFR rules, privileges & recency / Règles, privilèges et récence IFR](rules-privileges.md) | `ifr` | 6 |

Flown procedures and QRCs stay in numbered cards: [11 · CAP plate reading](../../cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md), [12 · IFR procedures](../../cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md).

## Provenance / Provenance

Units moved on 14 November 2026 from cards 09 (IFR knowledge) and 10 (INRAT knowledge) with their text unchanged (`from:` on each unit); both cards were then deleted. Units identical in both cards are kept once. Thirteen near-duplicate pairs were then merged into single units (`from: 09, 10`), keeping every distinct fact and qualifier; each concept file ends with a `#### Pebble` recapping only that file. Cycle-dated lines are review-dated (14 Nov 2026). Nothing was re-validated against CARs, AIM or CAP. The original card headers still apply:

- Card 09 (`from: 09`):
  - `SEPTEMBER CPAER REVIEW: retained reference, not freshly revalidated` | use exact aircraft/current operational sources
  - `R` rule | `P` proc | `T` trap | `M` memory | `!` safety | Canada IFR study; current CAP/NOTAM/POH/SOP win
  - `RELEASE:` `OPS/EXAM-REF PROVISIONAL` | `CANONICAL SOURCE:` `ifr_knowledge_core_av_cave_v0_2.md` | `NOT FLIGHT AUTHORITY`
- Card 10 (`from: 10`):
  - `SEPTEMBER CPAER REVIEW: retained reference, not freshly revalidated` | use exact aircraft/current operational sources
  - `R` rule | `F` formula | `P` procedure | `T` trap | `M` memory | `!` safety | `?` verify | Canada INRAT exam prep
  - `RELEASE:` `EXAM/CYCLE-REF PROVISIONAL` | `CANONICAL SOURCE:` `inrat_knowledge_core_av_cave_v0_3.md` | `NOT FLIGHT AUTHORITY`

Units tagged `from: 01 / 03 / 04 / 06 / 13` were added on 14 November 2026 when the remaining knowledge cards were retired; they are unmerged and the file's Pebble does not yet recap them.
