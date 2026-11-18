# Review package — theme:normal-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:normal-jp — origin CN, population #208 [GOSIGN2-LEDGER (b) row 208]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 208]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 37 errors / 1 warn / 0 infos (hotlink×35, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 223; GOSIGN2-LEDGER (b) row 208]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink incl. candidate-own ah-sandbox.wdfiles.com, fontsapi.zeoseven.com, hormress.github.io (judgment-required); sample credit-modal (preview-form), runtime-hotlink incl. the same candidate-own hosts + sample font host; no page-overflow on either page; T3 clean on both pages (PC sidebar collapsed with the theme's own hamburger visible top-left; machine contrast warn is a false positive, dark text on light blue readable; em overflow and hl-code overflow are intentional specimens); sample webkit 375/320 *-full.png missing (32767px cap). [RENDER-ROWS-RERUN16 (CN10) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN10)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 207, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 207]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 208]
- Computed against: canonical commit 379eb44032d541453098c3177e0b1e3fc62c5964; candidate file pages/theme:normal-jp.txt sha256:e41ddbf88a5b43f46fe16ee8a8f4c2731e9ce5fabfb564a167b7ee1ed9fe7dc3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 208). Its render verdict rests on the RERUN16 re-run, which supersedes the original ROWS-2 row under rule S1 |
| Standing items | **DISPOSITIONED** — the GitHub-Pages delivery dependence (P4, "delivery class (ii): original-state CDN delivery", GOSIGN2-LEDGER §(c3)); T1's 35 hotlinks (class (ii) / KB-58 family) and 2 pseudo-refs (the draft-host base import, class (iii)); the RERUN16 render items, several of them judged in the row itself (the contrast warn a false positive, the em and hl-code overflows intentional specimens, the missing webkit full-page capture a 32767px tooling cap; section 11). **NOTED, not flagged** — the mono stack's JP fallback face is named but not loaded in this file (per-theme record, item 1), and the credit fields rest partly on a fragment outside the frozen source (item 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:normal | theme:normal-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 1 (first translation; the candidate's credit block records 初訳時参照リビジョン: 1) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-normal.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:normal-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 1,136 lines / 37,835 bytes | 1,162 lines / 41,886 bytes |
| SHA-256 | cd0b7a05842703b83217a326c71125e2c0409323257495e7f1f5e49ed117682e | e41ddbf88a5b43f46fe16ee8a8f4c2731e9ce5fabfb564a167b7ee1ed9fe7dc3 |

Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave, in the layered form sources.tsv records as kind K5b-3: the candidate layers over theme:parallel-jp, the JP port candidate of the author's Parallel base framework, and this package's diff covers the theme's own layer (the base framework's CSS is imported, not carried, on both sides). The EN/CN original has been superseded upstream since revision 1; sources.tsv records a follow-up diff artifact (`diff-normal-from1.txt`, class K5a-i) in the campaign record for that drift, which is outside this package's scope. Wave history: a89eccf (CN10 integration), f1138e4 (FIX-P4, the pattern-4 repoint of base-theme CSS imports to JP port candidates — this file's base import is that wave's work), and 379eb44 (FIX4-MOPUP, the KB-65 duplicate-import cleanup; the verdict stamp's computed-against commit). No FIX5 commit touches this file.

## Summary

