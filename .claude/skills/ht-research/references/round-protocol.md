# Round protocol — per-stage detail

Companion to `SKILL.md`. Adapted from governance_wiki's `wiki-research/references/round-protocol.md`.

## Survey brief (stage 2)

> Read `raw/<file>` once, for gist and provenance. Report: what it is (owner's manual / spec sheet /
> bench measurement / review / vendor doc / forum thread / retailer price capture); publisher and
> author as printed; publication or capture date; the public URL, verified by search, or
> `no public URL found`; which receiver models, room-correction systems and streaming platforms
> it covers; for measurements, the test conditions (load in ohms, channels driven, distortion
> threshold, bandwidth); depth; whether it is manufacturer, independent, or anecdote; and which
> other files in `raw/` it overlaps. Do not extract, quote, or judge it against the wiki.

Unconfirmed attributions are marked `(best guess)`; a wrong date on a review propagates into
staleness judgments.

## Manifest rows (stage 3)

```
TITLE | FILENAME | AUTHOR(S) | DATE | URL  [annotations]
```

Dates `YYYY-MM-DD`, `YYYY-MM`, or `... (best guess)`. Multiple authors separated by `;`.
Annotations: `[VENDOR]` marketing copy, `[ANECDOTE]` owner report, `[LOW RELEVANCE: why]`,
`[SUPERSEDED by <file>]`, `[REMOVED YYYY-MM-DD]`, `[PRICE YYYY-MM-DD]` for a dated price capture.

## Extract brief (stage 4)

> Read `raw/<file>` in full. Write `extracts/<slug>.md` and nothing else; do not touch `wiki/` or
> `MANIFEST.md`. Begin with:
>
> ```
> source: <exact filename>
> provenance: <publisher, title, version/firmware, date as printed>
> read: full | partial (sections X–Y, and why)
> ```
>
> Then one entry per claim:
>
> ```
> → products/denon-avr-x3800h.md          [spec | measurement | claim | opinion | price | anecdote]
> "verbatim from the source, exact"        (file.pdf p.12 / §Specifications / URL#anchor)
> note: test condition, which firmware, or what it contradicts elsewhere
> ```
>
> Quotes verbatim. One target page per entry; duplicate if it serves two. Use `NO-HOME` when no page
> owns it. In the final report flag: power figures without load/channels-driven, features that need
> a paid license, claims tied to a firmware version, marketing copy, and contradictions with other
> sources you know of.

## Triage (stage 5)

| Class | Becomes |
|---|---|
| Confirms | source added to the page's `sources:` |
| **Contradicts** | a correction, committed first, with both sources named |
| New, has a home | a threading edit: a link plus at most one sentence |
| New, no home | a candidate page argued at stage 7 |

## Verification standard (stage 6)

Per claim in `extracts/verification-<round>.md`:

```
claim: <page> — <the claim>
primary: <source, date>   confirms | contradicts | partial
detail: <what exactly matches or differs, incl. test conditions>
```

A manufacturer spec is primary for what the manufacturer claims, not for how the unit performs.
A bench measurement is primary for performance under its stated conditions only.

## Integration plan (stage 7)

1. New pages: path, kind, criteria, why it earns existence (≥2 inbound or >300 words).
2. Merges, splits, renames (slugs are never renamed once created; prefer a redirecting section).
3. Threading edits, one line each.
4. Corrections, each with the evidence.
5. Changes to rankings in `criteria/` hubs, with the reason.
6. **Deliberately not added, and why.** Zero new pages is a valid outcome.

## Writing order (stages 8–9)

Corrections commit → new pages → threading → ranking changes → `MANIFEST.md` rows → scripts →
`log.md` → ht-lint → commit. Verify every commit with `git show --stat`.
