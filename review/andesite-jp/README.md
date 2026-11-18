# Review package — theme:andesite-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:andesite-jp — origin CN, population #163 [GOSIGN2-LEDGER (b) row 163]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); both OPEN items re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 1 info (hotlink×5, pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 140; GOSIGN2-LEDGER (b) row 163]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 500–501px@320/375 (page) and 512–513px@320/375 (sample); runtime-hotlink site-theme chain; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-E (CN1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 162, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 162]
- FIX5 re-judgement: items 43 (class H) FIXED, 44 (class H) FIXED — FIX5-TEXTA §8, commit 6f6b349: four Chinese content: chrome strings translated (containment, description, tags, page-info); prose links repointed to theme:basalt-jp, component:sigma-plus-jp, component:betterbetterfootnote-jp (all existing candidates) [GOSIGN2-LEDGER-SUPPLEMENT (a) items 43–44]
- Computed against: canonical commit 6f6b34974c400a68e01363f5423d1cf817492522; candidate file pages/theme:andesite-jp.txt sha256:37d45777565fb364f3bffaf6f901b5e6218e6b6549a7a7d2455ab1afd8cacb38; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); this theme's stamp is not stale, because the FIX5 commit is the candidate's last change |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 43 [H] (Chinese chrome labels standing in CSS `content:` strings) and item 44 [H] (prose links still leading to the CN site / a personal wiki where JP counterparts exist) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md rows 43 and 44: both **FIXED** (FIX5-TEXTA §8, commit 6f6b349); both re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c2) render row: page-overflow (KB-33/KB-34 families), runtime-hotlink site-theme chain (KB-40), credit-modal preview form (KB-32); the §(e) item 43 charge itself records the row's pattern-9 header variables and pattern-5 hosts as dispositioned in §(c3) (P9 under ruling 2; P5 under class (ii) / KB-58) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:andesite | theme:andesite-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 10 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-andesite.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:andesite-jp.txt`, copied at worktree HEAD c63afef |
| Lines / bytes | 1,640 lines / 35,865 bytes (the file's last line carries no trailing newline, so `wc -l` reports 1,639) | 1,642 lines / 38,059 bytes |
| SHA-256 | e4ce108b8bbbdd7f8c9577b358a1b4ffc9c43d807b81378ee9dc77df0781e49b | 37d45777565fb364f3bffaf6f901b5e6218e6b6549a7a7d2455ab1afd8cacb38 |

Follow-up note (sources.tsv, K5a-i): the original has been superseded upstream since revision 10; the campaign record holds a follow-up diff artifact (`diff-andesite-from10.txt`) for that later movement. This package's mirror stays at revision 10, the revision the port was actually made from; the supersession is recorded here rather than absorbed silently (section 12).

Wave history: the candidate was created by the Stage 2 CN1 integration (commit 4a2f4a5, the LOCALIZE-S2-D wave's port); rework2-p3 (2d69b1c) made it a Sigma-Plus shared receiver and added the betterbetterfootnote receiver; FIX-P4 (f1138e4) repointed its base-theme CSS imports to the JP port candidates; FIX5-TEXTA (6f6b349) closed items 43 and 44 and completed the usage example's posting name, all in the one commit whose hunks are quoted in the per-theme record.

## Summary

Andesite is a Sigma+ theme: the original self-delivers its own code block from the CN wiki and builds on the CN sigma-plus component, whose code its stylesheet imports directly. The candidate keeps that architecture and re-bases every leg of it: its own delivery moves to the draft host under the standard frame, the base import becomes the JP sigma-plus candidate, and the differences the CN sigma-plus carried are preserved as an explicit override layer at the head of the candidate's code block, with porter comments saying so. Around that delivery core, the port swaps two exhibit sets of the CN credit component for the single JP preview credit block, translates the documentation tabview, and replaces the samples that depended on an unported personal-wiki component with a note that says exactly that. Measured churn is small against the file's size (diff.md, the generator's difflib count: +156/−160 in 69 change blocks / 11 hunks; a GNU-diff count of the same pair gives 262 changed lines — the difference is alignment choice, not content), because the 1,400-line stylesheet body is carried in place. The two blocking items were both reader-visible Chinese residue (chrome labels in CSS strings; prose links to the CN site), and both fixes are small, late, and verified below line by line. No defect flag arises from this package's checks; the one provenance caveat (the credit author's name has no in-source occurrence) is recorded in section 1.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 69 change blocks — 42 specific (60.9%), 20 heuristic (29.0%), 7 residue (10.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 26 |
| TRANS-UNANCHORED | 24 |
| FONTLOAD-CJK-STACK | 6 |
| GLYPH-FORM | 5 |
| DRAFT-HOST | 4 |
| CONTENT-STRING | 4 |
| DELIVERY-HOST | 3 |
| COLON-ENC | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| SELF-DELIVERY | 2 |
| SIGMA-PLUS-JP | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes, and the sections below are written from classification.json's label_spans, not from the skeleton's per-section text). The seven residue blocks are exactly the seven unlabeled ones, and each resolves: B3 (the `[<]` wrapper lines of the head credit exhibit, removed with it — section 1); B9 (the usage-example exhibit line — section 2); B18 (the Q&A font answer, Noto Sans SC → Noto Sans JP in prose — section 4); B20 (the in-tab credit exhibit set's deletion — section 1); B51 (two lines inside the cobs sample region — section 8); B68 and B69 (the code block's closing alignment and the added trailing newline — section 9). Three labeled blocks need correction against the bytes: B19's RATE-EXHIBIT-KEPT-CANDIDATE is a false fire — its candidate side holds only the tab heading, and the original's in-tab bare Rate was deleted, not kept (no `[[module Rate]]` exists in the candidate; section 1). B55's primary T7-CREDIT-CSS names one rule inside a block whose substance is the code head (delivery imports, the sigma-plus override layer, the font loads — sections 3 and 4); the credit CSS proper is inherited, as section 1 records. B56's CSS-BODY heuristic is the Font Awesome import pair plus the deleted fendsfox footnote import whose JP replacement sits at candidate L192 (section 3). The 20 heuristic blocks are the TRANS-UNANCHORED mass: one-line prose translations and CSS comment translations (R1), resolved by shape in section 6 and the appendix note there. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:andesite-jp; original theme:andesite on scp-wiki-cn at reference revision 10; candidate `pages/theme:andesite-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original opens with its self-delivery module (original L1–3, importing its own `theme:andesite/code/1` from the CN wiki) and then its gate `[[iftags +版式]]` (L4); the candidate opens with the same delivery re-based (candidate L1–3, own /1 on the draft host), adds the interwiki-style frame (L4–7), and opens the localized gate after it (L9).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for andesite-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is two exhibit sets of the CN credit component plus a bare Rate: a head set in a `[<]` wrapper (original L11–19: credit:start / more / end around sample page-info text) and an in-tab set (original L62–80: a centered `[[module Rate]]` at L62–63, credit:start / more / end at L64–72, and the start-standalone / end-standalone pair at L74–80). The candidate replaces all of it with the single JP preview credit block (candidate L17–26) carrying the eight ruling-3 fields (title 安山岩 版式; 翻訳責任者 AI; 翻訳年 2026; 原題 安山岩 版式; 著作権者 AsWheat; 作成年 2024; 初訳時参照リビジョン 10; the source link, section 7). No `[[module Rate]]` and no credit-component include remains in the candidate. The credit CSS is inherited, not supplemented: the rate-box and creditButton rules (original L1129–1213) stand in the candidate at L1131–1215 with the same selectors, and the one added credit-adjacent rule is the override layer's rate-box alignment (candidate L216–218, part of section 3's sigma-plus layer, which is where B55's T7-CREDIT-CSS label fired). No license box exists on either side (the only "license" strings in both files are site-chrome CSS selectors, `#license-area` and `.side-block.license`, inside the stylesheet).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form; the original's sets are component exhibits demonstrating the CN credit component, and the JP page's credit rendering is the head block itself, so the exhibits and the duplicate bare Rate (KB-09) go with the swap. Ruling 3 fixes the eight fields. T7 (KB-11/KB-12): no supplement block was needed because the theme's own CSS already styles the credit furniture, and it was carried over.
- **Verify:** `grep -n 'module Rate\|credit:start\|credit:more' candidate.txt` returns nothing; read candidate L17–26 against the eight fields; compare the credit-rule selectors at original L1129–1213 and candidate L1131–1215.
- **Disposition:** FIXED (ledger §(c3) via the credit waves for the P3 fields; the exhibit removal is part of the same swap). One provenance caveat, recorded rather than flagged as a defect: the 著作権者 name AsWheat occurs nowhere in the original page source (the string appears in the candidate only, at L22); it is evidenced by the campaign's own record of the page's authorship (the LOCALIZE-S2-D lane report names the theme's author), not by anything inside the two diffed files, and a reviewer working from this package alone cannot re-derive it from the sources. The field is not contradicted by the original; it is underivable from it, which is a different thing, and the distinction is stated here so the field is not mistaken for an in-source quotation.

### 2. Includes and components

- **What:** The candidate's live includes are four: the interwiki-style frame (candidate L4), the credit pair (L17/L26, section 1), and the image-block exhibit in its unprefixed same-name form (candidate L93), which the original also carries unprefixed (original L106). The usage-example exhibit (candidate L42) is the escaped self-include, repointed and completed (below). Everything else the original included is gone with its exhibits: the two credit sets (section 1) and the `:fendsfox:component:cobs` samples (section 8). The SIGMA-PLUS-JP spans are B12 (the prose link of item 44, section 7) and the code import (section 3).
- **Why:** P1 (KB-15): live includes name JP counterparts; the image-block component is a same-name shared component on both wikis, so its form does not change. Ruling 4 is not engaged for the credit or image components (both exist on scp-jp); it is the cobs component that has no JP port, and its treatment is section 8's, not an include kept foreign.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the four live includes above plus the escaped exhibit, no foreign target among them.
- **Disposition:** Applied; no foreign include kept.

### 3. Delivery and code loading

- **What:** Three delivery legs, all re-based. (a) Own code: the original's head module imports its own `theme:andesite/code/1` from scp-wiki-cn (original L2); the candidate's head module imports its own /1 from the draft host (candidate L2) and the interwiki-style frame at priority 1 names the same /1 (candidate L4–7). The candidate's only code block (candidate L187–1639) holds the stylesheet, so the frame's address names the block that holds the CSS. (b) The base: the original's code block imports the CN sigma-plus code directly (original L227); the candidate's code block imports the JP candidate's code, `component%3Asigma-plus-jp/1` on the draft host (candidate L188), and immediately adds an override layer (candidate L194–226) preserving what the CN sigma-plus carried that the JP base does not — its `:where(:root)` variables (L196–201), the Safari media-query hack, the sidebar and search rules, and the rating-box alignment — under two porter comments stating that the layer keeps only the CN adaptation differences (section 10). (c) The two satellite components: the non-savingpage import is kept on its original host, evernight-aquarium (original L228 → candidate L190), because no JP port of that component exists; the footnote component's import moves from the author's personal wiki (original L232, fendsfox) to the JP candidate on the draft host (candidate L192). The wave record matches the bytes: rework2-p3 (2d69b1c) set up the shared receivers, and FIX-P4 (f1138e4) repointed the base imports.
- **Why:** P4/T9 (delivery from JP distributions: sigma-plus via its JP candidate's code, the theme's own code via the draft host) and P6/T3 (the supplement frame, priority 1 for the theme's own layer over the imported base). The override layer is the mechanism that lets the base be shared without losing the CN adaptation the original obtained by importing CN sigma-plus; without it, repointing the import would silently change the theme's furniture values.
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L2 and L6 (own delivery), L188 (sigma-plus-jp), L192 (betterbetterfootnote-jp); read candidate L187–235 against original L226–262.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii), KB-41; the kept evernight-aquarium import, original-state delivery, class (ii), KB-54 family — the render row dispositions this theme's candidate-own foreign hosts on exactly that ground).

### 4. Fonts and assets

- **What:** Loads (code head): the candidate adds a Noto Serif JP import (candidate L228) ahead of the inherited pair, converts the text import from Montserrat + Noto Sans SC to Montserrat + Noto Sans JP (original L230 → candidate L231), and keeps the Font Awesome 6.5.1 cdnjs import (candidate L232). Stacks: six FONTLOAD-CJK-STACK blocks (B58–B63) rewrite `Noto Sans SC` to `Noto Sans JP` in the stylesheet's font stacks (e.g. original L257–258 → candidate L259–260; the blockquote rule at original L1345 → candidate L1347), and the Q&A's prose font answer makes the same change (B18: "Noto Sans SC, Font Awesome" → "Noto Sans JP、Font Awesome", candidate L64). Every family the stacks name is loaded by the imports above or by Font Awesome; no stack names an unloaded face. Assets: the body logo image keeps its personal-wiki host with the path colon-encoded (original L24 `theme:genshin` → candidate L30 `theme%3Agenshin`, block B5); the override layer's sigma-9 logo stays on the CN host sigma9.scpwikicn.com (candidate L200); the theme's own `:root` logo is the Basalt logo file on scp-wiki with its colon encoded (original L235 → candidate L237, block B57); the image-block exhibit's school.png stays on scp-wiki.wdfiles.com in both files (candidate L94).
- **Why:** P7/T5 with KB-16 (the font load gap): the SC faces cannot render Japanese text, so load and stacks change together — here they demonstrably do, which is the check this section exists to make. JPFONT-LOAD is the added Serif import, giving the stacks' serif role a JP face. P5/KB-17 with KB-58 covers the kept asset hosts: they are original-state files with no JP re-host, dispositioned as a class rather than silently passed over.
- **Verify:** `grep -n 'Noto Sans SC' candidate.txt` returns nothing; `grep -n '@import' candidate.txt` lists the delivery and font imports of sections 3–4 and no other.
- **Disposition:** Font load and stacks applied and mutually consistent; the kept asset hosts are DISPOSITIONED (class (ii) / KB-58; they are T1's hotlink errors, section 11).

### 5. Header, sidebar, and site furniture

- **What:** Two header-variable sets, both carried with Chinese values. The override layer's `:where(:root)` (candidate L196–201): `--header-title: "SCP基金会"`, `--header-subtitle: "控制，收容，保护"`, and the CN sigma-9 logo (section 4). The theme's own `:root` (candidate L236–252): `--header-title: "SCP基金会"`, `--header-subtitle: "控制 收容 保护"` (the original's space-separated form), with only the logo line's encoding changed (section 4). The small `.logo img` module at the head is carried verbatim (original L5–9 → candidate L11–15). No P8 layout adaptation appears; the sidebar rules are the inherited ones, including their two source-citation comments (candidate L486, https; candidate L677, http — the second is section 11's HTTP-KEPT line).
- **Why:** P9/T6 is the variable class; the values are header and title language, which ruling 2 (2026-11-16) places outside migration correctness as translation taste. Item 43's charge text itself records that this row's pattern-9 header variables are dispositioned in §(c3) — the FIX5 charge was the chrome labels of section 6's per-theme record, not these variables, and the distinction (chrome UI text vs header/title text) is the ledger's own.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — four lines, values identical to the original's.
- **Disposition:** DISPOSITIONED (P9, ruling 2).

### 6. Text translation

- **What:** The documentation body is translated throughout: 26 TRANSLATION-ANCHORED blocks (tab titles, the Q&A, the heading samples, the usage text) and the prose half of the 24 TRANS-UNANCHORED blocks, each verified against the mirror for this README. Three sub-shapes are stated separately, per the taxonomy. (a) Reader-visible CSS strings (CONTENT-STRING, B64–B67): the four chrome labels of item 43 — containment （特殊収容手順， candidate L1351), description （説明， L1355), tags （タグ, L1417), page-info （ページ情報, L1471) — argued in the per-theme record. (b) R1 in-CSS text: the stylesheet's Chinese comments are partly translated and partly kept (e.g. `/* 全局 */` stands at candidate L235; the betterbetterfootnote source comment at candidate L1363 keeps its fendsfox URL as a citation); comments are porter-visible only, are not reader-visible strings, and no charge attaches to them. (c) R5 glyph-form conversion (GLYPH-FORM spans in B6, B43, B47, B64, B65): retained strings whose characters change form rather than language, e.g. the tab title 基础信息 → 基本情報 (candidate L35) and 描述 → 説明 inside item 43's set. Chinese survives reader-visible only in the header variables (section 5, ruling 2) and inside the SEXTNK note's retained footnote text (section 8).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings, including `content:`), with R1 and R5 named so a reviewer can tell "translated", "converted", and "kept as a comment" apart instead of re-deriving them from the diff.
- **Verify:** The pairs are diff.md's body sections in order; `grep -n 'content:' candidate.txt` shows the four labels of item 43 in Japanese and no Chinese `content:` string.
- **Disposition:** Standing (the port itself); item 43's strings FIXED (per-theme record); the survivals dispositioned as recorded.

### 7. Links

- **What:** Item 44's three prose links, all in the Q&A (re-derived in the per-theme record): the Basalt reference (candidate L50), the Sigma+ statement (candidate L52), and the footnote-component credit (candidate L56) — URL-form links to scp-wiki-cn and fendsfox in the original, page-link form to the -jp candidates in the candidate. The credit block's source link (candidate L25) reads `https://scp-wiki-cn.wikidot.com/theme:andesite` — the host matches the original's recorded host in review/sources.tsv (scp-wiki-cn.wikidot.com), and no defect arises. No other prose link in the candidate targets a CN-wiki or personal-wiki page; the remaining foreign-host strings in the file are asset URLs and CSS comments (sections 4–5), not links.
- **Why:** P11 under the dead-reference evidence standard: prose links take the JP counterpart where one exists, and all three targets exist as candidates (theme:basalt-jp, component:sigma-plus-jp, component:betterbetterfootnote-jp), which is what made the original state a MISSED charge rather than a disposition.
- **Verify:** `grep -n 'scp-wiki-cn.wikidot.com\|fendsfox' candidate.txt` — the source link and the CSS source comment only; read candidate L50, L52, L56.
- **Disposition:** FIXED (item 44, supplement row 44).

### 8. Structure

- **What:** The localize.md closing rule holds for the stylesheet: the code block sits where the original's sits (after the tabview, inside the gate), its internal order, variable names, and selectors are preserved, and the JP additions are the head frame, the override layer at the code head, and the credit block — not interleaved edits. Two exhibit decisions, each with its ground. (a) The credit exhibits (section 1): replaced by the credit block, the P3 form. (b) The cobs samples (EXHIBIT-RESTRUCTURE, B50–B52): the original's component tab closes with two live `:fendsfox:component:cobs` includes carrying sample classifications (original L186–202) and an escaped usage exhibit of the same component (original L204–213). The candidate deletes the includes and the exhibit and puts a translated note in their place (candidate L171) stating that the classification components designed for this theme (CN branch's fendsfox:component:cobs) are not ported to SCP-JP and are therefore not handled by this port, keeping the SEXTNK explanation and its footnote. The surrounding furniture (the wikiwalk nav, the joke tab) is carried and translated. This is a stated replacement, not a silent deletion: the note is in the body where the samples stood.
- **Why:** R3 exists to force exactly this distinction, because a restructure and a deletion share a diff shape and ledger class I charges the silent form. The ground for dropping the samples rather than keeping the includes is P1/KB-54's other side: a live include of a personal-wiki component with no JP counterpart would be a foreign include the JP environment cannot resolve, and ruling 4's port-alongside obligation was not exercised for this component; the taxonomy scout records this theme as an R3 instance on the same facts.
- **Verify:** Read original L184–224 against candidate L168–185; the note at candidate L171 names the component and the ground.
- **Disposition:** Standing (restructuring recorded in the body itself; no ledger item charges it, and the taxonomy record names it).

### 9. Formatting only

- **What:** Minor. No whitespace-only block pair and no re-indentation (classifier: reindent_blocks 0), so the R7 follow-up-diff hazard is not triggered. The residue tail blocks are B68 (the code block's closing lines: the candidate's block ends one line shorter at the tail, candidate L1639) and B69 (the final `[[/iftags]]` plus the trailing newline the original lacks). The code tag's type value changes case (`type="CSS"` → `type="css"`, candidate L187) as part of the head block B54.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Diff.md's final hunk and the classifier summary in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The annotations are the override layer's comments (block B55's COMMENT-TEXT span): the two header comments at candidate L194–195 (naming the layer as the Sigma-Plus CN adaptation override and stating that only the differences from the EN-based base are kept), the inline note on the sidebar rule (candidate L209, recording that the original deleted an `align-self: start` the base carries), and the body marker `/* ===== andesite 本体（原語版のコードブロック） ===== */` at candidate L227 separating the layer from the theme's own CSS. The skeleton's per-section text understates this section; the spans above are the bytes.
- **Why:** R2: porter-added text is part of the change record, and these comments are load-bearing — they are the only in-file explanation of why the candidate's code block opens with a layer the original does not have, and a future editor who deletes the "duplicate" rules without them would silently change the theme's furniture.
- **Verify:** Read candidate L194–195, L209, and L227.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section: (1) T1's eight errors — hotlink ×5 (the kept foreign-host asset and import lines of sections 3–4: the fendsfox logo, the CN sigma-9 logo, the EN-host exhibit image, the kept component import; class (ii) / KB-58 and the KB-41/KB-54 family) and pseudo-ref ×3 (the draft-host delivery and base-import lines, class (iii)); no class (i) error stands. (2) One HTTP-KEPT line (derived presence in classification.json): the CSS comment at candidate L677, `/* source: http://ah-sandbox.wikidot.com/component:collapsible-sidebar-x1 */`, inherited byte-identical from original L675 — a source citation inside a comment, not a load and not a link; class (ii) by the http mapping, and recorded here so the count is explained rather than passed over. (3) The render row's items, all cross-cutting or environment layer, not charged to the candidate: page-overflow 500–501px@320/375 (page) and 512–513px@320/375 (sample) in the KB-33/KB-34 families; the runtime-hotlink site-theme chain (KB-40); the sample credit-modal errors (KB-32, ruling 5). (4) The header variables (P9, ruling 2, section 5) and the pattern-5 hosts (P5, class (ii) / KB-58), which item 43's charge text records as dispositioned in §(c3).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 140): exit 1, 8 errors / 1 warn / 1 info (hotlink×5, pseudo-ref×3); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN1)): FINDINGS, the items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 162): FINDINGS jointly, display-affecting findings 5; of these, two reached the §(e) register as items 43 and 44 and the rest are the §(c3) dispositions the item 43 charge names (pattern-9 variables, pattern-5 hosts). (d) The FIX5 closures re-derived for this package from the commit (6f6b349) and the current bytes: item 43's four strings and item 44's three links, line by line in the per-theme record; the same commit also completed the usage example's name (candidate L42), so this file needed no later sweep repair, which is why its stamp is PASS rather than STALE. (e) T4 follow-up: the original has moved upstream since revision 10, and the follow-up diff artifact `diff-andesite-from10.txt` in the campaign record (K5a-i) is the instrument for that movement; it does not change this package, whose mirror is the revision the port was made from. (f) A brace-depth scan of the delivered code block (candidate L187–1639) ends at depth 0 with no negative excursion. (g) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +156/−160 in 69 change blocks / 11 hunks; the GNU-diff count of the same pair is 262 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:andesite-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 163 as re-judged by supplement rows 43–44; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 43 re-derived (ledger class H)

The charge: reader-visible UI labels stood in Chinese in the candidate's CSS `content:` strings — the containment-procedures, description, tags, and page-info chrome labels — charged as the row's main display-affecting item, with the ledger noting these are chrome UI text, not header/title text, so ruling 2 does not cover them. FIX5-TEXTA §8 (commit 6f6b349) translated all four, and the bytes confirm each one at its line: `content: "\f023  特殊収容措施"` (original L1349) → `"\f023  特殊収容手順"` (candidate L1351); `content: "\f1c2   描述"` (original L1353) → `"\f1c2   説明"` (candidate L1355); `content: "标签"` (original L1415, the page-tags label) → `"タグ"` (candidate L1417); `content: "页面信息"` (original L1469, the page-options label) → `"ページ情報"` (candidate L1471). The commit's four hunks are exactly these lines (plus item 44's), and a `content:` scan of the current candidate finds no remaining Chinese chrome string. One neighbour line is worth separating from the charge: the CSS comment `/* 页面信息 */` above the page-options rules stands untranslated in the candidate (candidate L1450, from original L1448). It is a comment — porter-visible only, never rendered — so it was not part of the item and its survival does not qualify the closure; it is recorded here so a reviewer who greps for the string finds the distinction already made (the R1 comment half of section 6).

### Item 44 re-derived (ledger class H)

The charge: prose links still led to the CN site or a personal wiki where JP counterparts exist, charged MISSED under pattern 11 — the Basalt link (ledger-cited at the then-current L50), the sigma-plus link (L52), and the betterbetterfootnote link (L56), with the JP candidates theme:basalt-jp, component:sigma-plus-jp, and component:betterbetterfootnote-jp all existing and no wave having repointed them. FIX5-TEXTA §8 (same commit) converted all three from URL form to page-link form at the -jp targets, and the current bytes confirm: `[[[theme:basalt-jp|玄武岩]]]` (candidate L50, from `http://scp-wiki-cn.wikidot.com/theme:basalt`), `[[[component:sigma-plus-jp|Sigma+]]]` (candidate L52, from `https://scp-wiki-cn.wikidot.com/component:sigma-plus`), and `[[[component:betterbetterfootnote-jp|ものすごくすごくすごくすごくすごく良い脚注コンポーネント]]]` (candidate L56, from `https://fendsfox.wikidot.com/component:betterbetterfootnote`). The fix is present and complete; the link text was already Japanese and is unchanged.

### The cobs samples (R3)

Section 8 records the shape; the record here is the census. Original: two live includes with sample data (item CN-3760, level Keter; item CN-3905, level Thaumiel) at original L186–202, one escaped usage exhibit at L204–213, all naming `:fendsfox:component:cobs`. Candidate: no cobs include in any form, and in their place the note at candidate L171, which names the component (CN 支部の fendsfox:component:cobs), states it is not ported to SCP-JP, and states that this port therefore does not handle it. The taxonomy scout's R3 class was defined on this instance among others; the package's judgment is that a stated replacement with the ground in the body meets the documentation standard the class exists to enforce, while a reviewer who disagrees has the full census here to disagree with.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-andesite-jp.txt` — the decoration sample page used by the render checks (its findings are the sample half of section 11(3)). (2) The shared receivers the delivery depends on: `component:sigma-plus-jp` and `component:betterbetterfootnote-jp`, whose candidate pages are the repoint targets of section 3 (the theme's row in `start-themes.tsv` records the dependency: "Sigma+ (via component:sigma-plus-jp; component:betterbetterfootnote-jp also linked)"); rework2-p3 (2d69b1c) is the wave that made this theme a receiver of those shared ports. (3) The follow-up diff artifact for the original's upstream movement (`diff-andesite-from10.txt`, campaign record) belongs to this theme's provenance record (section 12(e)). There is no theme-owned companion fragment: the candidate's stylesheet is its own code block, as the original's was.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the Stage 2 CN1 integration (4a2f4a5) produced the port (translation, credit swap, delivery re-base, the cobs replacement, and the Chinese residue it left in strings and links); rework2-p3 (2d69b1c) attached the shared sigma-plus and footnote receivers; FIX-P4 (f1138e4) repointed the base-theme CSS imports to the JP candidates; and FIX5-TEXTA (6f6b349) closed items 43 and 44 and completed the usage example. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) items 43–44; GOSIGN2-LEDGER-SUPPLEMENT.md rows 43–44; REPORT-GOSIGN2-FIX5-TEXTA.md §8. The go-sign re-run over that record is what the Status block certifies.

## License and attribution

- **Title:** 安山岩 版式
- **Author:** AsWheat
- **Source:** https://scp-wiki-cn.wikidot.com/theme:andesite — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
