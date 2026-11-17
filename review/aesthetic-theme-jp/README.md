# Review package — theme:aesthetic-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:aesthetic-theme-jp — origin EN, population #1 [GOSIGN2-LEDGER (b) row 1]
- Overall: PASS — passed at the ledger determination; no OPEN items [GOSIGN2-LEDGER (b) row 1]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 3 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 1; GOSIGN2-LEDGER (b) row 1]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow at 320/375 (337–419px), TOC highlight staircase overlap, mobile preview-notice left-clip, sample credit-modal (shared showcase); runtime-hotlink site-theme chain. [RENDER-ROWS-1 (RENDER-A row 1)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 1)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 2, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 2]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 1]
- Computed against: canonical commit 443c60879a7c53fa5dfe6e5fc9f72e8785196d05; candidate file pages/theme:aesthetic-theme-jp.txt sha256:105e4df70db270cee3754839338f6bab30dbcfcc4967e502b8f9efbea9a92c09; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 1) |
| Wave history | Three commits touch the candidate: the canonical import (d727e92), the live-pair reconcile (ffad285), and FIX4-REPOINT (443c608: the JP font supplement). The candidate's body is older than the campaign: it descends from the production SCP-JP page (human translation, 2024). Section 0 and the per-theme record separate the layers |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×3 (class (iii), section 11); the render row's four items (KB-33/KB-34 families and the KB-40 environment chain); the EN header variables (ruling 2). No defect flag is raised against this candidate; two provenance observations are recorded (the production-adoption route is unmarked in sources.tsv; the credit link's bracket form differs from the campaign's other candidates) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:aesthetic-theme | theme:aesthetic-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 68 (created 2022-09-28 17:32:25 UTC; the candidate's credit block records 初訳時参照リビジョン: 68) | — |
| Source of this copy | Campaign fetch regeneration `review-mirrors/regens/orig-aesthetic-theme-rev68.txt` (class FETCH-REGEN: the mirror was regenerated from the live page and hash-verified against review/sources.tsv), via the mirror store | Canonical file `pages/theme:aesthetic-theme-jp.txt`, copied at worktree HEAD 1605bbd; the file's last content change is commit 443c608 (FIX4-REPOINT) |
| Lines / bytes | 866 lines / 27,817 bytes | 906 lines / 30,592 bytes (the generator's line count; `wc -l` reports 905 because of the final line's newline state) |
| SHA-256 | ac50f66db2a09788d55e0e010d899f5b35d648442c5c4bf93e71fa6 | 105e4df70db270cee3754839338f6bab30dbcfcc4967e502b8f9efbea9a92c09 |

The candidate's real ancestor is neither the mirror nor a campaign translation: it is the production page `pages-existing/existing:theme-aesthetic-theme.txt`, to which the candidate is 0.981 similar (SequenceMatcher ratio over full texts), against 0.454 similarity to the EN original. review/sources.tsv records the fact in its notes ("production page theme:aesthetic-theme exists; no phase17 diff page (TSV exist: 一致)") but classifies the row as a standard kind; the per-theme record (item 1) flags that gap. The mirror remains the diff baseline, as sources.tsv fixes it — which means most of this package's diff measures the 2024 production localization, not campaign work. The sections below keep the layers separate.

## Summary

Aesthetic is a Black Highlighter theme: a gated page whose head module imports the BHL stylesheets, whose body is a long sequence of translated exhibits (component squares, headings, quotes, code blocks, tables), and whose `:root` variable block sits in a `[[code]]` exhibit. The candidate is that page as SCP-JP already had it: the production JP localization (translator nebula2700, 2024), imported into the canonical repo (d727e92), reconciled to the live pair state (ffad285, "Reconcile 15 theme pages to the live pair state"), and then touched once by the campaign's waves: FIX4-REPOINT (443c608) added the Noto Sans JP import and the two JP stack supplements, which is the landing commit of the ledger's "P7 FIXED (font wave)" for this row. On top of the production text the candidate also carries three appended tail correction modules that the production page does not have (verified by probe, per-theme record item 2) and one escaped exhibit module where production carries the bare form. Measured churn against the EN original (diff.md, the generator's difflib count with autojunk off: +505/−465 in 159 classifier change blocks, Tier 2; a GNU-diff count gives +535/−495). Of that mass, 94 blocks are whitespace-only (the production file's tab-to-space conversion, section 9) and 40 are translation pairs (the 2024 localization, section 6); the campaign's own edits are a handful of blocks, and this README names them individually rather than letting the totals speak.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 159 change blocks — 138 specific (86.8%), 19 heuristic (11.9%), 2 residue (1.3%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| WS-ONLY | 94 |
| TRANS-UNANCHORED | 20 |
| TRANSLATION-ANCHORED | 20 |
| INCLUDE-REPOINT | 6 |
| DELIVERY-HOST | 5 |
| EXHIBIT-RESTRUCTURE | 5 |
| T7-CREDIT-CSS | 5 |
| DRAFT-HOST | 4 |
| CSS-BODY | 2 |
| HEADERVAR | 2 |
| SELF-DELIVERY | 2 |
| ASSET-REHOST | 1 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every non-formatting block was read against the bytes; the 94 WS-ONLY blocks were verified as a class, section 9): the five T7-CREDIT-CSS primaries split — four (B122, B124, B126, B146) are false fires over whitespace-drifted inherited CSS inside the body (B122 spot-checked: `#main-content` rules, not credit CSS), and one (B159) is genuine T7-family content in the appended tail modules (section 1). The five EXHIBIT-RESTRUCTURE primaries adjudicate in section 8 (head-zone alignment drift and the credit zone; the exhibit census shows no restructuring). The two CSS-BODY blocks are the typeface replacement (B54, a P7-family font rewrite in the production layer) and the mountains-mask re-host with its whitespace shift (B88). The two residue blocks are B16 (a heading translation, section 6) and B154 (the escaped `[[footnoteblock]]` exhibit, per-theme record item 2). The 19 heuristic blocks are font-stack and delivery pairings inside the production layer, each narrated in its section. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:aesthetic-theme-jp; original theme:aesthetic-theme on scp-wiki at reference revision 68; candidate `pages/theme:aesthetic-theme-jp.txt`. Provenance route: **R4, production-derived** — the candidate's body is the production SCP-JP page's text (a human localization credited to nebula2700, 2024), imported at d727e92 and reconciled to the live pair state at ffad285; the campaign did not translate this theme. The frame order reflects the theme family: an ungated head include of the BHL base (candidate L1–3, section 2), then the `+テーマ` gate whose module carries the BHL imports, and the credit block inside the gate (L38–47). review/sources.tsv classifies the row as a standard kind with the production fact in its notes only.
- **Why:** Section 0 exists to declare the route before any count is read: against this baseline, a "change" is usually the production localization, and the campaign's edits must be picked out by commit, which the later sections do.
- **Verify:** The sources.tsv row for aesthetic-theme-jp; `sha256sum original.txt` against the Provenance table; the similarity figures reproduce with any SequenceMatcher run over `pages-existing/existing:theme-aesthetic-theme.txt`, candidate.txt, and original.txt.
- **Disposition:** Standing (the route itself); the unmarked-kind observation is in the per-theme record.

