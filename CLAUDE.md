# CLAUDE.md

## What this repo is

An LLM-maintained wiki for one decision: which AV receiver to buy for a **5.1/5.2** system, with
**room correction** and **music & streaming** as the top priorities and no fixed budget. One
subwoofer is assumed, and Radio Paradise FLAC may come from an external streamer (owner decisions,
2026-11-08). The method
is Karpathy's "LLM Wiki" pattern (gist, April 2026): sources are compiled once into a persistent,
cross-linked markdown wiki that the LLM maintains and the owner reads, instead of being
re-searched on every question. The rigor (source manifest, verbatim extracts, verification,
linter, checkpoints) is ported from `~/projects/governance_wiki`.

Write for the owner: technically fluent, will read measurements, wants the reasoning and the
tradeoffs, not a listicle.

## The three layers

```
raw/                LAYER 1 — sources. Immutable. Manuals, spec sheets, measurement reports,
                    reviews, vendor docs, forum threads, price captures. manifest.txt is the
                    register and the only file here that may be written. raw/assets/ holds
                    clipped images (Obsidian attachment folder). Untracked: copyright.
wiki/               LAYER 2 — the compiled wiki. LLM-owned; the owner reads it.
CLAUDE.md           LAYER 3 — the schema: this file. Co-evolved; change it when a convention changes.
```

Supporting files at the root:

```
SCHEMA.md           page spec by kind; tables generated from wiki_lint.py by gen_schema.py
MANIFEST.md         page registry: path, title, kind, criteria, state, words, in, out
log.md              append-only chronological log (Karpathy format, see §Log)
OPEN-QUESTIONS.md   build-side register: claims needing verification and what would settle them
extracts/           verbatim scratch, by-page/ bundles, verification-<round>.md. Untracked.
scripts/            seven tools (see §Tooling)
.claude/skills/     ht-research, ht-lint, ht-query
```

## Layout of wiki/

```
index.md                    the catalog: every page, one-line hook each, by section. Read FIRST
                            on every query. Reading paths: "what to buy" / "understand the tradeoffs".
start-here/my-system.md     the requirements: room, speakers, subs, sources, habits, constraints.
                            Every ranking is relative to this page.
criteria/                   the spine: 7 hubs (see §Spine). Navigational plus the ranking.
concepts/                   how things work: bass management, crossovers, room modes, target
                            curves, pre-outs, amplifier power ratings, why 5.1 skips height.
systems/                    one page per platform: room-correction systems (Audyssey, Dirac Live,
                            ARC Genesis, YPAO) and streaming/multiroom platforms (HEOS, MusicCast,
                            BluOS, WiiM, Radio Paradise). AirPlay 2, Google Cast, the Connect
                            family and Roon Ready share one page, streaming-protocols. Sony DCAC
                            is a paragraph in the room-correction hub.
products/                   one page per receiver model. The decision unit.
comparisons/                filed-back query answers: head-to-heads, shortlist tables.
decision/                   shortlist.md, recommendation.md, buying-checklist.md,
                            setup-and-calibration.md.
reference/                  glossary.md, matrix.md (generated), bibliography.md, open-questions.md.
```

## One axis per page

| Directory | Answers | Example |
|---|---|---|
| `concepts/` | What does this mean and how does it work? | Bass management and LFE |
| `systems/` | What does this platform do, in which versions? | Dirac Live and Bass Control |
| `products/` | What is this receiver and how does it measure up? | Denon AVR-X3800H |
| `criteria/` | What matters here, and how do candidates rank on it? | Room correction |
| `comparisons/` | What is the answer to this specific question? | Dirac on Onkyo vs Denon |
| `decision/` | What do I buy and do? | Recommendation |

Boundary calls decided in advance:

- **A room-correction system and a product are separate pages.** The product page says which
  system and tier it ships with and links; it does not re-explain Dirac. The system page says what
  the tiers do and links the products that carry them.
- **Concepts explain; criteria judge.** "What a crossover is" lives in `concepts/`; "which
  candidates let me set per-speaker crossovers and independent dual-sub delays" lives in the hub.
- **Comparisons are answers, not new canon.** A comparison cites the product and system pages;
  if it establishes a new fact, the fact moves to its canonical page and the comparison links it.
- **Rankings live only in hubs** under "How the candidates rank". `reference/matrix.md` is
  generated from them and from product front matter.

## The spine: 7 criteria

1. Room correction & bass management — `criteria/room-correction.md` (priority)
2. Music & two-channel performance — `criteria/music-performance.md` (priority)
3. Streaming & multiroom — `criteria/streaming-and-multiroom.md` (priority)
4. Amplification & pre-outs — `criteria/amplification-and-preouts.md`
5. Connectivity — `criteria/connectivity.md`
6. Usability, app & firmware support — `criteria/usability-and-support.md`
7. Value, reliability & resale — `criteria/value-and-reliability.md`

The numbers are what `criteria:` front matter carries and are defined in `wiki_lint.CRITERIA`.
Every hub: bold claim → why it matters for this room (from `my-system.md`) → a
minimum / good / best table → systems and concepts linked → how the candidates rank, as an
ordered list of product links with a one-line reason each → open questions.

## Page schema

`SCHEMA.md` is the spec of record. Its tables are generated from `wiki_lint.py` constants by
`gen_schema.py`; change the linter, then regenerate. Never hand-edit either copy of a table.

## Ground rules

