# Review package — theme:mcf-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:mcf-jp — origin EN, population #113 [GOSIGN2-LEDGER (b) row 113]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now b5a5692934a7bb21445105384b4fadd6f589ff17b602ea2d735cafc8258a8076); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 0 infos (hotlink×4, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 113; GOSIGN2-LEDGER (b) row 113]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow (one combo http.cat among hosts); T3 clean on both pages. [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 113, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 113]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 113]
- Computed against: canonical commit 41048ca2b13766899b5c5d5d426a980ad00f8a04; candidate file pages/theme:mcf-jp.txt sha256:b5a5692934a7bb21445105384b4fadd6f589ff17b602ea2d735cafc8258a8076; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 113) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×4 and pseudo-ref ×1 (sections 4 and 3); the render row's items (section 11); T4's two findings are the same served-source lines, dispositioned with them. Two observations are flagged in the per-theme record, not hidden |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:mcf | theme:mcf-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 15 (first translation; the candidate's credit block records 初訳時参照リビジョン: 15) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-mcf.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:mcf-jp.txt`, byte-identical to the canonical file in its post-sweep state (the usage sweep's repair, canonical commit b5cb724, landed after this batch's snapshot; see the per-theme record) |
| Lines / bytes | 348 lines / 6,863 bytes | 348 lines / 7,824 bytes |
| SHA-256 | 81cd666319bf401d140955e8fd04a969d090de2729bc85745226f5a532da38aa | 0bd990b5fbb41820a19d26d6484cead09947d38c4355c23fb06150a1bdb2ec19 |

Wave history: the candidate was created by the Stage 2 EN14 integration (commit 49c7627) and has exactly one later commit, f1138e4, whose mcf hunk is a one-line credit-field correction (the translator field taking its ruling-3 form, section 1). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A standard mechanical port. The original is a self-contained EN theme page: it self-delivers its CSS through a head module and an interwiki-style frame, carries a bare Rate module, an info pair, and a placeholder info body for credit, and presents its full CSS in one code exhibit. The candidate swaps the credit furniture for the JP preview credit block, repoints the delivery frame and every include to the JP side, replaces one self-hosted font load with the same family's Google Fonts form while keeping the other (a served EN-storage source, dispositioned), appends JP families to the font stacks, and translates the exhibit body and every CSS comment. Measured churn (diff.md, the generator's difflib count with autojunk off: +76/−76, 152 changed lines in 41 change blocks / 14 hunks; a GNU-diff count of the same pair gives 144 changed lines, +72/−72 — the difference is alignment choice, not content). Two observations are carried openly in the per-theme record: the usage example's self-reference named the theme by its plain slug on the JP side until the population sweep repaired the include line after the verdict (the link sample beside it still names the plain form), and the credit block's author field names the restoring author alone while the theme's own banner credits the 2014 creator as well (the banner itself is retained, translated, in the candidate).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 41 change blocks — 19 specific (46.3%), 19 heuristic (46.3%), 3 residue (7.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 18 |
| COMMENT-TEXT | 13 |
| WS-ONLY | 7 |
| TRANSLATION-ANCHORED | 3 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| JPFONT-STACK | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| INFO-DEL | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 13 COMMENT-TEXT blocks and the code-exhibit TRANS-UNANCHORED blocks are CSS comment translations, resolved in section 6 by shape; B25 and B29 (CSS-BODY) are P7 font-stack rewrites (section 4); B30 (CSS-BODY) is a selector supplement for the JP sidebar/interwiki markup (section 5); the 2 EXHIBIT-RESTRUCTURE primaries are include repoints, not exhibit changes (sections 2 and 3); the 3 residue blocks resolve as a trailing-space blank line inside the code exhibit (B15, section 9), a CSS comment translation (B20, section 6), and the closing tag of the collapsible wrapped around the code exhibit (B41, section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:mcf-jp; original theme:mcf on scp-wiki at reference revision 15; candidate `pages/theme:mcf-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN14 wave (sources.tsv kind: standard; no production JP counterpart is recorded for this theme, so the R4 adoption question does not arise). The frame order is the original's own: delivery module and interwiki-style include first (original L1–7), then the tag gate (original L10); the candidate keeps that order (candidate L1–9) with the gate's tag localized (section 2).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate is P2, the frame is P4/P6 (section 3).
- **Verify:** The sources.tsv row for mcf-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a right-aligned div under a "Rating:" label (original L11–15), a second div headed "Rating w/ Info Pane:" (original L17–19), and an `:scp-wiki:info:start`/`end` pair whose body is the placeholder text "Info about your page." (original L21–27). The candidate deletes all three (blocks B5, B7) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L11–20) carrying the eight ruling-3 fields (title Manna Charitable Foundation Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Manna Charitable Foundation Theme; 著作権者 stormbreath; 作成年 2020; 初訳時参照リビジョン 15; the source link, section 7). The translator field took its ruling-3 form in f1138e4, the file's only post-creation commit. There is no T7 credit-CSS supplement: the theme's own "Credit Rating Module" CSS section is carried over with its selectors unchanged (its `.creditButton p a` rule is the original's own styling, not a restatement for the JP module). One value-level observation is recorded in the per-theme record: the banner comment the candidate retains (candidate L55–59) credits Reach as the theme's 2014 creator and Stormbreath and UncleNicolini as its restorers, while the field names stormbreath alone.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the info pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'info:start\|info:end\|module Rate' candidate.txt` returns nothing; read candidate L11–20 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified). The author-field observation is flagged in the per-theme record; T4's row for this theme charges nothing on the field.

