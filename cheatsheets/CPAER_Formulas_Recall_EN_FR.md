# CPAER · Formulas & quick recall / Formules et rappels

Condensed offline study reader · Formulas, navigation, CFS communications and NOTAMs · Reviewed 13 Oct 2026 / Révision 13 oct. 2026

***

**Time · fuel / Temps · carburant**

| Label | English | Français |
|---|---|---|
| Distance | D(NM) = GS(kt) × t(h) | D(NM) = vitesse sol(kt) × durée(h) |
| Time / Durée | t(min) = 60D/GS | t(min) = 60D/vitesse sol |
| GS / Vitesse sol | GS(kt) = 60D/t(min) | Vitesse sol(kt) = 60D/t(min) |
| Fuel / Carburant | Fuel = hourly flow × hours; endurance = usable fuel/flow | Carburant = débit horaire × heures; autonomie = carburant utilisable/débit |
| Specific range | GS/fuel flow = NM per fuel unit | Vitesse sol/débit = NM par unité de carburant |
***

**Wind · navigation / Vent · navigation**

| Label | English | Français |
|---|---|---|
| Components | Crosswind = W sin θ; headwind = W cos θ; θ is wind-from angle relative to course | Vent traversier = W sin θ; vent de face = W cos θ; θ entre provenance du vent et route |
| WCA / Dérive | WCA = asin(crosswind/TAS); steer into wind | Correction = asin(vent traversier/TAS); corriger vers le vent |
| Heading / Cap | True heading = true course + signed WCA | Cap vrai = route vraie + correction signée |
| T → M → C | Subtract EAST / add WEST: variation, then deviation | Soustraire EST / ajouter OUEST : déclinaison, puis déviation |
| Track error | TE° ≈ 60 × off-track/distance flown | Erreur de route ≈ 60 × écart latéral/distance parcourue |
| Closing angle | CA° ≈ 60 × off-track/distance remaining | Angle de convergence ≈ 60 × écart latéral/distance restante |
| Correction | TE + CA towards track; small-angle approximation | Erreur + convergence vers la route; approximation pour petits angles |
***

**Weight · balance / Masse · centrage**

| Label | English | Français |
|---|---|---|
| Moment | Moment = weight × arm | Moment = masse × bras de levier |
| CG | CG = total moment/total weight | CG = somme des moments/masse totale |
| Shift / Déplacement | ΔCG = moved weight × distance moved/total weight | ΔCG = masse déplacée × déplacement/masse totale |
| Required weight | w = total weight × ΔCG/distance moved | w = masse totale × ΔCG/déplacement |
| Add / remove | CGnew = (W × CGold ± w × arm)/(W ± w) | CGnouveau = (W × CGancien ± w × bras)/(W ± w) |
| % MAC / CMA | 100(CG − LEMAC)/MAC; common datum and units | 100(CG − bord d’attaque CMA)/CMA; même référence et unités |
***

**Altitude · weather / Altitude · météo**

| Label | English | Français |
|---|---|---|
| ISA | T°C ≈ 15 − 2 × altitude(thousands ft); troposphere | T°C ≈ 15 − 2 × altitude(milliers pi); troposphère |
| PA / AP | PA ≈ IALT + 1000(29.92 − setting inHg) | AP ≈ altitude indiquée + 1000(29,92 − calage inHg) |
| DA / AD | DA ≈ PA + 120(OAT − ISA at PA) | AD ≈ AP + 120(température extérieure − ISA à AP) |
| True altitude | Correction ft ≈ 4 × height above setting source(thousands ft) × ΔT°C; warm add, cold subtract | Correction pi ≈ 4 × hauteur au-dessus de la source du calage(milliers pi) × ΔT°C; chaud ajouter, froid soustraire |
| Temperature | F = 1.8C + 32; C = (F − 32)/1.8 | F = 1,8C + 32; C = (F − 32)/1,8 |
| DALR | Unsaturated rising parcel: −3°C/1000 ft | Parcelle ascendante non saturée : −3°C/1000 pi |
| SALR | Saturated rising parcel: ≈ −1.5°C/1000 ft; variable | Parcelle ascendante saturée : ≈ −1,5°C/1000 pi; variable |
| Dew point | Unsaturated parcel: ≈ −0.5°C/1000 ft | Point de rosée, parcelle non saturée : ≈ −0,5°C/1000 pi |
| Cloud base | Convective base AGL ft ≈ 400(T − Td) | Base convective AGL pi ≈ 400(T − Td) |
| Freezing level | Height change ft = 1000 × T/lapse rate(°C/1000 ft); use actual profile | Dénivelé pi = 1000 × T/gradient(°C/1000 pi); utiliser le profil réel |
***

