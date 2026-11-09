---
title: "Arcam AVA15"
slug: arcam-ava15
kind: product
criteria: [1, 2, 3, 4, 5, 6, 7]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [v-arcam-ava15-spec-sheet-v1.2.pdf, v-arcam-ava15-ava25-owners-manual-v1.5.pdf, arcam-ava15-product-page.md, arcam-radia-av-launch-news-2026-02-03.md, dirac-pricing-and-device-pages.md, asr-avr-sinad-database.md]
brand: Arcam
model: "AVA15"
model_year: 2026
msrp_usd: 4499.95
street_usd: "4,499.95 (US retailer listings incl. Audiolab, search snippets, 2026-11-08; stock unverified)"
channels: "9 amp (Class D) / 12 processing"
room_correction: "Dirac Live RC included (bandwidth unstated, Full inferred); Bass Control $299, ART $299, BC + ART $549 paid"
streaming: [AirPlay, Google Cast, Spotify Connect, TIDAL Connect, Qobuz Connect, Roon Ready, Arcam Radia]
preouts: "12 RCA (2 V RMS), no XLR; up to 3 sub outputs assignable"
successor_of: ?
---

# Arcam AVA15

**Dirac Room Correction is included and Bass Control costs $299, matching the cheapest Dirac route to Bass Control here, but the $4,499.95 AVA15 has no independent measurements and unconfirmed US stock.**

Ranked in: [Room correction & bass management](../criteria/room-correction.md) · [Music & two-channel performance](../criteria/music-performance.md) · [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Amplification & pre-outs](../criteria/amplification-and-preouts.md) · [Connectivity](../criteria/connectivity.md) · [Usability, app & firmware support](../criteria/usability-and-support.md) · [Value, reliability & resale](../criteria/value-and-reliability.md).

## Verdict

Provisional. The AVA15's best case is the full Dirac stack for one sub at the lowest add-on cost, on a 2026 platform with HDMI 2.1, a 192 kHz coax input for the external streamer, and Google Cast alongside AirPlay and the Connect services. Its main problem is price against unmeasured performance: $4,499.95 plus $299 for Bass Control is $4,799, while a Denon AVR-X3900H at $1,849 plus Dirac's $599 RC + BC bundle is $2,448 for the same licences with Full bandwidth stated (Denon US and dirac.com, 2026-11-08). Until a bench test exists, nothing in the evidence shows what the extra $2,351 buys in sound.

## Specs that matter

| Spec | AVA15 | Basis |
|---|---|---|
| Amp channels | 9, Class D; 12 processing channels | Spec sheet v1.2 |
| Rated power, 0.5% THD | 85 W, 8 Ω, 20 Hz–20 kHz, 2 ch driven; 150 W, 4 Ω, 1 kHz, 2 ch; 85 W (7 ch) and 65 W (9 ch), 8 Ω, 1 kHz; 65 W, 4 Ω, 1 kHz, 7 or 9 ch | Spec sheet (manufacturer claim) |
| Sub outputs | Up to 3: Sub 1, plus Sub 2 or Subs 2 + 3 assigned to the surround-back or Height 2 pre-outs; independent level and delay for Sub 2 and Sub 3 not stated | Owner's manual v1.5, pp.33–34 |
| Pre-outs | 12 RCA (6 fixed, 6 assignable), 2 V RMS, THD+N −100 dB; no XLR | Spec sheet; manual |
| Digital audio inputs | 2 coax to 192 kHz, 2 optical to 96 kHz, 16 or 24 bit | Spec sheet |
| HDMI | 7 in / 2 out, HDMI 2.1a, HDCP 2.3, 8K/60 or 4K/120, VRR, ALLM, eARC on output 1 | Spec sheet |
| Network | Ethernet; Wi-Fi 802.11ac; Bluetooth 5.4 sink and source | Manual; spec sheet |

The 0.5% THD threshold is looser than the NAD T 758 V3i's 0.05% or the WiiM Amp Ultra's 0.08%, and the full-bandwidth figure is two channels only (see [power ratings](../concepts/amplifier-power-ratings.md)). A one-sub 5.1 setup leaves four amp channels spare, which the manual lets you assign to bi-amp the front pair. Zone 2 is listed only for the AVA25 and AVP45 (Arcam launch news, 2026-02-03).

## Room correction

