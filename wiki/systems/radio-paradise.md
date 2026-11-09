---
title: "Radio Paradise"
slug: radio-paradise
kind: system
criteria: [3]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [radioparadise-ways-to-listen.md, radioparadise-faqs-and-info.md, radioparadise-stream-links.md, radioparadise-stream-links-url-table.md, bluos-support-radio-paradise-articles.md, denon-avr-x3900h-owners-manual-na.pdf, v-marantz-cinema-70s-series-2-owners-manual-selected.md, v-marantz-cinema-50-series-2-owners-manual-selected.md, marantz-cinema-70s-series-2-info-sheet-na.pdf, marantz-cinema-50-series-2-info-sheet-na.pdf, onkyo-tx-rz50-spec-sheet.pdf, yamaha-rx-a4a-user-guide.pdf, yamaha-musiccast-supported-services.md, arcam-ava15-product-page.md, wiim-home-pc-app-help.md, wiimforum-radio-paradise-lossless.md, r2-sonos-music-service-pages.md, r4-wiim-http-api-for-wiim-products.pdf]
---

# Radio Paradise

**Radio Paradise publishes a free FLAC stream for each of its eight channels, but among the candidate receivers only the NAD T 758 V3i (BluOS) carries the service natively, the HEOS manuals checked (Denon X3900H, Marantz CINEMA Series 2) list lossy internet-radio formats only, and the rest are undocumented, so FLAC comes from the external streamer; station-directory routes such as TuneIn give lower quality and no skipping by RP's own account.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md).

## What it does

Radio Paradise is a listener-supported internet station with no ads, subscription or degraded free tier (RP FAQ, 2026-11-08). It reaches a system three ways, of unequal quality:

1. **A dedicated integration** in a player platform or app: BluOS, Sonos, the RP iOS and Android apps, Alexa, TV apps. RP says these carry its higher-quality streams, though Sonos labels its RP service standard quality; on Sonos and BluOS they add skip and pause.
2. **A station directory** (TuneIn, vTuner, airable) inside a receiver's internet-radio input. RP says that on Sonos the default TuneIn route works but misses skip and pause and the highest-quality audio, and that TuneIn has been inserting pre-roll ads RP does not want (RP FAQ). The directories do not state which RP codec they carry.
3. **A stream URL** pasted into any player that accepts one, chosen on RP's stream-links page by channel and bitrate.

On BluOS, an RP login adds thumbs up and down and, after 100 thumbs up, a personal "My Paradise" mix (BluOS support).

**Stream links.** All URLs are plain `http://`, not https (RP stream-links page, captured 2026-11-08). RP offers three FLAC variants: plain, with metadata (`flacm`), and "processed for background listening" (`flacbg`), the last undescribed. RP's pages give no bit depth or sample rate for its FLAC; WiiM forum users put it at 16/44.1.

| Channel | FLAC | FLAC + metadata | Other options |
|---|---|---|---|
| Main Mix | `stream.radioparadise.com/flac` | `/flacm` | `/flacbg`; AAC 32–320k, MP3 192k, Ogg Vorbis 192k |
| Mellow Mix | `/mellow-flac` | `/mellow-flacm` | `/mellow-flacbg`; AAC, MP3 |
| Rock Mix | `/rock-flac` | `/rock-flacm` | `/rock-flacbg`; AAC, MP3 |
| Global Mix | `/global-flac` | `/global-flacm` | `/global-flacbg`; AAC, MP3 |
| Beyond... | `/beyond-flac` | `/beyond-flacm` | `/beyond-flacbg`; AAC, MP3 |
| Serenity | `/serenity-flac` | none | 64k AAC+ only |
| Radio 2050 | `/radio2050-flac` | `/radio2050-flacm` | no `flacbg`; AAC, MP3 |
| KFAT | `/kfat-flac` | `/kfat-flacm` | `/kfat-flacbg`; AAC, MP3 |

RP's FAQ, its stream-links page and BluOS name the rock and global channels differently, and BluOS lists My Paradise and KFAT but not Radio 2050.

## Versions and tiers

Every route is free; quality varies, and RP states it for only some platforms.

