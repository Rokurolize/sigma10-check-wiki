# Review package — theme:food-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:food-jp — origin CN, population #189 [GOSIGN2-LEDGER (b) row 189]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0364dcc7cca090d4b68ac383f25d6f16ddba1a7ba42b56f3775690bddaafc174); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 0 infos (hotlink×4, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 167; GOSIGN2-LEDGER (b) row 189]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 337–419px@320/375. [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 188, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 188]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 189]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:food-jp.txt sha256:0364dcc7cca090d4b68ac383f25d6f16ddba1a7ba42b56f3775690bddaafc174; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 189) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×4 + pseudo-ref ×1 (classes (ii)/(iii), section 11); the render row's two items (KB-40 / KB-32+KB-33+KB-34, section 11); the T4 items P5, P7, P9 (section 11) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:food | theme:food-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 40 (first translation; the candidate's credit block records 初訳時参照リビジョン: 40) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-food.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:food-jp.txt`, copied at worktree HEAD b3ce875 |
| Lines / bytes | 370 lines / 8,687 bytes | 381 lines / 10,269 bytes |
| SHA-256 | 2e73fa341f96e111a7d00cd1f615ef79e425880aa8d2128b2f75b127dbbf1ce3 | 80e75915a5259c3be6c8ff2eac88a4f59a64d07909a31468ee27bbfea4ba8d77 |

Wave history: the candidate was created by the Stage 2 CN6 integration (commit 4166a2f, the LOCALIZE-S2-D wave's port); commit 95fd1d1 (rework2-p1) restored base deliveries for nine dropped pairs, this theme among them; 1869877 (FIX-CREDIT-D) normalized the translator attribution; a497307 (FIX4-MECH) removed a duplicated @import under KB-65. The sources.tsv note for this row records that the original has been superseded upstream since the reference revision, with the follow-up diff artifact `diff-food-from40.txt` in the campaign record (kind K5a-i): the port is judged against rev 40, and the upstream delta is a follow-up artifact, not part of this diff.

## Summary

A CN BHL-family port whose original carries its CSS twice (a live `[[module CSS]]` copy and a `[[code]]` source copy) behind a bare Rate and three head modules (CN BHL imports, a Google Fonts module, the theme CSS). The candidate keeps the code copy as the single delivered body (local--code /1, frame priority 3), rebuilds the base delivery around the JP BHL distribution (the JP BHL candidate include, the same two imports repointed to scp-jp.github.io, and interwiki frames at priorities 1 and 2 naming them), swaps in the JP preview credit block, and translates the exhibits — while three recorded items stay exactly as the original had them, each under a named disposition: the Chinese header strings (ruling 2), the four CN sandbox asset links (KB-58 deferred hosting), and the dropped Google Fonts load (the P7 disposition). Measured churn (diff.md, the generator's difflib count with autojunk off: +145/−136, 281 changed lines in 9 change blocks / 3 diff hunks — the small block count is the duplicated-CSS alignment, adjudicated in section 8).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 9 change blocks — 4 specific (44.4%), 1 heuristic (11.1%), 4 residue (44.4%), 0 skipped. The residue share is an artefact of this page's duplicated-CSS form (the frame insertions and the fonts-module deletion align as unlabeled blocks), not of unexplained change; every residue block is adjudicated below. Pattern citations name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| IFTAGS | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-MOVE | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): B2 (heuristic, CSS-BODY) is the BHL import repoint, P4/T9 in substance (section 3). The four residue blocks resolve as the two halves of the fonts-module deletion folded into the frame insertions (B3, B4; sections 3–4), the original's blank-line tail before its code closer (B7; section 9), and the candidate's added `[[/collapsible]]` for its source-code exhibit (B8; section 8). B6's EXHIBIT-RESTRUCTURE primary does not survive the exhibit census (section 8). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:food-jp; original theme:food on scp-wiki-cn at reference revision 40; candidate `pages/theme:food-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: standard, with the K5a-i follow-up note recorded in the Provenance above; no production JP counterpart exists, so the R4 adoption question does not arise). The candidate's head is rebuilt rather than inherited: an unconditional `[[iftags]]` wrapper carrying the JP BHL include (candidate L1–3), the repointed BHL import module (L5–9), two interwiki frames (L10–18), the centered-header include (L20), then the localized gate `[[iftags +テーマ]]` (L22).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frames are P6/T3, the base form is T9 (section 3).
- **Verify:** The sources.tsv row for food-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the frame changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a `[[>]]` wrapper (original L1–3) and nothing else — no info pair, no license box; its authorship record is the banner comment inside the CSS body ("Powered on 2023/02/25 … Created by fishalt, CC BY-SA 3.0"). The candidate deletes the bare Rate (B1) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L24–33) carrying the eight ruling-3 fields (タイトル 异常美食部 主题版式; 翻訳責任者 AI; 翻訳年 2026; 原題 异常美食部 主题版式; 著作権者 fishalt; 作成年 2023; 初訳時参照リビジョン 40; the source link to scp-wiki-cn.wikidot.com/theme:food). The タイトル field carries the theme's Chinese name unchanged, as does the 原題 field it translates from; the T4 row records the Chinese title field as a non-display/minor item, and the header-language question is dispositioned under ruling 2 (section 11). The CSS banner comment is carried over unchanged in the delivered CSS body. T7 credit-module CSS: none on either side (grep returns 0/0); nothing was added and no correction was needed. No license box is added: the original carried none, and the banner comment's CC BY-SA line travels with the CSS.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields; FIX-CREDIT-D (1869877) is the translator form arriving.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L24–33 against the eight fields.
- **Disposition:** Applied; the title field's language is DISPOSITIONED with the P9 item (section 11).

