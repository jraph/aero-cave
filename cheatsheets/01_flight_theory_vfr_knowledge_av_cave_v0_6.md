### FLIGHT THEORY & VFR KNOWLEDGE — AV-CAVE v0.6
`TARGETED CPAER REVIEW: 2026-09-06` | see `00_CPAER_REVIEW_NOTES.md` for scope and remaining gaps
`R` rule | `F` formula | `P` proc | `T` trap | `M` memory | `!` safety | `?` verify
`RELEASE:` `LEGAL/CYCLE-REF PROVISIONAL` | `CANONICAL SOURCE:` `flight_theory_vfr_knowledge_av_cave_v0_6.md` | `NOT FLIGHT AUTHORITY`
***
#### Current publication cycle

- The July 2026 cycle statement in this card is historical. Check each product’s printed effective dates and current amendments.
- Publication schedules differ by product; do not assign a universal 56-day validity to all charts and publications.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### Docs / legal

- PIC responsible. Onboard as applicable: CofR, flight authority/CofA, current POH/AFM/supplements, journey log unless exception, required licences/medical.
- Insurance coverage is required; the CARs do not impose one universal onboard proof-of-insurance document rule for every private flight.
- `T:` valid document≠current pilot or airworthy aircraft. Current CFS/AIP/NOTAM/POH wins.
- Pax brief: belts/doors/exits/no smoking/ELT/survival/sterile cockpit/emerg. `M:` SAFETY.
***
#### Flight plan / itinerary / PIREP

- VFR flight plan/itinerary unless within `25 NM` dep AD. Intl = flight plan. `T:` itinerary needs responsible person.
- Arrival report: ident + plan/itinerary + dep + arr + date/time. `T:` close it.
- VFR pos report: ident-pos-time-alt-plan-dest. PIREP: loc/time-alt-type-cloud-temp-wind-turb-ice-rmk.
***
#### CFS / aerodrome scan

- `P:` aerodrome ID/elevation→RWY dimensions/surface/slope→circuit direction/altitude→FREQ/MF/ATF→lighting/PCL→`PRO`→`CAUTION`→services/fuel→nearby airspace.
- CFS sections: General | Aerodrome Directory | Planning | Radio Navigation/Communications | Military | Emergency.
- `T:` CFS page still requires current NOTAM/AIP SUP; a Trigger NOTAM is only a pointer.
***
#### Radio / transponder

