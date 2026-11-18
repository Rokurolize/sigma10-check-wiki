# Review package — theme:laruetheme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:laruetheme-jp — origin EN, population #106 [GOSIGN2-LEDGER (b) row 106]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 47fb39f8f0830d4a2b4ea21d0368c8b8735254a80947170c986b8208de0ad1e4); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 1 warn / 1 info (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 96; GOSIGN2-LEDGER (b) row 106]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2); T3 page credit modal opens, preview-notice left-clip (shared chrome). [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-C (EN13))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 106, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 106]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 106]
- Computed against: canonical commit 41048ca2b13766899b5c5d5d426a980ad00f8a04; candidate file pages/theme:laruetheme-jp.txt sha256:47fb39f8f0830d4a2b4ea21d0368c8b8735254a80947170c986b8208de0ad1e4; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 106) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×7 (sections 3 and 4); the render row's items (section 11); T4's one finding (P9) dispositioned under ruling 2. One defect is flagged in the per-theme record, not hidden: the original's Latin font load has no counterpart in the candidate |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:laruetheme | theme:laruetheme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 42 (first translation; the candidate's credit block records 初訳時参照リビジョン: 42) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-laruetheme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:laruetheme-jp.txt`, byte-identical to the canonical file in its post-sweep state (the usage sweep's repair, canonical commit b5cb724, landed after this batch's snapshot; see the per-theme record) |
| Lines / bytes | 747 lines / 22,661 bytes | 752 lines / 23,248 bytes |
| SHA-256 | 752c2aa0dbd26afd2bb925b7f7c7c7757d72ca2e8090a8e6bbc6159c2b7c48c6 | b966fa73a5b9a5e4c65b8330578ef9d1a9ccc9d81b36bf126ff8bc9d7f125ccf |

Wave history: the candidate was created by the Stage 2 EN13 integration (commit d7c1af6), then touched by 1869877 (FIX-CREDIT-D, translator-attribution normalization) and a497307 (FIX4-MECH, which removed a duplicated Noto Sans JP import from this file, KB-65). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge. This theme is a dependent theme: the original layers over the Black Highlighter base, and the candidate's delivery relationships are treated in section 3.

## Summary

A mechanical port with a rebuilt delivery frame and one real defect. The original is a Black Highlighter-based EN theme: its head module imports the base's two stylesheets from the author's GitHub, its own CSS lives in the page's code exhibit and is re-delivered by a tail module outside the tag gate, and its credit furniture is a bare Rate module. The candidate repoints the base delivery to the JP side in the population's form for BHL-based themes (the production JP BHL page at the head, the scp-jp.github.io mirror in the frame and in the exhibit), moves its own delivery into the head frame, swaps the Rate for the JP preview credit block, re-hosts its images to the draft host, translates the exhibit body (including the theme-squares color names), appends a license box, and repairs one invalid `var()` reference in the original's CSS with an in-file comment explaining the repair. Measured churn (diff.md, the generator's difflib count with autojunk off: +141/−143, 284 changed lines in 65 change blocks / 9 hunks; a GNU-diff count of the same pair gives 233 changed lines — the difference is alignment choice, not content). One defect is flagged in the per-theme record with probe evidence: the original loads its three Latin display faces (Rubik, Parisienne, Courier Prime) from fonts.bunny.net, and nothing in the candidate or in its base delivery loads them, while the stacks still name Rubik and Parisienne first.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 65 change blocks — 36 specific (55.4%), 27 heuristic (41.5%), 2 residue (3.1%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 29 |
| TRANSLATION-ANCHORED | 18 |
| DRAFT-HOST | 10 |
| EXHIBIT-RESTRUCTURE | 4 |
| INCLUDE-REPOINT | 3 |
| SELF-DELIVERY | 3 |
| IFTAGS | 2 |
| CSS-BODY | 2 |
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| ESCAPED-INCLUDE | 1 |
| HEADERVAR | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 2 CSS-BODY blocks are the font-variable stack rewrites (B56, section 4) and the `var()` repair with its porter comment (B62, sections 8 and 10); the 4 EXHIBIT-RESTRUCTURE primaries are two include repoints (sections 2 and 3), the credit zone (section 1), and the tail delivery's deletion (section 3, a genuine delivery restructure); the 2 residue blocks are a heading translation (B23, section 6) and a blank-line deletion at the code exhibit's tail (B63, section 9); the large TRANS-UNANCHORED mass is the exhibit body's translation, resolved in section 6 by shape with the one deliberate deletion (the template-custody warning) argued in section 8. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:laruetheme-jp; original theme:laruetheme on scp-wiki at reference revision 42; candidate `pages/theme:laruetheme-jp.txt`. Provenance route: derived from the original at the reference revision by the Stage 2 EN13 wave (sources.tsv kind: standard; no production JP counterpart of the theme itself is recorded, so the R4 adoption question does not arise — the production page in this port's life is its base, section 3). The original opens with its tag gate ahead of its head module (original L1–2); the candidate inverts that order, placing the base include and the delivery frame ahead of the localized gate (candidate L1–19), the wave-standard frame form.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate is P2, the frame is P4/P6 (section 3).
- **Verify:** The sources.tsv row for laruetheme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` inside a right-aligned div (original L22–24, inside block B5), and nothing else: no info pair, no license box; the attribution lives in the usage prose ("developed by [[*user MalyceGraves]]", original L88's zone) and in the prose statement that the theme is licensed under CC BY-SA 3.0. The candidate deletes the Rate and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L21–31) carrying the eight ruling-3 fields (title ラ・リュ・マカブル テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 La Rue Macabre Theme; 著作権者 [[*user MalyceGraves]]; 作成年 2020; 初訳時参照リビジョン 42; the source link, section 7). The field's author matches the original's prose attribution — no name is dropped. The translator field took its ruling-3 form in 1869877. The candidate also appends a license box before the gate closes (candidate L733–751, block B64): a `:scp-jp:component:license-box-backend`/`license-box-end` pair with entries for the theme's five image files (sigil.png / sigil2.png; elegantdivider.png / tilewood.jpg / wood.png — author MalyceGraves, license CC BY-SA 3.0 with the deed.ja link, source the EN wiki's file list) and one font entry (Courier Prime / Parisienne / Rubik, SIL Open Font License via Google Fonts, with a note that Noto Sans JP / Noto Serif JP accompany them for Japanese text). The box's license matches the original's own prose statement; the original carries no box, so the box is an added attribution record (T12), and its font entry is part of the per-theme record's flag: it describes the three faces as distributed via Google Fonts, but no load of them exists in the candidate (section 4).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become). Ruling 3 fixes the eight fields and the translator credit form; the license box is the campaign's TASL record-keeping applied to a theme whose assets arrived with only a prose license statement.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L21–31 against the eight fields, and candidate L733–751 for the license box.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); the license box is a standing supplement, with its font entry flagged in the per-theme record.

### 2. Includes and components

- **What:** The include repoints: the two interwiki-style includes of the original's frame (:scp-wiki: → :scp-jp:, blocks B3/B4; their theme= parameters are section 3); the theme-squares exhibit's include, `:scp-wiki:component:theme-squares` → `:scp-jp:component:theme-squares` (block B7, original L47 → candidate L38; its color-name parameters are section 6); and the credit and license-box includes (section 1). The head's base include, `[[include :scp-jp:theme:black-highlighter-theme]]` (candidate L1), is a delivery line and is treated in section 3. The usage example's two includes are exhibit text and are treated in section 7.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; all repointed targets have verified JP counterparts, so all are repointed and none is kept as an exception. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include names a `:scp-jp:` target.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** This theme's delivery is rebuilt, and the rebuild is the port's largest structural act. The original delivers in three places: a head `[[module css]]` importing Black Highlighter's normalize and base stylesheets from nu-scptheme.github.io (`/stable/styles/` paths, original L3–4) plus two image-block rules for the theme page itself; two interwiki-style includes at priorities 1 and 2 naming the same base files at their `/css/min/` paths on the same GitHub host (original L17–27); and, outside the tag gate at the page's tail, a `[[module css]]` importing its own `local--code/theme%3Alaruetheme/1` from scp-wiki.wdfiles.com with a third interwiki-style include at priority 3 naming the same (original L739–747, block B65) — the tail pair is what serves the page's own code exhibit as the theme's CSS. The candidate delivers in one place: `[[include :scp-jp:theme:black-highlighter-theme]]` (candidate L1) pulls the production JP Black Highlighter page, the form every BHL-based candidate in this population uses (theme:doap-bhl-jp, theme:fmd-bhl-theme-jp, and theme:minimalist-bhl-jp open with the identical line, read for this package); a head `[[module CSS]]` imports the candidate's own `local--code/theme%3Alaruetheme-jp/1` from the draft host (candidate L3–5); and three interwiki-style includes at priorities 1, 2, and 3 name the base's normalize and base files on the JP mirror host scp-jp.github.io (`/css/min/` paths) and the candidate's own /1 on the draft host (candidate L7–17). The tail module is deleted, and the tag gate now wraps the whole page, license box included. The code exhibit itself opens with the two base imports from scp-jp.github.io (candidate L183–184), so the served /1 is self-contained where the original's exhibit relied on the page's head frame for the base. One loss rides with the rebuild, recorded here rather than hidden: the original head module's two image-block rules styled the theme page's own exhibits; the `img` rule survives inside both exhibits (original L481, candidate L476), but the `.scp-image-block.block-right` margin rule (original L6–8) has no counterpart in the candidate (the base's own stylesheet carries image-block styling, and the rule was the original's page-local patch; see the per-theme record). The draft-host lines in this frame are part of T1's seven pseudo-ref errors.
- **Why:** Ruling 1: a dependent theme imports its base theme's JP delivery rather than the raw upstream branch delivery — for BHL-based themes the population's JP delivery is the production BHL page plus its JP mirror host, which is what the bytes show. P4/T9 (delivery served from JP hosts) and P6/T3 (the interwiki-style frame, here with the base at priorities 1–2 and the theme's own layer at priority 3, preserving the original's cascade order). The draft-host form of the own-code lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** Read candidate L1–19 against original L1–27 and L739–747; `grep -n 'local--code' candidate.txt` returns the head import and the priority-3 parameter, both draft-host.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)); the frame rebuild itself is the applied port, with the one rule loss recorded in the per-theme record.

