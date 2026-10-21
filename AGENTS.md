# Aero CAVE authoring mode

Default to **CAVE mode** for repository content: super-condensed, scan-first aviation study notes.

- Maximize useful facts per line; remove introductions, filler and repetition.
- Prefer compact tables, fragments, standard abbreviations, symbols and arrows over prose.
- Keep one decision, rule, formula or trap per row/bullet.
- Preserve every qualifier that changes legality, applicability or safety; never compress into ambiguity.
- Explicitly distinguish similar concepts: clearance, separation, conflict resolution, traffic information, authorization, recommendation and memory aid.
- Use existing tags where useful: `F` formula, `M` memory, `T` trap, `P` procedure, `R` rule, `?` verify.
- Maintain a `#### Pebble` section in numbered CAVE study cards: ultra-dense final recall of the card’s highest-yield rules, formulas and traps.
- Pebbles summarize facts already explained above; introduce no new rule or qualifier. Use short tokens, `|`, arrows and standard abbreviations.
- Update the Pebble whenever a material study point changes. Bilingual readers/glossaries may use their existing memory-trap format instead of a Pebble.
- Match the language pattern of the destination: bilingual EN/FR where already bilingual; otherwise retain the card’s language.
- Use official **MANAB and CFS wording/format where applicable**: codes, capitalization, punctuation, field order, compact syntax and EN/FR terms.
- Do not invent or casually expand MANAB/CFS abbreviations. Preserve source-specific meanings and flag collisions (`S 5 ≠ PF 5`, weather code ≠ CFS code).
- For CFS examples, mirror published notation (`PF A-1,2 B-5`, hours in UTC, units/qualifiers) and identify edition-sensitive content.
- Use current authoritative Canadian sources for operational/regulatory claims; keep citations compact and adjacent.
- When content overlaps a Markdown card and HTML reader, update both in the same change. Record material source/review changes in `CONTENT_REVIEW.md`.
- For L4 Pebble / compact CAVE note authoring or audit, invoke repo-local `$write-l4-pebble` (`.agents/skills/write-l4-pebble/SKILL.md`) **before drafting**; check MANAB/CFS codes and preserve legal/operational qualifiers.
- For CAVE reader creation or updates, invoke the repo-local `$build-cave-study-readers` skill and follow its existing-reader vs generator-backed routing.
- Keep paths and anchors stable when practical. Validate links, counts, examples and HTML structure after edits.
