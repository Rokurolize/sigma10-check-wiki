# Review package — theme:deserted-years-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:deserted-years-theme-jp — origin CN, population #182 [GOSIGN2-LEDGER (b) row 182]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 182]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 1 warn / 1 info (hotlink×7); standing classes dispositioned in register c1 [T1-ROWS row 217; GOSIGN2-LEDGER (b) row 182]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only (cleanest run of the 17); sample credit-modal (preview-form), page-overflow 335px@320 chromium + 334px@320 webkit + 884px@768 both engines (cross-cutting static-credit), runtime-hotlink site-theme chain + sample font host; T3 complete in the final report (pending in the partial) and clean on both pages (page credit modal opens; sample black-on-black redaction by design; subtitle doubling + preview-notice clipping cross-cutting). [RENDER-ROWS-RERUN16 (CN5) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN5)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 181, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 181]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 182]
- Computed against: canonical commit 8c62b7b5207f684c8373dfe00f28b90427d28027; candidate file pages/theme:deserted-years-theme-jp.txt sha256:610f5be5af13798f8034b6b7150688a72ef789a5abb3beefbd1727e45b2e4d11; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->


## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 182) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×7 (original-state asset URLs with scheme rewritten, section 11); P5 asset hosting and P11 prose links (section 11). No defect flag from this package: the header `content:` strings the ared package flags were converted here (section 6) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:deserted-years-theme | theme:deserted-years-theme-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 11 (first translation; the candidate's credit block records 初訳時参照リビジョン: 11) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-deserted-years-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:deserted-years-theme-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 443 lines / 10,066 bytes | 447 lines / 10,503 bytes |
| SHA-256 | a7daccab6310d41379e3b55b8e8d5389d5c91107f6bd68cdfc0a95ddac3a288c | 610f5be5af13798f8034b6b7150688a72ef789a5abb3beefbd1727e45b2e4d11 |