### 4. Fonts and assets

- **What:** Loads: the original's code exhibit opens with one font load, fonts.bunny.net serving Courier Prime, Parisienne, and Rubik (original L194). The candidate's exhibit opens with the two base imports (section 3) and two JP font loads: Noto Sans JP (candidate L186, carrying an inline `/* 日本語フォント */` comment ahead of the @import on the same line) and Noto Serif JP (candidate L189, under a `/* 日本語フォント (JP localization) */` comment). No load anywhere in the candidate names Courier Prime, Parisienne, or Rubik — the full @import list is candidate L4, L183, L184, L186, L189 — and the base delivery does not load them either (probe in the per-theme record). Stacks (block B56): the theme's font variables gain JP fallbacks — `--body-font: 'Rubik', "Noto Sans JP", sans-serif`, `--header-font: 'Parisienne', "Noto Serif JP", cursive`, `--title-font: 'Rubik', "Noto Sans JP", sans-serif`, `--mono-font: pennsylvania, "Noto Sans JP", monospace` (candidate L203–206) — so Rubik and Parisienne stand first in their stacks with nothing loading them; in practice the header renders in Noto Serif JP and the body in Noto Sans JP. This is the per-theme record's defect flag, stated here in its section so the font account is complete in one place. Assets: the theme's images are re-hosted to the draft host's own folder — the two sigil images' `link=` targets (blocks B14, B16: candidate L63, L70), the `--logo-image` variable (block B55, candidate L201), and five texture/background URLs inside the CSS (blocks B57–B61: original L279, L296, L326, L383, L403), all under `sigma10-jp-test.wdfiles.com/local--files/theme%3Alaruetheme-jp/`. These draft-host lines complete T1's seven pseudo-ref errors.
- **Why:** P7/T5 with KB-16 (the font load gap): the JP loads and stack appends are the supplement half of the pattern, and they are correctly present; the pattern's other half — the theme's own faces must still load — is where this candidate fails, because the original's bunny.net load was dropped at creation (the creation-era candidate already lacks it) and no wave restored it. P5 with KB-17 (asset hosts): the theme's own images are re-hosted to the JP side; the draft-host form is class (iii) at this stage.
- **Verify:** `grep -n '@import' candidate.txt` — five lines, none naming the three families; `grep -n 'Rubik\|Parisienne' candidate.txt` — the stacks and exhibit prose only.
- **Disposition:** JP loads and stacks applied; asset re-hosts DISPOSITIONED (class (iii)); the Latin font load is flagged as a defect in the per-theme record.