### 2. Includes and components

- **What:** Two repoint blocks, and no other include change. B2: the interwiki-style include, `:scp-wiki:component:interwiki-style` → `:scp-jp:component:interwiki-style` (original L4 → candidate L3; its theme= parameter is section 3). B8: the image-block exhibit's include, `component:image-block` → `:scp-jp:component:image-block` (original L30 → candidate L27; its asset host is section 4 and its caption translation is section 6). The credit includes (section 1) complete the candidate's live include list; every live include in the candidate names a `:scp-jp:` target. The usage example's include is exhibit text and is treated in section 7.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; a kept `:scp-wiki:` include is a foreign-include error, class (i), and both targets have verified JP counterparts, so both are repointed and none is kept as an exception. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — four live includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original self-delivers: a head `[[module CSS]]` importing its own `local--code/theme%3Amcf/1` from scp-wiki.wdfiles.com (original L2), and the interwiki-style include at priority 1 whose `theme=` names the same delivery (original L4–7). The candidate keeps the same two-part frame and repoints it: the module (now `[[module css]]`) imports `local--code/theme%3Amcf-jp/1` from the draft host sigma10-jp-test.wdfiles.com (candidate L2), and the include's `theme=` names the same draft-host URL (candidate L6). Two form notes, both verified against the population: the original already carried the interwiki-style frame, so this theme is M-pure, not M-frame — the port repoints the frame, it does not add it; and the candidate's `theme= ` value carries a leading space the original's does not, a variant this file shares with 50 of the 286 candidates (236 carry the unspaced form), with no unstyled-content finding in this theme's render record. The T1 pseudo-ref error is the head import line.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame form, priority 1 for the theme's own layer). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L2 and L6, both draft-host; compare the sibling heads in `pages/`.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii); the production-host rewrite at posting is class (ii) mechanics).

### 4. Fonts and assets

