# Review package — theme:diamond-highlighter-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:diamond-highlighter-jp — origin EN, population #81 [GOSIGN2-LEDGER (b) row 81]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 81]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 0 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 101; GOSIGN2-LEDGER (b) row 81]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — chromium-320 header wordmark clipped + webkit-320 footer license clipped; engine-divergent wordmark vs canonical = stale test-wiki page state (noted, not a defect); sample overflow 337–419px; assets 404 deferred. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 81, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 81]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 81]
- Computed against: canonical commit 1869877ffdcd33cb214b8dc421fb39e3de8d7e8d; candidate file pages/theme:diamond-highlighter-jp.txt sha256:968b6a54e3024f63fff1fe523fe679037a0ef9696e2610dcb10f7c51be4c086e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/diamond-highlighter-jp/candidate.txt (sha256 968b6a54e3024f63fff1fe523fe679037a0ef9696e2610dcb10f7c51be4c086e)
Original: theme:diamond-highlighter — scp-wiki, revision 11 (sha256 0d208a5404c0ee400d3badc7772e2f3bca950cd77c30fd598c94e4a8050657d7)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 81); one of the 286 of 286 pass-eligible themes. The generated stamp above also reads PASS: no post-verdict commit has touched the candidate |
| The class-U question | This theme sits in class U because its render record cites the FIX3-S2EN adjudication. The wave's own report lists the theme among its 29 **no-edit** pages, and the file history agrees: no wave edited this candidate. Section "Per-theme record" item 1 records the attribution gap in full |
| Standing items | **DISPOSITIONED** — T1 baseline pseudo-ref×3 (class (iii), section 11); the render row's items (KB-35 narrow-width clips; the KB-49 stale-page caution; KB-33/KB-34 sample overflow; KB-58 deferred assets); T4's P9 (ruling 2) and P11 (sibling / batch-posting class) |
| Record defect flagged | The review/sources.tsv note for this row claims the original was superseded upstream after the reference revision. The row's own cited follow-up artifact records rev11 → rev11, no changes. Flagged in the Per-theme record (item 4) for the coordinator's correction; this package follows the artifact |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:diamond-highlighter | theme:diamond-highlighter-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 11, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 11 | — |
| Source of this copy | Campaign mirror store (hash-verified against review/sources.tsv) | Canonical file `pages/theme:diamond-highlighter-jp.txt`, created in commit 184cb65 (Stage 2 EN8 integration); its only later change is commit 1869877 (the translator normalization) |
| Lines | 143 (generator count, diff.md) | 150 (generator count, diff.md) |
| SHA-256 | 0d208a5404c0ee400d3badc7772e2f3bca950cd77c30fd598c94e4a8050657d7 | 968b6a54e3024f63fff1fe523fe679037a0ef9696e2610dcb10f7c51be4c086e |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard). No production counterpart exists, so the R4 question does not arise. Reference-revision currency: revision 11 is still the upstream latest — the T4 follow-up artifact `diff-diamond-highlighter-from11.txt` records rev11 → rev11, no changes.

Wave history: none. The candidate's whole history is the EN8 port (184cb65) and the population-wide translator normalization inside 1869877. The FIX3-S2EN wave report (REPORT-GOSIGN2-FIX3-S2EN.md) names this theme in its no-edit list: "no in-scope display defect evidenced, or only disposition classes". What the register's class-U placement rests on is the citation of that report inside the theme's render items, where it serves as the disposition authority for the KB-35/KB-49 classes, not as an edit record.

## Summary

