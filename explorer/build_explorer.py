#!/usr/bin/env python3
"""Build index.html: the Aero CAVE explorer and landing page (offline, single file).

Reads explorer/ontology.json + the Markdown cards, splits cards into sections,
maps each section to ontology concepts and licence paths, and embeds everything
into explorer/template.html -> index.html.

  python3 explorer/build_explorer.py            # write index.html
  python3 explorer/build_explorer.py --check    # fail if index.html is stale
  python3 explorer/build_explorer.py --report   # print mapping report

Markdown stays the editorial source: re-run after any card or ontology change.
No third-party dependencies.
"""
import json, re, sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ONT = ROOT / "explorer" / "ontology.json"
TPL = ROOT / "explorer" / "template.html"
SYL = ROOT / "explorer" / "syllabus.json"
UID = re.compile(r"^<!--\s*id:\s*([a-z][a-z0-9-]*)\s*((?:\|[^>]*?)?)-->\s*\n?")
KBHEAD = re.compile(r"^<!--\s*concept:\s*([a-z][a-z0-9-]*)\s*((?:\|[^>]*?)?)-->", re.M)
STUB = re.compile(r"^→ Moved[^\n]*\]\(([^)#\s]+)#([^)\s]+)\)\s*$")


def attrs(raw):
    """'| also: a, b | level: PPL IR' -> {'also': [...], 'level': [...]}"""
    out = {}
    for part in raw.split("|"):
        if ":" in part:
            k, v = part.split(":", 1)
            out[k.strip()] = [x for x in re.split(r"[,\s]+", v.strip()) if x]
    return out
OUT = ROOT / "index.html"
HEAD = re.compile(r"^(#{1,4})\s+(.*\S)\s*$")
BOLD = re.compile(r"^\*\*([^*]+)\*\*$")


