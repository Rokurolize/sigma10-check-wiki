# Review package — theme:hansarp-jp (EN → JP port, production-derived)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:hansarp-jp — origin EN, population #15 [GOSIGN2-LEDGER (b) row 15]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 571d82e986f5e8cb74905383fc5a864879db3f72250d9e2ff1ce42eae19aa406); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 5 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 15; GOSIGN2-LEDGER (b) row 15]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 page no summary (baseline crash ×2), sample credit-modal + SP overflow 338–421px + runtime-hotlink; BHL double-include noted source-side only. [RENDER-ROWS-1 (RENDER-B row 15)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-B row 15)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 16, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 16]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 15]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:hansarp-jp.txt sha256:571d82e986f5e8cb74905383fc5a864879db3f72250d9e2ff1ce42eae19aa406; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 15) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (class (iii), section 11); the T4 item P9 (ruling 2, section 11). The T4 item P3 (missing credit fields) was **FIXED** by the credit waves and is verified against the current bytes in section 1. The render row's coverage is partial (its T2 page produced no summary; section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

This is the batch's K6 package: three sources, not two. A production SCP-JP page for this theme already exists, and the candidate descends from it. The diff in this package is original → candidate, as everywhere; the production page is brought in as the third source because without it the candidate's provenance cannot be stated honestly.

| | Original | Production page | Candidate |
|---|---|---|---|
| Page | theme:hansarp | theme:hansarp | theme:hansarp-jp |
| Wiki | scp-wiki.wikidot.com | scp-jp.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14 (the re-translation basis; the first translation was made from rev 12) | — | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s1/orig-hansarp.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages-existing/existing:theme-hansarp.txt` | Canonical file `pages/theme:hansarp-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 841 lines / 25,163 bytes | 857 lines / 26,561 bytes | 910 lines / 29,433 bytes |
| SHA-256 | d8484393306d5ae7ded365f3a0a611258213a0dc9cb011829015802bbfbaa01e | (canonical existing-page copy; not part of the diff) | a9da587bf1d1cea17deb6f1c2dbdb6f7a2140966d0c905d2454b95d678eda900 |

Provenance route, declared honestly (the Per-theme record gives the measurements): the production page is nebula2700's 2023 SCP-JP translation of the EN original at rev 12, later brought to the rev 14 basis by the recorded migration delivery `pages/phase17-diff-hansarp-jp.txt` (a Phase 17 delivery, headed as a Phase 22 差分 against the existing page, recording 原語版 rev12 → rev14). The candidate was built from that production page, not re-translated from the EN original: line-level similarity (difflib, autojunk off) is candidate~production 0.9576 against candidate~original 0.8498 (original~production 0.8728). The campaign's own changes on top of the production inheritance are the credit-field completion (section 1), the delivery repoints to the draft host (section 3), the credit-CSS supplement's completion (section 1), and trailing-whitespace normalization. The sources.tsv row records the production drift as 一致 (match) at the /start conversion, and the mirror's reference revision (14) is the re-translation basis the credit block itself records （改訳時参照リビジョン： 14).

Wave history: the candidate entered the canonical repo in the sources import (commit d727e92), was normalized for trailing whitespace (3010ef7), recorded its reference revisions in Phase 17 (8dcac74), incorporated the pending drifts in Phase 22 (d2a9dc0), received the gosign2 T1 fixes (b816e10: credit fields and furniture for rows 1–44, colon encoding, foreign-include rewrites), and the FIX-CREDIT-C translator-pair completion (5c32672).

## Summary

