# Review package — theme:i57-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:i57-jp — origin EN, population #99 [GOSIGN2-LEDGER (b) row 99]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 99]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 13 errors / 1 warn / 1 info (hotlink×13); standing classes dispositioned in register c1 [T1-ROWS row 109; GOSIGN2-LEDGER (b) row 99]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — runtime-hotlink incl. scp-wiki.wikidot.com, 1366 content-overflow fncon/a up to +104px, 1366 sidebar-collapsed with own ☰; notice/panel items cross-cutting. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 99, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 99]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 99]
- Computed against: canonical commit a497307c6e7eedc2580739ba55d2c3212d9cacd2; candidate file pages/theme:i57-jp.txt sha256:06c32f4da1c19a286fe66d6371eb582a9d049759e057c3b57a7e3987cc21dbe7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/i57-jp/candidate.txt (sha256 06c32f4da1c19a286fe66d6371eb582a9d049759e057c3b57a7e3987cc21dbe7)
Original: theme:i57 — scp-wiki, revision 41 (sha256 0fd1b84235997e84ade0801ab75ff0a94e70d44b521360c6acec3109893cc483)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 99); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no i57 entries |
| Fixed after the localize check | P7 (Bebas Neue title stack gained a Japanese font), landed inside commit f931619 (FIX2-COLON) together with the KB-01 colon encoding and the ruling-3 translator normalization; the exhibit copy's duplicate font imports were removed in commit a497307 (FIX4-MECH) |
| Standing items | **DISPOSITIONED** — T1 hotlink×13, class (ii) (ledger (c1)); localize P5 EN-storage assets live ×6, class (ii) / KB-58 (ledger (c3)); render findings: runtime hotlink, the 1366 content-overflow (fncon/a, up to +104px) and the notice/panel items, all cross-cutting (ledger (c2)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:i57 | theme:i57-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 41, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 41 | — |
| Source of this copy | Campaign mirror store `orig-i57-rev41.txt` (class COPY, byte-identical; review/sources.tsv) | Canonical file `pages/theme:i57-jp.txt`, created in commit a869415 (Stage 2 EN11); later commits f931619 (FIX2-COLON) and a497307 (FIX4-MECH, last content change) |
| Lines / bytes | 681 lines / 17,718 bytes | 1,139 lines / 31,973 bytes |
| SHA-256 | 0fd1b84235997e84ade0801ab75ff0a94e70d44b521360c6acec3109893cc483 | 06c32f4da1c19a286fe66d6371eb582a9d049759e057c3b57a7e3987cc21dbe7 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; standalone BHL base). No production counterpart was adopted: the candidate's CSS body measures 0.976-similar to the original's own code exhibit (classifier topology pass). The localize follow-up records "No unincorporated upstream updates."

## Summary

The original is a Black Highlighter theme ("FACILITY-57") with a split delivery: a small head module holding the BHL imports and the #page-title rules, two BHL frames, a bare Rate module as page furniture, and its main stylesheet in a code exhibit (orig L217–671) delivered by a tail module @import of its own /1 plus a third frame (priority=3). The candidate merges the delivery into one head module (cand L2–473): the BHL imports repointed to scp-jp.github.io, the head module's own rules kept, and the exhibit body inlined after them; the two BHL frames are repointed, the tail self-import module and the priority=3 frame are deleted as consistent with the inline, the bare Rate is removed, and the preview credit block naming Rounderhouse is added where the original had no credit device at all (no info module exists on the original). The exhibit is retained whole as documentation (cand L683–1136). Two wave commits follow the population pattern: FIX2-COLON carrying the P7 font fix (Noto Sans JP into the Bebas Neue header stack, both copies) inside its colon scope, and FIX4-MECH removing the exhibit copy's two font @imports as duplicates. The classifier counts 12 blocks (11 specific, 1 heuristic, resolved in the Appendix); diff.md measures +676/−218 in 8 sections. The theme passed with no open items; its 13 T1 hotlink errors are the EN-storage asset lines, dispositioned class (ii).

## Classification

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 8 |
| COLON-ENC | 4 |
| EXHIBIT-RESTRUCTURE | 2 |
| HEADERVAR | 2 |
| TRANS-UNANCHORED | 2 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| COMMENT-TEXT | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |

