# Review package — theme:suprematism-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:suprematism-jp — origin CN, population #235 [GOSIGN2-LEDGER (b) row 235]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7e0d5949b9b6e2e6e047050ee5211a0792dab209672a1c25fa7a38d017e2c952); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 14 errors / 0 warns / 0 infos (hotlink×11, pseudo-ref×2, old-bhl×1); standing classes dispositioned in register c1 [T1-ROWS row 195; GOSIGN2-LEDGER (b) row 235]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 454px@320/375 on page and sample + sidebar-unreachable at 375/320 + runtime-hotlink site-theme chain + candidate hosts cdn.jsdelivr.net, lemoncat233.github.io, nu-scptheme.github.io; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN15)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN15)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 234, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 234]
- FIX5 re-judgement: items 91 (class H) FIXED, 92 (class I) FIXED — FIX5-STRUCTA, commit 8c0cd35: credit title -> (JP form matching the body); credit author field -> LemonCat233 & Liurd; all 11 #ifexpr preset bodies restored verbatim from original L669-972 into the existing shells, one JP adaptation in the restored scp preset (old-BHL host -> scp-jp.github.io, the KB-17 named rewrite); spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) items 91–92; (c) check 5]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:suprematism-jp.txt sha256:7e0d5949b9b6e2e6e047050ee5211a0792dab209672a1c25fa7a38d017e2c952; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 91 [H] (credit fields) and item 92 [I] (emptied preset blocks) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md rows 91 and 92: both **FIXED** (FIX5-STRUCTA, commit 8c0cd35); supplement §5 spot-check 5: PASS |
| Standing items | **DISPOSITIONED** — ledger §(c3): P1 (posting-procedure convention), P4 (delivery, class (ii)), P5 (class (ii) / KB-58), P9 (ruling 2); ledger §(c2) render row: foreign-host delivery class (ii) (KB-41/KB-54 family), credit-modal preview form (KB-32); KB-17 old-bhl line (class (ii)) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:suprematism | theme:suprematism-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 7, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 7 | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-suprematism.txt` (fetched once by the LOCALIZE-S2-E lane; its working diff is `diff-suprematism-from7.txt` in the same lane directory) | Canonical file `pages/theme:suprematism-jp.txt`, copied at worktree HEAD c196257; the file's last content change is commit 8c0cd35 (FIX5-STRUCTA) |
| Lines / bytes | 972 lines / 27,936 bytes (the file's last line carries no trailing newline, so `wc -l` reports 971) | 1,052 lines / 34,686 bytes |
| SHA-256 | 38f866dea559ba25fbb06e89295a412cad5427ec0715d73aff1e57f98fb0ccaf | 7fccdaa1e8432bd5c4d0602cdd1258126383474655ae988ac3513ea6b4ac09a4 |

## Summary

The original is a thin shell: its main stylesheet is not in the page at all (it is imported from the author's GitHub Pages and from a fragment on another wiki), and the page body is an exhibit gallery wrapped around that delivery. The candidate is self-contained: the base stylesheet is re-hosted as a JP candidate fragment, the theme's own CSS is consolidated into the page's own code block and delivered from it, and the exhibit body is translated. The measured churn (diff.md: +498/−418, 916 changed lines in 110 change blocks) is therefore mostly delivery relocation and exhibit restructuring, not 916 lines of independent edits. Two defects found by the sweep (a stripped credit co-author and eleven emptied preset blocks) were restored by FIX5; the remaining oddities a reviewer will spot (an old BHL host in one preset copy, Chinese display strings in two presets, author-hosted exhibit images) are standing dispositions, argued in the per-theme sections below rather than hidden.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with a delivery header (original L1–18): a `[[module ThemePreviewer]]` pointing at the EN Black Highlighter normalize stylesheet on cdn.scpwiki.com, the base-fragment include (L3), and a `[[module css]]` importing the author's GitHub stylesheet. The candidate has no header frame at all: it opens with the exhibit gate `[[iftags +テーマ]]` and the credit block (candidate L1–12). Provenance route: this package's original is the lane-cached page source at revision 7 (see Provenance); no live re-fetch was made for this package.
- **Why:** The header frame is where the original declares its delivery; removing it without a replacement delivery would leave the candidate unstyled. The replacement is recorded in section 3.
- **Verify:** Read original L1–18 against candidate L1–12.
- **Disposition:** Recorded; part of the delivery change argued under "Disposition argument 3".

### 1. Credit and attribution

- **What:** The original carries two credit exhibits inside the body (`:scp-wiki-cn:credit:start` at L81–86 and `credit:start-standalone` at L88–93), both naming LemonCat233 & Liurd. The candidate carries one credit block at the top of the page (`:scp-jp:credit:start-preview`, candidate L3–12) with the eight standard fields; the exhibit copies in the body became plain prose name/author lines. FIX5 repaired two fields in that block: the title (L4, from the untranslated CN title to the Japanese form the body itself uses) and the copyright holder (L8, from "Liurd" alone to "LemonCat233 & Liurd", restoring the dropped co-author). The original-title field and the source-link field correctly keep the CN title, as quotations of the original.
- **Why:** Ledger charge classes P1/P3 as charged in §(e) item 91 [H]: a credit block that drops a co-author and leaves the title untranslated misattributes the work and contradicts the page's own body. Ruling 3 (2026-11-16) fixes the translator credit form used in the block (翻訳責任者: AI).
- **Verify:** Read candidate L3–12 against original L81–93 and the license box (candidate L370–379); the supplement spot-verified L4/L8 after the fix.
- **Disposition:** FIXED (ledger §(e) item 91; supplement row 91).

### 2. Includes and components

- **What:** Original includes: the base fragment `:backrooms-wiki-cn:fragment:suprematism` (L3), two credit component forms (L81–93), `component:image-block` (L97), and `:scp-wiki-cn:component:license-box-theme` + end (L654–663). Candidate includes: `:scp-jp:credit:start-preview` / `end-preview` (L3/12), `component:image-block` (L38, same component, Japanese caption), `:scp-jp:component:license-box` + `license-box-end` (L370/379), and the delivery frame's `:scp-jp:component:interwiki-style` (L1049–1052). The license-box includes were repaired earlier by FIX2-INCLUDE. The backrooms fragment include has no include counterpart in the candidate: its role is taken over by the re-hosted base fragment delivered by @import (section 3).
- **Why:** Component localization (branch forms of shared components) and ruling 4 (2026-11-16): a component or fragment the theme needs is ported together with the theme, which is what the base-css fragment in the change set is.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** FIXED / standing as recorded; no include in the candidate points at a CN-wiki page.

### 3. Delivery and code loading

- **What:** Original delivery is external on three channels: the ThemePreviewer theme_url (BHL normalize, cdn.scpwiki.com), the @import of `suprematism.css` from the author's GitHub Pages (original L5–16), and the backrooms-wiki-cn fragment include (L3). The page's own CSS in the original is only the banner module (L20–59) and the preset modules (L669–972). Candidate delivery is a closing frame (candidate L1045–1052): a `[[module css]]` importing two local--code deliveries on the draft host (the base fragment's code block and this page's own code block), plus an interwiki-style include at priority 1 naming the page's own code block. The theme's own CSS is consolidated into that single `[[code type="css"]]` block (candidate L684–1040), which is both the displayed "source code" exhibit and the delivered stylesheet. Draft-host URLs are the draft-form class (iii): they are rewritten to the production host at posting time.
- **Why:** Own-code delivery via interwiki-style is the campaign's standard supplement frame for page-source themes; it removes the candidate's runtime dependence on the author's personal hosting and on a third wiki's fragment, which the ledger dispositioned for the original as delivery class (ii) (P4: original-state CDN delivery).
- **Verify:** Read candidate L1043–1052; confirm `pages/fragment:suprematism-jp-base-css.txt` exists in the canonical repo (change set, below).
- **Disposition:** DISPOSITIONED (ledger §(c3) P4; the two draft-host @imports stand as the checker's pseudo-ref lines, class (iii)).

### 4. Fonts and assets

- **What:** Exhibit images are hosted on the author's GitHub Pages in both files (12 URL occurrences in the original, including the stylesheet @import; 11 in the candidate, all exhibit images — these are the checker's 11 standing hotlink errors). Font stacks: the original's variable exhibits name the CN fonts (e.g. Noto Sans SC); the candidate's consolidated code block names Noto Sans JP in the body/UI stacks (candidate L1036–1038) while the mono stack keeps Noto Serif SC. The larger font replacement (Noto Sans SC → Noto Sans JP throughout the base stylesheet, Bootstrap Icons via jsdelivr kept, Zhuque Fangsong dropped as outside the direct-link exceptions) lives in the base fragment, outside the two diffed files (change set, below).
- **Why:** KB-17/KB-18 family (font delivery hosts; text inside CSS). Author-hosted exhibit images are original-state delivery, T1 class (ii): the pages render styled today and no error-box defect arises from these hosts (ledger §(c2) render row, KB-41/KB-54 family).
- **Verify:** `grep -c lemoncat233.github.io` on both files (12 / 11); read the header comment of `pages/fragment:suprematism-jp-base-css.txt`.
- **Disposition:** DISPOSITIONED (class (ii), posting-time or original-state delivery as recorded in the ledger).

### 5. Header, sidebar, and site furniture

- **What:** The theme's furniture controls are its eleven `#ifexpr` preset blocks (static-header, left-header, no-header-desktop, collapse-sidebar-desktop, show-sidebar, fullscreen, big-banner, minecraft, no-banner, evernight, scp): original L669–972, candidate modules L382–679, each an `[[iftags #ifexpr]]` shell wrapping one `[[module css]]` body. At ledger time the candidate's eleven shells stood empty and the presets did nothing; FIX5 restored all eleven bodies verbatim from the original (see the per-theme section). The minecraft and scp presets carry Chinese display strings, kept verbatim (Disposition argument 2).
- **Why:** Ledger §(e) item 92 [I], structural mangling (cross-cutting class 5): the presets are the theme's headline feature, and reader-visible preset switches that do nothing are a display defect, class (i) — so this one was fixed, not dispositioned.
- **Verify:** Count the shells and bodies: `grep -c '#ifexpr' candidate.txt` (11) and the module blocks between candidate L382–679 (11); supplement §5 spot-check 5 records the same count.
- **Disposition:** FIXED (item 92); the Chinese strings inside two presets are DISPOSITIONED under ruling 2 (P9).

