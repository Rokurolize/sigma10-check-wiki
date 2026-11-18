# Review package: theme:supply-n-demand-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:supply-n-demand-jp — origin CN, population #234 [GOSIGN2-LEDGER (b) row 234]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now a9aed09aa078ee45c7eaaf2b5f8bbd1f07cc8424a3596995f1ec59a8d6bcec10); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 2 warns / 1 info (hotlink×5, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 194; GOSIGN2-LEDGER (b) row 234]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 507px@320/375 (page) and 519px@320/375 (sample) + runtime-hotlink site-theme chain + candidate hosts cdn.jsdmirror.com, cdn.scpwiki.com, scp-wiki-cdn.nyc3.cdn.digitaloceanspaces.com; sample credit-modal (preview-form); T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN15)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN15)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 233, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 233]
- FIX5 re-judgement: item 90 (class I) FIXED — FIX5-STRUCTA, commit 8c0cd35: deleted showcase restored, 250 lines copied from original L199-448 at L42-291 with prose and labels translated (26 line-targeted replacements) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 90]
- Computed against: canonical commit cdb1e6daa1f322aa4ec093f5f9967319e746274c; candidate file pages/theme:supply-n-demand-jp.txt sha256:a9aed09aa078ee45c7eaaf2b5f8bbd1f07cc8424a3596995f1ec59a8d6bcec10; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| Item | State |
|---|---|
| Population row | 234 (CN block) |
| Class | R-fix: ledger (e) item 90 (class I), re-judged FIXED by FIX5-STRUCTA [GOSIGN2-LEDGER-SUPPLEMENT (a) item 90] |
| Verdict stamp | STALE: the candidate changed after the 435a6bb-era verdict (FIX-P4 repoint f1138e4 and the usage sweep b5cb724); re-judgement belongs to the refresh-3 pass, not to this package |
| Package contents | original.txt, candidate.txt, classification.json, diff.md, this README |
| Open flags | F1 documentation section drop beyond the restored showcase (section 8); F2 credit title field untranslated (section 1). Flags are recorded, never edited into the candidate |

## Provenance

| Field | Value |
|---|---|
| Original | theme:supply-n-demand on scp-wiki-cn, reference revision 3 |
| original.txt | Byte copy of the frozen mirror; sha256 e4cd95b65b0abed957607c695345018698a2768bb24e81cc8d8f60378dfee4bf, equal to the review/sources.tsv value; 75,646 bytes, 2,886 lines |
| Candidate | pages/theme:supply-n-demand-jp.txt; candidate.txt byte-identical to the canonical file (cmp-verified); sha256 031b7d9c69d907826712968a888571087c870c727af940f1e120c0f38cb3c29a; 73,445 bytes, 2,761 lines |
| Upstream currency | The sources.tsv note claims the original was "superseded upstream since the reference revision". The follow-up artifact it cites (diff-supply-n-demand-from3.txt, campaign record K5a-i) records rev3 to rev3, no changes. The note is wrong; the correct form is: upstream latest remains rev 3, and the S2 artifact records rev3 to rev3 with no changes. Recorded here and in the batch report for the coordinator's harvest correction; sources.tsv is not edited by this package |

## Summary

