---
title: "Multiroom: receiver Zone 2, WiiM or Sonos"
slug: multiroom-options
kind: comparison
criteria: [3, 4, 7]
status: unverified
confidence: medium
last_verified: 2026-11-09
sources: [denon-avr-x3900h-owners-manual-na.pdf, onkyo-tx-rz50-spec-sheet.pdf, yamaha-rx-a4a-user-guide.pdf, r2-wiim-amp-product-page.md, r2-wiim-amp-pro-product-page.md, r2-wiim-help-amp-amp-pro-tech-spec.md, r2-wiim-amp-user-manual.pdf, wiim-amp-ultra-product-page.md, wiim-amp-ultra-user-manual.pdf, r2-wiim-sound-product-page.md, r2-wiim-sound-lite-product-page.md, r2-wiim-edition-a10-mkii-product-page.md, r2-wiim-edition-c10-mkii-product-page.md, r2-wiim-help-mrm-system.md, r2-wiim-help-multiroom-music.md, r2-wiim-help-multiroom-limitations.md, r2-wiim-help-pro-input-ports.md, r2-wiim-help-multiroom-audio-delay-sync.md, v-wiim-faq-apple-music.md, wiimforum-radio-paradise-lossless.md, r2-sonos-port-product-page.md, r2-sonos-port-setup-support.md, r2-sonos-amp-product-page.md, r2-sonos-wireless-speakers-product-pages.md, r2-sonos-music-service-pages.md, r2-sonos-supported-audio-formats.md, r2-sonos-trueplay-support-articles.md, r2-sonos-speaker-location-humidity-support.md, r2-sonos-airplay-support.md, r2-sonos-line-in-support-articles.md, r2-sonos-ceo-letter-app-update-2024-07-25.md, r2-denon-home-150-product-page-us.md, r2-denon-wireless-speakers-category-us.md, r2-denon-heos-1-archived-product-page-us.md, v-heos-cli-protocol-specification-v1.10.pdf]
---

# Multiroom: receiver Zone 2, WiiM or Sonos

**A WiiM Amp in each stereo room and WiiM speakers in the kitchen and bathroom, $1,116 at 2026-11-09 prices, keep the house in one app with Radio Paradise FLAC and AirPlay 2; the Amp's power rating has no stated conditions and no WiiM product has a bathroom rating.**

## Question

The main room is an [AVR-X3900H](../products/denon-avr-x3900h.md) running 5.1, fed Radio Paradise FLAC by a WiiM Pro on coax ([my system](../start-here/my-system.md)). Two stereo rooms with passive speakers, a kitchen and a bathroom are to be added, the last two with one wireless speaker each, all playing [Radio Paradise](../systems/radio-paradise.md) FLAC, Spotify and Apple Music. The routes are receiver Zone 2, WiiM per room, Sonos, and HEOS, costed for the four rooms only, excluding passive speakers and wire.

## Answer

**WiiM per room is the cheapest route that covers all four rooms in one app.** Two WiiM Amps ($329 each) and two Edition A10 MKII speakers ($229 each) total $1,116. The main-room Pro leads a [WiiM](../systems/wiim.md) group carrying its own Radio Paradise stream; groups are capped at 16 devices and 48 kHz/16-bit, which a 16/44.1 FLAC stream fits (WiiM help). The Amp and A10 MKII list AirPlay 2, and an Apple Music AirPlay group needs an AirPlay-capable lead, which the Pro and Amp are. The WiiM Sound ($299) and Sound Lite ($229) lack AirPlay 2. Weaknesses: the Amp's 60 W/ch into 8 Ω carries no THD, bandwidth or channels-driven condition anywhere WiiM publishes; Radio Paradise lossless on WiiM is owner-reported; casting or Roon into a WiiM group plays on the lead only, and the Pro's coax path can lag the other rooms by more than 50 ms, which WiiM's sync settings exist to correct.

**The recommendation's Amp Ultra per room costs $440 more and loses AirPlay 2.** The [Amp Ultra](../products/wiim-amp-ultra.md) ($549) is rated 100 W/ch into 8 Ω, two channels driven at 0.08% THD, and ASR measured about 97 W. With speaker sensitivity and room size unknown, that rating is its only case. The Amp Pro ($399) also lacks AirPlay 2.

**Zone 2 suits one stereo room, and only if wire from the rack is cheap to run.** The default Amp Assign (7.1ch + ZONE2) keeps 5.1 in the main room and powers Zone 2 from the HEIGHT2 terminals at the 105 W/ch rating (8 Ω, 20 Hz–20 kHz, 0.08% THD). Zone 2 accepts coax at 2-channel PCM, so the WiiM Pro's stream reaches it, as do HEOS and analog. It runs with the main zone off but keeps the receiver powered, with tone, level and a high-pass filter but no stated room correction or sub output; the manual does not describe HEOS app control of Zone 2. There is no Zone 3. A 9-channel receiver does not solve the second room: the [Onkyo TX-RZ50](../products/onkyo-tx-rz50.md) spec sheet claims powered Zone 2 and Zone 3, but Zone 3 takes analog and network only, not the WiiM's coax, and its terminal cost needs the manual. The Yamaha RX-A4A has Zone 2 only.

