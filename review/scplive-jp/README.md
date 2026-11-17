# Review package — theme:scplive-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scplive-jp — origin CN, population #224 [GOSIGN2-LEDGER (b) row 224]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); both OPEN items re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 189; GOSIGN2-LEDGER (b) row 224]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 884px@768; T3 none seen, no candidate-specific visual defect; broken board.png (deferred asset); full-engine coverage. [RENDER-ROWS-G (CN13)]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN13)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 223, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 223]
- FIX5 re-judgement: items 78 (class H) FIXED, 79 (class D) FIXED — FIX5-FONTSB, commit 3911f7b: live probes CN hub HTTP 200 vs JP 404; link rewritten to the serving CN original per the FIX3-B precedent; body font replaced with loaded Noto Sans JP [GOSIGN2-LEDGER-SUPPLEMENT (a) items 78–79]
- Computed against: canonical commit 3911f7b2f69cc4e5a4d7611024cf3d96b5b73e92; candidate file pages/theme:scplive-jp.txt sha256:f99b319d3ef0a01b7450f857a8b742a88a5acf6fd98511f749600bb2e0461880; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation over the classifier skeleton; the verdict stamp above is generated)
Candidate: review/scplive-jp/candidate.txt (sha256 f99b319d3ef0a01b7450f857a8b742a88a5acf6fd98511f749600bb2e0461880)
Original: theme:scplive — scp-wiki-cn, revision 34 (sha256 b545fd981b0479057cf4da8e79952a2a4f2266607fb479cbf0a32f64f16128ec)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.

Provenance route: direct derivation at the reference revision (R1). The mirror is review-mirrors/orig-scplive-rev34.txt (FETCH-REGEN, 10,837 bytes, sha256 b545fd98…1880), byte-identical to original.txt in this package and to the sources.tsv row. Body similarity (difflib, autojunk off) between candidate and mirror is 0.804; there is no production counterpart. One provenance correction is owed, the same shape as scpdeclassified's: the sources.tsv note claims the original was superseded upstream since the reference revision, but its cited follow-up artifact (diff-scplive-from34.txt in the campaign record) records "rev34 → rev34, no changes", so the claim does not hold; the correct note in the standard form is recorded in the batch report (BATCH-RFIX11) for the coordinator's harvest correction. The stamp above is PASS: the candidate is unchanged since the verdict (its last change is the FIX5 commit itself), so this is the one package in the batch whose stamp needs no staleness reading.

## Class summary

| Label | Blocks |
|---|---|
| ASSET-REHOST | 1 |
| COMMENT-TEXT | 51 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 2 |
| DRAFT-HOST | 2 |
| GLYPH-FORM | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 8 |
| TRANSLATION-ANCHORED | 5 |

Counts: 77 blocks, 38 specific, 37 heuristic, 2 residue, 0 skipped (comment text).

## Per-theme record — the FIX5 re-derivations

This theme carries two blocking items in GOSIGN2-LEDGER section (e) (ledger (b) row 223). Item 78 [H]: a dead prose link to `scplive-foundation-idol-project` (P11). Item 79 [D]: pattern 7 in substance — the body font-family names "等线" (DengXian, a Chinese system font), loaded nowhere and not carried by JP readers' machines. GOSIGN2-LEDGER-SUPPLEMENT re-judges both FIXED (FIX5-FONTSB, canonical commit 3911f7b).

Item 78, re-derived: the original's intro names the project page inline (original line 10: `[[[scplive-foundation-idol-project|SCPLive!]]]`). The candidate rewrites it to the serving CN original with a Japanese label and the untranslated note carried inside the sentence (candidate line 22: `[*https://scp-wiki-cn.wikidot.com/scplive-foundation-idol-project 原語版のSCPLive!]` … 、原語版・未訳）. `git show 3911f7b` shows exactly this rewrite. FIXED holds.

