---
title: "BluOS (Bluesound, NAD)"
slug: bluos
kind: system
criteria: [3, 6]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [bluos-supported-services.md, bluos-support-radio-paradise-articles.md, bluos-apple-music-support-2026-10-20.md, v-bluos-digital-passthrough-bluesound-players.md, v-bluos-release-notes-4.16.22-excerpt.md, bluesound-node-product-page.md, bluesound-pulse-flex-product-page.md, nad-t-758-v3i-data-sheet.pdf, radioparadise-ways-to-listen.md, radioparadise-faqs-and-info.md, asr-nad-t758-v3-review.md]
---

# BluOS (Bluesound, NAD)

**BluOS is the only platform in this wiki with Radio Paradise documented as a built-in service, and it announced native Apple Music on 2026-10-20, but its Radio Paradise stream is MQA that unfolds only inside the player, so what a NODE sends to a receiver's digital input is undocumented.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Usability, app & firmware support](../criteria/usability-and-support.md).

## What it does

BluOS is Lenbrook's streaming and multiroom platform, used by Bluesound and NAD and licensed to PSB, Cyrus, DALI and Monitor Audio, and controlled from the BluOS Controller app (BluOS press release, 2026-10-20). On a NAD receiver it arrives on a plug-in MDC module; the T 758 V3i data sheet says BluOS is included as an upgrade kit, and that BluOS lets the receiver group with other BluOS players (NAD T 758 V3i data sheet, 2020).

Receivers carrying it: [NAD T 758 V3i](../products/nad-t-758-v3i.md).

All three of your music sources have a native route on BluOS:

| Source | Route on BluOS | Basis |
|---|---|---|
| [Radio Paradise](radio-paradise.md) | Built-in service, free, no account, worldwide; streams MQA, which BluOS calls an exclusive | BluOS supported services (about 2026-11-04); BluOS Radio Paradise articles |
| Spotify | In-app with a free account, and Spotify Connect, with Spotify Lossless support listed on the NODE | BluOS supported services; NODE product page, 2026-11-08 |
| Apple Music | Native service, Premium subscription, 172 countries; also AirPlay 2 | BluOS supported services; press release 2026-10-20 |

The rest of the service list includes Qobuz, TIDAL, Deezer, Amazon Music, TuneIn, Pandora (US) and several niche services, all subject to a regional-availability caveat. Integrations are AirPlay 2, Spotify Connect, TIDAL Connect, Qobuz Connect and Roon Ready, plus Alexa and Siri for voice (NODE product page; BluOS supported services). Roon needs its own subscription. Qobuz Connect arrived in BluOS 4.12.4 on 2025-09-23, and 4.14.12 (2026-03-10) fixed playback across sample-rate changes on Qobuz Connect and Spotify Connect (BluOS release notes, captured 2026-11-08). Google Cast is not listed on the NODE or Pulse Flex pages.

Radio Paradise itself ranks BluOS MQA as its best-sounding option (Radio Paradise, Ways to Listen, captured 2026-11-08). That is the broadcaster's claim; no measurement or listening test backs it in the evidence. Track skip and rating work only through the dedicated Radio Paradise service, not through the generic radio or TuneIn entries (Radio Paradise FAQ).

## Versions and tiers

BluOS itself is free and firmware-delivered, so features depend on the release a player runs. Native Apple Music was announced on 2026-10-20 as a free update for compatible Bluesound, NAD, PSB, Cyrus, DALI and Monitor Audio products during October. The release names no models, no firmware number and no audio resolution (BluOS press release). The BluOS release-notes page on 2026-11-08 still had 4.16.22 (2026-08-25) as its newest entry, with no Apple Music mention, though the supported-services article already listed Apple Music. Whether Apple Music has reached the T 758 V3i is open question #25 ([open questions](../reference/open-questions.md)).

Hardware endpoints that matter for this system, priced on bluesound.com on 2026-11-08:

| Product | Price | Role here | Notes |
|---|---|---|---|
| NODE | $849 | External streamer for any receiver | Outputs: analog RCA (with fixed-level option), optical, coaxial, USB Audio 2.0; HDMI eARC, optical and analog inputs. Dirac Live Ready as a paid upgrade |
| Pulse Flex | $429 | Kitchen or bathroom speaker | Mono, 50 W total (10 W tweeter, 40 W woofer, no conditions given). AirPlay 2, Spotify/TIDAL/Qobuz Connect, Roon Ready, aptX HD receive |

