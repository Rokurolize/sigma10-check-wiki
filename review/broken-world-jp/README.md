# Review package — theme:broken-world-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:broken-world-jp — origin CN, population #172 [GOSIGN2-LEDGER (b) row 172]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 3f81a42331723ef836e7dce3cbb3235c6ed17ae9266fe223eb287f5ba46ee690); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 14 errors / 4 warns / 2 infos (pseudo-ref×13, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 197; GOSIGN2-LEDGER (b) row 172]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — `hidden-interwiki` on all 8 combos on both pages (translation module hidden, theme-level; T3: explicitly documented in the page text as an original quirk), page-overflow 374px@320 + 425px@375 + 810px@768 chromium and 450px@320 + 478px@375 webkit, runtime-hotlink site-theme chain only; sample adds credit-modal (preview-form); T3 complete in the final report (pending in the partial), no further finding (desktop sidebar collapsed with no visible reopen tab, mobile hamburger opens in both engines; low-contrast credit title and 404 logos intended/deferred). [RENDER-ROWS-RERUN16 (CN3) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN3)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 171, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 171]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 172]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:broken-world-jp.txt sha256:3f81a42331723ef836e7dce3cbb3235c6ed17ae9266fe223eb287f5ba46ee690; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 172) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×13 and hotlink ×1 (class (ii), section 11); the re-run render row's items (the hidden-interwiki quirk documented in the page itself as the original's, the overflow readings, the sample's credit-modal preview form, section 11); T4's two display-affecting items, of which the EN-fragment import is **FIXED in the current bytes** by the FIX-P4 repoint (section 3) and the Chinese gallery caption stands as recorded (section 6) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:broken-world | theme:broken-world-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 306 (first translation; the candidate's credit block records 初訳時参照リビジョン: 306) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs2-cn3/CACHE/orig/broken-world.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:broken-world-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 2,125 lines / 48,264 bytes | 1,979 lines / 47,859 bytes |
| SHA-256 | a7ed353a6cd7e6dba94610db962ba7029c7cb3c48762c866061d1f96120b5319 | 1109d499f9ba8b02352bb76db4cc952974f44bcd4811aaf1e122cc443aea6741 |