Counts: 12 blocks — 11 specific (91.7%), 1 heuristic (8.3%, B3, resolved in the Appendix), 0 residue, 0 skipped. Topology: the original's code exhibit (orig L216–671) moved to the candidate's module-css (cand L1–473) at 0.976 similarity; the candidate-side own-delivery companion body was unavailable to the classifier (its recorded caveat). Labels are sets per block; this README's sections were written from classification.json's label spans, not from the skeleton's per-section lists. The RATE-EXHIBIT-KEPT-CANDIDATE label needs adjudication against the bytes and gets it in section 1 (the Rate was removed, not kept), as in highroller-jp in this batch.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with the `[[iftags +theme]]` gate (L1, block B1) and the head module (L2–17). The candidate keeps the order, the gate localized, and the module becomes the whole delivery (section 3). Provenance route: derived from the original at reference revision 41 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P1/P4 rework exactly this frame.
- **Verify:** Read original L1–17 against candidate L1–20; block B1 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original has no credit block and no info module (grep: no `info:` include anywhere); its only rating device is the bare `[[module Rate]]` at orig L30, inside a `[[>]]` block, and its attribution is the exhibit's comment header naming Rounderhouse. The candidate removes the bare Rate (grep: no `[[module Rate]]` in the candidate) and adds the preview credit block (cand L485–494): `:scp-jp:credit:start-preview` / `end-preview` with all eight ruling-3 fields — title I57 BHLテーマ, translator AI, translation year 2026, original title "I57 BHL Theme", copyright holder Rounderhouse, creation year 2020, reference revision 41, and the source link to the EN page. The author field agrees with the original's exhibit header. The classifier's RATE-EXHIBIT-KEPT-CANDIDATE label on B4 spans only the original side (orig L29–30) and its own note routes it to the writer's kept-vs-removed reasoning: the reasoning is that the Rate was removed, because the preview credit module is rate-bearing (KB-09). No license box exists on either side, and none was charged (KB-63 covers dropped boxes; this original never had one). The theme carries no credit-module CSS of its own; the credit styling is BHL's and the preview module's.
- **Why:** P3/T1: the preview credit module is the JP environment's credit form and it is rate-bearing, so a separate bare Rate beside it would duplicate the rating widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields and credits campaign translations to AI; f931619 normalized this file's translator field from SCP-JP to AI under that ruling.
- **Verify:** Read candidate L485–494 against the eight-field list and the original's exhibit header (orig L218–220 region); `grep -n 'module Rate' candidate.txt` (absent); `grep -n 'info:' original.txt` (absent).
- **Disposition:** Standing (the port's credit form); the localize lane verified the credit form and charged no credit item.

### 2. Includes and components

- **What:** The candidate's include list (grep): the two interwiki-style frames (cand L475, L480, repointed `:scp-jp:`), the credit pair (L485/L494), the theme-squares component (cand L505, repointed), the escaped usage exhibits (cand L543: @@[[include:scp-jp:theme:black-highlighter-theme]]@@, the prefix form kept as in the original; cand L544: @@[[include theme:i57-jp]]@@, the bare form), and the tail `component:bhl-dark-sidebar` repointed (cand L1139; the original's at orig L674). The original's third frame (priority=3, its own /1) left with the tail delivery module (section 3). No `:scp-wiki:` include remains live in the candidate.
- **Why:** P1: foreign-site includes are repointed to the JP site; the usage exhibits keep the original's two forms with the site prefix updated on the BHL line and the bare fullname on the theme's own line. Ruling 4 does not engage: every component the theme uses exists on the JP site.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; no include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** The original loads BHL through the head module's @imports (orig L3–4, from nu-scptheme.github.io) and two frames (priority=1 the normalize layer, priority=2 the black-highlighter layer, both nu-scptheme theme= URLs), and loads its own stylesheet from the tail: a module @import of its own /1 on scp-wiki.wdfiles.com (orig L675–677) and a third frame (priority=3, theme= the same /1, orig L678–681). The candidate repoints the BHL @imports to scp-jp.github.io (cand L3–4), keeps the head module's own #page-title rules, inlines the exhibit body into the same module (cand L2–473; topology code-css → module-css at 0.976), repoints the two BHL frames (cand L475–484), and deletes the tail self-import module and the priority=3 frame (B12: SELF-DELIVERY spans orig L675–676 and L679–680, candidate side empty). That deletion is consistent with the inline: the deleted channels carried the same body the module now carries, and they took no include parameters, so no variant channel was lost — the explicit contrast with greystyle-jp in this batch, where the deleted tail modules were parameter-gated. The candidate has no self-delivery reference left for the population audit to class; its delivery is the inline module plus the BHL frames. The BHL logo image in the body is repointed to scp-jp.github.io/Black-Highlighter/img/black-highlighter-logo.svg.
- **Why:** P4/T9: deliveries are served from JP hosts in this environment, and inlining removes the candidate's runtime dependence on the EN wiki's code page altogether.
- **Verify:** Read orig L2–4 and L674–681 against cand L2–6, L475–484 and L1139; block B12 in classification.json.
- **Disposition:** Standing; no delivery item was charged for this theme beyond the asset hosts in section 4.

