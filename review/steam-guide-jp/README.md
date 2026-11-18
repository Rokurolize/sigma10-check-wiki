# Review package: theme:steam-guide-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:steam-guide-jp — origin CN, population #233 [GOSIGN2-LEDGER (b) row 233]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 5f72b6fbcb293b2dde1d65b41db52e379815687e8f765f3bb72156644df13033); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 7 errors / 2 warns / 7 infos (hotlink×5, http×1, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 193; GOSIGN2-LEDGER (b) row 233]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 371–372px@320 (both engines) + runtime-hotlink site-theme chain + candidate cdn.jsdelivr.net; sample credit-modal (preview-form) + page-overflow 371px@320; T3 page not separately walked, no additional visual finding; mixed coverage: page full-engine, sample chromium-only (no WebKit verdict). [RENDER-ROWS-G (CN15)]
- Engine coverage: mixed: page full-engine, sample chromium-only [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN15)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 232, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 232]
- FIX5 re-judgement: item 89 (class I) FIXED — FIX5-STRUCTA, commit 8c0cd35: deleted ListPages wrapper restored at L2 verbatim from original L188; four CN credit includes repointed to :scp-jp:credit:*; spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) item 89; (c) check 2]
- Computed against: canonical commit cdb1e6daa1f322aa4ec093f5f9967319e746274c; candidate file pages/theme:steam-guide-jp.txt sha256:5f72b6fbcb293b2dde1d65b41db52e379815687e8f765f3bb72156644df13033; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| Item | State |
|---|---|
| Population row | 233 (CN block) |
| Class | R-fix: ledger (e) item 89 (class I), re-judged FIXED by FIX5-STRUCTA [GOSIGN2-LEDGER-SUPPLEMENT (a) item 89] |
| Verdict stamp | STALE: the candidate changed after the 435a6bb-era verdict (usage-example sweep b5cb724); re-judgement belongs to the refresh-3 pass, not to this package |
| Package contents | original.txt, candidate.txt, classification.json, diff.md, this README |
| Open flags | F1 credit title field (section 1); F2 plain-slug self-delivery import (section 3); F3 plain-slug guide links (section 2); F4 include-parameter gates absent (section 2). Flags are recorded, never edited into the candidate |

## Provenance

| Field | Value |
|---|---|
| Original | theme:steam-guide on scp-wiki-cn, reference revision 10 |
| original.txt | Byte copy of the frozen mirror; sha256 7669b325b0411c85d2312b2ad8ac23b7ac18f1ef6648df5ad5faffe1ec6f7345, equal to the review/sources.tsv value; 63,530 bytes, 2,307 lines |
| Candidate | pages/theme:steam-guide-jp.txt; candidate.txt byte-identical to the canonical file (cmp-verified); sha256 3568fbc8ee7b52091a3a8080db68441eb25a5590149ccfcf744c3d47fdc5e1f9; 62,209 bytes, 2,136 lines |
| Upstream currency | The sources.tsv note claims the original was "superseded upstream since the reference revision". The follow-up artifact it cites (diff-steam-guide-from10.txt, campaign record K5a-i) records rev10 to rev10, no changes. The note is wrong; the correct form is: upstream latest remains rev 10, and the S2 artifact records rev10 to rev10 with no changes. Recorded here and in the batch report for the coordinator's harvest correction; sources.tsv is not edited by this package |

## Summary

A documentation-heavy CN guide theme by hoah2333, built in the original around 17 include-parameter gates and six ListPages modules. The port keeps the guide body and the single large stylesheet, repoints credit and component references to scp-jp, restores the ListPages wrapper whose deletion was the ledger's structural charge (item 89, re-derived below), and delivers the stylesheet from the candidate's own code block through the tail frame. Four defects are flagged for the coordinator: the credit title field keeps the simplified-Chinese title against the body's own Japanese form (F1); one self-delivery import names the plain un-suffixed slug (F2); four guide links name the plain slug on the JP host (F3); and the include-parameter gate definitions are absent while the documentation still teaches the parameters (F4).