Wave history: the candidate was created by the Stage 2 CN3 integration (commit 6a8eb9d, the LOCALIZE-S2-D wave's port), normalized by 1869877 (FIX-CREDIT-D), and repointed by f1138e4 (FIX-P4, the pattern-4 repoint across 39 files — for this file it is the fragment repoint of section 3; the verdict stamp is computed against f1138e4 for that reason). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

The batch's largest port: a 2019 CN Black Highlighter theme （破碎的世界， "Broken World") built as a small system — a ~1,360-line main CSS body, a separate Latin-font exhibit, parameterized variant modules at the tail (custom logo, golden header, custom title, an English-font module, a collapsible-sidebar gate), a theme-squares palette, a credits demonstration that exhibits the Rate and credit modules as labelled specimens, and a classical-Chinese epigraph. The port consolidates that system into the campaign's frame: the JP BHL include and a head module serving the theme's own /1, an interwiki-style layer at priority 3 serving its /2, the font exhibit and the English-font module folded into the main exhibit's head (six display faces loaded once, duplicates deleted), and the variant modules carried at the tail with their comment banners translated. Two of the original's dependencies do not survive, for different reasons: the author's personal-wiki component (vol-title, imported from etinjat.wikidot.com) is dropped with its import, there being no JP counterpart; and the custom-logo module's fragment import, which pointed at a fragment page on the EN wiki, was repointed by the FIX-P4 wave to the JP fragment candidate's own delivery — so the one item T4 left open-ended ("to be resolved to a JP fragment before posting") is resolved in the current bytes. The theme's best-known quirk is documented in its own text and confirmed by the re-run render row: the interwiki/translation module is hidden on both the original and the candidate, by the theme's design. Measured churn is the batch's largest (diff.md: +421/−568 in 181 change blocks; a GNU-diff count of the same pair gives 897 changed lines, and the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 181 change blocks — 114 specific (63.0%), 49 heuristic (27.1%), 18 residue (9.9%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Per the class M treatment, the mechanical masses are counted, not narrated block by block: the 88 DELIVERY-MOVE blocks are the delivery consolidation of section 3, and the 77 COMMENT-TEXT blocks are the translation of the theme's own CSS comment banners, counted in section 6.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 122 |
| DELIVERY-MOVE | 88 |
| COMMENT-TEXT | 77 |
| TRANSLATION-ANCHORED | 15 |
| DRAFT-HOST | 15 |
| EXHIBIT-RESTRUCTURE | 9 |
| CONTENT-STRING | 5 |
| FONT-IMPORT | 4 |
| IFTAGS | 4 |
| SELF-DELIVERY | 4 |
| DELIVERY-HOST | 3 |
| INCLUDE-REPOINT | 3 |
| RESTORATION | 3 |
| DUPIMPORT-DEL | 2 |
| GLYPH-FORM | 2 |
| HEADERVAR | 2 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README: the 49 heuristic blocks are prose translations, comment-banner translations, and the font/body work (sections 4 and 6), verified by region against the diff. The 9 EXHIBIT-RESTRUCTURE primaries adjudicate in section 8 (the font exhibit's merge is real; the rest are frames). The 18 residue blocks collapse into the appendix table at the end of this document, per the class M treatment. The 3 RESTORATION blocks are spans the classifier marks as restored verbatim — the classical epigraph and the variant modules' texts that the port carries in the original's wording where the wording is the content (section 6). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:broken-world-jp; original theme:broken-world on scp-wiki-cn at reference revision 306; candidate `pages/theme:broken-world-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind K5b-4; the composition includes the companion fragment candidate, section 3 and the closing section). The original wraps the page in `[[iftags +版式]]` (L1–1989), with a head module inside the gate carrying the theme's first CSS block and the vol-title import (L4–101), and a tail outside the gate: the own-layer module (L1991–1993) and the ifexpr-gated variant modules (L1995–2125). The candidate puts the frame first, outside any gate (BHL include, head module, interwiki-style include, candidate L1–10), localizes the gate to `+テーマ` (candidate L12–1901), and keeps the variant modules at the tail (candidate L1903–1979).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for broken-world-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The page's own credit furniture is replaced in the standard form, and this theme's credit block is the batch's fullest: a `:scp-jp:credit:start-preview`/`end-preview` block at the head (candidate L14–25) carrying the eight ruling-3 fields (title 破砕世界 BHL テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 破碎的世界 BHL 主题； 著作権者 Etinjat; 作成年 2019; 初訳時参照リビジョン 306; the source link, naming scp-wiki-cn.wikidot.com/theme:broken-world, the recorded host, which serves the original) plus two theme-specific attribution lines the porter kept inside the block: a ロゴ line (the Broken Church / Cogwork Orthodox / Maxwellism / Xia logos by SunnyClockwork, CC BY-SA 3.0, and the standard SCP logo's attribution) and a フォント line naming the theme's eight faces. Separately, the theme's *credits demonstration section* (candidate L70–83) exhibits a bare `[[module Rate]]` and an info pair side by side in labelled cells （評価モジュール / クレジット付き評価モジュール) — that Rate is a specimen the theme documents, not the page's credit furniture, which is why no BARE-RATE-DEL block exists for this theme and why T4 recorded the pair as a labelled exhibit-pair exception. In the demonstration, the original's CN credit pair (`:scp-wiki-cn:credit:start`/`end`) became the JP info pair (`:scp-jp:info:start`/`end`) with the placeholder text translated. T7 credit-module CSS: none added beyond the theme's own. License box: none on either side, and none added; the logo attributions ride in the credit block's ロゴ line instead.
- **Why:** P3/T1 (KB-09) governs the page's own furniture; a documented specimen inside the theme's own documentation is content, and deleting it would have falsified the documentation. Ruling 3 fixes the eight fields; the two extra lines are the theme's own attribution facts, kept where a reader looks for them.
- **Verify:** Read candidate L14–25 against the eight fields; read candidate L70–83 for the specimen pair and its labels.
- **Disposition:** Applied (the head block is in the bytes); the specimen pair stands as a labelled exception, recorded here and in the T4 row.