Wave history: the candidate was created by the Stage 2 CN5 integration (commit 04b38eb); FIX-CREDIT-D (1869877) normalized its credit attribution; FIX4-IWA (8c62b7b, missing interwiki frames added to 31 themes, KB-07a) added its frame and is the last commit and the stamp's computed-against commit. The original has been superseded upstream since revision 11; the follow-up diff artifact `diff-deserted-years-theme-from11.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A CN story-series theme （廃年， by Dr Hormress) whose port is a CSS-conversion exercise: the exhibit body is small (usage line, three blockquote specimens, a rule specimen) and is translated in place, while the theme's large inherited CSS is converted line by line — the Chinese calligraphy face Zhi Mang Xing is replaced by the Japanese Yuji Syuku in the load and in all five stacks that named it, Noto Serif SC becomes Noto Serif JP in the load and the body stack, seven asset URLs on original-state hosts gain the https scheme, the two header `content:` strings are translated or glyph-converted, and the theme's own credit-button rules are corrected in place to the JP credit DOM. At the head, the CN rating/credit furniture is replaced by the JP credit block and the FIX4-IWA frame. Measured churn (diff.md, the generator's count: +47/−43 in 28 change blocks / 13 hunks). No defect flag arises: this is the batch's cleanest conversion, and its T4 row records the prose as clean with no display-breaking defect.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 28 change blocks — 10 specific (35.7%), 18 heuristic (64.3%), 0 residue, 0 skipped. The heuristic share is high because the classifier's CSS-BODY catch-all absorbs single-line CSS rewrites; every one was adjudicated against the bytes. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CSS-BODY | 13 |
| TRANS-UNANCHORED | 7 |
| IFTAGS | 3 |
| CREDIT-PREVIEW | 2 |
| SELECTOR-CORRECTION | 2 |
| T7-CREDIT-CSS | 2 |
| TRANSLATION-ANCHORED | 2 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| DRAFT-HOST | 1 |
| FONT-IMPORT | 1 |
| GLYPH-FORM | 1 |
| INCLUDE-REPOINT | 2 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 13 CSS-BODY primaries resolve as 6 scheme rewrites (section 4), 6 font-stack rewrites (section 4), and 1 `content:` translation (section 6) — the standing lesson's font-stack case at full strength; the 5 heuristic TRANS-UNANCHORED blocks are one-line specimen translations (section 6); the 2 SELECTOR-CORRECTION blocks are the R6 in-place credit-DOM correction (section 1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:deserted-years-theme-jp; original theme:deserted-years-theme on scp-wiki-cn at reference revision 11; candidate `pages/theme:deserted-years-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 CN5 wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The original opens with its tag gate (`[[iftags +版式]]`, original L1) and hides its CSS module behind a second, negative gate (`[[iftags -版式]]`, original L47); the candidate opens with the added frame (candidate L1–4), and both gates are localized.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gates' tags are P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for deserted-years-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a rating block and a CN credit block (original L2–14): a bare `[[module rate]]` under its 评分模块 label, and the `:scp-wiki-cn:credit:start`/`more`/`end` triple. The candidate deletes both (blocks B1–B3) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L7–20) carrying all eight ruling-3 fields (title 廃年テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 废年 版式; 著作権者 [[*user Dr Hormress]]; 作成年 2021; 初訳時参照リビジョン 11; the source link, section 7). The section's CSS half is the in-place correction (blocks B25–B26, SELECTOR-CORRECTION): the theme's own credit rules name `.creditButton p a` in the original (original L344, L362), styling the anchor through a `<p>` wrapper; the candidate restates both selectors as `.creditButton a` (candidate L348, L366), declarations unchanged — the JP credit module emits the anchor as a direct child, so the inherited rules would not have matched.
- **Why:** P3/T1 for the furniture swap (the preview credit module is rate-bearing, so the bare rate module is deleted rather than duplicated, KB-09; the CN credit triple is the foreign form of the same furniture). T7 by its R6 in-place form (KB-11's frozen-markup mechanism, as amended): nothing was added — an inherited rule was corrected to the JP DOM, which is why no supplement block appears in the diff for it. Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module rate\|credit:start\|creditButton' candidate.txt` — the JP preview pair and the two corrected selectors; read candidate L7–20 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the selector correction is standing T7 practice.

### 2. Includes and components

- **What:** One usage-include change (block B4, COMPONENT-SWAP label): the escaped usage line `@@[[include :scp-wiki-cn:theme:deserted-years-theme]]@@` becomes `@@[[include theme:deserted-years-theme-jp]]@@` (candidate L23) — the bare local form naming the candidate itself, without the `:scp-jp:` prefix the ared package's usage lines use; both forms occur in the campaign and the bytes are stated as they are. The candidate's remaining includes are the frame (section 3) and the credit pair (section 1); every named include is `:scp-jp:` or the bare local form.
- **Why:** P1 (KB-15): the snippet a user pastes must name the JP theme page that actually exists; the bare form names this candidate on its own wiki. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, and the one escaped usage line.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The theme's CSS is an inline `[[module CSS]]` block hidden behind the negative tag gate (original L49 → candidate L53), its position and form preserved apart from the dropped `show="true"` attribute (block B11). **Frame paragraph (the M-frame addition):** the candidate adds the interwiki-style frame at the head (candidate L1–4) with `priority=1` and `theme=` naming the candidate's own `local--code/theme%3Adeserted-years-theme-jp/1` on the draft host — the single-layer own-code form, since the theme imports no base distribution. The frame was absent at the T4 measurement (LOCALIZE-ROWS row 181 lists the gap as minor) and was added by FIX4-IWA (commit 8c62b7b, the KB-07a missing-frame wave), which the ledger records as P6 FIXED (frame waves; checker-verified).
- **Why:** P6/T3 (the interwiki-style supplement frame, KB-07): every candidate carries the frame so its own code delivery is named in the JP layering convention. The draft-host form of the theme= URL is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** Read candidate L1–4 and L51–56; `grep -n 'interwiki-style' original.txt` returns nothing.
- **Disposition:** FIXED (P6, FIX4-IWA frame wave); the draft-host URL is DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts, in three moves. Load swap (block B11): the display face's @import converts from `family=Zhi+Mang+Xing` to `family=Yuji+Syuku` (candidate L54, Google Fonts on both sides) — a Chinese calligraphy face replaced by a Japanese one. Load conversion (block B12, JPFONT-LOAD): `family=Noto+Serif+SC` becomes `family=Noto+Serif+JP` with weights and subsets unchanged (candidate L56). Stacks (6 CSS-BODY blocks adjudicated here): the body stack `"Noto Serif SC", "Noto Serif", serif` → `"Noto Serif JP", "Noto Serif", serif` (B14, candidate L62), and the five stacks that named the calligraphy face convert `"Zhi Mang Xing", sans-serif` → `"Yuji Syuku", "Noto Serif JP", serif` (B16 with Oswald kept first, candidate L109; B20, B24, B27, B28 at candidate L194, L245, L391, L399) — each also gains the JP serif as its fallback and takes `serif` as its generic, where the original's generic was `sans-serif`. Assets (6 CSS-BODY blocks, 7 URLs): every asset URL in the theme keeps its host and folder and gains the https scheme — bg-marble.png from the EN about-the-scp-foundation folder (5 lines: candidate L60, L153, L204, L227, L233) and the skyline pair from the EN theme%3Aswirling-ashes folder (candidate L74, two URLs on one line). These seven URLs are the T1 baseline's seven hotlink errors.
- **Why:** P7/T5 with KB-16 (the font load gap): the SC and CN calligraphy faces cannot render Japanese text, so each load and every stack that names it convert together; Yuji Syuku keeps a brush calligraphy face in the display role the original gave Zhi Mang Xing. P5/KB-17 with the c1 http class for the assets: the scheme is rewritten (the class (ii) posting-time rewrite, already applied in the candidate), while the original-state hosts themselves are the deferred hosting state (KB-58).
- **Verify:** `grep -n 'Zhi\|Serif SC' candidate.txt` returns nothing; `grep -n 'http://' candidate.txt` returns nothing; `grep -c 'scp-wiki.wdfiles.com' candidate.txt` counts the seven asset URLs.
- **Disposition:** Font conversions applied; the asset URLs are DISPOSITIONED (class (ii) / KB-58; GOSIGN2-LEDGER §(c3) P5), their schemes already rewritten in the candidate.

### 5. Header, sidebar, and site furniture

- **What:** The header's two rendered strings are `content:` values, converted in section 6 (`SCP FOUNDATION` → `SCP財団`; 废年 → 廃年）. No header variable is overridden (no `--header-title` / `--header-subtitle` / `--logo-image` assignment); the mobile top-bar's open-menu rule is one of the section 4 scheme lines (candidate L233) — the P8 mobile position shape is the original's own rule, carried unchanged apart from its asset scheme. The sidebar rules are carried with only their font and scheme lines converted (sections 4 and 6).
- **Why:** P9/T6 is a per-theme judgment and none was needed; P8's check is satisfied by carrying the original's furniture rules without structural change.
- **Verify:** `grep -n -- '--header-' candidate.txt` returns nothing; the furniture rules correspond one to one in diff.md's hunks.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose and strings, in counted groups. The intro prose (inside block B3): the theme's origin sentence is translated, its three CN-wiki links kept with translated link text and the https scheme (section 7). Five heuristic one-line specimen translations (B5–B9): the three blockquote labels （引用块 → 引用ブロック; 浅色引用块 → 明るい引用ブロック; 深色引用块 → 暗い引用ブロック）, the rule label （分割线 → 区切り線）, and the fancyhr caption, reordered to Japanese syntax. Two `content:` strings: `"SCP FOUNDATION"` → `"SCP財団"` (B17, candidate L127, a translation) and `"废年"` → `"廃年"` (B18, candidate L133, an R5 glyph-form conversion — the theme's own name converted from simplified to Japanese kanji forms, with its surrounding `/* {$deserted}/ … /{$deserted} */` conditional comment carried unchanged). The credit title field takes a translated form （廃年テーマ) while the original-title field keeps 废年 版式 as the work's name. Simplified Chinese survives only in that original-title field.
- **Why:** P10 (body and specimen translation), KB-18 (reader-visible strings, including `content:`), R5 (glyph-form conversion as a named sub-shape). The contrast with this batch's ared package is the point: there the same class of string was carried unconverted and is flagged; here both strings were converted, and the T4 row records this theme's prose as clean.
- **Verify:** `grep -n 'content:' candidate.txt` — the two converted strings; a simplified-only-character scan of candidate.txt returns only the original-title field.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the original-title field.

### 7. Links

- **What:** The candidate's live outbound links are the credit source link and the intro prose's three hub links. The source link (candidate L17) names `https://scp-wiki-cn.wikidot.com/theme:deserted-years-theme` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. The three prose links (candidate L22) keep their CN targets (the 廃年 story hub, the CN about page, the CN swirling-ashes theme) with translated link text and the https scheme: they document where the theme and its background images come from, and the ledger dispositions them as the sibling / batch-posting class (§(c3) P11 DISPOSITIONED).
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; for origin-documenting links to the source branch's own pages, the serving original is the right target, and the ledger's disposition records the class.
- **Verify:** Compare candidate L17's host against the sources.tsv row's original_url host (scp-wiki-cn.wikidot.com) — identical; read candidate L22's three targets against original L16's.
- **Disposition:** Source link standing; the three prose links DISPOSITIONED (P11, sibling / batch-posting class).

### 8. Structure

- **What:** The localize.md closing rule holds in full: variable names, selectors, and channel order are preserved (the 28 blocks are single-line or head/tail changes; the CSS body between them is carried line for line), the gated exhibit body keeps its order, and the JP additions sit at the head. The classifier fires no EXHIBIT-RESTRUCTURE primary for this theme, and an exhibit census confirms why: the usage code div, the three blockquote specimens, and the rule specimen are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise.
- **Why:** R3's census is the deciding check even when the label does not fire; here label and census agree.
- **Verify:** Compare `grep -n '\[\[div\|\[\[module\|\[\[include' original.txt candidate.txt` — the sequences correspond one to one, with the frame include the only addition.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered. The dropped `show="true"` attribute on the CSS module (block B11) is recorded in section 3, not here, because it rides inside the font-load block.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None added. The candidate carries no `[!-- --]` translator notes and no editor line. Its CSS comments are the original's own, including the `/* {$deserted}/ … /{$deserted} */` conditional markers around the theme-title `content:` rule (candidate L129–135), carried unchanged (section 6).
- **Why:** R2: porter-added text is part of the change record; here the check was run explicitly and the answer is none.
- **Verify:** `grep -n '\[!--' candidate.txt` returns nothing; the `/*` lines in candidate.txt all have original counterparts.
- **Disposition:** Standing (checked, absent).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's seven hotlink errors: the original-state asset URLs of section 4 — DISPOSITIONED in register c1 (hotlink, class (ii)) and per-theme as P5 (class (ii) / KB-58); their schemes are already rewritten in the candidate, so what stands is the hosting state, not the scheme. (2) The render row's items (RENDER-ROWS-RERUN16 (CN5), superseding the earlier row by rule S1): the page's only runtime lines are the site-theme hotlink chain (KB-40, environment layer — the row calls it the cleanest run of the 17); the sample's credit-modal errors are the preview form's property (KB-32, ruling 5); the sample's overflow figures are the cross-cutting static-credit shape (KB-33/KB-34); the sample's black-on-black redaction is a deliberate specimen shape (KB-37); subtitle doubling and preview-notice clipping are the shared site-theme shape (KB-35); and T3 was clean on both pages, with the page's credit modal confirmed opening. All DISPOSITIONED or not-charged, none charged to the candidate. (3) The prose links of section 7: DISPOSITIONED (P11, sibling / batch-posting class).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–3 as stated).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 217): exit 1, 7 errors / 1 warn / 1 info; all seven errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-RERUN16 (CN5), superseding the RENDER-ROWS-2 row by rule S1): FINDINGS, every item dispositioned (section 11 item 2); engine coverage full (chromium and webkit, both pages); T3 clean on both pages. (c) T4/T5 (LOCALIZE-ROWS row 181): FINDINGS jointly, display-affecting findings 2 — the three EN-site images direct-linked (the section 4 assets; dispositioned) and the absent interwiki-style (since FIXED by FIX4-IWA, section 3); the row also records the three CN prose links as minor (P11, dispositioned) and states the prose and T5 text are clean with no display-breaking defect. The ledger §(c3) line records the outcomes: P5 DISPOSITIONED, P6 FIXED, P11 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's: +47/−43 in 28 change blocks / 13 hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:deserted-years-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 182; go-sign, COMPLETION-REPORT §10).

