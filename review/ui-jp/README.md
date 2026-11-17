# Review package — theme:ui-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ui-jp — origin EN, population #152 [GOSIGN2-LEDGER (b) row 152]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 0 infos (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 137; GOSIGN2-LEDGER (b) row 152]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — hidden-* cluster (header-link, hidden-footer/license/login/pageContent/rate, sidebar-unreachable) across most combos on both pages; sample credit-modal (preview-form) + 884px@768 overflow; T3 nothing pointable beyond the machine lines. [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 152, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 152]
- FIX5 re-judgement: item 35 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 fix; checker code-multiset identical before/after [GOSIGN2-LEDGER-SUPPLEMENT (a) item 35]
- Computed against: canonical commit 8eacd6e675b726c2fcf93372dc4dd7899958c2d4; candidate file pages/theme:ui-jp.txt sha256:4bc00d214a680346f20416740695e83a5ba295ea02316bfa9fa5f767c3d88a06; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:ui` on scp-wiki (EN), revision 44 — `original.txt` in this package (362 lines / 6,701 bytes; `wc -l` reports 361 because the last line is unterminated) |
| Candidate | `theme:ui-jp` — `candidate.txt` (377 lines / 7,842 bytes), a byte copy of `pages/theme:ui-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the EN theme carried over with the JP credit form, the own-delivery repoint, the translation and the JP font fix applied. |

This theme's `review/sources.tsv` note column is empty: no supersession correction is owed for this package.

Summary: a small Sigma-9-era theme for the Unusual Incidents tale series. The port is the standing supplement set (preview-credit swap, own-delivery repoint to the draft host, the FIX5 JP font fix) plus translation of the header strings and the CSS comments. The delivered CSS is otherwise byte-conserved: a whitespace-insensitive census of the single code block finds exactly 17 substantive hunks, and every one is named in the sections below. The theme carried one blocking item, 35 (class D, pattern-7), re-derived in the per-theme record.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 11 |
| CONTENT-STRING | 2 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |

Counts: 23 blocks, 10 specific, 13 heuristic, 0 residue, 0 skipped (comment text). Topology: module-css + code-css on both sides, no moves, external own delivery true.

## 1. Credit and attribution

- The original has no credit block. It opens its `[[iftags +テーマ]]` gate with a right-aligned bare `[[module Rate]]` (original L11–13). The candidate replaces it with `credit:start-preview` and the eight ruling-3 fields (candidate L13–22; blocks B4, labels BARE-RATE-DEL + CREDIT-PREVIEW + IFTAGS + TASL-FIELDS). Class P3 / KB-09 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): the preview credit module is rate-bearing, so the bare module is deleted rather than duplicated. Census: `[[module Rate]]` 1 → 0.
- The 著者 field names `[[*user GreenWolf]]` with （改訂： `[[*user stormbreath]]`). The original's code-block banner names the same two in the same roles (original L23 "Created by GreenWolf", L26 "Revised by stormbreath"). The banner's remaining attributions — the Sigma 9 base by Aelanna and Dr Devan, and the UIU logo by Zhange under CC-BY-SA 3.0 — stand in the banner, carried verbatim at candidate L29–36; they were in no credit field on either side, and the port drops none of them.
- No license box stands on either side (the original carries none; class T4 not applicable). The logo's license line is the banner's, above.
- T7 credit-module CSS: none in either file. The theme's own rate-widget styling (original L284–322, `.page-rate-widget-box`) is page furniture, carried unchanged.
- Verify: `grep -c 'module Rate'` on both package files (1 / 0); read candidate L13–22 against original L20–27.
- Disposition: ledger verdict PASS at go-sign; the credit form is part of the S2 port, and no (e) item charged credit for this theme.

## 2. Includes and components

- The only body include besides the frame and credit pair is the usage example's self-include, completed to the candidate's own name `theme:ui-jp` (original L17 → candidate L26; block B6, INCLUDE-REPOINT).
- The frame include's branch prefix is section 3. No `theme-squares`, no foreign include, and no include of a page that will not exist stands in the candidate.
- Verify: `grep -n 'include' candidate.txt` — three live includes (frame, credit pair counted as the section-1 block) plus the one usage line.

## 3. Delivery and code loading

