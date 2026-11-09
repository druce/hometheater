---
title: "Measurements and audibility"
slug: measurements-and-audibility
kind: concept
criteria: [2]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [v-asr-what-matters-about-sinad.md, asr-marantz-cinema-40-review.md, asr-avr-sinad-database.md, asr-yamaha-rx-a8a-review.md, asr-anthem-mrx1140-review.md, asr-onkyo-tx-rz50-review.md, asr-nad-t758-v3-review.md, audioholics-yamaha-rx-a6a-bench-test.md, audioholics-anthem-mrx-740-1140-bench-test.md, denon-avr-x3900h-owners-manual-na.pdf, yamaha-rx-a4a-user-guide.pdf, wiim-amp-ultra-product-page.md, wiim-ultra-product-page.md, ethanwiner-assessing-room-eq-dirac.md, v-welti-devantier-multisub-aes2006.pdf]
---

# Measurements and audibility

**SINAD and the other bench figures are good at exposing careless engineering in a receiver, but ASR, the main source of them, says SINAD is not a perceptual measure, its AVR figures come from the Toslink input at one configuration, and no source in this wiki establishes a dB figure above which differences stop being audible.**

Used by: [Music & two-channel performance](../criteria/music-performance.md). Terms: [glossary](../reference/glossary.md).

## The mechanism

SINAD is the ratio of a test signal to everything else at the output, noise and distortion together; it is THD+N expressed in dB. Audio Science Review measures amplifiers at 5 W rather than 1 W, and its reviewer (amirm) states in ASR's own explainer that SINAD is a general indicator of engineering quality, does not correlate with perception, and that two amps with identical SINAD can differ in whether their distortion is audible (ASR, What matters about SINAD measurements, 2019-04-23). He groups results into four buckets for that reason. The dB cut-offs behind the colour bands on ASR's SINAD charts are not documented in anything retrieved (open question 31).

**ASR's AVR SINAD is a Toslink, DAC-path number.** ASR has no reference-grade HDMI generator: the Audio Precision HDMI module costs about $7,000 by the reviewer's recollection and does not fit his APx555, so AVRs are ranked on Toslink and HDMI is given the benefit of the doubt (ASR, Marantz Cinema 40 thread, 2023-12-19). A member argued the Cinema 40's HDMI result was about 90 to 92 dB. Since HDMI is how most receivers are fed, a published AVR SINAD is the best case for the digital path.

Three more limits apply to any figure you read:

- **Configuration moves the number.** On the Anthem MRX 1140, leaving the subwoofer disabled cost about 10 dB of SINAD (ASR, MRX 1140 review).
- **The rig sets a ceiling.** A reviewer measuring the Yamaha RX-A8A on an APx525B reports his loopback limit at 108 to 109 dB in a 22.4 kHz bandwidth and says results above about 100 dB are strongly affected by test gear and environment; he also warns against comparing his absolute numbers with Audioholics' RX-A6A bench test (ASR, RX-A8A thread).
- **The database row carries no conditions.** ASR's data table lists, for example, Denon AVR-X3900H 102, Marantz Cinema 40 98, Denon AVR-X3800H 87, Onkyo TX-RZ50 77 and NAD T 758 V3 53 (ASR data, captured 2026-11-08), but does not say which output or level each row used. The NAD's 53 and the "70 dB, 11.6 bits" in its review text are different tests (SINAD versus a 32-tone multitone), not a conflict (ASR, NAD T 758 V3 review).

Manufacturer specifications measure something else again and cannot be set against ASR's SINAD:

| Product | Published figure | Conditions given |
|---|---|---|
| Denon AVR-X3900H | D/A S/N 104 dB; analogue S/N 100 dB, distortion 0.008 % | IHF-A weighted, Direct mode; 20 Hz–20 kHz (manual p.330) |
| Yamaha RX-A4A | S/N 110 dB or more; THD 0.05 % or less | IHF-A, input shorted, speaker out, Pure Direct; 55 W, 8 Ω, 20 Hz–20 kHz (user guide p.404) |
| WiiM Amp Ultra | SNR 121 dB (product page) vs 120 dB (compare table, manual) | weighting and bandwidth not stated |
| WiiM Ultra | line out THD+N −116 dB, SNR 121 dB | level and weighting not stated |

Jitter, linearity and processing paths are measured too, and the reviewers' own audibility calls go both ways. ASR measured jitter spikes on the TX-RZ50's HDMI and S/PDIF inputs and judged them too low to matter, and measured that enabling bass management forces a resampling path, which a member then argued is practically inaudible (ASR, TX-RZ50 review, 2022-02-12; see [bass management](bass-management-and-crossovers.md)).

