# Review package — theme:wondertainment-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:wondertainment-jp — origin EN, population #158 [GOSIGN2-LEDGER (b) row 158]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 6ca75213a2b1e42ee975269a34ace1d302a3ac2ebc42e048b028a9c6c8e01b95); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 0 warns / 2 infos (pseudo-ref×6); standing classes dispositioned in register c1 [T1-ROWS row 173; GOSIGN2-LEDGER (b) row 158]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 158, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 158]
- FIX5 re-judgement: item 40 (class B) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 40]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:wondertainment-jp.txt sha256:6ca75213a2b1e42ee975269a34ace1d302a3ac2ebc42e048b028a9c6c8e01b95; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:wondertainment` on scp-wiki (EN), revision 64 — `original.txt` in this package (308 lines / 6,715 bytes; `wc -l` reports 307, the last line is unterminated) |
| Candidate | `theme:wondertainment-jp` — `candidate.txt` (317 lines / 7,855 bytes), a byte copy of `pages/theme:wondertainment-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the EN Dr. Wondertainment theme carried over with the JP credit form, its three attachments re-hosted to the candidate's own draft-host folder, the font host swap plus the JP font supplement, and the body translation. |

This theme's `review/sources.tsv` note column is empty: no supersession correction is owed for this package.

Status note: the verdict stamp above reads STALE by design. The usage-example sweep (commit b5cb724) changed the candidate's usage line after the FIX5 verdict was computed (the stamp's computed-against commit is b5cb724 itself); the stamp's verdicts describe the pre-sweep file. The per-theme record below re-derives the theme's one blocking item on the current bytes.

Summary: a playful EN theme for Dr. Wondertainment, delivered as one code block behind a head module. The port swaps in the preview credit, re-hosts the attachments, moves the two Latin font loads from bunny.net to Google Fonts and adds the Noto Sans JP supplement, and translates the body, including the two header content strings. The theme carried one blocking item, 40 (class B), re-derived in the per-theme record and confirmed. No defect flags arise from this package.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 14 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 2 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 7 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 4 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 18 |
| TRANSLATION-ANCHORED | 4 |
| WS-ONLY | 1 |

Counts: 39 blocks, 22 specific, 15 heuristic, 2 residue, 0 skipped. Topology: module-css + code-css on both sides, no moves, external own delivery true. The diff is Tier 1 (+62/-53, 13 hunks).

## 1. Credit and attribution

- Credit block (candidate L11-21; CREDIT-PREVIEW + TASL-FIELDS), nine fields. 著者 and 著作権者 both name "DarkStuff・taylor_itkin（改訂: stormbreath）", matching the original's byline (original L17). The code banner (original L33-39) also carries the pixabay header-image credit and "logo made by Zhange, edited by taylor_itkin"; both survive verbatim in the candidate's banner (candidate L42-48). No pointer-in-place-of-a-name defect stands, and no attribution line the original carries is dropped.
- The bare `[[module Rate]]` that stood at original L13-15 is this theme's blocking item 40; the per-theme record re-derives its removal. Census: `[[module Rate]]` 1 → 0 (class P3 / KB-09, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa: the preview credit module is rate-bearing).
- License box: none on either side; nothing was dropped, and this is not a license-box case. T7 credit-module CSS: none in either file (`grep -c creditButton` = 0 / 0).
- Verify: read candidate L11-21 and L42-48 against original L17 and L33-39; `grep -c 'module Rate'` on both files (1 / 0).

## 2. Includes and components

- Live includes: the head frame (section 3) and the credit pair (section 1). The one usage example (original L19 "+ Usage" → candidate L27 "+ 使用方法"; blocks B8-B9 area, COMPONENT-SWAP + ESCAPED-INCLUDE) names `:scp-jp:theme:wondertainment-jp` in its post-sweep form; the sweep's single `-jp` insertion in this file is the STALE ground of section 0.
- No include is duplicated, and no component swap stands beyond the credit pair and the frame prefix.
- Verify: `grep -n 'include' candidate.txt`.

## 3. Delivery and code loading

- Topology unchanged (the classifier records no moves): the head `[[module CSS]]` (candidate L1-3) imports own `/1`, repointed from scp-wiki.wdfiles.com to the draft host (DELIVERY-HOST / DRAFT-HOST), and the interwiki frame (original L5-8, `:scp-wiki:` form) is repointed to `:scp-jp:` with its `theme=` naming own `/1` (candidate L4-7, SELF-DELIVERY x2).
- Census, counting every code-block form: exactly one `[[code type="css"]]` block on each side (original L29-307; candidate L37-316), holding the stylesheet; `/1` names it. Self-delivery census: MATCH (FIX-CODEADDR); no navla-style shape.
- No include-parameter gates stand on either side, so the render-time gate test has nothing to bite on.
- Verify: `grep -n 'local--code' candidate.txt`; count `[[code` blocks (1 / 1).