### 1. Credit and attribution

- **What:** The original's credit furniture is a centered bare Rate (`[[=]] [[module Rate]] [[/=]]`, deleted — block B8) and no credit block. The candidate carries the JP preview credit block (candidate L38–47) with the eight ruling-3 fields, in the production page's form: title 美的テーマ; 翻訳責任者 **nebula2700** (a human name, kept under ruling 3's exception for names matching the live JP creator — this block is the production page's own credit, carried in, not a campaign normalization target); 翻訳年 2024; 原題 Aesthetic Theme; 著作権者 Esteban Vargas, Inconsistent Doom; 作成年 2022; 初訳時参照リビジョン 68; the source link (section 7, form noted there). T7 in this theme is not a carried supplement: the candidate's tail appends three correction modules after the gate (candidate L893–906), one of which is credit CSS — the BHL credit otherwise-dialog back-link rule (`[id*=u-credit] div.credit-back a{white-space:nowrap;flex-shrink:0}`, candidate L900) under an English porter comment. The production page does not carry these modules (probe, per-theme record item 2), so this supplement's source is the campaign-side composition itself, not a production counterpart — the reverse direction from the 3law themes in this batch, and recorded as such.
- **Why:** P3/T1 (the preview credit module is rate-bearing, so the bare Rate is deleted, KB-09); ruling 3 for the fields, with its human-name exception doing real work here. T7 (KB-11): the JP credit module's DOM needs rules the branch original never shipped; where the fix is a small appended correction rather than a carried block, it lands as a tail module with its reason in a comment (R2).
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L38–47 against the eight fields; read candidate L893–906 for the three appended modules and their comments.
- **Disposition:** Standing (production credit carried; the campaign did not re-credit this theme). No license box exists on either side, so the T4/KB-63 question does not arise.

