# ATC, radio & transponder / ATC, radio et transpondeur
<!-- concept: law-atc | level: PPL CPL -->

[Index](README.md) · concept `law-atc` · unit IDs are stable: never rename one.

***
#### Radio / transponder
<!-- id: law-radio-transponder | from: 01 | level: PPL CPL -->

- XPDR: `1200 ≤12500` | `1400 >12500` | `7600 comm` | `7700 emerg` | `7500 hijack`.
- Call: who-called | who-you-are | where | what-want. Readback: clearance/runway/hold-short/alt/hdg/squawk.
- `T:` “roger”≠cleared. listen before transmit. aviate before radio.
***
#### ATC clearances / instructions
<!-- id: law-atc-clearances-instructions | from: 04 | level: PPL CPL IR -->

- Comply with ATC clearances/instructions received and accepted, except emergency authority or amended clearance. `[CAR 602.31]`
- If unable/unsafe: advise ATC immediately; do not silently improvise.
- `T:` clearance ≠ information; “roger” does not mean approval to deviate.
***
#### ATS surveillance / wake / RVSM
<!-- id: law-ats-surveillance-wake-rvsm | from: 04 | level: CPL -->

| CAVE | Rule / trap |
|---|---|
| `G` ATS SEP | Surveillance **5 NM standard / 3 NM authorized terminal**; other minima may apply. [AIM RAC](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim) |
| `G` vertical | **1,000 ft below FL290**; RVSM **FL290–FL410 incl. 1,000 ft** for approved ACFT; higher non-RVSM generally **2,000 ft**. |
| `G` WAKE CAT | **S=A380 · H>136t · M>7t to <136t · L≤7t**. |
| `G` WAKE NM | Leader→follower: **S→S/H/M/L=4/6/7/8 · H→H/M/L=4/5/6 · M→L=4**; unspecified pairs still need normal ATS SEP. |
| `G` TKOF MIN | Specified same/close-parallel THLD: **H→following 2 min**; specified INTXN/downstream: **3 min**; **M→L same THLD advisory, INTXN 3 min**. Check configuration. |
| `G` WAKE AVOID | Strongest heavy+clean+slow; vortex ↓ and downwind drift; avoid behind/below/downwind · jet blast/propwash ≠ vortex WAKE. |

`M:` **ATS 5/3NM | RVSM FL290–410 1,000ft | WAKE S 4/6/7/8 · H 4/5/6 · M→L 4NM | H TKOF 2/3min cases**.
***
#### TWR light signals — NORDO
<!-- id: law-twr-light-signals-nordo | from: 04 | also: emg-comms | level: PPL CPL -->

| Signal | IN FLT | ON GND |
|---|---|---|
| Steady GN | LDG CLNC | TKOF CLNC |
| Flash GN | Return for LDG (not CLNC) | Taxi CLNC |
| Steady RED | Give way / circle | STOP |
| Flash RED | A/D unsafe / NO LDG | Taxi clear LDG area / RWY |
| Flash WHITE | — | Return starting point |
| Alternating RED/GN | Extreme caution | Extreme caution |

- `P:` ACK IN FLT → rock wings; night → flashing lights as prescribed. [TC AIM RAC](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim).
- `T:` Flash GN ≠ LDG CLNC; **steady GN** = LDG CLNC.
- `M:` **IN FLT GN steady=LDG/flash=return · RED steady=circle/flash=unsafe | GND GN steady=TKOF/flash=taxi · RED steady=STOP/flash=clear · WHITE=return**.
***
#### Communications · weather / Communications · météo
<!-- id: fx-communications-weather-communications-m-t-o | from: F | also: met-products | kind: glossary | level: PPL CPL -->

| Label | English | Français |
|---|---|---|
| RADIO | FSS/FIC information and advisories | Information et conseils FSS/FIC |
| RCO | Remote radio link to FSS/FIC: FISE or RAAS | Liaison radio distante FSS/FIC : FISE ou RAAS |
| DRCO | Dial-up RCO; 4 deliberate mic clicks | RCO à liaison téléphonique; 4 pressions délibérées |
| FISE | Flight Information Service En Route | Service d’information de vol en route |
| RAAS | Remote Aerodrome Advisory Service | Service consultatif télécommandé d’aérodrome |
| ATIS | Recorded terminal weather and operational information; note letter | Information météo et opérationnelle enregistrée; noter lettre |
| CLNC DEL | Clearance delivery | Délivrance des autorisations |
| APRON | Apron movement management/advisory | Gestion/conseils des mouvements sur aire de trafic |
| GND | Ground control: taxi instructions | Contrôle sol : instructions de circulation |
| GND ADV | Ground advisory at certain MF sites; may relay pre-taxi clearances | Conseils au sol à certains sites MF; relais possible d’autorisations avant circulation |
| TWR | Tower: runway and local airborne control | Tour : contrôle piste et circulation aérienne locale |
| MF | Mandatory Frequency; mandatory reporting area, not necessarily controlled | Fréquence obligatoire; comptes rendus obligatoires, pas nécessairement contrôlé |
| ATF | Aerodrome Traffic Frequency for uncontrolled traffic coordination | Fréquence de trafic d’aérodrome pour coordination non contrôlée |
| TML | Terminal ATC | Contrôle terminal |
| ARR / DEP | Arrival / departure ATC | Contrôle des arrivées / départs |
| VFR ADV | VFR advisory service | Service consultatif VFR |
| PAL | Peripheral station: remote ATC radio site | Station périphérique : site radio ATC distant |
| UNICOM | Private airport information/advisory radio | Radio privée d’information/conseils d’aéroport |
| APRT RDO | Airport Radio, usually CARS observer/communicator | Radio d’aéroport, généralement observateur/communicateur CARS |
| A/G | Air/Ground communications | Communications air-sol |
| MIL | Military frequency; read named unit | Fréquence militaire; lire unité indiquée |
| VDF / UDF | VHF / UHF direction finding: bearing from your transmission | Radiogoniométrie VHF / UHF : relèvement de votre émission |
| INTL AIR | International air-carrier communications, commonly HF | Communications transporteurs internationaux, souvent HF |
| AWOS | Automated Weather Observation System | Système automatisé d’observation météorologique |
| LWIS | Limited Weather Information System: wind, temperature, dew point, altimeter | Système limité : vent, température, point de rosée, calage |
| AUTO | Local automated weather; does not meet METAR/SPECI/LWIS reporting requirements | Météo automatisée locale; ne satisfait pas exigences METAR/SPECI/LWIS |
| PMSV | Pilot to Metro Service: military meteorological personnel | Liaison pilote–service météo militaire |
| VOLMET | Weather for aircraft in flight: voice broadcast | Météo pour aéronefs en vol : diffusion vocale |
| D-VOLMET | Weather via data link; D = data link | Météo par liaison de données; D = données |
***
#### FIR · FIC
<!-- id: fx-fir-fic | from: F | also: law-airspace | level: PPL CPL -->

