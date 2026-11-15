# Night & VFR over-the-top / Vol de nuit et VFR OTT
<!-- concept: law-night | level: PPL CPL -->

[Index](README.md) · concept `law-night` · unit IDs are stable: never rename one.

***
#### Twilight · time zones · DST / Crépuscule · fuseaux · heure avancée
<!-- id: fx-twilight-time-zones-dst-cr-puscule-fuseaux-h | from: F | also: law-oprules, nav-dr | level: PPL CPL -->

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
#### Night definition
<!-- id: law-night-definition | from: 04 | also: law-oprules | level: PPL CPL -->

- `Night` = period from end of evening civil twilight to beginning of morning civil twilight. `[CAR 101.01]`
- `T:` sunset is not the legal start of night; use official twilight data.
***
#### VFR OTT
<!-- id: law-vfr-ott | from: 04 | also: law-airspace | level: PPL CPL -->

- Day cruise only; vertical cloud separation `≥1000 ft`; between layers at least `5000 ft`; flight visibility `≥5 SM`; destination weather and rating/equipment conditions apply. `[CAR 602.116; 401.44–401.45; 605.15]`
- `T:` PPL alone does not automatically include VFR OTT privilege.
***