A minimal Black Highlighter theme by tetsusquared, built for the Minecraft Division: the original delivers the BHL base as two `@import`s from nu-scptheme.github.io inside a head module (orig L4-5), frames its own CSS through three `component:interwiki-style` includes at priorities 1, 2 and 3, exhibits its CSS in a single `[[code]]` block, and self-delivers that block from a tail module (orig L138). The port keeps the topology exactly and changes only what the JP environment forces: the credit block is added, the bare Rate is deleted, the base host becomes the JP BHL host (scp-jp.github.io/Black-Highlighter), the frame includes drop their `:scp-wiki:` prefix to the same-site form, and the two logo assets move to the draft host. Measured churn (diff.md, the generator's difflib count: +39/−33 in 4 hunks, Tier 1) is the smallest in this batch. The two things a reviewer should look at hardest are not in the diff at all: the register's wave language for this theme claims a wave provenance the file history does not contain (Per-theme record, item 1), and the sources.tsv note contradicts its own cited artifact (item 4).

## Classification

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 26 change blocks — 17 specific (65.4%), 9 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Labels are sets per block; the sections below were written from classification.json's label sets, not from the skeleton's per-section lists.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 11 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 4 |
| INCLUDE-REPOINT | 4 |
| TRANSLATION-ANCHORED | 4 |
| EXHIBIT-RESTRUCTURE | 3 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| TASL-FIELDS | 1 |
| WS-ONLY | 1 |

Topology (classification.json): three components on each side, matching by kind — module-css (the head BHL imports), code-css (the single CSS exhibit, orig L61-133 / cand L69-140), module-css (the tail self-delivery). No component moved, was added, or was dropped.

## 0. Header / provenance

- What: the package diffs the mirror of `theme:diamond-highlighter` at revision 11 against the canonical candidate `pages/theme:diamond-highlighter-jp.txt`. No delivery relocation: the component census matches by kind and position.
- Why: the mirror is the reference revision the port was made from; provenance for every row lives in review/sources.tsv, and this package's original.txt hash equals that row's value.
- Verify: `sha256sum review/diamond-highlighter-jp/original.txt` against review/sources.tsv; `cmp review/diamond-highlighter-jp/candidate.txt pages/theme:diamond-highlighter-jp.txt`.
- Disposition: PASS at the ledger determination (GOSIGN2-LEDGER (b) row 81), stamp PASS.

## 1. Credit and attribution

- What: CREDIT-PREVIEW / TASL-FIELDS (B2): the candidate carries the eight-field preview credit block at cand L3-12, where the original carries none. The author field reads `**著作権者:** tetsusquared`, matching both the original's prose credit (orig L22) and its CSS comment header. 作成年 2022. The source link's text is 「ソース」, the population-standard form the credit waves settled on; the LOCALIZE-S2-A lane's shared EN8 record had read localize.md §3 as requiring the original title instead, and that reading was superseded by the waves' standardization (137 candidate files use 「ソース」).
- Why: P3 / ruling 3: the JP environment's preview credit module is the rate-bearing form, and the TASL record is what a campaign port must carry. The original's bare `[[module Rate]]` inside its `[[>]]` wrapper (orig L18-20) is deleted (BARE-RATE-DEL, B7): the preview module already bears a rate (KB-09).
- Verify: read cand L3-12 against orig L18-22; all eight fields present, author value identical in name.
- Disposition: no P3 item stands against this theme in the ledger; the only credit change after the port is the FIX-CREDIT-D translator normalization inside 1869877 (`SCP-JP` → `AI`, the FIX-CREDIT-D report's row for this theme), the population form for campaign translations under ruling 3.

## 2. Includes and components

- What: INCLUDE-REPOINT ×4. The three interwiki-style frame includes were repointed from `:scp-wiki:component:interwiki-style` to the bare same-site form and their theme= arguments from the EN delivery to the JP one: priority=1 (normalize, cand L19), priority=2 (BHL, cand L24), priority=3 (own CSS, cand L147). The fourth is the usage exhibit's component reference inside B12. No include was added or removed; the priority ladder 1/2/3 is the original's own.
- Why: ruling 1's same-site form for JP-resident components, and KB-41's draft-stage delivery for the theme= arguments. The base theme itself is NOT delivered by a `theme:black-highlighter-theme-jp` include in this file: the original imports the BHL CSS directly, and the port preserves that (section 3). The usage exhibit (cand L40-41) tells users to include `:scp-jp:theme:black-highlighter-theme` (the production page, which exists in pages-existing/) and then `theme:diamond-highlighter-jp`, which is the original's two-step usage in JP dress.
- Verify: `grep -n "interwiki-style" review/diamond-highlighter-jp/candidate.txt` — three includes, priorities 1, 2, 3, no `:scp-wiki:` prefix anywhere in the file.
- Disposition: no P6 item stands against this theme; the frame's form is the checker's accepted JP form.

## 3. Delivery and code loading

- What: DELIVERY-HOST ×5 and SELF-DELIVERY ×2. The head module's two BHL `@import`s moved from nu-scptheme.github.io to scp-jp.github.io/Black-Highlighter (cand L15-16), the JP BHL project's own host. The tail module self-delivers the exhibit: `@import` of own /1 (cand L145) with the priority=3 frame naming the same address (cand L147-150). The address is correct: the page holds exactly one `[[code]]` block (cand L69-140), so /1 names the block that holds the CSS.
- Why: the EN GitHub host serves the EN edition of the base; the JP edition of Black Highlighter is published from the JP project's host, and a port that kept the EN host would silently track EN's base instead of the JP fixed base (ruling 1's substance). The self-delivery's draft-host form is class (iii) (KB-41), sanctioned at draft stage.
- Verify: `grep -n "@import" review/diamond-highlighter-jp/candidate.txt` — the BHL pair names scp-jp.github.io; the tail import names own /1 on the draft host. Brace-depth scan of the exhibit ends at depth 0 with 11 top-level rules, the same count as the original's exhibit.
- Disposition: T1 baseline pseudo-ref×3 (T1-ROWS row 101) is this delivery's draft-form self-references, dispositioned at class (iii) in register (c1).

## 4. Fonts and assets

- What: DRAFT-HOST ×4, two of them the asset rehosts with HEADERVAR (B22, B23): the Minecraft Division logo (cand L122) and watermark (cand L137) moved from scp-wiki.wikidot.com/local--files/theme:diamond-highlighter/ to sigma10-jp-test.wdfiles.com/local--files/theme%3Adiamond-highlighter-jp/. No font imports exist on either side; the theme declares no JP font supplement, and none was added by any wave.
- Why: the draft-host asset form is the campaign's draft-stage convention (KB-41 family); posting rewrites the host (class (ii)). On fonts: the theme's stacks are the BHL base's, and the base candidate carries the JP font story; this theme's own layer names no family.
- Verify: `grep -n "wdfiles" review/diamond-highlighter-jp/candidate.txt` — the asset and self-delivery lines, all on the draft host; no third-party host remains.
- Disposition: the render row's asset 404s are DISPOSITIONED as deferred (KB-58): the files are absent on the draft host because campaign assets are not re-uploaded.

## 5. Header, sidebar, site furniture

- What: the `:root` header variables are carried with per-language title blocks. The `:root:lang(ja)` block (cand L94-97) localizes the title to Minecraft部門 but keeps `--header-subtitle: "Systematic Containment with Playability"` in English, as does the default `:root` (cand L124). One upstream defect is carried byte-faithful: the `:root:lang(cs)` block sets `--header-title` twice and never sets `--header-subtitle` (orig L78-79, cand L85-86, identical).
- Why: ruling 2 (header and title language is out of scope for migration correctness) covers the subtitle; the LOCALIZE-S2-A lane additionally noted that the JP Site-418 dossier page itself keeps the motto in English, supporting the world-building reading. The lang(cs) duplication is the original author's error, not the port's; fixing EN technical mistakes in the port and reporting them is the campaign's rule for defects, and this one is recorded here for the report-back channel rather than silently corrected or silently shipped.
- Verify: `sed -n '85,86p' review/diamond-highlighter-jp/candidate.txt` against the same lines of original.txt — identical duplication both sides.
- Disposition: P9 DISPOSITIONED under ruling 2 (ledger (c3), LOCALIZE-S2-A line for this theme). The lang(cs) item is this package's per-theme record (item 3), not a ledger item.

## 6. Text translation

- What: TRANSLATION-ANCHORED ×4 and TRANS-UNANCHORED ×11: the short documentation body is translated throughout (the intro, the usage text, the per-language exhibit notes). The unanchored mass is the expected shape for a small file whose prose lines were restructured around the repointed includes; every unit was read against the mirror for this package and has a Japanese counterpart.
- Why: P10 (KB-18): the documentation is part of the deliverable.
- Verify: read cand L28-67 against orig L21-59; no English prose line survives outside code, links and the dispositioned subtitle.
- Disposition: T5 FINDINGS at the ledger row, closed by the joint T4/T5 verdict; no translation item for this theme reached section (e).

## 7. Links

- What: one link carries the batch's noted tension. The original's local link `[[[secure-facility-dossier-site-418|Minecraft Division]]]` became cand L31 `[[[https://scp-wiki.wikidot.com/secure-facility-dossier-site-418|Minecraft部門]]]`: the label is localized, the target stays on the EN wiki.
- Why: the LOCALIZE-S2-A lane verified that the JP counterpart exists (scp-jp.wikidot.com/secure-facility-dossier-site-418, fetched 2026-11-16, Japanese body confirmed) and recommended the local link form. The ledger nevertheless dispositioned P11 for this theme as the sibling / batch-posting class, under which link targets are settled at posting time in the batch, not per file.
- Verify: `sed -n '31p' review/diamond-highlighter-jp/candidate.txt`; the lane's verification is in its part-EN8.md section for this theme.
- Disposition: P11 DISPOSITIONED (ledger (c3): sibling / batch-posting class). This package records both halves faithfully: the disposition stands, and the lane's contrary evidence is on record beside it. No defect is flagged; the posting batch owns the final form.

## 8. Structure

- What: EXHIBIT-RESTRUCTURE fired three times (B3, B5, B25), each time on an interwiki-style frame include (the priority=1, 2 and 3 instances). Adjudicated against the census: these are mere include repoints (section 2) that happen to sit where the classifier looks for exhibit structure; no exhibit was restructured, replaced or dropped. The file's one exhibit, the CSS code block, is present on both sides at the same size (72 lines each).
- Why: the standing adjudication rule for this label: a repoint inside an exhibit region is not a restructure. The census is the deciding evidence.
- Verify: topology counts in the Classification section; `grep -c "\[\[code" review/diamond-highlighter-jp/candidate.txt` is 1, as in the original.
- Disposition: nothing to disposition; the label is resolved here as a false fire.

## 9. Formatting only

- What: WS-ONLY ×1 (B21, inside the exhibit). Re-indentation: 0 blocks.
- Why / Verify / Disposition: whitespace-only change inside the carried CSS exhibit; no rule text differs at that locus. Nothing to disposition.

## 10. Porter annotations

- What: none. A hand check of the candidate finds no porter comment or annotation block; the credit block's fields are the only campaign-added prose at the head, and the CSS exhibit carries no JP-localization comment (contrast the fandom package in this batch, whose font supplement is annotated).
- Why / Verify: `grep -n "localization\|JP\b" review/diamond-highlighter-jp/candidate.txt` returns no annotation lines.
- Disposition: nothing to disposition; the section is present with its ground, per the format.

## 11. Dispositions and exceptions

- T1 pseudo-ref×3: DISPOSITIONED, class (iii) — the draft-form self-references of section 3 (register (c1) preamble; T1-ROWS row 101 baseline: exit 1, 3 errors / 1 warn / 0 infos).
- Render items (RENDER-S2-B, EN8 block): the chromium-320 header wordmark clip and webkit-320 footer license clip DISPOSITIONED under the KB-35 narrow-width family; the engine-divergent wordmark reading DISPOSITIONED as stale test-wiki page state (KB-49 caution — the deployed page, not the candidate, was behind); the sample overflow at 337-419px DISPOSITIONED under KB-33/KB-34; asset 404s DISPOSITIONED as deferred (KB-58).
- T4 P9 (subtitle): DISPOSITIONED under ruling 2 (section 5). T4 P11 (Site-418 link): DISPOSITIONED as the sibling / batch-posting class (section 7).
- The FIX3-S2EN citation inside those render items is a disposition authority, not an edit record; see the Per-theme record.

## 12. Verification

- T1 (source check): baseline 2026-11-16, T1-ROWS row 101: exit 1, 3 errors / 1 warn / 0 infos (pseudo-ref×3); standing classes dispositioned in register (c1). Re-runnable with the staff checker's check_source.py against candidate.txt.
- T2/T3 (render): RENDER-S2-B EN8 block (RENDER-ROWS-1): FINDINGS, all items dispositioned as in section 11.
- T4 follow-up (reference-revision currency): `diff-diamond-highlighter-from11.txt` records rev11 → rev11, no changes; upstream latest is still revision 11.
- Package checks: `python3 review/build_review.py --check` passes for this package; candidate.txt is byte-identical to the canonical file; original.txt's SHA-256 equals the sources.tsv row.

## Per-theme record

1. **The wave that did not edit.** Class U is defined by a named wave edit beyond the mechanical port. For this theme there is none: REPORT-GOSIGN2-FIX3-S2EN.md lists diamond-highlighter among its 29 no-edit pages ("no in-scope display defect evidenced, or only disposition classes"), the FIX-CREDIT-D report's row for the theme records only the translator normalization, and the file's complete history is two commits (184cb65, 1869877) whose combined diff beyond the port is that one field. The register's class-U signal for the row is the FIX3-S2EN citation token inside its (c2) render items (the X1-X9/KB-35 disposition authority). The citation names the adjudication document; it does not evidence an edit. A reviewer who reads the ledger's wave language at face value will believe a wave shaped this port; the bytes say the port is the EN8 lane's work alone, plus one population-wide credit normalization. Recorded as an attribution gap in the register, not as a defect in the candidate.
2. **The base is imported, not included, and that is the original's form.** The candidate carries no `theme:black-highlighter-theme-jp` include; the BHL CSS arrives by `@import` from the JP BHL host (section 3), exactly as the original imports it from the EN host. The usage exhibit's two-step include text (production base page, then this candidate) is user-facing instruction, not this file's delivery.
3. **Upstream defect carried verbatim.** The `:root:lang(cs)` block duplicates `--header-title` and omits `--header-subtitle` (orig L78-79 = cand L85-86). Byte-faithful carry; recorded for the report-back-to-author channel.
4. **The sources.tsv note does not survive its own artifact.** The row's note claims the original was superseded upstream since the reference revision; the cited follow-up artifact records rev11 → rev11 with no changes, and revision 11 remains the upstream latest. This package follows the artifact. The note is flagged here and in the batch report for the coordinator to correct in sources.tsv (the same shape as the ambrose note corrected at b3ce875 and the alcur note corrected at f1e25db); the lane does not edit sources.tsv.

## Change set outside the two diffed files

One companion candidate: `pages/theme-decoration-sample-diamond-highlighter-jp.txt`, the decoration sample that applies this theme on the check wikis. The EN-named `pages/theme:diamond-highlighter.txt` and `pages/theme-decoration-sample-diamond-highlighter.txt` are composition members of the display-check wikis, not the JP candidate.

## Multi-wave provenance

- Port: Stage 2 EN8 integration, commit 184cb65 — credit block, bare-Rate deletion, BHL host repoint, frame-include repoints, asset rehosts.
- Check waves: T1 baseline (T1-ROWS row 101); render walk RENDER-S2-B (RENDER-ROWS-1, EN8 block); localize walk LOCALIZE-S2-A (LOCALIZE-ROWS row 81) with the rev11 follow-up diff.
- Fix waves: none edited this file. FIX3-S2EN adjudicated its render items without editing (no-edit list); FIX-CREDIT-D's translator normalization is the file's only post-port change, inside commit 1869877.
- Ledger determination: GOSIGN2-LEDGER (b) row 81, PASS, no section (e) items; go-sign COMPLETION-REPORT.md §10.

## Appendix — heuristic blocks

No residue blocks (0). The 9 heuristic blocks resolve by shape: TRANS-UNANCHORED ×11 across sections 6-7 (small-file prose restructured around repointed includes; each unit verified against the mirror), and the single-line CSS-body heuristic blocks inside the exhibit (per-language `:root` blocks carried with at most the asset-host change of section 4). No new signature is proposed from this theme; the EXHIBIT-RESTRUCTURE false-fire shape on frame includes is already the standing adjudication rule.

## License and attribution

- **Title:** Diamond Highlighter Theme
- **Author:** tetsusquared
- **Source:** https://scp-wiki.wikidot.com/theme:diamond-highlighter — revision 11
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
