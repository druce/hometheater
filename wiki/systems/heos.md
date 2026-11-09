---
title: "HEOS (Denon, Marantz)"
slug: heos
kind: system
criteria: [3, 6]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [denon-heos-us.md, denon-avr-x3900h-owners-manual-na.pdf, denon-av-receivers-category-us.md, v-marantz-cinema-70s-series-2-owners-manual-selected.md, v-marantz-cinema-50-series-2-owners-manual-selected.md, marantz-cinema-50-series-2-info-sheet-na.pdf, marantz-cinema-70s-series-2-info-sheet-na.pdf, harman-marantz-cinema-series-2-press-release.md, asr-denon-avr-x3900h-review.md, v-heos-cli-protocol-specification-v1.10.pdf, r4-denon-heos-cli-protocol-specification-v1.17.pdf, v-apple-appstore-hark-stream-heos.md, r2-denon-heos-buying-guide.md, r2-denon-home-150-product-page-us.md, r2-denon-home-150-nv-product-page-us.md, r2-denon-home-200-product-page-us.md, r2-denon-wireless-speakers-category-us.md, r4-apple-appstore-heos.md, r4-home-assistant-heos-integration.md, r4-denon-inside-denon-airplay-alexa-google.md]
---

# HEOS (Denon, Marantz)

**HEOS covers Spotify, TIDAL and Qobuz through their Connect protocols, plus AirPlay 2 and Roon Ready, but its internet radio decodes only MP3, WMA and AAC and Apple Music arrives only over AirPlay, so Radio Paradise FLAC on a Denon or Marantz receiver needs an external streamer.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Usability, app & firmware support](../criteria/usability-and-support.md).

## What it does

HEOS is the streaming and multiroom layer that Denon and Marantz build into their receivers, speakers, soundbars and amplifiers, controlled from the HEOS app on iOS and Android (Denon HEOS page, captured 2026-11-08; X3900H manual, 2026-04, p.106). On the Denon US site it appears on 16 of 18 receiver listings; only the AVR-S570BT and AVR-S270BT lack it (Denon AV receivers category page, 2026-11-08). Because the platform is shared across both brands, a Marantz CINEMA receiver in the main room can group with Denon Home speakers in the kitchen and bathroom.

Receivers carrying it: [Denon AVR-X3900H](../products/denon-avr-x3900h.md), [Denon AVR-X3800H](../products/denon-avr-x3800h.md), [Denon AVR-X2900H](../products/denon-avr-x2900h.md), [Marantz CINEMA 70s Series 2](../products/marantz-cinema-70s-series-2.md), [Marantz CINEMA 50 Series 2](../products/marantz-cinema-50-series-2.md), [Marantz CINEMA 50](../products/marantz-cinema-50.md).

Your three music sources reach HEOS by three different routes:

| Source | Route on HEOS | Basis |
|---|---|---|
| Spotify | Spotify Connect from the Spotify app; free or Premium account | Denon HEOS page; X3900H manual p.118 |
| Apple Music | AirPlay 2 (or Bluetooth) from an Apple device; not in the HEOS app | Denon HEOS page; X3900H manual p.115 |
| [Radio Paradise](radio-paradise.md) | Not a HEOS service. Internet radio is the TuneIn directory, which plays only lossy formats | X3900H manual pp.100, 285, 303 |

Inside the HEOS app, Denon lists Amazon Music, Pandora, TuneIn, SiriusXM, Qobuz, TIDAL, Deezer, AWA, SoundCloud and iHeartRadio, with a regional-availability caveat. TIDAL Connect and Qobuz Connect also work from their own apps (Denon HEOS page, 2026-11-08). AirPlay, Spotify Connect and the in-app services all play on the receiver's "HEOS Music" input (X3900H manual p.115).

Local playback covers DLNA servers and USB storage. The X3900H manual lists FLAC, WAV and ALAC up to 192 kHz and DSD 2.8/5.6 MHz for network and USB files, all two-channel, with bit depth not stated (X3900H manual p.17, p.300). The rear USB port on the X3900H supplies 5 V/1.5 A and cannot play files, which makes it useful for powering an external streamer. Denon's own page says HEOS handles DSD, FLAC, ALAC, WAV, WMA and MP3 but gives no rate limits; that is a vendor claim about files, not streams.

