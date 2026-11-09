---
title: "Amplifier power ratings"
slug: amplifier-power-ratings
kind: concept
criteria: [2, 4]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [v-ftc-16cfr432-amplifier-rule-ecfr.md, v-ftc-amplifier-rule-final-2024-06-12-89fr49801.pdf, denon-avr-x3900h-owners-manual-na.pdf, denon-avr-x3900h-info-sheet.pdf, denon-avr-x3900h-product-page.md, marantz-cinema-50-series-2-info-sheet-na.pdf, marantz-cinema-70s-series-2-info-sheet-na.pdf, yamaha-rx-a4a-user-guide.pdf, yamaha-rx-a4a-specifications.md, onkyo-tx-rz50-spec-sheet.pdf, onkyo-tx-rz50-firmware-update-2026-03.pdf, v-anthem-mrx-540-8k-product-page.md, nad-t-758-v3i-data-sheet.pdf, v-arcam-ava15-spec-sheet-v1.2.pdf, arcam-ava15-product-page.md, sony-str-az3000es-product-page.md, wiim-amp-ultra-user-manual.pdf, asr-wiim-amp-ultra-review.md, audioholics-anthem-mrx-740-1140-bench-test.md, audioholics-yamaha-rx-a6a-bench-test.md, asr-denon-avr-x3900h-review.md, asr-onkyo-tx-rz50-review.md, asr-pioneer-vsx-lx505-review.md, asr-pioneer-vsx-lx505-power-remeasurement.md, v-asr-onkyo-tx-nr7100-review-post1.md, asr-onkyo-tx-rz30-review.md, asr-marantz-cinema-70s-review.md, asr-nad-t758-v3-review.md, asr-anthem-mrx1140-review.md, v-asr-limp-mode-for-beginners.md]
---

# Amplifier power ratings

**The FTC rule only obliges a receiver's headline rating to hold for the two front channels into 8 ohms, 20 Hz–20 kHz, at no more than 1% THD+N, so no candidate's rating tells you what five channels get at once; on the Onkyo/Pioneer platform a latched power limiter matters more than the rated watts.**

Used by: [Music & two-channel performance](../criteria/music-performance.md) · [Amplification & pre-outs](../criteria/amplification-and-preouts.md). Terms: [glossary](../reference/glossary.md).

## The mechanism

### What the FTC rule requires

The US rule (16 CFR Part 432, amended by the Final Rule of 2024-06-12, effective 2024-08-12) defines rated power as continuous power per channel with all *associated* channels driven, and associated channels as, at a minimum, the left and right fronts (§432.3(g)–(h)). That power must hold from 250 mW up, across 20 Hz–20 kHz, into 8 ohms, at no more than 1.0% THD+N (§432.3(e)). A five- or seven-channel figure may appear only if labelled as not tested under the FTC standard and shown less prominently (§432.4). The FTC tests no receivers, and no enforcement action on receiver ratings was found.

A figure marked FTC, or "8 ohm, 20–20k, 2 ch driven", is therefore a two-channel number by design. A maker may quote a stricter THD than 1%, and no 4-ohm rating is required.

### How the candidates state their ratings

| Receiver | Comparable rating (8 Ω, 20 Hz–20 kHz, 2 ch driven) | Other published figures |
|---|---|---|
| Denon AVR-X3900H | 105 W at 0.08% THD | 135 W at 6 Ω, 1 kHz, 0.7%; 70% of rated power to five channels claimed, no conditions |
| Marantz Cinema 50 Series 2 | 110 W at 0.08% | 150 W at 6 Ω, 1 kHz, 0.7% |
| Marantz Cinema 70s Series 2 | 50 W at 0.08% | 70 W at 6 Ω, 1 kHz, 0.7% |
| Yamaha RX-A4A | 110 W at 0.06% | 135 W 1 ch, 1 kHz, 0.9%; 165 W at 10% THD |
| Onkyo TX-RZ50 | 120 W at 0.08%, labelled FTC | headline 250 W is 6 Ω, 1 kHz, 10% THD, 1 ch driven; "dynamic" 130/220/250 W at 8/4/3 Ω, method unstated |
| Anthem MRX 540 8K | 100 W at 1% THD | 130 W at 6 Ω, same conditions |
| NAD T 758 V3i | FTC 110 W "within rated distortion" | 7 × 60 W, all channels driven, 0.05%, 20–20k |
| Arcam AVA15 | 85 W at 0.5% THD | 150 W at 4 Ω, 1 kHz, 2 ch; 7 ch at 1 kHz: 85 W (8 Ω), 65 W (4 Ω); 9 ch: 65 W |
| Sony STR-AZ3000ES | none on the captured page | about 120 W at 8 Ω, 1 kHz, 0.9% THD, 2 ch |
| WiiM Amp Ultra (stereo) | 100 W at 0.08%, bandwidth not stated | 200 W at 4 Ω; ASR measured about 97 W (8 Ω) and 168 W (4 Ω), both channels driven |

