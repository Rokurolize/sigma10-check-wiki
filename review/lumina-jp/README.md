# Review package — theme:lumina-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:lumina-jp — origin EN, population #110 [GOSIGN2-LEDGER (b) row 110]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now c3629fe0d2802ab63b640443c3078f98ce43f63917a8024df5237a7fb9462542); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 110; GOSIGN2-LEDGER (b) row 110]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 512–519px@320/375 (page) and 512–519px@≤375 + 859px@768 (sample); runtime-hotlink site-theme chain + cdn.jsdelivr.net (page), one sample combo http.cat among hosts; sample credit-modal (preview-form); T3 clean on both pages. [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 110, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 110]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 110]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:lumina-jp.txt sha256:c3629fe0d2802ab63b640443c3078f98ce43f63917a8024df5237a7fb9462542; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 110) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×3 and pseudo-ref ×3 (sections 4 and 3); the render row's items (section 11); T4's two findings (P4 base delivery, P5 served-source assets) dispositioned class (ii), with the P4 item's file history recorded in section 3 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:lumina | theme:lumina-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 27 (first translation; the candidate's credit block records 初訳時参照リビジョン: 27) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-lumina.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:lumina-jp.txt`, byte-identical to the canonical file in its post-sweep state (the usage sweep's repair, canonical commit b5cb724, landed after this batch's snapshot; see the per-theme record) |
| Lines / bytes | 712 lines / 22,257 bytes | 717 lines / 23,185 bytes |
| SHA-256 | e9116a6ace87e15a07402662c8039ee73535282ec5740223048854dad6541c99 | c3629fe0d2802ab63b640443c3078f98ce43f63917a8024df5237a7fb9462542 |

Wave history: the candidate was created by the Stage 2 EN14 integration (commit 49c7627, importing its base from the EN CDN and carrying the translator value SCP-JP), then touched by f1138e4 (GOSIGN2 FIX-P4: the head's base imports repointed to the basalt JP candidate's delivery, and the translator field normalized to AI in the same pass), a497307 (FIX4-MECH: the duplicated base import removed, KB-65, and the font URL grammar repaired, KB-04), and b5cb724 (the usage-example sweep). The theme is a dependent theme of kind K5b-3 (sources.tsv): the candidate layers over theme:basalt-jp, and this package's diff covers the theme's own layer only — the base's own layer is the basalt-jp package's subject. Its delivery relationships get explicit treatment in section 3, as the brief for dependent themes requires.

## Summary