### 6. Text translation

- **What:** The exhibit body is translated throughout (original L19–664 → candidate L1–380): the introduction (the banner subtitle line at candidate L14 is the translation of the original's module-level subtitle), section headings (例 / プリセット / カスタマイズ for the original's 示例 / 预定义 / 自定义), exhibit captions, collapsible labels, heading samples, and the footer navigation text. Deliberately untranslated text is confined to the two preset display-string sets (section 5) and to quotations of the original inside the credit block (section 1).
- **Why:** Translation of the theme's documentation body is the port's purpose (the candidate is the JP edition of the theme page, not only of its CSS). The untranslated remainder is not an oversight; it is dispositioned (P9, ruling 2).
- **Verify:** Read candidate L14–380 against original L60–664 section by section; the translated headings align one-to-one.
- **Disposition:** Standing (the port itself); exceptions DISPOSITIONED as above.

### 7. Links

- **What:** The candidate's source link points back to the original page (credit block, candidate L11). User links in the introduction name both authors in `[[*user …]]` form (candidate L16). No prose link in the candidate targets the un-suffixed `theme:suprematism` name. The inbound side of this theme's links was repaired in another file: theme:trauma-jp carried a dead prose link to `theme:suprematism` (a page that does not exist on SCP-JP), repointed to `theme:suprematism-jp` by FIX5-TEXTB (ledger §(e) item 95, FIXED in the supplement).
- **Why:** Dead-target links (P11 family) fail at click time on the posted wiki; a theme's link surface includes the links other candidates point at it with.
- **Verify:** `grep -n 'theme:suprematism' candidate.txt` (only the -jp self-reference and the CN source URL should appear); item 95's fix is in `pages/theme:trauma-jp.txt`.
- **Disposition:** FIXED (item 95, in the trauma-jp file); no open link item in this file.

