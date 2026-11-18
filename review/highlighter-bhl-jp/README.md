# Review package — theme:highlighter-bhl-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:highlighter-bhl-jp — origin CN, population #196 [GOSIGN2-LEDGER (b) row 196]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 87cdb659aefea29934eb148450a2f32a191ffe3d38d0e33bcd74be0a8adf139e); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 7 warns / 1 info (pseudo-ref×3, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 179; GOSIGN2-LEDGER (b) row 196]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page page-overflow 467px@320 + 495px@375 chromium and 430px@320 + 458px@375 webkit, runtime-hotlink site-theme chain only; sample credit-modal (preview-form), page-overflow 467px@320 + 495px@375 chromium and 430px@320 + 419px@375 webkit, runtime-hotlink site-theme chain + sample font host; T3 clean on both pages (sidebar left JP position, opens in both engines; preview-notice clipping and overflow cross-cutting); sample webkit *-full.png absent (screenshot set incomplete, 32767px cap). [RENDER-ROWS-RERUN16 (CN7) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN7)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 195, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 195]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 196]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:highlighter-bhl-jp.txt sha256:87cdb659aefea29934eb148450a2f32a191ffe3d38d0e33bcd74be0a8adf139e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 196) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 and hotlink ×1 (the EN-host logo, P4 class (ii)); the rerun render row's items (section 11). **One defect flag from this package:** the usage snippet names this theme without its `-jp` suffix (candidate L59; per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:highlighter-bhl | theme:highlighter-bhl-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 16 (the candidate's credit block records 初訳時参照リビジョン: 16) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-highlighter-bhl.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:highlighter-bhl-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 648 lines / 27,587 bytes | 685 lines / 30,697 bytes |
| SHA-256 | 09b7c8a11f9c1e07a1ab3a89c40b2d4a9a11ee00af3d5be8b9bdaa6d2ef27c6b3 | bc9df80bd78be23e16f0dda656c8ada794ee011c175f5a8c261144bc91ab2060 |

Wave history (git log for the candidate file): created by the Stage 2 CN7 integration (6d745e5); FIX-CREDIT-D (1869877) normalized the credit block's translator field; and the last commit touching the file, FIX4-IWA (8c62b7b, the stamp's computed-against commit), added its missing interwiki frames and restored its croqstyle include. The original has been superseded upstream since revision 16; the campaign's follow-up diff artifact is diff-highlighter-bhl-from16.txt (class K5a-i). The theme is a Black Highlighter variant layer (sources.tsv kind: standard); its diff covers its own layer only.

## Summary

