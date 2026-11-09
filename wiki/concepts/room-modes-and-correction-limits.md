---
title: "Room modes and the limits of correction"
slug: room-modes-and-correction-limits
kind: concept
criteria: [1]
status: contested
confidence: medium
last_verified: 2026-11-08
sources: [ethanwiner-assessing-room-eq-dirac.md, v-welti-devantier-multisub-aes2006.pdf, soundandvision-audyssey-multeq-x-review.md, soundandvision-audyssey-multeq-x-test-bench.md, denon-avr-x3900h-owners-manual-na.pdf, denon-dirac-live-us.md, marantz-dirac-live-us.md, dirac-live-art.md, wiim-roomfit-settings-help.md]
---

# Room modes and the limits of correction

**Room correction can flatten the bass at the seat where it was calibrated, but with one subwoofer the improvement fades within a foot or two and can turn into a worse response than no correction, so sub placement, a second sub and absorption are the tools for anything beyond that seat.**

Used by: [Room correction & bass management](../criteria/room-correction.md). Terms: [glossary](../reference/glossary.md).

## The mechanism

At low frequencies a small room behaves as a set of standing waves. Their frequencies follow from the room's length, width and height; the axial modes, set by one dimension each, dominate in most rooms, and pressure is always at a maximum at the walls (Welti and Devantier, J. AES 2006-05, §2). Between the maxima sit nulls, which in the rooms Welti and Devantier measured were typically about 25 dB deep. Because the peaks and nulls are fixed in space, the response changes from one seat to the next, and the authors' conclusion is that with one sub a seat a few feet from the best spot will sound very different and nothing about the single sub can prevent it.

Equalisation acts on the signal before it reaches the room, so it changes level at a frequency everywhere at once. That makes peaks and nulls behave differently. A peak can be cut, and the cut helps wherever that peak is strong. A null is a cancellation at that position, and boosting it costs amplifier and driver headroom, raises distortion and, by Winer's account, can lengthen ringing (Winer, Assessing Room EQ: Dirac). His advice is to correct peaks rather than nulls, use lower-Q filters, and cut a peak by about half of what the measurement suggests. Correction systems expose the same choice: WiiM RoomFit has a Max Q control and a Non-Boost Mode (RoomFit settings help).

Vendors claim more than magnitude correction. Denon's manual says Dirac Live corrects the impulse response as well as frequency response, and that MultEQ XT32 corrects time and frequency problems in the listening area (X3900H manual, p.313–314); Dirac says ART reduces how long sound lingers in the room (Dirac ART page). These are manufacturer claims with no measurements in the sources. [Dirac Live](../systems/dirac-live.md) and [Audyssey](../systems/audyssey-multeq.md) carry the per-system detail.

### Measured seat-to-seat degradation

Two measured sources address how far a correction extends. They agree on direction and differ in method and interest.

| | Winer, Assessing Room EQ: Dirac (about 2020-09) | Welti and Devantier, J. AES 54(5) (2006-05) |
|---|---|---|
| What was tested | Dirac Live on a PC, default nine-position calibration and a one-position run; version not stated | Modelled and measured multi-sub layouts; no commercial correction product |
| Rooms and speakers | Large treated home studio with JBL 4430s; empty 10 ft bathroom (lowest mode 56.5 Hz) with one Mackie HR624 monitor; no subwoofer | Several listening rooms; 1 to 8 subwoofers; seating areas of several seats |
| At the calibrated seat | Response flattened in both rooms | Not the paper's question |
| 1 ft behind | Studio: improvement starting to fail, some useful correction left | n/a |
| 2 ft behind | Studio: worse than uncorrected at several bass frequencies. Bathroom: improvement completely lost and worse at 60 Hz and below | One sub: seats a few feet away differ greatly from the main seat |
| Decay (ringing) | Largest reduction 17 % at 49 Hz, about 1.6 dB, in the studio; in the bathroom the peak above 70 Hz rang longer, and null decay times grew | n/a |
| Limits | Author is a principal of RealTraps and designs bass traps; studio and bathroom, PC software, no sub; graphs not in the capture; no blind listening | Harman-funded; optimises multiple subs, which the owner does not have |