### 8. Structure

- **What:** Three structural changes beyond translation. (a) Exhibit restructuring: the original presents its CSS variables as six `[[code type="CSS"]]` exhibits inside the customize tabview (original L423–641) and carries a separate module CSS block for the presents gallery (original L231–250); the candidate removes both from the body and consolidates all of the theme's own CSS into the single trailing code block (candidate L684–1040), which also absorbs the banner module (original L20–59) and copies of three preset bodies (minecraft, evernight, scp). (b) Placement: that code block sits inside the scp preset's ifexpr gate (the gate opens at candidate L591 and its `[[/iftags]]` closes at L1043), where the original's exhibits sat in the open exhibit body — a placement a reviewer should notice, recorded here because the diff alone does not explain it. (c) The two in-body credit exhibits became the single top-of-page credit block (section 1). The diff's own alignment shows the strain: diff section 18 aligns the candidate's whole tail (L676–1052) as one insertion, and section 11 shows the original's exhibit region collapsing by 222 lines; the relocation is real, the line pairing is the differ's.
- **Why:** Residue class R3 (documentation/sample exhibit restructuring; this theme is one of its confirmed instances). Consolidating the own CSS into one code block is what makes the own-code delivery of section 3 possible: the delivery and the exhibit are the same block.
- **Verify:** Compare the structural maps: `grep -n` for `[[module`, `[[code`, `[[iftags` in both files.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** Minor. The restored preset bodies are verbatim, so no re-indentation was introduced by the restoration. The purely formatting residue of the whole diff is the set of single blank-line deletions at preset boundaries (diff sections 12–17, one deleted line each; the generator's heuristic counts 8 mechanical blocks / 11 lines in total, which also covers token-level host and branch substitutions). There is no wholesale re-indentation in this package.
- **Why:** Formatting-only churn is disclosed as its own class so a reviewer does not have to re-derive it from the diff, and so it is never mistaken for semantic change (the negative-ledger rule for re-indentation, R7, is not triggered here).
- **Verify:** Diff sections 12–17 in diff.md (grouped under "Purely mechanical sections").
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One porter annotation was added inside the candidate: the header comment of the consolidated code block (candidate L685), which states in Japanese that the block is the theme's own CSS and that the Suprematism base is imported from fragment:suprematism-jp-base-css. It is the only place inside the two diffed files that explains the delivery split; the base fragment carries its own longer header comment (outside these files, change set below).
- **Why:** Residue class R2 (porter annotation additions): annotations added by the porter are part of the change record, and this one is load-bearing — it is the pointer a future editor needs before touching the code block.
- **Verify:** Read candidate L684–686.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in full in the per-theme sections or the ledger rows cited: (1) the old-BHL logo URL — two copies in the candidate, one JP-adapted by FIX5, one standing as KB-17 class (ii) (Disposition argument 1); (2) Chinese preset display strings kept under ruling 2 (Disposition argument 2); (3) original-state foreign-host delivery for the base stylesheet and exhibit images, class (ii) (sections 3–4); (4) draft-host local--code URLs, class (iii) draft form, rewritten at posting (section 3); (5) render-row dispositions: page-overflow findings and the credit-modal preview form (ruling 5; KB-32) recorded in ledger §(c2). No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the campaign checker reports identical totals for this file before and after FIX5 (14 errors / 0 warnings / 0 info; the 14 are the standing classes: 11 hotlink, 1 old-bhl, 2 pseudo-ref), so the restoration introduced no new error; (b) the supplement's re-judgment spot-verified the restoration (11 shells, 11 preset module bodies, credit L4/L8) and marked §5 spot-check 5 PASS; (c) render checks T2/T3 produced dispositions only, no open finding (ledger §(c2)); (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib, autojunk off): +498/−418. A GNU-diff count of the same pair gives 918 changed lines; the difference is alignment choice, not content.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:suprematism-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### The FIX5 restoration (ledger items 91 and 92)

At ledger time this candidate had two blocking defects. Its credit block named only one of the theme's two authors and kept the untranslated CN title (item 91 [H]). Its eleven `#ifexpr` preset shells stood empty — the preset CSS had survived only inside the static code exhibit, so every documented preset switch did nothing (item 92 [I]). FIX5-STRUCTA (commit 8c0cd35, the file's last content change) repaired both in three hunks: two credit lines (candidate L4 and L8), the preset region (eleven bodies restored verbatim from original L669–972 into the existing shells), and one line in the code exhibit (the logo URL adaptation in Disposition argument 1). The lane's checker run is the control: verbatim restoration alone raised the error count from 14 to 15 (the restored scp body re-added the old-BHL host), and the one-line adaptation returned it to the baseline 14. Lane report: REPORT-GOSIGN2-FIX5-STRUCTA.md; re-judgment: GOSIGN2-LEDGER-SUPPLEMENT.md rows 91–92 and §5 spot-check 5.

