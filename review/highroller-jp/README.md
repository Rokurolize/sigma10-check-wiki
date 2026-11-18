# Review package — theme:highroller-jp (EN → JP port)
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:highroller-jp — origin EN, population #97 [GOSIGN2-LEDGER (b) row 97]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 97]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 1 warn / 1 info (hotlink×11); standing classes dispositioned in register c1 [T1-ROWS row 107; GOSIGN2-LEDGER (b) row 97]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — 768px sidebar×notice overprint + ≤375 notice left-clip + WebKit CC "S" (all cross-cutting); sample 320px right-floated image clipped at left edge. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 97, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 97]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 97]
- Computed against: canonical commit a497307c6e7eedc2580739ba55d2c3212d9cacd2; candidate file pages/theme:highroller-jp.txt sha256:61e9e63e6b4648170a5ddc435452212120fdeb358da080a50dd97f99d5336562; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/highroller-jp/candidate.txt (sha256 61e9e63e6b4648170a5ddc435452212120fdeb358da080a50dd97f99d5336562)
Original: theme:highroller — scp-wiki, revision 17 (sha256 cd680502821c6609be411c8276ea22c7eb1424bb10b452e9225b8efb26cd84cc)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 97); one of the 286 of 286 pass-eligible themes |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no highroller entries |
| Fixed after the localize check | P7 (Japanese font supplement), landed inside commit f931619 (FIX2-COLON) together with the KB-01 colon encoding and the ruling-3 translator normalization; the exhibit copy's duplicate font imports were removed in commit a497307 (FIX4-MECH) |
| Standing items | **DISPOSITIONED** — T1 hotlink×11, class (ii) (ledger (c1)); localize P5 EN-storage imagery, class (ii) / KB-58 (ledger (c3)); render findings: the 768px sidebar×notice overprint, the ≤375 notice left-clip and WebKit CC "S" (cross-cutting families), and the sample's 320px right-floated image clipped at the left edge (KB-37 specimen shape) (ledger (c2)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:highroller | theme:highroller-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 17, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 17 | — |
| Source of this copy | Campaign mirror store `orig-highroller-rev17.txt` (class COPY, byte-identical; review/sources.tsv) | Canonical file `pages/theme:highroller-jp.txt`, created in commit a869415 (Stage 2 EN11); later commits f931619 (FIX2-COLON) and a497307 (FIX4-MECH, last content change) |
| Lines / bytes | 534 lines / 17,179 bytes | 862 lines / 30,300 bytes |
| SHA-256 | cd680502821c6609be411c8276ea22c7eb1424bb10b452e9225b8efb26cd84cc | 61e9e63e6b4648170a5ddc435452212120fdeb358da080a50dd97f99d5336562 |

Provenance route: derived from the original at the reference revision (sources.tsv kind: standard; standalone BHL base). No production counterpart was adopted: the candidate's CSS body measures 0.963-similar to the original's own code exhibit (classifier topology pass). The localize follow-up records no unincorporated upstream updates for this theme.

## Summary

The original is a Black Highlighter theme ("UNDERVEGAS") that loads BHL by module import and two frames, shows a bare Rate module and a template info module as page furniture, and delivers its own stylesheet from its code exhibit (orig L192–526) through a tail module @import of its own /1. The candidate inlines the exhibit into the head module (cand L3–341), repoints the frames, removes the bare Rate, replaces the template info module with the preview credit block naming Rounderhouse, translates the body, and retains the exhibit as documentation; the tail self-import module is deleted, consistently with the inline, and unlike greystyle's parameter modules it carried no include parameters, so nothing else was lost with it. The font host repoint (fonts.bunny.net → Google Fonts) was already present at creation in both copies. Two wave commits follow: FIX2-COLON, which again carries the P7 font supplement inside its named colon scope, and FIX4-MECH, which removes the exhibit copy's four @import lines as duplicates. The classifier counts 10 blocks, all specific; diff.md measures +532/−204 in 7 sections. The theme passed with no open items; its 11 T1 hotlink errors are the EN-storage imagery lines, dispositioned class (ii).

## Classification

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 5 |
| EXHIBIT-RESTRUCTURE | 2 |
| WS-ONLY | 2 |
| COLON-ENC | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| RESTORATION | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| TRANSLATION-ANCHORED | 1 |

