---
name: write-l4-pebble
description: Author or audit ultra-condensed L4 Pebble aviation memory lines and CAVE study cards using verified MANAB/CFS abbreviations where applicable. Use for CPAER/INRAT recall, Canadian air law, weather, navigation, aircraft systems, and edits to numbered Aero-CAVE cards; preserve every legally or operationally material qualifier.
---

# L4 Pebble · CAVE authoring

Read repository `AGENTS.md` **before** drafting. Treat this skill as the *content/recall* companion to `$build-cave-study-readers` (the latter governs paired Markdown/HTML readers).

## Output contract

- **Default chat response when a memory line is requested:** one dense `L4 · TOPIC: ...` line; no intro, table, heading stack or unsolicited tutorial. Expand only on request or when compression would conceal a safety/legal condition.
- **Numbered Markdown card:** compact `####` subsection(s); one testable rule/decision/trap per bullet or short table row; maintain/update existing **`#### Pebble`** at card end. The Pebble **recaps** the new facts and never introduces unverified new ones.
- **Style:** fragmentary, scan-first; `|` separates independent clauses, `→` for consequence, `≠` for distinction, `≤ ≥ < >` for bounds. Keep units and thresholds adjacent to their condition. Use `R` legal rule / `P` procedure / `F` formula / `T` trap / `M` memory / `?` verify only where useful.
- **No rigid character limit.** Prefer one meaningful line, but split a line if the scope/exception becomes ambiguous. Legal precision outranks brevity.

## Abbreviation protocol

1. Consult `cheatsheets/MANAB_CFS_Essential_EN_FR.md` and, as needed, the **current original NAV CANADA MANAB/CFS** before replacing a word with an abbreviation.
2. Use only established abbreviation **with the applicable meaning and publication context**, e.g. `ACFT` aircraft, `TKOF` takeoff, `LDG` landing, `RWY` runway, `THLD` threshold, `ALT` altitude, `CLNC` clearance, `MAINT` maintenance, `TFC` traffic. Write the word out if no verified code exists.
3. Preserve collisions and context: `AD` (MANAB) / `A/D` (CFS); `RPT` meaning differs; `S 5` ≠ `PF 5`; weather symbols are not universally CFS codes. Never invent abbreviations or expand an existing code to a different meaning.
4. Retain technical/regulatory acronyms (e.g. `AME`, `AMO`, `CoR`, `CoA`, `ELT`, `MEL`, `RVSM`) **without claiming they are MANAB/CFS codes**.
5. Match destination EN or EN/FR; for bilingual terms verify official Canadian French wording rather than translating aviation phraseology mechanically.

## Accuracy gates — mandatory before compression

1. **Authority:** extract the exact rule from current CAR/Standard, AIM, CFS/CAP/NOTAM, AFM/POH, or relevant primary publication as appropriate. Do not extrapolate from a study mnemonic.
2. **Scope:** record *who/what operation/which ACFT*, **exceptions**, **threshold inclusivity**, units, dates, conditions and whether a rule is required/advisory.
3. **Distinctions:** separate REG vs title vs flight authority; AME vs AMO; MEL vs DML; flight vs air time; maintenance entry vs maintenance release; ATC CLNC vs SEP vs conflict resolution vs TFC information.
4. **No silent simplification:** never strip a qualifier to fit one line. If source is incomplete/outdated, use `?` and state what needs verification.
5. **Sources:** link the controlling section beside the detailed card; store edition/review details in `CONTENT_REVIEW.md` for material source changes. In chats, cite when regulatory claims require verification.
6. **Consistency:** search the existing repo card **before** adding a duplicate or proposing a new card. Keep existing heading anchors and cross-card terms stable; update Markdown + matching HTML where a reader exists.

## Procedure

1. Read `AGENTS.md`; locate target card, existing `#### Pebble`, glossary and any paired reader.
2. Build a private *full-fidelity rule set*: applicability → requirement → exception → timeline/threshold → trap → authority.
3. Condense to tagged rows, then an L4 Pebble. Compare every number, unit, condition, exception and negation against the rule set.
4. Run a **counterexample test**: could an examiner pose a case wrongly answered by the Pebble? If yes, restore the qualifier or split the line.
5. For repo edits: update the card, its final Pebble, any paired HTML, and the material `CONTENT_REVIEW.md` entry; verify rendered Markdown/table syntax, stable anchors, links and the fetched commit. Do not create new automation/JSON generation merely to draft text.
6. For conversation answers: when the topic is missing/incomplete in Aero-CAVE, offer a specific addition or correction; **do not commit without user approval**.

## Compression examples

- **Wrong:** `TECH records: airframe + ENG + PROP`
- **L4:** `TECH: journey log + airframe + each ENG + **variable-pitch PROP only** + applicable component records + W&B | title transfer→deliver records` (CAR 605.92, .97)
- **Wrong:** `ELT exempt within 25 NM`
- **L4:** `ELT: FTU certificate holder + training FLT + ≤25 NM DEP → exception` (CAR 605.38(3)); private personal FLT not automatically exempt.
- **Wrong:** `Interim CoR valid 3 months`
- **L4:** `CoR: qualifying transfer→interim REG, until *earliest* 3mo / new CoR / further transfer | second successive interim transfer NO` (CAR 202.36)
- **Wrong:** `C-class ATC separates VFR`
- **L4:** `Class C: SEP IFR–IFR | conflict resolution IFR–VFR as necessary | TFC all | VFR–VFR conflict resolution O/R after TFC` (verify against current AIM/ATS standards).

## Ready-to-commit checklist

- [ ] Read `AGENTS.md`; reviewed current relevant authorities and glossary.
- [ ] Each statement testable; **all** material qualifiers preserved.
- [ ] Abbreviations verified/context-correct; no fictitious MANAB/CFS code.
- [ ] `#### Pebble` is present/updated, reflects detail and introduces nothing new.
- [ ] No duplication or unrequested prose; existing EN/FR and file identity maintained.
- [ ] Paired HTML synchronized if present; `CONTENT_REVIEW.md` updated when material.
- [ ] Commit fetched/verified before claiming success.
