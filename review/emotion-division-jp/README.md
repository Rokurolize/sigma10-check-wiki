# Review package — theme:emotion-division-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:emotion-division-jp — origin CN, population #186 [GOSIGN2-LEDGER (b) row 186]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 186]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 1 info (hotlink×2, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 221; GOSIGN2-LEDGER (b) row 186]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 497–504px@320/375 on page and sample (+ 884px@768 on sample); page hidden-* cluster (no sidebar-unreachable) confined to chromium-1366, whose only hotlink host is http.cat = transient 503 capture, not a result; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN5))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 184, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 184]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 186]
- Computed against: canonical commit 8c62b7b5207f684c8373dfe00f28b90427d28027; candidate file pages/theme:emotion-division-jp.txt sha256:2aa88cf61a6bafef117ad3e8f26cd1cf23fd6cc10eace0ebd3661de87b7ebb10; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 186) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×2 (class (ii): the borrowed CN sandbox exhibit images, section 4) and pseudo-ref ×1 (class (iii)); the render row's items (section 11); P1/P4/P5/P11 classes (ledger §(c3)). No defect flag from this package |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:emotion-division | theme:emotion-division-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 10 (first translation; the candidate's credit block records 初訳時参照リビジョン: 10) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-emotion-division.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:emotion-division-jp.txt`, copied at worktree HEAD f9cae19 |
| Lines / bytes | 626 lines / 16,189 bytes | 639 lines / 18,299 bytes |
| SHA-256 | 3f075772b3b1f741d13221d25e60f3ad8d499c78e7159e829e7dac43457bf9ff | 2aa88cf61a6bafef117ad3e8f26cd1cf23fd6cc10eace0ebd3661de87b7ebb10 |

Wave history: the candidate was created by the Stage 2 CN5 integration (commit 04b38eb, the LOCALIZE-S2-D wave's port); FIX-CREDIT-D (1869877) normalized its translator field; FIX4-IWA (8c62b7b) added the interwiki-style frame, and is the stamp's computed-against commit. No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. The original has been superseded upstream since revision 10; the follow-up diff artifact `diff-emotion-division-from10.txt` sits in the campaign record (sources.tsv note, class K5a-i / KB-19), and this package judges the port against the reference revision only.

## Summary

A CN aesthetic theme （情感缢裂， "emotion strangled apart") for summer and emotion pieces, ported with its whole apparatus intact: a prose body quoting SCP-CN-2733 and the Aozora Society, a long tab specimen, and a 476-line CSS exhibit. The port's changes are the batch's standard set — CN credit module swapped for the JP preview block, frame added, header variables translated, the sandbox exhibit images kept on their serving host with their scheme upgraded, the theme's own credit-module CSS selectors corrected in place to the JP module's DOM — plus a very large, very regular translation mass: forty unanchored blocks, most of them the tab specimen's repeated lines and the CSS exhibit's section-banner comments. Measured churn (diff.md, the generator's difflib count with autojunk off: +136/−122 in 64 change blocks). No defect flag arises: the credit source link names the recorded host, the credit field names the original's publisher, and the usage line names this candidate's own page.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 64 change blocks — 26 specific (40.6%), 38 heuristic (59.4%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 40 |
| TRANSLATION-ANCHORED | 15 |
| COMMENT-TEXT | 10 |
| SELECTOR-CORRECTION | 4 |
| T7-CREDIT-CSS | 4 |
| CREDIT-PREVIEW | 2 |
| DRAFT-HOST | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| GLYPH-FORM | 1 |
| HEADERVAR | 1 |
| INCLUDE-REPOINT | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 40 TRANS-UNANCHORED blocks are one-line prose, specimen, and comment translations, verified line by line (section 6); the 4 T7-CREDIT-CSS blocks are not a supplement addition but the R6 in-place form — the theme's own inherited credit rules corrected to the JP credit DOM (section 1), which is why SELECTOR-CORRECTION rides on the same four blocks; the single CSS-BODY block (B53) is the sandbox background's scheme upgrade, not CSS churn (section 4); the GLYPH-FORM block (B50) is a CSS banner comment whose change is glyph form plus translation (section 6). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:emotion-division-jp; original theme:emotion-division on scp-wiki-cn at reference revision 10; candidate `pages/theme:emotion-division-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The original's shape: a head delivery module, the gate (`[[iftags +版式]]`, the CN theme tag), a bare Rate and the CN credit pair, prose with a floated exhibit image, the specimen body, and the CSS exhibit (original L148–622); the candidate preserves that shape with the frame inserted ahead of the gate (candidate L5–8).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 and the delivery shape is section 3.
- **Verify:** The sources.tsv row for emotion-division-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2–3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L7–9) plus the CN credit module pair `:scp-wiki-cn:credit:start`/`end` (original L11–14) whose whole body is one line: 发布者：[[*user quisqualis]]. The candidate deletes the Rate (block B3) and swaps the pair for the JP preview form (blocks B4–B6): `:scp-jp:credit:start-preview`/`end-preview` (candidate L12, L23) carrying the eight ruling-3 fields (title 情感縊裂テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 情感缢裂 版式； 著作権者 [[*user quisqualis]]; 作成年 2022; 初訳時参照リビジョン 10; the source link, section 7) — the 著作権者 field names the same publisher the CN pair named, so no one is dropped. The translator field took its ruling-3 form in FIX-CREDIT-D (1869877). The section's CSS half is the R6 correction: the theme's own CSS styles the credit module, and its four anchor rules name the CN module's DOM (`.creditButton p a`, original L586, L589, L605, L610); the candidate corrects all four in place to the JP module's direct-child form (`.creditButton a`, candidate L599, L602, L618, L623), declarations unchanged — blocks B61–B64. There is no license box on either side.
- **Why:** P3/T1 (KB-09) for the furniture swap (the preview credit module is rate-bearing, so the bare Rate is deleted rather than duplicated, and a foreign credit module does not render in the JP environment). T7 in its R6 form for the selectors: the JP credit module emits the anchor as a direct child of `.creditButton`, so rules written against the `<p>`-wrapper form would never match; correcting the inherited rules in place is the mechanism SUPPLEMENT-TYPES T7 names for a theme that carries its own credit CSS, as against the appended-supplement form for one that does not.
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns only the JP preview pair; read candidate L12–23 against the eight fields; `grep -n 'creditButton' candidate.txt` — the four corrected selectors, none with the `p a` form.
- **Disposition:** Standing (the swap is the port itself; the T4 row charges nothing against this section).