## 0. Header and provenance

What: the diff is Tier 2: +201 / -372 lines, 573 changed lines in 108 blocks across 16 sections; review-stage comments account for 0 of the +201 added lines. The candidate's git history is 9f252b5 (Stage 2 CN15), f931619 (FIX2-COLON), 443c608 (FIX4-REPOINT), 8c0cd35 (FIX5-STRUCTA), b5cb724 (usage sweep). Why: provenance discipline; the stamp's STALE state traces to b5cb724 landing after the verdict. Verify: `sha256sum review/steam-guide-jp/original.txt` against review/sources.tsv; `cmp review/steam-guide-jp/candidate.txt pages/theme:steam-guide-jp.txt`. Disposition: stamp STALE as recorded in the Status table; the package is written against the current bytes.

## 1. Credit and attribution

What: the preview credit block (candidate L3-11) carries the full field set; the author field names hoah2333, matching the original's named author (original L217 prose; creator machinery at original L444-446 and L564-566). The source link's host is scp-wiki-cn.wikidot.com, equal to the host recorded in sources.tsv. Neither file carries a license box (no license string in either). Croquembouche (candidate L28) is a design reference, not a co-author. Why: TASL completeness (TASL-FIELDS fired once); a credit field that names nobody, or the wrong host, breaks attribution. Verify: read candidate L3-11 against the original loci above. Disposition: one defect. F1: the title field (candidate L4) reads 「游戏指南 版式」, the simplified-Chinese title, while the candidate's own body names the theme 「ゲームガイド」 (candidate L209 and L233). The original-title field (L7) and the source-link label (L11) correctly quote the CN title; the title field is the one field that should carry the form the body uses (the suprematism item-91 family). Flagged with both forms; the candidate is not edited.

## 2. Includes and components

