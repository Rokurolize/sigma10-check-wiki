# Review package — theme:vanguard-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:vanguard-jp — origin EN, population #155 [GOSIGN2-LEDGER (b) row 155]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 88b6481b45033d0fe5a2f309357f5cd6a2546fd454144908aab0323a0536fd1b); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 4 warns / 1 info (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 170; GOSIGN2-LEDGER (b) row 155]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 330px@320 + 385px@375 + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 155, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 155]
- FIX5 re-judgement: item 37 (class B) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 37]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:vanguard-jp.txt sha256:88b6481b45033d0fe5a2f309357f5cd6a2546fd454144908aab0323a0536fd1b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:vanguard` on scp-wiki (EN), revision 10 — `original.txt` in this package (452 lines / 9,125 bytes; `wc -l` reports 451, last line unterminated) |
| Candidate | `theme:vanguard-jp` — `candidate.txt` (478 lines / 10,746 bytes), a byte copy of `pages/theme:vanguard-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the EN Black Highlighter sub-theme carried over with the JP credit form, the JP license box, the standard head frame, the translation and the JP font supplement applied. |

This theme's `review/sources.tsv` note column is empty: no supersession correction is owed for this package.

Status note: the verdict stamp above reads STALE by design. The stamp was computed against canonical commit b5cb724 — the usage-example sweep changed the candidate (its two usage lines) after the FIX5 verdict was computed. The stamp's verdicts describe the pre-sweep file; the per-theme record below re-derives the theme's one blocking item on the current bytes, which is the point of the STALE form.

Summary: a BHL sub-theme for the Vanguard organization, with a parameter-gated dark mode delivered as a second code block. The port adds the standard head frame the original lacks, swaps in the preview credit and the JP license-box form, re-hosts the logo and the exhibit street photograph, applies the pattern-7 font supplement, and translates the body. The dark code block is byte-conserved (a whitespace-insensitive census finds 0 substantive hunks in it; the main block has exactly 5, all named below). The theme carried one blocking item, 37 (class B), re-derived in the per-theme record.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 3 |
| CONTENT-STRING | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 2 |
| DRAFT-HOST | 2 |
| EXHIBIT-RESTRUCTURE | 5 |
| HEADERVAR | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 3 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 2 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 12 |
| TRANSLATION-ANCHORED | 15 |

Counts: 43 blocks, 31 specific, 11 heuristic, 1 residue, 0 skipped (comment text). Topology: module-css + code-css on both sides, no moves, external own delivery true.

## 1. Credit and attribution

- The original has no credit block; its attribution is the intro prose ("created by `[[*user MisterFrown]]`", original L45) and the code-block banner ("Vanguard Theme by MisterFrown", original L174). The candidate's credit block (candidate L21–31; block B3, CREDIT-PREVIEW + TASL-FIELDS) carries the eight ruling-3 fields plus one extra line: both 著作権者 `[[*user MisterFrown]]` (L27) and a plain 著者： MisterFrown (L25) name the person the original names, in two carriers. No pointer-in-place-of-a-name defect stands. Ledger (c3): P3 credit fields FIXED by the credit waves, checker-verified.
- The bare `[[module Rate]]` that stood at original L8–10 is this theme's blocking item 37; the per-theme record re-derives its removal. Census: `[[module Rate]]` 1 → 0 (class P3 / KB-09, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa: the preview credit module is rate-bearing).
- License box (blocks B39, B40): the original's `component:license-box-theme` (original L430–437, one entry) becomes `:scp-jp:component:license-box-backend` with `author=MisterFrown` (candidate L454–463) — class T4 applied as a form swap, not an addition, since the original already carried the box. Its single entry is carried and translated: the exhibit street photograph （ファイル名： street.jpg — the name the re-hosted exhibit file carries, section 4; 作者： epSos.de; ライセンス： CC BY-SA 2.0 with the deed.ja link; 出典： Wikimedia Commons). Nothing the original's box carried was dropped.
- T7 credit-module CSS: none in either file.
- Verify: `grep -c 'module Rate'` on both files (1 / 0); read candidate L21–31 and L454–463 against original L45, L174 and L430–437.

## 2. Includes and components

