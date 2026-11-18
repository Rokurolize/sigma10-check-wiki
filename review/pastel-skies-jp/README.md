# Review package — theme:pastel-skies-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:pastel-skies-jp — origin EN, population #122 [GOSIGN2-LEDGER (b) row 122]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now de2424bca53f5c57eae01915fdf0406ae1f3b3121a35546b16c534eedda09500); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 1 warn / 1 info (pseudo-ref×11); standing classes dispositioned in register c1 [T1-ROWS row 157; GOSIGN2-LEDGER (b) row 122]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 467–478px@320/375 + 792–803px@768 (page) and 479–490px@320/375 + 953px@768 (sample); T3 overflow visually confirmed as content extending past the pastel frame; sample credit-modal (preview-form); broken logo deferred. [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN16))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 122, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 122]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 122]
- Computed against: canonical commit a2bd1fb983b56a82b69d82c9350a628c2e32197d; candidate file pages/theme:pastel-skies-jp.txt sha256:de2424bca53f5c57eae01915fdf0406ae1f3b3121a35546b16c534eedda09500; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; no OPEN items (GOSIGN2-LEDGER (b) row 122) |
| Standing items | **DISPOSITIONED** — the P9 inlined-base header defaults (ruling 2; sections 5, 11); T1 pseudo-ref ×11 (classes (ii)/(iii), section 11). **Recorded topology** — the candidate carries its Sigma+ base inline where the original includes it (per-theme record, with the campaign's sanction ground). **FLAGGED by this package** — the usage exhibit names the plain slug on the JP side; 'Noto Sans JP' is named in four stacks and the credit font field but loaded nowhere in the file (per-theme record) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:pastel-skies | theme:pastel-skies-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 15 (first translation; the candidate's credit block records 初訳時参照リビジョン: 15) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-pastel-skies.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:pastel-skies-jp.txt`, copied at worktree HEAD 9068bb7 |
| Lines / bytes | 1,499 lines / 42,951 bytes | 2,202 lines / 63,748 bytes |
| SHA-256 | 09f2ecec8e30d33afc4ee8df02d9a5bfae8dcbbf6e1b3e07c34ad47c9ee3 | edad5b97b4df10b7527c2a716d9c00b3eefbbd3454907e7ce44deed76ee9d012 |

Wave history: the candidate was created by the Stage 2 EN16 integration (commit 88d2d99, the LOCALIZE-S2-B wave's port, lane-dsh-en16) and has exactly one later commit, 1869877 (FIX-CREDIT-D), whose pastel-skies hunk is the translator-field normalization. No FIX5 commit touches this file. (The verdict stamp cites T1-ROWS row 157 for the T1 baseline; the theme's population number is 122. The offset is the register's own, recorded here so the citation can be followed.)

## Summary

A Sigma+-based aesthetic theme, and the batch's largest file growth (+703 lines), for one declared reason: the theme's base, EN's component:sigma-plus, is not posted on scp-jp, so the candidate carries the base's CSS inline in its first code file, with the base's author credited in the credit block and the carry explained in the file's own prose. The campaign's records name this exact carry as the sanctioned form for the absent component (the fandom row of the same register prescribes "carry the CSS inline as pastel-skies did"), and the per-theme record below sets out the topology with its evidence rather than narrating it as a routine supplement. Everything else is the standing set at larger scale: the info-module credit zone (both its rated and standalone demonstrations) becomes the preview credit block, extended with two extra fields (the font list and the base credit); the original's three cross-theme font stylesheets are replaced one-for-one by loaded Google Fonts faces with the mapping written into a CSS comment; the delivery splits over two code files as the original's did, both on the draft host; and the body is translated throughout. Two mechanical notes belong in this summary because a skim would miss them: the pair's 121 whitespace-only blocks are the carried CSS's whitespace normalization (section 9), and a brace-depth scan ends at +1 on both files, in the theme's own stylesheet on both sides — carried, not introduced (section 8). Measured churn against the current (post-repair) candidate (diff.md, the generator's difflib count with autojunk off: +992/−288 in 221 change blocks / 56 diff sections; GNU-diff 1288 changed lines). The one added line against the pre-repair figure (+991/−288) is the font-load @import whose repair is recorded in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 221 change blocks — 164 specific (74.2%), 56 heuristic (25.3%), 1 residue (0.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| WS-ONLY | 121 |
| TRANS-UNANCHORED | 79 |
| TRANSLATION-ANCHORED | 24 |
| DRAFT-HOST | 7 |
| EXHIBIT-RESTRUCTURE | 6 |
| INFO-DEL | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| SIGMA-PLUS-JP | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the dominant block is B83 (original L241–242 → candidate L255–956), the inlined Sigma+ base CSS, whose primary is T7-CREDIT-CSS because the base ships the credit-button rules (candidate L679–757, the rate-box-with-credit-button family); it is treated as the base carry of section 3, not as a theme-authored credit supplement. B221 (original L1485–1499 → candidate at L2202) is the tail zone where the original's sigma-plus include stood; its SIGMA-PLUS-JP span is the include the inline carry replaces. The 121 WS-ONLY blocks are whitespace normalization across the carried CSS (section 9). The single residue block is a translation pairing in the sample text, resolved in the appendix. The 6 EXHIBIT-RESTRUCTURE labels adjudicate to the credit-zone replacement and the tail-zone replacement (sections 1, 3); the exhibit census of section 8 is otherwise one-to-one. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:pastel-skies-jp; original theme:pastel-skies on scp-wiki at reference revision 15; candidate `pages/theme:pastel-skies-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame order changed: the original opens with its tag gate and credit zone and delivers from the tail (original L1, L1491–1499); the candidate opens with the delivery set (the toggle-sidebar include, the frame, and the module CSS, candidate L1–11) and places the localized gate `[[iftags +テーマ]]` after it (candidate L13).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3 (section 3).
- **Verify:** The sources.tsv row for pastel-skies-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the delivery rebuild is section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is the info module in both its forms — `:scp-wiki:info:start` / `info:end` ("Rating with info module.", original L2–4) and `:scp-wiki:info:start-standalone` / `info:end-standalone` ("Info module without rating.", original L10–12) — with a right-floated bare `[[module Rate]]` between them (original L6–8) and the attribution in prose ("created by [[*user Miss Lapis]] and co-created by [[*user radian628]]", original L14). The candidate deletes both info pairs (INFO-DEL ×2) and the Rate, and installs the preview credit block (candidate L15–26) carrying the eight ruling-3 fields (title パステルスカイズテーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Pastel Skies Theme; 著作権者 [[*user Miss Lapis]]、[[*user radian628]] — both names, matching the prose; 作成年 2025; 初訳時参照リビジョン 15; the source link https://scp-wiki.wikidot.com/theme:pastel-skies, whose host matches the sources.tsv record) plus two theme-specific fields the ruling's form admits as additions: a **フォント** field listing the four Google Fonts faces and their license (SIL Open Font License), and a **基盤** field crediting the base ("Sigma+（[[*user EstrellaYoshte]]作、EN component:sigma-plus のCSSをインラインで同梱、CC BY-SA 3.0）") — the TASL record for the inlined base of section 3. The license zone at the tail takes the settled JP backend form (LICENSE-BOX). T7: the classifier's T7-CREDIT-CSS signature fires inside the inlined base block (B83), on the base's own credit-button rules (candidate L679–757); the theme itself adds no credit-module CSS of its own, and none was needed beyond what the base ships.
- **Why:** P3/T1 with KB-09 (the preview module is rate-bearing; the floated bare Rate goes with the zone). Ruling 3 fixes the eight fields and the translator form; the file's last commit (1869877) is that form arriving. The two added fields are attribution records (ruling 3's TASL standard applied to the fonts and the base), not decoration.
- **Verify:** `grep -n 'module Rate\|info:start' candidate.txt` returns nothing; read candidate L15–26 against the eight fields and the two additions.
- **Disposition:** FIXED by construction at creation (P3 credit fields; the base and font attribution recorded in the block itself).

