# Review package — theme:uiu-bhl-theme-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:uiu-bhl-theme-jp — origin EN, population #153 [GOSIGN2-LEDGER (b) row 153]
- Overall: PASS — NOT PASS at the ledger determination (section (e) register); its one OPEN item re-judged FIXED by the FIX5 wave; go-sign issued 2026-11-17 (COMPLETION-REPORT §10) [GOSIGN2-LEDGER (b); GOSIGN2-LEDGER-SUPPLEMENT (d)]
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 2 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 138; GOSIGN2-LEDGER (b) row 153]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 470px@320 + 525px@375 + 918px@768 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN22))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 153, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 153]
- FIX5 re-judgement: item 36 (class D) FIXED — FIX5-FONTSB, commit 3911f7b: pattern-7 fix [GOSIGN2-LEDGER-SUPPLEMENT (a) item 36]
- Computed against: canonical commit 3911f7b2f69cc4e5a4d7611024cf3d96b5b73e92; candidate file pages/theme:uiu-bhl-theme-jp.txt sha256:c12d56a949499fee589532e0f81cd04c985478ce4237ef3696123d2cf353cb69; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:uiu-bhl-theme` on scp-wiki (EN), revision 88 — `original.txt` in this package (1,028 lines / 29,936 bytes; `wc -l` reports 1,027, last line unterminated) |
| Candidate | `theme:uiu-bhl-theme-jp` — `candidate.txt` (1,037 lines / 33,708 bytes), a byte copy of `pages/theme:uiu-bhl-theme-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the EN Black Highlighter theme carried over with the JP credit form, the JP-distribution base repoint, the translation and the JP font fix applied. |

This theme's `review/sources.tsv` note column is empty: no supersession correction is owed for this package.

Summary: a Black Highlighter (BHL) theme for the Unusual Incidents Unit, the largest diff of this batch (1,025 changed lines by difflib) — and the mass is mostly not substance. The candidate re-indents the 829-line code block from tabs to spaces wholesale (109 WS-ONLY blocks, class R7) and translates its comments; a whitespace-insensitive census of the code block finds exactly 30 substantive hunks, every one named below. The port otherwise keeps the original's two-channel shape (head module with the BHL pair and own rules; exhibits; one code block; tail self-delivery frame) and applies the standing supplements. The theme carried one blocking item, 36 (class D, pattern-7), re-derived in the per-theme record.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 14 |
| COMPONENT-SWAP | 1 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 13 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 7 |
| JPFONT-LOAD | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 25 |
| TRANSLATION-ANCHORED | 29 |
| WS-ONLY | 109 |

Counts: 182 blocks, 154 specific, 26 heuristic, 2 residue, 0 skipped (comment text). Topology: module-css + code-css on both sides, no moves, external own delivery true.

## 1. Credit and attribution

- The original has no credit block; it carries a centered bare `[[module Rate]]` (original L38–40). The candidate replaces it with `credit:start-preview` and the eight ruling-3 fields (candidate L38–47; blocks B7 CREDIT-PREVIEW + TASL-FIELDS, B8 BARE-RATE-DEL). Class P3 / KB-09 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): the preview module is rate-bearing, so the bare module is deleted. Census: `[[module Rate]]` 1 → 0.
- The 著者 field names `[[*user Woedenaz]]`. The original's only attribution text is the UIU logo caption (original L83: the logo by `[[*user Zhange]]`, slight edits by `[[*user Woedenaz]]`, CC BY-SA 3.0), and the candidate carries that caption translated at candidate L90, naming the same two people in the same roles. The field names a person, and the name agrees with the only authorial name the original carries for the theme itself; the logo's own credit stands in its caption on both sides. No pointer-in-place-of-a-name defect stands.
- No license box stands on either side (the original carries none; class T4 not applicable). T7 credit-module CSS: none in either file (the BHL base carries the credit styling).
- Verify: `grep -c 'module Rate'` on both files (1 / 0); read candidate L38–47 and L90 against original L38–40 and L83.
- Disposition: ledger verdict PASS at go-sign; no (e) item charged credit for this theme.

## 2. Includes and components

