# Review package — theme:amethyst-v2

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:amethyst-v2 — origin CN, population #162 [GOSIGN2-LEDGER (b) row 162]
- Overall: EXCEPTION — named exception, outside the pass-eligible set: no candidate could be produced; the go-sign (COMPLETION-REPORT §10) covers the 286 pass-eligible themes with this exception standing [GOSIGN2-LEDGER (b) row 162; GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): EXCEPTION — no candidate exists; the part carries the theme as an unnamed exception row with all cells blank [T1-ROWS row 144]
- T2/T3 (render, combined verdict): NOT-RUN — [combined T2/T3] report `EXCEPTION` — standing named exception: component-family theme, no standalone candidate or sample could be produced (CN1 lane MANIFEST.md evidence; canonical file pages/theme:amethyst-v2-jp.txt absent); no T2/T3 runs were made. [RENDER-ROWS-2, where the row is spelled theme:amethyst-v2-jp]
- Engine coverage: not run [RENDER-ROWS-2 row]
- Credit modal: not applicable — no sample run exists [RENDER-ROWS-2 row]
- T4 (localize patterns + follow-up): N/A (named exception — no candidate) — display-affecting findings: 0 [LOCALIZE-ROWS row 287, where the fullname cell is blank]
- T5 (translation text): N/A (named exception — no candidate) — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 287]
- FIX5 re-judgement: none — the theme is the named exception and stands outside the 107-item register [GOSIGN2-LEDGER-SUPPLEMENT (d)]
- Computed against: canonical commit 435a6bb7193bf09bc02fa5bf529280c2a2389ec2; candidate file: absent (pages/theme:amethyst-v2-jp.txt does not exist); record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **EXCEPTION** — the single named go-sign exception; excluded from the 286 pass-eligible themes, not counted as a failure and not silently dropped [GOSIGN2-LEDGER.md §(b) row 162, §(d) item 1; GOSIGN2-LEDGER-SUPPLEMENT.md §§161, 164; COMPLETION-REPORT.md §147] |
| Effort class | Class S (special / bespoke), one of four; package kind K1 (no candidate exists) with composition K5b-2 (shell + three foreign components + ~199 KB external CSS) [ROLLOUT.md §2 Class S; SPECIAL-ROWS.md K1, K5b-2] |
| Ledger position | Population #162, origin CN; T1 = EXCEPTION, T2/T3 = NOT-RUN, T4/T5 = N/A; Overall = EXCEPTION (named) [GOSIGN2-LEDGER.md §(b) row 162] |
| Render | NOT-RUN as a **final disposition**, not a pending measurement — no candidate or sample page exists to render [GOSIGN2-LEDGER.md §(d) item 1; LEDGER-POPULATION-CHECK.md line 121; RENDER-ROWS-2.md, row `theme:amethyst-v2-jp`] |
| Package files | `original.txt` only. There is deliberately **no `candidate.txt`, no `diff.md` and no `classification.json`** — see Parts 2 and 3 [SPECIAL-ROWS.md K1] |
| Go-sign basis | COMPLETION-REPORT.md §10; the standard is the staff-skill sweep over all 287 themes with this exception standing [GOSIGN-TESTS.md line 29] |
| Named exception | This theme *is* the sweep's single named exception [GOSIGN2-LEDGER.md §(d) item 1; SPECIAL-ROWS.md K1; ROLLOUT.md Class S] |

## Provenance — Part 1 source

