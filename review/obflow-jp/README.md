# Review package — theme:obflow-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:obflow-jp — origin CN, population #209 [GOSIGN2-LEDGER (b) row 209]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7bd3dd14afa63e34a3bb6f3d0055d4bfc07dd76df64caea72968a5ac92a759c8); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (hotlink×6); standing classes dispositioned in register c1 [T1-ROWS row 224; GOSIGN2-LEDGER (b) row 209]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 323–325px@320 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 208, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 208]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 209]
- Computed against: canonical commit 1db8300464d032875c6f8cc6ab61a5cafc6b7433; candidate file pages/theme:obflow-jp.txt sha256:7bd3dd14afa63e34a3bb6f3d0055d4bfc07dd76df64caea72968a5ac92a759c8; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 209) |
| Standing items | **DISPOSITIONED** — the live CN code import (P4, "delivery class (ii): original-state CDN delivery", GOSIGN2-LEDGER §(c3)); the sandbox-hosted images (P5 family inside T1's hotlink ×6, class (ii) / KB-58); the render row's items (323–325px@320 overflow, the runtime-hotlink site-theme chain; the sample's render run returned no machine verdict and is recorded as such, section 11). **FLAGGED by this package** — the holder field's silence on the base theme's author (per-theme record, item 1) and one inherited credit rule in the pre-correction selector form (item 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:obflow | theme:obflow-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 2 (first translation; the candidate's credit block records 初訳時参照リビジョン: 2) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-obflow.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:obflow-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 966 lines / 25,995 bytes | 987 lines / 28,087 bytes |
| SHA-256 | 2384d8d243a57b0791d7db27ee91805cf7fbc20f5808e083ba96467fafe0971f | b701e4b8daa7ba92ae02068a2f25c39b011b0b5d6331d1df6aebd6a7e88bacf0 |

Wave history: the candidate was created by the Stage 2 CN10 integration (commit a89eccf, the LOCALIZE-S2-E wave's port) and has two later commits: f931619 (FIX2-COLON, the colon-encoding fix wave; this file's delivery and asset URLs) and 8c62b7b (FIX4-IWA, the frame wave; the verdict stamp's computed-against commit). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge; its T4 finding was closed by disposition in the ledger (§(c3)), not by edits.

## Summary

A CN theme built by modifying the Penumbra theme, whose port is organized around one fact: its live stylesheet stays on the CN wiki. The original's head module imports its 884-line exhibit from scp-wiki-cn.wdfiles.com, and the candidate's head module keeps that import (colon-encoded), so as shipped the theme's applied CSS is the CN original — T4 charged exactly this ("the theme's single live stylesheet *is* a CN-hosted local--code — if the CN site goes down or the file changes, every JP page using this theme breaks/changes") and the ledger dispositions it as delivery class (ii). Around that kept import the port builds its JP layer where it can take effect regardless: the head module gains the JP font loads, a porter-annotated stack-override block, and the localized header-title rule; the interwiki-style frame is added, framing the candidate's own exhibit (which is carried in full, its comments translated and its strings converted, ready to become the delivery at posting); the toggle-sidebar component is repointed to its JP counterpart; the credit furniture is swapped for the JP preview block; and the body is translated in place. Measured churn (diff.md: +121/−100, 221 changed lines in 64 change blocks / 31 diff sections) is mostly comment and prose translation inside the unmoved exhibit.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 64 change blocks — 32 specific (50%), 32 heuristic (50%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 37 |
| COMMENT-TEXT | 34 |
| GLYPH-FORM | 16 |
| TRANSLATION-ANCHORED | 15 |
| EXHIBIT-RESTRUCTURE | 2 |
| HEADERVAR | 2 |
| SELF-DELIVERY | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 1 |
| DELIVERY-HOST | 1 |
| DELIVERY-MOVE | 1 |
| JPFONT-LOAD | 1 |
| DRAFT-HOST | 1 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| JPFONT-STACK | 1 |

Adjudication for this README (every specific block was read against the bytes; the heuristic mass was resolved by shape): the 86 translation-family blocks (TRANS-UNANCHORED 37, COMMENT-TEXT 34, TRANSLATION-ANCHORED 15) are the body, exhibit, and CSS-comment translation of section 6, counted per line-pair inside an exhibit that never moved; GLYPH-FORM (16) is the R5 conversion inside retained strings, stated separately there. The two EXHIBIT-RESTRUCTURE primaries are the standing false-fire family: B1 is the toggle-sidebar include line at the head (an INCLUDE-REPOINT), and B9 is the collapsible headings exhibit, whose change is its translated show/hide text and heading labels. B2's five labels are one head-module block (the kept import, the JP loads, the stack overrides, the header-title rule), adjudicated in sections 3–5. After adjudication no block is left unexplained, and no residue appendix is needed (0 residue blocks).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:obflow-jp; original theme:obflow on scp-wiki-cn at reference revision 2; candidate `pages/theme:obflow-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved: the original opens with the toggle-sidebar include, its delivery module, and its gate (original L1–7); the candidate opens with the repointed include, the enlarged delivery module (candidate L3–25), the interwiki-style frame (candidate L27–31), and then the localized gate (candidate L33).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for obflow-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labeled bare `[[module Rate]]` (original L9–12) and the CN credit trio `:scp-wiki-cn:credit:start`/`more`/`end` (original L16–20), its bodies the placeholders 页面信息 and 更多页面信息. The candidate deletes both and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block directly under the gate (candidate L35–44) carrying the eight ruling-3 fields (title 逆流テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 逆流 版式, the original's simplified-Chinese title kept as the original-title field; 著作権者 AI_Mayca; 作成年 2022; 初訳時参照リビジョン 2; the source link, candidate L43, on scp-wiki-cn.wikidot.com, the host sources.tsv records for the original). Author check against the original: AI_Mayca is the theme's author (the exhibit banner, original L85: "By AI_Mayca"); the banner also credits the base theme ("Based on Penumbra by EstrellaYoshte", original L86) and the field names the author of record alone — the base author is flagged in the per-theme record, item 1. The banner itself is carried verbatim in the candidate's exhibit (candidate L104–109), including its "Logo licensed under CC BY SA 3.0" line; no license box exists on either side. T7 credit-module CSS: the theme carries its own credit rules inside the exhibit (the `.rate-box-with-credit-button .creditButton` group and a `.creditButtonStandalone` pair, original L589–617), carried byte-identically (candidate L610–638); one selector in the group is flagged in the per-theme record, item 2. No supplement was added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate and the branch credit trio are deleted rather than duplicated (a kept Rate would be the KB-09 duplicate; a kept branch credit module does not render in the JP environment). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns only the preview pair at L35 and L44; read candidate L35–44 against the eight fields.
- **Disposition:** Applied; no credit item is charged in the theme's T4 row.

### 2. Includes and components

- **What:** The candidate's live includes are four: the toggle-sidebar component at the head (original L1's `:scp-wiki:component:toggle-sidebar` → candidate L1's `:scp-jp:component:toggle-sidebar`, the B1 repoint), the interwiki-style frame (candidate L27–31, section 3), and the credit pair (section 1). The usage example changes form: the original's `@@[[include :scp-wiki-cn:theme:obflow]]@@` (original L27) becomes the bare `@@[[include theme:obflow-jp]]@@` (candidate L50), naming the candidate's own fullname without a site prefix — the correct page under the posting name, in contrast to the plain-slug shape flagged in sibling packages. One live include is not repointed: the logo exhibit, `[[include component:image-block name=https://scpsandboxcn.wikidot.com/local--files/collab%3Amayca/logo_…]]` (original L31 → candidate L52), a bare component include (it resolves on the local wiki on both sides) whose changes are the scheme upgrade, the colon encoding, and its translated caption; its image host is section 4's P5 family. The original's CN credit trio is deleted in the section 1 swap.
- **Why:** P1/T2: components resolve to their JP counterparts where a counterpart exists; the image-block include is site-local on both sides, so no repoint arises, and its asset is a P5 item, not a P1 item.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the toggle-sidebar at L1, the frame, the credit pair, and the image-block line at L52.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS by importing its code exhibit from the CN wdfiles host: a head `[[module cSs]]` with `@import url(https://scp-wiki-cn.wdfiles.com/local--code/theme:obflow/1)` (original L3–5). The candidate's head module (candidate L3–25) keeps that import in place — still naming scp-wiki-cn.wdfiles.com, with the colon encoded by the FIX2-COLON wave (candidate L6) — and builds the JP layer around it in the same module: the two JP font loads (candidate L4–5, section 4), the stack-override rules under a porter annotation (candidate L8–18, sections 4 and 10), and the localized header-title rule (candidate L20–24, section 5). The candidate also carries its own exhibit in full (candidate L102–985, 884 lines, the original's length) and frames it: the interwiki-style frame at priority=1 names the exhibit on the draft host (candidate L27–31), so a page including this theme receives both the module (with its CN import and JP overrides) and the framed JP exhibit. T4's finding names the resulting state exactly: "P4 MISSED (the theme's single live stylesheet *is* a CN-hosted local--code — if the CN site goes down or the file changes, every JP page using this theme breaks/changes; …)" (LOCALIZE-ROWS row 208). The ledger dispositions the item as "delivery class (ii): original-state CDN delivery" (§(c3)): the kept import stands in its original state until the posting procedure converts the delivery, on the same footing as the draft host in the frame. The head module's overrides are written to take effect under either delivery, which is why they exist as a separate layer instead of only as exhibit edits (the exhibit carries the same JP stack additions in place, section 4).
- **Why:** P4/T9 govern own-code delivery; the frame is P6/T3. The kept import is not narrated as a normal supplement: it is the charged P4 item, and its standing is the ledger's disposition, quoted above with its ground.
- **Verify:** `grep -n '@import' candidate.txt` returns six lines: the module's JP loads (L4–5), the kept CN import (L6), and the exhibit's own font loads (L111–113).
- **Disposition:** DISPOSITIONED (P4, delivery class (ii), GOSIGN2-LEDGER §(c3)); the frame is class (iii) mechanics.

