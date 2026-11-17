# Review package — theme:dear-dictator-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:dear-dictator-jp — origin KO, population #9 [GOSIGN2-LEDGER (b) row 9]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now cca02a94b20026ab00a60d07edb316c84cdbccdd480e65772cd1186ff1b96512); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 9; GOSIGN2-LEDGER (b) row 9]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — webkit-768 header background image HTTP 503, large source-code content-overflow warn (transcribed only), sample credit-modal. [RENDER-ROWS-1 (RENDER-A row 9)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 9)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 10, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 10]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 9]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:dear-dictator-jp.txt sha256:cca02a94b20026ab00a60d07edb316c84cdbccdd480e65772cd1186ff1b96512; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 9) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×6 (class (iii)); P5 asset hosting and P10 specimen text (register c3). **One defect flag from this package:** the usage snippet names a page that is not this candidate (candidate L76; per-theme record below) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:dear-dictator | theme:dear-dictator-jp |
| Wiki | scpko.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 65 (first translation; the candidate's credit block records 初訳時参照リビジョン: 65) | — |
| Source of this copy | Fresh fetch for this review (mirror class FETCH-REGEN, fetched 2026-11-17; hash-verified against review/sources.tsv) | Canonical file `pages/theme:dear-dictator-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 886 lines / 24,851 bytes | 919 lines / 27,048 bytes |
| SHA-256 | c483fe043bdda463c1e6e379fdb5788f0ce6d5652212930fd05c9b3e82ad707c | 407081036abe8f189d580c7017c040dd26d9d45b13a14f878cfe7177bf1ed41a |

Wave history: the candidate descends from the Stage 2 KO3 wave; its commit record runs d727e92 (canonical sources), 8dcac74 (Phase 17), b816e10 (the T1-fix wave: credit fields and head furniture for rows 1–44, colon encoding, foreign-include rewrites), 5c32672 (FIX-CREDIT-C), and 1869877 (FIX-CREDIT-D), the last being the stamp's computed-against commit. The original has been superseded upstream since revision 65; the follow-up diff artifact `diff-dear-dictator-from65.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A KO parody theme （敬愛する独裁者， by thd-glasses) that styles pages as North-Korean state design, with a large specimen body (color and font sets, tabbed document files, command specimens) and a 609-line CSS exhibit delivered from the theme's own code page. The port keeps the code-page delivery shape but repoints it to the candidate's own JP code page, moves the delivery module and the tower/light graphic divs from the original's tail to the head, replaces the KO info block with a JP credit block that carries three attribution notes the T4 examination had found missing, translates the whole specimen body (its propaganda voice rendered in a marked Japanese style), deletes the Korean webfont loads and rewrites their stacks to Japanese system fonts, repoints the artwork to the JP test bucket, deletes the KO branch's navigation-position rules under a porter comment explaining why, restates the license area as visible, and appends a porter supplement inside the exhibit: sample-support rules plus the JP credit-module corrections, with a long comment stating their grounds. Measured churn (diff.md, the generator's count: +228/−195 in 66 change blocks). One defect flag arises, on the usage snippet's page name (per-theme record).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 66 change blocks — 27 specific (40.9%), 30 heuristic (45.5%), 9 residue (13.6%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 25 |
| TRANSLATION-ANCHORED | 16 |
| CSS-BODY | 8 |
| DRAFT-HOST | 8 |
| CONTENT-STRING | 4 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| INFO-DEL | 2 |
| INCLUDE-REPOINT | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 41 translation labels are the specimen body, counted in section 6; the 8 CSS-BODY blocks resolve as 6 font-stack rewrites (section 4), 1 license-area restatement (section 1), and 1 deleted CSS region (appendix, B63); the 8 DRAFT-HOST labels are the delivery and asset repoints to the JP test bucket (sections 3–4); the 9 residue blocks are adjudicated one by one in the appendix (five are color-name table cells the classifier could not anchor; three carry porter comments; one is a pairing line at the exhibit close). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:dear-dictator-jp; original theme:dear-dictator on scpko at reference revision 65; candidate `pages/theme:dear-dictator-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 KO3 wave (sources.tsv kind: standard; no production JP counterpart exists). The original gates its body under `[[iftags +테마]]` (original L1) and puts its delivery module after the gate's close (original L867–870); the candidate inverts the order — delivery module first (candidate L1–3), graphic divs, frame, then the gate (candidate L28).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate tag is P2 and the delivery shape is section 3.
- **Verify:** The sources.tsv row for dear-dictator-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate change is recorded in section 2.

### 1. Credit and attribution

- **What:** The original's furniture (blocks B2–B3) is a bare `[[module Rate]]` and a `:scpko:info:start`/`end` block carrying the author ([[*user thd-glasses]]), three noonnu font-source links and a pixabay illustration link, the note that all images were made and edited by the author, and a hub link box. The candidate deletes both and installs the JP form (candidate L29–42): a `:scp-jp:credit:start-preview`/`end-preview` block with the eight ruling-3 fields (title Dear Dictator Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 경애하는 독재자 꾸밈양식; 著作権者 thd-glasses; 作成年 2024; 初訳時参照リビジョン 65; the source link, section 7) plus three attribution notes the original's info block carried in prose and the T4 record found dropped at its measurement: 翻訳について (the JP text is this port's new translation, not a modification of an existing one), 画像の出典 (all images by thd-glasses, per the original-language credit), and フォントの出典 (the original's noonnu-distributed faces and the pixabay illustration; the JP version substitutes Japanese system fonts because those distribution sources fall outside the direct-link exception). The section's CSS half is the exhibit-tail supplement (block B64, T7-CREDIT-CSS; section 8) and one restatement: the original hid the license area (`#license-area { display: none; }`, original L308); the candidate restates the rule as a visible, styled block (candidate L309–315, `display: block` with padding, text color, and paper background, plus a link rule) — the JP form shows the license area the KO form suppressed.
- **Why:** P3/T1 (KB-09) for the furniture swap (the preview credit block is rate-bearing, so the bare rate module is deleted, BARE-RATE-DEL). T7 by its KB-11 amendment form for the supplement: appended rules at the delivery tail, with a porter comment stating the two grounds (the credit anchor the JP module emits, and the rate-box background losing to credit:style's `transparent !important`). The attribution notes are ruling-3 TASL substance, restored after the T4 finding (LOCALIZE-ROWS row 10, item (i)) recorded their loss.
- **Verify:** Read candidate L29–42 against the eight fields and the three notes; `grep -n 'license-area' candidate.txt` — the restated rule; the supplement and its comment are at candidate L814–915.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Two include repoints and one flag. (1) The specimen's image-block include repoints from `:scpko:component:image-block` to `:scp-jp:component:image-block` (block B25). (2) The frame include (section 3). (3) The usage snippet (block B11, candidate L76): the original's `@@[[include :scpko:theme:dear-dictator]]@@` becomes `@@[[include :scp-jp:theme:dear-dictator]]@@` — the wiki prefix is repointed but the page name keeps the original's form, without the `-jp` suffix that this candidate's own name, its file name, its frame `theme=` URL, and its code-page URL all carry, and that the batch's EN and CN candidates use in theirs; this batch's other KO candidate (doap-bhl-jp) shows the same shape, which the per-theme record discusses. This was flagged, not edited, at build time (per-theme record below); the population sweep has since landed the repair, and the snippet now names `:scp-jp:theme:dear-dictator-jp`. Every other named include in the candidate is `:scp-jp:`.
- **Why:** P1 (KB-15): includes name the JP component or theme page that actually exists. The image-block repoint follows it; the usage snippet, on the bytes, does not name this candidate.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the image-block specimen, and candidate L76.
- **Disposition:** Repoints applied; the usage snippet is the package's defect flag (per-theme record).

### 3. Delivery and code loading

- **What:** The theme self-delivers from its own code page in both versions. In the original, a tail `[[module CSS]]` (original L867–870, after the gate close) imports `https://scpko.wdfiles.com/local--code/theme:dear-dictator/1`, and the gated body holds the same CSS as a `[[code type="CSS"]]` exhibit (original L253–862, 609 lines). The candidate moves the delivery module to the head (candidate L1–3) and repoints the import to its own JP code page, `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Adear-dictator-jp/1`; the exhibit grows to 642 lines (candidate L274–916) with the port's changes inside it (sections 4–6, 8, 10). The small `#extra-div-4` module (original L23–30) is carried unchanged at candidate L43–50. **Frame paragraph (the M-frame addition):** the original carried no interwiki-style frame (LOCALIZE-ROWS row 10, item (iii)); the candidate adds one at candidate L23–27 with `priority=1` and `theme=` naming its own code page on the draft host — the single-layer own-code form — written with the compact `|priority=1` parameter style. The ledger records the outcome as P6 FIXED (frame waves; checker-verified); the head furniture, frame included, was rebuilt in the T1-fix wave (commit b816e10).
- **Why:** P4/T2: the code-page delivery is the original's own shape, kept; only its host and page move to the JP candidate's own delivery (KB-41 for the draft-host form, class (iii), rewritten to the production host at posting). P6/T3 (KB-07) for the added frame.
- **Verify:** Read candidate L1–3 and L23–27; `grep -n 'scpko.wdfiles' candidate.txt` returns nothing.
- **Disposition:** FIXED (P6); the draft-host URLs are DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts, by substitution rather than conversion. The original loads Korean webfonts through `@font-face` declarations at the exhibit's head (original L255–275: the noonnu-distributed faces) and names them in its stacks ('JeonjuCraftGoR', 'GapyeongHanseokbong-Bold', 'ONE-Mobile-Title' — two of the original stacks even carry the malformed generic `san-serif`). The candidate deletes the `@font-face` block (block B45, whose added line is the exhibit's porter comment, section 10) and rewrites all six stacks (CSS-BODY blocks B47, B49, B53, B56, B57, B60) to Japanese system fonts: the JeonjuCraftGoR and ONE-Mobile-Title stacks become `"Yu Gothic", "Hiragino Kaku Gothic ProN", …` and the GapyeongHanseokbong stacks become `"Yu Mincho", "Hiragino Mincho ProN", …`, generics well-formed. No webfont is loaded anywhere in the candidate; the credit block's フォントの出典 note (section 1) states the ground. Assets: the emblem image in the body (block B8) and three CSS background URLs (blocks B52, B58, B59) repoint from scpko.wdfiles.com to the JP test bucket (sigma10-jp-test.wdfiles.com, the theme's own JP file area), and the supplement's `.dd-emblem` rule (section 8) draws the emblem from the same bucket; the original tail's inline tower image (original L880, inside the toweroff div) does not ride into the candidate's divs — the graphic layers are delivered by CSS instead, as the supplement's head comment states.
- **Why:** P7/T5 with KB-16, in its substitution form: the Korean faces cannot render Japanese and their distribution sources fall outside the direct-link exception the campaign applies, so the stacks land on system fonts that every JP reader's device carries; the specimen text that demonstrates the faces (section 6) is translated with the stacks it names. P5/KB-58 for the asset hosting state.
- **Verify:** `grep -n '@font-face\|noonnu\|Jeonju\|Gapyeong\|ONE-Mobile' candidate.txt` returns nothing outside the credit note's prose; `grep -n 'Yu Gothic\|Yu Mincho' candidate.txt` counts the six stacks.
- **Disposition:** Substitution applied; the asset URLs are DISPOSITIONED (class (ii) / KB-58; GOSIGN2-LEDGER §(c3) P5).

### 5. Header, sidebar, and site furniture

- **What:** Three furniture adaptations, two of them porter-commented in the CSS itself. (1) The KO branch's top-bar navigation-position rules (original L703–750: a run of `nth-child` rules keyed to the Korean branch's menu layout, including a `content: "SCP 인터나쇼날"` label rule) are deleted (block B61); in their place stands the porter's comment: "The Korean branch navigation positions are not stable SCP-JP selectors." (2) The sidebar blocks' background changes from `none` to `var(--red)` (block B62, candidate L729–733), under a porter comment about keeping the theme's pale labels readable against SCP-JP's light article canvas while preserving the red navigation-panel identity. (3) The mobile-nav div (`dd-mobile-nav`, candidate L5–7, with メニュー / 閉じる anchor links) stands at the head with the graphic divs; the tower/light div set itself (candidate L9–21) is the original's tail furniture (original L874–886) moved before the frame and ungated. The render row's webkit-768 header-background 503 is an original-state asset availability line, dispositioned in section 11.
- **Why:** P9/T6 and P8: furniture rules keyed to another branch's menu structure cannot transfer, and the deletion is annotated at the point of removal rather than silent; the sidebar recolor is a readability adaptation of the same kind, likewise annotated. R2 covers the annotations (section 10).
- **Verify:** Read candidate L710 (the comment where the nav rules stood) and L729–733; compare original L703–750 and L769–773.
- **Disposition:** Standing as annotated adaptations; no unannotated furniture loss.

