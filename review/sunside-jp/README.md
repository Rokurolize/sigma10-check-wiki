# Review package: theme:sunside-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:sunside-jp — origin EN, population #142 [GOSIGN2-LEDGER (b) row 142]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now c5843f9da9e67d5bd4187323b919f3838b8d864a34a66711d379320fd8ff44af); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 0 infos (hotlink×3); standing classes dispositioned in register c1 [T1-ROWS row 162; GOSIGN2-LEDGER (b) row 142]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 502–510px@320/375 + 828–833px@768 (page) and 514–522px@320/375 + 828–833px@768 (sample); sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN20))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 142, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 142]
- FIX5 re-judgement: item 31 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: pattern-7 fix; probe evidence recorded that 'Noto Sans Mono CJK JP' returns HTTP 400 'Font family not found' on Google Fonts, so loadable Noto Sans JP was appended instead [GOSIGN2-LEDGER-SUPPLEMENT (a) item 31]
- Computed against: canonical commit 8868b5d164cbce9c07f6e76da11a5bdec2ec80d8; candidate file pages/theme:sunside-jp.txt sha256:c5843f9da9e67d5bd4187323b919f3838b8d864a34a66711d379320fd8ff44af; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| Item | State |
|---|---|
| Population row | 142 (EN block) |
| Class | R-fix: ledger (e) item 31 (class D), re-judged FIXED by FIX5-FONTSA [GOSIGN2-LEDGER-SUPPLEMENT (a) item 31] |
| Verdict stamp | PASS, and it carries: the stamp was computed against commit 8eacd6e, which is the candidate file's last change, and the candidate sha256 still matches. The only one of this batch whose verdict is not STALE |
| Package contents | original.txt, candidate.txt, classification.json, diff.md, this README |
| Open flags | F1 iA Writer font program substitution (section 4); F2 prose Sigma+ link to the EN component page (section 2). Flags are recorded, never edited into the candidate |

## Provenance

| Field | Value |
|---|---|
| Original | theme:sunside on scp-wiki, reference revision 17 |
| original.txt | Byte copy of the frozen mirror; sha256 38a13da3acb34a25fe5ad1a67a3fff76ea299aab37500d91c5fde61ea9c81e25, equal to the review/sources.tsv value; 67,725 bytes, 1,486 lines |
| Candidate | pages/theme:sunside-jp.txt; candidate.txt byte-identical to the canonical file (cmp-verified); sha256 4d20f7847d8fc847091958cee022e50b79596cfe18cc3812bbfd2e511a353123; 127,129 bytes, 2,679 lines |
| Upstream currency | The sources.tsv note for this theme is empty; no supersession claim is made or checked |

## Summary

An EN Sigma-Plus theme by EstrellaYoshte for the fictional city of Esterberg. The port inlines the full stylesheet into a head CSS module (the original delivered it from a tail import of its own code block), keeps the code block as the source exhibit, repoints Sigma-Plus delivery to the JP shared component, and, in the FIX5 repair, appends a loadable Japanese font to the mono stack (item 31, re-derived below). Two flags: the original's iA Writer font program (eight @font-face blocks) was dropped wholesale and both font variables re-pointed to other typefaces, with no record in the ledgers this package cites (F1); and one prose link names the EN Sigma+ component page although the JP counterpart is this file's own delivery component (F2).

## 0. Header and provenance

What: the diff is Tier 2: +1,459 / -267 lines, 1,726 changed lines in 19 blocks across 7 sections; review-stage comments account for 0 of the +1,459. The growth is structural: the stylesheet now stands twice, once as the delivered head module and once as the source exhibit. The candidate's git history is 3faf2e1 (Stage 2 EN20), 2d69b1c (rework2-p3), f931619 (FIX2-COLON), 8c62b7b (FIX4-IWA), 379eb44 (FIX4-MOPUP), 8eacd6e (FIX5-FONTSA). Why: provenance discipline; the PASS stamp's currency rests on 8eacd6e being the file's last change. Verify: `sha256sum` on both package files against sources.tsv and the stamp; `cmp` candidate.txt against the canonical file. Disposition: the stamp as built read PASS; the regenerated stamp now reads STALE against the post-build repairs (canonical commits cdb1e6d and 8868b5d, Post-package repairs), matching the Status table, with the record verdict standing.