### Disposition argument 1 — the two copies of the BHL logo URL

The original has one `--logo-image` line (original L917, in the scp preset module) pointing at the old BHL host `nu-scptheme.github.io`. The candidate has two copies, because it carries the scp preset twice: in the gated module (candidate L592–678; the logo line is L624) and in the consolidated code exhibit (the logo line is L812). FIX5 restored the module copy verbatim, old host included, and applied the KB-17 named rewrite to the exhibit copy (candidate L812 now reads `scp-jp.github.io`). The standing checker error is therefore the module copy at L624, and its disposition is KB-17 class (ii): at posting time the old-BHL host is rewritten to scp-jp.github.io/Black-Highlighter by the posting procedure (AGENTS.md §3 old-bhl rule), and fix lanes leave class (ii) lines untouched. Two cautions for the reviewer. First, the split is deliberate but asymmetric: only one of the two copies was adapted in the repo, so until posting, the gated scp preset and the delivered exhibit disagree about the logo host; the class (ii) rewrite closes that gap at posting. Second, the FIX5 lane report describes these two copies with their roles swapped (it calls L812 the "restored live block" and L624 the "exhibit copy"); the git diff of commit 8c0cd35 shows the one-line adaptation landing in the exhibit copy and the module copy restored verbatim, and this package follows the bytes.

