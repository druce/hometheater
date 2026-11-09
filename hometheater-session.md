# Home theater receiver research: session transcript

_Exported from Claude Code session df184a1b. User messages, assistant replies and your answers to questions; tool calls are listed by description only._


---

## You — 2026-11-08 21:57

i am in plan mode. my goal is to research a home theater receiver.  walk me through in detail how to create a wiki in a new ~/projects/hometheater directory using the karpathy methodology. ask questions and research as necessary.

- _tool: ToolSearch_ select:WebSearch,WebFetch
- _tool: WebSearch_ Karpathy LLM wiki gist raw wiki schema ingest query lint
- _tool: WebFetch_ https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

**Claude asked:**

- **How heavy should the hometheater wiki's machinery be? (governance_wiki has 8 lint/build scripts and 3 skills; Karpathy's gist is just raw/ + wiki/ + CLAUDE.md + index.md + log.md.)** Lean Karpathy (Recommended) / Lean + one lint script / Port governance machinery
- **What's the speaker setup the receiver must drive?** 5.1 / 5.2 / 5.1.2 or 5.1.4 Atmos / 7.x.4 or bigger / Not decided yet
- **Budget for the receiver alone?** Under $800 / $800–$2,000 / $2,000+ / Open
- **Which features matter most? (pick all)** Room correction / Music & streaming / Gaming / HDMI 2.1 / Upgrade path


> **Your answers:** Your questions have been answered: "How heavy should the hometheater wiki's machinery be? (governance_wiki has 8 lint/build scripts and 3 skills; Karpathy's gist is just raw/ + wiki/ + CLAUDE.md + index.md + log.md.)"="Port governance machinery", "What's the speaker setup the receiver must drive?"="5.1 / 5.2", "Budget for the receiver alone?"="Open", "Which features matter most? (pick all)"="Room correction,Music & streaming". You can now continue with these answers in mind.

- _tool: Bash_ Survey governance scripts, skills, and manifest format
- _tool: Write_ /Users/drucev/.claude/plans/i-am-in-plan-zippy-treehouse.md
- _tool: ToolSearch_ select:ExitPlanMode

<details><summary>Plan presented for approval</summary>

# Plan: `~/projects/hometheater` — an LLM wiki for choosing an AV receiver

## Context

Goal: pick an AV receiver for a **5.1/5.2** system, budget **open**, priorities **room correction** and **music & streaming**. Method: Karpathy's "LLM Wiki" gist (Apr 2026) — instead of re-asking an LLM over raw documents each time, the LLM incrementally *compiles* sources into a persistent, cross-linked markdown wiki that it maintains and the human reads.

Karpathy's three layers:
1. **Raw sources** — immutable, curated (spec sheets, manuals, reviews, measurements, forum threads). LLM reads, never edits.
2. **Wiki** — LLM-owned markdown: summaries, entity/concept pages, comparisons, synthesis. Plus `index.md` (catalog, read first on every query) and `log.md` (append-only, entries prefixed `## [YYYY-MM-DD] ingest | Title` so `grep "^## \[" log.md | tail` works).
3. **Schema** — `CLAUDE.md`, co-evolved, defining structure, conventions and workflows.

Operations: **ingest** (one source → summary page + updates to 10–15 related pages + index + log), **query** (answer from the wiki with citations; good answers get *filed back* as pages), **lint** (contradictions, stale claims, orphans, missing pages/links, gaps to fill by web search).

You chose to **port the governance_wiki machinery** on top of that. So the gist supplies the shape (raw/wiki/schema, index, log, file-back), and governance_wiki supplies the rigor (source manifest, verbatim extracts, regroup-by-page, primary-source verification, a linter, skills with hard stops, a checkpoint before writing). Scripts are adapted, not copied blind: their constants (kinds, sections, word limits, banned list) are governance-specific.

## Directory layout

```
~/projects/hometheater/
  CLAUDE.md            schema: purpose, my requirements, axes, page kinds, ground rules, workflows
  SCHEMA.md            page spec, tables generated from wiki_lint.py by gen_schema.py
  MANIFEST.md          page registry (path, title, kind, state, words, in/out links)
  log.md               Karpathy log: ingest | query | lint | decision entries (replaces BUILD-LOG.md)
  OPEN-QUESTIONS.md    build-side: claims needing verification + what would settle them
  raw/                 immutable sources (Karpathy name for governance's agents/). gitignored.
    manifest.txt       TITLE | FILENAME | AUTHOR | DATE | URL  [annotations]
    assets/            Obsidian attachment folder for clipped images
  extracts/            verbatim scratch, by-page/ bundles, verification-<round>.md. gitignored.
  wiki/
    index.md           map + reading paths ("just tell me what to buy" / "understand the tradeoffs")
    start-here/my-system.md     room size, speakers, sub(s), sources, listening habits, constraints
    criteria/          the spine: ~7 hub pages (see below), each with a "what good looks like" table
    concepts/          how things work: bass management, crossover, room modes, target curves,
                       Atmos/height (why 5.1 skips it), pre-outs, amp power ratings (FTC vs marketing)
    systems/           one page per *platform*: Audyssey MultEQ XT32, Dirac Live (+ Bass Control),
                       Anthem ARC Genesis, Yamaha YPAO, Sony DCAC; HEOS, MusicCast, BluOS,
                       Google Cast, AirPlay 2, Spotify Connect, Roon Ready
    products/          one page per receiver model (unlike governance's "never per vendor" rule —
                       here the product *is* the decision unit)
    comparisons/       filed-back query outputs: head-to-heads, shortlist tables
    decision/          shortlist.md, recommendation.md, buying-checklist.md, setup-and-calibration.md
    reference/         glossary.md, matrix.md (generated), bibliography.md, open-questions.md
  scripts/             ported tools (below)
  .claude/skills/      ht-research, ht-lint (ported)
```

### The spine: decision criteria (replaces 12 dimensions)

1. Room correction & bass management (top priority) 2. Music / two-channel performance 3. Streaming & multiroom (top priority) 4. Amplification & pre-outs 5. Connectivity (HDMI 2.1/eARC, phono, network) 6. Usability, app & firmware support 7. Value, reliability & resale.

Each criterion hub: claim → why it matters for *this* room → a "minimum / good / best" table (analog of Crawl/Walk/Run/Fly) → concepts and systems linked → products ranked on it, linked.

### Page kinds and required sections (encoded in `wiki_lint.py` constants)

| kind | dir | required sections |
|---|---|---|
| hub | criteria/ | Why this matters here · What good looks like · Systems & concepts · How the candidates rank · Open questions |
| concept | concepts/ | The mechanism · Why it matters for a 5.1 room · Common misconceptions · Sources |
| system | systems/ | What it does · Versions & tiers (incl. paid upgrades) · Measured/observed results · Limits · Sources |
| product | products/ | Verdict · Specs that matter · Room correction · Streaming · Measurements · Known issues · Price & availability · Sources |
| comparison | comparisons/ | Question · Answer · Table · Sources |
| decision | decision/ | exempt shape (checklists) |

Front matter: `title, slug, kind, criteria[], status (settled|contested|unverified), confidence, sources[], last_verified`; products add `brand, model, model_year, msrp_usd, street_usd, channels, room_correction, streaming[], preouts, successor_of`. Those product fields are what the generated matrix reads. Staleness: 60 days for `products/` (price/availability move fast), 180 elsewhere.

### Ground rules carried over from governance_wiki CLAUDE.md
- `raw/` read-only except `manifest.txt`; extracts never ship; no verbatim source text in `wiki/`.
- Do not invent specs, prices or measurements; conflicting sources are shown side by side (e.g. manufacturer watts vs. measured watts).
- Canonicalize: one concept per page; check MANIFEST.md first.
- A page earns existence (≥2 inbound links or >300 words), otherwise it's a section.
- Source hierarchy: manufacturer manuals/spec sheets & firmware notes → independent measurements (Audio Science Review, Audioholics, Sound & Vision bench tests) → room-correction vendors' own docs → established reviews → owner threads (AVS Forum) flagged as anecdote.
- Keep the voice rules short: answer first, calibrated confidence, no marketing adjectives. Skip governance's long rhythm contract and `restyle_check.py` — for a personal purchase wiki it's cost without payoff (can add later).

## Tooling to port (from `/Users/drucev/projects/governance_wiki/scripts/`)

| Script | Port as | Change |
|---|---|---|
| `source_manifest.py` | same | `agents/` → `raw/`, ignore `raw/assets/` |
| `regroup.py` | same | target dirs list |
| `wiki_lint.py` | same | rewrite constants: KINDS, SECTIONS, FM keys, LIMITS (product 300–1200), STALE_DAYS, BANNED (add "audiophile-grade", "immersive", "stunning"); drop RECIP/crosswalk checks, add "product page front matter complete" check |
| `linkcheck.py` | same | none beyond paths |
| `manifest_stats.py` | same | none |
| `gen_schema.py` | same | follows new constants |
| `gen_crosswalk.py` | `gen_matrix.py` | builds `reference/matrix.md`: product × criteria table from product front matter, plus criterion → products links from backlinks |
| `restyle_check.py` | not ported | |