A small dependent-theme port whose interest is concentrated in its delivery and its fonts. The original layers a personal theme (Lumina Crash, by EstrellaYoshte) over the Bedrock variant of Basalt: its head module imports the base's two stylesheets from the EN CDN (cdn.scpwiki.com), its own CSS is served by a tail module outside the tag gate, and its credit furniture is a labeled bare Rate plus prose attribution. The candidate repoints the base delivery to the basalt JP port candidate's own delivery address (the FIX-P4 wave's pattern-4 repair), keeps its own tail delivery in draft-host form, swaps the Rate for the JP preview credit block, translates the documentation body and the CSS banner and comments, and — the batch's contrast case on fonts — repairs its font loads properly: the original's bunny.net URLs used a kebab-case family grammar that names the families in a form the delivery could not serve as written, and the candidate rewrites them into Google Fonts form for the same families and adds Noto Sans JP (the ledger's KB-04 entry records this theme as FIXED by FIX4-MECH). Its three background images stay on EN storage as served-source lines, dispositioned class (ii). Measured churn (diff.md, the generator's difflib count with autojunk off: +64/−62, 126 changed lines in 38 change blocks / 14 hunks; a GNU-diff count of the same pair gives 107 changed lines — the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 38 change blocks — 21 specific (55.3%), 13 heuristic (34.2%), 4 residue (10.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 15 |
| TRANSLATION-ANCHORED | 10 |
| COMMENT-TEXT | 7 |
| DELIVERY-HOST | 3 |
| DRAFT-HOST | 3 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| SELF-DELIVERY | 2 |
| WS-ONLY | 2 |
| ANNOTATION | 0 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 1 CSS-BODY block is the font-variable supplement (B23, section 4); the 1 EXHIBIT-RESTRUCTURE block is the tail interwiki include's repoint (B36, section 3), not a restructuring — the exhibit census is complete; the 4 residue blocks are two CSS section-banner comment translations the classifier left unlabeled (B29, B32, section 6), a blank line added ahead of the closing gate at the tail (B34, section 8), and the deleted `[[/div]]` of the original's tail wrapper (B38, section 3). The CREDIT-PROSE label rides on the intro line's translation block (B4); the prose itself is section 6. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:lumina-jp; original theme:lumina on scp-wiki at reference revision 27; candidate `pages/theme:lumina-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN14 wave (sources.tsv kind K5b-3, a dependent-theme kind: the candidate layers over theme:basalt-jp and this package's diff covers the theme's own layer only). The original opens with its tag gate ahead of its head module (original L1–2); the candidate places its head delivery module ahead of the localized gate (candidate L1–5), the frame order the self-delivering candidates in this population use.
- **Why:** Section 0 declares the provenance route and the layering scope so every later count is read against the right baseline: changes to the base's layer are not this package's to narrate. The gate is P2; the delivery is section 3.
- **Verify:** The sources.tsv row for lumina-jp (kind K5b-3 and its note); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route and scope themselves).

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare Rate under a bold "**Rating:**" label inside a right-aligned div (original L7–10, block B3), plus prose attribution in the intro: the theme was created by [[*user EstrellaYoshte]] for personal use (original L12). The candidate deletes the Rate and its label, and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L7–16) carrying the eight ruling-3 fields (title Lumina Crash Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 Lumina Crash Theme; 著作権者 EstrellaYoshte; 作成年 2023; 初訳時参照リビジョン 27; the source link, section 7). The author field names EstrellaYoshte in plain form, matching the original's naming; the original's own CSS banner agrees (it credits EstrellaYoshte as the author of Lumina Crash and of the Generic Space Theme it is based on — the banner's translation at candidate L86–89 keeps both credits, section 6), so no named creator is dropped. The translator field was created with the value SCP-JP and took its ruling-3 form (AI) in f1138e4. No license box is appended in this candidate, and the original carries none; the theme's three images are the original author's own files on EN storage (section 4), and no TASL supplement was added for them — the credit block and the banner carry the attribution the original itself makes.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L7–16 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** The include repoints: the tail's interwiki-style include, `:scp-wiki:component:interwiki-style` → `:scp-jp:component:interwiki-style` (block B36; its theme= parameter is section 3); and the credit includes (section 1). The usage example's two escaped includes are exhibit text (block B6, ESCAPED-INCLUDE): their repoints and names are treated in section 7. The head's base delivery is an @import, not an include, and is treated in section 3. No other live include changes fire.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; both repointed targets have verified JP counterparts. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include names a `:scp-jp:` target.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery relationships, stated explicitly because this is a dependent theme. The original has two deliveries. Its base delivery: a head `[[module css]]` importing Basalt's normalize and bedrock stylesheets from the EN CDN, `cdn.scpwiki.com/theme/en/basalt/normalize-min.css` and `basalt-bedrock-min.css` (original L3–4) — the base is imported, not inlined, and it is the upstream branch's CDN form of the base. Its own delivery: a tail `[[module css]]` importing its own `local--code/theme%3Alumina/1` from scp-wiki.wdfiles.com, with an interwiki-style include at priority 3 naming the same, the pair wrapped in a `[[div_]]` and placed outside the tag gate (original L704–712). The candidate's base delivery: a head `[[module CSS]]` importing `local--code/theme%3Abasalt-jp/1` from the draft host (candidate L2) — that address is the basalt JP port candidate's own delivery, so the candidate imports its base in the form of the base's JP port candidate, not the upstream CDN form and not the production page. That form arrived in two steps: at creation the head still imported the EN CDN pair; f1138e4 (FIX-P4, the pattern-4 repoint of base-theme CSS imports to JP port candidates) replaced both CDN lines with the basalt-jp/1 address (duplicated, one per replaced line), and a497307 removed the duplicate (KB-65). The candidate's own delivery keeps the original's tail topology: a `[[module css]]` importing `local--code/theme%3Alumina-jp/1` from the draft host and an interwiki-style include at priority 3 naming the same (candidate L712–716), still outside the tag gate; two byte-level untidinesses ride with it — the module's @import line has no trailing semicolon, and the include's parameter is written `| theme= https://…` with a space after the equals sign — and the original's `[[div_]]` wrapper around the tail include does not survive (block B38). The three draft-host lines (head base import, tail own import, tail priority-3 parameter) are T1's three pseudo-ref errors.
- **Why:** Ruling 1 is the governing rule for dependent themes: a dependent theme imports the base theme's JP port candidate delivery rather than the raw upstream branch delivery — the FIX-P4 repoint is that rule applied to this file, and the original's EN CDN form is exactly the raw upstream delivery the rule excludes. P4/T9 (delivery served from the JP side) for the frame as a whole; the draft-host form of all three lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** Read candidate L1–3 and L710–717 against original L1–5 and L704–712; `grep -n 'cdn.scpwiki' candidate.txt` returns nothing; `git log --oneline -- pages/theme:lumina-jp.txt` in the canonical repo shows the f1138e4 and a497307 steps.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the ledger's P4 disposition is quoted and discussed in section 11.

### 4. Fonts and assets

- **What:** Fonts (block B22): the original's code exhibit loads two families from fonts.bunny.net in bunny's kebab-case grammar, `family=barlow-semi-condensed:300,300i,400,400i,700,700i` and `family=space-grotesk:300,400,700` (original L86–87). The candidate rewrites both loads into Google Fonts form for the same families and weights (`family=Barlow+Semi+Condensed:…`, `family=Space+Grotesk:…`) and adds Noto Sans JP in the same form (candidate L92–94). The stacks follow (block B23): `--header-font-primary` and `--UI-font-primary` gain the `'Noto Sans JP'` fallback, and a `--body-font-primary: 'Inter', 'Noto Sans JP'` variable appears that the original's :root did not define (it inherited the base's) — the candidate pins it explicitly with the JP fallback appended; Inter is the base delivery's family, so the pin names a face the base loads. Assets: the theme's three background images stay at their EN-storage addresses byte-identically in the code exhibit — `--lumina-background` (bg-galaxy.jpg), `--lumina-header-image` (moon.png), `--lumina-footer-image` (earth.png), all under `scp-wiki.wdfiles.com/local--files/theme%3Alumina/` (candidate L138, L139, L142). Those are T1's three hotlink errors and T4's finding (b).
- **Why:** P7/T5 with KB-04 (font loads failing at the delivery layer): the bunny grammar as written names the families in a kebab-case form the load could not serve as intended; the repair keeps the families and changes the grammar, which is why this theme is the batch's font contrast case — its faces load. The ledger's KB-04 summary records the outcome in one line: FIXED for lumina (FIX4-MECH). P5 with KB-58 for the assets: served-source lines naming the original author's own EN-storage files are class (ii), retained as the original serves them.
- **Verify:** `grep -n '@import' candidate.txt` — the head delivery line and the three font loads, all in serving form; `grep -n 'wdfiles' candidate.txt` — the three asset lines and the tail delivery lines only.
- **Disposition:** Fonts FIXED (FIX4-MECH, KB-04); assets DISPOSITIONED (class (ii) / KB-58).