### 2. Includes and components

- **What:** The candidate's includes: the JP BHL theme include at the head (candidate L1); the credit pair (section 1); one interwiki-style include (candidate L7–10, section 3); the theme-squares palette (candidate L29 onward, repointed to `:scp-jp:component:theme-squares` with its parameters carried over — residue B5 in the appendix is a parameter typo the port fixed, "May  Black" → "May Black"); the JP info pair in the credits demonstration (section 1); and the image-block family includes of the examples. One include family does **not** survive: the original imports and thrice includes the author's personal component `:etinjat:component:vol-title` (import at original L6 from etinjat.wikidot.com; includes at original L120, L169, L199). The candidate carries neither the import nor the includes: there is no JP counterpart to repoint to, and the port did not exercise ruling 4 for a personal-namespace component. Every live include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp. The vol-title deletion is the same rule's other edge: a foreign personal-wiki dependency with no counterpart is removed rather than kept as a live dependency on the author's own wiki. The deletion is stated here because it is a real content decision, not a repoint.
- **Verify:** `grep -n '\[\[include' candidate.txt` — all `:scp-jp:`; `grep -n 'vol-title\|etinjat' candidate.txt` returns nothing.
- **Disposition:** Applied (repoints in the bytes); the vol-title removal stands as recorded here.

### 3. Delivery and code loading

