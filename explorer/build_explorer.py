#!/usr/bin/env python3
"""Build explorer.html: Aero CAVE knowledge explorer (offline, single file).

Reads explorer/ontology.json + the Markdown cards, splits cards into sections,
maps each section to ontology concepts and licence paths, and embeds everything
into explorer/template.html -> explorer.html.

  python3 explorer/build_explorer.py            # write explorer.html
  python3 explorer/build_explorer.py --check    # fail if explorer.html is stale
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
UID = re.compile(r"^<!--\s*id:\s*([a-z][a-z0-9-]*)\s*-->\s*\n?")
OUT = ROOT / "explorer.html"
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
    matchers = [(c["id"], [parse_match(m) for m in c["match"]]) for c in concepts]
    rules = [(set(r["cards"].split(",")), re.compile(r["re"], re.I), r["paths"]) for r in ont["pathRules"]]

    sections, cards, report, uids = [], [], [], set()
    for cid, card in ont["cards"].items():
        for p in card["paths"]:
            if p not in pathset:
                errors.append(f"card {cid}: unknown path {p}")
        text = (ROOT / card["file"]).read_text(encoding="utf-8")
        title, secs = split_card(text, card.get("boldHeadings", False))
        cards.append({"id": cid, "en": card["en"], "fr": card["fr"], "file": card["file"],
                      "reader": card.get("reader"), "title": title})
        for i, (head, anchor, body) in enumerate(secs):
            cs = []
            for conc, ms in matchers:
                for only, rx in ms:
                    if (only is None or cid in only) and rx.search(head):
                        cs.append(conc)
                        break
            specific = [c for c in cs if c not in ("study-formulas", "study-abbrev", "type-c150")]
            if not specific:
                cs += [f for f in card["fallback"] if f not in cs]
                report.append(f"fallback  {cid} · {head}")
            paths = card["paths"]
            for only, rx, ps in rules:
                if cid in only and rx.search(head):
                    paths = ps
                    break
            sec = {"id": f"{cid}-{i}", "card": cid, "h": head, "a": anchor, "c": cs, "p": paths}
            m = UID.match(body)
            if m:
                if m.group(1) in uids:
                    errors.append(f"duplicate unit id {m.group(1)}")
                uids.add(m.group(1))
                sec["u"] = m.group(1)
                body = body[m.end():].strip()
            elif "<!-- id:" in body:
                errors.append(f"{cid} · {head}: unit id must be the first line under the heading")
            sec["md"] = body
            sections.append(sec)

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
        for ref in v.get("concepts", []):
            if ref not in idset:
                errors.append(f"view {v['id']}: unknown concept {ref}")
        if v.get("re"):
            re.compile(v["re"])
    if errors:
        sys.exit("ontology errors:\n  " + "\n  ".join(errors))
    syl = json.loads(SYL.read_text(encoding="utf-8"))
    for g in syl["guides"]:
        for grp in g["groups"]:
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
    data = {
        "guides": syl["guides"],
        "paths": ont["paths"],
        "views": ont["views"],
        "concepts": [{k: c[k] for k in ("id", "en", "fr", "broader", "related")} for c in concepts],
        "cards": cards,
        "sections": sections,
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    stamp = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    html = TPL.read_text(encoding="utf-8").replace("/*__DATA__*/null", payload).replace("__BUILD__", stamp)
    return html, data, report


def main():
    html, data, report = build()
    if "--report" in sys.argv:
        from collections import Counter
        n = Counter(c for s in data["sections"] for c in s["c"])
        for c in data["concepts"]:
            print(f"{n[c['id']]:4d}  {c['id']:14s} {c['en']}")
        print("\n".join(report))
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != html:
            sys.exit("explorer.html is stale: run python3 explorer/build_explorer.py")
        print("explorer.html is up to date")
        return
    OUT.write_text(html, encoding="utf-8")
    print(f"explorer.html: {len(data['sections'])} sections, {len(data['concepts'])} concepts, "
          f"{len(data['cards'])} cards, {len(html)//1024} KiB")


if __name__ == "__main__":
    main()