Counts: 10 blocks — 10 specific (100%), 0 heuristic, 0 residue, 0 skipped. Topology: the original's code exhibit (orig L191–526) moved to the candidate's module-css (cand L2–341) at 0.963 similarity; the candidate-side own-delivery companion body was unavailable to the classifier (its recorded caveat). Labels are sets per block; this README's sections were written from classification.json's label spans, not from the skeleton's per-section lists. Two labels need adjudication against the bytes and get it in the sections: RATE-EXHIBIT-KEPT-CANDIDATE (section 1: the Rate was removed, not kept) and the second TASL-FIELDS firing (Appendix: a font-sample exhibit, not credit fields).

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with the `[[iftags +theme]]` gate (L1, block B1) and the BHL module (L3–6). The candidate keeps the same order with the gate localized and the module carrying the inlined delivery (section 3). Provenance route: derived from the original at reference revision 17 (see Provenance); no R4 adoption.
- **Why:** The header frame is where the original declares its delivery; P1/P4 rework exactly this frame.
- **Verify:** Read original L1–6 against candidate L1–6; block B1 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original's furniture holds two rating/credit devices: a bare `[[module Rate]]` inside a `[[>]]` block (orig L19–21) and an info module (orig L23–31) whose content is a template — placeholder SCP-XXXX / AUTHOR / TRANSLATOR fields, i.e. the theme's sample info module for article pages, not the theme's own credit. The theme's own attribution is the exhibit's comment header, "by ROUNDERHOUSE" (orig L196). The candidate removes the bare Rate (grep: no `[[module Rate]]` in the candidate) and replaces the info module with the preview credit block (cand L353–362): `:scp-jp:credit:start-preview` / `end-preview` with all eight ruling-3 fields — title ハイローラーテーマ, translator AI, translation year 2026, original title "Highroller", copyright holder Rounderhouse, creation year 2023, reference revision 17, and the source link to the EN page. The author field agrees with the original's exhibit header. The classifier's RATE-EXHIBIT-KEPT-CANDIDATE label on B3 spans only the original side (orig L19–20) and its own note routes it to the writer's kept-vs-removed reasoning: the reasoning is that the Rate was removed, because the preview credit module is rate-bearing (KB-09). INFO-DEL spans (orig L22–23, L30–31, inside B3) record the template info module's removal in the same swap. No license box exists on either side, and none was charged (KB-63 covers dropped boxes; this original never had one). The theme carries no credit-module CSS of its own; the credit styling is BHL's and the preview module's.
- **Why:** P3/T1: the preview credit module is the JP environment's credit form and it is rate-bearing, so a separate bare Rate beside it would duplicate the rating widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields and credits campaign translations to AI; f931619 normalized this file's translator field from SCP-JP to AI under that ruling.
- **Verify:** Read candidate L353–362 against the eight-field list, original L19–31 and original L196; `grep -n 'module Rate' candidate.txt` (absent).
- **Disposition:** Standing (the port's credit form); the localize lane verified the credit form and charged no credit item.

### 2. Includes and components

- **What:** The candidate's include list (grep): the two interwiki-style frames (cand L343–352, section 3), the credit pair (L353/L362), the escaped usage exhibits (cand L412: @@[[include:scp-jp:theme:black-highlighter-theme]]@@, the prefix form kept because the exhibit names a same-site page in its full prefixed form as the original did; cand L413: @@[[include theme:highroller-jp]]@@, the bare form), and the tail component includes repointed to `:scp-jp:` (cand L861–862; the original's tail pair at orig L530–531). The theme-squares component in the body is likewise repointed. No `:scp-wiki:` include remains live in the candidate.
- **Why:** P1: foreign-site includes are repointed to the JP site; the usage exhibits keep the original's two forms with the site prefix updated on the BHL line and the bare fullname on the theme's own line. Ruling 4 does not engage: every component the theme uses exists on the JP site.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; no include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** The original loads BHL through the head module's @imports (orig L3–6, from nu-scptheme.github.io) and two interwiki frames (priority=1 and 2, theme= the nu-scptheme layer URLs), and loads its own stylesheet through a tail module @import of its own /1 on scp-wiki.wdfiles.com (orig L532–534). The candidate repoints the BHL @imports to scp-jp.github.io, inlines the exhibit body into the same head module (cand L3–341; topology code-css → module-css at 0.963), repoints the two frames to the JP host forms (cand L343–352; DELIVERY-HOST), and deletes the tail self-import module (B10: SELF-DELIVERY span orig L532–533, candidate side empty). That deletion is consistent with the inline: the module's content is the exhibit's content, and the deleted module took no include parameters, so no variant channel was lost with it — the explicit contrast with greystyle-jp in this batch, where the deleted tail modules were parameter-gated. The BHL logo image in the body is repointed to scp-jp.github.io/Black-Highlighter/img/black-highlighter-logo.svg.
- **Why:** P4/T9: deliveries are served from JP hosts in this environment, and inlining removes the candidate's runtime dependence on the EN wiki's code page altogether.
- **Verify:** Read orig L3–6 and L530–534 against cand L3–6, L343–352 and L861–862; block B10 in classification.json.
- **Disposition:** Standing; no delivery item was charged for this theme beyond the asset hosts in section 4.

