# Review package — theme:tales-of-the-mosaic-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:tales-of-the-mosaic-jp — origin EN, population #143 [GOSIGN2-LEDGER (b) row 143]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 21 errors / 1 warn / 1 info (hotlink×20, foreign-include×1); standing classes dispositioned in register c1 [T1-ROWS row 163; GOSIGN2-LEDGER (b) row 143]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 143, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 143]
- FIX5 re-judgement: item 32 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 fix; checker code-multiset identical before/after [GOSIGN2-LEDGER-SUPPLEMENT (a) item 32]
- Computed against: canonical commit 8eacd6e675b726c2fcf93372dc4dd7899958c2d4; candidate file pages/theme:tales-of-the-mosaic-jp.txt sha256:62f0576e9497294824a81066041cffbd188fb3c448c17af6b3b43596a2bcdfca; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: explanation written (lane rfix16, 2026-11-17); the verdict stamp above is generated, and the candidate has not changed since the stamp was computed (the stamp reads PASS, computed against the FIX5 commit itself).
Candidate: review/tales-of-the-mosaic-jp/candidate.txt (sha256 62f0576e9497294824a81066041cffbd188fb3c448c17af6b3b43596a2bcdfca)
Original: theme:tales-of-the-mosaic — scp-wiki, revision 25 (sha256 3587315ee1ded018b17f189b315b4e2da84bd278d0f8bc4f4bc935f3714407a2)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:tales-of-the-mosaic` on scp-wiki (EN), revision 25 — `original.txt` in this package |
| Candidate | `theme:tales-of-the-mosaic-jp` — `candidate.txt`, a byte copy of `pages/theme:tales-of-the-mosaic-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the candidate is the original's body, exhibits and CSS carried over with the JP environment's delivery frame, credit form and translations applied. No production JP counterpart was adopted, and no upstream supersession is recorded for this theme (the `review/sources.tsv` note field is empty). |

Summary: a Black Highlighter theme whose original delivers its own CSS from a `[[code type="css"]]` block (original L195–834) fetched through a `local--code` self-import (original L934–936). The port delivers the same CSS body as an inline `[[module CSS]]` at the head of the page (candidate L1–646), keeps the code block as the source-code exhibit (candidate L860–1492), repoints the BHL base delivery to the JP frame (interwiki-style priorities 1–2, candidate L648–657), swaps the credit apparatus to the JP preview form naming Jezixo, translates the documentation body, and keeps the dusk/night variant modules behind their include-parameter comment gates. The theme carried one blocking item: ledger item 32 (class D), the pattern-7 JP font named but never loaded, re-judged FIXED by FIX5-FONTSA (commit 8eacd6e). The per-theme record below re-derives that closure from the bytes in this package.

## Class summary

| Label | Blocks |
|---|---|
| COLON-ENC | 14 |
| COMMENT-TEXT | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-MOVE | 43 |
| EXHIBIT-RESTRUCTURE | 3 |
| HEADERVAR | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 3 |
| LICENSE-BOX | 2 |
| RESTORATION | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 18 |
| TRANSLATION-ANCHORED | 3 |
| WS-ONLY | 5 |

Counts: 49 blocks, 49 specific, 0 heuristic, 0 residue, 0 skipped (comment text).

## 1. Credit and attribution