### 2. Includes and components

- **What:** The candidate's includes: the ungated head include of the BHL base on its production JP name (`[[include :scp-jp:theme:black-highlighter-theme]]`, candidate L1–3, inside its own iftags), the credit pair (L38/L47), the theme-squares include (L53, its color names Bossanova / Golden Fizz kept in English as design tokens), and at the tail the BHL furniture components repointed to `:scp-jp:` (toggle-sidebar-bhl, centered-header-bhl). The original's corresponding includes name `:scp-wiki:` (its BHL base and furniture); the classifier's six INCLUDE-REPOINT blocks are these repoints. The usage exhibits are escaped and repointed (candidate L105–106): `@@[[include :scp-jp:theme:black-highlighter-theme]]@@` and `@@[[include :scp-jp:theme:aesthetic-theme]]@@` — the second names the production page's name (theme:aesthetic-theme), not the candidate's own -jp name, because the exhibit documents the production usage form; recorded here as a fact a poster must notice, not as a defect (the exhibit is escaped text, and the production form is what a JP author copying it would use on the production wiki).
- **Why:** P1 (KB-15): includes name the JP counterpart that exists; for a production-derived candidate the counterpart is the production page itself. The escaped exhibits are documentation, governed by accuracy to the usage they teach.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include is `:scp-jp:`; read L105–106 for the escaped pair.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The head module (inside the gate) imports the BHL stylesheets from the JP distribution host: `scp-jp.github.io/Black-Highlighter/css/min/normalize.min.css` and `black-highlighter.min.css` (candidate L7–8), where the original imports the same files from `nu-scptheme.github.io` — the T9 JP-distribution repoint, production-layer. The interwiki-style includes at priorities 1 and 2 (candidate L29–36) name the same scp-jp.github.io URLs (the original names the nu-scptheme URLs through `:scp-wiki:` includes). At the tail, the candidate delivers its own code: a `[[module CSS]]` @import of its own `local--code/theme%3Aaesthetic-theme-jp/1` on the draft host (candidate L886) and an interwiki-style frame at priority 3 naming the same (L890) — the classifier's DRAFT-HOST and SELF-DELIVERY blocks. The original's tail names its own /1 on scp-wiki.wdfiles.com; the production page names scp-jp.wdfiles.com. The five DELIVERY-HOST blocks are the github.io distribution moves.
- **Why:** P4/T9 (delivery from JP-side hosts; the BHL JP distribution is the canonical JP form of the base) and P6/T3 (the frame at the tail priority this theme family uses). The draft-host own-code lines are KB-41, class (iii), rewritten to the production host at posting.
- **Verify:** `grep -n 'github.io\|local--code' candidate.txt` — the distribution imports and the two draft-host delivery lines; compare original L10–14 and its tail.
- **Disposition:** DISPOSITIONED (the draft-host delivery lines, class (iii)); the distribution repoint is applied and standing.

