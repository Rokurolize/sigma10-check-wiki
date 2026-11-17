# Review package — theme:dream-of-the-stars-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:dream-of-the-stars-jp — origin CN, population #183 [GOSIGN2-LEDGER (b) row 183]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 183]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 218; GOSIGN2-LEDGER (b) row 183]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 337px@320 + 996–999px@320/375 + 1018px@768 (page) and 581–584px@320/375 + 996–1018px (sample); sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 182, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 182]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 183]
- Computed against: canonical commit 8c62b7b5207f684c8373dfe00f28b90427d28027; candidate file pages/theme:dream-of-the-stars-jp.txt sha256:73a4e751db083a973949ea8461ee1e46c91b90796449969338fa22e73d8e71fd; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 183) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×2 and pseudo-ref ×1 (classes (ii)/(iii)); P4 original-state CDN delivery, P5 asset hosting, and P7 font stack (register c3). No defect flag from this package |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:dream-of-the-stars | theme:dream-of-the-stars-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 13 (first translation; the candidate's credit block records 初訳時参照リビジョン: 13) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-dream-of-the-stars.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:dream-of-the-stars-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 746 lines / 22,645 bytes | 763 lines / 24,844 bytes |
| SHA-256 | b9632a15fbe5cfc12f85bb8e43999d679550614b2b945264c1146a006508276d | 73a4e751db083a973949ea8461ee1e46c91b90796449969338fa22e73d8e71fd |

Wave history: the candidate was created by the Stage 2 CN5 integration (commit 04b38eb); the rework2-p4 wave (7d9877c) separated its big third-party bases (the wave record counts 10 inlined pairs for this theme); FIX-CREDIT-D (1869877) normalized its credit attribution; FIX4-IWA (8c62b7b, missing interwiki frames added to 31 themes, KB-07a) added its frame and is the last commit and the stamp's computed-against commit. The original has been superseded upstream since revision 13; the follow-up diff artifact `diff-dream-of-the-stars-from13.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A CN starfield theme (by Mercuresphere) built on Black Highlighter with a separable unfold-sidebar layer and a third-party dustjacket base. The port's delivery work is the story: the head module that imported the theme's own CN code page now imports the JP BHL distribution (scp-jp.github.io), the theme's own code delivery moves to a new tail module (its own JP code page, alongside the dustjacket base kept on its original-state CDN under the P4 disposition), the exhibit's load-bearing jsDelivr import is deleted in favor of the inlined and separated bases from the rework wave, and the frame is added at the gate. The border-image artwork is genuinely rehosted, from a third-party wiki's file area to SCP-JP's own storage wiki. The specimen body is translated in full, the `:lang(cn)` root becomes `:lang(ja)`, the credit-button rule is corrected in place with its ground stated in an inline comment, and the credit block gains a header-image attribution line beyond the eight fields. Measured churn (diff.md, the generator's count: +136/−124 in 67 change blocks / 12 hunks).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 67 change blocks — 36 specific (53.7%), 29 heuristic (43.6%), 2 residue (3.0%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 30 |
| TRANSLATION-ANCHORED | 22 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 3 |
| COMMENT-TEXT | 2 |
| COMPONENT-SWAP | 2 |
| CREDIT-PREVIEW | 2 |
| DRAFT-HOST | 2 |
| LINK-REPOINT | 2 |
| WS-ONLY | 2 |
| ASSET-REHOST | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DUPIMPORT-DEL | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 52 translation labels are the specimen body and prose, counted in section 6; the delivery labels (DELIVERY-HOST, SELF-DELIVERY ×3, DUPIMPORT-DEL) are the base separation of section 3; the 2 COMMENT-TEXT blocks are CSS comments — one translated original comment (B65) and the frame iframe's region — adjudicated in sections 3 and 10; the single CSS-BODY block (B3) is a font-stack conversion, narrated as P7 in section 4 per the standing lesson. The 2 residue blocks are adjudicated in the appendix. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:dream-of-the-stars-jp; original theme:dream-of-the-stars on scp-wiki-cn at reference revision 13; candidate `pages/theme:dream-of-the-stars-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN5 wave (sources.tsv kind: standard; no production JP counterpart exists). Both files open ungated, with delivery modules and the unfold-sidebar layer before the gate (`[[iftags +版式]]`, original L96 → candidate L102); the gate itself is localized, and the frame stands immediately before it (candidate L97–100).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate tag is P2 and the delivery shape is section 3.
- **Verify:** The sources.tsv row for dream-of-the-stars-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's furniture is a bare rate region (`[[>]]` with the rate module) and the `:scp-wiki-cn:credit:start`/`end` pair carrying 作者 [[*user Mercuresphere]] (original L214–224, blocks B5–B7). The candidate deletes the bare rate (BARE-RATE-DEL) and installs the JP form (candidate L220–232): a `:scp-jp:credit:start-preview`/`end-preview` block with the eight ruling-3 fields (title 星の夢テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 星之梦 主题版式; 著作権者 [[*user Mercuresphere]]; 作成年 2022; 初訳時参照リビジョン 13; the source link, section 7) plus a ninth line the eight do not cover: **ヘッダー画像:** with the pixabay illustration URL the header background derives from — the attribution the prose also records (section 7). The section's CSS half is the in-place correction (block B64, T7-CREDIT-CSS): the theme's credit-button rule named `.creditButton > p > a:after` in the original (original L543); the candidate restates the selector as `.creditButton > a:after` (candidate L556), declarations unchanged, with the ground written on the rule's own line: "/* SCP-JP credit module: anchor is a direct child of .creditButton, not wrapped in <p> */".
- **Why:** P3/T1 (KB-09) for the furniture swap (the preview credit block is rate-bearing, so the bare rate is deleted rather than duplicated). T7 by its R6 in-place form (KB-11's frozen-markup mechanism, as amended): an inherited rule corrected to the JP credit DOM, its ground annotated at the rule. The header-image line is ruling-3 TASL substance for an image the credit fields do not otherwise reach.
- **Verify:** Read candidate L220–232 against the eight fields plus the header-image line; `grep -n 'creditButton' candidate.txt` — the corrected selector and its comment.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the selector correction is standing T7 practice.

### 2. Includes and components

- **What:** The usage lines (blocks B13, B15, COMPONENT-SWAP) repoint from `:scp-wiki-cn:theme:dream-of-the-stars` to the bare local form naming this candidate, in both variants the original documents: `@@[[include theme:dream-of-the-stars-jp]]@@` (candidate L293) and the sidebar variant `@@[[include theme:dream-of-the-stars-jp unfold-sidebar=--]]@@` (candidate L297) — the include variable that activates the unfold-sidebar layer survives the port with its name and value form intact. The remaining named includes are the frame (section 3), the credit pair (section 1), and the interwiki iframe's embed region (section 3); every one is `:scp-jp:` or the bare local form.
- **Why:** P1 (KB-15): the snippets a user pastes must name the JP theme page that actually exists, with its documented option variable preserved.
- **Verify:** `grep -n '\[\[include' candidate.txt` — frame, credit pair, and the two escaped usage lines.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery is re-layered in three moves. (1) Head: the original's head module imported the theme's own CN code page (`scp-wiki-cn.wdfiles.com/local--code/theme%3Adream-of-the-stars/1`); the candidate's head module (candidate L1–4) instead imports the JP BHL distribution — normalize and black-highlighter from scp-jp.github.io (block B1, DELIVERY-HOST) — because the base is a separate layer now. The unfold-sidebar module follows in both files, carried unchanged (its marker comment `[!-- {$unfold-sidebar}]` is the original's own, section 10). (2) Exhibit: the CSS exhibit's load-bearing jsDelivr import (original L415) is deleted (block B58, DUPIMPORT-DEL), and the exhibit carries the porter's own-CSS section header (block B57, section 10); the rework2-p4 wave's separation (10 inlined pairs in the wave record) is what the exhibit's current shape embodies. (3) Tail: the candidate adds a delivery module after the gate (block B67, candidate L759–763) importing the crimson-anemone dustjacket.css from its original-state CDN (fastly.jsdelivr.net/gh/Crimone) and the candidate's own code page (`local--code/theme%3Adream-of-the-stars-jp/1` on the draft host) — the own-code delivery the original's head module performed, moved to the tail and repointed. The interwiki iframe in the gated head (block B4, residue) repoints with the frame: from a CN-wdfiles code URL to `//interwiki.scp-jp.org/styleFrame.html?bhl` (candidate L216). **Frame paragraph (the M-frame addition):** the candidate adds the interwiki-style frame immediately before the gate (candidate L97–100) with `priority=1` and `theme=` naming its own code page on the draft host — the own-code form, the base layer being delivered by the head imports rather than through the frame. The frame was absent at the T4 measurement (LOCALIZE-ROWS row 182, pattern 6) and was added by FIX4-IWA (commit 8c62b7b, the KB-07a missing-frame wave), which the ledger records as P6 FIXED.
- **Why:** P4/T2 for the layering (KB-02's delivery class): each base is delivered from its JP or dispositioned source, and the theme's own layer from its own code page. The dustjacket base stays on its original-state CDN under the ledger's P4 disposition (delivery (ii), original-state CDN delivery) — the same class the T4 record's pattern-4 finding (a load-bearing jsDelivr `gh/` base at the measurement candidate's L756) was answered by: the load-bearing base import inside the exhibit is gone, and what remains on a CDN is the separated tail import the disposition names. P6/T3 (KB-07) for the frame; KB-41, class (iii), for the draft-host form.
- **Verify:** Read candidate L1–4, L97–100, and L759–763; `grep -n 'jsdelivr' candidate.txt` — the only hit is the tail's dustjacket import; `grep -n 'scp-wiki-cn.wdfiles' candidate.txt` returns nothing.
- **Disposition:** FIXED (P6); the dustjacket delivery is DISPOSITIONED (P4, class (ii)); the draft-host URL is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts. One stack converts inside the gated head module (block B3, CSS-BODY adjudicated as P7): the colors container's `font-family: zuijinregular, serif` becomes `'Zen Old Mincho', serif` (candidate L120) — the CN-embedded face's name replaced by the JP Mincho face. No load for Zen Old Mincho exists anywhere in the candidate, so the stack's first family is a dead reference and the serif fallback governs; this is exactly the state the T4 record found (LOCALIZE-ROWS row 182, pattern 7: JP webfont not loaded, Zen Old Mincho dead reference), and the ledger dispositions it as P7 DISPOSITIONED (recorded without a display-affecting mark; the T4 bar). The body stack in the exhibit's `:root:lang(ja)` (block B60, candidate L464) reads `Texturina, Optima, Segoe, Segoe UI, Candara, Calibri, Arial, 'Noto Sans JP', sans-serif` — Texturina is the port's body face (the specimen text follows it, section 6), and Noto Sans JP stands in the stack as the Japanese fallback. Assets: the two border-image URLs are genuinely rehosted (blocks B61–B62, ASSET-REHOST): from evernight-aquarium.wdfiles.com (a third-party wiki's file area, the T4 record's pattern-5 direct link) to scp-jp-storage.wdfiles.com — SCP-JP's own storage wiki — under file:3438721-307-flvk/wl_hr.png and file:3438721-307-yhhi/wl_border.png (candidate L506, L513). The remaining original-state references are the T1 baseline's two hotlink errors, dispositioned below.
- **Why:** P7/T5 with KB-16 for the stack conversion; the missing load is recorded with its disposition rather than silently passed over, because the stack conversion without a load is a half-state a future porter may complete. P5 for the assets: rehosting onto the JP storage wiki is the completed form of the class the other candidates in this batch leave dispositioned (KB-58's deferred state), and it is credited as such.
- **Verify:** `grep -n 'Zen Old Mincho' candidate.txt` — the single stack mention, no load; `grep -n 'evernight' candidate.txt` returns nothing; `grep -n 'scp-jp-storage' candidate.txt` — the two rehosted URLs.
- **Disposition:** Rehost applied; the font stack is DISPOSITIONED (P7); the T1 hotlinks are DISPOSITIONED (class (ii) / KB-58; §(c3) P5).

### 5. Header, sidebar, and site furniture

- **What:** The `:root:lang(cn)` block becomes `:root:lang(ja)` (block B60, HEADERVAR; candidate L462–468), carrying the theme's header and body variables into the JP language scope, with the body font of section 4. The unfold-sidebar layer — the theme's signature furniture, a BHL-style dark sidebar delivered by its own module and activated by the usage variant — is carried unchanged in both its module and its documentation (sections 2–3). The render row's overflow figures (section 11) are the wide-layout shapes the layer produces at narrow widths, recorded against the cross-cutting families.
- **Why:** P9/T6: the language-scoped root is the header-variable mechanism this theme uses, and converting its language is what makes the JP variable set apply; P8's check is satisfied by the carried sidebar layer.
- **Verify:** `grep -n 'lang(' candidate.txt` — the single `:lang(ja)` root; `grep -n 'unfold' candidate.txt` — the marker comment, the module, and the usage variant.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The gated prose and specimens are translated in full (52 translation labels over blocks B8–B56). In groups: the theme-color section head (B8); the about prose (B9–B11 — the starfield description, with its two source links repointed and glossed, section 7); the usage prose (B12, B14); the specimens — horizontal rules and the fancyhr form, the fancyborder note, headings 1–6 with their collapsible, the tabviews (including the repeated long-tab text, blocks B29–B49), blockquotes with footnote, and the table (B16–B54); and the font specimen line (B55), whose stated body font follows the port: 本文フォントはTexturina / ブラウザ既定フォントです。 where the original named Skolar Sans. One CSS comment inside the exhibit is translated with the code (block B65, COMMENT-TEXT: the "collapse the user-info and search bars by default" section header). Simplified Chinese survives only in the credit block's original-title field （星之梦 主题版式）.
- **Why:** P10 (body and specimen translation), KB-18 (reader-visible strings). The font specimen line is the standing lesson's prose-follows-bytes case in its benign form: the specimen describes the theme's fonts, so when the port changes the body face the specimen text changes with it, and the two agree (candidate L406 with L464).
- **Verify:** Read candidate L235–409 against original L227–401 (the gated body before the source-code section); a simplified-only-character scan of candidate.txt returns only the original-title field.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The credit source link (candidate L229) names `https://scp-wiki-cn.wikidot.com/theme:dream-of-the-stars` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. The about prose's two links (blocks B10–B11, LINK-REPOINT) keep CN targets with （中国語版） glosses: the flowing-night-sky theme (the header background's source theme, candidate L287) and the wanderers-station page (candidate L289, where the original used an interwiki `wanderers:` link and the candidate writes the full scp-wiki-cn URL the record carries). The header-image attribution link (pixabay) stands in the credit block (section 1).
- **Why:** P11: prose links take the JP counterpart or the serving original under the dead-reference evidence standard; origin-documenting links to the source branch are glossed, as in this batch's doap-bhl package.
- **Verify:** Compare candidate L229's host against the sources.tsv row's original_url host (scp-wiki-cn.wikidot.com) — identical; read candidate L287–289.
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds for the gated body: variable names, selectors, and channel order are preserved, the specimens stand in the original's order, and an exhibit census finds every specimen present (rules, headings, tabviews, blockquotes, table, source-code exhibit). The structural events are at the delivery layer, not the body: the head module's import changes layer (section 3), the tail delivery module is added (B67), and the exhibit loses its jsDelivr import (B58) and gains its own-CSS section header (B57). One line at the exhibit's tail (block B66, original L741) is not carried; it is a spacing line beside the `/* ----END---- */` marker, which itself is carried.
- **Why:** R3's census decides exhibit questions; here it confirms preservation, and the delivery-layer moves are P4 events recorded in section 3 rather than structural deletions.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[collapsible\|\[\[code\|\[\[module' original.txt candidate.txt` — the sequences correspond, with the tail module the only addition.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two whitespace-only blocks (B59, B63; WS-ONLY primaries): trailing-space removals on two CSS declaration lines inside the exhibit (candidate L449, L549). No re-indentation blocks exist.
- **Why:** R7: whitespace churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 2, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two porter items, both inside the exhibit. (1) The own-CSS section header (block B57, candidate L416–421): a six-line CSS comment opening "/* ===== dream-of-the-stars-jp：テーマ独自の CSS（…" that marks where the theme's own CSS begins inside the separated exhibit — the rework wave's signpost. (2) The inline comment on the corrected credit rule (candidate L556, section 1), stating the JP credit DOM ground. The candidate's two `[!-- --]` comments are NOT porter annotations: the `{$unfold-sidebar}` marker (candidate L6) and the empty comment (candidate L95) stand at the same positions in the original (original L5, L94) and are the theme's own constructs, carried. The exhibit's remaining CSS comments (23 comment lines in total) are the original's own, one of them translated (section 6).
- **Why:** R2: porter-added text is part of the change record; the check was run explicitly, and carried original comments are distinguished from added ones rather than lumped together.
- **Verify:** `grep -n '\[!--' candidate.txt original.txt` — the same two positions in both; read candidate L416–421.
- **Disposition:** Standing (checked, enumerated).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's three errors: the two hotlinks are class (ii) (original-state references), the one pseudo-ref is class (iii) (the not-yet-posted self-reference class); neither is a class (i) error. (2) The render row's items (RENDER-ROWS-2, RENDER-S2-E (CN5)): the page and sample overflow figures (337px and 996–1018px across widths and engines) are the cross-cutting wide-layout families (KB-33/KB-34), and the sample's credit-modal errors are the preview form's property (KB-32, ruling 5) — all DISPOSITIONED, none charged to the candidate. (3) P4 original-state CDN delivery (the dustjacket tail import): DISPOSITIONED (delivery (ii)). (4) P7 font stack (the unloaded Zen Old Mincho reference): DISPOSITIONED (recorded without a display-affecting mark; the T4 bar), section 4.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–4 as stated).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 218): exit 1, 3 errors / 1 warn / 1 info (hotlink×2, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-E (CN5)): FINDINGS, every item dispositioned (section 11 item 2); engine coverage full. (c) T4/T5 (LOCALIZE-ROWS row 182): FINDINGS jointly, display-affecting findings 4 — the load-bearing jsDelivr `gh/` base (pattern 4; answered by the base separation and the P4 disposition, section 3), the evernight-aquarium direct link (pattern 5; since rehosted to SCP-JP storage, section 4), the absent interwiki-style (pattern 6; since FIXED by FIX4-IWA), and the unloaded JP webfont reference (pattern 7; dispositioned, section 4). The ledger §(c3) line records the outcomes: P4 DISPOSITIONED, P5 DISPOSITIONED, P6 FIXED, P7 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +136/−124 in 67 change blocks / 12 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:dream-of-the-stars-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 183; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports 2 residue blocks; both were adjudicated against the bytes:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B4 | 210-210 → 216-216 (body → body) | no signature | The interwiki iframe `src` repoint, CN-wdfiles code URL → `//interwiki.scp-jp.org/styleFrame.html?bhl`; section 3 |
| B66 | 741-741 → at 754 (code-css → code-css) | no signature | One spacing line at the exhibit's tail, beside the carried `/* ----END---- */` marker; section 8 |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-dream-of-the-stars-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row); it belongs to this theme's record but carries no port change of its own to explain here. The rehosted border images live in the SCP-JP storage wiki's file area (section 4), outside this repo. There are no companion fragments and no shared base file; the BHL base arrives from the JP distribution the head module imports.
