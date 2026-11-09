---
title: "Criterion 2: Music & two-channel performance"
slug: music-performance
kind: hub
criteria: [2]
status: unverified
confidence: low
last_verified: 2026-11-08
sources: [r3-onkyo-tx-rz30-owners-manual-selected.md, r3-dirac-store-onkyo-tx-rz30.md, r3-onkyo-tx-rz30-product-page-rendered-2026-11-09.md, asr-denon-avr-x3900h-review.md, asr-denon-avr-x3800h-review.md, asr-denon-avr-x4800h-review.md, asr-onkyo-tx-rz50-review.md, asr-marantz-cinema-40-review.md, asr-marantz-cinema-50-review.md, asr-marantz-cinema-70s-review.md, asr-anthem-mrx1140-review.md, asr-nad-t758-v3-review.md, asr-yamaha-rx-a8a-review.md, asr-avr-sinad-database.md, v-asr-what-matters-about-sinad.md, audioholics-anthem-mrx-740-1140-bench-test.md, audioholics-yamaha-rx-a6a-bench-test.md, v-arcam-ava15-spec-sheet-v1.2.pdf, harman-marantz-cinema-series-2-press-release.md, denon-avr-x3900h-owners-manual-na.pdf, v-welti-devantier-multisub-aes2006.pdf]
---

# Criterion 2: Music & two-channel performance

**On measured two-channel results the Denon AVR-X3900H leads (ASR SINAD 102, recommended); only two other candidates have been measured at all, and in this room room correction, not a few dB of SINAD, dominates what the bass sounds like.**

## Why this matters here

All three music sources in [my system](../start-here/my-system.md) arrive digitally. Radio Paradise FLAC comes from a WiiM on coax, and Spotify Connect and AirPlay 2 decode inside the receiver, so the receiver's DAC path and analog stages are what a bench figure should describe. ASR's AVR SINAD is close to that path: it is measured from the digital (Toslink) input to the pre-out, at one configuration, and HDMI may be a few dB worse ([measurements and audibility](../concepts/measurements-and-audibility.md)). The coax path the WiiM uses is a different S/PDIF connector from the one ASR tests; that it measures the same is an inference.

Two limits keep SINAD from deciding this criterion on its own. ASR itself says SINAD indicates engineering quality and does not track perception, and no source here establishes a dB level above which differences stop being audible; Audioholics calls 70 dB inaudible for most listeners, an attributed position without a listening test. And in a small closed room the room dominates low-frequency sound quality (Welti and Devantier, J. AES 2006), which is why the [room correction](room-correction.md) hub carries more weight for music than this one. The practical consequence on Denon and Marantz is the listening mode: Pure Direct removes the correction (X3900H manual p.133), so the measured "purest" path is the one that leaves the room's bass uncorrected; see [bass management and crossovers](../concepts/bass-management-and-crossovers.md).

Bench numbers still do a useful job as a screen. A SINAD in the 50s, a forced resampling path, or an amplifier fault at 4 ohms is a finding about a design, and it is what this ranking looks for.

## What good looks like

| Level | Threshold for this room | Cheapest candidate that reaches it (2026-11-08) |
|---|---|---|
| Minimum | Measured on the model itself, DAC-path SINAD above 70 dB, no measured fault in the path you will use | Denon AVR-X3800H, $1,399, SINAD 87 |
| Good | Measured above 90 dB, Audioholics' state-of-the-art bar, with correction available in a stereo mode | Denon AVR-X3900H, $1,849, SINAD 102 |
| Best | Measured above 100 dB and recommended by ASR, amplifier rated very good for the class | Denon AVR-X3900H, $1,849 |

The thresholds are attributed reviewer positions, not perceptual limits. Power, protection and 4-ohm behaviour are ranked on [amplification and pre-outs](amplification-and-preouts.md); the power figures are explained on [amplifier power ratings](../concepts/amplifier-power-ratings.md).

## Systems and concepts

- [Measurements and audibility](../concepts/measurements-and-audibility.md)
- [Amplifier power ratings](../concepts/amplifier-power-ratings.md)
- [Lossless streaming paths](../concepts/lossless-streaming-paths.md)