Multiroom limits, per the X3900H manual: up to 32 HEOS products in one system, and up to 16 in a group playing the same track in sync (p.111). Denon's undated HEOS buying guide instead claims up to 64 zones, without defining a zone (captured 2026-11-09); that is marketing copy against the dated manual, so the manual's figures stand. For the future plan of two stereo rooms plus a kitchen and a bathroom speaker, that is not a constraint.

Sharing a physical input is the tighter limit. The HEOS CLI spec (v1.17, Denon-hosted, 2021-10-11, keeping the v1.10 rule) lets one player's external input, coax included, play on another HEOS player, but only to one player or one group, and not while the source device is playing that input itself; whether current firmware and the HEOS app keep that rule, or expose the X3900H's coax this way, is not stated. By the spec, the WiiM on the receiver's coax cannot play in the main room and on a Denon Home speaker at once. No current Denon Home speaker states a humidity or IP rating, including the compact Home 150 ($249), Home 150 NV ($219) and Home 200 ($399) (denon.com, 2026-11-09). HEOS is costed against WiiM and Sonos in [multiroom options](../comparisons/multiroom-options.md).

**Control beyond the app.** The HEOS app rates 4.39 on 27,267 App Store ratings and claims no Siri or Shortcuts support (2026-11-09); Siri reaches a HEOS receiver only as an AirPlay 2 speaker added to Apple Home, for playback (Denon AirPlay page, undated). The CLI v1.17 documents `play_input` for physical inputs and `play_quickselect` for receiver Quick Selects, both already in v1.10, but no power, sound-mode or zone command. Home Assistant's HEOS integration (Platinum, local push) covers playback, inputs, Quick Selects, URLs and grouping, and states that receiver power and zones are out of its reach (HA docs, 2026-11-09). The routes are compared in [control and automation](../comparisons/control-and-automation.md).

## Versions and tiers