- Live includes: the three `component:interwiki-style` frames (section 3), the credit pair (section 1), and `theme-squares`, repointed to `:scp-jp:` (original L46 → candidate L53; block B9 — its color names are kept in English, the population's recorded form for that component's parameters).
- Usage exhibits (block B16, original L93–95 → candidate L100–102): the two `@@`-escaped include lines. The self line is completed to `theme:uiu-bhl-theme-jp`. The BHL line names `theme:black-highlighter-theme` with no branch prefix: that is the production JP page — the candidate's own prose at candidate L96 links `https://scp-jp.wikidot.com/theme:black-highlighter-theme`, which serves (the T1 checker's link-label warning names its live title, "Black Highlighterテーマ"). This is the monotypical adjudication ground: a plain-form reference naming a page that exists in the environment is correct as written, and the usage sweep left the form on that ground. The classifier's COMPONENT-SWAP label on this block is its name for the self-name completion.
- The EXHIBIT-RESTRUCTURE primaries on blocks B3, B5, B9 and B181 are the include-prefix shape, not exhibit changes; adjudicated in the appendix. No exhibit was dropped: the exhibit census (theme-squares, both logo images, tabview, blockquote and table specimens, the font specimens, the footnote specimens) is complete against the original.
- Verify: `grep -n 'include' candidate.txt`.

## 3. Delivery and code loading

- Topology is identical on both sides: head `[[module CSS]]` (27 lines), one code block, tail module plus tail frame. The candidate has exactly one code block (`[[code type="css"]]`, candidate L198–1026, 829 lines) — the stylesheet — and both tail addresses name `/1`. Self-delivery census: MATCH (class FIX-CODEADDR).
- Blocks B2, B4, B6 (INCLUDE-REPOINT): the BHL pair is repointed from `nu-scptheme.github.io` to `scp-jp.github.io` in the head module (candidate L3–4) and in the two head frame `theme=` URLs (candidate L31, L36) — classes P4 / T9, the JP distribution host. The head frame keeps the original's priorities 1 (normalize) and 2 (BHL); own-CSS delivery is the tail's, as in the original.
- Tail (blocks B180–B182): the tail module's `@import` (candidate L1032) names own `/1` on the draft host; the tail frame's `theme=` (candidate L1036) names the same `/1` on `scp-jp.wdfiles.com`, the posting-host form, and its include drops the `:scp-wiki:` prefix. The tail's two lines use the two sanctioned stage forms of one address; recorded as an observation, not a defect — both forms name the block that holds the CSS.
- Verify: `grep -n 'local--code' candidate.txt` (two addresses, both `/1`); count code blocks (1).

## 4. Fonts and assets