Dr Hormress's "Normal Projection" theme, a large all-module design (there is no code exhibit on either side: a 362-line main `[[module CSS]]`, a long documentation body, and a tail of preset modules) built on his Parallel framework. The port's decisive move is at the base layer: where the original's main module imports the framework's normalize and parallel CSS from the author's personal GitHub Pages, the candidate's new head module imports the base's JP port candidate (theme:parallel-jp) from the draft host instead, keeping only the branch add-on CSS on GitHub Pages. The rest of the GitHub Pages dependence (the branch main/elements CSS and the seven color presets) is T4's charged P4 item, dispositioned as original-state CDN delivery. The sidebar styleFrame embeds (one per preset, iframes to the CN interwiki host) are converted to the JP interwiki-style component form rather than deleted. The credit furniture (a lowercase rate module and a CN credit pair whose body is the author's shared fragment) is swapped for the JP preview block. The documentation body, some 600 lines of element specimens, is translated in place. Measured churn (diff.md: +236/−210, 446 changed lines in 148 change blocks / 20 diff sections) is mostly that translation.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 148 change blocks — 59 specific (40%), 79 heuristic (53%), 10 residue (7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 82 |
| TRANSLATION-ANCHORED | 51 |
| GLYPH-FORM | 4 |
| EXHIBIT-RESTRUCTURE | 4 |
| INCLUDE-REPOINT | 3 |
| IFTAGS | 2 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 1 |
| JPFONT-LOAD | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| TASL-FIELDS | 1 |
| CSS-BODY | 1 |

Adjudication for this README (every specific block was read against the bytes; the heuristic mass was resolved by shape): the 133 translation-family blocks are the documentation body's translation (section 6), counted per line-pair; GLYPH-FORM (4) is the R5 conversion inside retained strings. The four EXHIBIT-RESTRUCTURE primaries are adjudicated individually: B36 is the image-block demo include losing its `:scp-wiki-cn:` prefix for the bare local form (section 2); B142 is the sidebar frame include's repoint (section 5); B132 and B135 are translated specimen lines in the body, the label's standing false-fire. B3's span (one original line against twenty candidate lines at the gate) is the gate zone's reassembly — the candidate's head module and frame order of section 0 — not an insertion into the body. The ten residue blocks collapse into the appendix table below, per the class M convention; every one is resolved there, most of them the styleFrame conversions the signature table has no label for.

### Residue appendix (10 blocks)

| Block | Original → Candidate | Resolution |
|---|---|---|
| B4 | orig L366 (blank) → cand L384–385 | A blank line added at the credit zone's head; formatting only (section 9) |
| B7 | orig L386–387 → cand L406 | The usage examples: the original's two annotated example lines (include theme:parallel, then theme:normal, the site prefix struck through in red spans) collapse to the single `@@[[include theme:normal-jp]]@@`, because the candidate internalizes the base import (section 2) |
| B21 | orig L447–449 → cand L461–462 | The parameterized example in its code div: the same collapse, keeping the variant parameter (`@@[[include theme:normal-jp \|indust=-]]@@`) |
| B140 | orig L994 (blank) → — | A blank line removed at the tail modules' head; formatting only (section 9) |
| B143 | orig L1058–1060 → cand L1078–1081 | The silver preset's styleFrame `[[embed]]` iframe (//interwiki.scpwikicn.com) converted to a `:scp-jp:component:interwiki-style` include at priority=4 naming the same preset CSS (section 5) |
| B144 | orig L1067–1069 → cand L1088–1091 | The deep preset's embed, converted the same way |
| B145 | orig L1076–1078 → cand L1098–1101 | The carbon preset's embed, converted the same way |
| B146 | orig L1085–1087 → cand L1108–1111 | The indust preset's embed, converted the same way |
| B147 | orig L1094–1096 → cand L1118–1121 | The night preset's embed, converted the same way |
| B148 | orig L1103–1105 → cand L1128–1131 | The cometic preset's embed, converted the same way |

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:normal-jp; original theme:normal on scp-wiki-cn at reference revision 1; candidate `pages/theme:normal-jp.txt`. Provenance route: derived at the reference revision by the LOCALIZE-S2-E wave, layered over theme:parallel-jp (kind K5b-3; the Provenance note above). The frame order is normalized: the original opens with its gate (original L1) and puts its main module inside it; the candidate opens with its new head module (candidate L1–23), then the localized gate (candidate L25) wrapping the main module and body — the population's standard order, in which the delivery layer stands ahead of the gate.
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2.
- **Verify:** The sources.tsv row for normal-jp (kind K5b-3 and its layering note); `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture stands in the body zone after the main module: a lowercase `[[module rate]]` in a centering block (original L369–371) and the CN credit pair `:scp-wiki-cn:credit:start`/`end` (original L373–377) whose body is not text but the author's shared fragment, `[[include :scp-wiki-cn:fragment:hormress]]` set in a centered block. The candidate deletes the rate module and the pair-with-fragment and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L387–396) carrying the eight ruling-3 fields (title 法線射影テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 法向投影 版式, the original's simplified-Chinese title kept as the original-title field; 著作権者 Dr Hormress; 作成年 2026; 初訳時参照リビジョン 1; the source link, candidate L395, on scp-wiki-cn.wikidot.com, the host sources.tsv records for the original). Author check: Dr Hormress is the theme's author (the framework is his, the fragment is his, and the documentation is written in his voice); no other creator is named in the frozen source, so no dropped-creator flag arises. One provenance caveat, recorded as per-theme item 2: the original's filled credit text lives in the fragment, which is not part of the frozen source, so the field values (notably 作成年 2026) rest on the wave's record rather than on bytes this package can check. No license box exists on either side. T7 credit-module CSS: neither file carries a credit-rule group (no `creditButton` selector on either side), so no T7 item arises.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the rate module and the branch credit pair are deleted rather than duplicated (a kept rate module would be the KB-09 duplicate; a kept branch credit module does not render in the JP environment, and its fragment body has no JP counterpart to repoint to). Ruling 3 fixes the eight fields and the translator credit form.
- **Verify:** `grep -n 'module rate\|credit:start\|fragment' candidate.txt` returns only the preview pair at L387 and L396; read candidate L387–396 against the eight fields.
- **Disposition:** Applied; no credit item is charged in the theme's T4 row.

### 2. Includes and components

- **What:** The candidate's live includes are the credit pair (section 1) and the interwiki-style frames (one sidebar frame at priority=3 and six preset frames at priority=4, section 5) — there is no head frame at priority=1, because this theme's delivery is its head module (section 3), and the frames exist for the sidebar layer. The documentation's component demo changes form: the original's `[[include :scp-wiki-cn:component:image-block |name=https://hormress.github.io/SCP/image/logo/main/black.svg …]]` (original L511–512) becomes the bare `[[include component:image-block …]]` (candidate L522–523), resolving to the local wiki's component on scp-jp, its image URL unchanged (section 4's family). The usage examples change with the delivery (residue B7 and B21): the original documents a two-include contract (the base theme:parallel first, then theme:normal, with the `:scp-wiki-cn:` prefix shown struck through as the part to replace); the candidate documents the single `@@[[include theme:normal-jp]]@@`, because its head module imports the base itself, and the parameterized variant example keeps its parameter form (`|indust=-`). The original's CN credit pair and fragment are deleted in the section 1 swap.
- **Why:** P1/T2: components resolve to their JP counterparts (the bare form resolves locally, where the JP component:image-block lives); a self-reference names the page that will exist, and the usage contract is rewritten to match the delivery the candidate actually has, which is the honest form of the example.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the credit pair, the seven interwiki-style frames, and the bare image-block demo at L522.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** This theme has no code exhibit on either side; delivery is entirely `[[module CSS]]` imports, in three layers. (a) The base framework: the original's main module opens by importing the framework from the author's GitHub Pages (original L4–5: `hormress.github.io/Parallel/normalize-min.css` and `parallel-min.css`), plus Google Sans (original L6) and the branch add-on (original L7: `…/branch/normal_projection/widget_layout_plus.css`). The candidate's new head module (candidate L1–23) replaces the two framework imports with a single import of the base's JP port candidate from the draft host (candidate L4: `local--code/theme%3Aparallel-jp/1` — the FIX-P4 wave's repoint, and the campaign's cross-theme rule that a dependent theme imports the base's JP candidate delivery, never the raw upstream delivery), keeps Google Sans and the branch add-on (candidate L5–6), adds the JP font loads ahead of them (candidate L2–3, section 4), and adds an annotated supplement block (candidate L8–22, sections 5 and 10). The main module itself follows inside the gate (candidate L26–382), its rules carried from the original's (original L3–364) with the import head removed. (b) The branch layer: a tail module imports the branch's main.css and elements.css from GitHub Pages (original L998–999 → candidate L1009–1010), kept, with the candidate's annotated :root additions after them (candidate L1012–1019, sections 4, 5, and 10). (c) The presets: seven color presets ship as modules whose imports are commented behind the include-parameter trick (`/* {$silver}/ …`, original L1008–1135), each followed by its sidebar frame (section 5); the candidate keeps the preset imports on GitHub Pages in the same commented form. T4's finding covers layers (b) and (c) and the kept add-on in (a): "P4 MISSED (the entire theme depends on the original author's personal GitHub Pages for its base CSS and all 7 color presets; JP readers would render with hormress.github.io …)" (LOCALIZE-ROWS row 207) — written before, or without crediting, the base-framework repoint in layer (a); the bytes show the framework itself no longer comes from GitHub Pages, and the ledger dispositions the P4 item as "delivery class (ii): original-state CDN delivery" (§(c3)) for the dependence that remains.
- **Why:** P4/T9 govern own-code and base delivery; the base repoint is the FIX-P4 pattern and the cross-theme dependency rule. The kept GitHub Pages imports are not narrated as a normal supplement: they are the charged P4 item, and their standing is the ledger's disposition, quoted above with its ground.
- **Verify:** `grep -n '@import' candidate.txt` — the head module's five lines (L2–6), the branch pair (L1009–1010), and the commented preset lines; no `normalize-min.css` or `parallel-min.css` reference remains.
- **Disposition:** DISPOSITIONED (the P4 remainder, delivery class (ii), GOSIGN2-LEDGER §(c3)); the base import and font loads are class (iii) mechanics.

### 4. Fonts and assets

- **What:** Loads added: the head module loads Noto Sans JP and Noto Serif JP from Google Fonts (candidate L2–3), ahead of the base import. The theme's own faces (Red Hat Display, Red Hat Text, JetBrains Mono, Google Sans) are loaded by the imported chain on both sides (the RERUN16 row records the chain's font host, fontsapi.zeoseven.com, among the candidate's runtime hosts); Google Sans is the one font load written in this file, kept (candidate L5). Stacks: the branch module's annotated :root block (candidate L1013–1019) sets the JP forms — `--header-font: "Red Hat Display", "Noto Sans JP", sans-serif`, `--title-font` and `--UI-font` with "Red Hat Text", and `--mono-font: "JetBrains Mono", "Noto Sans Mono", "Noto Sans JP", monospace` — and the documentation's font specimens are updated to match (original L983–986 → candidate L995–998: 思源黑体 becomes "Noto Sans JP（源ノ角ゴシック）", and the mono specimen's 獅尾圓體SC becomes "Noto Sans Mono"). One gap is noted, not flagged (per-theme record, item 1): "Noto Sans Mono" is named in the mono stack and the specimen but loaded by no @import in this file. Assets: the theme is image-heavy and keeps its images on their original hosts — the author's GitHub Pages file tree (the logo SVGs and specimen images), ah-sandbox.wdfiles.com (for example the hoverlink specimen's background, candidate L981), and the sandbox hosts — T1's hotlink ×35, the P5 family, dispositioned class (ii) / KB-58 in register c1; the RERUN16 row records the candidate-own hosts as judgment-required and the ledger determination charges none of them to the candidate.
- **Why:** P7 (JP fallbacks in load and stack; the serif load covers the theme's serif uses in the base layer). P5's disposition is the register's.
- **Verify:** `grep -n '@import' candidate.txt` for the loads; `grep -n 'hormress.github.io\|ah-sandbox' candidate.txt | wc -l` for the kept asset hosts.
- **Disposition:** Loads and stacks applied; the images DISPOSITIONED (class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** Header strings as variables: the branch module's :root block sets `--title: "SCP財団"` and `--subtitle: "確保 · 収容 · 保護"` (candidate L1018–1019) — the JP header title and the Foundation motto in Japanese, supplied as the theme's variables in the KB-57 form. Sidebar: the original frames its sidebar two ways — a `:scp-wiki-cn:component:interwiki-style` include at priority=3 naming the branch main.css (original L1003–1007), and one hidden styleFrame `[[embed]]` iframe per color preset, pointed at the CN interwiki host with priority=4 (original L1058–1105). The candidate repoints the sidebar frame to the JP component (candidate L1023–1027, the type=sidebar parameter dropped to the JP component's default form) and converts each preset embed into the same JP component form at priority=4 naming the same preset CSS (candidate L1078–1131; residue B143–B148) — the KB-43 styleFrame shape given a JP component counterpart instead of deletion, because here the frame carries the theme's own preset CSS, not a foreign wiki's sidebar file (the contrast with theme:oneiroi-west-jp in this batch, whose embed pointed at a CN nav file and was deleted). Head-module supplements (candidate L8–22, annotated): the base theme's Safari-mode flag (`--set-safari-mode-disabled: set`), an iframe-spacing rule, and tt styling keyed to the base's `--basalt-secondary-color` variable — the last being visible evidence of the Parallel framework's Basalt lineage inside this file. The RERUN16 row's furniture judgments are recorded in section 11 (the collapsed PC sidebar with the theme's own hamburger is the theme's design, judged clean by T3).
- **Why:** P8/T6 (sidebar and frame adaptation) and P9 (header variables keep their names, their defaults localized).
- **Verify:** `grep -n 'interwiki-style\|--title:\|--subtitle:' candidate.txt` — the sidebar frame, the six preset frames, and the two variable lines.
- **Disposition:** Standing; the render judgments DISPOSITIONED in section 11.

### 6. Text translation

- **What:** The documentation body (roughly 600 lines of element specimens between the credit zone and the tail modules) is translated throughout: the design notes (candidate L416, crediting the Basalt and Monotypical designs with labeled CN links, section 7), the font specimens, the hoverlink specimen, and every element example, in the original's order. The translation mass is the classifier's bulk (TRANS-UNANCHORED 82, TRANSLATION-ANCHORED 51), resolved here in aggregate per the class M convention: line-pair translation inside an unmoved body, with no structural change riding in it. In-CSS text (R1): the main module's comments are translated with the same mass. R5 glyph-form conversion, stated separately (GLYPH-FORM, 4 blocks): retained strings take Japanese glyph forms where a string survives (the credit title's 法向投影 is kept as the original-title quotation; its display form 法線射影 is the translation). Chinese survives in the candidate in the credit block's original-title field (candidate L391), where it is a quotation.
- **Why:** P10 (body, usage, and sample translation) and KB-18 (reader-visible strings in the specimens).
- **Verify:** The body sections of diff.md in order; a Chinese-prose scan of candidate.txt outside the credit field returns nothing.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the one quotation.

### 7. Links

- **What:** The documentation's branch references change form throughout: intra-wiki CN links become labeled external-form links to the same pages on scp-wiki-cn.wikidot.com with branch notes (candidate L416: Basalt（中国語版） and Monotypical（中国語版）; candidate L791: the SCP style resource; candidate L949: SCP-CN-1353; candidate L967: the Letters hub; candidate L979: the hoverlinks component; candidate L985: the Parallel classic header component), because those pages have no JP counterparts in the composition to repoint to. The credit source link (candidate L395) names scp-wiki-cn.wikidot.com, the recorded host, and serves the original.
- **Why:** P11: a prose link takes the JP counterpart where one exists and the serving original where it does not; the dead-reference standard is not engaged, nothing here is dead.
- **Verify:** `grep -n 'scp-wiki-cn.wikidot.com' candidate.txt` — the source link and the labeled documentation links.
- **Disposition:** Standing.

### 8. Structure

- **What:** The declared deviations are the delivery items of section 3 (the head module's creation and the base repoint; the gate's move behind the delivery layer) and the usage-contract rewrite of section 2 (the two-include example collapsing to one, because the delivery internalized the base). Everything else holds: the module inventory corresponds one to one (main module, branch module, the seven preset modules with their parameter-trick comments preserved), the documentation's specimen census corresponds in the same order, and the styleFrame embeds are converted, not dropped (section 5), so no R3 deletion arises. The EXHIBIT-RESTRUCTURE primaries are adjudicated in the class summary.
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census and by naming the deviations, not by the label.
- **Verify:** Compare `grep -n '\[\[module\|\[\[include\|\[\[embed' original.txt candidate.txt` — the embeds are the only original forms with no same-form counterpart, and each has its converted include.
- **Disposition:** Standing with the deviations declared; no class I item.

### 9. Formatting only

- **What:** Two single blank-line changes, both in the residue appendix (B4, a blank line added at the credit zone's head; B140, a blank line removed at the tail modules' head). No WS-ONLY label fired and the classifier finds 0 re-indentation blocks, so there is no other formatting churn to disclose.
- **Why:** Formatting churn is disclosed as its own class; the follow-up-diff hazard is limited to these two lines.
- **Verify:** The B4 and B140 entries in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two porter annotations, both in module CSS comments. (a) At candidate L8, `/* SCP-JP port additions: Safari mode flag from the base theme, iframe spacing, tt styling */`, introducing the head module's supplement block (candidate L9–22). (b) At candidate L1012, `/* SCP-JP port: JP font fallbacks after the upstream imports */`, introducing the branch module's :root block (candidate L1013–1019). Both are the port explaining its own additions in the file, in English; no `[!-- --]` note exists.
- **Why:** R2: annotations are part of the port's record; these two document the supplement blocks' intent, which sections 4 and 5 rely on.
- **Verify:** `grep -n 'SCP-JP port' candidate.txt` returns candidate L8 and L1012.
- **Disposition:** Standing (part of the candidate as reviewed).

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) The GitHub Pages delivery dependence (P4): charged by T4 as MISSED with the wording quoted in section 3 (LOCALIZE-ROWS row 207) and DISPOSITIONED at GOSIGN2-LEDGER §(c3) as "delivery class (ii): original-state CDN delivery"; the base-framework half of the dependence was in fact removed by the FIX-P4 repoint, as section 3 records. (2) T1's 35 hotlinks and 2 pseudo-refs: the hotlinks are the section 4 images (class (ii) / KB-58, register c1); the pseudo-refs are the draft-host base import pair (class (iii)). (3) The RERUN16 render items (RENDER-ROWS-RERUN16 (CN10), superseding ROWS-2 under rule S1), with the lane's own judgments: the candidate-own runtime hosts (ah-sandbox.wdfiles.com, fontsapi.zeoseven.com, hormress.github.io) recorded as judgment-required and charged to no one at the determination; no page-overflow on either page; T3 clean on both pages, the collapsed PC sidebar with the theme's own hamburger being the theme's design; the machine contrast warn judged a false positive in the row ("dark text on light blue readable"); the em and hl-code overflows judged intentional specimens; the sample's missing webkit full-page captures a 32767px tooling cap, recorded as a capture limitation rather than a page defect; and the sample's credit-modal errors (KB-32, ruling 5). (4) The two per-theme notes are recorded below, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; the render lane's in-row judgments are carried verbatim so a reviewer can see which items were judged and how.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–3 as stated); the per-theme items noted with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 223): exit 1, 37 errors / 1 warn / 0 infos; 35 hotlink (class (ii)) and 2 pseudo-ref (class (iii)); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-RERUN16 (CN10)): FINDINGS, the items of section 11(3), all dispositioned or judged in the row; engine coverage full (chromium+webkit, both pages). (c) T4/T5 (LOCALIZE-ROWS row 207, LOCALIZE-S2-E): FINDINGS / FINDINGS jointly, display-affecting findings 1 (the P4 item), dispositioned at §(c3). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (diff.md): +236/−210, 446 changed lines in 148 change blocks / 20 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:normal-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 208; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the mono stack's unloaded JP fallback (note)

The branch module's :root block sets `--mono-font: "JetBrains Mono", "Noto Sans Mono", "Noto Sans JP", monospace` (candidate L1017), and the documentation's mono specimen names the same pair (candidate L998). No @import in this file loads "Noto Sans Mono": the head module loads the Sans and Serif JP faces only (candidate L2–3), and the file's other font load is Google Sans. The face is a mid-stack fallback, not a first face, so the standing flag shape (a first-named face loaded nowhere) does not arise; and the load could in principle arrive through the imported base chain, which this package does not review (theme:parallel-jp is a separate package). If it arrives from nowhere, the stack falls through to "Noto Sans JP", which is loaded — a soft landing, not a broken one. Recorded so the base package's reviewer can close the question from the other side.

### Item 2 — the credit fragment's provenance (note)

The original's credit body is an external fragment (`:scp-wiki-cn:fragment:hormress`, original L374), not text in the frozen source. The candidate's filled fields (notably 作成年 2026, candidate L392) therefore rest on the wave's record of that fragment and the live page, not on bytes this package can check. The holder value itself (Dr Hormress) is independently supported by the frozen source (the framework imports, the fragment's name, and the documentation's voice are all his). Recorded so a reviewer does not mistake the year field for a value checked against the original; no dropped-creator flag arises, since the frozen source names no one else.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-normal-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)). The base theme's candidate, `pages/theme:parallel-jp.txt`, is a separate theme package in this campaign, not part of this change set; this candidate's dependence on it is recorded in section 3. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 法向投影 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:normal — revision 1
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
