# Review package — theme:twin-files-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:twin-files-jp — origin EN, population #151 [GOSIGN2-LEDGER (b) row 151]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 01cc7ea529556e0bf0cffe01370cc42f61bc356b3564b39275f8647ff588f8a8); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 12 errors / 1 warn / 1 info (pseudo-ref×12); standing classes dispositioned in register c1 [T1-ROWS row 136; GOSIGN2-LEDGER (b) row 151]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 337–419px@320/375. [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 151, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 151]
- FIX5 re-judgement: item 34 (class D) FIXED — FIX5-FONTSB, commit 3911f7b: pattern-7 fix [GOSIGN2-LEDGER-SUPPLEMENT (a) item 34]
- Computed against: canonical commit 4176cc76aa668e42056010548f62a1db8d06a32e; candidate file pages/theme:twin-files-jp.txt sha256:01cc7ea529556e0bf0cffe01370cc42f61bc356b3564b39275f8647ff588f8a8; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 34 [D] (JP font named, never loaded) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 34: **FIXED** (FIX5-FONTSB, commit 3911f7b); re-derived from this package's bytes and from the fix commit's own diff in the per-theme record below |
| Stamp state | The generated stamp above reads STALE by design: it was computed against canonical commit 4176cc7, whose self-delivery address repair postdates the 435a6bb-era verdict the stamp carries. The repair is recorded with its citation in section 3; no re-judgement is fabricated, and the frozen ledger remains the verdict record for the bytes it judged |
| Open flags from this package | None. Two in-CSS repairs of original defects are recorded in the per-theme record for the EN-author report file |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:twin-files | theme:twin-files-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 32, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 32 | — |
| Source of this copy | Campaign mirror store `review-mirrors/orig-twin-files-rev32.txt`, a byte copy (class COPY in the mirror INDEX) of the S2 lane cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-twin-files.txt`, fetched once 2026-11-16 | Canonical file `pages/theme:twin-files-jp.txt` at worktree HEAD c6454ab; the file's last content change is 4176cc7 (self-delivery repair) over 3911f7b (FIX5-FONTSB) |
| Lines / bytes | 1,196 lines / 32,901 bytes (the final line carries no trailing newline, so `wc -l` reports 1,195) | 1,206 lines / 36,084 bytes |
| SHA-256 | d3b38af68014a95f23b0fb36f51ecae4a8eaa49d9376fbd0c122adf70cbf0796 (equals the review/sources.tsv mirror hash) | 01cc7ea529556e0bf0cffe01370cc42f61bc356b3564b39275f8647ff588f8a8 |

Provenance route: derived from the branch original at the reference revision (no production-counterpart adoption; the topology pass finds no relocation and the body diffs against the EN original throughout). This theme's review/sources.tsv note makes no supersession claim and none is owed.

## Summary

A large documentation theme (diff.md: +217/−207, 424 changed lines in 160 change blocks) whose port is nevertheless conservative: the topology is unchanged component for component (two BHL frames at the head, seven exhibit code blocks, one stylesheet code block that is both the source exhibit and the delivered CSS, a tail delivery frame), and the great majority of the 160 blocks are the translation of the theme's long documentation body (39 TRANSLATION-ANCHORED and 69 TRANS-UNANCHORED blocks, plus the residue lines resolved in the appendix, are that mass). The substantive changes are few and nameable: the BHL delivery hosts move from the old BHL host to the JP distribution, the Latin font loads move from fonts.bunny.net to Google Fonts, the credit block is added with its author correctly named, the bare Rate is removed, and the theme's one blocking item (a JP font named in the stacks but loaded nowhere) was repaired by FIX5 with the loads and the stack alignment this package re-derives. The candidate's self-delivery address, which the port initially pointed at the wrong code block, was repaired after the verdict by the population audit's landing (4176cc7) and is recorded with that citation. No open flag stands against this candidate.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens inside its gate `[[iftags +theme]]` with the BHL delivery header (original L3–18): a `[[module CSS]]` importing the normalize and black-highlighter stylesheets from the old BHL host (nu-scptheme.github.io), and two interwiki-style frames at priority 1 and 2 naming the same two URLs. The candidate mirrors the header line for line (candidate L3–18) with the gate localized (`+テーマ`) and the hosts repointed to the JP BHL distribution (scp-jp.github.io); its frame includes use the bare `component:interwiki-style` form, this file's house form throughout. Provenance route: this package's original is the mirror-store copy of the S2 lane cache at revision 32 (see Provenance); no live re-fetch was made for this package.
- **Why:** The header is the base-delivery declaration (P4/T9); the host repoint is the KB-17 old-BHL rewrite in its delivered form.
- **Verify:** Read original L1–18 against candidate L1–18.
- **Disposition:** Recorded; part of the delivery change argued under section 3.

### 1. Credit and attribution

- **What:** The original carries no credit block: its attribution is the stylesheet banner (original L408–412: "Twin Files Theme / [2022 Wikidot Theme] / by JackalRelated"). The candidate adds the preview credit block at candidate L24–33, in this file's bare include form (`[[include credit:start-preview]]`), with the eight standard fields; the fields were completed by FIX2-CREDIT (commit 666f543). The 著作権者 field names `[[*user JackalRelated]]` (candidate L29) — checked against the original's banner and correct; this file is not one of the credit-pointer cases. The original's bare `[[module Rate]]` inside a `[[>]]` block (original L24–26) does not stand in the candidate (block B8, BARE-RATE-DEL): the preview credit block is rate-bearing, so the widget renders once (KB-09). No license box stands on either side (both files carry only the `#license-area` CSS variables inside the stylesheet); the T4 box is absent from the original and was not supplemented here, a standing state the supplement catalogue shares with about half the A13 population, and no record charges it. No T7 credit-module CSS stands in either file (census: `creditButton` 0× on both sides).
- **Why:** P3/T1 for the block addition, ruling 3 for its fields, KB-09 for the Rate removal.
- **Verify:** Read candidate L24–33 against original L408–412; census `module Rate` and `license-box` on both files.
- **Disposition:** Standing as recorded; no attribution defect in this file.

