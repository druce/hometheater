---
- Onkyo, USA Limited Warranty, captured 2026-11-08 — `v-onkyo-us-warranty.md`
title: "Onkyo TX-RZ50"
slug: onkyo-tx-rz50
kind: product
criteria: [1, 2, 3, 4, 5, 6, 7]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [onkyo-tx-rz50-spec-sheet.pdf, v-onkyo-tx-rz50-product-page-rendered-2026-11-08.md, onkyo-tx-rz50-product-page.md, onkyo-tx-rz50-firmware-update-2026-03.pdf, pac-press-2024-11-firmware-dirac-bass-control.md, dirac-store-onkyo-tx-rz50.md, asr-onkyo-tx-rz50-review.md, asr-onkyo-tx-rz30-review.md, asr-pioneer-vsx-lx505-review.md, asr-pioneer-vsx-lx505-power-remeasurement.md, v-asr-onkyo-tx-nr7100-review-post1.md, v-asr-limp-mode-for-beginners.md, asr-avr-sinad-database.md, onkyo-av-receivers-lineup.md, onkyo-press-ces-2026-horizon.md, v-onkyo-us-warranty.md]
brand: Onkyo
model: "TX-RZ50"
model_year: 2020
msrp_usd: 1399.99
street_usd: "1,399.99 backorder (onkyo.com, 2026-11-08; retailer 1,699.99 reference prices unverified)"
channels: "9 amp / 11.2 processing"
room_correction: "Dirac Live Room Correction (full bandwidth) included; Bass Control $299 paid; ART not offered"
streaming: [Google Cast, AirPlay 2, Spotify, TIDAL, Deezer, Amazon Music HD (via Play-Fi), Pandora, TuneIn, DTS Play-Fi, Works with Sonos, Bluetooth]
preouts: "11.2 RCA, variable (sub pre-out 1 V rms; sub independence ?)"
successor_of: ?
---

# Onkyo TX-RZ50

**The TX-RZ50 ships with full-bandwidth Dirac Live included and adds Bass Control for $299, but ASR measured a 4-ohm power limiter that latches until the AC cord is pulled, and no firmware through March 2026 addresses it.**

Ranked in: [Room correction & bass management](../criteria/room-correction.md) · [Music & two-channel performance](../criteria/music-performance.md) · [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Amplification & pre-outs](../criteria/amplification-and-preouts.md) · [Connectivity](../criteria/connectivity.md) · [Usability, app & firmware support](../criteria/usability-and-support.md) · [Value, reliability & resale](../criteria/value-and-reliability.md).

## Verdict

Provisional. For [this room](../start-here/my-system.md) the RZ50 is one of two candidates, with the Arcam AVA15, where Dirac Room Correction is included and Bass Control costs $299, so the full one-sub Dirac setup is $1,698.98 all in at Onkyo's direct price. Its main problem is the amplifier, which ASR found limits power into 4 ohms until the mains cord is pulled, with no indicator and no fix. Whether five channels at small-room levels ever reach it depends on speakers not yet chosen.

## Specs that matter

| Spec | TX-RZ50 | Source |
|---|---|---|
| Amplifier channels | 9 | Spec sheet |
| Rated power | 120 W/ch, 8 Ω, 20 Hz–20 kHz, 0.08% THD, 2 ch driven (FTC) | Spec sheet p.1–2 |
| Headline (not comparable) | 250 W/ch: 6 Ω, 1 kHz, 10% THD, 1 ch driven | Spec sheet |
| Sub outputs | 2 (the ".2"); whether independently delayed or levelled is not stated | Spec sheet |
| Pre-outs | 11.2 RCA, variable; sub pre-out 1 V rms; Zone 2/B and Zone 3 line outs | Spec sheet |
| Digital audio in | 1 coax, 1 optical; maximum sample rate not stated | Spec sheet |
| HDMI | 7 in (1 front) / 2 out (Main with eARC, Sub/Zone 2); 8K/60, 4K/120 | Spec sheet |
| Network | 10/100 Ethernet, Wi-Fi 802.11ac 2×2, Bluetooth receive and transmit | Spec sheet |

The spec sheet (Dec 2020) labels its power row "All channels" but states two channels driven, as the FTC rule permits; see [amplifier power ratings](../concepts/amplifier-power-ratings.md).

## Room correction

Full-bandwidth [Dirac Live](../systems/dirac-live.md) Room Correction is included with a measurement microphone (onkyo.com, 2026-11-08). Bass Control is $299 on Dirac's store for this model and needs the 28 Oct 2024 firmware or later; ART is not offered (Dirac store, 2026-11-08). For one sub, Room Correction plus Bass Control is the combination the Dirac Live page argues for,; see the [licence comparison](../comparisons/which-dirac-license-to-buy.md).

Pure Audio mode bypasses bass management and with it Dirac, while bass management forces internal resampling that a forum member argues is inaudible; see [bass management and crossovers](../concepts/bass-management-and-crossovers.md). Firmware fixed a Bass Control crossover error on 1 Jul 2025 and improved speaker S/N under Bass Control on 3 Mar 2026 (Onkyo firmware notes).

## Streaming

Onkyo lists Chromecast built-in, AirPlay 2, DTS Play-Fi, Spotify, TIDAL, Deezer, Pandora, TuneIn and Amazon Music HD (through Play-Fi), plus Works with Sonos through a Sonos Port (spec sheet; onkyo.com, 2026-11-08). The spec sheet says Roon Tested, a different designation from Roon Ready, and does not say whether Spotify and TIDAL are the Connect protocols; see [streaming protocols](../systems/streaming-protocols.md).