- Live includes: the head frame ×3 (section 3), the credit pair (section 1), `theme-squares` repointed to `:scp-jp:` (candidate L45), the image-block exhibit (candidate L96; its `name=` is re-hosted, section 4), the license pair (section 1), and the tail furniture `component:centered-header-bhl` and `component:toggle-sidebar-bhl`, repointed to `:scp-jp:` (original L441–442 → candidate L467–468; block B41) and kept outside the gate, as in the original.
- Usage examples (blocks B10, B12; original L49–57 → candidate L72–80): both `@@`-escaped include lines are repointed — `:scp-jp:theme:black-highlighter-theme` (the production JP base page) and `:scp-jp:theme:vanguard-jp` (the candidate's own name) — and the dark variant's include-parameter gate form `|dark=--` is preserved verbatim (candidate L78–80). The classifier's COMPONENT-SWAP labels on these blocks are its name for the repoints.
- The EXHIBIT-RESTRUCTURE primaries (B6 theme-squares, B15 image block, B39/B40 license box, B41 tail furniture) are include-form changes at exhibit loci; the exhibit census (section 8) shows nothing dropped or restructured.
- Verify: `grep -n 'include' candidate.txt`.

## 3. Delivery and code loading

- The candidate adds the head frame the original lacks (candidate L6–17): three `component:interwiki-style` includes — priority 1 (normalize) and 2 (BHL) from the JP distribution, priority 3 naming own `/1` on the draft host — and the `[[iftags +テーマ]]` gate moves below it (block B1: the original's gate opened at its L1, ahead of its head module; the candidate's gate opens at L19), so delivery is not tag-gated. Ledger (c3): P6 FIXED by the frame waves, checker-verified.
- Block B2: the BHL pair is repointed from `nu-scptheme.github.io/Black-Highlighter/stable/styles/` to `scp-jp.github.io/Black-Highlighter/css/min/` — the JP distribution's host and path form (classes P4 / T9).
- The original's tail is kept: block B42 (original L445 → candidate L471), the tail module's `@import` repointed from `scp-wiki.wikidot.com/theme:vanguard/code/1` to the draft-host `local--code/theme%3Avanguard-jp/1`; block B43 (original L449–450 → candidate L475–478), the `{$dark}` comment gate with its module importing own `/2`, form preserved.
- Census: exactly two code blocks stand on each side (candidate L195–359 main, L361–448 dark), and the addresses name `/1` and `/2` in document order — the blocks that hold the CSS. Self-delivery census: MATCH (class FIX-CODEADDR). Own-CSS delivery is duplicated by design: the head frame's priority 3 and the tail module both serve `/1` — the standard supplement frame over the kept original tail.
- Gate placement: the `{$dark}` gate stands in the theme page's render-time text (candidate L475–478), not inside a URL-delivered code block, so the include-parameter substitution reaches it — the delivery-chain test the campaign's parallel gate repair established. A gate inside the code block would be inert even if correctly formed; this one is not.
- Verify: `grep -n 'local--code' candidate.txt` (addresses `/1` twice, `/2` once); count `[[code` blocks (2).

## 4. Fonts and assets

- Block B34 (original L178–179 → candidate L201–203): the two Latin imports (Zilla Slab; Alegreya SC) swap host from `fonts.bunny.net` to `fonts.googleapis.com` css2 with family specifications byte-identical, and a Noto Sans JP css2 load is added (candidate L203). Block B37 (candidate L217): `--header-font` becomes `'Zilla Slab', 'Noto Sans JP', serif`. Block B38 (original L311 → candidate L335): the `.vantitle` stack gains 'Noto Sans JP'. This is the S2 pattern-7 supplement (class P7); no (e) item charged fonts for this theme. Every stack that names the JP face is served by the L203 load, in the delivered main block.
- The porter prose at candidate L33 announces the program (all fonts OFL 1.1, loaded from Google Fonts, Noto Sans JP serving Japanese text) — section 10.
- Assets: block B4 (original L13 → candidate L36): the BHL logo is repointed to `scp-jp.wdfiles.com/local--files/theme%3Ablack-highlighter-theme/black-highlighter-logo.svg` (posting-host form). Block B35 (original L189 → candidate L213): `--logo-image` is re-hosted to SCP-JP storage (`scp-jp-storage.wdfiles.com/local--files/file%3A2963469-77-1a78/vanguard transparent.png`) — class P5. Block B15: the image-block exhibit's street photograph, which the original took from borealis-constant-theme's EN attachments, is re-hosted as the candidate's own draft-host attachment `street.jpg` (candidate L96 — the checker's pseudo-ref error there); the license entry names the same file (section 1).
- Verify: `grep -n 'Noto Sans JP' candidate.txt` (load, two stacks, the L33 prose); `grep -n 'street' candidate.txt` (exhibit and license entry agree).

## 5. Header, sidebar and site furniture

