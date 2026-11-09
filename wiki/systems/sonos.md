---
title: "Sonos"
slug: sonos
kind: system
criteria: [3, 6]
status: contested
confidence: medium
last_verified: 2026-11-09
sources: [r2-sonos-port-product-page.md, r2-sonos-port-product-guide.md, r2-sonos-port-setup-support.md, r2-sonos-amp-product-page.md, r2-sonos-amp-product-guide.md, r2-sonos-wireless-speakers-product-pages.md, r2-sonos-speaker-location-humidity-support.md, r2-sonos-supported-audio-formats.md, r2-sonos-music-service-pages.md, r2-sonos-airplay-support.md, r2-sonos-line-in-support-articles.md, r2-sonos-trueplay-support-articles.md, r2-sonos-app-release-notes.md, r2-sonos-ceo-letter-app-update-2024-07-25.md, r2-sonos-press-release-quality-commitments-2024-10-01.md, r2-spotify-spotify-on-sonos.md, r2-techradar-sonos-app-improved-navigation-2026-06.md, r2-verge-sonos-new-app-missing-features-2024-05-08.md, denon-avr-x3900h-owners-manual-na.pdf, radioparadise-faqs-and-info.md, r4-sonos-siri-apple-home-support.md, r4-sonos-presets-support.md, r4-sonos-developer-control-api.md, r4-home-assistant-sonos-integration.md]
---

# Sonos

**Sonos can run every room in this house from one app, with Spotify Connect, native Apple Music to 24/48 and AirPlay 2 throughout, but it stops at 48 kHz, labels its Radio Paradise service standard quality, shares line-in at 16/44.1, and cannot wake or switch the X3900H.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md).

Compared in: [multiroom options](../comparisons/multiroom-options.md).

## What it does

Sonos is a closed multiroom platform: the Sonos app (iOS, Android) controls Sonos hardware only, and from app version 84 requires a minimum speaker firmware (release notes, 2026-04-14). The layout under evaluation is a Port into the [Denon AVR-X3900H](../products/denon-avr-x3900h.md), an Amp per stereo room, and wireless speakers in the kitchen and bathroom ([my system](../start-here/my-system.md)).

**Sources.** Spotify plays over Spotify Connect, which Spotify's support page names; Sonos accepts Free and Premium accounts (Spotify Support, "Spotify on Sonos"; Sonos service pages, captured 2026-11-09). Apple Music is native in the Sonos app at up to 24/48, though on spatial-audio speakers such as the Era 300 it defaults to Dolby Atmos until spatial audio is switched off (Sonos, "Apple Music on Sonos"). AirPlay 2 is on every current product below, and an AirPlay stream into one room can be grouped with any other Sonos room (Sonos AirPlay article). No captured Sonos page lists Google Cast; that is an absence, not a stated no. Background: [streaming protocols](streaming-protocols.md).

**Port into the receiver.** The Port has analog RCA and digital coax outputs and an RCA line input, with no optical or HDMI (Port product page, product guide and setup article; an image caption saying optical contradicts all three). Output is Fixed (receiver sets volume, app loses volume and EQ), Variable (app sets volume) or Pass-Through (fixed level, volume commands forwarded to an amplifier that supports it) (Port product guide). Sonos names no Pass-Through amplifiers and no command channel, so Fixed is the mode to assume on the X3900H.

**Line-in sharing.** Any room or group can play another product's line-in, digitised at 16-bit/44.1 kHz (Sonos, "Use Line-In on Sonos"). The current app offers Automatic, the default, which sends WAV and falls back to SBC when the network needs it, or Compressed, SBC throughout; forced uncompressed is S1-only ("Adjust Line-in Audio Compression"). Autoplay, off by default, starts a Sonos room when the line-in senses signal.

**Trueplay.** Trueplay tunes a speaker from room measurements and works on every Sonos product except Port, Connect and Roam SL (Trueplay-compatible devices article). Advanced tuning needs a supported iPhone or iPad, and many recent iPads are excluded; Android gets quick tuning from the speaker's own microphones on Arc Ultra, Beam Ultra, Era 100, Era 100 Pro and Era 300 only. Portables with microphones tune automatically. Amp supports Trueplay only with Sonos In-Wall or In-Ceiling Architectural speakers by Sonance, or Sonos rear channels, so not with the owner's passive speakers. Context: [room modes and correction limits](../concepts/room-modes-and-correction-limits.md).