A highlighter variant of Black Highlighter from the CN branch: a variable layer and specimen body over the BHL base, its own CSS carried on the original page as a live shown module. The port converts that delivery to the JP form (base include, head module importing its own exhibit block, the BHL frame stack), translates the specimen entire (including the original specimen's repeated lines, translated as found), restores one component include the first port had dropped (croqstyle, FIX4-IWA), and adds a license box the original never carried. The T4 lane charged four display-affecting findings; each has a visible outcome: the frame duplication is the adjudicated alignment (section 3), the EN-host logo is the dispositioned class (ii) form (section 4), the missing Croq-style include is restored (section 2), and the consistency items (two names for the theme, three orphan labels) stand as charged and are recorded where they live. One defect flag arises from this package's own checks: the usage snippet's self-reference (per-theme record). Measured churn (diff.md, the generator's difflib count with autojunk off: +192/−160 in 68 change blocks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 68 change blocks — 30 specific (44.1%), 35 heuristic (51.5%), 3 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 40 |
| TRANSLATION-ANCHORED | 20 |
| INCLUDE-REPOINT | 4 |
| DRAFT-HOST | 4 |
| IFTAGS | 3 |
| COMMENT-TEXT | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 40 TRANS-UNANCHORED blocks are the specimen translation (section 6), each verified line by line; the two EXHIBIT-RESTRUCTURE primaries are the head consolidation (block B3, section 3) and the credit-furniture zone (block B9, section 1), neither an exhibit change. The single CSS-BODY block is a variable-value line inside the delivered exhibit. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:highlighter-bhl-jp; original theme:highlighter-bhl on scp-wiki-cn at reference revision 16; candidate `pages/theme:highlighter-bhl-jp.txt`. Provenance route: derived from the original at the reference revision by the CN7 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The theme is a variant layer over Black Highlighter: its own contribution is a variable set (its `--theme-name`, accent system, and logo variables) plus the specimen body, and its original delivery rides a shown CSS module (section 8).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the variant anatomy decides how sections 3 and 4 are read.
- **Verify:** The sources.tsv row for highlighter-bhl-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery is recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a right-aligned block (original L16–29): the labels **评分：**, **评分模块与著作信息模块：**, **著作信息模块：**, a bare `[[module Rate]]`, and the CN credit trio (`:scp-wiki-cn:credit:start` / `more` / `end`). The candidate deletes the trio and the bare Rate (blocks B6–B8) and installs the JP form inside its `[[iftags +テーマ]]` gate: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L21–30) carrying the eight ruling-3 fields (title マーカー・ブラック テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 标记笔 黑标主题版式; 著作権者 in the same-creator form, "原語版ページの作成者に同じ（scp-wiki-cn の theme:highlighter-bhl）"; 作成年 2023; 初訳時参照リビジョン 16; the source link, section 7). On the author question the bytes are complete: the original's credit apparatus names no individual, and its prose names the creator — "[[*user Liurd]]が制作した" (candidate L53, carried from the original's own intro) — so the attribution a reader needs is present in the file on both sides, and the field's deferral to the original page drops nobody the apparatus named. The three furniture labels survive the modules they headed (candidate L41, L43, L45), standing over the theme-squares include and the intro prose; the T4 lane charged them as orphan labels (LOCALIZE-ROWS row 195), and they stand as charged. The candidate also adds a license box the original never carried (candidate L678–683): a `:scp-jp:component:license-box-backend` pair whose author parameter repeats the same-creator form and whose note states the re-hosting and author-confirmation terms, the same addition as gsk's.
- **Why:** P3/T1 (KB-09) for the swap (the preview module is rate-bearing; the CN trio is ledger class C residue); ruling 3 for the fields; the license box is porter hygiene for a theme that re-hosts assets (section 4).
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns only the preview pair; read candidate L21–30 against the eight fields, L41–53 against original L16–53, and L678–683 for the added box.
- **Disposition:** Swap standing; labels charged by T4 and retained as charged (minor, recorded here); license box added by the port.

### 2. Includes and components

