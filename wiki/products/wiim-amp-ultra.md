---
title: "WiiM Amp Ultra"
slug: wiim-amp-ultra
kind: product
criteria: [3, 6, 7]
status: settled
confidence: medium
last_verified: 2026-11-08
sources: [wiim-amp-ultra-user-manual.pdf, wiim-amp-ultra-product-page.md, asr-wiim-amp-ultra-review.md, v-wiim-faq-apple-music.md, wiim-home-pc-app-help.md, wiimforum-radio-paradise-lossless.md, wiim-roomfit-help.md, wiim-roomfit-settings-help.md]
brand: WiiM
model: "Amp Ultra"
model_year: ?
msrp_usd: 549
street_usd: "549 (wiimhome.com, 2026-11-08)"
channels: "2"
room_correction: "RoomFit included (parametric EQ, magnitude only, phone or external mic)"
streaming: [WiiM Home, Google Cast, Spotify Connect, TIDAL Connect, Qobuz Connect, Roon Ready, DLNA, Bluetooth]
preouts: "none (mono sub out 2.0 Vrms; USB out digital)"
successor_of: ?
---

# WiiM Amp Ultra

**The $549 Amp Ultra is a well-measured, ASR-recommended streaming amp for the future stereo rooms, but its lack of AirPlay 2 and native Apple Music conflicts with the owner's Apple Music requirement.**

Ranked in: [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Usability, app & firmware support](../criteria/usability-and-support.md) · [Value, reliability & resale](../criteria/value-and-reliability.md).

## Verdict

Provisional, and for the stereo rooms only: the Amp Ultra is a two-channel amplifier and not a 5.1 candidate, so it is ranked only on streaming, usability and value. Its best case is one box per stereo room that measures well, takes a sub and a TV over HDMI ARC, and shares the WiiM Home app with a WiiM Pro or Pro Plus feeding the main receiver. **Its main problem is Apple Music**, one of the owner's three sources ([my system](../start-here/my-system.md)): with no AirPlay 2 and no native client, Apple Music arrives only by Bluetooth, by Google Cast from an app that supports it, or by cable. If Apple Music from an iPhone has to work the way it does on the receiver, a model with AirPlay 2 fits the stereo rooms better.

## Specs that matter

| Spec | Amp Ultra | Basis |
|---|---|---|
| Amp channels | 2, Class D with post-filter feedback, dual TI TPA3255 | Manual v1.0.5 p.8 |
| Rated power | 100 W/ch into 8 Ω and 200 W/ch into 4 Ω, two channels driven, THD 0.08%; load range 2–8 Ω | Manual p.8; product page (manufacturer claim) |
| Sub output | One mono RCA, 2.0 Vrms, crossover and level set in the app | Manual |
| Pre-outs | None: no line out, no optical or coax out | Manual pp.9–12, 18 |
| Digital audio inputs | 1 optical to 192 kHz/24-bit; HDMI ARC (PCM to 192/24, Dolby Digital 5.1, no DTS); no coax; USB in for storage only | Manual |
| Other I/O | Line in, 2 Vrms, digitised by an ADC; USB out, 8 channels to 192/24 (UAC 2.0) | Manual p.10 |
| Network | Wi-Fi 6E per the manual, Wi-Fi 6 upgradeable to 6E per the product page; 10/100 Ethernet; Bluetooth 5.3, SBC and AAC, sink and source | Manual; product page |

The manual says the unit outputs to one interface at a time apart from the sub out, so it cannot feed an external DAC or receiver except over USB.

## Room correction

[RoomFit](../systems/wiim.md) is included at no charge. It measures with the phone's microphone or an external mic with a calibration file and applies parametric EQ toward a chosen target; it corrects magnitude only, and multi-position measurement is in beta (RoomFit help, 2026-11-04). With Subwoofer Calibration on, RoomFit runs in stereo mode only, so per-channel correction and sub integration exclude each other. No microphone comes in the box, and RoomFit has no independent measurement in the evidence.

## Streaming

How the three sources reach it:

- **Radio Paradise:** WiiM's PC-app help lists Radio Paradise as an integrated service with no codec stated (2026-09-24). Owners on the WiiM forum report the in-app service as lossless 16/44.1 FLAC, which WiiM has not confirmed (open question #10). See [Radio Paradise](../systems/radio-paradise.md).
- **Spotify:** Spotify Connect.
- **Apple Music:** **no AirPlay 2** (manual p.9, which also lists no HomePod grouping and no Siri) and no native integration in WiiM Home (WiiM FAQ, 2025-09-11). The routes left are Bluetooth, which WiiM says delivers Apple Music at 44.1 kHz/16-bit; Google Cast, where the manual lists Apple Music among Cast-enabled apps (p.52); or a wired source on the optical or line input.

TIDAL Connect, Qobuz Connect, Roon Ready and DLNA are also supported. In multiroom, network streams can join Alexa or Google Cast groups, while physical inputs are shared only within an all-WiiM group (product page). The WiiM Pro, Pro Plus, Mini and the older Amp keep AirPlay 2 (WiiM pages, 2026-11-08); protocol detail is on [streaming protocols](../systems/streaming-protocols.md).

## Measurements

ASR measured a manufacturer-supplied unit and recommended it (ASR, 2025-12-29). At 5 W and maximum volume, SINAD was 99.9 dB from the Toslink input and 87.2 dB from the RCA line input, the analog path about 12.7 dB worse. Signal-to-noise at full power was about 118 dB in a 20 kHz bandwidth. On the power sweep with both channels driven from Toslink, maximum power was about 97 W into 8 Ω and 168 W into 4 Ω, against the 100 W and 200 W ratings. A separate burst chart shows 184 to 185 W into 4 Ω under a title saying 1% THD and an annotation saying 0.1%, so its limit is unclear. The amp handled clipping with no shutdown and stayed load-independent thanks to post-filter feedback, and ASR found network streaming performing the same as Toslink. Reading these: [power ratings](../concepts/amplifier-power-ratings.md), [measurements and audibility](../concepts/measurements-and-audibility.md).

## Known issues

- **Manufacturer spec conflicts:** damping factor 94 in the manual against 282 (8 Ω) and 146 (4 Ω) on the product page; Wi-Fi 6E against Wi-Fi 6 with a promised upgrade; and the manual's THD+N of 0.005% does not match its own −106 dB, which equals 0.0005%.
- **Support horizon unresolved:** the ASR reviewer first read security updates ending 2026-12-31, then cited an online notice saying December 2029; manual v1.0.5 (2026-04-13) gives no date (open question #29).
- **App and controls, anecdote:** the ASR reviewer's app failed to add the unit on the first try, and there is no power button. The reviewer praised the touchscreen and the USB-C rechargeable remote.

## Price and availability

$549 on wiimhome.com, 2026-11-08, where the page does not say whether that is list or a sale price; ASR reviewed it at $529 on 2025-12-29 (open question #29). Two stereo rooms at that price come to $1,098. WiiM positions it above the Amp and Amp Pro, and it was on sale by December 2025; launch date, predecessor and warranty term are not in the evidence.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- WiiM, Amp Ultra user manual v1.0.5, 2026-04-13 — `wiim-amp-ultra-user-manual.pdf`
- WiiM, Amp Ultra product page, captured 2026-11-08 — `wiim-amp-ultra-product-page.md`
- Audio Science Review, WiiM Amp Ultra review, 2025-12-29 — `asr-wiim-amp-ultra-review.md`
- WiiM Help Center, "Is Apple Music supported?", modified 2025-09-11 — `v-wiim-faq-apple-music.md`
- WiiM Help Center, WiiM Home app for PC, modified 2026-09-24 — `wiim-home-pc-app-help.md`
- WiiM forum, Radio Paradise lossless thread, 2025-10 — `wiimforum-radio-paradise-lossless.md`
- WiiM Help Center, RoomFit and RoomFit settings, modified 2026-11-04 and 2026-10-23 — `wiim-roomfit-help.md`, `wiim-roomfit-settings-help.md`
