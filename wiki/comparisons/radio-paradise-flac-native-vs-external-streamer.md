---
title: "Radio Paradise FLAC: native receiver vs external streamer"
slug: radio-paradise-flac-native-vs-external-streamer
kind: comparison
criteria: [3, 7]
status: unverified
confidence: medium
last_verified: 2026-11-08
sources: [radioparadise-ways-to-listen.md, radioparadise-faqs-and-info.md, radioparadise-stream-links-url-table.md, bluos-support-radio-paradise-articles.md, v-bluos-digital-passthrough-bluesound-players.md, bluesound-node-product-page.md, bluos-apple-music-support-2026-10-20.md, nad-t-758-v3i-data-sheet.pdf, wiim-pro-product-page.md, wiim-pro-plus-product-page.md, wiim-home-pc-app-help.md, v-wiim-faq-apple-music.md, wiimforum-radio-paradise-lossless.md, denon-avr-x3900h-owners-manual-na.pdf, dirac-pricing-and-device-pages.md, r2-wiim-sound-product-page.md]
---

# Radio Paradise FLAC: native receiver vs external streamer

**A $169 WiiM Pro on the receiver's coax input is the best route to Radio Paradise FLAC for this system: it costs least, leaves the receiver to be chosen for room correction, and shares an app with the future stereo rooms, though its lossless playback is owner-reported rather than documented.**

## Question

Should the main room get Radio Paradise FLAC from a receiver that plays it natively, which among the candidates means the NAD T 758 V3i on [BluOS](../systems/bluos.md), or from any receiver fed by an external streamer? The [owner accepted an external streamer](../start-here/my-system.md) on 2026-11-08, so the test is cost against confidence that the stream arrives lossless, with Spotify, Apple Music and the planned rooms covered.

Four routes are compared: the NAD natively; any receiver plus a WiiM Pro ($169) or Pro Plus ($219); any receiver plus a Bluesound NODE ($849); and, on a [HEOS](../systems/heos.md) receiver with no extra hardware, the Radio Paradise iOS app over AirPlay 2, or Roon. HEOS internet radio itself is out, because its manuals list WMA, MP3 and AAC only (X3900H manual pp.285, 303).

## Answer

**Buy the receiver for room correction and music performance, and put a WiiM Pro on its coax input.** Over coax the Pro and Pro Plus are equivalent; the Pro Plus's extra $50 buys an analog output stage this system would not use (WiiM Pro Plus page, 2026-11-08). The WiiM Home app lists Radio Paradise as a built-in service (WiiM PC-app help, 2026-09-24), owners report it plays lossless 16/44.1 FLAC (WiiM forum, 2024–2025; open question #10), and WiiM documents bit-perfect digital output with Fixed Volume on and EQ off. The same app runs the WiiM Amp Ultra proposed for the stereo rooms. The weak point: WiiM publishes nothing on the codec, and one owner saw a 320 kbps label in March 2025.