Dirac Live on the NODE is a paid upgrade whose price is not on the product page, and it needs Bluesound's $59 Room Calibration Kit. It applies to the analog and optical/coax outputs but not to USB (NODE product page, 2026-11-08). If the receiver does the [room correction](dirac-live.md), Dirac on the NODE would stack on top of it and should stay off. The NODE's two-way aptX Adaptive Bluetooth is marked as coming in a future update. The NODE's HDMI eARC input decodes Dolby Digital only.

## Measured and observed results

No independent measurement of a current BluOS player is in the evidence. The NODE's published SNR of -118 dB and THD+N of 0.0007% are manufacturer figures with no level, load or bandwidth stated. ASR's NAD T 758 V3 review (2019) measures the receiver's own DAC and amplifiers, not BluOS, and belongs on the [V3i page](../products/nad-t-758-v3i.md).

What reaches a NODE's coax output when it plays Radio Paradise is unmeasured. Forum posts found during verification, not captured as sources, say Radio Paradise's FLAC streams are 16-bit/44.1 kHz and that one Node X owner sees a 44.1 kHz/24-bit MQA Studio indicator on the native service. Treat both as unverified owner reports.

## Limits

**MQA does not leave the player.** BluOS states that the Radio Paradise MQA unfold happens only in the BluOS player and cannot be passed to an external DAC (BluOS, Radio Paradise in MQA, about 2024-11). Your plan of record puts a streamer on a receiver's digital input, so that external DAC is the receiver. BluOS's Digital Passthrough article adds that the NODE and VAULT cap digital output to an external DAC at 24-bit/96 kHz, that passthrough needs tone controls off, replay gain disabled and fixed output level, and that sending MQA to a DAC without MQA certification produces distorted audio or none (BluOS support, about 2026-06). The two articles do not agree on what happens to folded MQA in passthrough.

**Whether a NODE outputs plain FLAC for Radio Paradise is open (#13).** Two readings fit the documents. In one, the native service is MQA only, and the NODE sends decoded PCM at up to 24/96 with passthrough off. In the other, BluOS still carries the non-MQA "CD-quality" Radio Paradise stations added in release 3.4.3 (2019-04-16), but the current service page says only "MQA streaming" and the current article shows no quality selector. The fallback, also untested, is to enter Radio Paradise's FLAC URL as a custom radio stream, or to use a [WiiM](wiim.md) instead. The [external-streamer comparison](../comparisons/radio-paradise-flac-native-vs-external-streamer.md) carries the decision.

MQA's footing is narrowing outside BluOS: BluOS's own support article says TIDAL dropped MQA on 2024-07-24, while BluOS 4.8.17 (2025-01-28) still shipped an MQA codec update. The BluOS Radio Paradise article refers to "four mix channels" while listing eight mixes; the four is stale text from the 2021 launch and does not bear on quality.

The Pulse Flex page gives no IP or splash rating and no battery, and its storage spec of 20 to 80% relative humidity implies non-condensing conditions. The page suggests kitchens and does not mention bathrooms. A steamy bathroom is therefore outside what Bluesound documents; that is an inference from the spec, since Bluesound states no exclusion. A stereo pair needs two units ($858 at list), and Pulse Flex speakers can act as surrounds only with Bluesound's own soundbars or POWERNODE, not with a third-party receiver.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- BluOS Support, "What Music Services does BluOS Support?", updated about 2026-11-04 — `bluos-supported-services.md`
- BluOS Support, "Radio Paradise - Advanced Features" (about 2026-08) and "Radio Paradise in MQA (BluOS exclusive)" (about 2024-11) — `bluos-support-radio-paradise-articles.md`
- Lenbrook / BluOS, "BluOS Now Supports Apple Music", 2026-10-20 — `bluos-apple-music-support-2026-10-20.md`
- BluOS Support, "Using Digital Passthrough with Bluesound Players", updated about 2026-06 — `v-bluos-digital-passthrough-bluesound-players.md`
- BluOS Support, release notes through 4.16.22 (2026-08-25), excerpt captured 2026-11-08 — `v-bluos-release-notes-4.16.22-excerpt.md`
- Bluesound, NODE product page, captured 2026-11-08 — `bluesound-node-product-page.md`
- Bluesound, PULSE FLEX product page, captured 2026-11-08 — `bluesound-pulse-flex-product-page.md`
- NAD, T 758 V3i data sheet, 2020 — `nad-t-758-v3i-data-sheet.pdf`
- Audio Science Review, NAD T 758 V3 review, 2019-09 — `asr-nad-t758-v3-review.md`
- Radio Paradise, "Ways to Listen" and FAQs, captured 2026-11-08 — `radioparadise-ways-to-listen.md`, `radioparadise-faqs-and-info.md`
