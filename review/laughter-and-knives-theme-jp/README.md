# Review package — theme:laughter-and-knives-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:laughter-and-knives-theme-jp — origin EN, population #108 [GOSIGN2-LEDGER (b) row 108]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0bf68d535ca68844eee6c8614a510e246fd3d7f3c94d5e7f91a7a388dbfbfb79); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 1 warn / 3 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 98; GOSIGN2-LEDGER (b) row 108]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + sidebar-not-opening [webkit 768/375]; sample T2 no machine verdict (exit 2); T3 "MAN ZOO LEAGUE" subtitle faint/overlapping at 375 (minor). [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 108, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 108]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 108]
- Computed against: canonical commit 41048ca2b13766899b5c5d5d426a980ad00f8a04; candidate file pages/theme:laughter-and-knives-theme-jp.txt sha256:0bf68d535ca68844eee6c8614a510e246fd3d7f3c94d5e7f91a7a388dbfbfb79; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 108) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×2 (section 3); the render row's items (section 11); T4's one finding (P9) dispositioned under ruling 2. One defect is flagged in the per-theme record, not hidden: the original's Latin font load has no counterpart in the candidate, the same shape as the laruetheme flag in this batch |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:laughter-and-knives-theme | theme:laughter-and-knives-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 58 (first translation; the candidate's credit block records 初訳時参照リビジョン: 58) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-laughter-and-knives-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:laughter-and-knives-theme-jp.txt`, byte-identical to the canonical file in its post-sweep state (the usage sweep's repair, canonical commit b5cb724, landed after this batch's snapshot; see the per-theme record) |
| Lines / bytes | 915 lines / 26,979 bytes | 912 lines / 28,477 bytes |
| SHA-256 | bca761afe91decff45c7a547eee3db7fb7b8cab41f37f569119a799ca227c38a | 5e93cbb732c1fcf86f0ffd7455add722cac64c5eca846a9c3f24ae4cb46cc355 |

Wave history: the candidate was created by the Stage 2 EN13 integration (commit d7c1af6), then touched by 1869877 (FIX-CREDIT-D, translator-attribution normalization) and a497307 (FIX4-MECH, duplicate @import removal, KB-65). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. This theme is a dependent theme: the original layers over the Black Highlighter base, and the candidate's delivery relationships are treated in section 3.

## Summary

A mechanical port with the same rebuilt delivery frame as its sibling laruetheme, and the same font defect. The original is a Black Highlighter-based EN theme (the Man Zoo League theme): its head module imports the base's two stylesheets from the author's GitHub and adds four page-local rules, its own CSS lives in the page's code exhibit and is re-delivered by a tail module outside the tag gate, and its credit furniture is a bare Rate module. The candidate repoints the base delivery to the JP side in the population's form for BHL-based themes, moves its own delivery into the head frame, swaps the Rate for the JP preview credit block, translates the exhibit body (including the theme-squares color names), appends a license box whose entries honestly record what the original does and does not state, and deletes exactly one CSS declaration — a background pointing at a decorative image on a personal CDN that no longer serves it — with the ground stated in the file itself. Measured churn (diff.md, the generator's difflib count with autojunk off: +136/−145, 281 changed lines in 63 change blocks / 4 hunks; a GNU-diff count of the same pair gives 237 changed lines — the difference is alignment choice, not content). One defect is flagged in the per-theme record with probe evidence: the original loads its two Latin display faces (Chicle, Overlock) from fonts.bunny.net, and nothing in the candidate or in its base delivery loads them, while the stacks still name them first.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 63 change blocks — 31 specific (49.2%), 30 heuristic (47.6%), 2 residue (3.2%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 31 |
| TRANSLATION-ANCHORED | 21 |
| EXHIBIT-RESTRUCTURE | 4 |
| DRAFT-HOST | 4 |
| INCLUDE-REPOINT | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 3 |
| CSS-BODY | 2 |
| ANNOTATION | 1 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 2 CSS-BODY blocks are the font-variable stack rewrites (B58, section 4) and the deleted dead-asset background declaration (B60, section 8); the 4 EXHIBIT-RESTRUCTURE primaries are the head delivery zone (section 3), the credit zone (section 1), the theme-squares repoint (section 2), and the tail delivery's deletion (section 3); the 2 residue blocks are an alignment artifact pairing the BHL note line with a heading (B22, section 6) and a blank-line deletion at the code exhibit's tail (B61, section 9); the ANNOTATION block is the license box's translator note (B62, section 10). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:laughter-and-knives-theme-jp; original theme:laughter-and-knives-theme on scp-wiki at reference revision 58; candidate `pages/theme:laughter-and-knives-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN13 wave (sources.tsv kind: standard; no production JP counterpart of the theme itself is recorded, so the R4 adoption question does not arise — the production page in this port's life is its base, section 3). The original opens with its tag gate ahead of its head module (original L1–2); the candidate places the base include and the delivery frame ahead of the localized gate (candidate L1–20), the wave-standard frame form.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate is P2, the frame is P4/P6 (section 3).
- **Verify:** The sources.tsv row for laughter-and-knives-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a right-aligned div (original L33–35, inside block B5), and nothing else: no info pair, no license box, and — checked explicitly — no author named anywhere in the file (its code banner is the Black Highlighter theme template's boilerplate, not an attribution). The candidate deletes the Rate and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L22–31) carrying the eight ruling-3 fields (title ラフター・アンド・ナイブズ テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Laughter and Knives Theme; 著作権者 [[*user Woedenaz]]; 作成年 2019; 初訳時参照リビジョン 58; the source link, section 7). The field records the theme page's author; since the original file names no author, there is no in-file attribution for the field to drop or contradict. The translator field took its ruling-3 form in 1869877. The candidate also appends a license box before the gate closes (candidate L899–911, block B62): a `:scp-jp:component:license-box-backend`/`license-box-end` pair with one entry for the theme's logo file (mzl-logo.svg, author Woedenaz, distributed in the original as the Man Zoo League logo) stating that the original carries no license statement for it and advising confirmation with the author before posting, with its source on the EN wiki — and a translator's note (訳注) recording the bobble.png deletion of section 8. The original carries no box; the box is an added attribution record (T12), and its "no license stated" wording is the honest form of it.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields and the translator credit form; the license box is the campaign's TASL record-keeping applied to a theme whose assets arrived without one.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L22–31 against the eight fields, and candidate L899–911 for the license box.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the license box is a standing supplement.

### 2. Includes and components

- **What:** The include repoints: the two interwiki-style includes of the original's frame (:scp-wiki: → :scp-jp:, blocks B3/B4; their theme= parameters are section 3); the theme-squares exhibit's include, `:scp-wiki:component:theme-squares` → `:scp-jp:component:theme-squares` (block B7, original L45 → candidate L37; its color-name parameters are section 6); and the credit and license-box includes (section 1). The head's base include, `[[include :scp-jp:theme:black-highlighter-theme]]` (candidate L1), is a delivery line and is treated in section 3. The usage example's two includes are exhibit text and are treated in section 7.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; all repointed targets have verified JP counterparts, so all are repointed and none is kept as an exception. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include names a `:scp-jp:` target.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The delivery is rebuilt, in the same form as the laruetheme package's. The original delivers in three places: a head `[[module css]]` importing Black Highlighter's normalize and base stylesheets from nu-scptheme.github.io (`/css/min/` paths, original L3–4) plus four page-local rules for the theme page itself (image-block margins and borders, and a rainbow animation for the ninth square of its own theme-squares exhibit, original L5–28); two interwiki-style includes at priorities 1 and 2 naming the same base files (original L30–39's zone); and, outside the tag gate at the page's tail, a `[[module css]]` importing its own `local--code/theme%3Alaughter-and-knives-theme/1` from scp-wiki.wdfiles.com with a third interwiki-style include at priority 3 naming the same (original L909–915, block B63) — the tail pair is what serves the page's own code exhibit as the theme's CSS. The candidate delivers in one place: `[[include :scp-jp:theme:black-highlighter-theme]]` (candidate L1) pulls the production JP Black Highlighter page, the form every BHL-based candidate in this population uses (theme:doap-bhl-jp, theme:fmd-bhl-theme-jp, and theme:minimalist-bhl-jp open with the identical line, read for the laruetheme package); a head `[[module CSS]]` imports the candidate's own `local--code/theme%3Alaughter-and-knives-theme-jp/1` from the draft host (candidate L3–5); and three interwiki-style includes at priorities 1, 2, and 3 name the base's files on the JP mirror host scp-jp.github.io and the candidate's own /1 on the draft host (candidate L7–17). The tail module is deleted, and the tag gate now wraps the whole page, license box included. The code exhibit itself opens with the two base imports from scp-jp.github.io (candidate L185–186), so the served /1 is self-contained where the original's exhibit relied on the page's head frame for the base. One loss rides with the rebuild, recorded here rather than hidden: the head module's four page-local rules have no counterparts in the candidate — the three image-block rules (the base's own stylesheet styles image blocks) and the `.colors-container .subcolors .color:nth-of-type(9)` rainbow animation rule (original L20–27), which animated the ninth square of the theme page's own theme-squares exhibit; the exhibit still declares the `--pastel-rainbow` variable and the theme's CSS still uses it (candidate L464, L792, L841), but the exhibit-square animation itself is gone (see the per-theme record). The draft-host lines in this frame are T1's two pseudo-ref errors.
- **Why:** Ruling 1: a dependent theme imports its base theme's JP delivery rather than the raw upstream branch delivery — for BHL-based themes the population's JP delivery is the production BHL page plus its JP mirror host, which is what the bytes show. P4/T9 (delivery served from JP hosts) and P6/T3 (the interwiki-style frame, here with the base at priorities 1–2 and the theme's own layer at priority 3, preserving the original's cascade order). The draft-host form of the own-code lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** Read candidate L1–20 against original L1–39 and L909–915; `grep -n 'local--code' candidate.txt` returns the head import and the priority-3 parameter, both draft-host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the frame rebuild itself is the applied port, with the rule losses recorded in the per-theme record.

### 4. Fonts and assets

- **What:** Loads: the original's code exhibit opens with one font load, fonts.bunny.net serving Chicle and Overlock (original L197). The candidate's exhibit opens with the two base imports (section 3) and two JP font loads: Noto Sans JP (candidate L188, carrying an inline `/* 日本語フォント */` comment ahead of the @import) and Noto Serif JP (candidate L191, under a `/* 日本語フォント (JP localization) */` comment). No load anywhere in the candidate names Chicle or Overlock — the full @import list is candidate L4, L185, L186, L188, L191 — and the base delivery does not load them either (probe in the per-theme record). Stacks (block B58): the theme's font variables gain JP fallbacks — `--body-font: 'Overlock', "Noto Sans JP", monospace`, `--header-font: 'Chicle', "Noto Serif JP", cursive`, `--title-font: 'Chicle', "Noto Serif JP", cursive` (candidate L287–289) — so Chicle and Overlock stand first in their stacks with nothing loading them; in practice the headers render in Noto Serif JP and the body in Noto Sans JP. This is the per-theme record's defect flag, stated here in its section so the font account is complete in one place. Assets: the theme's one own image, the logo, is re-hosted and renamed in the move: `--logo-image` goes from `scp-wiki.wdfiles.com/local--files/theme:laughter-and-knives-theme/mzl_logo.svg` (original L297) to the draft host's `theme%3Alaughter-and-knives-theme-jp/mzl-logo.svg` (candidate L291, block B59) — same image, JP file name with a hyphen where the original's has an underscore, and the license box's entry (section 1) records both names' relationship by linking the original as its source. The deleted bobble.png background is an asset act of the opposite kind and is argued in section 8.
- **Why:** P7/T5 with KB-16 (the font load gap): the JP loads and stack appends are the supplement half of the pattern, and they are correctly present; the pattern's other half — the theme's own faces must still load — is where this candidate fails, because the original's bunny.net load was dropped at creation and no wave restored it (the same failure as the laruetheme package's, from the same wave). P5 with KB-17 (asset hosts): the theme's own image is re-hosted to the JP side; the draft-host form is class (iii) at this stage.
- **Verify:** `grep -n '@import' candidate.txt` — five lines, none naming the two families; `grep -n 'Chicle\|Overlock' candidate.txt` — the stacks and exhibit prose only.
- **Disposition:** JP loads and stacks applied; the asset re-host DISPOSITIONED (class (iii)); the Latin font load is flagged as a defect in the per-theme record.

### 5. Header and sidebar furniture

- **What:** Two items. (1) The logo: the original's logo is its own mzl_logo.svg (section 4); the candidate's `--logo-image` re-hosts it. (2) The header text: the theme's subtitle "MAN ZOO LEAGUE" is kept in English in the candidate. That is the P9 item of the localize ledger, and the render row adds a display reading for it: the subtitle renders faint and overlapping at the 375px viewport (recorded as minor in the row). Ruling 2 takes header and title language out of Sigma-10 migration scope (case-by-case translation taste), and the localize ledger dispositions the P9 item on exactly that ground; the render reading is a display note attached to the same kept string, not a separate open defect.
- **Why:** P9's kept-English subtitle is the ruling-2 boundary: the port localizes the theme's prose and exhibits, and the header furniture's language is the author's and translator's taste call, dispositioned rather than silently kept.
- **Verify:** `grep -n 'MAN ZOO' candidate.txt` — the string stands as the original set it.
- **Disposition:** DISPOSITIONED (P9, ruling 2; LOCALIZE-ROWS row 108, GOSIGN2-LEDGER line 1501's per-theme note); the render row's subtitle reading is recorded in section 11.

### 6. Text translation

- **What:** The exhibit body translates throughout: the theme-squares color and subcolor names (Moss Green → モスグリーン, Lavender Rose → ラベンダーローズ, Quartz → クォーツ; candidate L37–70's zone, block B7 and the parameter lines), the headings (テーマカラー, 使い方, 見本), the usage prose including the BHL dependency note (candidate L83, with its link in section 7), the examples (collapsible labels, the titles and headings walkthrough), and the font-sample prose, which presents Overlock as the body font and Chicle as the header and title font (candidate L178–179) — the prose half of section 4's flag, since the faces it names do not load. The translation blocks (52 of the 63: 21 anchored, 31 unanchored) are the expected mass of a full exhibit translation; the one residue block in this range (B22) is an alignment artifact pairing the original's note line with the candidate's 見本 heading, both of which are accounted above. One comment translation fires (COMMENT-TEXT 1): the exhibit's comment text follows the prose into Japanese, the expected shape.
- **Why:** P9 (text and exhibit prose into Japanese), with the ruling-2 carve-out of section 5 as its only boundary in this theme. The color names translate because they are exhibit prose, not identifiers; the variable names beside them (`--gray-monochrome` and the rest) stay byte-identical, which is what keeps the exhibit truthful about the CSS it displays.
- **Verify:** Read any exhibit range against its original (for example candidate L37–70 against original L45–80 for the color names); `grep -n 'Moss Green' candidate.txt` returns nothing.
- **Disposition:** Applied (the theme's T4 record shows no translation finding; the one finding was the P9 item of section 5, dispositioned).

### 7. Links and references

- **What:** Three link acts. (1) The credit block's source link names the original at its recorded host (scp-wiki.wikidot.com, section 1) — host check clean. (2) The BHL dependency note's link: the original's note ends with a relative link, `[[[theme:black-highlighter-theme|To learn more go here]]]` (original L95), which resolves on whatever wiki hosts the page; the candidate keeps the relative form with translated text, `[[[theme:black-highlighter-theme|詳しくはこちら]]]` (candidate L83), which on the JP side resolves to the production BHL page the candidate imports — the correct target, reached by the same mechanism the original used. (3) The usage example's code block (candidate L87–90): its base line reads `@@[[include :scp-jp:theme:black-highlighter-theme]]@@`, the production JP page, correct; its self line reads `@@[[include :scp-jp:theme:laughter-and-knives-theme-jp]]@@` — at this batch's snapshot it named the plain EN slug rather than the candidate's posting name theme:laughter-and-knives-theme-jp, and the population sweep repaired it after the verdict (per-theme record). No other external references ride in the prose.
- **Why:** P1/P9 link hygiene: credit and prose links must resolve on the JP side, which (1) and (2) do by their different mechanisms (an absolute recorded-host link and a host-relative page link). The example self-reference is exhibit text, but it is the text a user copies to install the theme, so its wrong name is a real defect of the printed instructions even though it executes nothing.
- **Verify:** `grep -n 'scp-jp:theme:laughter' candidate.txt` — one hit, the example line; `grep -n 'theme:black-highlighter-theme' candidate.txt` — the import, the note link, and the example's base line, all in their correct forms.
- **Disposition:** (1) and (2) applied; (3) applied, with its post-verdict repair recorded in the per-theme record.

### 8. Structure and exhibits

- **What:** Beyond the delivery rebuild (section 3) and the credit swap (section 1), three deletions and no restructuring. (1) The BHL logo image exhibit: the original's usage section opens with a flex div displaying the base theme's logo image from the base's EN file folder (original L92–94); the candidate's usage section opens directly with the dependency note. The image is the base theme's own asset, not this theme's, and it is decoration for the note the candidate keeps in text form. (2) The bobble.png background declaration (block B60): the original's `.bobble-bg` rule sets `background: url(http://kontainer.djkakt.us/local--files/theme:laughter-and-knives-theme/bobble.png)` (original L723) — a decorative image on a personal CDN, over plain http. The candidate's rule keeps the element, its spin animation, and the hover rule, and drops only the background declaration (candidate L715–729's zone). The porter's ground is stated in the file, in the license box's translator note: the distribution host had disappeared and the file could not be obtained. The review's own probe (2026-11-17) confirms the substance: the recorded URL answers 308 to its https form and then 404 — the file does not serve at its recorded address. The deletion is therefore a documented dead-asset act, recorded here with its evidence rather than narrated as a supplement; the alternative the standards offer (keep the line byte-unchanged) would have kept a plain-http reference to a file that does not exist, and T1 would have flagged the line itself. (3) The original's `[[footnoteblock]]` (original L907) does not survive the tail restructure; neither page contains a single footnote, so nothing the block would have rendered exists — a boilerplate loss with no visible effect, recorded for completeness. The EXHIBIT-RESTRUCTURE primaries (4) are the delivery and credit zones and the theme-squares repoint, all treated in their sections; the exhibit census is otherwise complete against the original (color exhibit, usage, examples, component samples, and the full code exhibit).
- **Why:** P8 (exhibit structure follows the original) governs the census; the three deletions are each argued on their own ground — a foreign asset's decoration, a dead asset with in-file documentation, and an empty boilerplate line — rather than by a general license to trim.
- **Verify:** `grep -n 'black-highlighter-logo' candidate.txt` returns nothing; `grep -n 'bobble' candidate.txt` — the surviving `.bobble-bg` rules and keyframes, no background declaration; `grep -n 'footnoteblock' candidate.txt` returns nothing, and `grep -c 'footnote' original.txt candidate.txt` shows the original's single hit is the block itself.
- **Disposition:** Applied and recorded; the bobble deletion carries its evidence in the file (license box) and in this section.

### 9. Formatting only

- **What:** No whitespace-only or reindent blocks fire in this package (WS-ONLY and REINDENT both absent from the label counts). The one formatting-adjacent residue is block B61: a blank line deleted at the code exhibit's tail (original L904), riding with the tail restructure of section 3. Everything else in the diff carries content.
- **Why:** Stated so the section's emptiness is a checked fact: the classifier separates formatting mass from content mass, and here there is no formatting mass to excuse.
- **Verify:** The label counts in the class summary (no WS-ONLY, no REINDENT); block B61 in classification.json.
- **Disposition:** Standing (nothing to disposition).

### 10. Porter annotations

- **What:** Two annotation forms ride in the candidate. (1) The license box's translator note (訳注, candidate L909, inside block B62, which carries the ANNOTATION label): it records the bobble.png deletion and its ground — the original had a rule loading the decorative image, the distribution source (a personal CDN) had disappeared and the file could not be obtained, so the JP version drops only that background declaration and keeps the rotation animation rules as they were. (2) The two font comments in the code exhibit: `/* 日本語フォント */` riding inline ahead of the Noto Sans JP @import (candidate L188) and `/* 日本語フォント (JP localization) */` above the Noto Serif JP import (candidate L190). No other porter prose stands in the file.
- **Why:** T11: an annotation is how a judgment call stays auditable after the fact. The bobble note is the model case — it names what was removed, why, and what was kept — and it is placed in the license box, where a reader auditing the theme's assets will look.
- **Verify:** Read candidate L899–911 (the box) and L188–191 (the font comments).
- **Disposition:** Standing (the annotations are part of the port as delivered; the deletion they document is section 8).

### 11. Dispositions and exceptions

- **What:** Four standing items, all closed. (1) T1's pseudo-ref ×2 (section 3): class (iii), sanctioned draft-host form. (2) The render row's page-side items: a runtime-hotlink in the site-theme chain (the KB-40 shape — a hotlink a checker reading only this file cannot see, found by loading the page) and a sidebar that did not open at the 768px and 375px webkit viewports; both are recorded in the row as the page's findings at review time, and neither is a line in this candidate that a later wave could edit — the hotlink rides in the chain the page loads, and the sidebar reading is an environment-layer observation the row preserves as classified. (3) The sample-side render item: the decoration sample's T2 run produced no machine verdict (exit 2), an instrument outcome recorded as such, and the T3 reading of the "MAN ZOO LEAGUE" subtitle (faint and overlapping at 375px, minor) attaches to the kept-English subtitle of section 5. (4) T4's one finding, the P9 subtitle item: DISPOSITIONED under ruling 2 (header/title language out of scope), recorded at GOSIGN2-LEDGER line 1501.
- **Why:** A disposition names its ground: class (iii) for the draft host, ruling 2 for the subtitle's language, and the render row's own classification for the page and sample readings. Nothing in this theme rests on an unnamed exception.
- **Verify:** The theme's rows in RENDER-ROWS-2 and LOCALIZE-ROWS; the disposition line in GOSIGN2-LEDGER.
- **Disposition:** DISPOSITIONED (all four, on the grounds named).

### 12. Verification record

- **What:** T1 (source check, T1-ROWS row 98): pseudo-ref ×2, no hotlink and no http errors — the candidate's own file is clean of the error classes that attach to source text, and the original's plain-http personal-CDN line (section 8) is absent from the candidate by deletion, not by oversight. T4 (localize check, LOCALIZE-ROWS row 108, wave LOCALIZE-S2-B): FINDINGS, 1 finding — the P9 item of sections 5 and 11, dispositioned under ruling 2; the row also records no unincorporated upstream updates. T2/T3 (render check, RENDER-ROWS-2, wave RENDER-S2-C (EN13)): the page and sample readings of section 11. The go-sign ledger row (§(b) row 108) aggregates T1 FINDINGS (classified), T2 FINDINGS, T3 FINDINGS, T4 FINDINGS, T5 PASS — every finding classified, none OPEN.
- **Why:** The counts are the acceptance evidence for the sections above: each checker's scope is stated so a clean result is not read past what the checker can see (T1 reads this file; the render check is what found the chain hotlink).
- **Verify:** The three ledger-part files named above, rows 98 and 108 and the theme's render row; GOSIGN2-LEDGER §(b) row 108 for the aggregate.
- **Disposition:** PASS at the ledger determination, with the items of section 11 dispositioned as recorded.

## Per-theme record

Four items belong to this theme alone.

**The Latin font load is missing (defect, flagged for the coordinator).** The original loads Chicle and Overlock from fonts.bunny.net (original L197: `@import url('https://fonts.bunny.net/css?family=Chicle|Overlock:400,900');`). The candidate loads neither family anywhere (its full @import list is candidate L4, L185, L186, L188, L191), its base delivery does not load them either (probe made for this review, 2026-11-17: the Black Highlighter stylesheet the candidate's frame serves, `https://scp-jp.github.io/Black-Highlighter/css/min/black-highlighter.min.css`, 487,467 bytes, contains zero occurrences of Chicle and zero of Overlock), and the stacks still name both faces first (`--body-font: 'Overlock', …`, `--header-font: 'Chicle', …`, `--title-font: 'Chicle', …`, candidate L287–289), as does the exhibit prose presenting them as the theme's fonts (candidate L178–179). The load was already absent at creation (d7c1af6) and no later commit restored it; a497307 removed only a duplicated Noto Sans JP import. The ledger's T4 record charged this theme only its P9 item, so the gap stands unrecorded there. This is the same defect shape as the laruetheme package's flag in this batch (a BHL-based theme whose bunny.net load the port dropped); the repair is the same one-line restoration of the load, and it belongs to the coordinator's repair wave, not to this package.

**The usage example's self-reference was repaired after the verdict.** At this batch's snapshot the example's self line (candidate L89) read `@@[[include :scp-jp:theme:laughter-and-knives-theme]]@@`, the plain EN slug where the candidate posts as theme:laughter-and-knives-theme-jp; the population sweep repaired it after the ledger determination (canonical commit b5cb724, a single -jp insertion on the line), and this package is built against the repaired candidate. The example's base line (candidate L88) was and is correct. The same repair reached the mcf, maxwell, laruetheme, lumina, and legend-of-blue packages in this batch.

**The bobble.png deletion is documented in the file, and its premise checks out.** The porter's license-box note (candidate L909) states the distribution host had disappeared; the review's probe of the recorded URL (2026-11-17) returns a 308 redirect to the https form and then a 404 — the host answers, the file does not. The deletion of the single background declaration (original L723), with the spin animation rules kept, is recorded in section 8 with this evidence.

**The head module's page-local rules did not survive the delivery rebuild (observation).** The original's head module carried four rules for the theme page itself (original L5–28): `.scp-image-block.block-right` margins, `.scp-image-block a` width, `.scp-image-block img` border and sizing, and the `.colors-container .subcolors .color:nth-of-type(9)` rainbow animation for the theme-squares exhibit's ninth square. None has a counterpart in the candidate (grep-verified). The image-block rules are plausibly covered by the base theme's own stylesheet, which the original's head frame also loaded; the rainbow rule animated only this page's own color exhibit, and its loss is a small display difference on the theme page itself, left to the coordinator's judgment alongside the laruetheme package's similar observation.

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:laughter-and-knives-theme-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FONTS7 item 2 — Latin face load restored (landing `41048ca2b13766899b5c5d5d426a980ad00f8a04`, "pages: larue and laughter font loads, two exhibit samples", 2026-11-17; record `FIX-FONTS7.md`).** +1/−0. L185 restored as the first @import of the code exhibit: `@import url('https://fonts.googleapis.com/css2?family=Chicle&family=Overlock:wght@400;900&display=swap');` — Chicle (`--header-font`/`--title-font`) and Overlock (`--body-font`) are stack-named in both files but loaded nowhere in the candidate; the css2 axis spec carries the original's `Overlock:400,900` weights (original L197, bunny.net). Probed once 200, `text/css`. Checker 2/1/3 unchanged, with no hotlink from the restored googleapis line (the file's established font source); class (i) 0.

## Change set outside the two diffed files

| File | Change |
|---|---|
| `pages/theme-decoration-sample-laughter-and-knives-theme-jp.txt` | The theme's decoration sample: a JP page applying the candidate, the surface the T2/T3 render checks measured (section 11's sample readings) |

## License and attribution

- **Title:** Laughter and Knives Theme
- **Author:** Woedenaz
- **Source:** https://scp-wiki.wikidot.com/theme:laughter-and-knives-theme — revision 58
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