- **What:** The include census divides three ways. (1) The base include and the credit pair (sections 3 and 1). (2) The component trio the theme loads with itself, repointed from the EN prefix to the JP prefix (original L266–268 → candidate L271–273): `:scp-jp:component:croqstyle`, `:scp-jp:component:betterfootnotes`, `:scp-jp:component:toggle-sidebar-bhl` — the same three the prose lists as loaded with the theme (candidate L83–85, their links repointed to scp-jp in the LINK-REPOINT block). The croqstyle include is the section's history: the first port dropped it while keeping the prose claim, the T4 lane charged the mismatch (the prose at L84 against an implementation without it), and FIX4-IWA (8c62b7b, whose message records "croqstyle restored") put it back — in the current bytes the prose and the implementation agree. (3) The specimen's own includes (the theme-squares include at candidate L47–51, its color names translated; the image-block example at L88–91, its file repointed to the candidate's own area) are specimen content, carried as found. The usage snippet's self-reference is flagged in the per-theme record.
- **Why:** P1 (KB-15): includes name the JP page that actually exists — and a theme's prose about its own loading is part of its contract, which is why the croqstyle gap was a charge and its restoration a fix.
- **Verify:** `grep -n '\[\[include' candidate.txt` against original.txt's list; `git show 8c62b7b -- pages/theme:highlighter-bhl-jp.txt` shows the restoration.
- **Disposition:** Repoints applied; the croqstyle gap FIXED (FIX4-IWA).

### 3. Delivery and code loading

- **What:** The original's delivery: a head module importing normalize and black-highlighter from the CN mirror host (bhl.scpwikicn.com, original L2–5), one sidebar frame delivering the CN interwiki style sheet (original L7–12), and its own CSS as a live shown module (`[[module CSS show="true"]]`, original L271–646). The candidate: the base include (candidate L1); a head module importing its own block /1 from the draft host (candidate L3–5), the exhibit converted to a `[[code type="css"]]` block (candidate L281–675) so the import delivers it; and the frames below. **Frame paragraph (the M-frame addition):** the candidate carries four interwiki-style frames. Three form the standard stack at candidate L7–18 (priority 1: normalize.min.css; 2: black-highlighter.min.css, both from scp-jp.github.io; 3: own /1 from the draft host), added by FIX4-IWA (8c62b7b, "missing interwiki frames added to 31 themes (KB-07a)"). The fourth (candidate L32–37, below the credit block) is the original's own sidebar frame carried over: the same type=sidebar, override=1 shape, its `theme=` repointed from the CN interwiki sheet to the JP BHL sheet (block B5), and its priority renumbered 0 → 2 (block B4), aligning it with the head stack's BHL leg (also priority 2) that it overrides, later in document order. The T4 lane charged the pair as a duplication (型 6); the ledger records P6 FIXED — the stack's arrival is the fix, and the sidebar frame's alignment is the same form FIX4-IWB recorded for gsk's override. The exhibit's head carries the porter banner (section 10) and the JP font loads (section 4).
- **Why:** P4/T9 for the delivery repoints; P6/T3 (KB-07) for the frame stack and the override's alignment. The shown-module form has no JP counterpart convention; the code-block-plus-import form is the campaign's standard own-delivery (the same shape as dear-dictator's and gsk's).
- **Verify:** Read candidate L1–37 against original L1–12; `grep -n 'module CSS\|code type' candidate.txt original.txt` for the delivery forms.
- **Disposition:** FIXED (P6, FIX4-IWA).

### 4. Fonts and assets

- **What:** Fonts: neither side declares a `font-family` anywhere (0 lines in each file) — this layer's typography is variable-driven, its stacks living in the base's CSS. The port adds the JP font supplement inside the exhibit (candidate L292–293: Noto Sans JP and Noto Serif JP from Google Fonts, the JPFONT-LOAD block), the standard JP supplement form for a BHL layer, so the faces the base's JP stacks name are loaded by the theme's own delivery as well. No P7 charge is on record for this theme. Assets: one charged item. The body's displayed logo (candidate L39) is an `[[image]]` of the base theme's logo file on the EN host (scp-wiki.wdfiles.com, theme:black-highlighter-theme's black-highlighter-logo.svg) — the T4 lane charged it as a 型 4/5 EN-host hotlink, and T1's single hotlink error is the same line. The ledger dispositions it P4 DISPOSITIONED (delivery class (ii)): the image is the base theme's own logo, displayed by a variant of that base, and the direct-link form is the class the campaign's asset rule allows for a serving original's file. The specimen's own image (candidate L89) repoints to the candidate's draft-host file area (foundation-logo.svg), and the CSS `--logo-image` variable keeps the original's EN-host minimalist-bhl logo URL as its default value (a variable a page overrides, carried as data).
- **Why:** P7's supplement form for the loads; P5/KB-17 with the class (ii) exception for the logo, whose ground is that the file is the base's own mark, not a third-party asset.
- **Verify:** `grep -n 'font-family' candidate.txt` returns nothing; `grep -n 'scp-wiki.wdfiles' candidate.txt` returns the L39 image and the logo variable; T1-ROWS row 179 records the hotlink.
- **Disposition:** DISPOSITIONED (P4, class (ii)); loads standing.

### 5. Header, sidebar, and site furniture

- **What:** The theme's furniture is its variable layer: the exhibit's `:root` sets the theme's identity variables (`--theme-base`, `--theme-id: "highlighter-bhl"`, `--theme-name`) and its accent system, carried from the original with its values intact (the HEADERVAR and CSS-BODY spans ride inside the delivered exhibit). The customization documentation (candidate L62–77) teaches the `:root:lang(ja)` override form for a page's own header title and subtitle — documentation, carried translated. The sidebar furniture is the base's, with this theme's toggle arriving by its own include (section 2). The T5 consistency item lives here as much as in section 6: the theme is named two ways — the credit block's title (candidate L22, マーカー・ブラック テーマ) and the prose's name for it at candidate L81 (ハイライターテーマ, in the loaded-components sentence) — charged by the T4/T5 row as a naming inconsistency and standing as charged; a reader meets both names within sixty lines.
- **Why:** P8 for the furniture carry; the naming item is a T5 consistency charge, recorded where a reviewer will meet it.
- **Verify:** Read candidate L22 and L81; read the exhibit's opening `:root` (candidate L296–310) against original L274–288.
- **Disposition:** Standing; the two-names item charged by T5 and retained as charged (minor).

### 6. Text translation

- **What:** The specimen body is translated entire: 20 TRANSLATION-ANCHORED and 40 TRANS-UNANCHORED primary blocks, each verified line by line — the intro, the customization documentation, the loaded-components list, and the heading/tab/table specimens. As with gsk (the two themes share the CN BHL specimen lineage), the translation is faithful to the original's own accidents: the tab specimen's repeated line (original L120–134, the same sentence eight times) is translated eight times (candidate L126–140), not tidied. The theme-squares include's color names are translated in place (candidate L48: 蛍光レッド）. Simplified Chinese survives only as quotation and data: the credit block's original-title field (candidate L25), the exhibit banner's title line (candidate L284), and the CSS identity variables' Chinese values (`--theme-base: "黑色标记笔"`, `--theme-name: "标记笔"` — variable values the base's CSS consumes as data, carried unchanged).
- **Why:** P10 (the specimen is the theme's documentation of itself) and KB-18 (reader-visible strings); the variable values are data, not prose, and changing them would change what the base renders.
- **Verify:** The pairs are diff.md's body sections in order; a Hanzi scan of candidate.txt returns only the survivals listed.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** Three link matters. (1) The credit block's source link (candidate L29) names `https://scp-wiki-cn.wikidot.com/theme:highlighter-bhl` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. (2) The loaded-components list's links (candidate L83–85) repoint from the CN host to the components' scp-jp pages (the LINK-REPOINT block) — the JP components exist as pages, so the links name serving JP targets. (3) The specimen's outbound example links are carried translated as specimen content. No P11 sibling-link item arises for this theme: its prose links all have JP targets.
- **Why:** P11 under the dead-reference evidence standard: each link names the serving page for its subject, the original for the source link and the JP components for the component list.
- **Verify:** Compare candidate L29's host against the sources.tsv row's original_url host (scp-wiki-cn.wikidot.com) — identical; read candidate L83–85 against original L77–79.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds. The candidate's components correspond to the original's: head module, frames, credit gate, specimen body, component trio, and the CSS — with one form change, the CSS's conversion from a live shown module (`[[module CSS show="true"]]`, original L271–646) to a code exhibit delivered by the head import (candidate L281–675), which is a delivery-form change (section 3), not a content change: the exhibit census finds the full variable layer and rule set on both sides in the same order, and the classifier's two EXHIBIT-RESTRUCTURE primaries adjudicate to the head consolidation and the credit zone. The gating changes form with the family: the original wraps its body in `[[iftags +版式]]` (original L1–264), the candidate gates its credit-through-license-box body under `[[iftags +テーマ]]` (candidate L19–685) with its delivery ungated. One vestige rides inside the body on both sides: a hidden div (gated `-テーマ` / `-版式`) wrapping an empty collapsible (candidate L274–277, original L269–271) — the probable referent of the T4 row's truncated final item ("空…", an empty item), carried identically, visible to no reader.
- **Why:** R3 exists to force exactly this adjudication; the census, not the label, decides, and here it decides for a form change with content carried.
- **Verify:** Compare `grep -n '\[\[module\|\[\[code\|iftags' original.txt candidate.txt` — the sequences correspond, with the delivery conversion the only structural event.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 68 blocks, so the R7 follow-up-diff hazard is not triggered. (The 3 residue blocks are content, adjudicated in the appendix.)
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations. (1) The exhibit banner (candidate L283–286): "标记笔 黑标 / Highlighter BHL Theme / Ported for SCP-JP (theme:highlighter-bhl rev 16 on scp-wiki-cn)" with its Japanese continuation stating the file holds the theme's own layer — porter-visible provenance; the TASL record proper is the credit block (section 1). (2) The license-box note (candidate L681, section 1): the re-hosting and author-confirmation statement. The candidate has no `[!-- --]` notes and no translator's notes in the body (its one omission-class decision, none, needed none).
- **Why:** R2: porter-added text is part of the change record.
- **Verify:** Read candidate L283–286 and L681.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's three pseudo-ref errors: the candidate's own not-yet-posted references (its head import and frame 3) — classes (ii)/(iii), posting-procedure and draft-form. (2) T1's hotlink error, the EN-host logo of section 4: DISPOSITIONED (P4, delivery class (ii)). (3) The rerun render row's items (RENDER-ROWS-RERUN16, CN7, which supersedes the first render row for this theme under rule S1): page-overflow readings on both pages in both engines (467–495px at mobile widths, recorded against the cross-cutting items the row names), the runtime-hotlink site-theme chain (the environment's own chain, not this candidate's text), the sample's credit-modal errors (KB-32, preview form, ruling 5), and the sample's incomplete webkit screenshot set (a capture cap, 32767px, not a page property). (4) The charged consistency items (three orphan labels, section 1; two theme names, section 5) stand under the ledger determination without separate disposition lines; they are recorded where they live so the determination is read against the facts. The usage-snippet flag (per-theme record) is not in this list: no ledger line dispositions it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); item 4 recorded as charged-and-standing.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 179): exit 1, 4 errors / 7 warns / 1 info; the errors are pseudo-ref ×3 (classes (ii)/(iii)) and hotlink ×1 (the section 4 logo, class (ii)); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-RERUN16, lane CN7 — the rerun record, which the stamp follows under supersession rule S1 in place of RENDER-ROWS-2): FINDINGS, the items of section 11(3), all dispositioned; engine coverage full (chromium and webkit, both pages); T3 clean on both pages (the row records the sidebar in its JP position, opening in both engines). (c) T4/T5 (LOCALIZE-ROWS row 195): FINDINGS jointly, display-affecting findings 4 — the EN-host logo （型 4/5), the frame duplication （型 6), and the consistency group （型 T5: the missing Croq-style implementation, since restored; the two theme names; the three orphan labels; and a final item the vendored row truncates at "空…", whose probable referent is the empty collapsible of section 8). The ledger §(c3) line records the outcomes: P4 DISPOSITIONED, P6 FIXED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +192/−160 in 68 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:highlighter-bhl-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 196; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports 3 residue blocks; all were adjudicated against the bytes:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B4 | 9-9 → 34-34 (body → body) | no signature | The sidebar frame's priority renumbering (0 → 2); section 3 |
| B5 | 11-11 → 36-36 (body → body) | no signature | The sidebar frame's `theme=` repoint (CN interwiki sheet → JP BHL sheet); section 3 |
| B64 | 264-264 → 269-269 (body) | no signature | The original's `[[/iftags]]` gate close, re-sited by the section 8 gating change; no content |

