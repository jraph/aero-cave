# Formulas & calculations / Formules et calculs

[All study cards](../README.md)

Navigation and operational additions reviewed 19 Oct 2026; source editions and scope in review record. / Ajouts navigation et exploitation revus le 19 oct. 2026; éditions et portée dans le compte rendu.

***

## Time · fuel / Temps · carburant
<!-- id: fx-time-fuel-temps-carburant | concepts: nav-dr, agk-fuel | level: PPL CPL -->

| Label | English | Français |
|---|---|---|
| Distance | D(NM) = GS(kt) × t(h) | D(NM) = vitesse sol(kt) × durée(h) |
| Time / Durée | t(min) = 60D/GS | t(min) = 60D/vitesse sol |
| GS / Vitesse sol | GS(kt) = 60D/t(min) | Vitesse sol(kt) = 60D/t(min) |
| Fuel / Carburant | Fuel = hourly flow × hours; endurance = usable fuel/flow | Carburant = débit horaire × heures; autonomie = carburant utilisable/débit |
| Specific range | GS/fuel flow = NM per fuel unit | Vitesse sol/débit = NM par unité de carburant |
***

## Wind · navigation / Vent · navigation
<!-- id: fx-wind-navigation-vent-navigation | concepts: nav-dr | level: PPL CPL -->

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

## Weight · balance / Masse · centrage
<!-- id: fx-weight-balance-masse-centrage | concepts: agk-wb | level: PPL CPL -->

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
<!-- id: fx-altitude-weather-altitude-m-t-o | concepts: met-atmos | level: PPL CPL -->

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
<!-- id: fx-stall-airspeed-d-crochage-vitesse | concepts: agk-stall, agk-vspeeds | level: PPL CPL -->

| Label | English | Français |
|---|---|---|
| Load / Charge | n = 1/cos(bank): coordinated LEVEL turn only | n = 1/cos(inclinaison) : virage coordonné EN PALIER uniquement |
| Stall / Décrochage | Vs loaded = Vs × √n; Vs₂ = Vs₁√(W₂/W₁) | Vs sous charge = Vs × √n; Vs₂ = Vs₁√(W₂/W₁) |
| VS / VS1 / VS0 | VS = generic stall speed; VS1 = specified configuration (often clean); VS0 = landing config. VS and VS1 can refer to the same clean speed; not VS0. | VS = vitesse de décrochage générique; VS1 = configuration spécifiée (souvent lisse); VS0 = configuration d'atterrissage. VS et VS1 peuvent désigner la même vitesse en configuration lisse; pas VS0. |
| VA · theoretical / théorique | VA_est = VS(clean)√n_limit; legacy Normal +3.8g → ≈1.95 VS1 (mental ≈2×VS1, not a VA range); VS1=50 KIAS → ≈97.5 KIAS. Positive stall/limit-load intersection, not necessarily certified VA. | VA_est = VS(lisse)√n_limite; Normal ancien +3,8g → ≈1,95 VS1 (calcul mental ≈2×VS1, pas une plage de VA); VS1=50 KIAS → ≈97,5 KIAS. Intersection décrochage/charge limite positive, pas nécessairement la VA certifiée. |
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
<!-- id: fx-climb-descent-mont-e-descente | concepts: agk-perfcalc | level: PPL CPL -->

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
<!-- id: fx-turns-virages | concepts: agk-load | level: PPL CPL -->

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
<!-- id: fx-radio-runway-radio-piste | concepts: agk-perfcalc, ifr-minima | level: PPL CPL -->

| Label | English | Français |
|---|---|---|
| VHF range | NM ≈ 1.23(√h₁ + √h₂); 1.25 also used; feet above surface | NM ≈ 1,23(√h₁ + √h₂); 1,25 également; hauteurs en pi au-dessus de la surface |
| Rotating tyre | Dynamic hydroplaning kt ≈ 9√pressure(psi); 36psi→54kt | Pneu en rotation : aquaplanage dynamique kt ≈ 9√pression(psi); 36psi→54kt |
| Non-rotating tyre | kt ≈ 7.7√pressure(psi); 36psi→46.2kt | Pneu sans rotation : kt ≈ 7,7√pression(psi); 36psi→46,2kt |
| FISE frequencies | 123.275 / 123.375 / 123.475 / 123.550 MHz; use local published RCO | 123,275 / 123,375 / 123,475 / 123,550 MHz; utiliser RCO publié |
| 126.7 | Generally not monitored by FIC at dedicated FISE RCOs; broadcasts may occur | Généralement non veillée par FIC aux RCO FISE dédiés; diffusions possibles |
***

## Conversions
<!-- id: fx-conversions | concepts: nav-units | level: PPL CPL -->

| Label | English | Français |
|---|---|---|
| NM | 1 NM = 1.852km = 6076ft = 1.151 statute mi | 1 NM = 1,852km = 6076pi = 1,151 mille terrestre |
| Gallon | US 3.785L; Imperial 4.546L | US 3,785L; impérial 4,546L |
| Mass / length | 1kg = 2.205lb; 1m = 3.281ft | 1kg = 2,205lb; 1m = 3,281pi |
| Earth / Terre | 15° longitude/hour; 4min/degree; 1′ latitude ≈ 1NM | 15° longitude/heure; 4min/degré; 1′ latitude ≈ 1NM |
***

## Timing shortcuts / Estimation du temps
<!-- id: fx-timing-shortcuts-estimation-du-temps | concepts: nav-dr | level: PPL CPL -->

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

## Memory traps & examples / Pièges et exemples
<!-- id: fx-memory-traps-examples-pi-ges-et-exemples | concepts: nav-dr | kind: trap | level: PPL CPL -->

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