- Block B52 (original L192 → candidate L199–201): the Latin font import's host is swapped from `fonts.bunny.net` to `fonts.googleapis.com` with the family set and weights unchanged (Google Fonts is a sanctioned host, class P5), and the FIX5 load is added beside it: a Japanese porter annotation (candidate L200) and the Noto Sans JP css2 `@import` (candidate L201). The per-theme record re-derives the fix.
- The four stacks (block B55, CSS-BODY heuristic — narrated here as the P7 font-stack rewrite it is): body (candidate L220) and header (L221) read `'Source Sans Pro', 'Noto Sans JP', 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif` — the original's second Latin names ('Lato', 'Poppins') are dropped and the JP chain stands; title (L222) reads `'Merriweather', 'Noto Sans JP', 'Hiragino Sans', 'Yu Gothic', serif`; mono (L223) reads `'Roboto Mono', 'Noto Sans JP', "Andale Mono", "Courier New", Courier, monospace` — the mono line is the charged fix. Every named JP face is the face the L201 import loads; no stack names an unloaded face and no load stands unused.
- Assets: block B10 (original L77 → candidate L84): the BHL logo image is repointed from the EN BHL page's attachments to the candidate's own draft-host attachments (the checker's pseudo-ref error at L84). Blocks B11 and B54 (original L81 and L206 → candidate L88 and L215): `UIU_Logo.svg` is re-hosted to SCP-JP storage (`scp-jp-storage.wdfiles.com/local--files/file%3A7450069-554-01o5/UIU_Logo.svg`) in both the exhibit image (with its link target) and the `--logo-image` variable — class P5 re-hosting, the campaign's storage form for carried assets.
- Verify: `grep -n 'Noto Sans JP' candidate.txt` (import, annotation, four stacks); the same grep on `original.txt` (the three non-mono stacks only, no import — the load gap the record describes).

## 5. Header, sidebar and site furniture

- Block B54 (HEADERVAR, original L206–208 → candidate L215–217): `--logo-image` re-hosted (section 4); `--header-title: "FBI"` kept (identity mark); `--header-subtitle` "Unusual Incidents Unit" → 「異常事件課」 — a prose subtitle rendered for every reader, translated under the T5 boundary. Block B53 (CONTENT-STRING): `--theme-name` "Unusual Incidents Unit BHL Theme" → 「異常事件課BHLテーマ」, the same Japanese form the credit block's タイトル field carries.
- The sidebar and interwiki furniture effect stands in the code block: four rules gain the JP DOM's selector forms (candidate L624, L634, L642, L662; section 8). The checker's `interwiki-touched` warning at candidate L624 records the first verbatim.
- Verify: `grep -n -- '--header-' candidate.txt` against the original.

## 6. Text translation

- Body prose and exhibits are translated throughout (TRANSLATION-ANCHORED 29 blocks, TRANS-UNANCHORED 25): the headings （テーマカラー / 使用方法 / 使用例）, the usage note, the tabview labels, the collapsible labels, the blockquote and table specimens, and the font specimen lines (candidate L191–193), which still name the Latin faces — those remain the stacks' primaries.
- In-CSS text (class R1, porter-visible): the S-CSS-P header comments and some 22 section comments are translated (COMMENT-TEXT 14 blocks). The reader-visible string variables are `--theme-name` (section 5).
- The two residue blocks are heading translations the signatures did not anchor: B13 (original L87 `+ Usage` → candidate L94 `+ 使用方法`) and B17 (original L98 `+ Examples` → candidate L105 `+ 使用例`) — class P10, adjudicated in the appendix.
- One correction rides inside block B53's span: the original's `--theme-base` value is the typo `"black-highlighte"` (original L198), contradicting its own comment; the candidate carries `"black-highlighter"` (candidate L207) and the translated comment's corrected branch name with it. An original-defect correction, recorded here; not a defect of the port.
- Verify: the COMMENT-TEXT and translation spans in `classification.json` against both files.

## 7. Links

- Block (LINK-REPOINT, candidate L96): the usage prose's BHL link is absolutized to `https://scp-jp.wikidot.com/theme:black-highlighter-theme` — the production JP page (class P11 form for a page whose JP home is the production wiki). The checker's `link-label` warning at L96 (label 「詳しくはこちらを参照してください」 against the live title "Black Highlighterテーマ") is recorded verbatim; warnings are recorded, not classified.
- No dead target stands: this lane's checker run found no `link-target-missing` for this file, and the usage line's plain-form BHL reference is adjudicated in section 2.

## 8. Structure

- Closing rule: channel order and component order are preserved, and the code block's rules stand in the original's order. The whitespace-insensitive census finds exactly 30 substantive hunks in the block; besides the sections 4–6 content, they are the four selector extensions below.
- R6 JP-DOM selector extensions (classifier CSS-BODY heuristic, blocks B113, B115, B116, B118): candidate L624 — `#interwiki` gains `iframe.scpnet-interwiki-frame`; L634 — the folded-heading selector gains `#side-bar.side-block.collapsible-block-link`; L642 — the collapsible-block-link rule gains the same alternate selector; L662 — the menu-item sub-text rule gains `#side-bar.side-block.menu-item >.image`. In each, an existing rule's selector list grows by the JP environment's DOM form and the declarations are byte-identical — the same family as ui-jp's filter extension. The lane report proposes naming this shape in patterns/.
- CSS brace balance was checked by depth, not count: both files scan to final depth 0 with minimum depth 0 — the re-indentation displaced no brace.
- The `[[footnoteblock]]` stands on both sides (candidate L1028) under three live footnotes on both sides; nothing was dropped there.

## 9. Formatting only

- The re-indentation (class R7): 109 WS-ONLY blocks — the code block's tab indentation became 4-space indentation wholesale. The TAXONOMY memo names this theme as the R7 index instance (its sample count was 107 blocks; this package's classifier counts 109 WS-ONLY blocks, and 109 is the figure of record here).
- Recorded consequence: the follow-up-diff property is weakened for this file — a future upstream revision cannot be diffed line-cleanly against the port. The compensating record is the substantive census: 30 hunks, all named.
- Body text outside the code block keeps its form.

## 10. Porter annotations

- One annotation was added: the Japanese comment at candidate L200, stating that the Noto Sans JP load serves the body and heading stacks and that the previously Latin-only mono stack gains the JP fallback — the FIX5-FONTSB annotation, riding inside block B52. Its statement matches the bytes (section 4). It is in prose-comment form inside the CSS, class R2's comment carrier.
- No other annotation stands; the S-CSS-P comments are the original's, translated.

## 11. Dispositions and exceptions