### 2. Includes and components

- **What:** Candidate includes: the two head frames and the tail frame (`component:interwiki-style`, bare form), `component:image-block` (the hidden FIIC logo exhibit, re-hosted, caption translated), the credit pair (bare form), `:scp-jp:component:theme-squares` (candidate L45, repointed from `:scp-wiki:` with its color names translated), the two escaped install exhibits (candidate L89–90: `theme:black-highlighter-theme`, the production page's name, and `theme:twin-files-jp`, the candidate's own posting name), and `:scp-jp:component:toggle-sidebar-bhl` at the tail (candidate L1199, repointed from `:scp-wiki:`). No include is duplicated, and no live include points at the EN wiki. The bare include forms (interwiki-style, image-block, credit) are this file's consistent house form, inherited from the original's own bare forms where it had them; they resolve on the local wiki, and the checker baseline records no foreign-include error for them.
- **Why:** P1 repoints and the T8 swap for theme-squares; the install exhibits follow the campaign's posting-name rule, with the base exhibit naming the production page that will exist on SCP-JP (the snippet audit's coherent class: a reference is drift only when the same file's delivery layer contradicts it, and this file's BHL delivery is by URL, not by that include).
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the lists.
- **Disposition:** Standing as recorded.

### 3. Delivery and code loading