**Stall · airspeed / Décrochage · vitesse**

| Label | English | Français |
|---|---|---|
| Load / Charge | n = 1/cos(bank): coordinated LEVEL turn only | n = 1/cos(inclinaison) : virage coordonné EN PALIER uniquement |
| Stall / Décrochage | Vs loaded = Vs × √n; Vs₂ = Vs₁√(W₂/W₁) | Vs sous charge = Vs × √n; Vs₂ = Vs₁√(W₂/W₁) |
| Approach / Approche | ≈ 1.3Vs0; POH speed takes precedence | ≈ 1,3Vs0; vitesse du manuel de vol prioritaire |
| Lift / Portance | L = ½ρV²SCL; dynamic pressure q = ½ρV² | L = ½ρV²SCL; pression dynamique q = ½ρV² |
| TAS | TAS = EAS√(ρ₀/ρ) | Vitesse vraie = vitesse équivalente × √(ρ₀/ρ) |
| TAS shortcut | ≈ CAS[1 + 0.02(PA/1000)]; rough; E6B for actual temperature | ≈ CAS[1 + 0,02(AP/1000)]; approximatif; E6B pour température réelle |
| 30° / 45° / 60° | n: 1.15 / 1.41 / 2; Vs factors: 1.07 / 1.19 / 1.41 | n : 1,15 / 1,41 / 2; facteurs Vs : 1,07 / 1,19 / 1,41 |
***

**Climb · descent / Montée · descente**

| Label | English | Français |
|---|---|---|
| Gradient | ft/NM = 60 × vertical speed(ft/min)/GS(kt) | pi/NM = 60 × vitesse verticale(pi/min)/vitesse sol(kt) |
| Required rate | ft/min = gradient(ft/NM) × GS/60 | pi/min = gradient(pi/NM) × vitesse sol/60 |
| Percent / Pourcentage | % = 100 × vertical/horizontal distance; same units | % = 100 × distance verticale/horizontale; mêmes unités |
| % → ft/NM | ft/NM = 60.76 × percent; 5% ≈ 304 ft/NM | pi/NM = 60,76 × pourcentage; 5% ≈ 304 pi/NM |
| 3° path / Pente | 3° ≈ 5.24% ≈ 318 ft/NM; NOT 3% | 3° ≈ 5,24% ≈ 318 pi/NM; PAS 3% |
| 3° rate / Taux | Descent ft/min ≈ 5.3 × GS; mental shortcut 5 × GS | Descente pi/min ≈ 5,3 × vitesse sol; raccourci 5 × vitesse sol |
| 3° distance | NM ≈ height to lose(ft)/318; rough 3 NM/1000 ft | NM ≈ hauteur à perdre(pi)/318; environ 3 NM/1000 pi |
| Descent time | Minutes = height change/vertical speed; NM = GS × minutes/60 | Minutes = dénivelé/vitesse verticale; NM = vitesse sol × minutes/60 |
| Worked / Exemple | Lose 4000 ft at GS120: ≈12.6 NM, 636 ft/min, 6.3 min on 3° | Perdre 4000 pi à GS120 : ≈12,6 NM, 636 pi/min, 6,3 min sur 3° |
| Wind / Vent | Same climb rate: headwind improves ground gradient; tailwind reduces it | Même taux de montée : vent de face améliore la pente sol; vent arrière la réduit |
***

**Turns / Virages**

