# SCHEMA.md — page spec of record

Everything between the markers below is generated from `scripts/wiki_lint.py` by
`scripts/gen_schema.py`. Change the linter's constants, then regenerate.

A minimal product page front matter, for copying:

```yaml
---
title: "Denon AVR-X3800H"
slug: denon-avr-x3800h
kind: product
criteria: [1, 2, 3, 4]
status: unverified
confidence: low
last_verified: 2026-11-08
sources: [denon-avr-x3800h-manual.pdf]
brand: Denon
model: AVR-X3800H
model_year: ?
msrp_usd: ?
street_usd: ?
channels: ?
room_correction: ?
streaming: [?]
preouts: ?
successor_of: ?
---
```

<!-- BEGIN GENERATED SCHEMA -->

### Front matter

Required keys, in order: `title` `slug` `kind` `criteria` `status` `confidence` `last_verified` `sources`.

Product pages add: `brand` `model` `model_year` `msrp_usd` `street_usd` `channels` `room_correction` `streaming` `preouts` `successor_of`. Write list values inline (`streaming: [HEOS, AirPlay 2]`) and unknowns as `?`.

| Field | Allowed values |
|---|---|
| `kind` | `hub` · `concept` · `system` · `product` · `comparison` · `decision` · `reference` |
| `status` | `settled` · `contested` · `unverified` |
| `confidence` | `high` · `medium` · `low` |
| `criteria` | integers 1–7 (see below) |
| `last_verified` | ISO date (YYYY-MM-DD) |
| `slug` | equal to the filename, kebab-case |

### Criteria (the spine)

| # | Hub | Name |
|---|---|---|
| 1 | `wiki/criteria/room-correction.md` | Room correction & bass management |
| 2 | `wiki/criteria/music-performance.md` | Music & two-channel performance |
| 3 | `wiki/criteria/streaming-and-multiroom.md` | Streaming & multiroom |
| 4 | `wiki/criteria/amplification-and-preouts.md` | Amplification & pre-outs |
| 5 | `wiki/criteria/connectivity.md` | Connectivity |
| 6 | `wiki/criteria/usability-and-support.md` | Usability, app & firmware support |
| 7 | `wiki/criteria/value-and-reliability.md` | Value, reliability & resale |

### Required `##` sections by kind

| Kind | Directory | Required sections |
|---|---|---|
| `hub` | criteria/ | Why this matters here · What good looks like · Systems and concepts · How the candidates rank · Open questions |
| `concept` | concepts/ | The mechanism · Why it matters for a 5.1 room · Common misconceptions · Sources |
| `system` | systems/ | What it does · Versions and tiers · Measured and observed results · Limits · Sources |
| `product` | products/ | Verdict · Specs that matter · Room correction · Streaming · Measurements · Known issues · Price and availability · Sources |
| `comparison` | comparisons/ | Question · Answer · Table · Sources |
| `decision` | decision/ | none checked; own shape |
| `reference` | reference/, start-here/, index.md | none checked; own shape |

Headers match as prefixes. Every body opens with a bold claim sentence.

### Word limits

| Kind | Floor–target |
|---|---|
| `hub` | 400–1,200 words |
| `product` | 300–1,200 words |
| `comparison` | 150–1,200 words |
| `decision` | 100–1,500 words |
| every other kind | 300–1,500 words |

Over target is `WORDS-HIGH`; over 2,000 is `WORDS-CEIL` and is two pages.
Under the floor is a merge candidate, never padded. `reference` pages have no floor.

### Staleness budgets

`last_verified` older than 60 days on `wiki/products/`, or
180 days anywhere else, is `STALE`. Prices, availability and successor
models move fastest.

### Pages exempt from a standard shape

- `wiki/index.md`
- `wiki/reference/bibliography.md`
- `wiki/reference/glossary.md`
- `wiki/reference/matrix.md`
- `wiki/reference/open-questions.md`
- `wiki/start-here/my-system.md`

Adding to this list is a decision recorded in `log.md`, never a way to silence a finding.

<!-- END GENERATED SCHEMA -->
