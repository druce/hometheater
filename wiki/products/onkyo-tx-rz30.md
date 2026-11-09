---
title: "Onkyo TX-RZ30"
slug: onkyo-tx-rz30
kind: product
criteria: [1, 2, 3, 4, 5, 6, 7]
status: contested
confidence: medium
last_verified: 2026-11-09
sources: [r3-onkyo-tx-rz30-spec-sheet-emea.pdf, r3-onkyo-tx-rz30-owners-manual-selected.md, r3-onkyo-tx-rz30-product-page-rendered-2026-11-09.md, r3-onkyo-tx-rz30-firmware-update-2026-03.pdf, r3-dirac-store-onkyo-tx-rz30.md, v-dirac-brand-and-device-pages-2026-11-08.md, asr-onkyo-tx-rz30-review.md, asr-avr-sinad-database.md, v-asr-limp-mode-for-beginners.md, onkyo-av-receivers-lineup.md, v-onkyo-us-warranty.md, pac-press-2024-11-firmware-dirac-bass-control.md]
brand: Onkyo
model: "TX-RZ30"
model_year: 2024
msrp_usd: 1099.99
street_usd: "1,099.99 backorder (onkyo.com, 2026-11-09; forum claims of about 800 at retailers unverified)"
channels: "9 amp / 9.2 processing"
room_correction: "Dirac Live Room Correction (full bandwidth) included; Bass Control $299 paid; ART not supported (dirac.com, 2026-11-09)"
streaming: [Google Cast, AirPlay 2, Spotify Connect, TIDAL, Deezer, Amazon Music HD, TuneIn, Works with Sonos, Bluetooth]
preouts: "9.2 RCA, rated 1 V (ASR max near 4 V); 2 independent sub outputs; Zone 2 and Zone 3 line outs"
successor_of: ?
---

# Onkyo TX-RZ30

**The TX-RZ30 is the cheapest route to full-bandwidth Dirac plus Bass Control in this wiki, $1,567.99 all in, but ASR measured the same latched power limiter as the RZ50 and declined to recommend it.**

Ranked in: [Room correction & bass management](../criteria/room-correction.md) · [Music & two-channel performance](../criteria/music-performance.md) · [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Amplification & pre-outs](../criteria/amplification-and-preouts.md) · [Connectivity](../criteria/connectivity.md) · [Usability, app & firmware support](../criteria/usability-and-support.md) · [Value, reliability & resale](../criteria/value-and-reliability.md).

## Verdict

Provisional. For [this room](../start-here/my-system.md) the RZ30 is the [RZ50](onkyo-tx-rz50.md)'s platform one tier down, $300 cheaper at Onkyo's direct price with the same Dirac arrangement and the same firmware version. The 5.1 plan uses five of its nine channels, so the RZ50's extra two processing channels and seventh HDMI input buy nothing here. The deciding question is the same as for the RZ50: whether five channels at small-room levels ever reach the limiter, which depends on speakers not yet chosen.

## Specs that matter

| Spec | TX-RZ30 | RZ50, for contrast | Source |
|---|---|---|---|
| Channels | 9 amp / 9.2 processing | 9 / 11.2 | EMEA spec sheet |
| Rated power (US, FTC) | 100 W/ch, 8 Ω, 20 Hz–20 kHz, 0.08%, 2 ch driven | 120 W | Manual p.175 |
| Headline (not comparable) | 220 W, 6 Ω, 1 kHz, 10%, 1 ch (US); 170 W at 1% (IEC, EMEA) | 250 W | Manual p.175; spec sheet |
| Sub outputs | 2, independent distance and level | 2, independence not stated | Spec sheet; manual pp.111–112 |
| Pre-outs | 9.2 RCA, rated 1 V/470 Ω | 11.2 RCA | Manual p.175 |
| Digital audio in | 1 coax, 1 optical, PCM to 96 kHz/24-bit | same count, rate unstated | Manual p.182 |
| HDMI | 6 in (3 at 40 Gbps) / 2 out, eARC on Main | 7 in / 2 out | Manual p.177 |
| Speaker impedance | 4–16 Ω, with a 4 Ω / 6 Ω setting | — | Manual pp.33, 109 |

FTC ratings allow two channels driven; see [amplifier power ratings](../concepts/amplifier-power-ratings.md). Onkyo links only an EMEA spec sheet, so US figures come from the manual.

## Room correction

Full-bandwidth [Dirac Live](../systems/dirac-live.md) Room Correction is included, per Onkyo's spec sheet and product page; Dirac's brand grid and store page show Bass Control for sale at $299 and ART as not supported (2026-11-09). Whether the RZ30 needs a minimum firmware for Bass Control is not stated: PAC's November 2024 release covers the RZ50 and not the RZ30, and the spec sheet already lists Bass Control as optional. Direct and Pure Audio modes disable Dirac (manual pp.75, 166). Firmware fixed a Bass Control crossover error on 1 Jul 2025, after which filters must be re-exported, and improved speaker S/N under Bass Control on 3 Mar 2026 (Onkyo firmware notes).

## Streaming