| | Original |
|---|---|
| Fullname | `theme:amethyst-v2` (there is no `-jp` candidate fullname) [sources.tsv row `amethyst-v2`; LEDGER-POPULATION-CHECK.md E3] |
| Wiki | `scp-wiki-cn.wikidot.com` [sources.tsv `wiki` = `scp-wiki-cn`; mirror INDEX.tsv row `theme:amethyst-v2`] |
| Page / URL | `theme:amethyst-v2` / `https://scp-wiki-cn.wikidot.com/theme:amethyst-v2` [sources.tsv; SPECIAL-ROWS.md K1] |
| Reference revision | 42. The mirror store records this revision's `updated_at` as 2026-08-24 03:04:21 and the page's `created_at` as 2025-11-08; the CN1 MANIFEST heading writes "rev 42, 2025-11-08" using the creation date. Both cite revision 42; the differing dates are the two timestamp fields, not two revisions [mirror INDEX.tsv; sources.tsv `rev_created_at`; lane-dsh-cn1 `evidence/amethyst-v2/original-meta.json`; MANIFEST.md §4] |
| Source of this copy | `review-mirrors/orig-amethyst-v2-rev42.txt`, store class **FETCH-EXCEPTION**, `source` = `FETCH 2026-11-17`; fetched once. The campaign cache `stage2-lanes/lane-oc-audit-inline/cache/cn/amethyst-v2.wikitext` carries the identical SHA-256, so the mirror is the cached revision-42 source, not a fresh re-fetch [mirror INDEX.tsv; sources.tsv; audit-inline cache] |
| Lines / bytes | 17 lines / 971 bytes, last line without a trailing newline [measured from `original.txt`; mirror INDEX.tsv `bytes` = 971; sources.tsv `mirror_bytes` = 971] |
| SHA-256 | `271c5a3272f28e0c48298d172854f5deae1ebd72d241290796990f505d2e05b7` — equal to the `mirror_sha256` in sources.tsv and the `sha256` in the mirror INDEX.tsv [verified by `sha256sum` on `review/amethyst-v2/original.txt`] |

Package files: `original.txt` (the frozen mirror above) and this README. No other file belongs to this package; in particular no candidate, diff or classification artifact exists or was synthesized.

## Part 1 — The mirror (present)

`original.txt` is a 17-line shell, not a theme. Read literally, line by line:

- **L1** — `[[module ThemePreviewer theme_url="https://g2lighter.github.io/theme/Amethyst%20V2/v2scp.css" noUi="true"]]` points the previewer at an external stylesheet on `g2lighter.github.io`.
- **L2–L5** — an `[[include :scp-wiki-cn:component:interwiki-style]]` at `priority=1`, `type=sidebar`, with `theme=` pointing at `https://g2lighter.github.io/theme/Amethyst%20V2/interwiki.css` — again external.
- **L6–L8** — `[[iftags +版式]]` wraps `[[include :g2lighter:component:v2desc-scp]]`, the description component, on another wiki.
- **L10–L13** — an empty `saving-page` div and an empty collapsible.
- **L15** — `[[include :g2lighter:component:v2para …]]`, the parametric applicator, with roughly twenty `{$…}` parameters (including a repeated `size` — `size={$size}` followed by `size=.82em` — carried verbatim from the original; there is no port here to correct it).
- **L17** — `[[include :g2lighter:component:v2ex]]`, the examples component.

The CSS named by L1 is itself a chain: `v2scp.css` (8,352 bytes) `@import`s `Amethyst V2.CSS` (184,131 bytes) and `scpComponent.css` (6,696 bytes), both on `g2lighter.github.io` — 199,179 bytes in total, the "~199 KB" of the record [lane-dsh-cn1 `evidence/amethyst-v2/upstream/v2scp.css` L9–L10; `evidence/_deps/Amethyst_V2.CSS` and `scpComponent.css`, bytes measured on disk; MANIFEST.md §4.1]. The three components are `v2desc-scp` (8,088 chars, rev 4), `v2para` (18,990 chars, rev 23) and `v2ex` (rev 65) [MANIFEST.md §4.1]. The mirror is therefore labelled honestly: it is the shell whose body lives on g2lighter, **not** a complete theme source. This is the K1 "part 1 present but misleading alone" case and the K5b-2 composition case [SPECIAL-ROWS.md K1, K5b-2].

## Part 2 — The candidate (absent)

