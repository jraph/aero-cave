# CPAER · Formulas & quick recall / Formules et rappels

[Open CAVE reader](https://jraph.github.io/aero-cave/readers/CPAER_Formulas_Recall_EN_FR.html) · [All study cards](../README.md)

Navigation and operational additions reviewed 19 Oct 2026; source editions and scope in review record. / Ajouts navigation et exploitation revus le 19 oct. 2026; éditions et portée dans le compte rendu.

***

## Time · fuel / Temps · carburant

| Label | English | Français |
|---|---|---|
| Distance | D(NM) = GS(kt) × t(h) | D(NM) = vitesse sol(kt) × durée(h) |
| Time / Durée | t(min) = 60D/GS | t(min) = 60D/vitesse sol |
| GS / Vitesse sol | GS(kt) = 60D/t(min) | Vitesse sol(kt) = 60D/t(min) |
| Fuel / Carburant | Fuel = hourly flow × hours; endurance = usable fuel/flow | Carburant = débit horaire × heures; autonomie = carburant utilisable/débit |
| Specific range | GS/fuel flow = NM per fuel unit | Vitesse sol/débit = NM par unité de carburant |
***

## Wind · navigation / Vent · navigation

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

## ADF · VOR · DME · intercepts / Interceptions

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

## Weight · balance / Masse · centrage

| Label | English | Français |
|---|---|---|
| Moment | Moment = weight × arm | Moment = masse × bras de levier |
| CG | CG = total moment/total weight | CG = somme des moments/masse totale |
| Shift / Déplacement | ΔCG = moved weight × distance moved/total weight | ΔCG = masse déplacée × déplacement/masse totale |
| Required weight | w = total weight × ΔCG/distance moved | w = masse totale × ΔCG/déplacement |
| Add / remove | CGnew = (W × CGold ± w × arm)/(W ± w) | CGnouveau = (W × CGancien ± w × bras)/(W ± w) |
| % MAC / CMA | 100(CG − LEMAC)/MAC; common datum and units | 100(CG − bord d’attaque CMA)/CMA; même référence et unités |
***

## Altitude · weather / Altitude · météo

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
| Cloud base · exam | Convective base AGL ft ≈ 1000(T − Td)/3; **simplified classroom shortcut** assuming Td approximately constant | Base convective AGL pi ≈ 1000(T − Td)/3; **raccourci de cours** avec Td supposé presque constant |
| Cloud base · parcel | Convective LCL AGL ft ≈ 1000(T − Td)/(3 − 0.5); rising unsaturated parcel cools 3°C/1000 ft, dew point falls 0.5°C/1000 ft → spread closes 2.5°C/1000 ft | NCL convectif AGL pi ≈ 1000(T − Td)/(3 − 0,5); la parcelle non saturée refroidit de 3°C/1000 pi, le point de rosée baisse de 0,5°C/1000 pi → écart réduit de 2,5°C/1000 pi |
| Freezing · exam | Parcel 0°C height AGL ≈ CB(exam) + 1000 Td/1.5; assumes T at cloud base ≈ surface Td, saturated lapse ≈ 1.5°C/1000 ft | Hauteur AGL de 0°C dans la parcelle ≈ base(examen) + 1000 Td/1,5; T à la base ≈ Td de surface, gradient saturé ≈ 1,5°C/1000 pi |
| Freezing · parcel | T_CB ≈ T − 3 CB(parcel)/1000; parcel 0°C height AGL ≈ CB(parcel) + 1000 T_CB/1.5 (if T_CB > 0°C); saturated lapse variable | T_base ≈ T − 3 base(parcelle)/1000; hauteur AGL de 0°C ≈ base(parcelle) + 1000 T_base/1,5 (si T_base > 0°C); gradient saturé variable |
| Freezing · actual | Parcel 0°C height ≠ atmospheric freezing level; environmental vertical temperature profile / GFA / winds-temp aloft wins. ASL = AGL + field elevation (same datum) | Hauteur de 0°C de la parcelle ≠ niveau de congélation réel; privilégier profil thermique ambiant / GFA / vents-températures en altitude. ASL = AGL + altitude du terrain (même référence) |
***

## Stall · airspeed / Décrochage · vitesse

| Label | English | Français |
|---|---|---|
| Load / Charge | n = 1/cos(bank): coordinated LEVEL turn only | n = 1/cos(inclinaison) : virage coordonné EN PALIER uniquement |
| Stall / Décrochage | Vs loaded = Vs × √n; Vs₂ = Vs₁√(W₂/W₁) | Vs sous charge = Vs × √n; Vs₂ = Vs₁√(W₂/W₁) |
| VS / VS1 / VS0 | VS = generic stall speed; VS1 = specified configuration (often clean); VS0 = landing config. VS and VS1 can refer to the same clean speed; not VS0. | VS = vitesse de décrochage générique; VS1 = configuration spécifiée (souvent lisse); VS0 = configuration d'atterrissage. VS et VS1 peuvent désigner la même vitesse en configuration lisse; pas VS0. |
| VA · theoretical / théorique | VA_est = VS(clean)√n_limit; legacy Normal +3.8g → ≈1.95 VS1 (quick 1.9–2.0×); VS1=50 KIAS → ≈97.5 KIAS. Positive stall/limit-load intersection, not necessarily certified VA. | VA_est = VS(lisse)√n_limite; Normal ancien +3,8g → ≈1,95 VS1 (repère 1,9–2,0×); VS1=50 KIAS → ≈97,5 KIAS. Intersection décrochage/charge limite positive, pas nécessairement la VA certifiée. |
| VA · weight / masse | VA₂ ≈ VA₁√(W₂/W₁) for same configuration/load-factor basis; lighter → lower VA. Published POH/AFM and weight schedule govern; VA does not protect against every abrupt/multiple input or gust. | VA₂ ≈ VA₁√(W₂/W₁), à configuration et facteur de charge comparables; masse moindre → VA moindre. POH/AFM et valeurs selon la masse prévalent; VA ne protège pas contre toute action brusque/combinée ni toute rafale. |
| VREF definition / Définition | Landing reference speed: the published POH/AFM speed to be maintained to 50 ft in the specified landing configuration. Use the published value; certification bases differ. | Vitesse de référence à l’atterrissage : vitesse publiée au POH/AFM à maintenir jusqu’à 50 pi dans la configuration d’atterrissage précisée. Utiliser la valeur publiée; les bases de certification diffèrent. |
| VREF fallback / Calcul | If VREF is not specified: 1.3 × VSO. Example: VSO 50 KIAS → VREF 65 KIAS. For approach category, use VSO at maximum certificated landing weight. | Si VREF n’est pas précisée : 1,3 × VSO. Exemple : VSO 50 KIAS → VREF 65 KIAS. Pour la catégorie d’approche, utiliser VSO à la masse maximale certifiée à l’atterrissage. |
| Weight / Masse | Same configuration/basis only: VREF₂ ≈ VREF₁√(W₂/W₁). POH/AFM landing-weight data takes precedence. Wind/gust additive changes the approach target, not VREF. | Même configuration et même base seulement : VREF₂ ≈ VREF₁√(W₂/W₁). Les données POH/AFM selon la masse ont priorité. La correction vent/rafale modifie la cible d’approche, pas VREF. |
| Lift / Portance | L = ½ρV²SCL; dynamic pressure q = ½ρV² | L = ½ρV²SCL; pression dynamique q = ½ρV² |
| TAS | TAS = EAS√(ρ₀/ρ) | Vitesse vraie = vitesse équivalente × √(ρ₀/ρ) |
| TAS shortcut | ≈ CAS[1 + 0.02(PA/1000)]; rough; E6B for actual temperature | ≈ CAS[1 + 0,02(AP/1000)]; approximatif; E6B pour température réelle |
| 30° / 45° / 60° | n: 1.15 / 1.41 / 2; Vs factors: 1.07 / 1.19 / 1.41 | n : 1,15 / 1,41 / 2; facteurs Vs : 1,07 / 1,19 / 1,41 |
***

## Climb · descent / Montée · descente

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

## Turns / Virages

| Label | English | Français |
|---|---|---|
| Standard rate | 3°/s; 90°=30s; 180°=60s; 360°=120s | 3°/s; 90°=30s; 180°=60s; 360°=120s |
| Rate / Taux | °/s ≈ 1091 tan(bank)/TAS(kt) | °/s ≈ 1091 tan(inclinaison)/TAS(kt) |
| Radius / Rayon | ft ≈ TAS²/[11.26 tan(bank)] | pi ≈ TAS²/[11,26 tan(inclinaison)] |
| Standard bank | bank = atan(3TAS/1091); 100kt≈15°; 150kt≈22° | inclinaison = atan(3TAS/1091); 100kt≈15°; 150kt≈22° |
| Double speed | Same bank: half turn rate, FOUR times radius | Même inclinaison : taux divisé par deux, rayon QUADRUPLÉ |
| Assumptions | Coordinated level turn; TAS; air-relative geometry; wind alters ground track | Virage coordonné en palier; TAS; géométrie dans l’air; vent modifie trajectoire sol |
***

## Radio · runway / Radio · piste

| Label | English | Français |
|---|---|---|
| VHF range | NM ≈ 1.23(√h₁ + √h₂); 1.25 also used; feet above surface | NM ≈ 1,23(√h₁ + √h₂); 1,25 également; hauteurs en pi au-dessus de la surface |
| Rotating tyre | Dynamic hydroplaning kt ≈ 9√pressure(psi); 36psi→54kt | Pneu en rotation : aquaplanage dynamique kt ≈ 9√pression(psi); 36psi→54kt |
| Non-rotating tyre | kt ≈ 7.7√pressure(psi); 36psi→46.2kt | Pneu sans rotation : kt ≈ 7,7√pression(psi); 36psi→46,2kt |
| FISE frequencies | 123.275 / 123.375 / 123.475 / 123.550 MHz; use local published RCO | 123,275 / 123,375 / 123,475 / 123,550 MHz; utiliser RCO publié |
| 126.7 | Generally not monitored by FIC at dedicated FISE RCOs; broadcasts may occur | Généralement non veillée par FIC aux RCO FISE dédiés; diffusions possibles |
***

## Conversions

| Label | English | Français |
|---|---|---|
| NM | 1 NM = 1.852km = 6076ft = 1.151 statute mi | 1 NM = 1,852km = 6076pi = 1,151 mille terrestre |
| Gallon | US 3.785L; Imperial 4.546L | US 3,785L; impérial 4,546L |
| Mass / length | 1kg = 2.205lb; 1m = 3.281ft | 1kg = 2,205lb; 1m = 3,281pi |
| Earth / Terre | 15° longitude/hour; 4min/degree; 1′ latitude ≈ 1NM | 15° longitude/heure; 4min/degré; 1′ latitude ≈ 1NM |
***

## Timing shortcuts / Estimation du temps

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

## CFS servicing · public facilities / Services · installations publiques CFS

| Label | English | Français |
|---|---|---|
| 1 | Storage available | Entreposage disponible |
| 2 | Servicing / minor repairs | Entretien / réparations mineures |
| 3 | Major repairs | Réparations majeures |
| 4 | Extended-term parking | Stationnement prolongé |
| 5 | Tie-down facilities | Dispositifs d’amarrage |
| 6 | Plug-in facilities | Prises de branchement |
| 7 | Pick-up/drop-off only; no extended parking | Embarquement/débarquement seulement; aucun stationnement prolongé |
| PF location / Lieu | `PF` = public facilities. `A` terminal; `B` on aerodrome; `C` within 5 NM; `D` within 30 NM. | `PF` = installations publiques. `A` aérogare; `B` sur l’aérodrome; `C` à moins de 5 NM; `D` à moins de 30 NM. |
| PF 1–4 | `1` phone; `2` food; `3` taxi; `4` medical. | `1` téléphone; `2` restauration; `3` taxi; `4` services médicaux. |
| PF 5–8 | `5` hotel; `6` car rental; `7` public Wi-Fi; `8` public Internet access. | `5` hôtel; `6` location auto; `7` Wi-Fi public; `8` accès Internet public. |
| PF example / Exemple | `PF A-1,2 B-5` = phone and food in terminal; hotel on aerodrome. `S 5` means tie-down, but `PF 5` means hotel. | `PF A-1,2 B-5` = téléphone et restauration dans l’aérogare; hôtel sur l’aérodrome. `S 5` signifie arrimage, mais `PF 5` signifie hôtel. |
***

## Communications · weather / Communications · météo

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

## FIR · FIC

| Label | English | Français |
|---|---|---|
| 7 FIR | Vancouver, Edmonton, Winnipeg, Toronto, Montréal, Moncton, Gander | Vancouver, Edmonton, Winnipeg, Toronto, Montréal, Moncton, Gander |
| 4 briefing FIC | Kamloops, Edmonton, London, Québec | Kamloops, Edmonton, London, Québec |
| Whitehorse | FIC for flight-plan processing/alerting; Kamloops provides telephone pilot briefings | FIC pour traitement plans de vol/alerte; Kamloops assure exposés téléphoniques |
| Five areas | Course shorthand: Pacific, Edmonton, Ontario, Québec, Atlantic; London serves Ontario + Atlantic. These are not the seven FIRs. | Raccourci pédagogique : Pacifique, Edmonton, Ontario, Québec, Atlantique; London dessert Ontario + Atlantique. Ce ne sont pas les sept FIR. |
***

## NOTAM · header & Q-line / En-tête et ligne Q

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

## Common NOTAM codes / Codes NOTAM courants

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

## Twilight · time zones · DST / Crépuscule · fuseaux · heure avancée

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

## Oxygen / Oxygène — CAR 605.31–32

| Label | English | Français |
|---|---|---|
| 10–13 / 30 | Cabin-pressure altitude >10,000 to ≤13,000 ft: crew USE oxygen after 30 min. | Altitude-pression cabine >10 000 à ≤13 000 ft : équipage UTILISE oxygène après 30 min. |
| Supply / Réserve | Unpressurized: supply for ALL crew +10% passengers (at least 1 passenger), for time beyond 30 min in that band. | Non pressurisé : réserve pour TOUT équipage +10 % passagers (au moins 1 passager), pour durée au-delà de 30 min dans cette tranche. |
| Above / Au-dessus 13,000 | All aboard USE oxygen throughout. Unpressurized supply: all aboard, entire time; air transport service minimum 1 hour. | TOUS utilisent oxygène tout le temps. Réserve non pressurisé : tous, durée entière; service de transport aérien : minimum 1 h. |
| Boundaries / Seuils | Exactly 13,000 ft remains in the 30-min band. At 13,100 ft, no 30-min grace. Cabin pressure altitude, not height AGL. | Exactement 13 000 ft reste dans tranche 30 min. À 13 100 ft, aucun délai. Altitude-pression cabine, pas hauteur AGL. |
| Pressurized / Pressurisé | Size emergency supply for worst-point decompression, descent profile and suitable landing aerodrome: use 605.31(2) table and notes; do not reuse unpressurized quantities. | Réserve d’urgence selon dépressurisation au point critique, profil de descente et aérodrome convenable : tableau et notes 605.31(2); quantités différentes du non pressurisé. |
| Pilot mask / Masque | Pilot at controls: mask required at/above FL250 without quick-donning masks; above FL410 with quick-donning masks. | Pilote aux commandes : masque à FL250 ou plus sans masque à pose rapide; au-dessus FL410 avec masque à pose rapide. |
***

## Passenger weights / Masse des passagers — AIM 2026-1 RAC 3.4.7

| Label | English | Français |
|---|---|---|
| Scope / Portée | Standard averages require the applicable approved W&B method. 703 uses actual/volunteered/estimated or approved segmented/survey methods; do not apply airline averages to a small private aircraft. | Moyennes standard selon méthode masse/centrage approuvée applicable. En 703 : masses réelles/déclarées/estimées ou segmentées/enquête approuvées; pas de moyennes compagnie pour petit avion privé. |
| Adult M / X ≥12 | Summer 206 lb (93.4 kg); winter 212 lb (96.2 kg). | Été 206 lb (93,4 kg); hiver 212 lb (96,2 kg). |
| Adult F ≥12 | Summer 172 lb (78.1 kg); winter 178 lb (80.7 kg). Adult winter increment =6 lb. | Été 172 lb (78,1 kg); hiver 178 lb (80,7 kg). Supplément adulte hiver =6 lb. |
| Children / Enfants | Age 2–11: 75 lb (34 kg), both seasons. Infant <2: 30 lb (13.6 kg); standard-method infant allowance note applies when infant count exceeds 10% of adults. | 2–11 ans : 75 lb (34 kg), deux saisons. Bébé <2 : 30 lb (13,6 kg); note de la méthode standard si nombre de bébés dépasse 10 % des adultes. |
| Baggage / Bagages | Standard adult weights include clothing/carry-on. No carry-on: permitted reduction 13 lb (5.9 kg). Checked baggage and cargo: actual weights. | Masses standard adultes incluent vêtements/bagage cabine. Sans bagage cabine : réduction permise 13 lb (5,9 kg). Bagages enregistrés/fret : masses réelles. |
| Small sample / Petit groupe | 1–4 maximum certificated passenger seats: actual, volunteered or estimated weights. Segmented weights depend on certificated capacity, not passengers aboard. | 1–4 sièges passagers max certifiés : masses réelles, déclarées ou estimées. Masses segmentées selon capacité certifiée, pas nombre à bord. |
| Segment 5 | 5 certificated passenger seats: summer M/X 243, F 204 lb; winter M/X 249, F 210 lb. | 5 sièges passagers certifiés : été M/X 243, F 204 lb; hiver M/X 249, F 210 lb. |
| Segment 6–8 | 6–8 certificated passenger seats: summer M/X 238, F 200 lb; winter M/X 244, F 206 lb. | 6–8 sièges passagers certifiés : été M/X 238, F 200 lb; hiver M/X 244, F 206 lb. |
| Segment 9–11 | 9–11 certificated passenger seats: summer M/X 230, F 193 lb; winter M/X 236, F 199 lb. | 9–11 sièges passagers certifiés : été M/X 230, F 193 lb; hiver M/X 236, F 199 lb. |
| Segment 12–16 | 12–16 certificated passenger seats: summer M/X 227, F 190 lb; winter M/X 233, F 196 lb. | 12–16 sièges passagers certifiés : été M/X 227, F 190 lb; hiver M/X 233, F 196 lb. |
| Segment 17–25 | 17–25 certificated passenger seats: summer M/X 223, F 187 lb; winter M/X 229, F 193 lb. | 17–25 sièges passagers certifiés : été M/X 223, F 187 lb; hiver M/X 229, F 193 lb. |
| Actual wins / Réel | If a group is heavier than the assumed average, account for actual weights. Never hide infant, baggage or unusual load in a blanket average. | Si groupe plus lourd que moyenne supposée, tenir compte des masses réelles. Ne pas masquer bébé, bagages ou charge inhabituelle dans moyenne générale. |
***

## Flight time · FDT · FDP / Temps de vol · service

| Label | English | Français |
|---|---|---|
| Terms / Termes | FDT = flight/duty time (general shorthand). FDP = flight duty period; flight time, FDP, work and rest are separate clocks. FPD = freezing-point depressant (fluid). | FDT = abréviation générale temps vol/service. FDP = période de service de vol; vol, service, travail et repos : compteurs distincts. FPD = abaisseur du point de congélation (liquide). |
| Applicability / Portée | 700 Division III: applicable commercial operations. 604 private operators have separate limits; ordinary private PPL/CPL flying is not automatically 604. 702 aerial work and 700 Division IV medevac differ. | 700 division III : opérations commerciales applicables. Exploitants privés 604 : limites distinctes; vol privé ordinaire PPL/CPL pas automatiquement 604. Travail aérien 702 et évacuation médicale division IV : règles distinctes. |
| 700.27 flight time | 112 h/28 days; 300 h/90 days; 1000 h/365 days. Single-pilot: 8 h/24 consecutive hours. | 112 h/28 jours; 300 h/90 jours; 1000 h/365 jours. Monopilote : 8 h/24 heures consécutives. |
| 604.98 flight time | 120 h/30 days; 300 h/90 days; 1200 h/12 consecutive months. Single-pilot IFR: 8 h/24 h. | 120 h/30 jours; 300 h/90 jours; 1200 h/12 mois consécutifs. IFR monopilote : 8 h/24 h. |
| FDP table key | 700.28: select average scheduled flight duration, number of flights, and applicable start-time reference. No universal 14-hour limit. Tables below are baseline, before special adjustments. | 700.28 : choisir durée moyenne des vols prévus, nombre de vols et référence horaire applicable. Pas de limite universelle 14 h. Tableaux de base avant adaptations particulières. |
| Columns A / B / C | Average <30 min: A=1–11 flights, B=12–17, C=18+. Average 30–<50: A=1–7, B=8–11, C=12+. Average ≥50: A=1–4, B=5–6, C=7+. | Moyenne <30 min : A=1–11 vols, B=12–17, C=18+. Moyenne 30–<50 : A=1–7, B=8–11, C=12+. Moyenne ≥50 : A=1–4, B=5–6, C=7+. |
| 00:00–03:59 | FDP maximum A / B / C = 9 / 9 / 9 hours. | FDP maximum A / B / C = 9 / 9 / 9 heures. |
| 04:00–04:59 | FDP maximum A / B / C = 10 / 9 / 9 hours. | FDP maximum A / B / C = 10 / 9 / 9 heures. |
| 05:00–05:59 | FDP maximum A / B / C = 11 / 10 / 9 hours. | FDP maximum A / B / C = 11 / 10 / 9 heures. |
| 06:00–06:59 | FDP maximum A / B / C = 12 / 11 / 10 hours. | FDP maximum A / B / C = 12 / 11 / 10 heures. |
| 07:00–12:59 | FDP maximum A / B / C = 13 / 12 / 11 hours. | FDP maximum A / B / C = 13 / 12 / 11 heures. |
| 13:00–16:59 | FDP maximum A / B / C = 12.5 / 11.5 / 10.5 hours. | FDP maximum A / B / C = 12.5 / 11.5 / 10.5 heures. |
| 17:00–21:59 | FDP maximum A / B / C = 12 / 11 / 10 hours. | FDP maximum A / B / C = 12 / 11 / 10 heures. |
| 22:00–22:59 | FDP maximum A / B / C = 11 / 10 / 9 hours. | FDP maximum A / B / C = 11 / 10 / 9 heures. |
| 23:00–23:59 | FDP maximum A / B / C = 10 / 9 / 9 hours. | FDP maximum A / B / C = 10 / 9 / 9 heures. |
| Day VFR / VFR jour | All flights day VFR: 700.28(9) uses column A values irrespective of flight count. Positioning is not a flight for table count. | Tous vols VFR jour : 700.28(9) utilise valeurs colonne A indépendamment du nombre de vols. Mise en place non comptée comme vol dans tableau. |
| Example / Exemple | Start 08:00, five 60-min flights → column B →12 h FDP (baseline). All day VFR →13 h. Flight time is 5 h, not 12 h. | Début 08:00, cinq vols de 60 min → colonne B →12 h FDP de base. Tous VFR jour →13 h. Temps de vol =5 h, pas 12 h. |
| Work / Travail 700.29 | 60 h/7 d or qualifying 70 h/7 d option; 192 h/28 d; 2200 h/365 d. Each option has its own time-off conditions. | 60 h/7 j ou option admissible 70 h/7 j; 192 h/28 j; 2200 h/365 j. Conditions de congé propres à chaque option. |
| Rest / Repos 700.40 | Home: 12 h OR 11 h + travel to/from rest OR 10 h in operator-provided suitable accommodation. Away: 10 h in suitable accommodation. Special schedules may require more. | Base : 12 h OU 11 h + trajets aller-retour repos OU 10 h en hébergement convenable fourni. Hors base : 10 h en hébergement convenable. Horaires particuliers : repos supplémentaire possible. |
| Fatigue trap | Being under a numeric limit does not establish fitness. Acclimatization, reserve/standby, split duty, extensions and augmented crews require their specific rules. | Respecter limite numérique ne prouve pas aptitude. Acclimatation, réserve/attente, service fractionné, prolongations et équipage renforcé : règles spécifiques. |
| 604 FDP base | 604.99: 14 h/24 h; 15 h only if preceding 30 d total FDP ≤70 h OR preceding REST ≥24 h. | 604.99 : 14 h/24 h ; 15 h si FDP total des 30 j précédents ≤70 h OU repos précédent ≥24 h. |
| 604 split 604.100 | Break ≥4 consecutive h in suitable accommodation + notice before first FLT/standby → FDP extension MIN(½ break,4 h). | Pause ≥4 h consécutives en hébergement convenable + préavis avant premier vol/veille → prolongation FDP MIN(½ pause,4 h). |
| 604 split REST | Next minimum REST += at least split FDP extension; break stays INSIDE FDP; flight time limits unchanged. | Repos minimal suivant augmenté d'au moins la prolongation ; pause DANS le FDP ; limites de temps de vol inchangées. |
| 604 UOC 604.102 | Unexpected operational circumstance AFTER FDP starts; PIC consults crew → safe FDP extension ≤3 h; next min REST += extension; PIC advises operator, retained 5 y. | Circonstance opérationnelle imprévue APRÈS début FDP ; CDB consulte équipage → prolongation sûre ≤3 h ; repos minimal suivant + prolongation ; avis exploitant, conservation 5 ans. |
| 700 split 700.50 | Break ≥60 min in suitable accommodation; deduct 45 min THEN credit 100% at 00:00–05:59 / 50% at 06:00–23:59 (acclimatized time). | Pause ≥60 min en hébergement convenable ; retrancher 45 min PUIS crédit 100 % à 00:00–05:59 / 50 % à 06:00–23:59 (heure acclimatée). |
| 700 split special | UOC replanning after FDP begins → 50% credit after 45-min deduction; night duty split ≤3 consecutive nights; reserve extension +2 h only with ≤2 FLTs after break. | Replanification pour imprévu après début FDP → crédit 50 % après déduction 45 min ; service de nuit ≤3 nuits consécutives ; réserve +2 h seulement si ≤2 vols après pause. |
| 700 UOC 700.63 | UOC within 60 min after FDP starts; PIC consults ALL crew; max FDP +1 h single / +2 h unaugmented / +3 h augmented 1 FLT / +2 h augmented 2–3 FLTs. | Imprévu dans les 60 min après début FDP ; CDB consulte TOUT équipage ; max +1 h solo / +2 h non renforcé / +3 h renforcé 1 vol / +2 h renforcé 2–3 vols. |
| 700 UOC REST / 700.64 | 700.63 extension → following REST += extension; PIC notifies operator at FDP end. 700.64 post-start split only on PIC agreement BEFORE ground break. | Prolongation 700.63 → repos suivant + prolongation ; CDB avise exploitant à fin FDP. 700.64 : fractionnement en cours seulement avec accord CDB AVANT pause au sol. |
| FDP vs FLT trap | SPLIT/UOC increases permitted FDP, NOT flight-time allowance (604.98/700.27); split + UOC not automatically cumulative; Part 700 Division IV MEDEVAC differs. | Fractionnement/imprévu prolonge FDP, PAS temps de vol permis (604.98/700.27) ; crédits non automatiquement cumulables ; Division IV MEDEVAC différente. |
***

## De-/anti-icing · FPD · HOT / Dégivrage · antigivrage

| Label | English | Français |
|---|---|---|
| De / Anti | De-icing removes contamination; anti-icing protects a clean surface temporarily. Clean-aircraft rule: CAR 602.11; ground fluid does not authorize flight in icing. | Dégivrage retire contamination; antigivrage protège temporairement surface propre. Aéronef propre : RAC 602.11; liquide au sol n’autorise pas vol en givrage. |
| I / II / III / IV | I: thin, usually heated, orange, short protection. II: thickened, pale/yellow. III: thickened, lower-speed applications, bright yellow. IV: thickened, longer protection, green. Verify product/aircraft approval. | I : fluide, généralement chauffé, orange, protection courte. II : épaissi, pâle/jaune. III : épaissi, vitesses inférieures, jaune vif. IV : épaissi, protection prolongée, vert. Vérifier produit/aéronef approuvé. |
| FPD / FDP | FPD = freezing-point depressant. FDP = flight duty period. ADF in fluid literature can mean aircraft deicing fluid, not the navigation receiver. | FPD = abaisseur du point de congélation. FDP = période de service de vol. ADF en dégivrage peut désigner liquide dégivrant, pas radiocompas. |
| LOUT | Use the warmest limit: aerodynamic acceptance; freezing point +10°C (I) or +7°C (II/III/IV); for diluted thickened fluids, coldest published HOT temperature. | Retenir limite la plus chaude : acceptation aérodynamique; congélation +10°C (I) ou +7°C (II/III/IV); liquides épaissis dilués : température minimale HOT publiée. |
| LOUT example | Type I: freezing point −30°C; aerodynamic limit −25°C → LOUT −20°C. OAT −22°C: too cold. Check aircraft skin temperature too. | Type I : congélation −30°C; limite aérodynamique −25°C → LOUT −20°C. OAT −22°C : trop froid. Vérifier aussi température du revêtement. |
| HOT clock | Starts at BEGINNING of final fluid application. Two-step: start of anti-icing step, not completion. Product/dilution, temperature, precipitation/intensity determine table. | Débute au COMMENCEMENT de dernière application. Deux étapes : début antigivrage, pas fin. Tableau selon produit/dilution, température, précipitations/intensité. |
| HOT judgement | HOT is an estimate, not assured protection. Fluid failure or changed conditions can end protection earlier. Expired HOT: approved inspection/re-treatment procedure; never automatic extra minutes. | HOT estimatif, protection non garantie. Défaillance ou changement météo peut raccourcir protection. HOT expiré : procédure approuvée inspection/nouveau traitement; aucun délai automatique. |
| Snow / Neige | Use TC snowfall-intensity/visibility table, including day/night and temperature. METAR −SN alone does not resolve very-light versus light HOT categories. | Utiliser tableau TC intensité neige/visibilité, jour/nuit et température. −SN seul ne distingue pas catégories HOT très faible/faible. |
| Annual tables | Use current winter 2026–27 HOT guidance and exact fluid table. No universal duration per type. Allowance-time rules for ice pellets/small hail differ from HOT. | Utiliser guide HOT hiver 2026–27 et tableau produit exact. Aucune durée universelle par type. Délais granulés de glace/petite grêle distincts des HOT. |
***

## Over water · survival / Survol de l’eau · survie

| Label | English | Français |
|---|---|---|
| Flotation trigger | Water takeoff/landing OR unable to reach shore after engine failure: one life preserver, individual flotation device or PFD per person. [602.62(1)] | Décollage/amerrissage OU rive inaccessible après panne moteur : un gilet, dispositif individuel de flottaison ou VFI par personne. [602.62(1)] |
| 50 NM / Shore | Landplane >50 NM from shore: LIFE PRESERVER for each person, even if engine-out shore reach is possible. Accessible while seated. [602.62(2),(4)] | Avion terrestre >50 NM rive : GILET DE SAUVETAGE par personne, même si rive accessible après panne. Accessible depuis siège. [602.62(2),(4)] |
| Raft / Radeau — SE | Single engine, or multi unable to maintain flight with any engine failed: rafts beyond lesser of 100 NM or 30 min at FILED cruise speed from suitable emergency landing site. [602.63(1)] | Monomoteur, ou multi incapable de maintenir vol avec panne d’un moteur : radeaux au-delà du moindre de 100 NM ou 30 min à vitesse croisière DÉPOSÉE depuis lieu convenable d’atterrissage d’urgence. [602.63(1)] |
| Raft / Radeau — ME | Multi able to maintain flight with any engine failed: lesser of 200 NM/60 min. Transport-category aeroplane exception: up to lesser of 400 NM/120 min. [602.63(2)–(3)] | Multi capable de maintenir vol avec panne d’un moteur : moindre de 200 NM/60 min. Exception avion catégorie transport : jusqu’au moindre de 400 NM/120 min. [602.63(2)–(3)] |
| Calculation / Calcul | SE threshold = min(100, filed kt ×0.5) NM. Filed 120 kt →60 NM; 180 kt →90 NM; 240 kt →100 NM. Beyond threshold triggers raft carriage. | Seuil monomoteur = min(100, kt déposés ×0,5) NM. 120 kt →60 NM; 180 kt →90 NM; 240 kt →100 NM. Au-delà : radeau requis. |
| Capacity / Capacité | Total raft rated capacity covers everyone. Stow accessible, visibly marked near exit; attached kit: shelter, water/purification, visual distress signals, suited to area/season. [602.63(6)] | Capacité nominale totale radeaux pour tous. Accessibles, emplacement signalé près sortie; trousse attachée : abri, eau/purification, signaux visuels, adaptée région/saison. [602.63(6)] |
| Shore ≠ landing site | Flotation test uses shore reach/distance; raft test uses a SUITABLE EMERGENCY LANDING SITE. Crossing width is not automatically distance from that site. | Flottaison : rive accessible/distance rive; radeaux : LIEU CONVENABLE D’ATTERRISSAGE D’URGENCE. Largeur traversée pas automatiquement distance de ce lieu. |
| 703 seaplane | 703.83: inflatable flotation worn on/above water; COM procedures and PIC instruction. Exception: person on stretcher, incubator or similar device. Not a blanket rule for every private landplane. | 703.83 : dispositif gonflable porté sur/au-dessus eau; procédures manuel exploitation et instruction CdB. Exception : civière, incubateur ou dispositif similaire. Pas règle universelle avion terrestre privé. |
| Land survival / Survie terre | 602.61: FIRE + SHELTER + WATER + SIGNAL, for everyone and climate. 25-NM exception requires staying within 25 NM of departure aerodrome AND surface-station radio capability throughout. Other listed exceptions exist. | 602.61 : FEU + ABRI + EAU + SIGNAL, pour tous selon climat. Exception 25 NM : rester à 25 NM aérodrome départ ET capacité radio avec station au sol tout le vol. Autres exceptions prévues. |
| Planning / Préparation | Recommendation: wear suitable inflatable flotation, brief evacuation and inflate only outside; assess cold-water exposure and rescue delay. Equipment carriage alone does not make a crossing safe. | Recommandation : porter dispositif gonflable adapté, expliquer évacuation et gonfler seulement dehors; évaluer eau froide et délai secours. Emport seul ne rend pas traversée sûre. |

***

## Memory traps & examples / Pièges et exemples

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

[TC CPAER TP12881](https://tc.canada.ca/en/aviation/publications/study-reference-guide-written-examinations-commercial-pilot-licence-aeroplane-tp-12881) · [TC AIM 2026-1 RAC 9.21; VREF checked 20 Oct 2026](https://tc.canada.ca/sites/default/files/2026-03/aim-2026-1_access_en.pdf) · [TC AWM 500/525; VREF certification basis checked 20 Oct 2026](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/canadian-aviation-regulations-sor-96-433/standards/airworthiness-manual-chapter-525-transport-category-aeroplanes/airworthiness-chapter-525-subchapter-b-canadian-aviation-regulations-cars) · [NAV CANADA CNOP v12 · 14 May 2026](https://www.navcanada.ca/en/comms/_localized-assets/guides/cnop/cnop-v12-04172026.pdf) · [NAV CANADA pilot briefings](https://www.navcanada.ca/en/flight-planning/flight-planning-and-reporting.aspx) · [TSB A02C0072 · 7.7√psi](https://tsb.gc.ca/eng/rapports-reports/aviation/2002/a02c0072/a02c0072.html) · [TC radio reception approximation](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/canadian-aviation-regulations-sor-96-433/standards/standard-724-commuter-operations-helicopters-canadian-aviation-regulations-cars) · [NRC twilight; time section checked 19 Oct 2026](https://nrc.canada.ca/en/research-development/products-services/software-applications/interpreting-results-sunrisesunset-calculator) · [TC TP 975, Exercise 24; navigation review 19 Oct 2026](https://tc.canada.ca/en/aviation/publications/flight-instructor-guide-aeroplane-tp-975) · [FAA Instrument Flying Handbook, Ch. 9 (2012), navigation geometry](https://www.faa.gov/sites/faa.gov/files/pilots/FAA-H-8083-15B.pdf) · [Oxygen CAR 605.31–32 · checked 19 Oct 2026](https://laws-lois.justice.gc.ca/eng/regulations/sor-96-433/page-77.html) · [Passenger weights AC 700-022; AIM 2026-1 RAC 3.4.7 · checked 19 Oct 2026](https://tc.canada.ca/en/aviation/reference-centre/advisory-circulars/advisory-circular-ac-no-700-022) · [FDP CAR 700.28 · checked 19 Oct 2026](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-700.28.html) · [TC fatigue rules · checked 19 Oct 2026](https://tc.canada.ca/en/aviation/commercial-air-services/fatigue-management-aviation/flight-duty-time-regulations-prescriptive-vs-performance-based-options) · [TP 14052 March 2026 · checked 19 Oct 2026](https://tc.canada.ca/en/aviation/publications/guidelines-aircraft-ground-icing-operations-tp-14052) · [TC current HOT edition · checked 19 Oct 2026](https://tc.canada.ca/en/aviation/general-operating-flight-rules/holdover-time-hot-guidelines-icing-anti-icing-aircraft) · [CAR 602.61 · checked 19 Oct 2026](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-602.61.html) · [CAR 602.62 · checked 19 Oct 2026](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-602.62.html) · [CAR 602.63 · checked 19 Oct 2026](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-602.63.html) · [CAR 703.83 · checked 19 Oct 2026](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/section-703.83.html)