## 1. Credit and attribution

What: the preview credit block (candidate L1253-1262) carries the full field set; the author field names EstrellaYoshte, matching the original's author (original L6 prose, "made by [[*user EstrellaYoshte]]"; the CSS banner in the code block). Ralliston, named in the original's prose as the person the theme was made for, is the dedicatee, not a co-author, and stays in the candidate's prose (candidate L1264). The source link's host is scp-wiki.wikidot.com, equal to the host recorded in sources.tsv. The license box swaps to the JP backend component with author=EstrellaYoshte (block B14: original L1448-1452 to candidate L2652-2656), and its five image entries are carried with names, authors and licenses preserved (Mount Ararat / Serouj Ourishian / CC BY-SA 4.0; Edinburgh Old Town / Depthcharge101 / CC BY-SA 3.0; Tuggeranong / Nick-D / CC BY-SA 4.0; Poznan Centrum / Kamilbelieve / Public Domain; the Esterberg flag / Jerden / CC BY-SA 3.0 with the EstrellaYoshte edit note). Why: TASL completeness (TASL-FIELDS and LICENSE-BOX fire; T7-CREDIT-CSS rides block B13). Verify: read candidate L1253-1262 and L2652-2679 against the original's tail. Disposition: no flag; attribution is complete on every field checked.

## 2. Includes and components

What: delivery includes stand at candidate L1243-1249: the Sigma-Plus JP shared component, the toggle-sidebar repoint, and the interwiki-style frame (SIGMA-PLUS-JP fires in 3 blocks; INCLUDE-REPOINT once). The original's tail carried the EN sigma-plus include, the EN toggle-sidebar and a module importing its own code block (original L1476-1486). Why: pattern 11 (patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): components with a JP counterpart are delivered from the JP component. Verify: read candidate L1243-1249 against original L1476-1486. Disposition: one defect. F2: the prose at candidate L1272 links [[[https://scp-wiki.wikidot.com/component:sigma-plus|Sigma+]]], the EN component page as an absolute URL in the very sentence that states delivery runs through component:sigma-plus-jp; the JP counterpart exists and is this file's own delivery include (candidate L1243), so a JP reader following the documentation leaves the wiki for a page whose JP twin the file itself uses (pattern-11 shape; the share-future precedent in batch R-fix-12). Not edited; flagged. Two neighbouring links are recorded, not flagged: the absolute EN link to the theme's subject article (candidate L1264) names a page with no JP counterpart and resolves where it points, and the license box's relative source link is kept from the original.

## 3. Delivery and code loading

What: DELIVERY-MOVE fires in 12 of the 19 blocks. The original's stylesheet stands in one code block (original L164-1445, 1,281 lines) and is delivered by a tail module importing the page's own /1 (original L1478-1481). The candidate inlines the stylesheet as a head CSS module (candidate L1-1241) and keeps the code block as the source exhibit (candidate L1424-2649, 1,225 lines); the interwiki-style frame at priority 1 names the draft-host address local--code/theme%3Asunside-jp/1 (candidate L1246-1249), which is the exhibit block, the file's only code block, while the live delivery is the inline module. The head comment (candidate L21) states the module code is identical to the source display, and the FIX5 repair indeed edited both copies (see the Per-theme record). SELF-DELIVERY fires twice, DRAFT-HOST once. Why: the delivered bytes and the exhibit bytes must agree, or the review surface and the live surface diverge. Verify: compare a rule present in both copies (the --mono-font variable stands at candidate L81 and L1489 with identical values). Disposition: no flag; the two-copy form is recorded here as the delivery topology, with the frame naming the exhibit block as the population's standard own-code form.

## 4. Fonts and assets