**Control and automation.** Sonos is the only platform in this wiki with documented native Shortcuts actions: app 86.00.41 (2026-06-09) added Play Content, Create Group, Ungroup, Play/Pause, Set Mute and Set Volume, and Night Sound and Speech Enhancement followed on 2026-09-08 (release notes). None stops playback, switches input, recalls a preset or powers anything; presets arrived on 2026-11-03, and Sonos says voice commands cannot start them. Siri reaches Sonos through AirPlay 2 in Apple Home, and Sonos says the Home app cannot control its speakers directly. The Control API runs through cloud OAuth or a LAN WebSocket on port 1443 with an API key, where Sonos says authentication is still to come. Home Assistant's Sonos integration is Bronze and needs the UPnP toggle switched on in the Sonos app. The routes are compared in [control and automation](../comparisons/control-and-automation.md).

## Versions and tiers

US prices, sonos.com, 2026-11-09.

| Product | Price | Role here | Line-in | Water and humidity | Trueplay |
|---|---|---|---|---|---|
| Port | $499 | Streamer into the X3900H | RCA | n/a | None |
| Amp | $799 | Stereo rooms | RCA, HDMI ARC (optical via adapter) | n/a | Sonos Architectural speakers only |
| Era 100 | $219 | Kitchen or bathroom | 3.5 mm via adapter | Humidity resistant, no IP rating | iOS advanced, Android quick |
| Era 100 SL | $189 | Kitchen or bathroom | 3.5 mm via adapter | Humidity resistant, no IP rating | iOS only |
| Era 300 | $499 | Kitchen | 3.5 mm via adapter | Humidity resistant, no IP rating | iOS advanced, Android quick |
| Roam 2 | $179 | Bathroom | None | IP67 | Automatic |
| Move 2 | $499 | Portable | 3.5 mm via adapter | IP56 | Automatic |
| Sonos Play | $299 | Bathroom | 3.5 mm via adapter | IP67 | Automatic |
| Line-In Adapter | $19 | Accessory | USB-C to 3.5 mm | n/a | n/a |

The Amp's 125 W per channel into 8 Ω comes with no distortion level, bandwidth or channels driven (Amp product page and guide), so it cannot be set against bench results ([amplifier power ratings](../concepts/amplifier-power-ratings.md)). It adds HDMI ARC, AirPlay 2 and an RCA sub output with a 50–110 Hz adjustable crossover. The Port's only performance figure is THD+N below 0.009%, 20 Hz–20 kHz, with no level or load (Port product guide).

For bathrooms, Sonos calls all current wireless speakers humidity resistant and warns that non-waterproof models can be damaged by direct water (Sonos, "Selecting a location for your Sonos speakers"). Only the portables carry IP ratings.

Sonos's pages disagree on which products have line-in. The Port and Amp guides list Era 100 SL, Era 300, Era 100, Amp, Port and Five; the "Use Line-In on Sonos" article adds Amp Multi, Beam Ultra, Move, Move 2 and Play; the Line-In Adapter page lists Amp Multi, Beam Ultra, the three Eras, Sonos Play, Move 2 and Move. Roam 2 is on none. The article and adapter page look newer, but none is dated. Wi-Fi conflicts too: the Amp page says 2.4 GHz only, the Amp guide 2.4 and 5 GHz under S2.

## Measured and observed results

**No independent measurement** of any Sonos product or of Trueplay is in the evidence.

**Format ceiling.** Sonos plays up to 48 kHz, with FLAC and ALAC to 24-bit on the current app and 16-bit under S1 (Sonos supported audio formats); the Apple Music page agrees. No coax-out sample rate is published for the Port.