A BHL-based theme with an existing JP production page, and the only package in this batch whose assets are actually re-hosted rather than deferred: the logo lives on JP storage (scp-jp-storage.wdfiles.com by file ID in the CSS, the draft wiki's files in the exhibit) because the production migration already moved it. Against the EN original the diff shows the standard port (triple base delivery on the JP BHL distribution, preview credit block, own-layer delivery, specimen translation) plus the production inheritance a fresh port would not have: a ten-field credit block naming the human translator, a credit-module CSS supplement, re-hosted assets, and an English masthead the campaign has dispositioned under ruling 2. Measured churn (diff.md, the generator's difflib count with autojunk off: +184/−120, 304 changed lines in 74 change blocks / 11 diff hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 74 change blocks — 48 specific (64.9%), 25 heuristic (33.8%), 1 residue (1.4%), 0 skipped. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| ASSET-REHOST | 1 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 3 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 5 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 4 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 24 |
| TRANSLATION-ANCHORED | 19 |
| WS-ONLY | 10 |

Adjudication for this README (every specific block was read against the bytes): the four EXHIBIT-RESTRUCTURE primaries are include repoints (B3, B5, B9, B72), not restructures (section 8). The single residue block (B16) is a heading translation (section 6). Two cautions a label reader needs: the classifier's summary for this package carries no JPFONT-LOAD, INFO-PAIR, or LICENSE-BOX firing against the bytes (grep confirms none of the three forms exists in the candidate), and the T7-CREDIT-CSS blocks measure the supplement against the EN original — against the production page, part of that CSS is inheritance (section 1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:hansarp-jp; original theme:hansarp on scp-wiki at reference revision 14; candidate `pages/theme:hansarp-jp.txt`; production page theme:hansarp on SCP-JP. Provenance route: production-derived (K6), declared in the Provenance above and measured in the Per-theme record — this is the R4 case the other packages do not have, and the route is adoption-plus-completion, not fresh translation. The candidate's head has the wave's two-part gate form: an unconditional `[[iftags]]` wrapper carrying the JP BHL base include (candidate L1–3), then `[[iftags +テーマ]]` (candidate L5) over the body.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; for this theme the baseline question is the section, because half the diff is inheritance.
- **Verify:** The sources.tsv row for hansarp-jp; `sha256sum original.txt` against the Provenance table; the similarity figures reproduce with difflib over the three files named there.
- **Disposition:** Standing (the route itself); the frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare Rate (original L17–19, inside B7). The candidate carries the production form, completed: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L21–32) with ten fields — the ruling-3 eight plus the two this page's history needs: タイトル HANSARP Theme; 翻訳責任者 nebula2700; 翻訳年 2023; 作者 EstrellaYoshte; 原題 HANSARP Theme; 著作権者 EstrellaYoshte; 作成年 2022; 初訳時参照リビジョン 12; 改訳時参照リビジョン 14; 元記事リンク to scp-wiki.wikidot.com/theme:hansarp. The translator named is the human translator of the production page, kept under the attribution rule (human translator names stand where they match the live JP creator); this is the batch's only candidate whose 翻訳責任者 is not AI, and it is correct that it is not. The T4 row's P3 finding — the credit block was missing its 翻訳責任者/翻訳年/元記事リンク fields — is the state the production page's older block still shows (its form names 作者 as a user link and lacks the completed field set); the ledger records P3 as FIXED by the credit waves, and the current candidate's bytes confirm the fix: all fields are present. T7 credit-module CSS: the candidate carries 18 matching lines against the original's 12 — a real supplement (B66 re-scopes a rate-box selector under `.creditButton`; B67, B70, and B74 add the credit rules, B74 being the tail block at candidate L874–910) — of which the production page already carried 14 lines' worth; the supplement over the original is thus part inheritance, part campaign completion, and either way the JP credit module is styled, which is the T7 requirement. No license box stands in either file (grep confirms); the theme's license record rides in the credit block.
- **Why:** P3/T1 with ruling 3's field set, extended by this page's two-revision history; KB-09 for the Rate replacement. The P3 fix is the credit waves' recorded work (b816e10, 5c32672), verified here against the bytes rather than taken on the ledger's word.
- **Verify:** Read candidate L21–32 against the ten fields above; compare `pages-existing/existing:theme-hansarp.txt`'s credit block to see the pre-fix form.
- **Disposition:** FIXED (P3, credit waves; GOSIGN2-LEDGER §(c3) line for this theme).

### 2. Includes and components

- **What:** Every live foreign include is repointed: the two head frames and the tail frame to `:scp-jp:component:interwiki-style` (B3, B5, B72), the colors exhibit's `:scp-jp:component:theme-squares` (candidate L36, B9), the credit pair (section 1), and the base include `:scp-jp:theme:black-highlighter-theme` (candidate L2). The usage exhibit's escaped BHL include follows (candidate L71–72, B15). No live include in the candidate names a `:scp-wiki:` target. One hygiene note belongs to this theme's sample, not to the candidate: the render record notes a source-side BHL double-include on the sample page (the KB-65 family); it is a sample-page source note with no display defect recorded, and the candidate file itself carries the base include exactly once.
- **Why:** P1 (KB-15) for the component repoints; T9 for the base include — a dependent theme imports the base's JP port candidate, never the raw upstream delivery.
- **Verify:** `grep -n '\[\[include' candidate.txt` against the list above.
- **Disposition:** Applied; the sample hygiene note stands as recorded (section 11).