### 4. Fonts and assets

- **What:** Font changes, by commit. At creation: the exhibit's font imports (Playfair Display, Ysabeau Office, Telex) were already repointed from fonts.bunny.net (orig L199–201) to fonts.googleapis.com in both copies (creation lines 13–15 and 532–534) — label FONT-IMPORT. In f931619 (FIX2-COLON): a Noto Sans JP @import added in both copies and 'Noto Sans JP' inserted into --header-font, --title-font and --body-font plus one unanchored font-family line, in both copies (label JPFONT-LOAD) — the P7 supplement, riding inside the colon commit (Per-theme record, item 1); the same commit colon-encoded the Bellagio_Fountain.webp URL (COLON-ENC, KB-01). In a497307 (FIX4-MECH): the exhibit copy's four @import lines (Playfair Display, Ysabeau Office, Telex, Noto Sans JP) removed as duplicates (KB-65); the live module copy retains all four (cand L13–16), so the retained exhibit now differs from the delivered CSS at the font-import block. Assets: the theme's imagery (the finished2.gif logo image and the fountain webp among them) stays on scp-wiki.wdfiles.com in both copies — the 11 lines that are the T1 checker's 11 hotlink errors.
- **Why:** P7/T5: Playfair Display, Ysabeau Office and Telex have no Japanese glyphs, so without a JP font in the stacks, Japanese headings and body text fall back to an OS-dependent generic (the localize lane's item (b), display-affecting). P5/KB-17: fonts.bunny.net is a mirror outside the permitted host list, so the import went to the canonical Google Fonts host. KB-65: a duplicated @import inside one file is removed from the non-delivering copy. P5/KB-58: re-hosting the EN-storage imagery is a posting-procedure act, class (ii).
- **Verify:** `grep -n 'fonts.bunny.net\|fonts.googleapis.com\|Noto Sans JP' candidate.txt` (bunny absent; googleapis imports and stack insertions in both copies); `git show f931619 -- pages/theme:highroller-jp.txt` and `git show a497307 -- pages/theme:highroller-jp.txt`.
- **Disposition:** P7 FIXED (ledger (c3), recorded there as "font wave"; the bytes sit in FIX2-COLON, see Multi-wave provenance). Assets DISPOSITIONED (ledger (c3): P5, class (ii) / KB-58; ledger (c1): the hotlink class is (ii)).

### 5. Header, sidebar, site furniture

- **What:** The header variables are carried verbatim in both copies: --header-title "SITE-666", --header-subtitle "UNDERVEGAS", and --logo-image naming finished2.gif on scp-wiki.wdfiles.com (part of the section 4 hotlink set). The classifier's HEADERVAR firing sits in the exhibit copy (B9 span cand L536–539). The in-CSS string variables --theme-id / --theme-name ("UNDERVEGAS THEME") are untranslated CSS text (residue class R1), not reader prose. Sidebar and top-bar rules are byte-preserved inside the moved body. P9 was not charged for this theme.
- **Why:** Ruling 2 (2026-11-16) places header and title language outside migration correctness (KB-57, patterns 9c5e907); the values are the work's own names in any case.
- **Verify:** `grep -n 'header-title\|header-subtitle\|theme-name' candidate.txt` (hits in both copies, values as above).
- **Disposition:** Standing; no header item was charged in any register.

### 6. Text translation

- **What:** The body prose, the usage text and the exhibit headings are translated (TRANSLATION-ANCHORED 1 block, TRANS-UNANCHORED 1 block). The template info module's placeholder text left with the module (section 1). In-CSS text stays in English where it is the theme's own data: the comment header (including the "by ROUNDERHOUSE" credit), the string variables (section 5), and the CONTENT-STRING firing (B9 spans cand L535–536, L588–589), which is the exhibit's own string content carried as defined. The localize T5 pass found no untranslated body paragraph and no mistranslation.
- **Why:** P10: body and usage text are translated; CSS comments and the theme's own string data are not reader prose.
- **Verify:** Read orig L34–190 against cand L364–524; LOCALIZE-ROWS row 97 (no T5 item charged).
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** The candidate's prose links are the credit block's source link (cand L361 area, to the EN original — the required ruling-3 back-reference) and the usage exhibits (section 2). The template info module's placeholder links left with the module. No other prose link targets an EN page; the un-suffixed fullname otherwise appears only inside asset URL paths (section 4).
- **Why:** P11 repoints links to JP counterparts where the link survives; here the surviving links are the required back-reference and the usage forms, so there was nothing further to repoint and no dead target arises.
- **Verify:** `grep -n 'highroller' candidate.txt` and read each hit's role.
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** The stylesheet's relocation (section 3) preserves rule order (0.963-similarity move), and the exhibit is retained whole as documentation (cand L526–857). The furniture restructure at the head (B3: orig L8–192 → cand at L7) is the Rate/info swap decided in section 1. The tail (B10) keeps the two component includes and drops the self-import module (section 3). No second CSS module, license entry or documentation body from the original is missing in the candidate: the original's content census (head module, frames, furniture, exhibits, exhibit, tail) maps one-to-one onto the candidate's, with the two furniture devices replaced as recorded.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the census is stated explicitly; here every original region has a named fate.
- **Verify:** The census above against `grep -n '\[\[module\|\[\[code\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** 2 of the 10 blocks are WS-ONLY (B6, B8), single blank-line changes inside the moved body; the classifier counts 0 re-indentation blocks. Brace balance, checked by depth with comment- and string-awareness: every channel (the original's head module, exhibit and tail module; the candidate's module and exhibit) ends at depth 0 on both sides. The candidate's one `http://` string (cand L164) is a W3C namespace identifier inside a data-URI SVG, the known HTTP-KEPT false-positive shape, not a kept HTTP load.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; the depth check exists because a displaced closing brace keeps the counts equal while swallowing every later rule.
- **Verify:** classification.json (2 WS-ONLY blocks, reindent_blocks 0); read cand L164 in place.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none — no signature fired, and direct inspection agrees: the candidate contains no `[!-- ... --]` translator notes. The only added text with no original counterpart is the frame repoint, the credit block and the font supplement, each accounted for in its own section.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here the ground for "none" is the inspection above plus the section-by-section accounting.
- **Verify:** `grep -n '\[!--' candidate.txt` (no translator-note lines).
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The 11 EN-storage imagery lines: T1 hotlink×11, DISPOSITIONED class (ii) (GOSIGN2-LEDGER (c1) hotlink entry; (c3) P5, KB-58). (2) The 768px sidebar×notice overprint and the ≤375 notice left-clip: DISPOSITIONED as cross-cutting narrow-width families (ledger (c2)). (3) WebKit CC "S": DISPOSITIONED, cross-cutting (KB-36). (4) The sample's 320px right-floated image clipped at the left edge: DISPOSITIONED with the render row (the KB-37 specimen shape). No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–4).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 11 errors / 1 warn / 1 info; all 11 errors are hotlink, the section 4 asset lines (T1-ROWS row 107). Register (c1) dispositions the hotlink class as (ii). (b) T2/T3 render: FINDINGS, all items dispositioned in (c2) (section 11, items 2–4); engine coverage is the lane's full matrix as run (RENDER-ROWS-1, RENDER-S2-B). (c) T4 localize plus follow-up: FINDINGS with 2 display-affecting items (LOCALIZE-ROWS row 97); outcomes P5 DISPOSITIONED / P7 FIXED (ledger (c3)). (d) T5: judged jointly with T4; no mistranslation finding. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp. Counts in this README are the classifier's (10 change blocks) and the generator's (diff.md: +532/−204 in 7 sections); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:highroller-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 97).