| Label | English | Français |
|---|---|---|
| Standard rate | 3°/s; 90°=30s; 180°=60s; 360°=120s | 3°/s; 90°=30s; 180°=60s; 360°=120s |
| Rate / Taux | °/s ≈ 1091 tan(bank)/TAS(kt) | °/s ≈ 1091 tan(inclinaison)/TAS(kt) |
| Radius / Rayon | ft ≈ TAS²/[11.26 tan(bank)] | pi ≈ TAS²/[11,26 tan(inclinaison)] |
| Standard bank | bank = atan(3TAS/1091); 100kt≈15°; 150kt≈22° | inclinaison = atan(3TAS/1091); 100kt≈15°; 150kt≈22° |
| Double speed | Same bank: half turn rate, FOUR times radius | Même inclinaison : taux divisé par deux, rayon QUADRUPLÉ |
| Assumptions | Coordinated level turn; TAS; air-relative geometry; wind alters ground track | Virage coordonné en palier; TAS; géométrie dans l’air; vent modifie trajectoire sol |
***

**Radio · runway / Radio · piste**

| Label | English | Français |
|---|---|---|
| VHF range | NM ≈ 1.23(√h₁ + √h₂); 1.25 also used; feet above surface | NM ≈ 1,23(√h₁ + √h₂); 1,25 également; hauteurs en pi au-dessus de la surface |
| Rotating tyre | Dynamic hydroplaning kt ≈ 9√pressure(psi); 36psi→54kt | Pneu en rotation : aquaplanage dynamique kt ≈ 9√pression(psi); 36psi→54kt |
| Non-rotating tyre | kt ≈ 7.7√pressure(psi); 36psi→46.2kt | Pneu sans rotation : kt ≈ 7,7√pression(psi); 36psi→46,2kt |
| FISE frequencies | 123.275 / 123.375 / 123.475 / 123.550 MHz; use local published RCO | 123,275 / 123,375 / 123,475 / 123,550 MHz; utiliser RCO publié |
| 126.7 | Generally not monitored by FIC at dedicated FISE RCOs; broadcasts may occur | Généralement non veillée par FIC aux RCO FISE dédiés; diffusions possibles |
***

**Conversions**

| Label | English | Français |
|---|---|---|
| NM | 1 NM = 1.852km = 6076ft = 1.151 statute mi | 1 NM = 1,852km = 6076pi = 1,151 mille terrestre |
| Gallon | US 3.785L; Imperial 4.546L | US 3,785L; impérial 4,546L |
| Mass / length | 1kg = 2.205lb; 1m = 3.281ft | 1kg = 2,205lb; 1m = 3,281pi |
| Earth / Terre | 15° longitude/hour; 4min/degree; 1′ latitude ≈ 1NM | 15° longitude/heure; 4min/degré; 1′ latitude ≈ 1NM |
***

**Timing shortcuts / Estimation du temps**

| Label | English | Français |
|---|---|---|
| 60 kt | 1 NM/min · 10 NM = 10.00 min | 1 NM/min · 10 NM = 10.00 min |
| 90 kt | 1.5 NM/min · 10 NM = 6.67 min | 1.5 NM/min · 10 NM = 6.67 min |
| 100 kt | 1.66667 NM/min · 10 NM = 6.00 min | 1.66667 NM/min · 10 NM = 6.00 min |
| 120 kt | 2 NM/min · 10 NM = 5.00 min | 2 NM/min · 10 NM = 5.00 min |
| 150 kt | 2.5 NM/min · 10 NM = 4.00 min | 2.5 NM/min · 10 NM = 4.00 min |
| 180 kt | 3 NM/min · 10 NM = 3.33 min | 3 NM/min · 10 NM = 3.33 min |
***

**CFS servicing / Services CFS**

| Label | English | Français |
|---|---|---|
| 1 | Storage available | Entreposage disponible |
| 2 | Servicing / minor repairs | Entretien / réparations mineures |
| 3 | Major repairs | Réparations majeures |
| 4 | Extended-term parking | Stationnement prolongé |
| 5 | Tie-down facilities | Dispositifs d’amarrage |
| 6 | Plug-in facilities | Prises de branchement |
| 7 | Pick-up/drop-off only; no extended parking | Embarquement/débarquement seulement; aucun stationnement prolongé |
***

