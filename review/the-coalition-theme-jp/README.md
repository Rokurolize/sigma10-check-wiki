# Review package — theme:the-coalition-theme-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:the-coalition-theme-jp — origin EN, population #147 [GOSIGN2-LEDGER (b) row 147]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now eb66f2f8c0a145e66e690ed27a6b6d3b047261834a067227bfa18831c37b174e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 132; GOSIGN2-LEDGER (b) row 147]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN21))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 147, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 147]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 147]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:the-coalition-theme-jp.txt sha256:eb66f2f8c0a145e66e690ed27a6b6d3b047261834a067227bfa18831c37b174e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 147) |
| Standing items | **DISPOSITIONED** — T1 pseudo-ref ×4 (class (ii), section 11); the render row's two items (KB-40 runtime chain; sample T2 no machine verdict, exit 2, a coverage caveat); T4's pattern-5 pair (both draft-host images 404, KB-58, section 11). The verdict stamp reads STALE because the candidate changed after the verdict in exactly one commit, the usage-example sweep b5cb724 (section 12) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:the-coalition-theme | theme:the-coalition-theme-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 12 (first translation; the candidate's credit block records 初訳時参照リビジョン: 12) | — |
| Source of this copy | Campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-C/orig-the-coalition-theme.txt`, via the mirror store (class COPY, hash-verified against review/sources.tsv) | Canonical file `pages/theme:the-coalition-theme-jp.txt`, copied at worktree HEAD e907bdd |
| Lines / bytes | 276 lines / 7,545 bytes | 305 lines / 10,216 bytes |
| SHA-256 | d28d8fcc08f6a73f3edadde47d33dc13ee73fe96315617da21e254d743aede2a | eb66f2f8c0a145e66e690ed27a6b6d3b047261834a067227bfa18831c37b174e |

Wave history: the candidate was created by the Stage 2 EN21 integration (commit dda4fd3, the LOCALIZE-S2-C wave's port), then touched by FIX-CREDIT-D (1869877, translator-attribution normalization over 163 files) and by the usage-example sweep (b5cb724, one include line, section 12). No FIX5 commit touches this file, because the theme had no OPEN items for FIX5 to re-judge.

## Summary

A Black Highlighter theme whose port is the standard classes applied once each, plus three small appended supplements. The original gates its whole page behind `[[iftags +theme]]`, imports the BHL base CSS from nu-scptheme.github.io, and delivers its own layer through interwiki-style includes at priorities 1–3. The candidate keeps that topology, repoints the base delivery to the JP side (the production BHL page include at the head, the base CSS imports on scp-jp.github.io), swaps the bare Rate for the preview credit block, re-hosts the font load to Google Fonts with JP stacks, translates the exhibit body, and appends three commented tail modules carrying JP-environment corrections (per-theme record). Measured churn (the generator's difflib count, autojunk off): +166/−142, 308 changed lines in 66 change blocks / 3 diff hunks; a GNU-diff count of the same pair gives 241 changed lines (+135/−106) — the difference is alignment choice, not content. Two items deserve a reviewer's eye rather than a skim: both of the theme's own images are 404 on the draft host (T4's pattern-5 finding, dispositioned as deferred hosting, KB-58), and the candidate loads PT Mono, which the original named in its mono stack but never loaded (section 4).

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 66 change blocks — 39 specific (59.1%), 26 heuristic (39.4%), 1 residue (1.5%), 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| TRANS-UNANCHORED | 28 |
| TRANSLATION-ANCHORED | 23 |
| COMMENT-TEXT | 8 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 5 |
| INCLUDE-REPOINT | 5 |
| EXHIBIT-RESTRUCTURE | 4 |
| SELF-DELIVERY | 2 |
| WS-ONLY | 2 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 1 |
| ESCAPED-INCLUDE | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |

Adjudication of the heuristic mass: the 26 heuristic blocks are the exhibit body's one-line translations (each sample line mixes translated text with Latin markup, so the anchor test fails by design) and CSS comment translations inside the code exhibit; none of them hides a structural change — the exhibit census in section 8 was taken line by line for this README. The four EXHIBIT-RESTRUCTURE primaries are include repoints inside exhibit regions, not restructurings (section 8). The single CSS-BODY block is the font-stack rewrite, adjudicated to section 4 as P7. The one residue block is in the appendix.

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:the-coalition-theme-jp; original theme:the-coalition-theme on scp-wiki at reference revision 12; candidate `pages/theme:the-coalition-theme-jp.txt`. Provenance route: derived from the original at the reference revision by the LOCALIZE-S2-C wave (sources.tsv kind: standard; no production JP counterpart exists for this theme, so the R4 adoption question does not arise). The frame moved: the original opens with its tag gate (original L1) and delivers the base through a head module; the candidate opens with a bare `[[iftags]]` pair wrapping the production BHL include (candidate L1–3), then the localized gate `[[iftags +テーマ]]` (candidate L5).
- **Why:** Section 0 declares the provenance route so every later count is read against the right baseline; the gate's tag is P2, the base include is P4/T9 (section 3).
- **Verify:** The sources.tsv row for the-coalition-theme-jp; `sha256sum original.txt` against the Provenance table.
- **Disposition:** Standing (the route itself); the gate and delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's credit furniture is a bare `[[module Rate]]` (original L18, inside a `[[>]]` block) and nothing else — no info block, no license box. The candidate deletes the Rate (BARE-RATE-DEL) and installs the JP preview credit block (candidate L21–30) carrying the eight ruling-3 fields: タイトル 世界オカルト連合テーマ; 翻訳責任者 AI; 翻訳年 2026; 原題 The Coalition Theme; 著作権者 Greyve（Calibri BoldおよびCroquemboucheの協力による）; 作成年 2021; 初訳時参照リビジョン 12; 元記事リンク https://scp-wiki.wikidot.com/theme:the-coalition-theme. The base-work attribution the field cannot hold survives in the code exhibit's banner (candidate L194–195), which names the Black Highlighter base by Woedenaz and Croquembouche in translation. The section's CSS half is the middle tail supplement (candidate L298–300): a `white-space:nowrap` rule for the BHL credit module's "otherwise" back-link (T7-CREDIT-CSS, block B66).
- **Why:** P3/T1: the preview credit module is the rate-bearing JP form, so the bare Rate is deleted rather than duplicated. Ruling 3 fixes the eight fields. The source link names scp-wiki.wikidot.com, the host sources.tsv records for the original — the check this package runs on every credit link (host against the recorded host) passes, so no probe was needed and no jiha-family defect arises. T7 (KB-11 family): the JP credit dialog's back-link wraps without the rule.
- **Verify:** Read candidate L21–30 against the eight fields; `grep -n 'module Rate' candidate.txt` returns nothing; the banner attribution is candidate L194–195.
- **Disposition:** FIXED (GOSIGN2-LEDGER §(c3): P3 credit fields FIXED, credit waves, checker-verified); no credit item is flagged for this theme.

### 2. Includes and components

- **What:** The candidate's live includes are: the production BHL page include `[[include :scp-jp:theme:black-highlighter-theme]]` (candidate L2, added — the original has no page-level base include, it imports the base CSS instead, section 3); the credit pair (section 1); two interwiki-style includes at priorities 1 and 2 in the head region, repointed from the original's identical pair (their targets are the JP BHL CSS files, section 3); and the tail interwiki-style frame at priority 3 (section 3). The one escaped include is the usage example (candidate L81, `:scp-jp:theme:the-coalition-theme-jp`), which the usage sweep brought to its -jp form after the verdict (section 12). No component had to be ported alongside this theme; the COMPONENT-SWAP block is the base-delivery form change of section 3.
- **Why:** P1 (KB-15): every include names the JP counterpart that exists on scp-jp; the production BHL page is that counterpart for the base. Ruling 4 is not engaged.
- **Verify:** `grep -n '\[\[include' candidate.txt` — every live include names a `:scp-jp:` target or the draft-host delivery of section 3.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers the BHL base by two `@import`s from nu-scptheme.github.io in its head module (normalize.min.css and black-highlighter.min.css) and its own layer by interwiki-style includes at priorities 1 (normalize), 2 (BHL), and 3 (its own `local--code/theme:the-coalition-theme/1` on scp-wiki.wdfiles.com). The candidate preserves the shape and repoints every host: the two base imports now name scp-jp.github.io (the JP BHL project's host), the priority-1/2 includes name the same JP files, the production BHL page include is added at the head (candidate L2), and the candidate's own layer is delivered at priority 3 by a tail module (candidate L284–286) importing `local--code/theme%3Athe-coalition-theme-jp/1` from the draft host plus the tail frame (candidate L287–289) naming the same /1. Census check: the candidate has exactly one `[[code]]` block (candidate L190), so both /1 addresses name the block that holds the CSS — correct. Brace scan: every component closes at depth 0 with no negative dips.
- **Why:** P4/T9 (base and own-code delivery served from JP hosts) and P6/T3 (the interwiki-style frame; priority 3 because the theme's own layer stacks over normalize and the base, exactly as the original ordered it). The draft-host form of the live lines is KB-41, class (iii): sanctioned at draft stage, rewritten at posting.
- **Verify:** `grep -n 'local--code\|interwiki-style' candidate.txt` — priorities 1, 2, 3 in order; count the `[[code]]` blocks (one).
- **Disposition:** DISPOSITIONED (draft-host lines, class (iii)).

### 4. Fonts and assets

- **What:** Load (JPFONT-LOAD): the original's code block loads one family — Roboto 400;500 from fonts.bunny.net. The candidate's code block loads one Google Fonts import (candidate L200): Roboto 400;500, PT Mono, and Noto Sans JP 400;500;700. PT Mono is the notable entry: the original names it in `--mono-font` but loads it nowhere, so mono text fell back on the original too; the candidate's load closes that gap rather than inventing a face. Stacks (the CSS-BODY block, adjudicated here): `--body-font`, `--header-font`, and `--title-font` gain `'Noto Sans JP', 'Hiragino Sans', 'Yu Gothic', 'Meiryo'` after `'Roboto'`; `--mono-font` gains `"Noto Sans JP"`. A font-license prose line (SIL OFL 1.1) and a third font specimen span (candidate L183) have no original counterpart; both are recorded here rather than passed over. Assets: the head logo `black-highlighter-logo.svg` (candidate L34) and `--logo-image`'s GOClogo.png (candidate L211) are repointed from the original's hosts to the draft host's own folder; T4 probed both on sigma10-jp-test and both returned 404 (section 11).
- **Why:** P2/KB-17 (fonts.bunny.net is not in the allowed hotlink set; Google Fonts is) and P7 (JP faces in the load and the stacks together). P5/KB-58 for the assets: own-folder re-hosting is the posting-time class, and the 404 pair is its recorded state on the draft host.
- **Verify:** `grep -n '@import' candidate.txt` — the delivery lines of section 3 plus the one font import; `grep -n 'font-family\|--body-font\|--mono-font' candidate.txt` for the stacks.
- **Disposition:** Font load and stacks applied; the two asset URLs are DISPOSITIONED (KB-58, class (ii)).

### 5. Header, sidebar, and site furniture

- **What:** The HEADERVAR block: `--logo-image` is repointed (section 4) and the two header strings are translated in place — `--header-title` → 世界オカルト連合, `--header-subtitle` → 事務次長室より (candidate L211–213 region). No other header variable is overridden. The classifier's one CONTENT-STRING label fires inside a block whose actual change is a CSS comment translation (`/* Intro */` → `/* イントロ */`); the pair in fact contains no CSS `content:` property at all (`grep -n 'content:'` returns nothing on either side), so there is no rendered-string item for this theme and the label is recorded as a false fire. The theme's sidebar and top-bar rules are carried unmodified apart from the font lines of section 4 and the appended top-bar supplement (per-theme record).
- **Why:** P9's subject matter (header text) with the opposite outcome from a kept-string case: the strings were translated, so ruling 2 and KB-57 are not engaged. The ledger's §(c3) line for this theme carries no P9 charge.
- **Verify:** `grep -n -- '--header-title\|--header-subtitle' candidate.txt` — the two translated values.
- **Disposition:** Standing.

### 6. Text translation

- **What:** The exhibit body is translated throughout: 23 TRANSLATION-ANCHORED blocks and the 28 TRANS-UNANCHORED blocks, the latter being one-line exhibit translations whose anchor test fails because each line mixes Japanese with Latin markup — each was verified against the mirror for this README rather than waved through. CSS comments inside the code exhibit are translated (COMMENT-TEXT ×8). The banner inside the code block is translated with its attribution intact (section 1). Two invalid style attributes inside exhibits are silently repaired in the candidate — a div style `filter: display:flex;` becomes `display:flex;`, and a caption style `width:width:100px;;` becomes `width:100px;` — recorded here because a repair inside a sample is still a change (per-theme record). English survives in the candidate only in the credit block's original-title field, the code banner's proper nouns, and the tail modules' comments (section 10).
- **Why:** P10 (body, usage, and sample translation is the port's purpose) and KB-18 (reader-visible strings). The unanchored group is where a silent deletion would hide, which is why it was read line by line.
- **Verify:** The pairs are diff.md's body sections in order; a Latin-only scan of the exhibit body returns only the recorded survivals.
- **Disposition:** Standing (the port itself); no untranslated reader-visible text remains outside the recorded survivals.

### 7. Links

- **What:** The candidate's one live outbound link is the credit block's source link (candidate L22's field, section 1), which names the recorded host and serves the original. Prose links inside the exhibits are sample text and follow P10. No prose link in the candidate targets a page that does not exist on its named host.
- **Why:** P11: prose links take the JP counterpart or the serving original, under the dead-reference evidence standard; the source link passes it on the recorded host.
- **Verify:** `grep -n 'wikidot.com' candidate.txt` — the source link and the delivery hosts of section 3 only.
- **Disposition:** Standing; no link item is flagged for this theme.

### 8. Structure

- **What:** The localize.md closing rule holds. The candidate's single code block sits where the original's sits (original L175–267 → candidate L190–281, 92 lines on both sides), the gate wraps the page furniture on both sides, and the JP corrections arrive as the head include (section 2) and the appended tail modules (per-theme record), not interleaved into the inherited CSS. The four EXHIBIT-RESTRUCTURE primaries adjudicate against the exhibit census: the tabview and its tabs, the image exhibits, the heading samples, and the code exhibit are present on both sides in the same order; the four blocks are include repoints inside exhibit regions (section 2/3), so no exhibit was restructured, dropped, or replaced, and the R3 question does not arise.
- **Why:** R3 exists to force exactly this adjudication, because a restructure and a deletion share a diff shape and ledger class I charges the silent form; here the census, not the label, decides.
- **Verify:** Compare `grep -n '\[\[tab\|\[\[code\|\[\[include' original.txt candidate.txt` — the sequences correspond.
- **Disposition:** Standing; no structural deletion, no class I item.

### 9. Formatting only

- **What:** Two WS-ONLY blocks (blank-line placement), and tab-to-space re-indentation inside parts of the code exhibit's `:root` block and its `@media` block; the classifier counts no pure re-indent block (reindent_blocks 0) because the re-indented lines also carry the host and value changes of sections 3–5. One micro-repair rides here: the original's `--theme-base: "nuscp"` line lacks its semicolon; the candidate's line has it. The two exhibit style-attribute repairs are recorded in section 6.
- **Why:** R7: formatting churn is disclosed as its own class so it is never mistaken for a semantic change; the semicolon is disclosed with it because it is a one-character semantic repair in the same region.
- **Verify:** The diff sections over the `:root` block in diff.md.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three annotations, all English `/* */` comments heading the appended tail modules (candidate L292–305, block B66): (1) "SCP-JP Wikidot page history: …" over the mobile history-form grid rule; (2) "SCP-JP Wikidot BHL credit otherwise correction: …" over the credit back-link rule of section 1; (3) "SCP-JP Wikidot the-coalition-theme-jp top bar labels: …" over the `word-break:keep-all` rule for the top-bar labels. The skeleton's per-section text for this section does not list them because they ride inside the T7-CREDIT-CSS-labeled block; they are recorded here from the bytes. The font-license prose line of section 4 is body prose, not an annotation.
- **Why:** R2: porter-added text is part of the change record, and these three comments are the only in-file explanation of why the tail modules exist.
- **Verify:** Read candidate L292–305.
- **Disposition:** Standing.

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's four pseudo-ref errors: class (ii), posting-procedure — they are the candidate's own draft-host delivery and asset lines (sections 3–4), which the posting procedure rewrites or re-hosts; fix lanes never "fix" them in the candidate. (2) The render row's items: the page's runtime-hotlink site-theme chain only (KB-40, environment layer, not the candidate), and the sample's T2 run returned no machine verdict (exit 2) — a coverage caveat under GOSIGN-TESTS (a), not a theme defect. (3) T4's pattern-5 finding (LOCALIZE-ROWS row 147, display-affecting 2): both images the draft references — the `--logo-image` GOClogo.png and the example image — returned 404 on sigma10-jp-test, so the header logo and the example never render there. The ledger's §(c3) line dispositions P5 for this theme as class (ii) / KB-58: the assets are re-hosted at posting time, and re-upload is barred before it. No item in this package is flagged beyond the ledger's own record.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; environment-layer lines are recorded as not-charged.
- **Verify:** Each item names its deciding record above.
- **Disposition:** DISPOSITIONED (all three items).

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 132): exit 1, 4 errors / 1 warn / 1 info; all four errors are pseudo-ref, class (ii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-2, lane RENDER-S2-D (EN21)): FINDINGS — the two items of section 11(2); engine coverage as run by the lane, with the sample's exit-2 run recorded as a caveat. (c) T4/T5 (LOCALIZE-ROWS row 147): FINDINGS jointly, display-affecting findings 2 (the pattern-5 pair); the row's T5 note names the usage-example include at L81, whose target then stood in its pre-sweep form — the usage sweep (commit b5cb724) has since repaired that one line to `:scp-jp:theme:the-coalition-theme-jp`, which is why the verdict stamp reads STALE: the file's only post-verdict change is that repair. The ledger §(c3) line records the theme's T4 outcome as P5 DISPOSITIONED (class (ii) / KB-58). (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (difflib, autojunk off): +166/−142 in 66 change blocks / 3 diff hunks; the GNU-diff count of the same pair is 241 changed lines, and the difference is alignment choice, not content.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:the-coalition-theme-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 147; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### The three appended tail modules

The candidate appends three live CSS modules after its tail delivery frame (candidate L292–305), each headed by the English comment recorded in section 10 and none with an original counterpart: (1) a page-history mobile rule, `#history-form-1>table>tbody>tr:first-child>td:nth-of-type(2){grid-template-columns:repeat(3,1fr)}`, keeping the history form's first row usable at phone widths; (2) the BHL credit "otherwise" correction, `[id*=u-credit] div.credit-back a{white-space:nowrap;flex-shrink:0}` (section 1); (3) a top-bar label rule, `#top-bar.top-bar>ul>li>a,…{word-break:keep-all}`, naming this theme. They are the closing rule's appended-supplement form: JP-environment corrections delivered as separate modules so the inherited CSS stays byte-close to the original. A reviewer should know they exist, because the classifier folds all three into one T7-CREDIT-CSS block (B66) and only the first impression of that label (a credit rule) describes one of them.

### The two exhibit style repairs

Recorded in section 6: inside the exhibit body, the candidate repairs two invalid style attributes the original carries — `style="filter: display:flex;"` (a property name in the value position; the declaration never applied) becomes `display:flex;`, and a caption's `style="width:width:100px;;"` becomes `width:100px;`. Both are one-token repairs inside samples; they change what the sample renders, which is why they are disclosed rather than folded into the translation mass.

## Appendix — residue blocks

| Block | Original | Candidate | Adjudication |
|---|---|---|---|
| B14 | L74 | L85 | The "+ Examples" heading sample translated to "+ 例" (R1, one-line heading translation; counted in section 6) |

## Change set outside the two diffed files

The diff covers two files; the port's record is one file larger. `pages/theme-decoration-sample-the-coalition-theme-jp.txt` is the decoration sample the render checks ran against — it includes `theme:black-highlighter-theme-jp` first and then this candidate, the BHL sample form — and its findings are the sample half of section 11(2). It belongs to this theme's record but carries no port change of its own to explain here. There are no companion fragments, no shared base file beyond the production BHL page the candidate includes, and no inbound-link repairs in other candidates for this theme.
