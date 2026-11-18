# Review package — theme:ch-scp-theme-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ch-scp-theme-jp — origin EN, population #69 [GOSIGN2-LEDGER (b) row 69]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 3fd16da98c20739fd35e3e853c1b7122ee7a30801076ec649bc667046b08ac8b); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 9 errors / 2 warns / 3 infos (hotlink×8, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 74; GOSIGN2-LEDGER (b) row 69]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — severe candidate-inherent page-overflow 2534px@320 / 2968px@375 (both engines) and 779px@webkit-768. [RENDER-ROWS-1 (RENDER-S2-A)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-A)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 69, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 69]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 69]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:ch-scp-theme-jp.txt sha256:3fd16da98c20739fd35e3e853c1b7122ee7a30801076ec649bc667046b08ac8b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 69) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×8 and pseudo-ref ×1 (class (ii), section 11); the render row's severe page overflow, recorded by the lane as candidate-inherent (section 11); T4's two display-affecting items (header title wording, EN-hosted assets), each with its ledger disposition in section 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ch-scp-theme | theme:ch-scp-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 100 (first translation; the candidate's credit block records 初訳時参照リビジョン: 100) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs2-en5/CACHE/orig/ch-scp-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ch-scp-theme-jp.txt`, copied at worktree HEAD 1605bbd |
| Lines / bytes | 763 lines / 23,713 bytes | 775 lines / 24,741 bytes |
| SHA-256 | 09fdc9ca9f23a30f5f7c31a9c94c56c4d3b5eef4cfd25c8d7e2ecbe0d3f7d56a | 95f9be4dbb1920cf6de495d9b09a480975a51ff0d49b8f05689951c3f2c683dd |