## Per-theme record

### Item 1 — wave attribution: the "font wave" for this file is inside FIX2-COLON

Ledger (c3) records P7 as "FIXED (font wave)". No font-wave commit touches this file: the history is a869415 (creation), f931619 (FIX2-COLON), a497307 (FIX4-MECH), and the Noto Sans JP import and the three stack insertions are in f931619's diff, alongside its named colon-encoding scope and the ruling-3 translator normalization. The bytes are right; the record's wave name is wrong for this theme. The same pattern recurs across this batch (greystyle, helix, i57) and in the ambrose package's FIX-CREDIT-D.

### Item 2 — the classifier's Rate label, adjudicated

The label RATE-EXHIBIT-KEPT-CANDIDATE fires on B3 with an original-side span only (orig L19–20), and the candidate contains no `[[module Rate]]` at all. Read literally, the label would claim the exhibit Rate was kept in the candidate; the bytes say it was removed in the credit swap. The label's own note anticipates the ambiguity ("removed Rate sits beside an exhibit label; routed to residue for the writer's kept-vs-removed reasoning"), and section 1 records the reasoning: removed, on KB-09 grounds. The same mislabel shape fires in i57-jp in this batch.

## Change set outside the two diffed files

None for this theme: no other canonical file carries part of this port. The two wave commits are shared vehicles — f931619 (FIX2-COLON) touched 18 theme files and a497307 (FIX4-MECH) touched 29; this file's hunks in each are narrated in sections 3–4 and in Multi-wave provenance.

