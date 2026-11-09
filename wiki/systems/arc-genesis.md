---
title: "Anthem ARC Genesis"
slug: arc-genesis
kind: system
criteria: [1]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [anthem-arc-genesis.md, v-anthem-mrx-avm-operating-manual.pdf, v-anthem-mrx-540-8k-product-page.md, anthem-mrx-540-740-1140-8k-spec-sheet.pdf, audioholics-anthem-mrx-740-1140-bench-test.md, asr-anthem-mrx1140-review.md]
---

# Anthem ARC Genesis

**ARC Genesis is free with the Anthem MRX 540 and exposes per-speaker-set target curves, crossovers and slopes with correction up to 20 kHz, but on the MRX 540 it does not set distances, both sub outputs carry the same signal, and Anthem names automatic speaker/sub phase alignment only for its STR products; no independent measurement of its results exists in the evidence.**

Used by: [Room correction & bass management](../criteria/room-correction.md).

## What it does

ARC Genesis is a Windows/Mac program that measures each speaker through Anthem's calibrated microphone, calculates correction curves, and uploads them to the receiver over USB or the network (Anthem ARC Genesis page, 2025-12). Older Anthem products that connect only over RS-232 need the earlier ARC-1 software instead. On an MRX receiver ARC also balances left and right, sets the speaker/sub crossover, sets the sub level, and adjusts sub phase and polarity relative to the speakers (MRX/AVM operating manual, §6.2, 2024-08). It does not set speaker distances, which must be measured and entered in the receiver's menu before or after the run (manual, Distances). Anthem's manual tells owners not to change the crossover by hand after running ARC.

The software has two modes. Auto Mode measures, calculates and applies corrections with guidance. Professional Mode opens the system-wide target curve (room gain, deep-bass boost, tilt, high-frequency roll-off) and, per speaker set, the crossover frequency and slope; subwoofers get their own high- and low-frequency extension and slope settings (ARC Genesis page). Correction defaults to 5,000 Hz and can be raised to 20,000 Hz per speaker set or lowered, for example to 400 Hz for dipole electrostatics; Anthem advises against raising it because the mic becomes directional at high frequencies (manual §6.1). ARC preserves the room's natural low-frequency gain by default and lets the user adjust how much is kept.

Practical tools for a small room: Quick Measure shows the response in real time while a sub or speaker is moved, Snapshot freezes a curve for comparison, a single speaker can be re-measured without redoing the rest, and measurements can be paused and resumed (ARC Genesis page). Each device holds up to four measurement sets (for example drapes open and closed) and up to four profiles, such as a 5.1 profile with sub and a two-channel profile without one. On MRX receivers amplifier channel assignment is also set from within the software. A Demo Mode runs without Anthem hardware, so the interface can be tried before buying.

Receivers carrying it: [Anthem MRX 540 8K](../products/anthem-mrx-540-8k.md).

## Versions and tiers

There is one version and no paid tier. The software is a free download from Anthem and the microphone ships with ARC-enabled products, including the MRX line (ARC Genesis page; MRX 8K spec sheet, 2022-07-15). Neither source mentions any paid feature, though neither rules one out explicitly. The same program serves Anthem, Paradigm and MartinLogan ARC- or PBK-enabled products. Per-model differences come from the hardware rather than the software:

| | MRX 540 8K | MRX 740 8K | MRX 1140 8K |
|---|---|---|---|
| Sub outputs | 2, paralleled | 2, paralleled | 2, independent |
| ARC per sub output | Own delay, level and filter, same signal | Same | Same, independent signals |

Sources: MRX/AVM operating manual (sub outputs section); anthemav.com MRX 540 8K spec accordion, 2026-11-08. The 1140's independent outputs are from the product-page accordion only. For the [bass management concept](../concepts/bass-management-and-crossovers.md), paralleled outputs mean two subs on a 540 would get individual delay, level and ARC filters applied to one shared bass signal; for the owner's single sub, this makes no difference.

## Measured and observed results

No independent measurement of ARC Genesis is in the evidence. Audioholics' MRX 740/1140 bench test reproduces Anthem's feature list, including automatic sub phase and polarity adjustment on the 1140, and calls ARC Genesis among the best and easiest room correction options, but the author did not test it in that report (Audioholics, 2022-03-17). ASR's MRX 1140 review did not test ARC either; the reviewer expected good results from his experience with Anthem's processor, and one forum member's claim that ARC falls short of Audyssey XT32 with SubEQ HT comes without data (ASR, 2025-11-04). The sample curves in Anthem's own manual (before and after, averaged over five positions, with a sub and bass management) are manufacturer illustrations.

## Limits

- **Automatic phase alignment is documented for STR products only.** The ARC Genesis page lists automatic speaker/subwoofer phase alignment as a new feature for the STR series and does not name MRX. The MRX manual says ARC adjusts sub phase and polarity relative to the speakers, and Audioholics lists auto sub phase for the 1140. Whether the MRX 540 gets the same automatic alignment as STR, or a simpler phase/polarity setting, is not stated by any source read.
- Distances are manual. A one-sub owner measures them by tape or ear, where Dirac Bass Control and Audyssey set them from the measurement.
- The MRX 540's two sub outputs carry one signal, so ARC cannot do multi-sub optimisation comparable to [Dirac Bass Control](dirac-live.md) on that model; with one sub this costs nothing.
- If ARC is turned off after it set levels, the sub level must be reduced by the room-gain amount by hand, or the sub plays too loud (manual, Level Calibration).
- No head-to-head with Dirac or Audyssey in the same room exists in the evidence, so ARC's rank on correction quality is unknown.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Anthem, ARC Genesis — Anthem Room Correction, 2025-12 (best guess) — `anthem-arc-genesis.md`
- Anthem, MRX/AVM operating manual, 2024-08-21 — `v-anthem-mrx-avm-operating-manual.pdf`
- Anthem, MRX 540 8K product page and spec accordion, 2026-11-08 — `v-anthem-mrx-540-8k-product-page.md`
- Anthem, MRX 1140/740/540 8K spec sheet, 2022-07-15 — `anthem-mrx-540-740-1140-8k-spec-sheet.pdf`
- Audioholics, Anthem MRX 740 & 1140 bench test, 2022-03-17 — `audioholics-anthem-mrx-740-1140-bench-test.md`
- Audio Science Review, Anthem MRX1140 review, 2025-11-04 — `asr-anthem-mrx1140-review.md`
