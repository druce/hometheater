---
title: "Open questions"
slug: open-questions
kind: reference
criteria: []
status: contested
confidence: medium
last_verified: 2026-11-09
sources: []
---

# Open questions

**Five unknowns could still change the purchase (speaker impedance, the Onkyo limiter, Radio Paradise lossless on the WiiM, what the Dirac licence and mic cover, and current list prices), and most of them are settled by the owner's speaker choice or a device test rather than by more reading.**

This is the reader-facing list. Each item gives its number in the build register, `OPEN-QUESTIONS.md`, where the evidence trail is kept; settled questions (#1, #3, #8, #11, #15, and #2 mostly) remain recorded there and are not repeated here. Items are judged against the [recommendation](../decision/recommendation.md): Denon AVR-X3900H, Dirac Room Correction plus Bass Control, and a WiiM Pro on coax, with the Onkyo TX-RZ50 as the conditional alternative.

## Open

### Could change the recommendation

- **Speaker impedance and sensitivity, and the room's dimensions (#4).** The front, centre and surround speakers have not been chosen. This matters because the [Onkyo TX-RZ50](../products/onkyo-tx-rz50.md) limited power at 4 Ω and not at 8 Ω in ASR's test, so nominal 8 Ω speakers without deep impedance dips reopen it as the $749-cheaper route, while 4 Ω or 6 Ω speakers close it ([amplification and pre-outs](../criteria/amplification-and-preouts.md)). Only the owner can settle it, by choosing the speakers and reading their impedance curves.
- **Whether the Onkyo limiter is fixed, and how often it triggers (#6, #14).** RZ50 firmware notes through 2026-03-03 are silent on protection, and ASR found the same latched limiting on a Pioneer sibling on February 2026 firmware and on the TX-RZ30 in May 2026. For a 5.1 system at small-room levels the useful number is whether five channels ever reach the threshold, and nobody has measured it; only an AC-cord pull clears the limiter once it engages. An ASR or Audioholics sweep of the [RZ50](../products/onkyo-tx-rz50.md) on current firmware settles #6, and a fixed-level five-channel bench test or an owner log with a power meter settles #14.
- **Whether Radio Paradise plays lossless on the WiiM Pro (#10, #23).** The WiiM app lists Radio Paradise as a built-in service, but WiiM publishes no codec, and lossless 16/44.1 playback rests on owner reports; separately, nobody reports playing Radio Paradise's `/flac` URL through Open Network Stream on a Pro or Pro Plus. The WiiM Pro is the recommended path to Radio Paradise FLAC, so a lossy result moves the plan to casting the Radio Paradise app over Google Cast, and only failure there reopens the [NAD T 758 V3i](../products/nad-t-758-v3i.md) on BluOS ([WiiM](../systems/wiim.md); [native vs external streamer](../comparisons/radio-paradise-flac-native-vs-external-streamer.md)). A device test reading the format the app and the receiver report settles both; the [buying checklist](../decision/buying-checklist.md) schedules it inside the return window.
- **What the $299 Bass Control licence covers, and whether a Dirac mic comes with a Denon upgrade (#19).** Denon and Marantz manuals list only the Audyssey microphone. A missing mic adds the cost of a calibrated USB mic to the [X3900H](../products/denon-avr-x3900h.md) total; licence coverage for more than one sub matters only if a second sub is added later. Dirac's licence terms, Denon's Dirac setup documentation, or a support reply settles it ([Dirac Live](../systems/dirac-live.md)).
- **Current list prices (#29).** The RZ50 is $1,399.99 on onkyo.com against an implied $1,699.99 reference price; at the higher figure its saving against the X3900H falls from $749 to $449. The [Yamaha RX-A4A](../products/yamaha-rx-a4a.md) lists at $1,399.95–$1,599.95 at retail, and the [WiiM Amp Ultra](../products/wiim-amp-ultra.md) at $549 against ASR's $529, with its security-support end date unresolved. A price check on the manufacturer pages at purchase settles it.

### Settled by a device test after purchase

- **Radio Paradise FLAC on the receiver itself, via Roon or AirPlay (#9).** The X3900H is Roon Ready and has AirPlay 2, and the Radio Paradise iOS app offers ALAC, but no route has been tested. It matters only as a backup to the WiiM path ([HEOS](../systems/heos.md); [streaming protocols](../systems/streaming-protocols.md)).
- **The Radio Paradise `/flac` URL through the HEOS CLI `play_stream` command (#22).** The X3900H manual lists internet-radio formats as WMA, MP3 and AAC only, so the result is uncertain. A local test with the HEOS CLI settles it ([HEOS](../systems/heos.md)).
- **One-app multiroom through Google Cast groups (#33).** Whether a receiver's Google Cast joins a Cast group with WiiM players decides how the main room and the two future stereo rooms are grouped. A Google Home group test settles it ([streaming and multiroom](../criteria/streaming-and-multiroom.md)).
- **MultEQ-X support for the X3900H (#5).** The iOS MultEQ Editor app lists the X3900H and X2900H, while the 2026-05-09 MultEQ-X listing omits them. XT32 is the baseline calibration before Dirac, so this decides whether that baseline can be edited on a PC. An owner calibration attempt or an Audyssey statement settles it ([Audyssey MultEQ](../systems/audyssey-multeq.md)).
- **Maximum sample rate on the coax and optical inputs (#12).** The X3900H, CINEMA Series 2, RZ50 and MRX 540 manuals are silent. Radio Paradise FLAC is 44.1 kHz, so this does not bind the recommended chain; a 96 or 192 kHz test file settles it ([lossless streaming paths](../concepts/lossless-streaming-paths.md)).

### Would not change the choice

- **#7** No bench test of the [NAD T 758 V3i](../products/nad-t-758-v3i.md) exists. Its problem here is room correction, which a measurement would not change.
- **#13** What a [Bluesound NODE](../systems/bluos.md) sends out its digital output for Radio Paradise (MQA unfolds in the player). Relevant only if the WiiM and Cast routes both fail; a BluOS support reply or device test settles it.
- **#16** Whether Yamaha's NET RADIO carries Radio Paradise FLAC ([MusicCast](../systems/musiccast.md)); an external streamer avoids the question.
- **#17** The bandwidth of Dirac included on the [Arcam AVA15](../products/arcam-ava15.md), and whether NAD's V3 licence applies to the V3i. Neither is shortlisted.
- **#18** Itemised Dirac tier prices on the [CINEMA 70s Series 2](../products/marantz-cinema-70s-series-2.md) and [CINEMA 50 Series 2](../products/marantz-cinema-50-series-2.md) ([which licence](../comparisons/which-dirac-license-to-buy.md)).
- **#20** Which Dirac tier gates custom target curves and third-party mics; the recommended bundle buys Full Room Correction ([Dirac Live](../systems/dirac-live.md)).
- **#21** Missing spec captures for the [AVR-X3800H](../products/denon-avr-x3800h.md) and the [AVR-X2900H](../products/denon-avr-x2900h.md)'s Zone 2 HDMI and "Pre-out 2.2". The X3800H is the fallback only if the X3900H's price rises.
- **#24** An Apple primary source for the AirPlay 2 format ceiling, which bears only on the AirPlay backup route ([streaming protocols](../systems/streaming-protocols.md)).
- **#25** Whether native Apple Music on BluOS reaches the [NAD T 758 V3i](../products/nad-t-758-v3i.md).
- **#26** Whether the [CINEMA 70s Series 2](../products/marantz-cinema-70s-series-2.md) repeats Series 1's 4 Ω warm-up distortion; it lacks Bass Control in any case.
- **#27** [RZ50](../products/onkyo-tx-rz50.md) sub pre-out independence, AirPlay version and the RZ70's limiter status. With one sub, independence costs nothing.
- **#28** Whether the [Anthem MRX 540 8K](../products/anthem-mrx-540-8k.md) is Roon Ready and loses SINAD with the sub disabled as the 1140 does.
- **#30** [Arcam AVA15](../products/arcam-ava15.md) US stock and sub-output independence; it sits $2,351 above the X3900H to target.
- **#31** Whether Toole supports the seat-to-seat EQ finding and whether ASR publishes SINAD band cut-offs ([room modes](../concepts/room-modes-and-correction-limits.md); [measurements and audibility](../concepts/measurements-and-audibility.md)).
- **#32** Denon and Marantz spare-parts policy for HDMI boards after warranty, known only from AVS Forum anecdotes ([value and reliability](../criteria/value-and-reliability.md)).
- **#34** The NAD V3i's digital input count and maximum rates ([connectivity](../criteria/connectivity.md)).
- **#35** Whether every HEOS receiver requires a HEOS account, and warranty terms for Yamaha, Anthem, NAD, Arcam and WiiM ([usability and support](../criteria/usability-and-support.md)).
- **#36** Whether a Dirac licence transfers on resale, and Arcam's HARMAN ownership from a primary source ([value and reliability](../criteria/value-and-reliability.md)).
- **#37** Conflicting HDMI counts in Anthem's and Arcam's own documents ([MRX 540 8K](../products/anthem-mrx-540-8k.md), [AVA15](../products/arcam-ava15.md)); current rear-panel pages settle them.

## Related

- [My system: requirements](../start-here/my-system.md)
- [Recommendation](../decision/recommendation.md)
- [Buying checklist](../decision/buying-checklist.md)
- [Bibliography](bibliography.md)
