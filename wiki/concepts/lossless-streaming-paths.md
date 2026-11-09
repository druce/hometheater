---
title: "Lossless streaming paths"
slug: lossless-streaming-paths
kind: concept
criteria: [3]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [denon-avr-x3900h-owners-manual-na.pdf, v-marantz-cinema-50-series-2-owners-manual-selected.md, v-marantz-cinema-70s-series-2-owners-manual-selected.md, marantz-cinema-50-series-2-info-sheet-na.pdf, yamaha-rx-a4a-user-guide.pdf, yamaha-musiccast-faqs.md, v-arcam-ava15-spec-sheet-v1.2.pdf, onkyo-tx-rz50-spec-sheet.pdf, onkyo-tx-rz50-firmware-update-2026-03.pdf, wiim-pro-plus-product-page.md, wiim-pro-product-page.md, wiim-ultra-product-page.md, wiim-amp-ultra-user-manual.pdf, wiimforum-radio-paradise-lossless.md, bluos-support-radio-paradise-articles.md, v-bluos-digital-passthrough-bluesound-players.md, bluesound-node-product-page.md, radioparadise-stream-links-url-table.md, radioparadise-faqs-and-info.md, asr-anthem-mrx1140-review.md, asr-wiim-amp-ultra-review.md, v-wiim-faq-apple-music.md, r4-onkyo-tx-rz50-owners-manual-selected.md]
---

# Lossless streaming paths

**A stream stays lossless only if every hop carries it unchanged: Denon and Marantz internet radio is lossy by specification, AirPlay 2 is reported (by WiiM, not by Apple) to carry 44.1 kHz/16-bit, BluOS unfolds Radio Paradise's MQA only inside its own player, and a WiiM Pro or Pro Plus on a receiver's coax input is the best-documented way to deliver Radio Paradise FLAC to any candidate.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md). Terms: [glossary](../reference/glossary.md).

## The mechanism

### Formats

FLAC and ALAC are lossless; MP3, AAC and WMA are lossy. MQA is a packaged format that a certified player has to unfold. Radio Paradise publishes a FLAC stream per mix (`http://stream.radioparadise.com/flac`, plus a FLAC + Metadata variant) and a 320 kbps AAC stream as the lossy alternative (Radio Paradise stream-links page, captured 2026-11-08). WiiM forum users report the FLAC is 16-bit/44.1 kHz; the stream-links page does not state it.

### Which hop decides the quality

Each path has a different weak link. Which candidate supports which protocol is on [streaming protocols](../systems/streaming-protocols.md); this page covers what each path does to the audio.

- **Native service in the device's app** ([HEOS](../systems/heos.md), [MusicCast](../systems/musiccast.md), [BluOS](../systems/bluos.md), [WiiM](../systems/wiim.md)): the receiver or streamer fetches the stream itself, so quality is whatever that platform's client supports for that service.
- **Internet radio on Denon and Marantz:** the AVR-X3900H manual lists the playable internet-radio formats as MP3, WMA and AAC (p.285). The Cinema 50 Series 2 and Cinema 70s Series 2 manuals give the same three, at 32–48 kHz and up to 320 kbps. FLAC radio cannot play through that input, even though the same units play FLAC files to 192 kHz from USB or a server (X3900H manual pp.300–302; Marantz info sheets).
- **Connect services (Spotify, TIDAL, Qobuz):** the phone acts as a remote and the device streams from the service, per the Denon manual's Spotify Connect description (p.118). Quality depends on the service tier and the device client.
- **AirPlay 2:** the phone or Mac sends the audio. WiiM's FAQ ("Is Apple Music supported?", modified 2025-09-11) says Apple Music over AirPlay or Bluetooth arrives at 44.1 kHz/16-bit. No Apple document read in this round states AirPlay 2's format ceiling, and one community post claims 24/48 (unverified), so the 44.1/16 figure is a vendor-secondary claim. Radio Paradise's iOS app can AirPlay to multiple AirPlay 2 devices (RP FAQ, 2026-09-26); whether its stream stays lossless that way has not been tested.
- **Bluetooth:** lossy. The RZ50 receives SBC or AAC only (Onkyo product page).
- **DLNA or URL file playback:** generally the highest ceiling. The RX-A4A plays FLAC to 384 kHz/24-bit from USB or a media server (user guide p.394), the X3900H to 192 kHz.
- **External streamer into a digital input:** the streamer decodes and sends PCM over coax, optical or HDMI, and the receiver applies its own room correction and bass management to it.

### The external-streamer path in detail

The WiiM Pro Plus ($219 on wiimhome.com, 2026-11-08) outputs up to 192 kHz/24-bit on optical or coax, and WiiM documents bit-perfect output when Fixed Volume is on and EQ and mono are off. The WiiM Pro also has optical and coax out. The WiiM Ultra ($349, 2026-11-08) has optical and coax out according to WiiM's setup FAQ (the manual itself was not read), but no AirPlay 2. The WiiM Amp Ultra has no S/PDIF or line output, only speaker, sub and USB out, so it cannot feed a receiver except over USB (manual v1.0.5).

Playing the Radio Paradise FLAC URL on a WiiM is owner-reported, not documented. Users have played direct station URLs through Open Network Stream on a WiiM Pro since 2023, and the WiiM app's built-in Radio Paradise service is reported lossless, but app readouts have been inconsistent, with one owner seeing 24-bit/44.1 kHz and a 320 kbps label in March 2025 (WiiM forum). WiiM has published nothing on it.

