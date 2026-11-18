# Review package — theme:the-foundation-sigma-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:the-foundation-sigma-jp — origin EN, population #148 [GOSIGN2-LEDGER (b) row 148]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 944d5db8e14b36d4ca6ba081bcd90ea0ef5c2aee83170a06c7ad68d2b309da6c); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 1 info (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 133; GOSIGN2-LEDGER (b) row 148]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 474–506px@320/375 (page) and 474–557px@320/375 (sample); sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 148, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 148]
- FIX5 re-judgement: item 33 (class H) FIXED — FIX5-TEXTA §5, commit 6f6b349: usage example repointed to theme:the-foundation-sigma-jp [GOSIGN2-LEDGER-SUPPLEMENT (a) item 33]
- Computed against: canonical commit fd36608a54c17d699155b725e041a75bfd044996; candidate file pages/theme:the-foundation-sigma-jp.txt sha256:944d5db8e14b36d4ca6ba081bcd90ea0ef5c2aee83170a06c7ad68d2b309da6c; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: explanation written (lane rfix16, 2026-11-17); the verdict stamp above is generated and reads STALE by design: it was computed against the 435a6bb-era file, and the candidate has since changed in commit 722ceb5 (the frame sub-shape (B) remedy, section 3). The explanation below is written against the current bytes.
Candidate: review/the-foundation-sigma-jp/candidate.txt (sha256 d5fb879b06f95aae455041c2682ef5fe8183c4fb2f98ee41b0ca8d1ea26098cc)
Original: theme:the-foundation-sigma — scp-wiki, revision 7 (sha256 1e81edbce7d85e888a98baac9cd3bbb562bbfbd3188874abc7edbbc45d684564)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:the-foundation-sigma` on scp-wiki (EN), revision 7 — `original.txt` in this package |
| Candidate | `theme:the-foundation-sigma-jp` — `candidate.txt`, a byte copy of `pages/theme:the-foundation-sigma-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): same page skeleton, same inline CSS module, with the JP credit form, the JP font substitution, the asset re-hosting and the translation applied. No production JP counterpart was adopted, and no upstream supersession is recorded for this theme (the `review/sources.tsv` note field is empty). |

Summary: a Sigma-9 variant of the Foundation BHL theme. Both sides carry the same topology: a three-line head module holding a `local--code` self-import, the gated documentation body, and the theme's CSS as one inline `[[module CSS show="true"]]` (original L113–785; candidate L127–804). The port swaps the credit apparatus to the JP preview form naming macro_au_micro, replaces the original's Adobe Fonts delivery with Google Fonts public equivalents plus Noto Sans JP (with the reasoning left in the file as a porter annotation), re-hosts the base theme's three image files to JP storage, and translates the body. The theme carried one blocking item: ledger item 33 (class H), the usage example pointing at the nonexistent `theme:the-foundation-sigma`, re-judged FIXED by FIX5-TEXTA (commit 6f6b349). Its head-module self-import is the codeaddr audit's one genuine sub-shape (A) instance; section 3 records it with that citation. One open flag stands against the candidate as it is: a prose link naming a page with no JP counterpart (section 7).

## Class summary

| Label | Blocks |
|---|---|
| ASSET-REHOST | 8 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 25 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 54 |
| TRANSLATION-ANCHORED | 9 |

Counts: 83 blocks, 22 specific, 52 heuristic, 9 residue, 0 skipped (comment text).

## 1. Credit and attribution