## Appendix — residue blocks

The classifier reports no residue blocks for this package. Its non-specific blocks, all adjudicated above, are:

| Block | Range (orig → cand) | Classifier state | Resolution |
|---|---|---|---|
| B5 | 23-23 → 27-27 (body → body) | heuristic TRANS-UNANCHORED | One-line specimen translation (blockquote label); section 6 |
| B6 | 28-28 → 32-32 (body → body) | heuristic TRANS-UNANCHORED | One-line specimen translation (light blockquote label); section 6 |
| B7 | 33-33 → 37-37 (body → body) | heuristic TRANS-UNANCHORED | One-line specimen translation (dark blockquote label); section 6 |
| B8 | 38-38 → 42-42 (body → body) | heuristic TRANS-UNANCHORED | One-line specimen translation (rule label); section 6 |
| B9 | 43-43 → 47-47 (body → body) | heuristic TRANS-UNANCHORED | One-line specimen translation (fancyhr caption); section 6 |
| B13 | 56-56 → 60-60 (module-css → module-css) | heuristic CSS-BODY | Scheme rewrite, bg-marble asset URL; section 4 |
| B14 | 58-58 → 62-62 (module-css → module-css) | heuristic CSS-BODY | Body font-stack conversion, Noto Serif SC → JP; section 4 |
| B15 | 70-70 → 74-74 (module-css → module-css) | heuristic CSS-BODY | Scheme rewrite, skyline asset line (two URLs); section 4 |
| B16 | 105-105 → 109-109 (module-css → module-css) | heuristic CSS-BODY | Display stack conversion (Oswald kept, Zhi Mang Xing → Yuji Syuku); section 4 |
| B17 | 123-123 → 127-127 (module-css → module-css) | heuristic CSS-BODY | `content:` translation, "SCP FOUNDATION" → "SCP財団"; section 6 |
| B19 | 149-149 → 153-153 (module-css → module-css) | heuristic CSS-BODY | Scheme rewrite, bg-marble asset URL; section 4 |
| B20 | 190-190 → 194-194 (module-css → module-css) | heuristic CSS-BODY | Font-stack conversion (Zhi Mang Xing → Yuji Syuku); section 4 |
| B21 | 200-200 → 204-204 (module-css → module-css) | heuristic CSS-BODY | Scheme rewrite, bg-marble asset URL; section 4 |
| B22 | 223-223 → 227-227 (module-css → module-css) | heuristic CSS-BODY | Scheme rewrite, bg-marble asset URL; section 4 |
| B23 | 229-229 → 233-233 (module-css → module-css) | heuristic CSS-BODY | Scheme rewrite, bg-marble asset URL (mobile open-menu rule); section 4 |
| B24 | 241-241 → 245-245 (module-css → module-css) | heuristic CSS-BODY | Font-stack conversion (page-title stack); section 4 |
| B27 | 387-387 → 391-391 (module-css → module-css) | heuristic CSS-BODY | Font-stack conversion (toc title stack); section 4 |
| B28 | 395-395 → 399-399 (module-css → module-css) | heuristic CSS-BODY | Font-stack conversion (toc list stack); section 4 |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-deserted-years-theme-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of the T2/T3 row); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
