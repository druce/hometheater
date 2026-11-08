# Round 1 page plan (checkpoint, awaiting approval)

Drafted 2026-11-08 from the 81 batch-1 sources (`raw/manifest.txt`). Nothing has been written to
`wiki/` or `MANIFEST.md` yet. Once this is approved, the rows are seeded as `planned`, the skeleton is
built, and that is the second checkpoint.

**45 pages total:** 1 requirements page, 7 criteria hubs, 5 concepts, 10 systems, 12 products,
2 seed comparisons, 3 decision pages, 4 reference pages, plus the index.

## Products (11): which receivers get a page

The selection rule is that a model gets a page if it is current or still sold new, covers 5.1/5.2,
and is a realistic winner on at least one priority criterion. Prices are the manufacturers' US list
prices captured on 2026-11-08.

| Page | Price | Why it is in | Main question it must answer |
|---|---|---|---|
| `denon-avr-x3900h` | $1,849 | XT32 + 4 sub outs, full Dirac suite eligible, ASR SINAD 102 recommended | Front-runner on measurements. Is Dirac worth the add-on cost? |
| `denon-avr-x3800h` | $1,399 (was $1,799) | Prior generation, same Dirac eligibility, discounted | Value against the X3900H, given ASR SINAD 87 |
| `denon-avr-x2900h` | $1,349 | Cheapest new Denon worth considering | XT (not XT32), and no Dirac Bass Control. Too limiting? |
| `marantz-cinema-70s-series-2` | $1,500 | Slim music-oriented 7.2 model | 50 W. Dirac Room Correction only. The Series 1 4 Ω distortion fault, does it carry over? |
| `marantz-cinema-50-series-2` | $3,000 | XT32, full Dirac suite, 9.4 channels | What does it buy over the X3900H for 5.1? |
| `marantz-cinema-50` | $2,499 | Series 1, discounted, full Dirac eligible | Same as above, cheaper; only a member review measures it |
| `yamaha-rx-a4a` | ? | YPAO, MusicCast; the AVENTAGE line is unchanged | YPAO only, no Dirac path. Radio Paradise FLAC unlikely |
| `onkyo-tx-rz50` | ? | Dirac Live full bandwidth included, Bass Control $299 | The ASR power-limiting finding, which persists on the Pioneer sibling's Feb 2026 firmware |
| `anthem-mrx-540-8k` | ? | ARC Genesis, 5 amplified channels and 7.2 processing, an exact 5.1/5.2 fit | No measurement of the 540 itself; the 740 and 1140 are proxies |
| `nad-t-758-v3i` | $2,299 | The only receiver with BluOS built in, so Radio Paradise FLAC is native; Dirac included | The V3 measured SINAD 53, V3i unmeasured, 4K-only HDMI, no Bass Control |
| `wiim-amp-ultra` | ~$549 (best guess, retailer) | Added at the owner's request 2026-11-08. A stereo streaming amp: 100 W per channel at 8 Ω, RoomFit room correction, one sub out, HDMI ARC (eARC unverified), native Radio Paradise lossless (owner reports) | Role (owner, 2026-11-08): the two future stereo rooms only, not a main-room 2.1 alternative. Ranked in `criteria/streaming-and-multiroom` and not against the 5.1 receivers. Not measured yet |
| `arcam-ava15` | $4,499.95 | Open budget: full Dirac included, Bass Control and ART available, Roon Ready | Is the premium justified for a small 5.1 room? No measurements yet |

## Hubs, concepts, systems

**Criteria hubs (7)**, exactly as in CLAUDE.md §Spine. Every product above is ranked in at least
the hubs for criteria 1, 2 and 3.

**Concepts (6):**
- `bass-management-and-crossovers`: LFE, crossover points and slopes, sub/main alignment, and
  integrating one sub, with a short section on what a second sub would add.
- `room-modes-and-correction-limits`: why EQ can tame peaks but not fill nulls, and how the
  correction degrades from seat to seat. The source is Winer's Dirac measurements.
- `amplifier-power-ratings`: rated against measured watts, channels driven, load, and protection or
  power-limiting modes (the Onkyo/Pioneer finding).
- `measurements-and-audibility`: what SINAD and pre-out voltage mean, and where the numbers stop
  mattering. This keeps ASR scores in proportion.
- `lossless-streaming-paths`: FLAC, AAC, ALAC over AirPlay, MQA, and the difference between
  Connect, Cast, AirPlay and a native service. The Radio Paradise requirement hangs on this page.

**Systems (9):**
- Room correction: `audyssey-multeq` (XT, XT32, MultEQ-X), `dirac-live` (Room Correction tiers,
  Bass Control and ART as anchored sections, with prices), `arc-genesis`, `ypao`.