### 4. Fonts and assets

- **What:** Loads added: the head module loads Noto Sans JP (300;400;700;900) and Noto Sans Mono (400) from Google Fonts (candidate L4–5). The exhibit's own loads are the original's three Latin faces (Josefin Sans, Roboto, Fira Code, original L90–92 → candidate L111–113), carried unchanged. Stacks, in two layers as in section 3: in the exhibit, the body stack gains the JP fallback in place (`'Roboto', sans-serif` → `'Roboto', 'Noto Sans JP', sans-serif`, original L96 → candidate L117, the JPFONT-STACK block); in the head module, the annotated override block restates the body, heading, and mono stacks with the JP faces appended (`'Roboto', 'Noto Sans JP'`; `'Josefin Sans', 'Noto Sans JP'`; `"Fira Code", 'Noto Sans Mono'`, candidate L9–18). First-face check: the stacks' first faces are the Latin faces, loaded by the exhibit's own imports on both delivery paths; the JP faces are fallbacks and are loaded on the same page, so no KB-16 gap arises. Assets: the theme's logo system stays on the author's sandbox host — the animated logo (the image-block exhibit, candidate L52) and its four clock-hand frame images inside the exhibit (original L143–158 → candidate L164–179, `logo_时间轰炸…` on scpsandboxcn.wikidot.com) — with the scheme upgraded to https and the colons encoded, the Chinese filenames kept as filenames. These are T1's hotlink ×6 family (P5), dispositioned class (ii) / KB-58: re-hosting is a posting-procedure act, not a candidate edit.
- **Why:** P7 (JP fallbacks in load and stack, in both layers the port maintains). P5's disposition is the ledger's, recorded here with its grounds.
- **Verify:** `grep -n '@import\|font-family' candidate.txt` against the lines cited; `grep -n 'scpsandboxcn' candidate.txt` returns the five sandbox asset lines.
- **Disposition:** Loads and stacks applied; the images DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The sidebar furniture is the toggle-sidebar component, repointed at candidate L1 (section 2). The header title: the original's exhibit sets it as `content: var(--header-title, "基金会时间部队")` (original L187, simplified-Chinese default). The candidate localizes the default in both of its layers: the exhibit line takes the Japanese form (candidate L208: `var(--header-title, "財団時間部隊")`, glyph-converted and translated) and the head module carries the same rule (candidate L20–24), so the JP title shows even while the live delivery is the CN import (section 3). The `--header-title` variable itself is the user's override point (KB-57's form: the theme supplies a localized default, the user supplies the variable). The theme sets no `--logo-image` override; its logo is the sandbox-hosted animated image of section 4. The render row's one layout item is the 323–325px@320 overflow, recorded in section 11.
- **Why:** P9/T6 (header variables keep their names; the default string is localized) and KB-18 (the header string is reader-visible).
- **Verify:** `grep -n 'header-title' candidate.txt` returns candidate L23 and L208, both with the Japanese default.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body is translated throughout: the about prose (candidate L46, keeping the tuna-sushi joke and the Penumbra credit, section 7), the usage prose, and the exhibits in the original's order (the collapsible heading samples, the logo exhibit's caption, the syntax samples). The translation mass is the classifier's heuristic bulk (TRANS-UNANCHORED 37, TRANSLATION-ANCHORED 15), resolved here in aggregate per the class M convention: line-pair translation inside an unmoved exhibit and body. In-CSS text (R1): the exhibit's Chinese section comments are translated to Japanese (COMMENT-TEXT, 34 blocks), porter-visible only; the banner comment is carried verbatim in English (candidate L104–109). R5 glyph-form conversion, stated separately: retained Chinese strings take Japanese glyph forms where the string survives (GLYPH-FORM, 16 blocks; the header default of section 5 is the headline instance, 基金会时间部队 → 財団時間部隊）, distinct from full translation. Chinese survives in the candidate in the credit block's original-title field (candidate L38), where it is a quotation, and inside the sandbox asset filenames (section 4), where it is a filename, not text.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings). R5 is separated per the taxonomy so a reviewer can tell a converted string from a translated one.
- **Verify:** The body sections of diff.md in order; a Chinese-prose scan of candidate.txt outside the credit field and the asset URLs returns nothing.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the two quotations named.

### 7. Links

- **What:** The about prose's base-theme link changes form: the original links Penumbra intra-wiki (`[[[theme:penumbra|半影版式]]]`, original L25); the candidate converts it to a labeled external-form link to the same page on scp-wiki-cn.wikidot.com, with a branch note (candidate L46: 半影テーマ（中国語版）), because the base theme has no JP counterpart page in the composition to repoint to. The credit source link (candidate L43) names scp-wiki-cn.wikidot.com, the recorded host, and serves the original. No other outbound links exist in the candidate outside the asset URLs of section 4.
- **Why:** P11: a prose link takes the JP counterpart where one exists and the serving original where it does not; the dead-reference standard is not engaged, nothing here is dead.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the Penumbra link and the source link.
- **Disposition:** Standing.

### 8. Structure

- **What:** No declared deviation beyond the delivery state of section 3, which is dispositioned there and in section 11, and the head module's growth from an import-only module to the JP adaptation layer (sections 3–5), which is additive. Variable names, selectors, and rule order inside the exhibit are preserved (the exhibit stands at its original 884 lines), and the exhibit census (the logo image-block, the collapsible samples, the syntax exhibits, the code exhibit) corresponds one to one in the same order, so no R3 deletion arises. The two EXHIBIT-RESTRUCTURE primaries are adjudicated in the class summary (an include repoint and a translated collapsible).
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census, not by the label.
- **Verify:** Compare `grep -n '\[\[code\|\[\[collapsible\|\[\[include' original.txt candidate.txt` — every exhibit form on the left has its counterpart on the right.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** No WS-ONLY or re-indentation class fired for this theme (0 blocks of either): the exhibit was edited in place without reformatting, so there is no formatting churn to disclose. The head module's added lines are content, recorded in sections 3, 4, and 10, not formatting.
- **Why:** The formatting section states its ground when empty, so a reviewer does not have to infer it from silence.
- **Verify:** classification.json carries no WS-ONLY label for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation exists, riding inside the head-module block B2: at candidate L8, `/* SCP-JP port: JP font fallbacks added to the stacks */`, introducing the stack-override rules of section 4 (candidate L9–18). It is the port explaining its own layer in the file, in English, and it is the only added comment; no `[!-- --]` note exists. The header-title rule that follows the overrides (candidate L20–24) carries no comment of its own.
- **Why:** R2: annotations are part of the port's record; this one documents the override layer's intent, which section 3 relies on to explain why the module exists in its enlarged form.
- **Verify:** `grep -n 'SCP-JP port' candidate.txt` returns candidate L8 only.
- **Disposition:** Standing (part of the candidate as reviewed).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) The live CN code import (P4): charged by T4 as MISSED with the wording quoted in section 3 (LOCALIZE-ROWS row 208) and DISPOSITIONED at GOSIGN2-LEDGER §(c3) as "delivery class (ii): original-state CDN delivery". (2) The sandbox-hosted images (P5): T1's hotlink ×6 family, DISPOSITIONED as class (ii) / KB-58 (section 4). (3) The render row's items (RENDER-ROWS-2, lane RENDER-S2-F (CN10)): the page's 323–325px@320 overflow and its runtime-hotlink site-theme chain (KB-40, environment layer; the chain item is items (1)–(2) seen from the render side), recorded verbatim; and the sample's render run, which returned no machine verdict (exit 2, no summary) — an inconclusive run, recorded as the row records it, so this theme's sample has no T2 verdict in the record and none is claimed here. No credit-modal line is recorded for this theme. The two per-theme flags are flagged, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; an inconclusive check is reported as inconclusive, not as a pass.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3 as stated); the per-theme items flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 224): exit 1, 6 errors / 1 warn / 1 info; all six errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-F (CN10)): FINDINGS on the page (the section 11(3) items, dispositioned); the sample run inconclusive as recorded; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 208, LOCALIZE-S2-E): FINDINGS / FINDINGS jointly, display-affecting findings 1 (the P4 item), dispositioned at §(c3). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (diff.md): +121/−100, 221 changed lines in 64 change blocks / 31 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:obflow-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 209; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the holder field and EstrellaYoshte (flagged)

