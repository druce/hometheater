# log.md

Append-only. Header format `## [YYYY-MM-DD] <op> | <title>`; ops: init, ingest, query, lint,
plan, write, decision. `grep "^## \[" log.md | tail -10` for recent history.

## [2026-11-08] init | scaffold

Repository created per the plan approved 2026-11-08: Karpathy three-layer layout (raw/, wiki/,
CLAUDE.md) with governance_wiki's machinery ported. Scripts adapted: source_manifest.py (raw/),
regroup.py, linkcheck.py and manifest_stats.py (no README page), wiki_lint.py (new kinds,
criteria 1–7, product spec completeness, UNRANKED, 60-day product staleness, marketing-adjective
bans; concern/control reciprocity and crosswalk checks dropped), gen_schema.py, and gen_matrix.py
replacing gen_crosswalk.py. restyle_check.py not ported. Skills: ht-research, ht-lint, ht-query.

Requirements (from the planning interview): 5.1/5.2 speaker layout, open budget, priorities room
correction and music/streaming. Next: interview for start-here/my-system.md, then seed raw/.

## [2026-11-08] write | start-here/my-system.md

Requirements from the interview: no sub owned yet (sub selection in scope), small closed room,
music from Radio Paradise FLAC + Spotify + Apple Music, one room now with four more rooms later
(two stereo, kitchen and bathroom wireless). Radio Paradise FLAC flagged as a discriminating
requirement; first-pass web findings (BluOS native, HEOS via TuneIn without FLAC, Roon AAC
fallback reports) recorded as unverified and logged as OPEN-QUESTIONS #2–4.
Accepted: ORPHAN on my-system.md (1 inbound, from index) until the skeleton creates the
criteria hubs that will link it.
