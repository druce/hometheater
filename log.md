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

## [2026-11-08] ingest | round 1 verification (stage 6)

Eight parallel Sonnet verification agents (groups A–H by page cluster) checked prioritised claims,
covering every front-matter value, every flagged contradiction, and secondary-sourced numbers. Each
claim got two checks: extract fidelity against raw/, and primary confirmation. Evidence:
extracts/verification-r1.md (merged from verification-r1-A…H.md), 163 claim blocks: 112
confirms, 35 partial, 24 unverifiable, 2 contradicts (some blocks carry more than one verdict).
Extract fidelity: no misquotes; the
Yamaha "condensed" rows match raw/ value-for-value (flattened HTML), and string-match misses were
markup or two-column PDF artefacts. 25 new primary captures (v- prefix) registered as batch 3 in
raw/manifest.txt; they are verification evidence, not extraction targets, so source_manifest.py
lists them as UNEXTRACTED by design. Fixed source_manifest.py to stop counting verification-*.md
as extracts (regroup.py already skipped them).

Contradictions and corrections that change drafting:
- FTC 16 CFR 432 (eCFR 2026-10-01; final rule 89 FR 49801, effective 2024-08-12) does NOT require
  all-channels-driven ratings: the floor is the two front channels at 8 Ω, 20 Hz–20 kHz, ≤1% THD.
  Every "FTC" rating in the wiki says nothing about five channels. Contradicts the skeleton's
  assumption in concepts/amplifier-power-ratings.
- Anthem MRX 540: two sub outputs are paralleled (same signal), not independent; power 100 W x 5 at
  1% THD, 2 ch driven, 8 Ω; $1,899.99 in stock; no Roon in current docs.
- Marantz CINEMA 70s S2: Dirac Room Correction only; its two sub outputs carry the same signal;
  internet radio WMA/MP3/AAC ≤48 kHz on both Series 2 models.
- Dirac reconciled from dirac.com (2026-11-08): X3900H/X3800H/CINEMA 50/50 S2 all three products
  paid (RC $259 Limited / $349 Full, BC $299, ART $299); X2900H and 70s S2 RC only; RZ50 and AVA15
  RC included (RZ50 BC $299, no ART; AVA15 BC and ART $299 each). Bass Control works with one sub
  (Dirac), but no source quantifies the single-sub gain.
- X3900H HDMI outputs settled at 3 (2 main + Zone 2). X3800H is a 2022 model, $1,699 launch MSRP.
- Onkyo RZ50: $1,399.99, temporarily out of stock / backorder (rendered onkyo.com 2026-11-08);
  limiter persists across platform, no manufacturer statement or fix; LX505 test load ambiguous
  (post edited from "4 ohm" to "8 ohm"), so the wiki must not claim limiting at 8 Ω from it.
- BluOS: RP on BluOS is MQA, unfolded only in the player; whether a NODE's digital out carries
  plain FLAC is undocumented, which weakens the NODE as the external streamer. WiiM Pro/Pro Plus
  (optical + coax, AirPlay 2) is the better-documented route; RP FLAC by URL on WiiM is
  user-reported only.
- Welti & Devantier (J. AES 2006) independently support Winer: with one sub, seat-to-seat bass
  variation cannot be equalised away; multiple subs are their remedy.
- ASR states SINAD is not perceptually correlated; no audibility threshold comes from ASR.
- Warranties: Denon AVR-X 3 yr; Marantz CINEMA (incl. S2) 5 yr; Onkyo RZ 3 yr (fetched, not saved).

States: 31 pages → verified. Still extracted (sampled, not verified block by block): streaming hub,
connectivity, usability, lossless-streaming-paths, RP comparison, buying-checklist, glossary,
reference/open-questions. OPEN-QUESTIONS.md rewritten with a status column: settled #1, #3, #8,
#11, #15; mostly or partly settled #2, #5, #9, #17; new #18–#32. Several questions can only be
settled by a device test (RP FLAC on WiiM, HEOS play_stream, NODE digital out).

## [2026-11-08] write | batch 1 drafted: 5 concepts, 10 systems (calibration checkpoint)

Five parallel drafting agents (default model) wrote the concept and system pages from their
bundles and verification-r1 only, no web search, to a shared brief carrying the CLAUDE.md voice
rules and a GOOD/BAD example. All 15 pass wiki_lint with zero findings; linkcheck 0 broken.
Body lengths 968–1,499 words; five pages sit within 10 words of the 1,500 target after the agents
cut to fit. Status: 1 settled, 10 contested, 4 unverified; confidence medium throughout.