## Multi-wave provenance

| Commit | Wave | What it changed in this file |
|---|---|---|
| a869415 | Stage 2 EN11 creation | The whole port: BHL imports repointed to scp-jp.github.io, the exhibit inlined into the head module, the frames repointed, the bare Rate removed, the template info module replaced by the credit block, the font imports repointed from fonts.bunny.net to Google Fonts in both copies, the body translated, the exhibit retained, the tail self-import module deleted |
| f931619 | FIX2-COLON | The P7 supplement riding inside the colon commit: Noto Sans JP @import added in both copies and 'Noto Sans JP' inserted into --header-font / --title-font / --body-font plus one unanchored font-family line, in both copies; the Bellagio_Fountain.webp URL colon-encoded (KB-01); the credit block's translator field normalized SCP-JP → AI (ruling 3) |
| a497307 | FIX4-MECH | The exhibit copy's four font @import lines (Playfair Display, Ysabeau Office, Telex, Noto Sans JP) removed as duplicates (KB-65); the live module copy keeps its imports (cand L13–16) |

## Appendix — heuristic and residue blocks

There are no heuristic and no residue blocks (10 specific of 10). Two specific labels are adjudicated here so they are not mistaken for content:

- **B9** (orig L473 → cand L288–804, RESTORATION): the two-copy alignment artefact. With two full copies of the stylesheet in each file, the differ pairs a late original region against a long candidate span; the block's label spans locate the real insertions inside it: CREDIT-PREVIEW (cand L352–353, L361–362) and TASL-FIELDS (cand L353–361) for the credit block, HEADERVAR (cand L536–539) and CONTENT-STRING (cand L535–536, L588–589) in the exhibit copy. The RESTORATION label is a diff-only signal (added lines matching the original's own earlier region, i.e. the second copy); nothing for this theme was deleted and later restored by a wave.
- **TASL-FIELDS second firing** (inside B9, cand L514–515): the signature fires on the font-sample `[[span]]` exhibit lines in the body, which are field-shaped documentation samples, not credit fields. The theme's only credit block is cand L353–362.

## License and attribution

- **Title:** Highroller Theme
- **Author:** Rounderhouse
- **Source:** https://scp-wiki.wikidot.com/theme:highroller — revision 17
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