### 4. Fonts and assets

- **What:** Font changes, by commit. At creation: the exhibit's Bebas Neue import (Google Fonts) carried into both copies. In f931619 (FIX2-COLON): a Noto Sans JP @import added in both copies and --header-font rewritten from `"Bebas Neue", cursive` to `"Bebas Neue", "Noto Sans JP", cursive` in both copies (labels JPFONT-LOAD and FONT-IMPORT) — the P7 fix, riding inside the colon commit (Per-theme record, item 1); the same commit colon-encoded the asset URLs in both copies (COLON-ENC ×4 blocks: the i57logo.png --logo-image, the i57.png backgrounds and the MAC-1.png background; `theme:i57` → `theme%3Ai57`, KB-01). In a497307 (FIX4-MECH): the exhibit copy's two font @import lines (Bebas Neue, Noto Sans JP) removed as duplicates (KB-65); the live module copy retains both (cand L5–6), so the retained exhibit now differs from the delivered CSS at the font-import block. The theme's other named faces (Inter for body text, Recursive for mono, per the translated font-sample prose at cand L676–678) arrive through the BHL layer the candidate imports, as they did in the original; no stack in this file names a font that nothing loads. Assets: the EN-storage lines (i57logo.png, i57.png, MAC-1.png and their kin across the two copies) are the T1 checker's 13 hotlink errors; the localize row counts 6 distinct EN-storage assets live.
- **Why:** P7/T5, in the localize lane's own formulation for this theme: "Bebas Neue on JP page titles" — Bebas Neue has no Japanese glyphs, so a Japanese page title in the header stack fell back to an OS-dependent generic until Noto Sans JP entered the stack behind it (the lane's item (b), display-affecting). KB-65: a duplicated @import inside one file is removed from the non-delivering copy. P5/KB-58: re-hosting EN-storage assets is a posting-procedure act, class (ii).
- **Verify:** `grep -n 'Bebas Neue\|Noto Sans JP' candidate.txt` (imports and stacks in the module copy; the stack only in the exhibit copy); `git show f931619 -- pages/theme:i57-jp.txt` and `git show a497307 -- pages/theme:i57-jp.txt`.
- **Disposition:** P7 FIXED (ledger (c3), recorded there as "font wave"; the bytes sit in FIX2-COLON, see Multi-wave provenance). Assets DISPOSITIONED (ledger (c3): P5, class (ii) / KB-58; ledger (c1): the hotlink class is (ii)).

### 5. Header, sidebar, site furniture

- **What:** The header variables are carried verbatim in both copies: --header-title "FACILITY-57" and --header-subtitle "SEGURIDAD. CONTENCIÓN. PROTECCIÓN" (orig L237–238 ↔ cand L39–40 in the module copy and cand L702–703 in the exhibit copy; HEADERVAR spans B6 at orig L234–235 → cand L36–37 for the --logo-image line, and inside B11 at cand L699–703). The subtitle is the work's own Spanish slogan, part of the theme's fiction. The #page-title rules from the original's head module survive at the module's head (cand L7–19 region), now with the supplemented header stack behind them (section 4). The render row notes the 1366 sidebar-collapsed state showing the theme's own ☰ glyph — the theme's own furniture behaving as designed, recorded in the row as an observation among the cross-cutting overflow items.
- **Why:** P9 was not charged for this theme; ruling 2 (2026-11-16) places header and title language outside migration correctness in any case (KB-57, patterns 9c5e907).
- **Verify:** `grep -n 'header-title\|header-subtitle' candidate.txt` (four hits, two per copy, values as above).
- **Disposition:** Standing; no header item was charged in any register.