- XPDR: `1200 ≤12500` | `1400 >12500` | `7600 comm` | `7700 emerg` | `7500 hijack`.
- Call: who-called | who-you-are | where | what-want. Readback: clearance/runway/hold-short/alt/hdg/squawk.
- `T:` “roger”≠cleared. listen before transmit. aviate before radio.
***
#### Airspace

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
- See the [VFR separation / conflict-resolution matrix](04_canadian_air_law_core_av_cave_v0_2_compact.md#vfr-separation--conflict-resolution-by-class) for who ATC separates in Classes B–E.
***
#### VFR minima / cruise altitude

- CTRL: flight vis `≥3 SM`, cloud `1 SM horiz / 500 ft vert`, visual reference to surface. CZ: reported ground vis also `≥3 SM`; stay `≥500 ft` from surface except takeoff/landing.
- UNCTRL ≥`1000 AGL`: day `1 SM`, night `3 SM`, cloud `2000h/500v`.
- UNCTRL <`1000 AGL` aeroplane: day `2 SM`, night `3 SM`, clear of cloud.
- CRZ >`3000 AGL`: SDA=`MTRK`, NDA=`TTRK`; `000–179 odd+500 / 180–359 even+500`. `T:` track≠heading.
***
#### MET

- METAR actual; SPECI special; TAF aerodrome forecast; GFA area; FD/FB winds/temp aloft.
- Clouds: FEW 1-2, SCT 3-4, BKN 5-7, OVC 8. Ceiling=lowest BKN/OVC/VV.
- Stable=smooth/layer/poor vis/steady precip. Unstable=bumps/CU/showers/good vis.
- `!:` TS/CB/gust front/wind shear/hail/icing/turb = avoid. Carb ice possible above freezing in humid partial power.
***
#### Altimetry / density altitude

- ISA SL: `29.92 / 1013 / 15°C`; lapse≈`2°C/1000 ft`.
- High→low or warm→cold = actual lower. `M:` look out below.
- DA↑ with temperature/humidity/pressure altitude↑. Weight does NOT change DA; it independently worsens takeoff/climb. Higher DA: roll↑ climb↓; TAS↑ for the same IAS.
- `F:` PA≈elev+(29.92-altset)×1000. DA≈PA+120×(OAT-ISA). `T:` approximation only.
***
#### Aerodynamics — lift, drag & equilibrium

| Key | Essential recall |
|---|---|
| `LIFT` | Force component ⟂ relative airflow; `L=½ρV²SCL` (V = TAS); AOA controls `CL` until critical AOA/stall. |
| `CP / CG / AC` | CP = location of resultant aero force on airfoil (moves with AOA); CG = weight acts here; AC ≈25% chord for typical subsonic airfoil (pitching moment approx constant with AOA). |
| `MOMENT` | Pitching moment about CG = force × perpendicular arm; trimmed unaccelerated FLT requires net pitching moment `ΣM(CG)=0` (tail force may balance wing/fuselage moment). |
| `DRAG` | Total = parasite + induced; parasite = form/pressure + skin friction + interference; induced = drag due to lift/downwash. |
| `SPD / DRAG` | At given GW/config/ALT in steady level FLT, IAS↓→AOA/induced drag↑; IAS↑→parasite drag↑; minimum total drag ≈ max `L/D`. |
| `EQUIL` | Straight/level/constant-speed simplified: `L=W; T=D; ΣM=0`; requires aligned thrust & negligible vertical thrust/tail geometry effects. |
| `BANK` | Coordinated level turn: `L cosφ=W`, `n=1/cosφ`, `Vs(turn)=Vs(level)√n` (same config/weight). |
| `T` | CP ≠ CG ≠ AC; lift vector ⟂ relative wind, not necessarily vertical; stall = critical AOA, not a fixed IAS. |

- `SRC:` [FAA PHAK, Ch. 4–5 · Principles/Aerodynamics of Flight](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak); general theory; aircraft POH/AFM governs performance.
***
#### Performance / W&B

- Vx=altitude/distance. Vy=altitude/time. Best glide=max distance no power. Min sink=max time.
- Headwind helps; tailwind hurts big. grass/soft/wet/snow roll↑ braking↓. +10% speed≈+21% energy.
- `F:` moment=`W×arm`; CG=`ΣM/ΣW`. `T:` within max weight≠within CG.
- FWD CG: stable↑ stall↑ elevator/flare↓. AFT CG: stable↓ stall/spin recovery worse.
***
#### Navigation

- Track=ground path. Heading=nose. Bearing=direction to object. Course=planned line.
- `T±V=M±D=C`; true→mag: east least, west best.
- `F:` time=dist/GS; fuel=time×burn; 1-in-60 error°≈offtrack×60/dist flown.
- Divert: decide early→dest→line feature→track/dist/GS/ETA/fuel→inform. Lost: climb safe→communicate→conserve→confess→comply.
***
#### Human / emergency

- IMSAFE | PAVE | DECIDE | 5P. `T:` external pressure makes bad plan feel reasonable.
- Hypoxia: night vision early. CO: heat off/vent/land. Meds/fatigue degrade before obvious.
- Emerg: aviate>navigate>communicate. MAYDAY×3→ident→problem→position→intention→POB/fuel.
- Rough engine: carb heat/mixture/fuel/mags/primer as POH/time. `T:` partial power can lure you past fields.
***
#### Pebble

- AERO `L⊥relative wind | CP resultant force / CG weight / AC≈¼ chord | ΣM(CG)=0 in trim | D=parasite(form+friction+interference)+induced | slow→induced↑; fast→parasite↑ | L/Dmax≈Dmin | straight level L=W,T=D | coordinated level turn n=1/cosφ, Vs×√n`
- docs-current | close plan | 1200/1400/7600/7700/7500 | A/B/C/D/E/F/G | CTRL 3-1-500 | unctl high 1/3+2000/500 | unctl low 2/3 COC | track≠hdg | hot-high-heavy bad | high→low/cold below | W×arm | T±V=M±D=C | 1:60 | lost C5 | aviate first.

***
#### Sources & review status

See the [separate review record](../CONTENT_REVIEW.md#historical-source-review-notes) for source editions, check dates and earlier validation notes.