HEOS has no paid tier. What varies is the network protocol set exposed per model. On the 2026 receivers, the Network menu carries separate on/off toggles for AirPlay, Spotify Connect, Roon Ready, TIDAL Connect and Qobuz Connect, all defaulting to On: the X3900H manual shows them (p.166, p.244), and the CINEMA 70s Series 2 and CINEMA 50 Series 2 manuals show the same set (Marantz owner's manuals, selected pages, captured 2026-11-08). The X3900H manual edition does not say which firmware added the TIDAL and Qobuz Connect toggles. "Roon Ready" in these manuals is a toggle and a trademark line; neither Denon nor Marantz states a maximum Roon sample rate, and certification was not checked against Roon's partner list in this round.

Google Cast and native Apple Music appear nowhere in the X3900H manual or on the Marantz Series 2 info sheets. The CINEMA Series 2 press release claims an "upgraded HEOS platform" with better responsiveness and multiroom, without listing a feature or version (HARMAN, 2026-08-06), so treat that as an unquantified manufacturer claim.

A HEOS account is part of setup. The X3900H manual says Wi-Fi network features do not work without signing in (p.238, repeated p.288); it does not say the same of wired Ethernet. ASR's reviewer found that first-run setup on the X3900H would not continue without creating an account, and noted that earlier units only suggested it at the end (ASR, X3900H review, 2026-09-17). The review does not state the firmware version, so whether a later update relaxes it is unknown.

## Measured and observed results

No independent measurement of HEOS streaming exists in the evidence. Nobody has bench-tested what bit depth or sample rate leaves the HEOS Music input, or whether AirPlay into a Denon is bit-perfect. ASR's X3900H review measures the receiver's DAC and amplifier paths, not the streaming stack; those numbers belong on the [X3900H page](../products/denon-avr-x3900h.md).

The one observed result is the mandatory account above, a reviewer's observation on one unit. The X3900H manual also recommends wired Ethernet when Wi-Fi playback drops out (p.104).

## Limits

**Radio Paradise FLAC cannot come from HEOS internet radio as documented.** The X3900H manual and the CINEMA 70s and 50 Series 2 manuals all give the internet-radio formats as WMA, MP3 and AAC at 32/44.1/48 kHz, with no FLAC (X3900H manual p.285, p.303; Marantz manuals, captured 2026-11-08). Radio Paradise's 320k AAC stream would play; its FLAC streams would not. This is the main reason the [external-streamer route](../comparisons/radio-paradise-flac-native-vs-external-streamer.md) exists for a Denon or Marantz.

The official HEOS app has no way to enter a stream URL; nothing in the manual or on Denon's pages offers one. Two side doors exist. The HEOS CLI protocol (Denon spec v1.17, 2021-10-11, local TCP port 1255) has a `play_stream` command that takes an absolute URL to a playable stream. The third-party iOS app Hark Stream plays direct stream links on HEOS devices, and its App Store listing says playlist files (PLS, M3U) will not play (App Store, captured 2026-11-08). Whether any HEOS firmware decodes a FLAC radio stream through either route is untested. A developer reply seen only in a search snippet says it does not, and that snippet was not captured, so it carries no weight here. Open questions #9 and #22 track this ([open questions](../reference/open-questions.md)).

Apple Music on HEOS is AirPlay 2 only, so the phone or Mac stays in the chain and the resolution is whatever AirPlay 2 carries; the format ceiling has no Apple primary source yet (see [streaming protocols](streaming-protocols.md) and [lossless streaming paths](../concepts/lossless-streaming-paths.md)). Spotify and Qobuz via their Connect protocols stream from the service to the receiver directly, with the phone acting only as a remote (X3900H manual p.118).

The account requirement ties Wi-Fi features and setup to Denon's cloud service. For a receiver you intend to keep for many years, that is a support risk to weigh under [usability](../criteria/usability-and-support.md), though it does not affect sound.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Denon US, "Denon HEOS" page with FAQ, captured 2026-11-08 — `denon-heos-us.md`
- Denon, AVR-X3900H Owner's Manual (North America), PDF dated 2026-04-06 — `denon-avr-x3900h-owners-manual-na.pdf`
- Denon US, AV receivers category page, captured 2026-11-08 — `denon-av-receivers-category-us.md`
- Marantz, CINEMA 70s Series 2 Owner's Manual, selected pages, captured 2026-11-08 — `v-marantz-cinema-70s-series-2-owners-manual-selected.md`
- Marantz, CINEMA 50 Series 2 Owner's Manual, selected pages, captured 2026-11-08 — `v-marantz-cinema-50-series-2-owners-manual-selected.md`
- Marantz, CINEMA 50 Series 2 and CINEMA 70s Series 2 information sheets (NA), undated — `marantz-cinema-50-series-2-info-sheet-na.pdf`, `marantz-cinema-70s-series-2-info-sheet-na.pdf`
- HARMAN, "Introducing Marantz CINEMA Series 2", 2026-08-06 — `harman-marantz-cinema-series-2-press-release.md`
- Audio Science Review, Denon AVR-X3900H review (amirm), 2026-09-17 — `asr-denon-avr-x3900h-review.md`
- Denon / Sound United, HEOS CLI Protocol Specification v1.17, 2021-10-11 (Denon-hosted) — `r4-denon-heos-cli-protocol-specification-v1.17.pdf`
- Sound United, HEOS CLI Protocol Specification v1.10, 2017 (best guess; third-party host, superseded by v1.17) — `v-heos-cli-protocol-specification-v1.10.pdf`
- Apple App Store, Hark Stream listing, captured 2026-11-08 — `v-apple-appstore-hark-stream-heos.md`
- Denon, HEOS Buying Guide (Inside Denon), undated, captured 2026-11-09 — `r2-denon-heos-buying-guide.md`
- Denon US, Denon Home 150, Home 150 NV and Home 200 product pages and wireless speakers category page, captured 2026-11-09 — `r2-denon-home-150-product-page-us.md`, `r2-denon-home-150-nv-product-page-us.md`, `r2-denon-home-200-product-page-us.md`, `r2-denon-wireless-speakers-category-us.md`
- Apple App Store, HEOS listing, captured 2026-11-09 — `r4-apple-appstore-heos.md`
- Home Assistant, Denon HEOS integration, captured 2026-11-09 — `r4-home-assistant-heos-integration.md`
- Denon US, "Inside Denon" AirPlay 2, Alexa and Google Assistant pages, undated, captured 2026-11-09 — `r4-denon-inside-denon-airplay-alexa-google.md`