Wave history: the candidate was created by the Stage 2 EN5 integration (commit 7e07438, the LOCALIZE-S2-A wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the translator-attribution normalization that swept all candidates). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A 2019 Black Highlighter theme that restyles the site as the in-universe Chinese branch: a ~590-line CSS body, eight asset references to the EN wiki's file host, and a header that reads "The Foundation". The port follows the BHL-theme frame the caretaker package also uses: the JP BHL theme include in a head wrapper, the base layers as interwiki-style includes at priorities 1 and 2 from the JP BHL distribution, the theme's own layer from its own local--code at priority 3, the credit block for the bare Rate, and the prose and the theme-squares palette translated. Two font decisions ride inside the exhibit: the original's display font came from a third-party Adobe Typekit kit, which the port drops, re-sourcing the Latin display face from Google Fonts (Poppins) and adding the Noto Sans JP supplement. What stands open is recorded, not hidden: all eight asset references still name the EN file host (T1's hotlinks, T4's Pattern 5, dispositioned in the deferred-asset class), the header title stays in English (ruling 2), and the render lane recorded a severe page overflow at phone widths which it classified as candidate-inherent — a property of this theme's fixed-width in-universe layout, stated in section 11 with its numbers. Measured churn (diff.md: +114/−114 in 64 change blocks; a GNU-diff count of the same pair gives 172 changed lines, and the difference is alignment choice, not content).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 64 change blocks — 35 specific (54.7%), 26 heuristic (40.6%), 3 residue (4.7%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 27 |
| TRANSLATION-ANCHORED | 22 |
| INCLUDE-REPOINT | 6 |
| EXHIBIT-RESTRUCTURE | 5 |
| DELIVERY-HOST | 4 |
| DRAFT-HOST | 2 |
| ESCAPED-INCLUDE | 2 |
| IFTAGS | 2 |
| SELF-DELIVERY | 2 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| FONT-IMPORT | 1 |
| JPFONT-LOAD | 1 |
| TASL-FIELDS | 1 |

Adjudication for this README (every block was read against the bytes): the 26 heuristic blocks are prose translations and the font/body work (the CSS-BODY primary is the font re-sourcing's stack side, section 4), verified line by line. The 3 residue blocks adjudicate as: the logo block (original L53–56 → candidate L59–66 — the image made a direct `[[image]]` line, its caption's malformed style `width:width:300px;;` normalized to `width:300px;`, and the caption translated, section 8), one prose line in the usage region (section 6), and a one-line delta inside the exhibit CSS (section 8). The 5 EXHIBIT-RESTRUCTURE primaries are the source-code section's frame and the palette section's frame, adjudicated in section 8. After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ch-scp-theme-jp; original theme:ch-scp-theme on scp-wiki at reference revision 100; candidate `pages/theme:ch-scp-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-A wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame: the original wraps the page in a single `[[iftags +theme]]` gate (L1–760), with a head module importing the base (L6–9) and a tail module outside the gate importing its own layer (L761–763). The candidate splits the frame as its BHL siblings do: an added head wrapper `[[iftags]]` (no tag list) holds the JP BHL theme include alone (candidate L1–3), the main gate is localized to `+テーマ` (candidate L5–766), and the tail delivery stands outside it (candidate L767–773).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for ch-scp-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's only credit furniture is a bare `[[module Rate]]` (original L3). The candidate deletes it (BARE-RATE-DEL block) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L7–16) carrying the eight ruling-3 fields (title In-Universe Chinese SCP Foundation Theme; 翻訳責任者 AI; 翻訳年 2026; 原題 In-Universe Chinese SCP Foundation Theme; 著作権者 Woedenaz; 作成年 2019; 初訳時参照リビジョン 100; the source link, naming scp-wiki.wikidot.com/theme:ch-scp-theme, the recorded host, which serves the original). The title is the theme's proper name in English on both fields, which no record flags. T7 credit-module CSS: none added; the theme's CSS carries no credit rules. License box: none on either side, and none added.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (KB-09). Ruling 3 fixes the eight fields.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L7–16 against the eight fields.
- **Disposition:** Applied (the swap is in the bytes; the ledger's credit outcome for this theme rides on the same credit-wave record as its siblings).

### 2. Includes and components

- **What:** The candidate's includes: the added `:scp-jp:theme:black-highlighter-theme` include inside the head wrapper (candidate L2); the credit pair (section 1); two interwiki-style includes for the base layers and one for the theme's own layer (candidate L18–26 and L770–773, section 3); the theme-squares palette component, repointed from `:scp-wiki:component:theme-squares` to `:scp-jp:component:theme-squares` with its color names translated (candidate L32 onward: タンドラ, バーミリオン, …); and the image-block family includes of the examples. The escaped usage examples (candidate L75–76 and L83–84) teach the two-line form: `:scp-jp:theme:black-highlighter-theme` plus, as built, `:scp-jp:theme:ch-scp-theme` — the repoint changed the branch prefix but kept the plain slug, naming a page that does not exist on scp-jp; the usage-example population sweep has since completed both self-references to this candidate's posting name, `:scp-jp:theme:ch-scp-theme-jp` (candidate L76 and L84; per-theme record). The 6 INCLUDE-REPOINT blocks are these repoints; every live include in the candidate names a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp — including components, whose parameter text (the palette's color names) is reader-visible and translates with the include. As built, the usage examples' repoint satisfied the branch half of that rule only; the sweep's completion of their name is what brings them under it. Ruling 4 is not engaged: the components named already exist on the JP side.
- **Verify:** `grep -n '\[\[include' candidate.txt` — all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The base's channel changes shape, and the own layer changes host. (1) The original's head module imports the base from the upstream distribution (`nu-scptheme.github.io/Black-Highlighter/css/min/normalize.min.css` and `.../black-highlighter.min.css`, original L7–8); the candidate drops the head module entirely — the base arrives through the JP BHL theme include (section 2) and is mirrored as interwiki-style layers naming the JP distribution, normalize at priority 1 and the base at priority 2 (candidate L18–26, `scp-jp.github.io/Black-Highlighter/css/min/…`). (2) The theme's own layer: the original's tail module imports its EN page's own delivery from the EN file host (`scp-wiki.wdfiles.com/local--code/theme%3Ach-scp-theme/1`, original L762); the candidate's tail module imports its own `local--code/theme%3Ach-scp-theme-jp/1` from the draft host (candidate L767–769, SELF-DELIVERY), and an interwiki-style include at priority 3 names the same delivery (candidate L770–773). The DELIVERY-HOST and DRAFT-HOST blocks are these changes; the own layer's body is the code exhibit (candidate L176–764).
- **Why:** P4/T9: delivery is served from JP hosts — the JP BHL distribution for the base, the theme's own code for its layer — never from the original's page or the upstream distribution. P6/T3 supplies the interwiki-style supplement frame and its priority order (1 normalize, 2 base, 3 own). The draft-host form of the own delivery is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n '@import' candidate.txt` — the exhibit's two font imports (section 4) and L768 (own draft-host delivery); no nu-scptheme or scp-wiki delivery URL remains.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Fonts first, because this theme makes two real decisions. The original loads its display face from a third-party Adobe Typekit kit (`@import url("https://use.typekit.net/rbw6esf.css")`, original L172, at the exhibit's head). The candidate deletes the Typekit import and re-sources the Latin display face from Google Fonts (Poppins, candidate L180, the FONT-IMPORT block), and adds the JP supplement (Noto Sans JP, candidate L177, the JPFONT-LOAD block); the CSS-BODY heuristic block is the stack side of the same re-sourcing. A Typekit kit is bound to its owner's account and kit configuration, so keeping the import would have made the JP page depend on a stranger's Adobe account; the Google Fonts form names the same class of face from a neutral host. Assets: eight references stay on the EN wiki's file host (scp-wiki.wdfiles.com), untouched apart from the frame around them — the branch logo image (candidate L59), the base theme's logo image (candidate L67), the header `--logo-image` (candidate L195), the tag banner background (candidate L346), and the subtle_white_mini_waves.png texture at four rules (candidate L380, L388, L436, L450). These are T1's eight hotlink errors and T4's Pattern 5 items; the ledger dispositions them in the deferred-asset class (section 11).
- **Why:** P7 (JP font supplement; the Typekit removal is the same account-bound-host reasoning as the KO ports' Typekit deletion) and P5 (assets served from JP hosts), whose disposition is KB-58's standing treatment for original-wiki file hosts (deferred re-host, class (ii)): the assets serve today from the EN host, and no JP-hosted copies exist to point at.
- **Verify:** `grep -n '@import' candidate.txt` for the fonts; `grep -n 'scp-wiki.wdfiles.com/local--files' candidate.txt` — eight lines, as listed.
- **Disposition:** DISPOSITIONED (assets, P5, class (ii) / KB-58); the font re-sourcing stands as applied.

### 5. Header, sidebar, and site furniture

- **What:** The header variables travel with the exhibit: `--logo-image` (candidate L195, the EN-hosted logo of section 4), `--header-subtitle: " "` (blank on both sides), and the recorded exception — `--header-title: "The Foundation"` stands in English at candidate L196, exactly as in the original (L188). T4's row 69 marks this Pattern 9 display-affecting; the ledger dispositions it under ruling 2 (section 11). No sidebar or topbar rule was adapted beyond what the moved CSS body already carried.
- **Why:** P9's JP-header expectation is what T4 measured; ruling 2 (header text language is translation taste, and this title is the in-universe branch's own masthead) is the ground the ledger dispositioned it on — recorded here because the title is always displayed.
- **Verify:** `grep -n -- '--header-title' candidate.txt` — L196, English.
- **Disposition:** DISPOSITIONED (P9, ruling 2, GOSIGN2-LEDGER §(c3) line for this theme).

