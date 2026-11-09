---
title: "Streaming protocols (AirPlay 2, Google Cast, Connect, Roon Ready)"
slug: streaming-protocols
kind: system
criteria: [3, 5]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [denon-avr-x3900h-owners-manual-na.pdf, marantz-cinema-50-series-2-info-sheet-na.pdf, marantz-cinema-70s-series-2-info-sheet-na.pdf, marantz-cinema-70s-series-2-product-page.md, yamaha-rx-a4a-user-guide.pdf, yamaha-rx-a4a-specifications.md, yamaha-musiccast-faqs.md, yamaha-musiccast-supported-services.md, onkyo-tx-rz50-spec-sheet.pdf, onkyo-tx-rz50-product-page.md, onkyo-tx-rz50-firmware-update-2026-03.pdf, pac-press-2024-11-firmware-dirac-bass-control.md, anthem-mrx-540-740-1140-8k-spec-sheet.pdf, v-anthem-mrx-540-8k-product-page.md, nad-t-758-v3i-data-sheet.pdf, bluos-apple-music-support-2026-10-20.md, bluesound-node-product-page.md, arcam-ava15-product-page.md, arcam-radia-av-launch-news-2026-02-03.md, v-arcam-ava15-spec-sheet-v1.2.pdf, wiim-pro-product-page.md, wiim-pro-plus-product-page.md, wiim-ultra-product-page.md, wiim-amp-ultra-product-page.md, wiim-amp-ultra-user-manual.pdf, asr-wiim-amp-ultra-review.md, asr-wiim-ultra-review.md, v-wiim-faq-apple-music.md]
---

# Streaming protocols (AirPlay 2, Google Cast, Connect, Roon Ready)

**AirPlay is on every receiver candidate, but AirPlay 2 is missing from WiiM's Ultra and Amp Ultra, which leaves Apple Music on those devices to Bluetooth, Cast or a cable; Google Cast is not listed for Denon, Marantz or the Yamaha RX-A4A, and Roon Ready is documented only by Denon, Marantz, Arcam, Bluesound and WiiM.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Connectivity](../criteria/connectivity.md).

## What it does

Each protocol hands playback to the receiver differently, which decides who fetches the audio and what quality arrives (the quality side is on [lossless streaming paths](../concepts/lossless-streaming-paths.md)).

- **AirPlay 2:** an iPhone, iPad or Mac sends the audio to the receiver. It can play to several AirPlay 2 devices in sync, requires iOS 11.4 or later, and follows the phone's volume (Denon X3900H manual pp.115–117). Yamaha's A4A can power on when AirPlay playback starts, if Network Standby is enabled (user guide p.147). Apple Music reaches every receiver candidate this way, since none has it as a native service.
- **Google Cast:** a Cast-enabled app tells the device what to play. WiiM's Amp Ultra manual lists Apple Music among Cast-enabled apps (p.52).
- **Spotify, TIDAL and Qobuz Connect:** the phone is a remote and the receiver streams from the service itself (Denon manual p.118).
- **Roon Ready:** the device is an endpoint for a Roon Core, which needs its own computer and subscription.
- **Bluetooth** is the universal fallback and is lossy (SBC or AAC on the RZ50 and A4A).

Receivers carrying it: [Denon AVR-X3900H](../products/denon-avr-x3900h.md), [Yamaha RX-A4A](../products/yamaha-rx-a4a.md), [Onkyo TX-RZ50](../products/onkyo-tx-rz50.md), [Anthem MRX 540 8K](../products/anthem-mrx-540-8k.md), [NAD T 758 V3i](../products/nad-t-758-v3i.md), [Arcam AVA15](../products/arcam-ava15.md), [WiiM Amp Ultra](../products/wiim-amp-ultra.md).

