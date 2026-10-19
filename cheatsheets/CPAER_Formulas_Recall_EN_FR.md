# CPAER · Formulas & quick recall / Formules et rappels

Navigation calculations reviewed 19 Oct 2026; other sections retain their source dates. / Calculs de navigation revus le 19 oct. 2026; autres rubriques selon leurs sources.

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

**ADF · VOR · DME · intercepts / Interceptions**

| Label | English | Français |
|---|---|---|
| Conventions | MH = magnetic heading; RB = clockwise relative bearing from nose; BTS/BFS = bearing TO/FROM station. Use one north reference throughout. | MH = cap magnétique; RB = gisement horaire depuis le nez; BTS/BFS = relèvement VERS/DEPUIS la station. Même référence nord pour tous les angles. |
| Wrap / Normaliser | wrap(x) = x modulo 360; add/subtract 360 until 0–359°. North may be written 000° or 360°. | wrap(x) = x modulo 360; ajouter/soustraire 360 pour obtenir 0–359°. Nord : 000° ou 360°. |
| BTS = MH + RB | BTS = wrap(MH + RB). MH 350°, RB 040° → BTS 030°. | BTS = wrap(MH + RB). MH 350°, RB 040° → BTS 030°. |
| BFS = BTS ±180 | BFS = wrap(BTS +180°). BTS 030° → BFS 210°: aircraft southwest of station. | BFS = wrap(BTS +180°). BTS 030° → BFS 210° : avion au sud-ouest de la station. |
| RB = BTS − MH | RB = wrap(BTS − MH). BTS 020°, MH 080° → RB 300° (60° left of nose). | RB = wrap(BTS − MH). BTS 020°, MH 080° → RB 300° (60° à gauche du nez). |
| MH = BTS − RB | MH = wrap(BTS − RB). BTS 100°, RB 250° → MH 210°. | MH = wrap(BTS − RB). BTS 100°, RB 250° → MH 210°. |
| ADF card / Rose | Fixed card: read RB. Movable card: set current MH under index to read magnetic BTS. RMI: correctly referenced needle head = BTS, tail = BFS. | Rose fixe : lire RB. Rose mobile : afficher MH à l’index pour lire BTS magnétique. RMI correctement référencé : pointe = BTS, queue = BFS. |
| Turn / Virage | At essentially unchanged position, right turn +30° → RB decreases 30°; left turn → RB increases. BTS stays nearly unchanged. | À position pratiquement constante, virage droite +30° → RB diminue de 30°; gauche → RB augmente. BTS reste presque constant. |
| Homing ≠ tracking | RB 000° points the nose at the station. In crosswind, holding RB 000° gives a curved homing path. Tracking needs wind correction. | RB 000° pointe le nez vers la station. Par vent traversier, maintenir RB 000° produit une trajectoire courbe. Suivre une route exige une correction de dérive. |
| VOR radial | Radial = bearing FROM station. On R-090: outbound course 090°; inbound course 270°. Identify aid and north reference (true-reference exceptions exist in Canada). | Radiale = relèvement DEPUIS station. Sur R-090 : route éloignement 090°; rapprochement 270°. Identifier aide et référence nord (exceptions au nord vrai au Canada). |
| TO / FROM | With CDI centred: selected course toward station → TO; reciprocal → FROM. Flag describes selected-course geometry, not aircraft heading or actual travel. | CDI centré : route sélectionnée vers station → TO; réciproque → FROM. Le drapeau décrit la géométrie sélectionnée, pas le cap ni le déplacement réel. |
| 30° intercept setup | C = desired direction of travel, NOT always radial. Choose H = C ±30° toward the course line. Sketch station, current BFS and target line first; heading alone cannot select the side. No-wind examples below. | C = route désirée, PAS toujours radiale. Choisir H = C ±30° vers la ligne. Dessiner station, BFS actuel et ligne cible; le cap seul ne donne pas le côté. Exemples sans vent ci-dessous. |
| Capture: inbound | At capture BTS = C; RB = wrap(C − H). H=C+30 → RB330; H=C−30 → RB030. Start rollout with appropriate lead. | À l’interception BTS = C; RB = wrap(C − H). H=C+30 → RB330; H=C−30 → RB030. Anticiper la sortie du virage. |
| Capture: outbound | At capture BTS = wrap(C+180); RB = wrap(C+180−H). H=C+30 → RB150; H=C−30 → RB210. | À l’interception BTS = wrap(C+180); RB = wrap(C+180−H). H=C+30 → RB150; H=C−30 → RB210. |
| Inbound example | Aircraft west-northwest of NDB (BFS285), intercept C090 inbound: H120 toward line. At capture BTS090, RB330. Turn left toward 090, then correct wind. | Avion au ouest-nord-ouest du NDB (BFS285), intercepter C090 en rapprochement : H120 vers ligne. À l’interception BTS090, RB330. Virer gauche vers 090, puis corriger le vent. |
| Outbound example | Aircraft northeast (BFS045), intercept C090 outbound: H120. At capture BFS090, BTS270, RB150. Turn left toward 090, then correct wind. | Avion au nord-est (BFS045), intercepter C090 en éloignement : H120. À l’interception BFS090, BTS270, RB150. Virer gauche vers 090, puis corriger le vent. |
| Wind trap / Vent | 30° is a chosen training intercept, not a universal rule. Wind changes the ground intercept angle. Always compute capture RB from actual heading; after capture fly the wind-corrected heading. | 30° est un choix pédagogique, pas une règle universelle. Le vent modifie l’angle au sol. Calculer RB à partir du cap réel; après interception appliquer la correction de dérive. |
| Cross-track distance | Lateral offset = ground range × sin(angular error); small angle ≈ range × error°/60. At 30 NM, 4° → about 2 NM. | Écart latéral = distance horizontale × sin(erreur angulaire); petit angle ≈ distance × erreur°/60. À 30 NM, 4° → environ 2 NM. |
| VOR dots | Conventional VOR CDI: normally 2° per dot, ±10° full scale. Two dots at 30 NM ≈ 2 NM. LOC and GNSS scales differ; check equipment/mode. | CDI VOR classique : normalement 2° par point, ±10° pleine échelle. Deux points à 30 NM ≈ 2 NM. Échelles LOC/GNSS différentes; vérifier équipement/mode. |
| DME geometry | Slant NM = √(ground NM² + height NM²); height NM = height above station(ft)/6076. Over station at 6076 ft above it → about 1 DME, not zero. | Distance oblique NM = √(distance horizontale NM² + hauteur NM²); hauteur NM = pieds au-dessus station/6076. À la verticale à 6076 ft au-dessus → environ 1 DME, pas zéro. |
| DME ground range | Ground NM = √(DME² − height NM²). DME 5 NM, height 6076 ft → √24 ≈4.90 NM. DME speed/time meaningful toward/away from station; unreliable for along-track speed on an arc. | Distance horizontale NM = √(DME² − hauteur NM²). DME 5 NM, hauteur 6076 ft → √24 ≈4,90 NM. Vitesse/temps DME pertinents vers/depuis station; pas la vitesse le long d’un arc. |
| 30° closing time | For a 30° GROUND-track intercept: closing speed = GS × sin30 = GS/2. Time(min)=120 × lateral NM/GS. 2 NM off at 120 kt → 2 min. Wind-correct heading to obtain that ground track. | Interception à 30° de ROUTE SOL : vitesse de rapprochement = GS/2. Temps(min)=120 × écart NM/GS. Écart 2 NM à 120 kt → 2 min. Corriger le cap pour obtenir cette route sol. |
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
| Units / Unités | Distance in NM × fraction = ETE in MINUTES; use groundspeed, including wind. | Distance en NM × fraction = ETE en MINUTES; utiliser la vitesse sol, vent compris. |
| 60 kt | ETE = distance × 1 → same number; 30 NM = 30 min | ETE = distance × 1 → même nombre; 30 NM = 30 min |
| 75 kt | ETE = distance × ⅘ → ÷5 then ×4; 30 NM = 24 min | ETE = distance × ⅘ → ÷5 puis ×4; 30 NM = 24 min |
| 90 kt | ETE = distance × ⅔ → ÷3 then ×2; 30 NM = 20 min | ETE = distance × ⅔ → ÷3 puis ×2; 30 NM = 20 min |
| 100 kt | ETE = distance × ⅗ → ÷5 then ×3; 30 NM = 18 min | ETE = distance × ⅗ → ÷5 puis ×3; 30 NM = 18 min |
| 120 kt | ETE = distance × ½ → ÷2; 30 NM = 15 min | ETE = distance × ½ → ÷2; 30 NM = 15 min |
| 150 kt | ETE = distance × ⅖ → ÷5 then ×2; 30 NM = 12 min | ETE = distance × ⅖ → ÷5 puis ×2; 30 NM = 12 min |
| 180 kt | ETE = distance × ⅓ → ÷3; 30 NM = 10 min | ETE = distance × ⅓ → ÷3; 30 NM = 10 min |
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

