# Review package — theme:scp-human-resources-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scp-human-resources-jp — origin EN, population #32 [GOSIGN2-LEDGER (b) row 32]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7b69ea3d432865ab3d909ebed984467e60e4117835f64499a4b795efcf638bc7); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): PASS — baseline 2026-11-16: exit 0, 0 errors / 1 warn / 0 infos (no error codes) [T1-ROWS row 32; GOSIGN2-LEDGER (b) row 32]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — sidebar x=0, mobile notice/logo clip, WebKit CC "S", page credit modal overflows at 320, sample credit-modal + overflow 337–419px, near-black section swallows its text. [RENDER-ROWS-1 (RENDER-C row 32)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 32)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 32, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 32]
- FIX5 re-judgement: item 6 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 fix; checker code-multiset identical before/after [GOSIGN2-LEDGER-SUPPLEMENT (a) item 6]
- Computed against: canonical commit 8c935d39aab93c2784fc512f9e5cd4203b08fa36; candidate file pages/theme:scp-human-resources-jp.txt sha256:7b69ea3d432865ab3d909ebed984467e60e4117835f64499a4b795efcf638bc7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes); the stamp reads STALE by design, because the candidate changed after the verdict (the 5d95177 frame remedy, section 3). The frozen ledger remains the verdict for the bytes it judged |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 6 [D] (pattern 7: header subtitle in a Latin-only face; no JP font named or loaded) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 6: **FIXED** (FIX5-FONTSA, commit 8eacd6e); re-derived from this package's bytes in the per-theme record |
| Standing items | **DISPOSITIONED** — ledger §(c3): P3 credit fields FIXED by the credit waves, P6 FIXED by the frame waves; ledger §(c2) render row: sidebar x=0, mobile notice/logo clip, WebKit CC "S", page credit-modal overflow at 320, sample credit-modal preview form (KB-32), sample overflow 337–419px, near-black section swallowing its text (KB-33/KB-34 families); T1 PASS outright (0 errors / 1 warn) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |
| Flags from this package | Two content omissions no ledger row dispositions: the SCP Offices delivery layer and the original head module's `.scp-image-block` rules (per-theme record). Flagged, not edited |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:scp-human-resources | theme:scp-human-resources-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 14, the re-translation reference revision (rev created 2023-01-06); recorded in the candidate's credit block: **初訳時参照リビジョン:** 14 (candidate L112) and in its body: **改訳時参照リビジョン:** 14 (candidate L123) | — |
| Source of this copy | Fetched 2026-11-17 for the mirror freeze (class FETCH-REGEN), via the mirror store; hash-verified against review/sources.tsv | Canonical file `pages/theme:scp-human-resources-jp.txt`, copied at worktree HEAD c92a320; the file's last content change is commit 5d95177 (frame remedy, sub-shape (D)) |
| Lines / bytes | 295 lines / 7,833 bytes (the last line carries no trailing newline, so `wc -l` reports 294) | 127 lines / 4,466 bytes |
| SHA-256 | abe2d93a20d14fb030131ae1326316b3a28412050f257839a8404c33e8c6f58b | feb319c1f764bdffb79a5d793bdc825245e3fa8bd38e9a719b96e5666b2d6cd9 |

Wave history: the candidate was added in b0cfebd ("Add eight standalone JP theme ports"); Phase 17 (8dcac74) recorded its reference revision; FIX-CREDIT-D (1869877) normalized its translator attribution; FIX5-FONTSA (8eacd6e) applied the pattern-7 fix; 5d95177 dropped the dead frame parameter. The production-side migration is a separate one-line delivery (change set, below).

## Summary

