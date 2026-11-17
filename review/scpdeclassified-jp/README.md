# Review package — theme:scpdeclassified-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scpdeclassified-jp — origin CN, population #223 [GOSIGN2-LEDGER (b) row 223]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now a614bc84d4a8b0a377e7246ab040241dec3a3f3df327bdd75ca48b9225780a5f); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 188; GOSIGN2-LEDGER (b) row 223]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 333px@320 + 851px@768 (one sample hotlink line also lists http.cat among other hosts, no hidden-* cluster); T3 .open-menu toggle overlaps body text at ≤375 on both pages, webkit-768 sample render unstyled from a transient 503 (not theme); full-engine coverage. [RENDER-ROWS-G (CN13)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN13)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 222, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 222]
- FIX5 re-judgement: items 76 (class H) FIXED, 77 (class D) FIXED — FIX5-FONTSB, commit 3911f7b: live probes CN hub HTTP 200 vs JP 404; link rewritten to the serving CN original per the FIX3-B precedent, with Japanese label and untranslated note; stacks rewired to loaded JP faces. Lane recorded a premise correction: the ledger said JP faces appear only in a non-delivering [[code]] exhibit, but the file's single code block is delivered via the /1 import at L2 [GOSIGN2-LEDGER-SUPPLEMENT (a) items 76–77]
- Computed against: canonical commit c1ba76a4aa2bdaa34cc62e1f9fa3c6b433c4df4c; candidate file pages/theme:scpdeclassified-jp.txt sha256:a614bc84d4a8b0a377e7246ab040241dec3a3f3df327bdd75ca48b9225780a5f; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation over the classifier skeleton; the verdict stamp above is generated)
Candidate: review/scpdeclassified-jp/candidate.txt (sha256 f5678fb68cddc936343144e4a02f930adf2aea80b09820fcd698fda68bbf94e3)
Original: theme:scpdeclassified — scp-wiki-cn, revision 14 (sha256 7d32e4739313f7f5f5140407e7070dd75e3c5b4283f66e808ef1a5ce3b9f146c)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

Provenance route: direct derivation at the reference revision (R1). The mirror is review-mirrors/orig-scpdeclassified-rev14.txt (FETCH-REGEN, 14,911 bytes, sha256 7d32e473…f146c), byte-identical to original.txt in this package and to the sources.tsv row. Body similarity (difflib, autojunk off) between candidate and mirror is 0.858; there is no production counterpart, so the distance is the port itself. One provenance correction is owed: the sources.tsv note claims the original was superseded upstream since the reference revision, but its cited follow-up artifact (diff-scpdeclassified-from14.txt in the campaign record) records "rev14 → rev14, no changes", so the claim does not hold. The correct note, in the standard form, is recorded in the batch report (BATCH-RFIX11) for the coordinator's harvest correction; sources.tsv itself is not edited here. The stamp above is STALE by design: the candidate changed after the verdict (the usage-example sweep line), and the per-theme record re-verifies both blocking items on current bytes.

## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| ASSET-REHOST | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 7 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 8 |
| DRAFT-HOST | 6 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| GLYPH-FORM | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 19 |
| TRANSLATION-ANCHORED | 13 |

Counts: 66 blocks, 38 specific, 27 heuristic, 1 residue, 0 skipped (comment text).

## Per-theme record — the FIX5 re-derivations

This theme carries two blocking items in GOSIGN2-LEDGER section (e) (ledger (b) row 222). Item 76 [H]: a dead prose link to the `scpdeclassified` hub (P11). Item 77 [D]: pattern 7 in substance — the stacks set JP text in Noto Sans SC / Noto Serif SC, and the JP faces the documentation claimed appeared only inside a [[code]] exhibit, with a false font claim in the documentation. GOSIGN2-LEDGER-SUPPLEMENT re-judges both FIXED (FIX5-FONTSB, canonical commit 3911f7b).

Item 76, re-derived: the original's intro names the hub inline (original line 23: `[[[scpdeclassified|解密 SCP 中心页]]]`). The candidate rewrites it to the serving CN original with a Japanese label and an untranslated note (candidate line 28: `[*https://scp-wiki-cn.wikidot.com/scpdeclassified 原語版のSCP解説ハブ]` followed by （原語版・未訳）). `git show 3911f7b` shows exactly this one-line rewrite for the link. FIXED holds.

