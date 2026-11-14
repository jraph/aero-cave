# Airspace, VFR minima & cruising altitudes / Espace aérien, minimums VFR et altitudes de croisière
<!-- concept: law-airspace | level: PPL CPL -->

[Index](README.md) · concept `law-airspace` · unit IDs are stable: never rename one.

***
#### Airspace
<!-- id: law-airspace | from: 01 | level: PPL CPL -->

| Class | Memory |
|---|---|
| A | IFR only |
| B | clearance + separation |
| C | clearance |
| D | 2-way comm |
| E | IFR controlled / VFR no clearance |
| F | CYR/CYA/CYD special |
| G | uncontrolled |

- `T:` chart/CFS floor/ceiling wins. class rules≠weather minima.
- See the [VFR separation / conflict-resolution matrix](#vfr-separation--conflict-resolution-by-class) for who ATC separates in Classes B–E.
***
#### VFR minima / cruise altitude
<!-- id: law-vfr-minima-cruise-altitude | from: 01 | level: PPL CPL -->

- CTRL: flight vis `≥3 SM`, cloud `1 SM horiz / 500 ft vert`, visual reference to surface. CZ: reported ground vis also `≥3 SM`; stay `≥500 ft` from surface except takeoff/landing.
- UNCTRL ≥`1000 AGL`: day `1 SM`, night `3 SM`, cloud `2000h/500v`.
- UNCTRL <`1000 AGL` aeroplane: day `2 SM`, night `3 SM`, clear of cloud.
- CRZ >`3000 AGL`: SDA=`MTRK`, NDA=`TTRK`; `000–179 odd+500 / 180–359 even+500`. `T:` track≠heading.
***
#### Cruising altitudes
<!-- id: law-cruising-altitudes | from: 04 | level: PPL CPL IR -->

- At more than `3000 ft AGL`, use appropriate cruising altitude/flight level based on track, unless otherwise authorized/required. `[CAR 602.34]`
- VFR: `000–179°` odd thousands +`500`; `180–359°` even thousands +`500`.
- Southern Domestic Airspace uses magnetic track; Northern Domestic Airspace true track.
- `T:` track, not heading.
***
#### Aerodrome / MF operations
<!-- id: law-aerodrome-mf-operations | from: 04 | also: ops-ldg | level: PPL CPL -->

- Ensure suitability/no collision; observe/conform to or avoid circuit; left turns unless CFS/ATC says right; comply CFS/NOTAM; into wind where practicable. Controlled aerodrome: clearance to taxi/TKOF/land. `[CAR 602.96]`
- No flight below `2000 ft over an aerodrome` except listed operations/ATC authorization; separate from circuit and CAR 602.14 minima. `[CAR 602.96(4)]`
- MF procedures/reports: CAR 602.97–602.104 + current CFS frequency/area/hours. `T:` uncontrolled≠unregulated; ATF calls≠MF mandatory reports.
***
#### VFR minima — controlled
<!-- id: law-vfr-minima-controlled | from: 04 | level: PPL CPL -->

- Visual reference to surface.
- Flight visibility `≥3 SM`.
- Cloud distance `≥500 ft vertical + 1 SM horizontal`.
- In control zone: reported ground visibility `≥3 SM`; except takeoff/landing, aircraft `≥500 ft` from surface.
- `[CAR 602.114]`
***
#### VFR minima — uncontrolled aeroplane
<!-- id: law-vfr-minima-uncontrolled-aeroplane | from: 04 | level: PPL CPL -->

| Height | Day | Night | Cloud |
|---|---:|---:|---|
| `≥1000 AGL` | `1 SM` | `3 SM` | `500 ft vert / 2000 ft horiz` |
| `<1000 AGL` | `2 SM` | `3 SM` | clear of cloud |

- Visual reference to surface required. `[CAR 602.115]`
- `T:` these are legal minima, not personal minima.
***
#### Special VFR
<!-- id: law-special-vfr | from: 04 | level: PPL CPL -->

- Only within a control zone; pilot requests and obtains ATC authorization.
- Aeroplane flight visibility `≥1 SM`; helicopter `≥1/2 SM`.
- Remain clear of cloud and in visual reference to surface. Reported ground visibility and radio conditions also apply. Night aeroplane SVFR authorization is to land at destination; do not generalize it to night departures. `[CAR 602.117; AIM RAC 2.7.3]`
- `T:` SVFR is not permission to enter cloud/IMC; ATC traffic capacity and conditions still apply.
***
#### VFR OTT
<!-- id: law-vfr-ott | from: 04 | level: PPL CPL -->

- Day cruise only; vertical cloud separation `≥1000 ft`; between layers at least `5000 ft`; flight visibility `≥5 SM`; destination weather and rating/equipment conditions apply. `[CAR 602.116; 401.44–401.45; 605.15]`
- `T:` PPL alone does not automatically include VFR OTT privilege.
***
#### IFR general
<!-- id: law-ifr-general | from: 04 | also: ifr | level: CPL IR -->

- IFR operation requires IFR flight plan/clearance where applicable, instrument rating/current privileges, appropriate equipment and compliance with IFR minima/procedures. `[CAR 602.121+]`
- Alternate, takeoff, approach, landing and approach-ban rules are separated in CAR 602.122–602.131.
- `T:` advisory visibility, approach-ban threshold and DA/MDA visual-reference rule are three different concepts.
***
#### Airspace entry memory
<!-- id: law-airspace-entry-memory | from: 04 | level: PPL CPL -->

| Class | VFR memory |
|---|---|
| A | IFR only |
| B | ATC clearance + specified equipment/qualification |
| C | ATC clearance before entry |
| D | establish two-way communication before entry |
| E | no VFR clearance generally; IFR controlled |
| F | special-use rules: `CYR/CYA/CYD` |
| G | uncontrolled; CARs still apply |

- Check current chart/CFS for floor, ceiling, transponder and communication requirements.
***
#### VFR separation / conflict resolution by class
<!-- id: law-vfr-separation-conflict-resolution-by-class | from: 04 | also: law-atc | level: PPL CPL -->

| Class | VFR entry | Airborne ATC service |
|---|---|---|
| A | prohibited | IFR only; `SEP ALL` |
| B | clearance; `CVFR` | `SEP ALL`, incl VFR–VFR |
| C | clearance | `SEP` IFR–IFR; `CR` IFR–VFR as needed; `TFC` all; VFR–VFR `CR O/R` after TFC |
| D | 2-way comm | `SEP` IFR–IFR only; `TFC` all; workload/equipment permitting: IFR–VFR `CR`, VFR–VFR `CR O/R` |
| E | none generally; MF/XPDR rules may apply | `SEP` IFR–IFR only; VFR `TFC O/R` workload/equipment permitting; may stop without notice |
| F | obey `CYR/CYA/CYD` | surrounding class unless specified; may be controlled, uncontrolled or both |
| G | none | no ATC control/`SEP`; see-and-avoid + CARs |

- `SEP` formal separation | `CR` conflict resolution for identified aircraft in ATC comm | `TFC` traffic information | `O/R` on request.
- `C/D → E` when ATC unit closed: check published hours + NOTAM.
- `C/D runway:` `SEP ALL`; this does **not** mean airborne VFR–VFR separation.
- `T:` clearance/TFC/flight following ≠ collision-avoidance transfer. Lookout + right-of-way remain.
- Sources: [TC AIM 2026-2 RAC 2.8.1–2.8.7](https://tc.canada.ca/sites/default/files/2026-10/aim-2026-2_rac_en.pdf) · [Standard 821.01 definitions](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/sor-96-433/standards/standard-821-canadian-domestic-air-traffic-control-separation-standards-canadian-aviation-regulations-cars)
***
