---
title: "Buying checklist"
slug: buying-checklist
kind: decision
criteria: [6, 7]
status: settled
confidence: medium
last_verified: 2026-11-09
sources: [denon-avr-x3900h-owners-manual-na.pdf, v-denon-limited-warranty-new-2024dec12.pdf, dirac-live-upgrade-denon-avr-x3900h-pricing.md, wiim-pro-plus-product-page.md, wiim-amp-ultra-user-manual.pdf]
---

# Buying checklist

**The checks that make the purchase match what this wiki assumed: prices and dealer status before paying, then firmware, calibration order and three device tests inside the return window.**

Written for the [recommendation](recommendation.md): AVR-X3900H, Dirac Room Correction plus Bass Control, WiiM Pro on coax. Items marked (#n) close a question in the [open questions](../reference/open-questions.md); results go back into the wiki as an ingest.

## Before buying

- [ ] Re-check the three prices against the 2026-11-08 figures: X3900H $1,849 (denon.com), Dirac RC + Bass Control bundle $599 (dirac.com device page), WiiM Pro $169 (wiimhome.com). Product pages go stale in 60 days.
- [ ] Buy from Denon or an authorised dealer; the 3-year warranty depends on it (Denon limited warranty, 2024-12-12).
- [ ] Note the seller's return window and keep the device tests below inside it; no return terms were captured.
- [ ] Confirm the Dirac device page still lists the X3900H with Bass Control, and whether the bundle price is a promotion against the struck-through list.
- [ ] Find out whether Denon or Dirac supplies a microphone with the upgrade (#19). If not, budget for a calibrated USB mic.
- [ ] Buy one coaxial digital cable for the WiiM Pro; the X3900H has two coax inputs.
- [ ] If the RZ50 is still in play, settle speaker impedance first (#4).

## After unboxing

The full order and settings are on [setup and calibration](setup-and-calibration.md).

- [ ] Update firmware through the HEOS app before calibrating. Expect a mandatory HEOS account at first-run setup and a slow restart after the update (ASR reviewer observations).
- [ ] Place the sub before any calibration. Placement sets the starting point that correction works from ([room modes](../concepts/room-modes-and-correction-limits.md)).
- [ ] Run Audyssey XT32 and save it as a baseline. Then buy and run Dirac Room Correction plus Bass Control into a separate preset, so the two can be compared in the same room.
- [ ] Play corrected music in Stereo mode, since Pure Direct and Direct bypass both Audyssey and Dirac (manual p.133).
- [ ] WiiM Pro: set Fixed Volume on and EQ off for bit-perfect output, and leave RoomFit off ([WiiM](../systems/wiim.md)).
- [ ] Device test #10: play Radio Paradise in the WiiM app and read the format the app and the receiver report. 16-bit/44.1 kHz FLAC is the expected result.
- [ ] Device test #23: try Radio Paradise's `/flac` URL through Open Network Stream; record whether it plays and holds 16/44.1 out the coax.
- [ ] Fallback test: cast from the Radio Paradise app set to FLAC to the WiiM Pro over Google Cast.
- [ ] Optional test #22: send the `/flac` URL to the receiver with the HEOS CLI `play_stream` command.
- [ ] Spotify Connect and AirPlay 2 (Apple Music) to the receiver, once each.
- [ ] Log every result in `log.md` and update the system and product pages it touches.

## Related

- [Recommendation](recommendation.md)
- [Setup and calibration](setup-and-calibration.md)
- [Dirac Live (Room Correction, Bass Control, ART)](../systems/dirac-live.md)
- [Open questions](../reference/open-questions.md)
