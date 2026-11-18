# Review package — theme:ethic-committee-jp (CN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ethic-committee-jp — origin CN, population #187 [GOSIGN2-LEDGER (b) row 187]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 993006639625198298b1f139aee6f861587153dfb8ad968fafc7063f8cab238a); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 1 info (hotlink×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 165; GOSIGN2-LEDGER (b) row 187]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 186, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 186]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 187]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:ethic-committee-jp.txt sha256:993006639625198298b1f139aee6f861587153dfb8ad968fafc7063f8cab238a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 187) |
| Standing items | **DISPOSITIONED** — T1 hotlink ×1 and pseudo-ref ×1 (classes (ii)/(iii), section 11); the render row's two items (KB-40, and the sample's no-verdict coverage caveat, section 11); T4's three localize items (P5, P7, P9) dispositioned in the ledger §(c3) line and argued on the bytes in sections 4, 5, and 11 |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:ethic-committee | theme:ethic-committee-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 36 (first translation; the candidate's credit block records 初訳時参照リビジョン: 36) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-ethic-committee.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:ethic-committee-jp.txt`, copied at worktree HEAD 5ab991e |
| Lines / bytes | 707 lines / 21,089 bytes | 708 lines / 23,227 bytes |
| SHA-256 | aaed603aa986e4be9031f4ab71bb22eaae0db343e88350f5f7b4522b541bf13e | 16167ddbd9f02f6bc29c00c96517ec894cdefda93624ca68ac71dc511c7c00a1 |

Wave history: the candidate was created by the Stage 2 CN6 integration (commit 4166a2f, the LOCALIZE-S2-D wave's port) and has exactly one later commit, 1869877 (FIX-CREDIT-D, the population-wide translator-attribution normalization). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A small diff by block count (8 blocks) that is one large structural move: the CN original delivers its CSS as a live inline `[[module css]]` at the head of the page and keeps its credit furniture, usage prose, and snippet exhibits inside a tag-gated body below it. The candidate inverts the page into the wave-standard JP form: the tag gate and the preview credit block open the page, the translated prose and snippet exhibits follow, the theme's whole CSS travels as a `[[code type="css"]]` source exhibit inside a collapsible, and live delivery moves to the tail, a module import of the candidate's own local--code page plus the interwiki-style frame at priority 1. Measured churn (diff.md, the generator's difflib count with autojunk off: +212/−211, 423 changed lines in 8 change blocks / 4 diff sections). Three T4 items ride on the bytes exactly as the ledger dispositioned them: the EN-host logo URL kept byte-identical (section 4), the un-loaded SC body font (section 4), and the Chinese header strings kept under ruling 2 (section 5). No defect was found in the candidate beyond what the record already carries.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 8 change blocks — 6 specific (75.0%), 1 heuristic (12.5%), 1 residue (12.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-MOVE | 3 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| JPFONT-LOAD | 1 |
| RATE-EXHIBIT-KEPT-CANDIDATE | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 2 |

Adjudication for this README (every block was read against the bytes): the two EXHIBIT-RESTRUCTURE blocks (B5, B6) are not exhibit deletions; they are the alignment shadow of the delivery move and the page re-ordering, adjudicated in section 8 against the exhibit census. The single residue block (B7) is the closing pair of the candidate's new source-code collapsible, resolved in the appendix. The RATE-EXHIBIT-KEPT-CANDIDATE label rides on B5: the original's gated body carries a bare `[[module Rate]]`, and the candidate keeps a rate-bearing form through the preview credit module (section 1). After adjudication no block is left unexplained.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:ethic-committee-jp; original theme:ethic-committee on scp-wiki-cn at reference revision 36; candidate `pages/theme:ethic-committee-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-D wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame itself moved: the original opens with its live CSS module (original L1) and places its tag gate `[[iftags +版式]]` at L492, around the exhibit body only; the candidate opens with the localized gate `[[iftags +テーマ]]` (candidate L1) around the whole page body and closes it at candidate L700, ahead of the delivery tail.
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2 (iftags tag localization), the delivery re-ordering is section 3.
- **Verify:** The sources.tsv row for ethic-committee-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture sits inside its gated body: a bare `[[module Rate]]` (original L496) plus a `:scp-wiki-cn:credit:start`/`end` pair (original L501–506) wrapping the CN credit prose. The candidate deletes both and installs the JP form at the head: a `:scp-jp:credit:start-preview`/`end-preview` block (candidate L3–12) carrying the eight ruling-3 fields (title 伦理委员会 版式; 翻訳責任者 AI; 翻訳年 2026; 原題 伦理委员会 版式; 著作権者 M4A1MODIII; 作成年 2025; 初訳時参照リビジョン 36; the source link, candidate L11, naming scp-wiki-cn.wikidot.com, the original's recorded host). The original's non-field credit prose survives translated directly below: the CC BY-SA line (candidate L14) and the author line (candidate L16). The translator field took its ruling-3 form in the FIX-CREDIT-D commit (1869877). There is no T7 credit-module CSS on either side: neither file styles `.creditButton`, `.creditRate`, or `.rate-box-with-credit-button` (grep returns nothing), so no credit CSS supplement was owed.
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated (the KB-09 duplicate-Rate failure is what a kept Rate would become), and the branch credit pair is ledger class C residue, not JP furniture. Ruling 3 fixes the eight fields and the translator credit form. The title and original-title fields keep the CN title text; that is the T5 notation item the localize record carries, in the same family as the section 5 header disposition (ruling 2 takes title language out of migration scope).
- **Verify:** `grep -n 'module Rate\|credit:start' candidate.txt` — only the `:scp-jp:` preview pair returns; read candidate L3–12 against the eight fields.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified).