1. **`raw/` is read-only**, `manifest.txt` excepted. Never edit, move, or reformat a source.
2. **Do not invent.** No fabricated specs, prices, measurements, firmware features, or quotes.
   An unknown spec is written `?` in front matter and stays `?` until a source settles it.
3. **Show conflicts.** Manufacturer watts vs. bench watts, two reviewers' SINAD figures, a
   forum claim vs. the manual: put both side by side with sources, say which is more credible
   and why.
4. **Canonicalize.** One concept per page; check `MANIFEST.md` before creating one. Log merges.
5. **A page earns existence**: ≥2 inbound links or >300 words, otherwise it is a section.
6. **Report failures.** A page that cannot pass the gates is recorded in `log.md`, not padded.
7. **Date everything that moves.** Prices, availability, firmware, and successor models carry the
   date they were observed. Products have a 60-day staleness budget.

## Source hierarchy

From most to least authoritative:

1. Manufacturer owner's manuals, spec sheets, firmware release notes, and support pages.
2. Independent bench measurements: Audio Science Review, Audioholics, Sound & Vision /
   Stereophile test reports. Record the test conditions (load, channels driven, distortion threshold).
3. Room-correction and streaming vendors' own documentation (Dirac, Audyssey, Anthem, Roon, Denon HEOS...).
4. Established reviews with hands-on time.
5. Owner reports (AVS Forum, Reddit): tagged `[ANECDOTE]` in the manifest, usable for reliability
   patterns and firmware bugs when several independent owners report the same thing.

Retailer pages are a source for price and availability only. Marketing copy is a source for what
the manufacturer claims, labelled as such.

## Voice

Answer first: the claim sentence states the conclusion, each paragraph opens with its point.
Concrete: the model, the number, the test condition, the menu setting. Calibrated: say
"measured", "manufacturer claim", "owner reports", or "unknown" rather than hedging. No marketing
adjectives (the linter bans the common ones). Second person is fine here; this is a personal wiki.
Tables where comparison is the point, prose otherwise. Cite inline at the point of claim,
paraphrased; no verbatim source text in `wiki/`.

## Operations

Three, per Karpathy, each with a skill.

- **Ingest** (`ht-research`) — sources arrive in `raw/` → detect → survey → manifest → extract →
  regroup → triage → verify → **checkpoint (stop for approval)** → write → close. A single clipped
  article can take the light path: read it, discuss takeaways with the owner, then update every
  page it touches (often 5–15), `index.md` and `log.md`.
- **Query** (`ht-query`) — read `index.md` first, then the relevant pages, answer with citations.
  An answer worth keeping is filed back as a `comparisons/` page (ask first) and logged.
- **Lint** (`ht-lint`) — gates, regeneration, fixes; also the semantic lint a script cannot do:
  contradictions between pages, stale prices, products superseded by a newer model, gaps that a
  web search could fill.

## Log

`log.md` is append-only. Every entry starts with a parseable header:

```
## [YYYY-MM-DD] <op> | <title>
```

`op` is one of `init`, `ingest`, `query`, `lint`, `plan`, `write`, `decision`. Body: what changed,
pages touched, conflicts found, exceptions accepted. `grep "^## \[" log.md | tail -10` is the
recent history.

## Tooling

Seven scripts in `scripts/`, ported from governance_wiki. All derive `ROOT` from their own
location and are safe to re-run. None writes to `raw/` except `source_manifest.py --stub`,
which appends to `manifest.txt`.

| Script | Owns |
|---|---|
| `source_manifest.py` | Diffs `raw/` against `raw/manifest.txt` and `extracts/`: NEW / GONE / UNEXTRACTED. `--json`, `--stub`. |
| `regroup.py` | Inverts `extracts/*.md` into `extracts/by-page/<dir>--<page>.md`; flags empty bundles, unknown targets, `NO-HOME`. |
| `wiki_lint.py` | Gate runner: front matter, product spec completeness, sections by kind, word limits, banned words, links, orphans, depth, unranked products, MANIFEST sync, staleness, residue. `--fix`, `--judgment`, `--json`. |
| `linkcheck.py` | Link graph only; exits non-zero on broken links, orphans, MANIFEST drift. |
| `manifest_stats.py` | Rewrites the Words / In / Out columns of `MANIFEST.md`. Add rows by hand first. |
| `gen_schema.py` | Regenerates `SCHEMA.md` tables from `wiki_lint.py` constants. |
| `gen_matrix.py` | Regenerates `wiki/reference/matrix.md`: product specs from front matter, rankings from hubs. Prints `?` and reports every hole. |

Gate before every commit: `python3 scripts/wiki_lint.py && python3 scripts/linkcheck.py --quiet`.
After every commit: `git show --stat`.

## Housekeeping

`MANIFEST.md` states run `planned → skeleton → extracted → verified → drafted → audited`. Update it
in the same commit as any page add or merge, then run `manifest_stats.py`.

`OPEN-QUESTIONS.md` (root) is the build register. `wiki/reference/open-questions.md` is the
reader-facing list of what is genuinely unknown (e.g. whether a promised firmware feature will
ship). Do not conflate them.

Git is local only, no remote. `raw/` and `extracts/` are gitignored and never committed.

The repo is an Obsidian vault: open `~/projects/hometheater`, set the attachment folder to
`raw/assets/`, bind "Download attachments for current file" to a hotkey, use graph view to spot
orphans. Obsidian Web Clipper saves articles straight into `raw/`.