What: the original loads Sora and Public Sans from api.fonts.coollabs.io (original L180-181) and defines eight @font-face blocks (original L183-239) loading iA Writer Mono and iA Writer Duo from a third-party webfont archive on cdn.jsdelivr.net; its variables name them (original L285: --UI-font 'iA Writer Duo'; original L286: --mono-font 'iA Writer Mono') and its prose announces them (original L158-160). The candidate loads Sora, Public Sans and JetBrains Mono from Google Fonts (candidate L2-4) plus Noto Sans JP (candidate L11, the FIX5 repair); its variables name Public Sans for UI (candidate L80) and JetBrains Mono for mono (candidate L81); it contains zero @font-face blocks and zero iA Writer strings, and its prose announcements are rewritten to match (candidate L1414-1418). FONT-IMPORT and JPFONT-LOAD each fire once. HTTP-KEPT fires 4 times (candidate L150-152, 573): all four are data:image/svg+xml URLs whose xmlns is the W3C namespace string, the classifier's known false-fire, not kept http links. Why: pattern 7 (patterns/ at 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa): named faces need loads, and loads the original carries are content. Verify: `grep -c '@font-face'` on both files (8 against 0); read the variable lines cited. Disposition: one defect and two records. F1: the iA Writer program's removal is a wholesale typeface substitution (both variables re-pointed, the prose rewritten to match), internally consistent but charged in no record this package cites: the ledger's font item for this theme (item 31) covers only the pattern-7 JP-glyph miss, and the T-runs record no substitution finding. A licensing ground is plausible, since the original loads a commercial typeface from a third-party archive, but the substitution changes the theme's rendered typography, the theme's signature UI face included, so it is flagged with this evidence for the coordinator's adjudication rather than narrated as a supplement. Record 1: the mono stack still names 'Noto Sans Mono CJK JP' (candidate L81, L1489), the face the FIX5 probe itself showed Google Fonts cannot serve (HTTP 400); it sits ahead of the loadable 'Noto Sans JP' the fix appended, so Japanese glyphs still resolve, and the stack's exact shape is the fix's own record, not a new flag. Record 2: Nanum Gothic is named in stacks but loaded by no import in either file (original L283-284 names it equally), an inherited parity residue.

## 5. Header, sidebar and site furniture

What: HEADERVAR fires in 3 blocks. A Sigma-Plus override layer at the head of the module (candidate L15-19) sets --header-title to 「SCP財団」 and --header-subtitle to 「確保 - 収容 - 保護」 and points --sp_header-logo at the original's own EN-host asset (esterberg-sun.png on scp-wiki.wdfiles.com, a kept class (ii) asset). The theme's own root variables translate the city name and its slogan (candidate L82-83: 「エスターバーグ」 and 「新たなパラダイムを紡ぐ」, against original L287-288: "Esterberg" and "Weaving New Paradigms"); the slogan is a prose sentence and translates under the standing boundary, while the city name is rendered in katakana as the body's established form. The original's head bare Rate module (original L2-4) has no candidate counterpart: the candidate's credit block is the rate-bearing preview form, so a separate bare Rate beside it would double-render the widget (the population census ground for this deletion shape). Why: header variables are rendered strings; the Rate deletion ground is the duplicate-widget failure it prevents. Verify: grep the --header-title loci in both files; `grep -ci 'module rate'` returns 1 for the original, 0 for the candidate. Disposition: no flag; the Rate deletion is recorded here with its ground because the classifier left it unlabelled inside block B1.

## 6. Text translation

What: TRANS-UNANCHORED fires in 9 blocks, TRANSLATION-ANCHORED in 1, COMMENT-TEXT in 3: the documentation body, the license entries and the CSS comments are translated, and the font announcement prose is rewritten to name the substituted faces (section 4). Why: T5 translation completeness on rendered strings. Verify: sample blocks B14-B18 (license entries) against diff.md. Disposition: no flag in this section; the substitution itself is F1 in section 4.

## 7. Links

What: the prose Sigma+ link (candidate L1272) is F2 in section 2. The subject-article link (candidate L1264) is an absolute EN URL kept for a page with no JP counterpart; the license box's source link stays relative as in the original; the header logo asset stays on the EN files host (section 5). Why: pattern 11 (patterns/ at 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa) governs counterpart repointing; pages without a counterpart keep a resolving target. Verify: read candidate L1264-1272. Disposition: F2 only, cross-referenced.