### 5. Header and sidebar furniture

- **What:** The theme's rendered header strings are translated in this candidate (block B24): `--header-title: "LUNAR AREA-32"` → `"月面エリア-32"` and `--header-subtitle: "Database Archive"` → `"データベース・アーカイブ"` (original L138–139 → candidate L144–145). No other header or sidebar variable changes fire; the logo and background variables are section 4's asset lines, unchanged in form.
- **Why:** Ruling 2 takes header and title language out of Sigma-10 migration scope as case-by-case translation taste; most candidates in this population keep the original's strings and have the keeping dispositioned as P9, and this candidate's porter exercised the same taste space in the other direction. Neither direction is a finding, and no ledger record charges this theme on the point — the section exists so the rendered-string change is on the record rather than passed over.
- **Verify:** `grep -n 'header-title\|header-subtitle' candidate.txt` — the two translated strings.
- **Disposition:** Standing (ruling 2 taste space; nothing charged, nothing to disposition).

### 6. Text translation

- **What:** The documentation body translates throughout: the intro (including the Bedrock base attribution, candidate L18), the usage prose, the grid-layout documentation with its `{{#page-content}}`, `{{content}}`, and `{{breakout-start}}` placeholder exhibits (the placeholders themselves are Wikidot layout tokens the theme documents, and they stay byte-identical, as they must), and the code exhibit's banner and section comments. The banner translation (block B21, candidate L86–89) renders the original's "By EstrellaYoshte / Based on: Generic Space Theme by EstrellaYoshte" as 作者： EstrellaYoshte / ベース: Generic Space Theme（EstrellaYoshte作） — both of the original's credits survive translation. The COMMENT-TEXT mass (7 labeled blocks) is the CSS comment translation, and the 2 unlabeled residue blocks in this range are the same shape (B29: `/*-------- MAIN --------*/` → `/*-------- 本文 --------*/`; B32: `/*-------- BOTTOM AREA --------*/` → `/*-------- 下部領域 --------*/`), resolved here by shape as the class-M appendix treatment prescribes.
- **Why:** P9/P10 (prose, documentation, and comments into Japanese). The placeholder tokens are the counterweight case: they are syntax the documentation is *about*, and translating or altering them would falsify the documentation — the port translates around them and leaves them exact.
- **Verify:** Read candidate L18–30 against original L12–24 for the intro and usage prose; `grep -n '{{' candidate.txt` — the placeholder exhibits, unchanged in form.
- **Disposition:** Applied (the theme's T4 record shows no translation finding; its two findings are sections 3 and 4).

### 7. Links and references

- **What:** Three link acts. (1) The credit block's source link names the original at its recorded host (scp-wiki.wikidot.com, section 1) — host check clean. (2) The intro's base link: the original's `[[[theme:bedrock|Bedrock]]]` becomes `[[[theme:bedrock-jp|Bedrock]]]` (candidate L18), naming the base's JP port candidate page, consistent with the delivery form of section 3. (3) The usage example's two escaped includes (candidate L22–23): they now read `:scp-jp:theme:bedrock-jp` and `:scp-jp:theme:lumina-jp`. At this batch's snapshot both named plain forms (`:scp-jp:theme:bedrock`, `:scp-jp:theme:lumina`) — the base's line was the same defect shape as the self line, since the base's JP candidate posts as theme:bedrock-jp — and the population sweep repaired both lines after the verdict (per-theme record). The example's escaping (`{{@@[[include …]]@@}}`) is retained exactly, so the example still prints as literal text.
- **Why:** P1/P9 link hygiene: prose and example references must name the pages that will exist on the JP side. The example is the text a user copies to install the theme, so its names are held to the same standard as live includes.
- **Verify:** `grep -n 'scp-jp:theme:' candidate.txt` — the two example lines, both in -jp form; `grep -n 'theme:bedrock' candidate.txt` — the intro link and the example, consistent.
- **Disposition:** Applied; the example lines' post-verdict repair is recorded in the per-theme record.

### 8. Structure and exhibits

- **What:** No restructuring: the exhibit census is complete against the original (intro and usage documentation, the grid-layout documentation exhibits, the full code exhibit), and the classifier's single EXHIBIT-RESTRUCTURE block is the tail include's repoint (section 3). Two byte-level items ride at the tail: a blank line added ahead of the closing `[[/iftags]]` (block B34, candidate L708), and the tail frame's untidiness recorded in section 3 (the dropped `[[div_]]` wrapper, the missing semicolon, the spaced parameter). The page's own layer is the whole diff (kind K5b-3): nothing of the base's layer is inlined or rewritten here.
- **Why:** P8 (exhibit structure follows the original) governs the census; the tail items are recorded because the tail is where this theme's delivery lives, and a reader comparing frames should not have to discover them.
- **Verify:** The block list in classification.json against the original's section census; read candidate L705–717 against original L700–712 for the tail.
- **Disposition:** Standing (nothing to disposition).

### 9. Formatting only

- **What:** Two whitespace-only blocks (B26, B27: original L247 and L255 → candidate L253 and L261), single lines inside the code exhibit whose only change is whitespace. They are counted here so the heuristic mass is not mistaken for content change; nothing else in the diff is formatting-only.
- **Why:** Stated so the formatting mass is separated from content mass, per the class treatment: whitespace inside a code exhibit changes nothing the exhibit renders or documents.
- **Verify:** Blocks B26 and B27 in classification.json (label WS-ONLY).
- **Disposition:** Standing (nothing to disposition).

### 10. Porter annotations

- **What:** None. Checked explicitly: the candidate carries no porter comment, no translator's note, and no annotation block (the classifier's ANNOTATION count is 0, and a read of the head, credit zone, and tail finds no annotation prose). The judgments this port embodies — the base-delivery repoint, the font grammar repair — are recorded in the canonical commit messages (f1138e4, a497307) rather than in the file.
- **Why:** T11 asks that judgment calls stay auditable; here the audit trail is the commit record, and the section states the in-file absence as a checked fact so a later reader does not search for an annotation that was never written.
- **Verify:** `grep -n '訳注\|porter\|JP localization' candidate.txt` — the only "JP localization"-family text is the credit block's own fields; no annotation stands in the file.
- **Disposition:** Standing (absence recorded).