Item 79, re-derived: the original's body rule reads `font-family: "等线", nonserif;` (original line 172), and the original's code block carries no @import at all, so the named face is loaded nowhere. The candidate's body rule reads `font-family: 'Noto Sans JP', sans-serif;` (candidate line 190), preceded by the porter's comment recording the replacement (line 189), and the code block's head now loads Noto Sans JP and Noto Serif JP from Google Fonts (candidate lines 166–167). `git show 3911f7b` shows the two-line change (the stack line plus its comment). The body font is a face loaded in the same delivered block. FIXED holds.

The ledger (c3) row charges both items to section (e); the stamp's T4 count of 1 display-affecting finding is item 79 (item 78 is the link class).

## 1. Credit and attribution

- CREDIT-PREVIEW (A): Credit block swap (P3/T1): the JP environment's preview credit module is the rate-bearing form; the branch-original credit module does not render here.
  Verify: Re-run the T1 checker (check_source.py); the credit includes must resolve on scp-jp.
  - B2: orig 4-10 -> cand 4-21 (body -> body)

This instance: the original's head bare Rate (original lines 6–8, `[[>]] [[module rate]] [[/>]]`, lowercase module form) is removed inside B2's pairing; the preview credit block at candidate line 36 is rate-bearing.

**Defect flag (credit pointer, two carriers).** The candidate's credit block (candidate lines 11–20) has no 著者 field, and its 著作権者 field (line 16) reads 「原語版ページの作成者に同じ（scp-wiki-cn の theme:scplive）」 — a pointer that names nobody. The original names the author in its intro prose (original line 10: made by [[*user Zihao Huang]]), and the candidate's own translated prose names him the same way (candidate line 22). The candidate's added license box repeats the pointer as its author parameter (candidate line 518: `|author=scp-wiki-cn theme:scplive の作者`). Same family as scpdeclassified in this batch, plugsoft, and path-of-jinin. Flagged for the coordinator with both sides' text; not edited here. The remaining fields are complete: title SCPLive テーマ, 翻訳責任者 AI, 翻訳年 2026, 原題 SCPLive版式, 作成年 2022, 初訳時参照リビジョン 34, and the source link (candidate line 20) naming scp-wiki-cn.wikidot.com, the recorded host in review/sources.tsv.

## 2. Includes and components

- COMPONENT-SWAP (B): Component swap to a JP port (T8, ruling 4): the campaign component candidate replaces the branch component it ports.
  Verify: The swapped target is in the campaign component inventory and exists on the check wiki.
  - B7: orig 21-22 -> cand 32-33 (body -> body)

This instance: the include census is credit:start-preview (candidate line 36), component:image-block (line 32), and the license-box pair (lines 517, 522). B7 is the image-block: the original names its logo on the JP storage wiki over http (original line 21: scp-jp-storage.wikidot.com/local--files/file:3741648-9-ikct/solidaro.png); the candidate carries the same file on the wdfiles host form with the caption translated (candidate line 32; sections 4 and 7). No base include exists on either side; the theme is standalone CSS over the site theme. No include is duplicated.

## 3. Delivery and code loading

- SELF-DELIVERY (A): Self-delivery (P4): the theme delivers its own code fragment; fragment numbers shift with the port's structure.
  Verify: Census the candidate's code blocks in order (every [[code]] form) and resolve each self-delivery address against the census.
  - B2: orig 4-10 -> cand 4-21 (body -> body)

- DRAFT-HOST (A): Draft-stage form (KB-41, class (iii)): the candidate's own local--code on the draft host is sanctioned at draft stage.
  Verify: Recorded as a disposition in section 11, not fixed; posting rewrites it (class (ii)).
  - B1: orig 1-3 -> cand 1-4 (module-css -> module-css)
  - B62: orig 264-264 -> cand 286-286 (code-css -> code-css)

