# Review package — theme:madoka-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:madoka-jp — origin CN, population #202 [GOSIGN2-LEDGER (b) row 202]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 202]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 95 errors / 2 warns / 1 info (pseudo-ref×95); standing classes dispositioned in register c1 [T1-ROWS row 268; GOSIGN2-LEDGER (b) row 202]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page sidebar-unreachable (4 combos, ≤375) + runtime-hotlink site-theme chain; sample hidden-* cluster at 5 combos (the webkit-1366 capture carries an http.cat-only hotlink line = transient 503; the remaining combos are recorded as-is) + credit-modal (preview-form) + sidebar-unreachable. [RENDER-ROWS-2 (RENDER-S2-F (CN9))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN9))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 201, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 201]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 202]
- Computed against: canonical commit 8c62b7b5207f684c8373dfe00f28b90427d28027; candidate file pages/theme:madoka-jp.txt sha256:132f483118bb9b779d37dc08888f9e0bd9da3cedc2ba17b4b5fac71d8d9e7696; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 202) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×95; the render row's items (section 11); P7 (the font load's families against the stacks' names, T4 bar). **No defect flag from this package:** its usage snippet names the candidate correctly, its credit field names the author, and its one charged font state was seen and dispositioned by the sweep (section 4, per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:madoka | theme:madoka-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 4 (the candidate's credit block records 初訳時参照リビジョン: 4) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-madoka.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:madoka-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 894 lines / 37,195 bytes | 898 lines / 38,857 bytes |
| SHA-256 | 31aabf903d3a5db4a04b27cbcb01b0c1a7db65cfb45cb09b64b | 132f483118bb9b779d37dc08888f9e0bd9da3cedc2ba17b4b5fac71d8d9e7696 |

Wave history (git log for the candidate file): created by the Stage 2 CN9 integration (bbd273c); FIX-CREDIT-D (1869877) normalized the credit block's translator field; and the last commit touching the file, FIX4-IWA (8c62b7b, the stamp's computed-against commit), added its interwiki frame. The original has been superseded upstream since revision 4; the campaign's follow-up diff artifact is recorded with the CN9 lane's records (class K5a-i). The port layers over theme:mox-jp (sources.tsv kind: K5b-3); this package's diff covers the theme's own layer only, and the base's delivery is read through the resolved base where a section says so. This package's diff.md is in the Tier 2 format (hunk index with mechanical hunks folded), the batch's only Tier 2 package.

## Summary

