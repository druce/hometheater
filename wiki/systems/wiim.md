---
title: "WiiM (WiiM Home, RoomFit)"
slug: wiim
kind: system
criteria: [3, 6, 7]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [wiim-mini-product-page.md, wiim-pro-product-page.md, wiim-pro-plus-product-page.md, wiim-ultra-product-page.md, wiim-amp-ultra-product-page.md, wiim-amp-ultra-user-manual.pdf, wiim-home-pc-app-help.md, wiim-roomfit-help.md, wiim-roomfit-settings-help.md, wiim-sound-product-page.md, asr-wiim-ultra-review.md, asr-wiim-amp-ultra-review.md, wiimforum-radio-paradise-lossless.md, v-wiim-faq-apple-music.md, v-wiim-faq-wiim-ultra-setup.md]
---

# WiiM (WiiM Home, RoomFit)

**The WiiM Pro ($169) and Pro Plus ($219, wiimhome.com, 2026-11-08) are the WiiM models to use as the receiver's external streamer, because they combine optical and coax out with AirPlay 2, Google Cast and Roon Ready; the Ultra and Amp Ultra drop AirPlay 2, no WiiM plays Apple Music natively, and WiiM documents Radio Paradise as built in only for its PC app.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Usability, app & firmware support](../criteria/usability-and-support.md) · [Value, reliability & resale](../criteria/value-and-reliability.md).

## What it does

WiiM Home is one app (phone, plus Windows and macOS) driving a range of streamers and streaming amplifiers. For this system it has two jobs: an external streamer on a receiver digital input, carrying the [Radio Paradise](radio-paradise.md) FLAC most receivers cannot play, and the platform for the future stereo rooms ([my system](../start-here/my-system.md)).

Receivers carrying it: [WiiM Amp Ultra](../products/wiim-amp-ultra.md).

**Streaming.** Protocol support differs by model (see the table, and [streaming protocols](streaming-protocols.md)); Spotify Connect, TIDAL Connect, Alexa Cast and DLNA are on all five. Apple Music is not integrated in WiiM Home, and over AirPlay or Bluetooth it arrives at 44.1 kHz/16-bit (WiiM FAQ, modified 2025-09-11). On the Ultra and Amp Ultra, which lack AirPlay 2, Apple Music therefore needs Bluetooth (SBC or AAC only), Google Cast from a supporting app, or a wired source.

**Radio Paradise.** WiiM's PC-app help article (2026-09-24) lists Radio Paradise as an integrated service and states no codec. Lossless playback is owner-reported (open question #10) and the custom-URL route user-reported (#23); see [Measured and observed results](#measured-and-observed-results).

**Room correction (RoomFit).** RoomFit measures the response at the listening position with the phone's microphone, or an external mic with a calibration file, and applies parametric EQ toward a target curve (RoomFit help, modified 2026-11-04). It corrects magnitude only; no phase or time-domain correction is described. Targets include B&K, Harman, Flat, Music and Auto, and Max Gain, Max Q, frequency range and a cut-only Non-Boost Mode are adjustable (RoomFit settings help, 2026-10-23). Multi-position averaging (Moving Mic Measurement) is Beta; phone-mic compensation is iOS-only. The profile applies to every input, with per-input EQ layered on top. Comparison with receiver-grade correction: [room modes and correction limits](../concepts/room-modes-and-correction-limits.md).

**Subwoofer.** The Ultra and Amp Ultra have a mono sub out with app-set crossover and level. Subwoofer Calibration exists only on the Amp, Amp Pro, Amp Ultra and Ultra, and with it on RoomFit runs in stereo mode only, so per-channel correction and sub integration exclude each other (RoomFit help; see [bass management and crossovers](../concepts/bass-management-and-crossovers.md)).

**Multiroom.** Network streams can join Alexa or Google Cast groups, but physical inputs (line, optical, HDMI ARC, Bluetooth) are shared only inside an all-WiiM group (Amp Ultra page), so a non-WiiM kitchen speaker can take Spotify from the group but not the TV.

## Versions and tiers

RoomFit, the app and multiroom carry no licence fee on any model. Prices are wiimhome.com list, 2026-11-08.

| Model | Price | Digital out to a receiver | AirPlay 2 | Google Cast | Roon Ready | Sub out | Manufacturer line-out claim |
|---|---|---|---|---|---|---|---|
| Mini | $99 | Optical only (plus analog Aux out) | Yes | Not listed | Not listed | No | 106 dB SNR, −92 dB THD+N |
| Pro | $169 | Optical and coax, plus RCA line out | Yes | Yes | Yes | No | 106 dB SNR, −92 dB THD+N |
| Pro Plus | $219 | Optical and coax to 24/192, plus RCA line out | Yes | Yes | Yes | No | 121 dB SNR, −113 dB THD+N (AKM AK4493SEQ) |
| Ultra | $349 | Optical, coax and USB, plus line out (WiiM FAQ "How to set up your WiiM Ultra") | **No** | Yes | Yes | Yes | 121 dB SNR, −116 dB THD+N (ES9038Q2M) |
| Amp Ultra | $549 | **None**: speaker, sub and USB out only (manual v1.0.5) | **No** | Yes | Yes | Yes | n/a (amplifier) |

WiiM's selection guide puts the Pro forward for use with an external DAC or receiver and the Pro Plus for buyers using its RCA line out (Pro Plus page). Over coax the two are equivalent, so the Pro Plus's extra $50 buys an analog stage this system would not use, plus the voice remote that costs extra on the Pro. Bit-perfect output needs Fixed Volume on and EQ off (Pro Plus FAQ; Amp Ultra manual p.18), so RoomFit stays off on a WiiM feeding a receiver. The Ultra's additions (HDMI ARC, phono, sub out, touchscreen) do nothing for a receiver feed.