### 3. Delivery and code loading

- **What:** Base (T9), the triple form: the original imports BHL from the upstream distribution host nu-scptheme.github.io; the candidate repoints the module imports and both frame parameters to the JP distribution scp-jp.github.io/Black-Highlighter (candidate L7–8, B2; parameters at candidate L13 and L18, B4/B6), adds the JP BHL candidate include (candidate L2), and keeps the frames at priority=1 (normalize) and priority=2 (BHL). The production page already delivered the base from scp-jp.github.io — this layer is inheritance confirmed, not new work. Own layer (T3): the original's tail import and priority=3 frame name its code on EN storage (original L836–840); the production page names its own code on the live JP wiki (scp-jp.wdfiles.com/local--code/theme%3Ahansarp/1); the candidate names its own code on the draft host (candidate L868–872, B71/B73) — the campaign's draft-wiki form of the production delivery. The delivered body is the candidate's own `[[code]]` block (the /1 index).
- **Why:** P4/T9 and P6/T3; the draft-host form of the own-layer lines is KB-41, class (iii). The three-way comparison is what makes this section K6: each delivery line's form is explained by which source it came from.
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` against the list above, and the same grep on the production file for the inheritance claim.
- **Disposition:** DISPOSITIONED (draft-host own-layer lines, class (iii)); the base repoint and frame stack stand.

### 4. Fonts and assets

- **What:** Fonts: no JP supplement was added for this theme — there is no Noto Sans JP load or stack entry in the candidate (grep returns nothing), and the production page has none either; the font state is the production inheritance, and the T4 row for this theme carries no P7 item. The one font-load change is the mono face's host: Azeret Mono was loaded from the third-party mirror fonts.bunny.net (original L158–161); the candidate loads it from fonts.googleapis.com (candidate L171–174, B53). The header face (Permanent Marker, per the font specimen at candidate L161–164) keeps its load unchanged. Assets — the K6 difference: this theme's artwork is re-hosted, not deferred. The logo's CSS background names JP storage by file ID (`https://scp-jp-storage.wdfiles.com/local--files/file%3A8260379-…`, candidate L312, B56, ASSET-REHOST) where the original named EN storage; the logo exhibit's image names the draft wiki's files (candidate L58, B10). Both forms are the production migration's doing: the production page's assets live on JP storage, and the candidate inherits them. No EN-storage asset reference survives in the candidate.
- **Why:** P5's usual JP outcome is the KB-58 deferral; here the production page had already settled hosting, so the candidate's P5 state is resolved rather than dispositioned — the contrast is recorded so a reviewer comparing themes does not read this theme's clean asset state as an inconsistency. The load repoint is KB-17's shape.
- **Verify:** `grep -cn 'scp-wiki.wdfiles.com' candidate.txt` — 0. `grep -n 'scp-jp-storage\|sigma10-jp-test.wdfiles' candidate.txt` — the two re-hosted forms above.
- **Disposition:** Standing (assets resolved by the production migration; no KB-58 item for this theme).

### 5. Header, sidebar, and site furniture

- **What:** The masthead variables stand in both files with identical values: `--header-title: "WHAT IS HANSARP?"` (candidate L234; original L221) and `--header-subtitle`-side `--header-title-mobile: "HANSARP?"` (candidate L235; original L222), with `--theme-name: "HANSARP Theme"` at candidate L183. The T4 row records the English masthead ("WHAT IS HANSARP?" / "HANSARP?") as a display-affecting P9 item needing a staff/author decision; the ledger dispositions it under ruling 2 — header title language is case-by-case translation taste, out of scope for Sigma-10 migration correctness — so the strings stand in English by decision, not by oversight. The candidate's tail carries one JP-side furniture addition the original does not have: a small closing module (candidate L905–910) whose comment reads "SCP-JP Wikidot Hansarp navigation labels: keep top-bar labels unbroken on narrow viewports", adding `word-break: keep-all` for top-bar labels — part of the production side of the record, carried over with the inheritance.
- **Why:** P9/T6 is the variable class; ruling 2 is the disposition that governs its language. Recording the decision here is what separates a kept string from an untranslated one (KB-18 does not charge text a ruling has placed out of scope).
- **Verify:** `grep -n -- '--header-title' candidate.txt` — candidate L234–235 as above, byte-identical to the original's L221–222.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3) P9 line for this theme).