| Platform | How it is added | Quality per RP's own pages (2026-11-08) |
|---|---|---|
| [BluOS](bluos.md) (Bluesound, NAD) | Built into the BluOS app | MQA, from 24-bit masters when available; RP calls it its best-sounding option. The MQA unfold happens only in the BluOS player and is not passed to an external DAC (BluOS support) |
| Sonos | Phone app, Settings, Add a Service | RP: highest quality, relative to the default TuneIn route, which cannot skip. Sonos: "standard quality", below its CD-quality (16/44.1) and hi-res labels (Sonos, 2026-11-09). Codec unstated by either |
| RP iOS app | App Store | ALAC (lossless) or AAC, set in the app; AirPlay to AirPlay 2 devices |
| RP Android app | Play Store or APK | Codec not stated; owner reports say casting is lossless when the app is set to FLAC (WiiM forum, 2025) |
| Alexa skill | Voice | Five levels, low to lossless; does not work with multi-speaker groups |
| TV apps (Apple TV, Fire TV, Roku, Sony or Google TV) | TV app store | Codec not stated |
| Wi-Fi radios and receivers | Station directory, or stream URL | Directory codec not stated; the URL route gives the chosen bitrate |
| [WiiM](wiim.md) | Built into the WiiM PC app per WiiM's help article; owners report it in the phone app | Not stated by WiiM; owner-reported lossless (open question #10) |

RP advises against its Windows desktop app. In the UK, RP is unavailable through TuneIn and Sonos Radio over a licensing dispute, though its own Sonos service works (RP FAQ).

## Measured and observed results

No measurement of any RP stream exists in the evidence; the table below rests on manuals, spec sheets and owner reports. The receiver's own path matters less since the owner accepted an external streamer (2026-11-08). The external path in every row is a WiiM Pro or Pro Plus, or a Bluesound NODE, on coax or optical. The user-reported 44.1 kHz rate is within every documented coax and optical input limit, though several candidates document none (open question #12).