- **What:** The original delivers from five places: the head module (its first CSS block inline, plus the vol-title import, original L4–101); a tail module importing its own layer from its CN page (`scp-wiki-cn.wikidot.com/theme:broken-world/code/1`, original L1992); the my-logo variant module importing a fragment from the **EN** wiki (`scp-wiki.wikidot.com/fragment:broken-world/code/2`, original tail); the {$English} variant module importing three Latin faces from Google Fonts; and an empty collapsible-sidebar gate with no module at all. The candidate consolidates: the head module imports only the candidate's own `local--code/theme%3Abroken-world-jp/1` from the draft host (candidate L3–5, SELF-DELIVERY); an interwiki-style include at priority 3 names the candidate's own /2 delivery (candidate L7–10); the CSS bodies live in the two code exhibits (candidate L377–1830, L1833–1897); the my-logo module now imports the JP fragment candidate's own delivery, `local--code/fragment%3Abroken-world-jp/2` on the draft host (candidate L1910) — the FIX-P4 repoint (commit f1138e4) that resolved T4's open-ended item; the golden-header and my-title variant modules carry their CSS inline as the original's did, their comment banners translated; and the {$English} module and the empty sidebar gate are gone, the Latin faces having been folded into the main exhibit's head (section 4). The 88 DELIVERY-MOVE blocks are this consolidation counted by the classifier; the 15 DRAFT-HOST blocks are the own-delivery references across the frame and the exhibits that reproduce the delivery form.
- **Why:** P4/T9: delivery is served from JP hosts — the theme's own code and its JP fragment candidate — never from the original's wiki, the EN wiki, or the author's personal wiki. P6/T3 supplies the interwiki-style supplement frame (priority 3 for the own layer riding on the base page). The ledger dispositions this theme's P4 charge in the delivery class (ii) (original-state CDN delivery), which the FIX-P4 repoint has since overtaken in the bytes: the package follows the bytes. The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n '@import' candidate.txt` — L4 (own /1), L387–392 (the exhibit's font loads, section 4), L1910 (the fragment /2); no scp-wiki-cn, scp-wiki, or etinjat delivery URL remains.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the fragment repoint is FIXED in the bytes (FIX-P4).

### 4. Fonts and assets

- **What:** Fonts: the main exhibit's head loads six display faces from Google Fonts (candidate L387–392): ZCOOL XiaoWei (the CN display face, kept), Iceberg, Iceland, Kumar One, Black Ops One, and Space Mono. This is a consolidation: the original loaded its Latin faces twice over, in the font exhibit （英文字体引用） and again in the {$English} tail module; the candidate loads each face once (the 4 FONT-IMPORT blocks) and deletes the duplicates (the 2 DUPIMPORT-DEL blocks, the KB-65 shape). The JP faces named in the credit block's font line (Noto Serif JP, Noto Sans JP) ride on the JP BHL base the frame includes; the candidate adds no separate JP import of its own. Assets: the branch-symbol gallery's images are re-hosted as the candidate page's own attachments on the draft host (for example `local--files/theme%3Abroken-world-jp/Logo-CN-hub.png` at candidate L238), and the logo attributions are recorded in the credit block (section 1). T1's single hotlink is the one foreign content URL left inside the applied body: the EN component URL named in the CSS at candidate L1239 (`scp-wiki.wikidot.com/component:collapsible-sidebar`), a reference the theme's CSS carries; it is not a delivery line.
- **Why:** P7 (the font loads are the theme's own design, deduplicated; KB-65 for the duplicate removal) and P5 (assets served from JP hosts — here satisfied by re-hosting for the gallery). The stray component URL is recorded under T1's hotlink class (ii).
- **Verify:** `grep -n '@import' candidate.txt` for the six faces; `grep -n 'local--files' candidate.txt` for the re-hosted gallery.
- **Disposition:** Applied (fonts and gallery in the bytes); the hotlink stands as class (ii).

### 5. Header, sidebar, and site furniture

- **What:** The header work is the variant system itself: the HEADERVAR blocks are the header-variable regions of the main body and the golden-header variant, carried with their values; the theme's parameterized title/logo variables ({$my-title}, {$my-logo}, {$set-logo} and friends) survive as parameters, their documentation translated (the parameter-example region is residue B68's consolidation, appendix). The sidebar item of record is the render row's: on desktop the sidebar renders collapsed with no visible reopen tab, while the mobile hamburger opens in both engines — and the theme's hidden-interwiki behavior (the translation module hidden on all eight engine/page combinations) is, per the re-run row and T3, explicitly documented in the page's own text as an original quirk of the theme, present identically on the original. The original's empty collapsible-sidebar gate does not survive (section 3); it contained no module and no rules.
- **Why:** P8/P9 checked against the variant system; the render readings belong to the disposition register because they describe what a reviewer will see, on the original as much as on the candidate.
- **Verify:** `grep -n 'my-logo\|my-title\|my-golden-header' candidate.txt` — the three surviving variant gates at the tail; the render row is RENDER-ROWS-RERUN16 (CN3).
- **Disposition:** Standing; the render readings are recorded in section 11.

### 6. Text translation

- **What:** The prose is translated throughout (the 122 TRANS-UNANCHORED heuristic primaries and 15 TRANSLATION-ANCHORED blocks, verified by region): the palette section, the credits demonstration's labels, the usage and parameter documentation, the branch-symbol gallery's captions, and the examples. The theme's CSS comment banners — its section headers inside the code, in Chinese in the original — are translated with the code (the 77 COMMENT-TEXT blocks, counted here as one mass per the class M treatment; for example the my-logo module's banner now reads カスタムロゴ). Two retentions are deliberate and labelled. (1) The classical-Chinese epigraph (candidate L64–68) stands in the original's wording, with its attribution （『校讎通義』より） added in Japanese: it is a quotation, and the RESTORATION blocks include it. (2) One gallery caption stands in Chinese in the current bytes (candidate L240–241: the SCP-CN branch symbol's caption, `中国支部`): T4's row recorded this residue; it is the CN branch's own name inside a gallery of branch symbols, and no ledger charge attaches to it — but it is Chinese prose on a JP page, and the package states it rather than smoothing it over. The GLYPH-FORM blocks are the simplified-to-Japanese glyph conversions inside the translated strings, and the 5 CONTENT-STRING blocks are reader-visible strings changed as content (captions and labels), counted here.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings). A quotation and a branch's own name are the two shapes retention legitimately takes; both are labelled so a reviewer can tell them from untranslated residue.
- **Verify:** The pairs are diff.md's body sections in order; `sed -n '240,241p' candidate.txt` for the retained caption.
- **Disposition:** Standing (the port itself); the retained caption is recorded as found.

### 7. Links

- **What:** The credit source link (candidate L22) names the recorded host (scp-wiki-cn) and serves. The prose links of the usage documentation name JP targets or the serving originals; no bare link names a page missing on scp-jp, and no prose link names a foreign wiki as content. The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) finds no divergence in the prose: the only foreign wikidot URLs left in the file are the CSS reference of section 4 and the delivery text inside exhibits, both accounted for. (The original's EN-fragment dependency was a delivery line, not a prose link; its repoint is section 3.)
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; this theme's prose links satisfy it as they stand.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link, the section 4 CSS reference, and exhibit text.
- **Disposition:** Standing; no P11 item was recorded for this theme.

### 8. Structure

- **What:** Exhibit census first, per R3. The original has three code exhibits: the main CSS body (L528–1887), the Latin-font exhibit (L1893–1913), and a third exhibit (L1915–1977). The candidate has two: the main body (L377–1830) and the third exhibit's counterpart (L1833–1897). The font exhibit was **merged**, not dropped: its imports stand at the main exhibit's head (candidate L387–392, section 4), deduplicated against the {$English} module's identical loads. The 9 EXHIBIT-RESTRUCTURE primaries adjudicate as that merge (the font exhibit's frame and the main exhibit's head), the source-code sections' frames, and the tail variant section's frame. The variant modules correspond three-for-five, the two absences being the empty sidebar gate and the folded English module (section 3). The parameter-documentation region is shorter in the candidate (residue B68's consolidation): the candidate documents the parameters it keeps, in the form its own usage section uses. No exhibit content is unaccounted for: every original exhibit's substance is either in a candidate exhibit or, for the font exhibit, in the main exhibit's import lines.
- **Why:** R3 exists to force exactly this census, because a merge and a deletion share a diff shape; here the merged content is located line by line, so the merge is stated as a merge.
- **Verify:** `grep -n '\[\[code' original.txt candidate.txt` — three exhibits against two; read candidate L387–392 against original L1893–1913 for the merged imports.
- **Disposition:** Standing (census complete; the merge is in the bytes).

### 9. Formatting only

- **What:** None as its own class: the classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The exhibit-boundary residue pairs in the appendix are alignment absorptions, counted there.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate contains no 訳注 footnotes and no `[!-- ... --]` porter comments; the comment text that fills 77 blocks is the theme's own CSS banners in translation (section 6), not porter annotation. The port's two real judgments (the vol-title removal, the font consolidation) are not announced in the page — their record is this package and the wave reports.
- **Why:** R2: porter-added text is part of the change record; its absence is stated, not assumed — and the theme's own comments are not misread as annotations.
- **Verify:** `grep -n '訳注\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (as an absence, stated).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's fourteen errors: pseudo-ref ×13 — the candidate's own draft-host delivery references across the frame and exhibits (section 3), class (ii); hotlink ×1 — the EN component URL inside the applied CSS (section 4), class (ii). There is no class (i) error; the 4 warns / 2 infos are recorded verbatim in T1-ROWS row 197 and are not classified. (2) The re-run render row's items (RENDER-ROWS-RERUN16, which supersedes the earlier row for this theme under rule S1): hidden-interwiki on all eight combinations on both pages — the translation module hidden by the theme's own design, explicitly documented in the page text as an original quirk (T3-confirmed); page overflow of 374px@320, 425px@375, 810px@768 (chromium) and 450px@320, 478px@375 (webkit); the page's runtime-hotlink chain only (KB-44 environment layer); the sample's credit-modal errors (KB-32 preview form, ruling 5); the desktop sidebar collapsed with no visible reopen tab (mobile hamburger opens in both engines); and the low-contrast credit title and 404 logos the row records as intended/deferred. (3) T4's two display-affecting items: the EN-fragment import — **FIXED** by the FIX-P4 repoint (section 3), overtaking the ledger's P4 DISPOSITIONED line for this theme, which described the pre-repoint delivery state; and the Chinese gallery caption — standing in the bytes as recorded (section 6), with the theme's credit and language items otherwise complete per the row. The theme's determination is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; where a later wave's bytes overtake a disposition, the package follows the bytes and says so.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1 and 2); item 3's first half FIXED, its second half recorded as found.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 197): exit 1, 14 errors / 4 warns / 2 infos; the errors are pseudo-ref ×13 and hotlink ×1, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-RERUN16 (CN3), superseding the RENDER-ROWS-2 row under rule S1): FINDINGS — the items of section 11(2), with T3 complete in the final report and no further finding; engine coverage full (chromium + webkit, both pages). (c) T4/T5 (LOCALIZE-ROWS row 171): FINDINGS jointly, display-affecting findings 2; the ledger §(c3) line records the theme's P4 outcome as DISPOSITIONED, since overtaken by the FIX-P4 bytes (section 11(3)). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +421/−568 in 181 change blocks; the GNU-diff count of the same pair is 897 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:broken-world-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 172; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; this port's record is larger than most. (1) `pages/theme-decoration-sample-broken-world-jp.txt` is the decoration sample the render checks ran against (its credit-modal reading is section 11(2)); the original-side sample `pages/theme-decoration-sample-broken-world.txt` is the campaign's mirror-side fixture. (2) The companion fragment candidate **fragment:broken-world-jp** is part of this port's composition (sources kind K5b-4): its /2 delivery is what the candidate's my-logo module imports (section 3), and its own record belongs to the fragment's package, not this one. (3) The re-hosted gallery images (section 4) are attachments of the candidate page itself, not separate repo files. There are no inbound-link repairs in other candidates for this theme.

