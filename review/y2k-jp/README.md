# Review package — theme:y2k-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:y2k-jp — origin EN, population #43 [GOSIGN2-LEDGER (b) row 43]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2b47d82fc95a275fa29370f56a516711c6c16de02933b2d7d42e2478dc25475a); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 0 warns / 3 infos (http×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 43; GOSIGN2-LEDGER (b) row 43]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — `logo.png` broken in chromium at ≤768 (load-failed/ORB, real broken asset), custom header tagline clips at ≤375 both edges, mobile sidebar handle overlaps body text at 320; T2 sample no machine verdict (webkit never completes). [RENDER-ROWS-1 (RENDER-D2 row 43)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-D2 row 43)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 43, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 43]
- FIX5 re-judgement: items 10 (class D) FIXED, 11 (class H) FIXED, 12 (class C) FIXED — FIX5-INFO, commit 9a1c86a: y2k font import and stack suffixes (pattern 7); heading '+ Examples' -> '+ ' (JP) and collapsible labels translated; orphaned info body text inside the credit panel removed. Lane documented on evidence (all five git revisions) that no literal info:start include ever existed; the ledger's wording was loose and the actually charged residue was removed [GOSIGN2-LEDGER-SUPPLEMENT (a) items 10–12]
- Computed against: canonical commit 87c92400a1bc327a00c056d29f538f62762ce4c5; candidate file pages/theme:y2k-jp.txt sha256:2b47d82fc95a275fa29370f56a516711c6c16de02933b2d7d42e2478dc25475a; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Candidate | `theme:y2k-jp` — `pages/theme:y2k-jp.txt`, 505 lines (the last line is unterminated), 12,292 bytes (sha256 in the stamp) |
| Original | `theme:y2k` on scp-wiki (EN), reference revision 16 (the re-translation revision) — `original.txt`, 462 lines, 9,625 bytes, sha256 matches `review/sources.tsv` |
| Class | R-fix — three blocking items (ledger items 10, 11, 12), FIXED in FIX5 |
| Reference-revision record | `start-themes.tsv`: "Complete (no change: keeps the JP-side color scheme)", delivery "Apply the diff page to the existing page", dependency Sigma-10, first-translation rev 15 / re-translation rev 16 |

Provenance route: production adoption (route R4). A production page theme:y2k exists on scp-jp; the candidate is that page adopted as the migration base, and the migration itself is delivered as `pages/phase17-diff-y2k-jp.txt`. The mirror is the EN original at rev 16, the later of the two recorded reference revisions. The credit block's translator credit (H0H0, 2024) is the production page's own and is kept as authored.

Status note: the verdict stamp is STALE by design. It computes the go-sign verdict against the 435a6bb-era bytes; the candidate changed in canonical 358955e after that verdict (the snippet audit repointed the usage include to the -jp name). The per-theme record re-derives all three FIX5 closures on the current bytes.

A year-2000 desktop theme. The candidate is the live JP production page: a credit block with a two-revision translation record, the original's labelled Rate specimens kept as a paired exhibit, the stylesheet's assets re-hosted to JP storage, a pattern-7 font supplement (FIX5 item 10), and three SCP-JP correction modules appended after the gate. Items 10–12 are re-derived below; one minor uncharged defect is flagged in §6.

## Class summary

| Label | Blocks |
|---|---|
| ASSET-REHOST | 2 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 2 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 6 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 26 |
| TRANSLATION-ANCHORED | 11 |

Counts: 55 blocks, 27 specific, 26 heuristic, 2 residue, 0 skipped (comment text).


Component topology (classifier): the candidate adds three module-css components (the tail correction modules, §3); no moves.

## 1. Credit and attribution