Item 77, re-derived: all five font-family lines in the candidate now lead with the loaded JP face — body `'Noto Sans JP', 'Noto Sans SC', sans-serif` (candidate line 160), serif stacks `'Noto Serif JP', 'Noto Serif SC', sans-serif` (lines 165, 169, 507), headings `'Noto Sans JP', 'Noto Sans SC', sans-serif` (line 520). The JP loads stand at the code block's head (candidate lines 145–146, Noto Sans JP and Noto Serif JP at wght 400;700), ahead of the kept SC imports (lines 147–148), so every stack's first face is loaded in the same delivered block. The documentation claim is now true: candidate line 131 states the body, header, and heading fonts are Noto Sans JP with Noto Serif JP for the mono display, where the original claimed the SC faces (original line 126). `git show 3911f7b` shows the five stack rewires. The supplement's premise correction also verifies: the ledger said the JP faces appeared only in a non-delivering [[code]] exhibit, but the file has exactly one code block per side (original line 134, candidate line 144) and the head module delivers it via the own-code /1 import (candidate line 2), so the exhibit is the delivery. FIXED holds, on the corrected premise.

The ledger (c3) row charges both items to section (e); the stamp's T4 count of 1 display-affecting finding is item 77 (item 76 is the link class).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B4: orig 11-14 -> cand 11-20 (body -> body)

- BARE-RATE-DEL (B): Duplicate bare Rate removed (KB-09, ledger class B): the preview credit module is already rate-bearing, so a second bare Rate module double-renders the widget.
  Verify: Grep both sources for [[module Rate]]; the candidate must hold none outside labelled exhibits.
  - B3: orig 6-10 -> cand 6-10 (body -> body)

This instance: the original's head Rate block (original lines 6–9, `[[>]]` + 评分 + `[[module Rate]]`) is deleted; the two section headings it introduced stand in the candidate as plain lines (candidate lines 22 and 24) and the preview credit block at candidate line 36 is rate-bearing.

**Defect flag (credit pointer, two carriers).** The candidate's credit block (candidate lines 11–19) has no 著者 field, and its 著作権者 field (line 17) reads 「原語版ページの作成者に同じ（scp-wiki-cn の theme:scpdeclassified）」 — a pointer that names nobody. The original names the author in its intro prose (original line 21: made by [[*user Ambersight]]), and the candidate's own translated prose names him the same way (candidate line 26). The candidate's added license box repeats the pointer as its author parameter (candidate line 686: `|author=scp-wiki-cn theme:scpdeclassified の作者`). A field that names nobody where the original names a person is the pointer defect family (compare plugsoft, path-of-jinin). Flagged for the coordinator with both sides' text; not edited here. The remaining fields are complete: title 「SCP 解密 テーマ」, 翻訳責任者 AI, 翻訳年 2026, 原題 「版式：SCP 解密」, 作成年 2022, 初訳時参照リビジョン 14, and the source link (candidate line 19) naming scp-wiki-cn.wikidot.com, the recorded host in review/sources.tsv.

## 2. Includes and components

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B16: orig 40-41 -> cand 45-46 (body -> body)

This instance: the include census is credit:start-preview (candidate line 36), component:image-block (line 45), the gated base include `[[include :scp-jp:theme:black-highlighter-theme]]` (line 56), and the license-box pair (lines 685, 690). B16 is the image-block: the original's example image names a personal host over http (original line 41: ye-zhi-d.wikidot.com, a sigma9 guide page's attachment); the candidate re-hosts it as its own draft-host attachment scp.png (candidate line 45; sections 3 and 4). No include is duplicated.

## 3. Delivery and code loading

