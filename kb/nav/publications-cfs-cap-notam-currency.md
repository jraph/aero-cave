# Publications: CFS / CAP / NOTAM & currency / Publications : CFS / CAP / NOTAM et validité
<!-- concept: nav-pubs | level: PPL CPL -->

[Index](README.md) · concept `nav-pubs` · unit IDs are stable: never rename one.

***
#### CFS / aerodrome scan
<!-- id: nav-cfs-aerodrome-scan | from: 01 | level: PPL CPL -->

- `P:` aerodrome ID/elevation→RWY dimensions/surface/slope→circuit direction/altitude→FREQ/MF/ATF→lighting/PCL→`PRO`→`CAUTION`→services/fuel→nearby airspace.
- CFS sections: General | Aerodrome Directory | Planning | Radio Navigation/Communications | Military | Emergency.
- `T:` CFS page still requires current NOTAM/AIP SUP: see `ref-current-publication-cycle-c01`.
***
#### Publication currency
<!-- id: ref-current-publication-cycle-c01 | from: 01 | level: PPL CPL -->

- Publication schedules differ by product; do not assign a universal 56-day validity to all charts and publications.
- `CAP/CAP GEN/CFS/AIP/DAH/charts` on the AIRAC cycle: update every `56 days`; AIP SUP/AIC publish on a `14-day` cycle. VNC: see `nav-lo-chart-navaid-depiction`.
- AIRAC cycle at last review (14 Nov 2026): effective `2026-10-29` through `2026-12-24`. `T:` this line ages every 56 days; read the effective dates printed on the product.
- `P preflight:` current publication→NOTAM→AIP SUP/AIC→airport/procedure page→aircraft data.
- Trigger NOTAM = notice that source material changed; retrieve the referenced amendment/Supplement. It may expire while the underlying AIP SUP remains active.
- `[NAV CANADA publication schedule; AIC 009/2026]`
***
#### CFS servicing · public facilities / Services · installations publiques CFS
<!-- id: fx-cfs-servicing-public-facilities-services-ins | from: F | also: agk-stall | kind: glossary | level: PPL CPL -->

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
#### NOTAM · header & Q-line / En-tête et ligne Q
<!-- id: fx-notam-header-q-line-en-t-te-et-ligne-q | from: F | level: PPL CPL -->

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
#### Common NOTAM codes / Codes NOTAM courants
<!-- id: fx-common-notam-codes-codes-notam-courants | from: F | kind: glossary | level: PPL CPL -->

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
#### Enroute low altitude (LO) chart
<!-- id: nav-lo-chart-navaid-depiction | level: CPL -->

- LO charts: IFR navigation along ATS routes **below 18 000 ft ASL**; show radio aids, airways, controlled/uncontrolled airspace, special use airspace, communication stations, selected aerodromes. 10-chart series.
- `T` **Not for VFR navigation**: no obstacles, terrain or roads. Check NOTAM and AIP Supplements: data current only to the effective date.
- VNC (1:500 000) limits: not for low ceiling/visibility, not all obstacles shown, updated every 1–5 years → VTA where available; new data appears first by NOTAM/AIP SUP, then CFS, then chart.
- `?:` navaid symbols (VOR, VORTAC, NDB, DME) not described here: read the chart legend.

- Sources: [NAV CANADA, Fit for Purpose (B1, B7)](https://www.navcanada.ca/en/publications/_localised-assets/files/14-403_aeronautical-publications-guide_e3.pdf).
***
#### Pebble
<!-- id: nav-publications-cfs-cap-notam-currency-pebble | level: PPL CPL -->

- CFS `ID/elevation → RWY → circuit → FREQ/MF/ATF → lighting/PCL → PRO → CAUTION → services/fuel → airspace | sections: General, Aerodrome Directory, Planning, Radio Nav/Comm, Military, Emergency | CFS page still needs current NOTAM/AIP SUP`
- CURRENCY `schedules differ by product | CAP/CFS/AIP/charts 56 days; AIP SUP/AIC 14 days | read printed effective dates | preflight: publication → NOTAM → AIP SUP/AIC → airport/procedure page → ACFT data | Trigger NOTAM = pointer only; may expire while AIP SUP stays active`
- LO `IFR <18000 ASL | airways + radio aids + airspace | not for VFR (no terrain/obstacles) | check NOTAM + AIP SUP`
***
