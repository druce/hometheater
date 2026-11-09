---
title: "Yamaha YPAO"
slug: ypao
kind: system
criteria: [1]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [yamaha-rx-a4a-user-guide.pdf, yamaha-rx-a4a-specifications.md, audioholics-yamaha-rx-a6a-bench-test.md]
---

# Yamaha YPAO

**YPAO on the RX-A4A is included, multipoint (up to 8 positions) and has no paid tier, but its automatic bass correction is incomplete by Yamaha's own description: the Low Frequency mode only detects problem frequencies and leaves Q and gain to be set by hand, and no independent measurement places it against Dirac or XT32.**

Used by: [Room correction & bass management](../criteria/room-correction.md).

## What it does

YPAO (Yamaha Parametric room Acoustic Optimizer) detects which speakers are connected, measures their distances to the listening position through the supplied microphone, and then sets levels and parametric EQ to suit the room (RX-A4A user guide p.17, rev. 02/2025). Yamaha's documentation describes distance, level and parametric EQ; it makes no claim of time-domain or phase correction of the kind Dirac and Audyssey XT32 advertise.

Multi Measure takes up to 8 positions, with the first at the seat used most often; Yamaha estimates about 15 minutes for all eight (pp.98, 100). The manual shows three patterns: five seats, one seat plus four points around it, or two seats plus points in front and behind. An optional Angle/Height Measure uses the supplied pole and mic base for four further measurements and corrects speaker angle and presence-speaker height, mainly for Cinema DSP effects (pp.98–99, 105–106).

After a run the Parametric EQ menu offers four automatic targets plus Manual and Through (p.213):

| Setting | What Yamaha says it does |
|---|---|
| YPAO:Flat | Gives every speaker the same response |
| YPAO:Front | Matches every speaker to the front pair |
| YPAO:Natural | As Flat, with treble lowered |
| YPAO:Low Frequency | Detects the low-frequency problem frequencies only; Q and gain are not set |
| Manual | User parametric EQ, starting from copied YPAO values if wanted |
| Through | No EQ (the factory default) |

For a small closed room, where one or two [room modes](../concepts/room-modes-and-correction-limits.md) usually dominate the bass, the Low Frequency entry is the important one. Yamaha's own description says it finds the frequency and stops; the manual's route is to copy those values into Manual with PEQ Data Copy and set Q and gain by hand. Manual PEQ covers 15.6 Hz to 16.0 kHz on the speakers and 15.6 to 250 Hz on the subwoofer, Q 0.500 to 10.080, and gain −20.0 to +6.0 dB (p.213). The number of bands per speaker is not stated in the pages read.

YPAO Volume, a volume-dependent loudness compensation, switches itself on after every measurement although its factory default is Off (pp.96, 408). Two speaker-setting patterns store separate layouts, distances, levels, PEQ and YPAO results, for example curtains open and closed (p.202), and Setup Reload restores the previous YPAO result after manual changes go wrong (p.217).

Receivers carrying it: [Yamaha RX-A4A](../products/yamaha-rx-a4a.md).

## Versions and tiers

YPAO has no paid tier, licence or companion app in any Yamaha source read; it ships built in with the supplied microphone. That is an absence in the documents rather than an explicit "free" statement. Feature sets differ by model (Yamaha RX-A4A specifications page, captured 2026-11-08):

| Model | YPAO features listed |
|---|---|
| RX-A4A (also A6A, A8A) | R.S.C. (Reflected Sound Control), 3D, 64-bit High Precision EQ Calculation, Low Frequency mode, Angle Measurement, multipoint |
| RX-A2A | R.S.C. only |

"Reflected Sound Control" appears only on the web spec page; the user guide does not use the term or explain what it changes, so its effect is a manufacturer claim with no mechanism given. The 64-bit EQ calculation is likewise a specification without a measured consequence.

## Measured and observed results

No independent measurement of YPAO on any receiver is in the evidence. Audioholics' RX-A6A bench test, a proxy, deferred YPAO testing to a later review. It did measure the manual PEQ: a 32 Hz filter at Q 1.6 and −8 dB measured close to the setting, and the reviewer counted the finer centre-frequency steps on recent Yamahas as a useful tool for hand-tuning (Audioholics, RX-A6A, 2021-12-22). Whether the A4A's PEQ has the same resolution is unconfirmed. The same review warns that Yamaha's Extra Bass mode, with speakers set Small, emphasises the second harmonic of frequencies the speakers cannot reproduce, which Yamaha says is deliberate; the reviewer advises leaving it off.

## Limits

- **Bass correction needs manual work.** The Low Frequency mode detects but does not correct, so getting a room mode under control means setting Q and gain by hand, ideally against an external measurement.
- The A4A's two subwoofer pre-outs carry the same signal: Yamaha's speaker-system pages state that two connected subs output the same sound (user guide, e.g. p.42). With one sub this does not matter; a second sub could not be delayed or equalised separately by YPAO. See [bass management and crossovers](../concepts/bass-management-and-crossovers.md).
- Multi Measure cannot be enabled when wireless (MusicCast Surround) speakers are used (pp.96, 98, 100, 103).
- Test tones play at high volume that cannot be lowered, and the operator has to stay in a back corner of the room during the run (pp.94, 100); the mic must be kept off warm equipment (p.96).
- WARNING 1 (possible reversed polarity) can fire with correct wiring depending on speaker type or room, and the manual says it may be ignored in that case; WARNING 3 flags large level differences and recommends matched speakers (pp.108–109).
- Factory defaults are all speakers Small, 80 Hz crossover, Parametric EQ Through (p.409), so nothing is corrected until YPAO is run and saved.
- How YPAO compares with [Audyssey MultEQ](audyssey-multeq.md), [Dirac Live](dirac-live.md) or [ARC Genesis](arc-genesis.md) in the same room is unknown.

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Yamaha, RX-A4A user guide (EN, AV19-0070, rev. H0), published 02/2025 — `yamaha-rx-a4a-user-guide.pdf`
- Yamaha USA, RX-A4A specifications (A4A/A8A/A6A/A2A table), captured 2026-11-08 — `yamaha-rx-a4a-specifications.md`
- Audioholics, Yamaha RX-A6A bench test, 2021-12-22 — `audioholics-yamaha-rx-a6a-bench-test.md`