Winer's one-position calibration flattened the seat further and still degraded quickly a foot or two away. He reports the same pattern from an earlier Audyssey test that is not in the corpus, and a smaller degradation with Sonarworks (Update #2, 2020-09). His conclusion, that no device in the signal path can undo time-domain room problems and that reported clarity gains come from cutting boomy peaks, is his position and is contested by the correction vendors; no source here tests it blind. Welti and Devantier support the mechanism independently and peer-reviewed: a single-position filter cannot be right at positions where the modal response differs, which is why they move subwoofers before equalising.

### What placement, extra subs and treatment do

These act on the room's response, where EQ acts on the signal. Welti and Devantier show that multiple subs at wall midpoints, or measured best positions, cut seat-to-seat variance enough that a single global EQ then works across the seating area (see [bass management](bass-management-and-crossovers.md#what-a-second-sub-would-add)). Winer recommends as many bass traps as practical, then EQ only on the worst remaining peaks, and adds that a second sub fills nulls below the 80 Hz crossover that traps cannot reach; his target is a peak-to-null span cut from the typical 30 dB or more to about 10 dB. The sub itself matters too: Sound and Vision swapped a pair of small sealed SVS SB-3000s for larger ported PB-3000s in the same positions, without recalibrating, and reports an upgrade across the whole range although the EQ above 80 Hz was unchanged (S&V, Audyssey MultEQ-X review); that was a very large room with two subs.

## Why it matters for a 5.1 room

The owner's room is small and closed with one sub, which is the configuration both sources say a single-seat correction serves least well beyond the calibrated spot. Room dimensions are not yet known, so the mode frequencies cannot be computed; for scale, Winer's 10 ft bathroom had its lowest mode at 56.5 Hz. Three things follow. Calibrate for the seat you actually use. Choose the sub's position before buying room-correction upgrades, since placement changes what every correction system starts from. And if more than one seat matters, the evidence points to a second sub rather than a better EQ licence (see [my system](../start-here/my-system.md), where a second sub output is a nice-to-have).

## Common misconceptions

**"Multi-position calibration widens the sweet spot."** Marantz's Dirac page claims improved spaciousness throughout the listening area (Marantz Dirac Live page). Winer's nine-position Dirac calibration still lost its improvement within two feet; how much a multi-position average helps a one-sub small room has not been measured in any source in hand.

**"Room correction fixes ringing."** Vendors claim time-domain correction (Denon manual; Dirac ART page). Winer measured at most a 1.6 dB decay reduction, with some peaks and nulls ringing longer. ART was not part of his test, and no independent ART measurement is in the corpus.

**"A smoothed before-and-after graph proves it works."** Sound and Vision's MultEQ-X curves were taken at one position with 1/6-octave smoothing (S&V test bench). Winer argues that judging bass EQ needs unsmoothed responses and decay plots with 2 Hz (500 ms) resolution, and that waterfalls make cut peaks look as if they decay faster than they do (see [measurements and audibility](measurements-and-audibility.md)).

Toole's *Sound Reproduction* is often cited for the same conclusions; it was not read for this page, so it is not cited (open question 31).

## Sources

- Ethan Winer, Assessing Room EQ, Part 3 (Dirac), about 2020-09 (updates to 2020-09) — `ethanwiner-assessing-room-eq-dirac.md`
- Welti and Devantier, Low-Frequency Optimization Using Multiple Subwoofers, J. Audio Eng. Soc. 54(5), 2006-05 — `v-welti-devantier-multisub-aes2006.pdf`
- Sound and Vision, Audyssey MultEQ-X review — `soundandvision-audyssey-multeq-x-review.md`
- Sound and Vision, Audyssey MultEQ-X test bench — `soundandvision-audyssey-multeq-x-test-bench.md`
- Denon, AVR-X3900H Owner's Manual (North America), as captured 2026-11-08 — `denon-avr-x3900h-owners-manual-na.pdf`
- Denon, Dirac Live (US) page, as captured 2026-11-08 — `denon-dirac-live-us.md`
- Marantz, Dirac Live (US) page, as captured 2026-11-08 — `marantz-dirac-live-us.md`
- Dirac, Dirac Live Active Room Treatment page, as captured 2026-11-08 — `dirac-live-art.md`
- WiiM, RoomFit settings help, as captured 2026-11-08 — `wiim-roomfit-settings-help.md`

Full list: [bibliography](../reference/bibliography.md).