- Draft-host lines: candidate L84 (the BHL logo image) and L1032 (the tail `@import`) — pseudo-ref ×2, the T1 baseline's only errors; the tail frame's posting-host form (candidate L1036) is section 3's observation.
- Warnings and info recorded verbatim: `link-label` (L96), `interwiki-touched` (L624); info `important` — 12 `!important` in the delivered CSS, inherited from the original's BHL-derived rules on both sides.
- Ledger (c3): P1 DISPOSITIONED, the posting-procedure convention class — the localize row's only item besides item 36.
- Render row (RENDER-S2-D, EN22): page-overflow 470px@320, 525px@375, 918px@768 (KB-33 / KB-34 family) plus the runtime-hotlink site-theme chain (KB-40, environment layer) — DISPOSITIONED. The sample's T2 returned no machine verdict (exit 2, no summary): a coverage caveat, not a theme defect.
- No class (i) item stands for this theme.

## 12. Verification

- T1 run by this lane on the current candidate: error 2 / warn 2 / info 1 — identical to the stamp baseline and to FIX5-FONTSB's before/after (2/2/1 → 2/2/1).
- T2/T3: FINDINGS with dispositions only (ledger row (c2)).
- T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `c12d56a949499fee589532e0f81cd04c985478ce4237ef3696123d2cf353cb69`); `original.txt` hash equals the sources.tsv value (`462281997ab86aac2e4fb1709dce11bb12bd086ea5ba6c13bfbb684a5ad3b201`); brace-depth scans clean on both files; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 36 (ledger (b) row 153, class D): "LOCALIZE-S2-C checklist item 8 — mono stack is Latin-only; no JP stack reference, no JP load" (T1-ROWS row 138; LOCALIZE-ROWS row 153).
- What the fix was supposed to change: close the pattern-7 gap — a JP face loaded, and named in the mono stack.
- Supplement re-judgement: FIXED, FIX5-FONTSB, commit 3911f7b, "pattern-7 fix".
- Re-derived from this package's bytes, with a precision the supplement's one line hides: at ledger time the body, header and title stacks already named 'Noto Sans JP' (an S2 supplement) but the face was loaded nowhere in the file — a KB-16 load gap — and the mono stack named no JP face at all. Both halves are visible in `original.txt`: the three stacks name the face (original L211–213) and no `@import` for it stands anywhere; the mono stack (original L214) is Latin-only. The fix (candidate L200–201: annotation plus the Noto Sans JP css2 `@import`, in the delivered code block; candidate L223: 'Noto Sans JP' added to the mono stack) closes both halves with one load — the charged mono gap and the uncharged load gap for the three stacks that already named the face.
- Control: the verdict stamp reads PASS computed against 3911f7b — the fix commit is the candidate's last content change. Checker totals identical before and after (2/2/1), per the FONTSB lane report and this lane's re-run.
- Closure: CONFIRMED from the bytes. The supplement's account is correct but compressed; the fuller form above is the record.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-uiu-bhl-theme-jp.txt` — the render-check sample page for this theme.
2. `pages/theme-decoration-sample-uiu-bhl-theme.txt` — the EN-named sample also present in the repository (the render lane's working copy); recorded for completeness.
3. No base fragment: the BHL base comes from the JP distribution host (`scp-jp.github.io`), not from a repository file.

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-C) produced the port, including the stack supplements that named Noto Sans JP without loading it; its P1 item was dispositioned, and the font gap became item 36.
- FIX5-FONTSB closed item 36 at commit 3911f7b, the candidate's last content change; the verdict stamp therefore reads PASS rather than STALE.
- The re-indentation (R7) predates the fix in the port's own history; the FIX5 lane's checker control (identical totals) is the evidence the fix itself added no formatting churn.

## Appendix — heuristic and residue adjudication

The classifier reports 2 residue blocks and 26 heuristic blocks. All resolve by shape:

- Residue B13 and B17: `+ Usage` → 「使用方法」 and `+ Examples` → 「使用例」 heading translations (class P10) the signatures did not anchor — section 6. Classifier artefacts, not content questions.
- COMMENT-TEXT heuristic blocks: the in-CSS comment translations — section 6, class R1 (the recorded negative-ledger shape).
- CSS-BODY blocks B113, B115, B116, B118: the four R6 selector extensions — section 8.
- CSS-BODY block B55: the P7 font-stack rewrite — section 4 (font rewrites are narrated as P7 even when the classifier labels them CSS-BODY).
- EXHIBIT-RESTRUCTURE primaries B3, B5, B9, B181: include-prefix changes inside exhibit-adjacent regions; the exhibit census (section 2) shows nothing dropped or restructured — false fires.
- Remaining TRANS-UNANCHORED blocks: body prose translations — section 6.

No heuristic or residue block is left unadjudicated.

## License and attribution

- **Title:** Unusual Incidents Unit BHL Theme
- **Author:** Woedenaz
- **Source:** https://scp-wiki.wikidot.com/theme:uiu-bhl-theme — revision 88
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
