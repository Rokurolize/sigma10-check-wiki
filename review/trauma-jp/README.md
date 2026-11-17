# Review package — theme:trauma-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:trauma-jp — origin CN, population #239 [GOSIGN2-LEDGER (b) row 239]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ee605cd60ac74024871b6a7dafe02fca440211d6e271d2776c1c11b7aef103d0); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 13 errors / 1 warn / 0 infos (pseudo-ref×12, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 204; GOSIGN2-LEDGER (b) row 239]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 517–520px@≤375 + 831px@768 (page) and 530–533px@≤375 + 831px@768 (sample) + runtime-hotlink site-theme chain + candidate hosts cdn.jsdelivr.net, lemoncat233.github.io; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN16)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN16)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 238, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 238]
- FIX5 re-judgement: item 95 (class H) FIXED — FIX5-TEXTB §3, commit 3f328d8: prose link repointed to theme:suprematism-jp (probe: unsuffixed name 404) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 95]
- Computed against: canonical commit 872057f3664b2fe570f4ca78e86406d0694e5692; candidate file pages/theme:trauma-jp.txt sha256:ee605cd60ac74024871b6a7dafe02fca440211d6e271d2776c1c11b7aef103d0; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 95 [H] (dead prose link to theme:suprematism) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md item 95: **FIXED** (FIX5-TEXTB §3, commit 3f328d8); re-derived from this package's bytes in the per-theme record below |
| Stamp state | The generated stamp above reads STALE by design: the candidate changed after the 435a6bb-era verdict, in exactly one line (the usage-example sweep completed the install example's name to the -jp posting name, canonical commit b5cb724). No re-judgement is fabricated; the frozen ledger remains the verdict record for the bytes it judged |
| Open flags from this package | Two, neither charged or dispositioned in any campaign record: the credit pointer in both attribution carriers (section 1), and the emptied #ifexpr preset gates (sections 3 and 5). Both are argued in the per-theme record; the package is written against the candidate as it stands |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:trauma | theme:trauma-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 6, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 6 | — |
| Source of this copy | Campaign mirror store `review-mirrors/orig-trauma-rev6.txt`, a byte copy (class COPY in the mirror INDEX) of the S2 lane cache `gosign2-lanes/lane-oc-gs-localize-s2-E/orig-trauma.txt`, fetched once 2026-11-16 | Canonical file `pages/theme:trauma-jp.txt` at worktree HEAD c6454ab; the file's last content changes are b5cb724 (usage-example sweep) over 3f328d8 (FIX5-TEXTB) |
| Lines / bytes | 854 lines / 20,668 bytes (the final line carries no trailing newline, so `wc -l` reports 853) | 889 lines / 24,539 bytes |
| SHA-256 | 8c37d6d46d65a92950e64c5d8fd134809a409f178eb9dbda885c10c0f23446fe (equals the review/sources.tsv mirror hash) | f147e1a0334c74851de7b2339cb5bc8c718f9eee64e15443b587f01c7e57a635 |

Provenance route: derived from the branch original at the reference revision (no production-counterpart adoption; there is no production theme:trauma page in pages-existing/). One correction is owed to this theme's review/sources.tsv note, which claims the original was "superseded upstream since the reference revision": the cited follow-up artifact (`diff-trauma-from6.txt`, campaign record) records the opposite, `theme:trauma rev6 → rev6 変更: なし` (re-checked at the current revision, no changes, empty intervening-revision table). Revision 6 is both the reference and the current revision. The correct standard form for the note is recorded in the lane report (BATCH-RFIX17.md) for the coordinator's harvest correction; this package's original.txt is unaffected (its hash equals the sources.tsv value).

## Summary

Trauma is a derivative theme: the original builds on Suprematism, importing the author's Suprematism stylesheet from GitHub Pages and the backrooms-CN Suprematism fragment, and adding a banner module, a large inline CSS module, and four parameter-gated preset modules. The candidate keeps that architecture's shape but re-plumbs every channel: the BHL base arrives as a live include, the Suprematism base arrives as an @import of the re-hosted JP fragment (shared with theme:suprematism-jp, ruling 4), and all of the theme's own CSS is consolidated into a single code block that is both the displayed source exhibit and the delivered stylesheet. The measured churn (diff.md: +290/−255, 545 changed lines in 18 change blocks) is therefore mostly delivery relocation (14 of 18 blocks carry DELIVERY-MOVE) plus the body translation, not 545 lines of independent edits. The theme's one blocking item, a dead prose link to the un-suffixed theme:suprematism, was repointed by FIX5 and is re-derived below. Two further defects that no campaign record charges are flagged by this package: the credit block and the license box both carry a pointer where the author belongs (the original names Liurd), and the four #ifexpr preset gates stand empty in the candidate's body while their CSS applies unconditionally from the code block, so the documented preset parameters cannot act.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with its delivery header inside the exhibit gate `[[iftags +版式]]` (original L1–5): a `[[module ThemePreviewer]]` pointing at the EN Black Highlighter normalize stylesheet on cdn.scpwiki.com, and the include of `:backrooms-wiki-cn:fragment:suprematism` (L4). The candidate opens outside the gate with the replacement delivery (candidate L1–11: the BHL include, the delivery module, the interwiki-style frame), then opens its gate `[[iftags +テーマ]]` at L12. Provenance route: this package's original is the mirror-store copy of the S2 lane cache at revision 6 (see Provenance); no live re-fetch was made for this package.
- **Why:** The header frame is where the original declares its delivery; replacing it is the port's delivery change, argued in section 3. The gate tag itself is localized (P2).
- **Verify:** Read original L1–5 against candidate L1–12.
- **Disposition:** Recorded; part of the delivery change argued under section 3.

### 1. Credit and attribution

- **What:** The original carries no credit block and no license box: its attribution is the intro byline (original L76: the theme was made by `[[*user Liurd]]` on the basis of Suprematism) and nothing else. The candidate adds the preview credit block at the top of the page (`:scp-jp:credit:start-preview`, candidate L13–22) with the eight standard fields, and a JP license box at the tail (candidate L882–888, T4 supplement; the original has only `#license-area` CSS rules, no box). Two of the added fields are defective in the same way: the credit block's 著作権者 field (candidate L18) reads "原語版ページの作成者に同じ（scp-wiki-cn の theme:trauma）" (same as the original page's creator), and the license box's author parameter (candidate L883) reads "scp-wiki-cn theme:trauma の作者" (the author of scp-wiki-cn theme:trauma). Both are pointers naming nobody, while the original names Liurd and the candidate's own prose names him too (candidate L38). The title field correctly uses the body's own Japanese form (トラウマ テーマ); the 原題 field correctly quotes the CN title. The original's bare `[[module Rate]]` inside a `[[>]]` block (original L87–89) does not stand in the candidate: the preview credit block is rate-bearing, so the widget renders once (census: `module rate` occurs 1× in the original, 0× in the candidate). No T7 credit-module CSS exists in either file (census: `creditButton`/`creditRate` 0× on both sides); the credit module's styling comes from the base.
- **Why:** P3/T1 for the block swap and KB-09 for the Rate removal. The pointer fields fail the campaign's TASL standard (ruling 3): the field must name the author the original names, and a pointer in place of the name breaks attribution exactly where a reader looks for it; this is the credit-pointer defect family the review pass has repaired in many sibling candidates.
- **Verify:** Read candidate L13–22 and L882–888 against original L76 and candidate L38.
- **Disposition:** **DEFECT FLAG (open)** — both carriers, one defect: the 著作権者 field (candidate L18) and the license-box author parameter (candidate L883) name nobody, where the original names Liurd. No ledger item charges it (the theme's only item is 95); flagged here and in the lane report with both loci for a repair lane. The remainder of this section's classes (preview swap, license-box presence, bare-Rate removal) are in their settled forms.

### 2. Includes and components

- **What:** Original includes: the base fragment `:backrooms-wiki-cn:fragment:suprematism` (L4) and `component:image-block` (body, the Malevich exhibit). Candidate includes: `:scp-jp:theme:black-highlighter-theme` (L1, the BHL base as a live include), `:scp-jp:component:interwiki-style` (L7–11), the credit pair (L13/L22), `component:image-block` (same component, Japanese caption), and the license-box pair (L882/L888). The backrooms fragment include has no include counterpart in the candidate: its role is taken over by the @import of the re-hosted base fragment in the delivery module (section 3), and a translator's note at the install example records the substitution (candidate L40). No include in the candidate points at a CN-wiki page.
- **Why:** P1 repoints for the standing components; ruling 4 (2026-11-16) for the fragment: a fragment the theme needs is ported together with the theme, which is what `fragment:suprematism-jp-base-css` in the change set is.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing as recorded; no foreign include stands in the candidate.

### 3. Delivery and code loading

- **What:** Original delivery is split over five channels: the ThemePreviewer normalize URL, the fragment include, a `[[module css]]` importing the author's GitHub `suprematism.css` (original L6–7), an inline banner module (original L6–64), a large inline `[[module CSS show="true"]]` (original L287–660) holding the main CSS, and four preset modules each wrapped in its own `#ifexpr` gate (original L661–687, L689–719, L721–762, L764–854). Candidate delivery is a closing-frame design at the head: a `[[module CSS]]` (candidate L2–5) importing two draft-host local--code deliveries (the base fragment's code block /1 and this page's own code block /1), plus the interwiki-style frame at priority=3 naming the page's own code block (candidate L7–11). All of the theme's own CSS is consolidated into that single `[[code type="css"]]` block (candidate L261–879, 619 lines), which is both the displayed source exhibit and the delivered stylesheet; the topology pass measures the five original module components moving into it at 0.88–0.97 similarity (14 DELIVERY-MOVE blocks). Self-delivery census: the candidate contains exactly one code block in any form (`[[code type="css"]]` at L261), so the /1 address names the stylesheet itself; the address was never in the population audit's mismatch set. Draft-host URLs are the draft-form class (iii), rewritten to the production host at posting. One structural consequence is a defect: the four preset gates stand in the candidate's body at L246–257 as nested empty shells (four opens, four closes, no content), and the preset bodies sit inside the code block (rainy at L703, yellow :root at L727, blue :root at L756, minimal :root at L794), delivered unconditionally. The delivery-chain test decides it: a gate can only act on content in render-time text, and here the gates wrap nothing while the content they gated is delivered by URL without them.
- **Why:** Own-code delivery via the interwiki-style frame is the campaign's standard supplement frame for page-source themes (P4/T9, P6/T3); it removes the runtime dependence on the author's personal hosting and on a third wiki's fragment. The emptied gates are the parameter-gate defect family (ledger class I shape; the same shape FIX5 repaired in suprematism's item 92): a documented include parameter that cannot change anything is a functional defect, not a formatting choice.
- **Verify:** Read candidate L1–11 and L243–261; census the code blocks (`grep -n '\[\[code' candidate.txt`, one hit); read the four gate lines at candidate L246–257 and find no module between them and their closes; locate the preset bodies at candidate L703/L727/L756/L794.
- **Disposition:** Delivery change standing (the two draft-host @imports stand as the checker's pseudo-ref lines, class (iii)). **DEFECT FLAG (open)** — the emptied preset gates (candidate L246–257) with their bodies delivered unconditionally from the code block; no ledger item charges or dispositions it. Flagged here and in the lane report for a repair lane; the package is written against the candidate as it stands.

### 4. Fonts and assets

- **What:** The consolidated code block opens with the delivery imports (candidate L262–269): BHL normalize and black-highlighter from scp-jp.github.io, Noto Sans JP and Noto Serif JP (the JP font loads, P7/T5), then the original's four Latin faces (Nixie One, Atkinson Hyperlegible, Outfit, Old Standard TT). Those four stood in the original at L288–290 (inside the show=true module) and L723 (inside the blue preset module); each is imported exactly once in the candidate. The classifier labels their original positions DUPIMPORT-DEL (blocks B5, B14); that is a relocation, not a deduplication, adjudicated in the appendix. The banner stack's "Alumni Sans Pinstripe" (candidate L285) is loaded by the base fragment (fragment:suprematism-jp-base-css L17), so no stack in the delivered chain names an unloaded face. The CN display face Zhuque Fangsong was dropped, with the ground stated in the code block's own header comment (it is not among the direct-link exception hosts; section 10). Assets: the preset exhibit images and the rainy preset's traumarain.svg are re-hosted to the candidate's own draft-host attachments (candidate L183–231, L710; class (ii) posting form); the Malevich exhibit image stays on the author's GitHub Pages in both files (the T1 baseline's single hotlink error), original-state delivery.
- **Why:** P7/T5 for the JP loads; KB-17 for the font hosts; P5 for the asset re-hosting. A font named in a stack but loaded nowhere in the delivery chain is the KB-16 defect; the census above is the check that this file does not have it.
- **Verify:** `grep -n '@import' original.txt candidate.txt` (5 / 10 lines, the candidate's tenth hit is the porter comment); `grep -n 'Alumni' pages/fragment:suprematism-jp-base-css.txt` for the fragment's load.
- **Disposition:** DISPOSITIONED (class (ii)) for the re-hosted assets and the author's GitHub image; the Zhuque drop is recorded with its ground in the file itself.

### 5. Header, sidebar, and site furniture

- **What:** The theme's furniture is its preset gallery (candidate L176–245): five preset exhibits (grey as the default, rainy, yellow, blue, minimal), each documenting its include parameter (`|rainy=true` and siblings at candidate L200, L212, L224, L236), with the warning that most Suprematism presets are incompatible. The header variables keep the original's values byte-identically, including `--header-title: "SCP 基金会"` (candidate L357 = original L312) and the blue preset's Chinese banner subtitle (candidate L775 region). The banner subtitle line in the body is translated (真理は幾何のあわいに潜む, candidate L33).
- **Why:** The preset gallery is documentation, and its parameters are the theme's headline mechanism; that the parameters cannot act is the section 3 flag, recorded there rather than repeated here. The retained header strings are ruling 2 territory (header and title language is translation taste, out of scope for migration correctness; KB-57), the same ground on which the sibling theme Suprematism's Chinese preset display strings were dispositioned (ledger §(c3) P9).
- **Verify:** Read candidate L176–245; `grep -n 'header-title' original.txt candidate.txt`.
- **Disposition:** DISPOSITIONED (ruling 2 / P9 family) for the retained header and preset display strings; the preset mechanism itself is the open flag in section 3.

### 6. Text translation

- **What:** The exhibit body is translated throughout (original L66–660 → candidate L28–256 in its new position): the introduction, the sample section, the heading collapsible, the Suprematism essay (with its reference footnote repointed from zh.wikipedia to ja.wikipedia, candidate L73), the tabview, the tables, the div exhibits (shadebox/block census: 3 occurrences on both sides, all present), and the preset documentation. In-CSS text (R1): the CSS comments inside the consolidated block are carried from the original's modules; the string-valued `--banner-title` values ("FOUNDATION", "BLUE") are the presets' identity strings and stand. The classifier's three TRANS-UNANCHORED blocks and one COMMENT-TEXT block are this mass, resolved in the appendix by shape.
- **Why:** P10 for the body; KB-18 for reader-visible strings. CSS comments are porter-visible only and are not a defect class (NEGATIVE-LEDGER shape); they are stated here so a reviewer does not have to re-derive them.
- **Verify:** Read candidate L28–256 against original L66–660 section by section; the translated headings align one-to-one.
- **Disposition:** Standing (the port itself); the reference-link localization is recorded above.

### 7. Links

- **What:** The candidate's source link points back to the original page (credit block, candidate L21). The author link in the introduction names Liurd in `[[*user …]]` form (candidate L38). The introduction's base-theme link is this theme's FIX5 item: the original names `theme:suprematism` (original L76), a page that does not exist on SCP-JP; the candidate names `theme:suprematism-jp` (candidate L38). The install example's two CN include lines became the candidate's own posting name plus a translator's note explaining the fragment substitution (candidate L40–41). No prose link in the candidate targets an un-suffixed theme name.
- **Why:** P11 (dead-target links fail at click time on the posted wiki); the usage-example name follows the campaign's settled posting-name rule for exhibits (AGENTS.md §6).
- **Verify:** `grep -n 'theme:suprematism' candidate.txt` (only the -jp form and the CN source URL appear); the item 95 re-derivation is in the per-theme record.
- **Disposition:** FIXED (item 95); no open link item in this file.

### 8. Structure

- **What:** Two structural changes beyond translation. (a) The delivery consolidation of section 3: five module components and the show=true module collapse into the single code block, which also becomes the source exhibit; the exhibit that stood in the hidden collapsible at original L285–660 now stands as the + ソースコード section (candidate L258–881). (b) The hidden collapsible that held it stands empty in the candidate (candidate L243–245: the `[[div [[iftags -テーマ]]…]]` wrapper, a collapsible open, and its immediate close, no content) — a leftover husk of the move, costing a stray toggle in a hidden div and nothing else. Brace depth, measured over both whole files: final depth 0 and no negative excursion on either side, so the consolidation displaced no closing brace. The localize.md closing rule (selectors, variable names, channel order preserved) holds for the CSS bodies themselves, whose text the topology pass matches at 0.88–0.97 similarity.
- **Why:** R3 (exhibit restructuring) for the exhibit's move, with the ground stated: the move is what makes the own-code delivery of section 3 possible, since the exhibit and the delivery are the same block. The empty husk is recorded as a minor observation, the same shape the review pass has noted in sibling candidates.
- **Verify:** Compare the structural maps: `grep -n` for `[[module`, `[[code`, `[[iftags`, `[[collapsible` in both files; read candidate L243–245.
- **Disposition:** Standing (restructuring recorded); the empty collapsible is a **minor observation (open)**, flagged in the lane report with the gate flag.

### 9. Formatting only

- **What:** None. The classifier counts 0 whitespace-only blocks and 0 re-indentation blocks over the 18 change blocks; the diff's size is relocation and translation, not formatting.
- **Why:** Formatting-only churn is disclosed as its own class so a reviewer does not have to re-derive it, and so it is never mistaken for semantic change (the R7 negative-ledger rule is not triggered here).
- **Verify:** The classifier summary in classification.json (`reindent_blocks: 0`; no WS-ONLY label).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Four porter annotations stand in the candidate, none of which has an original counterpart: two `//訳注:` lines in the body recording that the original's CN preview module and the backrooms fragment include are omitted as JP-absent (candidate L24, L26); a third `訳注` inside the install example (candidate L40) recording the fragment substitution; and the header comment of the consolidated code block (candidate L271–277), which states in Japanese that the Suprematism base is imported from fragment:suprematism-jp-base-css, that the icon CSS is loaded by the base from jsdelivr, and that the CN font CDN (Zhuque Fangsong) was dropped as outside the direct-link exceptions. The two body notes are imprecise in one respect a reviewer should know: the fragment is not simply omitted, it is delivered by @import instead (section 3); the notes describe the include line's fate, not the base's.
- **Why:** R2 (porter annotation additions): annotations added by the porter are part of the change record, and the code block's header comment is load-bearing — it is the pointer a future editor needs before touching the delivery split.
- **Verify:** Read candidate L24, L26, L40, and L271–277.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section or in the ledger rows cited: (1) the render-row dispositions (ledger §(c2), RENDER-ROWS-G (CN16)): page-overflow figures on page and sample, the runtime-hotlink site-theme chain, and the credit-modal preview form (ruling 5; KB-32), all class (ii) or preview-form properties, plus the chromium-only coverage statement; (2) the T1 standing classes (register c1): 12 pseudo-ref errors, the draft-host delivery form (class (iii)/(ii)), and 1 hotlink error, the author's GitHub exhibit image (class (ii)); (3) the retained Chinese header and preset display strings under ruling 2 (section 5); (4) the dropped Zhuque Fangsong face, with its ground stated in the file (section 4). Not dispositions, and not hidden by this list: the two open defect flags (sections 1 and 3) and the minor observation (section 8), which no record has decided.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above, except the flagged items, which are open).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the campaign checker baseline for this file is 13 errors / 1 warning / 0 info (12 pseudo-ref, 1 hotlink), and the FIX5 lane's control run around item 95's edit reports identical totals before and after (13/1/0), so the repoint introduced no new error; (b) the supplement's re-judgment of item 95 is re-derived from this package's own bytes in the per-theme record below; (c) render checks T2/T3 produced dispositions only, no open finding (ledger §(c2)); (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +290/−255 across 18 blocks. The classifier's adjudication: 17 specific blocks, 0 heuristic, 1 residue (resolved in the appendix).
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:trauma-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement), with the two open flags recorded above.

## Per-theme record

### The FIX5 closure (ledger item 95), re-derived

At ledger time this candidate carried one blocking defect: its introduction linked to `theme:suprematism` (ledger §(e) item 95 [H], charged under P11 and in the LOCALIZE-S2-E lane's cross-cutting dead-target list), a page that does not exist on SCP-JP. FIX5-TEXTB §3 (commit 3f328d8) records the fix: a single-token repoint of the link target to `theme:suprematism-jp`, label and surrounding text byte-unchanged, on probe evidence (the un-suffixed name returns HTTP 404; the -jp candidate exists), with the checker totals identical before and after (13/1/0; the single warning merely renamed from the dead target to the unposted -jp candidate, the batch-posting class). Re-derived from this package's bytes: the original's intro names `[[[theme:suprematism|至上主义]]]` (original L76); the candidate's intro names `[[[theme:suprematism-jp|至上主義]]]` (candidate L38); no other occurrence of the un-suffixed name stands in the candidate outside the CN source URL in the credit block. The closure holds exactly as the supplement states it.

### Flag A — the credit pointer, in both carriers

Argued in section 1. The campaign's TASL standard (ruling 3) requires the credit apparatus to name the author the original names. This original names its author in the one place it has: the intro byline (original L76, Liurd, as the maker working from Suprematism). The candidate's two attribution carriers both decline to name him: the credit block's 著作権者 field (candidate L18) defers to "the original page's creator", and the license box's author parameter (candidate L883) defers to "the author of scp-wiki-cn theme:trauma". A reader of either carrier learns that someone else holds the credit without learning who; the candidate's own prose (candidate L38) names Liurd, so the information was in the porter's hands. This is the credit-pointer defect the review pass has repaired across the population (the field and the parameter each take the named author in the population's forms). It is flagged, not edited, by this package.

### Flag B — the emptied preset gates

Argued in sections 3 and 5. The original's four presets are functional: each is a `[[module css]]` body wrapped in its own `[[iftags [[#ifexpr {$name} == (true) | - ]]]]` gate in render-time text (original L661–687 rainy, L689–719 yellow, L721–762 blue, L764–854 minimal), so an including page switches a preset on by passing the parameter the documentation teaches. The candidate documents the same parameters (candidate L177, L200, L212, L224, L236) and keeps the four gate lines (candidate L246–257), but the gates are nested inside each other and wrap nothing, and the four bodies were consolidated into the delivered code block (candidate L703, L727, L756, L794), where they apply unconditionally in cascade order. No parameter an including page can pass will change which preset rules apply, and the rules of all four presets apply at once where they do not conflict. The delivery-chain test is the deciding check: include-parameter substitution reaches render-time text only, and these gates stand in render-time text with nothing inside them. No ledger item, FIX wave, or disposition in the campaign record charges or decides this state; the render rows record only that the pages render styled, which they do, with every preset at once. It is flagged, not edited, by this package.

### Minor observation — the empty code-exhibit collapsible

Candidate L243–245: the hidden div and collapsible that held the original's code exhibit stand empty after the exhibit's move to the + ソースコード section (section 8). The exhibit itself is complete in its new position; the husk costs a stray toggle inside a hidden div. Recorded for the same repair pass as the flags, at minor weight.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/theme:trauma-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX17 items 1–2, landing `872057f3664b2fe570f4ca78e86406d0694e5692`** ("pages: R-fix-17 flags repaired (trauma, travellers-book)", 2026-11-17, R/review-scout/FIX-RFIX17.md §§1–2; 889 → 892 lines):
  - **Item 1 — credit pointer → Liurd.** The 著作権者 field at L18 now reads `**著作権者:** [[*user Liurd]]` and the license-box author parameter at L693 reads `|author=Liurd]]` (pre-edit both were pointers naming nobody). Evidence: the original names its author only in its intro byline (orig L76, `[[*user Liurd]]`), and the candidate's own prose already named him. This closes the package's Flag A, which is kept above as the as-built record.
  - **Item 2 — emptied preset gates restored.** The four preset bodies were extracted from the consolidated code block and returned to inline gated `[[module css]]` blocks at the file tail, in the original's own gate form and order, as siblings outside the `[[iftags +テーマ]]` gate (the suprematism-jp item-92 repaired form): rainy at L701/L702, yellow L729/L730, blue L761/L762, minimal L804/L805 (file ends at L892 with minimal's `[[/iftags]]`). The empty nested shells formerly at L246–257 were removed; the blue preset's Old Standard TT `@import` was relocated from the code block's head into the blue gated module as its first line (byte-identical, stated once), because only the blue preset's `--banner-font` names the face. Rule-multiset census: 80 items / 78 distinct before and after, multisets exactly equal; @imports 10 before, 10 after. Restored modules byte-compared to the original: minimal and blue identical; rainy and yellow identical except their two URLs, which keep the candidate's settled draft-host re-host. This closes Flag B and the minor empty-collapsible observation, kept above as the as-built record.
Checker (FIX-RFIX17 table): error 13 / warn 1 / info 0 → 13 / 1 / 0, finding sets identical modulo shifted line numbers; class (i) 0 before and after.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/fragment:suprematism-jp-base-css.txt` — the re-hosted Suprematism base stylesheet, shared with theme:suprematism-jp and recorded as this theme's dependency in the `start-themes.tsv` row (deps column: `fragment:suprematism-jp-base-css (@import)`); it is also where the banner stack's Alumni Sans Pinstripe load lives. (2) `pages/theme-decoration-sample-trauma-jp.txt` — the decoration sample page used by the render checks. (3) The deliveries themselves: the local--code code blocks served from the draft host (fragment /1 and theme /1), which are the runtime form of file (1) and of the candidate's own code block. The original side of the change set is the two external sources the shell pointed at (the author's GitHub stylesheet and the backrooms-CN fragment); their content enters the record through file (1) and through the candidate's consolidated code block.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave (LOCALIZE-S2-E) produced the initial port (translation, delivery consolidation, exhibit restructuring, and, as this package flags, the emptied preset gates and the pointer credit fields); FIX-CREDIT-D (commit 1869877) normalized translator attribution across the population; FIX4-IWB (commit 5559209) adjudicated the interwiki-style frame's priority (KB-07); FIX5-TEXTB (commit 3f328d8) repaired item 95's dead link; and the usage-example sweep (commit b5cb724) completed the install example's posting name. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c2) (render row), §(c3) (localize row), §(e) item 95; GOSIGN2-LEDGER-SUPPLEMENT.md item 95; REPORT-GOSIGN2-FIX5-TEXTB.md §3. The go-sign re-run over that record is what the Status block certifies.

## Appendix — classifier residue and label adjudication

- **B7 (the one residue block; original L657–659 → candidate at L702):** the closing lines of the original's show=true module (`[[/module]]` and the collapsible/div closers around it). No signature fires because the lines are pure structure; they are part of the DELIVERY-MOVE consolidation argued in sections 3 and 8, and are assigned there.
- **DUPIMPORT-DEL on B5 and B14:** the spans are the original's font @import lines (original L288–290 and L723). The label reads them as deleted duplicates; the bytes show relocation — all four faces stand exactly once in the candidate's code block head (candidate L266–269). Adjudicated in section 4; not a deduplication and not a defect.
- **EXHIBIT-RESTRUCTURE on B5 (original L66–290):** the differ's seam for the exhibit region, whose candidate counterpart was absorbed into block B3's insertion by the relocation. The exhibit census (section 8) finds every exhibit present; the label fired on the move, not on a drop.
- **Skeleton "none" sections:** the skeleton printed sections 2, 4, 5, 6, 7, and 10 as "none" because it lists each block once under its primary label. The label_spans in classification.json show the signatures firing inside multi-label blocks (FONT-IMPORT and JPFONT-LOAD inside B3/B5/B14, TRANS-UNANCHORED inside B2/B3/B18, COMMENT-TEXT inside B3, LICENSE-BOX as B18's primary); the sections above are written from the spans, per the settled format.