- Streaming: `heos`, `musiccast`, `bluos` (including NODE / NODE NANO as the external-streamer
  option), `streaming-protocols` (AirPlay 2, Google Cast, the Spotify/Tidal/Qobuz Connect family,
  Roon Ready), `wiim` (WiiM Home, RoomFit, the Ultra / Pro Plus / Mini streamers as the cheaper
  alternative to a NODE, and the Amp line), and `radio-paradise` (its streams, codecs, and which
  platforms carry FLAC).

## Comparisons, decision, reference

- **Seed comparisons (2)**, written after the products:
  - `radio-paradise-flac-native-vs-external-streamer`: a BluOS receiver against any receiver plus a
    WiiM streamer or a NODE.
  - `which-dirac-license-to-buy`: Limited or Full, and whether Bass Control is worth $299 with one
    sub in a small room.

  More will come from queries.
- **Decision (3):** `shortlist`, `recommendation`, `buying-checklist`.
  `setup-and-calibration` waits until a receiver is chosen.
- **Reference (4):** `glossary`, `matrix` (generated), `bibliography`, `open-questions`.

## Corrections to existing pages

- `start-here/my-system.md`: change the Radio Paradise bullets from first-pass forum findings to the
  primary sources (Radio Paradise's own pages, BluOS support, the X3900H manual's internet-radio
  formats), and add BluOS's native Apple Music (2026-10-20).
- `CLAUDE.md` layout examples: drop "Sony DCAC" and "Google Cast" as standalone system pages. They
  fold into a section and `streaming-protocols` (see below).

## Deliberately not added, and why

- **Sony STR-AN1000 / ES models:** no Dirac path, no independent measurements, and DCAC is
  documented only at feature level. DCAC gets a paragraph in `criteria/room-correction.md` instead
  of a page. It can be added if the owner wants it considered.
- **Denon X4800H, Marantz CINEMA 40/30/60, Anthem MRX 740/1140, NAD T 778:** these are 9-to-15
  channel models priced for channels a 5.1 room doesn't use. Their measurements are still used as
  proxies on sibling pages. The X4800H could come back if Bass Control's multi-sub handling turns out
  to need it.
- **Onkyo TX-RZ30, Pioneer VSX-LX805, Integra:** these share the RZ50 platform and its
  power-limiting finding, so they are covered in the RZ50 page's "Known issues" section.
- **Yamaha RX500A / RX300A:** new, but below AVENTAGE. YPAO is unnamed on the page and the
  streaming stack is unclear. They wait for more sources.
- **Arcam AVA25/35:** the AVA15 already tests whether Arcam is worth its premium.
- **"Why 5.1 skips height channels":** under 300 words, so it becomes a line in `my-system.md`.
- **Separate Dirac Bass Control and ART pages:** they are anchored sections in `dirac-live`.
  They can split later if that page passes 1,500 words.
- **Subwoofer pages, and a `multiple-subwoofers` concept:** the owner chose to assume one sub
  (2026-11-08). Second-sub value becomes a section of `bass-management-and-crossovers`, and Bass
  Control is weighed for one sub only.

## Owner decisions (2026-11-08)

1. **Subwoofer:** assume one sub. No subwoofer section this round.
2. **Radio Paradise FLAC:** an external streamer is acceptable. Criterion 3 ranks receivers on their
   own streaming. Radio Paradise FLAC is met by the chain (a receiver plus a WiiM or BluOS
   streamer), so NAD's native BluOS is a convenience rather than a gate.
3. **Products:** the 11 approved as listed, plus `wiim-amp-ultra` added at the owner's request.
4. **WiiM's role:** (a) the Amp Ultra goes in the two future stereo rooms; (b) the WiiM streamers
   (Ultra, Pro Plus, Mini) are candidates for the external Radio Paradise FLAC streamer feeding the
   receiver, next to the Bluesound NODE / NODE NANO. A WiiM-based 2.1 main room is out of scope.
   A shared WiiM Home (or BluOS) app across the main-room streamer, the stereo rooms, and the
   kitchen and bathroom speakers becomes an explicit multiroom criterion.

## Sources still needed before extraction (batch 2)

WiiM's official pages: the Amp Ultra spec page and manual, the RoomFit documentation, the WiiM Home
service list and Radio Paradise integration, and the WiiM Ultra / Pro Plus / Mini streamer specs.
Also any independent measurement of the Amp Ultra (ASR has reviewed earlier WiiM amps).
The current evidence for native Radio Paradise lossless on WiiM is
[WiiM forum owner reports](https://forum.wiimhome.com/threads/radio-paradise-losless-flac.8399/),
marked as anecdote.

## Next steps after approval

1. Seed the `MANIFEST.md` rows as `planned`.
2. Build the skeleton: front matter, claim line, headers and links for all 44 pages, with the link
   graph green. This is checkpoint 2.
3. Extract with parallel subagents (writing only to `extracts/`), then run `regroup.py`, then verify
   against primary sources.