def slug(text):
    """GitHub-style heading anchor."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.U)
    return s.replace(" ", "-")


def split_card(text, bold_headings=False):
    """Return (title, [(heading, anchor|None, body)])."""
    title, sections, cur, buf = None, [], None, []
    seen = {}

    def flush():
        body = "\n".join(buf).strip()
        body = re.sub(r"(^|\n)\*\*\*\s*$", "", body).strip()
        body = re.sub(r"^\*\*\*\s*\n", "", body).strip()
        if cur is None:
            if len(re.sub(r"[\s*]", "", body)) > 60:
                sections.append(("Overview", None, body))
        elif body:
            sections.append((cur[0], cur[1], body))

    for line in text.splitlines():
        m = HEAD.match(line)
        b = BOLD.match(line.strip()) if bold_headings else None
        if m or b:
            head = (m.group(2) if m else b.group(1)).strip()
            if m and title is None:
                title = head
                continue
            flush()
            buf = []
            anchor = None
            if m:
                a = slug(head)
                n = seen.get(a, 0)
                seen[a] = n + 1
                anchor = a if n == 0 else f"{a}-{n}"
            cur = (head, anchor)
        else:
            buf.append(line)
    flush()
    return title, sections


def parse_match(entry):
    if ">" in entry:
        cards, rx = entry.split(">", 1)
        return set(cards.split(",")), re.compile(rx, re.I)
    return None, re.compile(entry, re.I)


def build():
    ont = json.loads(ONT.read_text(encoding="utf-8"))
    concepts = ont["concepts"]
    ids = [c["id"] for c in concepts]
    errors = []
    if len(ids) != len(set(ids)):
        errors.append("duplicate concept ids")
    idset = set(ids)
    pathset = {p["id"] for p in ont["paths"]}
    for c in concepts:
        for ref in c["broader"] + c["related"]:
            if ref not in idset:
                errors.append(f"{c['id']}: unknown concept {ref}")
        if c["id"] in c["broader"]:
            errors.append(f"{c['id']}: broader loop")
    sections, cards, uids, stubs = [], [], set(), []
    kindset = {k["id"] for k in ont["kinds"]}
    for cid, card in ont["cards"].items():
        text = (ROOT / card["file"]).read_text(encoding="utf-8")
        title, secs = split_card(text, card.get("boldHeadings", False))
        cards.append({"id": cid, "en": card["en"], "fr": card["fr"], "file": card["file"],
                      "reader": card.get("reader"), "title": title})
        for i, (head, anchor, body) in enumerate(secs):
            if head == "Overview" and anchor is None:
                continue
            m = UID.match(body)
            if not m:
                errors.append(f"{cid} · {head}: unit id comment required under the heading")
                continue
            a = attrs(m.group(2))
            cs, ps = a.get("concepts", []), a.get("level", [])
            if m.group(1) in uids:
                errors.append(f"duplicate unit id {m.group(1)}")
            uids.add(m.group(1))
            if not cs or any(c not in idset for c in cs):
                errors.append(f"{cid} · {head}: missing or unknown concepts {cs}")
            if not ps or any(p not in pathset for p in ps):
                errors.append(f"{cid} · {head}: missing or unknown level")
            kd = (a.get("kind") or [card.get("kind", "procedure")])[0]
            if kd not in kindset:
                errors.append(f"{cid} · {head}: unknown kind {kd}")
            if kd == "knowledge" and cid not in ("17",):
                errors.append(f"{cid} · {head}: knowledge notes live in kb/, not in a card")
            sections.append({"id": f"{cid}-{i}", "card": cid, "h": head, "a": anchor, "c": cs, "p": ps, "kd": kd,
                             "u": m.group(1), "md": body[m.end():].strip()})
    for kid, kb in ont.get("kb", {}).items():
        files = sorted(p for p in (ROOT / kb["dir"]).glob("*.md") if p.name != "README.md")
        entry = {"id": kid, "en": kb["en"], "fr": kb["fr"], "file": kb["dir"] + "/README.md", "reader": None,
                 "title": None, "kb": True, "files": {}}
        cards.append(entry)
        n = 0
        for fp in files:
            rel = fp.relative_to(ROOT).as_posix()
            text = fp.read_text(encoding="utf-8")
            title, secs = split_card(text)
            hm = KBHEAD.search(text)
            if not hm or hm.group(1) not in idset:
                errors.append(f"{rel}: missing or unknown '<!-- concept: … -->' header")
                continue
            concept, fa = hm.group(1), attrs(hm.group(2))
            entry["files"][rel] = title
            for head, anchor, body in secs:
                if anchor is None:
                    continue
                m = UID.match(body)
                if not m:
                    errors.append(f"{rel} · {head}: unit id comment required under the heading")
                    continue
                ua = attrs(m.group(2))
                if m.group(1) in uids:
                    errors.append(f"duplicate unit id {m.group(1)}")
                uids.add(m.group(1))
                cs = [concept] + [c for c in ua.get("also", []) if c != concept]
                ps = ua.get("level") or fa.get("level") or []
                for c in cs:
                    if c not in idset:
                        errors.append(f"{rel} · {head}: unknown concept {c}")
                if not ps or any(p not in pathset for p in ps):
                    errors.append(f"{rel} · {head}: missing or unknown level")
                kd = (ua.get("kind") or ["pebble" if head == "Pebble" else "knowledge"])[0]
                if kd not in kindset:
                    errors.append(f"{rel} · {head}: unknown kind {kd}")
                sections.append({"id": f"{kid}-{n}", "card": kid, "f": rel, "h": head, "a": anchor, "c": cs,
                                 "p": ps, "kd": kd, "u": m.group(1), "md": body[m.end():].strip()})
                n += 1
    for st in stubs:
        target = (ROOT / st["from"]).parent / st["to"]
        if not target.exists():
            errors.append(f"stub {st['card']} · {st['h']}: target {st['to']} not found")
        else:
            rel = target.resolve().relative_to(ROOT).as_posix()
            if not any(s.get("f") == rel and s["a"] == st["a"] for s in sections):
                errors.append(f"stub {st['card']} · {st['h']}: no heading #{st['a']} in {rel}")
    used = {c for s in sections for c in s["c"]}
    for c in concepts:
        if c["id"] not in used and not any(c["id"] in o["broader"] for o in concepts):
            errors.append(f"concept {c['id']} has no sections and no narrower concepts")
    if errors:
        sys.exit("ontology errors:\n  " + "\n  ".join(errors))

    vids = set()
    for v in ont["views"]:
        if v["id"] in vids or v["id"] in pathset or not re.fullmatch(r"[a-z0-9]+", v["id"]):
            errors.append(f"view {v['id']}: bad or duplicate id")
        vids.add(v["id"])
        if v.get("level") and v["level"] not in pathset:
            errors.append(f"view {v['id']}: unknown level")
        for k in v.get("kinds", []):
            if k not in kindset:
                errors.append(f"view {v['id']}: unknown kind {k}")
        for ref in v.get("concepts", []):
            if ref not in idset:
                errors.append(f"view {v['id']}: unknown concept {ref}")
        if v.get("re"):
            re.compile(v["re"])
    if errors:
        sys.exit("ontology errors:\n  " + "\n  ".join(errors))
    syl = json.loads(SYL.read_text(encoding="utf-8"))
    gids = [g["id"] for g in syl["guides"]]
    if len(gids) != len(set(gids)):
        errors.append("duplicate guide id")
    for v in ont["views"]:
        if v.get("guide") and v["guide"] not in gids:
            errors.append(f"view {v['id']}: unknown guide {v['guide']}")
    for g in syl["guides"]:
        if g.get("level") not in pathset:
            errors.append(f"{g['id']}: level must be one of the paths")
        if g.get("kind") not in ("written", "flight"):
            errors.append(f"{g['id']}: kind must be written or flight")
        for key in ("method", "scope"):
            if not (g.get(key) or {}).get("en") or not g[key].get("fr"):
                errors.append(f"{g['id']}: {key} needs en and fr")
        for grp in g["groups"]:
            if grp.get("concept") not in idset:
                errors.append(f"{g['id']} {grp['code']}: group needs a known concept")
            for it in grp["items"]:
                if it["s"] not in "CPME":
                    errors.append(f"{g['id']} {grp['code']} {it['n']}: bad status")
                if it["s"] in "CP" and not it["u"]:
                    errors.append(f"{g['id']} {grp['code']} {it['n']}: C/P needs a unit")
                if it["s"] == "P" and not it["gap"]:
                    errors.append(f"{g['id']} {grp['code']} {it['n']}: P needs a gap note")
                for u in it["u"]:
                    if u not in uids:
                        errors.append(f"{g['id']} {grp['code']} {it['n']}: unknown unit {u}")
    if errors:
        sys.exit("syllabus errors:\n  " + "\n  ".join(errors))
    # levels come from the guides that cite a unit; Pebbles take their concept file's levels;
    # a unit no guide cites keeps its hand-set level as a fallback ("ph")
    order = [p["id"] for p in ont["paths"]]
    cited, essential = {}, set()
    for g in syl["guides"]:
        for grp in g["groups"]:
            for it in grp["items"]:
                for u in it["u"]:
                    cited.setdefault(u, set()).add(g["level"])
                    if it.get("e"):
                        essential.add(u)
    by_file = {}
    for s in sections:
        by_file.setdefault(s.get("f") or s["card"], set()).update(cited.get(s["u"], ()))
    for s in sections:
        lv = cited.get(s["u"]) or (by_file[s.get("f") or s["card"]] if s["h"] == "Pebble" else set())
        hand = s.pop("p")
        s["p"] = [p for p in order if p in lv]
        if not s["p"]:
            s["ph"] = hand
        if s["u"] in essential:
            s["e"] = 1
    # related links: hand-set ones plus derived ones (a unit tagged with both concepts, or
    # two or more TC items citing units of both); never between a concept and its ancestors
    byid = {c["id"]: c for c in concepts}
    def anc(i, seen=None):
        seen = seen if seen is not None else set()
        for b in byid[i]["broader"]:
            if b not in seen:
                seen.add(b); anc(b, seen)
        return seen
    pair = {}
    def bump(a, b, w):
        if a != b and a not in anc(b) and b not in anc(a):
            k = tuple(sorted((a, b))); pair[k] = pair.get(k, 0) + w
    prim = {s["u"]: s["c"][0] for s in sections}
    for s in sections:
        for i, a in enumerate(s["c"]):
            for b in s["c"][i + 1:]:
                bump(a, b, 2)
    for g in syl["guides"]:
        for grp in g["groups"]:
            for it in grp["items"]:
                ps = sorted({prim[u] for u in it["u"]})
                for i, a in enumerate(ps):
                    for b in ps[i + 1:]:
                        bump(a, b, 1)
    for (a, b), w in sorted(pair.items()):
        if w >= 2 and b not in byid[a]["related"] and a not in byid[b]["related"]:
            byid[a].setdefault("related", []).append(b)
    used = {c for s in sections for c in s["c"]}
    for c in concepts:
        if c["id"] not in used and not any(c["id"] in x["broader"] for x in concepts):
            errors.append(f"{c['id']}: concept has no note and no narrower concept")
    if errors:
        sys.exit("ontology errors:\n  " + "\n  ".join(errors))
    # each TC guide is also a view: the units its items cite
    for g in syl["guides"]:
        units = sorted({u for grp in g["groups"] for it in grp["items"] for u in it["u"]})
        ont["views"].append({"id": g["id"], "group": "guide", "en": g["guide"] + " · " + g["en"], "fr": g["guide"] + " · " + g["fr"], "guide": g["id"], "kind": g["kind"], "units": units})
    data = {
        "guides": syl["guides"],
        "stubs": len(stubs),
        "paths": ont["paths"],
        "kinds": ont["kinds"],
        "views": ont["views"],
        "concepts": [{k: c.get(k, []) for k in ("id", "en", "fr", "broader", "related", "alt")} for c in concepts],
        "cards": cards,
        "sections": sections,
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    stamp = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    html = TPL.read_text(encoding="utf-8").replace("/*__DATA__*/null", payload).replace("__BUILD__", stamp)
    return html, data, []


def ont_kb_files():
    out = {}
    for p in ROOT.glob("kb/*/*.md"):
        m = KBHEAD.search(p.read_text(encoding="utf-8"))
        if m:
            out[m.group(1)] = str(p.relative_to(ROOT))
    return out


def main():
    html, data, report = build()
    if "--report" in sys.argv:
        from collections import Counter
        n = Counter(c for s in data["sections"] for c in s["c"])
        for c in data["concepts"]:
            print(f"{n[c['id']]:4d}  {c['id']:14s} {c['en']}")
    if "--audit" in sys.argv:
        from collections import Counter
        own = {}
        for kid, kb in ont_kb_files().items():
            own[kid] = kb
        cited = {u for g in data["guides"] for grp in g["groups"] for it in grp["items"] for u in it["u"]}
        n = Counter(c for s in data["sections"] for c in s["c"])
        print("Concepts without a kb file (notes only via cards or 'also'):")
        for c in data["concepts"]:
            if c["id"] not in own and n[c["id"]]:
                print(f"  {c['id']:14s} {n[c['id']]:3d} notes")
        print("Concepts with TC items but no knowledge note:")
        kn = Counter(c for s in data["sections"] if s["kd"] == "knowledge" for c in s["c"])
        gi = Counter(grp["concept"] for g in data["guides"] for grp in g["groups"] for _ in grp["items"])
        for c in data["concepts"]:
            if gi[c["id"]] and not kn[c["id"]]:
                print(f"  {c['id']:14s} {gi[c['id']]:3d} TC items")
        un = [s for s in data["sections"] if s["u"] not in cited and s["kd"] in ("knowledge", "procedure")]
        print(f"Knowledge / procedure notes no TC item cites: {len(un)}")
        return
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != html:
            sys.exit("index.html is stale: run python3 explorer/build_explorer.py")
        print("index.html is up to date")
        return
    OUT.write_text(html, encoding="utf-8")
    print(f"index.html: {len(data['sections'])} sections, {len(data['concepts'])} concepts, "
          f"{len(data['cards'])} cards, {len(html)//1024} KiB")


if __name__ == "__main__":
    main()