### 11. Dispositions and exceptions

- **What:** Four standing items, all closed. (1) T1's pseudo-ref ×3 (section 3): class (iii), sanctioned draft-host form. (2) T1's hotlink ×3 and T4's finding (b) (section 4): the three EN-storage background images, DISPOSITIONED class (ii) / KB-58. (3) T4's finding (a), the P4 base delivery: the localize ledger dispositions it as "P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery)" (GOSIGN2-LEDGER line 1503). The bytes tell a fuller story, and this package follows the bytes: the EN CDN import the finding charged was the candidate's state at localize-check time, and the FIX-P4 wave subsequently repointed the head delivery to the basalt JP candidate's address (f1138e4, section 3), so the candidate as it now stands loads no EN CDN at all. The disposition is quoted as recorded; the delivery's current form is as section 3 states. (4) The render row's items: page-overflow of 512–519px at the 320/375px viewports on the theme page and the sample (with 859px at 768px on the sample); a runtime-hotlink in the site-theme chain plus a cdn.jsdelivr.net reference on the page (the chain the page loaded at review time, when its head still imported the EN CDN — the same pre-repair state item (3) records); one sample combination with http.cat among its hosts; and the sample's credit-modal reading, dispositioned preview-form (the standing GOSIGN-TESTS T2 amendment: credit:start-preview has no modal mechanism). T3 was clean on both pages.
- **Why:** A disposition names its ground: class (iii) for the draft host, class (ii) / KB-58 for the served-source assets, the ledger's own words for the P4 item with the file's later history stated beside them, and the preview-form amendment for the modal reading. Nothing in this theme rests on an unnamed exception.
- **Verify:** The theme's rows in T1-ROWS, LOCALIZE-ROWS, and RENDER-ROWS-2; the disposition lines in GOSIGN2-LEDGER (line 1503 for this theme, line 1676 for the KB-04 fix).
- **Disposition:** DISPOSITIONED (all four, on the grounds named).

