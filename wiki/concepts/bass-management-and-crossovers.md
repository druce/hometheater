---
title: "Bass management and crossovers"
slug: bass-management-and-crossovers
kind: concept
criteria: [1, 4]
status: settled
confidence: medium
last_verified: 2026-11-08
sources: [denon-avr-x3900h-owners-manual-na.pdf, denon-avr-x3900h-info-sheet.pdf, yamaha-rx-a4a-user-guide.pdf, onkyo-tx-rz50-spec-sheet.pdf, sony-str-an1000-help-guide.pdf, audioholics-yamaha-rx-a6a-bench-test.md, audioholics-anthem-mrx-740-1140-bench-test.md, asr-onkyo-tx-rz50-review.md, marantz-cinema-50-series-2-info-sheet-na.pdf, marantz-cinema-70s-series-2-info-sheet-na.pdf, wiim-roomfit-help.md, wiim-roomfit-settings-help.md, wiim-ultra-product-page.md, v-welti-devantier-multisub-aes2006.pdf, v-marantz-cinema-70s-series-2-owners-manual-selected.md]
---

# Bass management and crossovers

**With one subwoofer, bass quality comes down to the per-speaker crossover, the sub's distance and level, and where the sub sits; on a Denon the listening mode chosen for stereo music also decides whether the sub plays at all and whether room correction stays on.**

Used by: [Room correction & bass management](../criteria/room-correction.md) · [Amplification & pre-outs](../criteria/amplification-and-preouts.md). Terms: [glossary](../reference/glossary.md).

## The mechanism

A 5.1 receiver sends two bass streams to the sub. One is the LFE channel, the ".1" the mixer authored, under its own low-pass filter: 70 to 250 Hz, default 120 Hz, on the Denon AVR-X3900H (Denon X3900H manual, p.233). The other is redirected bass: each speaker given a crossover is high-passed and everything below the crossover goes to the sub (manual, p.230). The two are separate menus, so the LFE low-pass does not change where your speakers hand off.

Crossovers are set per speaker on every candidate whose documentation is in hand:

| Receiver | Crossover choices | Default | Source |
|---|---|---|---|
| Denon AVR-X3900H | Full Range, 40, 60, 70, 80, 90, 100, 110, 120, 150, 180, 200, 250 Hz | 80 Hz | manual p.230 |
| Onkyo TX-RZ50 | 40, 50, 60, 70, 80, 90, 100, 120, 150, 180, 200 Hz, per channel | not stated | spec sheet p.1 |
| Yamaha RX-A4A | Small/Large per speaker; 40, 60, 80, 90, 100, 110, 120, 160, 200 Hz | 80 Hz, all Small | user guide p.205, 208, 409 |
| Sony STR-AN1000 | per speaker, set by Auto Calibration, manually adjustable; range not in captured text | measured | help guide p.212 |

On the Denon a speaker can be Full Range only if the fronts are, and with no sub the fronts are forced to Full Range (manual, p.230); Yamaha behaves the same and suggests Small for any woofer under 16 cm (user guide, p.205).

Measured filter slopes are uneven. Yamaha specifies a 12 dB/octave high-pass on the speakers and a 24 dB/octave low-pass on the sub (RX-A4A user guide, p.405), and Audioholics measured exactly that on the RX-A6A at 80 Hz (Audioholics, RX-A6A bench test). Audioholics measured the Anthem MRX 740/1140 sub output at 12 dB/octave instead of the expected 24, on firmware current at the time of the test and not named (Audioholics, MRX 740/1140 bench test); the MRX 540 8K has not been measured, so this does not carry to it. Denon, Onkyo and Marantz publish no slopes here.

Distance and level align the sub with the mains in time and loudness. On the X3900H, Distances run 0.0 to 59.1 ft (0.0 to 50.0 ms under Dirac Live) and sub level −12 to +12 dB (manual, p.171, 228). [Audyssey](../systems/audyssey-multeq.md) sets distance, level, polarity and sub crossover from the microphone; the manual notes that a sub usually measures farther away than it is, because of its own electrical delay. Yamaha has only a Normal/Reverse phase switch in the pages read (user guide, p.210) and says to set the sub's crossover knob to maximum and its level to half before calibrating, leaving the receiver's filter as the only low-pass (p.94). Denon's Bass Sync delays only the LFE track of multichannel discs and is not a sub alignment control (manual, p.171).

### Stereo music: LFE versus LFE + Main on Denon and Marantz

The Denon Subwoofer Output setting has two values (manual, p.232). **LFE**, the default, sends the LFE track plus bass redirected from speakers that have a crossover set. **LFE + Main** also copies the low bass of any speaker set to Full Range into the sub, through a Bass Extraction LPF of 40 to 250 Hz (default 80 Hz) that applies only to Full Range channels.

The listening mode matters as much. In two-channel Direct, Pure Direct and DSD Direct the sub plays only with LFE + Main (manual, p.304), and Direct and Pure Direct switch off MultEQ XT32, Dynamic EQ, the [Dirac Live](../systems/dirac-live.md) filter and Graphic EQ (p.133). That leaves two coherent setups for stereo music:

| Goal | Fronts | Subwoofer Output | Mode | Room correction |
|---|---|---|---|---|
| Corrected bass, sub carries the low end | crossover (e.g. 80 Hz) | LFE | Stereo or another processed mode | on |
| Minimum processing | Full Range | LFE + Main | Direct / Pure Direct | off |