Claims revised from the skeleton on the evidence: removed an unsourced SINAD audibility
threshold (measurements) and an unsourced "crossover beats correction brand" ranking (bass
management); BluOS no longer the "reference external streamer" (NODE digital out undocumented,
#13); WiiM now names Pro/Pro Plus as the receiver feed; Dirac now gives a priced purchase
recommendation for one sub ($299 where RC is included, $558–$599 on Denon/Marantz); power ratings
lead with the FTC two-channel finding and note that latched protection was also measured on the
Series 1 CINEMA 70s, not only Onkyo/Pioneer; ARC Genesis does not set distances (MRX manual).

Review fixes by the orchestrator: three WiiM Help Center articles that verification read but did
not save were captured (raw batch 4) and the pages re-cited to them; bass-management corrected,
since the Marantz 70s S2 manual (already in raw/) shows the same LFE / LFE + Main menu, and the
agent had marked it unverified; two pages trimmed back under 1,500 after source lines were added.
Two WiiM forum threads remain uncaptured (bot check) and are labelled anecdote on the pages.
Index lines for the 15 pages now carry the drafted claims (first 45 words). MANIFEST: 16 drafted.
Accepted exception: WORDS-HIGH on wiki/index.md (1,604 words). The index is the catalog read first
on every query; its length tracks page count × hook length, and full-claim hooks carry the "but"
clause that a shorter hook drops (tested: a split at ", but" removed the conclusion of
room-modes). Revisit if it passes the 2,000 ceiling, by shortening hooks rather than splitting.

## [2026-11-08] write | batch 2 drafted: 12 product pages

Four parallel drafting agents wrote the product pages to an addendum (claim ≤ ~35 words, ~700-word
aim, link systems/concepts instead of restating them, product front matter in fixed formats from
the verification tables, `contested` only for real source conflicts). Results: 896–1,197 words;
statuses 2 settled, 1 contested (RZ50: list price and limiter frequency), 9 unverified. gen_matrix.py
now fills reference/matrix.md for 12 products with five honest `?` holes: model_year on MRX 540
and Amp Ultra; preouts on X3800H, CINEMA 50 (Series 1) and T 758 V3i.

Cross-checks between batches, resolved against raw/:
- The Denon agent said the "70% Guarantee" belongs only to the X2900H and that the
  amplifier-power-ratings page was wrong to give it to the X3900H. Wrong: the X3900H info sheet and
  product page both carry it. The concept page stands; the X3900H product page gained the row it had
  omitted, and the X2900H row now cites its own info sheet as well as AV Nirvana.
- Marantz agent correct twice: the CINEMA 70s (Series 1) fault condition was 5 W per channel into
  4 Ω (10 W total), now stated per channel on the power page; and the Series 1 CINEMA 50 Audyssey
  tier is XT32 per the compare tile on Marantz's 50 S2 page (line 1777), so audyssey-multeq.md no
  longer says "not confirmed".
- dirac-live.md: $558 (Limited RC + BC) holds only on the X3900H, where Dirac lists Limited and Full
  separately; the claim now gives $599 bundle for the X3800H and Marantz models.
- NAD V3i streaming front matter trimmed to [BluOS, AirPlay 2]; Spotify/TIDAL/Qobuz Connect are
  BluOS platform features no source ties to the V3i (body already said so).
- Onkyo USA warranty captured (raw/v-onkyo-us-warranty.md; RZ Series 3 years parts and labor) and
  cited in place of "fetched, not saved". NAD stock facts read in verification are labelled as not
  captured; Arcam's street price is labelled as search snippets.
Pages pushed over 1,500 words by these corrections were trimmed in the corrected sentences.
MANIFEST: 28 drafted. wiki_lint: 18 judgment findings, all accepted or expected (index catalog
exception; five FM-PRODUCT `?`; 12 WORDS-LOW on undrafted hubs, comparisons, decision, reference).

## [2026-11-08] write | batch 3 drafted: 7 criteria hubs and 2 comparisons

Three agents wrote the hubs and comparisons from the drafted pages only (no web), to an addendum:
claim ≤ ~35 words, minimum/good/best table, tiered ranking in product-link order, unmeasured
models never above measured ones on measurement criteria, WiiM Amp Ultra ranked only in a
stereo-rooms sub-list on hubs 3, 6 and 7. gen_matrix.py regenerated reference/matrix.md with all
seven rankings. Status: hubs unverified (confidence low to medium); Dirac comparison contested
(single-sub Bass Control gain unquantified); RP comparison unverified.

Headline rankings (first place): room correction X3900H (RZ50 second, the cheapest at $1,698.99
with RC included and Bass Control $299); music X3900H (only three candidates measured themselves);
streaming X3900H; amplification X3900H (RZ50 near the bottom for its latched limiter);
connectivity Arcam AVA15 (it and the RX-A4A state input rates); usability CINEMA 50 Series 2 (5-yr
warranty); value X3900H at $2,617 all-in with Dirac RC+BC bundle and a $169 WiiM Pro, with the
backordered RZ50 at $1,868 the only cheaper route to the same target.
Comparisons: RP FLAC → WiiM Pro ($169) on coax; NODE rejected ($680 more, digital out for RP
undocumented). Dirac → buy RC + Bass Control wherever Bass Control is sold.

Fixes found by agents and applied: RZ50 all-in sum $1,698.98 → $1,698.99 and a typo; a stray
Sources bullet my batch 2 insertion placed inside the RZ50 front matter (my script's rfind fell
through to the top of the file) — moved to Sources, and wiki_lint.py gained an FM-STRAY check
(front-matter lines before the first key), SCHEMA regenerated. Agents ran gen_matrix.py out of
turn twice (one reverted with git checkout); the matrix is regenerated here from final hubs.
Not on any drafted page: HARMAN/Gentex ownership (on the value hub only, cited to primaries);
threading it to product pages is a follow-up. New open questions #33–#37.
MANIFEST: 37 drafted. wiki_lint 10 judgment findings, all expected: index catalog exception;
five FM-PRODUCT `?`; three WORDS-LOW on the undrafted decision pages; none on drafted pages.
Next: decision checkpoint (shortlist and recommendation are the owner's call).

## [2026-11-09] decision | shortlist X3900H and RZ50; recommendation X3900H + Dirac RC+BC + WiiM Pro

Owner approved the shortlist of the Denon AVR-X3900H and Onkyo TX-RZ50. Decision pages written
from the drafted hubs and comparisons, no new sources:
- shortlist: the two models side by side; eight eliminations with the deciding fact each; the
  X3800H named as the fallback if the X3900H's price rises by more than $450.
- recommendation: X3900H $1,849 + Dirac RC (Full) + Bass Control bundle $599 + WiiM Pro $169 on
  coax = $2,617 (2026-11-08). The RZ50 ($1,868) is conditional on 8 Ω speakers, acceptance of a
  months-long backorder and of a 2020 platform; what would change the choice is listed.
- buying-checklist: price, dealer and return-window checks before paying; firmware, sub placement,
  XT32 baseline then Dirac preset, Stereo not Pure Direct, WiiM Fixed Volume/EQ off, and device
  tests #10, #23, #22 plus the Google Cast fallback after unboxing.

## [2026-11-09] write | reference pages: glossary, bibliography, open questions

Two agents, wiki pages and raw/manifest.txt only. Glossary: 62 terms, each linked to its page;
eARC is defined in the agent's words with no new fact; target curve links to dirac-live.md because
no target-curves concept page exists. Bibliography: 119 of the registered sources, the ones wiki
pages cite, with "Read these first" (7). Four registered sources are cited by no page:
onkyo-pioneer-home-usa-warranty.md, onkyo-press-2024-rebirth-ownership.md,
v-asr-limp-mode-debunked.md, v-wiim-faq-supported-services.md. Open questions: reader-facing,
grouped as could change the recommendation (5), settled by a device test (5), would not change the
choice (19).
Matrix skeleton line removed. Index hooks refreshed from the new claims.

## [2026-11-09] lint | round 1 closed

All 45 MANIFEST rows set to audited. wiki_lint: 7 judgment findings, all accepted:
- index.md WORDS-HIGH (1,796): catalog exception, logged 2026-11-08.
- bibliography.md WORDS-CEIL (2,558): accepted as a catalog exception on the same reasoning. The
  length is 119 entries with URLs; splitting a bibliography costs more navigation than it saves.
- Five FM-PRODUCT `?` values (Anthem and WiiM Amp Ultra model_year; X3800H, CINEMA 50 and NAD
  pre-outs). These are unresolved in the sources and stay `?` (#21, #34).
linkcheck: 0 broken, 0 orphans.
Follow-ups not done: thread HARMAN/Gentex ownership onto product pages; capture the X3800H info
sheet, CINEMA 50 S1 docs and RZ50 manual; decision/setup-and-calibration.md; owner device tests;
the four uncited sources.

## [2026-11-09] write | decision/setup-and-calibration.md

New decision page, written from the drafted concept and system pages with no new sources: sub
placement first (wall midpoint per Welti and Devantier), 5.1 layout and 80 Hz starting crossover,
Audyssey XT32 into Preset 1 as a free baseline, Dirac RC + Bass Control into Preset 2 with a tight
position cluster (Winer: the improvement fades within about 2 ft), peaks cut and boosts held to
about 5 dB, A/B by preset, Stereo rather than Direct/Pure Direct, WiiM Pro Fixed Volume on and EQ
off. Status unverified until it is run in the room. Inbound from recommendation, buying-checklist
and index. The index is now 1,947 words with the refreshed hooks and the new row, still under the
2,000 ceiling and covered by the catalog exception. wiki_lint unchanged at 7 accepted findings.

## [2026-11-09] ingest | round 2: multiroom options (receiver Zone 2, WiiM per room, Sonos)

Owner asked whether the wiki covers feeding the future rooms (two stereo rooms, kitchen, bathroom)
and raised using a 9-channel receiver to power two stereo zones. Survey before writing: the wiki
covered app fragmentation and named the WiiM Amp Ultra for stereo rooms; nothing on receiver zones,
wiring or Sonos.

Sources: 47 new files (r2- prefix), captured by three agents: 7 Denon/HEOS, 22 WiiM/Google/Amazon,
18 Sonos/Spotify/press; plus extracts from the X3900H manual, RZ50 spec sheet, RX-A4A guide and HEOS
CLI spec already in raw/. support.denon.com was unreachable (Oracle error, 403, EU bot check), so no
HEOS support article was captured. Agents checked every extract quotation against its raw file.

Findings that decide the question:
- X3900H has Zone 2 only, no Zone 3, so it cannot power two extra stereo rooms. Powered Zone 2
  comes from the HEIGHT2 terminals under the default Amp Assign with a 5.1 main room; coax/optical
  2ch PCM only (the WiiM qualifies); no stated room correction or sub in Zone 2. The RZ50 spec sheet
  claims powered Zone 2 and Zone 3, but Zone 3 takes analog and network only.
- The $329 WiiM Amp has AirPlay 2, Cast and RoomFit; the Amp Pro ($399), Ultra and Amp Ultra do not
  have AirPlay 2. WiiM groups cap at 16 devices and 48 kHz/16-bit; Cast/Roon into a group play on
  the lead only.
- Sonos labels its Radio Paradise service "standard quality", below its CD-quality label; system
  ceiling 48 kHz; Port $499 cannot wake or switch the X3900H.
- No WiiM speaker and no current Denon Home speaker states a humidity or IP rating; only Sonos
  portables do (Roam 2 and Play IP67, Move 2 IP56).

Corrections, committed first ("fix: round 2 corrections"): Sonos RP quality on radio-paradise.md;
WiiM Sound now $299 and the AirPlay-2-less WiiM list on wiim.md, streaming-protocols.md and the RP
comparison; HEOS 32 per system / 16 per group plus the "64 zones" marketing conflict; Yamaha RX-A4A
user guide date 02/2025 and Onkyo RZ50 spec sheet date 2020 in manifest.txt, ypao.md, bibliography.

New pages (owner approved "research and write" for the comparison; systems/sonos.md added as the
canonical home for Sonos facts so the comparison links rather than restates): comparisons/
multiroom-options.md (verdict: WiiM Amp per stereo room plus WiiM speakers, $1,116; Zone 2 hybrid
$787 if one room is cheap to wire; Sonos $1,996 to $2,495 and loses RP FLAC) and systems/sonos.md.

Threading: recommendation and my-system now name the WiiM Amp ($329) per stereo room with the Amp
Ultra as the alternative; streaming hub, wiim.md (six tier rows, multiroom limits), heos.md (input
sharing, Denon Home ratings), X3900H and RZ50 zone notes, Amp Ultra page, RP comparison.

Conflicts shown, not resolved: Sonos line-in product lists (three pages differ), Sonos Amp Wi-Fi
bands, Port output caption, WiiM Amp SNR 98 vs 108 dB, Edition A10 MKII AirPlay 2 (two of three page
statements list it, #45, and the recommendation's kitchen/bath speaker depends on it).
Open questions #38–#46 added. Index hooks shortened to 38 words to stay under the ceiling.
wiki_lint: 13 judgment findings. Accepted: index and bibliography catalog exceptions, five
FM-PRODUCT `?`. New WORDS-HIGH soft-target findings on six pages (1,214–1,945, all under the 2,000
ceiling) come from this round's additions and are accepted rather than cut. linkcheck clean.
