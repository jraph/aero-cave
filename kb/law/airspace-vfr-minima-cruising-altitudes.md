# Airspace, VFR minima & cruising altitudes / Espace aérien, minimums VFR et altitudes de croisière
<!-- concept: law-airspace | level: PPL CPL -->

[Index](README.md) · concept `law-airspace` · unit IDs are stable: never rename one.

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
| `<1000 AGL` | `2 SM` (unless otherwise authorized in an AOC) | `3 SM` | clear of cloud |

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
#### IFR general
<!-- id: law-ifr-general | from: 04 | also: ifr | level: CPL IR -->

- IFR operation requires IFR flight plan/clearance where applicable, instrument rating/current privileges, appropriate equipment and compliance with IFR minima/procedures. `[CAR 602.121+]`
- Alternate, takeoff, approach, landing and approach-ban rules are separated in CAR 602.122–602.131.
- `T:` advisory visibility, approach-ban threshold and DA/MDA visual-reference rule are three different concepts.
***
#### Airspace classes / entry
<!-- id: law-airspace-entry-memory | from: 01, 04 | level: PPL CPL -->

- Class-by-class VFR entry and ATC service: see `law-vfr-separation-conflict-resolution-by-class` ([matrix](#vfr-separation--conflict-resolution-by-class)).
- Check current chart/CFS for floor, ceiling, transponder and communication requirements.
- `T:` class rules≠weather minima.
***
#### VFR separation / conflict resolution by class
<!-- id: law-vfr-separation-conflict-resolution-by-class | from: 04 | also: law-atc | level: PPL CPL -->

| Class | VFR entry | Airborne ATC service |
|---|---|---|
| A | prohibited | IFR only; `SEP ALL` |
| B | clearance + specified equipment/qualification; `CVFR` | `SEP ALL`, incl VFR–VFR |
| C | clearance before entry | `SEP` IFR–IFR; `CR` IFR–VFR as needed; `TFC` all; VFR–VFR `CR O/R` after TFC |
| D | 2-way comm established before entry | `SEP` IFR–IFR only; `TFC` all; workload/equipment permitting: IFR–VFR `CR`, VFR–VFR `CR O/R` |
| E | no VFR clearance generally; IFR controlled; MF/XPDR rules may apply | `SEP` IFR–IFR only; VFR `TFC O/R` workload/equipment permitting; may stop without notice |
| F | obey `CYR/CYA/CYD` | surrounding class unless specified; may be controlled, uncontrolled or both |
| G | none; uncontrolled, CARs still apply | no ATC control/`SEP`; see-and-avoid + CARs |

- `SEP` formal separation | `CR` conflict resolution for identified aircraft in ATC comm | `TFC` traffic information | `O/R` on request.
- `C/D → E` when ATC unit closed: check published hours + NOTAM.
- `C/D runway:` `SEP ALL`; this does **not** mean airborne VFR–VFR separation.
- `T:` clearance/TFC/flight following ≠ collision-avoidance transfer. Lookout + right-of-way remain.
- Sources: [TC AIM 2026-2 RAC 2.8.1–2.8.7](https://tc.canada.ca/sites/default/files/2026-10/aim-2026-2_rac_en.pdf) · [Standard 821.01 definitions](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/sor-96-433/standards/standard-821-canadian-domestic-air-traffic-control-separation-standards-canadian-aviation-regulations-cars)
***
#### Transponder airspace — CAR 601.03
<!-- id: law-transponder-airspace-car-601-03 | also: law-atc | level: PPL CPL IR -->

- Transponder airspace = all Class **A, B, C** + any Class **D or E** specified as transponder airspace in the DAH. [CAR 601.03]
- Need transponder + automatic pressure-altitude reporting there (Class A also ADS-B per AIM). [AIM RAC 2.8.1–2.8.5]
- `T:` Class D/E only if DAH says so. Check chart/DAH, not class letter alone.
- `M:` `ABC always · D/E if DAH`.
***
#### Class F special use airspace — CAR 601.04
<!-- id: law-class-f-special-use-car-601-04 | level: PPL CPL IR -->

| Type | Rule |
|---|---|
| CYR restricted | no flight unless authorized by user agency in DAH [CAR 601.04(2)] |
| CYA advisory | non-participants may enter; avoid unless participating; extra vigilance [RAC 2.8.6.3] |
| CYD danger (intl waters) | no ATC clearance for non-participants [RAC 2.8.6.2] |
| MOA | ATC won't clear non-participating IFR through active MOA unless IFR separation possible; VFR need not avoid [RAC 2.9.4] |
| Joint-use | ops authorized by controlling agency [RAC 2.8.6.5] |

- ID: `CY` + `R/A/D` + 3 digits; advisory activity letter in brackets, e.g. `CYA113(A)`. [RAC 2.8.6.1]
- IFR vs active Class F: ATC separates unless pilot states permission, ALTRV APVL, or contact/visual approach. IFR gets 500 ft vertical from active CYA (wake may need 1000). [RAC 2.8.6.1, 2.8.6.3]
- NOTAM-activated CYR: NOTAM ≥24 h before activation. [RAC 2.8.6.6]
- `T:` MSA/TAA ignore CYA, CYR, blasting areas: pilot stays clear. [CAP GEN]
- Activity letters: A acro · F test · H hang glider · M military · P parachute · S soaring · T training. [CAP GEN symbol legend]
***
#### Forest fire areas — 601.15–.17
<!-- id: law-forest-fire-601-15-17 | level: CPL -->

- `R` No flight **over or within 5 NM of a forest fire area below 3 000 ft AGL**, nor in airspace described in a forest fire **NOTAM** (location + dimensions of fire area, airspace of fire control operations).
- `R` Exempt: aircraft operating at the request or with authorization of the **fire control authority** · with Minister's **written authorization** (for public safety or to support an A/D in/near the fire area; conditions apply; authorization **on board**) · TC enforcement/surveillance staff.

- Sources: [601.15](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-601.15.html), [601.16](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-601.16.html), [601.17](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-601.17.html).
***
#### Pebble
<!-- id: law-airspace-vfr-minima-cruising-altitudes-pebble | level: PPL CPL IR -->

- CLASSES `A IFR only | B clearance + specified equipment/qualification (CVFR) | C clearance before entry | D two-way comm before entry | E no VFR clearance generally, IFR controlled | F CYR/CYA/CYD | G uncontrolled, CARs still apply | class rules ≠ weather minima`
- ATC SERVICE `B SEP ALL | C SEP IFR–IFR, CR IFR–VFR, TFC all | D SEP IFR–IFR only | E SEP IFR–IFR only | clearance/TFC ≠ collision-avoidance transfer`
- VFR CONTROLLED CAR 602.114 `visual reference to surface | flight vis ≥3 SM | cloud 500 ft vertical + 1 SM horizontal | control zone: ground vis ≥3 SM, ≥500 ft from surface except TKOF/LDG`
- VFR UNCONTROLLED CAR 602.115 `≥1000 AGL: day 1 SM / night 3 SM, cloud 500 ft vert / 2000 ft horiz | <1000 AGL aeroplane: day 2 SM / night 3 SM, clear of cloud`
- SVFR `control zone only | pilot requests | aeroplane flight vis ≥1 SM | clear of cloud, visual reference to surface | night aeroplane: to land at destination`
- CRUISE CAR 602.34 `>3000 ft AGL | VFR 000–179° odd +500 / 180–359° even +500 | SDA magnetic track, NDA true track | track ≠ heading`
- AERODROME `left turns unless CFS/ATC says right | no flight below 2000 ft over an aerodrome except listed operations | ATF calls ≠ MF mandatory reports`
- XPDR/CLASS F `601.03: ABC always, D/E if DAH | CYR = authorization · CYA = avoid unless participating · CYD no clearance · MOA no IFR through unless separated | IFR 500 ft from active CYA | CYR NOTAM ≥24 h`
- FOREST FIRE `no flight <3000 AGL over or ≤5 NM | NOTAM airspace | exempt: fire authority, Minister written authorization on board, TC`
***