A Bluesound NODE is a weaker fit for this purpose. BluOS states that Radio Paradise's MQA stream is unfolded only by the BluOS player and cannot be passed to an external DAC, and that Digital Passthrough to an external DAC is capped at 24-bit/96 kHz on NODE and VAULT. No BluOS document says what format the native Radio Paradise service sends to the NODE's coax or optical output.

Receiver input limits, where published, do not bind a 44.1 kHz stream: the RX-A4A takes up to 96 kHz on optical and 192 kHz on coax (user guide p.400), and the Arcam AVA15 the same split (spec sheet v1.2). The TX-RZ50 manual states PCM to 96 kHz on coax and optical (p.209); the X3900H and MRX 540 do not state coax or optical rates.

Digital beats analog into the receiver on the evidence available. ASR measured the Anthem MRX 1140's Toslink input cleaner than its analog input at 5 W (2025-11-04), and the WiiM Amp Ultra at about 99.9 dB SINAD on Toslink against about 87 dB on its analog input (2025-12-29).

## Why it matters for a 5.1 room

[My system](../start-here/my-system.md) lists Radio Paradise FLAC, Spotify and Apple Music, and accepts an external streamer. A WiiM Pro or Pro Plus on coax covers all three, including AirPlay 2 for Apple Music, while the receiver keeps doing room correction; the trade-offs are worked through in [Radio Paradise FLAC: native vs external streamer](../comparisons/radio-paradise-flac-native-vs-external-streamer.md) and [Radio Paradise](../systems/radio-paradise.md). Choosing a WiiM Ultra instead loses AirPlay 2, leaving Apple Music on Bluetooth, Cast or a cable. For the future stereo rooms, MusicCast linked rooms down-convert to 48 kHz while only the master room plays at native rate (MusicCast FAQ), and the Amp Ultra lacks AirPlay 2 ([WiiM Amp Ultra](../products/wiim-amp-ultra.md)).

## Common misconceptions

- **"If the app says FLAC, it is lossless."** Onkyo's firmware of 20 Jul 2021 fixed TIDAL playback falling back to AAC on the RZ50, and WiiM's Radio Paradise readouts have disagreed with each other. Check the receiver's signal-info screen after firmware updates.
- **"AirPlay 2 carries Apple Music's lossless and hi-res tiers."** The only source in hand, WiiM's FAQ, says 44.1/16. Apple's own statement is still missing ([open questions](../reference/open-questions.md)).
- **"A BluOS streamer hands its best Radio Paradise stream to the receiver."** The MQA unfold stays inside the BluOS player, and what reaches the digital output is undocumented.
- **"Hi-res inputs are needed for FLAC radio."** A 16/44.1 stream fits within every published optical limit among the candidates.

## Sources

- Denon, AVR-X3900H owner's manual (NA) — `denon-avr-x3900h-owners-manual-na.pdf`
- Marantz, Cinema 50 Series 2 and Cinema 70s Series 2 owner's manuals (selected pages, captured 2026-11-08) and Cinema 50 Series 2 info sheet — `v-marantz-cinema-50-series-2-owners-manual-selected.md`, `v-marantz-cinema-70s-series-2-owners-manual-selected.md`, `marantz-cinema-50-series-2-info-sheet-na.pdf`
- Yamaha, RX-A4A user guide; MusicCast FAQs — `yamaha-rx-a4a-user-guide.pdf`, `yamaha-musiccast-faqs.md`
- Arcam, AVA15 spec sheet v1.2 — `v-arcam-ava15-spec-sheet-v1.2.pdf`
- Onkyo, TX-RZ50 spec sheet, Dec 2020; firmware history to 2026-03-03 — `onkyo-tx-rz50-spec-sheet.pdf`, `onkyo-tx-rz50-firmware-update-2026-03.pdf`
- Onkyo, TX-RZ50 Instruction Manual (SN29404020B), selected pages, captured 2026-11-09 — `r4-onkyo-tx-rz50-owners-manual-selected.md`
- WiiM, Pro Plus, Pro and Ultra product pages, 2026-11-08; Amp Ultra user manual v1.0.5 — `wiim-pro-plus-product-page.md`, `wiim-pro-product-page.md`, `wiim-ultra-product-page.md`, `wiim-amp-ultra-user-manual.pdf`
- WiiM Help Center, "Is Apple Music Supported?", modified 2025-09-11, captured 2026-11-08 — `v-wiim-faq-apple-music.md`
- WiiM forum, Radio Paradise lossless thread, 2025-10-26 (anecdote) — `wiimforum-radio-paradise-lossless.md`
- WiiM forum, "Adding internet radio stations to Open Network Stream" (2023) and "WiiM ultra radio paradise" (2024–2025) threads (anecdote; read in verification r1, not saved to raw/)
- Lenbrook/BluOS, Radio Paradise support articles; Digital Passthrough article; Bluesound NODE product page — `bluos-support-radio-paradise-articles.md`, `v-bluos-digital-passthrough-bluesound-players.md`, `bluesound-node-product-page.md`
- Radio Paradise, stream links, captured 2026-11-08; FAQ, 2026-09-26 — `radioparadise-stream-links-url-table.md`, `radioparadise-faqs-and-info.md`
- Audio Science Review, Anthem MRX 1140 review, 2025-11-04; WiiM Amp Ultra review, 2025-12-29 — `asr-anthem-mrx1140-review.md`, `asr-wiim-amp-ultra-review.md`

Full list: [bibliography](../reference/bibliography.md).