### 6. Text translation

- **What:** The prose is translated throughout (the 27 TRANS-UNANCHORED heuristic primaries and 22 TRANSLATION-ANCHORED blocks, verified line by line): the palette section's color names and notes (section 2), the usage sections (including the note at candidate L70, whose EN absolute link to the base theme became the bare posting-form link `[[[theme:black-highlighter-theme|詳しくはこちら]]]`), the examples, and the exhibit's surrounding prose; the one residue prose line in the usage region is counted here with its fellows. English survives only as quotation: the credit fields (candidate L8, L11, L15), the header title (section 5), and the exhibit CSS's own comments, which are the S-CSS-P template's code comments and travel with the code.
- **Why:** P10 (body and usage translation is the port's purpose) and KB-18 (reader-visible strings).
- **Verify:** The pairs are diff.md's body sections in order.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** No prose link names a foreign wiki: the intro's base-theme link is the bare posting form (candidate L70), the credit source link (candidate L15) names the recorded host and serves, and the remaining `[[[...]]]` links are the page's internal examples. The host check the jiha exemplar taught (candidate host vs recorded host, probe on divergence) therefore has nothing to probe: the only scp-wiki URLs in the file are the recorded source link and the asset/delivery lines already accounted for in sections 3 and 4 — and those name the recorded host, not a divergent one.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; this theme's links satisfy it as they stand.
- **Verify:** `grep -n 'scp-wiki' candidate.txt` — L15 (source) plus the section 3/4 lines.
- **Disposition:** Standing; no P11 item was recorded for this theme.

### 8. Structure

- **What:** The skeleton corresponds: gate, palette, usage, examples, source-code exhibit, tail delivery. The 5 EXHIBIT-RESTRUCTURE primaries and the remaining residue adjudicate to frame and repair items, not content restructuring. (1) The palette section's frame: the theme-squares include moved into the candidate's centered heading frame (candidate L28–30), its parameters translated — a frame change around a corresponding component. (2) The logo block repair (residue, original L53–56 → candidate L59–66): the original wraps its logo image in a block whose caption style is malformed (`width:width:300px;;`); the candidate makes the image a direct `[[image]]` line and normalizes the caption style to `width:300px;`, translating the caption — a repair of a broken attribute, recorded here because it is a real byte change beyond translation. (3) The source-code section's frame (collapsible labels and heading localized) around a body that corresponds rule for rule; the one-line residue delta inside the body is a single declaration line in the closing rules, counted with the CSS-BODY work of section 4. Exhibit census: one exhibit on each side (the theme's own CSS), no exhibit added, dropped, split, or merged.
- **Why:** R3 requires the census before a restructure is narrated; here the census shows correspondence plus one attribute repair.
- **Verify:** `grep -n '\[\[code' original.txt candidate.txt` — one exhibit each; read original L53–56 against candidate L59–66 for the repair.
- **Disposition:** Standing (correspondence established; the repair is in the bytes).

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation (0 and 0), so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The classifier's section-9 counts in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate contains no `[!-- ... --]` comments and no 訳注 footnotes; the port's judgments (the English header title, the kept EN assets) are not announced in the page — their record is the T4 row, the ledger line, and this package.
- **Why:** R2: porter-added text is part of the change record; its absence is stated, not assumed.
- **Verify:** `grep -n '訳注\|\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing (as an absence, stated).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's nine errors: hotlink ×8 — the EN-hosted assets of section 4, class (ii) (KB-58); pseudo-ref ×1 — the candidate's own draft-host local--code lines (section 3), class (ii). There is no class (i) error; the 2 warns / 3 infos are recorded verbatim in T1-ROWS row 74 and are not classified. (2) The render row's finding, stated with its numbers because it is the largest reading in this batch: a severe page overflow of 2534px at the 320 viewport and 2968px at 375 (both engines) and 779px at webkit-768, which the lane recorded as **candidate-inherent** — the theme's in-universe layout is built around fixed wide elements, and the overflow is a property of the theme's design as ported, not a break the port introduced; the row records no other theme-specific defect, and no credit-modal line exists in this theme's row. It is carried here so a reviewer opening the page at phone width meets a recorded fact, not a surprise. (3) T4's two display-affecting items and their ledger dispositions (§(c3) line for this theme): the English header title — P9 DISPOSITIONED (ruling 2); the EN-hosted assets — P5 DISPOSITIONED (class (ii) / KB-58). The theme's determination is PASS and this package does not re-open it.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a lane-classified inherent property is recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (items 1 and 3); item 2 recorded as candidate-inherent by the render lane.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 74): exit 1, 9 errors / 2 warns / 3 infos; the errors are hotlink ×8 and pseudo-ref ×1, all class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, lane RENDER-S2-A): FINDINGS — the candidate-inherent overflow of section 11(2); engine coverage full matrix as run by the lane. (c) T4/T5 (LOCALIZE-ROWS row 69): FINDINGS jointly, display-affecting findings 2; the ledger §(c3) line records the theme's P5/P9 outcomes as DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +114/−114 in 64 change blocks; the GNU-diff count of the same pair is 172 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ch-scp-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 69; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's posting name

The usage examples at candidate L76 and L84 as built read `@@[[include :scp-jp:theme:ch-scp-theme]]@@`: the porting wave's repoint changed the branch prefix but left the plain name, so each example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed both references to `:scp-jp:theme:ch-scp-theme-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), two of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-ch-scp-theme-jp.txt` is the decoration sample the render checks ran against; it belongs to this theme's record but carries no port change of its own to explain here. The original-side sample `pages/theme-decoration-sample-ch-scp-theme.txt` is the campaign's mirror-side fixture, likewise outside the port. There are no companion fragments, no shared base file, and no inbound-link repairs in other candidates for this theme.

## License and attribution

- **Title:** In-Universe Chinese SCP Foundation Theme
- **Author:** Woedenaz
- **Source:** https://scp-wiki.wikidot.com/theme:ch-scp-theme — revision 100
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