This is the campaign's K6 shape: SCP-JP production already hosts this theme (theme:scp-human-resources, translated 2022), so the candidate is not a fresh port of the EN page. It is a standalone re-statement of the production theme under the -jp name: the theme's own CSS (the original's code-block body) is inlined into a head module over the JP Black Highlighter distribution, the credit block is the production credit form with the ruling-3 adaptation line, and a twelve-line body replaces the original's 190-line documentation, which lives on the production page. The measured churn (diff.md: +87/−252 in a single hunk) is therefore mostly provenance, not edits: the production adoption, the standalone restructuring, and one FIX5 font fix ride in the same diff, and the per-theme record separates them. Two omissions relative to both the original and the production page are flagged in the per-theme record (the Offices layer; the image-block rules).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 20 change blocks — 20 specific (100%), 0 heuristic, 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Label counts are signature spans across blocks (a block carries several).

| Label | Spans |
|---|---|
| DELIVERY-MOVE | 19 |
| WS-ONLY | 12 |
| IFTAGS | 3 |
| EXHIBIT-RESTRUCTURE | 2 |
| FONT-IMPORT | 2 |
| HEADERVAR | 2 |
| TRANS-UNANCHORED | 2 |
| ASSET-REHOST | 1 |
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DUPIMPORT-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens inside its `[[iftags +theme]]` gate with a head `[[module css]]` (original L2–31): the two Black Highlighter @imports from nu-scptheme.github.io, a `:root` logo line, and four `.scp-image-block` rules. The candidate opens ungated with a larger head module (candidate L1–87) carrying the BHL imports from scp-jp.github.io, the Zilla Slab and Noto Sans JP loads, and the theme's whole own CSS inlined (the DELIVERY-MOVE of section 3); its gate (`+テーマ`, L103) wraps only the credit block and body. Provenance route: **production-counterpart adoption (R4) in standalone form (kind K6)**. Evidence: review/sources.tsv records that the production page theme:scp-human-resources exists, that production drift against it is 一致 (matching), and that the Sigma-10 migration is delivered as `pages/phase17-diff-scp-human-resources-jp.txt`; the candidate's credit block names the production translator (section 1); its own prose declares the standalone intent (candidate L118); its git origin is the standalone-ports commit b0cfebd.
- **Why:** Section 0 is where R4 is declared: a diff against the branch original misattributes production form to the port unless the adoption is stated. The K6 shape (production page as a third source) is the SPECIAL-ROWS scout's K6 class.
- **Verify:** Read candidate L116–126 against original L42–279; read the sources.tsv note for this row; `git log --oneline -- pages/theme:scp-human-resources-jp.txt`.
- **Disposition:** Recorded (K6); the two omissions the adoption does not explain are flagged in the per-theme record, not dispositioned here.

### 1. Credit and attribution

- **What:** The original carries no credit block at all (a bare `[[module Rate]]` at original L42–44 is its only furniture). The candidate carries the preview credit block (candidate L104–114) with the eight ruling-3 fields plus a ninth line, **翻訳について:**, recording that the text adapts KanekoLiku's existing translation (the ruling-3 form for a modified human translation; the human translator's name is kept, as ruling 3 requires). **著作権者:** ©CityToast. The original mirror names no theme author in its body (its names are Woedenaz, author of the base SCP Offices theme, at original L95, and an approval comment by Croquembouche at original L293–295); CityToast is the production page's **著者:** (visible in the phase17-diff file's context lines), carried over with the adoption. No license box exists on either side (T4: none — the original has none and the candidate adds none; the production page likewise carries only the credit block). No T7 credit-module CSS is added; the preview module supplies the credit furniture. The original's bare Rate is removed (P3): the preview credit block is rate-bearing, so no rating surface is lost.
- **Why:** P3/T1 (credit block swap; the branch-original credit form does not render here), ruling 3 (translator credit and adaptation line), KB-09 (no duplicate or orphaned bare Rate beside a rate-bearing credit block).
- **Verify:** Read candidate L103–114; `grep -c 'module Rate' candidate.txt` (0); the phase17-diff file in `pages/` shows the production credit block's author line.
- **Disposition:** FIXED (P3 credit fields, credit waves; ledger §(c3)) and standing.