### 2. Includes and components

- **What:** The toggle-sidebar the theme bundles is repointed and hoisted to the head (`:scp-jp:component:toggle-sidebar`, candidate L1), and the prose link to it is repointed with a translated label (candidate L34). The image-block exhibit keeps the original's bare `component:image-block` form with its asset re-hosted (candidate L38). The frame include keeps the original's bare `component:interwiki-style` form (candidate L3–6; its delivery aspect is section 3). The one include that leaves is the base itself: `:scp-wiki:component:sigma-plus` (original L1487, at the tail) has no JP counterpart to repoint to, and its replacement is the inline carry of section 3, recorded as topology in the per-theme record. The credit and license includes are section 1. No component swap (T8) was needed.
- **Why:** P1 (KB-15): includes name the JP counterpart that exists; where none exists, the campaign's prescribed form is the inline carry with attribution (section 3's ground), not a repoint to a page that is not there.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the full list; `grep -n 'sigma-plus' candidate.txt` — the credit field (L25), the prose link (L34), and the carry note (L258), but no include.
- **Disposition:** Applied; the base's form is the per-theme record's topology item.

### 3. Delivery and code loading

- **What:** The original delivers from its tail: a module CSS importing its own `local--code/theme%3Apastel-skies/1` (original L1491) alongside the sigma-plus include (original L1487) that pulls in the base. The candidate rebuilds delivery at the head with two code files, both on the draft host: the module CSS imports `local--code/theme%3Apastel-skies-jp/1` and `/2` (candidate L9–10), and the frame at priority 1 names `/2` as its `theme=` (candidate L3–6). The first code file carries the inlined Sigma+ base CSS (its exhibit block is candidate L255–956, introduced by the porter's prose at candidate L258: the base is incorporated into this page because it is not posted on JP), and the second carries the theme's own CSS (candidate L958–2165). The base's CSS is therefore delivered as part of the theme's own delivery instead of through a component include — the topology change the per-theme record sets out with its grounds. The theme's own asset URLs re-host to the draft folder (DRAFT-HOST loci, section 4). Both delivery lines are draft-host form, class (iii).
- **Why:** P4/T9 and P6/T3 for the head pair and the import forms; KB-41 for the draft lines. The base carry's ground is the campaign's own: component:sigma-plus is absent on scp-jp (a posting blocker wherever a theme includes it), and the register's prescribed alternatives are a JP port of the component or the inline carry "as pastel-skies did" (LOCALIZE-ROWS row 87, theme:fandom-jp).
- **Verify:** `grep -n 'local--code' candidate.txt` — L5, L9, L10; read candidate L255–260 for the carry's introduction.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)); the base topology is recorded below with its sanction ground.

### 4. Fonts and assets

- **What:** The original loads three font stylesheets out of other pages' file areas (original L264–266): vga8.css and terminus.css from theme:isolated-terminal's files, and departuremono.css from scp-8980's files — cross-theme @font-face deliveries defining 'mxplus_ibm_vga_8x16regular', 'terminus_ttfmedium', and 'Departure Mono', which the stacks name (original L273–276). The candidate replaces all three with Google Fonts loads (candidate L981–983: VT323; IBM Plex Mono; Sometype Mono) and rewrites the stacks one-for-one (candidate L990–993): --header-font and --title-font 'VT323', --body-font 'Sometype Mono', --UI-font 'IBM Plex Mono', each with 'Noto Sans JP' appended. The mapping and its reason are written into the file as a porter comment at the substitution point (candidate L977–979, section 10): the original sources are not among the hosts the JP environment keeps as direct-link exceptions, so they were replaced, with the family correspondence stated. One gap stands against this tidy picture and is flagged in the per-theme record: 'Noto Sans JP' is appended in all four stacks and listed in the credit block's font field, but no load for it exists anywhere in the candidate — the three loads at L981–983 are the only font loads in the file. Assets: the theme's own images (moon_icon.svg and the remaining url() targets) re-host to the draft host's `theme%3Apastel-skies-jp/` folder, filenames unchanged.
- **Why:** P5 (the cross-theme font CSS files are foreign deliveries the JP environment does not keep; Google Fonts is the kept host) and P7/T5 with KB-16 for the stacks — KB-16 being exactly the rule the flagged gap breaches in-file: a stack should not name a face nothing loads.
- **Verify:** `grep -n '@import' candidate.txt` — L9, L10, L981–983; `grep -n 'family=Noto' candidate.txt` returns nothing.
- **Disposition:** Applied for the substitutions; the Noto Sans JP load gap is flagged below (T4 did not charge it for this theme; its row's one finding is section 5's item).

### 5. Header, sidebar, and site furniture

- **What:** The theme's own header variable blanks the title text (`--header-title: "⠀⠀⠀"`, candidate L995 zone — a row of blank Braille cells, the theme's design), and its header and title font variables take the substituted faces (section 4). The dispositioned item lives deeper: the inlined base CSS carries the EN Sigma+ header defaults, and where the theme never overrides them they render as-is; T4 charged this as the theme's one display-affecting finding, "P9 (inlined EN header defaults never overridden, display-affecting)" (LOCALIZE-ROWS row 122), and the (c3) register dispositions the theme's P9 line under ruling 2. The sidebar component is section 2; no P8 layout adaptation was needed.
- **Why:** P9/T6 with ruling 2: the base's default strings are the base author's text, and header language is case-by-case translation taste, out of scope for migration correctness; the ledger recorded the choice and its display effect openly.
- **Verify:** LOCALIZE-ROWS row 122 states the finding in the words quoted above.
- **Disposition:** DISPOSITIONED (ruling 2; (c3) register, pastel-skies line).