- **What:** Loads (block B13): the original's code exhibit opens with two self-hosted font loads from EN storage, `quantico.css` and `sansation.css` under `local--files/theme%3Amcf/` (original L52–53). The candidate replaces the Quantico load with the same family's Google Fonts form (`family=Quantico:ital,wght@0,400;0,700;1,400;1,700`, candidate L49) and keeps the Sansation load on scp-wiki.wdfiles.com unchanged (candidate L50). Stacks: the two `quanticoregular` stacks become `'Quantico'` plus the JP families (B25, candidate L151; B29, candidate L172 — CSS-BODY primaries adjudicated here as P7 rewrites), and the two `sansationregular` stacks keep their first family and append `'Noto Sans JP', 'Yu Gothic', 'Hiragino Kaku Gothic ProN'` (B16, candidate L64; B17, candidate L70). No stack names a family that nothing loads: Quantico loads from Google Fonts, Sansation from the kept EN-storage CSS. Assets: the theme's two images stay on EN storage — `body_bg_MCF2.png` (candidate L92's zone) and `MCF-4.png` (the header background and the image-block exhibit's `name=`, candidate L27) — all under `scp-wiki.wdfiles.com/local--files/theme%3Amcf/`, live and serving. These kept lines are T1's four hotlink errors and T4's two findings (LOCALIZE-ROWS row 113: "(a) P4 Sansation CSS import from EN storage (served source); (b) P5 live + served EN-storage assets").
- **Why:** P7/T5 with KB-16 (the font load gap): the Latin faces have no kana glyphs, so every stack gains a JP family; the Quantico load changes host because the family is a standard Google Fonts face and the port names it in its canonical form in both load and stacks. P5: assets that serve from their recorded source are dispositioned class (ii) (re-hosting is a posting-procedure matter), not edited in the candidate.
- **Verify:** `grep -n 'font-family\|@import' candidate.txt` — the loads at L49–50 and four stack lines, all as listed; `grep -n 'wdfiles' candidate.txt` returns exactly the kept EN-storage lines.
- **Disposition:** Font loads and stacks applied; the kept EN-storage lines DISPOSITIONED (class (ii), served source).

### 5. Header, sidebar, and site furniture

- **What:** The theme overrides no header variables on either side (no `--header-title`, `--header-subtitle`, or `--logo-image` in the candidate); its header is the MCF-4.png background of section 4. One supplement lands here (block B30, a CSS-BODY primary): the hue-rotate filter rule's selector list grows from `#interwiki .menu-item img` (original L205) to `#interwiki .menu-item img, #interwiki .menu-item > .image, #side-bar .side-block .menu-item > .image` (candidate L203). The sidebar and top-bar font lines are section 4's stack changes; no P8 layout adaptation was needed.
- **Why:** The JP site furniture renders sidebar and interwiki menu icons as `.image` elements where the EN original's markup used `img`; without the two added selectors the theme's icon filter would silently miss them on the JP side. The rule's declarations are unchanged.
- **Verify:** Read candidate L203 against original L205; the declarations below them are byte-identical.
- **Disposition:** Standing (supplement argued from the JP markup form).

### 6. Text translation

- **What:** The exhibit body is translated throughout, in counted groups. Three TRANSLATION-ANCHORED blocks (B9: the "+ Header" sample heading → "+ ヘッダー"; B11 and B12: the tabview's tab titles and bodies). The body-prose TRANS-UNANCHORED blocks are B6 (the intro paragraph: the theme's purpose and the paste instruction) and B10 (the link sample's labels, 未訪問リンク / 訪問済みリンク). Everything else in this section's mass sits inside the code exhibit and resolves by shape in one appendix group: the 13 COMMENT-TEXT blocks plus the comment-bearing TRANS-UNANCHORED blocks are CSS comment translations — the banner comment (B14, candidate L55–59: the theme's name, its 2014/2020 history, and its thanks, with all personal names carried unchanged) and the section comments (共通, 全体幅, ヘッダー, トップメニュー, サイドメニュー, YUIタブ, フッター, 装飾ボックス, カスタムページ本文クラス, ページ評価モジュールのカスタマイズ, クレジット付き評価モジュール, 標準画像ブロック, モバイル用メディアクエリ, and the two inline YUI-tab notes). Residue block B20 (全体幅) is the same shape and is counted here, not in the appendix. No English reader-visible text remains in the candidate outside proper names and the credit block's title fields, which quote the work's name.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). CSS comments are not reader-visible, but they are the theme's own documentation of its sections, and the wave translated them as a class; they are counted here so the mass is explained, not waved through.
- **Verify:** The pairs are diff.md's hunks in order; `grep -n '/\*' candidate.txt` returns only Japanese comments and the banner.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L19): `https://scp-wiki.wikidot.com/theme:mcf`, whose host is the original's recorded host in sources.tsv and which serves the original — no probe discrepancy, no defect. The two exhibit links are sample text: the usage example's include (candidate L24), which now reads `:scp-jp:theme:mcf-jp` after the population sweep's post-verdict repair, and the link sample's `[[[theme:mcf|訪問済みリンク]]]` (candidate L38), which still names the theme by its plain slug on the JP side — the per-theme record's first item. No prose link in the candidate targets an EN-wiki page.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; the source link satisfies it as written. Exhibit placeholders follow P10 for their text, but an exhibit that documents the theme's own include must name the page a user would actually paste — that is the flag's ground, argued in the per-theme record.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Source link standing; the exhibit name form is flagged in the per-theme record.

### 8. Structure

- **What:** The localize.md closing rule holds. Variable names, selectors, and channel order are preserved; the candidate's single code exhibit sits where the original's sits, and an exhibit census confirms the shape: the tabview and its two tabs, the link sample, the header sample, the image-block div, and the code exhibit are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise for the exhibits themselves. Two form changes ride on the exhibit: the code exhibit is wrapped in a `[[collapsible]]` with Japanese show/hide labels (candidate L48, closed at candidate L346–347; blocks B13 and B41), and its code type is lowercased (`CSS` → `css`). The classifier's two EXHIBIT-RESTRUCTURE primaries adjudicate elsewhere: B2 is the interwiki include repoint (section 2) with a blank-line deletion (section 9), and B8 is the image-block include repoint (section 2). The JP corrections arrive at the head (sections 1–3) and inside the inherited CSS only as the stack and selector changes of sections 4–5.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides. The collapsible wrap is a presentation supplement: it changes how the exhibit is displayed on the theme page, not what the theme delivers.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include\|\[\[collapsible' original.txt candidate.txt` — the sequences correspond, with the collapsible as the only addition.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Seven WS-ONLY blocks (B18, B19, B22, B23, B26, B27, B40) plus residue block B15: every one is a blank line inside the code exhibit that carried a trailing space on the original side and loses it on the candidate side (`" \n"` → `"\n"`), at section boundaries of the CSS. The same trailing-space removal rides inside several translation blocks of section 6. The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered. One further deletion of the same family is the blank line between the delivery module and the interwiki include (inside B2).
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The WS-ONLY blocks are listed in classification.json; each pair differs only in the trailing space.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no porter-added comment: every comment in the file is the original's own, translated (section 6), and there is no provenance comment of the kind some sibling candidates carry at the head of their code block. The only added text is functional: the credit block (section 1) and the collapsible's show/hide labels (section 8). This section was checked explicitly against the candidate's comment lines rather than taken from the skeleton's "none".
- **Why:** R2: porter-added text is part of the change record; here the record is that there is none.
- **Verify:** `grep -n '/\*' candidate.txt` — all hits are the translated comments of section 6.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four hotlink errors: the kept EN-storage lines of section 4 (the Sansation font load and the theme's two images, one of which appears twice), all live and serving from the recorded source; class (ii), posting-procedure re-hosting, and the same lines are T4's two findings, judged served-source in LOCALIZE-ROWS row 113. (2) T1's one pseudo-ref error: the candidate's own draft-host local--code import (section 3); class (iii), sanctioned at draft stage. (3) The render row's items, all environment or capture layer, not charged to the candidate: the page's runtime-hotlink site-theme chain (KB-40); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the sample's 884px@768 overflow reading, taken in a combo whose hosts include http.cat (a transient capture host, KB-44 family). T3 is clean on both pages. The two per-theme record items below are flags, not dispositions: neither has a ledger ground, and this package does not invent one.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the per-theme record's two items flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 113): exit 1, 5 errors / 1 warn / 0 infos; the errors are hotlink ×4 and pseudo-ref ×1, all in the standing classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN14)): FINDINGS, the items of section 11(3), all dispositioned; T3 clean on both pages; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 113): FINDINGS jointly, display-affecting findings 2 — the served-source font import and assets of section 4 — and the row records no unincorporated upstream updates. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +76/−76 in 41 change blocks / 14 hunks; the GNU-diff count of the same pair is 144 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:mcf-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 113; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's self-reference (repaired after the verdict; the link sample still names the plain slug)

At this batch's snapshot the candidate's usage example (candidate L24) read `> @@[[include :scp-jp:theme:mcf]]@@`: the wiki prefix had been repointed from the original's `:scp-wiki:` form, but the page name kept the original's plain slug, and this candidate's posting name is theme:mcf-jp, so the example named a page that will not exist on scp-jp. The population sweep that the earlier batches' flags of this same shape (five themes in M-pure-3, two in M-frame-1) set in motion repaired the line after the ledger determination (canonical commit b5cb724, a single -jp insertion on the line); this package is built against the repaired candidate, whose L24 now reads `:scp-jp:theme:mcf-jp`. One member of the shape survives the sweep: the link sample (candidate L38) still links `[[[theme:mcf|訪問済みリンク]]]`, a relative-link syntax sample outside the sweep's `:scp-jp:theme:` token scope. It is recorded here for the coordinator's judgment — as a visited-link styling sample, its target's existence is part of what it demonstrates. The ledger's determination for this theme is PASS and this package does not re-open it.

### The credit author field and the banner's creator (observation)

The credit block's 著作権者 field names stormbreath (candidate L16). The theme's own banner comment, retained translated at candidate L55–59, records a longer attribution: the theme was "Originally created for the SCP Foundation GoI Contest of 2014 ... by Reach", with thanks to Aelanna and Crayne, and was "Brought back by Stormbreath and UncleNicolini". The original's credit furniture (the info pair) names no author at all — its body is placeholder text — so there is no original field value to compare against; the banner is the only attribution the original carries, and it survives in full in the candidate. T4's row for this theme (LOCALIZE-ROWS row 113) records two findings, both served-source lines, and charges nothing on the field. This package therefore records the difference between the field's single name and the banner's three, with both texts, and flags it for the coordinator's judgment rather than asserting a defect the campaign's own checker did not charge.

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:mcf-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FONTS7 item 3 — link-exhibit sample posting name (landing `41048ca2b13766899b5c5d5d426a980ad00f8a04`, "pages: larue and laughter font loads, two exhibit samples", 2026-11-17; record `FIX-FONTS7.md`).** +1/−1. L38 link-styling exhibit sample `[[[theme:mcf|訪問済みリンク]]]` → `[[[theme:mcf-jp|訪問済みリンク]]]`, the `-jp` posting name (the plain name does not exist on the JP site). This is the surviving sub-form of the usage sweep: that sweep's scope was `:scp-jp:theme:` token references, not relative `[[[theme:<slug>|…]]]` samples. Checker 5/1/0 unchanged; the single `link-target-missing` warning now names `theme:mcf-jp` and persists until posting; class (i) 0.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-mcf-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Manna Charitable Foundation Theme
- **Author:** stormbreath
- **Source:** https://scp-wiki.wikidot.com/theme:mcf — revision 15
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