**Radio Paradise.** Sonos labels Radio Paradise's Sonos service "standard quality", below its CD-quality (16/44.1) and hi-res (24/48) labels (Sonos service pages). RP's FAQ calls the same service its highest-quality Sonos route, relative to TuneIn. Neither names a codec or bitrate, so the two do not strictly conflict; by Sonos's label the stream is below CD quality. See [Radio Paradise](radio-paradise.md) and [lossless streaming paths](../concepts/lossless-streaming-paths.md).

**Grouped line-in.** Sonos documents that grouped line-in can stop or skip and recommends compression and added delay, with no latency figure (support article, captured 2026-11-09).

**The 2024 app.** Sonos shipped a rebuilt app on 2024-05-07 without features from the S2 app, including queue editing and the sleep timer (The Verge, 2024-05-08, secondary). The CEO's letter of 2024-07-25 apologised and promised fixes to stability, the music library, volume response, alarms and queue editing. The 2024-10-01 press release said more than 80% of missing features were back, extended warranties by a year for home-theater and plug-in speakers then under warranty, and promised releases every two to four weeks. Release notes through 2026-11-09 show releases roughly every two weeks, and a new navigation became the default on 2026-09-08 after an opt-in period (TechRadar dated the beta to June 2026, secondary). No captured Sonos statement says reliability is resolved, so it stays contested.

## Limits

- **No auto-wake or input switching on the X3900H.** The Port's 12 V trigger is an output and the X3900H has only a TRIGGER OUT (Denon X3900H owner's manual, p.75), so the receiver is powered on and set to coax by hand.
- **48 kHz ceiling** on every product and source.
- **No Radio Paradise FLAC** in Sonos rooms, by Sonos's own label. The main-room WiiM through a Port line-in shares at 16/44.1, possibly SBC.
- **No Trueplay on Port, or on Amp with third-party speakers.**
- **No cross-platform grouping documented.** No source documents grouping Sonos with [HEOS](heos.md) or [WiiM](wiim.md). AirPlay 2 from an Apple device is the only protocol they share, and the WiiM Ultra and Amp Ultra lack it.
- **Era speakers have no IP rating**; for a bathroom, Roam 2 or Sonos Play (IP67).

## Sources

Full list: [bibliography](../reference/bibliography.md). Sonos and Spotify pages undated unless shown, captured 2026-11-09; all files `raw/`.

- Sonos product pages and guides: Port (`r2-sonos-port-product-page.md`, `r2-sonos-port-product-guide.md`), Amp (`r2-sonos-amp-product-page.md`, `r2-sonos-amp-product-guide.md`), wireless speakers and Line-In Adapter (`r2-sonos-wireless-speakers-product-pages.md`)
- Sonos Support: Port setup, speaker location, audio formats, service pages, AirPlay, line-in (five articles), Trueplay (`r2-sonos-port-setup-support.md`, `r2-sonos-speaker-location-humidity-support.md`, `r2-sonos-supported-audio-formats.md`, `r2-sonos-music-service-pages.md`, `r2-sonos-airplay-support.md`, `r2-sonos-line-in-support-articles.md`, `r2-sonos-trueplay-support-articles.md`)
- Sonos, app release notes to 2026-11-09; CEO letter, 2024-07-25; press release, 2024-10-01 (`r2-sonos-app-release-notes.md`, `r2-sonos-ceo-letter-app-update-2024-07-25.md`, `r2-sonos-press-release-quality-commitments-2024-10-01.md`)
- Spotify Support, Spotify on Sonos — `r2-spotify-spotify-on-sonos.md`
- TechRadar, June 2026, and The Verge, 2024-05-08 [secondary] — `r2-techradar-sonos-app-improved-navigation-2026-06.md`, `r2-verge-sonos-new-app-missing-features-2024-05-08.md`
- Denon, AVR-X3900H owner's manual, p.75 — `denon-avr-x3900h-owners-manual-na.pdf`
- Radio Paradise, FAQs — `radioparadise-faqs-and-info.md`
- Sonos Support, Siri and Apple Home, and Presets (`r4-sonos-siri-apple-home-support.md`, `r4-sonos-presets-support.md`); Sonos developer docs, Control API, updated 2026-04-16 to 2026-09-18 (`r4-sonos-developer-control-api.md`)
- Home Assistant, Sonos integration — `r4-home-assistant-sonos-integration.md`
