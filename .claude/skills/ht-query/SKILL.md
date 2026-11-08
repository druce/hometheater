---
name: ht-query
description: Answer a question about AV receivers, room correction, streaming or the owner's setup from the home theater wiki, with citations, and file good answers back as comparison pages. Use for questions like "which is better for dual subs", "is Dirac worth it over Audyssey", "what should I buy", "compare X and Y", or any question the wiki should be able to answer.
---

# ht-query

Karpathy's **query** operation: the compiled wiki is the first place to look, not the raw sources.

## Hard stops

- **Answer from the wiki, then say where it is thin.** If the wiki lacks the answer, say so and
  propose an ingest (ht-research) rather than answering from memory as if it were sourced.
- **Never present an unverified number as settled.** Carry the page's `status` and `confidence`
  into the answer.
- **Ask before filing back.** A comparison page is a new page and goes through `MANIFEST.md`.

## Sequence

1. Read `wiki/index.md`, then `wiki/start-here/my-system.md` (every answer is relative to it).
2. Read the relevant `criteria/`, `systems/`, `products/` and existing `comparisons/` pages.
   If `comparisons/` already answers the question, start from it and check its date.
3. Answer: verdict first, then the reasoning, then a table if it is a comparison. Cite wiki pages
   by relative link and, through them, the sources. Name conflicts and unknowns.
4. If the answer is worth keeping, offer to file it as `wiki/comparisons/<slug>.md` (kind
   `comparison`: Question · Answer · Table · Sources). On yes: write it, link it from `index.md`
   and from at least one hub or product page, add the `MANIFEST.md` row, run
   `manifest_stats.py` and the gates, commit `query: <slug>`.
5. Append `## [YYYY-MM-DD] query | <question>` to `log.md` either way, noting gaps found. Gaps that
   need research go to `OPEN-QUESTIONS.md`.