- Block B36 (HEADERVAR, original L191 → candidate L215): `--header-subtitle` "SHELTER, NORMALIZE, INFORM" → 「保護、正常化、告知」. The slogan is a complete prose sentence rendered for every reader, so it translates under the T5 boundary (names, brand marks and slogans functioning as marks stay as identity strings; this one is prose). `--header-title: "ANGUARD"` is kept — the mark itself, its missing V being the logo's design — and `--theme-name: "Vanguard Theme"` is kept as an identity string.
- The tail furniture (centered-header, toggle-sidebar) is section 2; the header's own rules in the code block are carried unchanged.
- Verify: `grep -n -- '--header-' candidate.txt` against the original.

## 6. Text translation

- The body is translated throughout (TRANSLATION-ANCHORED 15 blocks, TRANS-UNANCHORED 12): the headings （テーマカラー / これは何？ / 例 / DivとSpan / ソースコード）, the intro, the usage prose, the exhibit specimens (tabview, headings, blockquote, table), the collapsible labels, and the footnote specimen's text （脚注例）.
- The one residue block is a heading translation: B14 (original L67–68 `+ Examples` → candidate L90–91 `+ 例`), class P10, adjudicated in the appendix.
- The code blocks' comments are minimal and kept as identity/provenance lines ("Vanguard Theme by MisterFrown", "Dark Mode").
- Verify: the translation spans in `classification.json` against both files.

## 7. Links

- Block B8 (original L45 → candidate L68): the intro's two links. `[[[no-return-hub|ヴァンガード]]]` — target kept, label translated; probed by this lane on 2026-11-17, `https://scp-jp.wikidot.com/no-return-hub` serves 200, so the kept target resolves in the JP environment. `[[[theme:foxtrot|Foxtrot]]]` — target kept; probed the same day, `https://scp-jp.wikidot.com/theme:foxtrot` serves 200 (the production JP page of the parent theme; the T1 checker's link-label warning independently names its live title, "Foxtrotテーマ"). The campaign's own candidate `theme:foxtrot-jp` also exists, but the link as written is live and names the same theme — the monotypical production-page ground (section 2 of the uiu package states the same adjudication). Recorded with probe evidence; not edited, and not a defect.
- Block B13 (original L62 → candidate L85): the BHL prose link is absolutized to `https://scp-jp.wikidot.com/theme:black-highlighter-theme` (class P11 form; production page).
- Block B16 (original L78 → candidate L101): the example-link specimen `[[[misterfrown |リンク例]]]` is kept as the original's specimen, beside the footnote specimen. The checker warns `link-target-missing` (no `misterfrown` page on scp-jp). The warning is recorded verbatim; the specimen's function is to show a link's rendering, and both sides carry it identically.
- The two `link-label` warnings (candidate L68, L85) are likewise recorded verbatim; warnings are recorded, not classified or fixed (campaign rule).

## 8. Structure

- Closing rule: both code blocks stand in the original's order and the dark block is byte-conserved — the whitespace-insensitive census finds exactly 5 substantive hunks in code block 1 (the font host swap and JP load, the logo re-host, the subtitle translation, the two stack appends; sections 4–5) and 0 in code block 2. Structural change is confined to the gate's relocation below the new head frame (section 3) and the credit/license furniture swaps (section 1).
- Exhibit census: theme-squares, the image block, the footnote specimen, the heading/blockquote/table specimens, the tabview, the twosideblock and vantitle specimens, and both code exhibits all stand against the original. Nothing was dropped or escaped away.
- The footnote specimen deserves its line: both sides carry one live `[[footnote]]` and no `[[footnoteblock]]` — parity with the original's own form (KB-59 family), not a candidate drop.
- CSS brace balance was checked by depth, not count: both files scan to final depth 0 with minimum depth 0.

## 9. Formatting only

- None. WS-ONLY is 0 blocks: the candidate preserves the original's blank-line rule separation inside both code blocks. Formatting churn is confined to the frame and credit regions named elsewhere.

## 10. Porter annotations

- One porter addition stands in body prose rather than comment form: candidate L33, the font-program statement (all fonts OFL 1.1, loaded from Google Fonts, Noto Sans JP serving Japanese text). It announces the section-4 supplement; its statement matches the bytes. Class R2 in its prose carrier — recorded here so the shape is visible to the patterns loop.
- No comment-form annotations were added; the code blocks' comments are the original's.

## 11. Dispositions and exceptions