The original credits EstrellaYoshte in its exhibit banner ("Based on Penumbra by EstrellaYoshte", original L86); the theme's own about prose credits her theme without naming her (original L25), and the candidate's translated prose does the same (candidate L46). The candidate's credit block names AI_Mayca alone in the 著作権者 field (candidate L40). EstrellaYoshte's credit survives in the carried banner (candidate L107 zone). The distinction from the sibling flags in this campaign is real — she authored the base theme this one modifies, not this theme — but the shape is the family the U-1 and U-2 batches repaired (a contributor the original names in its credit furniture, absent from the TASL field), and the same item is recorded for theme:mr-reprisal-jp (Denevola) and theme:oneiroi-west-jp (Feitag) in this batch. This package flags the gap with both sides' text and does not edit the candidate; the ledger's determination for this theme is PASS and its T4 row charges only the P4 delivery item.

### Item 2 — the inherited `.creditButton p a` selector (flagged)

The exhibit carries the theme's own credit-rule group, including `#page-content .rate-box-with-credit-button .creditButton p a` (original L589 → candidate L610), byte-identical on both sides. The campaign's T7 record (SUPPLEMENT-TYPES T7; KB-11) states the JP credit module emits the anchor as a direct child of `.creditButton`, without the `<p>` wrapper this selector requires, and sibling ports corrected exactly this shape (theme:sodium-jp in place, theme:jiha-jp by restatement). Here the rule stands uncorrected, so on the JP DOM it cannot match. The same flag is recorded for theme:mr-reprisal-jp, theme:oneiroi-west-jp, theme:nameless-jp, and theme:much-cool-jp in this batch — five of the batch's ten themes, every one that carries its own credit CSS — which suggests the correction was applied only where a wave happened to touch the file, and that the inherited copies form a population a single sweep could settle. The group's `.creditButtonStandalone p a` pair (original L607–617 → candidate L628–638) is a different component's shape and is not charged here. This package flags the rate-box selector with its evidence and does not edit the candidate; the theme's T4 row does not charge it.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-obflow-jp.txt` is the decoration sample the render checks ran against (its run is the inconclusive one recorded in section 11(3)). There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.