Skills (from `.claude/skills/`): `wiki-research` → **`ht-research`** (detect → survey → manifest → extract → regroup → triage → verify → **checkpoint** → write → close; add Karpathy's per-source ingest mode for single clipped articles), `wiki-lint` → **`ht-lint`** (measure → regenerate → `--fix` → judgment findings → report to `log.md`). Add a small **`ht-query`** skill: read `index.md` first, answer with citations, ask whether to file the answer into `comparisons/`, log it.

## Execution sequence (each step commits; checkpoints marked ⏸)

1. **Scaffold.** `mkdir ~/projects/hometheater`, `git init`, `.gitignore` (`raw/`, `extracts/`, `.DS_Store`, `.obsidian/workspace*`). Write `CLAUDE.md`, empty `MANIFEST.md`, `log.md` with first entry `## [2026-11-08] init | scaffold`. Port and adapt scripts; run `gen_schema.py`; `wiki_lint.py` clean on an empty wiki. Port the three skills. Commit `init: scaffold`.
2. **Capture requirements.** Interview you for `start-here/my-system.md`: room dimensions/open plan, front/center/surround speakers (model, sensitivity, impedance), one or two subs, TV and sources, music sources (Spotify/Tidal/Qobuz/local/vinyl), whether Roon is used, multiroom wishes, preferred app ecosystem. ⏸ This drives what counts as "minimum/good/best."
3. **Seed sources.** You (Obsidian Web Clipper into `raw/`, or PDFs) and I (WebSearch/WebFetch, saved as markdown into `raw/`) gather: owner's manuals + spec sheets for the candidate set; ASR / Audioholics measurement reports; Dirac, Audyssey, ARC, YPAO docs; HEOS/MusicCast/BluOS feature docs; current street prices. Initial candidate set to *verify*, not assume (lineups turn over yearly and some may have successors by now): Denon AVR-X2800H/X3800H/X4800H, Marantz Cinema 70s/50, Yamaha RX-A4A/A6A (and successors), Onkyo TX-RZ30/RZ50, Pioneer VSX-LX805, Anthem MRX 540/740, Arcam AVR5, NAD T 758 V3, Sony STR-AN1000. Selection logic: 5.2 + room correction priority favors units with Dirac Live or ARC Genesis and independent dual-sub outputs; music priority favors good two-channel measurements and Roon Ready/BluOS/HEOS.
4. **Survey + manifest** (parallel subagents, one per source; Phase 0 discipline) → `raw/manifest.txt` rows. Commit.
5. **Plan** ⏸: page list with kind and home, merges, what's judged stale. Seed `MANIFEST.md` `state: planned`.
6. **Skeleton** ⏸: every page with front matter, claim line, headers; link graph resolves, no orphans.
7. **Extract** (parallel, one subagent per source, writes only `extracts/<slug>.md` in `→ page.md [tag] / "verbatim" (loc) / note:` grammar) → `regroup.py`.
8. **Verify**: every number (power, SNR/SINAD, price, firmware feature) checked against primary sources → `extracts/verification-r1.md`; dead ends to `OPEN-QUESTIONS.md`.
9. **Draft**: concepts + systems first, ⏸ calibration after first batch; then products; then criteria hubs, `index.md`.
10. **Query & file back**: run comparisons ("best room correction under $X for dual subs", "Dirac on Onkyo vs Denon upgrade", "does ARC Genesis justify Anthem's price") → `comparisons/`; produce `decision/shortlist.md` and `decision/recommendation.md`. ⏸ your decision.
11. **Lint & close**: `ht-lint`, `gen_matrix.py`, `manifest_stats.py`, log entry, commit.
12. **Afterwards**: `decision/setup-and-calibration.md` (mic placement, sub crossover, Dirac/ARC workflow); future rounds via `ht-research` when new reviews/firmware drop.

Viewing: open `~/projects/hometheater` as an Obsidian vault (graph view for orphans; set attachments to `raw/assets/`; optional Dataview over product front matter). Local git only, no remote, since `raw/` holds copyrighted material and nothing is published.

## Verification

- `python3 scripts/wiki_lint.py && python3 scripts/linkcheck.py --quiet` exit 0 after each step from 1 on.
- `python3 scripts/source_manifest.py` shows no NEW/UNEXTRACTED rows before drafting.
- `git show --stat` after every commit.
- Spot-check: pick three numbers on product pages and trace each to its `raw/` source via the extract bundle.
- `grep "^## \[" log.md` shows every ingest/query/lint as a parsable entry.
- `reference/matrix.md` regenerates with no em-dash holes (every product has complete front matter).


</details>

- _tool: update_plan_ 
- _tool: Bash_ Read the governance linter source
- _tool: Bash_ Read remaining governance scripts to port
- _tool: Bash_ Read the research and lint skills
- _tool: update_plan_ 
- _tool: Bash_ Create hometheater scaffold, git repo, gitignore, manifest

### Claude — 2026-11-08 22:13

Now adapting the copied scripts (raw/ instead of agents/, no README page).

- _tool: Bash_ Adapt copied scripts for raw/ and no README
- _tool: Write_ /Users/drucev/projects/hometheater/scripts/wiki_lint.py
- _tool: Write_ /Users/drucev/projects/hometheater/scripts/gen_schema.py
- _tool: Write_ /Users/drucev/projects/hometheater/scripts/gen_matrix.py

### Claude — 2026-11-08 22:14

I left a garbled line in `gen_matrix.py`; fixing it.

- _tool: Edit_ /Users/drucev/projects/hometheater/scripts/gen_matrix.py
- _tool: update_plan_ 

### Claude — 2026-11-08 22:14

Now the schema file (CLAUDE.md) and the registry files.

- _tool: Write_ /Users/drucev/projects/hometheater/CLAUDE.md
- _tool: Bash_ Write registry files, index, and run all scripts

### Claude — 2026-11-08 22:15

Everything is clean on an empty wiki. Next I'll smoke-test the linter and matrix generator on a throwaway copy with a fake product page, so I know the new checks actually fire.

- _tool: Bash_ Smoke-test linter and matrix on a scratch copy

### Claude — 2026-11-08 22:16

Every new check fires as intended. One fix: a missing key is also being reported as "unknown", so it shows up twice.

- _tool: Edit_ /Users/drucev/projects/hometheater/scripts/wiki_lint.py
- _tool: Write_ /Users/drucev/projects/hometheater/.claude/skills/ht-research/SKILL.md
- _tool: Write_ /Users/drucev/projects/hometheater/.claude/skills/ht-research/references/round-protocol.md
- _tool: Write_ /Users/drucev/projects/hometheater/.claude/skills/ht-lint/SKILL.md
- _tool: Write_ /Users/drucev/projects/hometheater/.claude/skills/ht-query/SKILL.md
- _tool: update_plan_ 
- _tool: Bash_ Run gates and commit the scaffold

### Claude — 2026-11-08 22:17

That removal wasn't needed (the folder is empty and gitignored), so I'll drop it and commit.

- _tool: Bash_ Run gates and commit the scaffold

### Claude — 2026-11-08 22:17

Scaffold committed. Now step 2 of the plan: the requirements interview for `my-system.md`.

- _tool: update_plan_ 

**Claude asked:**

- **For my-system.md: how many subwoofers, and do you already own them? (Room correction that handles two subs independently, like Dirac Bass Control, ARC Genesis, or Audyssey's independent sub outputs, is one of the biggest differences between candidates.)** One sub / Two subs, owned / Plan to add a second / No sub yet
- **Where does your music come from? (pick all) This decides which streaming platforms count as 'native' versus 'via phone'.** Spotify / Apple Music / Tidal / Qobuz hi-res / Roon or local library / Vinyl
- **What are the room and speakers like? Rough size, open-plan or closed, and the speaker models if you know them. (Speaker sensitivity and impedance decide whether the receiver's amps are enough.)** Small closed room / Medium room / Large or open-plan
- **Do you want music in other rooms, through a second zone or a multiroom ecosystem?** No, one room only / Yes, wireless speakers / Yes, a wired Zone 2


> **Your answers:** The user answered: "For my-system.md: how many subwoofers, and do you already own them? (Room correction that handles two subs independently, like Dirac Bass Control, ARC Genesis, or Audyssey's independent sub outputs, is one of the biggest differences between candidates.)"="No sub yet", "Where does your music come from? (pick all) This decides which streaming platforms count as 'native' versus 'via phone'."="radio paradise FLAC https://radioparadise.com/listen/stream-links,Spotify / Apple Music", "What are the room and speakers like? Rough size, open-plan or closed, and the speaker models if you know them. (Speaker sensitivity and impedance decide whether the receiver's amps are enough.)"="Small closed room", "Do you want music in other rooms, through a second zone or a multiroom ecosystem?"="today one room only.  future 2 additional rooms with stereo speakers, kitchen and bathroom with e.g. a wireless speaker each.". Read the answers carefully — they may request clarification, changes, or that you not proceed — and follow what they actually say.


### Claude — 2026-11-08 22:20

Radio Paradise FLAC is the specific requirement here, so I'll check what that stream actually is before writing it down.

- _tool: WebFetch_ https://radioparadise.com/listen/stream-links
- _tool: WebSearch_ Radio Paradise FLAC stream URL lossless supported devices BluOS Roon HEOS MusicCast
- _tool: Write_ /Users/drucev/projects/hometheater/wiki/start-here/my-system.md
- _tool: Bash_ Link requirements page, update registry and log, commit

> _Recap:_ ~/projects/hometheater is set up and committed: the three-layer Karpathy layout, seven ported scripts, the ht-research/ht-lint/ht-query skills, and a requirements page. Both gates pass. The one remaining lint finding, the requirements page having a single inbound link, is expected and logged. raw/ is still empty.
>
> _Asked:_ Should I start gathering sources into raw/ for the candidate receivers?


### Claude — 2026-11-08 22:21

I've set up `~/projects/hometheater` and made two commits. The linter and link check both pass, and every new lint check flagged a deliberately broken test page in a throwaway copy.

## How the method maps onto the repo

Karpathy's "LLM Wiki" gist has three layers. You add sources, the LLM compiles them once into linked pages, and later questions are answered from those pages instead of the raw documents.

| Layer | In the repo | Rule |
|---|---|---|
| **Sources** | `raw/`, registered in `raw/manifest.txt` | Never edited. Gitignored for copyright. Images go in `raw/assets/`. |
| **Wiki** | `wiki/` | Written and maintained by the LLM; you read it. |
| **Schema** | `CLAUDE.md` | Structure, conventions and workflows. You and the LLM change it together. |

Two files from the gist navigate it. `wiki/index.md` lists every page and is read first on every question. `log.md` is append-only, with headers like `## [2026-11-08] ingest | …` that grep can parse.

The three operations are skills in `.claude/skills/`:
- **Ingest (`ht-research`):** sources go through detect → survey → manifest → verbatim extracts → regroup by page → triage → verify against primary sources. It then **stops for your approval** before writing. A single clipped article can take a lighter path.
- **Query (`ht-query`):** answers start from `index.md` and your requirements, with citations. Answers worth keeping get saved as `comparisons/` pages, after asking you.
- **Lint (`ht-lint`):** the scripted checks, plus the ones a script can't do: contradictions between pages, stale prices, models replaced by a successor.

From governance_wiki I adapted seven scripts. The linter now checks product spec completeness (unknowns stay `?`, never guessed), flags products no criterion page ranks, gives product pages a 60-day staleness limit, and bans marketing adjectives. `gen_matrix.py` replaces the crosswalk generator: it builds a product-by-spec table plus a criterion ranking, and reports every gap instead of leaving it blank. I didn't port `restyle_check.py`.

The wiki is organised around seven criteria instead of governance_wiki's twelve dimensions, with room correction and streaming weighted highest. Room-correction and streaming platforms get their own pages, separate from product pages.

## Your requirements

These are in `wiki/start-here/my-system.md`: 5.1, small closed room, no sub yet (choosing one is in scope), Spotify, Apple Music and **Radio Paradise FLAC**, and four more rooms later.

Radio Paradise FLAC turns out to separate the candidates. These are first-pass findings, not yet checked against primary sources:
- **BluOS:** reported as carrying the lossless stream natively, as Sonos does.
- **HEOS (Denon, Marantz):** goes through TuneIn, which reportedly doesn't carry the FLAC stream.
- **Roon:** owners have reported it falling back to AAC.
- **MusicCast and the others:** nothing found yet.

That would favour NAD's BluOS receivers or an external streamer, but it's logged as unverified.

**Decision for you:** must the FLAC stream play natively on the receiver, or is a small external streamer acceptable? If an external streamer is fine, the receiver can be chosen on room correction alone.

## What happens next
1. **Gather sources:** manuals, bench measurements, Dirac/Audyssey/ARC documentation, platform service lists, prices. You can also clip pages straight into `raw/` with Obsidian Web Clipper.
2. **Page-list checkpoint**, then **skeleton checkpoint**: I stop at each for your OK.
3. Extract, verify, draft (with a voice check after the first batch), compare, then the shortlist and recommendation.

When you have them, I still need your speaker models and room dimensions.

Sources:
- [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [stereonet: great-sounding internet radio stations](https://stereonet.com/forums/topic/516085-great-sounding-internet-radio-stations)
- [eCoustics: interview with Radio Paradise's William Goldsmith](https://www.ecoustics.com/podcasts/radio-paradise-william-goldsmith/)
- [Roon community: Radio Paradise FLAC link producing an AAC stream](https://community.roonlabs.com/t/radio-paradise-flac-link-producing-limited-aac-stream-of-approx-350kbps/314664)
- [zby: Karpathy LLM Wiki ingest summary](https://zby.github.io/commonplace/sources/karpathy-llm-wiki.ingest/)


---

## You — 2026-11-08 22:52

Yes, gather sources

- _tool: update_plan_ 
- _tool: Bash_ Check which capture tools are installed
- _tool: update_plan_ 
- _tool: Agent_ Gather Denon/Marantz/HEOS sources
- _tool: Agent_ Gather Yamaha/Sony/Onkyo sources
- _tool: Agent_ Gather Anthem/NAD/Arcam/BluOS/Dirac sources
- _tool: Agent_ Gather independent measurements and reviews

### Claude — 2026-11-08 22:54

The four research agents are running in the background and saving sources into `raw/`:

1. **Denon and Marantz:** current lineups and successor models, Audyssey, the paid Dirac upgrade, and HEOS support for Radio Paradise FLAC.
2. **Yamaha, Sony, Onkyo and Pioneer:** YPAO, Sony's DCAC, the Dirac version built into Onkyo/Pioneer, and support for Radio Paradise FLAC on Yamaha's MusicCast and on Onkyo/Pioneer.
3. **Premium tier and platforms:** Anthem (ARC Genesis), NAD (BluOS), Arcam, Dirac Live and Bass Control, and Radio Paradise's own stream and device pages.
4. **Independent measurements:** Audio Science Review, Audioholics, Sound & Vision and Stereophile bench tests, room-correction comparisons, and owner reliability threads (marked as anecdote).

When they report back, I'll check the captures (bot-blocked pages, PDFs that didn't download properly), write the `raw/manifest.txt` rows myself so it isn't written in parallel, and run `source_manifest.py`. Then I'll bring you the current candidate list, with any models that now have successors flagged, and what the sources say about Radio Paradise FLAC.


### Claude — 2026-11-08 23:02

The Denon/Marantz agent has finished and saved 24 files. Three findings so far, all from manufacturer or Dirac pages:

- **Several models have successors.** Denon's AVR-X3900H and X2900H launched in May 2026 at $1,849 and $1,349. Marantz announced CINEMA Series 2 in August 2026, and the Series 2 CINEMA 70s is down to 50 W with the lower-tier Audyssey (MultEQ XT rather than XT32). HARMAN, which Samsung owns, has owned Denon and Marantz since September 2025.
- **Dirac is a paid add-on on these models, not built in.** On the X3900H it costs $259 to $799 depending on tier. Only the higher models can take Bass Control.
- **Radio Paradise FLAC doesn't play natively on HEOS.** Radio Paradise isn't in the HEOS service list, and the X3900H's internet radio only plays MP3, AAC and WMA. Two lossless routes are possible but neither is confirmed for Radio Paradise: its iOS app over AirPlay, or Roon.

The other three agents are still running. I'll hold this agent's manifest rows and write `raw/manifest.txt` in one pass once all four have reported.


### Claude — 2026-11-08 23:04

The Yamaha/Sony/Onkyo agent has finished too. In short:

- **Yamaha** has no new AVENTAGE models, so the RX-A4A, A6A and A8A are still current.
- **Onkyo** keeps Dirac built in at full bandwidth on the RZ50 and charges $299 for Bass Control. Gentex now owns Onkyo.
- **Pioneer** home AV in the US appears to be winding down.
- **Radio Paradise FLAC** has no confirmed native route on MusicCast or Onkyo.

Three issues from this batch:

- **One file may have been overwritten.** Both agents saved `radioparadise-ways-to-listen.md` and `radioparadise-stream-links.md` under the same names, so the second write may have replaced the first. I'll check the files when I write the manifest.
- **The FLAC stream URL wasn't captured.** The Radio Paradise stream-links page saved with the default AAC 128 link, so the FLAC address is still missing.
- **Leftover browser files in your governance_wiki checkout.** The browser tool left its own snapshot and console logs in `governance_wiki/.playwright-mcp/`. They're untracked, but I haven't deleted them.

Two agents are still running: the premium tier and platforms, and the independent measurements.


### Claude — 2026-11-08 23:06

The measurements agent has finished. The biggest finding: on independent bench tests from Audio Science Review (ASR), **the Onkyo/Pioneer family measures badly.** On the RZ50, RZ30 and LX505, the amps drop into a low-power mode under load and only recover when the unit is unplugged. The LX505 still does this on February 2026 firmware. That weighs heavily against the one brand that includes Dirac at no extra cost.

The Denon AVR-X3900H measures well (ASR SINAD 102, recommended). The Marantz Cinema 70s showed a distortion fault at 4 Ω. The NAD T758 V3 measured worst of the candidates, although the current V3i hasn't been tested.

There's no controlled comparison of Dirac, Audyssey, Anthem's ARC and Yamaha's YPAO in the same room, so the room-correction ranking will rest on weaker evidence. The Anthem MRX 540, Yamaha RX-A4A, Arcam, Sony and NAD V3i have no independent measurements either.

The premium tier and platforms agent (Anthem, NAD, Arcam, Dirac, BluOS) is still running. Once it reports I'll write all the manifest rows.


### Claude — 2026-11-08 23:11

All four agents are done. Next I'll sanity-check the captures and write the manifest.

- _tool: update_plan_ 
- _tool: Bash_ List raw captures with type, size, bot-wall check

### Claude — 2026-11-08 23:11

The bot-wall grep flagged every ASR capture. That's likely just the forum's normal footer text, but I'll confirm, and also check that the tiny files have real content.

- _tool: Bash_ Confirm ASR captures and small files are real content

### Claude — 2026-11-08 23:11

The X3900H review capture contains no "SINAD" text at all, so I'll check what's actually in it.

- _tool: Bash_ Inspect ASR capture content quality
- _tool: Bash_ Append batch 1 manifest rows and diff against raw/

### Claude — 2026-11-08 23:12

81 files and 81 manifest rows, with nothing new or missing. All 81 show as unextracted, which is expected: extraction comes after the page-list checkpoint. Now the log entry and open questions.

- _tool: update_plan_ 
- _tool: Bash_ Log batch, add open questions, commit, check governance repo

> _Recap:_ 81 sources are saved in raw/ and registered in raw/manifest.txt, with nothing new or missing. The log entry and five new open questions are committed. raw/ itself is gitignored by design. No extraction or wiki pages exist yet; the page-list plan comes next and stops for your approval.
>
> _Asked:_ Should I draft the page-list plan from these 81 sources?


### Claude — 2026-11-08 23:13

I gathered and registered 81 sources in `raw/`. `source_manifest.py` shows 81 files and 81 rows, with nothing new or missing. The log entry and new open questions are committed; `raw/` itself stays gitignored. Everything below is from what the agents captured and hasn't been checked against primary sources yet; that happens in the verification step.

## What the sources change

**The candidate list has moved on:**
- **Denon:** AVR-X3900H ($1,849) and X2900H ($1,349), launched May 2026, replace the X3800H and X2800H.
- **Marantz:** CINEMA Series 2 (August 2026). The 70s S2 is 50 W with MultEQ XT, and the 50 S2 ($3,000) has XT32.
- **Arcam:** the Radia AVA15/25/35 replace the AVR5/11, starting at $4,499.
- **Yamaha:** no new AVENTAGE models, so the RX-A4A, A6A and A8A are still current.
- **Onkyo:** the RZ30, RZ50 and RZ70 are current, with the next generation teased for 2027.
- **Pioneer:** its US home AV business appears to be winding down.
- **Anthem:** the MRX 540/740/1140 8K are current. NAD's T 758 V3i ($2,299) is current.
- **Ownership:** HARMAN (Samsung) owns Denon, Marantz, HEOS and Arcam. Gentex owns Onkyo.

**Room correction:**
- **Dirac:** a paid add-on on Denon and Marantz ($259 to $799 depending on tier). It's built in at full bandwidth on Onkyo, with Bass Control at $299. NAD can't get Bass Control or ART at all.
- **Comparisons:** no controlled, same-room comparison of Dirac, Audyssey, Anthem's ARC and Yamaha's YPAO was found. Ethan Winer's Dirac measurements show improvement at the main seat that breaks down 1 to 2 ft away.

**Measurements (Audio Science Review):**
- **Onkyo/Pioneer:** the RZ50, RZ30 and Pioneer LX505 all drop into a low-power mode under load. Only unplugging the unit restores full power, and the LX505 still does this on February 2026 firmware. That is a serious mark against the one family with Dirac built in.
- **Denon X3900H:** SINAD 102 and recommended. ASR's one complaint is that setup forces you to create a HEOS account.
- **No independent measurements:** RX-A4A, MRX 540, the Arcam AVA models, Sony, NAD V3i, Marantz Series 2 and Denon X2900H.

**Radio Paradise FLAC:**
- **BluOS:** native, according to both Radio Paradise's and BluOS's own pages (Sonos also has a native service). BluOS also added native Apple Music on 20 October 2026, which fits your future multiroom rooms.
- **HEOS:** its internet radio plays only MP3, AAC and WMA, so no FLAC.
- **MusicCast and Onkyo:** no documented native route.
- **Possible workarounds:** Roon, or Radio Paradise's iOS app sending ALAC over AirPlay. Neither is tested, so both are logged as open questions.

## Capture defects
- **Rendered text, not page source:** Dirac, BluOS support, Sony, Audioholics and Radio Paradise blocked direct download, so they were saved as rendered browser text. Each file's header says how it was captured.
- **Overwritten files:** two agents saved the same Radio Paradise filenames. The lost URL table was re-saved as its own file.
- **ASR files:** they carry a lot of leftover forum HTML, and most of the numbers are in chart images. The ASR database capture has the SINAD figures as text.

The one remaining lint finding is the requirements page having a single inbound link, which is expected and logged.

The next step is the page-list plan, and it stops for your approval before anything is written to `wiki/`. Your answer on whether Radio Paradise FLAC must be native or can come through an external streamer will shape the shortlist. It decides between a BluOS receiver (NAD) and a strong-measuring receiver like the X3900H plus a $499 Bluesound NODE NANO.


---

## You — 2026-11-08 23:20

Yes, draft the plan

- _tool: update_plan_ 
- _tool: Bash_ Check which Denon/Marantz models are still listed
- _tool: Bash_ Extract model names and prices from lineup pages

### Claude — 2026-11-08 23:21

I have current US list prices for Denon and Marantz now, so I can write the plan.

- _tool: update_plan_ 
- _tool: Write_ /Users/drucev/projects/hometheater/plans/round-1-page-plan.md
- _tool: update_plan_ 

**Claude asked:**

- **You don't own a subwoofer yet, and the sub choice interacts with the receiver choice (one sub or two, and whether Dirac's Bass Control matters). How should the wiki handle subwoofers?** Later round (Recommended) / Concept page only / Separate wiki
- **Must Radio Paradise FLAC play natively on the receiver, or is an external streamer acceptable (a Bluesound NODE NANO is $499)?** External streamer OK / Native preferred / Native required
- **Approve the 11 product pages (Denon X3900H, X3800H, X2900H; Marantz CINEMA 70s S2, 50 S2, 50; Yamaha RX-A4A; Onkyo TX-RZ50; Anthem MRX 540; NAD T 758 V3i; Arcam AVA15)?** Approve as listed / Add Sony STR-AN1000 / Trim the list


> **Your answers:** The user answered: "You don't own a subwoofer yet, and the sub choice interacts with the receiver choice (one sub or two, and whether Dirac's Bass Control matters). How should the wiki handle subwoofers?"="assume 1 subwoofer", "Must Radio Paradise FLAC play natively on the receiver, or is an external streamer acceptable (a Bluesound NODE NANO is $499)?"="External streamer OK", "Approve the 11 product pages (Denon X3900H, X3800H, X2900H; Marantz CINEMA 70s S2, 50 S2, 50; Yamaha RX-A4A; Onkyo TX-RZ50; Anthem MRX 540; NAD T 758 V3i; Arcam AVA15)?"="Approve as listed". Read the answers carefully — they may request clarification, changes, or that you not proceed — and follow what they actually say.


---

## You — 2026-11-08 23:23

consider wiim ultra amp


### Claude — 2026-11-08 23:23

I'll look up the WiiM Amp Ultra before deciding where it goes, since it could be either a Radio Paradise streamer or an amp for the future rooms.

- _tool: WebSearch_ WiiM Amp Ultra specifications price room correction subwoofer output HDMI eARC
- _tool: WebSearch_ WiiM Radio Paradise FLAC lossless custom radio URL WiiM Home app
- _tool: update_plan_ 
- _tool: Bash_ Fold answers and WiiM Amp Ultra into the plan
- _tool: update_plan_ 

**Claude asked:**

- **The WiiM Amp Ultra is a stereo streaming amp with one sub out and RoomFit room correction, so at most 2.1 and not a 5.1 receiver. What role should it play in the wiki?** Future stereo rooms / Main-room 2.1 option / RP FLAC streamer


> **Your answers:** Your questions have been answered: "The WiiM Amp Ultra is a stereo streaming amp with one sub out and RoomFit room correction, so at most 2.1 and not a 5.1 receiver. What role should it play in the wiki?"="Future stereo rooms,RP FLAC streamer". You can now continue with these answers in mind.

- _tool: Bash_ Record WiiM role in plan, log, commit

> _Recap:_ The round 1 page plan now has 45 pages and is committed, along with your decisions: one sub, an external streamer is fine for Radio Paradise FLAC, the 11 receivers approved, and WiiM added for the stereo rooms and as a streamer. Nothing has been written to wiki/ yet. WiiM's official pages still need capturing.
>
> _Asked:_ Should I capture the WiiM sources, then build the skeleton?


### Claude — 2026-11-08 23:25

I've added the WiiM to the plan, so it's now 45 pages. The full plan is in [plans/round-1-page-plan.md](../hometheater/plans/round-1-page-plan.md) and is committed; nothing is written to `wiki/` yet.

**The WiiM Amp Ultra is a stereo streaming amp, not a surround receiver.** Retailers list it at 100 W per channel into 8 Ω, with one sub output, WiiM's RoomFit room correction and HDMI ARC (eARC is unconfirmed). They give it as about £499 in the UK; a comparison site puts it at about $549 in the US. Given your answer, it has two roles:

- **The two future stereo rooms:** it gets its own product page, ranked only on the streaming and multiroom hub. It isn't compared against the 5.1 receivers.
- **External Radio Paradise streamer:** a new WiiM platform page covers the Ultra, Pro Plus and Mini streamers as candidates to feed the main receiver, next to the Bluesound NODE.

WiiM owners report that its built-in Radio Paradise option plays lossless FLAC, and you can also add the FLAC stream by URL, though that loses the track title. These are forum reports, marked as anecdote until WiiM's own pages confirm them.

**How your other answers shaped the plan:**
- **One subwoofer:** I dropped the multiple-subwoofers concept page. What a second sub would add becomes a short section of the bass-management page, and Dirac's Bass Control is judged for one sub only.
- **External streamer acceptable:** NAD's built-in BluOS is a convenience rather than a requirement. Receivers are ranked on room correction and music performance, and Radio Paradise FLAC can come from the streamer.
- **New multiroom criterion:** whether one app (WiiM Home or BluOS) can run the main-room streamer, the stereo rooms, and the kitchen and bathroom speakers is now part of the streaming criterion.

**Before the skeleton is built:** I need WiiM's official pages (Amp Ultra specs and manual, RoomFit, the service list, the streamer specs) and any independent measurement of the Amp Ultra. Audio Science Review has reviewed earlier WiiM amps. After that I'll create all 45 pages with front matter, claim lines, section headers and links. That is the second checkpoint.

Sources:
- [audiovolt: WiiM Amp Ultra](https://www.audiovolt.co.uk/products/wiim-amp-ultra-network-streaming-amplifier)
- [speakerdecision: WiiM Amp vs WiiM Amp Ultra](https://speakerdecision.com/compare-amps/WiiM-Amp-vs-WiiM-Amp-Ultra)
- [Smart Home Sounds: WiiM Amp Ultra](https://www.smarthomesounds.co.uk/wiim-amp-ultra)
- [hifimart: WiiM Amp Ultra](https://hifimart.com/product/wiim-amp-ultra/)
- [WiiM forum: Radio Paradise lossless FLAC](https://forum.wiimhome.com/threads/radio-paradise-losless-flac.8399/)
- [WiiM forum: WiiM Ultra and Radio Paradise](https://forum.wiimhome.com/threads/wiim-ultra-radio-paradise.4762/)
- [WiiM forum: URL FLAC streams not showing artist and title](https://forum.wiimhome.com/threads/wiim-app-not-showing-artist-and-song-title-for-url-flac-streams.3240)
- [MinimServer forum: Radio Paradise FLAC URL](https://forum.minimserver.com/showthread.php?tid=5172)


---

## You — 2026-11-08 23:26

Yes, go ahead

- _tool: update_plan_ 
- _tool: Agent_ Capture WiiM sources

### Claude — 2026-11-08 23:26

While WiiM capture runs, I'll do the corrections first, in their own commit as the protocol requires.

- _tool: update_plan_ 
- _tool: Write_ /Users/drucev/projects/hometheater/wiki/start-here/my-system.md
- _tool: Bash_ Correct CLAUDE.md layout, log, commit corrections

### Claude — 2026-11-08 23:27

Corrections are committed. Next I'll seed the manifest and generate the 45-page skeleton from one spec file, so the link graph is consistent by construction.

- _tool: update_plan_ 
- _tool: Write_ /private/tmp/claude-501/-Users-drucev--claude-spares-spare-j1GWM6/df184a1b-8efd-485e-a668-381a49af473d/scratchpad/gen/skeleton.py
- _tool: Bash_ Generate skeleton, refresh stats and matrix, run gates
- _tool: Bash_ Spot-check a product page and a hub
- _tool: Bash_ Log and commit the skeleton
- _tool: update_plan_ 

### Claude — 2026-11-08 23:29

The skeleton is built and committed, but I haven't stopped at checkpoint 2 yet: the WiiM capture agent is still running, and its sources need to go into `raw/manifest.txt` first.

What's in place in `~/projects/hometheater`:
- **Corrections, in their own commit:** `my-system.md` now cites primary sources for Radio Paradise and records your decisions: one sub, an external streamer is fine, and WiiM for the stereo rooms and as the streamer. `CLAUDE.md`'s layout is updated to match.
- **Skeleton, 45 pages:** every page has front matter, a draft claim, section headers each with a one-line note on what it will argue, and its links. It covers 7 criteria pages, 5 concepts, 10 platform pages, 12 products, 2 seed comparisons, 3 decision pages, 4 reference pages, the requirements page and the index.
- **Gates:** the link check is clean: no broken links, no orphan pages, everything within three clicks of the index, and every product ranked by at least one criteria page. The linter's 51 findings are all expected at this stage and logged: 39 pages under their word floor because there's no prose yet, and 12 product pages whose specs stay `?` until verified.

The draft claims reuse survey numbers, such as the X3900H's ASR SINAD of 102. They stay marked unverified until the verification step.

When the WiiM agent reports, I'll check its captures, add them to the manifest, and then stop at checkpoint 2. That's the last cheap point to restructure before extraction starts.


### Claude — 2026-11-08 23:35

The WiiM agent found something that matters: according to WiiM's own pages, **the Amp Ultra and the WiiM Ultra don't support AirPlay 2**, and neither has native Apple Music. That conflicts with your Apple Music requirement for the stereo rooms. It also makes two draft claims wrong: the streaming-protocols page says every candidate supports AirPlay 2, and the WiiM page names the Ultra as the streamer. I'll register the sources and correct those two claims.

- _tool: Bash_ Register WiiM sources, correct claims, log, commit
- _tool: update_plan_ 

> _Recap:_ The 45-page skeleton is committed with a clean link graph, and 94 sources are registered. WiiM's pages show the Amp Ultra and Ultra lack AirPlay 2 and native Apple Music; the two affected draft claims are corrected. Extraction hasn't started; this is checkpoint 2.
>
> _Asked:_ Approve the skeleton and start extraction?


### Claude — 2026-11-08 23:35

I've reached checkpoint 2. The 45-page skeleton is committed with a clean link graph, and 94 sources are registered, 13 of them WiiM's.

**The WiiM pages changed the picture:**
- **No AirPlay 2 on the Amp Ultra or the WiiM Ultra.** Neither has native Apple Music either, which conflicts with your Apple Music requirement for the stereo rooms. The cheaper Mini ($99), Pro ($169) and Pro Plus ($219) do have AirPlay 2. I corrected the two draft claims that had this wrong: the streaming-protocols page and the WiiM page.
- **Radio Paradise:** WiiM's own help pages list it as a built-in service only in the PC app. Lossless playback in the phone app is reported only by owners on the WiiM forum. One owner says casting from the Radio Paradise app over Google Cast is lossless when FLAC is selected there.
- **Amp Ultra:** $549, HDMI ARC only (no eARC), no DTS, and a 2 V sub output. ASR recommends it: about 97 W per channel into 8 Ω and 168 W into 4 Ω with both channels driven, and SINAD about 99.9 dB from optical at 5 W.
- **WiiM Ultra streamer:** $349. ASR measured its line out at about 115 dB SINAD.
- **WiiM Sound speaker:** listed as "Coming Soon", with no price and no water rating found.

**An Apple Music decision is coming up.** The options are a WiiM Pro Plus as the external streamer (it has both AirPlay 2 and digital outputs), or BluOS, which has had native Apple Music since 20 October 2026. This doesn't block extraction; it affects the drafting.

**Things in the skeleton you might want to change before extraction:**
- Six product pages are Denon or Marantz.
- Separate pages for HEOS and MusicCast.
- WiiM covered as both a platform page and the Amp Ultra product page.

After extraction starts, restructuring means redoing extracts.

**If you approve:** one subagent per source writes verbatim extracts into `extracts/` only, then `regroup.py` bundles them by page. After that comes verification against primary sources, and then drafting, starting with the concept and platform pages, with a voice check after the first batch.


---

## You — 2026-11-08 23:41

Approve, extract

- _tool: update_plan_ 
- _tool: Bash_ Get page list and source count for briefs
- _tool: Write_ /private/tmp/claude-501/-Users-drucev--claude-spares-spare-j1GWM6/df184a1b-8efd-485e-a668-381a49af473d/scratchpad/extract-brief.md
- _tool: Agent_ Extract group 1: Denon pages
- _tool: Agent_ Extract group 2: Denon manual, Audyssey
- _tool: Agent_ Extract group 3: Marantz
- _tool: Agent_ Extract group 4: Dirac
- _tool: Agent_ Extract group 5: Yamaha
- _tool: Agent_ Extract group 6: Onkyo/Pioneer
- _tool: Agent_ Extract group 7: Anthem/NAD/Arcam
- _tool: Agent_ Extract group 8: BluOS/Radio Paradise
- _tool: Agent_ Extract group 9: WiiM products, Sony
- _tool: Agent_ Extract group 10: ASR Denon/Marantz
- _tool: Agent_ Extract group 11: ASR other brands
- _tool: Agent_ Extract group 12: other measurements

### Claude — 2026-11-08 23:43

Twelve extraction agents are running in the background over the 94 sources. They're grouped by brand and source type:

1. Denon pages
2. Denon manual and Audyssey
3. Marantz
4. Dirac
5. Yamaha
6. Onkyo/Pioneer
7. Anthem, NAD and Arcam
8. BluOS and Radio Paradise
9. WiiM and Sony
10. ASR reviews of Denon and Marantz
11. ASR reviews of the other brands
12. Audioholics, Sound & Vision, Winer and AVS

Each agent writes only `extracts/<source>.md`, one file per source. The format is the arrow grammar: target page, verbatim quote with location, note. Material about sibling models without their own page is tagged as a proxy, for example the Pioneer LX505 standing in for the RZ50, or the MRX 1140 for the MRX 540. They're on Sonnet to keep the cost of 94 careful reads down.

Each agent reports a one-line summary per source. When they're all back, I'll collect those into `extracts/extractor-reports.md` myself so no two agents write the same file, then run `regroup.py`. After that I'll go through the empty bundles, the `NO-HOME` entries and any unknown targets.


### Claude — 2026-11-08 23:44

The Dirac group is done. I'll keep each report's per-source lines in a scratch file as they arrive, so they can be merged into `extractor-reports.md` once everything is in.

- _tool: Bash_ Save group 4 report lines to scratch

### Claude — 2026-11-08 23:44

Dirac extraction is done (1 of 12): 91 entries across 9 sources. The key extracted finding is that Dirac's price depends on which device the store page is showing. On the X3900H, full-range Room Correction is $349. Bass Control is a separate $299, and ART requires Bass Control whenever a sub is in use. The other 11 groups are still running.

- _tool: Bash_ Save group 8 report lines to scratch

### Claude — 2026-11-08 23:45

2 of 12 extraction groups are done. The BluOS and Radio Paradise group wrote 111 entries across 11 sources.

The most useful finding: BluOS says Radio Paradise's MQA stream is decoded only inside the BluOS player and can't be passed to an external DAC. So a Bluesound NODE feeding the receiver over optical or coax may not deliver Radio Paradise at its best BluOS quality. No source says whether BluOS also offers plain FLAC. This weakens the NODE as a clean route to the receiver.

Plain FLAC stream URLs exist for every Radio Paradise channel, so any streamer that accepts a manual stream URL can play them losslessly.

The extracts also list the NODE at $849 and the Pulse Flex at $429. The Pulse Flex has no IP rating and lists humidity only as a storage condition, which makes it doubtful for the bathroom.

The remaining 10 groups are still running.

- _tool: Bash_ Save group 7 report lines to scratch

### Claude — 2026-11-08 23:46

3 of 12 extraction groups are done. The Anthem/NAD/Arcam group wrote 135 entries across 7 sources. Findings:

- **NAD T 758 V3i:** the included Dirac is a limited version, and the full version is an upgrade. The data sheet is a 2020 preliminary with 4K/60 HDMI and no HDMI 2.1.
- **Anthem MRX 540:** the spec sheet, dated 2022, gives only a headline "100W" with no conditions. It lists dual sub outputs only under the MRX 1140. The 540's manual is needed to settle its power rating and sub outputs.
- **Arcam AVA15:** the product page doesn't say which Dirac tier is included. Its power is rated at 0.5% THD with seven channels driven, so it can't be compared directly with the NAD's figures. It has the broadest built-in streaming of the three, and its coax input takes 192 kHz, which suits an external streamer.

Nine groups are still running.

- _tool: Bash_ Save group 1 report lines to scratch

### Claude — 2026-11-08 23:46

4 of 12 extraction groups are done. The Denon pages group wrote 100 entries across 8 sources.

For about $500 more, the X3900H gets you over the X2900H:
- Four independent sub outputs instead of two.
- 11.4 pre-outs instead of 2.2.
- Audyssey MultEQ XT32 instead of XT.
- Eligibility for the full Dirac suite instead of Room Correction only.

Every Denon power rating is for two channels driven at 8 Ω and 0.08% THD. The "70% of rated power to five channels" claim has no measurement behind it, so it needs checking against bench data.

Denon's own Dirac page still leaves out both 2026 models.

Eight groups are still running.

- _tool: Bash_ Save group 10 report lines to scratch

### Claude — 2026-11-08 23:46

Five of 12 extraction groups are done. The latest, the ASR Denon/Marantz group, wrote 168 entries across 7 sources.

- **Denon X3900H:** the only Denon that ASR recommends with no caveat, at SINAD 102. The X3800H's weaker score comes from its DAC and pre-out section; ASR describes its amplifier as unchanged.
- **Marantz CINEMA 70s (original version):** at 5 W into 4 Ω its distortion jumps after about two minutes of warm-up and stays high until the unit is power-cycled.
- **No five-channel power figures:** ASR's amplifier tests drive only two channels, so no source gives power with all five channels driven. That gap will be noted on the amplifier power ratings page.

Seven groups are still running.

- _tool: Bash_ Save group 3 report lines to scratch
- _tool: Bash_ Save group 12 report lines to scratch

### Claude — 2026-11-08 23:47

Seven of 12 groups are done.

- **Marantz:** Dirac is a paid add-on on both Series 2 models. The 70s S2 has one optical and one coax input and two sub outputs; the 50 S2 has two of each input and four independent sub outputs. Marantz's own Dirac page is out of date and lists only the Series 1 models.
- **Room correction, measured:** Winer found that at 2 ft from the measuring seat the correction's benefit was gone, and some bass frequencies came out worse than uncorrected.
- **Anthem:** the MRX 740 and 1140 pre-outs measure very well, but their amps run out of current into 4 Ω.
- **Yamaha:** on the RX-A6A, setting the speaker impedance switch to Low or turning on Eco mode cuts power sharply.
- **Reliability:** owners report Denon HDMI board repairs out of warranty costing $600–750.

Five groups are still running: Denon manual, Yamaha, Onkyo, WiiM/Sony, and ASR other brands.

- _tool: Bash_ Save group 6 report lines to scratch

### Claude — 2026-11-08 23:47

8 of 12 groups done. **Onkyo:** no firmware note addresses the power limiting ASR measured. The only amp-related change is a power-supply sequencing fix. Full-bandwidth Dirac is included on the RZ50. Bass Control costs extra, and its first firmware had a crossover bug that took about eight months to fix. The RZ50 platform dates from December 2020, with a successor expected in 2027.

Still running: the Denon manual, Yamaha, WiiM/Sony, and ASR reviews of the other brands.

- _tool: Bash_ Save group 2 report lines to scratch

### Claude — 2026-11-08 23:48

9 of 12 groups are done. The Denon X3900H manual group came back with 134 entries across 3 sources.

- **No FLAC over internet radio.** The X3900H's internet radio plays only MP3, WMA and AAC. That's the strongest manual-based case for an external Radio Paradise streamer.
- **USB powers, doesn't play.** The rear USB port supplies power only, so it could run a streamer but not take audio from one.
- **Coax and optical limits unknown.** The manual doesn't state the maximum sample rate for these inputs; it's now an open question.
- **Audyssey and Dirac can coexist.** They can be stored side by side in two speaker presets.
- **Sub on stereo music.** For the sub to play during stereo music with full-range fronts, the setting has to be "LFE + Main".
- **Spare amp channels for a second zone.** In a 5.1 setup, the four unused amp channels can power a stereo Zone 2, without room correction.
- **MultEQ-X support for the 2026 models is still undocumented.** The X3900H isn't on the MultEQ-X supported list, which was last updated May 2026.

Still running: Yamaha, WiiM/Sony, and ASR reviews of the other brands.

- _tool: Bash_ Save group 9 report lines to scratch
- _tool: Bash_ Save group 11 report lines to scratch

### Claude — 2026-11-08 23:50

Eleven of 12 groups are done. The two that just finished add three findings that change the plan:

- **The WiiM Amp Ultra can't feed a receiver.** It has no S/PDIF and no line output; its only outputs are speaker, sub and USB. Of WiiM's streamers, only the Pro ($169) and Pro Plus ($219) have both optical and coax outputs plus AirPlay 2.
- **Onkyo/Pioneer power limiting shows up across the platform.** ASR measured it on the RZ50, on the LX505 in 2023 and again in 2026, and on the RZ30. Once it triggers it stays on until the AC cord is pulled, with no indicator, and no firmware fixes it. How often it would trigger in real use isn't known. One owner says a 5.1 setup ran clean and adding height speakers set it off; that's a single owner report.
- **The Anthem MRX 1140 loses about 10 dB of SINAD when its sub output is disabled.** It's unknown whether the MRX 540 behaves the same.

Only the Yamaha group is still running.


### Claude — 2026-11-08 23:51

All 12 groups are back. Next I'll write the extractor reports and run `regroup.py`.

- _tool: Bash_ Write extractor-reports, check coverage, run regroup
- _tool: Bash_ Inspect misnamed extract and bad target

### Claude — 2026-11-08 23:52

`iim-mini-product-page.md` is an empty stray file; the real `wiim-mini` extract is fine. I'll remove the stray file, retarget the two entries to `concepts/`, and regroup.

- _tool: Bash_ Remove empty stray, fix target, regroup
- _tool: update_plan_ 
- _tool: Bash_ Update MANIFEST states, log, open questions, commit

### Claude — 2026-11-08 23:52

The commit went through, but my count of `extracted` rows came back 0, so I'll check whether the state override actually applied:

- _tool: Bash_ Check MANIFEST state column

### Claude — 2026-11-08 23:52

The state override didn't apply: the rows still say `skeleton`. I'll debug it:

- _tool: Bash_ Debug state override arguments

### Claude — 2026-11-08 23:53

The arguments are correct. The cause is zsh: an unquoted `$args` isn't split into separate words, so the script received one long argument. Passing them through `xargs` instead:

- _tool: Bash_ Apply extracted states via xargs and commit

> _Recap:_ Extraction is done: all 94 sources extracted into 1,771 verbatim entries in 39 page bundles. MANIFEST shows 39 pages as extracted, and the contradictions and six new open questions are logged and committed. Next is verification against primary sources; no wiki prose has been written yet.
>
> _Asked:_ Start verification against primary sources?


### Claude — 2026-11-08 23:53

Extraction is done and committed: 94 sources produced 1,771 verbatim entries, regrouped into 39 page bundles. `source_manifest.py` shows nothing new, missing or unextracted, and `regroup.py` shows no unknown targets. 39 pages are now marked `extracted` in `MANIFEST.md`.

I fixed two small problems along the way: an empty stray extract file, and two entries pointing at a page that doesn't exist. My first attempt to set the `extracted` states silently did nothing, because zsh passed the arguments as one string. I re-ran it and committed the fix.

**Findings that change the plan** (unverified until the next step):
- **The WiiM Amp Ultra can't be the Radio Paradise streamer.** It has no optical, coax or line output. The WiiM Pro ($169) and Pro Plus ($219) can feed a receiver: both have optical and coax outputs, and both support AirPlay 2.
- **A Bluesound NODE may not deliver Radio Paradise at full quality to a receiver.** BluOS says Radio Paradise's MQA stream is decoded only inside its own player, so it can't be passed to an external DAC. Whether the NODE sends plain FLAC over its digital output is unconfirmed.
- **The Onkyo/Pioneer power limiting looks like a platform-wide problem.** ASR found it on the RZ50, the RZ30, and the LX505 in 2023 and again in 2026. It stays on until the power cord is pulled, and none of Onkyo's firmware release notes mention it. How often it would trigger in a small 5.1 room isn't known.
- **The X3900H's own internet radio can't play Radio Paradise FLAC.** Its manual lists MP3, WMA and AAC only, which supports the external-streamer plan.
- **Denon's and Marantz's own Dirac pages are out of date.** Dirac's site is the current source, and pricing depends on the model.
- **No source gives power with five channels driven.** Every rating found is for one or two channels.

**Caveats for verification:**
- The Yamaha extracts condensed some spec-table rows rather than quoting them exactly.
- The Onkyo spec-sheet quotes were pieced back together from a two-column PDF.
- Most of ASR's receiver numbers are in chart images that weren't captured.

**`NO-HOME` (77 entries):** mostly Sony specs, which are out of scope. The rest are prices of other Marantz models, ownership background, and WiiM and Bluesound speakers for the kitchen and bathroom. They suggest four possible additions, which I'll argue at the next plan checkpoint rather than create now:
- Product pages for the WiiM Pro Plus and the Bluesound NODE as the external streamer.
- A comparison of kitchen and bathroom speakers.
- The Marantz CINEMA 60 Series 2 ($2,000).
- A setup-and-calibration page.

Six new open questions are logged, among them the X3900H's coax/optical sample-rate limit and the MRX 540's sub outputs. Others: the NODE's Radio Paradise output, Onkyo limiting in real use, Yamaha's internet radio and Radio Paradise FLAC, and which Dirac tiers Arcam and NAD include.

The next step is verification: checking each number against primary sources and recording an evidence block per claim. A few gaps could be captured first if you want them in the evidence: the Marantz Series 2 and Anthem MRX 540 manuals, and ASR's "limp mode" threads.


---

## You — 2026-11-08 23:53

Yes, verify

- _tool: update_plan_ 
- _tool: Write_ /private/tmp/claude-501/-Users-drucev--claude-spares-spare-j1GWM6/df184a1b-8efd-485e-a668-381a49af473d/scratchpad/verify-brief.md
- _tool: update_plan_ 
- _tool: Agent_ Verify A: Denon, HEOS, Audyssey
- _tool: Agent_ Verify B: Marantz
- _tool: Agent_ Verify C: Dirac and room correction
- _tool: Agent_ Verify D: Onkyo and power ratings
- _tool: Agent_ Verify E: Yamaha and Anthem
- _tool: Agent_ Verify F: NAD, Arcam, BluOS
- _tool: Agent_ Verify G: WiiM, Radio Paradise, streaming
- _tool: Agent_ Verify H: concepts and remaining hubs

### Claude — 2026-11-08 23:54

Eight verification agents are running in the background. Each takes one page cluster:

- **A:** Denon, HEOS and Audyssey.
- **B:** Marantz, using the Series 2 manuals.
- **C:** Dirac and room correction, building one table of which Dirac tiers each candidate has, which are included, which are paid, and at what price.
- **D:** Onkyo power limiting, ASR's "limp mode" threads, and the FTC's power-rating rule.
- **E:** Yamaha and Anthem, using the MRX 540 manual.
- **F:** NAD, Arcam and BluOS, including whether a NODE sends Radio Paradise as plain FLAC.
- **G:** WiiM, Radio Paradise and the streaming protocols.
- **H:** concepts and the remaining hubs: room-correction research beyond Winer, ASR thresholds, and warranty terms.

Each agent makes two checks per claim. First, is the quote really in the cited source, word for word? Second, does the most authoritative source confirm it? Each writes only its own `extracts/verification-r1-<group>.md` and proposes product front-matter values, using `?` where no source settles them. Any new web captures are saved to `raw/` with a `v-` prefix. The agents only report manifest rows, so I'll add them to `raw/manifest.txt` myself, one at a time. The agents also try to settle the open questions for their pages.


### Claude — 2026-11-08 23:58

Group G (WiiM and streaming) is done: 13 checks, none contradicted. Two open questions moved:

- **#11 is settled.** The WiiM Ultra has optical and coax outputs. The Amp Ultra's only digital output is USB.
- **#10 stays open.** WiiM makes no official claim that its Radio Paradise service is lossless.

Apple Music isn't built into WiiM's app. WiiM's own FAQ says it plays only through AirPlay, Bluetooth or Cast, and over AirPlay or Bluetooth that's 44.1 kHz/16-bit. Playing the Radio Paradise FLAC stream by URL on the WiiM Pro or Pro Plus is supported only by 2023 user posts. Settling both of those needs a test on the actual device.

Seven groups are still running.

- _tool: Bash_ Queue group B's new manifest rows
- _tool: Bash_ Queue group H's new manifest rows

### Claude — 2026-11-08 23:59

Groups B (Marantz) and H (concepts and remaining hubs) are done, so three of the eight verification groups are finished.

- **CINEMA 70s Series 2:** its Dirac upgrade is Room Correction only. Its two sub outputs carry the same signal, so it would be a poor base if a second sub is ever added.
- **Internet radio:** both Series 2 models play only WMA, MP3 and AAC, so Radio Paradise FLAC needs an external streamer on Marantz too.
- **Series 1 warm-up fault:** no one has measured the Series 2 70s, so the fault is neither confirmed nor ruled out.
- **Single-sub bass:** a 2006 Harman paper (Welti and Devantier) backs Winer's room-correction finding. With one sub, bass varies from seat to seat in a way room correction can't fix; the paper's remedy is multiple subs.
- **SINAD:** ASR says outright that SINAD isn't tied to what you can hear.
- **Warranties:** 3 years for Denon AVR-X models, 5 years for Marantz CINEMA models, 3 years for Onkyo RZ.

Six new primary sources are queued for the manifest: two Marantz manual extracts, the Denon and Marantz warranties, the Welti paper and ASR's SINAD explainer. Five groups are still running.

- _tool: Bash_ Queue group A's new manifest rows

### Claude — 2026-11-08 23:59

Group A, covering Denon, HEOS and Audyssey, is done, which makes four of eight groups finished.

- **X3900H HDMI outputs:** the conflict is settled. The manual describes three outputs: two for the main room and one for Zone 2.
- **X3800H:** it's a 2022 model that launched at $1,699. It's still on sale, and Denon never says the X3900H replaces it.
- **MultEQ-X:** support on the 2026 models is still unconfirmed, though the vendor's list looks out of date rather than exclusionary. The $19.99 iOS MultEQ Editor app explicitly lists the X3900H and X2900H.
- **Radio Paradise on HEOS:** HEOS can play a direct stream URL, but only through its developer command interface or the third-party Hark Stream app. Whether FLAC works that way isn't documented. Roon or AirPlay remain the other untested options.

Five more sources are queued for the manifest. Groups C (Dirac), D (Onkyo and power ratings), E (Yamaha and Anthem) and F (NAD, Arcam and BluOS) are still running.

- _tool: Bash_ Queue group C's new manifest rows
- _tool: Bash_ Queue group E's new manifest rows

### Claude — 2026-11-09 00:00

Six of eight groups are done. These are the findings from C (Dirac) and E (Yamaha and Anthem) that change the plan:

- **Dirac is reconciled from Dirac's own pages.**
  - Denon X3900H and X3800H, and Marantz CINEMA 50 and 50 S2: Room Correction costs $259 (Limited) or $349 (Full). Bass Control is $299 and ART is $299.
  - Denon X2900H and Marantz 70s S2: Room Correction only.
  - Onkyo RZ50 and Arcam AVA15: Room Correction is included.
  - Bass Control does work with a single sub, but nobody has measured how much it helps in that case.
- **Anthem MRX 540:**
  - $1,899.99 and in stock.
  - The two sub outputs carry the same signal, so they are not independent.
  - Power is rated at 1% THD, a looser standard than the other brands use, so the figures can't be compared directly.
  - It has no Roon support.
- **Yamaha RX-A4A:**
  - Around $1,400–$1,600 at retailers.
  - There is no independent measurement of it.
  - Whether Radio Paradise FLAC plays through its internet radio is still open. Its coax input accepts 192 kHz, so an external streamer avoids the question.

Two more sources are queued for the manifest: the Anthem manual and the MRX 540 spec page. Groups D (Onkyo and power ratings) and F (NAD, Arcam and BluOS) are still running.

- _tool: Bash_ Queue group F's new manifest rows

### Claude — 2026-11-09 00:00

Group F (NAD, Arcam and BluOS) is done, which makes 7 of 8.

- **NODE as the Radio Paradise streamer is still unconfirmed (#13).** BluOS documents Radio Paradise only as MQA. Its passthrough mode caps a NODE's digital output at 24/96. No BluOS page says what the Radio Paradise service sends to an external receiver. The WiiM Pro or Pro Plus route is better documented.
- **NAD T 758 V3i:** $2,299, still unmeasured (#7). Its Dirac tier, native Apple Music support and Connect support are all unconfirmed for that specific model.
- **Arcam AVA15:** $4,499.95, 85 W per channel (8 Ω, two channels driven, 0.5% THD). Room Correction is included. It has up to 3 sub outputs, and its US stock status is unclear.

Four more sources are queued. Only group D (Onkyo and the FTC power-rating rule) is still running.


### Claude — 2026-11-09 00:02

All 8 verification groups are back. I'll register the 25 new primary captures, merge the evidence into one file and update the open questions.

- _tool: update_plan_ 
- _tool: Bash_ Queue group D rows, check every queued file exists

### Claude — 2026-11-09 00:02

All 25 queued files exist on disk, and there are exactly 25 `v-` files. Next I'll write the manifest rows, merge the evidence and update the open questions:

- _tool: Bash_ Register batch 3 rows, merge verification files, tally
- _tool: Bash_ Fix extract count, list open-question updates
- _tool: Write_ /Users/drucev/projects/hometheater/OPEN-QUESTIONS.md
- _tool: update_plan_ 
- _tool: Read_ /Users/drucev/projects/hometheater/OPEN-QUESTIONS.md
- _tool: Write_ /Users/drucev/projects/hometheater/OPEN-QUESTIONS.md

### Claude — 2026-11-09 00:03

Next: set `verified` on every page that has a verification section, then log and commit.

- _tool: Bash_ List pages with verification sections vs extracted

### Claude — 2026-11-09 00:03

31 pages have verification sections. The other 8 bundled pages were only sampled or weren't priorities, so they stay `extracted` and I'll note that in the log.

- _tool: Bash_ Set verified states, log, commit verification round

> _Recap:_ Verification is done and committed. 163 claim blocks were checked against primary sources, with no misquotes found. 25 new primary sources are registered and 31 pages are marked verified. Open questions now carry a status: five settled, fifteen new. Next is drafting, starting with the concept and platform pages, then a check of the writing voice.
>
> _Asked:_ Should I draft the first batch, the concepts and platform pages?


### Claude — 2026-11-09 00:04

Verification is done and committed. Eight agents checked 163 claims against primary sources:

| Verdict | Count |
|---|---|
| Confirmed | 112 |
| Partial | 35 |
| Couldn't be settled | 24 |
| Contradicted | 2 |

Some claims got more than one verdict, so the counts add up to more than 163. None of the extracts misquoted their sources. The agents saved 25 new primary sources, which are now registered as batch 3 in the manifest. 31 pages are marked `verified`. The remaining 8, mainly the streaming and connectivity pages, were only spot-checked and stay `extracted`.

**What changed the picture:**
- **The FTC rule doesn't require power ratings with all channels driven.** Under 16 CFR 432 (final rule effective 2024-08-12), a rating only has to cover the two front channels at 8 Ω and 1% distortion. So no "FTC" rating in this wiki tells you anything about five channels, which contradicts what the skeleton assumed.
- **Several candidates' sub outputs aren't independent.** The Anthem MRX 540's two sub outputs carry the same signal ($1,899.99, in stock, no Roon), and so do the Marantz CINEMA 70s Series 2's. With one sub this doesn't matter, but it closes off a later two-sub upgrade.
- **The Dirac line-up is reconciled from Dirac's own site.**
  - **X3900H, X3800H and CINEMA 50 / 50 S2:** all three products, paid (Room Correction $259/$349, Bass Control $299, ART $299).
  - **X2900H and 70s S2:** Room Correction only.
  - **Onkyo RZ50 and Arcam AVA15:** Room Correction included.

  Bass Control does work with a single sub, but nobody has measured how much it helps with one.
- **Onkyo RZ50:** $1,399.99 and on backorder. The power limiting shows up across the Onkyo/Pioneer models, and there's no fix or manufacturer statement. The Pioneer LX505 review's test load is ambiguous, because the post was edited from "4 ohm" to "8 ohm". So the wiki won't claim from it that the problem happens at 8 Ω.
- **The streamer choice now leans towards WiiM.** A Bluesound NODE may not send Radio Paradise to the receiver as plain FLAC, because BluOS documents its Radio Paradise stream only as MQA, which it decodes inside the player. That makes a WiiM Pro or Pro Plus the better-documented external streamer.
- **A Harman research paper backs Winer's room-correction finding.** With one sub, the bass varies from seat to seat in a way room correction can't remove (Welti & Devantier, 2006).
- **Warranties:** Denon AVR-X 3 years, Marantz CINEMA 5 years, Onkyo RZ 3 years.

The open questions file now has a status column: 5 settled, 15 new.

**Three questions can only be answered by testing a device you'd own:**
- Whether WiiM plays Radio Paradise FLAC.
- Whether HEOS can play the Radio Paradise FLAC link directly.
- What a NODE sends from Radio Paradise to the receiver.

**Two things you could do yourself if you want:**
- Open the Audioholics RZ70 bench test in a normal browser, since it blocked automated fetches.
- Tell me your speaker models and impedance. That decides whether the Onkyo limiting would even be reachable at small-room listening levels.

The next stage is drafting. The first batch is the 5 concept pages and 10 platform pages, written only from their evidence bundles and verification records. After that I'll stop so you can check the writing voice before the product and criteria pages.


---

## You — 2026-11-09 00:28

Yes, draft batch 1

- _tool: update_plan_ 
- _tool: Write_ /private/tmp/claude-501/-Users-drucev--claude-spares-spare-j1GWM6/df184a1b-8efd-485e-a668-381a49af473d/scratchpad/draft-brief.md
- _tool: update_plan_ 
- _tool: Agent_ Draft concepts: bass, room modes, measurements
- _tool: Agent_ Draft power ratings, lossless, protocols
- _tool: Agent_ Draft room-correction system pages
- _tool: Agent_ Draft HEOS, MusicCast, BluOS pages
- _tool: Agent_ Draft WiiM and Radio Paradise pages

### Claude — 2026-11-09 00:30

Five drafting agents are writing batch 1 in the background, 15 pages in all:

1. **Bass and room concepts:** bass management and crossovers, room modes and the limits of correction, measurements and audibility.
2. **Power and streaming concepts:** amplifier power ratings (led by the FTC finding), lossless streaming paths, streaming protocols.
3. **Room-correction systems:** Dirac Live (with the reconciled per-receiver table), Audyssey MultEQ, ARC Genesis, YPAO.
4. **Streaming platforms:** HEOS, MusicCast, BluOS.
5. **WiiM and Radio Paradise:** includes a per-candidate table of how Radio Paradise FLAC reaches each receiver.

Each agent writes only its own pages. It works from that page's evidence bundle and verification record, with no web search. Every page keeps its existing links and must pass its own lint findings.

The shared brief sets the voice from `CLAUDE.md`:
- Answer first.
- Every number carries its test conditions and date.
- Each claim is labelled as measured, manufacturer claim, owner report or unknown.
- No marketing adjectives.

When they report back, I'll read the drafts and run the gates. Then I'll update the index lines, `MANIFEST.md` and the log, and stop for you to check the voice before the product and criteria pages are written.


### Claude — 2026-11-09 00:35

The HEOS, MusicCast and BluOS pages are drafted, with lint clean and no broken links. The agent revised one skeleton claim on the evidence: the BluOS page no longer calls the NODE "the reference external streamer", because it isn't documented whether a NODE sends plain FLAC to a receiver.

The other four drafting agents are still running. 3 of 15 pages are done.


### Claude — 2026-11-09 00:36

The three bass, room and measurement concept pages are drafted, with lint clean and no broken links. 6 of 15 pages are done.

The agent removed two skeleton claims that no source supports:
- "Above roughly the high-80s dB, SINAD differences are inaudible."
- "Crossover settings matter more than which room correction brand you have."

That's the verification step working as intended. Two notes to check at review:
- The bass-management page is 1,491 words, just under the 1,500 ceiling.
- The agent says no Marantz manual was in its evidence. Selected pages of both Series 2 manuals were captured during verification, so the Marantz sub-output behaviour on that page is marked unverified when the evidence actually covers it. I'll fix that when reviewing.

The other three drafting agents are still running.


### Claude — 2026-11-09 00:37

WiiM and Radio Paradise are drafted, with lint clean. That's 8 of 15 pages.

- **WiiM page.** It now makes a specific recommendation: the WiiM Pro ($169) or Pro Plus ($219) as the receiver's external streamer. They're the only WiiMs with optical and coax out plus AirPlay 2.
- **Radio Paradise page.** It has a per-candidate table of how Radio Paradise FLAC reaches each receiver. Only the NAD carries it natively.

One provenance problem to fix at review. Some claims on the WiiM page rest on sources that were read during verification but never saved to `raw/`: WiiM's Apple Music FAQ, its Ultra-outputs FAQ, and the old forum threads. Saving rules require every cited source to be in `raw/`. So I'll either capture those pages or mark the claims that depend on them as unverified.

Two drafting agents are still running: power ratings and streaming, and the room-correction systems.


### Claude — 2026-11-09 00:38

Room correction is drafted: Dirac Live, Audyssey, ARC Genesis and YPAO, with lint clean. That's 12 of 15 pages.

- **Dirac:** the page now gives a buying conclusion for your one-sub room.
  - Room Correction plus Bass Control costs $299 on the Arcam and Onkyo, where Room Correction is included.
  - The same pair costs $558 to $599 on the Denon X3800H/X3900H and Marantz CINEMA 50 models.
  - The X2900H and 70s S2 can't take Bass Control at all.
- **ARC Genesis:** the MRX/AVM manual shows it doesn't set speaker distances; those are entered by hand.
- **YPAO:** the RX-A4A manual answers the open question on its two sub outputs, which carry the same signal.
- **Audyssey:** the Editor app supports the 2026 models; MultEQ-X support is still open.

Only the power-ratings, lossless-streaming and streaming-protocols agent is still running.


### Claude — 2026-11-09 00:39

All 15 batch-1 pages are drafted. Now the review: run the gates, fix the gap where some claims cite sources that were never saved to `raw/`, and read a sample of pages for voice.

- _tool: update_plan_ 
- _tool: Bash_ Run gates and list drafted pages
- _tool: Bash_ Fetch the three uncaptured WiiM FAQ articles
- _tool: Bash_ Convert and save WiiM FAQs, check key content
- _tool: Bash_ Read Apple Music FAQ key lines

### Claude — 2026-11-09 00:40

The FAQ confirms 44.1 kHz/16-bit over AirPlay and Bluetooth. Next I'll point the pages at these now-saved captures instead of "read during verification":

- _tool: Bash_ Find citations to sources not in raw/
- _tool: Bash_ Inspect sources sections citing uncaptured FAQs
- _tool: Bash_ Point pages at the newly captured WiiM FAQs
- _tool: Bash_ Check Marantz claims against Marantz manual captures
- _tool: Bash_ Read the sentence to correct and Marantz Direct rule
- _tool: Edit_ /Users/drucev/projects/hometheater/wiki/concepts/bass-management-and-crossovers.md
- _tool: Bash_ Add Marantz manual source, re-lint, word count
- _tool: Read_ /Users/drucev/projects/hometheater/wiki/concepts/bass-management-and-crossovers.md

### Claude — 2026-11-09 00:41

The voice is what the contract asks for: claim first, every number dated or cited, conditions carried, and caveats inside the sentence. Applying the Marantz correction and trimming back under 1,500:

- _tool: Edit_ /Users/drucev/projects/hometheater/wiki/concepts/bass-management-and-crossovers.md
- _tool: Edit_ /Users/drucev/projects/hometheater/wiki/concepts/bass-management-and-crossovers.md
- _tool: Bash_ Re-lint; read WiiM page section to trim

### Claude — 2026-11-09 00:41

The WiiM page is 12 words over the target. Shortening the WiiM Sound sentence:

- _tool: Read_ /Users/drucev/projects/hometheater/wiki/systems/wiim.md
- _tool: Edit_ /Users/drucev/projects/hometheater/wiki/systems/wiim.md
- _tool: Bash_ Gate batch 1 and list words and claims
- _tool: update_plan_ 
- _tool: Bash_ Register FAQs, refresh index hooks, set drafted, gate
- _tool: Bash_ Redo index hooks, log, commit batch 1

### Claude — 2026-11-09 00:42

The judgment count went from 36 to 37 with the longer index lines. Checking what's new:

- _tool: Bash_ Find the new lint finding
- _tool: Bash_ Record index exception and commit

> _Recap:_ Batch 1 is drafted and committed: 5 concept pages and 10 system pages, built from verified evidence. Lint and link checks pass on all of them. Products, criteria, comparisons and decision pages are still skeletons, waiting on your voice check.
>
> _Asked:_ Is the voice right, or should the next batch be tighter?


### Claude — 2026-11-09 00:42

Batch 1 is drafted and committed: 5 concept pages and 10 system pages, written only from the verified evidence. All 15 pass lint with no findings, and there are no broken links.

**Pages worth opening to judge the voice:**
- [bass-management-and-crossovers.md](../hometheater/wiki/concepts/bass-management-and-crossovers.md): a manual-heavy page.
- [dirac-live.md](../hometheater/wiki/systems/dirac-live.md): the per-receiver price table and the one-sub purchase advice.
- [room-modes-and-correction-limits.md](../hometheater/wiki/concepts/room-modes-and-correction-limits.md): two conflicting kinds of evidence, side by side.

**Conclusions the drafts changed on the evidence:**
- **External streamer:** the WiiM Pro ($169) or Pro Plus ($219) on the receiver's coax input is the best-documented way to get Radio Paradise FLAC. Over coax the Pro Plus's extra $50 buys nothing you'd use.
- **Dirac for one sub:** Room Correction plus Bass Control costs $299 on the Onkyo and Arcam, where Room Correction is included. On the Denon X3800H/X3900H and Marantz CINEMA 50 models it costs $558–$599. The X2900H and 70s Series 2 can't take Bass Control at all.
- **Power ratings:** the FTC rule only covers two channels, so no rating here describes five. Latched protection was measured on the Marantz CINEMA 70s Series 1 as well as on Onkyo/Pioneer.
- **Removed as unsourced:** a SINAD audibility threshold and a "crossover matters more than correction brand" ranking. Both were in the skeleton, and no source supports either.

**Fixes I made in review:**
- Three WiiM help pages that verification had read but not saved are now captured and cited.
- A Marantz claim had been marked unverified, but the Marantz manual already in the sources confirms it, so I corrected it.
- I accepted the index going over 1,500 words, since it's a catalog. The reason is in the log.

**What I'd tighten:**
- **Long claim sentences.** The bold claims run 40–60 words. The Dirac one names five receivers and two price ranges. A shorter claim plus a table would read faster.
- **Pages at the ceiling.** Five pages sit within 10 words of the 1,500 target, because the agents cut to fit. That means the evidence is dense, not that the pages are padded. A tighter brief for products (300–1,200 words) would force more selection.
- **Status labels.** "Contested" is on 10 of the 15 pages. It's honest, but it's used broadly. "Contested" could be kept for real conflicts between sources and "unverified" for gaps.

If you choose to tighten, I'll update the brief and rework the claim sentences on these 15 pages first, then write the product pages to the new standard. Otherwise batch 2 starts with the 12 product pages, filling their spec fields from the verification tables.


---

## You — 2026-11-09 01:23

Voice is right, continue

- _tool: update_plan_ 
- _tool: Write_ /private/tmp/claude-501/-Users-drucev--claude-spares-spare-j1GWM6/df184a1b-8efd-485e-a668-381a49af473d/scratchpad/draft-brief-products.md
- _tool: update_plan_ 
- _tool: Agent_ Draft Denon product pages
- _tool: Agent_ Draft Marantz product pages
- _tool: Agent_ Draft Yamaha, Onkyo, Anthem pages
- _tool: Agent_ Draft NAD, Arcam, WiiM Amp Ultra pages

### Claude — 2026-11-09 01:24

Batch 2 is under way: four agents are drafting the 12 product pages in the background.

1. **Denon:** X3900H, X3800H, X2900H.
2. **Marantz:** CINEMA 70s Series 2, 50 Series 2, original CINEMA 50.
3. **Yamaha, Onkyo and Anthem:** RX-A4A, TX-RZ50, MRX 540.
4. **NAD, Arcam and WiiM:** T 758 V3i, AVA15, Amp Ultra. The Amp Ultra is ranked only for the future stereo rooms.

The product addendum keeps the voice you approved and adds four rules for product pages:
- **Spec fields from verification:** they're filled from the verification tables in fixed formats, and anything not settled stays `?`.
- **Shorter pages:** claims are capped at about 35 words and pages target about 700.
- **Link, don't repeat:** each page links to the system and concept pages rather than restating them, and must not contradict them.
- **Status labels used more narrowly:** "contested" only where sources genuinely conflict, "unverified" where evidence is missing.

When they finish, I'll run `gen_matrix.py`, which builds the spec table from the product pages and reports every gap. I'll check the pages against the system pages, run the gates and commit. After that come the 7 criteria pages and 2 comparisons, which do the actual ranking.


### Claude — 2026-11-09 01:29

The Denon pages are done (3 of 12). The agent flagged two possible errors in batch 1 pages, and I'll check both against the raw sources once all four agents have reported:

- **"70% of rated power into five channels" on the power-ratings page.** It's attributed to the X3900H, but the agent says the evidence ties it only to the X2900H. Extraction notes conflict on this, with one mentioning a "70% Guarantee" on the X3900H info sheet, so the raw source has to decide.
- **The $558 Room Correction + Bass Control figure on the Dirac page for the X3800H.** Only the $599 bundle is confirmed for that model.

Three agents are still running: Marantz; Yamaha, Onkyo and Anthem; and NAD, Arcam and WiiM.

- _tool: Bash_ Record batch 1 corrections to check

### Claude — 2026-11-09 01:30

The Marantz pages are done, so 6 of 12 product pages are drafted. The CINEMA 50 Series 2 page puts the main question plainly: it has the same XT32 and Dirac options as the $1,849 Denon X3900H, costs $3,000, and no measurement shows what the extra $1,151 buys.

Two more batch 1 corrections came out of this, now listed alongside the Denon ones:
- **CINEMA 70s Series 1 fault.** The power-ratings page says it appeared "at 10 W". ASR's actual condition was 5 W into each of two 4 Ω channels.
- **Series 1 CINEMA 50 Audyssey tier.** The Audyssey page says it isn't confirmed. A Marantz compare tile lists XT32 for it, which is a weak source but still a Marantz one.

I'll check all four corrections against the raw sources after the last two agents report.

- _tool: Bash_ Record NAD/Arcam review items

### Claude — 2026-11-09 01:30

NAD, Arcam and WiiM are done, so 9 of 12 product pages are drafted. Only the Yamaha, Onkyo and Anthem agent is still running.

- **Arcam AVA15:** the page sets out the real cost gap. With Bass Control it comes to $4,799. A Denon X3900H with Dirac's $599 Room Correction + Bass Control bundle comes to $2,448.
- **WiiM Amp Ultra:** the conflict with Apple Music is stated outright. With no AirPlay 2 and no native app, Apple Music can reach it only over Bluetooth at 44.1/16, over Google Cast, or through a wired input.

**Two review items added:**
- **NAD streaming list.** The spec fields list Spotify, TIDAL and Qobuz Connect. Those are documented only for the BluOS platform, not for the V3i, so I'll trim the list to what's model-specific.
- **NAD and Arcam stock claims.** These come from web reads during verification that were never saved to `raw/`, so I'll check they're labelled that way.


### Claude — 2026-11-09 01:32

All 12 product pages are drafted. Next I'll work through the six review items against the raw sources, starting with the "70%" claim:

- _tool: update_plan_ 
- _tool: Bash_ Check the 70% claim and the 10 W wording in raw sources
- _tool: Bash_ Check 70% on product pages, $558, Audyssey CINEMA 50 tile
- _tool: Bash_ Find the CINEMA 50 Audyssey compare tile
- _tool: Bash_ Map compare tiles to model names

### Claude — 2026-11-09 01:32

Confirmed: the tile at line 1777 belongs to the CINEMA 50 (Series 1) and lists MultEQ XT32. Applying fixes 1–5:

- _tool: Bash_ Locate lines for the remaining edits
- _tool: Bash_ Apply fixes 1–5 with exact replacements
- _tool: Bash_ Label NAD stock source; try capturing Onkyo warranty
- _tool: Bash_ Save Onkyo warranty to raw and register it
- _tool: Bash_ Read the RZ50 warranty citation
- _tool: Bash_ Show warranty text in RZ50 paragraph
- _tool: Bash_ Re-cite RZ50 warranty to the capture

### Claude — 2026-11-09 01:33

The warranty capture confirms the 2018 date. I'll add it to the RZ50's Sources list, then run the matrix generator and the gates:

- _tool: Bash_ Add warranty source, generate matrix, run gates
- _tool: Bash_ Show WORDS-HIGH and HYGIENE findings

### Claude — 2026-11-09 01:33

My corrections pushed the power-ratings page and the Dirac page over 1,500. I'll tighten my own added wording and clear the `.DS_Store` residue with `--fix`:

- _tool: Bash_ Trim the two pages and clear residue

### Claude — 2026-11-09 01:33

Still a few words over on each. I'll read the surrounding text and cut something that isn't carrying information:

- _tool: Bash_ Read the two paragraphs to trim
- _tool: Bash_ Trim further and re-lint
- _tool: Bash_ Refresh index, set drafted, log, commit batch 2
- _tool: update_plan_ 
- _tool: Write_ /private/tmp/claude-501/-Users-drucev--claude-spares-spare-j1GWM6/df184a1b-8efd-485e-a668-381a49af473d/scratchpad/draft-brief-hubs.md
- _tool: Agent_ Draft hubs: room correction, music, amps
- _tool: Agent_ Draft hubs: streaming, connectivity, usability, value
- _tool: Agent_ Draft the two comparison pages

### Claude — 2026-11-09 01:35

Batch 2 is committed: 12 product pages, plus the generated spec matrix with 5 honest gaps.

**Cross-batch corrections, settled against the raw sources:**
- **Denon "70% Guarantee":** the Denon product agent said the power-ratings page was wrong to give this to the X3900H. It was the agent that was wrong: the X3900H's own info sheet carries it. The concept page stands, and the X3900H product page now has the row it had left out.
- **Marantz, two findings the Marantz agent got right:**
  - The CINEMA 70s Series 1 fault happened at 5 W per channel into 4 Ω.
  - The Series 1 CINEMA 50 has Audyssey XT32, from a Marantz compare tile.
- **Dirac $558 price:** it applies only to the X3900H, the one model where Dirac lists Limited and Full Room Correction separately.
- **NAD streaming fields:** trimmed to BluOS and AirPlay 2, the only services documented for the V3i itself.
- **Onkyo warranty:** the RZ50 page cited a warranty page that was never saved. It's now captured, confirming 3 years parts and labor for RZ Series receivers.

Batch 3 is running in the background with three agents:
- **Room correction, music and amplification hubs.** These are the measurement-led rankings. Unmeasured models go under "not enough evidence" rather than above measured ones.
- **Streaming, connectivity, usability and value hubs.** Value counts the full cost: receiver, plus Dirac licence, plus WiiM streamer.
- **The two comparisons:** Radio Paradise FLAC native on the receiver versus an external streamer, and which Dirac licence to buy with one sub.

The hubs work only from the drafted pages, so the rankings can't contradict the product pages. When they're back I'll regenerate the matrix with the rankings and run the gates. Then I'll stop before the shortlist and recommendation, since that decision is yours.

- _tool: Bash_ Fix RZ50 arithmetic error and typo

### Claude — 2026-11-09 01:38

Both comparison pages are drafted, and both reach clear verdicts:

- **Radio Paradise FLAC: a $169 WiiM Pro on the receiver's coax input.**
  - It's the cheapest route and leaves the receiver free to be chosen for room correction.
  - It uses the same app as the future stereo rooms.
  - The NAD is the only native path, but it loses on room correction.
  - The NODE costs $680 more, and what it sends out for Radio Paradise is undocumented.
- **Dirac for one sub: buy Room Correction plus Bass Control wherever Bass Control is sold.**
  - That's $299 on the Onkyo RZ50 and Arcam AVA15, and the $599 bundle on the Denon and Marantz CINEMA 50 models.
  - Bass Control is recommended for what it automates, not for any measured gain, because nobody has measured its benefit with one sub.

The comparisons agent also found two errors on the Onkyo RZ50 page, both now fixed: a $1,698.98 total that should have been $1,698.99, and a stray-comma typo. The two hub agents are still running.


### Claude — 2026-11-09 01:41

The hub agent caught a bug of mine. When I added the Onkyo warranty source, my insertion missed the Sources list and put the bullet inside the RZ50 page's front matter, above `title:`. The linter didn't flag it. Fixing that now, and checking the Dirac page for the $1,698.98 arithmetic error:

- _tool: Bash_ Inspect RZ50 front matter and Sources, find bad sum
- _tool: Bash_ Fix RZ50 front matter; add a stray-line lint check

### Claude — 2026-11-09 01:41

Fixed, and the linter now has an `FM-STRAY` check, so a line sitting outside any key in the front matter fails the gate. The $1,698.98 error isn't anywhere else. Room correction, music and amplification are ranked: the Denon X3900H leads all three. The Onkyo RZ50 ties for best on room correction, at the lowest all-in cost of $1,698.99 including Bass Control, but sits near the bottom on amplification because of its limiter. The last hub agent, for streaming, connectivity, usability and value, is still running.


### Claude — 2026-11-09 01:44

All seven hubs and both comparisons are drafted. One process note: an agent reverted the matrix to its last committed version, so the first hub agent's regeneration is gone. I'll regenerate it from the final hub rankings, register the new open questions, run the gates and commit:

- _tool: Bash_ Regenerate matrix, add open questions, refresh index, gate

### Claude — 2026-11-09 01:44

The matrix now carries all seven rankings. The Denon X3900H is first on four criteria and second on two more. I'll check the one new `WORDS-HIGH` finding:

- _tool: Bash_ Show word-limit findings

### Claude — 2026-11-09 01:44

The RZ50 page is 4 words over its 1,200 limit, because of the warranty line I added. I'll trim one sentence, then log and commit:

- _tool: Bash_ Trim RZ50, log batch 3, commit

### Claude — 2026-11-09 01:44

The RZ50 page is still one word over and went into that commit, so here's a one-word follow-up:

- _tool: Bash_ Trim RZ50 one more word and commit
- _tool: update_plan_ 

> _Recap:_ All 37 non-decision pages are drafted and committed: 7 ranked criteria, 2 comparisons and a generated ranking matrix. Gates are clean on every drafted page. The shortlist, recommendation and buying checklist are still skeletons waiting on your decision.
>
> _Asked:_ Shortlist the X3900H and RZ50, then write the recommendation?


### Claude — 2026-11-09 01:45

Batches 2 and 3 are drafted and committed, so 37 of 45 pages are done. Gates show no findings on any drafted page, and there are no broken links. The 10 remaining lint findings are all expected: the index's accepted length, five `?` spec gaps, and the three decision pages, which are still skeletons.

## What the wiki concludes

**Cost to the full target** (receiver, plus Dirac Room Correction and Bass Control, plus a $169 WiiM Pro for Radio Paradise FLAC, at 2026-11-08 prices):

| Setup | All-in | Why |
|---|---|---|
| **Denon AVR-X3900H** | **$2,617** | First on room correction, music, streaming, amplification and value; second on usability. ASR's only unqualified recommendation among the candidates (SINAD 102). XT32 is included, the $599 Dirac bundle adds Room Correction and Bass Control, and it has 4 independent sub outputs. 3-year warranty. |
| **Onkyo TX-RZ50** | **$1,868** | The only cheaper way to the same room-correction target, because full Dirac Room Correction is included. But ASR measured a 4 Ω power limiter on the platform that stays on until you pull the plug, and no firmware fixes it. It's on backorder, and a successor is teased for 2027. |
| Denon AVR-X3800H | $2,167 | Same Dirac options as the X3900H, but its DAC measured worse (SINAD 87, not recommended), and its full spec sheet hasn't been captured. |
| Marantz CINEMA 50 Series 2 | $3,768 | Best on usability (5-year warranty), but no measurement shows what the extra $1,151 over the X3900H buys a 5.1 room. |

**Comparison verdicts:**
- For Radio Paradise, a WiiM Pro on coax beats a NODE.
- For Dirac with one sub, buy Room Correction plus Bass Control wherever Bass Control is sold.
- The NAD is the only receiver that plays Radio Paradise natively, but it loses on room correction and measurements.

## What decides between the top two

The RZ50's limiter was measured at 4 Ω. How often it triggers at normal levels in a small room is unknown (OPEN-QUESTIONS #14), and your speaker impedance (#4) decides whether you'd ever reach it. With 8 Ω speakers and a willingness to wait for stock, the RZ50 saves $749. Otherwise the X3900H is the choice the evidence supports, without caveats.

## Fixes during review
- **My own bug, found by a hub agent.** My script put a Sources line inside the RZ50 page's front matter. The linter now has an `FM-STRAY` check so it can't recur.
- **A Denon agent's claim, rejected.** It said the X3900H doesn't carry Denon's "70% Guarantee". The X3900H's own info sheet carries it.
- **Smaller fixes:** an arithmetic error ($1,698.98 → $1,698.99), the Dirac $558 price limited to the X3900H, and the CINEMA 50's Audyssey tier confirmed as XT32.
- **Follow-up still open:** who owns each brand (HARMAN/Samsung for Denon and Marantz, Gentex for Onkyo) appears only on the value hub. It still needs adding to the product pages.

Once you decide, I'll write the shortlist, recommendation and buying checklist, then the reference pages: glossary, bibliography and the open questions that matter to you as a buyer.


---

## You — 2026-11-09 13:30

Yes, shortlist both

- _tool: update_plan_ 
- _tool: Bash_ Show decision and reference skeletons plus the matrix
- _tool: Bash_ Read the two shortlisted product pages and two hub rankings
- _tool: Agent_ Draft glossary page
- _tool: Agent_ Draft bibliography and open questions
- _tool: Bash_ Check decision lint rules and comparison answers
- _tool: Bash_ Write the three decision pages and check sources and lint

### Claude — 2026-11-09 13:32

Decision pages are written and pass link checks; the glossary and bibliography agents are still running. Tightening one hedge now.

- _tool: Bash_ Soften the Google Cast claim and rerun lint
- _tool: Bash_ Remove the matrix skeleton line and clean residue
- _tool: update_plan_ 

### Claude — 2026-11-09 13:32

Waiting on the two reference-page agents.


### Claude — 2026-11-09 13:34

Glossary is done (62 terms, clean lint). Still waiting on the bibliography and open-questions agent.

- _tool: Bash_ Check manifest_stats usage, MANIFEST rows and log tail
- _tool: Bash_ Regenerate matrix and stats, mark rows audited, run gates
- _tool: Bash_ Inspect manifest_stats state-override syntax
- _tool: Bash_ Count MANIFEST states
- _tool: Bash_ Mark all MANIFEST rows audited

### Claude — 2026-11-09 13:36

All 45 pages are now marked audited. Checking the index hooks for the newly drafted pages, then the log and commit.

- _tool: Bash_ Show index hooks for decision and reference pages
- _tool: Bash_ Refresh index hooks from the new claims and rerun gates
- _tool: Bash_ Append log entries and commit the round

> _Recap:_ Round 1 is finished and committed: all 45 pages are audited, including the shortlist, recommendation, buying checklist, glossary, bibliography and open questions. There are no broken links, and the 7 remaining lint findings are all accepted. The device tests and speaker impedance are still yours to settle.
>
> _Asked:_ Write the setup and calibration page next?


### Claude — 2026-11-09 13:37

The wiki is finished: all 45 pages are drafted, linted, marked audited and committed to the local repo.

## The recommendation

| Item | Price (2026-11-08) |
|---|---|
| Denon AVR-X3900H | $1,849 |
| Dirac Room Correction (Full) + Bass Control bundle | $599 |
| WiiM Pro on the receiver's coax input, for Radio Paradise FLAC | $169 |
| **Total** | **$2,617** |

The X3900H works whatever speakers you buy. It ranks first on five of the seven criteria and measured best of the candidates (Audio Science Review SINAD 102). Audyssey XT32 is included, so Dirac can be bought after you've lived with the receiver for a while. The microphone may not come with the Denon Dirac upgrade, which could mean buying a USB measurement mic, an extra cost not included above (open question #19).

The **Onkyo TX-RZ50 ($1,868)** is the backup. It's better value only if three things are all true:
- your speakers are 8 Ω with no deep impedance dips;
- you can wait months for the backorder;
- a 2020 design with a successor expected in 2027 is fine for resale.

The **AVR-X3800H** becomes the pick if the X3900H's price goes up by more than $450.

## The pages
- **[Shortlist](wiki/decision/shortlist.md):** the two models side by side, plus each eliminated receiver with the fact that ruled it out.
- **[Recommendation](wiki/decision/recommendation.md):** what to buy and what would change the choice.
- **[Buying checklist](wiki/decision/buying-checklist.md):** checks before paying (prices, an authorised dealer so the 3-year warranty applies, the return window, the mic question), then setup order and the three Radio Paradise device tests to run while you can still return it.
- **[Glossary](wiki/reference/glossary.md):** 62 terms.
- **[Bibliography](wiki/reference/bibliography.md):** the 119 sources the pages cite, with 7 worth reading in full listed first.
- **[Open questions](wiki/reference/open-questions.md):** the five unknowns that could still change the purchase. Most are settled by your speaker choice or a test after buying, not by more reading.

## Lint
Seven findings remain, none of them problems:
- the index and the bibliography are long, as lists of links are;
- five spec fields stay `?` because no source settles them.

## Not done
- **Your side:** the device tests and your speaker impedance.
- **Missing sources:** I haven't captured the X3800H spec sheet, the original CINEMA 50 docs or the RZ50 manual.
- **Brand ownership:** who owns each brand (HARMAN/Samsung, Gentex) is only on the value page so far, not the product pages.


---

## You — 2026-11-09 14:25

Yes, write it

- _tool: update_plan_ 
- _tool: Bash_ Read the four setup-relevant concept and system pages
- _tool: Read_ /Users/drucev/.claude/projects/-Users-drucev-projects-governance-wiki/df184a1b-8efd-485e-a668-381a49af473d/tool-results/b358b082f.txt
- _tool: Bash_ Find raw filenames for the setup page's sources
- _tool: Bash_ Write the setup and calibration page
- _tool: Bash_ Link the new page, register it, run gates

### Claude — 2026-11-09 14:26

The page is written, linked and passes the gates. Now I'm logging and committing.

- _tool: Bash_ Log the new page and commit

> _Recap:_ The setup and calibration page is written, linked from the recommendation, the buying checklist and the index, and committed, so the wiki now has 46 pages and no broken links. No step has been run in your room yet, so the page is marked unverified.


### Claude — 2026-11-09 14:26

I've written [setup-and-calibration.md](../hometheater/wiki/decision/setup-and-calibration.md) (1,005 words) and committed it. It's linked from the recommendation, the buying checklist and the index. No step has been tried in your room yet, so the page is marked unverified.

The order it sets for the X3900H with one sub:

1. **Place the sub first.** Its position changes the room's bass itself, while correction only changes the signal. The first spot to try is the middle of a wall, which a 2006 Harman study (Welti and Devantier) found best in rectangular rooms. Turn the sub's own crossover knob to maximum so the receiver does the filtering.
2. **Speaker settings.** Set up as 5.1 with an 80 Hz crossover until your speakers are chosen, and set Subwoofer Output to LFE. Changing the speaker layout later switches off both Audyssey and Dirac until you re-run them.
3. **Audyssey XT32 into Preset 1.** This is your free baseline: six or more mic positions within about 2 ft of the main seat. Try both the Reference and Flat curves; Denon suggests Flat for small rooms.
4. **Dirac Room Correction and Bass Control into Preset 2.**
   - Keep the mic positions close to the seat. In Ethan Winer's measurements the benefit faded within about 2 ft.
   - Cut peaks rather than boosting dips, and keep any boost to about 5 dB.
   - You may need to buy a USB measurement mic (open question #19).
5. **Compare.** Switch between the two presets at the same volume and on the same tracks. No source measures XT32 against Dirac with one sub, so your result is new evidence for the wiki.
6. **Music in Stereo mode, not Pure Direct.** Pure Direct and Direct switch off all room correction, and with this setup they also drop the bass below the crossover.
7. **WiiM Pro on coax.** Turn Fixed Volume on and EQ off, leave RoomFit off, then run the Radio Paradise tests from the buying checklist.

The "What this doesn't cover" section lists what's left out: crossovers for your specific speakers, which wait on that choice; how a second sub would change the steps; and calibration for the stereo rooms.


---

## You — 2026-11-09 14:36

can you make a github repo 'hometheater' and push, or give me the git commands

- _tool: Bash_ Check history for source files and GitHub auth

### Claude — 2026-11-09 14:36

No commit has ever contained `raw/` or `extracts/`, and the tree is clean. Creating the repo as **private**, since the wiki has never been reviewed for publication.

- _tool: Bash_ Create a private GitHub repo and push master
- _tool: Bash_ Check CLAUDE.md for a no-remote rule
- _tool: Bash_ Update CLAUDE.md remote note, commit and push

> _Recap:_ The wiki is pushed to a new private repo, github.com/druce/hometheater, and master tracks origin. CLAUDE.md now records the remote. No raw/ or extracts/ file has ever been committed, so none are in the repo.


### Claude — 2026-11-09 14:37

I created the repo and pushed: **https://github.com/druce/hometheater**. Local `master` tracks `origin/master`.

- **Private:** I made it private because nobody has reviewed the wiki for publishing. The pages contain no copied source text, but the log and bibliography include frank notes about the sources. You can make it public with `gh repo edit druce/hometheater --visibility public --accept-visibility-change-consequences`.
- **No source files:** I checked the full history before pushing. No commit has ever included `raw/` or `extracts/`, so the copyrighted captures aren't on GitHub.
- **CLAUDE.md:** it said "Git is local only, no remote". It now names the private remote and says to repeat that history check before going public. That change is committed and pushed too.

These are the commands I ran, for doing it by hand next time:

```bash
cd ~/projects/hometheater
```
```bash
gh repo create druce/hometheater --private --source=. --remote=origin --push
```


---

## You — 2026-11-09 15:06

make the repo public

- _tool: Bash_ Recheck history for source files and secrets
- _tool: Bash_ Make the repo public and record it in CLAUDE.md

> _Recap:_ github.com/druce/hometheater is now public. Before the switch, a history scan found no raw/ or extracts/ files and no secrets. CLAUDE.md now records that the repo is public and is pushed.


### Claude — 2026-11-09 15:07

**https://github.com/druce/hometheater** is now public.

- **Checked first:** I scanned every commit before switching. None contains `raw/` or `extracts/`, so the copyrighted captures aren't on GitHub, and none contains a secret pattern.
- **Recorded:** CLAUDE.md now says the repo is public. It also notes that `log.md`, `MANIFEST.md` and `OPEN-QUESTIONS.md` are published along with the wiki, so they should be written knowing anyone can read them. That change is committed and pushed.
- **One thing to know:** the log and bibliography contain blunt assessments of sources, such as "a badge isn't a report" and Winer's ties to a bass-trap business. That's how governance_wiki already handles it, but those assessments are now readable by the people and companies they describe.


---

## You — 2026-11-09 15:08

do you discuss options for multiroom system and how to connect 

probably would get external wiim or sonos , connect to the receiver, get additional  systems to drive other rooms. 

although an option is a 9.1 receiver, using 9.1 to drive additional stereo zones in 2 other rooms

- _tool: Bash_ Search the wiki for zone, Sonos and multiroom coverage
- _tool: Bash_ Search the wiki for zone, Sonos and multiroom coverage
- _tool: Bash_ Read the multiroom paragraph and list relevant sources
- _tool: Bash_ Search the X3900H manual for zone and amp assignment rules
- _tool: Bash_ Extract the Amp Assign option list from the manual

### Claude — 2026-11-09 15:09

I'm reading the X3900H manual's zone rules so the answer rests on the source, not memory.

- _tool: Bash_ Read the Amp Assign table and options
- _tool: Bash_ Find Zone 2 source and format restrictions
- _tool: Bash_ Read the Zone 2 playback section

> _Recap:_ Only part of the wiki covers multiroom: the streaming hub on app fragmentation, the WiiM Amp Ultra as the stereo-room plan, and one row in the Radio Paradise comparison. Receiver zones, wiring and Sonos have no page. I read the X3900H manual's zone rules but changed no files.
>
> _Asked:_ Write a multiroom comparison page, with a Sonos research pass?


### Claude — 2026-11-09 15:09

Only partly. The wiki covers the app question and names the WiiM Amp Ultra for the stereo rooms. It doesn't cover your two options, the receiver's own zones or a Sonos setup, and nothing explains how to wire any of it. I read the zone section of the X3900H manual to answer the 9.1 question.

## What the wiki says now
- **[Streaming & multiroom hub](../hometheater/wiki/criteria/streaming-and-multiroom.md):** the receiver's own app (HEOS) becomes a second app next to WiiM Home unless the whole house runs on one platform.
  - WiiM speakers can join Google Cast or Alexa groups. But a physical input, such as the TV, can only be shared within an all-WiiM group.
  - The Amp Ultra has no AirPlay 2, so an iPhone can't group it with the receiver.
- **[My system](../hometheater/wiki/start-here/my-system.md):** a WiiM Amp Ultra ($549) for each stereo room.
- **Sonos:** almost nothing. The build register records that Radio Paradise says Sonos plays its FLAC stream natively, and the Onkyo supports "Works with Sonos" through a Sonos Port. There are no Sonos prices, models or limits.

## The 9.1 idea: the X3900H can power only one other room
The manual (pp.157–163, 214) shows the X3900H has a **Zone 2 but no Zone 3**, so it can't drive two extra rooms on its own.

**Powered Zone 2:**
- Set "Amp Assign" to "7.1ch + ZONE2", which is the default. Zone 2 then plays from the Height 2 speaker terminals.
- Your 5.1 main room is unaffected.
- What it needs: a speaker-wire run from the receiver to that room's speakers.

**Other Zone 2 outputs:**
- A Zone 2 pre-out, to feed an amp in that room.
- An HDMI Zone 2 output, for a second TV.
- These are other ways to reach the same zone, not an extra zone.

**What Zone 2 can play:**
- The same source as the main room, or a different one.
- Sources: HEOS, analog, USB, the tuner, and the coax or optical inputs (two-channel PCM only).
- So the WiiM Pro's Radio Paradise stream on coax can play in Zone 2.
- HDMI sources need Zone 2's "HDMI Audio" set to PCM.
- If both zones play the same HDMI source, the main room may drop to two-channel PCM as well (manual p.253).

The manual doesn't settle these points, so they're unverified:
- whether room correction applies in Zone 2;
- whether Zone 2 needs the main receiver switched on.

Other receivers: the Onkyo RZ50 has Zone 2 and Zone 3, but Zone 3 is a line output that needs its own amp. The Yamaha RX-A4A can assign two amp channels to Zone 2.

## How the two approaches compare

| | Receiver Zone 2 for one room + a streaming amp for the other | A streaming amp in each room (WiiM or Sonos) |
|---|---|---|
| Hardware cost | Lowest: the X3900H's spare amp channels are already paid for | About $549 per room for an Amp Ultra; Sonos not priced |
| Wiring | Speaker wire from the receiver to Zone 2 | Power and network only |
| Rooms | One from the receiver; the second room needs a separate box anyway | Any number |
| Room correction | Unverified for Zone 2 | RoomFit on each Amp Ultra |
| Control | HEOS app or receiver for Zone 2, WiiM Home for the rest | One app across the house (WiiM Home, or Sonos) |
| Main room off | Unverified whether Zone 2 needs it on | Independent |

A **Sonos-based house** would change the external streamer as well: a Sonos Port into the receiver, with Sonos amps and speakers elsewhere. Radio Paradise says Sonos plays its FLAC natively, which could remove the WiiM. Sonos was never researched, though, so its prices, AirPlay support and limits aren't in the wiki and I won't guess them.

**My view so far:** a WiiM Amp Ultra in each stereo room is the simpler house. One app covers everything, nothing depends on the receiver, and no speaker wire runs between rooms. Zone 2 is worth using only if one stereo room is close enough to wire cheaply, and it covers at most one room.


---

## You — 2026-11-09 15:12

Yes, research and write

- _tool: update_plan_ 
- _tool: Bash_ Read the ht-research skill
- _tool: Bash_ Read capture conventions and the manifest tail
- _tool: Write_ /private/tmp/claude-501/-Users-drucev--claude-spares-spare-j1GWM6/df184a1b-8efd-485e-a668-381a49af473d/scratchpad/round2-capture-brief.md
- _tool: Agent_ Capture Sonos sources
- _tool: Agent_ Capture WiiM per-room sources
- _tool: Agent_ Extract receiver zone and HEOS sources
- _tool: update_plan_ 

### Claude — 2026-11-09 15:14

Three research agents are gathering sources in parallel: one on Sonos, one on WiiM's per-room options, and one on the receiver's Zone 2 and HEOS. I'll register what they find, check it, then write the pages.


### Claude — 2026-11-09 15:23

Zone research is in. The X3900H powers only one extra zone. The Onkyo RZ50, by contrast, claims powered Zone 2 and Zone 3, which bears directly on your 9.1 idea. Still waiting on the Sonos and WiiM agents.


### Claude — 2026-11-09 15:29

WiiM research is in, and it contradicts something the wiki says. The $329 WiiM Amp has AirPlay 2, RoomFit and a sub out, while the Amp Ultra the wiki currently recommends for the stereo rooms ($549) has no AirPlay 2. Waiting on Sonos.


### Claude — 2026-11-09 15:30

All three research agents are done. Registering 47 new sources, then spot-checking the numbers that matter most.

- _tool: Bash_ Register round 2 sources and spot-check key claims
- _tool: Bash_ Check round 2 registration and regroup extracts
- _tool: Bash_ Show manifest summary and regroup unknown targets
- _tool: Bash_ Create skeletons for the two new pages and regroup extracts
- _tool: Agent_ Apply round 2 corrections
- _tool: Agent_ Draft Sonos system page
- _tool: Agent_ Draft multiroom comparison page

### Claude — 2026-11-09 15:32

While the agents write, I'm fixing two source dates in the register that the zone agent found wrong.

- _tool: Bash_ Check the two manifest dates against the files
- _tool: Bash_ Correct the two manifest dates
- _tool: Bash_ Fix the Yamaha guide date on the two pages that cite it
- _tool: Bash_ Fix the Onkyo spec sheet date in the bibliography

### Claude — 2026-11-09 15:33

The two source dates are corrected. Waiting on the corrections, Sonos and multiroom agents.


### Claude — 2026-11-09 15:36

The Sonos page is drafted (1,394 words, status contested). Its orphan finding clears once I link it from the index and the comparison page.


### Claude — 2026-11-09 15:37

The comparison page is drafted, and it changes the stereo-room plan. **2 × WiiM Amp + 2 × Edition A10 MKII costs $1,116 and has AirPlay 2.** The Amp Ultra plan costs $1,556 and has no AirPlay 2. Waiting on the corrections agent before committing.


### Claude — 2026-11-09 15:37

Corrections are in. Committing them on their own first, as the procedure requires.

- _tool: Bash_ Commit the correction edits separately

### Claude — 2026-11-09 15:37

Now the threading edits: linking the new pages from the existing ones and updating the stereo-room plan.

- _tool: Agent_ Thread round 2 into existing pages

### Claude — 2026-11-09 15:37

Meanwhile I'm adding the two new pages to the index and the new open questions to the register.

- _tool: Bash_ Find index sections for systems and comparisons
- _tool: Bash_ Add index entries for the two new pages
- _tool: Bash_ Add a reading path and new open questions

### Claude — 2026-11-09 15:38

Index and register are updated. Waiting on the threading agent, then lint, log, commit and push.

- _tool: Bash_ Regenerate stats and matrix, run gates

### Claude — 2026-11-09 15:42

The index went over the 2,000-word ceiling with the two new entries, so I'm shortening every hook from 45 words to 38.

- _tool: Bash_ Trim index hooks and rerun gates
- _tool: Bash_ Log round 2, commit, and push

> _Recap:_ Round 2 is committed and pushed: 47 new sources, corrections committed separately, a multiroom comparison page and a Sonos page. The recommendation now puts a $329 WiiM Amp in each stereo room. Not yet checked: whether the A10 MKII speaker has AirPlay 2, and whether any WiiM speaker is safe for a bathroom.


### Claude — 2026-11-09 15:43

I've researched the multiroom options and added them to the wiki, all committed and pushed. Two new pages, [multiroom options](../hometheater/wiki/comparisons/multiroom-options.md) and [Sonos](../hometheater/wiki/systems/sonos.md), are built on 47 new sources.

## Your 9.1 idea
**The X3900H can power only one extra room.** It has a Zone 2 but no Zone 3. Zone 2 works with the default amp setting and your 5.1 main room, using the Height 2 speaker terminals, and it can play the WiiM's Radio Paradise stream. The manual doesn't mention room correction or a sub output for Zone 2, and it needs speaker wire run from the receiver to that room.

The **Onkyo RZ50** claims powered Zone 2 and Zone 3. But its Zone 3 takes only analog and network sources, so the WiiM's coax output can't reach it.

## Verdict: one WiiM Amp per stereo room

| Route (list prices 2026-11-09, excluding your passive speakers and wire) | Cost |
|---|---|
| **2 × WiiM Amp + 2 × WiiM Edition A10 MKII speakers** | **$1,116** |
| Receiver Zone 2 for one room + 1 WiiM Amp + 2 speakers | $787, cheapest if one room is easy to wire |
| 2 × WiiM Amp Ultra + 2 speakers (the old plan) | $1,556 |
| 2 × Sonos Amp + Era 100 + Roam 2 (+ $499 Port to hear the receiver) | $1,996 to $2,495 |

- **The plan changed from the Amp Ultra to the $329 WiiM Amp.** The Amp has AirPlay 2 (so Apple Music works), Google Cast, RoomFit correction, HDMI ARC and a sub out. It runs in the same app as the WiiM Pro in your main room. The Amp Ultra costs $220 more per room and has no AirPlay 2. The recommendation and my-system pages now say this, with the Amp Ultra kept as the alternative if you want a power rating with published test conditions; the WiiM Amp's 60 W has none.
- **Sonos costs more and loses Radio Paradise FLAC.** Sonos labels its Radio Paradise service "standard quality", below its own CD-quality label, and the Sonos system tops out at 48 kHz. A Port can't wake the X3900H or switch its input. Its one advantage is Apple Music in its own app, up to 24-bit/48 kHz.
- **Bathroom.** No WiiM speaker and no current Denon Home speaker states a water or humidity rating. Only Sonos's portables do: Roam 2 ($179) is IP67, but it would mean a second app.

## Corrections to the existing wiki (committed separately)
- **Sonos and Radio Paradise:** the wiki had read Radio Paradise's own claim as meaning Sonos gets its full-quality stream. Sonos's own label is "standard quality".
- **WiiM models without AirPlay 2:** the wiki listed only two; the Amp Pro and the WiiM Sound speakers lack it as well.
- **WiiM Sound:** now $299; it was unpriced a day earlier.
- **HEOS group sizes:** the streaming page now gives the manual's figures, 32 devices per system and 16 per synchronized group. Denon's buying guide claims "64 zones", which is recorded as a conflict.
- **Source dates:** two were wrong (the Yamaha user guide and the Onkyo spec sheet).

## Still open (questions #38–#46)
- **A10 MKII and AirPlay 2:** two of three statements on its product page list AirPlay 2 and the spec table doesn't. The kitchen and bathroom choice depends on it.
- **Zone 2 in the HEOS app:** whether the X3900H's Zone 2 shows up as a player you can group. Denon's support site was unreachable.
- **Group latency:** the delay when WiiM rooms share a physical input.
- **WiiM Amp power:** the test conditions behind its 60 W rating.


---

## You — 2026-11-09 15:46

how can i export this session ? can I resume in claude code cli?


### Claude — 2026-11-09 15:47

**Resuming in the CLI:** this session's transcript is saved at `~/.claude/projects/-Users-drucev-projects-governance-wiki/df184a1b-8efd-485e-a668-381a49af473d.jsonl`. The CLI finds sessions by the folder they started in, and this one started in `governance_wiki`, not `hometheater`. So run it from there:

```bash
cd ~/projects/governance_wiki
```
```bash
claude --resume df184a1b-8efd-485e-a668-381a49af473d
```

Running `claude --resume` without the ID shows a picker of that folder's sessions. I haven't tested resuming a desktop-app session from the CLI, but it reads the same transcript file.

**Starting fresh in the wiki folder works better.** This session is long and has already been compacted once. The wiki keeps its own state in files: `CLAUDE.md` (the rules), `log.md` (every round), `MANIFEST.md`, `OPEN-QUESTIONS.md`, and the `ht-research`, `ht-lint` and `ht-query` skills. A new session there picks up everything that matters:

```bash
cd ~/projects/hometheater && claude
```

Then ask, for example, "read log.md's latest entries and continue."

**Exporting:**
- In the CLI, `/export` saves the conversation to a text file or the clipboard.
- I can also export this session's transcript from here; just ask.
- The raw transcript is the `.jsonl` file above, which you can copy anywhere.


---

## You — 2026-11-09 15:56

crikey, how do I export the convo as shown in the claude mac app. your compaction messed everything up, the /export is garbage. also tried selecting everything and pasting.

- _tool: ToolSearch_ select:mcp__ccd_session_mgmt__export_transcript
- _tool: Bash_ Inspect the session transcript's record types
- _tool: Bash_ Convert the transcript to readable Markdown and HTML in Downloads