- **What:** Base delivery: the head module and the two head frames serve BHL's normalize (priority 1) and black-highlighter (priority 2) stylesheets, repointed from the old BHL host to scp-jp.github.io (section 0). Own delivery: the theme's CSS lives in its eighth code block (`[[code type="css"]]`, candidate L414–1196), which is both the displayed source exhibit and the delivered stylesheet; the tail module (candidate L1200–1202) imports it as local--code /8 from the draft host, and the tail frame at priority=3 names the same address (candidate L1203–1206). Code-block census, counting every form: exactly 8 code blocks on each side (seven `[[code]]` exhibits and the one `[[code type="css"]]` stylesheet, in the same order), so /8 names the stylesheet itself. The address has a history a reviewer should see whole: the original names /8 (original L1191, L1195); the ported candidate initially named /1, the first exhibit block, which the ledger register dispositioned on render evidence (RENDER-S2-D §17's later measurement showed both pages styled); the population audit (R/review-scout/FIX-CODEADDR.md) then re-checked every self-delivery address by census, classified this one a mismatch, and canonical commit 4176cc7 repointed both lines to /8, probe-verified on the draft host. That repair, not the earlier disposition, is the current state, and it is why the stamp above reads STALE against the pre-repair verdict. Draft-host URLs are the draft-form class (iii).
- **Why:** P4/T9 for the base hosts, P6/T3 for the frame stack (priorities 1/2 base, 3 own). A self-delivery address must name the block that holds the CSS (the audit's census rule); the served-byte census is the deciding check, and it is the check 4176cc7 applied.
- **Verify:** Census the code blocks (`grep -n '\[\[code'`, 8 hits per side, the eighth is the stylesheet); read candidate L1199–1206 against original L1189–1195; `git show 4176cc7 -- pages/theme:twin-files-jp.txt` shows the two repointed lines.
- **Disposition:** Standing as repaired (4176cc7, cited, not re-litigated); the two draft-host delivery lines stand as checker pseudo-ref lines, class (iii).

### 4. Fonts and assets

- **What:** The stylesheet's font loads stand at the code block's head (candidate L420–429). The six Latin faces (Jost, Rubik, Archivo, IBM Plex Mono, Sedgwick Ave, Arimo) move from fonts.bunny.net (original L414–419) to Google Fonts (candidate L421–426) with families, weights, and order unchanged — bunny.net is not among the direct-link exception hosts, Google Fonts is. The theme's own attachment stylesheet-alt.css is re-hosted from the EN wiki's file host to the candidate's draft-host attachments (candidate L420). The JP loads (Noto Sans JP and Noto Serif JP, candidate L428–429) and the stack alignment behind them are the FIX5 fix, re-derived in the per-theme record. The :root stacks (candidate L440–456) name the loaded JP faces as the CJK fallbacks in every font variable (the classifier's CSS-BODY blocks B124–B127 are these P7 stack rewrites, narrated here as that class); four stacks also keep 'Noto Sans Mono CJK JP' behind the loaded Noto Sans JP, which is a system-font name in that position (the basalt-jp precedent) and needs no load. Assets: the FIIC logo (fiic-logo-wash.png) is re-hosted to the candidate's draft-host attachments in both its occurrences (candidate L20, L436; class (ii) posting form).
- **Why:** KB-17 for the font hosts, P5 for the asset re-hosting, P7/T5 and KB-16 for the JP loads (a named face with no load is the defect item 34 charged; section 12 and the per-theme record carry its closure).
- **Verify:** `grep -n '@import' original.txt candidate.txt`; read the stacks at candidate L440–456.
- **Disposition:** DISPOSITIONED (class (ii)) for the re-hosted assets; the font-host swap and the JP loads are standing fixes, recorded above.

### 5. Header, sidebar, and site furniture

- **What:** The header variables keep the original's values: `--logo-image` re-hosted (candidate L436, block B123 HEADERVAR), `--header-title: "FIIC"` and `--header-subtitle: " "` byte-identical (candidate L437–438 = original L427–428). "FIIC" is the theme's fictional agency mark, an identity string. The theme-squares exhibit at the head of the body carries the palette with its color names translated (candidate L45 onward).
- **Why:** P9/T6 for the variables; ruling 2 for the retained identity strings (header and title language is translation taste, out of scope for migration correctness).
- **Verify:** `grep -n 'header-title\|logo-image' original.txt candidate.txt`.
- **Disposition:** DISPOSITIONED (ruling 2) for the retained strings; the logo re-host is class (ii).

### 6. Text translation

- **What:** The documentation body is translated throughout: the introduction, the theme-colors section, the div-exhibit documentation (the "uses X div" lines), the sample records and logs (including the `**> RECORDING STARTED <**` strings and SPEAKER labels), the tabview content, and the usage prose. In-CSS text (R1) is stated separately: the stylesheet banner is translated (candidate L415–419: "Twin Filesテーマ / [2022年Wikidotテーマ] / JackalRelated作"), and the CSS color comments are translated in place (blocks B128–B133: /* WHITE - GREY */ → /* 白 - 灰色 */ and siblings; B146: /* MAIN CONTENT */ → /* 本文領域 */). CSS comments are porter-visible only. The classifier's mass over this body is 39 TRANSLATION-ANCHORED blocks, 69 TRANS-UNANCHORED blocks, 9 COMMENT-TEXT blocks, and 21 residue blocks; the residue is adjudicated by shape in the appendix (every one is a one-line documentation translation or a CSS comment translation).
- **Why:** P10 for the body and the exhibits; KB-18 for reader-visible strings, including the recording-log strings inside the samples. Comment translation is not a defect class (NEGATIVE-LEDGER shape) and is disclosed so it is not mistaken for untranslated residue.
- **Verify:** Read candidate L36–413 against original L29–406 section by section; the exhibit sequence aligns one-to-one.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** No prose link in the candidate targets a dead page: the body's links are the component and include references of section 2, the credit block's source link back to the EN original (candidate L32), and exhibit content carried from the original (the sample correspondence and log exhibits, whose addresses are fictional in both files). No link item was charged against this theme at any stage.
- **Why:** P11's deciding check is the target census; there is nothing to repoint.
- **Verify:** `grep -n '\[\[\[' candidate.txt` and check each target against the repo's page list.
- **Disposition:** Standing; no open link item in this file.

### 8. Structure

- **What:** No structural change. The topology pass finds no relocation (10 delivery components on each side, matched by kind and order), the channel order of the original is preserved (head frames, body exhibits in sequence, stylesheet block, tail delivery), and brace depth measured over both whole files ends at 0 with no negative excursion on either side. The classifier's five EXHIBIT-RESTRUCTURE labels (B3, B5, B12, B157, B159) are false-fires on include repoints inside frame and exhibit lines: the exhibit census finds every exhibit present against its original (theme-squares, the div samples, the logs, the post-it exhibit, the code exhibits), and the label's own blocks show only the include lines changing. Two single-line CSS corrections inside the stylesheet are repairs of original defects, recorded in the per-theme record (an undefined variable reference at candidate L688 and an invalid color value at candidate L715).
- **Why:** The localize.md closing rule (structure, variable names, selectors, channel order preserved) is this port's discipline; R3 requires the ground for any dropped or replaced exhibit, and there are none.
- **Verify:** Compare the structural maps: `grep -n` for `[[module`, `[[code`, `[[tabview`, `[[include` in both files.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** Seven whitespace-only blocks (the classifier's WS-ONLY labels), blank-line adjustments at exhibit boundaries; 0 re-indentation blocks. Nothing else in the 160 blocks is formatting-only; the diff's size is translation.
- **Why:** Formatting-only churn is disclosed as its own class so a reviewer can skip it; at this size it carries no follow-up-diff hazard (the R7 rule is not triggered).
- **Verify:** The WS-ONLY labels in classification.json, with their ranges.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation stands in the candidate: the comment above the JP font loads (candidate L427: "JP 字形: 読み込んだ Noto Sans JP / Noto Serif JP を各フォントスタックのフォールバックとして指定する"), added by FIX5-FONTSB as part of item 34's fix, stating that the loaded JP faces are specified as fallbacks in each font stack. The translated stylesheet banner (candidate L415–418) is a translation of the original's banner, not an addition, and is counted in section 6. There are no `[!-- --]` note blocks in this file.
- **Why:** R2 (porter annotation additions): annotations are part of the change record, and this one is the in-file pointer to the fix a future editor must not undo.
- **Verify:** Read candidate L427 and the fix commit (`git show 3911f7b -- pages/theme:twin-files-jp.txt`).
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme: (1) the render-row dispositions (ledger §(c2), RENDER-ROWS-2 (RENDER-S2-D (EN22))): the runtime-hotlink site-theme chain (environment layer, KB-40), the credit-modal preview form (ruling 5; KB-32), and the page-overflow figures (337–419px at 320/375) in the recorded cross-cutting families (KB-33/KB-34); (2) the T1 standing classes (register c1): 12 pseudo-ref errors, the draft-host and own-host delivery lines (class (iii)/(ii)); (3) the retained header identity strings under ruling 2 (section 5); (4) the earlier register disposition of the /1 delivery address, superseded by the 4176cc7 repair and recorded in section 3 so the sequence is auditable. No item for this theme is left as an unexplained exception, and no open flag stands.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the campaign checker baseline for this file is 12 errors / 1 warning / 1 info (all 12 errors pseudo-ref), the standing delivery classes; (b) the supplement's re-judgment of item 34 is re-derived below from the package's bytes and from the fix commit's diff, both of which are in this repo; (c) render checks T2/T3 produced dispositions only, no open finding (ledger §(c2)); (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +217/−207 across 160 blocks. The classifier's adjudication: 68 specific blocks, 71 heuristic, 21 residue, all resolved by shape in the appendix.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:twin-files-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement); no open flags.

## Per-theme record

### The FIX5 closure (ledger item 34), re-derived

At ledger time this candidate carried one blocking defect (ledger §(e) item 34 [D], LOCALIZE-S2-C checklist item 8, pattern 7): its font stacks named JP faces (Noto Sans JP in the body/header/title stacks, Noto Serif JP in the manila-body stack) but no @import or @font-face anywhere in the file loaded a JP face, so the named fallbacks could never render. The ledger register is explicit that the theme's separate local--code /1 item was dispositioned elsewhere and does not cover this one. FIX5-FONTSB (commit 3911f7b) is the fix, and its diff is verifiable in this repo: it adds the porter comment and the two Google Fonts loads (Noto Sans JP wght 400;700 and Noto Serif JP wght 400;700, candidate L427–429) immediately after the Arimo import, and it inserts 'Noto Sans JP' ahead of 'Noto Sans Mono CJK JP' in the stacks that had named only the system face. Re-derived from this package's bytes: the loads stand at candidate L428–429, and every font variable in the :root block names a loaded JP face as its CJK fallback (candidate L440–456: body, header, title, mono, manila-tabs, manila-body, ticker, printer-paper, windows, logs-header, logs-text, logs-dialogue, logs-action). The closure holds exactly as the supplement states it, and the pre-fix state is recoverable from the commit's parent for any reviewer who wants the before picture.

### Two original defects the port repaired in passing

Recorded for the EN-author report file; neither was charged by the ledger, and neither is a defect of the candidate. (1) Original L678: `--dropdown-links-hover-color: var(---printer-paper)` references a variable named `---printer-paper` that is defined nowhere in the file (the definition census finds `--printer-paper:` exactly once, at the :root), so the declaration could never take effect; the candidate reads `var(--printer-paper)` (candidate L688). (2) Original L705: `background: #transparent` is an invalid color value; the candidate reads `background: transparent` (candidate L715). Both are single-token corrections inside otherwise carried CSS (classifier blocks B140 and B144, CSS-BODY), and both preserve the original's evident intent.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-twin-files-jp.txt` — the decoration sample page used by the render checks. (2) The delivery itself: the local--code code block served from the draft host (theme /8), which is the runtime form of the candidate's stylesheet block. No companion fragment belongs to this theme.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave (lane-oc-en22 integration, commit 6fa35a9) produced the initial port (translation, delivery repoints, font-host swap); FIX2-CREDIT (commit 666f543) completed the credit block's missing fields; FIX5-FONTSB (commit 3911f7b) repaired item 34's font loads; and the codeaddr landing (commit 4176cc7) repaired the self-delivery address after the verdict. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2) (render row), §(c3) (localize row), §(e) item 34 and the register note on the delivery item; GOSIGN2-LEDGER-SUPPLEMENT.md item 34; REPORT-GOSIGN2-FIX5-FONTSB.md; R/review-scout/FIX-CODEADDR.md. The go-sign re-run over that record is what the Status block certifies.