### 6. Text translation

- **What:** The body is translated throughout: the usage prose, the collapsible samples, the ACS documentation, and the formatting examples, in 24 TRANSLATION-ANCHORED blocks and the TRANS-UNANCHORED grain (79 label counts, most riding inside the CSS-adjacent blocks), each verified against the mirror for this README. The prose link to the base is rewritten as well as translated: the original's bare `[[[component:sigma-plus|]]]` becomes a full-URL link to the EN component page with the label Sigma+ (candidate L34), because the component has no JP page to name. R1 in-CSS text: the CSS's section comments are largely carried as the base's and theme's structural labels; the translated comment mass is the porter's own substitution comment (section 10) and scattered one-line translations inside the theme's CSS, counted under COMMENT-TEXT's family in the label table's grain. No reader-visible string stays in English outside the credit block's original-title field, the section 5 defaults, and proper nouns.
- **Why:** P10 and KB-18 (reader-visible strings localize). The base link's form follows P11 (the serving original, since no JP counterpart exists).
- **Verify:** The pairs are diff.md's body sections in order; the base link is candidate L34.
- **Disposition:** Standing (the port itself); T4/T5 judged the theme FINDINGS with the one dispositioned item of section 5 (LOCALIZE-ROWS row 122).

### 7. Links

- **What:** One LINK-REPOINT block: the base link of section 6 (candidate L34). The credit block's source link (candidate L23) names the original on scp-wiki.wikidot.com, the host the campaign's provenance records name for it, and serves the original page. The license entries' source links are section 1's zone. No link in the candidate is dead on the evidence of the mirror; the render row's "broken logo" item is an asset delivery matter (the --lgurl image in the T3 capture, recorded as deferred), not a prose link.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard.
- **Verify:** `grep -n 'component:sigma-plus' candidate.txt` — L25 (credit field), L34 (the link), L258 (the carry note).
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds for the gated body: the exhibit census corresponds one to one (the usage exhibit, the image exhibit, the collapsible and formatting samples, the pre-styled ACS section, and the two CSS code exhibits), and the JP corrections arrive as the head delivery set, the credit swap, and the license-box form. Two structural facts are stated rather than absorbed. First, the head's standalone info-module demonstration (original L10–12) leaves with its zone: it demonstrated a foreign module form that does not render in the JP environment, and the credit block is the zone's replacement; the theme's info-module styling itself is carried in its CSS. Second, the brace balance: a naive depth scan of each whole file ends at +1 on both sides, and per-block the surplus sits in the theme's own stylesheet on both sides (the original's single code block carries delta +1; the candidate's second code block — the same CSS — carries +1, while its inlined base block is balanced at 0). The surplus is therefore the original's own (a brace character in a comment or string context in the carried CSS), not a brace displaced by the port; no rule boundary moved. The base topology change is section 3's item, recorded in the per-theme record.
- **Why:** R3: a restructure and a silent deletion share a diff shape; the census decides for the body, and the two stated items carry their grounds with them. The depth check is the campaign's standing structural probe: balance by depth, not by count, because a displaced brace keeps counts equal while swallowing rules.
- **Verify:** The per-block depth deltas are reproducible with any brace counter over the code blocks of original.txt (L244–1448) and candidate.txt (L255–956, L958–2165).
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** 121 WS-ONLY blocks — the batch's entire formatting mass sits in this one theme. The carried CSS (the theme's own stylesheet, whose original form carries trailing whitespace and mixed line endings of its author's editor) was whitespace-normalized as it was carried, so line after line pairs up as whitespace-only. The R7 consequence is real and is stated plainly: any follow-up diff of this candidate against the original will re-show this churn, and reviewers of future changes should diff with whitespace ignored first. No re-indentation blocks pair up (0), and no semantic change hides in the WS-ONLY set — each such block was confirmed whitespace-only by the classifier's own test (equality after whitespace stripping).
- **Why:** R7: formatting churn is disclosed as its own class with its count, so it is never mistaken for semantic change and its follow-up cost is on the record.
- **Verify:** The classification summary's WS-ONLY count is 121; `diff -w` between the two CSS exhibits collapses them.
- **Disposition:** Standing (disclosed, counted).

