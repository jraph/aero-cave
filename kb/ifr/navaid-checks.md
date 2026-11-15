# Radio navigation (VOR / ADF / DME / ILS) / Radionavigation (VOR / ADF / DME / ILS)
<!-- concept: nav-radio | level: IR -->

[IFR index / Index IFR](README.md) · concept `nav-radio` · sources, legend and release status in the index. Unit IDs are stable: never rename one.

***
#### Navigation aid checks
<!-- id: ifr-navigation-aid-checks | from: 10 -->

- VOR: identify Morse/voice, correct frequency/course/TO-FROM, service volume and NOTAM.

##### VOR receiver checks — 4–6–4

| Check | Maximum acceptable error / difference |
|---|---|
| VOT / designated ground checkpoint | **±4°** from the reference indication (FAA AIM reference; see Canadian scope below) |
| Airborne landmark / published-radial check | **±6°** from the published radial |
| Dual independent VOR receivers, same station | **4° total difference** between indicated bearings |

- `M:` **4 ground — 6 airborne — 4 between receivers.**
- `P VOT:` with CDI centred, reference indication is **000° FROM** or **180° TO**; apply ±4°. A designated ground checkpoint uses its published radial instead.
- `T dual:` NAV1 030° / NAV2 034° = at the limit; 030° / 035° = exceeds tolerance. This is **4° between receivers**, not ±4° each. Compare using the same TO/FROM sense.
- `T airborne:` ±6° is a **receiver-check tolerance**, not permission to track 6° off course.
- **Canadian scope:** TC AIM 2026-1 COM 4.5.1–4.5.2 specifies the dual comparison and airborne check: difference greater than 4° requires investigation/correction before IFR use; airborne error greater than 6° means the equipment should not be used for IFR navigation. The ground/VOT ±4° and VOT indications above are explicitly sourced to the FAA AIM; do not infer U.S. checking intervals or recordkeeping requirements for Canada.
- **Sources:** [TC AIM 2026-1, COM 4.5.1–4.5.2](https://tc.canada.ca/en/aviation/publications/transport-canada-aeronautical-information-manual-tc-aim-tp-14371); [FAA AIM 1-1-4, VOR Receiver Check](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap1_section_1.html). Reviewed 2026-10-19.


- ILS: identify LOC; set front course; GS alive from below; marker/DME/fixes per plate.
- NDB: identify; station passage/needle swing; ADF errors near TS/coast/night/mountain.
- GNSS: current DB, RAIM/WAAS, correct mode, CDI scaling, annunciations.
- `T:` failed identification = unusable navaid for approach.
***
#### Navigation aids — ADF / VOR / DME / intercepts
<!-- id: nav-navigation-aids-adf-vor-dme-intercepts | from: 06 | kind: formula | level: CPL IR -->

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
- `M VOR checks:` **4–6–4** = ground/VOT ±4° (FAA reference), airborne ±6°, dual receivers ≤4° total difference. Receiver accuracy ≠ tracking allowance. See [VOR receiver checks and Canadian source scope](navaid-checks.md#navigation-aid-checks).
***
#### ILS and VORTAC principles — AIM COM 4
<!-- id: nav-ils-vortac-principles-com-4 | level: IR -->

- ILS = localizer (course) + glide path + FAF fix (NDB or DME/RNAV). [COM 4.10]
- LOC 108.1–111.9 MHz; reliable 18 NM within 10°, 10 NM within 35°. False courses 6–35° off: don't couple until within 6°. [COM 4.10.1, 4.10.7]
- GP 329.3–335 MHz, paired with LOC; ~3°, beam 1.4°. False GP at 2× and 3× angle: check altitude at FAF. [COM 4.10.2, 4.10.7]
- VOR: 360 radials, Morse ID. VORTAC: civil users get VOR azimuth + TACAN DME; TACAN azimuth not for civil. [COM 4.5, 4.9]
- DME = slant range; ±0.5 NM or 3 %. [COM 4.7]
- `T:` intercept GP from below; above = risk of false GP.
***
#### Nav displays — RMI, HSI, flight director, radio altimeter
<!-- id: nav-rmi-hsi-fd-radio-altimeter | also: agk-inst | level: IR -->

- **RMI**: slaved heading card + bearing pointer. Head = magnetic bearing **to** station, tail = reciprocal (from). Read directly: no RB + heading sum (that is fixed-card ADF). [TP 2076 2.2.6]
- **HSI**: rotating heading card, bearing pointer, aircraft symbol with track (deviation) bar, TO/FROM in one view. Dots: VOR ~5° / 10°, ILS ~1¼° / 2½°. [TP 2076 2.1.5 C]
- **Flight director**: FDI command bars = computed pitch/bank to fly selected mode (HDG, VOR/LOC, APP, G/S, GA, ALT). Computer takes nav receivers, attitude gyro, radar altimeter, compass, air data. `T:` FD shows what to do, not where you are: cross-check raw data. [TP 2076 2.1.5 A–D]
- **Radio (radar) altimeter**: absolute height by timed radio echo; less accurate over ice, deep snow, rapidly changing terrain. CAT II DH based on radio altimeter. `T:` height AGL ≠ altitude ASL. [TP 2076 2.1.2 F.3; CAP GEN CAT II/III chart legend]
- `?:` HSI back course: set front (inbound) course → normal sensing; not in TP 2076, check aircraft AFM/avionics guide.
***
#### Pebble
<!-- id: ifr-navaid-checks-pebble -->

- VOR CHECK `4 ground — 6 airborne — 4 between receivers | VOT: 000° FROM or 180° TO, ±4° (FAA AIM source) | airborne ±6° from published radial | dual: 4° TOTAL difference, same TO/FROM sense | Canada (TC AIM COM 4.5.1–4.5.2): dual >4° or airborne >6° → not for IFR until corrected`
- T `±6° = receiver-check tolerance ≠ permission to track off course | failed identification = unusable navaid for approach | do not infer U.S. intervals/recordkeeping for Canada`
- ILS/DME `LOC 108.1–111.9 · GP 329.3–335, 3°, false GP at 2× and 3× | couple within 6° | DME slant ±0.5 NM or 3 % | RMI head = TO`
***