### 5. Header, sidebar, and site furniture

- **What:** The theme's header variables are carried in their original language: `--header-title: "La Rue Macabre"` and `--header-subtitle: "Sit a spell & share your story"` (candidate L201–202's zone, block B55's span), with `--theme-name` likewise unchanged. The one variable that changes is `--logo-image`, re-hosted to the draft host (section 4). No other furniture change: the sidebar and top-bar rules are the base's and the theme's own, carried apart from the font variables of section 4.
- **Why:** The kept English header strings are T4's one finding for this theme (P9, display-affecting), and the ledger dispositions it under ruling 2: header and title language is translation taste, out of scope for migration correctness. This package records the disposition and does not re-argue it.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — both values in English, as the original's.
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P9 DISPOSITIONED, ruling 2).

### 6. Text translation

- **What:** The exhibit body is translated throughout. The counted groups: the theme-squares exhibit's ten color names (block B7's span: Tombstone → トゥームストーン, Parchment → パーチメント, Wild Sand → ワイルドサンド, Alto → アルト, Shadow on Pine → シャドウ・オン・パイン, Dull Gold → ダルゴールド, Lisbon Brown → リスボンブラウン, and the remaining subcolors in the same form); the usage prose (block B20's span and its neighbors: the development credit, the CC BY-SA statement, the Black Highlighter note, the Old Money variant note); the font-sample prose (candidate L174–176: 本文フォントはRubikです / タイトルフォントはParisienneです / 等幅フォントはCourier Primeです — the samples name the faces the stacks name, which is what makes section 4's flag reader-visible); the sigil captions (ラ・リュのシジル - 黒 / 白）; the section headings (テーマカラー, 使い方, 見本 — residue block B23 is the last of these); and the collapsible's labels (+ テーマのコードを表示 / - テーマのコードを閉じる). The single COMMENT-TEXT block is inside the font zone. Two body changes are not translations and are argued in section 8: the template-custody warning div is deleted outright, and a closing `[[/div]]` is added at the sigil exhibit. English survives in the candidate in the header variables (section 5, dispositioned), the credit block's title fields (quotations of the work's name), and the license box's file names.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored mass is where a silent deletion would hide; the one deletion in it is named and argued in section 8 rather than waved through.
- **Verify:** The pairs are diff.md's hunks in order; read candidate L33–100 against original L29–110.
- **Disposition:** Standing (the port itself); the deletion is recorded in section 8.

### 7. Links

- **What:** The credit block's source link (candidate L30) names `https://scp-wiki.wikidot.com/theme:laruetheme`, the original's recorded host in sources.tsv, and serves the original — no probe discrepancy, no defect. The usage prose's Black Highlighter note link is repointed from the original's `http://www.scp-wiki.net/theme:black-highlighter-theme` to `https://scp-jp.wikidot.com/theme:black-highlighter-theme` (candidate L83's zone), the production JP base page, matching the head include's target. The Old Money note's link is repaired in form: the original's `[[[component: Old Money theme]` is not a resolvable link at all, and the candidate links the EN component page by URL with the label "Old Moneyテーマ（英語版）" (candidate L85's zone, block B20) — the component has no JP port, so the serving original is the correct target under the dead-reference standard. The larue-hub link keeps the original's relative form (`[[[larue-hub|ラ・リュ・マカブル]]]`, candidate L79), resolving on the hosting wiki as it did on the original's. The usage example's two includes are exhibit text: the base line names `:scp-jp:theme:black-highlighter-theme` (the production page, correct as written) and the self line names `:scp-jp:theme:laruetheme-jp` (candidate L92) — its plain-slug form at this batch's snapshot was repaired after the verdict by the population sweep (per-theme record).
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; all three prose links satisfy it. An exhibit that documents the theme's own include must name the page a user would actually paste — that is the flag's ground.
- **Verify:** `grep -n 'wikidot.com\|scp-wiki.net' candidate.txt` — the source link, the BHL note link, and the Old Money URL are the only hits.
- **Disposition:** Prose links standing; the exhibit self-reference is recorded in the per-theme record (repaired after the verdict).

### 8. Structure

- **What:** Three structural acts, each argued. (1) The delivery rebuild of section 3: the original's three delivery sites (head module, two frame includes, tail module outside the gate) become one head frame, and the tag gate now wraps the whole page. The classifier's EXHIBIT-RESTRUCTURE primaries B3 and B7 are include repoints inside it; B65 is the tail deletion itself. (2) The template-custody warning is deleted (block B6, original L31–39): the gold div reading "PLEASE STOP — This is a template page used internally by the SCP Wiki. PLEASE DO NOT TOUCH THIS PAGE WITHOUT PERMISSION" addresses the EN wiki's editors about the original page's custody. It is not theme content, it makes a false claim about the candidate page, and the candidate drops the whole div rather than translating it; the theme-colors heading that followed it is kept and translated. This is the one deliberate body deletion in the port, recorded here so it is a decision on the record, not a silent loss. (3) Two repairs inside the inherited material: the sigil exhibit gains the closing `[[/div]]` its outer wrapper div required and the original left unclosed (block B18, candidate L75); and inside the CSS, `color: rgb(var(-black-monochrome))` becomes `rgb(var(--black-monochrome))` (block B62, candidate L547) — the original's single-dash variable name makes the declaration invalid, and the port corrects it in place with a comment saying so (the comment is section 10). An exhibit census otherwise confirms the shape: the theme-squares exhibit, both sigil exhibits, the usage and examples sections, the font samples, and the code exhibit are present on both sides in the same order.
- **Why:** R3 exists to force exactly these adjudications, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here each act is named with its ground. The `[[/div]]` and `var()` repairs are R6 in-place corrections of the original's own syntax.
- **Verify:** Compare `grep -n '\[\[div\|\[\[/div\]' original.txt candidate.txt` around the sigil exhibit; read candidate L547 against original L552; the warning div's absence is `grep -n 'PLEASE STOP' candidate.txt` returning nothing.
- **Disposition:** Standing; no unrecorded structural deletion, no class I item.

### 9. Formatting only

- **What:** Almost none. The classifier finds no WS-ONLY block in this pair (the original's code exhibit is tab-indented and carries no trailing-space blank-line mass), and no re-indentation (0 blocks). The one residue formatting item is block B63: a single blank line deleted at the code exhibit's tail (original L735). The head's blank-line tightening rides inside the frame blocks of section 3.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change; here the class is a single blank line and the section says so with its ground.
- **Verify:** classification.json's summary for this package: WS-ONLY absent, reindent_blocks 0; block B63 in the appendix listing.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three annotations, all inside the code exhibit. (1) Candidate L547, riding inside block B62: the English comment `/* JP port: the original wrote this variable name with a single dash, which made the declaration invalid; corrected here */`, placed between the repaired declaration's value and its semicolon — the only in-file explanation of the `var()` repair, and load-bearing for any future porter who diffs against the original. (2) Candidate L186: `/* 日本語フォント */`, inline ahead of the Noto Sans JP import. (3) Candidate L188: `/* 日本語フォント (JP localization) */`, ahead of the Noto Serif JP import. There is no provenance comment at the head of the code block of the kind some sibling candidates carry.
- **Why:** R2: porter-added text is part of the change record, and annotation (1) is the record of a deliberate deviation from the original's bytes — without it, the corrected line reads as a porting error.
- **Verify:** Read candidate L186, L188, and L547.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's seven pseudo-ref errors: the candidate's own draft-host lines (the head import and priority-3 parameter of section 3, the asset lines of section 4); class (iii), sanctioned at draft stage, with the posting rewrite class (ii) mechanics. There is no hotlink error and no class (i) error. (2) The render row's items: the page's runtime-hotlink site-theme chain (KB-40, environment layer); the sample's T2 line, which records no machine verdict (the checker exited 2) — a gap in the measurement, recorded as such, not a pass and not charged to the candidate; and the T3 page reading, credit modal opens with the preview notice left-clipped, which the row itself attributes to shared chrome (the JP site's own frame, not this theme). (3) T4's one finding (P9, the header variables of section 5), DISPOSITIONED under ruling 2 in the ledger's §(c3) line for this theme. The per-theme record's font item is not among these dispositions: no ledger ground covers it, and this package does not invent one.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3); the per-theme record's font item flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 96): exit 1, 7 errors / 1 warn / 1 info; all seven errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN13)): FINDINGS, the items of section 11(2), with the sample's T2 carrying no machine verdict as recorded there. (c) T4/T5 (LOCALIZE-ROWS row 106): FINDINGS jointly, display-affecting findings 1 — the P9 header item, dispositioned under ruling 2 — and the row records no unincorporated upstream updates. The font-load gap of section 4 is not in any of the three records; it is this package's own finding, from reading the two files and probing the base delivery. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +141/−143 in 65 change blocks / 9 hunks; the GNU-diff count of the same pair is 233 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:laruetheme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 106; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The Latin font load is missing (defect flag)

The original loads its three Latin faces in one line: `@import url('https://fonts.bunny.net/css?family=Courier+Prime|Parisienne|Rubik&display=swap')` (original L194, at the head of its code exhibit). The candidate loads none of them. Its complete @import list is candidate L4 (its own delivery), L183–184 (the base's two files), and L186/L189 (Noto Sans JP, Noto Serif JP). The base delivery does not load them either: probed for this package (2026-11-17), the base stylesheet the candidate actually pulls, `https://scp-jp.github.io/Black-Highlighter/css/min/black-highlighter.min.css` (487,467 bytes), imports Recursive, Inter, and M PLUS 1p from Google Fonts, and contains zero occurrences of Rubik, Parisienne, or Courier. Meanwhile the candidate's stacks name the faces first (`--body-font: 'Rubik', ...`, `--header-font: 'Parisienne', ...`, `--title-font: 'Rubik', ...`, candidate L203–206), its exhibit prose presents them as the theme's fonts (candidate L174–176), and its license box describes them as "SIL Open Font License（Google Fonts から配信）" — distributed via Google Fonts — although no such load exists in the file. The practical effect: the header renders in the Noto Serif JP fallback instead of Parisienne, and the body in Noto Sans JP instead of Rubik. The load was already absent in the creation-era candidate (commit d7c1af6), so no FIX wave removed it; the FIX4-MECH touch on this file (a497307) removed only a duplicated Noto Sans JP import. T4's row for this theme records one display-affecting finding (the P9 header item) and does not charge the font load. This package flags the gap with its evidence and does not edit the candidate; the natural repair is to restore a load for the three families in the exhibit head, in the Google Fonts form the license box already describes. The ledger's determination for this theme is PASS and this package does not re-open it; the flag is the documentation doing its job, because a reviewer comparing the rendered header against the original's Parisienne face will find a different font.

### The usage example's self-reference (repaired after the verdict)

At this batch's snapshot the candidate's usage example (candidate L92) read `@@[[include :scp-jp:theme:laruetheme]]@@`: the wiki prefix had been repointed from the original's `:scp-wiki:` form, but the page name kept the original's plain slug, where this candidate's posting name is theme:laruetheme-jp. The population sweep that the earlier batches' flags of this same shape set in motion repaired the line after the ledger determination (canonical commit b5cb724, a single -jp insertion on the line); this package is built against the repaired candidate, whose L92 now reads `:scp-jp:theme:laruetheme-jp`. The example's other line, naming the base, was and is correct as written: `:scp-jp:theme:black-highlighter-theme` is the production JP base page, the same target the candidate's own head include uses.

### The head module's image-block margin rule (observation)

The original's head module carried two rules for the theme page's own exhibits (original L6–13). The `.scp-image-block img` rule survives in both code exhibits (original L481, candidate L476). The `.scp-image-block.block-right { margin: 1em 0 1em 2em; }` rule (original L6–8) has no counterpart anywhere in the candidate. The base's stylesheet carries its own image-block styling, and the dropped rule was the original's page-local patch to it, so the practical exposure is the theme page's own right-floated image exhibits sitting without that margin. This package records the difference with its lines and leaves the judgment to the coordinator, rather than asserting a defect in a rule whose absence the render record does not charge.

### The original's invalid var() reference (for report-back to the EN author)

Original L552 reads `color: rgb(var(-black-monochrome));` — a custom property name with a single dash, which makes the declaration invalid and drops it. The port repairs it to `var(--black-monochrome)` and comments the repair in the file (candidate L547, section 10). The defect is the original's, and it belongs on the report-back list for the EN author alongside the derivative record, in the same form as the derby batch's malformed `var()` findings.

### Post-package repairs (REFRESH3-H)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:laruetheme-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-FONTS7 item 1 — Latin face load restored; Courier Prime non-restore (landing `41048ca2b13766899b5c5d5d426a980ad00f8a04`, "pages: larue and laughter font loads, two exhibit samples", 2026-11-17; record `FIX-FONTS7.md`).** +1/−0. The Latin load is restored as the first @import of the code exhibit at L183: `@import url('https://fonts.googleapis.com/css2?family=Parisienne&family=Rubik&display=swap');` — the two faces its stacks name (`--body-font`/`--title-font` 'Rubik', `--header-font` 'Parisienne'), which the original loaded (original L194, bunny.net) but the candidate loaded nowhere. Google Fonts css2 is used instead of the original's bunny.net verbatim form because the candidate's own license box (L746–747) declares Google Fonts as the distribution source for these faces; probed once 200, `text/css`. **Courier Prime non-restore adjudication (recorded, not a defect):** Courier Prime was in the original's load bundle but is named by no stack in either file (only exhibit prose L176 and the license-box font entry L746; `--mono-font` names pennsylvania in both), so its load is deliberately not restored; adding `family=Courier+Prime` to the same line would be a one-token change if byte-parity of the load bundle were preferred. Checker 7/1/1 unchanged; class (i) 0.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-laruetheme-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)); it belongs to this theme's record but carries no port change of its own to explain here. The base theme's own package (theme:black-highlighter-theme-jp) is a separate record in this campaign; this package covers only the dependent theme's own layer and its delivery relationship to that base. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** La Rue Macabre Theme
- **Author:** MalyceGraves
- **Source:** https://scp-wiki.wikidot.com/theme:laruetheme — revision 42
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
