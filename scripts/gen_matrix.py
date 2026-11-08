#!/usr/bin/env python3
"""Regenerate the decision matrix in wiki/reference/matrix.md.

Replaces governance_wiki's gen_crosswalk.py. Two tables, both derived, never hand-edited:

  1. Product specs   one row per wiki/products/*.md, read from product front matter.
  2. Criterion rank  for each criteria/ hub, the product pages it links to, in the
                     order they first appear under its "How the candidates rank" section.

A missing field prints `?` and is reported on stdout, never silently blanked, because
the governance crosswalk's silent em dash was its known defect.
Everything between the BEGIN/END markers is overwritten. Edit the pages, not the table.
"""
import os, re, sys, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wiki_lint as wl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
PAGE = os.path.join(WIKI, "reference", "matrix.md")
BEGIN, END = "<!-- BEGIN GENERATED MATRIX -->", "<!-- END GENERATED MATRIX -->"
COLS = [("model", "Model"), ("model_year", "Year"), ("channels", "Ch"),
        ("room_correction", "Room correction"), ("streaming", "Streaming"),
        ("preouts", "Pre-outs"), ("msrp_usd", "MSRP $"), ("street_usd", "Street $")]
PROD_LINK = re.compile(r"\]\((?:\.\./)?products/([a-z0-9-]+)\.md")


def fm_of(path):
    fm_text, body, _ = wl.split_page(open(path, encoding="utf-8").read())
    return (wl.parse_fm(fm_text) if fm_text else {}), body


def clean(v):
    v = (v or "?").strip().strip('"')
    return v[1:-1] if v.startswith("[") and v.endswith("]") else v


def main():
    if not os.path.exists(PAGE):
        print("no wiki/reference/matrix.md yet; nothing to generate")
        return 0
    holes = []
    rows = ["### Product specs", "",
            "| Product | " + " | ".join(h for _, h in COLS) + " | Status | Verified |",
            "|---" * (len(COLS) + 3) + "|"]
    for p in sorted(glob.glob(os.path.join(WIKI, "products", "*.md"))):
        fm, _ = fm_of(p)
        s = os.path.basename(p)[:-3]
        cells = []
        for k, _ in COLS:
            v = clean(fm.get(k))
            if v in ("", "?"):
                holes.append(f"{s}: {k}")
                v = "?"
            cells.append(v)
        name = clean(fm.get("brand")) + " " + cells[0]
        rows.append(f"| [{name}](../products/{s}.md) | " + " | ".join(cells) +
                    f" | {clean(fm.get('status'))} | {clean(fm.get('last_verified'))} |")
    rows += ["", "### How each criterion ranks the candidates", "",
             "| Criterion | Ranked products (hub order) |", "|---|---|"]
    for n, (slug, name) in sorted(wl.CRITERIA.items()):
        hp = os.path.join(WIKI, "criteria", slug + ".md")
        if not os.path.exists(hp):
            rows.append(f"| {n}. {name} | (hub not written) |")
            continue
        _, body = fm_of(hp)
        m = re.search(r"^##\s+How the candidates rank.*?$(.*?)(?=^##\s|\Z)", body, re.M | re.S)
        seen = []
        for s in PROD_LINK.findall(m.group(1) if m else ""):
            if s not in seen:
                seen.append(s)
        cell = " → ".join(f"[{s}](../products/{s}.md)" for s in seen) or "(none ranked)"
        rows.append(f"| [{n}. {name}](../criteria/{slug}.md) | {cell} |")

    body = "%s\n\n%s\n\n%s" % (BEGIN, "\n".join(rows), END)
    text = open(PAGE, encoding="utf-8").read()
    if BEGIN in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: body, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + body + "\n"
    open(PAGE, "w", encoding="utf-8").write(text)
    print(f"matrix.md: {len(glob.glob(os.path.join(WIKI, 'products', '*.md')))} products")
    for h in holes:
        print(f"  UNKNOWN {h}")
    return 1 if holes else 0


if __name__ == "__main__":
    sys.exit(main())