### 2. Includes and components

- **What:** Four includes in the candidate, all `:scp-jp:`: the credit pair (candidate L3, L12, section 1), the escaped usage exhibit as built `{{@@[[include :scp-jp:theme:ethic-committee]]@@}}` (candidate L23; the original's exhibit at original L515 named `:scp-wiki-cn:theme:ethic-committee`) — a repoint that changed the branch prefix but kept the plain slug, so the exhibit named a page that does not exist on scp-jp; the usage-example population sweep has since completed the name on the same line to `{{@@[[include :scp-jp:theme:ethic-committee-jp]]@@}}` (SWEEP-USAGE.md; canonical commit b5cb724), and the interwiki-style frame (candidate L705–708, section 3). The original's live includes were its `:scp-wiki-cn:` credit pair. No foreign include is kept on either side of the diff, and no component had to be ported alongside this theme.
- **Why:** P1 (KB-15): an include must name the JP counterpart that actually exists on scp-jp; a kept `:scp-wiki-cn:` include is a foreign-include error, class (i). The exhibit's repoint as built satisfied the branch half of that rule only — its plain slug named no JP page — and the sweep's completion to the posting name is what brings it under the rule. Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt` — four includes, all `:scp-jp:`.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The package's centre of gravity (blocks B1, B3–B5, B8; the topology pass pairs the bodies at similarity 0.99 / 0.90 / 0.75). The original delivers its CSS live and inline: a `[[module css]]` body of 485 lines at the head (original L1–485), plus a second module importing its own code page, `local--code/theme:ethic-committee/1` from scp-wiki-cn.wdfiles.com (original L489–491). The candidate moves that CSS body, merged with the original's two `[[code]]` snippet exhibits, into a single `[[code type="css"]]` source exhibit inside a collapsible (candidate L200–698, banner comment at L202), and delivers live from the tail: a `[[module css]]` importing the candidate's own `local--code/theme%3Aethic-committee-jp/1` from the draft host (candidate L702–704), and the interwiki-style include at priority 1 with `theme=` naming the same /1 delivery (candidate L705–708). The font-import seam of the moved body is block B3 (candidate L204, section 4) and the `--header-font` seam is B4 (candidate L217).
- **Why:** P4/T9 (own-code delivery served from JP hosts) and P6/T3 (the interwiki-style supplement frame; priority 1 is the theme's own layer). The original's inline-module form has no JP counterpart convention; the code-exhibit-plus-local--code form is the wave-standard delivery for these CN originals, and it is what makes the CSS copyable to the code page at posting. The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten to the production host at posting.
- **Verify:** `grep -n 'local--code' candidate.txt` — candidate L703 and L707, both the candidate's own /1 on the draft host; the moved body compares against original L1–485 in diff.md at 0.99 similarity.
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Loads (block B3, JPFONT-LOAD): inside the moved CSS body, the first `@import` changes Noto Serif SC → Noto Serif JP (candidate L204; the original's is original L4); the Roboto Mono and FontAwesome 4.3.0 imports are carried over unchanged (candidate L205–206), both sanctioned hosts. Stacks: `--header-font` becomes `'Noto Serif JP', serif` (candidate L217, block B4), while `--body-font` keeps `'Noto Sans SC', sans-serif` byte-identical (candidate L218) — no JP body face is loaded anywhere in the file, so Japanese body text falls back. Assets: the theme's one image variable, `--logo-image`, keeps the EN branch host byte-identical (candidate L220 = original L20: `https://scp-wiki.wdfiles.com/local--files/departments/ethics-committee.png`).
- **Why:** P7/T5 with KB-16 (the font load gap) covers the serif display face, which is the face the theme's headings actually render in; the ledger judged the body-font half under the T4 bar and dispositioned it (below), so the port loads the JP serif and leaves the body stack as the original wrote it. P5 with KB-17/KB-58 covers the logo: a branch-shared departments asset with no JP re-host on record, dispositioned as a deferred asset rather than silently passed over.
- **Verify:** `grep -n '@import\|--header-font\|--body-font\|--logo-image' candidate.txt` against the lines above.
- **Disposition:** DISPOSITIONED — P7 (GOSIGN2-LEDGER §(c3): recorded without a display-affecting mark; T4 bar; LOCALIZE-ROWS row 186 carries it as the minor type-7 item) and P5 (same line: class (ii) / KB-58).

### 5. Header, sidebar, and site furniture

- **What:** The theme's header text is set in CSS, and it stays Chinese in the candidate: `#header h1 a::before { content: "伦理委员会" }` (candidate L294) and `#header h2::before { content: "审查 · 裁决 · 监督" }` (candidate L297), byte-identical to the original's rules inside the moved body. These are T4's first display-affecting item (LOCALIZE-ROWS row 186: Chinese header strings displayed constantly on the JP page). No other furniture change: the candidate sets no `--header-title` or `--header-subtitle` variable, and its sidebar and topbar rules are the original's, carried inside the moved body apart from the section 4 seams.
- **Why:** P9/T6 is the class that would override these strings; the ledger dispositioned this theme's P9 under ruling 2, which takes header and title language out of migration-correctness scope. KB-57 is the standing header-language disposition family.
- **Verify:** Read candidate L293–298; compare original L93–98 in diff.md (unchanged lines inside the moved body).
- **Disposition:** DISPOSITIONED (GOSIGN2-LEDGER §(c3): P9, ruling 2).

### 6. Text translation

- **What:** The body prose is translated throughout (the TRANS-UNANCHORED blocks ride inside B2's head insertion and the exhibit seams): the usage prose, the license and author lines (section 1), the collapsible labels (`+ 折叠 - 点击这里` → `+ 折り畳み - ここをクリック`, candidate L49), and the snippet-exhibit captions. In-CSS text (R1) splits two ways: the source exhibit's banner comment is the porter's Japanese (candidate L202, section 10), while the inherited CSS comments inside the exhibit stay Chinese (e.g. `/* 字体引入 */` at candidate L203, `/* 1. 更新: 根变量 */` below it) — porter-visible only, and the localize record carries them as a T5 minor non-display item together with the exhibit's duplicated sample content. The two header `content:` strings are reader-visible but belong to section 5's disposition, not to this section's translation set. Simplified-Chinese glyph forms survive only inside those kept strings and the credit title fields; no R5 conversion was applied to them because they were not translated at all.
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). R1 comments are porter-visible text; the taxonomy records CSS-comment translation as a non-finding, and the record here states openly which comments stayed.
- **Verify:** A scan for simplified-Chinese-specific characters (e.g. 伦, 审, 监) in candidate.txt outside the CSS exhibit returns only the credit fields (candidate L4, L7, L11); inside the exhibit, the kept comments are the ones named above.
- **Disposition:** Standing (the port itself); the kept in-CSS comments are recorded, not hidden.

### 7. Links

- **What:** No LINK-REPOINT block fired, and the bytes bear that out. The candidate's one live outbound link is the credit source link (candidate L11), which names scp-wiki-cn.wikidot.com — the original's recorded host in review/sources.tsv — so the jiha-class host defect does not occur here and no probe was needed. The one body link, the design-reference `[[[ theme:redsquare | 赤の広場テーマ ]]]` (candidate L28), keeps the original's target page name (original L522) with its text translated; it is a same-wiki page reference on both sides and no record flags it.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; a link whose host already matches the recorded original needs no change.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link is the only hit.
- **Disposition:** Standing; no dead or mis-hosted link found.

### 8. Structure

- **What:** One declared deviation from the localize.md closing rule, and it is the delivery restructure of section 3: the CSS body changed channel (live module → code exhibit) and the page furniture re-ordered around it (gate and credit to the head, delivery to the tail). Variable names, selectors, and rule order inside the moved body are preserved (0.99 similarity). The classifier's two EXHIBIT-RESTRUCTURE blocks adjudicate here, not as deletions. B5 (original L484–669 in diff.md's numbering) is the original's gated-body furniture — the bare Rate, the CN credit pair, the usage prose, the collapsible, and the first snippet exhibits — which the candidate re-presents reordered at candidate L3–193 rather than in place; B6 (original L680–700) is the second snippet exhibit pair (the `hr-scales` code exhibit and its live div), whose lines re-pair inside the candidate's merged source exhibit (candidate L695) and body exhibit (candidate L193). An exhibit census confirms the shape: the gavel snippet (original L668–680 code exhibit, live divs L686–692) appears in the candidate both as body exhibits (candidate L179, L185) and inside the source exhibit (candidate L686, L692), and the hr-scales snippet likewise (candidate L193 and L695) — the original itself carried each snippet twice (code exhibit plus live div), and the candidate preserves that duplication, which the localize record notes as a T5 minor property of the source, not a port change. Nothing was dropped or replaced, so the R3 question (sanctioned replacement vs silent deletion) resolves as: neither, a relocation.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n 'class="gavel"\|class="hr-scales"' original.txt candidate.txt` — two occurrences each per file, in corresponding roles.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** None. The classifier finds no whitespace-only block and no re-indentation pair (0 and 0), so the R7 follow-up-diff hazard is not triggered; the moved body kept its original indentation inside the new channel.
- **Why:** Formatting churn is disclosed as its own class so it is never mistaken for a semantic change.
- **Verify:** Section 9 of the skeleton counts in classification.json (`reindent_blocks: 0`); diff.md shows no whitespace-only section.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** One annotation with no original counterpart: the banner comment at the head of the source exhibit, candidate L202 — `/* ===== ethic-committee：原語版の CSS（モジュール＋コードブロック）をまとめたもの ===== */` ("the original-language CSS (module + code blocks), gathered together"). It is load-bearing: it is the only in-file statement that the exhibit merges the original's two CSS channels, which is the fact section 3's adjudication rests on. It rides inside the moved body, which is why no separate ANNOTATION signature fired. No `[!-- --]` translator notes and no editor lines exist in the candidate.
- **Why:** R2: porter-added text is part of the change record and must never be mistaken for original content or for translation.
- **Verify:** Read candidate L202; `grep -n '\[!--' candidate.txt` returns nothing.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Five items, each with its ground. (1) T1's hotlink ×1: the candidate's own draft-host delivery lines (candidate L703, L707), class (iii) draft form (KB-41), sanctioned at draft stage. (2) T1's pseudo-ref ×1: the same delivery family read as a posting-procedure reference, class (ii); the posting procedure rewrites it to the production host, and fix lanes never "fix" it in the candidate. (3) The render row's page item: the runtime-hotlink site-theme chain (KB-40), environment-layer, not charged to the candidate. (4) The render row's sample item: no machine verdict (render_check exit 2, no summary) — a coverage caveat recorded in the ledger register, not a theme defect; the stamp carries it verbatim. (5) T4's three localize items, argued on the bytes in sections 4 and 5: the EN-host logo URL (P5, class (ii) / KB-58), the un-loaded body font (P7, T4 bar), and the Chinese header strings (P9, ruling 2).
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above; the T1 classes are T1-ROWS row 165's, the render items are the ledger §(c2) block for this theme, the localize items are §(c3)'s single line.
- **Disposition:** DISPOSITIONED (all five).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 165): exit 1, 2 errors / 2 warns / 1 info; the errors are hotlink ×1 and pseudo-ref ×1, both dispositioned in section 11; there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-E (CN6)): FINDINGS, the two items of section 11(3–4), both dispositioned; the sample's missing machine verdict is a coverage caveat of the run, recorded as such. (c) T4/T5 (LOCALIZE-ROWS row 186): FINDINGS jointly, display-affecting findings 2 (the header strings and the logo link), plus the minor font item; the ledger §(c3) line records the theme's T4 outcome as P5/P7/P9 DISPOSITIONED. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +212/−211 in 8 change blocks / 4 diff sections.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:ethic-committee-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 187; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The delivery restructure, stated plainly

A reviewer opening the diff cold sees 423 changed lines in 8 blocks and could read B5/B6 as the port deleting the original's exhibit body. The bytes say otherwise, and this package's sections 3 and 8 carry the census that proves it: every content family in the original (CSS body, credit prose, usage prose, both snippet exhibits in both of their roles) is present in the candidate exactly once per role, relocated into the JP delivery form. The one genuinely new furniture is the candidate's source-code collapsible wrapper (candidate L200 and L698), whose closing line is the appendix's residue block B7; the original presented its CSS as a live module and needed no such wrapper.

### The usage example's posting name

The usage example at candidate L23 as built read `> {{@@[[include :scp-jp:theme:ethic-committee]]@@}}`: the porting wave's repoint changed the branch prefix from `:scp-wiki-cn:` but left the plain name, so the example named a page that does not exist on scp-jp (the campaign's settled rule for usage examples, AGENTS.md §6). The usage-example population sweep has since completed the reference to `:scp-jp:theme:ethic-committee-jp` on the same line (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724), one of its 287 repairs across 157 candidates. This package documents the corrected candidate; its stamp reads STALE against the pre-repair verdict, by design.

## Appendix — residue blocks

For class M the residue set is resolved in one table, not per-block slots.

| Block | Shape | Resolution |
|---|---|---|
| B6 (heuristic, EXHIBIT-RESTRUCTURE) | Original L680–700: the `hr-scales` code exhibit and its live div, unmatched by the differ | Relocation, not deletion: the lines re-pair inside the merged source exhibit (candidate L695) and the body exhibit (candidate L193); adjudicated in section 8 |
| B7 (residue, no signature) | Original L703–705 → candidate L698: the `[[/collapsible]]` closing line of the new source exhibit | Added structural line of the delivery restructure; the original had no collapsible around its CSS because the CSS was a live module; recorded in sections 3 and 8 |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-ethic-committee-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(3–4)); it belongs to this theme's record but carries no port change of its own to explain here. The candidate layers over no base theme, there are no companion fragments, and no inbound-link repairs in other candidates belong to this theme.

## License and attribution

- **Title:** 伦理委员会 版式
- **Author:** M4A1MODIII
- **Source:** https://scp-wiki-cn.wikidot.com/theme:ethic-committee — revision 36
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
