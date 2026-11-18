# Review package — theme:oceanbound-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:oceanbound-jp — origin EN, population #114 [GOSIGN2-LEDGER (b) row 114]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now eead4f0fc8a9c38bacec7673c1ab843d868e8571c6c64823fd2505313c04d815); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 0 warns / 1 info (hotlink×4, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 114; GOSIGN2-LEDGER (b) row 114]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 340px@320 on page and sample; runtime-hotlink site-theme chain + scp-wiki.wikidot.com; sample credit-modal (preview-form); T3 clean on both pages. [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-C (EN14))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 114, source LOCALIZE-S2-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 114]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 114]
- Computed against: canonical commit d554544b88a5b14936b0f0e67c10361c79179ad3; candidate file pages/theme:oceanbound-jp.txt sha256:eead4f0fc8a9c38bacec7673c1ab843d868e8571c6c64823fd2505313c04d815; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/oceanbound-jp/candidate.txt (sha256 e902a842323bb9073e6e372a050bafae68d072f0bd3338112f87d46dc048f9b6)
Original: theme:oceanbound — scp-wiki, revision 62 (sha256 7c34140ce3b76ad8d69495d7ffda8f93708d71cca876601dc0c3b74c464ca039)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.
- Provenance route: derived from the original at the reference revision. The original is theme:oceanbound on scp-wiki at revision 62 (sources.tsv row: kind standard, no production JP counterpart). The candidate is a fresh campaign translation made by the Stage 2 lane LOCALIZE-S2-B and integrated in commit 49c7627 (Stage 2 EN14); its credit block records 翻訳年 2026 and, after the FIX-CREDIT-D normalization, 翻訳責任者 AI (ruling 3: campaign translations are credited to AI). Three later wave edits touch the file: FIX-CREDIT-D (1869877), FIX4-LICENSE (c2a8bee), and the population usage-example sweep (b5cb724). The sweep postdates the FIX5 verdict head, so the generated stamp above reads STALE; the verdict lines under it describe the pre-sweep file, and the only post-verdict change is the sweep's two usage lines (section 2 and the Multi-wave provenance section).

## Status

| Check | Verdict | Source |
|---|---|---|
| Overall | STALE (stamp) — candidate changed after the verdict; verdicts below describe the pre-change file | GOSIGN2-LEDGER (b) row 114, stamp regenerated at b5cb724 |
| T1 source check | FINDINGS (classified) — exit 1, 6 errors / 0 warns / 1 info (hotlink×4, pseudo-ref×2) | T1-ROWS row 114 |
| T2/T3 render | FINDINGS — page-overflow 340px@320 on page and sample; runtime-hotlink site-theme chain + scp-wiki.wikidot.com; sample credit-modal (preview-form); T3 clean on both pages | RENDER-ROWS-2 (RENDER-S2-C (EN14)) |
| T4 localize patterns | FINDINGS — 1 display-affecting finding (P5) | LOCALIZE-ROWS row 114 (LOCALIZE-S2-B) |
| T5 translation text | FINDINGS — judged jointly with T4 by the source report | LOCALIZE-ROWS row 114 |
| FIX5 re-judgement | none — no OPEN items at the ledger determination | GOSIGN2-LEDGER (b) row 114 |

## Provenance

