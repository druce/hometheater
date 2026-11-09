---
title: "Audyssey MultEQ (XT, XT32, MultEQ-X)"
slug: audyssey-multeq
kind: system
criteria: [1]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [denon-avr-x3900h-owners-manual-na.pdf, denon-avr-x3900h-info-sheet.pdf, denon-avr-x3900h-product-page.md, denon-avr-x2900h-info-sheet.pdf, denon-avr-x2900h-product-page.md, marantz-cinema-50-series-2-info-sheet-na.pdf, marantz-cinema-70s-series-2-info-sheet-na.pdf, v-avnirvana-denon-x2900h-x3900h-launch.md, audyssey-home-solutions-multeq-x.md, audyssey-multeq-x-microsoft-store-listing.md, v-apple-appstore-audyssey-multeq-editor.md, soundandvision-audyssey-multeq-x-review.md, soundandvision-audyssey-multeq-x-test-bench.md]
---

# Audyssey MultEQ (XT, XT32, MultEQ-X)

**Audyssey comes free on every Denon and Marantz candidate, as XT32 on the X3900H and CINEMA 50 Series 2 and as the lower XT on the X2900H and CINEMA 70s Series 2, but its built-in menus offer only three fixed curves; editable targets need the $19.99 iOS Editor app, which lists the 2026 models, or the Windows MultEQ-X, whose model list does not.**

Used by: [Room correction & bass management](../criteria/room-correction.md).

## What it does