The Amp Ultra (100 W/ch into 8 Ω, two channels driven, THD 0.08%, manual p.8) belongs to the stereo rooms. The WiiM Sound powered speaker ("100W Peak", no RMS or load) showed "Coming Soon" with no price on 2026-11-08, and its page states no IP rating, which matters for the bathroom.

## Measured and observed results

**Measured, Ultra (ASR, 2024-09-30).** Line out, Ethernet streaming from Roon, 48 kHz source, 1 kHz into 100 kΩ: 2.05 Vrms, SINAD 114.9 and 115.6 dB by channel, on a WiiM-supplied unit then priced $329. Bluetooth measured poorly. ASR recommended it; a forum member found the extras over cheaper models underwhelming. Ethernet and Wi-Fi cannot run together. SINAD audibility: [measurements and audibility](../concepts/measurements-and-audibility.md).

**Measured, Amp Ultra (ASR, 2025-12-29).** At 5 W, SINAD was 99.9 dB from Toslink and 87.2 dB from the RCA input, both at maximum volume. Maximum power on the sweep, both channels driven from Toslink, was about 97 W into 8 Ω and 168 W into 4 Ω against the 100/200 W rating; a 184–185 W burst figure into 4 Ω carries a chart labelled 1% THD and annotated 0.1%, so its limit is unclear. No shutdown in clipping. Detail on the [product page](../products/wiim-amp-ultra.md). RoomFit itself has never been independently measured in the evidence.

**Radio Paradise, owner reports.** A WiiM forum user labelled Community Curator (2025-10-26, Amp Pro thread) says RP inside the WiiM app is always lossless CD-quality FLAC and the vTuner and TuneIn routes are not. Other users (2024-09, 2025-03) put it at 16/44.1, though one saw the app show 24-bit/44.1 kHz and 320 kbps, unanswered. Lossless is likely and unconfirmed by WiiM until a device test reads the format. Casting from the RP app over Google Cast is reported lossless when the app is set to FLAC.

**Custom URL, user reports.** In 2023 users played station URLs on a WiiM Pro via Open Network Stream, one reporting 24/96 FLAC arriving as 16/96. Nobody reports RP's `/flac` URL on a Pro or Pro Plus, and WiiM documents no such feature.

**App, anecdote.** The ASR reviewer's app would not add the Amp Ultra on first try; owners in the thread and the Ultra review report no such trouble.

## Limits

- **AirPlay 2 is missing on the Ultra and Amp Ultra** (Ultra page footnote; Amp Ultra manual). An ASR member's claim that the Ultra has it is wrong.
- **No native Apple Music** on any model; [BluOS](bluos.md) added it on 2026-10-20.
- **The Amp Ultra cannot feed a receiver**: no optical, coax or line out (manual p.18).
- **RoomFit is single-position magnitude EQ by default**, global, and off under bit-perfect settings.
- **HDMI ARC and optical inputs take PCM and Dolby Digital 5.1 only**, no DTS (Amp Ultra manual p.22). WiiM's 5.1 mode builds center and surrounds from other WiiM devices and does not replace the main-room receiver.
- **Support horizon is unresolved.** The ASR reviewer first read security updates to 2026-12-31 in a manual, then cited an online notice saying December 2029; manual v1.0.5 (2026-04-13) states no date (open question #29).

WiiM versus a Bluesound NODE as the streamer: [Radio Paradise FLAC: native vs external streamer](../comparisons/radio-paradise-flac-native-vs-external-streamer.md). The lossless chain: [lossless streaming paths](../concepts/lossless-streaming-paths.md).

## Sources

Full list: [bibliography](../reference/bibliography.md).

- WiiM, WiiM Mini product page, 2026-11-08 — `wiim-mini-product-page.md`
- WiiM, WiiM Pro product page, 2026-11-08 — `wiim-pro-product-page.md`
- WiiM, WiiM Pro Plus product page and FAQ, 2026-11-08 — `wiim-pro-plus-product-page.md`
- WiiM, WiiM Ultra product page, 2026-11-08 — `wiim-ultra-product-page.md`
- WiiM, WiiM Amp Ultra product page, 2026-11-08 — `wiim-amp-ultra-product-page.md`
- WiiM, WiiM Amp Ultra User Manual v1.0.5, 2026-04-13 — `wiim-amp-ultra-user-manual.pdf`
- WiiM Help Center, Introducing the WiiM Home App for PC, 2026-09-24 — `wiim-home-pc-app-help.md`
- WiiM Help Center, How to Perform RoomFit, 2026-11-04 — `wiim-roomfit-help.md`
- WiiM Help Center, Introducing RoomFit Settings, 2026-10-23 — `wiim-roomfit-settings-help.md`
- WiiM, WiiM Sound product page, 2026-11-08 — `wiim-sound-product-page.md`
- Audio Science Review, WiiM Ultra Streamer Preamp Review, 2024-09-30 — `asr-wiim-ultra-review.md`
- Audio Science Review, WiiM Amp Ultra Streaming Amplifier Review, 2025-12-29 — `asr-wiim-amp-ultra-review.md`
- WiiM forum, "radio paradise losless flac ?", 2025-10-26 to 2025-10-29 [anecdote] — `wiimforum-radio-paradise-lossless.md`
- WiiM Help Center, "Is Apple Music Supported?", modified 2025-09-11, captured 2026-11-08 — `v-wiim-faq-apple-music.md`
- WiiM Help Center, "How to Set Up Your WiiM Ultra", captured 2026-11-08 — `v-wiim-faq-wiim-ultra-setup.md`
- Not captured (forum bot check; anecdote only): WiiM forum threads "WiiM ultra radio paradise" (2024–2025) and "Adding internet radio stations to Open Network Stream" (2023).
