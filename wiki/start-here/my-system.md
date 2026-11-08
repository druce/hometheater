---
title: "My system: requirements"
slug: my-system
kind: reference
criteria: [1, 2, 3, 4, 7]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [radioparadise-ways-to-listen.md, radioparadise-stream-links-url-table.md, bluos-support-radio-paradise-articles.md, bluos-apple-music-support-2026-10-20.md, denon-avr-x3900h-owners-manual-na.pdf]
---

# My system: requirements

**The receiver has to run a 5.1 system with one subwoofer in a small closed room, with room correction and music quality ranked first. Radio Paradise FLAC can come from an external streamer, so the receiver is judged on its own merits.** Every ranking in this wiki is relative to this page. Change it here first when a requirement changes.

## Captured 2026-11-08 (planning interview and plan checkpoint)

| Area | Requirement | Consequence for the receiver |
|---|---|---|
| Layout | 5.1 with one subwoofer (owner decision, 2026-11-08) | Seven amp channels are more than enough. A second independent sub output is a nice-to-have, not a requirement. Height channels are out of scope, so Atmos processing counts for nothing here. |
| Subwoofer | None owned yet. Assume one; choosing it happens outside this round | Room correction has to integrate one sub well (bass management, sub/main alignment). Dirac Bass Control is judged on what it does for a single sub. |
| Room | Small closed room (under about 2,500 cu ft) | Amp power is unlikely to be the limit with typical speakers. Room modes will dominate the bass, so room correction quality matters more than watts. |
| Budget | Open | Rank on merit first, then price each step up against what it buys. |
| Priorities | Room correction; music and streaming | Criteria 1, 2 and 3 carry the most weight. |
| Music sources | Radio Paradise lossless FLAC; Spotify; Apple Music | Spotify Connect and AirPlay 2 are table stakes. Radio Paradise FLAC may come from an external streamer (owner decision, 2026-11-08). |
| Multiroom, now | One room only | Not a factor today. |
| Multiroom, future | Two more rooms with stereo speakers, plus one wireless speaker each in the kitchen and bathroom | A WiiM Amp Ultra is the candidate for the stereo rooms. One app across the main-room streamer, the stereo rooms and the wireless speakers counts in the streaming criterion. |

## Radio Paradise FLAC: where it plays

Radio Paradise publishes FLAC streams for each of its mixes, for example `http://stream.radioparadise.com/flac` (Radio Paradise stream-links page, captured 2026-11-08). These findings are from primary sources and are still awaiting verification:

- **BluOS:** Radio Paradise is built into the BluOS app, and Radio Paradise calls BluOS its best-sounding option (Radio Paradise "Ways to Listen"; BluOS support articles). BluOS added native Apple Music on 2026-10-20 (Lenbrook announcement).
- **HEOS (Denon, Marantz):** Radio Paradise is not in the HEOS service list. The AVR-X3900H manual lists internet radio formats as WMA, MP3 and AAC only, so HEOS internet radio cannot carry the FLAC stream.
- **MusicCast (Yamaha), Onkyo/Pioneer, Anthem:** no native lossless Radio Paradise path is documented. Roon, or casting or AirPlaying the Radio Paradise app (ALAC on iOS), may work but is untested.
- **WiiM:** owners report a built-in Radio Paradise option that plays lossless, and a custom-URL route that loses track metadata. These are forum reports awaiting WiiM's own documentation.

Since an external streamer is acceptable, the plan of record is: any receiver plus a WiiM or BluOS streamer on a digital input.

## Still unknown

- Speaker models, sensitivity and impedance (front L/R, center, surrounds).
- Exact room dimensions, and where the listening position and sub can go.
- Display and sources (TV model, eARC, consoles), plus any vinyl.
- Whether the future stereo rooms use passive speakers on a WiiM Amp Ultra (assumed) or something else.
- Tolerance for paid room-correction upgrades (for example a Dirac license) and for calibration effort.