Audyssey Setup measures every speaker through the supplied microphone from up to eight positions, then sets speaker distance, level, polarity and the subwoofer crossover from the first position and calculates correction filters that address both time and frequency response (X3900H owner's manual pp.183, 203–204). Denon recommends six or more positions, each after the first within about 2 ft (60 cm) of it, and the mic at least 20 in (50 cm) from walls. Distances, levels and crossovers can be edited afterwards without disabling the correction (p.214). Results save to Speaker Preset 1.

Running setup also enables three companion functions. Dynamic EQ is a volume-dependent loudness compensation, on by default, with a Reference Level Offset of 0, 5, 10 or 15 dB; it disables the tone controls (pp.123, 184–185). Dynamic Volume compresses level jumps and is switched to Medium if accepted at the end of setup. LFC (Low Frequency Containment) removes bass that would pass through walls and adds psychoacoustic processing to restore perceived bass; it is off by default and works only with XT32 (p.12, p.186). SubEQ HT, which levels and time-aligns up to four subs before correcting them together, does nothing for a one-sub room (p.12).

Receivers carrying it: [Denon AVR-X3900H](../products/denon-avr-x3900h.md), [Denon AVR-X3800H](../products/denon-avr-x3800h.md), [Denon AVR-X2900H](../products/denon-avr-x2900h.md), [Marantz CINEMA 70s Series 2](../products/marantz-cinema-70s-series-2.md), [Marantz CINEMA 50 Series 2](../products/marantz-cinema-50-series-2.md), [Marantz CINEMA 50](../products/marantz-cinema-50.md).

## Versions and tiers

The built-in tier is fixed by the receiver. Denon sells XT32 as "Platinum" and XT as "Silver" (Denon info sheets, 2026).

| Receiver | Built-in tier | Source | Editor app (iOS) | MultEQ-X (Windows) |
|---|---|---|---|---|
| Denon AVR-X3900H | MultEQ XT32 | Denon info sheet, manual p.183 | Listed | Not listed |
| Denon AVR-X3800H | Not confirmed in the sources read | — | Listed | Listed |
| Denon AVR-X2900H | MultEQ XT | Denon info sheet and product page | Listed | Not listed |
| Marantz CINEMA 70s Series 2 | MultEQ XT | Marantz info sheet p.2 | Listed | Not listed |
| Marantz CINEMA 50 Series 2 | MultEQ XT32 | Marantz info sheet | Listed | Not listed |
| Marantz CINEMA 50 | Not confirmed in the sources read | — | Listed | Listed |

App lists from the App Store and Microsoft Store, both captured 2026-11-08. XT32's marketed advantages over XT are higher filter resolution (Denon claims more than 10,000 control points) and the XT32-only LFC and SubEQ HT functions (X3900H info sheet; AV Nirvana launch article, 2026-05-14); Denon describes XT as low-frequency-focused and aimed at mid-size rooms. No source measures the audible difference between the two tiers.

The built-in menus give three curves plus Off: Reference (default, a slight treble roll-off), L/R Bypass (leaves the front left and right uncorrected) and Flat (suggested for small rooms with a close listening position) (X3900H manual p.183). A nine-band Graphic EQ (63 Hz to 16 kHz, −20 to +6 dB) works only with MultEQ XT32 switched off, and Curve Copy can load the Flat result into it as a starting point (pp.187–188).

**MultEQ Editor** (iOS, $19.99 on the App Store, 2026-11-08) edits the target curve per channel pair, moves the high-frequency roll-off, switches the midrange compensation dip on or off, and saves and loads calibrations. Its compatible list names the AVR-X3900H, AVR-X2900H, CINEMA 50 Series 2 and CINEMA 70s Series 2 explicitly. Sound & Vision used it chiefly to limit correction to the bass region, where room modes do most damage (S&V, 2022).

**MultEQ-X** is a Windows app from the Microsoft Store that is free to download, with calibration licensed by in-app purchase per user and per receiver serial number, for the life of that receiver and non-transferable (Microsoft Store listing, updated 2026-05-09). Sound & Vision gave the price as $199 one-time, with free upgrades, in its June 2022 review; the current price is not in the capture. It allows up to 32 positions, separate fully adjustable target curves per channel, parametric filters, and removal of Audyssey's 2–3 kHz midrange dip. It works only with Audyssey's batch-calibrated bundled mic or the individually calibrated ACM1-X ($79 in 2022), not a UMIK-1 (S&V, 2022). S&V found the learning curve steep and lost work to an unsaved session.

**2026-model support for MultEQ-X is unconfirmed.** The store's model list ends at the 2022–23 generation (X3800H, X2800H, S970H, CINEMA 50, CINEMA 70S) and states that unlisted models are not compatible. Against that, the same list also omits the X6800H, A10H and X1800H that the Editor app supports, so it lags generally, and S&V's 2022 rule of thumb was that any Editor-compatible receiver works with MultEQ-X. The vendor's explicit exclusion is the stronger evidence until Audyssey, Denon or an owner report says otherwise.

## Measured and observed results

The only bench result in the evidence is Sound & Vision's MultEQ-X test: before-and-after response at one seat, left channel, with two SVS SB-3000 subs in a large room, and a left/right match after correction (S&V test bench, 2022). The plotted data were not captured and the reviewer's verdict is subjective; it says nothing about built-in XT32 or XT, a one-sub system or a small room. S&V also doubted MultEQ-X's own estimate that its tower speakers reached 20 Hz in-room. The Editor app has 208 App Store ratings averaging 3.0 (2026-11-08), which measures user satisfaction with the app rather than correction quality.

## Limits

- **Direct and Pure Direct switch off MultEQ XT32**, Dynamic EQ, the Dirac filter and Graphic EQ, so corrected music needs a processed mode such as Stereo (X3900H manual p.133).
- XT32 cannot be selected for DTS:X above 48 kHz, and headphones set it to Off (p.183).
- Enabling a new speaker in Speaker Layout after setup disables MultEQ XT32, Dynamic EQ and Dynamic Volume until setup is re-run (pp.210, 214), so a future zone or extra speaker means recalibrating.
- Audyssey and [Dirac Live](dirac-live.md) can sit side by side, Audyssey in Speaker Preset 1 and Dirac in Preset 2, switched from the Option menu (p.128); a preset stores layout, distances, levels, crossovers and both systems' data (p.231). This allows a direct listening comparison on one receiver.
- Subwoofer distance reads longer than the physical distance because of the sub's own electrical delay; Denon calls this normal (p.210).
- Test tones are loud chirps, and noise or a volume change cancels a measurement (pp.204, 207).

## Sources

Full list: [bibliography](../reference/bibliography.md).

- Denon, AVR-X3900H owner's manual (NA), 2026 — `denon-avr-x3900h-owners-manual-na.pdf`
- Denon, AVR-X3900H info sheet and product page, 2026 — `denon-avr-x3900h-info-sheet.pdf`, `denon-avr-x3900h-product-page.md`
- Denon, AVR-X2900H info sheet and product page, 2026 — `denon-avr-x2900h-info-sheet.pdf`, `denon-avr-x2900h-product-page.md`
- Marantz, CINEMA 50 Series 2 and CINEMA 70s Series 2 info sheets (NA), 2026 — `marantz-cinema-50-series-2-info-sheet-na.pdf`, `marantz-cinema-70s-series-2-info-sheet-na.pdf`
- AV Nirvana, Denon AVR-X2900H and AVR-X3900H launch, 2026-05-14 — `v-avnirvana-denon-x2900h-x3900h-launch.md`
- Audyssey, Home Solutions: MultEQ-X and microphones, 2026-11-08 — `audyssey-home-solutions-multeq-x.md`
- Microsoft Store, MultEQ-X listing, updated 2026-05-09, captured 2026-11-08 — `audyssey-multeq-x-microsoft-store-listing.md`
- Apple App Store, Audyssey MultEQ Editor app, 2026-11-08 — `v-apple-appstore-audyssey-multeq-editor.md`
- Sound & Vision, Audyssey MultEQ-X review and test bench, 2022-06 — `soundandvision-audyssey-multeq-x-review.md`, `soundandvision-audyssey-multeq-x-test-bench.md`