## 4. Fonts and assets

- Fonts (class P7): the original's two fonts.bunny.net imports (Berkshire Swash; Sansita — original L30-31) become Google Fonts css2 imports of the same families (candidate L38-39; FONT-IMPORT 1), and a Noto Sans JP load is added (candidate L40, wght@400;700; JPFONT-LOAD 1). Stacks are extended in place: `'Berkshire Swash', 'Noto Sans JP', cursive` (candidate L54, L134) and `'Sansita', 'Noto Sans JP', sans-serif` (candidate L77, L145) (JPFONT-STACK 4). Every face a stack names is loaded in the delivered block, and no load is unapplied.
- The porter prose at candidate L23 announces the program (all fonts OFL via Google Fonts; Noto Sans JP serving Japanese text) — section 10.
- Assets: the three EN-host attachments are re-hosted to the candidate's own draft-host folder: `AnotherTest.png` (candidate L82; the original's attachment name at original L73 is "AnotherTest" without an extension, and the re-hosted copy carries `.png` — recorded as the copy's name, nothing more), `wondertainmentSmall.png` (candidate L87), and `tabs.png` (candidate L211, L216, L221). These are five of the six T1 pseudo-ref loci (section 11).
- Verify: `grep -n 'Noto Sans JP' candidate.txt` (the load, four stacks, the L23 prose); `grep -n 'local--files' candidate.txt`.

## 5. Header, sidebar and site furniture

- The two header content strings were translated by the port (CONTENT-STRING x2): original L130 "Dr. Wondertainment!" → candidate L139 ワンダーテインメント博士！; original L142 "Know in your Head is a Wonderful Place" → candidate L151 きみのあたまの中はワンダフルな場所. Header and title language is out of scope for migration correctness under ruling 2, in either direction; the porter's choice is recorded as its boundary application, standing, not a defect.
- Sidebar and tab rules are carried CSS; the one duplication inside them is the original's own (section 8).
- Verify: read original L130 and L142 against candidate L139 and L151.

## 6. Text translation

- The body is translated throughout (TRANSLATION-ANCHORED 4 blocks, TRANS-UNANCHORED 18): the headings, the intro, the usage prose, and the exhibit specimens (tabview, headings, blockquote, table).
- CSS section comments are translated (COMMENT-TEXT x14, class R1), with three English comments inside the tab rules kept verbatim (candidate L214-216), porter-visible only.
- The two residue blocks resolve here: B8, the `+ Usage` → `+ 使用方法` heading translation (class P10); B13, the `/* COMMON */` → `/* 共通 */` comment translation (class R1). Both are adjudicated in the appendix.
- Verify: the translation spans in `classification.json` against both files.

## 7. Links

- None. Neither file carries prose links (`grep -n '\[\[\['` returns no hits on either side); the only page references are the usage example (section 2), the credit block (section 1), and the asset URLs (section 4).
- Verify: the grep above.

## 8. Structure

- The duplicated `.yui-navset .yui-nav` border-color rule pair (original L215-222) is carried verbatim (candidate L224-231): inherited duplication from the original, parity, recorded here rather than flagged; the port introduced no duplication of its own.
- Exhibit census: the tabview, heading, blockquote and code specimens all stand against the original; nothing was dropped or escaped away. Footnotes: none on either side.
- CSS brace balance was checked by depth, not count: both code bodies scan to final depth 0 with minimum depth 0.
- Verify: a brace-depth scan over original L30-306 and candidate L38-315.

## 9. Formatting only

- One WS-ONLY block (whitespace-only churn inside the carried stylesheet). No other formatting-only change stands; the remaining churn rides inside the blocks named above.
- Verify: the label counts in `classification.json`.

## 10. Porter annotations

- One porter addition stands in body prose rather than comment form: candidate L23, the font-program statement (all fonts OFL via Google Fonts; Noto Sans JP for Japanese text). It announces the section-4 supplement, and its statement matches the bytes. Class R2 in its prose carrier, the same shape the vanguard package records.
- No comment-form annotations were added; the code banner is the original's own (section 1).
- Verify: read candidate L23 against section 4's census.

## 11. Dispositions and exceptions

