---
title: "Yamaha MusicCast"
slug: musiccast
kind: system
criteria: [3, 6]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [yamaha-musiccast-faqs.md, yamaha-musiccast-supported-services.md, yamaha-rx-a4a-specifications.md, yamaha-rx-a4a-user-guide.pdf, yamaha-rx500a-product-page.md, audioholics-yamaha-rx-a6a-bench-test.md]
---

# Yamaha MusicCast

**MusicCast gives the RX-A4A Spotify Connect, AirPlay 2, TIDAL, Qobuz and Amazon Music in one free app, but it has no documented lossless Radio Paradise path and down-converts every linked room to 48 kHz.**

Used by: [Streaming & multiroom](../criteria/streaming-and-multiroom.md) · [Usability, app & firmware support](../criteria/usability-and-support.md).

## What it does

MusicCast is Yamaha's streaming and multiroom system, built into its receivers, soundbars, wireless speakers and stereo network receivers, and run from the free MusicCast Controller app, Alexa, or a control system such as Control4 or Crestron (Yamaha MusicCast FAQs, captured 2026-11-08; RX-A4A User Guide, 2025-03, pp.89-90). It runs over your existing Wi-Fi or Ethernet. No account or subscription is required for MusicCast itself; the FAQ's stated minimum phone OS (iOS 10, Android 4.1) is years out of date and should not be read as current.

Receivers carrying it: [Yamaha RX-A4A](../products/yamaha-rx-a4a.md).

Yamaha publishes a per-model services table. The rows that matter here, as read on 2026-11-08 (Yamaha USA, MusicCast Streaming Services; the column mapping of the stacked check marks is inferred from rows with fewer marks):

| Model | Apple Music via | Spotify Connect | Pandora | Deezer, SiriusXM, TIDAL | Qobuz, Amazon Music | Internet radio |
|---|---|---|---|---|---|---|
| RX-A4A (also A2A, A6A, A8A, V4A, V6A) | AirPlay 2 | Free/Paid | yes | yes | yes | yes |
| MusicCast 20, MusicCast 50 (speakers) | AirPlay 2 | Free/Paid | yes | yes | yes | yes |
| WXA-50, WXC-50 (older streamers) | AirPlay (v1) | Paid only | 3 of these 4 columns checked; which 3 is unclear | | | |

Apple Music is never a native MusicCast service; Yamaha routes it through AirPlay or AirPlay 2 from an Apple device. Only the R-N stereo network receivers carry a "TIDAL Connect" annotation in the table, so TIDAL on the A4A is in-app, not TIDAL Connect. The cheaper RX500A, which is absent from the table, advertises TIDAL Connect, Qobuz Connect and Google Cast on its product page. Roon and Google Cast appear nowhere in the A4A user guide or spec sheet. A footnote adds that other services work over Bluetooth, which on the A4A is SBC or AAC.

Internet radio on the A4A is the NET RADIO input, which uses the airable.Radio directory run by airable GmbH (A4A User Guide p.151). For local files over USB or a DLNA server, the A4A spec sheet lists FLAC up to 384 kHz/24-bit, WAV and AIFF up to 384 kHz/32-bit, ALAC up to 96 kHz/24-bit and DSD up to 11.2 MHz, with gapless playback for the lossless formats (Yamaha RX-A4A specs, 2026-11-08; User Guide p.394).

## Versions and tiers

MusicCast has no paid tier. Compatibility splits by generation: products from August 2015 onward interoperate, while the older MusicCAST (2003) and MusicCAST2 (2009) systems do not (MusicCast FAQs). MusicCast Surround, introduced April 2018, and MusicCast Stereo pairing need newer models that also support 5 GHz, and they use a separate 5 GHz link that bypasses the router.

MusicCast Surround lets the A4A use wireless speakers as surrounds and a wireless sub. The A4A guide lists only the MusicCast 20, MusicCast 50 and MusicCast SUB 100 as compatible, as of 2021-03-01 (p.92); no newer list was captured. The constraints are hard: wireless surrounds mute the wired surround outputs, surround backs cannot be used, a wireless sub disables both wired sub pre-outs, and DSD and SACD/DVD-Audio over HDMI do not reach the wireless speakers (p.93). Using wireless surrounds also disables multi-point [YPAO](ypao.md) measurement. For a calibrated 5.1 room with a wired sub, MusicCast Surround is something to leave off.