| Label | English | Français |
|---|---|---|
| 7 FIR | Vancouver, Edmonton, Winnipeg, Toronto, Montréal, Moncton, Gander | Vancouver, Edmonton, Winnipeg, Toronto, Montréal, Moncton, Gander |
| 4 briefing FIC | Kamloops, Edmonton, London, Québec | Kamloops, Edmonton, London, Québec |
| Whitehorse | FIC for flight-plan processing/alerting; Kamloops provides telephone pilot briefings | FIC pour traitement plans de vol/alerte; Kamloops assure exposés téléphoniques |
| Five areas | Course shorthand: Pacific, Edmonton, Ontario, Québec, Atlantic; London serves Ontario + Atlantic. These are not the seven FIRs. | Raccourci pédagogique : Pacifique, Edmonton, Ontario, Québec, Atlantique; London dessert Ontario + Atlantique. Ce ne sont pas les sept FIR. |
***
#### Radar service and vectors — AIM RAC 1.5
<!-- id: law-radar-service-vectors-rac-1-5 | also: ifr-enr | level: IR -->

- Vectoring IFR (and CVFR, IFR arrivals): ATC assumes terrain/obstacle clearance until normal nav resumes. [RAC 1.5.2, 1.5.5(a)]
- ATC tells you when vectors end — except vectors to final or circuit: approach clearance = resume own nav. [RAC 1.5.2]
- Identified ≠ relieved of see-and-avoid or terrain responsibility. [RAC 1.5.2]
- Comm failure on low vector: climb to published minimum altitude unless VMC. [RAC 1.5.5(a)]
- VFR on vectors: pilot keeps terrain, traffic, VFR weather responsibility. [RAC 1.5.4, 1.5.5(b)]
- Identified: position reports over compulsory points no longer required until told to resume. [RAC 8.1]
- `T:` "radar contact" ≠ terrain clearance for VFR.
***
#### Transponder, SSR, PSR, ADS-B — AIM COM 7–8
<!-- id: law-transponder-ssr-psr-ads-b-com-7-8 | also: nav-radio | level: PPL CPL IR -->

| System | Principle | Limit |
|---|---|---|
| PSR | range + azimuth from reflected RF | no transponder needed; no altitude/ID |
| SSR | interrogates transponder 1030 MHz, reply 1090 MHz; range by timing | sees only aircraft with working transponder |
| Mode C | adds pressure altitude | |
| Mode S | selective address; base for ADS-B Out + TCAS II | |
| ADS-B | aircraft broadcasts own position (1090 ES via Mode S) | ATS matches flight ID to flight plan |

- Codes: VFR `1200` ≤12 500 ASL · `1400` above · IFR high level `2000` unless assigned · `7500` unlawful (only once ATC told) · `7600` comm · `7700` emergency. [COM 8.2–8.8]
- IDENT only when ATS asks. [COM 8.5]
- `T:` SSR has longer range + positive ID; PSR still sees non-transponder targets. [COM 7.1–7.2]
***
#### Pebble
<!-- id: law-atc-radio-transponder-pebble | level: PPL CPL IR -->

- XPDR `1200 ≤12,500 | 1400 >12,500 | 7600 comm | 7700 emergency | 7500 hijack`
- ATC CAR 602.31 `comply with clearances/instructions received and accepted, except emergency authority or amended clearance | unable → advise immediately | “roger” ≠ cleared`
- LIGHTS `in flight: steady green = LDG clearance / flashing green = return for landing / steady red = give way, circle / flashing red = unsafe, no landing | ground: steady green = TKOF / flashing green = taxi / steady red = STOP / flashing red = taxi clear / flashing white = return to start`
- ATS / WAKE `surveillance 5 NM standard / 3 NM authorized terminal | 1,000 ft below FL290; RVSM FL290–FL410 1,000 ft approved ACFT | wake S→S/H/M/L 4/6/7/8 NM · H→H/M/L 4/5/6 · M→L 4 | H ahead: 2 min same threshold, 3 min intersection`
- RADAR `IFR vectors: ATC owns terrain until vectors end · approach clearance = own nav | VFR keeps terrain | identified → no compulsory reports | SSR 1030/1090 needs XPDR · PSR sees all · IDENT only on request`
***