A special theme for a 2025 fantasy-month work (a magical-girl alliance story), built as a layer over the CN mox base theme: a small component-CSS module of its own, a documentation and specimen body, a large CSS exhibit that is its delivery, and a tail module of utility CSS. The port is the batch's most faithful mirror: its four components correspond one-to-one with the original's, in the same order, and its changes concentrate at the supply lines (the base import repointed to mox-jp's block 8, its own assets re-hosted, the CN theme-previewer wrapper dropped) and in the translation, which localizes even the specimen's color-block labels to the JP names of the characters they denote. Its one charged weakness is typographic: the stacks were re-pointed to the JP Noto faces while the load that should deliver them delivers the SC faces instead, and the original's display face lost its delivery entirely (section 4) — charged by the T4 lane as a minor miss and dispositioned at its bar. Measured churn (diff.md, the generator's difflib count with autojunk off; Tier 2 header): the hunk index in diff.md carries the counts.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 64 change blocks — 41 specific (64.1%), 23 heuristic (35.9%), 0 residue, 0 skipped. The batch's highest specific share, because this candidate's delivery repoints are numerous and exact. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DRAFT-HOST | 24 |
| TRANS-UNANCHORED | 22 |
| TRANSLATION-ANCHORED | 14 |
| COMMENT-TEXT | 6 |
| CSS-BODY | 3 |
| DELIVERY-HOST | 2 |
| SELF-DELIVERY | 2 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| COMPONENT-SWAP | 1 |
| GLYPH-FORM | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 24 DRAFT-HOST spans are asset and delivery repoints inside the delivered CSS (sections 3–4), most of them the tail module's icon-sprite URLs; the 6 COMMENT-TEXT spans are CSS comment translations inside the exhibit (section 6); the 3 CSS-BODY blocks are the two font-stack rewrites and one variable line (section 4). After adjudication no block is left unexplained, and there is no residue.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:madoka-jp; original theme:madoka on scp-wiki-cn at reference revision 4; candidate `pages/theme:madoka-jp.txt`. Provenance route: derived from the original at the reference revision by the CN9 wave (sources.tsv kind: K5b-3, layer theme over a ported base; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The theme is a work-specific skin (for the 2025 fantasy-month piece named in its intro) over the mox base: its own layer is a set of color-block components, CSS variables layered on the base's `--mox-*` system, and documentation.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the layer anatomy decides sections 3 and 4 (its fonts are the base's system, extended).
- **Verify:** The sources.tsv row for madoka-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the layering is recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit apparatus is a bare `[[module rate]]` inside a right-aligned block (original L73–75), naming nobody. The candidate replaces the module with the JP form inside the same `[[>]]` wrapper (candidate L74–85): a `:scp-jp:credit:start-preview`/`end-preview` block carrying the eight ruling-3 fields (title 魔法同盟 特殊テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 魔法联盟 特种版式; 著作権者 OxygenNine; 作成年 2025; 初訳時参照リビジョン 4; the source link, section 7). The author field names the theme's creator outright: the original page's own provenance establishes him (the theme is OxygenNine's, its assets served from his file area, oxygen9-files-2, on the CN sandbox — the URLs section 4 re-hosts), so the field records the attribution the apparatus lacked rather than deferring to it. The T4 lane's credit item for this theme was notation-level （クレジット表記， its item #3), and the field as it stands is the completed form. The intro prose below the block (candidate L87) credits the base theme with its link repointed to the JP base candidate (section 7).
- **Why:** P3/T1 (KB-09) for the swap (the preview module is rate-bearing, so the bare module is replaced, not duplicated); ruling 3 for the fields. Where the original's authorship is established by the page's own evidence, the field names the author — the same-creator deferral form is for pages whose authorship the record does not establish.
- **Verify:** Read candidate L74–85 against the eight fields; `grep -n 'module rate' candidate.txt` returns nothing.
- **Disposition:** Standing (the T4 notation item closed at the determination).

### 2. Includes and components

- **What:** The include census is short. The candidate's live includes are the frame (section 3) and the credit pair (section 1); its base arrives by @import, not include (section 3). The usage snippet (block B9, candidate L91) is the batch's clean one: `{{@@[[include theme:madoka-jp]]@@}}`, the unprefixed local form naming this candidate exactly (the original's was the prefixed `:scp-wiki-cn:theme:madoka`). The documentation's component references (the mox-float, mox-card, mox-note preset divs of the specimen) are class names in prose, carried as found. One wrapper deletion rides at the head: the original opens inside a `[[module ThemePreviewer …]]` (original L1–3) pointing at a cloudfront preview URL — a CN-side preview harness for the theme page itself, with no JP counterpart and no function in the candidate's delivery; the candidate drops the wrapper and keeps the head module it wrapped (block B1).
- **Why:** P1 (KB-15) for the snippet's form; the previewer is environment tooling of the original branch, not theme content — its removal is the same class as a check-wiki harness line, recorded here so the deletion is a judged one.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, and the escaped snippet; `grep -n 'ThemePreviewer' candidate.txt` returns nothing.
- **Disposition:** Standing; the previewer wrapper dropped as branch tooling.

### 3. Delivery and code loading

- **What:** Four components, mirroring the original's four in order. (1) The head module (original L3–10 → candidate L1–7) imports the base's block 8 and its own block 1: repointed from scp-wiki-cn.wdfiles.com (`theme:mox/8`, `theme:madoka/1`) to the draft host (`theme%3Amox-jp/8`, `theme%3Amadoka-jp/1`, candidate L4–5, block B2). The base import names the JP base candidate's block 8, the same block number the original imported from the CN base — the layer's contract with its base is unchanged in shape. (2) The component module (original L13–70 → candidate L16–72, inside the gate): the `.madoka-block` color-block CSS, its two asset URLs re-hosted from the author's CN sandbox area to the candidate's own draft-host files (blocks B4–B5). (3) The exhibit (original L250–656 → candidate L261–660): a `[[code type="CSS"]]` block that is the candidate's block /1, hence its own delivery — the variables, the font load, and the rule set (sections 4–5). (4) The tail module (original L663–895 → candidate L667–899): the utility CSS (editor-toolbar icon sprites and the mox component rules), its sprite URLs re-hosted to the candidate's own files (the bulk of the 24 DRAFT-HOST spans). **Frame paragraph (the M-frame addition):** the original carried no interwiki-style frame (LOCALIZE-ROWS row 201, 型 6); the candidate adds one at candidate L9–12 with `priority=1` and `theme=` naming its own /1 delivery on the draft host — the single-layer own-code form, in the spaced parameter style. The ledger records the outcome as P6 FIXED (frame waves; checker-verified); the frame arrived in FIX4-IWA (8c62b7b). The gate changes form with the family: the original's `[[iftags +版式 +原创]]` (theme tag plus original-work tag) becomes `[[iftags +テーマ]]` (candidate L14), the JP gate naming the theme tag alone.
- **Why:** P4/T9 for the delivery repoints; P6/T3 (KB-07) for the frame. The block-8 import is the layer contract: a layer theme that imports a numbered block of its base must name the JP base's corresponding block, and mox-jp's block 8 is that block (the base's own package is its record).
- **Verify:** Read candidate L1–14 against original L1–12; compare `grep -n '\[\[module\|\[\[code' original.txt candidate.txt` — four components each, in the same order.
- **Disposition:** FIXED (P6); delivery standing.

### 4. Fonts and assets

- **What:** Fonts, in the state the T4 lane charged. The prose declares the theme's faces (candidate L254–258): UI font Noto Serif JP / Cinzel, body font Noto Sans JP, mono Oxygen Mono / Noto Sans JP. The exhibit's stacks were re-pointed to those JP names (blocks B38–B39: `--mox-ui-font` and `--madoka-serif` now read `'ZSFT-q', 'Noto Serif JP', 'Noto Serif CJK JP', serif`, and `--mox-text-font` / `--madoka-content-serif` name the JP faces likewise). The load that should deliver them (block B40, candidate L296) is one Google Fonts `@import` delivering Cinzel, Oxygen Mono, and the **SC** forms (Noto Serif SC, Noto Sans SC) — not the JP faces the stacks name. The resolved base does not close the gap: theme:mox-jp's own load (its L554) delivers Noto Sans SC, Oxygen Mono, and Raleway. And the original's display face lost its delivery outright: the original loaded 'ZSFT-q' from a Chinese font service (original L285, fontsapi.zeoseven.com, with its @font-face at L287); the candidate drops that load without replacement, so 'ZSFT-q', still first in two stacks, is loaded nowhere in the candidate or its base, and the UI stack falls through to its second name. The T4 lane charged the JP-face half of this （型 7, recorded as a minor miss: the JP body font is never actually loaded), and the T5 half (its item #1: the prose's declared typefaces against the code's first-named ZSFT-q). The ledger dispositions the class P7 DISPOSITIONED, the row carrying no display-affecting mark — the theme renders in fallback faces, which for CJK text on JP systems means the platform's own serif and sans faces where the Noto JP faces are absent. The bytes stand as charged, and this package records the full chain (prose, stacks, load, base load, dropped load) so the disposition is read against the facts. Assets: the theme's images re-host from the author's CN sandbox file area (scpsandboxcn.wikidot.com, oxygen9-files-2) to the candidate's own draft-host file area, names carried (mdk-bg-7.svg, the icons-2 sprite, iama-logo-dark.svg, madoka-bg.jpg; blocks B4–B5 and the DRAFT-HOST spans throughout the tail module).
- **Why:** P7/T5 with KB-16 states the completed form (load and stacks change together, each stack's first face delivered); this theme's P7 is the dispositioned incomplete form, in both its halves. P5/KB-17 for the asset re-hosting.
- **Verify:** `grep -n 'fonts.googleapis\|zeoseven' candidate.txt original.txt` — the candidate's one load against the original's two; `grep -n 'Noto Sans JP\|Noto Serif JP' candidate.txt` returns stack and prose lines only, no load; `grep -n 'fonts.googleapis' pages/theme:mox-jp.txt` for the base's load.
- **Disposition:** DISPOSITIONED (P7 at the T4 bar, minor).

### 5. Header, sidebar, and site furniture

- **What:** The header variables ride inside the exhibit's `:root`: `--mox-header-title: "I. A. M. A."` carried unchanged, and `--mox-header-subtitle` translated (block B37: "国际反法西斯魔法少女联盟" → "国際反ファシスト魔法少女同盟", the alliance's name in its JP glyph forms). The logo variable re-hosts to the candidate's own file (iama-logo-dark.svg). The sidebar and editor furniture is the tail module's utility CSS (section 3, component 4): the editor-toolbar icon rules and the mox component rules, carried with their sprite URLs re-hosted and their selectors untouched — the classifier's DRAFT-HOST spans in that module are URL repoints inside minified rules, not rule changes (the one long minified line at candidate L658 corresponds rule-for-rule to the original's). The render row's sidebar finding (section 11) is about the assembled page at mobile widths, not about a furniture rule this layer drops.
- **Why:** P8: furniture rules transfer with their assets re-hosted; header strings translate as reader-visible text (KB-18), the alliance name with its glyph forms converted (R5).
- **Verify:** Read candidate L281–296 against original L270–296; `grep -n 'icons-2' candidate.txt` against the original's sprite lines.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The documentation and specimen body are translated throughout: 14 TRANSLATION-ANCHORED and 22 TRANS-UNANCHORED primary blocks (B7–B36), each verified line by line — the intro, the include-parameter documentation, the preset-div catalogue (the repeated "= または" alternative lines, translated as found), the page-element specimens, and the font declarations of section 4. The specimen's most visible localization is its color-block labels (blocks B12–B16): the original's labels are oblique Chinese codenames （秀色， 人鱼， 武旦， 救济， 彼岸）, and the candidate renders them as the JP names of the characters they denote （巴マミ, 美樹さやか, 佐倉杏子, 鹿目まどか, 暁美ほむら) — the theme is a Madoka Magica skin, its blocks are the five magical girls, and the JP text names them as a JP reader knows them. In-CSS comment text (R1): the exhibit's section comments are translated (the 6 COMMENT-TEXT spans ride inside the translation and delivery blocks). Simplified Chinese survives only as quotation and data: the credit block's original-title field (candidate L80) and the exhibit's retained SC font names inside the load itself (section 4).
- **Why:** P10 (the documentation is the theme's operating instructions) and KB-18 (reader-visible strings, including the labels a reader picks a color block by). The label localization follows the same rule as any specimen name: it renders in the form the target branch's readers use.
- **Verify:** The pairs are diff.md's body sections in order; a Hanzi scan of candidate.txt returns only the survivals listed.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** Two link matters. (1) The credit block's source link (candidate L84) names `https://scp-wiki-cn.wikidot.com/theme:madoka` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises; its label is the plain word ソース ("source"), the T4 notation item's subject, standing as the determination left it. (2) The intro's base-theme link (block B7, candidate L87): the original's `[[[theme:mox |…]]]` becomes `[[[theme:mox-jp|mox基礎テーマ]]]` — the unprefixed local form naming the JP base candidate exactly, the correct counterpart of the section 2 snippet. No other outbound links arise; the theme's prose links are its base reference and its source.
- **Why:** P11 under the dead-reference evidence standard for the source link; P1 for the base link, which names the page this port actually layers over.
- **Verify:** Compare candidate L84's host against the sources.tsv row's original_url host (scp-wiki-cn.wikidot.com) — identical; read candidate L87 against original L76.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds in its strongest form in this batch: the topology pass finds the same four components on both sides in the same order (head module, component module, code exhibit, tail module), no component moves kind, and the classifier reports no DELIVERY-MOVE and no EXHIBIT-RESTRUCTURE primary at all. The structural events are the head wrapper's removal (section 2), the gate's tag change (section 3), and the frame's addition (section 3) — all at the head, none interleaved into the inherited CSS. An exhibit census confirms the shape: the variable sets, the font load, the rule set, and the utility module are present on both sides in the same order, so the R3 question does not arise beyond the delivery layer, where section 3 answers it.
- **Why:** R3 exists to force the adjudication; here the census and the topology agree that there is nothing to adjudicate.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code' original.txt candidate.txt` — four components each, same kinds, same order.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 64 blocks, and no residue, so the R7 follow-up-diff hazard is not triggered and the appendix is empty.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0, residue 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None as added prose: the candidate carries no `[!-- --]` notes, no translator's notes, and no porter banner of the kind the batch's other exhibits carry — its exhibit opens directly on its `:root`. The port's decisions are recorded in the campaign record and in this package rather than in the file. (The two in-file statements a reviewer might mistake for annotations are content: the font declarations at candidate L254–258, which are the theme's own documentation, translated, and the credit block, which is furniture.) This section is present, and empty, so the absence is a checked fact rather than an oversight.
- **Why:** R2: porter-added text is part of the change record; where there is none, the section says so with its ground.
- **Verify:** `grep -n '訳注\|SCP-JP版\|Ported for' candidate.txt` returns nothing.
- **Disposition:** None (checked, not overlooked).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's 95 pseudo-ref errors, the batch's highest count: the candidate's own not-yet-posted references, concentrated in its delivered CSS (its exhibit's and tail module's draft-host file URLs, the icon sprite's many rules among them) — classes (ii)/(iii), posting-procedure and draft-form; the count reflects the theme's asset density, not a distinct defect per line. (2) The render row's items (RENDER-ROWS-2, RENDER-S2-F (CN9)): the sidebar unreachable at ≤375px in four combinations on the page and on the sample (the mox family's mobile sidebar behavior, recorded against the assembled page), the sample's hidden-* cluster at five combinations (one webkit capture's hotlink line is http.cat, KB-44, a transient 503 capture, not a result), the sample's credit-modal errors (KB-32, preview form, ruling 5), and the runtime-hotlink site-theme chain (the environment's own chain). (3) P7 DISPOSITIONED: the font load's families against the stacks (section 4). (4) The dropped ThemePreviewer wrapper (section 2) is a deletion with its ground stated there, not a disposition. No defect flag from this package joins this list, because none arose.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 268): exit 1, 95 errors / 2 warns / 1 info; all 95 errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-F (CN9)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage full matrix as run by the lane, not separately caveated in its row. This theme is not one of the 17 rerun themes, so the first render row stands. (c) T4/T5 (LOCALIZE-ROWS row 201): FINDINGS jointly, display-affecting findings 3 — the row's charges are 型 6 (the absent frame, since FIXED by FIX4-IWA) and 型 7 (the unloaded JP body font, minor; section 4), with the T5 items (the prose/code typeface mismatch, section 4; the credit notation, section 1) and the row's positive record that delivery, images, and credit structure are sound with no display-breaking defect. The ledger §(c3) line records the outcomes: P6 FIXED, P7 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off), in diff.md's Tier 2 header and hunk index.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:madoka-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 202; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports no residue blocks for this package (0 of 64). The 23 heuristic blocks are the specimen translations counted in section 6 (the preset-div catalogue's repeated alternative lines among them), the CSS comment translations of section 6, and the font-stack rewrites of section 4 (blocks B38–B39, CSS-BODY primaries).

## Per-theme record

### The font state, charged and dispositioned, recorded in full

This theme's font chain is the one place where the package's evidence runs longer than the ledger's one-line disposition, so it is set out once, in order. The prose (candidate L254–258) promises a reader three faces: Noto Serif JP (with Cinzel) for UI text, Noto Sans JP for body text, Oxygen Mono for monospace. The stacks (candidate L291–296 zone) name those JP faces, each behind or beside 'ZSFT-q' in the UI and serif stacks. The loads deliver none of the JP faces: this file's one load (candidate L296) delivers Cinzel, Oxygen Mono, Noto Serif SC, and Noto Sans SC, and the base's load (theme:mox-jp, its L554) delivers Noto Sans SC, Oxygen Mono, and Raleway. 'ZSFT-q' is delivered by nothing: the original's zeoseven delivery (original L285–292) was dropped and not replaced. The practical consequence is bounded and should be stated plainly: the theme renders, in the platform's fallback serif and sans faces wherever the named faces are absent, and a reader whose system carries the Noto JP faces (many Android devices, some JP Windows installs) gets the designed typography without any load. The T4 lane saw the JP half of this and charged it as a minor miss （型 7); the T5 lane saw the prose half (its item #1); the ledger dispositioned the class (P7) at the bar the row set, which recorded no display-affecting mark. This package does not re-flag it: the sweep's evidence and the package's evidence are the same evidence, and the determination was made on it. It is recorded here at length because the one-line disposition ("P7 DISPOSITIONED") does not tell a reviewer what the font state actually is, and the package's job is to tell them.

## Change set outside the two diffed files

The diff covers the theme's own layer. (1) `pages/theme-decoration-sample-madoka-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. (2) The declared base, theme:mox-jp, is another row's candidate with its own review package; this package reads its block-8 delivery contract and its font load from that file where sections 3–4 say so, and explains no part of it. There is no companion file of this theme's own.

## License and attribution

- **Title:** 魔法联盟 特种版式
- **Author:** OxygenNine
- **Source:** https://scp-wiki-cn.wikidot.com/theme:madoka — revision 4
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
