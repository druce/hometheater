#!/usr/bin/env python3
"""Deterministic gate runner for the home theater wiki.

Ported from governance_wiki/scripts/wiki_lint.py. Every check here is one a machine
can decide. Findings are tagged AUTO when a script can safely fix them and JUDGE when
the page has to be read: banned prose gets rewritten, never regex-substituted, and a
product page with a missing spec gets flagged rather than given an invented number.

  python3 scripts/wiki_lint.py            report everything
  python3 scripts/wiki_lint.py --fix      apply the AUTO set, then report
  python3 scripts/wiki_lint.py --judgment only the findings needing a model
  python3 scripts/wiki_lint.py --json     machine-readable

Exit 0 when nothing outstanding, 1 otherwise, so it can gate a commit.
"""
import os, re, sys, json, glob, datetime, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
TODAY = datetime.date.today()

# --- schema, from CLAUDE.md "Page schema" -----------------------------------
FM_KEYS = ["title", "slug", "kind", "criteria", "status",
           "confidence", "last_verified", "sources"]
# Extra keys every product page carries; gen_matrix.py builds reference/matrix.md from them.
PRODUCT_KEYS = ["brand", "model", "model_year", "msrp_usd", "street_usd", "channels",
                "room_correction", "streaming", "preouts", "successor_of"]
KINDS = {"hub", "concept", "system", "product", "comparison", "decision", "reference"}
STATUSES = {"settled", "contested", "unverified"}
CONFIDENCES = {"high", "medium", "low"}

# The spine: decision criteria. Numbers are what `criteria:` front matter holds.
CRITERIA = {
    1: ("room-correction", "Room correction & bass management"),
    2: ("music-performance", "Music & two-channel performance"),
    3: ("streaming-and-multiroom", "Streaming & multiroom"),
    4: ("amplification-and-preouts", "Amplification & pre-outs"),
    5: ("connectivity", "Connectivity"),
    6: ("usability-and-support", "Usability, app & firmware support"),
    7: ("value-and-reliability", "Value, reliability & resale"),
}

# --- required sections per kind ----------------------------------------------
# Each section is a tuple of accepted header prefixes, canonical wording first.
# SCHEMA.md's tables are generated from these constants by gen_schema.py.
HUB = [("Why this matters here",), ("What good looks like",), ("Systems and concepts",),
       ("How the candidates rank",), ("Open questions",)]
CONCEPT = [("The mechanism",), ("Why it matters for a 5.1 room",),
           ("Common misconceptions",), ("Sources",)]
SYSTEM = [("What it does",), ("Versions and tiers",), ("Measured and observed results",),
          ("Limits",), ("Sources",)]
PRODUCT = [("Verdict",), ("Specs that matter",), ("Room correction",), ("Streaming",),
           ("Measurements",), ("Known issues",), ("Price and availability",), ("Sources",)]
COMPARISON = [("Question",), ("Answer",), ("Table",), ("Sources",)]
SECTIONS = {"hub": HUB, "concept": CONCEPT, "system": SYSTEM, "product": PRODUCT,
            "comparison": COMPARISON}
# Pages whose shape is deliberately their own (decision/ and reference/ kinds have no
# required sections at all). Listed pages also skip the word floor.
SECTION_EXEMPT = {"wiki/index.md", "wiki/start-here/my-system.md",
                  "wiki/reference/glossary.md", "wiki/reference/matrix.md",
                  "wiki/reference/bibliography.md", "wiki/reference/open-questions.md"}

# --- word limits ------------------------------------------------------------
LIMITS = {"hub": (400, 1200), "product": (300, 1200), "comparison": (150, 1200),
          "decision": (100, 1500)}
DEFAULT_LIMIT = (300, 1500)
CEILING = 2000

# --- staleness ---------------------------------------------------------------
STALE_DAYS = 180
STALE_DAYS_PRODUCTS = 60   # street prices, availability and successors move fastest