- SELF-DELIVERY (A): Self-delivery (P4): the theme delivers its own code fragment; fragment numbers shift with the port's structure.
  Verify: Census the candidate's code blocks in order (every [[code]] form) and resolve each self-delivery address against the census.
  - B1: orig 1-3 -> cand 1-4 (body -> body)
  - B2: orig 4-5 -> cand 5-10 (body -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B12: orig 38-38 -> cand 45-45 (body -> body)
  - B33: orig 216-217 -> cand 231-232 (code-css -> code-css)
  - B53: orig 563-564 -> cand 602-603 (code-css -> code-css)

This instance: both sides deliver the single code block through the head module's own local--code/1 import; the host moves from scp-wiki-cn.wdfiles.com (original line 2) to the draft host (candidate line 2). The candidate additionally names the same /1 in a priority=1 interwiki frame (candidate lines 5–9) placed before the [[iftags +テーマ]] gate; the original delivers by the module alone. The census is one code block per side ([[code type="CSS"]] at original line 134, [[code type="css"]] at candidate line 144), so /1 names the stylesheet itself — the premise the supplement's item 77 correction rests on. The remaining DRAFT-HOST lines are the candidate's own image attachments (candidate lines 45, 231, 351, 602, 651); with line 2 they are the T1 baseline's six pseudo-ref errors, class (iii).

## 4. Fonts and assets

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B46: orig 143-143 -> cand 157-159 (code-css -> code-css)

This instance: the font fix is the per-theme record's item 77: JP loads added at candidate lines 145–146 (the classifier's JPFONT-LOAD/FONT-IMPORT pairing lands on the banner block B46), the five stacks rewired JP-first (the CSS-BODY blocks B47–B64 carry them), the SC faces kept as loaded fallbacks (lines 147–148), and the documentation claim corrected to match (candidate line 131). No stack names a face that nothing loads, and no load is left unapplied: Noto Sans JP and Noto Serif JP are both loaded and both named. The image assets move from the original's hosts to the candidate's own attachments (section 3); the banner comment records the re-hosting of the sandbox images (section 10).

## 5. Header, sidebar, and site furniture

none — no furniture signature fired over 66 change blocks. Ground: the header and sidebar styling is carried inside the single code block on both sides; the only header-text change is the font stack of section 4.

## 6. Text translation

- TRANSLATION-ANCHORED (B): Anchored translation (T5): prose paired by structural anchors (headings, list markers) is translated.
  Verify: Spot-check the paired lines; an untranslated anchored line is a flag.
  - B6: orig 21-22 -> cand 26-27 (body -> body)
  - B7: orig 23-24 -> cand 28-30 (body -> body)
  - B42: orig 115-117 -> cand 120-122 (body -> body)

- GLYPH-FORM (B): Glyph form (T5): characters are written in their Japanese forms rather than the source branch's.
  Verify: Compare the character forms on the paired lines.
  - B11: orig 36-37 -> cand 41-42 (body -> body)
  - B42: orig 115-117 -> cand 120-122 (body -> body)

This instance: the documentation body and specimens are translated throughout; B11 and B42 carry the simplified-to-Japanese glyph conversions inside anchored translations (for example 示例 → 例）. The CSS comments inside the code block stand untranslated in Chinese on the candidate (for example /* 全局 */ at candidate line 154): in-CSS text (R1), the expected heuristic mass, resolved here by shape.

## 7. Links

- ASSET-REHOST (B): Asset re-host (T9/KB-58): the asset is carried on the candidate page's own attachments rather than hotlinked.
  Verify: The re-hosted file is among the candidate page's attachments (its upload record is in the campaign record).
  - B12: orig 38-38 -> cand 45-45 (body -> body)

This instance: the section's load-bearing link is item 76, re-derived in the per-theme record: the dead hub link rewritten to the serving CN original (candidate line 28). The credit source link matches the recorded host (section 1). The image-block re-host (B12) is the asset form of the same move.

## 8. Structure

- EXHIBIT-RESTRUCTURE (B): Exhibit restructured (P6): the usage exhibit's frame or layout markup changed.
  Verify: The exhibit still demonstrates the same usage.
  - B15: orig 39-39 -> cand 44-44 (body -> body)

This instance: B15 is the image-block's lead line, re-hosted, not restructured in content. The footnoteblock stands live on both sides (original line 129, candidate line 134) and the footnote specimens are live on both sides (original line 116, candidate line 121), so the footnote apparatus is intact. One furniture defect stands: **an empty collapsible**. Candidate lines 138–139 open and immediately close a collapsible ("+ ソースコード"), a reader-visible toggle that opens to nothing; a second "+ ソースコード" heading (line 141) and a second collapsible (line 143) then wrap the code block itself. The original has a single collapsible wrapping the code block (original lines 133–134). Flagged for the coordinator as minor furniture; not edited here. The candidate also adds the license box the original lacks (section 1; candidate lines 685–690, the classifier's LICENSE-BOX block), the settled KB-63 form.

## 9. Formatting only

- WS-ONLY (C): Whitespace-only (heuristic): lines differ in whitespace alone.
  Verify: Byte-compare after whitespace normalization; content must be identical.
  - B56: orig 495-495 -> cand 534-534 (code-css -> code-css)
  - B63: orig 615-615 -> cand 656-656 (code-css -> code-css)