### Disposition argument 2 — Chinese preset display strings kept

The restored minecraft and scp presets keep their Chinese display strings exactly as in the original (the minecraft header title and banner strings and its loading text; the scp banner title and subtitle), in both the module copies and the exhibit copies; the big-banner preset likewise keeps the author's Chinese CSS comment. This is not untranslated residue awaiting a wave: ledger §(c3) dispositioned the item (P9) under ruling 2 (2026-11-16), which places header and title language outside migration correctness as a matter of translation taste. Translating them during the FIX5 restoration would also have broken the restoration's own control (verbatim copy, checker totals unchanged). A future JP editor may localize them as an editorial choice; the migration record neither requires nor forbids it.

### Disposition argument 3 — the delivery change is part of the record

A reviewer comparing only the two page sources will under-read this port, because the original's main stylesheet is not in the original: the page is a shell around a ThemePreviewer module, a fragment hosted on the backrooms CN wiki, and a stylesheet on the author's GitHub Pages. The candidate replaces that topology with a self-contained one (re-hosted base fragment plus own code block, section 3). The delivery change is therefore not an implementation detail behind the port; it is one of the port's three substantive changes, alongside the translation and the exhibit restructuring, and it is the reason the change set below is part of this package's record. Its risk is also recorded: the candidate's styling now depends on campaign-maintained deliveries (the fragment and the draft-host local--code URLs) rather than on the author's hosting, and the draft-host URLs stand as class (iii) until posting rewrites them.

### The usage example's posting name

The include census in section 2 covers live includes; the theme's centered install example at candidate L18 is an escaped exhibit line and was not listed there. As built it read `= {{@@[[include :scp-jp:theme:suprematism]]@@}}`, naming the original's slug on the JP branch — a page that does not exist on scp-jp, under the campaign's settled rule for usage examples (AGENTS.md §6). The usage-example population sweep has since completed the name to this candidate's posting name, `:scp-jp:theme:suprematism-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724). This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/fragment:suprematism-jp-base-css.txt` — the re-hosted base stylesheet (3,482 lines): the author's GitHub `suprematism.css` with the JP font replacement described in its header comment; shared with theme:trauma-jp, and recorded as this theme's dependency in the `start-themes.tsv` row (deps column: `fragment:suprematism-jp-base-css (@import)`). (2) `pages/theme-decoration-sample-suprematism-jp.txt` — the decoration sample page used by the render checks. (3) `pages/theme:trauma-jp.txt` — carries item 95's inbound link fix (section 7). (4) The deliveries themselves: the local--code code blocks served from the draft host (fragment /1 and theme /1), which are the runtime form of files (1) and of the candidate's own code block. The original side of the change set is the two external sources the shell pointed at (the GitHub stylesheet and the backrooms fragment), neither of which exists as a file in this repo; their content enters the record only through file (1).

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave produced the initial port (translation, delivery frame, exhibit restructuring, and, as later found, the emptied preset shells and the stripped credit co-author); FIX2-INCLUDE repaired the license-box includes; the credit waves completed the credit fields that FIX5 then corrected; the FIX4 era fixed this theme's dispositions (old-bhl and foreign-host delivery as class (ii)); and FIX5-STRUCTA made the final restorations. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) items 91/92/95; GOSIGN2-LEDGER-SUPPLEMENT.md rows 91/92/95; REPORT-GOSIGN2-FIX5-STRUCTA.md (suprematism section). The go-sign re-run over that record is what the Status block certifies.