### 4. Fonts and assets

- **What:** Fonts, in three layers. (a) Production layer: the original's Typekit faces (prenton, flood-std, eurostile-extended) are replaced in the candidate's variable block by "Open Sans" / "Permanent Marker" (display) and "Yusei Magic" / "Orbitron" (title) — block B54, a P7-family typeface rewrite from the 2024 localization — and the loads sit at the code exhibit's head (candidate L204–208: Google Fonts @imports for Permanent Marker, Yusei Magic, Orbitron, Open Sans). (b) Campaign layer: FIX4-REPOINT (443c608) added the Noto Sans JP @import at the module head and `"Noto Sans JP"` to the `--body-font` stack (candidate L228) and the `--title-font` stack (L230) — the ledger §(c3) line's "P7 FIXED (font wave)", landed by the FIX4 commit. (c) The LOCALIZE row's pattern-7 charge (no JP font) predates both supplements and is closed by (b). Assets: the logo variable is re-hosted to the production storage form (`scp-jp-storage.wdfiles.com/local--files/file%3A8260379-57-rycj/AESTHETIC_logo.svg`, block B53) — production form, not the draft form; the mountains-mask SVG is re-hosted from the author's own host (elusionillusion.com) to `scp-jp.github.io/files/theme/aesthetic-theme/AESTHETIC_mtns_vs2.svg` (block B88). The T1 checker's three pseudo-ref errors attach to this file's draft-host lines (the delivery pair at candidate L886/L890 and the draft-host image exhibits at L88/L97 on sigma10-jp-test.wdfiles.com) — four lines carry the draft host and the checker counts three errors; this package does not force a one-to-one mapping the checker output does not state.
- **Why:** P7/T5 with KB-16 for the JP supplement; the typeface replacement is the production localization's own font decision, inherited. P5 with KB-17 for the re-hosts (JP-side and production-storage hosts are the allowed forms). The draft-host lines are class (iii) / KB-41.
- **Verify:** `git show 443c608 -- pages/theme:aesthetic-theme-jp.txt` reproduces layer (b) exactly (the import plus the two stack lines); `grep -n 'typekit\|prenton' candidate.txt` returns nothing.
- **Disposition:** Font supplement applied (443c608); the draft-host lines DISPOSITIONED (class (iii)).

### 5. Header, sidebar, and site furniture

