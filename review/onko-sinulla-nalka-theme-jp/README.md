# Review package — theme:onko-sinulla-nalka-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:onko-sinulla-nalka-theme-jp — origin EN, population #116 [GOSIGN2-LEDGER (b) row 116]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 372cc01afca3771b40b23c00c92257a291c6441af08d026fa0d09145ee42df1e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 1 warn / 0 infos (pseudo-ref×7); standing classes dispositioned in register c1 [T1-ROWS row 116; GOSIGN2-LEDGER (b) row 116]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + page-overflow 337–419px@320/375. [RENDER-ROWS-2 (RENDER-S2-C (EN15))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN15))]
- T4 (localize patterns + follow-up): PASS — display-affecting findings: 0 [LOCALIZE-ROWS row 116, source LOCALIZE-S2-B]
- T5 (translation text): PASS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 116]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 116]
- Computed against: canonical commit 4176cc76aa668e42056010548f62a1db8d06a32e; candidate file pages/theme:onko-sinulla-nalka-theme-jp.txt sha256:372cc01afca3771b40b23c00c92257a291c6441af08d026fa0d09145ee42df1e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 116) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×7 (class (ii), section 11); the render row's items (site-theme chain, credit-modal preview form, page-overflow, section 11). Two items this package flagged have since been repaired: the usage example's plain-slug self-include (candidate L57, sweep commit b5cb724) and the own-layer delivery address /1, which served a 90-byte rating sample rather than the CSS exhibit (canonical commit 4176cc7) — both closed in the per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:onko-sinulla-nalka-theme | theme:onko-sinulla-nalka-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 28 (first translation; the candidate's credit block records 初訳時参照リビジョン: 28) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-B/orig-onko-sinulla-nalka-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:onko-sinulla-nalka-theme-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 329 lines / 10,580 bytes | 358 lines / 11,523 bytes |
| SHA-256 | 755b4ccc5cb36b4ff037c1cde9ecaa38722f6bc3f409d9ff3d69f379f671b998 | e1d6473729c5eb70a5107af6e5de66a17e295820535d143a6e1dbc856d6882d4 |

Wave history: the candidate was created by the Stage 2 EN15 integration (commit fde02f3, the LOCALIZE-S2-B wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the translator-attribution normalization run over 163 candidate files). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Black Highlighter variant (a Sarkic recipe-blog theme) whose port is dominated by a delivery consolidation. The original delivers its CSS from two points: a head `[[module CSS]]` carrying the EN BHL imports and four small rule groups, and the `[[code]]` exhibit served as `local--code` /2 by a tail module. The candidate consolidates everything into the single code exhibit (now `local--code` /2 after the self-delivery audit repair), frames it with the standard BHL layering (the JP BHL distribution at priorities 1 and 2, the theme's own layer at priority 3), swaps the credit furniture for the JP preview block, converts the body's two image-license exhibits into a JP license box at the tail, and translates the demonstration body in place. Measured churn (diff.md, the generator's difflib count with autojunk off: +228/−199, 427 changed lines in 12 change blocks / 6 diff sections) overstates the semantic change, because the two largest blocks are the head rebuild and the relocation itself. Two items this package flagged rather than skimmed have since been repaired: the usage example's plain-slug self-include (candidate L57; sweep commit b5cb724) and the own-layer address, which as built named a 90-byte rating sample instead of the CSS exhibit (canonical commit 4176cc7); both are closed in the per-theme record.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 12 change blocks — 12 specific (100%), 0 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| DELIVERY-MOVE | 8 |
| DRAFT-HOST | 5 |
| TRANS-UNANCHORED | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| HEADERVAR | 2 |
| SELF-DELIVERY | 2 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 1 |

Adjudication for this README (every block was read against the bytes): the DELIVERY-MOVE count of 8 is the consolidation's shadow, not eight relocations — B3 and B5–B10 are single lines or pairs inside the one moved body whose only change is a host form or a variable value (sections 3–5). B4's two labels do not survive the bytes: its EXHIBIT-RESTRUCTURE primary is the whole body block displaced by the relocation (the exhibit census in section 8 shows every exhibit carried, translated), and its RATE-EXHIBIT-KEPT-CANDIDATE label is wrong for this theme — the candidate contains no `[[module Rate]]` at all; the original's bare Rate (original L40–42) was deleted under P3 (section 1). B1 spans candidate L1–155 because the head was rebuilt around the moved body; its seven labels are adjudicated in sections 1–3 and 6. The skeleton's "none" for sections 2, 4, 5, 6, and 10 does not survive the label_spans: B1 carries INCLUDE-REPOINT (section 2), B2 carries FONT-IMPORT and JPFONT-LOAD (section 4), B5 and B7 carry HEADERVAR (section 5), B1/B2/B11 carry TRANS-UNANCHORED (section 6), and two porter comments ride inside B2 (section 10). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:onko-sinulla-nalka-theme-jp; original theme:onko-sinulla-nalka-theme on scp-wiki at reference revision 28; candidate `pages/theme:onko-sinulla-nalka-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-B wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original opens with the two EN BHL furniture includes ahead of its tag gate (original L1–3); the candidate opens with the base-theme include, the repointed furniture pair, the delivery frame, and only then the localized gate (candidate L1–23).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the furniture repoints are P1, the frame is P6/T3 (sections 2 and 3).
- **Verify:** The sources.tsv row for onko-sinulla-nalka-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and frame changes are recorded in sections 2 and 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` in a centered div at the head of the body (original L40–42) and no info block; authorship appears in the body's two image-license exhibits (original L190–207: "Author: DJ Pettitt" and "Author: Metaphysician", each "Edited by IronShears"). The candidate deletes the Rate (inside B4) and installs the JP form: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L25–34) carrying the eight ruling-3 fields (title オンコ・シヌッラ・ナルカ テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 Onko Sinulla Nälkä? Theme; 著作権者 [[*user IronShears]]; 作成年 2024; 初訳時参照リビジョン 28; the source link, candidate L33, on scp-wiki.wikidot.com, the host sources.tsv records for the original). Author check against the original: IronShears is the theme's author (both license entries name him as editor, and the body's comment exhibits sign him, original L167 and L173); the two exhibit authors are image credits, not theme co-authors, so the field drops no one. The translator field took its ruling-3 form in 1869877 (FIX-CREDIT-D). The section's T4 half: the two image entries move into a JP license box at the tail (candidate L339–356, block B11): `license-box-backend` with `author=IronShears`, the entries translated (ファイル名/作者/ライセンス/出典/補足) with their facts intact (PaperTextureSarkic.png and PaperTextureSarkicDark.png, DJ Pettitt, CC-BY 2.0, Flickr source; SarkicLogo.png, Metaphysician, CC-BY-SA 3.0, the Sarkicism hub), and a closing line recording that all other images are IronShears' own under CC-BY-SA 3.0. T7 credit-module CSS: none on either side (no credit selectors exist in either file), so nothing was added and nothing needed correcting in place.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (a kept Rate would be the KB-09 duplicate). Ruling 3 fixes the eight fields and the translator credit form. T4: the license entries take the settled JP box form; the original carried them as body exhibits, so this is a form conversion, not a KB-63 restoration.
- **Verify:** `grep -n 'module Rate' candidate.txt` returns nothing; read candidate L25–34 against the eight fields; `grep -n 'license-box' candidate.txt` returns the pair at L339 and L356.
- **Disposition:** Applied (LOCALIZE-ROWS row 116 records this theme's T4 outcome as PASS with no credit item).

### 2. Includes and components

- **What:** The skeleton prints "none" for this section; the label_spans in B1 say otherwise. Three include changes: (a) the two EN BHL furniture includes are repointed in place (original L1–2 → candidate L3–4: `component:toggle-sidebar-bhl`, `component:centered-header-bhl`); (b) one include with no original counterpart is added at the head (candidate L1: `[[include :scp-jp:theme:black-highlighter-theme]]`, the JP BHL base theme itself); (c) the usage example's two escaped includes are repointed (original L64–65 → candidate L56–57), of which the second was a flagged plain-slug self-reference, since completed to `:scp-jp:theme:onko-sinulla-nalka-theme-jp` by the sweep (b5cb724; per-theme record). The credit pair (section 1), the three interwiki-style includes (section 3), and the license-box pair (section 1) complete the candidate's live include list: ten live includes, every one naming a `:scp-jp:` target.
- **Why:** P1 (KB-15): an include must name the JP counterpart that exists; `theme:black-highlighter-theme` is the production JP page name for the base (the sources.tsv record for theme:black-highlighter-theme-jp), so the base include resolves today. Ruling 4 is not engaged: no component had to be ported alongside this theme.
- **Verify:** `grep -n '\[\[include' candidate.txt` — ten live includes plus the two escaped exhibit lines, all `:scp-jp:`.
- **Disposition:** Applied; the example's self-reference was flagged and is now repaired by the sweep (b5cb724; per-theme record).

### 3. Delivery and code loading

- **What:** The original delivers from two points: a head `[[module CSS]]` (original L6–38) importing the EN BHL pair from nu-scptheme.github.io and carrying four small rule groups, and a tail `[[module CSS]]` plus interwiki-style include (original L322–329) serving the `[[code]]` exhibit as `local--code` /2 at priority 3. The candidate consolidates delivery into the single code exhibit (candidate L187–336), now `local--code` /2: a head `[[module CSS]]` imports the own /2 from the draft host (candidate L6–7), and three interwiki-style includes frame the layers (candidate L10–21): priority 1 the JP BHL normalize sheet, priority 2 the JP BHL black-highlighter sheet (both on scp-jp.github.io), priority 3 the own /2 on the draft host. As built the candidate named /1, which the probe served as a 90-byte rating sample (code block 1); the self-delivery audit (FIX-CODEADDR.md in R/review-scout/) classified the reference a mismatch and canonical commit 4176cc7 repointed both the head `@import` (candidate L7) and the priority-3 frame `theme=` (candidate L20) to /2, the 4,397-byte CSS exhibit. The head module's four rule groups (`#page-title { display: none }`, the `.scp-image-block` padding, `.fonts-display`, and the `.title-font`/`.header-font`/`.UI-font`/`.mono-font` family rules) travel into the exhibit body behind the hoisted imports (candidate L202–231); the topology pass measures the move module-css → code-css at 0.87 similarity, and the rest of the exhibit is the original's code-css body. The tail module and its /2 import are deleted (B12), and B3 is the head module's closing `[[/module]]` line, deleted with it: there is nothing left for either to serve.
- **Why:** P4/T9 (base delivery from the JP BHL distribution: scp-jp.github.io replaces nu-scptheme.github.io) and P6/T3 (the interwiki-style frame; BHL layering is priority 1 normalize / 2 base / 3 own). The draft-host form of the own-code lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code\|interwiki-style' candidate.txt` — L7 and L10–21; compare original L6–8 and L322–329.
- **Disposition:** DISPOSITIONED (the draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Loads: the original's code exhibit loads Itim and Playwrite GB S from fonts.bunny.net (original L211–212). The candidate loads the same two families from fonts.googleapis.com (candidate L195–196) and adds the two JP faces, Noto Sans JP (400;700) and Noto Serif JP (400;700), also from Google Fonts (candidate L199–200). Stacks (B7's font lines and the `:root` group): the original's single-face stacks gain JP faces — `--body-font` and `--UI-font` become `"Itim", "Yu Gothic", "Hiragino Kaku Gothic ProN", "Noto Sans JP", cursive` (candidate L256, L259) and `--title-font`/`--header-font` become `"Playwrite GB S", "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif JP", cursive` (candidate L257–258). Load-gap check: every non-system face named first in a stack is loaded (Itim, Playwrite GB S, Noto Sans JP, Noto Serif JP); the Yu Gothic / Yu Mincho / Hiragino names are OS faces and need no load, so there is no KB-16 gap. Assets: five image URL lines move from `scp-wiki.wdfiles.com/local--files/theme%3Aonko-sinulla-nalka-theme/` to the candidate's own `theme%3Aonko-sinulla-nalka-theme-jp` folder with file names unchanged — `--diagonal-stripes` (candidate L253, draft host), `--logo-image` (candidate L254, production host scp-jp.wdfiles.com), the horizontal-rule background (candidate L286, draft host), and the two `#content-wrap` backgrounds (candidate L294, L301, draft host). The one production-form line among draft-form siblings is recorded here because a reviewer will trip on it; both forms are posting-procedure mechanics.
- **Why:** P5 with KB-17 (font and asset hosts: Google Fonts is an allowed hotlink host, and fonts.bunny.net is a mirror of it, so the port takes the canonical host; the theme's own images are re-hosted to the JP side). P7 (the JP faces enter the stacks that render Japanese text; loads and stacks change together).
- **Verify:** `grep -n '@import' candidate.txt` — six imports, L7 (own code) and L192–200 (the exhibit's five); `grep -n 'local--files' candidate.txt` against the five asset lines above.
- **Disposition:** Loads and stacks applied; the asset URL host forms are DISPOSITIONED (classes (ii)/(iii)).

### 5. Header, sidebar, and site furniture

- **What:** Two variable changes beyond section 4's assets (the HEADERVAR spans of B5 and B7): `--header-title` (original L243 → candidate L261) keeps its value, "Onko Sinulla Nälkä?", the theme's own name; `--header-subtitle` (original L244 → candidate L262) is translated, "The Taste of Home." → "故郷の味。". The candidate's sidebar and header furniture comes from the repointed BHL component pair (section 2) over the JP BHL base; no P8 layout-adaptation block fired and none was needed.
- **Why:** P9/T6 for the variables themselves; the subtitle is reader-visible header text, so its translation is P10/KB-18; the title is the work's name, kept under the header-language disposition (KB-57; ruling 2 puts header-title language outside migration correctness).
- **Verify:** `grep -n -- '--header-' candidate.txt` — two lines, L261–262.
- **Disposition:** Standing; the title is kept by disposition (KB-57).

### 6. Text translation

- **What:** The demonstration body is translated throughout: the intro paper (original L44–53 → candidate L36–47, with the theme's own Finnish greeting "Hyvää ruokahalua!" kept as content), the usage prose (candidate L49–57), and the full syntax-example body (original L67–213 → candidate L62–185): heading samples, tab titles, collapsible labels, the blockquote and comment exhibits, and the table sample. The classifier's translation labels ride inside B1, B2, B4, and B11 (TRANSLATION-ANCHORED 1 block, TRANS-UNANCHORED 3 blocks by primary label), which understates the mass because the body travels inside the relocation blocks; the honest measure is the exhibit census in section 8. In-CSS text (R1), stated separately: the `--theme-name` string "Onko Sinulla Nälkä?" is the theme's name and is kept on both sides; the original's English CSS comments (`/* Intro */` and its siblings) are carried unchanged, porter-visible only. Finnish survives in the candidate only where it is the theme's own content (its name and its greeting), never as untranslated prose.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). R1 is separated per the taxonomy so a reviewer can tell reader-visible text from porter-visible text.
- **Verify:** The body sections of diff.md in order; an English-prose scan of candidate.txt outside the code exhibit returns only the theme's name and greeting.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the theme's own name and greeting.

### 7. Links

- **What:** One prose link: the BHL link in the usage prose, original `[theme:black-highlighter-theme Black Highlighter]` → candidate L53 `[[[theme:black-highlighter-theme|Black Highlighter]]]`, its target name unchanged (it names the production JP page, so no repoint was needed) and its form converted to the triple-bracket house form. The credit block's source link (candidate L33) names scp-wiki.wikidot.com, the recorded host, and serves the original. The license box's CC and Flickr links are the original's own, carried inside the translated entries (section 1). No other outbound link exists in the candidate.
- **Why:** P11: prose links take the JP counterpart or the serving original; the dead-reference evidence standard is not engaged because nothing here is dead.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit (the wdfiles asset lines are section 4).
- **Disposition:** Standing.

### 8. Structure

- **What:** The localize.md closing rule holds with one declared deviation: the delivery consolidation (section 3) merges the head module's rules into the code exhibit, so the candidate has one CSS channel where the original had two; inside the exhibit, variable names, selectors, and rule order are preserved (topology similarity 0.87, and the differences are exactly the imports and stacks of section 4). Exhibit census: the tabview and its tabs (original L104–147), the paper and blockquote exhibits, the comment exhibit and its `[[code]]` twin (original L170–176 → candidate L162–168), the table sample, and the theme-code collapsible (original L210–211) are present on both sides in the same order — nothing was dropped or replaced, so the R3 question does not arise. The two EXHIBIT-RESTRUCTURE primaries adjudicate against the census: B4 is the body block displaced by the relocation (its one real deletion is the bare Rate, section 1), and B12 is the tail delivery module deleted because its function moved to the head frame (section 3). The license entries' move from body exhibits to the tail box is a form conversion (section 1), not a deletion: both entries survive with their facts.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[collapsible' original.txt candidate.txt` — the sequences correspond one to one.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds 0 WS-ONLY blocks and 0 re-indentation pairs; the churn in this diff is relocation and translation, not formatting, so the R7 follow-up-diff hazard is not triggered.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** The skeleton's section 9 counts in classification.json (`reindent_blocks`: 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations, both inside the code exhibit and both riding inside B2 (the skeleton's "none" for this section does not survive contact with the bytes). (1) Candidate L189–190, in English: the port provenance comment, "Onko Sinulla Nälkä? Theme — ported for SCP-JP (theme:onko-sinulla-nalka-theme rev 28). Imports are hoisted to the top so the stylesheet stays valid." (2) Candidate L198, in Japanese: the font note, "日本語フォント (JP localization; stacks mined from the prior-art JP translation)", recording that the section 4 JP stacks were taken from a prior JP translation of this theme rather than invented for this port.
- **Why:** R2: porter-added text is part of the change record. Annotation (1) is the only in-file explanation of the import hoisting in section 3, and annotation (2) is the provenance of the section 4 stacks.
- **Verify:** Read candidate L189–190 and L198.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's seven pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host `local--code` and `local--files` lines (sections 3 and 4), which the posting procedure rewrites or re-hosts; fix lanes never "fix" them in the candidate. (2) The render row's three items (RENDER-ROWS-2, lane RENDER-S2-C (EN15)), none charged to the candidate at the ledger determination: the page's runtime-hotlink site-theme chain (KB-40, environment layer); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and the page-overflow of 337–419px at 320/375, recorded verbatim in the render row. (3) The usage example's self-include (candidate L57): was flagged in the per-theme record; the sweep (b5cb724) has since completed it to the posting name, and the record is closed.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 flagged with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 116): exit 1, 7 errors / 1 warn / 0 info; all seven errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, RENDER-S2-C (EN15)): FINDINGS, the three items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 116, LOCALIZE-S2-B): PASS / PASS, display-affecting findings 0. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +228/−199 in 12 change blocks / 6 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:onko-sinulla-nalka-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 116; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The usage example's self-include (repaired)

As built, the candidate's usage example (candidate L56–57) showed `:scp-jp:theme:black-highlighter-theme` for the base and `:scp-jp:theme:onko-sinulla-nalka-theme` for this theme. The base's line is correct (the production JP counterpart of theme:black-highlighter-theme-jp). This theme's line named a page that does not exist on scp-jp: the candidate's posting name is theme:onko-sinulla-nalka-theme-jp. The original's example (original L64–65) named its own page correctly on scp-wiki; the port repointed the site prefix and kept the plain name, which is where the defect entered. The usage-example population sweep completed the reference to `:scp-jp:theme:onko-sinulla-nalka-theme-jp` (sweep report SWEEP-USAGE.md in R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design, as it does for the second repair below.

### The self-delivery code-block address (repaired)

As built, the candidate's head `@import` (candidate L7) and priority-3 interwiki frame `theme=` (candidate L20) named `local--code/theme%3Aonko-sinulla-nalka-theme-jp/1`, but code block 1 is a 90-byte rating sample; the CSS exhibit is code block 2 (candidate L187–336). The candidate therefore did not deliver its own layer. The self-delivery code-block address audit (R/review-scout/FIX-CODEADDR.md) censused every `[[code]]` fragment in document order, classified the reference a MISMATCH and probe-verified both addresses on the draft host (block 1 = 90 B rating sample; block 2 = 4,397 B CSS exhibit). Canonical commit 4176cc7 repointed both lines from /1 to /2. The repair changes two address tokens; nothing else in the candidate changed. The stamp reads STALE against the pre-repair verdict by design: no re-judgement is fabricated, and the frozen ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is larger. `pages/theme-decoration-sample-onko-sinulla-nalka-theme-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). The canonical composition also carries the original under its own name, `pages/theme:onko-sinulla-nalka-theme.txt`, as the render checks' original-side page; it carries no port change to explain here. The base theme is theme:black-highlighter-theme-jp's own record, not this theme's companion file. There are no companion fragments and no inbound-link repairs in other candidates for this theme.
