---
title: "Setup and calibration"
slug: setup-and-calibration
kind: decision
criteria: [1, 2, 6]
status: unverified
confidence: medium
last_verified: 2026-11-09
sources: [denon-avr-x3900h-owners-manual-na.pdf, v-welti-devantier-multisub-aes2006.pdf, ethanwiner-assessing-room-eq-dirac.md, dirac-live-room-correction.md, v-dirac-live-bass-control-expanded.md, v-arcam-ava15-ava25-owners-manual-v1.5.pdf, wiim-pro-plus-product-page.md, wiim-amp-ultra-user-manual.pdf]
---

# Setup and calibration

**On the AVR-X3900H with one sub, setup runs in a fixed order: place the sub, set the speakers and the 80 Hz starting crossover, calibrate Audyssey XT32 into Preset 1, then Dirac into Preset 2, and play music in Stereo rather than Pure Direct.**

Written for the [recommendation](recommendation.md) and run after the firmware and dealer checks on the [buying checklist](buying-checklist.md). Page references are to the Denon AVR-X3900H owner's manual (NA) unless stated. Status is unverified because no step has yet been run in this room; results go back into the wiki as an ingest.

## 1. Place the sub before measuring anything

Placement changes the room response itself, while every correction system only changes the signal, so it comes first and every later step depends on it ([room modes and correction limits](../concepts/room-modes-and-correction-limits.md)). With one sub the response at seats a few feet from the main one will differ greatly whatever the position (Welti and Devantier, J. AES 2006-05). In their modelling of rectangular rooms, wall midpoints were the best positions for one to four subs, which makes a wall midpoint the first candidate here. Calibrate for the seat actually used.

The sub's own crossover knob goes to maximum, or its LFE input is used, so the receiver's filter is the only low-pass in the chain. Yamaha's user guide says this explicitly (p.94); Denon's manual does not state it, and the same logic applies.

## 2. Speaker setup

- **Layout:** 5.1, set before calibrating. Changing the layout after calibration disables Audyssey (pp.210, 214) and Dirac (p.275) until each is re-run.
- **Crossover:** 80 Hz, the Denon default, on every speaker until the speakers are chosen and measured; the X3900H offers 40 to 250 Hz per speaker or Full Range (p.230). A speaker can be Full Range only if the fronts are.
- **Subwoofer Output:** LFE, the default (p.232). LFE + Main matters only for full-range fronts in Direct modes, which this setup does not use.
- **LFE low-pass:** 120 Hz default (p.233). It filters the authored ".1" channel only and does not move the speaker crossovers ([bass management and crossovers](../concepts/bass-management-and-crossovers.md)).

## 3. Audyssey XT32 into Preset 1

[Audyssey](../systems/audyssey-multeq.md) is included and gives a free baseline before any Dirac purchase.

- Use the supplied mic at ear height at the main seat for the first position, at least 20 in (50 cm) from walls. Denon recommends six or more positions, each within about 2 ft (60 cm) of the first (pp.203–204).
- Keep the room quiet; noise or a volume change cancels a measurement (pp.204, 207).
- Expect the sub's distance to read longer than the tape measure, because of its electrical delay; Denon calls this normal (p.210).
- Curve: try Reference and Flat. Denon suggests Flat for a small room with a close listening position (p.183).
- Dynamic EQ is on by default and Dynamic Volume is offered at the end of setup (pp.184–185). Dynamic Volume compresses level changes, so music listening is better off without it.
- Results save to Speaker Preset 1 (p.214).

## 4. Dirac Room Correction and Bass Control into Preset 2

[Dirac Live](../systems/dirac-live.md) runs from Dirac's desktop software or phone app and exports its filters to the receiver, which saves them to Preset 2 on first export (p.128). Preset 1 keeps the Audyssey result, so the two can be compared in the same room from the Option menu.

- **Microphone.** Dirac names a UMIK-1-class external mic; whether Denon or Dirac supplies one with the upgrade is open (#19).
- **Positions.** Use the main seat and a tight cluster around it. Winer's nine-position Dirac calibration lost its improvement within about 2 ft of the seat, so a wide spread buys little in a one-sub room (Winer, about 2020-09).
- **Bass Control** computes the crossovers, sub distance and level that Room Correction alone leaves to hand (Arcam AVA15/AVA25 manual p.40, describing the same licence).
- **Target curve and boosts.** Cut peaks and limit boost into nulls. Winer suggests boosts of no more than about 5 dB, since filling a null costs headroom and can add ringing. Dirac lets the target be drawn to allow this.
- **Re-run** after any layout change or sub move.

## 5. Compare and choose

Switch between Preset 1 and Preset 2 at the same volume and on the same tracks. Preference here is a listening judgment in one room. No source in the wiki measures the difference between XT32 and Dirac with one sub, so the result belongs in the [open questions](../reference/open-questions.md) as owner evidence.

## 6. Music modes

Play stereo music in **Stereo**, not Direct or Pure Direct. Those two modes switch off MultEQ XT32, Dynamic EQ, the Dirac filter and Graphic EQ (p.133), and with fronts on a crossover and Subwoofer Output on LFE they also leave the bass below the crossover unplayed. The trade between corrected and minimally processed playback is set out in [bass management and crossovers](../concepts/bass-management-and-crossovers.md#stereo-music-lfe-versus-lfe--main-on-denon-and-marantz).

## 7. WiiM Pro on coax

- Connect the [WiiM Pro](../systems/wiim.md)'s coax output to one of the X3900H's two coax inputs and assign the input to a source name.
- Turn **Fixed Volume on and EQ off** for bit-perfect output (WiiM Pro Plus FAQ; Amp Ultra manual p.18), and leave RoomFit off. Volume and correction then belong to the receiver.
- Run the [Radio Paradise](../systems/radio-paradise.md) device tests on the buying checklist: format in the WiiM app (#10), the `/flac` URL by Open Network Stream (#23), and casting from the RP app as fallback.

## What this doesn't cover

Speaker-specific crossover choices wait on the speakers (#4). A second sub would change steps 1 and 4, since Welti and Devantier's two-sub midpoint layouts cut seat-to-seat variation substantially and Bass Control then has more than one sub to align. Calibration of the future stereo rooms belongs to the WiiM Amp Ultra and RoomFit ([WiiM Amp Ultra](../products/wiim-amp-ultra.md)), where enabling Subwoofer Calibration limits RoomFit to stereo mode.

## Related

- [Buying checklist](buying-checklist.md)
- [Recommendation](recommendation.md)
- [Bass management and crossovers](../concepts/bass-management-and-crossovers.md)
- [Room modes and the limits of correction](../concepts/room-modes-and-correction-limits.md)