This instance: the original delivers its code block with a relative own-code import in the head module (original lines 1–3: `@import url(/theme:scplive/code/1)`). The candidate delivers the same block from its own draft-host local--code/1 address (candidate line 2) and adds a priority=1 interwiki frame naming the same address (candidate lines 5–9) before the [[iftags +テーマ]] gate. The census is one code block per side ([[code type="css"]] at original line 150, candidate line 163), so /1 names the stylesheet itself. One exhibit deserves a note: the usage example at candidate lines 26–29 quotes the original's install snippet byte-for-byte, including `@import url(/theme:scplive/code/1);` (original lines 15–18). As an instruction it cannot work as written on the JP wiki, where neither the page name nor the relative form resolves; it stands as a verbatim quote of the original's documented method. Recorded here and flagged in the batch report as a minor instruction-exhibit instance for the coordinator's adjudication; the token-form usage sweep did not cover module-css exhibits.

## 4. Fonts and assets

- JPFONT-LOAD (A): JP font load added (P7/T5, KB-16): Japanese text needs a JP typeface loaded, and the resolved base may not load one.
  Verify: KB-16 recipe with base subtraction: the resolved base does not already load the family.
  - B60: orig 151-151 -> cand 164-172 (body -> code-css)
  - B61: orig 168-169 -> cand 189-191 (code-css -> code-css)

This instance: the font fix is the per-theme record's item 79. B60 is the code block's head: the JP loads (candidate lines 166–167) and the porter banner (lines 169–172). B61 is the body rule itself: DengXian out, loaded Noto Sans JP in, with the porter's comment. The candidate's other font-family lines name Latin faces carried from the original (Times New Roman at lines 223 and 302, Consolas at line 328). Noto Serif JP is loaded (line 167) but named by no stack in this file; it is the population-standard companion load the FIX5 wave added alongside Noto Sans JP, recorded here as loaded-but-unapplied rather than silently passed over. The header board image is re-hosted: the original names a personal wiki's attachment (original line 264: 1145141919810.wdfiles.com, 画板 1.png); the candidate carries it as board.png in its own draft-host folder (candidate line 286, the B62 DRAFT-HOST line). The ledger's render row records the board image as a deferred broken asset (KB-58); the candidate-side re-host is the draft form of that repair.

## 5. Header, sidebar, and site furniture

none — no furniture signature fired over 77 change blocks. Ground: header and sidebar styling is carried inside the single code block on both sides; the header's background image re-host is section 4.

## 6. Text translation

- TRANSLATION-ANCHORED (B): Anchored translation (T5): prose paired by structural anchors (headings, list markers) is translated.
  Verify: Spot-check the paired lines; an untranslated anchored line is a flag.
  - B5: orig 12-14 -> cand 24-25 (body -> body)
  - B6: orig 19-20 -> cand 30-31 (body -> body)

- GLYPH-FORM (B): Glyph form (T5): characters are written in their Japanese forms rather than the source branch's.
  Verify: Compare the character forms on the paired lines.
  - B6: orig 19-20 -> cand 30-31 (body -> body)
  - B7: orig 21-22 -> cand 32-33 (body -> body)

This instance: the documentation body and specimens are translated throughout, with simplified-to-Japanese glyph conversions inside the anchored pairs. The COMMENT-TEXT mass (51 blocks) is the code block's Chinese comments translated wholesale into Japanese; that is this theme's dominant change shape and is resolved here by shape, not block by block: comment text inside delivered CSS is porter-visible documentation (R1 records in-CSS text as carried text; here the port translated it, uniformly, with no rule text riding on the comment blocks — the two CSS-BODY blocks, B61 and B71, are accounted in sections 4 and 8).

## 7. Links

- ASSET-REHOST (B): Asset re-host (T9/KB-58): the asset is carried on the candidate page's own attachments rather than hotlinked.
  Verify: The re-hosted file is among the candidate page's attachments (its upload record is in the campaign record).
  - B7: orig 21-22 -> cand 32-33 (body -> body)