- **What:** The candidate's variable block ADDS two header variables the original's block does not carry: `--header-title: "SCP FOUNDATION"` and `--header-subtitle: "Secure, Contain, Protect"` (candidate L221–222, the classifier's HEADERVAR blocks) — they make the BHL base's defaults explicit in the theme's own block, in English. This is the LOCALIZE row's pattern-9 charge (the EN header overriding the JP BHL defaults). The render row's items: page overflow at 320/375 (337–419px), a TOC highlight staircase overlap, a mobile preview-notice left-clip, and the sample credit-modal item (the shared showcase property) — all dispositioned in the render record; plus the runtime-hotlink site-theme chain item, which is the environment layer's, not this file's (KB-40).
- **Why:** Header language is dispositioned under ruling 2 per the ledger §(c3) outcome for this row ("P9 DISPOSITIONED (ruling 2)"), and the explicit-variables form changes no rendered text: the values are the base's own defaults. The render items are the narrow-width clip/collision and modal families (KB-33/KB-34); the credit-modal item on a preview-module page is ruling 5's preview-form property, not a theme defect.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — the two lines at L221–222; the render record is RENDER-ROWS-1 (RENDER-A row 1).
- **Disposition:** DISPOSITIONED (ruling 2 for the header variables; the render families for the render items).

### 6. Text translation

- **What:** The body exhibits are translated throughout: 40 translation blocks (20 TRANSLATION-ANCHORED + 20 TRANS-UNANCHORED pairs) covering the component squares, headings, quotes, code exhibits, and tables. This translation is the production page's 2024 human work, inherited by the candidate — the campaign translated nothing in this file, and the package says so rather than letting the block counts imply campaign authorship. Two small blocks adjudicate individually: B16 (residue) is a heading translation ("+ Examples" → "+ 例"), and B47 (heuristic) is a blockquote exhibit translation; both are pattern-10 reader-visible text, whose ledger outcome for this row is DISPOSITIONED at the lane-recorded severity (the specimen class), not a defect. The theme-squares color names stay in English (section 2) as design tokens.
- **Why:** P10 for the prose and exhibits; KB-18 for reader-visible strings. The T5 half of the LOCALIZE row is pattern 10, closed by the §(c3) line as "P10 DISPOSITIONED (lane-recorded severity / specimen class)".
- **Verify:** The translation pairs are diff.md's body; the credit block (candidate L40) names the translator and year.
- **Disposition:** Standing (inherited localization); pattern 10 DISPOSITIONED as recorded.

### 7. Links

- **What:** The candidate's credit source link (candidate L46) reads `[https://scp-wiki.wikidot.com/theme:aesthetic-theme ソース]` — the single-bracket link form, where the other four candidates in this batch use the `[*…]` star form. Its host is the original's recorded host in review/sources.tsv (scp-wiki.wikidot.com), so no jiha-class defect arises and no probe was needed; the bracket form is the production page's own form, carried in. Recorded as a form observation: if a future normalization pass unifies credit-link forms, this file is one of the ones it will touch. The body's prose links are the translation's, counted in section 6; the CSS file URLs are sections 3 and 4.
- **Why:** P11, under the dead-reference evidence standard; form consistency across candidates is a campaign-style question, not a link-correctness one.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the storage-host asset lines.
- **Disposition:** Standing; the form difference is recorded, not hidden.

### 8. Structure

- **What:** The localize.md closing rule holds: the CSS body's names, selectors, and order are preserved through both layers (the long unchanged runs are diff.md's context), and corrections arrive as appended modules or declared supplements. The exhibit census decides the EXHIBIT-RESTRUCTURE question: the original's exhibits (the `[[code]]` variable block, the component and typography exhibits, the tail exhibits) are all present in the candidate, translated; the candidate is longer than the original (906 vs 866 lines), and its deletions are the centered Rate (section 1), the nu-scptheme delivery lines (section 3), and prose lines replaced by their translations. The five EXHIBIT-RESTRUCTURE primaries are the head module's image-block region (B3/B5, alignment drift across the production layer's edits) and the credit zone — label artefacts against this census, with one exception already counted: none. No silent drop was found in this file, which is the R3 statement for this theme.
- **Why:** R3 forces the census because a restructure and a deletion share a diff shape; here the census, not the label, decides, and it decides clean.
- **Verify:** Compare the exhibit markers: `grep -c '\[\[code' original.txt candidate.txt` and the section headings on both sides.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** This is the package's headline formatting fact: 94 WS-ONLY blocks, the largest single class in the diff. The original's `:root` swatch block (and the variable block generally) is indented with a 4-space-plus-tab mix; the production file converted the tabs to spaces, so whole runs of variable lines pair up as whitespace-only changes with their values byte-identical after indentation. The classifier's reindent count is 0 because its WS-ONLY signature already absorbs these pairs; either way, the values are unchanged and the churn is disclosed here so the +505/−465 totals are never read as semantic change. This is exactly the R7 hazard shape (a formatting conversion that makes every later diff noisy), inherited from the production layer and now frozen into both files of this package.
- **Why:** Formatting churn is disclosed as its own class; at 94 of 159 blocks it is the majority of this diff and the first thing a reviewer must know.
- **Verify:** Any WS-ONLY block in classification.json (e.g. the swatch run) — strip leading whitespace from both sides of the pair and the lines are identical.
- **Disposition:** None required (inherited, disclosed).

### 10. Porter annotations

- **What:** Three annotations, all in the appended tail modules (candidate L893–906), each an English comment stating the correction's reason: the history-form mobile-viewport fix (comment at L894), the BHL credit back-link nowrap (L899), and the top-bar label word-break (L904). They ride inside the tail's SELF-DELIVERY/T7 blocks, which is why no separate annotation signature fired. No other porter text exists in the candidate; the production layer's text carries no translator notes either.
- **Why:** R2: porter-added text is part of the change record, and these three comments are the only in-file statements of why the candidate differs from the production page at its tail.
- **Verify:** Read candidate L893–906.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Four items, each with its ground. (1) T1's three pseudo-ref errors: class (iii) — the draft-host lines (section 4), rewritten to production hosts at posting. (2) The render row's four items (overflow, TOC staircase, preview-notice clip, sample credit modal): DISPOSITIONED in the render record under the KB-33/KB-34 families and ruling 5's preview-form property; the row's runtime-hotlink chain item is the KB-40 environment layer. (3) The EN header variables: ruling 2, per the ledger §(c3) outcome. (4) Pattern-10 reader-visible text severity: DISPOSITIONED at the lane-recorded severity (specimen class), per the same §(c3) line.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries and rulings), not an omission.
- **Verify:** Each item names its deciding record above; the T1 lines are enumerable by the greps in sections 3 and 4.
- **Disposition:** DISPOSITIONED (all four items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 1): exit 1, 3 errors / 1 warn / 3 infos; all three errors are pseudo-ref, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-A row 1): FINDINGS, the items of section 11(2), all dispositioned; engine coverage the full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 2, lane LOCALIZE-A): FINDINGS jointly, display-affecting findings 3 (patterns 9, 7, 10); the ledger §(c3) line (ledger L1401) closes P7 FIXED (font wave — landed as 443c608, section 4), P9 DISPOSITIONED (ruling 2), P10 DISPOSITIONED (lane-recorded severity / specimen class). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +505/−465 in 159 change blocks, Tier 2; the GNU-diff count is +535/−495, and at this size the difference is alignment choice across the whitespace-converted regions, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:aesthetic-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 1; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — a candidate whose provenance the TSV does not mark

