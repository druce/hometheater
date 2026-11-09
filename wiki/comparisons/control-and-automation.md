---
title: "Control and automation: apps, Siri, Shortcuts, Home Assistant"
slug: control-and-automation
kind: comparison
criteria: [3, 6]
status: unverified
confidence: medium
last_verified: 2026-11-09
sources: [r4-apple-support-home-add-accessory-airplay.md, r4-apple-support-home-scenes-automations-hub.md, r4-apple-support-matter-accessories.md, r4-apple-support-siri-play-music.md, r4-apple-guide-home-app-iphone-homepod.md, r4-apple-developer-homekit-tv-receiver-types.md, r4-apple-shortcuts-guide-automation-siri-api-ios27.md, r4-apple-tv-guide-cec-receiver-control.md, r4-apple-appstore-denon-avr-remote.md, r4-apple-appstore-heos.md, r4-apple-appstore-onkyo-controller.md, r4-apple-appstore-third-party-denon-remotes.md, r4-apple-app-store-wiim-home.md, r4-apple-app-store-sonos.md, denon-avr-x3900h-owners-manual-na.pdf, denon-avr-x3900h-info-sheet.pdf, r4-denon-inside-denon-airplay-alexa-google.md, r4-denon-heos-cli-protocol-specification-v1.17.pdf, onkyo-tx-rz50-spec-sheet.pdf, r4-onkyo-tx-rz50-owners-manual-selected.md, r3-onkyo-tx-rz30-owners-manual-selected.md, r4-onkyo-iscp-spec-receivers-v1.15-2009-third-party-mirror.pdf, r4-homebridge-onkyo-plugins-npm.md, r4-wiim-help-apple-home-accessory.md, r4-wiim-help-siri-play-music.md, r4-wiim-help-smart-home-integrations-overview.md, r4-wiim-http-api-for-wiim-products.pdf, r4-wiim-linkplay-upnp-api-external.pdf, r4-wiim-support-page-api-documents.md, r2-sonos-app-release-notes.md, r4-sonos-community-shortcuts-play-content-thread.md, r4-sonos-siri-apple-home-support.md, r4-sonos-presets-support.md, r4-sonos-developer-control-api.md, r4-home-assistant-denonavr-integration.md, r4-home-assistant-heos-integration.md, r4-home-assistant-onkyo-integration.md, r4-home-assistant-wiim-integration.md, r4-home-assistant-sonos-integration.md, r4-home-assistant-homekit-bridge-integration.md]
---

# Control and automation: apps, Siri, Shortcuts, Home Assistant

**Siri and Apple Home can stop the WiiM but cannot power or switch either receiver, and neither Denon nor Onkyo ships Shortcuts actions. The full "stop Radio Paradise and let me watch TV" sequence is documented only through Home Assistant and its HomeKit Bridge.**

## Question

The owner, on iPhone and iPad, wants app control of the receiver and the multiroom system ([WiiM](../systems/wiim.md), or [Sonos](../systems/sonos.md)), then Siri and Shortcuts acting across devices: one phrase that stops Radio Paradise on the WiiM Pro, switches the receiver to the TV input with a movie sound mode, and turns the TV on ([my system](../start-here/my-system.md); the TV model is still unknown).

## Answer

**Apple's native routes reach music only.** The WiiM Mini, Pro, Pro Plus and Amp join Apple Home as AirPlay 2 speakers: Siri plays by room, pauses, skips and sets volume, with no input, preset or power control (WiiM help, 2026-04-27). Apple documents "stop playing music in the bedroom" (support 105053, 2025-11-19) and AirPlay speakers in scenes (102313). Home offers input selection only for TV accessories (iPhone User Guide), and AirPlay does not imply Home support, Apple's example being Samsung TVs (104998, 2026-03-03). HomeKit's audio-receiver category needs HAP, which no candidate claims, and Home's Matter support has no media types (102135, 2026-05-07). Whether Siri's stop halts a stream WiiM Home started natively is undocumented.

**No receiver maker ships Shortcuts actions.** The App Store listings for Denon AVR Remote, HEOS, Onkyo Controller and WiiM Home claim no Siri, Shortcuts or widget support (2026-11-09), though only a device can confirm absence. Sotto, a third-party app, claims Shortcuts actions for Denon power, input and scenes, but runs the X3900H in "experimental mode" (12 ratings; unverified). Shortcuts' Get Contents of URL makes HTTP requests; Apple is silent on LAN targets and self-signed certificates. WiiM's HTTP API v1.2 documents stop, play URL, volume, presets 1–12 and input switching, with no authentication described and no grouping, and specifies HTTPS while writing several examples as http.

**Sonos alone ships native Shortcuts actions, and they stop short of this scenario.** App 86.00.41 (2026-06-09) added Play Content, Create Group, Ungroup, Play/Pause, Set Mute and Set Volume, plus Night Sound and Speech Enhancement on 2026-09-08 (release notes): no stop, input, preset or power. A forum user reports Play Content limited to Favorites (anecdote), and Sonos says Apple Home cannot control its speakers directly, against Apple's scene page. The advantage is real for music but does not reach the receiver, so it does not reopen the [multiroom verdict](multiroom-options.md), which rests on Radio Paradise FLAC and cost.