**Communications · weather / Communications · météo**

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

**FIR · FIC**

| Label | English | Français |
|---|---|---|
| 7 FIR | Vancouver, Edmonton, Winnipeg, Toronto, Montréal, Moncton, Gander | Vancouver, Edmonton, Winnipeg, Toronto, Montréal, Moncton, Gander |
| 4 briefing FIC | Kamloops, Edmonton, London, Québec | Kamloops, Edmonton, London, Québec |
| Whitehorse | FIC for flight-plan processing/alerting; Kamloops provides telephone pilot briefings | FIC pour traitement plans de vol/alerte; Kamloops assure exposés téléphoniques |
| Five areas | Course shorthand: Pacific, Edmonton, Ontario, Québec, Atlantic; London serves Ontario + Atlantic. These are not the seven FIRs. | Raccourci pédagogique : Pacifique, Edmonton, Ontario, Québec, Atlantique; London dessert Ontario + Atlantique. Ce ne sont pas les sept FIR. |
***

**NOTAM · header & Q-line / En-tête et ligne Q**

| Label | English | Français |
|---|---|---|
| Example / Exemple | Training example: H1234/26 NOTAMN; Q) CZUL/QMRLC/IV/NBO/A/000/999/4528N07345W005 | Exemple pédagogique : H1234/26 NOTAMN; Q) CZUL/QMRLC/IV/NBO/A/000/999/4528N07345W005 |
| 1 Header | H = series; 1234 = number; /26 = year | H = série; 1234 = numéro; /26 = année |
| 2 Type | NOTAMN new; NOTAMR replacement; NOTAMC cancellation | NOTAMN nouveau; NOTAMR remplacement; NOTAMC annulation |
| 3–5 | Q) qualifiers; CZUL FIR; QMRLC = runway closed (MR runway, LC closed) | Q) qualificatifs; CZUL FIR; QMRLC = piste fermée (MR piste, LC fermé) |
| 6 Traffic | I IFR; V VFR; IV both | I IFR; V VFR; IV les deux |
| 7 Purpose | N immediate attention; B briefing; O flight operations; M miscellaneous on request; K checklist | N attention immédiate; B exposé; O opérations de vol; M divers sur demande; K liste récapitulative |
| 8 Scope | A aerodrome; E en route; W navigation warning; AE aerodrome + en route | A aérodrome; E en route; W avertissement navigation; AE aérodrome + en route |
| 9–10 Vertical | Lower/upper in FL; 000/999 commonly default filtering values | Limites inférieure/supérieure en FL; 000/999 souvent valeurs de filtrage par défaut |
| 11–12 Geography | 4528N07345W = centre; 005 = 5 NM RADIUS | 4528N07345W = centre; 005 = RAYON de 5 NM |
| A / B / C | A location; B start UTC; C end UTC or PERM | A lieu; B début UTC; C fin UTC ou PERM |
| D / E / F / G | D schedule; E operational text; F/G lower/upper limits when applicable | D horaire; E texte opérationnel; F/G limites inférieure/supérieure si applicables |
***

**Common NOTAM codes / Codes NOTAM courants**

| Label | English | Français |
|---|---|---|
| QMRLC | Runway closed | Piste fermée |
| QMXLC | Taxiway closed | Voie de circulation fermée |
| QFALC | Aerodrome closed | Aérodrome fermé |
| QICAS | ILS unserviceable | ILS hors service |
| QILAS | Localizer unserviceable | Radiophare d’alignement hors service |
| QIGAS | Glide path unserviceable | Alignement de descente hors service |
| QNVAS | VOR unserviceable | VOR hors service |
| QNDAS | DME unserviceable | DME hors service |
| QNBAS | NDB unserviceable | NDB hors service |
| QCAAS | Air-ground communications unserviceable | Communications air-sol hors service |
| QOBCE | Obstacle erected | Obstacle érigé |
| QOLAS | Obstacle lights unserviceable | Feux d’obstacle hors service |

***