- What: the original carries no credit module; attribution stands in the page byline (original L56–58, "by Jezixo"), the CSS banner (original L197–204, "Created by Jezixo") and the license box (original L838–931, `:scp-wiki:component:license-box-theme` with per-file entries; one entry names Jezixo and Ghostdyes as image authors, original L925–929). The candidate holds the JP preview credit block at L702–711 (`credit:start-preview` / `credit:end-preview`, CREDIT-PREVIEW and TASL-FIELDS labels, both inside the B19 alignment block): タイトル "Tales of the Mosaicテーマ", 著作権者 Jezixo, 作成年 2025, 原題， 翻訳責任者 AI, 翻訳年 2026, 初訳時参照リビジョン 25, and the 元記事リンク to the EN original. The license apparatus stands at candidate L1497 (`license-box-backend |author=Jezixo`) through L1588 (`license-box-end`), LICENSE-BOX blocks B20 and B38, with the per-file entries translated (ファイル名 / 作者 / ライセンス / ソースリンク）; the Jezixo-and-Ghostdyes image entry is among them (candidate L1583–1586 region).
- Why: class P3/T1 (credit swap) and T4 (license box). The branch credit apparatus does not render in the JP environment; the preview form is the rate-bearing JP form, and the TASL fields are what let a reader trace the port to its original and its reference revision. The author field names the person the original names — Jezixo, in the byline, the banner and the license parameter alike; no pointer stands in place of the name.
- Verify: read candidate L702–711 against original L56–58 and L197–204; `grep -n "license-box" candidate.txt` returns the backend include at L1497 and the end include at L1588, matching the original's pair at L838/L930 in JP form.
- Disposition: no credit item was charged against this theme in GOSIGN2-LEDGER (b) row 143; the swap is the standing P3/T4 form. PASS at the ledger determination for this section's classes (register (c1)).

## 2. Includes and components

- What: every live include is repointed to its `:scp-jp:` counterpart. The usage exhibits name `:scp-jp:theme:black-highlighter-theme`, `:scp-jp:component:toggle-sidebar-bhl` and `:scp-jp:component:centered-header-bhl` (candidate L736–738, escaped exhibits, against original L72–74), and the self-includes name the candidate itself, plain and with the variant parameters (candidate L739, L745 `dusk=--`, L751 `night=--`, against original L75, L81, L87). The head module's component imports are repointed to the JP file host (candidate L663–664, `scp-jp.wdfiles.com/local--code/component%3Atoggle-sidebar-bhl/1` and `component%3Acentered-header-bhl/1`, against original L7–8 on `scp-wiki.wdfiles.com`). The license includes are covered in section 1 (INCLUDE-REPOINT label on B38). One foreign include survives, inside an escaped documentation exhibit: `@@[[include :snippets:html5player@@` at candidate L829, identical in form to original L165 — exhibit text in both files, never a live include.
- Why: class P1 (include repoint). A kept `:scp-wiki:` include imports the EN page into JP pages or fails; the escaped exhibit is documentation of the syntax, and its foreign name is the point of the example. The self-include parameters `dusk=--` / `night=--` are the variant gates of section 3 and must name the candidate, not the original.
- Verify: `grep -n "\[\[include" candidate.txt` — every live include is `:scp-jp:`; the only other match is the escaped html5player line, which sits inside `@@` markers in both files.
- Disposition: the html5player exhibit is the theme's one T1 foreign-include error, dispositioned in GOSIGN2-LEDGER (c1) as an escaped documentation example (FIX2-INCLUDE). No include item stands open.

## 3. Delivery and code loading

- What: the delivery topology is restructured (DELIVERY-MOVE, 43 blocks; the classifier's topology pass matches the original's code-css body to the candidate's module at similarity 0.973 and to the region containing the exhibit copy at 0.971). The original's shape: head module (L3–45) importing BHL normalize/base and the two BHL components; the theme's own CSS in the code block (L195–834); a tail module (L934–936) importing `theme:tales-of-the-mosaic/code/1`, which makes the code block the delivered stylesheet; then the dusk module (L940–986) and night module (L991–1036) behind comment gates. The candidate's shape: the own CSS delivered as an inline `[[module CSS]]` at L1–646, outside the tag gate; the BHL base delivered by the frame (interwiki-style priority 1 normalize, priority 2 base, candidate L648–657) and again as direct imports inside the gated head module (candidate L660–700, the counterpart of original L3–45, BHL imports repointed to `scp-jp.github.io/Black-Highlighter`); the tail self-import module is deleted (SELF-DELIVERY block B39: original L933–936 → candidate L1590, the `[[/iftags]]` line) because the inline module replaces the channel it served; the code block survives as the source-code exhibit (candidate L859–1492, inside the translated collapsible at L858); the dusk and night modules stand at candidate L1592–1641 and L1643–1689 behind the same `[!-- {$dusk}]` / `[!-- {$night}]` comment gates, their asset URLs colon-encoded (section 4). The two CSS copies in the candidate differ by exactly one edit: measured by direct comparison, the exhibit omits the module's whole import group (module L12–22: the three original Google Fonts imports, the FIX5 annotation and the two JP imports) and is otherwise identical (similarity 0.9914, one non-equal opcode).
- Why: class P4 (delivery). The JP environment delivers a theme's own CSS from the page's module channel; a `local--code` self-import of the exhibit block is the EN page's mechanism, and keeping it would serve the exhibit copy rather than the delivered text. The variant gates are include parameters: the modules render only when an including page passes `dusk=--` / `night=--`, exactly as in the original, so the gate contents were carried, not inlined.
- Verify: `grep -n "module CSS\|\[\[code" candidate.txt` returns the module openers at L1, L660, L1594, L1645 and the single code block at L859; `grep -n "local--code" candidate.txt` returns only the two BHL component imports at L663–664 — no self-import remains. Brace depth of both candidate CSS copies and of the original code block: final depth 0, minimum 0 (measured, not counted).
- Disposition: delivery classes dispositioned in the ledger registers for row 143; no delivery item stands open. The exhibit copy's missing import group is adjudicated in the per-theme record: the omission is uniform over original and added imports alike, the delivered module carries all five, and the exhibit is a reading copy — recorded, not a defect.

## 4. Fonts and assets

- What: fonts first, because this theme's blocking item lives here. The original's stacks name Latin faces loaded by three Google Fonts imports (original code block L206–208: Hepta Slab, EB Garamond, IM Fell DW Pica SC) and the port's stacks additionally name Noto Serif JP and Noto Sans JP (candidate module L91–93: `--body-font` / `--header-font` / `--UI-font`; further stacks at candidate L181, L186, L439 — JPFONT-STACK blocks B5, B6, B11, with their exhibit-copy counterparts at candidate L938–940, L1028, L1033, L1286). Until FIX5 no import loaded either JP face: pattern 7, ledger item 32. The candidate's delivered module now carries the load at L21–22 (`family=Noto+Sans+JP:wght@400;700` and `family=Noto+Serif+JP:wght@400;700`), under the annotation comment at L16–20 (JPFONT-LOAD block B2; COMMENT-TEXT rides on the same block — the annotation is the porter's own text, section 10). Every stack-named face is loaded in the delivered channel: the three Latin faces at module L12–14 and the two JP faces at L21–22; no imported face goes unused. Assets: the theme's images stay on the EN host as original-state delivery — 20 `scp-wiki.wikidot.com/local--files` references in the candidate (the CSS body exists twice, module and exhibit, plus the dusk/night modules) against 15 in the original; the one `http://` asset URL in the original (L807, day-bg.webp) stands as `https://` in both candidate copies (L620, L1467). COLON-ENC fires 14 times: the `theme%3Atales-of-the-mosaic` encodings in asset URLs, five of them in the night module (blocks B45–B49, original L1009–1025 → candidate L1662–1678) and the rest across the two CSS copies and the license entries.
- Why: pattern 7 / KB-16 (a named JP face with no load falls back to an OS default face, the display defect item 32 charged) and KB-01 (an unencoded colon in a `local--files` path segment breaks the address). The EN-host assets are class (ii): they are the original's own attachments, re-hosted to JP storage at posting time, not in the candidate.
- Verify: `grep -n "Noto Sans JP\|Noto Serif JP" candidate.txt` — the loads at L21–22 precede every stack that names the faces (first stack at L91). `grep -c "scp-wiki.wikidot.com/local--files" candidate.txt` returns 20, and `grep -n "http://" candidate.txt` returns nothing.
- Disposition: item 32 FIXED (FIX5-FONTSA, commit 8eacd6e; supplement (a) item 32, checker code-multiset identical before/after). The asset references are the theme's T1 hotlink errors (×20), dispositioned class (ii) / KB-58 in GOSIGN2-LEDGER (b) row 143 and register (c3) P5 line.

## 5. Header, sidebar, site furniture

- What: the header variables stand in both CSS copies: `--header-title: "Tales of the Mosaic"` kept as the identity string (candidate L94, L941; original L281), `--logo-image: none` unchanged (candidate L96; original L283), and `--header-subtitle` translated — original L282 `"It's always been this way"` → candidate L95 and L942 「それはいつもこうだった」 (HEADERVAR blocks B4 and B19). The title-container markup and the tessera eyebrow/title furniture are carried translated in the body (candidate L713–724 against original L47–60). The sidebar furniture arrives through the BHL base and the toggle-sidebar-bhl component import (section 2); no sidebar markup of the theme's own changes form.
- Why: the subtitle default is a complete prose sentence, hence visible text that translates under the main chat's boundary (names, brand marks and slogans functioning as marks stay as identity strings; a sentence does not). The title is the theme's name and stays.
- Verify: `grep -n -- "--header-title\|--header-subtitle\|--logo-image" candidate.txt` returns the two copies at L94–96 and L941–943; compare original L281–283.
- Disposition: header/title language as such is out of scope under ruling 2 (ledger (c3) P9); this candidate's sentence-subtitle translation is the porter's application of the boundary, recorded here, not an item.

## 6. Text translation

- What: the documentation body is translated throughout: the usage prose, the tessera instructions, the audio collapsible (candidate L802, show/hide strings translated, against original L138), the source-code collapsible (candidate L858), and the exhibit captions. TRANSLATION-ANCHORED fires 3 times (B4 the subtitle, B26 and B32 license-entry lines); TRANS-UNANCHORED fires 18 times, concentrated in the license entries (B21–B37 region, candidate L1500–1586) where the per-file attribution lines were restructured into the JP license form, and in B19/B20 at the credit/license seams. The exhibit markup examples (the `@@`-escaped tessera samples) are carried with their prose translated and their code text intact (candidate L756–788 against original L92–124).
- Why: class P10 (translation). Reader-visible prose localizes; exhibit code text does not, because the exhibit teaches the syntax itself.
- Verify: read candidate L726–754 against original L62–90 — the usage exhibits pair line for line with only the include targets and prose changed.
- Disposition: T5 judged jointly with T4 in LOCALIZE-ROWS row 143 (FINDINGS, the one display-affecting finding being item 32's font class, section 4). No translation item stands open beyond it.

## 7. Links

- What: prose links are carried with their targets intact: the byline link to Jezixo's EN author page stands in the credit block's source field rather than the body (section 1), and the license entries' source links name the EN theme page with colon-encoded attachment paths (section 4). No prose link was repointed to a JP counterpart and none was dropped; the theme's documentation links are its attribution apparatus, covered in sections 1 and 4.
- Why: class P11's dead-reference standard: a repoint needs sameness evidence, and a link that names the original as a source is a quotation, not a navigation aid. No candidate link names a page that will not exist in a navigational role.
- Verify: `grep -n "http" candidate.txt` outside the CSS modules returns the credit source link and the license source links only.
- Disposition: no link item was charged against this theme; nothing stands open.

## 8. Structure

- What: the gate structure is preserved: the original opens `[[iftags +theme]]` at L1 and closes it at L932, with the delivery modules outside; the candidate opens `[[iftags +テーマ]]` at L658 (IFTAGS blocks B1, B19 — the tag localized, section 2's class) and closes it at L1590, with its delivered module and frame includes outside, mirroring the original's placement. The bare `[[module rate]]` the original carries inside its title container (original L48) does not stand in the candidate (the title container at candidate L713–724 holds no rate module): the preview credit block is rate-bearing, so the widget renders once, from the credit apparatus. The three EXHIBIT-RESTRUCTURE blocks adjudicate as follows. B1 (original L1–196 → candidate L1) is the differ's seam for the delivery restructure of section 3, not an exhibit change: every exhibit in that range is present in the candidate (census in section 2 and below). B20 and B38 are the license-box seams of section 1. The exhibit census: usage exhibits (candidate L735–752), tessera sample (L759–788), audio sample (L813–855 region), source-code exhibit (L859–1492), license entries — each present against its original counterpart; nothing was dropped, and the one replacement is the license apparatus form (section 1).
- Why: class R3's question — replaced or dropped, and on what ground — is answered per block above; the rate removal is the KB-09 ground (a second bare Rate beside the rate-bearing preview credit double-renders the widget).
- Verify: `grep -n -i "module rate" candidate.txt` returns only the two escaped exhibit occurrences (L761, L816); the original returns those plus the live one at L48.
- Disposition: no structure item was charged against this theme. The RESTORATION label on B19 is a classifier artifact of the same seam (this theme's FIX5 item was the font load, not a class-I restoration); adjudicated in the appendix.

## 9. Formatting only

- What: WS-ONLY fires 5 times (B7–B10, B12), single lines inside the moved CSS body whose only change is whitespace; the class summary records 0 re-indentation pairings. These lines ride inside the delivery move of section 3 and carry no content change.
- Why / Verify / Disposition: formatting-only by the classifier's normalization; spot-check any one of them in diff.md. No disposition needed.

## 10. Porter annotations

- What: two annotation sites. (1) The FIX5 font annotation at candidate L16–20 (inside the delivered module, riding on JPFONT-LOAD block B2): a Japanese-headed comment (`日本語フォント`) whose body explains, in English, that the stacks name Noto Serif JP and Noto Sans JP but no load was present, that JP glyphs fell back to an OS default, and that the faces are now loaded from Google Fonts under the SIL Open Font License with the stacks unchanged. (2) The theme's own CSS banner (candidate L2–7) is the original's banner carried unchanged ("Created by Jezixo / CC BY-SA 3.0") — the original's text, not a porter note. No other porter annotation stands in the candidate; in particular the exhibit copy carries no annotation (section 3's one-opcode difference).
- Why: an annotation is how a wave leaves its reasoning in the file the next reader opens; the font note records the pattern-7 diagnosis at the exact locus of the fix.
- Verify: read candidate L16–22.
- Disposition: annotation present and accurate against the diff; nothing stands open.

## 11. Dispositions and exceptions

- Derived presence: no derived-presence label fired for this package (the classifier's derived_presence map is empty). The standing dispositions, each re-derivable from the two sources in this package:
- The 20 EN-host `local--files` asset references (section 4): class (ii) posting rewrite, KB-58 — the original's own attachments, re-hosted when the candidate is posted; the ledger's P5 line for this theme (register (c3)) dispositions them on exactly that ground, and the T2/T3 record's "runtime-hotlink site-theme chain only" finding is the same references seen at render time.
- The escaped `:snippets:html5player` exhibit (section 2): dispositioned as a documentation example (FIX2-INCLUDE, register (c1)); the line is exhibit text in the original too.
- The sample page's 884px@768 overflow in the T2/T3 record: a classified FINDINGS entry in RENDER-ROWS-2 (RENDER-S2-D (EN20)), not charged to an item in (e); it stands as recorded render evidence, and no source change in this package's scope answers it.
- The header-subtitle translation (section 5): ruling 2 takes header/title language out of scope as a defect class; the translation stands as the porter's boundary application, not as an exception needing a disposition.

## 12. Verification

- Package integrity: `original.txt` SHA-256 equals the `review/sources.tsv` mirror hash (3587315e…) and `candidate.txt` is byte-identical to `pages/theme:tales-of-the-mosaic-jp.txt` (sha256 62f0576e…); both were verified when the package was assembled and are re-verified by `python3 review/build_review.py --check`.
- T1: baseline exit 1, 21 errors / 1 warn / 1 info (hotlink×20, foreign-include×1) [T1-ROWS row 163]; every code is dispositioned above. The FIX5 wave's own checker comparison for this file: code-multiset identical before/after (supplement (a) item 32).
- T2/T3: FINDINGS as recorded in the verdict stamp (page runtime-hotlink chain only; sample credit-modal preview-form; 884px@768 overflow) [RENDER-ROWS-2 (RENDER-S2-D (EN20))]. The credit-modal entry is the standing preview-form disposition (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2).
- T4 follow-up: the FIX5 re-derivation in the per-theme record below is the follow-up check for this theme's one display-affecting finding; it passes on the current bytes.
- Brace depth: both candidate CSS copies and the original code block scan to final depth 0 with no negative dip (section 3).

## Per-theme record — the FIX5 closure, re-derived

- The item: GOSIGN2-LEDGER (e) item 32, class [D] — "JP font named, never loaded (pattern 7)": the candidate's stacks referenced JP faces (the ledger names the stack references) with no JP font import anywhere in the file, so Japanese text fell back to an OS default face. Population row 143; the finding is LOCALIZE-S2-C's one display-affecting finding for this theme.
- The re-judgement: GOSIGN2-LEDGER-SUPPLEMENT (a) item 32 — FIXED, wave FIX5-FONTSA, commit 8eacd6e; checker code-multiset identical before/after.
- What the fix was supposed to change: add a load for the named JP faces (the settled supplement form: Noto Sans JP / Noto Serif JP from Google Fonts) without replacing any Latin family and without changing the stacks.
- Verification against the bytes: commit 8eacd6e's diff for this file is a single hunk (+8 lines) inserting the annotation comment and the two `@import` lines after the Latin imports — in current bytes, candidate L16–22 of the delivered module. The loads precede every naming stack (first at L91). The stacks themselves are unchanged in form (JPFONT-STACK blocks record the suffix state the S2 port left). The delivered channel is the module at L1–646, so the load is live on every page that includes the theme. One boundary, recorded in section 3: the source-code exhibit copy does not carry the load — it carries no imports at all, the original's three included, so the omission is the exhibit's uniform convention in this candidate and not a selective loss of the FIX5 change; a reader who copies the exhibit gets the same import-less text for the Latin faces as for the JP faces. The fix is complete in the channel that renders.
- Verdict: the supplement's account matches the bytes. FIXED stands, re-derived.

## Change set outside the two diffed files

- None inside this repository: the package diffs the candidate page only, and the theme's delivery is self-contained in that page (its base arrives through the shared BHL frame and components, which are other packages' subjects). The dusk/night variant modules are sections of the same page, inside the diff.

## Multi-wave provenance

- S2 port (LOCALIZE-S2-C): the translation, the credit swap, the delivery restructure and the JP stack suffixes.
- FIX2-INCLUDE: the foreign-include register disposition for the html5player exhibit (no file change).
- FIX5-FONTSA (commit 8eacd6e, 2026-11-17): the pattern-7 font load, section 4 — also the last change to the candidate file, which is why the verdict stamp computes against this commit and reads PASS rather than STALE.
- GOSIGN2 determination and go-sign (COMPLETION-REPORT §10, 2026-11-17): the ledger verdict the stamp records.

## Appendix — heuristic and residue adjudication

No heuristic and no residue blocks: all 49 blocks carry specific labels. Three classifier artifacts are adjudicated here so a reader does not have to re-derive them:

- B19's RESTORATION label: the block is the differ's alignment seam over the whole post-code region (original at L834 → candidate L648–1492), created by the delivery restructure. This theme has no class-I item and nothing was restored by a wave; the label does not describe a restoration. The credit, license and exhibit contents inside the seam are verified individually in sections 1, 2 and 8.
- B1's EXHIBIT-RESTRUCTURE label: same seam at the head of the file; the exhibits are all present (section 8 census).
- The topology pass's second move (code-css → candidate L660–1639 at 0.971): the matched region is the gated body containing the exhibit copy of the CSS, not a second delivery; the delivery is the single module at L1–646 (section 3).