## 8. Structure

What: the candidate inverts the original's order: delivery module, includes and frame first (candidate L1-1249), then the tag gate [[iftags +テーマ]] opens at candidate L1251 with the documentation body inside it; the original ran the body first under its tag gate and delivered from the tail. Block B13 (original L1445 to candidate L1240-2648) carries the exhibit and body relocation; its RESTORATION label is the classifier's name for a large re-inserted region, not a ledger restoration, since this theme's ledger item was the font miss. Block B19 shows the original's tail delivery as removed at the tail because it moved to the head zone. IFTAGS fires twice. Why: delivery outside the documentation gate keeps the stylesheet live on the theme page itself. Verify: read candidate L1243-1253 and the original's tail. Disposition: no flag.

## 9. Formatting only

What: WS-ONLY fires in 2 blocks (B11, B12): trailing-whitespace-only line changes inside the moved stylesheet, at original L1063 to candidate L858 and original L1385 to candidate L1180. Why: whitespace inside a delivered stylesheet has no rendered effect. Verify: the two blocks in classification.json. Disposition: none, on that ground.

## 10. Porter annotations

What: three porter comment blocks stand at the head of the delivered module: the FIX5 Japanese-font note with its import (candidate L6-11), the Sigma-Plus override layer's heading comment (candidate L13-14), and the module identity note stating the module code equals the source display (candidate L21). The check was made explicitly; the exhibit's own comments are the original's. Why: annotations are the porter's voice and are marked as such. Verify: read candidate L1-21. Disposition: the three stand as the port's working notes; the FIX5 note is part of item 31's repair record.

## 11. Dispositions and exceptions

What: ledger register (c3) records P6 FIXED for this theme (frame waves, checker-verified) and P7 carried to the (e) register as item 31. The T1 baseline (3 errors / 2 warns / 0 infos, hotlink x3) is dispositioned in register c1. The T2/T3 overflow findings (502-510px at 320/375 and 828-833px at 768 on the page; 514-522px and 828-833px on the sample) are standing render findings; the sample credit-modal errors are dispositioned preview-form (GOSIGN-TESTS T2 amendment). T4/T5 record 3 display-affecting findings, of which the pattern-7 miss is the one that reached the (e) register as item 31. Why: dispositions are the campaign's recorded judgements; this package re-derives the FIX5 one and cites the rest. Verify: the stamp lines above carry each citation. Disposition: as recorded; F1 and F2 are new flags this package adds, covered by no existing disposition.

## 12. Verification

Checks run for this package: sha256 of original.txt against review/sources.tsv (equal); cmp of candidate.txt against the canonical file (identical); classifier and build_review.py runs; credit author, dedicatee and source-host comparison; license entry census (five entries, authors and licenses preserved); code-block census in every form (one block in each file); @font-face census (8 against 0) and font load/stack comparison in both copies of the CSS; the bare Rate check (present in the original, absent in the candidate, ground recorded in section 5); HTTP-KEPT adjudication (four data-URI namespace false-fires); and the FIX5 re-derivation below, including the commit's own diff.

## Per-theme record: FIX5 re-derivation (item 31)