| Device | AirPlay 2 | Google Cast | Spotify Connect | TIDAL Connect | Qobuz Connect | Roon Ready | Native Apple Music |
|---|---|---|---|---|---|---|---|
| Denon AVR-X3900H | yes | not listed | yes | yes | yes | yes | no |
| [Marantz Cinema 50 / 70s Series 2](../products/marantz-cinema-50-series-2.md) | yes | not listed | yes | yes | yes | yes | no |
| Yamaha RX-A4A | yes | not listed | yes | TIDAL in app; Connect not stated | Qobuz in app; Connect not stated | not listed | no |
| Onkyo TX-RZ50 | yes | yes | Spotify built in; Connect not named | TIDAL built in; Connect not named | not listed | "Roon Tested", not Ready | no |
| Anthem MRX 540 8K | AirPlay 2 on 2022 sheet; current page says AirPlay | yes | yes | not listed | not listed | not listed | no |
| NAD T 758 V3i | yes | not listed | via BluOS, V3i not named | via BluOS, V3i not named | via BluOS, V3i not named | unconfirmed | BluOS added it 2026-10-20; V3i unconfirmed |
| Arcam AVA15 | AirPlay, version not stated | yes | yes | yes | yes | yes | no |
| Bluesound NODE (streamer) | yes | not listed | yes | yes | yes | yes | BluOS added it 2026-10-20; per-model list not published |
| WiiM Pro / Pro Plus (streamer) | yes | yes | yes | yes | not listed | yes | no |
| WiiM Ultra (streamer) | **no** | yes | yes | yes | not listed | yes | no |
| WiiM Amp Ultra | **no** | yes | yes | yes | yes | yes | no |

Sources by row: Denon manual p.244 (Connect and Roon toggles; no Cast anywhere in the manual); Marantz info sheets p.2; Yamaha A4A spec page and user guide p.402 plus Yamaha's services table; Onkyo spec sheet (Dec 2020) and product page; anthemav.com MRX 540 page (2026-11-08), which no longer carries the 2022 sheet's "Roon coming soon"; NAD data sheet (2020) and BluOS release notes; Arcam spec sheet v1.2; NODE product page; WiiM product pages (2026-11-08) and Amp Ultra manual v1.0.5. "Not listed" means the maker's own documents are silent, which is weaker than a stated no.

## Versions and tiers

None of the sources lists a fee for these protocols; Roon needs its own subscription. Versions that matter:

- **AirPlay vs AirPlay 2.** Older Yamaha receivers such as the RX-A1060 have first-generation AirPlay only, and AirPlay 2 arrived with the RX-A1080 generation (Yamaha services table). Arcam's and Anthem's current pages say "AirPlay" without a version.
- **Google Cast 2.0.** Onkyo's 28 Oct 2024 firmware moved the RZ50 to the Cast 2.0 network setup method and its 3 Mar 2026 firmware updated the Chromecast version, number not given (Onkyo firmware notes; PAC press release, 2024-11).
- **Spotify.** Denon supports free as well as Premium accounts on Spotify Connect (manual p.118), and Yamaha's services table marks Free/Paid on its AirPlay 2 generation. Onkyo lists Spotify Lossless support for the RZ50 under a 1 Jul 2025 heading annotated "Added in November 2025", so the release date is internally inconsistent.
- **Qobuz Connect** reached BluOS in release 4.12.4 (2025-09-23). Which Denon firmware added the Qobuz and TIDAL Connect toggles is not stated in the manual.
- **Roon Ready vs Roon Tested.** The RZ50 spec sheet says Roon Tested for the Roon Core, a different designation from Roon Ready; the sources do not say what it means in practice.

Streamer prices, for the external-streamer route: WiiM Pro Plus $219, WiiM Ultra $349 (wiimhome.com, 2026-11-08).

## Measured and observed results

No bench test in hand measures what AirPlay 2, Cast or Connect deliver on any receiver candidate. ASR found network streaming on the WiiM Amp Ultra performing the same as its Toslink input (2025-12-29) and rated the WiiM Ultra's streaming path excellent (ASR, WiiM Ultra review). Firmware history shows the protocols can regress: Onkyo's 20 Jul 2021 firmware fixed TIDAL playback falling back to AAC on the RZ50, and BluOS 4.14.12 (2026-03-10) fixed playback at sample-rate changes over Qobuz Connect and Spotify Connect.

## Limits