This instance: two single lines inside the code block. Nothing else in this package is whitespace-only.

## 10. Porter annotations

- ANNOTATION (B): Porter annotation (T7): the porter's own note about this port; its universal claims must hold population-wide.
  Verify: A universal claim is checked against the population census, not this file alone.
  - B1: orig 1-3 -> cand 1-4 (body -> body)

This instance: the banner comment inside the code block (candidate lines 149–152) names the theme, the reference revision 14, and records that the sandbox's four images are re-hosted as the candidate page's attachments; the `/* 日本語フォント (JP localization) */` comment follows it. The classifier's B65 residue is the tail comment `/* page module css */` at candidate line 681, the porter's marker before [[/code]]. All three are file-local and checkable from this package.

## 11. Dispositions and exceptions

- (a) The six draft-host lines (candidate lines 2, 45, 231, 351, 602, 651) are the T1 baseline's six pseudo-ref errors, class (iii) draft-stage form (KB-41): recorded, rewritten at posting, not a defect.
- (b) The render row (ledger (c2) row 222) is DISPOSITIONED: the runtime-hotlink site-theme chain (KB-40), the sample credit-modal preview form with 337–419px-class overflow (KB-33/KB-34, owner ruling 5), the T3 open-menu overlap (KB-34), and a transient webkit-768 503 (KB-44); engine coverage is full. Nothing in the candidate's bytes is charged by them.
- (c) The credit pointer (section 1) and the empty collapsible (section 8) are NOT dispositioned; they are open defect flags for a repair lane.

## 12. Verification

The theme's own verdict is the stamp above: overall STALE by design (the candidate changed after the verdict; the frozen record remains the verdict for the bytes it judged). Independent checks run for this package: both FIX5 closures are re-derived from the commit and the current bytes in the per-theme record; a fresh T1 run (check_source.py --kind theme --translation, 2026-11-17) returns error 6 / warn 0 / info 1, every error the pseudo-ref class (iii) of section 11(a) (the baseline recorded in the stamp additionally carried 1 warn under its link-check configuration); a brace-depth scan of both code blocks ends at depth 0 with no negative excursion; `python3 review/build_review.py --check` lists this package as current after generation (the batch acceptance compares the stale set against the pre-existing refresh population).

Change set outside the two diffed files: pages/theme-decoration-sample-scpdeclassified-jp.txt (the render sample the (c2) row measured). No other change-set files: the theme is single-page with one code block.

## Post-package repairs (REFRESH3-J)

The items above describe this package as built. The repairs recorded below postdate the package build; `candidate.txt` has been recopied from the current canonical `pages/theme:scpdeclassified-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RFIX11 Item 2 — credit pointer, both carriers named (landing c1ba76a; record FIX-RFIX11.md).** As built, the credit block's 著作権者 field (candidate L17) read 「原語版ページの作成者に同じ（scp-wiki-cn の theme:scpdeclassified）」, naming nobody, and the block had no 著者 field; the license-box author parameter (candidate L686) repeated the pointer. The original names the author in prose (original L21, `[[*user Ambersight]]`) and so does the candidate's own prose (L26). The remedy named him in both carriers: credit L17 → `**著作権者:** [[*user Ambersight]]`, license-box parameter → `|author=Ambersight]]`. No pointer form remains.

**FIX-RFIX11 Item 3 — empty collapsible removed (landing c1ba76a; record FIX-RFIX11.md).** As built, candidate L138–139 opened and immediately closed an empty `+ ソースコード` collapsible, followed by a blank and a bare duplicated `+ ソースコード` heading (L141), ahead of the load-bearing `> コードを表示` collapsible wrapping the code block. The original has one collapsible wrapping the code block (original L133–134) and no empty furniture to restore into, so the remedy deleted the four lines (empty pair, blank, duplicate heading). The surviving collapsible and code block, and the live `[[footnoteblock]]` at L134, are byte-untouched. Per FIX-RFIX11.md the T1 finding set is unchanged (error 6 / warn 0 / info 1 before and after; class (i) 0 → 0); only the `!important` info's line reference moved (L177 → L173). The section-11(c) open flags are now resolved on current bytes.

## Appendix — residue blocks

- B65: orig at 661 -> cand 680-681 (code-css -> code-css) — the added `/* page module css */` tail comment before [[/code]]; section 10.
