---
title: "NAD T 758 V3i"
slug: nad-t-758-v3i
kind: product
criteria: [1, 2, 3, 4, 5, 6, 7]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [nad-t-758-v3i-data-sheet.pdf, nad-t-758-v3i-product-page.md, nad-t-778-product-page.md, dirac-pricing-and-device-pages.md, asr-nad-t758-v3-review.md, asr-avr-sinad-database.md, v-bluos-release-notes-4.16.22-excerpt.md, bluos-apple-music-support-2026-10-20.md, bluos-support-radio-paradise-articles.md]
brand: NAD
model: "T 758 V3i"
model_year: 2020
msrp_usd: 2299
street_usd: "2,299 (nadelectronics.com and ListenUp, 2026-11-08)"
channels: "7 amp / ? processing"
room_correction: "Dirac Live RC Limited included (inferred); Full upgrade $99 (T 758 V3 price); Bass Control and ART not supported (inferred)"
streaming: [BluOS, AirPlay 2]
preouts: ?
successor_of: "T 758 V3"
---

# NAD T 758 V3i

**The only candidate with Radio Paradise built in, the $2,299 T 758 V3i likely ships Limited-bandwidth Dirac with no Bass Control, and its only bench data is the V3 predecessor's poor 2019 DAC result.**

Ranked in: [Room correction & bass management](../criteria/room-correction.md) · [Music & two-channel performance](../criteria/music-performance.md) · [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Amplification & pre-outs](../criteria/amplification-and-preouts.md) · [Connectivity](../criteria/connectivity.md) · [Usability, app & firmware support](../criteria/usability-and-support.md) · [Value, reliability & resale](../criteria/value-and-reliability.md).

## Verdict

Provisional. The V3i's best case is a one-box main room on [BluOS](../systems/bluos.md): Radio Paradise, Spotify and AirPlay 2 inside the receiver, with BluOS speakers later in the kitchen and bathroom. Its main problem is that this case rests on unchecked facts. No V3i has been measured, its Dirac tier is inferred from older models, and native Apple Music on it is unconfirmed. With an external streamer acceptable ([my system](../start-here/my-system.md)), BluOS no longer offsets those gaps, and $2,299 buys less room correction than the Arcam AVA15 or Onkyo TX-RZ50, which include Room Correction and sell Bass Control.

## Specs that matter

| Spec | T 758 V3i | Basis |
|---|---|---|
| Amp channels | 7 | Data sheet, 2020 |
| Rated power | 7 × 60 W into 8 Ω, all channels driven, 20 Hz–20 kHz, 0.05% THD; 110 W FTC into 8 Ω; IHF dynamic 137 W (8 Ω), 243 W (4 Ω) | Data sheet (manufacturer claim) |
| Sub outputs | Unknown; neither the data sheet nor the captured product page gives a count | — |
| Pre-outs | Unknown | — |
| Digital audio inputs | Count and maximum rate not stated; BluOS plays FLAC, WAV and AIFF to 24-bit/192 kHz | Data sheet |
| HDMI | 3 in / 1 out, 4K/60 4:4:4, HDCP 2.2, ARC; no HDMI 2.1, no eARC listed | Data sheet; NAD store text, 2026-11-08 |
| Network | BluOS on a plug-in MDC module (upgrade kit included); Zone 2 can run from the back-channel amps | Data sheet |

The 60 W figure is stated under a stricter condition than a two-channel rating, every channel driven across the full band (see [power ratings](../concepts/amplifier-power-ratings.md)). The spec table on the same data sheet gives rated-power THD as below 0.08%, a small mismatch with the 0.05% headline. In a 5.1 room the two spare back channels can power a stereo Zone 2.

## Room correction

[Dirac Live](../systems/dirac-live.md) ships with a calibrated microphone (data sheet, 2020), but no source names the tier. Dirac has no V3i page (404), and its NAD grid lists only the T 758 and T 758 V3, both shown as Limited included with a $99 upgrade to Full and no Bass Control or ART (Dirac device pages, 2026-11-08). The V3i data sheet's promise of an upgrade to a full-featured Dirac fits that pattern, so Limited plus a $99 Full upgrade is the best-supported reading; it remains an inference (open question #17). Without Bass Control, sub distance, level and crossover are set by hand after Dirac runs, as covered in [bass management and crossovers](../concepts/bass-management-and-crossovers.md).