### 6. Text translation

- **What:** The specimen body is translated in full: the description prose (candidate L34–60, including the Woedenaz challenge anecdote in the translator's voice — the production translation's first-person register is kept, as inheritance), the usage prose (L64), the heading specimens (2番目の見出し through 6番目， L86–94), the tab specimens (L100–144, including this theme's distinctive タブを作る/タブが作られた pair), the table specimen (L156–158), and the font specimen lines (L161–164). The 24 TRANS-UNANCHORED and 19 TRANSLATION-ANCHORED blocks are this mass, resolved by shape in the appendix; the residue block B16 is the `+ Examples` → `+ 例` heading (candidate L75). English survives as live text in the section 5 masthead (dispositioned) and in proper names.
- **Why:** P10 and KB-18: reader-visible strings are translated. For a production-derived candidate, the translation quality being judged is the production translation's, which the campaign adopted rather than redid (section 0).
- **Verify:** diff.md's body sections in order; `grep -n 'Second Title\|Tabulator' candidate.txt` returns nothing.
- **Disposition:** Standing (the port itself, by adoption).

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L31), naming scp-wiki.wikidot.com/theme:hansarp, the original's recorded host in sources.tsv — the serving form, not a defect. The asset references are re-hosted JP forms, not prose links (section 4). No prose link in the candidate targets a page that does not serve, and T1 records no dead-reference error for this theme (its two errors are both pseudo-ref, section 11).
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve or a JP counterpart exists; neither holds here.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only prose hit.
- **Disposition:** Standing.

### 8. Structure