Only NAD and Arcam publish multichannel figures. Anthem's 1% and Arcam's 0.5% are looser bases than Denon's 0.08% or Yamaha's 0.06%, so Anthem's 100 W and Yamaha's 110 W are not on the same footing.

Measured five-channel output falls well short of the ratings, though only siblings have been tested. Audioholics measured an Anthem MRX 740 at 89 W with five channels driven (1 kHz, 8 Ω, 1% THD) against a 140 W two-channel rating (2022-03-17), and a Yamaha RX-A6A at 81 W with five channels and 52 W with seven, where a limiter engaged, against 150 W (2021-12-22, ECO off, High Z). ASR drives two channels only (AVR-X3900H review).

### Protection and power limiting

ASR has measured a latched limiter across the Onkyo/Pioneer platform, each time on a single sample:

- **TX-RZ50** (2022-02-12): very low output before clipping in the 4-ohm sweep, unchanged by the impedance setting or power-save off; an AC-cord pull gave two full-power sweeps, then it limited again. No problem at 8 ohms, and the unit ran cool. No bench power figure exists.
- **Pioneer VSX-LX505** (2023-01): rated 120 W, about 20 W once limited; full power lasted about 35 s at 44 W per channel. The load is stated inconsistently (8 ohm in the current text, 4 ohm in a member's quote of the original, edited 2023-01-09), so it is not evidence of limiting at 8 ohms.
- **LX505 re-test** (2026-02-08, latest firmware, version unnamed): limited straight after a factory reset; an AC-cord pull restored two full sweeps; a stress test near 50 W re-triggered it.
- **TX-NR7100** (2024-08-13) and **TX-RZ30** (2026-05-30): the same. Only the AC cord clears it, not the power button, and nothing indicates it.

No manufacturer statement on the limiter was found; ASR's reviewer infers it exists to pass UL heat-rise tests. RZ50 firmware notes through 2026-03-03 say nothing about amplifier protection.

How often it triggers in use is unknown ([open questions](../reference/open-questions.md)). Owner reports in ASR's "Limp mode" thread (2026) run both ways and are anecdote: an LX505 owner with 3-ohm-minimum speakers in a 25 m² room never met it, one RZ30 owner reports a protection event, and an LX305 owner's 5.1 ran clean for years until heights were added. That the RZ70 does not limit is secondhand and unverified.

Limiting is neither universal nor confined to Onkyo. ASR's Marantz Cinema 70s (Series 1, 2023-12-11) showed a distortion jump after about 2 minutes at 10 W with ECO off that lasted until a power cycle, and higher-level sweeps tripped protection that also needed one. The NAD T 758 V3 held 50 W into 4 ohms with no pull-back (ASR, 2019-09-07), the Anthem MRX 1140 never shut down (ASR, 2025-11-04), and the WiiM Amp Ultra clipped without shutting down (ASR, 2025-12-29).

### ECO and low-impedance modes cut power

Denon's ECO Mode lowers the amplifier's supply rail and so its maximum output (X3900H manual pp.247–248). The default, Auto, restores the savings after 2 minutes without signal, and the manual advises Off if loud playback distorts. Yamaha's RX-A4A guide also says ECO Mode Off for high volume (p.302) and offers 8Ω MIN or 6Ω MIN impedance, the latter permitting 4-ohm fronts (p.215).

That the impedance selector cuts power is a practitioner claim with no manufacturer document behind it: Audioholics tested the RX-A6A in High Z because the low setting starves the speakers, and ASR's reviewer says the 4-ohm setting on Onkyo/Pioneer units guarantees limiting.

## Why it matters for a 5.1 room

[My system](../start-here/my-system.md) drives five amplified channels at once in a small closed room. The figure that matters is five-channel output, which only NAD and Arcam state with conditions. Under about 2,500 cu ft power is unlikely to be the limit, but that depends on speaker sensitivity and impedance, still unknown. Those figures also decide whether the Onkyo limiter is reachable: ASR's reviewer puts "loud" above about 20 W. Leave the impedance setting at its default unless the manual says otherwise, set ECO Mode Off for loud sessions, and on an Onkyo treat an AC-cord pull as the only reset.

## Common misconceptions

- **"FTC ratings are all channels driven."** The rule requires only the two front channels (§432.3(h)); the RZ50 spec-sheet row labelled "All channels" states 2 channels driven.
- **"The bigger number is more power."** Onkyo's 250 W is a one-channel, 10% THD figure beside a 120 W FTC rating; only the middle column of the table compares across brands.
- **"The 4-ohm setting gets more out of 4-ohm speakers."** Denon and Yamaha default to 8 ohm, and the bench reviewers above report the low setting reduces power.

## Sources

- FTC, 16 CFR Part 432, eCFR 2026-10-01 — `v-ftc-16cfr432-amplifier-rule-ecfr.md`
- FTC, Final Rule 89 FR 49801, 2024-06-12 — `v-ftc-amplifier-rule-final-2024-06-12-89fr49801.pdf`
- Denon, AVR-X3900H manual, info sheet, product page — `denon-avr-x3900h-owners-manual-na.pdf`, `denon-avr-x3900h-info-sheet.pdf`, `denon-avr-x3900h-product-page.md`
- Marantz, Cinema 50 / 70s Series 2 info sheets — `marantz-cinema-50-series-2-info-sheet-na.pdf`, `marantz-cinema-70s-series-2-info-sheet-na.pdf`
- Yamaha, RX-A4A user guide, specifications — `yamaha-rx-a4a-user-guide.pdf`, `yamaha-rx-a4a-specifications.md`
- Onkyo, TX-RZ50 spec sheet, 2020-12; firmware notes, 2026-03 — `onkyo-tx-rz50-spec-sheet.pdf`, `onkyo-tx-rz50-firmware-update-2026-03.pdf`
- Anthem, MRX 540 8K page, 2026-11-08 — `v-anthem-mrx-540-8k-product-page.md`
- NAD, T 758 V3i data sheet, 2020 — `nad-t-758-v3i-data-sheet.pdf`
- Arcam, AVA15 spec sheet v1.2, product page — `v-arcam-ava15-spec-sheet-v1.2.pdf`, `arcam-ava15-product-page.md`
- Sony, STR-AZ3000ES page — `sony-str-az3000es-product-page.md`
- WiiM, Amp Ultra manual v1.0.5, 2026-04-13 — `wiim-amp-ultra-user-manual.pdf`
- Audioholics, Anthem MRX 740/1140 bench test, 2022-03-17 — `audioholics-anthem-mrx-740-1140-bench-test.md`
- Audioholics, Yamaha RX-A6A bench test, 2021-12-22 — `audioholics-yamaha-rx-a6a-bench-test.md`
- ASR, Denon AVR-X3900H review — `asr-denon-avr-x3900h-review.md`
- ASR, Onkyo TX-RZ50 review, 2022-02-12 — `asr-onkyo-tx-rz50-review.md`
- ASR, Pioneer VSX-LX505 review, 2023-01 — `asr-pioneer-vsx-lx505-review.md`
- ASR, LX505 power re-measurement, 2026-02-08 — `asr-pioneer-vsx-lx505-power-remeasurement.md`
- ASR, Onkyo TX-NR7100 review, 2024-08-13 — `v-asr-onkyo-tx-nr7100-review-post1.md`
- ASR, Onkyo TX-RZ30 review, 2026-05-30 — `asr-onkyo-tx-rz30-review.md`
- ASR, Marantz Cinema 70s review, 2023-12-11 — `asr-marantz-cinema-70s-review.md`
- ASR, NAD T 758 V3 review, 2019-09-07 — `asr-nad-t758-v3-review.md`
- ASR, Anthem MRX 1140 review, 2025-11-04 — `asr-anthem-mrx1140-review.md`
- ASR, WiiM Amp Ultra review, 2025-12-29 — `asr-wiim-amp-ultra-review.md`
- ASR forum, "Limp mode" for Beginners, 2026 (anecdote) — `v-asr-limp-mode-for-beginners.md`

Full list: [bibliography](../reference/bibliography.md).
