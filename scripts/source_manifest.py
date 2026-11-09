#!/usr/bin/env python3
"""Diff the raw corpus in raw/ against raw/manifest.txt and extracts/.

Three questions, answered mechanically so a round never starts by guessing:

  NEW          a file sits in raw/ with no row in manifest.txt
  GONE         a manifest row names a file that is no longer on disk
  UNEXTRACTED  a file in raw/ that no extracts/*.md claims as its source

raw/ documents are read-only. --stub is the only write, and it only appends
placeholder rows to manifest.txt for the survey stage to fill in.

Extract ownership is resolved from the `source: <filename>` header line that each
extract carries, falling back to slug similarity, because extract filenames are
sometimes hand-shortened rather than mechanically slugified.
"""
import os, re, sys, json, datetime, difflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENTS = os.path.join(ROOT, "raw")
EXTRACTS = os.path.join(ROOT, "extracts")
MANIFEST = os.path.join(AGENTS, "manifest.txt")

SKIP = {"manifest.txt", ".DS_Store", "assets"}
# a slug close enough to the filename's slug is treated as the same document
SLUG_MATCH_RATIO = 0.82


def slug(name):
    """Canonical extract slug for a source filename: the naming rule for new extracts."""
    stem = os.path.splitext(name)[0]
    s = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return s[:60].rstrip("-")


def corpus_files():
    if not os.path.isdir(AGENTS):
        sys.exit(f"no raw/ directory at {AGENTS}")
    return sorted(f for f in os.listdir(AGENTS)
                  if f not in SKIP and not f.startswith(".")
                  and os.path.isfile(os.path.join(AGENTS, f)))


def manifest_rows():
    """(filename, whole_line) per data row. Comments and blanks are skipped."""
    rows = []
    if not os.path.exists(MANIFEST):
        return rows
    for line in open(MANIFEST, encoding="utf-8").read().splitlines():
        if line.startswith("#") or line.count("|") < 4:
            continue
        fields = [f.strip() for f in line.split("|")]
        rows.append((fields[1], line))
    return rows


def extract_owners():
    """source filename -> extract slug, from each extract's `source:` header."""
    owners = {}
    slugs = []
    if not os.path.isdir(EXTRACTS):
        return owners, slugs
    for fn in sorted(os.listdir(EXTRACTS)):
        # extractor-reports and verification-<round> files are round scratch, not extracts
        if not fn.endswith(".md") or fn == "extractor-reports.md" or fn.startswith("verification"):
            continue
        s = fn[:-3]
        slugs.append(s)
        try:
            head = open(os.path.join(EXTRACTS, fn), encoding="utf-8").read(2000)
        except OSError:
            continue
        m = re.search(r"^\s*source:\s*(.+?)\s*$", head, re.M)
        if m:
            owners.setdefault(m.group(1), s)
    return owners, slugs


def has_extract(fname, owners, slugs):
    if fname in owners:
        return owners[fname]
    want = slug(fname)
    if want in slugs:
        return want
    near = difflib.get_close_matches(want, slugs, n=1, cutoff=SLUG_MATCH_RATIO)
    return near[0] if near else None


def main():
    files = corpus_files()
    rows = manifest_rows()
    listed = {fn for fn, _ in rows}
    owners, slugs = extract_owners()

    new = [f for f in files if f not in listed]
    gone = [(fn, line) for fn, line in rows
            if not os.path.exists(os.path.join(AGENTS, fn)) and "[REMOVED" not in line]
    unextracted = [f for f in files if not has_extract(f, owners, slugs)]

    if "--json" in sys.argv:
        print(json.dumps({
            "new": [{"file": f, "slug": slug(f)} for f in new],
            "gone": [fn for fn, _ in gone],
            "unextracted": [{"file": f, "slug": slug(f)} for f in unextracted],
            "corpus": len(files), "rows": len(rows), "extracts": len(slugs),
        }, indent=2))
        return 0

    print(f"corpus: {len(files)} files | manifest: {len(rows)} rows | extracts: {len(slugs)}\n")

    print(f"== NEW — in raw/, absent from manifest.txt ({len(new)}) ==")
    for f in new:
        print(f"  {f}\n      suggested extract slug: {slug(f)}")

    print(f"\n== GONE — manifest row, no file on disk ({len(gone)}) ==")
    for fn, _ in gone:
        print(f"  {fn}")
    if gone:
        print("  (annotate with `— [REMOVED YYYY-MM-DD]`; do not delete the row)")

    print(f"\n== UNEXTRACTED — no extracts/*.md claims this source ({len(unextracted)}) ==")
    for f in unextracted:
        print(f"  {f}\n      write: extracts/{slug(f)}.md")

    if "--stub" in sys.argv and new:
        today = datetime.date.today().isoformat()
        with open(MANIFEST, "a", encoding="utf-8") as fh:
            fh.write(f"\n# Added {today} — survey stage must replace every ? below.\n\n")
            for f in new:
                fh.write(f"? | {f} | ? | ? | ?\n")
        print(f"\nappended {len(new)} stub rows to {os.path.relpath(MANIFEST, ROOT)}")

    return 1 if (new or gone or unextracted) else 0


if __name__ == "__main__":
    sys.exit(main())