Three of this batch's five candidates were translated by the campaign from the mirror revision; this one was not. Its body is the production SCP-JP page (0.981 similar), reconciled to the live pair state, and its credit block names a human translator and the year 2024. review/sources.tsv knows this (its notes say so) but classifies the row with the standard kind used for campaign translations, so a reader of the TSV alone, or of the diff totals alone, will misread this package as a very free campaign translation (+505/−465) when it is in fact a near-copy of an existing JP page with a small campaign delta (one font commit, three appended modules, one escaped exhibit). The package declares the route in section 0; the record here proposes the TSV grow a marker for production-reconciled candidates, because the distinction decides how every other number in the package is read.

### Item 2 — where the candidate goes beyond production

The reconcile commit (ffad285) defines the candidate as the live pair state, so candidate/production differences after it are the interesting ones. Two were verified by direct comparison and probe. (a) The three appended tail modules (candidate L893–906: history-form viewport, credit back-link, top-bar word-break) do not exist in the production page: searching the production text for their signatures (`history-form-1`, `u-credit`, `word-break:keep-all`) returns nothing, while all three are present in the candidate. They are campaign-side corrections carried only by the candidate. (b) The footnoteblock exhibit: production carries `[[footnoteblock]]` bare (production L880); the candidate escapes it as `@@[[footnoteblock]]@@` (candidate L881, the classifier's residue block B154) — the KB-59 footnoteblock-exhibit family, where the bare form inside a theme page's documentation zone acts as a live module instead of displaying as text. The candidate's form is the correct exhibit form; the difference is recorded because it is a candidate/production divergence a reviewer comparing the pair will meet.

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages-existing/existing:theme-aesthetic-theme.txt` is the production counterpart and this candidate's actual ancestor (section 0) — a record source, not a port output. `pages/theme-decoration-sample-aesthetic-theme-jp.txt` is the decoration sample the render checks ran against. The BHL base the candidate includes is the production page `theme:black-highlighter-theme` on scp-jp (section 2), not a campaign candidate file. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