## Appendix — residue and heuristic blocks, adjudicated by shape

- **One-line documentation translations (14 blocks: B25, B60, B62, B68, B73, B78, B81, B90, B92, B95, B99, B101, B106, B112):** single prose lines of the exhibit documentation (section headings such as "+ Examples" → "+ 例", the "uses X div" lines, the sample logs' speaker and recording lines) that the classifier left unlabeled because a one-line block carries no anchor majority. All are P10 translation, assigned to section 6.
- **CSS comment translations (7 blocks: B128–B133, B146):** the stylesheet's color-group comments and section comments translated in place (R1, porter-visible only). Assigned to section 6.
- **CSS-BODY heuristic blocks (B124–B127, B140, B144):** B124–B127 are the P7 font-stack rewrites in the :root (narrated as that class in section 4, per the settled rule that font-family rewrites are P7 even when the classifier labels them CSS-BODY); B140 and B144 are the two original-defect repairs in the per-theme record.
- **EXHIBIT-RESTRUCTURE labels (B3, B5, B12, B157, B159):** false-fires on include repoints inside frame and exhibit lines, adjudicated in section 8 against the exhibit census; no exhibit was dropped or replaced.
- **Heuristic TRANS-UNANCHORED / COMMENT-TEXT mass (the remaining heuristic blocks):** the documentation translation and the CSS comment translations at block granularity; resolved as sections 6's mass.
- **Skeleton "none" sections:** the skeleton's per-section listing follows primary labels only; the sections above are written from classification.json's label_spans (JPFONT-LOAD and FONT-IMPORT fire inside B122, HEADERVAR inside B123, SELF-DELIVERY inside B158/B160), per the settled format.

## License and attribution

- **Title:** Twin Files Theme
- **Author:** JackalRelated
- **Source:** https://scp-wiki.wikidot.com/theme:twin-files — revision 32
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