- **What:** No structural change. The classifier's four EXHIBIT-RESTRUCTURE primaries are include repoints in exhibit-adjacent lines (B3, B5, B9, B72); the exhibit census (theme squares, headings, tabs, table, font specimen, source code) stands in the original's order on both sides. The candidate's growth over the original (+69 lines) is accounted for without any exhibit change: the ten-field credit block, the credit-CSS supplement (section 1), the tail navigation module (section 5), and the frame/gate head form. The R3 question (a silent structural deletion) does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a repoint share a diff shape; here the census, not the label, decides.
- **Verify:** Compare the exhibit sequence via `grep -n 'theme-squares\|見出し\|タブ' original.txt candidate.txt` and the four blocks in diff.md.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** 10 WS-ONLY blocks, each the deletion of a whitespace-only line — for this candidate the class has a named origin: commit 3010ef7 is the trailing-whitespace normalization pass in its history. No re-indentation and no line-ending conversion beyond it, so the R7 follow-up-diff hazard is not triggered beyond this disclosure.
- **Why:** Formatting churn is disclosed as its own class (R7) so it is never mistaken for a semantic change.
- **Verify:** The WS-ONLY blocks are diff.md's whitespace-only entries; their count is classification.json's label count for WS-ONLY (10).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation-class item, inherited: the tail navigation module's English comment ("SCP-JP Wikidot Hansarp navigation labels: keep top-bar labels unbroken on narrow viewports", candidate L906) explains a JP-side rule in the file itself (section 5). There is no `Ported for SCP-JP` banner and no `[JP]` markers; the port's provenance record is the ten-field credit block and this package.
- **Why:** R2: annotations are recorded where they exist, and their absence is recorded where they do not; this theme has exactly one, and it documents a behaviour a reviewer would otherwise have to guess at.
- **Verify:** `grep -n 'SCP-JP Wikidot Hansarp' candidate.txt` — candidate L906.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items. (1) T1's two pseudo-ref errors: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3); this theme has no hotlink errors, because its assets are re-hosted (section 4). (2) T4's P9 item (the English masthead): DISPOSITIONED under ruling 2, per the ledger's §(c3) line. (3) T4's P3 item (the missing credit fields): FIXED by the credit waves, not dispositioned — the distinction matters and section 1 verifies the fix against the bytes. The render row's source-side BHL double-include note on the sample page (KB-65 family, section 2) stands as a hygiene note with no display defect recorded against it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); ruling 2), and a fix is a different thing from a disposition; the package keeps the two apart.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–2); FIXED (item 3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 15): exit 1, 2 errors / 2 warns / 5 infos (pseudo-ref×2); no class (i) error, and no hotlink errors (section 4). (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-B): FINDINGS at the row level, with a coverage caveat recorded in the ledger's §(c2) block for this theme: the sample's T2 page produced no summary (baseline crash ×2), so the render verdict for the sample rests on the remaining engines and the source-side note of section 2; the ledger dispositions the row on that basis, and this package records the caveat rather than papering over it. (c) T4/T5 (LOCALIZE-ROWS row 16): FINDINGS jointly, display-affecting count 0 in the row's count column, with the P9 masthead and the P3 fields named in its text; the ledger's §(c3) line records P3 FIXED and P9 DISPOSITIONED for this theme. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +184/−120 in 74 change blocks / 11 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance; a check that produced no summary is reported as such.
- **Verify:** Re-run the checker on `pages/theme:hansarp-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 15; go-sign, COMPLETION-REPORT §10), with the render coverage caveat recorded above.

## Per-theme record

### The three-source comparison (K6)

This package is the batch's worked example of why the provenance route must be declared before the diff is read. Read as a fresh port, the candidate looks anomalous in four places: its translator field names a human, its credit block has ten fields, its assets are already on JP storage, and it carries credit CSS and a navigation module the original lacks. Every one of those anomalies is the production page showing through. The deciding measurements: candidate~production line similarity 0.9576, candidate~original 0.8498, original~production 0.8728 (difflib, autojunk off, over the three files in the Provenance table). The campaign's own layer on top of the inheritance is thin and identifiable: the credit-field completion (the production block's older form is still visible in `pages-existing/existing:theme-hansarp.txt`), the own-layer delivery's move from the live JP host to the draft host, and whitespace normalization. The migration delivery that connects the production page to the rev 14 basis is itself a canonical file, `pages/phase17-diff-hansarp-jp.txt`, and the sources.tsv row's drift verdict （一致） records that production and candidate had not diverged at the /start conversion. A reviewer who wants to audit the campaign's contribution should diff candidate against production; a reviewer who wants to audit the port should read the diff in this package. Both audits are possible from the canonical repo alone, which is the point of recording all three sources.

## Appendix — heuristic and residue mass, resolved by shape

Class M treatment: the 25 heuristic blocks are not listed one by one; they fall into the shapes below, each verified against the bytes at the cited ranges. The 1 residue block is listed in full. The 10 WS-ONLY blocks are treated in section 9.

| Shape | Blocks | Where | Resolution |
|---|---|---|---|
| Specimen sentence translation (unanchored) | The TRANS-UNANCHORED body mass (24 label occurrences across heuristic and mixed blocks) | candidate L34–180 | P10 translation, production inheritance (section 6) |
| CSS body and comment mass | CSS-BODY ×3 and the CSS portions of mixed blocks | the delivered CSS body | Stack and rule carry-over; no behaviour change beyond sections 1, 4, 5 |
| Residue: heading translation | B16 | candidate L75 (`+ 例`) | P10 translation of the `+ Examples` heading |

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-SNIPPET — production-predecessor reference audit (landing 358955e).** `FIX-SNIPPET.md` records the self-reference at candidate L72 as DRIFT ground D1 (own code addresses under `theme%3Ahansarp-jp`). Commit 358955e inserted `-jp` after the target, `theme:hansarp` → `theme:hansarp-jp`. The BHL exhibit at L71 is COHERENT ground C1 and was not touched. T1 before/after unchanged (2/0/5).

## Change set outside the two diffed files

The diff covers two files; this theme's record is larger than any other in the batch. `pages-existing/existing:theme-hansarp.txt` is the production page, the candidate's parent (Per-theme record). `pages/phase17-diff-hansarp-jp.txt` is the migration delivery that brought the production page to the rev 14 basis. `pages/theme-decoration-sample-hansarp-jp.txt` is the decoration sample the render checks ran against, and `pages/theme-decoration-sample-hansarp.txt` is its production-side counterpart. The base include `:scp-jp:theme:black-highlighter-theme` is another candidate in the population with its own package; this theme's record names it as a dependency, not a change.
