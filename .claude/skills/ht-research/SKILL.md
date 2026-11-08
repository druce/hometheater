---
name: ht-research
description: Ingest new source documents in raw/ into the home theater wiki — detect what arrived, survey and manifest it, extract and verify it, then propose an integration plan before writing. Use when manuals, spec sheets, reviews, measurement reports, forum threads or price captures have been added to raw/, when the user says "ingest", "a new review is in", "I clipped an article", or asks whether the wiki is current with its sources. Stops for approval before creating pages or restructuring anything.
---

# ht-research

Karpathy's **ingest** operation with governance_wiki's rigor. Read `references/round-protocol.md`
before stage 2: subagent briefs, manifest row format, extract grammar, triage rules, plan template.

## Hard stops

- **`raw/` is read-only**, `manifest.txt` excepted. A source edited is a source no longer trusted.
- **No verbatim source text in `wiki/`.** Extracts are scratch; the wiki paraphrases and cites.
- **Stage 7 is a hard stop.** No page is created, merged, split or renamed before approval,
  because restructuring after drafting costs a rewrite.
- **Corrections commit before additions**, so a wrong spec fixed is not buried in a feature commit.
- **Never invent a number.** A spec, price, or measurement no source gives stays `?`.
- **Serialize `MANIFEST.md` writes.** Parallelize reading; never parallelize the registry.

## Two paths

- **Light path** (one clipped article or review, owner present): read it, tell the owner the 3–5
  takeaways and any contradiction with existing pages, agree what to change, then update every
  page it touches, `index.md`, `MANIFEST.md`, and append an `ingest` entry to `log.md`. Still add the
  manifest row and still run ht-lint before committing.
- **Full round** (several sources, or a new product family): the nine stages below.

## The nine stages

1. **Detect.** `python3 scripts/source_manifest.py`. NEW / GONE / UNEXTRACTED all empty → say so
   and stop. Check `manifest.txt` annotations (`[LOW RELEVANCE]`, `[SUPERSEDED]`) before treating an
   UNEXTRACTED file as work.
2. **Survey.** One subagent per NEW file, in parallel: what it is, publisher/author, date, URL,
   which models and systems it covers, depth, test conditions if it is a measurement report,
   first-party (manufacturer) vs independent vs anecdote. No extraction.
3. **Manifest.** Append rows to `raw/manifest.txt` under a dated `#` block:
   `TITLE | FILENAME | AUTHOR(S) | DATE | URL  [annotations]`. GONE rows get `[REMOVED YYYY-MM-DD]`.
4. **Extract.** One subagent per file, holding the `MANIFEST.md` page list, writing only
   `extracts/<slug>.md` in the arrow grammar. Then `python3 scripts/regroup.py`.
5. **Triage.** Each claim: confirms (add source to front matter) / **contradicts** (a correction) /
   new with a home (threading edit) / new with no home (candidate page). Typical contradictions in
   this domain: power ratings at different load or channels driven, a feature that needs a paid
   upgrade, a firmware feature announced but not shipped, a model superseded.
6. **Verify.** Every number against the primary source; hardest where a review quotes a figure the
   manufacturer does not publish. Evidence blocks to `extracts/verification-<round>.md`; dead ends
   to `OPEN-QUESTIONS.md` with what would settle them.
7. **Checkpoint.** Present the integration plan (template in references) and **stop**.
8. **Write.** Corrections (own commit) → new pages → threading. New pages need ≥2 inbound links,
   and a new product needs a ranking line in at least one `criteria/` hub.
9. **Close.** Add `MANIFEST.md` rows by hand → `manifest_stats.py` → `gen_matrix.py` →
   `log.md` entry → **ht-lint** → commit `ingest: <what>` → `git show --stat`.

```bash
python3 scripts/source_manifest.py
python3 scripts/regroup.py
python3 scripts/manifest_stats.py && python3 scripts/gen_matrix.py
python3 scripts/wiki_lint.py && python3 scripts/linkcheck.py --quiet
```

## Report

To `log.md`, header `## [YYYY-MM-DD] ingest | <batch>`: what the survey found → contradictions
found in existing pages → what was verified and against what → conflicts shown rather than
resolved → deliberately not added, and why → numbers (sources, entries, pages touched). To the
owner: the same, shorter, plus anything that changes the current shortlist.