- Topology is unchanged: a head `[[module CSS]]` importing the theme's single code block, and the block itself. The candidate has exactly one code block (`[[code type="CSS"]]`, candidate L28–376, 349 lines), and both delivery addresses name `/1` — the block that holds the stylesheet. Self-delivery census: MATCH (class FIX-CODEADDR: a `local--code/<own name>/N` reference naming the stylesheet block).
- Block B1 (original L1–2 → candidate L1–3): the head module's `@import` is repointed from `scp-wiki.wdfiles.com/local--code/theme%3Aui/1` to the candidate's own draft-host address `sigma10-jp-test.wdfiles.com/local--code/theme%3Aui-jp/1` (classes P4 / T9 own-delivery repoint; DRAFT-HOST). One rule is added at candidate L3: the hue-rotate(15deg) filter is extended to `iframe.scpnet-interwiki-frame`, the JP environment's interwiki frame element, beside the original's `.menu-item > .image` selector.
- Block B3 (original L5–8 → candidate L6–10): the `component:interwiki-style` frame include drops the `:scp-wiki:` branch prefix, names own `/1` on the draft host, and gains a `css=` parameter carrying the same filter rule scoped to `#interwiki`. The classifier's EXHIBIT-RESTRUCTURE primary on this block is a false fire: the block is the frame include's repoint, and no exhibit stands at that locus (adjudicated in the appendix).
- The code block carries the same selector extension in its own copy of the rule (candidate L204–207; block B16, section 8), so every delivery channel carries it. The T1 checker's two `interwiki-touched` warnings (candidate L3, L204) record these touches verbatim; warnings are recorded, not classified.
- Verify: `grep -n 'local--code' candidate.txt` (two addresses, both `/1`); count code blocks (1).

## 4. Fonts and assets

- The FIX5 font fix stands here; the per-theme record re-derives it. Block B7 (candidate L38–42): a porter annotation plus the Noto Sans JP `@import` at the head of the code block. Block B11 (original L131 → candidate L146): the file's only font stack, `Arial, sans-serif`, becomes `Arial, 'Noto Sans JP', sans-serif`. Class P7 (pattern-7): a named JP face with no load, or no JP face at all, leaves Japanese text to fallback rendering.
- Asset: block B10 (original L78 → candidate L93): `UIU_Logo.png` is repointed from the EN page's attachments to the candidate's own draft-host attachments (`local--files/theme%3Aui-jp/`) — draft form, rewritten at posting (the checker's second pseudo-ref error). No other asset stands in the file.
- Verify: `grep -n 'Noto Sans JP' candidate.txt` (the import line and the stack line); the same grep on `original.txt` returns nothing.

## 5. Header, sidebar and site furniture

- The header `content:` strings are translated. Block B12 (original L136 → candidate L151): "Federal Bureau of Investigation " → 「連邦捜査局」. Block B13 (original L148 → candidate L163): "Unusual Incidents Unit, Three Portlands Office " → 「異常事件課、スリー・ポートランド支局」. Block B22 (original L343 → candidate L358): the mobile subtitle "UIU, Three Portlands Office " → 「UIU、スリー・ポートランド支局」; the mobile title "FBI " (candidate L352) is kept — an identity string, not prose.
- Ledger item P9 (header/title language) was DISPOSITIONED under ruling 2 (out of scope for migration correctness). The delivered bytes translate the strings anyway; the disposition records that no fix was owed, and the translation stands as delivered. This is recorded as a fact of the bytes, not as a contradiction.
- The sidebar furniture effect of the section-3 selector extension: the interwiki menu image keeps its hue-rotate treatment in the JP frame form.
- Verify: `grep -n 'content:' candidate.txt` against the same grep on `original.txt`.

## 6. Text translation

- The intro prose is translated (block B5, original L15 → candidate L24; the series title rendered 「ケネス・スペンサーとロビン・ソーンの異常事件簿」).
- CSS comments: 11 COMMENT-TEXT blocks (B7–B9, B14, B15, B17–B21, B23) — the section headings are translated （リンク / ヘッダー / トップメニュー / サイドメニュー / YUIタブ / フッター / 装飾ボックス / 評価モジュールの調整 / 標準画像ブロック / プレビューモジュール, ten headings; the eleventh block is the FIX5 annotation comment, section 10). Class R1: comments are porter-visible; the reader-visible strings are the `content:` values of section 5.
- One inline comment is kept in English: `/* visited link color */` (candidate L63). Porter-visible only; recorded in section 11, not a finding.
- Verify: the COMMENT-TEXT spans in `classification.json` against both files.

## 7. Links

- None fired as a signature, and the census supports the empty section: the only prose link is the intro's `[[[unusual-investigations|...]]]` (target unchanged, label translated — the series hub slug is the page's name in both environments), and the credit block's 元記事リンク names the original page `https://scp-wiki.wikidot.com/theme:ui` as a quotation, its host matching the sources.tsv record.
- No link in the candidate names a page that will not exist.

## 8. Structure

- Closing rule: selector set, rule order and channel order are preserved. The whitespace-insensitive census of the code block finds exactly 17 substantive hunks; each is named in sections 1–6 (the font pair, the selector extension, the comment translations, the content strings).
- Block B16 (original L189 → candidate L204): the filter rule's selector gains `iframe.scpnet-interwiki-frame`, declarations unchanged — an in-place JP-DOM correction of the R6 shape, applied in three places (head module, frame `css=`, code block) so every channel carries it. The classifier labels it CSS-BODY heuristic; the appendix adjudicates it, and the lane report proposes naming this shape in patterns/.
- No exhibit was dropped or replaced: the file's only exhibit is the usage line (section 2).
- CSS brace balance was checked by depth, not count: both files scan to final depth 0 with minimum depth 0.

## 9. Formatting only

- None. WS-ONLY is 0 blocks: the candidate keeps the original's indentation inside the code block. The difflib totals in `diff.md` (+42 / −27) are fully accounted by the named changes.