### 12. Verification record

- **What:** T1 (source check, T1-ROWS row 110): hotlink ×3, pseudo-ref ×3 (6 errors / 1 warn / 1 info) — every error is one of the served-source or draft-host lines dispositioned above. T4 (localize check, LOCALIZE-ROWS row 110, wave LOCALIZE-S2-B): FINDINGS, 2 findings — (a) P4 EN CDN Basalt base (display-affecting), (b) P5 EN-storage bg-galaxy/moon/earth served source (display-affecting); the row also records no unincorporated upstream updates. T2/T3 (render check, RENDER-ROWS-2, wave RENDER-S2-C (EN14)): the readings of section 11, T3 clean on both pages. The go-sign ledger row (§(b) row 110) aggregates T1 FINDINGS (classified), T2 FINDINGS, T3 FINDINGS, T4 FINDINGS, T5 PASS — every finding classified, none OPEN.
- **Why:** The counts are the acceptance evidence for the sections above: each checker's scope is stated so a clean result is not read past what the checker can see (T1 reads this file; the render check is what saw the loaded chain).
- **Verify:** The three ledger-part files named above, row 110 in each and the theme's render row; GOSIGN2-LEDGER §(b) row 110 for the aggregate.
- **Disposition:** PASS at the ledger determination, with the items of section 11 dispositioned as recorded.

## Per-theme record

Two items belong to this theme alone.

**The usage example's self-reference — and its base reference — were repaired after the verdict.** At this batch's snapshot the example (candidate L22–23) read `:scp-jp:theme:bedrock` and `:scp-jp:theme:lumina`: both plain forms, the base's line defective in the same way as the self line because the base's JP port candidate posts as theme:bedrock-jp (the name the candidate's own intro link already used). The population sweep repaired both lines (canonical commit b5cb724, a single -jp insertion on each), and this package is built against the repaired candidate. The same repair reached the mcf, maxwell, laruetheme, laughter-and-knives, and legend-of-blue packages in this batch.

**This theme is the batch's font contrast case.** Where laruetheme and laughter-and-knives lost their originals' Latin font loads entirely (flagged as defects in their packages), lumina's loads were defective in grammar rather than absent — the bunny.net kebab-case family form — and the FIX4-MECH wave repaired them into serving Google Fonts form for the same families (KB-04, recorded FIXED for this theme at GOSIGN2-LEDGER line 1676). The three themes together show the two failure shapes of the same pattern (P7): a load dropped, and a load whose URL names the family in a form the host does not serve.

## Change set outside the two diffed files

| File | Change |
|---|---|
| `pages/theme-decoration-sample-lumina-jp.txt` | The theme's decoration sample: a JP page applying the candidate, the surface the T2/T3 render checks measured (section 11's sample readings) |
| `pages/theme:basalt-jp.txt` (the base candidate) | Not part of this package's change set, but this candidate's delivery imports that candidate's /1 code (section 3); the base's own port is documented in the basalt-jp review package |

## License and attribution

- **Title:** Lumina Crash Theme
- **Author:** EstrellaYoshte
- **Source:** https://scp-wiki.wikidot.com/theme:lumina — revision 27
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