## How the candidates rank

Only models measured themselves are ranked; proxies place the rest under "Not enough evidence". Same-method reference points from ASR's database: X4800H 95, X3600H 99, A1H 105 (ASR data, captured 2026-11-08).

### Best for this criterion

- [Denon AVR-X3900H](../products/denon-avr-x3900h.md): SINAD 102 at the pre-out with the amplifiers off and recommended (ASR, 2026-09-17); amplifier very good for the class, with low-level jitter noise noted.

### Good

- [Denon AVR-X3800H](../products/denon-avr-x3800h.md): SINAD 87 from Toslink, not recommended for distortion spikes that Denon's own measurements confirmed (ASR, 2022-10-27); 15 dB behind its successor on the same test, still above every stated audibility threshold.

### Weaker

- [Onkyo TX-RZ50](../products/onkyo-tx-rz50.md): 77 in ASR's table with conditions unstated, amplifier SINAD well below competing AVRs, and a 192 kHz input cut sharply in bandwidth outside Pure Audio, the only mode that skips Dirac (ASR, 2022-02-12).
- [Onkyo TX-RZ30](../products/onkyo-tx-rz30.md): 75 in ASR's table, conditions unstated, below the RZ50's 77; ASR could not recommend it (2026-05-30), and full-power playback meets the same latched limiter.

### Not enough evidence to rank

Ordered by what the proxies suggest. A bench test of the model itself would place each one.

- [Marantz CINEMA 50 Series 2](../products/marantz-cinema-50-series-2.md): sibling CINEMA 40 scored 98 and was recommended (proxy, ASR, 2023-12-19), but Series 2 has a new DAC.
- [Marantz CINEMA 50](../products/marantz-cinema-50.md): the same CINEMA 40 proxy; its own forum measurement exists only as uncaptured charts with no numbers.
- [Anthem MRX 540 8K](../products/anthem-mrx-540-8k.md): the MRX 1140's DAC was rated very good to excellent and recommended (81 in ASR's table) and the MRX 740's pre-outs measured 105 dB (Audioholics, 2022-03-17), on different rigs and different amplifier counts.
- [Marantz CINEMA 70s Series 2](../products/marantz-cinema-70s-series-2.md): Series 1 measured 94 at 2 V over HDMI, was not recommended, and showed a 4-ohm warm-up distortion fault (ASR, 2023-12-11); whether Series 2 inherits it is open question #26.
- [Yamaha RX-A4A](../products/yamaha-rx-a4a.md): the RX-A6A's analog pre-out reached about 100 dB in Pure Direct with amplifier SINAD about 70 dB (Audioholics, 2021-12-22), on a different DAC.
- [Arcam AVA15](../products/arcam-ava15.md): only Arcam's own −100 dB THD+N pre-out claim; the older AVR850 (84) and AVR10 (75) predate its platform.
- [Denon AVR-X2900H](../products/denon-avr-x2900h.md): no measurement and no proxy; the X3900H's figure does not transfer.
- [NAD T 758 V3i](../products/nad-t-758-v3i.md): the T 758 V3 measured about 55 dB (53 in the table), the worst DAC ASR had seen to 2019, with 192 kHz input resampled (proxy, ASR, 2019-09-07); NAD does not say whether the V3i changed it.

## Open questions

Reader-facing list: [open questions](../reference/open-questions.md). These would change the ranking:

- **Any measurement of the CINEMA 50 Series 2, CINEMA 70s Series 2, MRX 540, RX-A4A, AVA15, X2900H or NAD V3i** (#7, #26). Eight of eleven candidates have no measurement of their own.
- **Does the MRX 540 lose about 10 dB with the sub disabled, as the 1140 did** (#28)? With a sub enabled, as here, the favourable case applies if it does.
- **What ASR's database rows measure.** The RZ50's 77 and the 1140's 81 carry no stated conditions, and the RZ50 review text calls its DAC slightly above average.
- **ASR's SINAD band cut-offs** (#31) are undocumented, so no candidate can be called audibly better or worse by its band.