What: the candidate's preview credit block (cand L19–29; B7) carries nine fields — the standard eight plus 改訳時参照リビジョン 16 — recording both reference revisions (初訳時参照リビジョン 15, 改訳時参照リビジョン 16). 著作権者 names etoisle, the author the original names (body at orig L27, "developed by [[*user etoisle]]"; stylesheet banner "By etoisle", orig L121); no pointer stands in place of a name. 翻訳者 H0H0 / 翻訳年 2024 is the production translator's credit, kept as authored — the campaign's AI-translation credit applies to campaign translations, not to an adopted production page. タイトル Y2Kテーマ against 原題 Y2K Theme. The labelled specimens: the original's paired exhibit (orig L12–19: a [[>]] block labelled **Rating:** holding a bare Rate module, beside the credit-module form) stands translated at cand L10–17, labels rendered 評価： and クレジット付き評価モジュール. The bare Rate at cand L12 is a labelled specimen inside that paired exhibit, not the duplicate-widget defect (patterns/ KB-09, commit 9c5e907); the T1 checker's double-rate note on this file is info-level and its own text allows the specimen reading. The T7 credit CSS stands inside the stylesheet's 日本語ローカライズ supplement block (cand L466–480; B54): .creditRate's shadow removed, .creditButton restyled — production credit styling (patterns/ KB-32 family).
Why: the preview credit is the JP environment's rate-bearing credit form (P3); the two-revision field set is this theme's TASL shape, recording that the production page was translated twice against two EN revisions.
Verify: read cand L10–29 against orig L12–27 and orig L121.
Disposition: ledger (c3) row 43 records P3 FIXED by the credit waves.

## 2. Includes and components

What: the frame include is repointed to :scp-jp: (cand L5–8; B2, B3). The credit pair stands at cand L19/L29. Image-block stands at cand L43 (B12). The usage include at cand L36 (B10: COMPONENT-SWAP, ESCAPED-INCLUDE, INCLUDE-REPOINT) reads `:scp-jp:theme:y2k-jp` — the snippet-audit form (canonical 358955e; §0's status note). The original's info specimen block (orig L21–25: info:start / info:more / info:end around a placeholder sentence) has no counterpart; the credit block stands in its place — the P3 form for an EN info-module theme, since the info module does not render in the JP environment. Item 12's charged residue is the per-theme record.
Why: components must resolve on scp-jp at posting; the credit module replaces the info specimen rather than duplicating it.
Verify: `grep -n "include\|info" candidate.txt` — "info" matches only .fa-info CSS selectors; no info: include stands.
Disposition: item 12 CONFIRMED closed (per-theme record).

## 3. Delivery and code loading

What: the head [[module CSS]] @import is repointed to the draft host's own /1 (cand L2; B1, class (iii)) and the priority-1 frame names the same own /1 (cand L5–8; B3). Census: exactly one code block in the candidate, `[[code]]` at cand L123–481, and it is the stylesheet (359 lines); the /1 address names it — the FIX-CODEADDR audit form: MATCH. Three [[module CSS]] correction blocks stand after [[/iftags]] (cand L485–504; B55): mobile navigation anchoring (≤767px), image-block width (≤479px), and the narrow top-bar teal ground (≤479px) — production-layer corrections, ungated as authored; the third module's [[/module]] is the file's last line, which carries no trailing newline.
Why: own-name delivery keeps the stylesheet with the page; corrections ride as separate modules so they apply after the stylesheet they correct.
Verify: count every code-block form (`grep -c "\[\[code" candidate.txt` = 1); read cand L483–505.
Disposition: the frame line carries the T1 pseudo-ref error (class (iii), §11).

## 4. Fonts and assets

What: item 10's font supplement is re-derived in the per-theme record; its mechanics are the Noto Sans JP import at cand L124 (B44, JPFONT-LOAD) and the `, "Noto Sans JP", sans-serif` suffix on all six "Microsoft Sans Serif" stacks (B45–B47, B51–B53, JPFONT-STACK). The seventh stack, 'Andale Mono', Courier (cand L448), is unchanged on both sides — a Latin mono specimen stack, outside the supplement's census in both the supplement's account and the bytes. Assets: the two stylesheet background URLs are re-hosted from scp-wiki.wdfiles to scp-jp-storage.wdfiles file forms over https — bg.png (orig L174 → cand L182) and logo.png (orig L178 → cand L186) (B48, B49, ASSET-REHOST). The image-block exhibit (cand L43) names the same logo.png in the `http://scp-jp-storage.wikidot.com/local--files/file%3A4094174-4-k55r/logo.png` form — the production page's own form; the T1 http error and the storage-host info attach to this line, and the render row's broken-logo finding is on it (§11).
Why: pattern-7 (patterns/ KB-16): a theme whose stacks name no JP face renders translated text in fallback; the supplement loads the face and stacks it. The storage re-host keeps the theme's images on JP-side storage.
Verify: `grep -n "@import\|font-family" original.txt candidate.txt` and the six-stack census in the per-theme record.
Disposition: the (c1) baseline carries the http and pseudo-ref errors as standing findings (§11); no class (i) item stands on them.

## 5. Header, sidebar, site furniture

What: `content: 'A New Millennium in Security'` (cand L430) stands in English — the header tagline. Under ruling 2's boundary a slogan functioning as a mark stays an identity string (contrast §6's flag: a section heading is prose, a tagline is a mark). The footer link colour: the original's own rule (`#footer a { color: rgb(0, 0, 255) }`, orig L387–389) is removed from its position (B50, CSS-BODY), and the production localization restates the footer colour as teal #008484 inside the 日本語ローカライズ supplement block (cand L466–480) — the delivered value is the supplement's. The narrow top-bar correction module paints the same teal at ≤479px (cand L497–504).
Why: the supplement block is the production page's localization layer; its overrides are the JP page's recorded colour scheme (the /start row: "keeps the JP-side color scheme").
Verify: `grep -n "008484\|#footer a" original.txt candidate.txt`.
Disposition: the render row's tagline-clip line is dispositioned with the row (§11).