## Streaming

BluOS is built in, and BluOS release 3.14.31 (2021-10) names the V3i among its players. The three sources reach it as follows:

- **Radio Paradise:** native BluOS service. It streams MQA, which unfolds only inside a BluOS player (BluOS support); here the player is the receiver itself, so the restriction that affects a NODE feeding another receiver does not apply. Details on [Radio Paradise](../systems/radio-paradise.md).
- **Spotify:** Spotify Connect is a BluOS platform feature, but no NAD or BluOS page names the V3i for it, and the same holds for TIDAL and Qobuz Connect (BluOS release notes, 4.12.4).
- **Apple Music:** AirPlay 2 is on the data sheet. BluOS announced native Apple Music on 2026-10-20 for compatible NAD products without naming models, and the release notes through 4.16.22 (2026-08-25) do not mention it, so V3i support is open question #25.

Roon Ready rests on one 2021 forum post and is left out of the front matter. Protocol detail is on [streaming protocols](../systems/streaming-protocols.md).

## Measurements

**No V3i measurement exists** in anything found (open question #7). The proxy is ASR's 2019 review of the T 758 V3 (proxy: T 758 V3). From the S/PDIF coax input to the pre-out at 0 dB volume, the third harmonic dominated and the reviewer gave SINAD as about 55 dB, the worst DAC he had measured to that date; ASR's database row lists 53 with no conditions (ASR, 2019-09-07). Backing the volume off 6 dB improved the result, which still sat in ASR's lowest quadrant. A 192 kHz sweep ended near 48 kHz, suggesting resampling to 96 kHz, and response was down 0.7 dB at the low end and 0.9 dB at 20 kHz; the roll-off disappeared on the 7.1 analog input, the V3's only bypass path. The amplifier was not class D.

Sound & Vision's V3 test bench reports 100.6 W at 0.1% THD and 113.6 W at 1%, two channels driven into 8 Ω (proxy: T 758 V3; search snippet, page not opened). NAD does not say whether the V3i changed the DAC or analog stages. How much a 55 dB SINAD matters at listening levels is discussed in [measurements and audibility](../concepts/measurements-and-audibility.md).

## Known issues

- **Measured (proxy: T 758 V3):** high distortion near full DAC output, as above. ASR did not test Dirac and did not recommend the V3.
- **Amplifier topology conflict:** the data sheet says PowerDrive, while a 2026 ListenUp listing says HybridDigital, probably copied from the T 778 page; the retailer text is unverified.
- **Upgrade path:** NAD states it cannot guarantee MDC compatibility with future formats, and no HDMI 2.1 module is offered in the sources. ASR doubted in 2019 that module upgrades would make economic sense.
- No repeated owner reports and no V3i firmware notes beyond BluOS releases are in the evidence.

## Price and availability

List $2,299 on nadelectronics.com, in stock (nine units in the store's data, 2026-11-08), and $2,299 at ListenUp, in stock and shipping within 24 hours (both read during verification and not captured to raw/); no street price below list was found. The V3i dates from 2020 per its data sheet, and the "V3i" name is the only evidence that it follows the T 758 V3. No successor is announced in the sources, and NAD's warranty term is not in the evidence. The 9-channel T 778 lists at $4,799 and was sold out on NAD's store the same day.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- NAD, T 758 V3i data sheet, 2020 — `nad-t-758-v3i-data-sheet.pdf`
- NAD, T 758 V3i product page, captured 2026-11-08 — `nad-t-758-v3i-product-page.md`
- NAD, T 778 product page, captured 2026-11-08 — `nad-t-778-product-page.md`
- Dirac, pricing and device pages (T 758, T 758 V3), 2026-11-08 — `dirac-pricing-and-device-pages.md`
- Audio Science Review, NAD T 758 V3 review, 2019-09-07 — `asr-nad-t758-v3-review.md`
- Audio Science Review, AVR/AVP SINAD database, captured 2026-11-08 — `asr-avr-sinad-database.md`
- BluOS Support, release notes through 4.16.22, captured 2026-11-08 — `v-bluos-release-notes-4.16.22-excerpt.md`
- Lenbrook / BluOS, "BluOS Now Supports Apple Music", 2026-10-20 — `bluos-apple-music-support-2026-10-20.md`
- BluOS Support, Radio Paradise articles — `bluos-support-radio-paradise-articles.md`