### 2. Includes and components

- **What:** The original's one live foreign include, `:scp-wiki:component:centered-header-bhl` (original L133), is repointed to `:scp-jp:component:centered-header-bhl` (candidate L20, inside B5). The candidate adds the JP BHL base include `:scp-jp:theme:black-highlighter-theme` at its head (candidate L2) and repeats it, with the centered-header include and the theme's own include, as escaped usage text (candidate L84–86). The theme's own line in that exhibit (candidate L85) as built read `@@[[include :scp-jp:theme:food]]@@`: the repoint changed the branch prefix but kept the plain slug, naming a page that does not exist on scp-jp; the usage-example population sweep has since completed it to `@@[[include :scp-jp:theme:food-jp]]@@` (see the per-theme record). One exhibit include keeps an unprefixed form: `[[include component:image-block` (candidate L69), inside the image exhibit; the T4 row recorded exactly this as a note item (unprefixed `component:image-block`, note), not a display-affecting finding. The candidate's remaining includes are the frames, credit, and license furniture of sections 1 and 3; every live include outside that exhibit names a `:scp-jp:` target.
- **Why:** P1 (KB-15) for the live repoint and the base include (T8/T9 family: the JP BHL port is the base this theme layers on). For the usage exhibit's own line, the as-built repoint satisfied the branch half of P1 only; the sweep's completion to the posting name is what brings it under the rule. The unprefixed exhibit include is sample text whose resolution is a posting-form matter; it is recorded here so it is not mistaken for a live foreign include.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the live list above; candidate L69 for the exhibit form.
- **Disposition:** Live repoints applied; the exhibit's unprefixed form is standing as recorded by the T4 row's note.

### 3. Delivery and code loading

- **What:** Three delivery changes, one per layer of the T3 stack. Base (T9): the original imports BHL from the CN distribution host (`@import url("https://bhl.scpwikicn.com/css/min/normalize.min.css")` and `black-highlighter.min.css`, original L7–8); the candidate repoints both imports to the JP distribution, scp-jp.github.io/Black-Highlighter (candidate L6–7, B2), adds the JP BHL candidate include (candidate L2), and names the same two files through interwiki frames at priority=1 (normalize) and priority=2 (BHL) (candidate L10–18). This triple form is the rework2-p1 restoration (95fd1d1) for a pair whose base delivery had been dropped; FIX4-MECH later removed a duplicated @import from it (KB-65), and the current bytes carry each import exactly once. Own layer (T3): the original delivered its own CSS from its live module copy; the candidate delivers from its code copy — a tail `[[module css]]` importing `local--code/theme%3Afood-jp/1` from the draft host (candidate L375–377, B9) and a third interwiki frame at priority=3 naming the same /1 (candidate L378–381, B9). The classifier's topology pass measures the body match directly: module-css → code-css at 0.98 similarity, code-other → code-css at 0.99 (the two originals of the delivered body). The head frames stand where the original's Google Fonts module stood (B3, B4; the fonts question is section 4).
- **Why:** P4/T9 (base delivery from the JP distribution) and P6/T3 (the layered frame stack: 1 normalize / 2 base / 3 own). The draft-host form of the own-layer lines is KB-41, class (iii).
- **Verify:** `grep -n '@import\|\[\[include' candidate.txt` against the list above; the topology figures are in classification.json.
- **Disposition:** DISPOSITIONED (draft-host own-layer lines, class (iii)); the base repoint and frame stack are applied.

### 4. Fonts and assets

