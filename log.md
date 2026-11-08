# log.md

Append-only. Header format `## [YYYY-MM-DD] <op> | <title>`; ops: init, ingest, query, lint,
plan, write, decision. `grep "^## \[" log.md | tail -10` for recent history.

## [2026-11-08] init | scaffold

Repository created per the plan approved 2026-11-08: Karpathy three-layer layout (raw/, wiki/,
CLAUDE.md) with governance_wiki's machinery ported. Scripts adapted: source_manifest.py (raw/),
regroup.py, linkcheck.py and manifest_stats.py (no README page), wiki_lint.py (new kinds,
criteria 1–7, product spec completeness, UNRANKED, 60-day product staleness, marketing-adjective
bans; concern/control reciprocity and crosswalk checks dropped), gen_schema.py, and gen_matrix.py
replacing gen_crosswalk.py. restyle_check.py not ported. Skills: ht-research, ht-lint, ht-query.

Requirements (from the planning interview): 5.1/5.2 speaker layout, open budget, priorities room
correction and music/streaming. Next: interview for start-here/my-system.md, then seed raw/.

## [2026-11-08] write | start-here/my-system.md

Requirements from the interview: no sub owned yet (sub selection in scope), small closed room,
music from Radio Paradise FLAC + Spotify + Apple Music, one room now with four more rooms later
(two stereo, kitchen and bathroom wireless). Radio Paradise FLAC flagged as a discriminating
requirement; first-pass web findings (BluOS native, HEOS via TuneIn without FLAC, Roon AAC
fallback reports) recorded as unverified and logged as OPEN-QUESTIONS #2–4.
Accepted: ORPHAN on my-system.md (1 inbound, from index) until the skeleton creates the
criteria hubs that will link it.

## [2026-11-08] ingest | batch 1 source gathering (81 files)

Four parallel capture agents saved 81 sources to raw/ (manufacturer pages, spec sheets and
manuals; Dirac, Audyssey, ARC, BluOS, MusicCast, HEOS and Radio Paradise docs; ASR, Audioholics,
Sound & Vision and Winer measurements; one AVS anecdote thread). Rows written to
raw/manifest.txt in one serialized pass; source_manifest.py: 81 files, 81 rows, 0 NEW, 0 GONE,
81 UNEXTRACTED (extraction follows the page-plan checkpoint).

Survey findings that change the candidate list (unverified until stage 6):
- Successors: Denon AVR-X3900H/X2900H (2026-05) replace X3800H/X2800H; Marantz CINEMA Series 2
  (2026-08); Arcam Radia AVA15/25/35 replace AVR5/11/21/31; Yamaha AVENTAGE unchanged (new RX500A
  /RX300A below it); Onkyo RZ30/50/70 current, next generation teased for 2027; Pioneer US home AV
  appears to be winding down.
- Ownership: HARMAN (Samsung) owns Denon/Marantz/HEOS/Arcam since 2025-09-23; Gentex owns
  Onkyo/Integra (PAC) since 2025-04-01.
- Dirac is a paid add-on on Denon/Marantz ($259–$799); built in (full bandwidth) on Onkyo with
  Bass Control $299; NAD offers Room Correction only, no Bass Control or ART.
- ASR measures power limiting on Onkyo RZ50, RZ30 and Pioneer LX505 (persisting on Feb 2026
  firmware); Denon X3900H SINAD 102, recommended; NAD T758 V3 SINAD 53.
- Radio Paradise FLAC: native only on BluOS (and Sonos) per RP's and BluOS's own pages; HEOS
  internet radio is MP3/AAC/WMA only; MusicCast and Onkyo have no documented native path.
- BluOS added native Apple Music on 2026-10-20.

Capture defects: dirac.com, support.bluos.net, Sony, Audioholics and radioparadise.com blocked
curl and were captured as rendered page text. Two Radio Paradise files collided between agents;
the lost URL table was re-saved separately. ASR captures carry heavy HTML residue and most
numbers are chart images. Not measured anywhere: Yamaha RX-A4A, Anthem MRX 540, Arcam AVA,
Sony STR-AN1000, NAD T758 V3i, Marantz Series 2, Denon X2900H.

## [2026-11-08] plan | round 1 page plan drafted (checkpoint)

plans/round-1-page-plan.md: 45 pages (7 hubs, 5 concepts, 10 systems, 12 products, 2 seed
comparisons, 3 decision pages, 4 reference pages, requirements page, index). Owner decisions: assume one subwoofer;
an external streamer is acceptable for Radio Paradise FLAC; the 11 receivers approved as listed;
WiiM Amp Ultra added for the future stereo rooms, and the WiiM streamers added as the external
Radio Paradise streamer option alongside Bluesound NODE. Dropped: multiple-subwoofers concept (folded into
bass-management). Batch 2 sources needed: WiiM official pages and any Amp Ultra measurement.
Awaiting approval to seed MANIFEST and build the skeleton.

## [2026-11-08] write | corrections before skeleton

my-system.md: Radio Paradise findings moved from forum reports to primary sources (RP pages, BluOS
support, X3900H manual internet-radio formats). Added the one-sub and external-streamer decisions,
BluOS Apple Music, and the WiiM role. CLAUDE.md layout: Sony DCAC and Google Cast are no longer
standalone system pages; WiiM and Radio Paradise added.
