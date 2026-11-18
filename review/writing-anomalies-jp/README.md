# Review package — theme:writing-anomalies-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:writing-anomalies-jp — origin EN, population #160 [GOSIGN2-LEDGER (b) row 160]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 0 warns / 1 info (pseudo-ref×5); standing classes dispositioned in register c1 [T1-ROWS row 180; GOSIGN2-LEDGER (b) row 160]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN24))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN24))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 160, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 160]
- FIX5 re-judgement: item 42 (class H) FIXED — FIX5-TEXTA §4, commit 6f6b349: usage example repointed to theme:writing-anomalies-jp [GOSIGN2-LEDGER-SUPPLEMENT (a) item 42]
- Computed against: canonical commit 6f6b34974c400a68e01363f5423d1cf817492522; candidate file pages/theme:writing-anomalies-jp.txt sha256:eb5ecfcf7927d3bca309daa585773281345a8e4ba4c2d17761ecd5b1aead2825; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Candidate | `theme:writing-anomalies-jp` — `pages/theme:writing-anomalies-jp.txt`, 307 lines, 8,181 bytes (sha256 in the stamp) |
| Original | `theme:writing-anomalies` on scp-wiki (EN), reference revision 20 — `original.txt`, 274 lines, 6,006 bytes, sha256 matches `review/sources.tsv` |
| Class | R-fix — one blocking item (ledger item 42), FIXED in FIX5 |
| Reference-revision record | `start-themes.tsv`: "Complete (merged in EN24, Check 5 not measured: retired 2026-11-16)", delivery standalone, first-translation rev 20 |

Provenance route: derived from the original at the reference revision (standard kind; no production JP counterpart exists — the /start delivery is "post the port candidate as a new page"). The mirror was produced by the S2 localization lane that built the port (LOCALIZE-S2-C).