- Draft-host lines (pseudo-ref x6, the T1 baseline's errors): candidate L2 (the `/1` import), L82, L87, L211, L216, L221 (the re-hosted attachments) — class (iii) draft forms, rewritten at posting, DISPOSITIONED.
- The `!important` info (candidate L172) is recorded verbatim.
- Render row (RENDER-ROWS-2, RENDER-S2-D (EN23)): the page's only entry is the runtime-hotlink site-theme chain (KB-40, environment layer), DISPOSITIONED. The sample's T2 returned no machine verdict (exit 2, no summary): a coverage caveat, not a finding. No credit-modal line is recorded for this theme.
- The STALE stamp's ground is section 0's status note: the post-verdict change is the usage sweep's one line (section 2), and no re-judgement is fabricated for it.
- No class (i) item stands for this theme.

## 12. Verification

- T1 run by this lane on the current candidate (`check_source.py --kind theme`): error 6 / warn 0 / info 1 — all six errors pseudo-ref at the loci in section 11, the info the `!important` note at L172, and no `double-rate` line. This is exactly FIX5-FURNA's after state (6/0/1); the stamp's baseline (6/0/2) describes the pre-FIX5 file.
- T2/T3: FINDINGS with the disposition in section 11. T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `6ca75213a2b1e42ee975269a34ace1d302a3ac2ebc42e048b028a9c6c8e01b95`); `original.txt` hash equals the sources.tsv value (`8db35c91c94321e3cfce941fcd2f3a63242184da8d06d7223e80ffc10a2d3c60`); brace-depth scans clean on both code bodies; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 40 (ledger (b) row 158, class B): a duplicate bare `[[module Rate]]` standing next to the preview credit module, which embeds its own rating module — two rating widgets on one page (LOCALIZE-S2-C cross-cutting observation 3: a bare `[[module Rate]]` in the credit flow, at the port's then-current L12).
- What the fix was supposed to change: remove the unlabelled duplicate block, leaving the rate-bearing preview credit as the page's only rating widget. The FURNA lane report's evidence: the block at pre-edit candidate L10-12 was unlabelled (`[[>]]` / `[[module Rate]]` / `[[/>]]`), immediately before `credit:start-preview`, with no paired exhibit label, so the labelled-exhibit exception does not apply; checker 6/0/2 → 6/0/1, the `double-rate` info cleared, no new errors.
- Supplement re-judgement: FIXED, FIX5-FURNA, commit 9e8931f.
- Re-derived from this package's bytes: the original carries the identical bare Rate at original L13-15. `git show 9e8931f -- pages/theme:wondertainment-jp.txt` removes exactly the four lines (`[[>]]`, `[[module Rate]]`, `[[/>]]`, and the following blank line) that stood between the gate and the credit include. The current candidate contains no `[[module Rate]]` anywhere (`grep -c` = 0), and its only rate-bearing element is `credit:start-preview` (candidate L11-21). This lane's checker run reproduces the after state, 6/0/1.
- Closure: CONFIRMED on current bytes — which matters here, because the verdict stamp is STALE (section 0): the closure is re-derived from the package, not inherited from the stamp.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-wondertainment-jp.txt` — the render-check sample page for this theme (it includes the candidate at its L1).
2. `pages/theme-decoration-sample-wondertainment.txt` — the production-side sample page.
3. The candidate's own delivered attachments: `AnotherTest.png`, `wondertainmentSmall.png`, `tabs.png` (section 4).

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-C) produced the port: the preview credit, the frame repoint, the font supplement, and the translation; the bare Rate survived that wave.
- FIX5-FURNA (commit 9e8931f) removed the Rate and closed item 40.
- The usage-example sweep (commit b5cb724) then completed the usage line's `:scp-jp:theme:wondertainment-jp` name — the post-verdict change behind the STALE stamp. The sweep touched nothing else in this file: the per-theme record's grep census runs on the swept file.

## Appendix — heuristic and residue adjudication

The classifier reports 15 heuristic blocks and 2 residue blocks. All resolve by shape:

- Residue B8: the `+ Usage` → `+ 使用方法` heading translation (class P10) — section 6. Residue B13: the `/* COMMON */` → `/* 共通 */` section-comment translation (class R1) — section 6. Classifier artefacts, not content questions.
- The heuristic mass is CSS-BODY and COMMENT-TEXT blocks inside the carried stylesheet and TRANS-UNANCHORED prose: font-stack rewrites are narrated as P7 in section 4 even where the classifier labels them CSS-BODY, comment translations are section 6, and the EXHIBIT-RESTRUCTURE primary is the credit/license furniture region of sections 1-2, where the exhibit census shows nothing dropped or restructured (a false fire).
- The duplicated yui-navset rules are carried content, not a classifier question (section 8).

No heuristic or residue block is left unadjudicated, and no defect flag arises from this package.