**The NAD is the only documented native path, and it costs the room-correction criterion.** At $2,299 it carries Radio Paradise inside the receiver, where the MQA unfold happens in the BluOS player itself, so the restriction that affects a NODE does not apply (BluOS support). But its Dirac tier is inferred as Limited with no Bass Control (Dirac device pages, 2026-11-08; open question #17), while the Onkyo TX-RZ50 at $1,399.99 includes full-bandwidth Room Correction and sells Bass Control for $299. Choosing the receiver for Radio Paradise gives up ground on the criterion ranked first, for a stream a $169 box can deliver.

**A NODE is the wrong streamer for this job.** It costs $680 more than a WiiM Pro, and the thing it would be bought for is undocumented: BluOS's Radio Paradise service is MQA, the unfold stays inside the player, and Digital Passthrough to an external DAC is capped at 24/96 (BluOS support, about 2024-11 and about 2026-06). Whether the NODE's coax carries plain FLAC or decoded PCM from the MQA stream is open question #13. Native Apple Music and BluOS's Radio Paradise login features do not cover the difference.

**The HEOS AirPlay or Roon route is a zero-cost fallback.** The RP iOS app offers ALAC and can AirPlay to AirPlay 2 devices (RP FAQ), and the only stated AirPlay 2 ceiling is WiiM's 44.1 kHz/16-bit (WiiM FAQ, 2025-09-11), which would fit the user-reported 16/44.1 stream. It is untested on a Denon or Marantz (#9, #24), the phone stays in the chain, and Roon needs a Core computer and a subscription.

## Table

Prices are list on the maker's site, 2026-11-08. "Extra cost" is what the route adds on top of whichever receiver is chosen; the NAD column is the receiver itself.

| | NAD T 758 V3i, native BluOS | Receiver + WiiM Pro / Pro Plus on coax | Receiver + Bluesound NODE on coax | HEOS receiver, RP app over AirPlay 2, or Roon |
|---|---|---|---|---|
| Extra cost | $2,299 receiver; no streamer | $169 / $219 | $849 | $0 for AirPlay; Roon subscription and a Core computer (price not in evidence) |
| Path | BluOS RP service, MQA unfolded in the receiver | WiiM Home RP service, or the `/flac` URL via Open Network Stream (#23); PCM out coax | BluOS RP service, MQA unfolded in the NODE; PCM out coax at up to 24/96 | iPhone RP app (ALAC) to the receiver's AirPlay 2 input; or Roon to Roon Ready |
| Lossless confidence | **Documented**: RP calls BluOS MQA its best-sounding option (broadcaster claim, unmeasured) | **Owner-reported** (#10); bit-perfect output documented with Fixed Volume on, EQ off | **Undocumented** at the digital output (#13) | **Untested** (#9); AirPlay 2 ceiling is a vendor-secondary claim (#24) |
| Metadata and control | Skip and pause; thumbs and My Paradise with an RP login (BluOS support) | Not documented for the built-in service; the URL route is reported to lose track metadata | Same BluOS features as the NAD | In the phone app |
| Spotify | Spotify Connect is a BluOS feature; V3i not named | Spotify Connect | Spotify Connect; Spotify Lossless listed | Spotify Connect on HEOS |
| Apple Music | AirPlay 2; native BluOS Apple Music unconfirmed on the V3i (#25) | AirPlay 2, 44.1/16 per WiiM | Native (announced 2026-10-20) and AirPlay 2 | AirPlay 2 |
| Room correction | Dirac Limited inferred, no Bass Control (#17) | Whatever the receiver has | Whatever the receiver has; NODE Dirac should stay off | Whatever the receiver has |
| Multiroom fit | BluOS: Pulse Flex ($429) for the kitchen; a different app from the Amp Ultra | WiiM Home, same app as the Amp Ultra; WiiM Sound speaker unpriced on 2026-11-08, $299.00 on 2026-11-09 | BluOS: Pulse Flex; a second app beside the Amp Ultra | HEOS: Denon Home speakers; a second app beside the Amp Ultra |

What would change the verdict: a device test reading the format a WiiM Pro sends out its coax for Radio Paradise (#10, #23) settles the WiiM column either way. If it showed lossy output, BluOS's answer to #13 would decide whether a NODE or the AirPlay route takes its place. Native Apple Music on the V3i (#25) does not move the NAD, whose problem is room correction.

## Sources

Full list: [bibliography](../reference/bibliography.md). Per-receiver evidence: [Radio Paradise](../systems/radio-paradise.md), [HEOS](../systems/heos.md), [streaming protocols](../systems/streaming-protocols.md).

- Radio Paradise, Ways to Listen; FAQs and Info; Stream Links URL table, 2026-11-08 — `radioparadise-ways-to-listen.md`, `radioparadise-faqs-and-info.md`, `radioparadise-stream-links-url-table.md`
- BluOS Support, Radio Paradise articles and Digital Passthrough article, captured 2026-11-08 — `bluos-support-radio-paradise-articles.md`, `v-bluos-digital-passthrough-bluesound-players.md`
- Bluesound, NODE product page, 2026-11-08 — `bluesound-node-product-page.md`
- Lenbrook / BluOS, "BluOS Now Supports Apple Music", 2026-10-20 — `bluos-apple-music-support-2026-10-20.md`
- NAD, T 758 V3i data sheet, 2020 — `nad-t-758-v3i-data-sheet.pdf`
- Dirac, device pages and pricing, 2026-11-08 — `dirac-pricing-and-device-pages.md`
- WiiM, Pro and Pro Plus product pages, 2026-11-08 — `wiim-pro-product-page.md`, `wiim-pro-plus-product-page.md`
- WiiM Help Center, WiiM Home App for PC, 2026-09-24; "Is Apple Music Supported?", 2025-09-11 — `wiim-home-pc-app-help.md`, `v-wiim-faq-apple-music.md`
- WiiM forum, Radio Paradise lossless thread, 2025-10 (anecdote) — `wiimforum-radio-paradise-lossless.md`
- WiiM, WiiM Sound product page, captured 2026-11-09 — `r2-wiim-sound-product-page.md`
- Denon, AVR-X3900H owner's manual (NA) — `denon-avr-x3900h-owners-manual-na.pdf`

## Related

- [Radio Paradise](../systems/radio-paradise.md)
- [BluOS (Bluesound, NAD)](../systems/bluos.md)
- [WiiM (WiiM Home, RoomFit)](../systems/wiim.md)
- [NAD T 758 V3i](../products/nad-t-758-v3i.md)
- [Denon AVR-X3900H](../products/denon-avr-x3900h.md)
- [Lossless streaming paths](../concepts/lossless-streaming-paths.md)