- **Radio Paradise FLAC:** no native integration. The built-in TuneIn is a station-directory route, which Radio Paradise says gives lower quality than its own integrations. The plan of record is the external streamer on coax or optical; Onkyo states no input rate limit, but ASR fed S/PDIF at 192 kHz (open question #12). See [Radio Paradise](../systems/radio-paradise.md) and the [external-streamer comparison](../comparisons/radio-paradise-flac-native-vs-external-streamer.md).
- **Spotify:** built in; Spotify Lossless is listed under a July 2025 firmware heading annotated November 2025.
- **Apple Music:** AirPlay 2 only.

## Measurements

ASR measured one member-bought unit (ASR, TX-RZ50 review, 2022-02-12):

- **Power:** the 4-ohm sweep gave very low output before clipping, whatever the impedance or power-save setting; an AC-cord pull gave two full-power sweeps before it limited again. At 8 ohms ASR saw no limiting, and the unit ran cool. Maximum and peak power could not be run, so no bench power figure exists.
- **Amplifier SINAD:** well below competing AVRs; values in uncaptured images.
- **DAC and pre-out:** slightly above average for an AVR; jitter on HDMI and S/PDIF judged inaudible.
- **Processing:** outside Pure Audio a 192 kHz input is cut sharply in bandwidth, which ASR attributes to an internal 44.1 or 48 kHz rate.

ASR's data table lists the RZ50 at SINAD 77 with conditions unstated, probably the DAC path rather than the amplifier (inference); (proxy: TX-RZ30) the RZ30 is at 75. See [measurements and audibility](../concepts/measurements-and-audibility.md).

## Known issues

**The power limiter is measured on the RZ50 and repeated across the platform.** ASR found the same latched behaviour on the (proxy: TX-NR7100) in 2024, the (proxy: TX-RZ30) in May 2026, and the (proxy: Pioneer VSX-LX505) in 2023 and on its latest firmware in February 2026. Only an AC-cord pull clears it, and nothing on the unit shows it has happened. The LX505 review states its load inconsistently, so nothing shows limiting at 8 ohms. No manufacturer statement exists; ASR's reviewer infers a UL heat-rise motive. RZ50 firmware notes through R145-1119-1284-0034 (3 Mar 2026) mention no protection change; the 28 Oct 2024 power-supply item was relay-noise reduction (Premium Audio Company, 2024-11).

How often it triggers in use is unknown (open questions #6 and #14). Owner reports in ASR's 2026 "Limp mode" thread run both ways, from an LX505 owner with 3-ohm-minimum speakers who never met it to an RZ30 owner reporting a protection event. The practical answer waits on speaker impedance and sensitivity (open question #4). ASR's LX505 verdict recommends the platform only as a processor feeding external amplifiers.

Firmware has since fixed silent Bluetooth from iPhones, wrong Dirac filters on some layouts (both 12 Mar 2025) and Standby Through switching itself off (3 Mar 2026).

## Price and availability

$1,399.99 on onkyo.com, temporarily out of stock and orderable on backorder (rendered 2026-11-08); a buyer review dated 2026-10-15 describes months of waiting. ASR paid $1,399 in February 2022. Unopened retailer snippets imply a $1,699.99 reference price, so the list price is unresolved (open question #29, [open questions](../reference/open-questions.md)).

The platform dates from December 2020. Onkyo still lists the RZ50 below the RZ70 flagship ($2,299.99, Bass Control preinstalled). No successor is named; the CES 2026 release teased next-generation concepts for 2027 with no models or prices. Warranty is 3 years parts and labour for RZ Series receivers sold after 2018-10-01 (Onkyo USA warranty, captured 2026-11-08).

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Onkyo, TX-RZ50 spec sheet, Dec 2020 — `onkyo-tx-rz50-spec-sheet.pdf`
- Onkyo, TX-RZ50 product page, static capture and browser-rendered capture, 2026-11-08 — `onkyo-tx-rz50-product-page.md`, `v-onkyo-tx-rz50-product-page-rendered-2026-11-08.md`
- Onkyo, TX-RZ50 firmware update notes, 2026-03-03 — `onkyo-tx-rz50-firmware-update-2026-03.pdf`
- Premium Audio Company, Dirac Bass Control firmware release, 2024-11 — `pac-press-2024-11-firmware-dirac-bass-control.md`
- Dirac, store page for the Onkyo TX-RZ50, 2026-11-08 — `dirac-store-onkyo-tx-rz50.md`
- Audio Science Review, Onkyo TX-RZ50 review, 2022-02-12 — `asr-onkyo-tx-rz50-review.md`
- Audio Science Review, platform proxies: TX-RZ30 (2026-05), VSX-LX505 (2023-01; remeasured 2026-02-08), TX-NR7100 (2024-08-13) — `asr-onkyo-tx-rz30-review.md`, `asr-pioneer-vsx-lx505-review.md`, `asr-pioneer-vsx-lx505-power-remeasurement.md`, `v-asr-onkyo-tx-nr7100-review-post1.md`
- Audio Science Review forum, "Limp mode for beginners" thread, 2026-06 to 2026-11 — `v-asr-limp-mode-for-beginners.md`
- Audio Science Review, AVR SINAD data table, captured 2026-11-08 — `asr-avr-sinad-database.md`
- Onkyo, AV receivers lineup, 2026-11-08, and CES 2026 press release — `onkyo-av-receivers-lineup.md`, `onkyo-press-ces-2026-horizon.md`