**Memory traps & examples / Pièges et exemples**

**60 ≠ 60** · Rate/gradient: 60 converts hours→minutes. 1-in-60: rounded radians→degrees. / Taux/pente : conversion heures→minutes. 1 sur 60 : radians→degrés arrondis.

**GS vs TAS** · Timing and ground gradient use GS; turn geometry uses TAS. / Temps et pente sol : vitesse sol; géométrie du virage : TAS.

**9 / 7.7** · Rolling tyre 9√psi; non-rotating 7.7√psi. Not a safe braking-speed guarantee. / Rotation 9√psi; sans rotation 7,7√psi. Pas une garantie de freinage.

**3° ≠ 3%** · 3° = about 5.24%, 318 ft/NM. / 3° = environ 5,24%, 318 pi/NM.

**DA ≠ weight** · Weight worsens performance but does not increase density altitude. / La masse dégrade les performances sans augmenter l’altitude-densité.

**True altitude** · Use height above setting source, not mountain elevation; temperature shortcut assumes column conditions. / Hauteur au-dessus de la source du calage, pas du sommet; hypothèses sur température de la colonne.

**Radio / ATC** · RCO links flight service; PAL links ATC. / RCO : service de vol; PAL : ATC.

**NOTAM** · N purpose ≠ NOTAMN new; radius ≠ diameter; E is operational detail. / N objet ≠ NOTAMN nouveau; rayon ≠ diamètre; détails en E.

**CFS S** · 1 store; 2–3 repair; 4 park; 5 tie; 6 plug; 7 drop/go. / 1 entreposer; 2–3 réparer; 4 stationner; 5 amarrer; 6 brancher; 7 déposer/repartir.

**Examples** · Training examples only; POH, published procedures and current NOTAMs govern. / Exemples pédagogiques; manuel de vol, procédures publiées et NOTAM courants prioritaires.