### 10. Porter annotations

- **What:** Two annotations, both substantive. (1) The prose note introducing the inlined base (candidate L258): "Sigma+（[[*user EstrellaYoshte]]作）のCSSをインラインで同梱しています。ENでは `component:sigma-plus` として提供されている基盤コンポーネントです。JPに未投稿のため、このページ内にそのまま組み込んでいます。" — the carry, its reason (not posted on JP), and its author, in the body where a reader meets the code. (2) The CSS comment at the font substitution (candidate L977–979), which names the original font sources with their authors (Isolated Terminal Theme by EstrellaYoshte; SCP-8980 by Yossipossi), states why they were replaced (not among the direct-link exception hosts), and gives the family correspondence one-for-one. The skeleton's "none" for this section does not survive contact with the bytes and is corrected here: both annotations exist, and both are load-bearing records (sections 3 and 4 cite them).
- **Why:** R2: porter-added text is part of the change record; these two carry the port's two largest decisions, with attribution.
- **Verify:** Read candidate L258 and L977–979.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) The P9 inlined-base header defaults (section 5): rendered as the base ships them, counted by T4 as the theme's one display-affecting finding, dispositioned under ruling 2 in the (c3) register. (2) T1's eleven pseudo-ref errors and one warn: the candidate's own draft-host local--code and local--files lines (class (iii), sections 3–4) and the frame's draft-host theme= line (class (iii)); the posting procedure rewrites or re-hosts them, and fix lanes never "fix" them in the candidate. (3) The render row's items, all environment, capture, or asset layer, not charged to the candidate: the page and sample overflow readings (467–478px at 320/375 and 792–803px at 768 on the page; 479–490px and 953px on the sample), with the T3 note that the overflow is content extending past the theme's pastel frame — a design-width property of the theme, visually confirmed in the row; the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the broken logo in the T3 capture, recorded as a deferred asset. The base topology (per-theme record) is not listed here as an exception: its ground is the campaign's prescription, cited in section 3, which makes it a recorded delivery decision rather than an exception.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes; ruling 2; the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS (cited as row 157 in the stamp) and register (c1).
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS, cited as row 157 in the verdict stamp): exit 1, 11 errors / 1 warn / 1 info; the errors are pseudo-ref, classes (ii)/(iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-C (EN16)): FINDINGS, the items of section 11(3), all dispositioned or deferred in the row; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 122): FINDINGS jointly, display-affecting findings 1 (the section 5 item); the (c3) register dispositions it under ruling 2. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. The churn count quoted in the Summary is the regenerated figure for the current candidate: +992/−288 in 221 change blocks / 56 diff sections (GNU-diff 1288 changed lines), one added line over the pre-repair +991/−288 for the font-load @import.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:pastel-skies-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 122; go-sign, COMPLETION-REPORT §10), with the per-theme record below standing as this package's addition to the record.

