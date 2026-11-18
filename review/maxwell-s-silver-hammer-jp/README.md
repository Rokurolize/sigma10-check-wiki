# Review package — theme:maxwell-s-silver-hammer-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:maxwell-s-silver-hammer-jp — origin EN, population #112 [GOSIGN2-LEDGER (b) row 112]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 589f0197307cb4b69bfae2d734a4cef9ea699a508b2fd1eb7fe85526eeb3355d); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 112; GOSIGN2-LEDGER (b) row 112]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + scp-wiki.wikidot.com; sample credit-modal (preview-form) + 884px@768 overflow (one combo http.cat among hosts); T3 header logo overprints subtitle/account links at 375/320 on both pages, h1 wraps to two lines at 320. [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 112, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 112]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 112]
- Computed against: canonical commit 41048ca2b13766899b5c5d5d426a980ad00f8a04; candidate file pages/theme:maxwell-s-silver-hammer-jp.txt sha256:589f0197307cb4b69bfae2d734a4cef9ea699a508b2fd1eb7fe85526eeb3355d; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 112) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 and pseudo-ref ×1 (sections 4 and 3); the render row's items (section 11); T4's one finding is the same served-source asset set. One observation is flagged in the per-theme record, not hidden |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:maxwell-s-silver-hammer | theme:maxwell-s-silver-hammer-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 20 (first translation; the candidate's credit block records 初訳時参照リビジョン: 20) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-maxwell-s-silver-hammer.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:maxwell-s-silver-hammer-jp.txt`, byte-identical to the canonical file in its post-sweep state (the usage sweep's repair, canonical commit b5cb724, landed after this batch's snapshot; see the per-theme record) |
| Lines / bytes | 442 lines / 8,676 bytes | 448 lines / 9,654 bytes |
| SHA-256 | e5416f6a1ed909a1a4913f1aa47437a2f60e51616527e0d3298c0dad815f24ec | 89343ab073c03e249b09181a9c694f96ea8a847ff0a549e174fe6697c4e29ef3 |

Wave history: the candidate was created by the Stage 2 EN14 integration (commit 49c7627) and has exactly one later commit, 1869877, the FIX-CREDIT-D wave's translator-attribution normalization. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A standard mechanical port of a self-contained EN theme. The original delivers its CSS through a head module and an interwiki-style frame (its `theme=` parameter, unusually, names a `/code/1` page URL rather than a local--code address), carries a bare Rate module and prose-only attribution, and presents its full CSS in one code exhibit. The candidate swaps the Rate for the JP preview credit block, repoints the delivery frame and every include to the JP side, moves the font load from fonts.bunny.net to the same family's Google Fonts form with Noto Sans JP added, appends the JP family to every font stack, colon-encodes the kept EN-storage asset URLs, and translates the exhibit body, the CSS comments, and the header's rendered title string. It also repairs three missing semicolons in the original's CSS, one of which changes what the original's own rules compute (section 8). Measured churn (diff.md, the generator's difflib count with autojunk off: +93/−92, 185 changed lines in 63 change blocks / 18 hunks; a GNU-diff count of the same pair gives 158 changed lines — the difference is alignment choice, not content). One observation is carried openly in the per-theme record: the usage example's self-reference named the theme by its plain slug on the JP side until the population sweep repaired the include line after the verdict (the link sample beside it still names the plain form).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 63 change blocks — 42 specific (66.7%), 20 heuristic (31.7%), 1 residue (1.6%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 19 |
| WS-ONLY | 18 |
| COMMENT-TEXT | 10 |
| JPFONT-STACK | 7 |
| TRANSLATION-ANCHORED | 6 |
| CSS-BODY | 5 |
| COLON-ENC | 2 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| ESCAPED-INCLUDE | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 5 CSS-BODY blocks are not churn — B29, B60, and B61 are missing-semicolon repairs in the original's CSS (section 8), and B62/B63 are the code exhibit's closing pair reordered around the added collapsible (section 8); the 2 EXHIBIT-RESTRUCTURE primaries are include repoints (sections 2 and 3); the single residue block (B21) is a banner-comment translation whose two lines are mostly URLs (section 6); the 2 COLON-ENC blocks are the kept asset URLs' colon-encoding (section 4); the COMMENT-TEXT and code-exhibit TRANS-UNANCHORED mass is CSS comment translation, resolved in section 6 by shape. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:maxwell-s-silver-hammer-jp; original theme:maxwell-s-silver-hammer on scp-wiki at reference revision 20; candidate `pages/theme:maxwell-s-silver-hammer-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN14 wave (sources.tsv kind: standard; no production JP counterpart is recorded for this theme, so the R4 adoption question does not arise). The frame order is the original's own: delivery module and interwiki-style include first (original L1–7), then the tag gate; the candidate keeps that order with the gate's tag localized (section 2) and two blank lines around the head tightened (section 9).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate is P2, the frame is P4/P6 (section 3).
- **Verify:** The sources.tsv row for maxwell-s-silver-hammer-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a right-aligned div under a "Rating:" label (original L15–18), and nothing else: there is no info pair and no license box; the attribution lives in the intro prose ("made by [[*user c_bonefish]] and [[*user Denevola]]", original L20) and in the CSS banner ("Created by c_bonefish & Denevola", with the adopted-code credits to thd-glasses and EstrellaYoshte). The candidate deletes the Rate (block B7) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L13–22) carrying the eight ruling-3 fields (title Maxwell's Silver Hammer CSSテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Maxwell's Silver Hammer CSS Theme; 著作権者 c_bonefish, Denevola; 作成年 2021; 初訳時参照リビジョン 20; the source link, section 7). The field names both creators, matching the original's prose and banner — no name the original credits is dropped. The translator field took its ruling-3 form in 1869877 (FIX-CREDIT-D). The intro prose and banner are retained, translated (sections 6), so the adopted-code credits survive in the candidate as well. No T7 credit-CSS supplement was needed: the theme's own rate-module CSS is carried unchanged in that region.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L13–22 against the eight fields; `grep -n 'c_bonefish' candidate.txt` shows the field, the prose, and the banner.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Two repoint blocks, and no other include change. B2: the interwiki-style include, `:scp-wiki:component:interwiki-style` → `:scp-jp:component:interwiki-style` (original L4 → candidate L4; its theme= parameter is section 3). B11: the image-block exhibit's include, `component:image-block` → `:scp-jp:component:image-block` (original L30 → candidate L34; its asset host is section 4 and its caption translation is section 6). The credit includes (section 1) complete the candidate's live include list; every live include in the candidate names a `:scp-jp:` target. The usage example's include is exhibit text and is treated in section 7.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; a kept `:scp-wiki:` include is a foreign-include error, class (i), and both targets have verified JP counterparts, so both are repointed and none is kept as an exception. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — four live includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original self-delivers: a head `[[module CSS]]` importing its own `local--code/theme%3Amaxwell-s-silver-hammer/1` from scp-wiki.wdfiles.com (original L2), and the interwiki-style include at priority 1 whose `theme=` names `https://scp-wiki.wikidot.com/theme:maxwell-s-silver-hammer/code/1` (original L4–7), the original's own code-page URL rather than a local--code address. The candidate keeps the same two-part frame and repoints it to the candidate's own delivery on the draft host: the module imports `local--code/theme%3Amaxwell-s-silver-hammer-jp/1` from sigma10-jp-test.wdfiles.com (candidate L2), and the include's `theme=` names the same draft-host URL (candidate L6), so the two halves of the frame agree in the candidate where the original's named different forms of the same delivery. The candidate's `theme= ` value carries a leading space the original's does not, a variant this file shares with 50 of the 286 candidates (236 carry the unspaced form), with no unstyled-content finding in this theme's render record. The original already carried the interwiki-style frame, so this theme is M-pure, not M-frame. The T1 pseudo-ref error is the head import line.
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame form, priority 1 for the theme's own layer). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code\|theme=' candidate.txt` — candidate L2 and L6, both draft-host; compare the sibling heads in `pages/`.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii); the production-host rewrite at posting is class (ii) mechanics).

### 4. Fonts and assets

- **What:** Load (block B22): the original loads Titillium Web from fonts.bunny.net (original L70); the candidate loads the same family from Google Fonts and adds Noto Sans JP in the same import (candidate L75: `family=Titillium+Web&family=Noto+Sans+JP`). Stacks: all seven `font-family` lines in the theme's own CSS name `'Titillium Web'` first and gain `'Noto Sans JP'` after it (B25, B32, B34, B35, B36, B41, B42 — the JPFONT-STACK blocks); no stack names a family that nothing loads. Assets: the theme's three images stay on EN storage under `scp-wiki.wikidot.com/local--files/theme:maxwell-s-silver-hammer/` — `background.png` (candidate L80's zone), `logo.png` (candidate L144's zone), and `logo-2.png` (the image-block exhibit's `name=`, candidate L34) — with the colon in the page name percent-encoded by the port (blocks B24, B30: `theme:maxwell-s-silver-hammer` → `theme%3Amaxwell-s-silver-hammer` in the URL path). These kept lines are T1's three hotlink errors and T4's one finding (LOCALIZE-ROWS row 112: "P5 (a,b EN-storage assets, display-affecting)").
- **Why:** P7/T5 with KB-16 (the font load gap): Titillium Web has no kana glyphs, so the load gains the JP family and every stack names it; the load's host change follows the family's canonical webfont form, as in the mcf package's Quantico case. P5: assets that serve from their recorded source are dispositioned class (ii) (re-hosting is a posting-procedure matter); the colon-encoding is the wave's URL-form normalization and does not change which file is named.
- **Verify:** `grep -n 'font-family\|@import' candidate.txt` — the load at L75 and seven stack lines, all as listed; `grep -n 'local--files' candidate.txt` returns exactly the three kept asset lines.
- **Disposition:** Font load and stacks applied; the kept EN-storage lines DISPOSITIONED (class (ii), served source).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header title is a CSS `content:` string, and it is translated: `content: "Maxwellism"` (original L98) → `content: "マクスウェリズム"` (candidate L103, block B27, the CONTENT-STRING block). The theme overrides no `--header-*` variables on either side; its header geometry (the 155px logo, the 60px title) is the original's, carried unmodified except for the semicolon repair of section 8 and the font lines of section 4. The sidebar and top-bar rules are carried over apart from those font lines and the comment translations of section 6; no P8 layout adaptation was needed.
- **Why:** P9/T6 for the string itself; the value is reader-visible header text, so its translation is P10/KB-18 carried in a string (the reader-visible half of R1). Ruling 2 is not engaged: the string was translated, not kept in the original's language.
- **Verify:** `grep -n 'content:' candidate.txt` — the header title line reads マクスウェリズム; `grep -n -- '--header-' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The exhibit body is translated throughout, in counted groups. Six TRANSLATION-ANCHORED blocks (B10: the "Page Elements" heading; B11's companion lines: the heading samples 見出し1–6; B12: the tabview's tabs and link samples; B13: the footnote sample; B17) and the body-prose TRANS-UNANCHORED blocks (B8: the intro paragraph, including the Maxwellism hub link's text; B14–B16: exhibit strings). The code-exhibit mass resolves by shape in one appendix group: the 10 COMMENT-TEXT blocks plus the comment-bearing TRANS-UNANCHORED blocks are CSS comment translations — the banner comment (candidate L58–67 zone: the creation credit, the two adopted-code credits, and the two background-image source lines, whose pixabay URLs are carried unchanged because they are the attribution record, not loads) and the section comments (ヘッダー, ログイン・検索・トップバー, ページ要素, サイドバー, 評価モジュール, タブ, 引用ブロック, その他). The single residue block (B21) is the banner's two background-image lines and is counted here, not in the appendix. No English reader-visible text remains in the candidate outside proper names and the credit block's title fields, which quote the work's name.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`). CSS comments are the theme's own documentation of its sections and were translated as a class; they are counted here so the mass is explained, not waved through.
- **Verify:** The pairs are diff.md's hunks in order; `grep -n '/\*' candidate.txt` returns only Japanese comments and the banner.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains.

### 7. Links

- **What:** Two live links, both correct as written. The credit block's source link (candidate L21) names `https://scp-wiki.wikidot.com/theme:maxwell-s-silver-hammer`, the original's recorded host in sources.tsv, and serves the original — no probe discrepancy, no defect. The intro prose's hub link is repointed from the EN hub to its JP counterpart (`https://scp-jp.wikidot.com/church-of-the-broken-god-hub`, candidate L24's zone), with its label translated. The two exhibit links are sample text: the usage example's include (candidate L28), which now reads `:scp-jp:theme:maxwell-s-silver-hammer-jp` after the population sweep's post-verdict repair, and the link sample's `[[[theme:maxwell-s-silver-hammer|訪問済みリンク]]]` (candidate L48), which still names the theme by its plain slug on the JP side — the per-theme record's item.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; both live links satisfy it. An exhibit that documents the theme's own include must name the page a user would actually paste — that is the flag's ground, argued in the per-theme record.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the hub link are the only hits.
- **Disposition:** Live links standing; the exhibit name form is flagged in the per-theme record.

### 8. Structure

- **What:** The localize.md closing rule holds, with three in-place CSS repairs that are this theme's only semantic CSS edits. An exhibit census confirms the shape: the tabview and its two tabs, the link and footnote samples, the heading samples, the image-block div, and the code exhibit are present on both sides in the same order. The code exhibit is wrapped in a `[[collapsible]]` with Japanese show/hide labels (opening at candidate L58's zone — block B18 — and the closing pair at the file's end, blocks B62/B63: the candidate ends `[[/code]]` then `[[/collapsible]]`, so the collapsible opened before the code block closes after it). The repairs (CSS-BODY primaries): B29 — `background-size: 155px` gains its missing semicolon (candidate L139), and this one is behavioral: in the original the unterminated declaration runs into the following `flex: 1;` line, so the original's own rule does not compute as written; B60 and B61 — the same missing semicolon at the two `box-shadow: 0 0 11px white` lines of the neon keyframes (candidate L434, L441), where the declaration is last in its block, so the repair is normalization with no behavioral change. The classifier's two EXHIBIT-RESTRUCTURE primaries adjudicate to include repoints (sections 2 and 3), not exhibit changes.
- **Why:** R3 forces the restructure-vs-deletion adjudication; here the census decides, and the only remaining CSS-BODY mass is the three repairs, which are R6 in-place corrections of the original's own syntax, recorded here rather than hidden inside a "carried over" claim. The collapsible wrap is a presentation supplement: it changes how the exhibit displays, not what the theme delivers.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include\|\[\[collapsible' original.txt candidate.txt`; read candidate L139, L434, L441 against original L134, L429, L436.
- **Disposition:** Standing; no structural deletion, no class I item; the three repairs recorded.

### 9. Formatting only

- **What:** Eighteen WS-ONLY blocks, every one a blank line inside the code exhibit that carried a trailing space on the original side and loses it on the candidate side (`" \n"` → `"\n"`), plus the blank-line tightening around the head frame (inside B2 and B4). The classifier finds no re-indentation anywhere (0 blocks pair up after leading-whitespace normalization), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change, and so a reviewer can skip it safely.
- **Verify:** The WS-ONLY blocks are listed in classification.json; each pair differs only in the trailing space.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate carries no porter-added comment: every comment in the file is the original's own, translated (section 6), and there is no provenance comment of the kind some sibling candidates carry at the head of their code block. The only added text is functional: the credit block (section 1) and the collapsible's show/hide labels (section 8). This section was checked explicitly against the candidate's comment lines rather than taken from the skeleton's "none".
- **Why:** R2: porter-added text is part of the change record; here the record is that there is none.
- **Verify:** `grep -n '/\*' candidate.txt` — all hits are the translated comments of section 6.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's three hotlink errors: the kept EN-storage asset lines of section 4, all live and serving from the recorded source; class (ii), posting-procedure re-hosting, and the same lines are T4's one finding, judged served-source in LOCALIZE-ROWS row 112. (2) T1's one pseudo-ref error: the candidate's own draft-host local--code import (section 3); class (iii), sanctioned at draft stage. (3) The render row's items: the page's runtime-hotlink site-theme chain plus a scp-wiki.wikidot.com host in the chain (KB-40, environment layer); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); the sample's 884px@768 overflow reading, taken in a combo whose hosts include http.cat (a transient capture host, KB-44 family); and the T3 header reading — the header logo overprints the subtitle and account links at 375/320 widths on both pages and the h1 wraps to two lines at 320. The header item is recorded as the row records it: the port carries the original's header geometry unmodified in that region (sections 5 and 8), the ledger carried the row into this theme's PASS determination without charging a fix, and this package does not re-open that determination. The per-theme record's item below is a flag, not a disposition: it has no ledger ground, and this package does not invent one.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the per-theme record's item flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 112): exit 1, 4 errors / 1 warn / 1 info; the errors are hotlink ×3 and pseudo-ref ×1, all in the standing classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN14)): FINDINGS, the items of section 11(3), all dispositioned there. (c) T4/T5 (LOCALIZE-ROWS row 112): FINDINGS jointly, display-affecting findings 1 — the served-source asset set of section 4 — and the row records no unincorporated upstream updates. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +93/−92 in 63 change blocks / 18 hunks; the GNU-diff count of the same pair is 158 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:maxwell-s-silver-hammer-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 112; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's self-reference (repaired after the verdict; the link sample still names the plain slug)

At this batch's snapshot the candidate's usage example (candidate L28) read `@@[[include :scp-jp:theme:maxwell-s-silver-hammer]]@@`: the wiki prefix had been repointed from the original's `:scp-wiki:` form, but the page name kept the original's plain slug, and this candidate's posting name is theme:maxwell-s-silver-hammer-jp, so the example named a page that will not exist on scp-jp. The population sweep that the earlier batches' flags of this same shape set in motion repaired the line after the ledger determination (canonical commit b5cb724, a single -jp insertion on the line); this package is built against the repaired candidate, whose L28 now reads `:scp-jp:theme:maxwell-s-silver-hammer-jp`. One member of the shape survives the sweep: the link sample (candidate L48) still links `[[[theme:maxwell-s-silver-hammer|訪問済みリンク]]]`, a relative-link syntax sample outside the sweep's `:scp-jp:theme:` token scope, recorded here for the coordinator's judgment. The ledger's determination for this theme is PASS and this package does not re-open it.

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:maxwell-s-silver-hammer-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FONTS7 item 3 — link-exhibit sample posting name (landing `41048ca2b13766899b5c5d5d426a980ad00f8a04`, "pages: larue and laughter font loads, two exhibit samples", 2026-11-17; record `FIX-FONTS7.md`).** +1/−1. L48 link-styling exhibit sample `[[[theme:maxwell-s-silver-hammer|訪問済みリンク]]]` → `[[[theme:maxwell-s-silver-hammer-jp|訪問済みリンク]]]`, the `-jp` posting name, with the label and all other text unchanged. Checker 4/1/1 unchanged; the single `link-target-missing` warning now names the `-jp` posting name and persists until posting; class (i) 0.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-maxwell-s-silver-hammer-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Maxwell's Silver Hammer CSS Theme
- **Author:** c_bonefish, Denevola
- **Source:** https://scp-wiki.wikidot.com/theme:maxwell-s-silver-hammer — revision 20
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