Onkyo lists Chromecast built-in, AirPlay 2, Spotify, TIDAL, Deezer, Amazon Music HD, TuneIn and Works with Sonos through a Sonos Port, and the sheet says Roon Tested rather than Roon Ready ([streaming protocols](../systems/streaming-protocols.md)). Neither the spec sheet nor the manual mentions DTS Play-Fi or Pandora, both of which the RZ50 lists.

- **Radio Paradise FLAC:** via the WiiM Pro on coax, which the manual rates for PCM up to 96 kHz/24-bit. Radio Paradise FLAC is 44.1 kHz, well inside that limit. See [Radio Paradise](../systems/radio-paradise.md).
- **Spotify:** the manual's Spotify page points to Spotify Connect; Spotify Lossless arrived with the July 2025 firmware, annotated November 2025.
- **Apple Music:** AirPlay 2 only.

For the future stereo rooms, the manual documents Zone 2 and Zone 3 as line outputs or, with a 5.1 main system, as powered zones. Zone 2 takes coax or optical sources as PCM; Zone 3 takes analog and network sources only, so the WiiM on coax cannot feed it. Network inputs must play the same source in the main room and a zone. See [multiroom options](../comparisons/multiroom-options.md).

## Measurements

ASR measured one member-supplied unit on the then-latest firmware (ASR, TX-RZ30 review, 2026-05-30):

- **Power:** the amplifier dropped into a lower-power mode under push, as on other Onkyo and Pioneer models, and only an AC-cord pull clears it. ASR could not run its power tests, so no bench power figure exists. The text does not say at which load it engaged; the RZ50 limited at 4 Ω and not at 8 Ω.
- **Amplifier:** distortion judged good before the power test, with HDMI and analog inputs measuring the same; ASR judged the RZ50's amplifier well below competitors.
- **DAC and pre-out:** about 16-bit-class performance at 2 V, good multitone, poor jitter and IMD. Maximum pre-out reached nearly 4 V (RZ50: 3.5 V), enough for any power amplifier.

ASR's data table lists SINAD 75 against the RZ50's 77, conditions unstated (probably the DAC path, inference). ASR's verdict was that it could not recommend the RZ30. See [measurements and audibility](../concepts/measurements-and-audibility.md).

## Known issues

**The latched limiter is measured on this model.** It gives no indication. No firmware release through 3 Mar 2026 mentions protection or power limiting, and ASR tested after that release (inference from dates). How often it triggers in a 5.1 system is unknown. Owner reports in ASR's "Limp mode" thread are anecdote and run both ways: an RZ30 owner driving tower fronts at apartment levels never met it, while another RZ30 owner tripped a separate, indicated protection by shorting an output.

ASR found no way to switch off the internal amplifiers, so the RZ30 cannot act as a pure processor. A forum post relays a reviewer's report that Onkyo said this generation lacks the processing for ART (secondhand, unverified). Firmware has also fixed silent iPhone Bluetooth (12 Mar 2025) and Standby Through switching itself off (3 Mar 2026).

## Price and availability

$1,099.99 on onkyo.com, temporarily out of stock and orderable on backorder (rendered 2026-11-09); no warranty statement appears on the page. ASR listed it at $1,100 in May 2026. Forum members claimed about $800 at retailers in May and November 2026 (anecdote).

All in to the owner's target at dated prices: receiver $1,099.99 (onkyo.com, 2026-11-09) + Bass Control $299 (dirac.com, 2026-11-09) + WiiM Pro $169 = **$1,567.99**, $300 below the RZ50.

Warranty is 3 years parts and labour for RZ Series receivers (Onkyo USA warranty, captured 2026-11-08). No successor is named by Onkyo; a forum member's mention of an RZ31 is unsourced.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Onkyo, TX-RZ30 spec sheet (EMEA, English), Sept 2024 — `r3-onkyo-tx-rz30-spec-sheet-emea.pdf`
- Onkyo, TX-RZ30 Instruction Manual, Sept 2025, selected pages — `r3-onkyo-tx-rz30-owners-manual-selected.md`
- Onkyo, TX-RZ30 product page, rendered 2026-11-09 — `r3-onkyo-tx-rz30-product-page-rendered-2026-11-09.md`
- Onkyo, TX-RZ30 firmware update notes, 2026-03-03 — `r3-onkyo-tx-rz30-firmware-update-2026-03.pdf`
- Dirac, store page for the Onkyo TX-RZ30, 2026-11-09, and Onkyo brand grid, 2026-11-08 — `r3-dirac-store-onkyo-tx-rz30.md`, `v-dirac-brand-and-device-pages-2026-11-08.md`
- Audio Science Review, Onkyo TX-RZ30 review, 2026-05-30, and AVR SINAD table, captured 2026-11-08 — `asr-onkyo-tx-rz30-review.md`, `asr-avr-sinad-database.md`
- Audio Science Review forum, "Limp mode for beginners", 2026-06 to 2026-11 — `v-asr-limp-mode-for-beginners.md`
- Onkyo, USA Limited Warranty and AV receivers lineup, captured 2026-11-08 — `v-onkyo-us-warranty.md`, `onkyo-av-receivers-lineup.md`
- Premium Audio Company, firmware press release, 2024-11 — `pac-press-2024-11-firmware-dirac-bass-control.md`