- **What:** Fonts: the original loads Noto Sans TC and ZCOOL XiaoWei in a dedicated Google Fonts module (original L14–18). The candidate deletes that module entire (B3, B4) and loads no webfont: the stacks that named ZCOOL XiaoWei (`--header-font` and the h1–h6 rule, in both CSS copies) keep the name as their first entry with serif fallback, so Japanese text falls back to the viewer's serif — exactly the state the T4 row records (型 7, the original Google Fonts removal and its Japanese fallback). No JP font supplement (T5) was added for this theme. Assets: four URLs on the CN sandbox host scpsandboxcn.wikidot.com are kept byte-unchanged in both CSS copies: the `--logo-image` (candidate L163, L270) and the container background (candidate L251 area and its copy) — the author's own sandbox storage (`fishalt-2` folder), naming the theme's logo and background artwork. These are the T4 row's 型 5 items (CN sandbox direct links ×4) and the ledger's P5 disposition (KB-58).
- **Why:** P7's supplement is the usual case, not a rule without exception: the ledger dispositions this theme's P7 (section 11), and the byte record shows the porter's choice was to keep the original's display face as a named stack entry rather than substitute a JP face for a Chinese display script. P5/KB-58: assets on a third-party sandbox host are the deferred-hosting state — re-upload is barred by owner order, and posting is where the hosting question is settled.
- **Verify:** `grep -n 'fonts.googleapis\|font-family' candidate.txt` — no import line; the stack entries as listed. `grep -n 'scpsandboxcn' candidate.txt` — four hits, all in CSS variable/background lines, none in prose.
- **Disposition:** DISPOSITIONED (P7 font load, ledger §(c3); P5 assets, class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The header variables are set in both CSS copies and are carried over byte-unchanged from the original: `--header-title: "异常美食部"` and `--header-subtitle: "民以食为天"` (candidate L204–205 and L311–312; original L76–77 and L305–306), and `--logo-image` naming the sandbox-hosted artwork (section 4). The centered-header component is repointed (section 2). The theme's sidebar and topbar rules are inherited unmodified. The T4 row records the Chinese header strings (its L205-208/L312-315, the same lines in the row's numbering) as display-affecting 型 9 items; the ledger dispositions the P9 question under ruling 2 — header and title language is out of scope for migration correctness — so the strings stand in Chinese by decision, not by oversight.
- **Why:** P9/T6 is the variable class; ruling 2 is the disposition that governs its language. Recording the decision here is what separates a kept string from an untranslated one (KB-18 does not charge text a ruling has placed out of scope).
- **Verify:** `grep -n -- '--header-' candidate.txt` — the four lines above (two per CSS copy), byte-identical to the original's.
- **Disposition:** DISPOSITIONED (ruling 2; GOSIGN2-LEDGER §(c3) P9 line for this theme).

### 6. Text translation

- **What:** The exhibit body is translated throughout: the food heading and its reading (candidate L35 `+ 食物` kept as the specimen character, L40 `+++ しょくもつ`), the classical-Chinese quotations kept as quotations with Japanese readings added (candidate L46, L63 — the Tang and 後漢書 citations), the explanatory prose, the blockquote samples (candidate L128–138), the table sample (candidate L136–138), and the footnote sample. Simplified-Chinese forms inside retained quotations are converted where the candidate restates them in Japanese (R5 glyph-form conversion applies to the gloss text, e.g. 韦彪传 → 韋彪伝 in the gloss at candidate L63, while the quoted sentence itself keeps its original wording as a citation). Chinese survives as live text in the places sections 1 and 5 record: the credit title fields, the specimen heading, the header variables, and the quoted citations — each a quotation or a dispositioned string, none an untranslated instruction or label. The CSS banner comment (section 1) is carried over in English as the original had it.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings). Retained original-language text is itemized here and in sections 1/5 so a reviewer can tell quotation and disposition from residue.
- **Verify:** The exhibit pairs are diff.md's body sections in order; compare candidate L35–145 against original L136–246.
- **Disposition:** Standing (the port itself); the retained Chinese is itemized above, each item with its ground.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L32), naming scp-wiki-cn.wikidot.com/theme:food, the original's recorded host in sources.tsv — the serving form, not a defect. The T4 row's 型 5 items are the four sandbox asset URLs, which are CSS asset references, not prose links (section 4). The usage exhibit's include lines (candidate L84–86) are escaped sample text naming `:scp-jp:` targets. No prose link in the candidate targets a page that does not serve, and no link was repointed away from a serving original.
- **Why:** P11 under the dead-reference evidence standard: a link is charged when its target does not serve or a JP counterpart exists; neither holds here.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only prose hit; the remaining hits are the CSS asset lines of section 4.
- **Disposition:** Standing.

### 8. Structure

