#!/usr/bin/env python3
"""Regenerate the schema tables in SCHEMA.md from wiki_lint.py's constants.

Everything between the BEGIN/END markers is overwritten; the prose around them is
hand-written. The linter's constants are the source of truth: change them there, then
re-run this. Presentation order lives here and is asserted against the linter's sets.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wiki_lint as wl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "SCHEMA.md")
BEGIN, END = "<!-- BEGIN GENERATED SCHEMA -->", "<!-- END GENERATED SCHEMA -->"

KIND_ORDER = ["hub", "concept", "system", "product", "comparison", "decision", "reference"]
DIR_OF = {"hub": "criteria/", "concept": "concepts/", "system": "systems/",
          "product": "products/", "comparison": "comparisons/", "decision": "decision/",
          "reference": "reference/, start-here/, index.md"}
STATUS_ORDER = ["settled", "contested", "unverified"]
CONF_ORDER = ["high", "medium", "low"]


def fmt_section(variants):
    head, *alts = variants
    return head if not alts else head + " (or " + ", ".join(f'"{a}…"' for a in alts) + ")"


def main():
    assert set(KIND_ORDER) == wl.KINDS, "KIND_ORDER out of sync with wiki_lint.KINDS"
    assert set(STATUS_ORDER) == wl.STATUSES, "STATUS_ORDER out of sync"
    assert set(CONF_ORDER) == wl.CONFIDENCES, "CONF_ORDER out of sync"

    out = ["### Front matter", "",
           "Required keys, in order: " + " ".join(f"`{k}`" for k in wl.FM_KEYS) + ".",
           "",
           "Product pages add: " + " ".join(f"`{k}`" for k in wl.PRODUCT_KEYS) +
           ". Write list values inline (`streaming: [HEOS, AirPlay 2]`) and unknowns as `?`.",
           "",
           "| Field | Allowed values |", "|---|---|",
           "| `kind` | " + " · ".join(f"`{k}`" for k in KIND_ORDER) + " |",
           "| `status` | " + " · ".join(f"`{s}`" for s in STATUS_ORDER) + " |",
           "| `confidence` | " + " · ".join(f"`{c}`" for c in CONF_ORDER) + " |",
           f"| `criteria` | integers 1–{len(wl.CRITERIA)} (see below) |",
           "| `last_verified` | ISO date (YYYY-MM-DD) |",
           "| `slug` | equal to the filename, kebab-case |", ""]

    out += ["### Criteria (the spine)", "", "| # | Hub | Name |", "|---|---|---|"]
    for n, (slug, name) in sorted(wl.CRITERIA.items()):
        out.append(f"| {n} | `wiki/criteria/{slug}.md` | {name} |")
    out.append("")

    out += ["### Required `##` sections by kind", "",
            "| Kind | Directory | Required sections |", "|---|---|---|"]
    for k in KIND_ORDER:
        secs = wl.SECTIONS.get(k)
        cell = " · ".join(fmt_section(v) for v in secs) if secs else "none checked; own shape"
        out.append(f"| `{k}` | {DIR_OF[k]} | {cell} |")
    out += ["", "Headers match as prefixes. Every body opens with a bold claim sentence.", ""]

    out += ["### Word limits", "", "| Kind | Floor–target |", "|---|---|"]
    for k in KIND_ORDER:
        if k in wl.LIMITS:
            lo, hi = wl.LIMITS[k]
            out.append(f"| `{k}` | {lo:,}–{hi:,} words |")
    dlo, dhi = wl.DEFAULT_LIMIT
    out += [f"| every other kind | {dlo:,}–{dhi:,} words |", "",
            f"Over target is `WORDS-HIGH`; over {wl.CEILING:,} is `WORDS-CEIL` and is two pages.",
            "Under the floor is a merge candidate, never padded. `reference` pages have no floor.", ""]

    out += ["### Staleness budgets", "",
            f"`last_verified` older than {wl.STALE_DAYS_PRODUCTS} days on `wiki/products/`, or",
            f"{wl.STALE_DAYS} days anywhere else, is `STALE`. Prices, availability and successor",
            "models move fastest.", ""]

    out += ["### Pages exempt from a standard shape", ""]
    out += [f"- `{p}`" for p in sorted(wl.SECTION_EXEMPT)]
    out += ["", "Adding to this list is a decision recorded in `log.md`, never a way to silence a finding."]

    body = "%s\n\n%s\n\n%s" % (BEGIN, "\n".join(out), END)
    text = open(PAGE, encoding="utf-8").read()
    if BEGIN in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda _: body, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + body + "\n"
    open(PAGE, "w", encoding="utf-8").write(text)
    print("SCHEMA.md: %d generated lines, %d kinds" % (len(out), len(KIND_ORDER)))


if __name__ == "__main__":
    main()