## Per-theme record

### Delivery topology: the base is carried inline (recorded, with its sanction ground)

The original imports its base: `[[include :scp-wiki:component:sigma-plus]]` at its tail (original L1487), next to its own delivery module. The candidate has no such include; the base's CSS stands inside the candidate's first code file (candidate L255–956), delivered through the candidate's own module imports (candidate L9–10). The topology change is real and is recorded here rather than narrated as a supplement, per the campaign's standing instruction for this shape. Its grounds, all on the record: the component is absent on scp-jp, so no repoint target exists (LOCALIZE-ROWS row 87 charges the same absence as a posting blocker for theme:fandom-jp and prescribes "JP-port the component or carry the CSS inline as pastel-skies did"); the carry is disclosed in the candidate itself, in the credit block's 基盤 field (candidate L25) and the prose note at candidate L258, both crediting [[*user EstrellaYoshte]] and the CC BY-SA 3.0 terms; and a JP port candidate of the component now exists in this repo (`pages/component:sigma-plus-jp.txt`), so a future repoint from the inline carry to the component is a mechanical option the coordinator can take when the component posts. This package takes no position beyond the record: the candidate stands as the campaign's reference implementation of the sanctioned form.

### The usage exhibit's slug (flagged by this package)

The usage exhibit (candidate L32) was repointed from `:scp-wiki:theme:pastel-skies` to `:scp-jp:theme:pastel-skies` at creation, keeping the plain slug. The candidate's own posting name is theme:pastel-skies-jp, so the documented syntax names a page that will not exist under that name on scp-jp; the file's own delivery lines use the -jp form throughout (candidate L5, L9, L10). This is the population-sweep family (the same shape is flagged in the plant, parawatch-pumpkin, pack-of-peanuts, paramycota, and past-oriented packages in this batch). The ledger's determination for this theme is PASS and this package does not re-open it; the line is flagged here with its locus, and the candidate is left unedited, as the sweep repairing this family is a coordinator matter.