[TC CPAER TP12881](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881) · [NAV CANADA CNOP v12 · 14 May 2026](https://www.navcanada.ca/en/comms/_localized-assets/guides/cnop/cnop-v12-04172026.pdf) · [NAV CANADA pilot briefings](https://www.navcanada.ca/en/flight-planning/flight-planning-and-reporting.aspx) · [TSB A02C0072 · 7.7√psi](https://tsb.gc.ca/eng/rapports-reports/aviation/2002/a02c0072/a02c0072.html) · [TC radio reception approximation](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/canadian-aviation-regulations-sor-96-433/standards/standard-724-commuter-operations-helicopters-canadian-aviation-regulations-cars)

***

**Twilight · time zones · DST / Crépuscule · fuseaux · heure avancée**

| Label | English | Français |
|---|---|---|
| 4 min/degree | Earth rotates 360°/24h = 15°/h = 4 min per degree LONGITUDE. 1′ longitude = 4 seconds of time. | Rotation terrestre : 360°/24h = 15°/h = 4 min par degré de LONGITUDE. 1′ de longitude = 4 secondes de temps. |
| Twilight chart | Read date and latitude; chart gives time at the time-zone STANDARD meridian. Check chart basis first. | Lire date et latitude; le graphique donne l’heure au méridien NORMAL du fuseau. Vérifier la référence. |
| WEST + / EAST − | Relative to chart reference meridian: WEST add 4 min/degree; EAST subtract. Applies to morning AND evening twilight. | Par rapport au méridien de référence : OUEST ajouter 4 min/degré; EST soustraire. Matin ET soir. |
| Workflow / Méthode | Chart → longitude correction → local STANDARD time → +1h if DST → UTC if required. Do not correct a location-specific result twice. | Graphique → correction longitude → heure NORMALE locale → +1h si heure avancée → UTC au besoin. Ne pas corriger deux fois un résultat déjà localisé. |
| Example / Exemple | Training: chart 18:00 at 75°W; location 73°30′W = 1.5° east. Subtract 6 min →17:54 EST →18:54 EDT; both =22:54Z. | Exercice : graphique 18:00 à 75°O; lieu 73°30′O = 1,5° à l’est. −6 min →17:54 HNE →18:54 HAE; les deux =22:54Z. |
| Newfoundland / Terre-Neuve | NST UTC−3:30 (meridian 52°30′W); NDT UTC−2:30 where observed. | HNT UTC−3:30 (méridien 52°30′O); HAT UTC−2:30 si appliquée. |
| Atlantic / Atlantique | AST UTC−4 (60°W); ADT UTC−3 where observed. | HNA UTC−4 (60°O); HAA UTC−3 si appliquée. |
| Eastern / Est | EST UTC−5 (75°W); EDT UTC−4. Montréal uses EST/EDT. | HNE UTC−5 (75°O); HAE UTC−4. Montréal utilise HNE/HAE. |
| Central / Centre | CST UTC−6 (90°W); CDT UTC−5 where observed. | HNC UTC−6 (90°O); HAC UTC−5 si appliquée. |
| Mountain / Rocheuses | MST UTC−7 (105°W); MDT UTC−6 where observed. | HNR UTC−7 (105°O); HAR UTC−6 si appliquée. |
| Pacific / Pacifique | PST UTC−8 (120°W); PDT UTC−7 are conventional standard/daylight offsets. Apply the aerodrome’s published factor; local observance may differ. | HNP UTC−8 (120°O); HAP UTC−7 sont les décalages conventionnels normal/avancé. Appliquer le facteur publié de l’aérodrome; régime local variable. |
| UTC → local | Local = UTC + signed offset. 18:00Z →13:00 EST /14:00 EDT. | Locale = UTC + décalage signé. 18:00Z →13:00 HNE /14:00 HAE. |
| Local → UTC | UTC = local − signed offset. 20:30 EDT +4h =00:30Z NEXT day. | UTC = locale − décalage signé. 20:30 HAE +4h =00:30Z LENDEMAIN. |
| DST / Heure avancée | Where seasonal DST applies: +1h in spring, −1h in autumn. UTC does not change. Usual rule: second Sunday March / first Sunday November at 02:00 local. | Si changement saisonnier : +1h au printemps, −1h à l’automne. UTC ne change pas. Règle habituelle : deuxième dimanche mars / premier dimanche novembre à 02:00 locale. |
| 2026 · Montréal | Seasonal changes: 8 March / 1 November 2026. Confirm local observance rather than assigning a zone from longitude alone. | Changements saisonniers : 8 mars / 1er novembre 2026. Vérifier régime local; la longitude seule ne détermine pas le fuseau légal. |
| CFS UTC−5(4) | Normal UTC−5; daylight UTC−4. No parentheses may indicate a year-round offset; follow REF entry. | Heure normale UTC−5; avancée UTC−4. Sans parenthèses peut indiquer décalage annuel; suivre rubrique REF. |
| CFS ‡ | 10–04Z‡ →09–03Z during DST: subtract ONE hour from the listed UTC schedule. This maintains the same local clock hours. | 10–04Z‡ →09–03Z en heure avancée : soustraire UNE heure à l’horaire UTC publié. Les heures locales restent identiques. |
| CFS explicit DT | If separate DT hours are printed, use them. If no ‡ or DT schedule, do not invent a seasonal UTC shift. | Si horaire DT distinct, l’utiliser. Sans ‡ ni horaire DT, ne pas inventer un décalage saisonnier UTC. |
| Night / Nuit | Canadian night: end of evening civil twilight to beginning of morning civil twilight. Not simply sunset→sunrise. | Nuit canadienne : fin du crépuscule civil du soir au début du crépuscule civil du matin. Pas simplement coucher→lever du Soleil. |
| Exceptions | Civil time is jurisdiction-specific. Use current CFS REF and authoritative local rules; standard/daylight pairs are not a claim that every region changes clocks. | Heure civile propre à la juridiction. Utiliser REF CFS courant et règles locales; les paires normale/avancée ne signifient pas que toutes les régions changent d’heure. |

Source: CFS General 3 Sep 2026, Time Zone Factor / Times of Operation; https://nrc.canada.ca/en/research-development/products-services/software-applications/interpreting-results-sunrisesunset-calculator · additions verified 19 Oct 2026.