A CN Sigma+ theme by Chhokmah Lu built for Marshall, Carter & Dark settings. The port adds the preview credit block, repoints the usage examples, consolidates delivery into a single code block served by the tail frame (the author's mirror base imports kept, the Sigma base repointed to the JP mirror by FIX-P4), and, in the FIX5 repair, restores the showcase section whose deletion was the ledger's charge (item 90, re-derived byte-exactly below). Two flags: a documentation region of the original (the color-scheme exhibit and the examples documentation, original L59-202) has no candidate counterpart, a drop separate from the restored showcase (F1); and the credit title field keeps the simplified-Chinese title with no Japanese form anywhere in the candidate (F2).

## 0. Header and provenance

What: the pair diffs at +93 / -227 lines in 7 hunks; the classifier resolves 35 blocks (18 specific, 15 heuristic, 2 residue). The candidate's git history is 9f252b5 (Stage 2 CN15), f1138e4 (FIX-P4), 8c0cd35 (FIX5-STRUCTA), b5cb724 (usage sweep). Why: provenance discipline; the stamp's STALE state traces to f1138e4 and b5cb724 landing after the verdict. Verify: `sha256sum` on both package files against sources.tsv and the stamp; `cmp` candidate.txt against the canonical file. Disposition: stamp STALE as recorded in the Status table; the package is written against the current bytes.

## 1. Credit and attribution

What: the preview credit block (candidate L3-12) carries the full field set; the author field names Chhokmah Lu, matching the original's named author (the author field of its credit block, original L25; prose at original L33; the CSS banner "Created by Chhokmah Lu", original L472). The creation year 2026 matches the original's own banner "[2026 Wikidot Theme]" (original L471), verified against the bytes rather than assumed. The source link's host is scp-wiki-cn.wikidot.com, equal to the host recorded in sources.tsv. CREDIT-PREVIEW and CREDIT-PROSE each fire once; TASL-FIELDS once. Why: TASL completeness; a credit field that names nobody, or a year the original contradicts, breaks attribution. Verify: read candidate L3-12 against the original loci above. Disposition: one defect. F2: the title field (candidate L4) reads 「供求理论 主题版式」, the simplified-Chinese title. The theme's name occurs nowhere else in the candidate under a Japanese form (its only occurrences are candidate L4, L7 and L11, all quoting the original), so this flag's ground is the untranslated title field itself, weaker than a contradiction with the body's own form; the original-title field (L7) and the source-link label (L11) correctly quote the CN title. Flagged for the coordinator's title-field decision, in the same family as the steam-guide flag in this batch; the candidate is not edited.

## 2. Includes and components

What: the credit includes swap from the CN credit pair (original L23, L30) to the JP preview pair (candidate L3, L12). The usage examples are repointed to the candidate's own posting name with its parameters (blocks B5, B7: candidate L19, 25, 31; COMPONENT-SWAP, ESCAPED-INCLUDE and INCLUDE-REPOINT each fire twice). No include stands duplicated. The original's theme-squares include (original L62) has no candidate counterpart; it belongs to the dropped documentation region flagged as F1 in section 8. Why: pattern 11 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): references with a JP counterpart name the JP page. Verify: `grep -n '\[\[include' candidate.txt` against the same census on original.txt. Disposition: no flag in this section; F1 is recorded in section 8.

## 3. Delivery and code loading

What: the original delivers through a head CSS module (original L1-16) importing the author's mirror base stylesheet plus two optional module imports held in CSS-comment parameter gates ({$betterfootnote}, {$togglesidebar}), with the stylesheet itself standing as a code exhibit (original L451-2885) and a small demo code block in the documentation (original L182-188). The candidate consolidates everything into one code block (candidate L297-2750): its head carries a porter comment (L298: 「supply-n-demand：原語版の CSS をまとめたもの」), the three mirror imports with both comment gates preserved verbatim (candidate L299-315), the demo block's content (candidate L312-315), then the stylesheet proper from @charset on. The tail module imports the block from the draft host (candidate L2756, local--code/theme%3Asupply-n-demand-jp/1) and the interwiki-style frame at priority 1 names the same address (candidate L2758-2761); the named block is the stylesheet block, the file's only code block in any form. DELIVERY-MOVE fires in 5 blocks; DUPIMPORT-DEL in 3, recording the removal of the module copy of the three mirror imports, whose single surviving copy stands at candidate L299-309. The FIX-P4 repoint moves the Sigma base from cdn.scpwiki.com/theme/en/sigma to scp-jp.github.io/sigma (block B33, candidate L320); the author's own mirror libraries (the base, sigma-plus.css, editor-icons.css) stay on cdn.jsdmirror.com as in the original. SELF-DELIVERY and DRAFT-HOST each fire once. Why: an own-code address must name the block that holds the CSS, and a base repoint must land on the JP port's delivery, not the EN host. Verify: read candidate L296-325 and L2754-2761; count code blocks in all forms (one). Disposition: no flag. One record: the demo rule absorbed at candidate L312-315 was exhibit-only in the original and is live CSS in the candidate's delivered block; its selectors are the theme's own header selectors and the stylesheet carries its own header rules (candidate L450-451), so the absorption is recorded as a consolidation side effect for the reader, not charged as a defect.

## 4. Fonts and assets

What: no font label fires for this theme. The only font load in either file is the Material Symbols icon font from Google Fonts (original L454, candidate L319), carried unchanged; text faces ride on the Sigma base delivery dispositioned in section 11. HTTP-KEPT fires twice (candidate L557, 567): both are data:image/svg+xml URLs whose xmlns is the W3C namespace string, the classifier's known false-fire, not kept http links. The header background variable names a relative ./img/mcd-bk.jpg path in both files (original L481, candidate L346), resolved against the CSS file's own host as in the original. Why: pattern 7 (patterns/ at 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa) is satisfied by the absence of named-but-unloaded faces in the theme's own text. Verify: `grep -n '@import' candidate.txt` returns the mirror imports, the icon font and the Sigma base only. Disposition: no flag.

## 5. Header, sidebar and site furniture