The ledger charges item 31 (class D) [GOSIGN2-LEDGER (e) item 31] with a pattern-7 font miss: the stacks named Japanese-capable faces that no load in the file served, so Japanese glyphs fell back to the OS default. The supplement re-judges it FIXED by FIX5-FONTSA, commit 8eacd6e [GOSIGN2-LEDGER-SUPPLEMENT (a) item 31], recording probe evidence that 'Noto Sans Mono CJK JP' returns HTTP 400 'Font family not found' on Google Fonts, so the loadable Noto Sans JP was appended instead. Re-derived from the commit and the current bytes: `git show 8eacd6e` makes exactly three edits to this file, (1) the Japanese explanatory comment and the Noto Sans JP @import at the head module, now candidate L6-11; (2) the --mono-font variable in the delivered module copy gains the 'Noto Sans JP' suffix, now candidate L81; (3) the same suffix in the exhibit copy, now candidate L1489. All three stand in the current candidate bytes, in both CSS copies. Closure CONFIRMED. Because the stamp was computed against 8eacd6e itself and the file has not changed since, the PASS verdict carries to the bytes in this package.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The two repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/theme:sunside-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX15 F2, landing `cdb1e6daa1f322aa4ec093f5f9967319e746274c`** ("pages: R-fix-15 flags repaired …", 2026-11-17, R/review-scout/FIX-RFIX15.md §5; +1/−1): the prose Sigma+ link at refreshed L1329 now reads `[[[component:sigma-plus-jp|Sigma+]]]` (pre-edit `[[[https://scp-wiki.wikidot.com/component:sigma-plus|Sigma+]]]`), label unchanged — the population's repaired form for this exact item (share-future-community-jp L41, tfnac-jp L22). The same sentence already stated delivery via component:sigma-plus-jp, the file's own delivery include. The one new `link-target-missing` warning naming the not-yet-posted candidate is the AGENTS.md posting-order class, recorded, not fixed. Checker: error 3 / warn 1 / info 0 → 3 / 2 / 0.
- **FIX-SUNSIDEFONT, landing `8868b5d164cbce9c07f6e76da11a5bdec2ec80d8`** ("pages: sunside iA Writer font program restored", 2026-11-17, R/review-scout/FIX-SUNSIDEFONT.md; +122/−7), executing the RESTORE recommendation of FIX-RFIX15 §7:
  - The eight `@font-face` blocks return in both delivered copies — the head `[[module CSS]]` (L12–69) and the source-exhibit FONTS section — byte-identical to the original's L183–239 (the exact block text now occurs twice, verified in the report). No exhibit @imports were added: the exhibit has none by the port's structure.
  - Both font variables name the iA faces as primaries again at L137–138 (`--UI-font: 'iA Writer Duo', 'Noto Sans JP', …`, `--mono-font: 'iA Writer Mono', 'Noto Sans Mono CJK JP', …`), keeping the port's JP fallbacks behind them.
  - The prose announcements at L1475/L1477 name `iA Writer Duo` / `iA Writer Mono` again, in the candidate's own translated sentence forms; the Sora and Public Sans announcements stand unchanged.
  - The substitute-only Google Fonts JetBrains Mono @import was removed (zero occurrences of JetBrains Mono remain); Sora, Public Sans and Noto Sans JP loads stay in their original roles.
  - Supply channel: the original's own SYwaves archive URLs, all eight probed HTTP 200 / font/woff2 and byte-identical to the official iaolo/iA-Fonts SIL OFL 1.1 release (SHA-256 table in FIX-SUNSIDEFONT §2) — a lawful channel twice over, not the clock-tower Colus posture. No annotation edit was needed (the JP-font comment remains true).
Checker (FIX-SUNSIDEFONT §3): error 3 / warn 2 / info 0 → 19 / 2 / 0, the delta exactly +16 hotlinks (8 URLs × 2 copies), all class (ii) "outside hosts that serve today"; class (i) 0 before and after.

The per-theme item-31 note that the stamp was computed against 8eacd6e and "the file has not changed since, the PASS verdict carries to the bytes" is the as-built record; the stamp now reads STALE against these two repairs.

## Change set

The port is the single file pages/theme:sunside-jp.txt; its git history names no companion candidate file. Sample pages are shared campaign records and sit outside this package.

## Appendix: residue and heuristic resolution

Residue blocks: none (0 of 19). Heuristic blocks: 3 of 19, namely B15-B17, the license-box entries at original L1454-1467 to candidate L2658-2671, which the classifier leaves unanchored; adjudicated as anchored license-entry translations in substance, since each entry's name, author and license carry over and only the field labels and notes are localized (section 1). Block B13's RESTORATION label is adjudicated in section 8. The four HTTP-KEPT firings are adjudicated in section 4 as the data-URI namespace false-fire.

## License and attribution

- **Title:** Sunside Theme
- **Author:** EstrellaYoshte
- **Source:** https://scp-wiki.wikidot.com/theme:sunside — revision 17
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
