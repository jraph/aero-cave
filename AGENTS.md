# Aero CAVE authoring mode

Default to **CAVE mode** for repository content: super-condensed, scan-first aviation study notes.

- Maximize useful facts per line; remove introductions, filler and repetition.
- Prefer compact tables, fragments, standard abbreviations, symbols and arrows over prose.
- Keep one decision, rule, formula or trap per row/bullet.
- Preserve every qualifier that changes legality, applicability or safety; never compress into ambiguity.
- Explicitly distinguish similar concepts: clearance, separation, conflict resolution, traffic information, authorization, recommendation and memory aid.
- Use existing tags where useful: `F` formula, `M` memory, `T` trap, `P` procedure, `R` rule, `?` verify.
- Maintain a `#### Pebble` section in numbered CAVE study cards and at the end of each concept file: ultra-dense final recall of the card’s highest-yield rules, formulas and traps.
- Pebbles summarize facts already explained above; introduce no new rule or qualifier. Use short tokens, `|`, arrows and standard abbreviations.
- Update the Pebble whenever a material study point changes. Bilingual readers/glossaries may use their existing memory-trap format instead of a Pebble.
- Match the language pattern of the destination: bilingual EN/FR where already bilingual; otherwise retain the card’s language.
- Use official **MANAB and CFS wording/format where applicable**: codes, capitalization, punctuation, field order, compact syntax and EN/FR terms.
- Do not invent or casually expand MANAB/CFS abbreviations. Preserve source-specific meanings and flag collisions (`S 5 ≠ PF 5`, weather code ≠ CFS code).
- For CFS examples, mirror published notation (`PF A-1,2 B-5`, hours in UTC, units/qualifiers) and identify edition-sensitive content.
- Use current authoritative Canadian sources for operational/regulatory claims; keep citations compact and adjacent.
- Use the human contributor’s configured Git identity. Omit automated tool co-author trailers and generated-by signatures from commits and pull requests. Preserve attribution to human collaborators.
- Publish new study topics through the knowledge base and explorer. The explorer replaces standalone readers. Migrate each existing pair with its bilingual content, memory traps, search, deep links and offline access. Keep corrections synchronized until that pair is retired. Record material source/review changes in `CONTENT_REVIEW.md`.
- For L4 Pebble / compact CAVE note authoring or audit, invoke repo-local `$write-l4-pebble` (`.agents/skills/write-l4-pebble/SKILL.md`) **before drafting**; check MANAB/CFS codes and preserve legal/operational qualifiers.
- For maintenance of a legacy CAVE reader, invoke the repo-local `$build-cave-study-readers` skill and follow its existing-reader vs generator-backed routing.
- **Knowledge base (`kb/<domain>/`):** one file per ontology concept; knowledge goes there, ordered procedures/flows/QRCs stay in `cheatsheets/`, aircraft-type data stays in its POH card. Format: `kb/README.md`.
- **Units:** every `####` section carries an ID comment under its heading declaring its concepts and level. IDs are permanent: never rename or reuse. A new unit needs a new unique ID.
- **Pebbles:** exactly one `#### Pebble` as the last unit of each concept file, recapping that file only. No separate Pebble files.
- **Ontology (`explorer/ontology.json`):** concepts (labels EN/FR, broader, related, alt search terms), levels and views only. Do not add content or status notes there. Add a concept only with at least one unit; give it a broader concept unless it is a domain root.
- **Subject vs kind:** a concept is a subject. What a note is (knowledge, procedure, formula, trap, pebble, glossary, aircraft, source) is its `kind:`. Knowledge notes live in `kb/`; the build rejects one in a card. Every guide group in `syllabus.json` names its `concept`. Related links are derived by the build from shared notes and TC items; hand-set `related` is only for links the data cannot show. `python3 explorer/build_explorer.py --audit` lists concepts without a kb file, concepts with TC items but no knowledge note, and uncited notes.
- **READMEs** hold indexes and format only: no migration notes, status or review commentary (those go in `CONTENT_REVIEW.md`).
- `explorer/syllabus.json`: one guide per TC study or flight test guide (`kind`: `written` or `flight`; `level`: the licence it serves; `method` and `scope` in EN and FR; `marks` explains `e` / `d`). Items: `s` = C / P / M; C and P cite unit IDs; P needs a gap note; `e: 1` = TC marks it essential (aeroplane icon), `d: 1` = shaded as commercial depth in TP 12881. Item labels are our own short wording. Unit level badges are derived from the guides that cite them, so cite at the item's level: a PPAER / CPAER item cites an IFR note only when no PPL/CPL-level note covers it.
- After editing any card, concept file, `explorer/ontology.json` or `explorer/syllabus.json`, run `python3 explorer/build_explorer.py` and `node --test tests/*.cjs`, then bump the service-worker VERSION. `index.html` is generated: never edit it by hand.
- Keep paths and anchors stable when practical. Validate links, counts, examples and HTML structure after edits.