## 6. Text translation

What: the body is translated (cand L31–117 against orig L26–111): the intro, the usage instructions, the four tab specimens, the blockquote, the table specimen, and the font specimen sentence (cand L117 names Microsoft Sans Serif, consistent with the stacks of §4). In the translated intro the developer's name stands as plain text where the original links it ([[*user etoisle]], orig L27) — the name is preserved, the user-link form dropped; a minor observation, recorded here (the same shape stands in yossistyle's review attributions). Heading `+ Examples` → `+ 例` (cand L41) and the collapsible labels (cand L49; cand L122) are item 11's loci, re-derived in the record.
**Defect flag (minor, uncharged)**: the section heading `+ Source code` at cand L121 stands in English, directly above the collapsible whose labels item 11's fix translated (cand L122). It is reader-visible prose of exactly the class item 11 charged; no ledger row charges or dispositions it. Flagged for repair; the package is written against the candidate as it stands.
Why: headings and labels are reader-visible text and translate with the body.
Verify: read cand L31–122 against orig L26–116.
Disposition: item 11 CONFIRMED for its charged items (per-theme record); the flag above is new.

## 7. Links

What: the credit block's 元記事リンク (cand L28) names the EN original on scp-wiki.wikidot.com — the recorded origin host in `review/sources.tsv`. No candidate link names a different host from the recorded one for the original page, so no host probe was required. No prose link names a JP page that will not exist; the only JP page references are the frame, the credit apparatus, and the usage include (§2).
Verify: `grep -n "wikidot.com" candidate.txt` and compare against the sources.tsv row.
Disposition: none recorded against these lines.

## 8. Structure

What: the exhibit census stands complete: image-block, the Titles collapsible, the tabview's four tabs, the blockquote, the table specimen, and the source-code collapsible. The info specimen's replacement by the credit block is §2. B55 (CSS-BODY heuristic) is the tail region — [[/iftags]] plus the three correction modules (§3). B50 is the #footer rule's removal locus (§5). Brace-depth scans of both files end at depth 0 with min 0 — no brace damage on either side.
Why: nothing the original carries is dropped; the only structural additions are the production correction modules.
Verify: the depth scan in §12; read cand L483–505.
Disposition: none recorded against the structure.