[Dirac Live](../systems/dirac-live.md) Room Correction is included, with a measurement microphone and a 5 m USB-C cable in the box, and Bass Control and ART are separate licences bought from Dirac (Arcam manual p.38). Neither Arcam nor Dirac states the bandwidth of the included tier; Dirac's store shows no Room Correction card for the AVA15 and labels NAD's bundled tier Limited while leaving Arcam's unlabelled, so Full is likely and unconfirmed (open question #17). Bass Control is $299, ART $299 and the pair $549 (dirac.com, 2026-11-08).

For this room the purchase is Bass Control. Under Room Correction alone the manual says crossovers are not calculated and must be set by hand; Bass Control computes distances, levels and crossovers, and those values cannot then be edited on the receiver (manual p.40). Manual crossovers run Full Range or 30–200 Hz in 10 Hz steps, default 80 Hz, with one slope of 12 or 24 dB/octave for all speakers (manual p.34). Background: [bass management and crossovers](../concepts/bass-management-and-crossovers.md).

## Streaming

The AVA15 has no multiroom platform comparable to BluOS or HEOS; control and internet radio run through the new Arcam Radia app. The three sources reach it as follows:

- **Radio Paradise:** not named by Arcam. Radia lists Internet Radio and UPnP and the receiver plays FLAC to 192 kHz, but whether Radia accepts RP's FLAC URL is undocumented ([Radio Paradise](../systems/radio-paradise.md)). The plan of record, a WiiM Pro or Pro Plus on coax, is within the 192 kHz coax limit, and optical's 96 kHz also covers RP's reported 16/44.1.
- **Spotify:** Spotify Connect, listed on the spec sheet.
- **Apple Music:** AirPlay, version not stated; no native Apple Music.

TIDAL Connect, Qobuz Connect, Roon Ready and Google Cast are also listed. Protocol detail: [streaming protocols](../systems/streaming-protocols.md).

## Measurements

**No independent measurement of the AVA15 exists** in the evidence or in verification searches. Arcam's own figures are manufacturer claims: −100 dB THD+N at the pre-outs, 0.003% THD at 80% power into 8 Ω at 1 kHz, and 100 dB A-weighted S/N for the digital inputs referenced to 50 W (spec sheet; product page). The nearest ASR data are two older Arcam receivers, SINAD 84 for the AVR850 (proxy: Arcam AVR850, 2020-06-12) and 75 for the AVR10 (proxy: Arcam AVR10, 2020-05-29), with no conditions in the database rows. Both predate the Radia platform and its Class D amplifiers, so they say little about this model. How to read SINAD: [measurements and audibility](../concepts/measurements-and-audibility.md).

## Known issues

- **Sub-output count conflicts in secondary sources:** a comparison table found by search says up to four assignable, and Audioholics says one dedicated sub out; the owner's manual supports three. The manual is followed here.
- **New platform:** the Radia app and AVA line launched in 2026, and no owner reports or firmware notes are in the evidence.
- The manual file is labelled v1.5 while its page footers read v1.4 (2026-08-05), a labelling slip only.

## Price and availability

Announced at $4,499.95, £2,599 and €2,999, with dealer availability from Q3 2026 (Arcam launch news, 2026-02-03). Arcam's own page shows no price, only a dealer finder (2026-11-08). US stock is unconfirmed: one Audiolab page shows in stock and another out of stock, Music Direct shows in stock, and Safe and Sound gave an arrival date of 2026-08-05 (retailer search snippets, 2026-11-08; open question #30). The step-up AVA25 is $5,499.95 with Class AB amplification and Zone 2. Arcam names no predecessor, and the warranty term is not in the evidence.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Arcam, AVA15 specification sheet v1.2, 2026 — `v-arcam-ava15-spec-sheet-v1.2.pdf`
- Arcam, AVA15/AVA25 owner's manual v1.5, 2026-08-05 — `v-arcam-ava15-ava25-owners-manual-v1.5.pdf`
- Arcam, AVA15 product page, captured 2026-11-08 — `arcam-ava15-product-page.md`
- Arcam, Radia AV launch news, 2026-02-03 — `arcam-radia-av-launch-news-2026-02-03.md`
- Dirac, pricing and device pages (Arcam AVA15), 2026-11-08 — `dirac-pricing-and-device-pages.md`
- Audio Science Review, AVR/AVP SINAD database, captured 2026-11-08 — `asr-avr-sinad-database.md`