For room measurements the standard is different. Winer argues that assessing bass EQ needs unsmoothed responses and decay plots with 2 Hz (500 ms) resolution or finer, and that waterfalls exaggerate how fast an EQ'd peak decays (Winer, Assessing Room EQ: Dirac); that method is the basis of [room modes and the limits of correction](room-modes-and-correction-limits.md).

### Who has stated an audibility threshold

These are attributed positions, none of them backed by a listening test in the sources:

- Audioholics: 70 dB SINAD (0.03 % THD+N; the arithmetic is right, 0.0316 %) is below audibility for most listeners, while the same author uses more than 90 dB as his state-of-the-art bar (Audioholics, RX-A6A bench test). He calls more than 60 dB crosstalk at 20 kHz sufficient (Audioholics, MRX 740/1140 bench test).
- ASR thread members: one works through a home-noise example to about −65 dB (under 0.05 %); another notes that the common −60 dB figure comes from sine tests and that music masks more; a third calls single-tone masking curves worst-case (ASR, What matters about SINAD, 2019).

## Why it matters for a 5.1 room

In a small closed room with one sub, the room dominates sound quality at low frequencies (Welti and Devantier, J. AES 2006-05, §1), and that is where the owner's [room correction](../criteria/room-correction.md) priority sits. Bench numbers are still useful as a screen: a SINAD in the 50s, a forced resampling path, or a 10 dB swing with one setting are findings worth knowing about a candidate. What the evidence does not support is ranking two receivers by a few dB of SINAD as if the higher one will sound better, because ASR itself does not claim that.

## Common misconceptions

**"Higher SINAD sounds better."** ASR's own explainer says SINAD is not perceptually correlated; it is an engineering-quality measure (ASR, 2019-04-23).

**"ASR's AVR SINAD is what I will hear over HDMI."** It is a Toslink figure, and HDMI may be a few dB worse (ASR, Cinema 40 thread, 2023-12-19).

**"A manufacturer's S/N figure can be read against ASR's SINAD."** They measure different things: Yamaha's 110 dB is IHF-A weighted noise with the input shorted, while SINAD counts noise and distortion together on a live signal (Yamaha RX-A4A user guide, p.404; ASR explainer).

## Sources

- Audio Science Review, What matters about SINAD measurements (thread), 2019-04-23 — `v-asr-what-matters-about-sinad.md`
- Audio Science Review, Marantz Cinema 40 review and thread, reply of 2023-12-19 — `asr-marantz-cinema-40-review.md`
- Audio Science Review, ASR Data: audio electronics, AVR/AVP rows, captured 2026-11-08 — `asr-avr-sinad-database.md`
- Audio Science Review, Yamaha RX-A8A review and thread — `asr-yamaha-rx-a8a-review.md`
- Audio Science Review, Anthem MRX 1140 review — `asr-anthem-mrx1140-review.md`
- Audio Science Review, Onkyo TX-RZ50 review and thread, 2022-02-12 — `asr-onkyo-tx-rz50-review.md`
- Audio Science Review, NAD T 758 V3 review — `asr-nad-t758-v3-review.md`
- Audioholics, Yamaha RX-A6A bench test results — `audioholics-yamaha-rx-a6a-bench-test.md`
- Audioholics, Anthem MRX 740/1140 bench test results — `audioholics-anthem-mrx-740-1140-bench-test.md`
- Denon, AVR-X3900H Owner's Manual (North America), as captured 2026-11-08 — `denon-avr-x3900h-owners-manual-na.pdf`
- Yamaha, RX-A4A User Guide, as captured 2026-11-08 — `yamaha-rx-a4a-user-guide.pdf`
- WiiM, Amp Ultra product page, as captured 2026-11-08 — `wiim-amp-ultra-product-page.md`
- WiiM, WiiM Ultra product page, as captured 2026-11-08 — `wiim-ultra-product-page.md`
- Ethan Winer, Assessing Room EQ, Part 3 (Dirac), about 2020-09 — `ethanwiner-assessing-room-eq-dirac.md`
- Welti and Devantier, Low-Frequency Optimization Using Multiple Subwoofers, J. Audio Eng. Soc. 54(5), 2006-05 — `v-welti-devantier-multisub-aes2006.pdf`

Full list: [bibliography](../reference/bibliography.md).