The 35 heuristic blocks are the specimen translations counted in section 6 and the credit-zone and exhibit-head blocks counted in sections 1 and 3.

## Per-theme record

### The usage snippet names this theme without its suffix (defect flag)

The usage snippet (candidate L57–60) is the code a reader copies to adopt the theme, and its second line reads `@@[[include :scp-jp:theme:highlighter-bhl]]@@` (candidate L59) — the original's page name under the JP prefix, without the `-jp` suffix this candidate's own name, file name, head import (candidate L4), and frame URL (candidate L17) all carry. The snippet's first line (the base include, candidate L58) is correct, so the pair as written includes a base and then a page that will not exist under that name. Probes run for this package (2026-11-17): neither name is posted yet, so the probe cannot settle intent; what the bytes settle is the inconsistency with the candidate's own identity. No ledger line dispositions the snippet's name (the T1 pseudo-ref classes cover references to the not-yet-posted page itself, which this is not, on the bytes). The candidate is left exactly as it stands, per the standing rule for fix lanes; the repair, if the coordinator confirms it, is the repoint of candidate L59 to theme:highlighter-bhl-jp, after which this package's diff.md and stamp need no change beyond regeneration (the candidate file's hash in the stamp would change).

### Charged items whose bytes stand as charged (for the record)

Two T4/T5 charges remain visible in the candidate under the ledger determination, recorded here so the package does not read as if they had been repaired. (1) The three orphan credit labels at candidate L41, L43, and L45 stand over the theme-squares include and the intro prose, their modules deleted into the credit block (section 1). (2) The theme is named マーカー・ブラック テーマ in its credit block (candidate L22) and ハイライターテーマ in its prose (candidate L81) (section 5). Neither is re-flagged as a defect: both were seen by the sweep, charged, and closed at the ledger determination. They are listed because a reviewer comparing this package against the T4/T5 row will find them, and the package should say why they are still there. The row's remaining charges do not stand: the Croq-style implementation gap was repaired by FIX4-IWA (section 2), and the frame duplication is the adjudicated form (section 3).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-highlighter-bhl-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. There is no companion file and no shared base file beyond the Sigma-10 base itself.

## License and attribution

- **Title:** 标记笔 黑标主题版式
- **Author:** 原語版ページの作成者に同じ（scp-wiki-cn の theme:highlighter-bhl）
- **Source:** https://scp-wiki-cn.wikidot.com/theme:highlighter-bhl — revision 16
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