# --- banned constructions -----------------------------------------------------
BANNED = [
    (r"it's important to note", "banned phrase"),
    (r"\bat its core\b", "banned phrase"),
    (r"\bfundamentally\b", "banned word"),
    (r"\brobust(ly|ness)?\b", "banned word"),
    (r"\bholistic(ally)?\b", "banned word"),
    (r"\bseamless(ly)?\b", "banned word"),
    (r"\bleverag(e|es|ed|ing)\b", "banned as a verb, check the usage"),
    (r"\bunlock(s|ed|ing)?\b", "banned word"),
    (r"\bempower(s|ed|ing|ment)?\b", "banned word"),
    # marketing register: says nothing a measurement could check
    (r"\baudiophile[- ]grade\b", "marketing adjective"),
    (r"\bimmersive\b", "marketing adjective"),
    (r"\bstunning\b", "marketing adjective"),
    (r"\bjaw[- ]dropping\b", "marketing adjective"),
    (r"\bbest[- ]in[- ]class\b", "marketing adjective"),
    (r"\bcrystal[- ]clear\b", "marketing adjective"),
    (r"\bgame[- ]chang(er|ing)\b", "marketing adjective"),
]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿️]")
LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
MD_LINK_TARGET = re.compile(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)")
PROTECTED = ("raw" + os.sep,)


class Finding:
    def __init__(self, code, path, msg, auto=False, line=None):
        self.code, self.path, self.msg, self.auto, self.line = code, path, msg, auto, line

    def __str__(self):
        loc = f"{self.path}:{self.line}" if self.line else self.path
        return f"  [{'AUTO ' if self.auto else 'JUDGE'}] {self.code:<16} {loc}\n      {self.msg}"

    def as_dict(self):
        return {"code": self.code, "path": self.path, "line": self.line,
                "auto": self.auto, "message": self.msg}


def pages():
    return sorted(os.path.relpath(p, ROOT)
                  for p in glob.glob(os.path.join(WIKI, "**", "*.md"), recursive=True))


