#!/usr/bin/env python3
"""Mechanical inversion: extracts/*.md -> extracts/by-page/<dir>--<page>.md.

Parses the '-> <page> [tag]' entry markers written by the extraction subagents,
groups entries by target page, and flags pages with empty bundles plus entries
with unknown or NO-HOME targets. Rebuilds by-page/ from scratch every run.

The canonical page set is scraped out of MANIFEST.md, so a page that is not in
the manifest will be reported as an unknown target rather than silently accepted.
"""
import os, re, collections, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = os.path.join(ROOT, "extracts")
BP = os.path.join(EX, "by-page")

# canonical pages from MANIFEST (paths relative to wiki/)
mtext = open(os.path.join(ROOT, "MANIFEST.md"), encoding="utf-8").read()
manifest_paths = re.findall(r"`(?:wiki/)?((?:[a-z-]+/)?[a-z0-9-]+\.md)`", mtext)
canonical = {p for p in manifest_paths if "/" in p or p == "index.md"}
canonical.add("index.md")

ARROW = re.compile(r"^→\s+(\S+)\s*(\[.*)?$")

if os.path.isdir(BP):
    shutil.rmtree(BP)
os.makedirs(BP)

bundles = collections.defaultdict(list)   # page -> list of (source_slug, entry_text)
unknown = collections.Counter()           # bad targets
nohome = []                               # (source, entry head)
entry_count = 0
per_source = {}

for fn in sorted(os.listdir(EX)):
    # extractor-reports and the verification files are round scratch, not extracts
    if not fn.endswith(".md") or fn == "extractor-reports.md" or fn.startswith("verification"):
        continue
    src = fn[:-3]
    lines = open(os.path.join(EX, fn), encoding="utf-8").read().splitlines()
    n = 0
    i = 0
    while i < len(lines):
        m = ARROW.match(lines[i].strip())
        if m:
            target = m.group(1).rstrip(",;")
            # collect entry block: this line + following lines until blank or next arrow
            block = [lines[i]]
            j = i + 1
            while j < len(lines) and lines[j].strip() and not ARROW.match(lines[j].strip()):
                block.append(lines[j])
                j += 1
            entry = "\n".join(block)
            n += 1
            entry_count += 1
            t = target.replace("wiki/", "")
            if t != "NO-HOME" and not t.endswith(".md"):
                t += ".md"
            if t == "NO-HOME":
                nohome.append((src, block[0][:100]))
            elif t in canonical:
                bundles[t].append((src, entry))
            else:
                unknown[(src, t)] += 1
            i = j
        else:
            i += 1
    per_source[src] = n

for page, entries in bundles.items():
    out = os.path.join(BP, page.replace("/", "--"))
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Bundle: {page} ({len(entries)} entries from {len(set(s for s,_ in entries))} sources)\n\n")
        for src, entry in entries:
            f.write(f"[{src}]\n{entry}\n\n")

print(f"sources parsed: {len(per_source)}; total entries: {entry_count}")
print(f"pages with bundles: {len(bundles)}")

zero = [s for s, n in per_source.items() if n == 0]
if zero:
    print("\n== SOURCES WITH ZERO PARSED ENTRIES (format problem?) ==")
    for s in zero: print(" ", s)

print("\n== EMPTY BUNDLES (pages with no extracts — expected for research-only pages) ==")
skel = {p for p in canonical if p != "index.md"}
for p in sorted(skel - set(bundles)):
    print(" ", p)

if unknown:
    print("\n== UNKNOWN TARGETS ==")
    for (s, t), c in unknown.most_common(40):
        print(f"  {t}  (from {s}, {c}x)")

if nohome:
    print("\n== NO-HOME ENTRIES ==")
    for s, h in nohome:
        print(f"  {s}: {h}")

print("\n== BUNDLE SIZES ==")
for p, es in sorted(bundles.items(), key=lambda kv: -len(kv[1])):
    print(f"  {len(es):4d}  {p}")
