# Review package — theme:nameless-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:nameless-jp — origin CN, population #207 [GOSIGN2-LEDGER (b) row 207]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 507cf3aaf2a62b6f1c6cc139eb40e3e5932a297d35d91790136135926f5d1360); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 10 errors / 1 warn / 1 info (hotlink×10); standing classes dispositioned in register c1 [T1-ROWS row 222; GOSIGN2-LEDGER (b) row 207]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 344px@320 on page and sample; candidate-own runtime hosts (fastly.jsdelivr.net, p.typekit.net / use.typekit.net, pokm.wdfiles.com, wanderers-library and scp-wiki-cn chains) recorded verbatim; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN10))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 206, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 206]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 207]
- Computed against: canonical commit 1db8300464d032875c6f8cc6ab61a5cafc6b7433; candidate file pages/theme:nameless-jp.txt sha256:507cf3aaf2a62b6f1c6cc139eb40e3e5932a297d35d91790136135926f5d1360; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 207) |
| Standing items | **DISPOSITIONED** — the gate-tag item (P2, T1 class (ii)); the live foreign code imports (P4, "delivery class (ii): original-state CDN delivery"); the un-rehosted images (P5, class (ii) / KB-58); the render row's items (344px@320 overflow on page and sample, the candidate-own runtime host chains, the credit-modal preview form; section 11). **FLAGGED by this package** — one inherited credit rule in the pre-correction selector form (per-theme record, item 1). **NOTED** — the credit holder field's value is named nowhere in the frozen original (per-theme record, item 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:nameless | theme:nameless-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 6 (first translation; the candidate's credit block records 初訳時参照リビジョン: 6) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-nameless.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:nameless-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 725 lines / 17,961 bytes | 742 lines / 20,868 bytes |
| SHA-256 | c9386a8dbaa04f6586c57312bee79a787f72b3d96411240d3c41a4cdebd48b29 | 77d032c59dfebe615000bee70fe1b37aa4056b3cde46d2db371450dc3e0406c1 |

Wave history: the candidate was created by the Stage 2 CN10 integration (commit a89eccf, the LOCALIZE-S2-E wave's port) and has two later commits: f931619 (FIX2-COLON, the colon-encoding fix wave; this file's active delivery URLs) and 8c62b7b (FIX4-IWA, the frame wave; the verdict stamp's computed-against commit). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge; its T4 findings were closed by disposition in the ledger (§(c3)), not by edits.

## Summary

A CN theme for the City of the Nameless setting, layered over Dr Hormress's Starry Library theme code, whose port keeps the original's delivery skeleton and adapts around it. The original carries three code exhibits (a 439-line main exhibit and two short variant exhibits, selected by include parameters) and a tail `[[module css]]` that imports exhibit /1 from the CN wiki, with the /2 and /3 imports commented out behind the parameter trick. The candidate keeps all of that — the tail module still imports the original's exhibit /1 from scp-wiki-cn.wikidot.com, a live dependence T4 charged as P4 MISSED ("as shipped the theme renders only because the CN site is up") and the ledger dispositions as delivery class (ii) — and adds the JP layer around it: an interwiki-style frame at the head naming the candidate's own exhibit /1 on the draft host, three Google Fonts JP loads and a stack-override block with a porter annotation in the tail module, and JP faces substituted into the exhibits' own stacks. The credit furniture (a bare Rate and the CN credit trio with placeholder bodies) is swapped for the JP preview block, the theme-squares exhibits are repointed to the JP component, and the body is translated in place. Measured churn (diff.md: +179/−167 in 19 hunks; classification.json: 98 change blocks) is mostly translation and comment mass inside the unmoved exhibits.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 98 change blocks — 45 specific (46%), 53 heuristic (54%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 56 |
| TRANSLATION-ANCHORED | 27 |
| COMMENT-TEXT | 18 |
| INCLUDE-REPOINT | 6 |
| GLYPH-FORM | 6 |
| SELF-DELIVERY | 4 |
| COMPONENT-SWAP | 4 |
| CONTENT-STRING | 4 |
| COLON-ENC | 4 |
| DELIVERY-MOVE | 4 |
| CSS-BODY | 3 |
| IFTAGS | 2 |
| EXHIBIT-RESTRUCTURE | 2 |
| BARE-RATE-DEL | 1 |
| DRAFT-HOST | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| DELIVERY-HOST | 1 |
| JPFONT-LOAD | 1 |

Adjudication for this README (every specific block was read against the bytes; the heuristic mass was resolved by shape): the 101 translation-family blocks (TRANS-UNANCHORED 56, TRANSLATION-ANCHORED 27, COMMENT-TEXT 18) are the body, exhibit, and CSS-comment translation of section 6, counted per line-pair inside exhibits that never moved; GLYPH-FORM (6) is the R5 conversion inside retained strings, stated separately there. The two EXHIBIT-RESTRUCTURE primaries are the standing false-fire family: B11 is the theme-squares include line itself (a COMPONENT-SWAP repoint), and B27 is the image-block include whose only change is its translated caption. B98's DELIVERY-MOVE primary is the tail-module porter annotation and stack-override block, adjudicated in sections 4 and 10. The four COMPONENT-SWAP blocks are one component (theme-squares) met four times (the live exhibit and its parameter variants in the documentation). The three CSS-BODY heuristic blocks are the in-exhibit font-stack lines of section 4, which are P7 by content. After adjudication no block is left unexplained, and no residue appendix is needed (0 residue blocks).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:nameless-jp; original theme:nameless on scp-wiki-cn at reference revision 6; candidate `pages/theme:nameless-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved: the original opens with its gate and furniture (original L1–15); the candidate opens with the interwiki-style frame (candidate L1–4) ahead of the localized gate (candidate L6).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for nameless-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery facts are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a labeled bare `[[module Rate]]` (original L2–5) and the CN credit trio `:scp-wiki-cn:credit:start`/`more`/`end` (original L10–15), whose bodies are the placeholders 页面信息 and 更多页面信息 — the original carries no filled credit text at all. The candidate deletes the Rate exhibit and the trio and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block under the gate (candidate L8–17) carrying the eight ruling-3 fields (title 無名城の具名者テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 无名城中的具名者 版式, the original's simplified-Chinese title kept as the original-title field; 著作権者 Re_spectators; 作成年 2024; 初訳時参照リビジョン 6; the source link, candidate L16, on scp-wiki-cn.wikidot.com, the host sources.tsv records for the original). Author check against the original: the frozen original names no author anywhere in its text — no banner, no filled credit body, no byline — so the holder value cannot be verified from this package's evidence; the per-theme record, item 2, records that. The base-work credit that the original does carry (Dr Hormress's Starry Library theme, in the about prose, original L19) survives in the candidate's translated prose (candidate L21, with his user link) and in the kept base import (section 3). No license box exists on either side. T7 credit-module CSS: the theme carries its own credit rules inside exhibit /1 (the `.rate-box-with-credit-button .creditButton` group, original L556–564), carried byte-identically (candidate L558–566); one selector in it is flagged in the per-theme record, item 1. No supplement was added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate and the branch credit trio are deleted rather than duplicated (a kept Rate would be the KB-09 duplicate; a kept branch credit module does not render in the JP environment). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` returns only the preview pair at L8 and L17; read candidate L8–17 against the eight fields.
- **Disposition:** Applied; no credit item is charged in the theme's T4 row.

### 2. Includes and components

- **What:** The candidate's live includes are three: the interwiki-style frame (candidate L1–4, section 3) and the credit pair (section 1). The component exhibit: the original's live `[[include :scp-wiki:component:theme-squares …]]` (original L31) is repointed to `:scp-jp:component:theme-squares` (candidate L33), its color parameters carried unchanged; the classifier meets the same swap four times because the documentation repeats the exhibit with its parameter variants. The usage examples change form: the original's `@@[[include :scp-wiki-cn:theme:nameless]]@@` (original L25) and its three variant forms with the `fixed=*` / `scp=*` parameters (original L66, L70, L74) become the bare `@@[[include theme:nameless-jp]]@@` forms (candidate L27, L68, L72, L76), naming the candidate's own fullname with the variant parameters preserved — the correct page, in contrast to the plain-slug shape flagged in sibling packages. One live include is not repointed: the Wanderers' Library logo exhibit, `[[include component:image-block name=https://wanderers-library.wdfiles.com/…]]` (original L107 → candidate L109), a bare component include (it resolves on the local wiki on both sides) whose only change is its translated caption; its image host is section 4's P5 family. The original's CN credit trio is deleted in the section 1 swap.
- **Why:** P1/T2: components resolve to their JP counterparts where a counterpart exists; the image-block include is site-local on both sides, so no repoint arises, and its asset is a P5 item, not a P1 item.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, the theme-squares exhibit, the bare self-references in the examples, and the image-block line at L109.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original's delivery has three layers, and the candidate keeps two of them verbatim in form. (a) The base layer: exhibit /1 opens with an `@import` of Dr Hormress's Starry Library theme code from his own wiki (original L223: `https://pokm.wikidot.com/local--code/theme:starry-library/1`); the candidate keeps the import with only the colon encoded (candidate L225, the FIX2-COLON wave's form). (b) The own-code layer: the original's tail `[[module css]]` imports exhibit /1 from the CN wiki (original L716: `https://scp-wiki-cn.wikidot.com/local--code/theme:nameless/1`), with the /2 and /3 imports commented out behind the include-parameter trick (`/* {$fixed}/ … /{$fixed} */`, original L718–724) that the usage examples' `fixed=*` / `scp=*` parameters activate. The candidate's tail module keeps the active import, re-hosted nowhere — it still names scp-wiki-cn.wikidot.com, with the colon encoded (candidate L721) — and keeps the two commented imports in their original unencoded form (candidate L724, L728). (c) The frame layer is the port's addition: the interwiki-style frame at the head (candidate L1–4, priority=1, `theme=` naming the candidate's own exhibit /1 on the draft host, class (iii) mechanics), added by the FIX4-IWA wave. The candidate therefore carries two live deliveries of exhibit /1 — its own, through the frame, and the original's, through the kept import — and T4's finding names the consequence: "P4 (live CN code imports) and P5 (un-rehosted images) are both MISSED — as shipped the theme renders only because the CN site is up" (LOCALIZE-ROWS row 206). The ledger dispositions the P4 item as "delivery class (ii): original-state CDN delivery" (§(c3)), that is, the kept imports stand in their original state until the posting procedure converts the delivery, on the same footing as the draft host in the frame. The three exhibits themselves are carried at their original ranges (439, 6, and 38 lines; candidate L224–662, L665–671, L674–712), and the variant exhibits' content is preserved (the /2 background-fix rules and the /3 SCP-header variant, original L663–710).
- **Why:** P4/T9 govern own-code delivery; the frame is P6/T3. The kept imports are not narrated as a normal supplement: they are the charged P4 item, and their standing is the ledger's disposition, quoted above with its ground.
- **Verify:** `grep -n '@import' candidate.txt` returns seven lines: the base import (L225), the three JP font loads (L718–720, section 4), the active own import (L721), and the two commented variant imports (L724, L728).
- **Disposition:** DISPOSITIONED (P4, delivery class (ii), GOSIGN2-LEDGER §(c3)); the frame is class (iii) mechanics.

### 4. Fonts and assets

- **What:** Loads added: the tail module loads Noto Sans JP, Noto Serif JP, and Noto Sans Mono from Google Fonts (candidate L718–720), ahead of the kept own-code import. The original loads no JP face anywhere. Stacks, in two layers. In the exhibits, the CJK faces are substituted in place: `--body-font: adelle-sans, 'Lato', 'Noto Sans SC', sans-serif` → `…, 'Noto Sans JP', sans-serif` (original L227 → candidate L229), and the header/title stacks take `'Noto Serif JP'` for `'Noto Serif SC'` (original L228–229 → candidate L230–231), with the same substitutions in exhibit /3 (original L675–677 → candidate L677–679); the classifier's three CSS-BODY heuristic blocks are these lines, P7 by content. In the tail module, a porter-annotated override block restates the four stacks with the JP faces appended after the SC faces (candidate L733–736: `--body-font: adelle-sans, 'Lato', 'Noto Sans SC', 'Noto Sans JP', sans-serif`, and likewise the serif stacks), plus a `div#header h1 a::before` rule naming `"Noto Serif SC", "Noto Serif JP"` (candidate L739–741) — so where the tail module's cascade wins, the SC faces remain available ahead of the JP cuts, and where the frame's exhibit copy wins, the stacks are the substituted forms; both forms are recorded here because a reviewer comparing only one delivery path will see only one of them. First-face check: the stacks' first faces (adelle-sans, zuijinregular, Poppins, Lato) are the original's own, loaded by the kept base chain (the render row records the candidate's runtime hosts verbatim: fastly.jsdelivr.net, p.typekit.net / use.typekit.net, pokm.wdfiles.com, the wanderers-library and scp-wiki-cn chains); the JP faces are never first in a stack, and where they are named they are loaded on the same page, so no KB-16 gap arises. Assets: the theme's images stay on their original hosts — the dustjacket-sigma goldfoil texture on scp-wiki.wdfiles.com (three uses in the exhibits), the city-of-the-nameless background and SCP.png on pokm.wikidot.com / pokm.wdfiles.com, and the Wanderers' Library logo of section 2 — the P5 family, part of T1's hotlink ×10, dispositioned class (ii) / KB-58.
- **Why:** P7 (JP faces in load and stack; the substitution in the exhibits and the appended fallbacks in the tail are the two halves of one adaptation, and the annotation at candidate L732 states the tail half's intent). P5's disposition is the ledger's.
- **Verify:** `grep -n '@import\|font-family\|--body-font\|--header-font' candidate.txt` against the lines cited; the annotation is at candidate L732.
- **Disposition:** Loads and stacks applied; the images DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The theme sets no `--header-title` or `--logo-image` override on either side; the header and subtitle are user-customized through the documented `content:` examples (the subtitle example at candidate L100–112 zone, carried from original L98–110), and the SCP-header variant is exhibit /3's business (section 3). No sidebar furniture exists in this theme beyond the base chain's. The render row's one layout item is the 344px@320 overflow, recorded in section 11.
- **Why:** P9/T6 do not apply to a theme that sets no header variables; P8 has no item here beyond the overflow disposition.
- **Verify:** `grep -n -- '--header-title\|--logo-image' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The body is translated throughout: the about prose (candidate L21, keeping the Dr Hormress credit and converting its intra-wiki links to labeled links to the CN pages, section 7), the usage prose and variant documentation, the theme-squares exhibit captions, and the syntax exhibits in the original's order. The translation mass is the classifier's heuristic bulk (TRANS-UNANCHORED 56, TRANSLATION-ANCHORED 27), resolved here in aggregate per the class M convention: it is line-pair translation inside unmoved exhibits and body blocks, with no structural change riding in it. In-CSS text (R1): the exhibits' Chinese section comments are translated to Japanese (COMMENT-TEXT, 18 blocks; for example the `/*------- 变量 ------- */` variable banner of original L225 becomes its Japanese form), which is porter-visible only. Reader-visible CSS strings (CONTENT-STRING, 4 blocks) are translated with the body. R5 glyph-form conversion, stated separately: retained Chinese strings take Japanese glyph forms where the string survives (GLYPH-FORM, 6 blocks), distinct from full translation. Chinese survives in the candidate on exactly one line, the credit block's original-title field (candidate L12), where it is a quotation.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings). R5 is separated per the taxonomy so a reviewer can tell a converted string from a translated one.
- **Verify:** The body sections of diff.md in order; a Chinese-prose scan of candidate.txt outside the credit field returns nothing.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the one quotation.

### 7. Links

- **What:** The about prose's links change form: the original links the setting's article and the base theme intra-wiki (`[[[SCP-CN-3612]]]`, `[[[theme:dustjacket-sigma|…]]]`, original L19); the candidate converts both to labeled external-form links to the same pages on scp-wiki-cn.wikidot.com, with branch notes (candidate L21: SCP-CN-3612, and ダストジャケットSigma-9テーマ（中国語版）), because neither page has a JP counterpart to repoint to. Dr Hormress's user link and his ah-sandbox theme link are kept (candidate L21). The documentation's link to the author's test page on pokm.wikidot.com (original L76) is carried in translation. The credit source link (candidate L16) names scp-wiki-cn.wikidot.com, the recorded host, and serves the original.
- **Why:** P11: a prose link takes the JP counterpart where one exists and the serving original where it does not; the dead-reference standard is not engaged, nothing here is dead.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the prose links and the source link, all on the recorded host or the base author's own hosts.
- **Disposition:** Standing.

### 8. Structure

- **What:** No declared deviation beyond the delivery state of section 3, which is dispositioned there and in section 11. Variable names, selectors, and rule order inside the exhibits are preserved (the three exhibits stand at their original ranges and lengths), the variant mechanism (exhibits /2 and /3 behind the include-parameter comment trick) is preserved byte-for-byte in the tail module, and the exhibit census (theme-squares, image-block, the subtitle example, the three code exhibits) corresponds one to one in the same order, so no R3 deletion arises. The two EXHIBIT-RESTRUCTURE primaries are adjudicated in the class summary (an include repoint and a caption translation). The head's furniture swap (Rate and credit trio out, frame and preview block in) is sections 1–3, not a structural deviation.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census, not by the label.
- **Verify:** Compare `grep -n '\[\[code\|\[\[include\|\[\[collapsible' original.txt candidate.txt` — every exhibit form on the left has its counterpart on the right.
- **Disposition:** Standing; no class I item.

### 9. Formatting only

- **What:** No WS-ONLY or re-indentation class fired for this theme (0 blocks of either): the exhibits were edited in place without reformatting, so there is no formatting churn to disclose. The tail module's added lines (the JP loads and the override block) are content, recorded in sections 4 and 10, not formatting.
- **Why:** The formatting section states its ground when empty, so a reviewer does not have to infer it from silence.
- **Verify:** classification.json carries no WS-ONLY label for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation exists, riding inside the tail-module block the classifier labels DELIVERY-MOVE (B98): at candidate L732, `/* SCP-JP port: JP font fallbacks appended to the stacks (same typefaces as upstream, JP cuts). */`, introducing the stack-override block of section 4 (candidate L733–741). It is the port explaining its own device in the file, in English, and it is the only added comment; no `[!-- --]` note exists.
- **Why:** R2: annotations are part of the port's record; this one documents the override block's intent (appended fallbacks, not substitutions), which section 4 relies on.
- **Verify:** `grep -n 'SCP-JP port' candidate.txt` returns candidate L732 only.
- **Disposition:** Standing (part of the candidate as reviewed).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) The gate-tag item (P2): DISPOSITIONED at GOSIGN2-LEDGER §(c3) as T1 class (ii). (2) The live foreign code imports (P4): the tail module's kept CN own-code import and, in the same delivery family, the kept pokm base import — charged by T4 as MISSED with the "renders only because the CN site is up" wording (LOCALIZE-ROWS row 206) and DISPOSITIONED at §(c3) as "delivery class (ii): original-state CDN delivery". (3) The un-rehosted images (P5): T1's hotlink ×10 family, DISPOSITIONED at §(c3) as class (ii) / KB-58. (4) The render row's items (RENDER-ROWS-2, lane RENDER-S2-F (CN10)), none charged to the candidate at the ledger determination: the 344px@320 overflow on page and sample, recorded verbatim; the candidate-own runtime host chains (fastly.jsdelivr.net, the typekit hosts, pokm.wdfiles.com, the wanderers-library and scp-wiki-cn chains), recorded verbatim, which are items (2) and (3) seen from the render side; and the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5). The per-theme flag (item 1, the inherited credit selector) is flagged, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–4 as stated); the per-theme item flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 222): exit 1, 10 errors / 1 warn / 1 info; all ten errors are hotlink, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-F (CN10)): FINDINGS, the items of section 11(4), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 206, LOCALIZE-S2-E): FINDINGS / FINDINGS jointly, display-affecting findings 1 (the combined P4/P5 item), dispositioned at §(c3). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (diff.md): +179/−167 in 19 hunks, 98 classified change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:nameless-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 207; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the inherited `.creditButton p a` selector (flagged) Repaired after this package was built (FIX-CREDITBTN item 1, commit 1db8300): the selector now reads `.creditButton > a`; see the post-package repairs item below.

Exhibit /1 carries the theme's own credit-rule group, including `#page-content .rate-box-with-credit-button .creditButton p a` (original L556 → candidate L558), byte-identical on both sides. The campaign's T7 record (SUPPLEMENT-TYPES T7; KB-11) states the JP credit module emits the anchor as a direct child of `.creditButton`, without the `<p>` wrapper this selector requires, and sibling ports corrected exactly this shape (theme:sodium-jp in place, theme:jiha-jp by restatement). Here the rule stands uncorrected, so on the JP DOM it cannot match. The same flag is recorded for theme:mr-reprisal-jp and theme:oneiroi-west-jp in this batch (in oneiroi's case in both of its CSS copies); three occurrences in one batch of ten suggests the correction was applied only where a wave happened to touch the file, and that the inherited copies form a population a single sweep could settle. This package flags the selector with its evidence and does not edit the candidate; the theme's T4 row does not charge it.

### Item 2 — the holder field's provenance (note)

The candidate's credit block names Re_spectators as 著作権者 (candidate L13). The frozen original names no author anywhere: its credit trio carried placeholder bodies (页面信息, original L12–14), its exhibits carry no banner, and no byline appears in its prose (the only person it names is Dr Hormress, credited with the base work). The field's value therefore rests on evidence outside this package — the live page's authorship metadata or the wave's own record — and this package can neither confirm nor contradict it from the bytes. Recorded so a reviewer does not mistake the field for a value checked against the original; the based-on credit that the original does carry (Dr Hormress) is preserved in prose and in the kept base import, so no dropped-creator flag of the sibling standing arises.

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-CREDITBTN item 1 — KB-11 selector correction (landing 1db8300).** Commit 1db8300 changed candidate L558 from `#page-content .rate-box-with-credit-button .creditButton p a {` to `#page-content .rate-box-with-credit-button .creditButton > a {`, declarations untouched. The adjacent `.creditButton a`/`a:hover` descendant rules (L561, L564) are the original's mixed form and were left as inherited; the flagged rule takes KB-11's canonical `> a` form. T1 before/after identical (10/0/1).

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-nameless-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(4)). There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 无名城中的具名者 版式
- **Author:** Re_spectators
- **Source:** https://scp-wiki-cn.wikidot.com/theme:nameless — revision 6
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
