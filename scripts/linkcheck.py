#!/usr/bin/env python3
"""Link-graph validator for the home theater wiki.

Broken internal links, orphans (inbound < 2), and a MANIFEST <-> disk cross-check
in both directions. Read-only; prints a report and exits non-zero if anything is
broken so it can gate a commit.
"""
import os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")

# canonical set: every .md under wiki/
pages = set()
for dirpath, _, files in os.walk(WIKI):
    for f in files:
        if f.endswith(".md"):
            pages.add(os.path.relpath(os.path.join(dirpath, f), ROOT))

LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
broken = []            # (src, target-as-written)
outbound = collections.Counter()
inbound = collections.Counter()
external = 0

for rel in sorted(pages):
    src = os.path.join(ROOT, rel)
    text = open(src, encoding="utf-8").read()
    for m in LINK.finditer(text):
        tgt = m.group(2).split("#")[0].strip()
        if not tgt or tgt.startswith(("http://", "https://", "mailto:")):
            external += 1
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(src), tgt))
        relr = os.path.relpath(resolved, ROOT)
        if relr in pages:
            outbound[rel] += 1
            inbound[relr] += 1
        else:
            broken.append((rel, tgt))

print("== BROKEN LINKS ==")
for s, t in broken:
    print(f"  {s} -> {t}")
print(f"total broken: {len(broken)}")

print("\n== ORPHANS (inbound < 2, excluding index) ==")
orphans = []
for p in sorted(pages):
    if p == "wiki/index.md":
        continue
    if inbound[p] < 2:
        orphans.append(p)
        print(f"  {p}: inbound={inbound[p]}")

# MANIFEST cross-check
mtext = open(os.path.join(ROOT, "MANIFEST.md"), encoding="utf-8").read()
mpaths = set(re.findall(r"`(wiki/[^`]*?\.md)`", mtext))
print("\n== MANIFEST paths missing on disk ==")
for p in sorted(mpaths - pages):
    print(f"  {p}")
print("== On-disk pages missing from MANIFEST ==")
for p in sorted(pages - mpaths):
    print(f"  {p}")

print(f"\npages: {len(pages)}, manifest rows: {len(mpaths)}, external links: {external}")

if "--quiet" not in sys.argv:
    print("\n== per-page in/out (for MANIFEST update) ==")
    for p in sorted(pages):
        print(f"{p}\t{inbound[p]}\t{outbound[p]}")

sys.exit(1 if (broken or orphans or (mpaths - pages) or (pages - mpaths)) else 0)
