# CPAER coverage matrix — content audit

**Reviewed:** 22 October 2026 · **Baseline:** [`3dbd013`](https://github.com/jraph/aero-cave/tree/3dbd013ba1e93160727d40b6fde8f4a0e50ca0f4) · **Stage:** Phase 2, first content audit; migration gates remain closed.

**Syllabus:** [TC TP 12881, seventh edition, August 2026](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881) ([PDF](https://tc.canada.ca/sites/default/files/2026-08/FINAL%20v1.3%20CPL%20EN%20-%20August%202026%20-%20TP12881E%20Seventh%20Edition.pdf)). Unofficial editorial mapping; TC source, no endorsement.

## Reading the matrix

- **Covered (C):** substantive explanation/rule/calculation found for the stated scope; not a certification of exam readiness or current regulatory accuracy.
- **Partial (P):** useful content exists, but specified syllabus elements/depth are absent.
- **Missing (M):** no substantive treatment located in the active Markdown collection; acronym expansions/source pointers alone do not count.
- **Conflicting (X):** incompatible current/historical framing or statements found; compare sources before choosing wording.
- **Needs verification (V):** evidence/applicability cannot support a reliable coverage decision yet. Never silently count as Covered.

**Granularity:** topic-group screening across the syllabus; individual numbered items for Flight Instruments and Human Factors below. Air Law regulation-by-regulation and remaining numbered-item expansion are **not complete**. No aggregate completeness percentage: grouped and individual rows have different denominators. TP topic numbering is local to its named group; Psychology jumps from 5 to 7 in the source.

**Evidence:** links identify actual sections inspected, not merely matching titles. All 14 active numbered cards were consulted; the bilingual formula collection and abbreviation glossary were checked as supplementary evidence. Attachments, archive and external publications are not counted as study-card coverage. Proposed ownership is editorial, not permission to move content. All rows inherit the baseline, syllabus revision and review date above; source currency remains as recorded in [CONTENT_REVIEW](CONTENT_REVIEW.md), not freshly revalidated here.

**Owner keys:** 01 theory; 02 practical procedures; 03 performance/operations; 04 law; 05 weather products; 06 shared calculations; 07 C150M-specific data; 08 systems. NAV / INST / HF = proposed topic home, path undecided. Retain 09–12 as IFR companions and 13 as ME companion.

## Air Law — regulation families and procedure groups

| TP scope | Status | Actual evidence | Proposed owner | Missing detail / overlap / action |
|---|---|---|---|---|
| Part I: definitions; inspection, document return, records | P | [04 night][law-night], [04 records][law-records] | 04 | Selected definitions/record duties; 103.02–.04 not systematically explained. |
| Part II: marks, registration, transfer, leasing | P | [04 registration][law-reg] | 04 | CoR/transfer/interim detail present; marks, owner eligibility and 203 leasing need item-level checks. |
| Part III: aerodromes/airports | P | [04 aerodromes][law-ad] | 04 | Circuit/suitability ≠ complete markers, lighting, prohibitions and fire-prevention rules. |
| Part IV: licences, recency, medical, FTUs | P | [04 validity][law-valid], [04 recency][law-recency], [03 CPL][cpl] | 04; 03 context | Licence/medical/recency substantial; foreign licences, full personal-log rules, medical examiner and FTU provisions incomplete. |
| 601 airspace | P | [04 class/service matrix][law-class] | 04 | Classes and ATC-service distinctions present; forest-fire restrictions, lasers and directed light not developed. |
| 602 general operating rules | P | [04 PIC][law-pic], [04 right of way][law-row] | 04 | Core rules present; not all listed provisions: smoking, fuelling/start, towing, formation, parachuting, fuel dumping, refusal/accommodation, etc. |
| 602 equipment and survival | P | [04 over water][law-water], [04 day equipment][law-day] | 04 | Detailed carriage thresholds present; 602.58–.60 and full land-survival exceptions require individual checks. |
| 602 planning and fuel | P | [04 plans][law-plan], [04 fuel][law-fuel] | 04; 06 math | Filing/closure and reserves present; full plan/arrival content, overdue reporting and crew instructions incomplete. |
| 602 aerodrome/MF/noise | P | [04 MF][law-ad] | 04 | Reporting provisions cited as range; individual calls/timing and 602.105–.106 noise rules not fully set out. |
| 602 VFR/OTT/SVFR | P | [04 controlled][law-vfr], [04 SVFR][law-svfr], [04 OTT][law-ott] | 04 | Useful minima; SVFR reported-ground-visibility/radio conditions and OTT destination conditions referenced rather than fully specified. |
| 602 radiocommunications/security | P | [08 radio failure][sys-radio], [04 tower lights][law-lights] | 04; 08 failure | VFR failure actions/light signals present; language/watch duties, interception, ADIZ and ESCAT incomplete. |
| 603 special operations | M | No dedicated explanation found | 04 | Event, parachuting and miscellaneous SFOC applicability/certification. |
| 604 private operators | P | [04 commercial scope][law-scope], [04 duty][law-duty], [04 extensions][law-ext] | 04 | Flight/FDP detail ≠ complete operational control, documents, cabin safety, qualifications, manuals and SMS. |
| 605 flight authority / serviceability | P | [04 authorities][law-auth], [04 no MEL][law-mel] | 04 | Strong authority/no-MEL treatment; MEL-equipped deferral and full equipment/placard standards incomplete. |
| 605 equipment | P | [04 night][law-night-eq], [04 ELT][law-elt], [04 oxygen][law-o2] | 04 | Night/O2/ELT detailed; all belt/child-restraint/lock/light/transponder conditions not individually covered. |
| 605 maintenance and records | P | [04 approvals][law-maint], [04 records][law-records] | 04 | Substantive record/release distinctions; full schedule and elementary-work requirements still need item checks. |
| 606 miscellaneous | P | [01 documents][vfr-doc] | 04 | Insurance existence only; munitions, insurance applicability/amounts and synthetic training equipment incomplete. |
| 700 general / Division III fatigue | P | [04 duty][law-duty], [04 extensions][law-ext] | 04 | Base tables, split/UOC covered in detail; reserve/standby, acclimatization, disruptive schedules, positioning and controlled rest incomplete. |
| 700 Division IV medevac fatigue | M | [04 applicability note][law-duty] only | 04 | Regime distinguished but listed 700.100–.134 requirements not taught. |
| 702 aerial work | P | [04 night equipment][law-night-eq], [04 applicability][law-duty] | 04 | Selected cross-references; authorization/plans, external loads, qualifications/training/manuals and separate fatigue regime incomplete. |
| 703 air taxi | P | [04 SE night/IFR][law-night-eq], [04 passenger weights][law-weights] | 04 | Selected strong topics; systematic 703 operating/equipment/crew/training/manual requirements absent. |
| 706 operator maintenance | P | [04 maintenance control][law-maint] | 04 | PRMCS ≠ complete maintenance arrangements/elementary work/servicing rules. |
| TSB reporting/evidence | C | [04 TSB][law-tsb] | 04 | Definitions, incident applicability, who/when and evidence preservation present; retain thresholds/qualifiers. |
| ATS procedures/services | P | [04 class/service][law-class], [04 wake][law-wake], [FIC/FSS reader][recall-fic] | 04; NAV index | Service types/readbacks/wake present; CFA, VFR holds, LAHSO, incursion prevention and ESCAT need explicit treatment. |
| International/legal framework | P | [04 international plan][law-plan], [04 cargo][law-cargo] | 04 | International plan/DG references ≠ entry/transit/customs, CTA licensing, Labour Code rights/duties or DG rules. |

**Law follow-through:** expand each listed CAR provision and its associated standard into its own row before marking Gate 1 complete. Do not infer complete coverage from a linked regulation number.

## Navigation — group screening

| TP group | Status | Actual evidence | Proposed owner | Missing detail / overlap / action |
|---|---|---|---|---|
| Definitions | P | [01 navigation][vfr-nav], [06 headings][calc-heading], [06 coordinates][calc-coord] | NAV; 06 math | Basic track/heading/bearing/variation present; rhumb/great circle, isogonal/agonic, air/ground positions need explanation. |
| Maps/charts | P | [01 CFS scan][vfr-cfs], [06 coordinates][calc-coord] | NAV | Scale/coordinates and publication use present; projections, VTA/VNC differences, contour/symbol interpretation incomplete. |
| Time/longitude/twilight | C | [reader time zones/twilight][recall-time], [06 clocks][calc-clock] | NAV; 06 math | 24-hour/UTC/date rollover, longitude/zone offsets and worked twilight-chart correction present; actual CFS factors remain location-specific. |
| Pilot navigation | P | [02 navigation flow][proc-nav], [06 1:60][calc-160], [01 nav][vfr-nav] | NAV; 02 application | Lost/divert/ETA/1:60 useful; fixes, 10° lines, double-track-error execution, low-level DR and air/ground plot examples incomplete. |
| Velocity triangle | P | [06 wind triangle][calc-wind] | NAV; 06 math | Equations present; plotted solution and worked multi-leg application missing. |
| Navigation computers | P | [06 calculations][calc-units], [07 calibration][poh-cal] | 06 | Formula library ≠ practical E6B wind/altitude/airspeed procedure and checks. |
| Preflight preparation | P | [03 planning][ops-plan], [04 preflight][law-preflight], [01 CFS][vfr-cfs] | NAV checklist; 04 legal | Good planning list; complete annotated chart/log preparation and NOTAM/application exercise missing. |
| Radio propagation/bands | M | Acronym/frequency mentions only | NAV | LF/HF/VHF propagation mechanisms, bands and operational limitations. |
| VOR | P | [06 intercepts][calc-nav], [10 receiver checks][ifr-check] | NAV; 06 math | Geometry/check tolerances present; signal/equipment theory, airway use and position fixes incomplete. |
| ADF | P | [06 intercepts][calc-nav], [10 NDB errors][ifr-check] | NAV; 06 math | RB/BTS/BFS and capture examples strong; receiver theory/checks, route use, fix construction and time-distance technique incomplete. |
| RMI | P | [06 ADF-card row][calc-nav] | NAV | Head/tail interpretation present; slaving/source failures and limitations undeveloped. |
| GNSS/GPS | P | [10 RNAV][ifr-gnss], [12 setup][proc-setup] | NAV; 09–12 application | Mode/integrity/sequence reminders; constellation/receiver principles, limitations and T-routes incomplete. |
| Other surveillance aids | P | [06 DME][calc-nav], [04 ELT][law-elt], [04 surveillance][law-wake] | NAV; 04 legal | DME geometry/ELT detail present; PSR/SSR, ADS-B and TCAS working principles/use incomplete; glossary definitions do not fill gaps. |
| EFB / portable devices | P | [12 readiness][proc-ready], [12 programming workload][proc-amend] | NAV; HF cross-link | Backup/setup/distraction reminders; EFB limitations, power contingency and lithium-battery fire management not taught systematically. |

## Meteorology — group screening

| TP group | Status | Actual evidence | Proposed owner | Missing detail / overlap / action |
|---|---|---|---|---|
| Atmosphere | P | [16 ISA][met-isa] | 16 | ISA/density present; composition, vertical structure, expansion/compression/mobility incomplete. |
| Pressure | P | [16 systems][met-pressure], [16 wind][met-wind] | 16 | High/low/isobars present; station vs sea-level pressure and measurement/reduction need detail. |
| Meteorological altimetry | C | [16 altitude/density][met-da], [16 pressure traps][met-alt], [06 cold correction][calc-cold] | 16; 06 formulas | PA/DA/settings and high-low/warm-cold effects explained. Approximation assumptions retained. |
| Temperature | P | [16 temperature][met-temp], [06 conversion][calc-temp] | 16; 06 formulas | Lapse/inversion/conversion present; heating mechanisms, horizontal differences/isothermal layers incomplete. |
| Moisture | P | [16 formation][met-cloud], [16 precipitation][met-precip] | 16 | Dewpoint/cloud/precip/lapse present; RH, latent heat and full phase-change/sublimation treatment incomplete. |
| Stability | P | [16 lapse/stability][met-stability], [16 lift][met-cloud] | 16 | Conditional stability and lifting present; stability modification, subsidence/convergence need more depth. |
| Clouds | P | [16 families][met-families] | 16 | Families/significance present; recognition/structure and hazard association need richer examples. |
| Surface visibility layers | C | [16 fog][met-fog], [16 visibility][met-vis] | 16 | Formation/types, haze/smoke/blowing obstructions substantively described; 05 decodes. |
| Turbulence | P | [16 turbulence][met-turb], [05 PIREP][wx-pirep] | 16; 05 reporting | Causes/wave/shear useful; intensity/reporting criteria incomplete. |
| Wind | P | [16 wind/local][met-wind], [16 jet][met-jet] | 16 | Forces/local winds/shear present; centrifugal balance, veer/back, gust/squall and seasonal jet variation incomplete. |
| Air masses | P | [16 masses][met-mass] | 16 | Source/classification/modification present; North American seasonal/geographic examples missing. |
| Fronts | P | [16 CF/WF tables][met-front] | 16; 05 decisions | Strong surface sequences; cross-section diagrams, frontogenesis/frontolysis, trowal/upper fronts incomplete. |
| Icing | P | [16 structural][met-ice], [16 carb ice][met-carb] | 16; 08 system; 05 gate | Types/engine effects/freezing precipitation present; hoar-frost mechanism needs explicit treatment. |
| Thunderstorms | P | [16 thunderstorms][met-ts], [16 microburst][met-micro] | 16; 05 gate | Ingredients/stages/hazards strong; air-mass versus frontal types/squall-line structure need expansion. |
| Other hazards | P | [16 TS hazards][met-ts], [16 smoke][met-vis] | 16 | Tornado/smoke mentions; hurricane, forest-fire meteorology, dust devils and eclipse hazards not developed. |
| Weather services | P | [05 FIC][wx-fic], [reader services][recall-fic] | 05 | FIC/FSS/inflight products present; CFPS access/use and complete service limitations need audit. |
| Observations/reports | P | [05 METAR][wx-metar], [05 PIREP][wx-pirep] | 05 | Decoding/PIREP useful; AWOS/LWIS/AUTO sensor/report limitations only briefly addressed. |
| Forecasts | P | [05 TAF][wx-taf], [05 GFA][wx-gfa], [05 upper winds][wx-upper] | 05; 16 theory | GFA timing/interpretation strong; full TAF/FB/AIRMET/SIGMET issue/validity, FB code examples incomplete. |
| Analysis/prognostic charts | M | Product scan/source pointers only | 05; 16 interpretation | Surface/500 hPa analysis, 700–400 hPa prog, symbols, issue/validity and worked chart interpretation. |

## Aeronautics — systems, theory and operations screening

| TP group | Status | Actual evidence | Proposed owner | Missing detail / overlap / action |
|---|---|---|---|---|
| Airframes | P | [07 aircraft][poh-aircraft], [07 preflight][poh-preflight] | 08; 07 example | Type-specific inspection ≠ construction types, handling/care/securing theory. |
| Gear/brakes/flaps | P | [08 gear][sys-gear], [08 brakes][sys-brake], [08 flaps][sys-flap] | 08 | Failure response stronger than mechanical/hydraulic/electrical working principles. |
| Engines | P | [08 essentials][sys-eng], [08 powerplant][sys-power], [08 MP][sys-mp] | 08 | Turbine/prop/ignition detail; 2/4-stroke, diesel, FADEC, exhaust/cooling and handling theory incomplete. |
| Electric propulsion | M | No substantive explanation found | 08 | Motors, electronic magneto, charging, battery types, limitations/operation. |
| Carburation | P | [07 carburetor][poh-carb], [08 mixture][sys-mix], [08 carb ice][sys-carb] | 08; 07 example | Operation/mixture/heat effects present; venturi/float/metering theory incomplete. |
| Fuel injection | P | [08 alternate air][sys-induction] | 08 | Induction escape actions ≠ fuel-injection working principle/icing distinctions. |
| Electrical | P | [08 alternator][sys-elec], [07 electrical][poh-elec] | 08 | Supply/battery/load-shed present; bus protection, lighting, grounding/bonding/circuit theory incomplete. |
| Lubrication/oils | P | [08 oil][sys-oil], [07 oil][poh-oil] | 08; 07 example | Indications/grades example; lubrication methods, venting, filters, relief/cooler theory incomplete. |
| Fuel systems/fuels | P | [08 grades][sys-fuel-grade], [08 fuel][sys-fuel], [07 tanks][poh-fuel] | 08 | Grade/FSII/contamination strong; detonation/preignition, vapour lock, heaters, baffling and fuelling/bonding incomplete. |
| Other systems | P | [08 pressurization][sys-press], [08 heat][sys-heat], [08 vacuum][sys-gyro], [04 O2][law-o2] | 08; 04 legal | Outflow/relief detailed; O2 system architecture and de/anti-ice/environmental operating principles incomplete. |
| Flight principles | M | [01 lift equation][theory] is related evidence only | 01 | Bernoulli and Newton principles are not actually explained. |
| Forces | P | [01 aerodynamics][theory], [06 load][calc-load] | 01; 06 math | Lift/drag/CP/equilibrium/turn relation present; manoeuvre force diagrams and roll-upset dynamics incomplete. |
| Aerofoils | P | [01 geometry/washout][theory], [16 icing][met-ice] | 01 | AOA/chord/ice effects present; pressure distribution, incidence/downwash/vortices need expansion. |
| Propellers | P | [08 pitch/governor][sys-power], [13 critical engine][me-critical] | 01 theory; 08 systems | Pitch/feather strong; efficiency vs speed, gyroscopic/slipstream/torque theory and care incomplete. |
| Wing design | P | [01 AR/washout/camber][theory] | 01 | Selected design concepts only; sweep, dihedral/anhedral, slots/slats/fences/strips, spoilers, generators, winglets, canards incomplete. |
| Load factor | P | [06 load][calc-load], [07 structural][poh-struct] | 01; 06 math | Turn/stall/weight/VA relations strong; linear manoeuvres, structural envelopes and gust loads incomplete. |
| Stability | P | [01 CG effects][vfr-perf] | 01 | CG consequences ≠ longitudinal/lateral/directional, inherent, static/dynamic stability explanation. |
| Flight controls | P | [02 core][proc-core], [08 controls][sys-controls] | 01 theory; 02 technique | Actions/failures present; axes, yaw-roll coupling, adverse yaw, balancing, trim design and autopilot axes/modes incomplete. |
| Flight instruments | P | Detailed item matrix below | INST; 08 failures | Separate principles from failure/recovery procedures; no new path selected. |
| Operations/general | P | [02 procedures][proc-core], [04 aerodrome][law-ad], [11 lights][plate-light] | 03; 02 technique; 04 law | Strong procedures; reader also gives hydroplaning recall. Wildlife/conservation, beacon/obstruction/marshalling, incursions, wheelbarrowing/porpoising and interference need item-level checks. |
| Aircraft performance | P | [01 aero][theory], [02 procedures][proc-core], [03 performance][ops-perf], [06 speeds][calc-va], [07 speeds][poh-speeds] | 03; 01 theory; 06 math | Recall/techniques strong; range/endurance optimization, stall speed vs altitude, safe recovery heights, external-load approvals incomplete. |
| Performance charts | P | [07 chart rules][poh-charts], [07 climb][poh-climb], [13 calculations][me-calc] | 03; 07/13 examples | Chart assumptions/samples ≠ complete worked takeoff/landing/cruise/crosswind/slope/surface/RSC calculations. |
| Weight and balance | P | [06 W&B][calc-wb], [04 passenger weights][law-weights], [07 envelope][poh-wb], [13 W&B][me-wb] | 03; 06 math; 04 legal methods | Calculations/standard+segmented data strong; MAC/weight terms, categories, ZFW vs MZFW need joined explanation/examples. |
| Wake turbulence | P | [04 wake][law-wake] | 03; 04 ATS minima | Strength/drift and separation present; phase-specific takeoff/landing avoidance scenarios incomplete. |
| SAR/survival | P | [04 ELT][law-elt], [04 survival][law-water], [08 emergency equipment][sys-elt] | 03; 04 law | Equipment rules present; SAR services/requesting/aiding others and practical survival techniques incomplete. |
| Critical-surface contamination | P | [05 fluids/HOT][wx-hot], [04 clean aircraft][law-ice], [16 ice][met-ice] | 03 operations; 05 HOT use | Fluid types/LOUT/HOT strong; cold soaking, full removal/inspection practices and performance effects need completion. |
| Human Factors | P | Detailed item matrix below | HF; 01/03 reminders | Mnemonics and IFR threat lists do not replace physiology/psychology/TEM teaching. |

## Flight Instruments — individual TP items

Numbers below refer to the named TP group. Evidence supports only the specific stated part.

| Group · item | Status | Actual evidence | Gap / next check |
|---|---|---|---|
| Pitot/static · 1 pitot | C | [08 pitot/static][sys-pitot] | ASI input/routing + blockage response present. |
| Pitot/static · 2 static | C | [08 pitot/static][sys-pitot] | Shared ASI/ALT/VSI supply and common-mode failure present. |
| Pitot/static · 3 anti-ice | P | [08 pitot/static][sys-pitot] | Pitot heat/static distinction; heat checks, limitations/system variants incomplete. |
| Pitot/static · 4 alternate static | P | [08 pitot/static][sys-pitot] | Source selection/errors noted, but cabin-pressure mechanism/corrections not explained. |
| ASI · 1 operating principle | P | [08 pitot/static][sys-pitot] | Inputs identified; differential-pressure mechanism missing. |
| ASI · 2 errors/malfunctions | P | [08 blockage table][sys-pitot] | Blockages covered; position/instrument/compressibility effects not fully developed. |
| ASI · 3 markings | C | [07 marking table][poh-mark] | White/green/yellow/red meanings and C150M-specific values retained separately. |
| ASI · 4 IAS/CAS/TAS | P | [07 calibration][poh-cal], [reader airspeeds][recall-stall] | Unit/calibration/density relations present; explicit definitions and conversion sequence incomplete. |
| VSI · 1 operating principle | M | No substantive mechanism found | Calibrated leak and pressure-rate operation. |
| VSI · 2 errors/malfunctions | P | [08 static failures][sys-pitot] | Blockage response present; other errors/limitations missing. |
| VSI · 3 lag | M | No substantive treatment found | Lag and interpretation. |
| Altimeter/encoder · 1 operating principle | P | [16 altitude][met-da], [08 independent sources][sys-alt] | Setting/pressure concepts present; aneroid/encoder operation missing. |
| Altimeter/encoder · 2 errors/malfunctions | P | [08 altitude failure][sys-alt], [16 pressure traps][met-alt] | Static/common-source/temp effects present; setting/mechanical/encoding error treatment incomplete. |
| Radio/radar altimeter · 1 principle | M | [04 radar-altimeter requirement][law-night-eq] is requirement only | Radio height measurement mechanism. |
| Radio/radar altimeter · 2 limitations | M | No substantive treatment found | Terrain/attitude/range/surface limitations. |
| Compass · 1 principle | M | [08 compass][sys-compass] lists errors only | Magnetic alignment/construction. |
| Compass · 2 dip | P | [08 compass][sys-compass] | Named, not physically explained. |
| Compass · 3 variation | C | [06 true/magnetic][calc-heading] | Conversion/sign convention explicit. |
| Compass · 4 adverse factors | P | [08 compass][sys-compass] | Oscillation/turbulence/dip present; local magnetic/electrical interference incomplete. |
| Compass · 5 reading | P | [06 heading conversions][calc-heading] | Conversion ≠ compass-card reading/reciprocal trap exercise. |
| Compass · 6 deviation | P | [06 true/magnetic/compass][calc-heading] | Correction named; aircraft magnetic cause not developed. |
| Compass · 7 correction card | M | No worked card found | Read/interpolate/apply correction card. |
| Compass · 8 turn/acceleration errors | P | [08 compass][sys-compass] | ANDS/UNOS scope present; explanation and worked rollouts incomplete. |
| Compass · 9 serviceability | P | [12 instrument check][proc-inst] | Taxi direction/flags check; complete compass-specific check incomplete. |
| Compass · 10 swinging | M | No substantive treatment found | Purpose/method/when required. |
| Compass · 11 ground/inflight heading check | P | [02 nav][proc-nav], [12 instrument check][proc-inst] | Cross-check reminders; practical heading check methods incomplete. |
| Gyroscope · 1 operating principle | M | [08 gyro failure][sys-gyro] concerns failures | Rotor principles not explained. |
| Gyroscope · 2 inertia | M | No substantive treatment found | Rigidity/inertia. |
| Gyroscope · 3 precession | P | [08 gyro failure][sys-gyro] | Symptom named, physical principle absent. |
| Heading indicator · 1 principle | M | [08 gyro failure][sys-gyro] is related evidence only | DI operation. |
| Heading indicator · 2 errors | P | [08 gyro failure][sys-gyro] | Slow/frozen indications; drift/precession errors need systematic explanation. |
| Heading indicator · 3 limits | P | [08 gyro failure][sys-gyro] | Source failure addressed; design/manoeuvre limitations missing. |
| Heading indicator · 4 power | C | [08 gyro failure][sys-gyro] | Legacy vacuum source qualified; actual equipment may differ. |
| Heading indicator · 5 slaved compass/HSI/RMI | P | [06 RMI row][calc-nav] | Needle interpretation only; slaving/erection/reference failure absent. |
| Attitude indicator · 1 principle | M | [08 gyro failure][sys-gyro] concerns failures | Attitude reference/erection mechanism. |
| Attitude indicator · 2 errors | P | [08 gyro failure][sys-gyro] | Failure recognition; acceleration/turn/erection errors not taught. |
| Attitude indicator · 3 limits | P | [08 gyro failure][sys-gyro] | Failure caveat only; instrument-specific pitch/bank limits absent. |
| Attitude indicator · 4 power | C | [08 gyro failure][sys-gyro] | Legacy vacuum dependence and common failure explained; retain scope. |
| Turn instrument · 1 principle | M | [12 instrument check][proc-inst] shows response only | Rate gyro; turn indicator vs coordinator distinction. |
| Turn instrument · 2 errors | P | [08 gyro failure][sys-gyro] | Failed TC fallback; systematic errors absent. |
| Turn instrument · 3 limits | P | [12 no-gyro][proc-nogyro] | Standard-rate use; rate vs bank/attitude limitations need explanation. |
| Turn instrument · 4 power | C | [08 gyro failure][sys-gyro] | Often electric; architecture explicitly qualified. |
| EFIS · 1 principle | M | No substantive treatment found | Sensors, processing, displays. |
| EFIS · 2 errors | M | No substantive treatment found | Sensor/reference/data/display failure chains. |
| EFIS · 3 limits | M | No substantive treatment found | System dependencies and degraded modes. |
| EFIS · 4 power | M | Generic electrical failure is not EFIS coverage | Main/standby/backup sources and common dependencies. |
| Instrument flying · 1 lost visual reference | P | [07 cloud/vacuum][poh-vac], [12 unusual attitudes][proc-ua] | Recovery reminders; full inadvertent-IMC transition incomplete. |
| Instrument flying · 2 control/performance instruments | P | [09 emergencies][ifr-emerg], [02 core][proc-core] | Phrase/attitude-power model present; instrument classification not set out. |
| Instrument flying · 3 scan/interpretation | P | [08 cross-check][sys-scan], [10 HF][ifr-human] | Cross-check/fixation warnings; scan technique needs explanation. |
| Instrument flying · 4 control | P | [12 procedures][proc-inst] | Useful IFR procedures; integrated basic-control lesson incomplete. |
| Instrument flying · 5 partial panel | C | [08 gyro failure][sys-gyro], [12 failure][proc-gyro] | Identify unreliable sources, reliable substitutes, workload/ATC help. |
| Instrument flying · 6 unusual attitudes | P | [12 nose high/low][proc-ua] | Nose-low flow useful; nose-high question-mark wording requires source/instructor check (issue X-03). |

**Proposed INST ownership:** one future principles section; 08 retains failures; 02/12 retain procedural applications; 06 retains calculations. Do not transplant the full IFR collection into CPAER.

## Human Factors — individual TP items

| Group · item | Status | Actual evidence | Gap / next check |
|---|---|---|---|
| Physiology · 1 hypoxia/hyperventilation | P | [01 human][vfr-human], [04 O2][law-o2] | Hypoxia/night/O2 reminders; symptom differentiation, mechanisms and hyperventilation absent. |
| Physiology · 2 trapped gas | M | No substantive treatment found | Boyle-law effects and mitigation. |
| Physiology · 3 decompression/scuba | P | [08 pressurization][sys-press] | Emergency response only; decompression physiology/scuba risk missing. |
| Physiology · 4 visual scan/references | P | [02 scan][proc-core], [05 night][wx-night] | Lookout/night hazards; visual scan technique/limitations incomplete. |
| Physiology · 5 hearing | M | No substantive treatment found | Hearing limits/protection. |
| Physiology · 6 orientation/illusions | P | [10 IFR HF][ifr-human], [05 night][wx-night] | Named vestibular/visual illusions; mechanisms, recognition and prevention incomplete. |
| Physiology · 7 positive/negative G | P | [06 load factor][calc-load] | Aircraft-load math ≠ physiological effects/tolerance. |
| Physiology · 8 airsickness | M | No substantive treatment found | Causes, recognition, mitigation. |
| Physiology · 9 body rhythm/jet lag | M | No substantive treatment found | Circadian disruption/acclimatization. |
| Physiology · 10 sleep/fatigue | P | [01 human][vfr-human], [04 duty][law-duty] | Degradation/legal clocks present; sleep debt and fatigue-management physiology incomplete. |
| Physiology · 11 anaesthetics | M | No substantive treatment found | Fitness implications; authoritative medical guidance needed. |
| Physiology · 12 blood donation | M | No substantive treatment found | Fitness implications; authoritative medical guidance needed. |
| Environment · 1 health/fitness | P | [01 IMSAFE][vfr-human], [04 fitness][law-fit] | Mnemonic/legal requirement; specific fitness self-assessment incomplete. |
| Environment · 2 diet/nutrition/fasting | M | No substantive treatment found | Practical human-performance consequences. |
| Environment · 3 medications | P | [01 human][vfr-human], [04 fitness][law-fit] | Impairment warning; prescribed/OTC effects and assessment incomplete. |
| Environment · 4 substances | P | [04 fitness][law-fit] | Alcohol/drug rule; broader impairment/residual effects not developed. |
| Environment · 5 pregnancy | M | No substantive treatment found | Appropriate aeromedical source required. |
| Environment · 6 heat/cold | P | [04 survival][law-water] | Equipment/climate reminder; physiological impairment not explained. |
| Environment · 7 noise/vibration | M | No human-performance treatment found | Engine-vibration diagnosis does not cover exposure effects. |
| Environment · 8 smoking/vaping | M | No substantive treatment found | Oxygen transport/exposure/human-performance effects. |
| Environment · 9 toxins/CO | P | [08 CO][sys-co] | CO source/symptoms/action substantive; other toxic exposures incomplete. |
| Psychology · 1 decision process | P | [01 mnemonics][vfr-human], [03 mindset][ops-mind] | Acronyms without step definitions/worked decision. |
| Psychology · 2 influences | P | [03 mindset][ops-mind], [03 emergency/human][ops-human] | Customer/time/pressure and hazardous attitudes; bias mechanisms incomplete. |
| Psychology · 3 situational awareness | P | [10 IFR HF][ifr-human], [12 mode checks][proc-setup] | Threat/mode awareness reminders; acquisition/comprehension/projection and loss/recovery incomplete. |
| Psychology · 4 stress | P | [03 pressures][ops-mind] | Stressors implicit; acute/chronic stress and performance relationship undeveloped. |
| Psychology · 5 risk management | P | [05 risk matrix][wx-matrix], [03 planning][ops-plan] | Good weather decision tool; broader risk assessment/mitigation cycle incomplete. |
| Psychology · 7 hazardous attitudes | C | [03 emergency/human][ops-human] | Five attitudes and corresponding antidotes explicitly listed. |
| Psychology · 8 attention/workload | P | [10 IFR HF][ifr-human], [12 amendments][proc-amend] | Fixation/programming workload warnings; information processing/channel capacity incomplete. |
| Equipment · 1 controls/displays | P | [12 source/mode checks][proc-setup], [11 nav source][plate-source] | Specific traps present; human-interface/selection/interpretation error model incomplete. |
| Equipment · 2 SOP rationale | P | [08 checklist][sys-checklist], [12 discipline][proc-discipline] | Practice/sequence useful; explicit rationale/benefits incomplete. |
| Equipment · 3 maps/charts errors | P | [11 plate method][plate-method], [01 CFS][vfr-cfs] | IFR chart traps useful; broader VFR chart interpretation errors missing. |
| Equipment · 4 automation/EFB/GPS | P | [12 programming][proc-amend], [10 HF][ifr-human] | Automation surprise/heads-down risks; EFB/moving-map dependence and mitigation incomplete. |
| Equipment · 5 checklists/manuals | C | [08 checklist][sys-checklist] | Memory items vs flow vs current checklist, and current POH priority explicitly distinguished. |
| Relations · 1 communication | P | [04 briefing][law-brief], [12 ATC workload][proc-atc] | Passenger/ATC examples; crew/ground/maintenance handoffs incomplete. |
| Relations · 2 family/peer/goals | P | [01 external pressure][vfr-human], [03 mindset][ops-mind] | Generic external pressure; family/peer/goal-conflict scenarios absent. |
| Relations · 3 employer pressure | P | [03 commercial mindset][ops-mind] | Pressure identified; refusal/escalation/decision exercise absent. |
| TEM · 1 sources/contributors | P | [10 threats][ifr-human], [03 mindset][ops-mind] | Threat lists; explicit TEM framework/classification absent. |
| TEM · 2 countermeasures | P | [12 setup gates][proc-setup], [05 decisions][wx-matrix] | Real countermeasures exist; not connected into TEM method. |
| TEM · 3 undesired aircraft state | M | No explicit TEM treatment found | Distinguish threat, error and resulting aircraft state. |
| TEM · 4 CRM/SPRM relationship | P | [10 single-pilot HF][ifr-human] | Single-pilot practices; explicit CRM/SPRM/TEM relationship absent. |

**Proposed HF ownership:** dedicated topic home, path undecided. Keep legal fitness/O2/fatigue limits in 04; systems CO/decompression response in 08; weather go/no-go tool in 05. HF supplies explanations/scenarios and links, not competing thresholds.

## Conflicts and verification queue

| ID | Evidence | Classification | Required comparison before any correction |
|---|---|---|---|
| X-01 | [01 current-cycle section][vfr-cycle] calls July cycle historical; [09][ifr-cycle], [10][inrat-cycle], [11][plate-cycle], [12][proc-cycle] still call 9 July–3 September current and generalize publication intervals. | Confirmed internal currency conflict | Product-specific NAV CANADA schedules/edition dates; separate historical worked examples from current guidance. Do not replace all dates with one universal cycle. |
| V-02 | [05 TAF][wx-taf] uses total TEMPO duration ≤half; [glossary memory traps][abbr-traps] uses <half. | Wording conflict; authoritative threshold not resolved in this audit | Current TC AIM MET / forecast coding definition; compare Markdown and HTML before updating. |
| X-03 | [12 unusual attitudes][proc-ua]: nose-high line includes “reduce if near stall?” alongside qualified generic recovery wording. | Needs verification; unresolved instructional ambiguity | Applicable training guidance + exact AFM/instructor procedure; do not compress into a universal memory action. |
| V-04 | [07 source status][poh-source] says serial/configuration not confirmed. | Applicability unresolved, not proven wrong | Exact aircraft POH revision, supplements, equipment/STCs and W&B before treating example data as fleet authority. |
| V-05 | [06 VOR][calc-nav] links Canadian and FAA check scopes in [10][ifr-check]. | Qualified cross-reference, **not** an established contradiction | Preserve Canadian versus FAA origin; do not import US intervals/recordkeeping into Canada. |
| V-06 | [16 cloud/freezing][met-cloud], [reader weather][recall-weather] now separate classroom and parcel models. | Useful alternative assumptions, **not** duplication/conflict | Preserve assumptions and environmental-freezing-level distinction; compare full versions before consolidation. |

## Ordered follow-through

1. Complete **numbered-item expansion** for Air Law, Navigation, Meteorology, systems/theory/operations; attach precise content evidence to each item, distinguishing no treatment from incomplete depth. This report does not close Gate 1.
2. Prioritize HF and INST gaps already isolated above; audit authoritative teaching sources before drafting new study facts. Electric propulsion, EFB fire/power, medevac/aerial-work fatigue and chart interpretation are additional explicit gaps.
3. Resolve X-01 / V-02 / X-03 by source comparison in a separate content change; update all affected Markdown/HTML/Pebbles and review records together.
4. For each actual consolidation, record **source A + source B → owner + every retained unique fact/example/qualifier/source/Pebble + links back**. No exact-duplicate deletion is proposed here.
5. Select one small pilot only after item-level audit and target path/compatibility decisions. Keep card 05 decoding versus 16 theory, card 06 shared formulas, and 07 aircraft-specific examples complementary.

**Change scope:** audit/planning only. No study card, HTML reader, language/search code, manifest, service worker, URL or Pebble changed.

## Evidence links

[ifr-check]: cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md#navigation-aid-checks
[ifr-gnss]: cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md#rnavgnss
[ifr-human]: cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md#human-factors--single-pilot-ifr
[inrat-cycle]: cheatsheets/10_inrat_knowledge_core_av_cave_v0_3.md#current-publication-cycle
[plate-light]: cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md#lighting--runway--visual-aids
[plate-source]: cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md#frequencies--nav-source
[plate-method]: cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md#inrat-plate-question-method
[plate-cycle]: cheatsheets/11_cap_plate_reading_qrc_av_cave_v0_2.md#current-publication-cycle
[proc-setup]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#approach-setup-gate
[proc-ready]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#before-engine-start--ifr-readiness
[proc-amend]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#atc-amendment
[proc-inst]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#ifr-cockpit--instrument-check
[proc-nogyro]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#no-gyro-vectors
[proc-ua]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#unusual-attitude--nose-high
[proc-gyro]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#vacuum--attitude-heading-failure
[proc-discipline]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#scope--discipline
[proc-atc]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#atc-workload-tools
[proc-cycle]: cheatsheets/12_ifr_procedures_qrc_av_cave_v0_2.md#current-publication-cycle
[me-critical]: cheatsheets/13_multi_engine_knowledge_core_av_cave_v0_1.md#critical-engine
[me-calc]: cheatsheets/13_multi_engine_knowledge_core_av_cave_v0_1.md#performance-calculations-required
[me-wb]: cheatsheets/13_multi_engine_knowledge_core_av_cave_v0_1.md#wb-me-traps
[met-isa]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#atmosphere--isa
[met-pressure]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#pressure-systems
[met-wind]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#wind
[met-da]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#pressure-altitude--density-altitude
[met-alt]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#altimetry--pressure-traps
[met-temp]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#temperature--dew-point
[met-cloud]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#moisture--cloud-formation
[met-precip]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#precipitation
[met-stability]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#lapse-rates--stability
[met-families]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#cloud-families
[met-fog]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#fog
[met-vis]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#visibility
[met-turb]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#turbulence
[met-jet]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#jet-stream--cat
[met-mass]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#air-masses
[met-front]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#cf--before--passing--after
[met-ice]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#structural-icing
[met-carb]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#carburetor-icing
[met-ts]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#thunderstorms--ingredients
[met-micro]: cheatsheets/16_weather_knowledge_core_av_cave_v0_1.md#microburst--llws
[vfr-cycle]: cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md#current-publication-cycle
[vfr-doc]: cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md#docs--legal
[vfr-nav]: cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md#navigation
[vfr-cfs]: cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md#cfs--aerodrome-scan
[theory]: cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md#aerodynamics--lift-drag--equilibrium
[vfr-perf]: cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md#performance--wb
[vfr-human]: cheatsheets/01_flight_theory_vfr_knowledge_av_cave_v0_6.md#human--emergency
[proc-core]: cheatsheets/02_flight_training_procedures_av_cave_v0_2.md#core
[proc-nav]: cheatsheets/02_flight_training_procedures_av_cave_v0_2.md#vfr-nav--diversion--lost
[cpl]: cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md#cpl-a-requirements
[ops-plan]: cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md#planning--fuel--go-no-go
[ops-perf]: cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md#performance--wb
[ops-mind]: cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md#cpl-mindset
[ops-human]: cheatsheets/03_licensing_performance_operations_av_cave_v0_2.md#emerg--human
[law-night]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#night-definition
[law-records]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#journey-log--technical-records--car-6059297
[law-reg]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#acft-reg--airworthiness--cor--coa
[law-ad]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#aerodrome--mf-operations
[law-valid]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#licence-validity-stack
[law-recency]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#recency
[law-class]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#vfr-separation--conflict-resolution-by-class
[law-pic]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#pic-responsibility--emergency
[law-row]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#right-of-way--collision-avoidance
[law-water]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#over-water--survival--survol-de-leau--survie
[law-day]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#day-vfr-equipment--power-driven
[law-plan]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#flight-plan--itinerary
[law-fuel]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#fuel-requirements
[law-vfr]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#vfr-minima--controlled
[law-svfr]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#special-vfr
[law-ott]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#vfr-ott
[law-scope]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#commercial-scope--flight-time-comparison--september-2026
[law-duty]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#flight-time--fdt--fdp--temps-de-vol--service
[law-ext]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#fdp-extensions--split--unforeseen--car-604-vs-700-division-iii
[law-auth]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#flight-authorities--car-507
[law-mel]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#unserviceable-equipment--no-mel
[law-night-eq]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#night-vfr-equipment--pax--commercial
[law-elt]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#elt--car-6053840
[law-o2]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#oxygen--oxygène--car-6053132
[law-maint]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#maintenance-approvals--abnormal-occurrences
[law-weights]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#passenger-weights--masse-des-passagers--aim-2026-1-rac-347
[law-tsb]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#tsb-occurrence-reporting--aim-gen-3334
[law-wake]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#ats-surveillance--wake--rvsm
[law-cargo]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#baggage--cargo
[law-lights]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#twr-light-signals--nordo
[law-preflight]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#pre-flight-information
[law-ice]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#aircraft-icing--clean-aircraft
[law-fit]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#fitness--alcohol--drugs
[law-brief]: cheatsheets/04_canadian_air_law_core_av_cave_v0_2_compact.md#passenger-briefing
[wx-pirep]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#airmet--sigmet--pirep
[wx-fic]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#fic--in-flight-update
[wx-metar]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#metar--speci-scan
[wx-taf]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#taf-scan--groups
[wx-gfa]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#gfa
[wx-upper]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#upper-winds--temperature
[wx-hot]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#de-anti-icing--fpd--hot--dégivrage--antigivrage
[wx-night]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#night-weather
[wx-matrix]: cheatsheets/05_weather_decoding_go_nogo_qrc_av_cave_v0_2_compact.md#personal-weather-matrix
[calc-heading]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#true--magnetic--compass
[calc-coord]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#coordinates--distance--map
[calc-clock]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#clocks--logbook
[calc-160]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#1-in-60-rule
[calc-wind]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#wind-correction--nav-triangle
[calc-units]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#units--constants
[calc-nav]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#navigation-aids--adf--vor--dme--intercepts
[calc-cold]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#cold-temperature--altitude-error
[calc-temp]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#temperature
[calc-load]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#load-factor--accelerated-stall
[calc-va]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#manoeuvring-speed--stall-speed-notation
[calc-wb]: cheatsheets/06_aviation_formulas_conversions_av_cave_v0_2.md#weight--balance
[poh-cal]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#airspeed-calibration-snapshots
[poh-aircraft]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#aircraft
[poh-preflight]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#preflight--poh-highlights
[poh-carb]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#carburetor--induction
[poh-elec]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#electrical-system
[poh-oil]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#oil
[poh-fuel]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#fuel
[poh-struct]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#manoeuvre--structural-limits
[poh-speeds]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#normal-speeds--max-weight-unless-noted
[poh-charts]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#performance-chart-rules
[poh-climb]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#rate-of-climb-memory--1600-lb-flaps-up-full-throttle-standard-temperature
[poh-wb]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#weight--cg--baggage
[poh-mark]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#airspeed-indicator-markings
[poh-vac]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#vacuum-system-failure--cloud
[poh-source]: cheatsheets/07_c150m_poh_core_av_cave_v0_2_compact.md#source--status
[sys-radio]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#radio-failure
[sys-gear]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#landing-gear-malfunction
[sys-brake]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#brake-failure
[sys-flap]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#flap-malfunction--asymmetry
[sys-eng]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#engine-essentials
[sys-power]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#powerplant--prop--l4-cave
[sys-mp]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#manifold-pressure--mp--l4
[sys-mix]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#mixture
[sys-carb]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#carburetor-icing
[sys-induction]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#induction--alternate-air
[sys-elec]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#electrical--alternator-failure
[sys-oil]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#oil-pressure--temperature
[sys-fuel-grade]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#aviation-fuel-grades--fsii--l4
[sys-fuel]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#fuel--starvation--contamination
[sys-press]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#cabin-pressurization--outflow--l4
[sys-heat]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#cabin-heat--defrost
[sys-gyro]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#vacuum--gyro-failure
[sys-controls]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#flight-control-malfunction
[sys-elt]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#elt--emergency-equipment
[sys-pitot]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#pitot--static
[sys-alt]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#altimeter-failure--unreliable-altitude
[sys-compass]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#magnetic-compass
[sys-scan]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#source--discipline--scan
[sys-co]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#carbon-monoxide
[sys-checklist]: cheatsheets/08_aircraft_systems_failures_qrc_av_cave_v0_2_compact.md#checklist--declaration
[ifr-cycle]: cheatsheets/09_ifr_knowledge_core_av_cave_v0_2.md#current-publication-cycle
[ifr-emerg]: cheatsheets/09_ifr_knowledge_core_av_cave_v0_2.md#ifr-emergencies
[recall-fic]: cheatsheets/CPAER_Formulas_Recall_EN_FR.md#fir--fic
[recall-time]: cheatsheets/CPAER_Formulas_Recall_EN_FR.md#twilight--time-zones--dst--crépuscule--fuseaux--heure-avancée
[recall-stall]: cheatsheets/CPAER_Formulas_Recall_EN_FR.md#stall--airspeed--décrochage--vitesse
[recall-weather]: cheatsheets/CPAER_Formulas_Recall_EN_FR.md#altitude--weather--altitude--météo
[abbr-traps]: https://github.com/jraph/aero-cave/blob/3dbd013ba1e93160727d40b6fde8f4a0e50ca0f4/cheatsheets/Aviation_Abbreviations_MANAB_CFS_TC_EN_FR.md#L477