### 'Noto Sans JP' is named but not loaded in-file (flagged by this package)

Four stacks name 'Noto Sans JP' (candidate L990–993) and the credit block's font field lists it among the theme's Google Fonts faces (candidate L24), but the candidate contains no load for it: the only font loads in the file are the three substitute faces (candidate L981–983), and a search for `family=Noto` returns nothing. This is the KB-16 shape that T4 charged for theme:plant-jp in this batch ("font credited/named but never loaded", LOCALIZE-ROWS row 123); for this theme T4's row records no such item (its one finding is section 5's), so the gap is uncharged. Whether the JP environment's site base loads the face is not decidable from this repo alone, and this package does not decide it: the flag records the in-file fact and its loci, for the coordinator's font pass. The candidate is left unedited.

That flag's condition has since been repaired — FIX-MISC9, canonical commit `a2bd1fb983b56a82b69d82c9350a628c2e32197d` ("pages: pastel-skies font load and parawatch-pumpkin links", 2026-11-17; report `R/review-scout/FIX-MISC9.md`). The lane checked the whole delivery chain — this file, its inlined Sigma+ base, and the JP environment's stylesheet, both repo and deployed copies — and found no load of the port-introduced face, so it added a single `@import` in the file's established form: the candidate now reads `@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP&display=swap');` at L984, alongside the three substitute-face imports (L981–983), and the four stacks L991–994 name the now-loaded face. The checker found no new class (i) error. The usage-exhibit slug flag above was also closed by the earlier population sweep b5cb724 (the candidate now names `:scp-jp:theme:pastel-skies-jp` at L32). This package was rebuilt from the post-repair canonical bytes: `candidate.txt` recopied from `pages/theme:pastel-skies-jp.txt`, `diff.md` and the stamp regenerated. The regenerated stamp reads STALE with the current file sha256 — no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-pastel-skies-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3)); it belongs to this theme's record but carries no port change of its own to explain here. The base component's own JP candidate (`pages/component:sigma-plus-jp.txt`) exists in the repo as a separate package's subject; it is named in the topology record above because a future repoint would consume it. There are no companion fragments and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** Pastel Skies Theme
- **Author:** Miss Lapis、radian628
- **Source:** https://scp-wiki.wikidot.com/theme:pastel-skies — revision 15
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