### 2. Includes and components

- **What:** Three include changes. (1) The credit pair (section 1). (2) The exhibit image: the original floats its photo through a sandbox component, `:scp-sandbox-3:image-zoom` (original L16, one line, an `http://` image URL and a Chinese caption); the candidate uses the JP component form, `:scp-jp:component:image-block` in the multi-line parameter style (candidate L25–29), with the same image over `https` and the caption translated. The component changed because image-zoom is a CN sandbox component with no JP counterpart under that name; the JP image-block is the environment's image component, and the float (`align=right`) is preserved. (3) The frame (section 3). The usage line is prose, not an include pair: inside the intro, the original's `[[include :scp-wiki-cn:theme:emotion-division]]` becomes `@@[[include theme:emotion-division-jp]]@@` (candidate L31) — the local form naming this candidate's own page with its `-jp` suffix, which is the correct name.
- **Why:** P1 (KB-15) for the credit pair and the frame; for the image, P1 with ruling 4's audit-first rule read in reverse — the sandbox component is not ported alongside, because the JP environment already carries the equivalent component the exhibit needs, and the exhibit's function (a floated, captioned photo) is preserved entire.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the image-block, and the prose usage line at L31; no `:scp-sandbox-3:` or `:scp-wiki-cn:` include survives.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The theme self-delivers from its own code page in both versions: a head `[[module CSS]]` importing `theme:emotion-division/code/1` from scp-wiki-cn.wikidot.com (original L2 — unquoted, and without the closing semicolon, the T4 row's 型 4 nit) becomes the same import from the candidate's own delivery on the draft host (candidate L2, block B1), quoted and terminated: the nit is repaired in passing by the repoint's own form. The CSS text rides as the `[[code]]` exhibit on both sides (original L148–622 → candidate L161–635) with the port's changes inside it (sections 1, 4–6). **Frame paragraph (the M-frame addition):** the original carried no interwiki-style frame (LOCALIZE-ROWS row 184, 型 6); the candidate adds one at candidate L5–8 with `priority=1` and `theme=` naming its own /1 delivery on the draft host — the single-layer own-code form, in the spaced parameter style. The ledger records the outcome as P6 FIXED (frame waves; checker-verified); the frame arrived in FIX4-IWA (commit 8c62b7b, "missing interwiki frames added to 31 themes (KB-07a)").
- **Why:** P4/T9 for the own-code repoint; P6/T3 (KB-07) for the added frame. KB-41 covers the draft-host form of both live delivery lines (class (iii), rewritten to the production host at posting).
- **Verify:** Read candidate L1–8; `grep -n 'scp-wiki-cn.wikidot' candidate.txt` returns only the prose reference links (section 7).
- **Disposition:** FIXED (P6); the draft-host URLs are DISPOSITIONED (class (iii)).

### 4. Fonts and assets

- **What:** Fonts: none — neither side declares a `font-family` or loads a face; the theme inherits the site theme's fonts entire, so P7 has nothing to attach to. Assets: the theme owns no images. Its two pictures are borrowed exhibit photographs from SCP-CN-2733, hosted on the CN sandbox (scpsandboxcn.wikidot.com, the `shanle` file area): the floated photo (original L16 → candidate L26) and the CSS background (original L248 → candidate L261). Both survive on that host — they are another article's files, not this theme's to re-host — with the scheme upgraded `http` → `https` on both lines (block B53 is the background's upgrade; the photo's upgrade rides inside block B7's include swap). These are T1's two hotlink errors and the T4 row's 型 5 charges; the ledger dispositions them P5 (class (ii) / KB-58): serving outside hosts are posting-procedure matters, and a borrowed exhibit photo is the standing case.
- **Why:** P5/KB-17 with the hotlink sub-case rules: own assets re-host, borrowed assets on a serving host are class (ii). The scheme upgrade is the AGENTS.md `http` rule's other half — the candidate carries the `https` form, so no scheme item remains open.
- **Verify:** `grep -n 'font-family' candidate.txt` returns nothing; `grep -n 'scpsandboxcn' candidate.txt` — the two lines above, both `https`.
- **Disposition:** DISPOSITIONED (P5, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The theme declares its header identity in variables, and both are translated (block B49): `--header-title: "SCP基金会"` → `"SCP財団"` (candidate L163; the foundation's name in its Japanese form, glyph forms converted) and `--header-subtitle: "现实所描述者乃情感 情感所链接者乃现实"` → `"現実が描き出すものは感情 感情が結びつけるものは現実"` (candidate L164; the theme's slogan, translated). No other header variable is overridden, and no sidebar or topbar rule was adapted: the furniture rules ride inside the exhibit, unchanged apart from the comment translations of section 6. The render row's page-overflow readings (497–504px at 320/375) are recorded in section 11 as the row states them.
- **Why:** P9/T6 for the variables; the subtitle is the theme's own creative text, so ruling 2 (header language as taste) is not engaged — it was translated as body text is, and the title takes the institution's standard Japanese name.
- **Verify:** `grep -n -- '--header-' candidate.txt` — the two lines above; read original L150–151 against candidate L163–164.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body is translated throughout, in the classifier's counts: 15 TRANSLATION-ANCHORED and 40 TRANS-UNANCHORED primary blocks (B7–B48, B51–B60), each verified line by line against the mirror for this README. In groups: the intro prose (candidate L31, L33) and the long Aozora Society quotation (candidate L35); the specimen instructions and div-block captions (B12–B19); the tab specimen entire, including its eleven repeated long-tab lines (B25–B35) and the tab titles (B20–B24, B36–B41); the table specimen (B43); the closing prose paragraphs (B44–B47); and the exhibit's collapsible labels (B10, B48). In-CSS text (R1): the exhibit's ten section-banner comments are translated in place (COMMENT-TEXT blocks B50–B52, B54–B60: 検索欄, ログイン表示, ヘッダーと背景, サイドバー, 見出し, 折りたたみ, 区切り線, リンク, 評価モジュール, and the image section's longer note, "変更方針がないためそのまま保持", which preserves the original's own remark that the image rules are kept unchanged). R5 glyph-form conversion: one banner (B50: 搜索区 → 検索欄） and the header title (section 5) convert simplified forms to Japanese forms as part of their translation; they are counted here and there respectively, not double-counted. Chinese survives in the candidate only as quotation: the credit block's original-title field (candidate L17).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18/R1 (in-CSS text stated separately from reader-visible text: the banners are porter-visible only). The unanchored mass is where a silent deletion would hide, which is why each block was read individually rather than waved through as a class — the eleven identical tab lines are the kind of repetition a skim skips and a deletion hides inside.
- **Verify:** The pairs are diff.md's body sections in order; a simplified-Chinese scan of candidate.txt returns only candidate L17.
- **Disposition:** Standing (the port itself); the ledger records the theme's T5 outcome jointly with T4 (section 12).

### 7. Links

- **What:** The prose links stay on the CN originals, by design, with their schemes upgraded. The intro's three reference links (candidate L31: the New Touhei theme, the Asagao literary-supplement page, and the CSS theme preparation tool, all on scp-wiki-cn.wikidot.com) are the port's credit references — the pages this theme's code was modelled on — and they name serving originals; the ledger dispositions the class P11 (sibling / batch-posting). The specimen's self-link (block B42, candidate L138: `[[[https://scp-wiki-cn.wikidot.com/theme:emotion-division |リンク。]]]`) names the original page itself, as a specimen of a visited link; it is the original's own URL with the scheme upgraded and the label translated. The credit block's source link (candidate L21) names `https://scp-wiki-cn.wikidot.com/theme:emotion-division` — the original's recorded host (review/sources.tsv), so it names the serving original and no host defect arises. The T4 row's 型 11 charges (CN direct links, minor) are these lines, dispositioned as recorded.
- **Why:** P11 under the dead-reference evidence standard: reference and specimen links to serving originals are kept; the class disposition (sibling / batch-posting) is the ledger's recorded ground for the set.
- **Verify:** Compare candidate L21's host against the sources.tsv row's original_url host (scp-wiki-cn.wikidot.com) — identical; `grep -n 'http://' candidate.txt` returns nothing.
- **Disposition:** DISPOSITIONED (P11, sibling / batch-posting class); the source link stands.

### 8. Structure

- **What:** The localize.md closing rule holds. The topology pass finds the same two components on both sides in the same order (head module-css, then the code-css exhibit), no relocations; variable names, selectors, and rule order inside the exhibit are preserved, and the JP corrections arrive at the edges (the head frame and credit swap) or as in-place corrections of inherited rules (section 1's selectors), not interleaved into the inherited CSS. No EXHIBIT-RESTRUCTURE label fired at all for this theme. An exhibit census confirms the shape: the intro, the heading collapsible, the div-block specimens, the tabview with all its tabs, the table specimen, the closing prose, and the full CSS exhibit are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise.
- **Why:** R3 exists to force the census behind exactly this claim; here the census, not the absence of a label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[collapsible\|\[\[code\|\[\[module' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None as a primary class: the classifier finds no whitespace-only block and no re-indentation (0 and 0) among the 64 blocks, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the classifier skeleton for this package (WS-ONLY 0, re-indentation 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None — checked, and the check is the content of this section. The candidate has no `[!-- --]` notes, no editor lines, and no added comments: every comment in its CSS is a translation of one of the original's (section 6), and its prose is translated original prose. The skeleton's silence for this section happens to match the bytes, which is recorded here rather than assumed.
- **Why:** R2: porter-added text is part of the change record; its absence, verified, is what lets a reviewer attribute every line of the candidate to the original or to a named change class.
- **Verify:** `grep -n '\[!--\|移植\|SCP-JP版' candidate.txt` returns nothing.
- **Disposition:** Standing (none present).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's three errors: hotlink ×2 (class (ii) — the borrowed sandbox exhibit images of section 4, serving today, posting-procedure) and pseudo-ref ×1 (class (iii) — the frame's draft-host URL, section 3). (2) The render row's items (RENDER-ROWS-2, RENDER-S2-E (CN5)): page-overflow readings of 497–504px at 320/375 on the page and the sample (plus 884px at 768 on the sample), the page's hidden-* cluster confined to chromium-1366 whose only hotlink host is http.cat (KB-44: a transient Wikidot 503 capture, not a result), and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5) — recorded as the row states them, dispositioned at the determination. (3) P1 and P4 classes: DISPOSITIONED (posting-procedure convention class; delivery class (ii), original-state CDN delivery) per the ledger §(c3) line. (4) P11 links: DISPOSITIONED (sibling / batch-posting class; section 7).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1–4 as stated).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 221): exit 1, 3 errors / 1 warn / 1 info; the errors are hotlink ×2 and pseudo-ref ×1, classes (ii) and (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN5)): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 184): FINDINGS jointly, display-affecting findings 4 — the row's charges are 型 5 (the two sandbox image links, dispositioned), 型 6 (the absent frame, since FIXED by FIX4-IWA), 型 4 nit (the delivery import's missing semicolon, repaired in the repoint's form, section 3), and 型 11 (the CN direct links, dispositioned); the same row records the prose and T5 text as clean. The ledger §(c3) line records the outcomes: P1 DISPOSITIONED, P4 DISPOSITIONED, P5 DISPOSITIONED, P6 FIXED, P11 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +136/−122 in 64 change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:emotion-division-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 186; go-sign, COMPLETION-REPORT §10).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-emotion-division-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 情感缢裂 版式
- **Author:** quisqualis
- **Source:** https://scp-wiki-cn.wikidot.com/theme:emotion-division — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