- What: the candidate holds the JP preview credit block at L10–19 (CREDIT-PREVIEW and TASL-FIELDS labels, block B3): タイトル "The Foundation Sigma-9テーマ", 著作権者 `[[*user macro_au_micro]]`, 作成年 2023, 原題 "The Foundation Sigma-9 Theme", 翻訳責任者 AI, 翻訳年 2026, 初訳時参照リビジョン 7, 元記事リンク to the EN original. The original names the same author in its CSS banner (original L118, "By macro_au_micro", inside the module comment at L115–121), and the candidate's translated banner (candidate L131–136) keeps the name and adds the adaptation lines the original's prose carries: Woedenaz's The Foundation BHL theme adapted, on Aelanna's and Dr Devan's SCP Sigma 9 base. The original's labelled bare Rate in the head zone (original L6–9: `[[>]]` / `**Rating:**` / `[[module Rate]]` / `[[/>]]`) does not stand in the candidate (BARE-RATE-DEL block B2). Neither side carries a license box: `grep -n "license" ` returns nothing in either file, and none was supplemented.
- Why: class P3/T1 (credit swap) and KB-09 (the preview credit module is rate-bearing, so the labelled bare Rate beside it double-renders the widget — the FIX-GUIDER census shape, where 91 of 96 comparable ports dropped theirs). The author field names the person the original's banner names; the base-work credits stand in the banner, where the original's own attribution apparatus puts its credits, rather than in the field that names this theme's author.
- Verify: read candidate L10–19 against original L115–121; `grep -n -i "module rate" candidate.txt` returns nothing, the original returns L8.
- Disposition: no credit item was charged against this theme in GOSIGN2-LEDGER (b) row 148. The absence of a license box is the original's own state carried over, not a drop; the credit block carries the TASL record.

## 2. Includes and components

