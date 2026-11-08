---
name: ht-lint
description: Lint, validate and clean up the home theater wiki — front matter, product spec completeness, required sections, word limits, marketing adjectives, link graph, orphans, unranked products, MANIFEST sync, staleness — plus the semantic lint a script cannot do (contradictions between pages, stale prices, superseded models, gaps a web search could fill). Use when asked to lint, check, audit or clean up the wiki, at the end of an ingest, or before committing wiki changes.
---

# ht-lint

Karpathy's **lint** operation. Mechanical findings are fixed by script; prose findings by reading
the page and rewriting it. Regex substitution across pages is how a cleanup becomes drift.

## Hard stops

- **Never edit `raw/`.** `wiki_lint.py --fix` refuses to touch residue there.
- **Never invent a value** to clear `FM-PRODUCT`. An unknown spec stays `?` and is a research task.
- **Never pad** a page to its word floor. `WORDS-LOW` is a merge candidate.
- **Never bump `last_verified` without re-checking** the page's sources. A moved date with no new
  check destroys the only staleness signal.
- **Never re-fix an accepted exception.** Check `log.md` first.

## Sequence

1. **Measure** (note counts before changing anything):
   ```bash
   python3 scripts/wiki_lint.py
   python3 scripts/linkcheck.py --quiet
   python3 scripts/source_manifest.py
   ```
2. **Regenerate** (no judgment, always safe):
   ```bash
   python3 scripts/regroup.py
   python3 scripts/manifest_stats.py
   python3 scripts/gen_matrix.py
   python3 scripts/gen_schema.py
   ```
3. **AUTO fixes:** `python3 scripts/wiki_lint.py --fix`.
4. **JUDGE findings:** `python3 scripts/wiki_lint.py --judgment`, read each page in full first.

   | Code | Fix |
   |---|---|
   | `BANNED` | Rewrite with the number or measurement the adjective was standing in for, or delete the sentence if there is none. |
   | `CLAIM` | Opening bold line must be a verdict, e.g. which room and priority this model wins for. |
   | `SEC-MISSING` | Write it. "Known issues" and "Limits" name real failures with sources, or say none were found and where you looked. |
   | `FM-PRODUCT` | Find the primary source; if none, leave `?` and log it in `OPEN-QUESTIONS.md`. |
   | `UNRANKED` | Add the product to the relevant hub's "How the candidates rank", or record why it is out of the running. |
   | `ORPHAN` / `DEPTH` | Link from the hub and a sibling page; never move or rename. |
   | `STALE` | Re-check price/availability/successor against primaries, then move the date; otherwise lower `confidence`. |
   | `MANIFEST` | Add the row by hand, re-run `manifest_stats.py`. |
   | `WORDS-HIGH` / `WORDS-CEIL` | Propose a split; do not perform it unasked. |

5. **Semantic lint** (no script can do this):
   - Contradictions: same spec stated differently on a product page and a system or comparison page.
   - Superseded: any product with a newer successor announced (search manufacturer lineups).
   - Prices older than the 60-day budget, or a street price above MSRP.
   - Missing pages: a concept or system linked in prose but without its own page or section.
   - Gaps: questions in `wiki/reference/open-questions.md` a web search could now answer.
6. **Verify and report:**
   ```bash
   python3 scripts/wiki_lint.py && python3 scripts/linkcheck.py --quiet
   ```
   Append `## [YYYY-MM-DD] lint | <scope>` to `log.md`: fixed by code, every page whose prose was
   rewritten, what could not be fixed and why, exceptions accepted with reasons. Commit as one
   change (`lint: <scope>`), then `git show --stat`.