- **No AirPlay 2 on WiiM Ultra or Amp Ultra.** WiiM's own pages and manual say so, and the manual's suggested alternatives do not name Apple Music. For the future stereo rooms in [my system](../start-here/my-system.md), an Amp Ultra means Apple Music by Bluetooth, by Cast, or by cable; the WiiM Pro, Pro Plus, Mini and the older Amp keep AirPlay 2. An ASR forum member's claim that the Ultra has AirPlay 2 is wrong. See [WiiM](../systems/wiim.md).
- **AirPlay 2 quality is not documented by Apple.** WiiM's FAQ gives 44.1 kHz/16-bit for Apple Music over AirPlay ([open questions](../reference/open-questions.md)).
- **No Cast on Denon, Marantz or the A4A.** A Cast-only app needs another path to those receivers.
- **Denon cannot forward AirPlay or Roon Ready audio to Bluetooth headphones** (X3900H manual p.89).
- **WiiM Pro Plus is an AirPlay 2 receiver only**; it does not send its physical inputs into an AirPlay group (Pro Plus FAQ).
- **Regional gaps.** Marantz footnotes its Connect services as not available in all regions.

Platform-level detail lives on [HEOS](../systems/heos.md), [MusicCast](../systems/musiccast.md) and [BluOS](../systems/bluos.md).

## Sources

- Denon, AVR-X3900H owner's manual (NA) — `denon-avr-x3900h-owners-manual-na.pdf`
- Marantz, Cinema 50 / 70s Series 2 info sheets; 70s Series 2 product page — `marantz-cinema-50-series-2-info-sheet-na.pdf`, `marantz-cinema-70s-series-2-info-sheet-na.pdf`, `marantz-cinema-70s-series-2-product-page.md`
- Yamaha, RX-A4A user guide and specifications; MusicCast FAQs; MusicCast supported services — `yamaha-rx-a4a-user-guide.pdf`, `yamaha-rx-a4a-specifications.md`, `yamaha-musiccast-faqs.md`, `yamaha-musiccast-supported-services.md`
- Onkyo, TX-RZ50 spec sheet, Dec 2020; product page; firmware notes to 2026-03-03 — `onkyo-tx-rz50-spec-sheet.pdf`, `onkyo-tx-rz50-product-page.md`, `onkyo-tx-rz50-firmware-update-2026-03.pdf`
- Premium Audio Company, firmware press release, 2024-11 — `pac-press-2024-11-firmware-dirac-bass-control.md`
- Anthem, MRX 540/740/1140 8K spec sheet, 2022; MRX 540 8K page, 2026-11-08 — `anthem-mrx-540-740-1140-8k-spec-sheet.pdf`, `v-anthem-mrx-540-8k-product-page.md`
- NAD, T 758 V3i data sheet, 2020 — `nad-t-758-v3i-data-sheet.pdf`
- BluOS, "BluOS Now Supports Apple Music", 2026-10-20 — `bluos-apple-music-support-2026-10-20.md`
- Bluesound, NODE product page — `bluesound-node-product-page.md`
- Arcam, AVA15 product page; Radia AV launch news, 2026-02-03; spec sheet v1.2 — `arcam-ava15-product-page.md`, `arcam-radia-av-launch-news-2026-02-03.md`, `v-arcam-ava15-spec-sheet-v1.2.pdf`
- WiiM, Pro, Pro Plus, Ultra and Amp Ultra product pages, 2026-11-08; Amp Ultra manual v1.0.5 — `wiim-pro-product-page.md`, `wiim-pro-plus-product-page.md`, `wiim-ultra-product-page.md`, `wiim-amp-ultra-product-page.md`, `wiim-amp-ultra-user-manual.pdf`
- WiiM Help Center, "Is Apple Music Supported?", modified 2025-09-11, captured 2026-11-08 — `v-wiim-faq-apple-music.md`
- Audio Science Review, WiiM Amp Ultra review, 2025-12-29; WiiM Ultra review — `asr-wiim-amp-ultra-review.md`, `asr-wiim-ultra-review.md`

Full list: [bibliography](../reference/bibliography.md).