**Home Assistant is the only documented end-to-end route.** The denonavr integration (local push) handles power, source, volume, sound mode and Zone 2 over TCP 23, 8080 and 60006, and its telnet option takes the receiver's single telnet connection; the X3800H is tested, the X3900H unlisted. The HEOS integration (Platinum) adds playback, inputs, Quick Select and groups, without power. The WiiM integration (HA 2026.4, Platinum) covers play/stop, volume, input, presets, grouping and URL play. HomeKit Bridge exposes a receiver-class media player as a HomeKit receiver (power, play/pause, source, volume steps; one per accessory-mode bridge) and a script as a switch, so Siri or a Home scene can fire a "Watch TV" script. Sound mode is not mapped, so it goes in the script or a Quick Select. The unstated cost is an always-on, owner-maintained host: a hobbyist-grade dependency in the TV path.

**A lighter partial route needs no hub.** Siri pauses the WiiM by room. With HDMI Control on, TV Audio Switching (default On) moves the X3900H to TV Audio on the TV's CEC command, and an Apple TV with "Control TVs and Receivers" turns TV and receiver on together (Apple TV guide). Sound mode is not set, the Denon manual never says the receiver turns the TV on, and the chain is untested.

**One setting matters on either route.** HDMI Control is off by default (X3900H manual p.191). Turning it on brings Power Off Control's default, All, which puts the receiver in standby whenever the TV turns off, coax music included (p.192); set it to Video. Network Control must stay Always On (the default) for apps, web control and HEOS (p.241), at under 2 W standby (info sheet).

**Denon is modestly ahead of Onkyo on control, and the receiver ranking stands.** The [X3900H](../products/denon-avr-x3900h.md) has a web control page with source, sound mode and Quick Select and no login described (manual pp.154–156), a Denon-hosted HEOS CLI v1.17 on port 1255 (playback, input, URL, Quick Select and groups, but no power or sound mode), four Quick Selects storing input, sound mode and Dirac slot (pp.147–150), and a Platinum HA integration. The [RZ50](../products/onkyo-tx-rz50.md) relies on eISCP (port 60128), documented only by a 2009 spec on a third-party mirror with a one-client limit; HA's Onkyo integration is Bronze; homebridge-onkyo was unpublished on 2026-11-08; Network Standby may switch itself off after a network loss (manual p.150); Web Setup defaults to admin/admin (p.157). Its Works with Sonos mode lets the Sonos app wake it and switch input (pp.103–104). The [RZ30](../products/onkyo-tx-rz30.md) appears only in its own manual's app and Network Standby pages. None of this outweighs room correction in the [recommendation](../decision/recommendation.md).

**Worked sequence, "Watch TV" through Home Assistant:**

1. Stop the WiiM Pro: HA WiiM stop (documented), or Siri by room (documented for AirPlay streams only).
2. Power the X3900H and recall a Quick Select holding TV input, Movie mode and Dirac slot: HA HEOS `quick_select`, or denonavr power, source and sound mode (documented by HA; untested on the X3900H).
3. Turn the TV on: an HA integration for the TV (model unknown) or CEC from the Apple TV (documented by Apple; untested here).
4. Trigger: expose the script through HomeKit Bridge and say "Hey Siri, turn on Watch TV" (documented piecewise; untested end to end).

## Table

App Store ratings captured 2026-11-09. HA = Home Assistant quality tier.

| Device | iOS app (rating) | Siri / Home | Shortcuts actions | Local API, maker-documented? | Home Assistant | Power | Input switch | Scene / preset |
|---|---|---|---|---|---|---|---|---|
| Denon X3900H | AVR Remote 2.0 (1,456); HEOS 4.39 (27,267) | AirPlay playback only | None claimed; Sotto (third party) | Web page and HEOS CLI yes; IP protocol not in manual | denonavr (X3900H untested); HEOS Platinum | App, web, HA | App, web, HEOS CLI, HA, CEC | 4 Quick Selects, network-recallable |
| Onkyo RZ50 / RZ30 | Onkyo Controller 2.2 (627) | AirPlay playback only | None claimed | eISCP: 2009 third-party mirror only | Bronze; Homebridge plugin removed | App, HA (Network Standby) | App, HA, CEC, Sonos link | None found |
| WiiM Pro / Amp | WiiM Home 3.87 (1,963) | Play, pause, skip, volume by room | None documented | HTTP v1.2 and UPnP, yes | Platinum (2026.4) | No wake command | HTTP API, HA | Presets 1–12 over HTTP |
| Sonos | Sonos 4.57 (944K) | AirPlay; no direct Home control per Sonos | Six, plus two home-theater | Control API: cloud OAuth, or LAN with key | Bronze; needs UPnP on | n/a | Line-in via Control API | Favorites; presets app-only |

What would change the verdict:

- **A receiver maker adding Shortcuts (App Intents) actions** for power and input would remove the hub.
- **The X3900H confirmed on HA denonavr** or the HEOS CLI's Quick Select would settle step 2.
- **Testing Get Contents of URL against the WiiM** over HTTPS and HTTP decides whether Shortcuts alone can stop it.

## Sources

Full list: [bibliography](../reference/bibliography.md). Files are in front matter: Apple, Denon, Onkyo, WiiM, Sonos, Home Assistant and Homebridge documentation and App Store listings captured 2026-11-09, plus one Sonos forum thread (anecdote).

## Related

- [Usability, app & firmware support](../criteria/usability-and-support.md)
- [Multiroom options](multiroom-options.md)
- [HEOS](../systems/heos.md)
- [WiiM](../systems/wiim.md)
- [Sonos](../systems/sonos.md)
- [Buying checklist](../decision/buying-checklist.md)