- Draft-host lines (pseudo-ref ×3, the T1 baseline's errors): candidate L96 (the exhibit image's `name=`), L471 (the `/1` import), L476 (the `/2` import) — class (iii) draft forms, rewritten at posting.
- Warnings recorded verbatim: `link-label` ×2 (L68, L85), `link-target-missing` ×1 (L101, the specimen; section 7).
- Render row (RENDER-S2-D, EN23): page-overflow 330px@320 and 385px@375 (KB-33 / KB-34 family) plus the runtime-hotlink site-theme chain (KB-40, environment layer) — DISPOSITIONED. The sample's T2 returned no machine verdict (exit 2): a coverage caveat, not a finding.
- The STALE stamp's ground is section 0's status note: the post-verdict change is the usage sweep's two lines (section 2), and no re-judgement is fabricated for it.
- The kept foxtrot and no-return-hub links (section 7) stand as recorded with probe evidence, not as exceptions.
- No class (i) item stands for this theme.

## 12. Verification

- T1 run by this lane on the current candidate: error 3 / warn 3 / info 0 — FIX5-FURNA's after state (3/3/0); the stamp baseline (3/4/1) describes the pre-FIX5 file.
- T2/T3: FINDINGS with dispositions only (ledger row (c2)).
- T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `88b6481b45033d0fe5a2f309357f5cd6a2546fd454144908aab0323a0536fd1b`); `original.txt` hash equals the sources.tsv value (`2b1bcd97cef3b4454b0fb2e31f5610cd69fdf63c8f9f9b9676168610d256c59a`); brace-depth scans clean on both files; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 37 (ledger (b) row 155, class B): a duplicate bare `[[module Rate]]` standing next to the preview credit module — two rating widgets on one page (T1-ROWS row 170; LOCALIZE-ROWS row 155; the theme's (c3) line records P3 FIXED by the credit waves and P6 FIXED by the frame waves, and the (e) item arose on the credit row).
- History: LOCALIZE-S2-C checklist item 14 had left the Rate an unmade staff call under the exhibit-exception reading — a labelled paired exhibit may keep a demonstration Rate.
- What the fix was supposed to change: remove the duplicate module, leaving the rate-bearing preview credit as the page's only rating widget — if the exception did not cover the block.
- Supplement re-judgement: FIXED, FIX5-FURNA, commit 9e8931f. The FURNA lane report's evidence: the block at pre-edit candidate L20–22 was unlabelled (`[[>]]` / `[[module Rate]]` / `[[/>]]`), immediately before `credit:start-preview` — not the labelled paired exhibit the exception covers, so the exception does not apply; checker 3/3/1 → 3/3/0, the `double-rate` info cleared, no new errors.
- Re-derived from this package's bytes: the original carries the identical bare Rate at original L8–10, inside its gate ahead of the intro. The current candidate contains no `[[module Rate]]` anywhere (`grep -c` = 0) and its credit block stands alone at candidate L21–31. This lane's checker run reports 3/3/0 with no `double-rate` line.
- Closure: CONFIRMED on current bytes — which matters here, because the verdict stamp is STALE (section 0): the closure is re-derived from the package, not inherited from the stamp.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-vanguard-jp.txt` — the render-check sample page for this theme.
2. `pages/theme:vanguard-supplement-jp.txt` — the sibling candidate (its own population row, #156; the FIX5 item 38 theme), related by name only; it is not part of this package.
3. The candidate's own delivered files: the re-hosted exhibit photograph `street.jpg` and the storage-hosted logo (section 4).

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-C) produced the port: P3 credit fields fixed by the credit waves, P6 by the frame waves (the head frame and gate relocation), the font supplement applied; the bare Rate survived that wave as the unmade staff call.
- FIX5-FURNA (commit 9e8931f) removed the Rate and closed item 37.
- The usage-example sweep (commit b5cb724) then completed the two usage lines' `:scp-jp:theme:vanguard-jp` names — the post-verdict change behind the STALE stamp. The sweep touched nothing else in this file: the per-theme record's grep census runs on the swept file.

## Appendix — heuristic and residue adjudication

The classifier reports 1 residue block and 11 heuristic blocks. All resolve by shape:

- Residue B14: the `+ Examples` → 「例」 heading translation (class P10) — section 6. A classifier artefact, not a content question.
- EXHIBIT-RESTRUCTURE primaries B6, B15, B39, B40, B41: include-form changes at exhibit loci (theme-squares prefix, image-block repoint and re-host, license-box form swap, tail furniture repoints) — sections 1, 2, 4, 8. The exhibit census shows nothing dropped or restructured; false fires.
- CSS-BODY block B37: the `--header-font` P7 stack append — section 4 (font rewrites are narrated as P7 even when the classifier labels them CSS-BODY).
- Remaining TRANS-UNANCHORED blocks: body prose translations — section 6.

No heuristic or residue block is left unadjudicated, and no defect flag arises from this package: the one candidate flag considered during analysis (the kept `theme:foxtrot` prose link) was discharged by probe evidence, recorded in section 7.