| Side | Identity |
|---|---|
| Original | theme:oceanbound, scp-wiki, revision 62; mirror class COPY (LOCALIZE-S2-B lane cache); sha256 7c34140ce3b76ad8d69495d7ffda8f93708d71cca876601dc0c3b74c464ca039 (review/sources.tsv) |
| Candidate | pages/theme:oceanbound-jp.txt in this repo; sha256 e902a842323bb9073e6e372a050bafae68d072f0bd3338112f87d46dc048f9b6 (stamp, computed against canonical commit b5cb724) |
| Reference revision | 62 (the credit block's 初訳時参照リビジョン agrees) |

## Summary

Oceanbound is a two-stylesheet theme: a main CSS payload and a dark "blood" variant payload, each delivered from its own [[code]] block through a [[module CSS]] import and an interwiki-style frame, the variant gated by the include parameter {$blood}. The port keeps that topology exactly, repoints both deliveries to the candidate's own code addresses on the check-wiki host, localizes the tag gate, the prose, the exhibit body, and the license entries, and adds the campaign credit block at the head. Four wave edits shape the file beyond the base port: the creation itself (LOCALIZE-S2-B), the FIX-CREDIT-D translator normalization, FIX4-LICENSE (the KB-04 font-URL grammar repair and the KB-63 license-box restoration), and the usage-example sweep. One defect is flagged: the license box drops one of the original's six attribution entries (section 8). One structural replacement is recorded without a defect charge: the original's head furniture (a hidden preload image-block and a bare Rate module) is replaced by the credit block (section 8). The one display-affecting localize finding, P5 (EN-storage assets kept), is dispositioned class (ii) in the ledger.

## Classification

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 4 |
| DRAFT-HOST | 4 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 7 |
| FONT-IMPORT | 2 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 5 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 4 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 37 |
| TRANSLATION-ANCHORED | 18 |
| WS-ONLY | 77 |

Across 149 classified blocks: 109 specific (73.2%), 38 heuristic (25.5%), 2 residue (1.3%), 0 skipped. The heuristic mass is the exhibit-body translation queue (TRANS-UNANCHORED) plus two CSS-BODY blocks adjudicated in sections 4 and 8; the WS-ONLY mass is the original's space-only padding lines inside the CSS, normalized to empty lines. The residue blocks are resolved in the Appendix.

## 1. Credit and attribution

**What.** The candidate opens its gated body with the campaign credit block (candidate L22–31): [[include :scp-jp:credit:start-preview]], the fields タイトル Oceanbound Theme, 翻訳責任者 AI, 翻訳年 2026, 原題 Oceanbound Theme, 著作権者 EstrellaYoshte（DrBleep のために）, 作成年 2022, 初訳時参照リビジョン 62, 元記事リンク to https://scp-wiki.wikidot.com/theme:oceanbound, and [[include :scp-jp:credit:end-preview]]. The classifier spans are TASL-FIELDS, CREDIT-PREVIEW, and CREDIT-PROSE inside block B10. The license box at the tail (candidate L1604–1632) is covered in section 8.

**Why.** The TASL record (ruling 3) is what makes a campaign translation attributable: title, author, source, license, and the reference revision a reviewer can diff against. The author field follows the original's own attribution: the original's prose states the theme was "made by [[*user EstrellaYoshte]] for [[*user DrBleep]]" (original L31), and the candidate's 著作権者 carries both names in that relation. The source link names scp-wiki.wikidot.com, the host recorded for the original in review/sources.tsv; no host discrepancy exists to probe. FIX-CREDIT-D (1869877) changed exactly one line in this file, 翻訳責任者 SCP-JP → AI, the population-wide ruling-3 normalization.

**Verify.** Read candidate L22–31 against original L31 and the sources.tsv row (host scp-wiki, revision 62). `git show 1869877 -- pages/theme:oceanbound-jp.txt` shows the single-line translator change.

**Disposition.** Ledger verdict PASS, row 114 [GOSIGN2-LEDGER (b)]; the credit content is not charged by any register.

## 2. Includes and components

**What.** Five INCLUDE-REPOINT spans and one block each for IFTAGS, COMPONENT-SWAP, and ESCAPED-INCLUDE. The include repoints: toggle-sidebar (candidate L1, block B1), the two interwiki-style frames (candidate L5–8 and L14–17, blocks B3/B7), and the license-box-end at the tail (B149). The tag gate localizes: original L20 [[iftags +theme]] → candidate L20 [[iftags +テーマ]] (B9, IFTAGS). The usage exhibits (candidate L37 and L41, block B15) read @@[[include :scp-jp:theme:oceanbound-jp]]@@ and the blood=-- variant; the COMPONENT-SWAP primary label on B15 is the classifier's name for the :scp-wiki: → :scp-jp: prefix change on those lines, and ESCAPED-INCLUDE records their @@...@@ exhibit form.

**Why.** Tag localization (P2, KB-08) is what makes the gated body render in the JP environment, where the theme tag is テーマ. The usage exhibits are the theme's own instructions to adopters; after the population sweep (b5cb724) they name the -jp posting name, which is the name this candidate will be posted under, so the exhibit resolves at posting instead of pointing at the EN page or at a not-yet-posted plain form. The sweep changed exactly these two lines and nothing else in the file, which is also the whole content of the stamp's STALE state.

**Verify.** `grep -n "iftags" candidate.txt` shows the single gate at L20 with the JP tag. `git show b5cb724 -- pages/theme:oceanbound-jp.txt` shows the two usage lines changing :scp-jp:theme:oceanbound → :scp-jp:theme:oceanbound-jp (and the blood=-- variant). No plain-form or EN-form usage reference remains: `grep -n "theme:oceanbound\]\]\|theme:oceanbound " candidate.txt` returns only the credit source link and CSS file paths, no include.

**Disposition.** The tag gate and repoints are part of the ledger PASS, row 114. The sweep is a coordinator landing recorded in the campaign record, post-verdict by design (the stamp marks the file STALE rather than carrying the PASS onto changed bytes).

## 3. Delivery and code loading

**What.** Both sides deliver two stylesheets the same way. Candidate L2–3: a [[module CSS]] importing https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aoceanbound-jp/1; candidate L5–8: an interwiki-style frame with priority=1 naming the same /1 address. The blood variant repeats the pair for /2 at priority=2 (candidate L11–17), gated by the parameter comment pair (candidate L10 [!-- {$blood} and L18 [!-- --]). The original names theme%3Aoceanbound/1 and /2 on scp-wiki.wdfiles.com with the same priorities and the same gate. The classifier spans are DELIVERY-HOST, DRAFT-HOST, and SELF-DELIVERY on blocks B2/B4/B6/B8.

**Why.** The addresses name the candidate's own code blocks in document order: the first [[code]] block (the main payload, candidate L199–1216) is /1 and the second (the blood variant, candidate L1218–1601) is /2, so each load pulls the payload written for it. The FIX-CODEADDR audit (R/review-scout/FIX-CODEADDR.md) does not list this theme among its mismatches or unresolved references, and the census here agrees with it. Keeping the original's priority values (1 for the main sheet, 2 for the variant) preserves the cascade order the author designed: the variant overrides the base only where it restates a rule.

**Verify.** List the loads: `grep -n "local--code" candidate.txt` returns L3, L7, L12, L16, two addresses, each named twice (import and frame). Count the code blocks: `grep -n "\[\[code" candidate.txt` returns the two payload blocks in the same order. The gate pair is candidate L10 and L18.

**Disposition.** Ledger PASS, row 114; the DRAFT-HOST form (the check-wiki host in the delivered address) is class (iii), the standing draft-stage form, resolved when the page is posted to production.

## 4. Fonts and assets

**What.** Two FONT-IMPORT blocks and the kept-asset lines. Code block 1 (candidate L209–211) imports Space Grotesk, Space Mono, and Grenze Gotisch from fonts.googleapis.com; code block 2 (candidate L1219) imports Inknut Antiqua from the same host. The original imports the same four families from fonts.bunny.net with lowercase hyphenated family parameters (original L207–209 and L1216). The font stacks in :root (candidate L213–216, block B62) add JP fallbacks to the original's stacks: 'Noto Serif JP' in --header-font, 'Noto Sans JP' in --UI-font and --body-font, 'Noto Sans Mono CJK JP' in --mono-font. Kept EN asset URLs: --header-image (candidate L223, orkn.jpg on scp-wiki.wdfiles.com), --title-image (candidate L224, orcadia.png on scp-wiki.wikidot.com), the blood variant's --header-image (candidate L1249, mountainous.jpg), and the Mither.jpeg image-block in the exhibit body (candidate L45, block B16).

**Why.** Two separate changes are stacked in the import lines, and the record only charges one of them. At port creation the delivery host moved from fonts.bunny.net to fonts.googleapis.com; no register charges the move itself. But the move broke the loads: the lowercase hyphenated family form (family=space-grotesk) is bunny.net's grammar, and the same string on googleapis returns 400, so all four families failed to load. FIX4-LICENSE (c2a8bee) repaired the grammar in place (family=Space+Grotesk, Space+Mono, Grenze+Gotisch, Inknut+Antiqua), and the ledger records the fix as live-probed 400→200 (KB-04; ledger (c3) pattern 7, FIXED for oceanbound via FIX4-LICENSE). The stack changes in B62 are the P7 font-stack localization: every family the stacks name first is loaded by the imports above, and the added fallbacks are the JP system fonts the campaign standard uses, so no named-not-loaded family arises. The kept asset URLs are the P5 finding (LOCALIZE-ROWS row 114: EN-storage assets including a cross-article image hotlink, the Mither.jpeg file hosted under scp-6700), dispositioned class (ii): the files are the original's own storage and are re-hosted or repointed at posting.

**Verify.** `git show c2a8bee -- pages/theme:oceanbound-jp.txt` shows the four import lines changing only the family parameter form, host unchanged. Compare candidate L209–211 and L1219 against original L207–209 and L1216 for the host move. The stack additions are candidate L213–216 against original L213–216.

**Disposition.** Pattern 7 FIXED (FIX4-LICENSE, KB-04) and P5 DISPOSITIONED (class (ii) / KB-58) in the ledger (c3) register for this theme; ledger PASS, row 114. The uncharged host move is recorded here and in the Per-theme record; it is not a defect, because the repaired googleapis loads probe 200 and no register requires bunny.net for this theme.

## 5. Header, sidebar, site furniture

**What.** One HEADERVAR block (B142): the blood variant's --header-title, original L1243 "Blood of Orcadia" → candidate L1246 "オルカディアの血". The main payload defines no --header-title on either side. The toggle-sidebar include is covered in section 2. The render record's furniture findings (page-overflow 340px@320 on both pages) are in section 11.

**Why.** The header title is the theme's visible title surface (KB-57). Ruling 2 puts header and title language outside migration correctness, so either language would stand; here the port translates the variant's title, and the translation is the author's own phrase (the canon name Orcadia rendered in katakana), not a substitution. No disposition is needed in either direction.

**Verify.** `grep -n "header-title" candidate.txt original.txt` returns one definition per side, candidate L1246 against original L1243, plus the shared content: var(--header-title) consumption line.

**Disposition.** Ledger PASS, row 114; ruling 2 covers the title-language question.

## 6. Text translation

**What.** TRANSLATION-ANCHORED spans in 18 blocks and TRANS-UNANCHORED spans in 37 blocks: the introductory prose (candidate L33–35), the usage instructions, the full demonstration body (headings, collapsible, tabview, tables, blockquotes, the code exhibits' surrounding text), and the license entries at the tail (blocks B145–B149). The Orcadia hub link changes form with its sentence: the original's triple-bracket page link becomes a bracket URL link to https://scp-wiki.wikidot.com/seas-of-orcadia-hub in the candidate (candidate L33), the standing form for linking the EN hub from a JP page.

**Why.** Reader-visible text localizes (P10, KB-18); the anchored pairs confirm the one-to-one mapping where anchors survive, and the unanchored mass is the same translation in restructured lines, resolved pair by pair against the mirror for this package. The demonstration body is retained entire: the exhibit census in section 8 confirms no exhibit was dropped in translation.

**Verify.** Read the pairs in diff.md from candidate L33 onward; the license-entry pairs are candidate L1606–1631 against original L1602–1631 (with the one-entry shortfall flagged in section 8).

**Disposition.** T5 FINDINGS judged jointly with T4 (LOCALIZE-ROWS row 114); the findings are the P5 item in section 4, not translation defects. Ledger PASS, row 114.

## 7. Links

**What.** No link-specific signature fired. The candidate's outbound links are the credit source link (section 1), the Orcadia hub link (section 6), the Wikimedia Commons source links inside the license entries (unchanged on both sides), and the Flickr source link in the Mither.jpeg entry (unchanged). The kept EN asset URLs are file loads, covered in sections 4 and 11, not prose links.

**Why.** No link repointing was needed beyond the include and delivery changes: the license entries' source links name the canonical Commons and Flickr pages on both sides, and the hub link names the EN hub the theme was written for.

**Verify.** `grep -n "commons.wikimedia.org\|flickr.com" candidate.txt original.txt` returns the same link set on both sides.

**Disposition.** Ledger PASS, row 114; no link finding is recorded for this theme in any register.

## 8. Structure

**What.** Seven EXHIBIT-RESTRUCTURE blocks and two CSS-BODY blocks, adjudicated one by one. B1, B3, B7 (head includes) and B16 (the Mither.jpeg image-block): mere repoints inside exhibit or furniture regions; the EXHIBIT-RESTRUCTURE primary is the standing false fire, and the exhibit census below confirms nothing was dropped. B15: the usage exhibits, repointed and sweep-renamed (section 2). B10 (original L21–29 → candidate L21–31): the original's head furniture, a display:none preload image-block for orcadia.png and a right-aligned bare [[module rate]], is replaced by the credit block; neither element appears anywhere in the candidate (grep confirms no [[module rate]] and no second image-block). B144 and B149 (tail): the license box. The original carries it as [[include :scp-wiki:component:license-box-theme]] (original L1601), six attribution entries (original L1602–1631), and license-box-end. The candidate carries [[include :scp-jp:component:license-box-backend]] (candidate L1604), five translated entries (candidate L1606–1631), and license-box-end (candidate L1632). B62 and B63 (CSS-BODY) are adjudicated in section 4 (P7 stacks; kept asset variables).

**Why.** The license box is the theme's attribution record for its images (KB-63 covers license boxes dropped by ports). The port dropped the box furniture; FIX4-LICENSE (c2a8bee) restored the backend and end includes around the surviving entries, and the commit subject records the restoration as this theme's share of that wave. The restoration is, however, one entry short against the mirror: the original's sixth entry, "Amazing Sunset of Pheriche" by Babin Dulal, CC BY-SA 4.0, source Wikimedia Commons (original L1627–1631), has no counterpart in the candidate. The entry never existed in the canonical file's history (`git log -S Pheriche` is empty), so it was dropped at port creation and the FIX4-LICENSE restoration did not bring it back. This is flagged as a defect below; the candidate is not edited by this package. For B10: the preload div's only payload (orcadia.png) still loads as the --title-image asset (candidate L224), and the theme page's own Rate module is the furniture the campaign credit block replaces at the head of a ported theme page; no register charges either element, and the render record's T3 is clean on both pages. The replacement is recorded here so the census is complete, without a defect charge.

**Verify.** Entry census: `grep -c "ファイル名:" candidate.txt` returns 5; `grep -c "Filename:" original.txt` returns 6; the missing entry is original L1627–1631. `grep -n "module rate" candidate.txt` returns nothing. `git show c2a8bee -- pages/theme:oceanbound-jp.txt` shows the wave adding the two license-box includes and no entry text.

**Disposition.** Ledger PASS, row 114; the license-box restoration is recorded under KB-63 in the FIX4-LICENSE wave. **Defect flag (this package): one license entry dropped** — "Amazing Sunset of Pheriche" (original L1627–1631) absent from the candidate's license box (candidate L1604–1632 carries five entries against the original's six). The FIX4-LICENSE restoration is incomplete by this one entry.

## 9. Formatting only

**What.** 77 WS-ONLY blocks, spread through both CSS payloads. The original pads its CSS with lines containing a single space (visible throughout original L210–1210); the candidate's corresponding lines are empty. No re-indentation pairs were found (0 blocks pair up after leading-whitespace normalization).

**Why.** Whitespace-only lines inside a stylesheet have no rendering effect on either side; the normalization is the port's text hygiene, and the count is large only because the padding habit is consistent across a 1,000-line stylesheet.

**Verify.** Any WS-ONLY block in diff.md shows a one-space line against an empty line with identical neighbors; the classifier's count is in classification.json.

**Disposition.** Formatting only; no register charges it. Ledger PASS, row 114.

## 10. Porter annotations

**What.** One ANNOTATION span (block B5): the gate opener line, original L10 [!-- {$blood}] → candidate L10 [!-- {$blood}. No other comment in the candidate lacks a counterpart in the original; the file's only comments are the gate pair (candidate L10, L18) and the CSS banner and section comments inside the payloads, which are the original's own, translated or retained with their rules.

**Why.** The ANNOTATION primary on B5 is a false fire of the same family as night-rush's banner residue: the changed line is the original's delivery mechanism (the {$blood} parameter gate, section 3), not a porter's note. The one-character difference (the candidate drops the stray closing bracket on the opener line) brings the opener to the form the gate uses across the population; the mechanism, the gated content, and the closer are unchanged, and the render record raises no variant-delivery finding. There are no translator notes, editor lines, or signed comments added by the port.

**Verify.** `grep -n "\[!--" candidate.txt original.txt` returns the gate pair on both sides and nothing else outside CSS comments. The payload banner (candidate L199–207 region) names the original's authors and predecessor themes, with no porter signature added.

**Disposition.** No porter annotations exist in this candidate. Ledger PASS, row 114.

## 11. Dispositions and exceptions

**What.** The dispositioned items for this theme: (1) P5, the kept EN-storage assets (section 4), DISPOSITIONED in the ledger (c3) register as class (ii) / KB-58 — the one display-affecting localize finding (LOCALIZE-ROWS row 114, items a,b: EN-storage assets including the cross-article Mither.jpeg hotlink). (2) The HTTP-KEPT census (7 occurrences): the deco-mask and header-logo-mask data URIs carry the W3C namespace string http://www.w3.org/2000/svg (candidate L236–237 region and the block-2 mask), which is the classifier's standing false fire on namespace strings, plus the kept asset URLs of item (1), class (ii). (3) The T1 residue: hotlink×4 is item (1) counted by the checker; pseudo-ref×2 is the checker's name for the theme%3Aoceanbound file references inside the CSS exhibits, class (i)/(ii) standing in register (c1). (4) The render findings: page-overflow 340px@320 on page and sample (the KB-33/KB-34 narrow-width family), the runtime-hotlink site-theme chain naming scp-wiki.wikidot.com (KB-40, an environment-layer property of the check wiki, not of this file), and the sample credit-modal errors (preview-form; credit:start-preview has no modal mechanism, GOSIGN-TESTS T2 amendment). T3 is clean on both pages.

**Why.** Each disposition rests on evidence a reviewer can re-derive from this package: the kept assets are the original's own files, byte-named in both sources; the namespace strings are inside data URIs on both sides; the render findings are the family dispositions the ledger records for the whole EN14 cohort, and none of them is charged to this file's bytes by the render report.

**Verify.** The kept-asset lines are candidate L223, L224, L1249, and L45 against their originals. The data-URI namespace strings: `grep -c "www.w3.org" candidate.txt`. The render text is RENDER-ROWS-2 row for this theme (RENDER-S2-C (EN14)).

**Disposition.** P5 DISPOSITIONED (ledger (c3)); pattern 7 FIXED via FIX4-LICENSE (KB-04); ledger PASS, row 114, with no section (e) items and no FIX5 re-judgement.

## 12. Verification

**What.** The checks behind this package, each re-runnable from the repo: T1 as recorded (exit 1, 6/0/1, T1-ROWS row 114); T2/T3 as recorded (RENDER-ROWS-2, RENDER-S2-C (EN14)); the wave diffs for 1869877, c2a8bee, and b5cb724 read against this file; the FIX-CODEADDR audit consulted (this theme absent from its mismatch and unresolved lists); CSS brace balance by depth (both files end at depth 0 with no negative dip); the license-entry census (5 against 6, section 8); the self-delivery census (section 3); and `python3 review/build_review.py --check`, which passes over this package (candidate.txt byte-identical to the canonical file; original.txt hash equal to the sources.tsv value).

**Why.** A package is only useful if its claims can be re-derived without trusting the writer; every factual claim above names the lines, the commit, or the register row that decides it.

**Disposition.** Package complete against the ledger PASS, row 114, with the one defect flag of section 8 carried to the batch report.

## Per-theme record

LOCALIZE-ROWS row 114 (source LOCALIZE-S2-B) records one display-affecting finding: P5 (items a,b, EN-storage assets including a cross-article image hotlink). The ledger (c3) register dispositions it (class (ii) / KB-58). The same register records pattern 7 as FIXED for this theme via FIX4-LICENSE under KB-04 (font URL grammar, live-probed 400→200); the localize row does not charge P7 separately, because the broken grammar was introduced by the port's own host move and repaired by the wave, a sequence documented in section 4. T1-ROWS row 114 records exit 1, 6 errors / 0 warns / 1 info (hotlink×4, pseudo-ref×2). RENDER-ROWS-2 (RENDER-S2-C (EN14)) records the combined T2/T3 FINDINGS quoted in the Status table. Two prose-vs-bytes discrepancies are recorded: (1) the FIX4-LICENSE commit subject claims license-box furniture restoration for this theme, and the bytes confirm the furniture (both includes) but not the full content, one of six entries missing (section 8); (2) the ledger's pattern-7 entry names the fix KB-04 without mentioning the host move that made the fix necessary, which the diff shows plainly (original bunny.net, candidate googleapis from creation onward). Neither discrepancy changes the verdict; both are recorded so the next reader is not misled by the shorter record.

### Post-package repairs (REFRESH3-G)

- **FIX-U8, landing `d554544b88a5b14936b0f0e67c10361c79179ad3`** ("pages: U-8 repairs …", 2026-11-17, R/review-scout/FIX-U8.md item 1): the sixth license entry restored — "Amazing Sunset of Pheriche" / Babin Dulal / CC BY-SA 4.0 / Wikimedia Commons source (refreshed candidate L1632–1636, after the Mither.jpeg entry and before `license-box-end` at L1637), +5 lines. The original's box has six entries (orig L1627–1631); FIX4-LICENSE (c2a8bee) restored the box furniture around five, and the missing sixth existed in no canonical version (BATCH-U8 `git log -S Pheriche` empty). The discrepancy note above ("one of six entries missing, section 8") is the as-built record; the entry is now present in the recopied candidate. Checker: error 6 / warn 0 / info 1 before and after, finding set identical, class (i) 0.

The regenerated stamp reads `Overall: STALE` against the pre-repair verdict, by design; no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

None. This theme has no production JP counterpart and no companion deliverable; the wave commits touch only this candidate file (the FIX-CREDIT-D and sweep commits are population commits touching many files, one or two lines each here).

## Multi-wave provenance

| Wave | Commit | Change to this file |
|---|---|---|
| Stage 2 creation (LOCALIZE-S2-B, EN14) | 49c7627 | The candidate created: translation, credit block, repoints, font host move (bunny.net → googleapis, grammar broken), license box furniture dropped with one entry |
| FIX-CREDIT-D | 1869877 | 翻訳責任者 SCP-JP → AI (1 line) |
| FIX4-LICENSE | c2a8bee | Font family grammar repaired in 4 import lines (KB-04); license-box-backend and license-box-end includes restored (KB-63) |
| Usage-example sweep (post-verdict) | b5cb724 | The two usage exhibits renamed :scp-jp:theme:oceanbound → :scp-jp:theme:oceanbound-jp; the stamp's STALE state dates from this commit |

## Appendix — residue blocks

- R1 = B13 (original L32–33 → candidate L38–39): the second usage exhibit line and its lead-in after restructuring; the pair is the blood-variant usage instruction, translated, with the include itself counted in B15's spans. No signature fires because the block mixes the translated lead-in with the escaped include line.
- R2 = B143 (original L1598 → candidate L1601–1602): the blank line and spacing added before the restored license-box-backend include at the tail; the include itself is counted in B144's LICENSE-BOX span. The residue is the padding around the restoration point, nothing else.

## License and attribution

- **Title:** Oceanbound Theme
- **Author:** EstrellaYoshte（DrBleep のために）
- **Source:** https://scp-wiki.wikidot.com/theme:oceanbound — revision 62
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