This instance: the section's load-bearing link is item 78, re-derived in the per-theme record (candidate line 22). The credit source link matches the recorded host (section 1). The image-block re-host (B7) moves the logo from the http wikidot.com storage form to the https wdfiles.com form of the same JP storage wiki.

## 8. Structure

This instance: the candidate wraps its code block in a "+ ソースコード" heading and a collapsible (candidate lines 161–164) that the original does not have (the original's code block follows a rule at original lines 149–150); the wrapper closes at candidate line 515. The candidate also adds the license box the original lacks (candidate lines 517–522, the classifier's LICENSE-BOX block; section 1). The footnote specimen inside the tabview (original line 64, candidate line 75, translated) has no [[footnoteblock]] on either side: the original carries the identical gap, so the specimen's footnote has no render position in the original either — inherited parity, recorded, not a defect. B71 (orig 447-452 -> cand 479-484, CSS-BODY) is a carried rule region inside the translated-comment mass; no rule text changed class there beyond the comment language.

## 9. Formatting only

none — no whitespace-only signature fired over 77 change blocks. Ground: the classifier's census for this pair is 0 WS-ONLY blocks; the code block's indentation is carried in the original's form, and the visible churn is the comment translation of section 6.

## 10. Porter annotations

- ANNOTATION (B): Porter annotation (T7): the porter's own note about this port; its universal claims must hold population-wide.
  Verify: A universal claim is checked against the population census, not this file alone.
  - B60: orig 151-151 -> cand 164-172 (body -> code-css)

This instance: the banner comment at the code block's head (candidate lines 169–172) names the theme and reference revision 34 and records that the original hotlinks a personal wiki's images, re-hosted as the candidate page's attachments. The font comment at candidate line 189 (inside B61) records the DengXian replacement. The classifier's B76 residue is the tail comment `/* page module css */` at candidate line 513 before [[/code]], the same porter marker as scpdeclassified's. All are file-local and checkable from this package.

## 11. Dispositions and exceptions

- (a) The two draft-host lines (candidate lines 2 and 286) are the T1 baseline's two pseudo-ref errors, class (iii) draft-stage form (KB-41): recorded, rewritten at posting, not a defect.
- (b) The render row (ledger (c2) row 223) is DISPOSITIONED: the runtime-hotlink site-theme chain (KB-40), the sample credit-modal preview form with overflow to 884px at 768 (KB-33/KB-34, owner ruling 5), T3 no findings, and the broken board.png deferred asset (KB-58; the candidate-side state is section 4); engine coverage is full.
- (c) The credit pointer (section 1) is NOT dispositioned; it is an open defect flag for a repair lane. The usage exhibit's original-form install snippet (section 3) is recorded for the coordinator's adjudication, not dispositioned here.

## 12. Verification

The theme's own verdict is the stamp above: overall PASS, computed against the FIX5 commit itself; the candidate has not changed since. Independent checks run for this package: both FIX5 closures are re-derived from the commit and the current bytes in the per-theme record; a fresh T1 run (check_source.py --kind theme --translation, 2026-11-17) returns error 2 / warn 0 / info 1, both errors the pseudo-ref class (iii) of section 11(a) (the baseline recorded in the stamp additionally carried 2 warns under its link-check configuration); a brace-depth scan of both code blocks ends at depth 0 with no negative excursion; `python3 review/build_review.py --check` lists this package as current after generation (the batch acceptance compares the stale set against the pre-existing refresh population).

Change set outside the two diffed files: pages/theme-decoration-sample-scplive-jp.txt (the render sample the (c2) row measured). No other change-set files: the theme is single-page with one code block.

## Appendix — residue blocks

- B58: orig 147-147 -> cand at 158 (body -> body) — one blank line dropped where the candidate inserts its "+ ソースコード" heading and collapsible before the code block; section 8.
- B76: orig at 490 -> cand 512-513 (body -> code-css) — the added blank line and `/* page module css */` tail comment before [[/code]]; section 10.