## 9. Formatting only

What: none as a class — the classifier records no WS-ONLY and no reindent block for this pair. The formatting mass a reader sees is the translation mass of §6.
Verify: classification.json label counts (WS-ONLY absent).

## 10. Porter annotations

What: the three tail correction modules carry English comment annotations (cand L486, L496, L503 — "SCP-JP Wikidot … correction: …"), and the in-stylesheet supplement is commented `/*日本語ローカライズ*/` (cand L466; B54's COMMENT-TEXT span). These are production-layer annotations (R2); their statements match the bytes. The credit block's revision fields are attribution apparatus (§1), not annotations.
Disposition: annotations of this form are the population's R2 shape.

## 11. Dispositions and exceptions

What: the T1 baseline (T1-ROWS row 43) stands as recorded findings, none a class (i) item: http×1 (cand L43, the production storage form, §4), pseudo-ref×1 (the frame's draft form, §3), and three infos — the double-rate specimen note (§1), the storage-host form note (§4), and the !important count. The render row (RENDER-ROWS-1, RENDER-D2 row 43) gives FINDINGS — logo.png broken in Chromium at ≤768px (ORB), the header tagline clipping at ≤375px, a sidebar handle overlap at 320px — DISPOSITIONED (patterns/ KB-47 family: the ORB/infrastructure layer; the remedy is posting-time re-hosting and no source defect was identified); the webkit sample carries no verdict, a coverage caveat. Ledger (c3) records P3 FIXED. The §6 heading flag is a defect recorded for repair, not a disposition.
Verify: T1-ROWS row 43; RENDER-D2 row 43.

## 12. Verification

- T1 checker (`check_source.py --kind theme --translation`), run by this lane on the current candidate: error 2 / warn 0 / info 3 — identical totals and classes to the stamp baseline (T1-ROWS row 43).
- Brace-depth scan (strip strings and comments, track `{}` depth): both files final depth 0, min 0.
- Censuses: code blocks 1; [[module Rate]] 1 (the labelled specimen of §1); info: includes 0.
- Package checks: candidate.txt is byte-identical to the canonical file; original.txt's sha256 equals the sources.tsv value; `python3 review/build_review.py --check` at acceptance (batch report).

## Per-theme record — the FIX5 closures, re-derived

Item 10 [D] (ledger (e) row; supplement, FIX5-INFO).
Charged: pattern 7 — no JP face anywhere: no @import in the file and no JP font named in any stack.
Fix as recorded: canonical commit 9a1c86a (FIX5-INFO) added the Noto Sans JP import and the stack suffixes; `git show 9a1c86a` carries the import line and six font-family lines for this file.
Re-derived: the import stands at cand L124 (`css2?family=Noto+Sans+JP:wght@400;700`). Census: the original's six "Microsoft Sans Serif" stacks (orig L132, L150, L158, L418, L424, L450) all carry `, "Noto Sans JP", sans-serif` in the candidate (cand L140, L158, L166, L423, L429, L455); the seventh stack ('Andale Mono', Courier) is unchanged on both sides. Exactly the supplement's account.
Closure: CONFIRMED.

Item 11 [H] (ledger (e) row; supplement, FIX5-INFO).
Charged: untranslated reader-visible text — the heading `+ Examples` (orig L37) and the collapsible labels (orig L45; orig L116, "> Show code" / "> Hide code").
Fix as recorded: the heading and labels translated in 9a1c86a.
Re-derived: cand L41 reads `+ 例`; cand L49's labels read 見出しを開く / 見出しを閉じる; cand L122's read コードを表示 / コードを閉じる. All three charged loci are translated on current bytes.
Closure: CONFIRMED for the charged items. The uncharged `+ Source code` heading at cand L121 is §6's flag.

Item 12 [C] (ledger (e) row; supplement, FIX5-INFO).
Charged (ledger wording): a stray info:start include line at L20 in the credit area.
The supplement corrects the wording on evidence: no literal info:start include exists in any of the candidate's five git revisions; the actual residue was the orphaned translated info body line あなたの記事に関する情報 standing inside the credit panel, removed by 9a1c86a (`git show 9a1c86a` shows the removal).
Re-derived: the current candidate contains no info: include and no orphan body line — `grep -n "info" candidate.txt` matches only .fa-info CSS selectors. The charged residue is absent; the ledger's phrasing was loose, as the supplement states.
Closure: CONFIRMED, with the wording correction recorded.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:y2k-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX21 item 2, landing `87c92400a1bc327a00c056d29f538f62762ce4c5`** ("pages: R-fix-21 flags repaired …", 2026-11-17, R/review-scout/FIX-RFIX21.md §2; 1 line): candidate L121 `+ Source code` → `+ ソースコード`. Evidence: the untranslated heading was the only "Source code" occurrence in the file, standing directly above the collapsible at L122 whose labels FIX5-INFO item 11 already translated (`show="> コードを表示" hide="> コードを閉じる"`); it is reader-visible prose of exactly the class item 11 charged but which no ledger row dispositioned. The population form `+ ソースコード` stands in 115 candidate files (foundom, eigenvector, turbo-vision, voyager, supply-n-demand, shancheng, rpma, mox); the colon-suffixed variants are only 3 files. Section 6's flag (and §11's reference to it) is kept as the as-built record; the flag is now repaired in the recopied candidate — item 11's closure line "the uncharged `+ Source code` heading at cand L121 is §6's flag" stands as issued. Checker (FIX-RFIX21 §3): plain error 2 / warn 0 / info 3 → 2 / 0 / 3 and `--check-links` 2 / 0 / 3 → 2 / 0 / 3, byte-identical finding sets; the two standing errors are L2 pseudo-ref (class iii) and L43 http (class ii), both on untouched lines; class (i) 0 before and after.

## Change set outside the two diffed files

- `pages/phase17-diff-y2k-jp.txt` — the production-migration delivery named in the sources.tsv row.
- `pages-existing/existing:theme-y2k.txt` — the production counterpart the candidate adopts.
- `pages/theme-decoration-sample-y2k-jp.txt` — the display-check sample (webkit no-verdict caveat, §11).

## Multi-wave provenance

- The production page was translated by H0H0 (first translation against EN rev 15, re-translation against rev 16, 2024) and adopted as the candidate under the K6 production-adoption row.
- FIX5-INFO commit 9a1c86a closed items 10–12 on the adopted file.
- The snippet audit (canonical 358955e) then repointed the usage include to the -jp name — the change that makes the verdict stamp STALE; the three closures were re-derived on current bytes in the record above.

## Appendix — heuristic and residue adjudication

- B5 (residue; orig L12–13 → cand L10–11): the specimen label lines (**Rating:** → 評価：) and their [[>]] frame — §1's labelled specimen; a bare label line carries no signature.
- B11 (residue; orig L36–37 → cand L40–41): the `+ Examples` → `+ 例` heading — item 11's locus (§6, record); a bare heading line carries no signature.
- B50 (heuristic, CSS-BODY): the #footer rule's removal from its original position — §5.
- B55 (heuristic, CSS-BODY): the tail region ([[/iftags]] plus the three correction modules) — §3/§8.
- B54 (heuristic spans COMMENT-TEXT, TRANS-UNANCHORED beside the specific T7-CREDIT-CSS): the 日本語ローカライズ supplement block — §1/§5/§10.
- B2, B12 (specific, EXHIBIT-RESTRUCTURE spans): B2 is the frame-include region (§2/§3); B12 is the image-block exhibit line, whose name= form is the production storage URL (§4). Neither exhibit is restructured in content.
- The TRANS-UNANCHORED mass (26 blocks) and TRANSLATION-ANCHORED blocks (11) are the body and specimen translation — §6, by shape.

## License and attribution

- **Title:** Y2K Theme
- **Author:** etoisle
- **Source:** https://scp-wiki.wikidot.com/theme:y2k — revision 16 (revision date 2025-12-20 09:19:59)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: H0H0 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