### 6. Text translation

- **What:** The body prose, the usage text, the exhibit headings and the font-sample prose are translated (TRANSLATION-ANCHORED 1 block, TRANS-UNANCHORED 2 blocks; the font samples at cand L676–678 now read as Japanese sentences naming Bebas Neue, Inter and Recursive). In-CSS text stays in English where it is the theme's own data: the exhibit comment header (COMMENT-TEXT firing at B5, orig L220 → cand L22) and the CONTENT-STRING spans inside B11 (cand L695–696, L744–745, L842–843, L858–859), which are the exhibit's own string content carried as defined. The localize T5 pass found no untranslated body paragraph and no mistranslation.
- **Why:** P10: body and usage text are translated; CSS comments and the theme's own string data are not reader prose.
- **Verify:** Read orig L34–216 against cand L496–682; LOCALIZE-ROWS row 99 (no T5 item charged).
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The candidate's prose links are the credit block's source link (cand L493 area, to the EN original — the required ruling-3 back-reference) and the usage exhibits (section 2). No other prose link targets an EN page; the un-suffixed fullname otherwise appears only inside asset URL paths (section 4).
- **Why:** P11 repoints links to JP counterparts where the link survives; here the surviving links are the required back-reference and the usage forms, so there was nothing further to repoint and no dead target arises.
- **Verify:** `grep -n 'theme:i57' candidate.txt` and read each hit's role.
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** The stylesheet's relocation (section 3) preserves rule order (0.976-similarity move), and the exhibit is retained whole as documentation (cand L683–1136). The head restructure (B4: orig L19–217 → cand at L20) is the Rate removal and the body reordering around the merged module, decided in section 1. The tail (B12) keeps the bhl-dark-sidebar include and drops the two self-delivery channels (section 3). The content census maps one-to-one: head module, frames, furniture, theme-squares, exhibits, exhibit, tail include — every original region has a named fate in these sections, and no second module, license entry or documentation body from the original is missing in the candidate.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the census is stated explicitly.
- **Verify:** The census above against `grep -n '\[\[module\|\[\[code\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** The classifier counts 0 re-indentation blocks and no WS-ONLY blocks for this theme; formatting churn rides inside the delivery-move blocks. Brace balance, checked by depth with comment- and string-awareness: every channel on both sides ends at depth 0 (the original's head module, exhibit and tail module; the candidate's module and exhibit). A naive brace count shows +1 on this theme's CSS; the depth profile with comment handling ends at 0, the +1 being a brace character inside a CSS comment — the count-vs-depth distinction is exactly why the check is run by depth.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; a displaced closing brace keeps the counts equal while swallowing every later rule, and only a depth scan sees it.
- **Verify:** classification.json (reindent_blocks 0); the depth figures are reproducible by scanning each [[module CSS]] / [[code]] channel of the two files with comment awareness.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none — no signature fired, and direct inspection agrees: the candidate contains no `[!-- ... --]` translator notes. The only added text with no original counterpart is the frame repoint, the credit block and the font supplement, each accounted for in its own section.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here the ground for "none" is the inspection above plus the section-by-section accounting.
- **Verify:** `grep -n '\[!--' candidate.txt` (no translator-note lines).
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The 13 EN-storage asset lines: T1 hotlink×13, DISPOSITIONED class (ii) (GOSIGN2-LEDGER (c1) hotlink entry; (c3) P5, KB-58). (2) The render findings: runtime hotlink including scp-wiki.wikidot.com, the 1366 content-overflow on fncon/a up to +104px, and the notice/panel items: DISPOSITIONED as cross-cutting classes with the render row (ledger (c2)). The row's sidebar-collapsed ☰ observation is the theme's own furniture (section 5), not a defect. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–2).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 13 errors / 1 warn / 1 info; all 13 errors are hotlink, the section 4 asset lines (T1-ROWS row 109). Register (c1) dispositions the hotlink class as (ii). (b) T2/T3 render: FINDINGS, all items dispositioned in (c2) (section 11, item 2); engine coverage is the lane's full matrix as run (RENDER-ROWS-1, RENDER-S2-B). (c) T4 localize plus follow-up: FINDINGS with 2 display-affecting items (LOCALIZE-ROWS row 99); outcomes P5 DISPOSITIONED / P7 FIXED (ledger (c3)); the follow-up found no unincorporated upstream updates. (d) T5: judged jointly with T4; no mistranslation finding. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (12 change blocks) and the generator's (diff.md: +676/−218 in 8 sections); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:i57-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 99).

## Per-theme record

### Item 1 — wave attribution: the "font wave" for this file is inside FIX2-COLON

Ledger (c3) records P7 as "FIXED (font wave)". No font-wave commit touches this file: the history is a869415 (creation), f931619 (FIX2-COLON), a497307 (FIX4-MECH), and the Noto Sans JP import and the --header-font rewrite are in f931619's diff, alongside its named colon-encoding scope and the ruling-3 translator normalization. The bytes are right; the record's wave name is wrong for this theme. The same pattern recurs across this batch (greystyle, helix, highroller, hytoth-two) and in the ambrose package's FIX-CREDIT-D.

### Item 2 — the classifier's Rate label, adjudicated

The label RATE-EXHIBIT-KEPT-CANDIDATE fires on B4 with an original-side span only (orig L29–30), and the candidate contains no `[[module Rate]]` at all. Read literally, the label would claim the Rate was kept in the candidate; the bytes say it was removed in the credit swap. The label's own note anticipates the ambiguity, and section 1 records the reasoning: removed, on KB-09 grounds. The same mislabel shape fires in highroller-jp in this batch.

## Change set outside the two diffed files

None for this theme: no other canonical file carries part of this port. The two wave commits are shared vehicles — f931619 (FIX2-COLON) touched 18 theme files and a497307 (FIX4-MECH) touched 29; this file's hunks in each are narrated in sections 3–4 and in Multi-wave provenance.

## Multi-wave provenance

| Commit | Wave | What it changed in this file |
|---|---|---|
| a869415 | Stage 2 EN11 creation | The whole port: BHL imports repointed to scp-jp.github.io, the exhibit inlined into the head module behind the original head rules, the two BHL frames repointed, the tail self-import module and priority=3 frame deleted, the bare Rate removed, the credit block added, the body translated, the exhibit retained |
| f931619 | FIX2-COLON | The P7 fix riding inside the colon commit: Noto Sans JP @import added in both copies and --header-font rewritten to `"Bebas Neue", "Noto Sans JP", cursive` in both copies; the asset URLs colon-encoded in both copies (KB-01); the credit block's translator field normalized SCP-JP → AI (ruling 3) |
| a497307 | FIX4-MECH | The exhibit copy's two font @import lines (Bebas Neue, Noto Sans JP) removed as duplicates (KB-65); the live module copy keeps its imports (cand L5–6) |

## Appendix — heuristic and residue blocks

There are no residue blocks. The one heuristic block and the two diff-only labels:

- **B3** (orig L17 → cand at L19, module-css → body, CSS-BODY, "no other signature matched"): the boundary artefact of the merged module. Orig L17 is the head module's closing line; in the candidate the same head rules end inside the enlarged module and the inlined body begins (the `/* Fonts */` comment at cand L20). Nothing was lost or added at this boundary beyond the inline itself, which section 3 accounts for.
- **B11** (orig L561 → cand L363–1026, RESTORATION): the two-copy alignment artefact. The differ pairs a single original line against the long candidate span containing the credit block and the exhibit's head; its label spans locate the real insertions: CREDIT-PREVIEW (cand L484–485, L493–494) and TASL-FIELDS (cand L485–493) for the credit block, HEADERVAR (cand L699–703) and CONTENT-STRING (cand L695–696, L744–745, L842–843, L858–859) in the exhibit copy. The RESTORATION label is a diff-only signal; nothing for this theme was deleted and later restored by a wave. The TASL-FIELDS label also fires at cand L674–675, on field-shaped lines in the font-sample documentation region; the theme's only credit block is cand L485–494.