- **What:** The one structural question in this package is B6 (orig 126–247, recorded as a deletion at candidate L254, primary label EXHIBIT-RESTRUCTURE), and it does not survive an exhibit census. The original's form duplicates its CSS (live module, then exhibits, then a `[[code]]` copy of the same CSS) and the candidate's form delivers from the code copy with the exhibits ahead of it; the SequenceMatcher alignment therefore records the original's module tail, exhibit region, and code opener as one large deletion and their candidate counterparts inside other blocks. The census decides: the heading exhibit, the quotation exhibits, the blockquote and table and footnote samples, and the CSS body itself are present on both sides, translated as section 6 records — nothing was dropped or replaced, so the R3 question does not arise. The candidate's code exhibit gains the wave-standard collapsible wrapper (opens candidate L144; the added `[[/collapsible]]` is B8). One genuine relocation stands: the exhibits precede the delivered CSS in the candidate and follow the live module in the original, a consequence of the delivery conversion (section 3), not an exhibit decision. Variable names, selectors, and the CSS body's internal order are preserved (the topology similarities are 0.98/0.99).
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[code\|\[\[module\|しょくもつ\|食物' original.txt candidate.txt` and the exhibit lines cited in section 6.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** One residue block: B7 (original L364–367 → candidate at L370), the original's run of blank lines before its `[[/code]]` closer, normalized away in the candidate. The classifier finds no WS-ONLY block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Original L360–371 against candidate L360–373 in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. This candidate carries no `Ported for SCP-JP` banner, no `[JP]` markers, and no translator-note comments; its CSS banner comment is the original's own, carried over (section 1). The skeleton's "none" for this section survives contact with the bytes: a full-text search for annotation forms returns nothing outside the translated exhibit prose.
- **Why:** R2: the absence is recorded so a reviewer does not have to wonder whether annotations were overlooked; the port's provenance for this theme lives in the credit block and this package, not in in-file comments.
- **Verify:** `grep -n 'Ported for\|\[JP\]\|訳注' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Five items, each with its ground. (1) T1's four hotlink errors: class (ii) — the sandbox-host asset lines of section 4, posting-time hosting state (KB-58); the ledger's §(c1) hotlink line dispositions the class. (2) T1's one pseudo-ref error: class (iii), draft-wiki form — the candidate's own draft-host delivery lines (section 3). (3) The render row's two items: the page's runtime-hotlink site-theme chain (KB-40, environment-layer, not charged) and the sample's credit-modal errors plus 337–419px@320/375 overflow (KB-32 preview form; KB-33/KB-34 cross-cutting families). (4) T4's P5 item (the four sandbox links): DISPOSITIONED, class (ii) / KB-58, per the ledger's §(c3) line. (5) T4's P7 and P9 items: P9 (the Chinese header strings and title field) DISPOSITIONED under ruling 2; P7 (the dropped font load) DISPOSITIONED per the same §(c3) line. One record tension is flagged, not smoothed over: the ledger's §(c3) parenthetical describes the P7 item as "recorded without a display-affecting mark", while the LOCALIZE-ROWS row itself lists the font fallback among this theme's display-affecting items (型 7). The bytes support the row — Japanese text does fall back — and the disposition stands on the ledger's authority either way; the package records both wordings so the discrepancy is visible to the next reader of either record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all five items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 167): exit 1, 5 errors / 1 warn / 0 infos (hotlink×4, pseudo-ref×1); no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN6)): FINDINGS, the two items of section 11(3), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 188): FINDINGS jointly, display-affecting count 4 as the row records it (the header strings, the four sandbox links, and the font fallback), with the title field, a heading-level item, the empty-iftags structure, and the unprefixed image-block include recorded as non-display/minor; the ledger's §(c3) line dispositions P5, P7, and P9 for this theme, and records no unincorporated upstream updates question beyond the K5a-i note in the Provenance. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +145/−136 in 9 change blocks / 3 diff hunks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:food-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 189; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The duplicated-CSS form and the dropped live module

This theme's original is one of the population's duplicated-delivery pages: the same CSS body appears as a live `[[module CSS]]` and as a `[[code]]` source exhibit. The port keeps one delivered body — the code copy, delivered by local--code — and the live module copy is deleted. A reviewer comparing module counts will see a module "missing"; the deciding check is the topology measurement in classification.json (the candidate's delivered body matches the original's module body at 0.98 and its code body at 0.99), together with the render record, which reports no unstyled-content finding for this theme. The form is the wave's standard conversion for duplicated pages, and it is why this package's diff has 3 hunks for 281 changed lines.

### The usage example's posting name

The usage example at candidate L85 as built read `@@[[include :scp-jp:theme:food]]@@`: the porting wave's repoint changed the branch prefix but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to this candidate's posting name, `:scp-jp:theme:food-jp` — candidate L85 now reads `@@[[include :scp-jp:theme:food-jp]]@@` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-food-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The base include `:scp-jp:theme:black-highlighter-theme` is another candidate in the population with its own package; this theme's record names it as a dependency, not a change. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 异常美食部 主题版式
- **Author:** fishalt
- **Source:** https://scp-wiki-cn.wikidot.com/theme:food — revision 40
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