def split_page(text):
    """(front_matter_text, body_text, body_start_line)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text, 1
    return m.group(1), text[m.end():], text[:m.end()].count("\n") + 1


def parse_fm(fm):
    """Flat top-level key -> raw string value. Block-list items are collected under their key."""
    out, cur = {}, None
    for line in fm.split("\n"):
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            cur = m.group(1)
            out[cur] = m.group(2).strip()
        elif line.startswith(("  -", "-")) and cur:
            out[cur] = (out.get(cur, "") + " " + line.strip()).strip()
    return out


def strip_code(body):
    """Blank out fenced code and HTML comments, keeping line numbers."""
    blank = lambda m: "\n" * m.group(0).count("\n")
    return re.sub(r"<!--.*?-->", blank, re.sub(r"```.*?```", blank, body, flags=re.S), flags=re.S)


def check_pages(f):
    docs = {}
    for rel in pages():
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        fm_text, body, body_line = split_page(text)
        docs[rel] = (fm_text, body, text)

        # --- front matter ---
        if fm_text is None:
            f.append(Finding("FM-MISSING", rel, "no front matter block"))
            continue
        fm = parse_fm(fm_text)
        missing = [k for k in FM_KEYS if k not in fm]
        if missing:
            f.append(Finding("FM-KEY", rel, f"front matter missing: {', '.join(missing)}",
                             auto=missing == ["sources"]))
        kind = fm.get("kind", "")
        if kind and kind not in KINDS:
            f.append(Finding("FM-ENUM", rel, f"kind '{kind}' is not in the schema"))
        if fm.get("status") and fm["status"] not in STATUSES:
            f.append(Finding("FM-ENUM", rel, f"status '{fm['status']}' is not in the schema"))
        if fm.get("confidence") and fm["confidence"] not in CONFIDENCES:
            f.append(Finding("FM-ENUM", rel, f"confidence '{fm['confidence']}' is not in the schema"))
        crit = re.findall(r"\d+", fm.get("criteria", ""))
        if any(int(c) not in CRITERIA for c in crit):
            f.append(Finding("FM-CRIT", rel, f"criteria out of range 1-{len(CRITERIA)}: {fm['criteria']}"))
        slug = fm.get("slug", "")
        if slug and slug != os.path.splitext(os.path.basename(rel))[0]:
            f.append(Finding("FM-SLUG", rel, f"slug '{slug}' does not match the filename"))

        # --- product spec completeness: the matrix is generated from these ---
        if kind == "product":
            absent = [k for k in PRODUCT_KEYS if k not in fm]
            unknown = [k for k in PRODUCT_KEYS if k in fm and k != "successor_of"
                       and fm[k].strip() in ("", "?", "[]", "[?]")]
            if absent:
                f.append(Finding("FM-PRODUCT", rel, f"product keys missing: {', '.join(absent)}"))
            if unknown:
                f.append(Finding("FM-PRODUCT", rel,
                                 f"product keys unknown (?): {', '.join(unknown)} — "
                                 "find the primary source or leave '?', never guess"))

        # --- staleness ---
        lv = fm.get("last_verified", "")
        try:
            age = (TODAY - datetime.date.fromisoformat(lv)).days
            budget = STALE_DAYS_PRODUCTS if rel.startswith("wiki/products/") else STALE_DAYS
            if age > budget:
                f.append(Finding("STALE", rel,
                                 f"last_verified {lv} is {age} days old (budget {budget})"))
        except ValueError:
            f.append(Finding("FM-DATE", rel, f"last_verified '{lv}' is not an ISO date"))

        # --- claim sentence (an H1 title may precede it) ---
        lines = [l.strip() for l in body.split("\n") if l.strip()]
        first = next((l for l in lines if not l.startswith("# ")), "")
        if not first.startswith("**"):
            f.append(Finding("CLAIM", rel, "body does not open with a bold claim sentence"))

        # --- required sections ---
        heads = [h.strip() for h in re.findall(r"^##\s+(.+)$", body, re.M)]
        if rel not in SECTION_EXEMPT:
            for want in SECTIONS.get(kind, []):
                if not any(h.startswith(v) for v in want for h in heads):
                    f.append(Finding("SEC-MISSING", rel, f"missing section '## {want[0]}'"))

        # --- word limits ---
        w = len(strip_code(body).split())
        lo, hi = LIMITS.get(kind, DEFAULT_LIMIT)
        if w < lo and rel not in SECTION_EXEMPT and kind != "reference":
            f.append(Finding("WORDS-LOW", rel,
                             f"{w} words, under the {lo} floor; a merge candidate, do not pad it"))
        elif w > CEILING:
            f.append(Finding("WORDS-CEIL", rel, f"{w} words, over the {CEILING} ceiling; this is two pages"))
        elif w > hi:
            f.append(Finding("WORDS-HIGH", rel, f"{w} words, over the {hi} target"))

        # --- banned constructions ---
        clean = strip_code(body)
        for i, line in enumerate(clean.split("\n"), start=body_line):
            for pat, why in BANNED:
                m = re.search(pat, line, re.I)
                if m:
                    f.append(Finding("BANNED", rel, f"{why}: '{m.group(0)}'", line=i))
            if EMOJI.search(line):
                f.append(Finding("BANNED", rel, "emoji", line=i))
            if re.search(r"^#{1,6}\s+.*\?\s*$", line):
                f.append(Finding("BANNED", rel, "question-form header", line=i))
            if re.search(r"!(?!\[)", line) and not line.strip().startswith(("|", ">")):
                f.append(Finding("BANNED", rel, "exclamation point", line=i))
    return docs


def check_graph(f, docs):
    known = set(docs)
    out, inb = {}, collections.defaultdict(set)
    for rel, (_, _, text) in docs.items():
        tgts = set()
        for m in MD_LINK_TARGET.finditer(text):
            t = os.path.relpath(os.path.normpath(
                os.path.join(os.path.dirname(os.path.join(ROOT, rel)), m.group(1))), ROOT)
            if t in known:
                tgts.add(t)
            elif not m.group(1).startswith(("http://", "https://")):
                f.append(Finding("LINK-BROKEN", rel, f"link target does not exist: {m.group(1)}"))
        tgts.discard(rel)
        out[rel] = tgts
    for r, ts in out.items():
        for t in ts:
            inb[t].add(r)

    for rel in sorted(known):
        if rel != "wiki/index.md" and len(inb[rel]) < 2:
            f.append(Finding("ORPHAN", rel, f"{len(inb[rel])} inbound links; every page needs at least 2"))

    depth, frontier = {"wiki/index.md": 0}, ["wiki/index.md"]
    while frontier:
        nxt = []
        for p in frontier:
            for t in out.get(p, ()):
                if t not in depth:
                    depth[t] = depth[p] + 1
                    nxt.append(t)
        frontier = nxt
    for rel in sorted(known):
        if rel not in depth:
            f.append(Finding("DEPTH", rel, "not reachable from wiki/index.md"))
        elif depth[rel] > 3:
            f.append(Finding("DEPTH", rel, f"{depth[rel]} clicks from wiki/index.md; the limit is 3"))

    # every product must be ranked by at least one criterion hub, or it is outside the decision
    for rel, (fm_text, _, _) in docs.items():
        if fm_text and parse_fm(fm_text).get("kind") == "product":
            if not any(src.startswith("wiki/criteria/") for src in inb[rel]):
                f.append(Finding("UNRANKED", rel, "no criteria/ hub links to this product"))
    return out, inb


def check_manifest(f, docs):
    mtext = open(os.path.join(ROOT, "MANIFEST.md"), encoding="utf-8").read()
    rows = set(re.findall(r"`(wiki/[^`]*?\.md)`", mtext))
    for p in sorted(rows - set(docs)):
        f.append(Finding("MANIFEST", p, "MANIFEST row has no file on disk"))
    for p in sorted(set(docs) - rows):
        f.append(Finding("MANIFEST", p, "page on disk has no MANIFEST row"))


def check_hygiene(f, fix):
    residue = []
    for dirpath, dirnames, files in os.walk(ROOT):
        if any(x in dirpath for x in (".git", "node_modules", ".obsidian")):
            dirnames[:] = []
            continue
        for name in files:
            p = os.path.join(dirpath, name)
            if re.match(r"^#.*#$", name) or name.startswith(".#") or name == ".DS_Store":
                residue.append(p)
            elif os.path.islink(p) and not os.path.exists(p):
                residue.append(p)
    for p in residue:
        rel = os.path.relpath(p, ROOT)
        protected = rel.startswith(PROTECTED)   # raw/ is read-only; scripts too
        if fix and not protected:
            try:
                os.remove(p)
            except OSError as e:
                f.append(Finding("HYGIENE", rel, f"could not remove: {e}"))
                continue
        f.append(Finding("HYGIENE", rel,
                         "residue inside read-only raw/ — remove it by hand" if protected
                         else ("editor residue removed" if fix else "editor residue or dangling symlink"),
                         auto=not protected))

    dp = os.path.join(ROOT, "CLAUDE.md")
    if os.path.exists(dp):
        for name in sorted(set(re.findall(r"`([A-Z][A-Za-z-]+\.md)`", open(dp, encoding="utf-8").read()))):
            if not os.path.exists(os.path.join(ROOT, name)):
                f.append(Finding("DANGLING-REF", "CLAUDE.md", f"names `{name}`, which is not on disk"))


def check_fm_fix(f, fix):
    """The one safe front-matter repair: append `sources: []` when simply absent."""
    if not fix:
        return
    for rel in pages():
        p = os.path.join(ROOT, rel)
        text = open(p, encoding="utf-8").read()
        fm_text, body, _ = split_page(text)
        if fm_text is None or "sources" in parse_fm(fm_text):
            continue
        open(p, "w", encoding="utf-8").write(f"---\n{fm_text}\nsources: []\n---\n{body}")
        f.append(Finding("FM-KEY", rel, "added sources: []", auto=True))


def main():
    fix = "--fix" in sys.argv
    f = []
    docs = check_pages(f)
    check_graph(f, docs)
    check_manifest(f, docs)
    check_hygiene(f, fix)
    check_fm_fix(f, fix)

    if "--judgment" in sys.argv:
        f = [x for x in f if not x.auto]
    if "--json" in sys.argv:
        print(json.dumps([x.as_dict() for x in f], indent=2))
        return 1 if any(not x.auto for x in f) else 0

    groups = collections.defaultdict(list)
    for x in f:
        groups[x.code].append(x)
    print(f"wiki_lint: {len(docs)} pages, {len(f)} findings{' (--fix applied)' if fix else ''}\n")
    for code in sorted(groups):
        print(f"== {code} ({len(groups[code])}) ==")
        for x in groups[code]:
            print(x)
        print()
    remaining = [x for x in f if not x.auto]
    print(f"AUTO: {len(f) - len(remaining)} | JUDGMENT: {len(remaining)}")
    return 1 if remaining else 0


if __name__ == "__main__":
    sys.exit(main())