| Candidate | Platform | RP FLAC on the receiver itself | Evidence |
|---|---|---|---|
| [NAD T 758 V3i](../products/nad-t-758-v3i.md) | BluOS | **Native** (MQA-encoded; whether plain FLAC is also offered is undocumented) | RP "Ways to Listen" names NAD hardware; BluOS support |
| [Denon AVR-X3900H](../products/denon-avr-x3900h.md) | HEOS | **No**: internet radio plays WMA, MP3 and AAC only; RP is not in the HEOS service list | X3900H manual pp.285, 303 |
| [Denon AVR-X3800H](../products/denon-avr-x3800h.md) | HEOS | Unknown, expected no: same platform, internet-radio format table not captured | — |
| [Denon AVR-X2900H](../products/denon-avr-x2900h.md) | HEOS | Unknown, expected no: same platform, not checked | — |
| [Marantz CINEMA 70s Series 2](../products/marantz-cinema-70s-series-2.md) | HEOS | **No**: internet radio (TuneIn) plays WMA, MP3 and AAC only | Owner's manual; info sheet |
| [Marantz CINEMA 50 Series 2](../products/marantz-cinema-50-series-2.md) | HEOS | **No**: same format table | Owner's manual; info sheet |
| [Marantz CINEMA 50](../products/marantz-cinema-50.md) | HEOS | Unknown, expected no: not checked | — |
| [Onkyo TX-RZ50](../products/onkyo-tx-rz50.md) | Onkyo network (TuneIn) | Unknown: FLAC file playback to 192/24, no internet-radio format list, no RP client | RZ50 spec sheet |
| [Yamaha RX-A4A](../products/yamaha-rx-a4a.md) | [MusicCast](musiccast.md) (airable) | Unknown: one 2024 forum claim of RP FLAC via airable, no Yamaha statement (#16) | A4A user guide p.151 |
| [Anthem MRX 540 8K](../products/anthem-mrx-540-8k.md) | AirPlay, Chromecast | Unknown: no RP client; casting from the RP app is untested | Anthem product page (live, read in verification) |
| [Arcam AVA15](../products/arcam-ava15.md) | Radia app | Unknown: internet radio and FLAC listed, RP not named | AVA15 product page |
| [WiiM Amp Ultra](../products/wiim-amp-ultra.md) | WiiM | Owner-reported native lossless (#10) | WiiM forum; WiiM PC-app help |

Three possible workarounds on HEOS receivers are documented but untested: the RP iOS app's ALAC over AirPlay 2, where the only stated ceiling is WiiM's 44.1 kHz/16-bit claim and Apple's own documentation is missing (#24); Roon Ready; and the HEOS CLI's play-URL command pointed at the FLAC stream (#9, #22). The bigger unknown on the reference streamer is what a Bluesound NODE sends out its coax for RP, since the service is MQA and BluOS documents no plain-FLAC variant (#13).

## Limits

- **Directory routes are the lossy default.** A receiver's TuneIn, vTuner or airable entry for RP states no codec; RP's Sonos guidance and WiiM owner reports both treat directories as lower quality, without skip, and TuneIn adds pre-roll ads.
- **The URL route needs a player that accepts a custom http FLAC URL.** HEOS offers URL play only through its CLI or a third-party app (#9); on WiiM, the HTTP API v1.2 documents URL playback and uses RP's `flacm` URL in a preset example, but whether a Pro plays RP's FLAC lossless that way and holds 16/44.1 out the coax is untested (#10, #23).
- **BluOS MQA stays in the BluOS device.** It cannot be unfolded by an external DAC or receiver (BluOS support), which matters for a NODE feeding a receiver.
- **`flacbg` is processed** in an undocumented way; avoid it in the main room.

Cost of native RP versus receiver plus streamer: [Radio Paradise FLAC: native vs external streamer](../comparisons/radio-paradise-flac-native-vs-external-streamer.md). Stream-to-DAC chain: [lossless streaming paths](../concepts/lossless-streaming-paths.md). AirPlay 2 and Cast: [streaming protocols](streaming-protocols.md).

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Radio Paradise, Ways to Listen, 2026-11-08 — `radioparadise-ways-to-listen.md`
- Radio Paradise, FAQs and Info, 2026-11-08 — `radioparadise-faqs-and-info.md`
- Radio Paradise, Stream Links page, 2026-11-08 — `radioparadise-stream-links.md`
- Radio Paradise, Stream Links generated URL table, 2026-11-08 — `radioparadise-stream-links-url-table.md`
- BluOS Support, Radio Paradise Advanced Features and Radio Paradise in MQA, captured 2026-11-08 — `bluos-support-radio-paradise-articles.md`
- Denon, AVR-X3900H Owner's Manual (NA) — `denon-avr-x3900h-owners-manual-na.pdf`
- Marantz, CINEMA 70s Series 2 Owner's Manual, selected pages, 2026-11-08 — `v-marantz-cinema-70s-series-2-owners-manual-selected.md`
- Marantz, CINEMA 50 Series 2 Owner's Manual, selected pages, 2026-11-08 — `v-marantz-cinema-50-series-2-owners-manual-selected.md`
- Marantz, CINEMA 70s Series 2 info sheet (NA) — `marantz-cinema-70s-series-2-info-sheet-na.pdf`
- Marantz, CINEMA 50 Series 2 info sheet (NA) — `marantz-cinema-50-series-2-info-sheet-na.pdf`
- Onkyo, TX-RZ50 spec sheet — `onkyo-tx-rz50-spec-sheet.pdf`
- Yamaha, RX-A4A User Guide — `yamaha-rx-a4a-user-guide.pdf`
- Yamaha, MusicCast supported services — `yamaha-musiccast-supported-services.md`
- Anthem, MRX 540 8K product page, read live 2026-11-08 during verification for its streaming list; the captured copy does not include it.
- Arcam, AVA15 product page — `arcam-ava15-product-page.md`
- WiiM Help Center, Introducing the WiiM Home App for PC, 2026-09-24 — `wiim-home-pc-app-help.md`
- WiiM forum, "radio paradise losless flac ?", 2025-10-26 to 2025-10-29 [anecdote] — `wiimforum-radio-paradise-lossless.md`
- WiiM (Linkplay), HTTP API for WiiM Products v1.2, 2024-07-10 — `r4-wiim-http-api-for-wiim-products.pdf`
- Sonos Support, Radio Paradise on Sonos service page and quality-label definitions, captured 2026-11-09 — `r2-sonos-music-service-pages.md`