**Signed statement: no candidate exists for this theme, and none is fabricated here.** `review/amethyst-v2/candidate.txt` is absent by design, and `pages/theme:amethyst-v2-jp.txt` is absent from the canonical repository [sources.tsv row `amethyst-v2`, `cand_fullname` and `candidate_path` empty; MANIFEST.md §4; RENDER-ROWS-2, row `theme:amethyst-v2-jp`; SPECIAL-ROWS.md K1]. The grounds, each from the record bytes:

1. **The production attempt was blocked.** The CN1 production lane produced four of its five themes and recorded amethyst-v2 as BLOCKED in MANIFEST.md §4 and §8. Its finding: the three `:g2lighter:` components do not exist on SCP-JP, on the Wikidot check wiki, or on the Wikijump instance, so a page carrying those includes renders three include-error boxes (its Check 3(a)); making the candidate standalone would mean inlining ~199 KB of CSS plus a 19 KB parameter engine, beyond a single theme page and beyond the lane's mandate; and the parameter API is a component contract, so porting it is a component review, not a theme-page port [MANIFEST.md §4.1, consequences (a)–(c); D2 in §7; lane verdict in §8].
2. **The prior-art translation does not fit the current form.** The reviewed Japanese file in `scp-wiki-translation` is 1,088 lines and reflects the superseded self-contained packaging; the live page at rev 42 is 17 lines. Porting it would ship a version the live page no longer ships while claiming revision 42 [MANIFEST.md §4.1 item (d); `evidence/amethyst-v2/prior-src.diff`, 34,836 bytes].
3. **The coordinator's three options were never resolved into a candidate.** The lane put to the coordinator: (i) a component-family port (port `g2lighter:component:v2para|v2ex|v2desc-scp` and settle where the 199 KB CSS lives), (ii) a self-contained reconstruction from the superseded packaging with an honest packaging revision, or (iii) leave the theme out of the CN batch [MANIFEST.md §4.2]. The campaign record shows option (iii) as the settled outcome: the theme is the named exception, excluded from the pass count, with a `/start` row added stating why no candidate could be produced [GOSIGN2-LEDGER.md §(d) item 1; COMPLETION-REPORT.md §§34, 131; canonical `start-themes.tsv`, amethyst row].

No candidate text is invented to make the package look complete. The empty `cand_fullname`/`candidate_path` cells in sources.tsv are the source of truth, not a gap to fill.

## Part 3 — The diff (absent)

**Signed statement: no diff exists for this theme, and none is fabricated.** A diff needs two sources; the candidate side is absent (Part 2), so any `diff.md` here would compare the mirror against an invented file. The generator's own package rule confirms the shape: `build_review.py.package_files()` requires both `original.<ext>` and `candidate.<ext>` before it treats a directory as a package, so this directory is not a diff-generating package and no `diff.md` is expected [review/build_review.py, `package_files()` / `packages()`]. No classification artifact is produced either: there is no candidate to classify against. This is the K1 rule "no diff may be fabricated against a nonexistent candidate" [SPECIAL-ROWS.md K1; cross-kind honesty rule 1].

## Part 4 — Explanation, status and disposition

**Why no candidate exists.** The original is a `[[module ThemePreviewer]]` shell whose substantive body is three components on `g2lighter` plus an externally hosted CSS chain of about 199 KB; the component set exists on none of the campaign's wikis, and no JP counterpart was ever prepared. That is the whole cause — it is an upstream composition/architecture property (K5b-2), not a localization defect in the porting lanes [MANIFEST.md §4, D2; sources.tsv `notes`; SPECIAL-ROWS.md K1/K5b-2]. The attempt record is Part 2's three grounds.

**Condition for revisiting.** The canonical `/start` row records it explicitly: "Revisit if the component set becomes available on the JP side" [canonical `start-themes.tsv`, amethyst row, detail text]. That is the stated gate; this package does not pre-empt it by inventing a component port.

**Row status (the adjudication, by name, not by measurement).**

