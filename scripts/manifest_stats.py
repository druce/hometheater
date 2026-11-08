#!/usr/bin/env python3
"""Recompute Words / In / Out columns in MANIFEST.md from the wiki tree.

Words = body word count (everything after the closing front-matter fence).
Out   = distinct internal .md targets linked from the page.
In    = distinct pages linking to it.
State column is left alone unless --state PATH=STATE pairs are supplied.
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'\]\(([^)#]+\.md)(?:#[^)]*)?\)')


def body(path):
    t = open(path).read()
    parts = t.split('---', 2)
    return parts[2] if len(parts) > 2 else t


def rel(p):
    return os.path.relpath(p, ROOT)


def main():
    overrides = {}
    for arg in sys.argv[1:]:
        if '=' in arg:
            k, v = arg.split('=', 1)
            overrides[k] = v

    pages = sorted(glob.glob(os.path.join(ROOT, 'wiki', '**', '*.md'), recursive=True))

    words, out, inb = {}, {}, {}
    for p in pages:
        r = rel(p)
        words[r] = len(body(p).split())
        targets = set()
        for m in LINK.finditer(open(p).read()):
            t = os.path.normpath(os.path.join(os.path.dirname(p), m.group(1)))
            if os.path.exists(t):
                targets.add(rel(t))
        targets.discard(r)
        out[r] = targets
    for r, ts in out.items():
        for t in ts:
            inb.setdefault(t, set()).add(r)

    mpath = os.path.join(ROOT, 'MANIFEST.md')
    lines = open(mpath).read().split('\n')
    seen = set()
    for i, line in enumerate(lines):
        m = re.match(r'^\| `([^`]+)` \| (.*) \|$', line)
        if not m:
            continue
        path = m.group(1)
        cells = [c.strip() for c in m.group(2).split('|')]
        if len(cells) < 6:
            continue
        title, kind, dims, state, _w, _i, _o = (cells + [''] * 7)[:7]
        state = overrides.get(path, state)
        w = words.get(path, 0)
        lines[i] = '| `%s` | %s | %s | %s | %s | %d | %d | %d |' % (
            path, title, kind, dims, state, w,
            len(inb.get(path, ())), len(out.get(path, ())))
        seen.add(path)
    open(mpath, 'w').write('\n'.join(lines))

    missing = [p for p in words if p not in seen]
    orphans = [p for p in words if p not in inb and p != 'wiki/index.md']
    print('rows updated: %d' % len(seen))
    if missing:
        print('pages not in MANIFEST: %s' % ', '.join(sorted(missing)))
    if orphans:
        print('orphans (no inbound links): %s' % ', '.join(sorted(orphans)))
    thin = {p: w for p, w in words.items() if w < 300}
    if thin:
        print('under 300 words: %s' % ', '.join('%s(%d)' % (k, v) for k, v in sorted(thin.items())))
    fat = {p: w for p, w in words.items() if w > 1500}
    if fat:
        print('over 1500 words: %s' % ', '.join('%s(%d)' % (k, v) for k, v in sorted(fat.items())))


if __name__ == '__main__':
    main()