### 6. Text translation

- **What:** The specimen body is translated in full, in the classifier's counts: 25 TRANS-UNANCHORED and 16 TRANSLATION-ANCHORED labels over blocks B4–B44 and B46. In groups: the warning blockquotes at the head (B4–B7 — the Korean cautions and the English parody note all become Japanese); the title and intro prose (B9–B10, keeping 이상교화국 glossed as 異常教化国（이상교화국）); the color set (B12–B18 — the named colors 主体， 太陽， 白頭， 先軍， 国防， ビニロン rendered in Japanese, five of them in table cells the classifier left unanchored, appendix); the font set specimens (B19–B20); the tool sets with their tabbed document files (B21–B44 — tab titles, specimen documents, collapsible labels, and the command specimens); and the slogan variables, translated both in the `@@--@@` specimen (B38) and in the CSS `:root` (B46: `--slogan1: "異常教化戦線を徹底構築し"`). Four `content:` banners are rewritten (blocks B50, B51, B54, B55): two are translations of the original warnings, and two are adaptations — the age-and-rating banner (original L394) becomes a creative-parody notice (⚠️ 創作上の政治風刺・CC BY-SA 3.0, candidate L401), and the long restriction text (original L401) is replaced by a JP disclaimer stating the theme depicts a fictional dictatorship and supports no real regime (candidate L408). The specimens' DPRK-style voice is carried into a marked Japanese style rather than flattened. The ledger dispositions the body-text class as P10 DISPOSITIONED (lane-recorded severity / specimen class).
- **Why:** P10 (body and specimen translation), KB-18 (reader-visible strings including `content:`). The banner adaptations belong to the same class: a literal transfer of the KO rating claim would assert a rating the JP text does not carry, so the port restates the caution in JP terms.
- **Verify:** Read candidate L53–271 against original L33–252 (the gated body before the exhibit); `grep -n 'content:' candidate.txt` for the four banners.
- **Disposition:** Standing (the port itself); the P10 class is DISPOSITIONED (§(c3)).