What: the sidebar option survives as a mechanism: the {$togglesidebar} CSS-comment gate and its module import stand inside the delivered block (candidate L305-311), and the usage example teaching the parameter stands at candidate L25-27. The original's head bare Rate module (original L19-21, above its credit block) is deleted (block B4, BARE-RATE-DEL): the candidate's credit block is the rate-bearing preview form, so a separate bare Rate beside it would double-render the widget, the population census ground for this deletion shape. Why: a documented parameter whose gate survives works; a duplicated rate widget is the failure the deletion prevents. Verify: read candidate L305-311; `grep -ci 'module rate'` returns 1 for the original, 0 for the candidate. Disposition: no flag; the Rate deletion's ground is stated here because it is the section's only furniture change.

## 6. Text translation

What: TRANS-UNANCHORED fires in 21 blocks and TRANSLATION-ANCHORED in 9, carrying the documentation prose, the restored showcase (26 targeted replacements there; see the Per-theme record) and the credit prose. COMMENT-TEXT fires once: the demo block's Chinese comment (「这是代码块」) survives untranslated inside the delivered block (candidate L312), a CSS comment, which is comment-text mass rather than a rendered string. Why: T5 translation completeness on rendered strings. Verify: sample the anchored blocks against diff.md. Disposition: no flag in this section; the untranslated rendered string is the credit title field, flagged as F2 in section 1.

## 7. Links

What: the credit prose and the image-source note (candidate L36-40) keep the Marshall, Carter & Dark wiki as the woodcut background's source, with the image file on themes.wdfiles.com, as in the original. The floating-box note (candidate L45) links the CN sunside theme page as [https://scp-wiki-cn.wikidot.com/theme:sunside 向陽 テーマ（中国語）], with its language annotation, a cross-wiki content reference that resolves where it points; the same note quotes the referenced CN Sigma-9 theme by its original title, a kept quotation of a work's name. The works the prose credits (OxygenNine's editor component, Mercuresphere's theme) are named in text as in the original. Why: content references keep a resolving target; quotations of work titles are not localized text. Verify: read candidate L14 and L36-45. Disposition: no flag.

## 8. Structure

What: the candidate opens with the tag gate [[iftags +テーマ]] (candidate L1); the original opened with its delivery module ahead of its own tag gate (original L18). The centering wrappers around the usage examples balance (4 openers, 4 closers in the candidate); residue block B8's added [[=]] line (candidate L30-31) pairs inside the examples. IFTAGS fires twice; EXHIBIT-RESTRUCTURE in 4 blocks. Why: the tag gate bounds the documentation body while delivery stands outside it. Verify: read candidate L1 and the tail (candidate L2754-2761). Disposition: one defect. F1: the original's documentation region at L59-202 has no candidate counterpart. It holds the color-scheme section (its heading at original L59, the theme-squares include spanning original L62-117 with some twenty named color variables and values), the examples documentation head with its table of contents (original L118-119), the image-block exhibit (original L120), and the typography demo body through original L202. The candidate's documentation passes from the usage examples (candidate L16-40) directly to the restored showcase (candidate L42). The classifier records the collapse in blocks B12 (original L62-66 to candidate L42) and B13 (original L68-202 to candidate L44-45). Only the demo code block's content survived, absorbed into the delivered block (section 3). This drop is separate from the showcase deletion the ledger charged and FIX5 restored (original L199-448; see the Per-theme record), and no record this package cites dispositions it. Flagged with both ranges; the candidate is not edited.

## 9. Formatting only

What: residue block B34 is a file-end difference with empty content (original L2887 to candidate L2752): trailing-line formatting at the end of the file. No WS-ONLY label fires for this theme. Why: an empty trailing difference has no rendered effect. Verify: block B34 in classification.json. Disposition: none, on that ground.

## 10. Porter annotations

What: one porter annotation: the code-block head comment (candidate L298) stating that the block consolidates the original-language CSS, riding block B32. The FIX5 restoration carries no annotation text. The check was made explicitly across the candidate. Why: annotations are the porter's voice and are marked as such. Verify: read candidate L298. Disposition: stands as the standard consolidation note.

## 11. Dispositions and exceptions

What: ledger register (c3) records P4 DISPOSITIONED (delivery class (ii)), P5 DISPOSITIONED (class (ii) / KB-58), P7 DISPOSITIONED (recorded without a display-affecting mark, at the T4 bar) and P9 DISPOSITIONED (ruling 2) for this theme. The T1 baseline (6 errors / 2 warns / 1 info: hotlink x5, pseudo-ref x1) is dispositioned in register c1. The T2/T3 findings (page-overflow 507px at 320/375 on the page and 519px on the sample; the runtime-hotlink site-theme chain; candidate hosts cdn.jsdmirror.com, cdn.scpwiki.com and the scp-wiki CDN) are environment-layer standing findings (KB-40); the sample credit-modal errors are dispositioned preview-form (GOSIGN-TESTS T2 amendment); the T3 re-run added no visual finding, and coverage is chromium-only. T4/T5 record one display-affecting finding, which is item 90. Why: dispositions are the campaign's recorded judgements; this package re-derives the FIX5 one and cites the rest. Verify: the stamp lines above carry each citation. Disposition: as recorded; F1 and F2 are new flags this package adds, covered by no existing disposition.