## Per-theme record

### The usage example's posting name

The usage examples at candidate L96, L269, L282, and L321 as built read `:scp-jp:theme:broken-world` — the first as a complete escaped include, `@@[[include :scp-jp:theme:broken-world]]@@`, the other three in the unclosed `@@[[include :scp-jp:theme:broken-world@@` exhibit forms the variant modules' documentation uses: the porting wave's repoint changed the branch prefix but left the plain name, so each example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed each reference to `:scp-jp:theme:broken-world-jp` at the same lines (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), four of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

All 18 residue blocks, adjudicated (class M treatment: one table, no per-block slots). Spans are 1-based lines in the two package files.

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B5 | L134 | L34 | Theme-squares parameter line: the double-space typo "May  Black" normalized to "May Black" (section 2) |
| B6 | L163–164 | L63 | Prose pair in the epigraph region: translation with a line consolidation (section 6) |
| B11 | L186–187 | L76 | The credits demonstration's Rate cell: the specimen pair's frame lines (section 1) |
| B18 | L215 | L106–107 | Usage-prose line, translated (section 6) |
| B20 | L220 | L112–113 | Usage-prose line, translated (section 6) |
| B25 | L250–251 | L129 | Section-boundary alignment pair at a heading; the heading text is carried in its anchored pair nearby (section 6) |
| B43 | L331–332 | L203 | Parameter-documentation line, translated (section 5) |
| B50 | L358–359 | L229 | Gallery-region prose line, translated (section 6) |
| B52 | L367–368 | L237 | Gallery-region line at the re-hosted CN-hub image (section 4) |
| B54 | L377–378 | L245 | Gallery-region prose line, translated (section 6) |
| B68 | L478–481 | L332 | Parameter-example consolidation: the original's four example lines are carried in the candidate's shorter parameter documentation (section 8) |
| B74 | L510–511 | L360–361 | Prose pair before the source-code section, translated (section 6) |
| B80 | L529 | L378–379 | Main exhibit's opening alignment pair (the exhibit head, section 8) |
| B163 | L1889–1890 | L1734 | Inside the main exhibit's tail region: a CSS line pair the delivery consolidation re-anchored (section 3) |
| B169 | L1916 | L1834–1835 | Third exhibit's opening alignment pair (section 8) |
| B173 | L1977 | L1896–1897 | Third exhibit's closing alignment pair (section 8) |
| B174 | L1980–1983 | L1900 | Gate-exit alignment: the original's raw-marker lines before the gate close are absorbed at the candidate's section exit (section 8) |
| B175 | L1985–1989 | L1901 | The main gate's closing lines, localized gate form (section 0) |

## License and attribution

- **Title:** 破碎的世界 BHL 主题
- **Author:** Etinjat
- **Source:** https://scp-wiki-cn.wikidot.com/theme:broken-world — revision 306
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