**ADF pebble / Repère** · HEAD + RELATIVE = TO; TO ±180 = FROM. Inbound capture: 330/030; outbound: 150/210 for H=C+30/C−30, no wind. / CAP + GISEMENT = VERS; VERS ±180 = DEPUIS. Interception sans vent : rapprochement 330/030; éloignement 150/210 pour H=C+30/C−30.

[TC CPAER TP12881](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881) · [NAV CANADA CNOP v12 · 14 May 2026](https://www.navcanada.ca/en/comms/_localized-assets/guides/cnop/cnop-v12-04172026.pdf) · [NAV CANADA pilot briefings](https://www.navcanada.ca/en/flight-planning/flight-planning-and-reporting.aspx) · [TSB A02C0072 · 7.7√psi](https://tsb.gc.ca/eng/rapports-reports/aviation/2002/a02c0072/a02c0072.html) · [TC radio reception approximation](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/canadian-aviation-regulations-sor-96-433/standards/standard-724-commuter-operations-helicopters-canadian-aviation-regulations-cars) · [NRC twilight; time section checked 19 Oct 2026](https://nrc.canada.ca/en/research-development/products-services/software-applications/interpreting-results-sunrisesunset-calculator) · [TC TP 975, Exercise 24; navigation review 19 Oct 2026](https://tc.canada.ca/en/aviation/publications/flight-instructor-guide-aeroplane-tp-975) · [FAA Instrument Flying Handbook, Ch. 9 (2012), navigation geometry](https://www.faa.gov/sites/faa.gov/files/pilots/FAA-H-8083-15B.pdf)