**[Sonos](../systems/sonos.md) costs $880 more and loses Radio Paradise FLAC,** which Sonos lists at standard quality. Apple Music is native at up to 24-bit/48 kHz, the one point where Sonos beats WiiM. Trueplay does not run on a Sonos Amp with third-party passive speakers. A Port at the receiver adds $499 and needs manual input selection on the X3900H, which has no trigger input. Sonos apologised publicly for its 2024 app.

**HEOS throughout cannot be fully priced.** Two Denon Home 150s cost $498; no HEOS stereo amplifier was researched for the second stereo room. [HEOS](../systems/heos.md) cannot play Radio Paradise FLAC, and its CLI spec limits sharing the receiver's coax input to one player or group, and not while the receiver plays it.

**Only Sonos portables carry a bathroom rating.** The Roam 2 ($179) is IP67; the Era 100 is "humidity resistant" without an IP rating. No WiiM speaker or current Denon Home model states an IP or humidity rating; the archived HEOS 1 was the last Denon speaker found claiming humidity resistance.

## Table

Maker list prices, 2026-11-09; passive speakers and wire excluded. A10 = Edition A10 MKII.

| Route | Rooms | Cost | Wiring | App | RP FLAC | Apple Music | Room correction | Bathroom rating | Main caveat |
|---|---|---|---|---|---|---|---|---|---|
| 2 × WiiM Amp + 2 × A10 | 4 | $658 + $458 = **$1,116** | Power, network | WiiM Home, with the main-room Pro | Built in, owner-reported lossless; 48/16 group cap | AirPlay 2 (A10 listing partly inconsistent) | RoomFit | None | Amp rating unconditioned |
| 2 × Amp Ultra + 2 × A10 (current plan) | 4 | $1,098 + $458 = $1,556 | Power, network | WiiM Home | As above | No AirPlay 2 on the Ultra | RoomFit | None | $440 more |
| Zone 2 + 1 × Amp + 2 × A10 | 4 | $0 + $329 + $458 = **$787** | Speaker wire to the Zone 2 room | Receiver for Zone 2, WiiM Home for the rest | Zone 2 via the Pro's coax | AirPlay 2 | None in Zone 2 | None | Zone 2 outside the WiiM app |
| 2 × Sonos Amp + Era 100 + Roam 2 | 4 | $1,598 + $219 + $179 = **$1,996** | Power, network | Sonos, a second app | Standard quality only | Native, to 24/48 | No Trueplay on the Amp; Trueplay on speakers | Roam 2 IP67 | Loses RP FLAC |
| Same + Port at the receiver | 4 | $1,996 + $499 = $2,495 | Port at the rack | Sonos and WiiM Home | WiiM via Port line-in at 16/44.1 | Native | As above | Roam 2 IP67 | Manual input selection |
| Zone 2 + 2 × Denon Home 150 | 3 | $498; fourth room unpriced | Speaker wire | HEOS, a second app | Not on HEOS | AirPlay 2 | Not researched | None stated | No HEOS stereo amp researched |

What would change the verdict:

- **A WiiM Amp bench test** well short of 60 W into 8 Ω, with low-sensitivity speakers, moves the stereo rooms to the Amp Ultra at the cost of AirPlay 2.
- **A bathroom that needs a rating.** The Roam 2 is on Sonos's AirPlay list, so an iPhone can send it Apple Music, but it needs the Sonos app and gets Radio Paradise at standard quality; an AirPlay group mixing it with WiiM devices is untested.
- **A device test of Radio Paradise on the WiiM Pro** (open questions #10, #23). Lossy output removes WiiM's Radio Paradise advantage over Sonos.
- **Wire runs.** A cheap run to one stereo room makes the $787 hybrid cheapest.

## Sources

Full list: [bibliography](../reference/bibliography.md). Files are listed in front matter: the X3900H manual, Onkyo and Yamaha zone documents, WiiM and Sonos product pages and help articles (2026-11-09), Denon Home pages, the HEOS CLI spec v1.10, and one WiiM forum thread (anecdote).

## Related


- [Streaming & multiroom](../criteria/streaming-and-multiroom.md)
- [WiiM](../systems/wiim.md)
- [Sonos](../systems/sonos.md)
- [HEOS](../systems/heos.md)
- [Recommendation](../decision/recommendation.md)