A handwriting-style Sigma-9 derivative. The port repoints delivery to the draft host, adds the preview credit block and a license box, removes the bare Rate module, translates the body and the CSS-visible strings, supplements the Latin handwriting stack with Noto Serif JP, and — silently, as an in-place repair — fixes three pieces of malformed CSS in the original's stylesheet tail (a broken border declaration, a stray slash, and brace damage that left the file's last rules unclosed). The one blocking item (42, the usage example's self-reference) is re-derived in the per-theme record. No defect is flagged from this package.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 10 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 6 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 3 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 9 |
| TRANSLATION-ANCHORED | 6 |
| WS-ONLY | 1 |

Counts: 39 blocks, 21 specific, 15 heuristic, 3 residue, 0 skipped (comment text).


Component topology (classifier): module-css 1 + code-css 1 on each side, no moves. The candidate adds one component the original does not carry (the interwiki-style frame, §3).

## 1. Credit and attribution

What: the original carries no credit block and no license box; its attribution is the stylesheet banner ("Writing anomalies" theme / [2021 Wikidot Theme] / Created by Cole 13 for the SCP Wiki / CC BY-SA 3.0, orig L84–89) and the body line naming [[*user Cole 13]] as the author (orig L16). The candidate adds the preview credit block at cand L12–21 (B4) with 著作権者 [[*user Cole 13]] — the named author the original names, in link form; no pointer stands in place of a name. It adds a license box at cand L287–305 (B40) whose author field names Cole 13, with three entries: HEADER H (Cole 13), THX@ (Cole 13), and thx, the page logo (Luxaiko — the original's own caption credit at orig L54, "Logo made by [[*user Luxaiko]]"). The bare Rate module at orig L10–12 is removed (B5, BARE-RATE-DEL); the preview credit block is rate-bearing, so no second widget stands.
Why: the JP environment's preview credit is the rate-bearing credit form that renders here (P3); a bare Rate beside it would double the widget (patterns/ KB-09, commit 9c5e907). The license entries record the theme's image assets (patterns/ KB-63).
Verify: `grep -n "module Rate" candidate.txt` returns nothing; read cand L12–21 against orig L84–89 and L16; read cand L287–305 against orig L54.
Disposition: ledger (c3) row 180 records P1 DISPOSITIONED (§11); the T4 display-affecting count is 1 (LOCALIZE-ROWS row 160). No class (i) defect stands against this theme.

## 2. Includes and components

What: the candidate's live includes are the interwiki-style frame at cand L5–8 (added, §3), the credit pair (cand L12, L21), image-block at cand L63, and the license-box pair (cand L287, L305). The original's only live include is image-block (orig L54). The usage example at cand L33 (B9: COMPONENT-SWAP, ESCAPED-INCLUDE, INCLUDE-REPOINT) is item 42's locus: its include was repointed from the non-`-jp` JP name to the candidate's own name — the per-theme record re-derives it.
Why: components must resolve on scp-jp at posting, and the usage example must name the page that will exist.
Verify: `grep -n "include" candidate.txt` against the same grep on `original.txt`.
Disposition: item 42 CONFIRMED closed (per-theme record).

## 3. Delivery and code loading

What: the head [[module CSS]] @import moves from `http://scp-wiki.wdfiles.com/local--code/theme%3Awriting-anomalies/1` (orig L2) to the draft host's own /1 (cand L2; B1, DRAFT-HOST, class (iii)). A frame include is added at cand L5–8 (B2, SELF-DELIVERY): component:interwiki-style, priority 1, naming the same own /1. Census: exactly one code block in the candidate, `[[code type="css"]]` at cand L91–282, and it is the stylesheet (192 lines); the /1 address names it — the FIX-CODEADDR audit form: MATCH, and the named block is the stylesheet, not an exhibit. The @import module stands outside the +テーマ gate on both sides and the code block inside it on both sides; delivery topology is otherwise unchanged.
Why: own-name delivery keeps the stylesheet with the page; the priority-1 frame gives the interwiki sidebar the same CSS (the population's frame stack, patterns/ KB-07).
Verify: count every code-block form (`grep -c "\[\[code" candidate.txt` = 1, the typed form included); read cand L1–8.
Disposition: the five T1 pseudo-ref errors are exactly these draft-host lines (class (iii), §11).

## 4. Fonts and assets

What: the Indie Flower import moves from fonts.bunny.net (orig L83) to fonts.googleapis.com (cand L92), same family and weights (B18, FONT-IMPORT). Noto Serif JP (wght 400;700) is loaded at cand L93 (JPFONT-LOAD), and the three 'Indie Flower', cursive stacks gain 'Noto Serif JP' (cand L112, L132, L149; B21, B26, B28, JPFONT-STACK). Assets: three local--files URLs are repointed from scp-wiki.wdfiles (http) to the draft host (https) — HEADER H (orig L108 → cand L119), THX@ (orig L111 → cand L122 and orig L144 → cand L155) (B23, B24, B29, DRAFT-HOST). The image-block exhibit's name=, a malformed string in the original (`thx . PNG image data`, orig L54), becomes the draft-host local--files URL for thx (cand L63).
Why: the pattern-7 JP supplement (patterns/ KB-16): translated text renders in the theme's display stacks, so the JP face must be both loaded and stacked. The bunny.net → Google Fonts move keeps the Latin face on the population's font host. Draft-host asset forms are the class (iii) posting convention.
Verify: `grep -n "@import\|font-family" candidate.txt` — every named face (Indie Flower, Noto Serif JP) is loaded and every loaded face is stacked.
Disposition: no font finding stands; the draft-host lines are the §11 baseline.

## 5. Header, sidebar, site furniture

What: the sidebar selector groups are extended with `#interwiki` counterparts (cand L196–216 against orig L185–205; B31–B35, CSS-BODY heuristic) — the same rule bodies now also style the JP environment's interwiki sidebar. Two CSS `content:` strings are translated: "SCP Foundation" → "SCP財団" (cand L130) and "Secure, Contain, Protect" → "確保、収容、保護" (cand L143) (the B25/B27 spans).
Why: the interwiki extension is the population's JP-DOM selector shape (taxonomy residue class R6). `content:` strings are rendered text (patterns/ KB-18) and translate with the body; header language is translation taste under ruling 2 either way — the port translated them, and the choice is recorded here rather than re-judged.
Verify: `grep -n "#interwiki\|content:" candidate.txt`.
Disposition: no ledger row charges or dispositions these lines.

## 6. Text translation

What: the whole body is translated (cand L23–88 against orig L14–79): the explainer prose, the tabview specimen's four tabs, the table specimen, the image-block caption, and the collapsible labels (+ Collapsible / - Close at orig L56 → + 折り畳み / - 閉じる at cand L65). The footnote at cand L38 is translated, and the port adds its [[footnoteblock]] at cand L285 — the original carries the footnote (orig L29) but no footnoteblock anywhere, so the block is a supplement the port adds, not the repair of a charged item; it gives the footnote its render position and is recorded here for that reason.
Why: translation is the port's purpose; the footnoteblock completes the original's own footnote apparatus.
Verify: read cand L23–88 against orig L14–79; `grep -n "footnoteblock" original.txt candidate.txt` returns 0 hits in the original and 1 in the candidate.
Disposition: T4 display-affecting 1 (LOCALIZE-ROWS row 160, LOCALIZE-S2-C).

## 7. Links

What: the credit block's 元記事リンク (cand L20) names the EN original on scp-wiki.wikidot.com — the recorded origin host in `review/sources.tsv`; the license entries' source links (cand L293, L298, L303) name the same page. No candidate link names a different host from the recorded one, so no host probe was required. No prose link names a JP page that will not exist; the only JP page reference is the usage include (§2).
Why: a credit/source link must reach the original page it credits.
Verify: `grep -n "wikidot.com\|wdfiles" candidate.txt` and compare hosts against the sources.tsv row.
Disposition: none recorded against these lines.

## 8. Structure

What: three in-place repairs of the original's malformed CSS, all inside the code block. (a) The blockquote border `border: 2px dashed; #000000;` (orig L104) becomes `border: 2px dashed #000000` (cand L115; B22). (b) A stray `/` line inside the `div.open-menu` rule (orig L259) is dropped (B36). (c) The tail brace damage: `.footnotes-footer` is left open by a stray `{` (orig L264) and the closing `@media` block (orig L265) never closes — a brace-depth scan of the original's code block ends at depth 3, the candidate's at depth 0; the candidate closes .footnotes-footer (cand L274), the hover selector group (cand L280), and the @media (cand L281) (B37, B38). The rule-less hover selector group itself is carried as authored. Presentation: the code block is wrapped in a テーマのソース collapsible the original does not have (cand L90, L283; the B17/B39 region) — an exhibit restructure; the exhibit census is otherwise unchanged (tabview, table, image-block, collapsible specimen, footnote all stand). The EXHIBIT-RESTRUCTURE label on B15 is the image-block line, adjudicated in §4: only its name= form changed, the exhibit stands.
Why: the port must deliver a stylesheet that parses; the original's tail damage is upstream's, repaired in place rather than propagated. The repairs change no rule's values.
Verify: the brace-depth scan in §12; read orig L258–270 against cand L269–281.
Disposition: no ledger row charges the original's CSS damage; the repairs are recorded here as port behaviour, not as a fix claim.

## 9. Formatting only

What: one whitespace-only block (B30: orig L182–183 → cand L193–194, trailing whitespace in the #top-bar rule area). No re-indentation and no line-ending change anywhere else.
Verify: classification.json, block B30.

## 10. Porter annotations

What: one annotation — the banner line "Ported for SCP-JP (theme:writing-anomalies rev 20)" added at cand L99 (B20, residue). Its statement matches the bytes: rev 20 is the reference revision. The license box's 出典 fields are attribution apparatus (§1), not annotations.
Disposition: annotations of this form are the population's R2 shape.

## 11. Dispositions and exceptions

What: T1 baseline (T1-ROWS row 180): 5 pseudo-ref errors, all class (iii) draft-host forms (the head @import, the frame, the image-block name=, the asset URLs) — DISPOSITIONED as the posting-time convention; ledger (c3) records P1 DISPOSITIONED on the same ground. The render row (RENDER-ROWS-2, RENDER-S2-D, EN24) gives the page verdict FINDINGS on the runtime-hotlink chain only — DISPOSITIONED (patterns/ KB-40: the chain lives at the environment layer, not in this source); the sample carries no machine verdict, a coverage caveat recorded in the row, not a theme defect. No class (i) item stands, and no defect is flagged from this package.
Verify: T1-ROWS row 180; the theme's RENDER-ROWS-2 row.

## 12. Verification

- T1 checker (`check_source.py --kind theme --translation`), run by this lane on the current candidate: error 5 / warn 0 / info 1 — identical totals and classes to the stamp baseline (T1-ROWS row 180); all 5 errors are the class (iii) draft-host lines of §3/§4.
- Brace-depth scan (strip strings and comments, track `{}` depth over the code block): original final depth 3, min 0; candidate final depth 0, min 0 (§8).
- Code-block census: 1 in the candidate (typed form counted); the /1 address names it (§3).
- Package checks: candidate.txt is byte-identical to the canonical file; original.txt's sha256 equals the sources.tsv value; `python3 review/build_review.py --check` at acceptance (batch report).

## Per-theme record — the FIX5 closure, re-derived

Item 42 [H] (ledger (e) row; GOSIGN2-LEDGER-SUPPLEMENT, FIX5-TEXTA §4).
Charged: the usage example at (then) L33 read `@@[[include :scp-jp:theme:writing-anomalies]]@@`, probed 404; the candidate itself is theme:writing-anomalies-jp, so the example named a page that will not exist.
Fix as recorded: one line repointed to the -jp name, canonical commit 6f6b349 — `git show 6f6b349` is exactly that one-line diff in this file.
Re-derived: cand L33 reads `@@[[include :scp-jp:theme:writing-anomalies-jp]]@@`. The change is present and complete, and no other plain-form self-reference stands in the file.
Closure: CONFIRMED.

## Change set outside the two diffed files

- `pages/theme-decoration-sample-writing-anomalies-jp.txt` — the display-check sample (the render row's page; no machine verdict, §11).
- The `start-themes.tsv` row quoted in §0 (the delivery record).

## Multi-wave provenance

- The port was built by the S2 localization wave (LOCALIZE-S2-C; the mirror came from that lane's store), with the credit and license apparatus of the credit waves.
- FIX5-TEXTA commit 6f6b349 closed item 42. The verdict stamp computes against that commit and the candidate's sha is unchanged since, so the stamp is current, not stale.

## Appendix — heuristic and residue adjudication

- B22 (heuristic, CSS-BODY): the blockquote border repair — §8(a).
- B25, B27 (heuristic, CSS-BODY): the `content:` string translations — §5. (The same blocks carry JPFONT-STACK label spans; labels are per-block primary forms, the sections are written from label_spans.)
- B31–B35 (heuristic, CSS-BODY): the `#interwiki` selector extensions — §5.
- B37, B38 (heuristic, CSS-BODY): the tail brace repairs — §8(c).
- B6, B7, B11, B13, B16 (heuristic, TRANS-UNANCHORED): body prose and specimen lines translated without an anchor majority — §6, by shape.
- B17 (heuristic, TRANS-UNANCHORED): the `@@ @@` separator run plus the added テーマのソース collapsible opening — §8.
- B15 (specific, EXHIBIT-RESTRUCTURE): the image-block name= re-host — §4/§8.
- B30 (specific, WS-ONLY): §9.
- B19 (residue; orig L84–85 → cand L94–95): the banner's head lines, carried verbatim; the block is the differ's seam beside the annotation line added at cand L99 (B20). No content change in B19 itself.
- B20 (residue; cand L99): the added banner annotation — §10.
- B36 (residue; orig L259): the stray `/` removal — §8(b).

## License and attribution

- **Title:** Writing Anomalies
- **Author:** Cole 13
- **Source:** https://scp-wiki.wikidot.com/theme:writing-anomalies — revision 20
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
