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

## [2026-11-08] write | round 1 skeleton (45 pages, checkpoint 2)

Generated all planned pages from plans/round-1-page-plan.md with a one-shot generator: front matter
(status unverified, confidence low, product spec keys '?'), a draft bold claim, required section
headers each with a one-line note, and the link graph (index → hubs → concepts/systems/products;
products ↔ systems; every page ≥2 inbound). MANIFEST seeded, 45 rows at state skeleton;
manifest_stats.py and gen_matrix.py run.
Gates: linkcheck 0 broken, 0 orphans. wiki_lint 51 judgment findings, all expected at skeleton and
accepted until drafting: WORDS-LOW ×39 (no prose yet) and FM-PRODUCT ×12 (specs stay '?' until
verified). Draft claims carry survey numbers (e.g. X3900H SINAD 102) that are unverified until
stage 6.

## [2026-11-08] ingest | batch 2: WiiM (13 files)

Registered 13 WiiM sources plus 7 ASR chart images in raw/assets/. Contradictions with the
skeleton, corrected in draft claims: WiiM's own pages say the Amp Ultra and WiiM Ultra do NOT
support AirPlay 2 (Mini, Pro, Pro Plus do), and no WiiM device lists native Apple Music, so
streaming-protocols' "every candidate supports AirPlay 2" and the WiiM page's claim were wrong.
WiiM documents Radio Paradise as an integrated service only for its PC app; mobile-app lossless
is forum-reported only. Amp Ultra: $549, HDMI ARC only (no eARC), no DTS, sub out 2 Vrms;
ASR (2025-12-29) recommended, SINAD ~99.9 dB optical at 5 W, ~97 W/ch 8 Ω and ~168 W/ch 4 Ω both
channels driven. WiiM Ultra ASR line-out SINAD ~115 dB. WiiM Sound speaker "Coming Soon", no
IP rating found. Raises an owner decision: the Apple Music requirement vs WiiM for stereo rooms.

## [2026-11-08] ingest | round 1 extraction (stage 4) and regroup

12 parallel Sonnet extraction agents, grouped by brand/source type (8 sources each on average,
one extract file per source) rather than one agent per source, for cost. Every source read in
full except three long manuals read partially with page ranges recorded (X3900H 337 pp, RX-A4A
415 pp, Sony help guide 361 pp). Orchestrator wrote extracts/extractor-reports.md from the agents'
reports. Fixes: an empty stray extract (iim-mini-product-page.md) removed; two entries retargeted
from a non-existent criteria/measurements-and-audibility.md to concepts/. Result: 94 sources,
94 extracts, 1,771 entries, 39 page bundles; source_manifest.py 0 NEW/GONE/UNEXTRACTED; regroup
0 unknown targets. 39 MANIFEST rows → extracted; the 5 empty bundles (my-system, shortlist,
recommendation, matrix, bibliography) are expected, since those pages are written from the rest.

Extract-quality caveats for stage 6: the Yamaha group condensed some spec-table rows (A4A spec
page and user guide pp.394, 400-408) rather than quoting strictly; Onkyo spec-sheet quotes were
reassembled from two-column PDF text; ASR AVR numbers are mostly in uncaptured chart images.

Contradictions found (to triage and verify):
- WiiM Amp Ultra has no S/PDIF or line output (manual), so it cannot be the external streamer;
  only WiiM Pro/Pro Plus (optical + coax, AirPlay 2) can feed a receiver. Product-page "analog
  line out or bit-perfect digital output" is template copy.
- BluOS Radio Paradise MQA unfolds only in the BluOS player and cannot pass to an external DAC;
  whether a NODE sends plain FLAC from RP over its digital out is unconfirmed.
- Onkyo/Pioneer power limiting: confirmed on RZ50, LX505 (2023 and 2026) and RZ30; latched
  until AC removed; no firmware note addresses it. Exposure in a 5.1 small room is unquantified.
- Manufacturer Dirac pages are stale (Denon omits X3900H/X2900H; Marantz lists only Series 1);
  dirac.com is current. Dirac price depends on device context; NAD's included Dirac is limited.
- Denon X3900H internet radio is MP3/WMA/AAC only (manual), confirming the external-streamer plan.
- Anthem MRX 540: no conditioned power rating, and dual sub outs listed only for the 1140 (2022
  sheet); MRX 1140 loses ~10 dB SINAD with the sub output disabled.
- Yamaha: two sub outputs carry the same signal; "YPAO: Low Frequency" leaves Q and gain manual.
- Every manufacturer power rating found is 1–2 channels driven; no source gives a five-channel
  figure, so "70% to five channels" (Denon) is unmeasured.

NO-HOME (77 entries): Sony product specs (out of scope by plan); Marantz siblings' prices
(CINEMA 60 S2 $2,000, 60 $1,399, 40 $3,800, 30 $4,800); ownership/corporate background; ASR
methodology and limp-mode discussion; WiiM and Bluesound speakers for kitchen/bathroom (Sound
Lite $229, Pulse Flex $429); Zone 2 from internal amps; AVR Bluetooth transmit (SBC). Candidate
additions to argue at the next plan checkpoint, not created: products for the external streamer
(WiiM Pro Plus, Bluesound NODE), a kitchen/bathroom speaker comparison, CINEMA 60 Series 2,
decision/setup-and-calibration (home verification of correction).