### 2. Includes and components

- **What:** Original includes: `:scp-wiki:component:interwiki-style` ×3 (priorities 1, 2 for BHL; priority 4 for its own code block, original L289–292), `:scp-wiki:component:theme-squares` (the colour exhibit, original L50–80), and a hidden `:scp-wiki:theme:scp-offices-theme` include (original L281–285). Candidate includes: `:scp-jp:component:interwiki-style` ×3 (priorities 1, 2 for BHL; priority 3 with its theme parameter dropped by remedy, section 3) and the `:scp-jp:credit:start-preview` / `end-preview` pair. The theme-squares exhibit is not carried (the documentation body lives on the production page, section 6). The Offices include has no counterpart in any form — flagged in the per-theme record.
- **Why:** P1 (branch repoint of shared components), P6/T3 (interwiki-style frame), ruling 4 (a needed component is ported with the theme — the ground the Offices flag is judged against).
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the lists.
- **Disposition:** Repoints standing; the Offices omission is a flag (per-theme record), not a disposition.

### 3. Delivery and code loading

- **What:** The theme's own CSS moves channel: in the original it sits in a `[[code type="css"]]` exhibit (original L201–277) and is delivered by a tail module @import of its own local--code /1 plus the priority-4 interwiki-style include (original L286–292). In the candidate the same body (topology match, similarity 0.885) is inlined into the head module (candidate L14–86), behind the BHL @imports whose host changes nu-scptheme.github.io → scp-jp.github.io (P4/T9, DELIVERY-HOST span in B1); the tail self-delivery @import is deleted with the move (the classifier's DUPIMPORT-DEL span in B3 — the BHL dual channel, module @import plus interwiki priorities 1/2, is retained exactly as in the original and the production page). The candidate's priority-3 interwiki-style include (candidate L99–101) stands with no theme parameter: until commit 5d95177 it named the candidate's own draft-host local--code /1, and 5d95177 dropped the parameter under sub-shape (D) of the frame-address audit (FIX-FRAMED record): the candidate contains no code block in any form (census 0), so the named block was verifiably dead, and the drop remedy (D)→(B) applies. The original's priority 4, by contrast, named its live code block. Separately: the original's Offices layer (hidden include, original L283) and the production page's Offices load (its priority-3 include naming scp-jp.github.io's style0.css) have no counterpart in the candidate — the candidate loads BHL and its own layer only. Flagged in the per-theme record.
- **Why:** P4/T9 (base delivery from the JP distribution), P6/T3 (layered priorities: 1 normalize, 2 base, 3 own — the candidate's own layer is inlined, so its slot stands empty after the (D) remedy), KB-07 (interwiki-style parameter discipline), the frame-address ruling (sub-shape (D) treated as (B)).
- **Verify:** `grep -c '\[\[code' candidate.txt` over all typed forms (0); read candidate L89–101; `git show 5d95177 -- pages/theme:scp-human-resources-jp.txt` for the dropped parameter.
- **Disposition:** Delivery form standing (the standalone shape is declared in the candidate's own prose, candidate L118); priority-3 remedy recorded (5d95177); Offices omission flagged (per-theme record).

### 4. Fonts and assets

- **What:** The Zilla Slab Google Fonts load is carried verbatim (candidate L6; FONT-IMPORT spans). FIX5's pattern-7 fix adds the Noto Sans JP load (candidate L12) under a bilingual porter comment (candidate L8–11) and suffixes the face into three stacks (candidate L18, L19, L54; JPFONT-LOAD in B3, JPFONT-STACK in B13) — the item 6 re-derivation in the per-theme record. The logo: `--logo-image` is repointed from the EN wiki's file host (original L227) to the JP storage copy `scp-jp-storage.wdfiles.com/local--files/file%3A7657035-44-ziy1/hrlogo.png` (candidate L37; ASSET-REHOST in B9) — the same hosted copy the production page uses. The original's exhibit image (original L83, the logo with a dorktoast.wdfiles.com link target) is not carried, with the body. No font is named in a stack but unloaded (Zilla Slab and Noto Sans JP are both loaded; the "IBM Plex Mono" of the original's dropped exhibit prose, original L194, names no stack in either file's CSS).
- **Why:** P7/T5 and ledger class D / KB-16 (a JP face must be loaded and named in the stacks it serves; the failure prevented is Japanese header text falling back to a Latin-only face), P5 (assets re-hosted to JP storage).
- **Verify:** `grep -n '@import' candidate.txt` (three loads: BHL pair in section 3, Zilla Slab, Noto Sans JP); read candidate L16–19 and L51–56.
- **Disposition:** FIXED (item 6, FIX5-FONTSA); logo re-host standing.

### 5. Header, sidebar, and site furniture

- **What:** `--header-subtitle`: the original's code block sets `"HUMAN RESOURCES DEPARTMENT"` (original L228); the candidate sets `"人事部門"` (candidate L38) — the production theme's Japanese name, carried with the adoption (header language would in any case fall under ruling 2, but here the JP form is the production page's own, not a porter's choice). `--logo-image` is section 4. The sidebar/interwiki heading rule (candidate L51–56) is one of the three stacks the pattern-7 fix suffixes. The theme-squares colour exhibit is not carried (section 2); the colour variables themselves are carried unchanged in the moved CSS body (candidate L23–31 against original L213–221).
- **Why:** P9/T6 (header variables), ruling 2 (header language as taste — noted, not needed here), KB-16 (the heading rule's stack is a pattern-7 locus).
- **Verify:** Candidate L37–38 against original L227–228.
- **Disposition:** Standing (production form).

### 6. Text translation

- **What:** The candidate's body is not a translation of the original's body. The original carries a 190-line documentation body (original L42–279: Rate exhibit, theme squares, usage, examples, font specimens). The candidate replaces it with a twelve-line Japanese statement (candidate L116–126): what the page is (a standalone port of SCP-JP's 人事部門テーマ）, how to use it (one include line naming its own posting name, candidate L120), credits, the re-translation revision line, and a source line citing the production page. The documentation itself lives on the production page (change set). Inside the moved CSS body, the English comments (`/* Typefaces */`, `/* Standard Colors */`) are carried verbatim. No text in the candidate is left untranslated: its prose is Japanese throughout, with the theme's English name kept as a name.
- **Why:** This is the K6/R4 shape declared in section 0, stated here so the translation section does not pretend a line-by-line P10 pass exists for a body that was replaced, not translated. The T5 verdict word for this theme (LOCALIZE-ROWS row 32) judges T4/T5 jointly and its charges were P3/P6/P7, all closed.
- **Verify:** Read candidate L116–126; compare the production page's body in `pages-existing/existing:theme-scp-human-resources.txt`.
- **Disposition:** Recorded (K6 adoption); no open translation item.

### 7. Links

- **What:** The candidate's outbound links are the credit source link (candidate L113, to the EN original — the recorded host in review/sources.tsv is scp-wiki, and the link matches it) and the production-page citation in its closing source line (candidate L126). The original's prose links (to theme:scp-offices-theme and theme:black-highlighter-theme, original L95–97) are not carried, with the body. No candidate link names a page that will not exist: its one usage exhibit names its own posting name (candidate L120).
- **Why:** P11 (hub/target links must resolve on the JP wiki); the dead-link family is the failure prevented.
- **Verify:** `grep -n 'http' candidate.txt` (five URLs: BHL pair, two font loads, storage logo, credit source link, production citation).
- **Disposition:** Standing; no link item charged or found.

### 8. Structure

- **What:** A whole-file restructure (the diff is one hunk). Preserved: the CSS body's internal order and declarations (the localize.md closing rule holds inside the moved body: variable names, selectors, and rule order match the original's code block rule for rule, apart from sections 4–5). Replaced: the exhibit body (EXHIBIT-RESTRUCTURE spans B3 and B20). B3 (original L13–202 → candidate L8–12) is the collapse of the head module's tail and the entire exhibit body into the font-fix comment region — replaced, ground: production adoption (the exhibits live on the production page). B20 (original L280–295 → candidate end) is the tail frame: hidden Offices include, tail delivery module, priority-4 include, and the approval comment ("Theme approved by Croquembouche 4/16/21") — replaced by the candidate's closing credit and source lines; the Offices part is the section 3 flag, and the approval comment is not carried anywhere in the candidate. The gate moved: the original wraps everything in `+theme`; the candidate gates only credit and body (`+テーマ`, candidate L103, P2).
- **Why:** R3 (exhibit restructuring needs its ground stated: here, adoption), R4 (the replacement body is the production form), P2 (tag localization).
- **Verify:** Structural census: `grep -n '\[\[module\|\[\[code\|\[\[iftags\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Recorded; the Offices omission is flagged in the per-theme record.

### 9. Formatting only

- **What:** WS-ONLY spans fire in 12 of the 20 blocks: the moved CSS body is re-indented from the original code block's tabs to the candidate module's four spaces throughout (e.g. original L207–208 against candidate L17–18). The classifier pairs 0 re-indentation blocks only because the channel move masks the pairing; the shape is visible in the diff. This is R7 formatting normalization riding inside the DELIVERY-MOVE, stated so the move's line churn is not mistaken for rule edits: the declaration-level comparison (per-theme record) shows the rules unchanged apart from sections 4–5.
- **Why:** R7 (wholesale re-indentation is disclosed as its own class; it is also why this package's diff cannot be read as 339 independent line edits).
- **Verify:** `sed -n '201,277p' original.txt` against `sed -n '14,86p' candidate.txt` with leading whitespace stripped.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Two annotations, both inside the head module: the delivery comment `/* Black Highlighter base (SCP-JP distribution) */` (candidate L2) and the bilingual JP-font comment added by FIX5-FONTSA (candidate L8–11), which states the pattern-7 ground in English and Japanese. The candidate's replacement body (candidate L116–126) is porter-authored text, counted in section 6 rather than here. No other annotation exists; the classifier's COMMENT-TEXT span (in B3) is the FIX5 comment.
- **Why:** R2 (porter additions are listed so they are never mistaken for original content).
- **Verify:** Read candidate L2 and L8–11.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** (1) T1: PASS outright — baseline exit 0, 0 errors / 1 warn / 0 infos (T1-ROWS row 32); the single warning is recorded verbatim there and carries no classification. (2) The render row's findings are all DISPOSITIONED in the cross-cutting families named in the Status table (KB-33/KB-34 overflow and preview chrome, KB-36 WebKit glyph, KB-32 preview-form modal). (3) The stamp's STALE is fully explained by the 5d95177 frame remedy (section 3), a post-verdict change the refresh records; it is not an unjudged edit. (4) Two items are **flags, not dispositions**: the Offices layer omission and the `.scp-image-block` rules drop (per-theme record). No ledger row dispositions either, and this package does not invent a disposition for them.
- **Why:** A disposition is a decision with grounds; items without grounds are carried as flags so the coordinator can decide them with the evidence attached.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (items 1–3); flags open (item 4).

### 12. Verification

- **What:** (a) T1 checker baseline: PASS (stamp; T1-ROWS row 32). (b) T2/T3: FINDINGS, every finding dispositioned in ledger §(c2) (RENDER-C row 32). (c) T4 follow-up: LOCALIZE-ROWS row 32 records display-affecting findings 2 (P6 frame, P7 font); P6 closed by the frame waves, P7 by FIX5 (item 6). (d) FIX5 re-derivation: per-theme record below. (e) This package: `python3 review/build_review.py --check` — this package is not in the stale set (the stale set is byte-identical with and without this batch's three packages; set comparison in the batch report). (f) Brace depth: both files' CSS is balanced (comment/string-stripped counts: the candidate module's 8 block opens — @supports, :root, and six rules — match the original code block's 8; the original head module's separate 5 opens are the logo :root plus the four image-block rules of the flag below).
- **Why:** Verification claims name the cheapest deciding check and its result.
- **Verify:** Re-run the checker on `pages/theme:scp-human-resources-jp.txt`; re-run `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### Ledger item 6 [D] — the pattern-7 fix, re-derived

The ledger charge (§(e) item 6): pattern 7 — the header subtitle sits in a Latin-only face (display-affecting); the current file names and loads no JP font, and no disposition ground covers a missing JP face. The supplement (row 6) re-judges it FIXED by FIX5-FONTSA, commit 8eacd6e, "pattern-7 fix; checker code-multiset identical before/after". The commit's diff for this file is exactly the fix and nothing else: it adds the Noto Sans JP @import (now candidate L12) with its bilingual explanatory comment (candidate L8–11), and suffixes `'Noto Sans JP'` into three stacks — `--header-font` (candidate L18), `--title-font` (candidate L19), and the sidebar/interwiki heading rule's `font-family` (candidate L54). The subtitle itself reads 人事部門 (candidate L38) and renders through `--header-font`, so the charged locus (subtitle in a Latin-only face) now has a loaded JP face in its stack. The current candidate carries all four elements byte-for-byte as the commit left them (the only later change is the unrelated 5d95177 parameter drop). **FIXED, confirmed from the bytes.**

### Flag 1 — the SCP Offices delivery layer is not loaded

The original is an extension of the SCP Offices theme and loads it: a hidden include at original L281–285 (`[[include :scp-wiki:theme:scp-offices-theme]]` inside a `display: none` div, the BHL-era layering form), on top of BHL. The production page loads the same layer as CSS (its priority-3 interwiki-style include naming `https://scp-jp.github.io/files/theme/scp-offices-theme/style0.css`). The candidate loads neither form: `grep -c offices candidate.txt` is 0, and its layering is BHL (module imports + priorities 1/2) plus its own inlined CSS. A JP candidate for the layer exists in this repo (`pages/theme:scp-offices-theme-jp.txt`). The candidate's prose declares a standalone form ("Black Highlighter を基盤としています", candidate L118), which states the choice but does not disposition it: no ledger row charges or dispositions this layer for this theme (the T4 row's charges were P3/P6/P7). Recorded for the coordinator: either the standalone declaration is accepted as the theme's JP form (and this flag closes as a disposition with that ground), or the Offices layer is restored in one of its two attested forms. This is the as-built state; the layer has since been restored in the hidden-include form (FIX-RFIX10 HR-1, landing 8c935d3) — see Post-package repairs (REFRESH3-E).

### Flag 2 — the head module's `.scp-image-block` rules are dropped

The original's live head module carries four rules styling floated image blocks (original L9–30: `.scp-image-block.block-right` margins, `.scp-image-block a` width, `.scp-image-block img` border, and the two `#page-content > div.scp-image-block` background/padding rules). The production page carries the same rules in its own head module (6 `scp-image-block` occurrences). The candidate carries none: `grep -c 'scp-image-block' candidate.txt` is 0. These rules are live theme CSS, not exhibits: they style any floated image block on any page using the theme. Their absence is a rendering difference from both sources in this package. The candidate's own body uses no image block, which is why nothing on the candidate page itself shows it. Recorded for the coordinator with the loci above; not edited here. This is the as-built state; the five rules have since been restored verbatim (FIX-RFIX10 HR-2, landing 8c935d3) — see Post-package repairs (REFRESH3-E).

### The priority-3 slot

Recorded in section 3: the empty priority-3 include is the frame-address audit's sub-shape (D) remedy (commit 5d95177, FIX-FRAMED record), applied because the candidate has no code block for the parameter to name. It is also the whole explanation of this package's STALE stamp: the verdict-era file (435a6bb) still carried the parameter; the remedy postdates the verdict.

### Post-package repairs (REFRESH3-E)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/theme:scp-human-resources-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**Frame sub-shape (D) treated as (B) — already in this package.** For the record chain: the priority-3 slot recorded above is this theme's FIX-FRAMED remedy. Its frame was sub-shape (D) — `theme=` named its own /1 code block, which the candidate (no `[[code]]` block; CSS in live `[[module CSS]]`) cannot contain — treated as (B) with the minimal remedy of dropping the `theme=` line and keeping the include, priority, and all else; the priorities 1 and 2 frames name the BHL GitHub Pages files and are untouched. The remedy landed at 5d95177 and predates this package's build (4b0f499), so no frame byte postdates the build.

**FIX-RFIX10 — the two open Flags closed (landing 8c935d3).** `FIX-RFIX10.md` records two repairs to this file, both postdating the package; the commit is +27/−0 in two hunks:

- **HR-1 (closes Flag 1 — SCP Offices layer).** The original's hidden include form is restored in the candidate's own frame structure: after the interwiki-style includes and before the `[[iftags +テーマ]]` gate, `[[div style="display: none"]]` / `[[include :scp-jp:theme:scp-offices-theme-jp]]` / `[[/div]]` (target repointed to the `-jp` candidate per cross-theme-delivery ruling 1). The candidate's empty priority-3 slot was deliberately not used — it remains the separate frame (D) remedy above.
- **HR-2 (closes Flag 2 — `.scp-image-block` rules).** The 22-line block from the original's head module (original L9–30, extracted programmatically, not retyped) is inserted verbatim in the candidate's head module after the `@supports`/`:root` block, before `[[/module]]`. The candidate now has 5 `scp-image-block` occurrences (the five restored rules).

The checker finding set is unchanged (error 0 / warn 0 / info 0 before and after; no new class (i) finding). Flags 1 and 2 above are recorded as the as-built state and are closed by these repairs; the recopied candidate carries the restored Offices layer and image-block rules.

## Change set outside the two diffed files

(1) `pages-existing/existing:theme-scp-human-resources.txt` — the production page (305 lines), this port's third source: credit form, logo hosting, Offices load, and documentation body all live there. (2) `pages/phase17-diff-scp-human-resources-jp.txt` — the migration's production-side delivery: a one-line diff adding **改訳時参照リビジョン:** 14 to the production page's credit block. (3) `pages/theme-decoration-sample-scp-human-resources-jp.txt` — the decoration sample used by the render checks. (4) `pages/theme:scp-offices-theme-jp.txt` — the JP candidate for the unloaded layer of Flag 1. The sibling theme:scp-human-resources-sigma-jp is a separate theme with its own package.

## Appendix — classifier adjudication

No residue and no heuristic blocks (20 specific of 20). Two labels need adjudication against the bytes. (a) RATE-EXHIBIT-KEPT-CANDIDATE (span in B3): a false fire. B3 spans original L13–202, which contains the original's bare Rate (original L43), against candidate L8–12, the font-fix comment region. The candidate contains no `[[module Rate]]` (grep count 0); the original's bare Rate was removed under P3 (section 1). The label describes the original side of the hunk, not a kept exhibit. (b) DUPIMPORT-DEL (span in B3): the deleted import is the tail self-delivery @import of the original's local--code /1 (original L287), subsumed by the DELIVERY-MOVE inlining (section 3); the BHL dual channel is retained, so no BHL import was deleted. The WS-ONLY spans are adjudicated in section 9.

## License and attribution

- **Title:** Human Resources Theme
- **Author:** ©CityToast
- **Source:** https://scp-wiki.wikidot.com/theme:scp-human-resources — revision 14 (revision date 2023-01-06 08:48:09)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: KanekoLiku — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