## 10. Porter annotations

- One annotation was added: the FIX5-FONTSA comment at candidate L38–41 (in English), stating that the header stack is Arial-only with no Japanese glyphs, so Noto Sans JP (Google Fonts, SIL Open Font License) is appended and the Latin face is unchanged. It rides inside block B7 (JPFONT-LOAD); the skeleton's "none" for this section is the primary-label artefact the brief warns about — checked explicitly, the annotation is present and its statement matches the bytes.
- No other annotation stands in the candidate.

## 11. Dispositions and exceptions

- Draft-host lines (class (iii), rewritten at posting): candidate L2 (the head `@import`) and L93 (the logo `url()`) — the T1 baseline's only two errors, both pseudo-ref.
- Warnings recorded verbatim: `interwiki-touched` at candidate L3 and L204 (section 3).
- Render row (RENDER-S2-D, EN22): the hidden-* cluster across most viewport combinations on both pages (KB-44 / KB-49 / KB-50 capture family — T3 found nothing pointable beyond the machine lines), the sample's credit-modal preview form (KB-32), and the 884px@768 overflow (KB-33 / KB-34 family) — all DISPOSITIONED, none a theme defect.
- P9 DISPOSITIONED (ruling 2) — section 5. The kept English comment (candidate L63) — section 6. No class (i) item stands for this theme.

## 12. Verification

- T1 (the campaign checker, `--kind theme --translation --check-links`) run by this lane on the current candidate: error 2 / warn 2 / info 0 — identical to the stamp baseline (pseudo-ref ×2; interwiki-touched ×2). FIX5-FONTSA's own before/after was likewise 2/2/0 → 2/2/0.
- T2/T3: FINDINGS with dispositions only (ledger row (c2)); nothing pointable stands.
- T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record below re-derives it from this package's bytes.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `4bc00d214a680346f20416740695e83a5ba295ea02316bfa9fa5f767c3d88a06`); `original.txt` hash equals the sources.tsv value (`378cdc7551df0df4d3e4b0437fc0135b4a00463406f89badc3653f3ea469c9ba`); brace-depth scans clean on both files; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 35 (ledger (b) row 152, class D): "Pattern 7 — no JP font anywhere. Current file: no font imports, no JP font named" (T1-ROWS row 137; LOCALIZE-ROWS row 152, LOCALIZE-S2-C; the theme's (c3) line reads P7 → (e) D).
- What the fix was supposed to change: give the theme's Japanese text a loaded JP face — load Noto Sans JP and name it in the Arial stack, the file's only stack.
- Supplement re-judgement (GOSIGN2-LEDGER-SUPPLEMENT): FIXED, FIX5-FONTSA, commit 8eacd6e, "checker code-multiset identical before/after".
- Re-derived from this package's bytes: the original names no JP face and loads none (its only stack is `Arial, sans-serif`, original L131; no font `@import` stands in either channel). The candidate carries the annotation and the Noto Sans JP `@import` at candidate L38–42, at the head of the delivered code block, and the stack at candidate L146 reads `Arial, 'Noto Sans JP', sans-serif`. The load stands in the delivered channel (the block the head module serves as `/1`), and the named face is the loaded face — neither the named-but-unloaded nor the loaded-but-unnamed mirror shape stands.
- Control: the verdict stamp in this package reads PASS computed against canonical commit 8eacd6e — the fix commit is the candidate's last content change, so the file the verdict describes is the file in this package. Checker totals identical before and after the fix (2/2/0), per the FONTSA lane report and this lane's re-run.
- Closure: CONFIRMED from the bytes. No discrepancy between the supplement's account and the package.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-ui-jp.txt` — the render-check sample page for this theme.
2. The delivery itself: the candidate's own code block, served as `local--code/theme%3Aui-jp/1` on the draft host. The theme is self-contained on both sides; no companion fragment or base file exists.

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-C) produced the port: credit swap, own-delivery repoint, translation, header strings. Its pattern-7 miss became item 35.
- FIX5-FONTSA closed item 35 at commit 8eacd6e, the candidate's last content change; the verdict stamp therefore reads PASS rather than STALE.
- The usage-example sweep did not change this file after the fix (its self-include already named `theme:ui-jp`, or the sweep's line predates the fix; the stamp is the evidence either way).

## Appendix — heuristic and residue adjudication

The classifier reports 0 residue blocks and 13 heuristic blocks. All 13 resolve by shape:

- B5 (TRANS-UNANCHORED): the intro prose translation — section 6.
- B8, B9, B14, B15, B17, B18, B19, B20, B21, B23 (COMMENT-TEXT): CSS comment translations — section 6, class R1. Comment translation is the recorded negative-ledger shape, not a new signature.
- B12 (CSS-BODY): the header `content:` string — section 5.
- B16 (CSS-BODY): the `iframe.scpnet-interwiki-frame` selector extension — section 8, the R6 JP-DOM shape.

No heuristic block is left unadjudicated, and no new signature is proposed from this package alone; the selector-extension shape is carried to the lane report as a cross-batch proposal.
