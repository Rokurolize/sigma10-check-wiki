# Review package — theme:parallel-jp (CN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:parallel-jp — origin CN, population #216 [GOSIGN2-LEDGER (b) row 216]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now add7ef557672d36ef4c8cfbb3a3d92925c4fb56cb86c50df3d68253f8601ad61); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 9 warns / 0 infos (hotlink×9, foreign-include×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 186; GOSIGN2-LEDGER (b) row 216]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 502–506px@320/375 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-F (CN11))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 5 [LOCALIZE-ROWS row 215, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 215]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 216]
- Computed against: canonical commit a6fe19237b2c46030c63e3fce28516242508cb0d; candidate file pages/theme:parallel-jp.txt sha256:add7ef557672d36ef4c8cfbb3a3d92925c4fb56cb86c50df3d68253f8601ad61; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items (GOSIGN2-LEDGER (b) row 216) |
| Standing items | **DISPOSITIONED** — five ledger lines, the batch's richest set: P1, P4, P5, P10, P11 (sections 2–4, 6–7, 11). **FLAGGED by this package** — the six preset usage exhibits name the plain slug on the JP side, and the preset parameter gates the exhibits teach stand empty in the candidate's consolidated CSS (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:parallel | theme:parallel-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 41 (first translation; the candidate's credit block records 初訳時参照リビジョン: 41) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-parallel.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:parallel-jp.txt`, copied at worktree HEAD f1138e4 |
| Lines / bytes | 761 lines / 25,254 bytes | 873 lines / 32,310 bytes |
| SHA-256 | 5ef1e68a5d11d803d0c3a5c31d59ee2f47ec2bcbd2b04e5dfc7e962aee3ef39 | b7b98a7cf0ff2a7e0169f68e67075164209b59257d22f8641cd774c51d7249a1 |

Wave history: the candidate was created by the Stage 2 CN11 integration (commit b8ee399, the LOCALIZE-S2-E wave's port), then reworked by 7cbe280 (deliver the Parallel base as an include target), touched by 1869877 (FIX-CREDIT-D, the translator-field normalization), and most recently by f1138e4 (FIX-P4, the base-import repoint). The verdict stamp is computed against that head. No FIX5 commit touches this file. This is the batch's only K5b-5 theme: its delivery is classed external in the campaign's typology, because the theme's own design serves its base stylesheets from the author's GitHub Pages site.

## Summary

A CN theme (Dr Hormress's Parallel, a heavily reworked derivative of the Bedrock base) whose delivery design is external and preset-driven, and whose port preserves the design's shape while changing its plumbing. The original serves two base stylesheets from the author's GitHub Pages, and five color presets as fragment code files on scp-wiki-cn, each preset's @import wrapped in a CSS-comment gate keyed on an include parameter (`bedrock=*`, `redstone=*`, …) that the theme's preset tabview teaches. The candidate keeps the two GitHub imports verbatim (the author's own CDN is the theme's original-state delivery, dispositioned under P4). After the two post-build repairs (FIX-GATES3/c7d6b2a and FIX-PARALLEL2/a6fe192, per-theme record) the four presets live in their own code blocks 2–5, deep-gold's content is restored in block 6 from the campaign's page-source capture, and the five gates stand in the delivery module in the original's exact form, each wrapping the local--code import of its own block — so the parameters the preset exhibits teach switch the presets as they do upstream. The earlier one-file consolidation and its emptied gates are superseded by those repairs; the per-theme record carries the correction. The rest of the port is complete: a preview credit block installed where the original has no credit furniture at all, the acknowledgements section carried with all five names, the sidebar frames replaced by the standard tail delivery pair, and the prose translated throughout, with two exhibits deliberately keeping their CN form (the red-marked original include syntax and the classic-header component exhibit) under the P1 disposition. Measured churn against the current (post-repair) candidate (diff.md, the generator's difflib count with autojunk off: +552/−406 in 12 change blocks / 3 diff sections; GNU-diff 956 changed lines). The pre-repair figures were +509/−398 in 11 classifier change blocks.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 11 change blocks — 10 specific (90.9%), 1 heuristic (9.1%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 8 |
| EXHIBIT-RESTRUCTURE | 2 |
| ANNOTATION | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the specific share (90.9%) is the batch's highest, and the block structure is simple to adjudicate. B1 (original L0–1 → candidate L0–391) is the head relocation: the gate, the credit install, and the whole translated prose body stand where the original's delivery module stood. B2 (RESTORATION; original L4 → candidate L394–497) is the presets' variable sets carried inline into the consolidated CSS. B3–B7 are the five parameter gates' relocation into that CSS, one block each. B8–B9 are the two exhibit-zone relocations (the gated module's second half and the mid-body samples). B10 is the CSS tail's relocation, and B11 the tail delivery pair. The single heuristic label (TRANS-UNANCHORED inside B1) is the prose translation mass. After adjudication no block is left unexplained; the per-theme flag concerns what the relocated gates no longer do, not any block's identity.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:parallel-jp; original theme:parallel on scp-wiki-cn at reference revision 41; candidate `pages/theme:parallel-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-E wave (sources.tsv kind: K5b-5, external delivery — the campaign's class for a theme whose base stylesheets are served from the author's own site rather than from wiki code pages; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order is rebuilt: the original opens with its delivery module and sidebar frames (original L1–41); the candidate opens with the localized gate `[[iftags +テーマ]]` and the credit block (candidate L1–12), and delivers from the tail (candidate L865–873).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the delivery pair is P6/T3 (section 3).
- **Verify:** The sources.tsv row for parallel-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself).

### 1. Credit and attribution

- **What:** The original has no credit furniture at all: no credit module, no Rate module, no license box — its attribution is prose, the information section naming [[*user Dr Hormress]] as the author (original L32 zone) and a closing acknowledgements section （致谢， original L752–759) crediting the Bedrock theme's creators ([[*user EstrellaYoshte]], [[*user Liryn]], [[*user Placeholder-mcd]]), the Black Highlighter influence ([[*user woedenaz]]), and early design input ([[*user hoah2333]]). The candidate installs the preview credit block at the head (candidate L3–12) carrying the eight ruling-3 fields (title 平行 版式 — the Chinese title kept, section 5; 翻訳責任者 AI; 翻訳年 2026; 原題 平行 版式； 著作権者 Dr Hormress, in the plain-name form; 作成年 2024; 初訳時参照リビジョン 41; the source link https://scp-wiki-cn.wikidot.com/theme:parallel, whose host matches the sources.tsv record). The acknowledgements section is carried and translated in full (candidate L376–382, + 謝辞）, all five names and their roles preserved, including the note that the theme's SCP logo derives from the Black Highlighter logo. No license box exists on either side and none was installed; the theme's attribution surface is the credit block and the acknowledgements, and T4 raised no box item for this theme. T7 credit-module CSS: none on either side.
- **Why:** P3/T1: the JP environment's theme pages carry the preview credit block as their attribution furniture; where the original has none, the block is installed from the prose record, which is what happened here. Ruling 3 fixes the eight fields and the translator form; 1869877 is that form arriving.
- **Verify:** Read candidate L3–12 against the eight fields; compare the acknowledgements at original L752–759 and candidate L376–382 name by name.
- **Disposition:** FIXED by construction at creation (P3 credit fields installed from the prose attribution).

### 2. Includes and components

- **What:** The original's page-level includes are its two sidebar frames (`:scp-wiki-cn:component:interwiki-style` with `type=sidebar`, priorities 1 and 2, naming the two GitHub stylesheets, original L31–41); they leave with the delivery rebuild, and the candidate's frame is the standard tail pair (section 3). The candidate's remaining includes are the credit pair (section 1) and a repointed image-block exhibit (`:scp-jp:component:image-block`, candidate L95, its asset the Basalt project's logo file on the EN wiki, named in full URL form as the original named it). Two exhibits deliberately keep their CN form, and both are the P1 disposition's substance: the theme-title exhibit prints the original include syntax with the wiki prefix marked in red as the part to notice (`@@[[include @@[[span …]]@@:scp-wiki-cn:@@[[/span]]@@theme:parallel]]@@`, candidate L27), and the classic-header exhibit prints `:scp-wiki-cn:component:parallel-classic-header` (candidate L45) — exhibit text about the original, not live includes, kept because the exhibits' subject is the original's own syntax. The prose link to the classic-header component page keeps its bare local form (candidate L42), resolving on the reader's wiki as the original's did.
- **Why:** P1 (KB-15), with the (c3) register's P1 disposition for this theme covering the kept exhibit forms: an exhibit that teaches the original's syntax is documentation of the original, and repointing it would falsify the lesson.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the credit pair, the frame, and the image-block exhibit; the two CN-form exhibits are at candidate L27 and L45.
- **Disposition:** DISPOSITIONED (P1; (c3) register, parallel line).

### 3. Delivery and code loading

- **What:** The original's delivery is three-layered. Layer one: a head module CSS importing the author's two GitHub Pages stylesheets (normalize-min.css and parallel-min.css from hormress.github.io/Parallel, original L2–3) — the theme's base, served from the author's own site by design. Layer two: five preset @imports from the theme's fragment pages on scp-wiki-cn (`fragment:parallel/code/2` … `/6`, original L5–23), each wrapped in a CSS-comment gate keyed on its include parameter (`/* {$bedrock}/` … `/{$bedrock} */` and its four siblings); the content lives in separately addressable fragments, the gates in render-time module text. Layer three: a second module CSS inside the gate with the theme's additional rules (original L43 onward), exhibited in the page's code block. The candidate now mirrors that split inside its own delivery architecture after two post-build repairs (per-theme record; FIX-GATES3/c7d6b2a and FIX-PARALLEL2/a6fe192). Its consolidated code block 1 (candidate L391–740) keeps the two GitHub imports at its head (candidate L392–393 — the FIX-P4 wave's repoint kept the author's CDN as the base delivery, the (c3) P4 disposition), the porter's consolidation comment (candidate L395, section 10), the theme's head rules, the demonstration/preset tabview CSS and the .earthworm rules; it holds no preset section and no gate. The four preset sections stand in their own code blocks 2–5 in source order inside the same collapsible/`[[iftags +テーマ]]` region (bedrock L741–760, redstone L761–788, deepslate L789–819, deep-diamond L820–849), each byte-identical to its former inlined form. Deep-gold's block 6 (L850–877) carries `fragment:parallel` code/6 content restored verbatim from the campaign's page-source capture; the consolidated block never held a deep-gold section — the earlier README claim that it did was wrong on the bytes and is corrected here. The delivery module (candidate L882–905) mirrors the original's head module in render-time text: the /1 import first (candidate L883, its terminating semicolon restored since further @imports now follow), then the five gates in the original's exact form, each wrapping the draft-host local--code import of its own block (candidate L885–903: `/* {$bedrock}/` … `local--code/theme%3Aparallel-jp/2` … `/{$bedrock} */`, and likewise /3, /4, /5 and /6 for redstone, deepslate, deep-diamond and deep-gold); the interwiki frame at priority 1 (candidate L907) names /1. An including page passing `bedrock=*` now substitutes into the delivery module's gate lines, opening the /2 import while the other four stay commented; with no parameter all five stay inert — the original's behaviour. The preset exhibits teach the working syntax (candidate L58–83, all naming `theme:parallel-jp` after the b5cb724 usage sweep).
- **Why:** P4/T9 and P6/T3 for the tail pair and the import form; KB-41 for the draft lines (class (iii)). The GitHub base is the theme's original-state delivery (the author's own placeholder site is part of the theme's design, as its prose explains), kept under the (c3) P4 disposition rather than re-hosted. The content-by-URL/gates-in-render-text split is the original's mechanism, restored so that the parameters the exhibits teach actually switch the presets; the earlier one-file consolidation broke that mechanism and is superseded, with its two repairs recorded in the per-theme record.
- **Verify:** `grep -n 'hormress.github.io\|local--code/theme%3Aparallel-jp\|{\$' candidate.txt` — the base imports at L392–393; the /1 import at L883 and the five gated imports at L886/890/894/898/902; the frame `theme=` at L907. Compare the five gate lines at candidate L885–903 against original L5–23.
- **Disposition:** DISPOSITIONED (P4, (c3) register, parallel line; the draft-host lines, class (iii)); the gates' present form is the two repairs recorded below, not an outstanding flag.

### 4. Fonts and assets

- **What:** No font loads of the theme's own: its faces come from the base stylesheets and the Sigma environment on both sides, so no JPFONT signature fired and there is no KB-16 question to answer — the skeleton's silence for this section is correct, and its ground is this inheritance, stated here rather than left blank. Assets: the theme's logo images are served from the author's GitHub Pages site on both sides (the candidate's head exhibits name hormress.github.io/Parallel/images/parallel-theme-logo.svg and its -zh variant, candidate L19–21, exactly as the original's did), and the tail's project image likewise (original L761 zone, carried). The image-block exhibit's Basalt logo keeps its full EN-wiki URL (candidate L95). These are the T1 baseline's hotlink family (hotlink×9), dispositioned with the delivery under P4/P5: the author's site is the theme's asset home by design, not a porting shortcut.
- **Why:** P5 with the (c3) register's P5 disposition for this theme: original-state external assets that are the author's own distribution are carried, not re-hosted.
- **Verify:** `grep -n 'hormress.github.io' candidate.txt` — the import pair and the image loci.
- **Disposition:** DISPOSITIONED (P5; (c3) register, parallel line).

### 5. Header, sidebar, and site furniture

- **What:** The HEADERVAR signature inside block B2 fires on the presets' variable sets (the basalt-derived color variables the presets redefine), which are carried as the presets' content, not translated as strings. The theme's title is kept in Chinese （平行 版式， candidate L4 and L8) — the P9-class retention the campaign's dispositions cover for this theme's family (its (c3) lines disposition P10/P11 for the text classes and P4/P5 for delivery; the title is the theme's proper name in both fields, original-title and title alike). The sidebar frames' replacement is section 3; the toggle behaviour the frames provided is part of the base delivery the JP environment supplies. No P8 layout adaptation was needed.
- **Why:** P9/T6: the header variables here are mechanism (color values), and the theme's name is its authors' display text.
- **Verify:** The preset variable sections are at candidate L396–497.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The prose is translated from Chinese throughout: the information section (the theme's basis in the Bedrock project, its design intent, its GitHub placeholder and repository links, candidate L30–36), the plugin section, the preset documentation (candidate L48–53), the element samples, and the acknowledgements (section 1), riding inside block B1's TRANS-UNANCHORED mass and verified passage by passage against the mirror for this README. One comment-form note is the original's own, translated in place: the hidden comment pointing to the derivative project theme:normal (original L332 → candidate L36), which is carried text, not a porter addition. The preset exhibits are translated in their labels and tab titles （デフォルト / 基岩 / レッドストーン / 深層岩 / 深層ダイヤモンド / 深層金鉱） while their include syntaxes keep the form flagged in the per-theme record. R1 in-CSS text: the preset section comments are carried in Chinese （配色方案：…, candidate L396–469) — porter-visible labels inside the delivered CSS, the original's own section markers, kept as the consolidation's signposts.
- **Why:** P10 and KB-18 (reader-visible strings localize), with the (c3) register's P10 disposition for this theme covering the exhibit-text classes. The CSS section comments are the R1 porter-visible half, carried as the original's structure.
- **Verify:** The pairs are diff.md's body sections in order; the comment note is candidate L36.
- **Disposition:** DISPOSITIONED in its exhibit classes (P10; (c3) register, parallel line); standing for the prose.

### 7. Links

- **What:** The candidate's live outbound link is the credit block's source link (candidate L11), naming the original on scp-wiki-cn.wikidot.com, the host the campaign's provenance records name for it. The prose's links to the author's GitHub placeholder and repository are carried with translated link text (candidate L34–36), as are the bare local links to the Basalt project's pages ([[[theme:basalt|玄武岩]]], [[[theme:bedrock|基岩]]], candidate L32), which resolve on the reader's wiki on both sides — on scp-jp they name the JP Basalt port candidates, which is the campaign's cross-theme dependency rule (a dependent theme references the base's JP port, not the raw upstream delivery). The (c3) register's P11 disposition for this theme covers this link set. No link in the candidate is dead on the evidence of the mirror.
- **Why:** P11: prose links take the JP counterpart or the serving original; bare local names that resolve to the JP port on scp-jp satisfy the rule in its strongest form.
- **Verify:** `grep -n 'theme:basalt\|theme:bedrock' candidate.txt` — candidate L32.
- **Disposition:** DISPOSITIONED (P11; (c3) register, parallel line).

### 8. Structure

- **What:** The localize.md closing rule holds for the content: the census corresponds — the information and plugin sections, the preset tabview with its six tabs, the element samples, the AIM/ACS component documentation, the acknowledgements, and the CSS (base imports, five preset sections, the theme's rules) all stand in the candidate, with the JP corrections arriving as the head credit install and the tail delivery pair. The two EXHIBIT-RESTRUCTURE blocks (B8, B9) adjudicate to relocations of the gated module's second half and the mid-body samples into the consolidated order. The one structural transformation is the delivery consolidation of section 3, which is a topology change with its mechanism cost recorded in the per-theme record; it is counted here so the census claim is not read as covering it. No brace-depth anomaly was found in this pair (the depth scan balances on both sides).
- **Why:** R3: a restructure and a silent deletion share a diff shape; the census decides for the content, and the delivery change is disclosed in-file (candidate L395), so it is a flagged mechanism note, not a class I deletion.
- **Verify:** Compare `grep -n '^\+\|code type' original.txt candidate.txt` — the section sequences correspond.
- **Disposition:** Standing for the content; the delivery gate is flagged below.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation anywhere in the pair (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classification summary's WS-ONLY count is 0.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation: the comment at the consolidated CSS's head (candidate L395), "parallel：原語版の CSS をまとめたもの" (the original's CSS, gathered into one), which marks the consolidation where it begins; it rides inside block B2. The classifier's ANNOTATION label inside B1 fires on the comment-form note at candidate L36, which is not a porter addition but the original's own hidden comment on its derivative project, translated in place (section 6) — the distinction is recorded here so the two comment forms are not conflated. There are no editor lines in the candidate.
- **Why:** R2: porter-added text is part of the change record; carried comments are part of the original's text, and the record keeps the two apart.
- **Verify:** Read candidate L36 and L395.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** This theme carries the batch's richest disposition set, five (c3) lines, each with its ground. (1) P1 (section 2): the two exhibits keeping their CN form, as documentation of the original's syntax. (2) P4 (sections 3–4): the author's GitHub Pages base delivery kept as the theme's original-state CDN form, the delivery class the K5b-5 typology records. (3) P5 (section 4): the author's-site assets carried, not re-hosted. (4) P10 (section 6): the exhibit-text classes. (5) P11 (section 7): the link set, including the bare local base-theme links resolving to the JP ports. Beyond the five: T1's eleven errors are hotlink×9 (items 2–3's family), foreign-include×1 (the original's frame form at baseline), and pseudo-ref×1 (the candidate's own draft-host line, class (iii)). The render row's items are environment or capture layer, not charged to the candidate: the page overflow readings (502–506px at 320/375) and the runtime-hotlink site-theme chain (KB-40), and, recorded verbatim because it limits the evidence, the sample's T2 run produced no machine verdict (exit 2, no summary) — the row itself carries that inconclusiveness, and this package does not paper over it. The preset gating flagged by the original build has since been repaired by two post-build lanes (FIX-GATES3, c7d6b2a, and FIX-PARALLEL2, a6fe192); it has no (c3) line of its own in the frozen ledger, and those repair records plus the per-theme record below are where it is now documented, rather than a disposition line that the ledger does not carry.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes; the named register lines), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 186 and register (c1).
- **Disposition:** DISPOSITIONED (items 1–5).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 186): exit 1, 11 errors / 9 warns / 0 infos; the errors are hotlink×9, foreign-include×1, pseudo-ref×1, all in the dispositioned classes of section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-F (CN11)): FINDINGS, the items of section 11, with the sample's T2 run inconclusive as recorded there; engine coverage as run by the lane, with the row's own caveat carried in the stamp. (c) T4/T5 (LOCALIZE-ROWS row 215): FINDINGS jointly, display-affecting findings 5, matching the five dispositioned P-lines of section 11; the (c3) register dispositions all five. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. The churn counts quoted in the Summary describe the pre-repair candidate; the regenerated diff.md for the current candidate reports +552/−406 in 12 change blocks / 3 diff sections (GNU-diff 956 changed lines), the authoritative count for the bytes now in this package.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:parallel-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 216; go-sign, COMPLETION-REPORT §10), with the per-theme flags below standing as this package's addition to the record.

## Per-theme record

### The preset exhibits' slug, and the gates they teach (flagged by this package)

> Historical flag — this paragraph records the state at package build. Both the exhibit slugs and the gate mechanics it describes have since been repaired; the repair record immediately below governs the current candidate, and section 3 has been rewritten accordingly.

The preset tabview's six exhibits were repointed from `:scp-wiki-cn:` to `:scp-jp:` at creation, keeping the plain slug: the default include (candidate L58) and the five preset forms (`:scp-jp:theme:parallel bedrock=*` at L63, `redstone=*` at L68, `deepslate=*` at L73, `deep-diamond=*` at L78, `deep-gold=*` at L83). The candidate's own posting name is theme:parallel-jp, so all six documented syntaxes name a page that will not exist under that name on scp-jp; the file's own delivery lines use the -jp form (candidate L868, L872). That is the population-sweep family, flagged here with its loci as in the sibling packages. The preset exhibits carry a second, theme-specific gap the sweep will not fix: the parameters they teach no longer switch anything in the candidate. In the original, each parameter breaks open a CSS-comment gate around that preset's fragment @import (original L5–23). In the candidate's consolidated CSS the presets' contents stand inlined as unconditional sections (candidate L396–497) and the five gates stand after them empty (candidate L498–518), each wrapping a blank line; and the delivered file is imported by URL from the tail module, so an including page's parameters have no gate left to act on in any case. The campaign's P4 disposition covers this theme's delivery rework in general (the delivery was reworked twice under that line, 7cbe280 and f1138e4), but no record addresses the preset gating specifically, so this package flags the state rather than dispositioning it: a JP author following the candidate's own preset instructions changes nothing, and either the gates should be restored around JP-side preset deliveries or the exhibits should stop teaching parameters. The candidate is left unedited.

### Both points of the gate flag have since been repaired — FIX-GATES3 (c7d6b2a) and FIX-PARALLEL2 (a6fe192)

The two claims the flag above raised are both corrected in the current candidate; the flag is kept as the historical record of the state at package build, and the section 3 passage was rewritten accordingly at this refresh, exactly as FIX-PARALLEL2's note for the coordinator requires.

1. **The gates — first restored, then made effective.** FIX-GATES3 (report `R/review-scout/FIX-GATES3.md`), landed in canonical commit `c7d6b2a132f5d8eb72a8e69a15e0c93a42fe1576` ("pages: parallel preset gates re-gated", 2026-11-17), wrapped the four inlined preset sections back in their parameter gates and deleted the four empty shells, with a rule-multiset census proving no rule text changed. Its own caveat — that gates inside a URL-delivered code block cannot be switched by an including page — was then resolved by FIX-PARALLEL2 (report `R/review-scout/FIX-PARALLEL2.md`), landed in canonical commit `a6fe19237b2c46030c63e3fce28516242508cb0d` ("pages: parallel preset delivery restructured to the original's form", 2026-11-17). That restructure moved the four preset sections into code blocks 2–5, restored deep-gold's content in block 6 from the page-source capture, and placed the five gates in the delivery module in the original's exact form, each wrapping that block's draft-host @import (candidate L882–905). A passing `bedrock=*` now substitutes into the gate text at render time and opens the /2 import; no parameter leaves all five inert. The "parameters have no gate to act on" claim is therefore no longer true.

2. **The "deep-gold section within the consolidated block" claim was wrong on the bytes.** The consolidated block never held a deep-gold section — only an empty shell — and its values survived solely in the tabview preview rule. FIX-PARALLEL2 restored `fragment:parallel` code/6 verbatim from the campaign capture into its own code block 6 (candidate L850–877), verified byte-identical to the page-source capture and declaration-equal to the independent audit-inline capture. The four moved preset rules were verified byte-identical to their former inlined sections; the delivery module's /1 import gained its terminating semicolon (mechanical necessity once further @imports follow), otherwise byte-identical. The checker's delta is exactly five new pseudo-ref findings, one per gated @import (/2…/6), the class (ii) posting-rewrite family of the pre-existing /1 pseudo-ref; no new class (i) error.

3. **The exhibits' plain-slug half of the flag** was closed earlier by the population sweep b5cb724: all six preset exhibits now name `:scp-jp:theme:parallel-jp` (candidate L58–83).

This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:parallel-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-parallel-jp.txt` is the decoration sample the render checks ran against (its T2 run is the inconclusive one recorded in section 11); it belongs to this theme's record but carries no port change of its own to explain here. The theme's companion component exhibits (the Parallel components and the classic header) are separate pages on the original wiki, referenced as exhibits in section 2; they are not part of this port. There are no companion fragments in this repo and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** 平行 版式
- **Author:** Dr Hormress
- **Source:** https://scp-wiki-cn.wikidot.com/theme:parallel — revision 41
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