- Named exception, excluded from the pass-eligible count of 286 (287 minus this row) [GOSIGN2-LEDGER.md §(b) row 162 and §(e) line 1721; GOSIGN2-LEDGER-SUPPLEMENT.md §§161, 164; COMPLETION-REPORT.md §147; GOSIGN-TESTS.md line 29].
- T1 (source check): EXCEPTION — the part carries the theme as an unnamed exception row with all cells blank [T1-ROWS.md row 144, line 152; LEDGER-POPULATION-CHECK.md E3].
- T2/T3 (render): NOT-RUN — a final disposition, not a pending measurement [RENDER-ROWS-2.md, row `theme:amethyst-v2-jp` line 76; LEDGER-POPULATION-CHECK.md line 121]. The report word `EXCEPTION` is preserved in the row's findings cell; no engine ran because there was no page to run on.
- T4/T5: N/A (named exception — no candidate); display-affecting findings 0 [LOCALIZE-ROWS.md row 287, line 303; GOSIGN2-LEDGER.md §(b) row 162]. The campaign records that T4/T5 are judged jointly and that amethyst is N/A exactly as min-theme/shushuin are N/A for a different reason (JP originals) [LOCALIZE-ROWS.md §9 note].
- The three spellings are one population row: T1 row 144's blank cell, LOCALIZE row 287's blank cell and RENDER-ROWS-2's `theme:amethyst-v2-jp` [LEDGER-POPULATION-CHECK.md E3 and normalization rule; GOSIGN2-LEDGER.md line 9 arithmetic: 269 measured + 17 rerun + 1 NOT-RUN = 287].

**Disposition class.** This verdict rests on the named-exception adjudication, not on a checker run, a render measurement or a diff — cross-kind honesty rule 4 [SPECIAL-ROWS.md]. The citations above are the adjudication; the EXCEPTION verdict stamp below is emitted mechanically from that same vendored record.

## Verification

- **Mirror integrity:** `sha256sum review/amethyst-v2/original.txt` = `271c5a3272f28e0c48298d172854f5deae1ebd72d241290796990f505d2e05b7`, 971 bytes — equal to `sources.tsv` `mirror_sha256` / `mirror_bytes` and the mirror INDEX.tsv row. No candidate file exists to compare (Part 2).
- **Generator:** `python3 review/build_review.py` and `python3 review/build_review.py --check` were run in this worktree. This package is not a diff-generating package (no `candidate.txt`), so no `diff.md` is emitted; the package was absent from the `--check` stale set measured before and after the package was added. The rest of the `--check` stale set (README generated regions of other lanes' packages) pre-dates this package and is not touched here.
- **Stamp citations:** every locator in the EXCEPTION stamp resolves against the vendored record — GOSIGN2-LEDGER (b) row 162, T1-ROWS row 144, LOCALIZE-ROWS row 287 and RENDER-ROWS-2's `theme:amethyst-v2-jp` row — checked with `build_review.check_stamp_citations()` (empty problem list).

## Generator behaviour — strain reported

The generator has an explicit `theme:amethyst-v2` branch inside `assemble_stamp()` (its `AMETHYST_LINES` constant) that emits the full EXCEPTION stamp, but `main()` applies stamps only to packages that have a `candidate.txt`. A K1 package has no candidate by definition, so `main()` neither regenerates nor `--check`es this package's stamp. To keep the stamp generator-emitted rather than hand-written, the block in this README was inserted by calling `build_review.assemble_stamp(rec, 'theme:amethyst-v2')` and `build_review.apply_stamp(...)` on this file; its bytes are exactly what the generator emits for the exception. This is a generator/workflow strain to report, not a reason to alter `build_review.py` (a file outside this package's assignment): the no-candidate case is handled in the stamp builder but unreachable from the generator's main loop. The package still behaves correctly under the generator — it is skipped cleanly, appears in no stale set, and its stamp's citations were verified independently with the generator's own citation checker.