## Measured and observed results

No independent measurement of MusicCast streaming exists in the evidence. Audioholics' RX-A6A bench test lists MusicCast among the features but measures only the analog and amplifier paths; the [RX-A4A page](../products/yamaha-rx-a4a.md) uses it as a proxy for those. Nothing has tested whether airable's Radio Paradise entries are lossless, or what the 48 kHz down-conversion does to 44.1 kHz material in practice.

One owner report exists for Radio Paradise: a What Hi-Fi forum post (2024-09-24, model not stated) claims Radio Paradise plays in FLAC through airable NET RADIO. Yamaha's documents describe NET RADIO browsing only and give no codec or bitrate. This is a single unverified anecdote, recorded as open question #16 ([open questions](../reference/open-questions.md)); it would be settled by reading the format on the app's now-playing screen on a device.

## Limits

**Linked rooms play at 48 kHz.** When MusicCast devices are linked, the master room plays at the native sample rate and every other room is down-converted to 48 kHz, and DSD cannot be linked at all (MusicCast FAQs). Radio Paradise's FLAC, 16-bit/44.1 kHz per owner reports, would therefore be resampled in the kitchen, bathroom and stereo rooms. Linked clients get the master's services whatever their own row in the table says, and an external input such as a streamer on the A4A's coax can be shared to linked rooms, subject to the same 48 kHz conversion.

**Radio Paradise FLAC has no documented native path.** Neither the services table nor the user guide names Radio Paradise, and airable's stream quality is unstated. The documented routes are AirPlay 2 from the Radio Paradise app, or an external streamer into the A4A's coaxial input (up to 192 kHz) or optical input (up to 96 kHz) (A4A User Guide p.400). See the [external-streamer comparison](../comparisons/radio-paradise-flac-native-vs-external-streamer.md) and [Radio Paradise](radio-paradise.md).

**The FLAC ceiling is stated two ways.** The MusicCast FAQ gives a platform-wide 192 kHz/24-bit for WAV, FLAC and AIFF and 96 kHz/24-bit for ALAC, with "select" devices going to 384 kHz/32-bit for single-room playback; the A4A spec sheet gives FLAC to 384 kHz/24-bit. The two are consistent if the A4A is one of the select devices, and the model-specific spec sheet is the more credible source for the A4A. Neither ceiling matters for Radio Paradise, whose FLAC owners report as 16-bit/44.1 kHz.

Defaults colour a purist music path. Compressed Music Enhancer is on by default for network, USB and Bluetooth inputs, with Hi-Res Mode on, so it processes lossless sources up to 48 kHz unless you switch it off per input (A4A User Guide pp.123, 408). AirPlay Volume Interlock defaults to Limited, which caps phone-controlled volume at -20.0 dB; Full extends it to +16.5 dB (pp.259, 411). Zone 2 shares the network, USB and Bluetooth inputs with the main room, so two different network sources cannot play at once, and the app gives only input and volume control for zones.

Yamaha suggests Bluetooth transmit from a MusicCast device to a water-resistant Bluetooth speaker for a bathroom, with the caveat that it plays slightly behind the MusicCast rooms (MusicCast FAQs), so a bathroom fed that way gets a lossy feed out of sync with the rest of the house.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Yamaha USA, "MusicCast FAQs", undated text, captured 2026-11-08 — `yamaha-musiccast-faqs.md`
- Yamaha USA, "MusicCast Streaming Services" table, undated, captured 2026-11-08 — `yamaha-musiccast-supported-services.md`
- Yamaha USA, RX-A4A specifications page, captured 2026-11-08 — `yamaha-rx-a4a-specifications.md`
- Yamaha, RX-A4A User Guide (EN), PDF created 2025-03-18 — `yamaha-rx-a4a-user-guide.pdf`
- Yamaha USA, RX500A product page, captured 2026-11-08 — `yamaha-rx500a-product-page.md`
- Audioholics, Yamaha RX-A6A bench test (feature list only) — `audioholics-yamaha-rx-a6a-bench-test.md`