- What: the gate opens as `[[iftags +テーマ]]` at candidate L9 (original L5 `+theme`; IFTAGS labels ride on B2 and B3) and the hidden furniture gate at candidate L121 reads `[[iftags -テーマ]]` (B43; section 5). The one component include is repointed: `:scp-wiki:component:toggle-sidebar` (original L111) → `:scp-jp:component:toggle-sidebar` (candidate L125; INCLUDE-REPOINT on B44). The frame include stands at candidate L5–7 (`component:interwiki-style`, priority 1, no theme parameter — the 722ceb5 state, section 3). No include is duplicated, and no other live include exists in either file.
- Why: class P2/T2 with KB-08 (iftags conditions name JP tags, because the gate tests the JP environment's tag set) and P1 (include repoint).
- Verify: `grep -n "\[\[include" candidate.txt` returns the frame, the two credit includes and the toggle-sidebar include, all `:scp-jp:`.
- Disposition: no include item was charged against this theme; nothing stands open.

## 3. Delivery and code loading

- What: no relocation (the classifier's topology pass finds one 3-line module-css component on each side and no moves; the main CSS module is body-channel in both). Three delivery facts need stating. (1) The head module's self-import: original L2 `@import url('http://scp-wiki.wikidot.com/local--code/theme:the-foundation-sigma/1')` → candidate L2, the same address repointed to the candidate's own page on the draft host over https (`sigma10-jp-test.wdfiles.com/local--code/theme%3Athe-foundation-sigma-jp/1`; DELIVERY-HOST, DRAFT-HOST and SELF-DELIVERY labels on B1). The address names code block 1 of the page — and neither file contains any code block in any form (census: `[[code`, `[[code type="css"]]` and other typed forms, 0 in the original, 0 in the candidate). The import is therefore dead in the original exactly as in the candidate; the theme's CSS is delivered by the inline module, not by this address. This is the population audit's one genuine sub-shape (A) instance (R/review-scout/FIX-CODEADDR.md): the original carries the identical self-import with zero code blocks, so the candidate's repoint of it is the inherited form, recorded here with that citation and not re-litigated as a defect. It is also the theme's one T1 error (pseudo-ref×1). (2) The frame: the candidate's interwiki-style include (candidate L5–7) carries priority=1 and no theme= parameter. It originally carried a self-address theme parameter; commit 722ceb5 dropped the parameter under the main chat's codeaddr ruling, sub-shape (B) (the original carries no frame self-address in that role), the frame include kept. That landing is what makes the verdict stamp STALE: the stamp was computed against the pre-722ceb5 file. (3) The delivered CSS itself: the inline module (candidate L127–804) is the original's module (L113–785) translated and supplemented, brace depth final 0 / minimum 0 on both sides (measured).
- Why: class P4 (delivery) and KB-41 (the draft-host form of the candidate's own addresses is the sanctioned draft-stage form; posting rewrites it, class (ii)/(iii)).
- Verify: the code-block census above; `git show 722ceb5 -- pages/theme:the-foundation-sigma-jp.txt` shows the single dropped parameter line; candidate L2 against original L2 for the import.
- Disposition: the self-import is dispositioned by the codeaddr audit citation; the frame parameter by ruling (B) in commit 722ceb5. No delivery item stands open.

## 4. Fonts and assets

- What: fonts. The original loads Adobe Fonts (original L123, `use.typekit.net/cjg4ysl.css`) for its franklin-gothic-urw / titling-gothic-fb-compressed / hypatia-sans-pro stacks. The candidate loads none of it: a single Google Fonts import at candidate L142 carries Libre Franklin, Oswald, Source Sans 3, IBM Plex Mono and Noto Sans JP, and the stacks name exactly those faces (candidate L145–148: `--body-font` Libre Franklin, `--header-font` Oswald, `--title-font` Source Sans 3, `--mono-font` IBM Plex Mono, each suffixed with Noto Sans JP; JPFONT-LOAD label on B47, original L123 → candidate L137–142). The substitution is explained in the file (section 10) and in the translated font prose (candidate L113, which names all five faces and their SIL OFL status). No stack names a face that is not loaded, and no loaded face goes unused. Assets: the base theme's three image files are re-hosted from EN storage to JP storage, all nine references (ASSET-REHOST blocks B50, B57, B58, B60, B70, B71, B78, B81): cons_circle.png ×6 (original `scp-wiki.wdfiles.com/local--files/theme:the-foundation-theme/` → candidate `scp-jp-storage.wdfiles.com/local--files/file%3A7657035-64-uv5d/`), foundation-circles-bg.png ×2 (→ `file%3A7657035-65-wnwd`), foundation-header-img.png ×1 (→ `file%3A7657035-63-eagk`). Per-file counts match the original exactly; no EN-host asset reference remains.
- Why: pattern 7 / KB-16 for the JP load (the resolved base loads no JP face) and P5 / KB-17 for the re-hosting (assets serve from the allowlisted JP storage). The Adobe substitution is a licensing-delivery judgment: the typekit kit is the original author's Adobe delivery, not a redistributable source, so the same typefaces' public equivalents carry the stacks instead — the mapping is one-to-one and recorded in the file.
- Verify: `grep -n "@import" candidate.txt` returns exactly two lines (L2 the self-import of section 3, L142 the font import); `grep -o "local--files[^)]*" candidate.txt | sort | uniq -c` returns the three JP-storage addresses with counts 6/2/1.
- Disposition: no font or asset item was charged against this theme; the T1 baseline's single error is the section-3 pseudo-ref, dispositioned there.

## 5. Header, sidebar, site furniture

- What: the theme defines no `--header-title` / `--header-subtitle` variables on either side (grep returns nothing in both files); its header is the BHL base's. The furniture gate is the hidden div at candidate L121 (`[[div [[iftags -テーマ]]style="display: none"[[/iftags]]]]`, IFTAGS block B43, against original L107 `-theme`), which hides the theme's furniture block on themed pages. The toggle-sidebar component include follows at candidate L125 (section 2). The render record's "EN header THE FOUNDATION" text (LOCALIZE-ROWS row 148, T5 finding (2)) is the site header served by the base on the check wiki, not a string in this file.
- Why: KB-08 for the gate tag; ruling 2 (ledger (c3) P9) takes header and title language out of scope as a defect class, and the ledger dispositions this theme's P9 instance on that ground.
- Verify: candidate L121 against original L107; the variable grep above.
- Disposition: P9 DISPOSITIONED (ruling 2) for this theme [GOSIGN2-LEDGER (c3)].

## 6. Text translation

- What: the body is the standard Foundation/BHL usage text, translated throughout: TRANSLATION-ANCHORED fires 9 times (B18, B19, B21, B33–B36, B41, B43 — one-to-one pairs in the examples body) and TRANS-UNANCHORED 54 times, of which the body-prose set (B5–B42 region) is the same text where the differ lost its anchors, and the module set is CSS comment translation (section 10's mass, adjudicated in the appendix). The one reader-visible string the campaign charged is in section 7's neighbourhood: the usage instruction prose around the example was already Japanese at ledger time; only the example's target was wrong (item 33). The font prose (candidate L113) is a rewritten paragraph, not a literal translation: it names the substitute faces of section 4.
- Why: class P10 (translation); CSS comments are porter-visible only (R1) and are adjudicated by shape in the appendix.
- Verify: read candidate L21–117 against original L11–103; the examples pair section by section (usage, titles, collapsibles, tabview, tables, blockquotes).
- Disposition: T5 judged jointly with T4 in LOCALIZE-ROWS row 148: two display-affecting findings — item 33 (section 7's record) and the P9 header (section 5). No other translation item stands open.

## 7. Links

- What: one repoint, one absolutization, and one open flag. The usage example (candidate L29) is item 33's locus, covered in the per-theme record. The SCP-4485 reference in the intro prose was absolutized with the pattern-11 annotation (candidate L23: `[[[https://scp-wiki.wikidot.com/scp-4485|SCP-4485（英語版）]]]`, against original L13's plain `[[[SCP-4485]]]`). The flag: the same sentence's base-theme link stands as `[[[theme:the-foundation-theme|The Foundation]]]` in both files (original L13, candidate L23). No page `theme:the-foundation-theme-jp` exists in this repository (no file in `pages/`, no row in `review/sources.tsv`), and `theme:the-foundation-theme` will not exist on scp-jp, so the link is dead in the JP environment — the same class-H family as item 33, one line away from the neighbour link that did receive the annotation treatment. The package is written against the candidate as it stands; the remedy is a repair-lane decision (the absolutized-and-annotated form its neighbour received, or plain text), not a builder edit.
- Why: class P11 (dead prose references): a prose link naming a page that will not exist sends the reader to a 404; the population's established remedy for a no-counterpart target is the pattern-11 annotation branch or plain text with the reference preserved.
- Verify: `ls pages/ | grep foundation-theme` returns nothing; candidate L23 against original L13 shows both links side by side.
- Disposition: item 33 FIXED (per-theme record). The base-theme link was not charged in the ledger; it is flagged here and in the lane report as an open item for the coordinator.

## 8. Structure

- What: the page skeleton is unchanged: head module, gate, credit, usage body, hidden furniture div, toggle-sidebar include, CSS module. The one EXHIBIT-RESTRUCTURE block (B44, original L111 → candidate L125) is the classifier's known false-fire shape: the only change at that locus is the toggle-sidebar include repoint of section 2, inside the furniture region; no exhibit was dropped or replaced anywhere in the file — the examples body is complete against the original (titles, collapsible, tabview, tables, blockquote and code exhibits all present, candidate L50–117 against original L36–103). The emptied-looking region at candidate L121–125 is the original's hidden-div furniture, carried in form.
- Why: class R3's question is answered: nothing replaced, nothing dropped; the label fired on an include repoint.
- Verify: the exhibit census above, read against diff.md's block index (83 blocks, none removing an exhibit range).
- Disposition: no structure item was charged against this theme.

## 9. Formatting only

- What: no WS-ONLY blocks and no re-indentation pairings (class summary: 0 / 0). Every changed line in this package carries content.
- Why / Verify / Disposition: nothing to adjudicate; the count is the classifier's, readable in classification.json's summary.

## 10. Porter annotations

- What: one substantial annotation, at candidate L137–141, inside the CSS module above the font import (riding on B47): headed `SCP-JP補正`, it records that the original's Adobe Fonts delivery is outside the direct-link exceptions, and maps each typekit family to its Google Fonts public equivalent (franklin-gothic-urw → Libre Franklin, titling-gothic-fb-compressed → Oswald with the note that the original face is not distributed, hypatia-sans-pro → Source Sans 3, IBM Plex Mono as-is). The translated CSS banner (candidate L131–136) is the original's banner in Japanese, not an annotation. The remaining comment mass — 25 COMMENT-TEXT blocks and the comment-shaped residue — is R1 translation of the original's own comments, adjudicated in the appendix, not porter commentary.
- Why: the annotation is the audit trail for section 4's substitution judgment; it sits at the locus a future porter will open first.
- Verify: read candidate L137–142.
- Disposition: annotation present and accurate against the original's L123 import.

## 11. Dispositions and exceptions

- Derived presence: no derived-presence label fired for this package. The standing dispositions, each re-derivable from the two sources in this package:
- The head-module self-import (section 3): sub-shape (A) of R/review-scout/FIX-CODEADDR.md — the audit's one genuine instance; the original carries the identical import with zero code blocks in any form, so the address is inherited dead text, and the candidate's repoint of it is recorded, not a defect. The same line is the T1 pseudo-ref error, dispositioned in register (c1) on this ground.
- The frame theme-parameter drop (section 3): sub-shape (B) remedy, commit 722ceb5, under the main chat's codeaddr ruling; the stamp's STALE state is this disposition's side effect, not an unjudged change.
- The draft-host form of the self-import (candidate L2): KB-41 class (iii) draft-stage form; posting rewrites the candidate's own addresses (class (ii)).
- The header language (section 5): P9, ruling 2.
- The sample credit-modal errors in the T2/T3 record: the standing preview-form disposition (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2). The T2/T3 page-overflow figures (474–506px@320/375 page, 474–557px sample) stand as classified render evidence in RENDER-ROWS-2 (RENDER-S2-D (EN21)); no item in (e) charges them.

## 12. Verification

- Package integrity: `original.txt` SHA-256 equals the `review/sources.tsv` mirror hash (1e81edbc…) and `candidate.txt` is byte-identical to `pages/theme:the-foundation-sigma-jp.txt` (sha256 d5fb879b…); both verified at assembly and re-verified by `python3 review/build_review.py --check`. The stamp's STALE reading is expected and explained in section 3; it is not a package defect.
- T1: baseline exit 1, 1 error / 1 warn / 1 info (pseudo-ref×1) [T1-ROWS row 133]; the error is dispositioned in section 11. FIX5-TEXTA's commit records no checker change on this file.
- T2/T3: FINDINGS as recorded in the verdict stamp (page-overflow at small widths; sample credit-modal preview-form) [RENDER-ROWS-2 (RENDER-S2-D (EN21))], engine coverage full matrix.
- T4 follow-up: the per-theme record below re-derives item 33 from the bytes; it passes. The section-7 flag is this package's one open item and is a candidate defect, not a package defect.

## Per-theme record — the FIX5 closure, re-derived

- The item: GOSIGN2-LEDGER (e) item 33, class [H] — the usage example at ledger-time L30 pointed at `theme:the-foundation-sigma`, a page that does not exist on scp-jp; the candidate is `theme:the-foundation-sigma-jp`. LOCALIZE-S2-C charged it as a copy-paste 404 (LOCALIZE-ROWS row 148, T5 finding (1)).
- The re-judgement: GOSIGN2-LEDGER-SUPPLEMENT (a) item 33 — FIXED, wave FIX5-TEXTA §5, commit 6f6b349: "usage example repointed to theme:the-foundation-sigma-jp".
- What the fix was supposed to change: exactly the example's target, from the plain name to the candidate's own name, in the escaped usage exhibit.
- Verification against the bytes: commit 6f6b349's diff for this file is one line: the example at (now) candidate L29 reads `> @@[[include :scp-jp:theme:the-foundation-sigma-jp]]@@`, against original L19's `:scp-wiki:theme:the-foundation-sigma`. A census of the plain name in the current candidate returns two remaining occurrences, both correct in role: the 元記事リンク source URL in the credit block (candidate L18, a quotation of the original) and nothing else — the delivery import at L2 names the -jp page. The fix is present and complete.
- Post-FIX5 change: commit 722ceb5 (frame sub-shape (B), section 3) touched the file after the FIX5 head; it does not touch the example. The stamp's STALE state dates from that landing.
- Verdict: the supplement's account matches the bytes. FIXED stands, re-derived. The neighbouring dead link of section 7 is a separate, uncharged instance of the same family and does not reopen item 33.

## Per-theme record


### Post-package repairs (REFRESH3-D)

FIX-FRAMEADDR (`722ceb5`) lands *before* this package's candidate build (`05f0db5`): the frame at L5 was remedied under sub-shape (B) and the head `@import` at L2 is the report's one sub-shape (A) instance; both were already in the built candidate and recopy confirms no byte change from them. The one post-package repair is the prose link below.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Athe-foundation-sigma-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L5.
- **FIX-FRAMEADDR, sub-shape (A) — Inherited** (report §1; same landing `{FRAME}`): the head `@import` at candidate L2 naming the candidate's own `local--code/theme%3Athe-foundation-sigma-jp/1` is the port of the original's identical dead self-import (original L2, 0 code blocks). The report applies no edit; this refresh leaves it byte-unchanged.
- **FIX-RFIX16 — dead base-theme prose link** (report `R/review-scout/FIX-RFIX16.md`; landing `fd36608a54c17d699155b725e041a75bfd044996`, 2026-11-17): candidate L22's `[[[theme:the-foundation-theme|The Foundation]]]` was absolutized to `[[[https://scp-wiki.wikidot.com/theme:the-foundation-theme|The Foundation（英語版）]]]`, matching the neighbouring SCP-4485 link's form. Recopy changed this line only (24,034 → 24,078 bytes).

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

- None inside this repository: the theme is self-contained in its page (its base is the shared BHL environment, not a file in this diff). The 722ceb5 remedy is a change to the candidate file itself, inside the diff's candidate side.

## Multi-wave provenance

- S2 port (LOCALIZE-S2-C): the translation, credit swap, font substitution and asset re-hosting.
- FIX5-TEXTA §5 (commit 6f6b349, 2026-11-17): the usage-example repoint.
- Codeaddr remedy (commit 722ceb5, 2026-11-17): the frame sub-shape (B) parameter drop — the candidate's last change and the stamp's STALE cause.
- GOSIGN2 determination and go-sign (COMPLETION-REPORT §10, 2026-11-17): the ledger verdict the stamp records.

## Appendix — heuristic and residue adjudication

52 heuristic blocks and 9 residue blocks, resolved by shape. Every block below was read against the mirror; the shapes are exhaustive over the two sets.

- Shape 1 — in-CSS comment translation (R1, porter-visible only): the 24 COMMENT-TEXT-only blocks B45, B46, B49, B51, B52, B53, B54, B56, B59, B61, B62, B63, B65, B66, B67, B68, B69, B72, B73, B74, B77, B79, B82, B83, plus residue B55, B75, B76, B80 (same shape, no signature fired). Each is a single banner or inline comment line inside the CSS module, translated in place: e.g. original L525 `/* RATING MODULE */` → candidate L544 `/* 評価モジュール */`; original L479 `/* MOBILE SIDE-BAR */` → candidate L498 `/* モバイル用サイドバー */`; original L700 `/* content background color */` → candidate L719 `/* 本文背景色 */`; original L732 `/* LINE */` → candidate L751 `/* 水平線 */`. B47 also carries COMMENT-TEXT but is specific-labeled (JPFONT-LOAD) and is adjudicated in sections 4 and 10. No rule, selector or value changes in any of these blocks.
- Shape 2 — usage-prose translation without anchors: B5, B6, B7, B9, B11, B12, B13, B14, B15, B16, B17, B20, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B37, B38, B39, B40, B42. The BHL boilerplate body (usage, examples, footnotes prose) translated line by line; the differ lost the pairing where Japanese word order or a rewritten sentence broke its anchor tokens. Read against the mirror, each pair is the same sentence in Japanese; no content was added, dropped or restructured. B3 and B44 also carry TRANS-UNANCHORED but are specific-labeled and adjudicated in sections 1 and 8.
- Shape 3 — exhibit-region residue: B4 (original L36–53 → candidate L50–67), B8 (original L46–53 region), B10. The titles/tabview exhibit, translated with its heading text and tab labels in Japanese; the classifier found no signature because the exhibit's own markup tokens changed language with its text. The exhibit is complete (section 8 census).
- Shape 4 — unchanged-line seams: B48 (original L439 `color: white;` → candidate L458, identical) and B64 (original L549 → candidate L568, identical `background-color` line). The lines themselves are byte-identical on both sides; the differ isolated them because their neighbouring lines changed (Shape 1 comments). No change to adjudicate.

## License and attribution

- **Title:** The Foundation Sigma-9 Theme
- **Author:** macro_au_micro
- **Source:** https://scp-wiki.wikidot.com/theme:the-foundation-sigma — revision 7
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