What: the credit demo includes are repointed to :scp-jp:credit:* targets (the item-89 repair; see the Per-theme record). COMPONENT-SWAP, INCLUDE-REPOINT and ESCAPED-INCLUDE each fire in 8 blocks: usage examples and demo machinery now name :scp-jp: pages in the post-sweep form. The toggle-sidebar include inside a %%content region is repointed (residue block B62: original L374 to candidate L186). Why: pattern 11 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): references with a JP counterpart name the JP page, so a reader following the documentation reaches a page that exists. Verify: `grep -n '\[\[include' candidate.txt` against the same census on original.txt. Disposition: two defects. F4: the original defines 17 include-parameter gates (comment gates at original L1, 5, 11, 18, 63, 69, 82, 94, 132, 136, 140, 150, 155, 159, 162, 179, 182: inc-css-only, inc-source, inc-preview, inc-sticky, inc-sidebar-start/end, inc-creator, inc-panel-start/end, inc-content-start/end, achi-left/right, inc-achi, clear). The candidate defines none (no gate opener anywhere), while at least ten escaped usage examples still teach the inc-* parameters (candidate L312, 321, 340, 352, 354, 356, 358, 373, 397, 399) and the gate contents stand inlined as static body content (the guide preview, candidate L185-245, replaces the ListPages variables with fixed sample values). A documented mechanism whose definitions are absent is a flag, not a supplement; the frame-based base CSS delivery is unaffected. F3: four guide links (candidate L31, 32, 33, 183), each reading [http://scp-jp.wikidot.com/theme:steam-guide/offset/1/page2_limit/1 こちらから確認できます], point at the plain slug theme:steam-guide on the scp-jp host over http. No production theme:steam-guide page exists (the population's page census holds only the -jp candidate and its samples), so the links name a page that will not exist (pattern-11 family; the starry item-88 precedent). The fourfold repetition itself is inherited (original L219-221 plus L371) and is not a defect.

## 3. Delivery and code loading

What: the original delivers through module-css fragments inside its parameter gates (original L5-8, L12-15, L18-23) plus one large code block (original L603-2304, 1,701 lines). The candidate carries one code block (candidate L423-2125, 1,702 lines) delivered by the tail module import (candidate L2131, draft host, naming local--code/theme%3Asteam-guide-jp/1) and the interwiki-style frame at priority 1 naming the same address (candidate L2133-2135). The named block is the stylesheet block itself; a census of every code-block form finds exactly one block. SELF-DELIVERY fires in 5 blocks. Why: an own-code address must name the block that actually holds the CSS (the FIX-CODEADDR census family). Verify: read candidate L2129-2136; count code blocks in all forms in both files. Disposition: one defect. F2: candidate L188, inside the page2 ListPages %%content module css, imports https://scp-jp.wdfiles.com/local--code/theme%3Asteam-guide/1, the plain slug, from the JP files host. Original L376 named the same plain slug on scp-wiki-cn.wdfiles.com, which was correct for the CN page; the port repointed the host but not the page name, so the address names a JP page that will not exist, where the block it should name is theme:steam-guide-jp/1 (block B63). FIX-CODEADDR.md carries no steam-guide entry: that audit matched own-fullname references, so a plain-slug reference escaped its census (see the patterns proposal in the batch report). The main frame delivery is correct, so the defect is confined to the page2 preview channel.

## 4. Fonts and assets

What: the code head imports (original L605-607) load Noto Sans SC, Fira Code and Font Awesome 4.7.0; the candidate (L426-428) loads Noto Sans JP, Fira Code and Font Awesome 4.7.0, a one-to-one swap at identical relative loci (JPFONT-LOAD once, block B102). Stacks swap SC to JP throughout (FONTLOAD-CJK-STACK in 5 blocks; e.g. block B103, original L676 to candidate L497); no Noto Sans SC string survives in the candidate (grep count 0). The stacks naming Fira Code with a CN fallback font name and Cousine (candidate L1651, 1658) are inherited verbatim from the original (original L1830, 1837): the CN font name is a fallback entry behind the loaded Fira Code, a parity residue, not a load miss. HTTP-KEPT fires 3 times (candidate L256, 375, 378): real http links to www.wikidot.com user info and avatar pages, kept-http of class (ii), not the classifier's data-URI namespace false-fire. Why: pattern 7 (patterns/ at 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): every named stack face needs a load covering its glyph range. Verify: compare the @import lines and grep font-family in both files. Disposition: no flag; the SC-to-JP swap is complete in loads and stacks.

## 5. Header, sidebar and site furniture

What: the original's six ListPages modules (original L27, 96, 102, 117 in the preview machinery; L188 the wrapper; L373 the page2 form) reduce to two in the candidate (candidate L2, the restored wrapper; candidate L185, the page2 form). The preview machinery region (original L37-228, block B5) collapses to static instructions plus the fixed-value guide preview (candidate L185-245). The sidebar toggle include is repointed (block B62, section 2). Why: the wrapper was item 89's structural charge; ListPages variables cannot run inside a static guide page, so the port shows fixed sample values where the original computed them. Verify: `grep -c 'module ListPages'` on both files (6 against 2). Disposition: the wrapper restoration is re-derived in the Per-theme record; the machinery collapse is the port's recorded form, with F4 (section 2) as its open edge.

## 6. Text translation

What: TRANS-UNANCHORED fires in 64 blocks and TRANSLATION-ANCHORED in 29, carrying the guide prose, the demo texts and the stylesheet's comment translation (COMMENT-TEXT fires in 83 blocks, mostly inside the CSS); GLYPH-FORM fires in 4 blocks. In the guide preview the ListPages variables are replaced by fixed Japanese sample values (「ゲームガイド テーマ」, 「hoah2333制作」, 「？ 件の評価」; candidate L185-245). Why: T5 translation completeness, judged on rendered strings. Verify: sample the anchored blocks against diff.md. Disposition: no flag in this section; the one untranslated rendered string is the credit title field, flagged as F1 in section 1.

## 7. Links

What: the avatar image upgrades scheme (residue block B70: original L443 http to candidate L255 https, www.wikidot.com/avatar.php). Three http links to www.wikidot.com user pages are kept (section 4). The image-block exhibit is carried unchanged apart from its translated caption (block B8: original L239 to candidate L51; the image stays on scp-wiki.wdfiles.com). The Croquembouche design reference links an EN theme page (candidate L28) that resolves on scp-jp under the population's own posting of that theme (the R-fix-10 sci-fi precedent). Why: link targets must resolve on the wiki the reader is on (pattern 11, patterns/ at 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Verify: `grep -n 'http://' candidate.txt` returns the three kept links plus the F3 links. Disposition: F3 (section 2) is the only link flag.

## 8. Structure

What: the candidate opens with the tag gate [[iftags +テーマ]] (candidate L1) where the original opened with gate comments (block B1). The tail delivery stands outside the tag gate (candidate L2129-2136). EXHIBIT-RESTRUCTURE fires twice: block B3 is the inc-source gate fragment becoming static body content (part of F4's ground, section 2), and block B8 is the image-block exhibit carried with only its caption translated, which is not a restructure on adjudication against the exhibit content. Why: delivery outside the documentation gate keeps the stylesheet live on the theme page itself. Verify: read candidate L1 and L2129-2136. Disposition: no flag.

## 9. Formatting only

What: none standing alone. Whitespace-only and glyph-form-only changes ride inside the translation blocks counted in section 6. Why: a formatting-only change has no rendered effect by definition. Verify: the classifier's summary in classification.json (no WS-ONLY label fires for this theme). Disposition: none, on that ground.

## 10. Porter annotations

What: one porter annotation: the code-block head comment (candidate L425), 「steam-guide：原語版の CSS をまとめたもの」, riding block B102. The check was made explicitly across the candidate; no other annotation text was found. Why: annotations are the porter's voice and are marked as such, so a reader can tell them from the theme's own text. Verify: read candidate L425. Disposition: stands as the standard consolidation note.

## 11. Dispositions and exceptions

What: ledger register (c3) records P4 DISPOSITIONED (delivery class (ii)) and P9 DISPOSITIONED (ruling 2) for this theme. The T1 baseline (7 errors / 2 warns / 7 infos: hotlink x5, http x1, pseudo-ref x1) is dispositioned in register c1. The T2/T3 findings (page-overflow 371-372px at 320 on both engines; the runtime-hotlink site-theme chain; candidate host cdn.jsdelivr.net) are environment-layer standing findings; the sample credit-modal errors are dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment). T4/T5 record one display-affecting finding, which is item 89. Why: dispositions are the campaign's recorded judgements; this package re-derives the FIX5 one and cites the rest. Verify: the stamp lines above carry each record's citation. Disposition: as recorded; F1-F4 are new flags this package adds, none of them covered by an existing disposition.

## 12. Verification

Checks run for this package: sha256 of original.txt against review/sources.tsv (equal); cmp of candidate.txt against the canonical file (identical); classifier and build_review.py runs; credit author and source-host comparison against the original and sources.tsv; code-block census in every form (one block in the candidate); grep counts for ListPages modules (6 to 2), CN credit references (0 surviving) and Noto Sans SC (0 surviving); the include-parameter gate census (17 in the original, 0 in the candidate); the FIX5 re-derivation below; and a read of the cited upstream follow-up artifact (rev10 to rev10, no changes).

## Per-theme record: FIX5 re-derivation (item 89)

The ledger charges item 89 (class I) [GOSIGN2-LEDGER (e) item 89] with three defects: the opening ListPages wrapper deleted, raw %%content{0}%% literals fused into the body, and unrewritten CN credit includes. The supplement re-judges it FIXED by FIX5-STRUCTA, commit 8c0cd35 [GOSIGN2-LEDGER-SUPPLEMENT (a) item 89], with a supplement spot-check pass. Re-derived from this package's bytes: (1) candidate L2, the ListPages module with offset and range attributes, is byte-identical to original L188, the charged wrapper; (2) no scp-wiki-cn:credit reference survives anywhere in the candidate (grep count 0), and the demo region carries five %%content{0}%% lines naming :scp-jp:credit:* targets (candidate L15, 17, 23, 25, 27); the supplement counts four repointed credit includes, and under either count the closure holds, since the charge was the survival of CN targets; (3) no raw %%content{0}%% literal stands fused in body text outside the demo machinery. Closure CONFIRMED. The stamp is STALE only because the later usage sweep (b5cb724) touched the file after the verdict; that sweep renamed usage-example page references and did not touch the item-89 content.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/theme:steam-guide-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX15, landing `cdb1e6daa1f322aa4ec093f5f9967319e746274c`** ("pages: R-fix-15 flags repaired (steam-guide, sunside, supply)", 2026-11-17, R/review-scout/FIX-RFIX15.md §§1–4; +192/−6). Four items, all confined to this candidate:
  - **F1 — credit title field.** The タイトル field no longer duplicates the CN 原題: refreshed candidate L190 now reads `**タイトル:** ゲームガイド テーマ`, the body's own name (the L233 prose form ゲームガイドテーマ is the same name without the space). 原題 and the 元記事リンク label still quote the Chinese title, correctly: they cite the original.
  - **F2 — plain-slug self-delivery import.** The page2 import at L374 now names the candidate's own block 1, `https://scp-jp.wdfiles.com/local--code/theme%3Asteam-guide-jp/1` (pre-edit plain `theme:steam-guide/1`); only the page name changed, host and scheme untouched. The checker does not flag the address before or after (scp-jp.wdfiles.com is allowlisted); the defect was the page name.
  - **F3 — four plain-slug guide links.** L217, L218, L219 and L369 now name `theme:steam-guide-jp` in the same URL form; the `http` scheme is the standing class (ii) posting rewrite, not edited. The fourfold repetition is inherited from the original and is not itself a defect.
  - **F4 — include-parameter gates restored (17).** The original's entire 17-gate include interface (orig L1–186) is prepended byte-for-byte before `[[iftags +テーマ]]`, with only the candidate's established transformations: the two delivery @imports at L7/L14 name this candidate's own block 1 on the draft host (`https://sigma10-jp-test.wdfiles.com/local--code/theme%3Asteam-guide-jp/1`); inc-source's toggle-sidebar include is repointed `:scp-wiki:` → `:scp-jp:`; static gate prose is translated with the candidate's own renderings; all `{$...}` parameters, ListPages variables, rating computation and module forms are byte-identical to the original. The body's static guide preview is the port of the original's own demo, not an inlining of the gates, so no inlined content was carried back.
The per-theme record's item-89 note that the stamp is STALE "only because the later usage sweep (b5cb724)" is the as-built record; these repairs are a further, later reason. Checker (FIX-RFIX15 §8): error 6 / warn 2 / info 7 → 9 / 2 / 7 — +2 pseudo-ref (class iii, the restored gates' own draft-host imports) and +1 hotlink (class ii, the gate's black.png); class (i) 0 before and after.

## Change set

The port is the single file pages/theme:steam-guide-jp.txt; its git history names no companion candidate file. Sample pages are shared campaign records and sit outside this package.

## Appendix: residue and heuristic resolution

Residue blocks (2 of 108): B62 resolves to section 2 (the toggle-sidebar include repoint inside a %%content region, original L374 to candidate L186); B70 resolves to section 7 (the avatar image scheme upgrade, original L443 to candidate L255). Heuristic mass: 55 of the 108 blocks are heuristic, dominated by COMMENT-TEXT (83 label firings across blocks, the stylesheet's comment translation) and TRANS-UNANCHORED prose translation; both are expected translation mass, resolved here by shape, with no content change beyond language. The three HTTP-KEPT firings are adjudicated in section 4 as real kept http links, not the data-URI false-fire shape.

## License and attribution

- **Title:** 游戏指南 版式
- **Author:** hoah2333
- **Source:** https://scp-wiki-cn.wikidot.com/theme:steam-guide — revision 10
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