## 12. Verification

Checks run for this package: sha256 of original.txt against review/sources.tsv (equal); cmp of candidate.txt against the canonical file (identical); classifier and build_review.py runs; credit author, creation year and source-host comparison against the original's credit block and CSS banner; code-block census in every form (one block in the candidate, two in the original); the delivery address check (the tail frame names the stylesheet block); the bare Rate check with its ground; the documentation-region comparison that grounds F1 (headings and distinctive strings on both sides); HTTP-KEPT adjudication (two data-URI namespace false-fires); the FIX5 re-derivation below, including the commit's insertion count and a direct diff of the restored region; and a read of the cited upstream follow-up artifact (rev3 to rev3, no changes).

## Per-theme record: FIX5 re-derivation (item 90)

The ledger charges item 90 (class I) [GOSIGN2-LEDGER (e) item 90] with the deletion of the theme's entire showcase section in porting. The supplement re-judges it FIXED by FIX5-STRUCTA, commit 8c0cd35 [GOSIGN2-LEDGER-SUPPLEMENT (a) item 90]: the showcase restored, 250 lines copied from original L199-448 at candidate L42-291 with prose and labels translated in 26 line-targeted replacements. Re-derived from the bytes: `git show 8c0cd35` for this file is exactly 250 insertions and 0 deletions; candidate L42-291 is 250 lines; original L199-448 is 250 lines; and a direct diff of the two regions differs on exactly 26 lines, the translated prose and labels. Closure CONFIRMED, byte-exactly on every number the supplement states. The boundary matters: the restoration covers original L199-448 only, and the separate documentation drop at original L59-202 (flag F1, section 8) stands outside the item and outside the supplement's account.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:supply-n-demand-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX15 F1, landing `cdb1e6daa1f322aa4ec093f5f9967319e746274c`** ("pages: R-fix-15 flags repaired …", 2026-11-17, R/review-scout/FIX-RFIX15.md §6; +141/−0, a pure insertion): the original's dropped documentation body (orig L58–197) is restored immediately before `+ カスタムスタイル` (now L183), after the candidate's 画像の出典 block — the `++ 配色` heading and theme-squares include with its 11 named colors at L43–46, the `例` heading with `[[toc]]`, the image-block exhibit at L104 (`[[include component:image-block name=https://site-eq-02.wdfiles.com/local--files/theme%3Amcdnew/mcd-bk.jpg|caption=MC&Dの神秘的な背景（小）|width=200px]]`), and the typography demos (rule/heading prose, collapsible heading, tabview, blockquote, code exhibit, two tables). Form decisions (FIX-RFIX15 §6): theme-squares repointed `:scp-wiki:` → `:scp-jp:`, variables/RGB values byte-identical, CN color names kept where they are standard Japanese and translated otherwise; headings `配色方案` → `配色`, `示例` → `例` (steam-guide's own rendering); the image-block URL kept byte-identical (probed 200, image/jpeg, 115,677 B — class (ii) re-host-at-posting, not dead); demo passages follow steam-guide-jp's translated versions where the source text is identical.
The item-90 record's boundary note — that the documentation drop at orig L59–202 "stands outside the item and outside the supplement's account" — is the as-built record; that drop is now repaired in the recopied candidate. Checker (FIX-RFIX15 §8): error 6 / warn 2 / info 1 → 7 / 2 / 1, the +1 being the restored image-block hotlink (class ii, the author's own serving demo image); class (i) 0 before and after.

## Change set

The port is the single file pages/theme:supply-n-demand-jp.txt; its git history names no companion candidate file. Sample pages are shared campaign records and sit outside this package.

## Appendix: residue and heuristic resolution

Residue blocks (2 of 35): B8 resolves to section 8 (the added centering opener inside the usage examples, balanced in the candidate's census); B34 resolves to section 9 (the empty file-end difference). Heuristic mass: 15 of the 35 blocks are heuristic, dominated by TRANS-UNANCHORED prose translation across the documentation and the restored showcase, resolved here by shape, with no content change beyond language. Blocks B12 and B13 carry EXHIBIT-RESTRUCTURE labels but are adjudicated as the F1 documentation drop in section 8, not as restructuring. The two HTTP-KEPT firings are adjudicated in section 4 as the data-URI namespace false-fire.

## License and attribution

- **Title:** 供求理论 主题版式
- **Author:** Chhokmah Lu
- **Source:** https://scp-wiki-cn.wikidot.com/theme:supply-n-demand — revision 3
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