The first row is this page's reading of the manual's routing rules; Denon prints no mode-by-mode table. The CINEMA 70s Series 2 manual has the same LFE and LFE + Main menu and the same warning that full-range fronts on LFE can leave the sub silent; the captured pages do not cover the Direct-mode rule, so that part is unverified for Marantz.

Other brands differ. Yamaha has a single Use/None sub switch (user guide, p.209) plus, per Audioholics, an Extra Bass feature that copies bass from Large mains to the sub (RX-A6A bench test). On the Anthem MRX 740/1140, mains without a crossover leave the sub on a 40 Hz low-pass for two-channel music unless Super Sub Fronts is used (Audioholics, MRX 740/1140 bench test). On the [Onkyo TX-RZ50](../products/onkyo-tx-rz50.md), ASR measured that enabling bass management forces resampling, and that Pure mode, which avoids it, disables bass management (ASR, TX-RZ50 review, 2022-02-12); whether the resampling is audible is disputed in the same thread (see [measurements and audibility](measurements-and-audibility.md)).

### What a second sub would add

A second sub mainly makes the bass consistent across more than one seat (Welti and Devantier, Harman, J. AES 54(5), 2006-05). With one sub, seats a few feet from the best spot respond very differently and no placement avoids it. Across more than 100,000 modelled layouts in rectangular rooms, wall midpoints were best for one to four subs; four at the midpoints was the best practical layout, two at opposite midpoints nearly as good with more output, and more than four not worth it. In their measured room 1, the best two locations with gain and delay optimised cut seat-to-seat variance from 33.4 dB² with one corner sub to 8.0 dB² (Table 4). The paper optimises several seats with Harman's own method and tests no commercial AVR feature.

The X3900H has four sub outputs with separate level and distance, plus a Directional/Standard Subwoofer Mode (manual, p.11, 224); the Sony STR-AN1000 has two, with no per-sub level or distance found in the sections read (help guide, p.34, 46). Per [my system](../start-here/my-system.md), a second sub output is a nice-to-have.

## Why it matters for a 5.1 room

The speakers and sub are not chosen yet, so no crossover can be named; 80 Hz, the Denon and Yamaha default, is the starting point. Because music is a priority, the Denon mode choice above matters most: Pure Direct with a sub gives up room correction across the whole range. With one sub in a small closed room, its position decides how far from the main seat the bass stays even (see [room modes and the limits of correction](room-modes-and-correction-limits.md)). For the future stereo rooms, the WiiM app exposes sub crossover and level (WiiM Ultra product page), and enabling Subwoofer Calibration restricts [RoomFit](../systems/wiim.md) to stereo correction (WiiM RoomFit help).

## Common misconceptions

**"Pure Direct is the best mode for music."** On the X3900H it disables all room correction and plays the sub only with LFE + Main (manual, p.133, 304), while at low frequencies the room dominates what you hear (Welti and Devantier, §1).

**"Bass management is for bookshelf speakers; music wants full-range mains."** The ASR reviewer suggested full-range speakers to avoid the RZ50's resampling, and a forum member replied that such resampling is practically inaudible unless the resampler is broken (ASR, TX-RZ50 thread, 2022-02-12). Welti and Devantier summarise the listening research as finding spatial effects of bass-managing two-channel music below 80 Hz subtle at best, and note, citing earlier work, that skipping bass management can produce seat-to-seat variation of 40 dB or more at some frequencies.

**"A sub distance longer than the tape measure is a calibration error."** Denon's manual says the sub's own electrical delay makes it normal (manual, Audyssey Setup).

## Sources

- Denon, AVR-X3900H Owner's Manual (North America), 2026-11-08 — `denon-avr-x3900h-owners-manual-na.pdf`
- Denon, AVR-X3900H information sheet, 2026-11-08 — `denon-avr-x3900h-info-sheet.pdf`
- Yamaha, RX-A4A User Guide, 2026-11-08 — `yamaha-rx-a4a-user-guide.pdf`
- Onkyo, TX-RZ50 spec sheet, 2026-11-08 — `onkyo-tx-rz50-spec-sheet.pdf`
- Sony, STR-AN1000 Help Guide, 2026-11-08 — `sony-str-an1000-help-guide.pdf`
- Marantz, Cinema 50 Series 2 and Cinema 70s Series 2 information sheets (NA), 2026-11-08 — `marantz-cinema-50-series-2-info-sheet-na.pdf`, `marantz-cinema-70s-series-2-info-sheet-na.pdf`
- Marantz, CINEMA 70s Series 2 owner's manual, selected pages, captured 2026-11-08 — `v-marantz-cinema-70s-series-2-owners-manual-selected.md`
- Audioholics, Yamaha RX-A6A bench test results — `audioholics-yamaha-rx-a6a-bench-test.md`
- Audioholics, Anthem MRX 740/1140 bench test results — `audioholics-anthem-mrx-740-1140-bench-test.md`
- Audio Science Review, Onkyo TX-RZ50 review and thread, 2022-02-12 — `asr-onkyo-tx-rz50-review.md`
- WiiM, RoomFit help, RoomFit settings help and WiiM Ultra product page, 2026-11-08 — `wiim-roomfit-help.md`, `wiim-roomfit-settings-help.md`, `wiim-ultra-product-page.md`
- Welti and Devantier, Low-Frequency Optimization Using Multiple Subwoofers, J. Audio Eng. Soc. 54(5), 2006-05 — `v-welti-devantier-multisub-aes2006.pdf`

Full list: [bibliography](../reference/bibliography.md).