### 7. Links

- **What:** The candidate's live outbound link is the credit source link (candidate L39), naming `https://scpko.wikidot.com/theme:dear-dictator` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. The original info block's font-source links do not survive as links: their substance is carried as text in the credit block's フォントの出典 note (noonnu.cc/font_page/678, /1235, /1279 and the pixabay source, section 1), which is where a reader needs them, since the JP version loads none of those faces. The author's hub link ([[[thd-glasses-hub]]]) stood inside the deleted info block and has no candidate counterpart; authorship itself is carried by the 著作権者 field.
- **Why:** P11: links take the JP counterpart or the serving original under the dead-reference evidence standard; attribution sources that no longer deliver anything are recorded as text, not kept as live links.
- **Verify:** Compare candidate L39's host against the sources.tsv row's original_url host (scpko.wikidot.com) — identical; read the フォントの出典 note at candidate L41.
- **Disposition:** Standing.

### 8. Structure

- **What:** The port rearranges the file's furniture without losing its body. Head/tail inversion: the delivery module and the tower/light divs move from the original's tail (original L867–886, block B66) to the candidate's head (candidate L1–21), and the frame and credit block are new head furniture. Exhibit preservation: an exhibit census shows the gated body entire — warnings, title, prose, usage, color set, font set, tool sets with both document-file tabviews, collapsibles, and the code exhibit in the original's order; the one EXHIBIT-RESTRUCTURE primary (B25) is the image-block include repoint inside a specimen, not a restructuring. Exhibit growth: the code exhibit gains the porter's supplement at its tail (block B64, candidate L814–915, +102 lines inside the exhibit): sample-support rules (.dd-introduction, .dd-emblem, .dd-palette and companions, drawing on the JP test bucket) and the T7 credit corrections of section 1, the whole under porter comments. Deletions: the nav-position rules (B61, section 5), one CSS region of ten lines (B63, original L784–793, inside the exhibit's top-bar run), and the info block (section 1).
- **Why:** R3's census is the deciding check for exhibit questions; here it separates furniture rearrangement from content loss. The supplement is R6's appended form (KB-11 amendment), placed inside the exhibit because the exhibit mirrors the code page that actually delivers the CSS.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[collapsible\|\[\[code\|\[\[div' original.txt candidate.txt` — the sequences correspond, with the supplement the only addition.
- **Disposition:** Standing; no unrecorded structural deletion.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 66 blocks. The frame's compact `|priority=1` parameter spacing (candidate L24) differs from the spaced form other candidates use; it is a one-line style variant inside the frame addition, recorded in section 3 rather than counted here.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Present, and all inside the CSS or the credit block — the candidate has no `[!-- --]` notes, so the annotations ride inside other blocks, as the standing lesson warns. The full census: (1) the exhibit's head comment (block B45, candidate L276): "Korean SCP branch Dear Dictator theme, ported for SCP-JP; source and asset hashes are in PORT.md." (2) The navigation-deletion comment (block B61, candidate L710), quoted in section 5. (3) The sidebar-readability comment (block B62, candidate L730–731), quoted in section 5. (4) The supplement's head comment (candidate L814): "SCP-JP port: preserve the original graphic layers and allow Japanese article samples to use them without external assets." (5) The supplement's credit comment (candidate L900–910), a ten-line explanation of the two credit corrections and their grounds, ending "Everything else in the port is left untouched." (6) The credit block's three attribution notes (candidate L40–42, section 1), which are TASL substance in annotation form. No other porter text exists; the specimen translations are the port's body, not annotations.
- **Why:** R2: porter-added text is part of the change record and is enumerated wherever it rides. The credit comment (5) is also the T7 supplement's required statement of grounds (KB-11 amendment).
- **Verify:** `grep -n '/\*' candidate.txt` — 12 CSS comment lines; each is either the original's own (carried specimens' comments) or one of the six items above; `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (checked, enumerated).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's six pseudo-ref errors: DISPOSITIONED in register c1 (pseudo-ref, class (iii)) — references whose targets resolve when the candidate and its JP siblings are posted. (2) The render row's items (RENDER-ROWS-1, RENDER-A row 9): the webkit-768 header background image HTTP 503 (an original-state asset's availability, not a candidate reference error), the large source-code content-overflow warning (transcribed only in that record), and the sample credit-modal errors (the preview form's property, KB-32, ruling 5) — all DISPOSITIONED (the KB-37 family). (3) P5 asset hosting: DISPOSITIONED (class (ii) / KB-58). (4) P10 body text: DISPOSITIONED (lane-recorded severity / specimen class). The usage-snippet flag (per-theme record) is not in this list: no ledger line dispositions it, which is why it is flagged rather than dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–4 as stated).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 9): exit 1, 6 errors / 1 warn / 1 info; all six errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, RENDER-A row 9): FINDINGS, every item dispositioned (section 11 item 2); no layout-blocking defect recorded against the candidate. (c) T4/T5 (LOCALIZE-ROWS row 10): FINDINGS jointly, display-affecting findings 1; the row's items are (i) the credit block as a two-field skeleton with the original's font/image attribution dropped (since restored, section 1), (ii) the artwork on the JP test bucket with attribution lost (the bucket stands, dispositioned; the attribution is restored), (iii) the absent interwiki-style (since FIXED, section 3), and (iv) the P10 body-text class (dispositioned). The ledger §(c3) line records the outcomes: P3 FIXED, P5 DISPOSITIONED, P6 FIXED, P10 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +228/−195 in 66 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:dear-dictator-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 9; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports 9 residue blocks; all were adjudicated against the bytes:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B13 | 73-73 → 93-93 (body → body) | no signature | Color-set table cell translation （主体/赤色）; section 6 |
| B14 | 79-79 → 99-99 (body → body) | no signature | Color-set table cell translation （太陽/金色）; section 6 |
| B15 | 89-89 → 109-109 (body → body) | no signature | Color-set table cell translation （白頭/白色）; section 6 |
| B16 | 95-95 → 115-115 (body → body) | no signature | Color-set table cell translation （先軍/茶色）; section 6 |
| B17 | 101-101 → 121-121 (body → body) | no signature | Color-set table cell translation （国防/黒色）; section 6 |
| B45 | 255-275 → 276-276 (code-css → code-css) | no signature | The `@font-face` load block deleted; its added line is the exhibit's porter head comment; sections 4 and 10 |
| B61 | 703-750 → 710-710 (code-css → code-css) | no signature | The KO nav-position rules deleted under their porter comment; sections 5 and 10 |
| B62 | 769-769 → 729-731 (code-css → code-css) | no signature | Sidebar background `none` → `var(--red)` under its porter comment; sections 5 and 10 |
| B65 | 863-863 → at 917 (body → body) | no signature | One line at the exhibit/gate close, pairing residue of the tail rearrangement; section 8 |

The 30 heuristic blocks are the one-line and short specimen translations counted in section 6 (blocks B4–B10, B18, B20, B23–B24, B26, B29, B31, B33, B35–B42, B44), the six font-stack rewrites of section 4 (B47, B49, B53, B56, B57, B60), the license-area restatement of section 1 (B48), and one deleted CSS region inside the exhibit's top-bar run (B63, original L784–793; section 8).

## Per-theme record — the usage snippet names a different page (defect flag, repaired)

The usage snippet is the one line a reader copies to adopt the theme, and on the bytes it names the wrong page. Candidate L76 reads `> @@[[include :scp-jp:theme:dear-dictator]]@@`. This candidate is theme:dear-dictator-jp: its canonical file is `pages/theme:dear-dictator-jp.txt`, its frame `theme=` URL and its code-page import both name `theme%3Adear-dictator-jp`, and the batch's EN and CN candidates with usage snippets (anon, ared, ashes-to-ashes, ad-abyssum-penumbra, crayon, deserted-years-theme, dream-of-the-stars) name their own `-jp` pages in theirs; the batch's other KO candidate, doap-bhl-jp, shows the same non-`-jp` shape at its candidate L32, which suggests a KO-wave habit rather than a considered naming decision, but a habit is not a disposition and no ledger line names it. Probes run for this package (2026-11-17): `https://scp-jp.wikidot.com/theme:dear-dictator` returns 404 and `https://scp-jp.wikidot.com/theme:dear-dictator-jp` returns 404 — neither page is posted yet, so the probe cannot settle intent; what the bytes settle is that the snippet is inconsistent with the candidate's own identity, and if the candidate posts under its canonical name the snippet will point at a page that does not exist. No ledger line dispositions the snippet's name (the T1 pseudo-ref class (iii) covers references to the not-yet-posted page itself, which this is not, on the bytes). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if the coordinator confirms it, is the one-line repoint of candidate L76 to the candidate's own page name, after which this package's diff.md and stamp need no change beyond regeneration (the candidate file's hash in the stamp would change). The coordinator confirmed it, and the repair has since landed as part of the usage-example population sweep (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), which repaired this shape across all 157 affected candidates: candidate L76 now reads `> @@[[include :scp-jp:theme:dear-dictator-jp]]@@`. This package is refreshed on the corrected bytes; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-dear-dictator-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row); it belongs to this theme's record but carries no port change of its own to explain here. The exhibit comment's reference to a PORT.md points at the campaign record outside this repo. There are no companion fragments and no shared base file.
