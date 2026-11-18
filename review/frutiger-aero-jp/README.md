# Review package — theme:frutiger-aero-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:frutiger-aero-jp — origin CN, population #191 [GOSIGN2-LEDGER (b) row 191]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now fc443f531c00ee7db81d591e8f75febd1a218a3b554f3a9f40c4fed98a5ca928); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (hotlink×3, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 169; GOSIGN2-LEDGER (b) row 191]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-login (6 combos) + sidebar-not-opening (webkit) + runtime-hotlink site-theme chain; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-E (CN6))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 190, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 190]
- FIX5 re-judgement: item 57 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: CN OS faces replaced with JP faces [GOSIGN2-LEDGER-SUPPLEMENT (a) item 57]
- Computed against: canonical commit c923abfb13007617bf34dd8cbde0512171d5cf10; candidate file pages/theme:frutiger-aero-jp.txt sha256:fc443f531c00ee7db81d591e8f75febd1a218a3b554f3a9f40c4fed98a5ca928; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation; verdict stamp and diff.md are generated and must not be hand-edited).
Candidate: review/frutiger-aero-jp/candidate.txt (sha256 df8304e23a048fd4ea5008054892071b39f5a45ecaefae8aa1955bdbe05c4924)
Original: theme:frutiger-aero — scp-wiki-cn, revision 24 (sha256 abafeb437a634b0c76cd6dac16298624f745c6d1676813cf1dbe8ee268891637)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (frozen record) | Where recorded |
|---|---|---|
| Population row | #191 of 287 | review/sources.tsv |
| T1 source check | FINDINGS (classified) | T1-ROWS row 169 |
| T2/T3 render | FINDINGS, all items dispositioned; sample T2 returned no machine verdict (coverage caveat) | RENDER-ROWS-2 (RENDER-S2-E (CN6)) |
| T4/T5 localize + translation | FINDINGS, display-affecting 3 | LOCALIZE-ROWS row 190, source LOCALIZE-S2-D |
| Blocking item | (e) item 57 [D], pattern 7 | GOSIGN2-LEDGER (e) |
| FIX5 re-judgement | FIXED (FIX5-FONTSA, commit 8eacd6e) | GOSIGN2-LEDGER-SUPPLEMENT item 57 |
| Overall | PASS in the go-sign determination; stamp reads STALE because the candidate changed after the verdict (one usage-sweep line) | GOSIGN2-LEDGER + SUPPLEMENT; generated stamp above |

## Provenance

| | |
|---|---|
| Original | theme:frutiger-aero, scp-wiki-cn, revision 24 (first-translation reference) |
| Original file | review/frutiger-aero-jp/original.txt, sha256 abafeb437a634b0c76cd6dac16298624f745c6d1676813cf1dbe8ee268891637, 55,262 B |
| Mirror route | COPY class: byte copy of the frozen S2 cache gosign2-lanes/lane-oc-gs-localize-s2-D/orig-frutiger-aero.txt (R/review-mirrors/INDEX.tsv) |
| Candidate | pages/theme:frutiger-aero-jp.txt, sha256 df8304e23a048fd4ea5008054892071b39f5a45ecaefae8aa1955bdbe05c4924 |
| Follow-up currency | diff-frutiger-aero-from24.txt records rev24 to rev24, no changes; nothing past the reference revision to follow |
| Provenance route | Derived: translated from the original at revision 24 (not a production adoption; no production JP counterpart exists) |

One record defect rides in review/sources.tsv itself: its note for this row claims the original was "superseded upstream since the reference revision", but the follow-up artifact the same note cites records rev24 to rev24 with no changes. The note's first clause is wrong (the same wrong-note shape corrected centrally for ambrose, alcur, inland-empire, wish-for-miracle and yore); the correction is the coordinator's to land in sources.tsv, and this package follows the artifact.

## Summary

A Frutiger Aero theme (Windows XP/Vista-era glass styling) built by modifying Sigma-9, from SCP-CN. The port swaps the CN credit block for the JP preview credit block, moves the theme's self-delivery from a head import on the CN host to a tail load on the draft host, and translates the exhibit body to a standard T4 called the most careful prose translation of its batch. The theme carried one blocking item, ledger item 57 [D]: no Japanese font was loaded or named, so Japanese text fell back to OS defaults. FIX5-FONTSA (commit 8eacd6e) loaded Noto Sans JP and Noto Serif JP and rewired the stacks; the fix is verified in the per-theme record below. Three documented items stand: the credit block misquotes the original's title, two stacks still lead with a font face the port itself removed, and an empty collapsible the candidate introduced stands where the original has none.

## 0. Header / provenance

- What: original.txt is the frozen mirror of theme:frutiger-aero at revision 24 (2,014 lines; the original has no trailing newline); candidate.txt is the canonical candidate (2,028 lines). The classifier found 70 change blocks (41 signature-specific, 29 heuristic, 0 residue); diff.md is Tier 1 (269 changed lines by the generator's count, 16 hunks, full unified diff printed).
- Why: a reviewer must be able to check the port against the exact revision it was made from; the mirror is hash-pinned in review/sources.tsv so any drift is detectable.
- Verify: `sha256sum review/frutiger-aero-jp/original.txt` against the sources.tsv value above; `python3 review/build_review.py --check`.
- Disposition: provenance stands as recorded, with the sources.tsv note defect flagged above and in the batch report.

## 1. Credit and attribution

- What: the original's CN credit includes (:scp-wiki-cn:credit:start/end, original L14/L18) are replaced by the JP preview credit block (candidate L3-12, block B2) carrying all eight TASL fields. The copyright-holder field names Meowait (candidate L8), matching the author the original's credit names ([[*user Meowait]], original L16), and the source link (candidate L11) points at https://scp-wiki-cn.wikidot.com/theme:frutiger-aero, the host recorded for the original in review/sources.tsv. One field is inaccurate: the title, original-title and link-text fields all read "我们曾被许诺的未来/Frutiger Aero版式" (candidate L4, L7, L11), but the original's own credit gives the title as "我们曾被许诺过的未来 Frutiger Aero主题版式" (original L15). The candidate's form drops the character 过, inserts a slash, and shortens 主题版式 to 版式. T4 recorded the misquote in its credit section and its T5 conclusion; it was not charged as a blocking item and stands uncorrected. The translator field is the bare string AI (set by FIX-CREDIT-D, commit 1869877, from SCP-JP; the ruling-3 form). The image license attributions the original carries in a body blockquote (background image: Wikimedia Commons, CC0; header image: Button_Icon_Cyan.svg by Sémhur, CC BY-SA 3.0) are carried translated at candidate L21-30.
- Why: pattern P3 with the TASL record (ruling 3 of RULINGS-20261116): the original-title field is a quotation, and a misquoted title misattributes the work. The preview form (credit:start-preview) is the campaign form for candidate pages (KB-32).
- Verify: diff block B2; read candidate L3-12 against original L14-18.
- Disposition: T4 judged P3 APPLIED with the title misquote and the bare translator string as its recorded findings; the ledger records no P3 charge for this row. The misquote was flagged in the batch report as a standing defect for a future repair wave; that wave has landed: landing `c923abfc` (FIX-RFIX4 F-1, Post-package repairs) made the three title fields quote the original character for character. This package's as-built record is kept; the flag is closed on the current bytes.

## 2. Includes and components

- What: the usage exhibit's escaped include is repointed to :scp-jp: and swept to the -jp self-name (candidate L18; block B5, the one post-verdict line). The sample image uses the unprefixed [[include component:image-block (candidate L35), the population form for this component (the same form appears across the candidate population, e.g. golden-wind-jp L22); T4 noted the JP resolution as unverifiable from its lane and recorded it as a note. One prose link needs a flag: the intro names the theme's template as [[[theme:greyday|Greyday]]] (candidate L14), the same fullname the original names on the CN site. The JP candidate for that theme is theme:greyday-jp, and no production page theme:greyday exists in the repo's production set (pages-existing/ holds no such file), so on scp-jp this link names a page that does not exist. T4 recorded the link's existence as unverified; the repo evidence now settles it, and the link is flagged in the batch report. The credit and interwiki includes are covered in sections 1 and 3.
- Why: pattern P1: include and link targets must resolve in the JP environment; a template credit that links nowhere misleads a reader tracing the theme's lineage.
- Verify: `grep -n '\[\[include' ` and `grep -n 'greyday' ` on candidate.txt; `ls pages-existing/ | grep greyday` (no match).
- Disposition: T4 judged P1 APPLIED with the image-block and greyday items as notes. The greyday link is this package's flag, recorded with the evidence above; the candidate is not edited here.

## 3. Delivery and code loading

- What: the original loads its own CSS twice over: a head module imports theme:frutiger-aero/code/1 from the CN host (original L1-3), and the same CSS sits inline in the page's single [[code type="css"]] block. The candidate removes the head import module (block B1) and loads its own code once, at the tail: a module import of the draft host's local--code/theme%3Afrutiger-aero-jp/1 (candidate L2023) plus an interwiki-style frame at priority=1 naming the same address (candidate L2025-2028; B70). The address /1 names the file's only code block (candidate L188), so the self-delivery census (FIX-CODEADDR) records this theme as MATCH and no remedy applies. The theme has no base include; it is a Sigma-9 modification delivered self-contained, as its prose declares (candidate L14). Inside the code block, the Font Awesome stylesheet import from cdnjs.cloudflare.com (candidate L191) is an exception-listed host (T4 pattern 4).
- Why: patterns P4/P6 and T9: delivery must resolve inside the JP environment, the self-delivery address must name the block that holds the CSS, and a non-BHL theme takes a single priority-1 frame.
- Verify: `grep -n '@import' ` on both files; count [[code]] blocks (one per side); read candidate L2021-2028.
- Disposition: T4 judged P4 and P6 APPLIED. The draft-host self-delivery is T1 class (iii) pseudo-ref, dispositioned in register (c1).

## 4. Fonts and assets

- What, assets: three references to the CN sandbox host (scpsandboxcn.wikidot.com) are kept: the sample image in the image-block (candidate L37), the page background (candidate L280), and the header logo (candidate L427; block B60, whose http-to-https scheme upgrade the classifier labels CSS-BODY heuristic). Both kept images are redistributions with license statements in the credit blockquote (section 1), so re-hosting at posting is legally clean.
- What, fonts: at verdict time the candidate loaded no Japanese face at all; its stacks named 'Segoe UI', 'Microsoft YaHei' and Simhei, none of which carries Japanese glyphs. FIX5-FONTSA (commit 8eacd6e) added a bilingual porter comment and Google Fonts imports for Noto Sans JP and Noto Serif JP at the head of the code block (candidate L193-200; B55), replaced 'Microsoft YaHei' with 'Noto Sans JP' in the heading and body stacks (B56, B57, labeled FONTLOAD-CJK-STACK), replaced Simhei in the Bauhaus stack (candidate L411; B59, labeled CSS-BODY heuristic and narrated here as the same P7 class), and appended 'Noto Sans JP' or 'Noto Serif JP' to eight further stacks (B58, B61-B64, B67-B69, and B65/B66 below). One font item stands: the original's @font-face for 'FlyFlowerSong' (original L189-193, a CN-sandbox-hosted face) was removed in the port, with the reason documented in a Japanese comment (candidate L189), a handling T4 singled out as the batch's most honest. But two stacks still lead with that removed face's name, 'FlyFlowerSong', 'Noto Serif JP', serif (candidate L1220 and L1232; B65, B66): FIX5 appended the loaded JP face behind the dead name rather than removing it. The stacks still render (the second name is loaded), but their first-named face is loaded nowhere in the file or any base, and the FIX5 comment's statement that FlyFlowerSong was among the replaced faces is imprecise for these two stacks.
- Why: pattern P7: Japanese text must render in a loaded Japanese face, and a stack must not name a face nothing loads (the named-but-unloaded shape). Pattern P5 / KB-58: sandbox attachments are class (ii), re-hosted at posting.
- Verify: `git show 8eacd6e` in the canonical history; `grep -n 'FlyFlowerSong\|@font-face' ` on both files (candidate: comment L189, comment L195, stacks L1220/L1232; no @font-face); `grep -n 'Microsoft YaHei\|Simhei' ` on the candidate (only the FIX5 comment, L194-195).
- Disposition: ledger item 57 [D] (pattern 7) re-judged FIXED by FIX5-FONTSA in GOSIGN2-LEDGER-SUPPLEMENT item 57, and re-derived from the bytes in the per-theme record below. Pattern 5 is DISPOSITIONED class (ii) / KB-58 in GOSIGN2-LEDGER (c3). The FlyFlowerSong stack residue is flagged in the batch report as a minor defect; it postdates the verdict's concern (the verdict-era stacks named the face with no JP face behind it at all) and does not disturb the FIXED judgement for item 57, whose charge was that no JP face was provided.

## 5. Header / sidebar / site furniture

- What: the theme renders its window-chrome titles through CSS content: strings, and the candidate keeps the original's Chinese and English strings unchanged: "页面" (candidate L314, main window title), "侧边栏" (candidate L1090, sidebar title), "Sidebar" (candidate L1165 and L1966, mobile and wide variants), "照片查看器" (candidate L1262, image-block title), "Document Viewer" (candidate L1486, tab-set title), and the Chinese lock-notice text (candidate L1804, L1816, L1821). The theme uses no --header-title variables (T4 confirmed none are defined on either side; the original relied on the CN site's base CSS). Its sidebar is its own :target overlay implementation, which T4 recorded as pattern 8 not-applicable with an observation.
- Why: pattern P9 covers header and title language; these strings are reader-visible on every page that uses the theme.
- Verify: `grep -n 'content: "' ` on candidate.txt and compare with the list above; the same strings sit at original L308, L1084, L1256 and L1798-1815.
- Disposition: T4 charged P9 as MISSED and display-affecting (its largest charge against this theme). GOSIGN2-LEDGER (c3) DISPOSITIONED P9 under ruling 2 of RULINGS-20261116 (header and title language is out of scope for migration correctness). The strings stand as the original's, per that ruling; a reader should know the disposition rests on reading these window-title and notice strings as title language, which is the ledger's recorded ground. The render row's sidebar-not-opening item was dispositioned as environment-layer (KB-40) in register (c2).

## 6. Text translation

- What: the exhibit body is translated throughout (24 TRANSLATION-ANCHORED blocks and the TRANS-UNANCHORED mass): headings, tab names, the preset gallery, the quoted lyric samples, and the image caption whose original is deliberate mojibake, rendered into natural Japanese (candidate L37-38). T4 judged the prose the most careful translation of its batch. Two residue classes stand, both recorded by T4: the reader-visible content: strings of section 5, and roughly thirty Chinese CSS comments inside the code block, carried from the original (source-visible only when a reader opens the code; the T5 comment class).
- Why: pattern P10 with T5: reader-visible prose must be Japanese; comments are the recorded exception class, resolved by shape in the appendix.
- Verify: read candidate L14-186 against original L20-187; `grep -n 'content:' ` for the section 5 strings.
- Disposition: T4 judged P10 APPLIED. T5's findings are the section 5 strings (with P9, dispositioned under ruling 2), the credit title misquote (section 1), and the empty collapsible (section 8).

## 7. Links

- What: the credit source link is verified in section 1 (host matches the original's recorded host). The template link to theme:greyday is flagged in section 2. The [[*user meowait]] link (candidate L14) names the author on the JP site under the population's user-link convention. No links to the original site's tag or hub pages exist on either side.
- Why: pattern P11: standing links must resolve in the JP environment; the credit link is the attribution path.
- Verify: the greps named in section 2.
- Disposition: T4 judged P11 APPLIED, with the greyday existence question as a note (settled, against the link, in section 2).

## 8. Structure

- What: the gate is retagged only: the original's page-wide [[iftags +版式]] (original L5) becomes [[iftags +テーマ]] (candidate L1), closing at candidate L2020. The original carries no bare Rate module outside its credit block, and none survives. One structural defect stands, introduced by the candidate: under a first "+ ソースコード" heading (candidate L177) sits an empty collapsible (candidate L178-180, show text "> コードを表示") with nothing inside it, and the real source section follows under a second, identical heading (candidate L184). The original has a single source section with the code inside it. T4 flagged the empty collapsible as a candidate-introduced leftover that should be deleted; it was not charged as a blocking item and stands unfixed.
- Why: an empty collapsible is reader-visible dead furniture: a reader who opens it gets nothing, and the duplicated heading makes the page structure look broken.
- Verify: read candidate L175-190 against original L181-190.
- Disposition: recorded from T4's theme verdict (non-display finding list); no ledger charge covers it. Flagged in the batch report with the section 1 and section 4 items as this theme's standing minor defects.

## 9. Formatting only

- What: none. The classifier records zero reindent blocks and no whitespace-only block for this pair; whitespace changes ride inside translated blocks.
- Why: formatting-only mass must be separable from real change so the reviewer does not mistake churn for edits.
- Verify: classification.json summary (reindent_blocks 0) and the appendix.
- Disposition: nothing to disposition.

## 10. Porter annotations

- What: three porter annotations exist, all inside the code block's head: the consolidation banner (candidate L188, stating the block gathers the original's module and code-block CSS; accurate, since the original's module held only its self-import), the FlyFlowerSong removal note (candidate L189, accurate about the @font-face and the reason), and the FIX5 bilingual font comment (candidate L193-198, accurate for the YaHei and Simhei stacks, imprecise for the two FlyFlowerSong stacks, section 4). Review-stage comment lines in the diff: 0 of the +139 added lines (all three annotations predate the review stage).
- Why: annotations are the porter's testimony about their own work; where testimony and bytes disagree, the bytes govern and the disagreement is documentation-relevant.
- Verify: read candidate L188-200.
- Disposition: recorded; no separate ledger charge covers annotation accuracy for this row.

## 11. Dispositions and exceptions

- What: the row's complete disposition set. T1: 4 errors / 1 warn / 1 info at the 2026-11-16 baseline (hotlink x3, the three sandbox references of section 4; pseudo-ref x1, the draft-host self-delivery), standing classes dispositioned in register (c1). T2/T3: the page items dispositioned as environment-layer (KB-40) in register (c2); the sample run returned no machine verdict (exit 2), a coverage caveat the register carries, not a theme defect. T4: P5 DISPOSITIONED class (ii) / KB-58; P9 DISPOSITIONED under ruling 2; P7 charged to (e) as item 57 and FIXED by FIX5. The candidate changed once after the verdict: the usage sweep (commit b5cb724) inserted -jp into the usage exhibit's self-include (candidate L18), which is why the generated stamp reads STALE.
- Why: a reader must be able to see that every charge against this theme has a named closure, and what the STALE stamp does and does not mean.
- Verify: GOSIGN2-LEDGER (b) row 191, (c1), (c2), (c3) and (e) item 57; GOSIGN2-LEDGER-SUPPLEMENT item 57; `git show b5cb724 -- pages/theme:frutiger-aero-jp.txt`.
- Disposition: PASS in the go-sign determination (286 of 286 pass-eligible themes), with the sections 1, 4 and 8 items standing as documented minor defects outside the charged item.

## 12. Verification

- What a reader can re-run from this repo alone: `python3 review/build_review.py --check` (diff.md and this stamp are current); the sha256 checks in section 0; the greps named in sections 2, 3, 4 and 5; `git show 8eacd6e` for the fix wave. A crude brace scan (comments and strings stripped) ends at the same depth on both files and the CSS diff blocks are all small and local, so no displaced-brace defect of the anniversary-jp shape is present; the scan's constant offset comes from braces inside wikitext and string content it cannot model, identically on both sides.
- Why: the package's claims are only worth what a reader can re-derive; every load-bearing claim above names its check.
- Disposition: verification route stands; the T1 baseline counts are the stamp's, and the FIX5 commit records zero new checker errors for its change.

## Per-theme record: ledger item 57 [D] re-derived

The ledger's blocking item 57 reads: LOCALIZE-S2-D row, pattern 7 in the display-affecting set (JP font not provided); current file has no font imports and names no JP font; no disposition ground covers a missing JP face. The supplement re-judges it FIXED by FIX5-FONTSA, commit 8eacd6e, "CN OS faces replaced with JP faces".

Re-derivation from the bytes. The commit's diff for this file adds the bilingual comment and the two Google Fonts imports (Noto Sans JP, Noto Serif JP) after the Font Awesome import, replaces 'Microsoft YaHei' with 'Noto Sans JP' in the h1 stack (candidate L236) and the body stack (candidate L252), replaces Simhei with 'Noto Sans JP' in the Bauhaus stack (candidate L411), and appends a JP face to eight further stacks, including the two FlyFlowerSong stacks (candidate L1220, L1232). Every edited line is present in the current candidate, and no stack names 'Microsoft YaHei' or Simhei any more (the names survive only inside the FIX5 comment). The supplement's account is exact for the CN OS faces its sentence names. The FIXED judgement is confirmed from the package's own bytes, with one precision the supplement does not make: the FlyFlowerSong stacks were suffixed with a loaded JP face, not stripped of the dead face name (section 4).

Discrepancies and standing items recorded by this package: (1) the sources.tsv supersession note is wrong against its own cited artifact (section 0). (2) The credit block's original-title field misquotes the original's title (section 1); no record dispositions it. (3) The greyday prose link names a page the JP production set does not contain (section 2). (4) The empty collapsible and duplicated source heading are the candidate's own introduction (section 8).

### Post-package repairs (REFRESH3-I) — R-fix-4 (landing c923abf)

The discrepancies in items (2)–(4) above and the Summary's "two stacks still lead with a font face the port itself removed" describe this package as built; the coordinator has since repaired them. Item record `FIX-RFIX4.md` in R/review-scout/ (its frutiger section, F-1…F-4), landing canonical commit `c923abfc` ("pages: R-fix-4 flags repaired (fmd, frutiger, golden-wind)", 2026-11-17), which postdates this package's build at `ded82a8`. `candidate.txt` has been recopied from the current canonical `pages/theme:frutiger-aero-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`; the stamp reads **STALE** by design — no re-judgement is fabricated, and the frozen ledger remains the verdict record. What changed in the candidate (+6/−14):

- **F-1** — all three title fields (タイトル L4, 原題 L7, 元記事リンク label L11) now quote the original's title character for character: 我们曾被许诺过的未来 Frutiger Aero主题版式 (previously 过 dropped, a slash inserted, 主题版式 shortened to 版式). Closes item (2) above. The holder field (Meowait) was already correct.
- **F-2** — the dead face name stripped from both title stacks (now L1209, L1221): `font-family: 'FlyFlowerSong', 'Noto Serif JP', serif;` → `font-family: 'Noto Serif JP', serif;`. Rendering is unchanged (the loaded second face already governed). **Brief-vs-bytes discrepancy (F-2), recorded as instructed:** the brief directed aligning the stacks to "the suffixed form the port itself uses for this face", but that form has no referent in the bytes — the only FlyFlower token is the unsuffixed name FlyFlowerSong (73 occurrences), and the two stacks already carried FIX5's only suffixed shape. The remedy applied instead is the port's own dominant treatment of dead face names in FIX5's parent commit 8eacd6e (where 'Microsoft YaHei' and Simhei were stripped from their stacks): strip the unloaded name, leaving the loaded JP face to govern; 'FlyFlowerSong' now survives only in the @font-face-removal note and the FIX5 comment. Recorded in FIX-RFIX4.md so the coordinator can re-direct if a different form was intended. Closes the Summary's dead-face item.
- **F-3** — the duplicate source furniture removed (8 lines): the premature `[[/collapsible]]`, ---- separator, second + ソースコード heading and second collapsible opener, so the `[[code]]` block stands directly in the original-form collapsible (now the file's only one, balance 1/1). Closes item (4) above; no code line moved.
- **F-4** — the greyday prose link repointed `[[[theme:greyday|Greyday]]]` → `[[[theme:greyday-jp|Greyday]]]` (now L14), the JP candidate harvested in commit 583285b. Closes item (3) above. The checker's one warn is unchanged in code and count (link-target-missing), now naming theme:greyday-jp, a known posting-resolution class.
- Checker (FIX-RFIX4): 4/1/1 → 4/1/1, finding codes identical; 0 class (i) before and after.

## Change set

| File | Role |
|---|---|
| pages/theme:frutiger-aero-jp.txt | the candidate (this package's candidate.txt) |
| pages/theme-decoration-sample-frutiger-aero-jp.txt | decoration sample the render check ran against |

No component ports, sibling candidates or base-theme candidates belong to this theme's change set; the theme is self-contained (a Sigma-9 modification with no base include).

## Multi-wave provenance

| Wave | Commit | What it changed in this file |
|---|---|---|
| Port creation | 4166a2f (Stage 2 CN6 integration) | translation, credit swap, delivery restructure, FlyFlowerSong @font-face removal |
| FIX-CREDIT-D | 1869877 | translator field SCP-JP to AI (ruling-3 form) |
| FIX5-FONTSA | 8eacd6e | ledger item 57: JP font loads and stack rewiring (section 4) |
| Usage sweep | b5cb724 | usage exhibit self-include to the -jp form (post-verdict; the STALE stamp's ground) |

## Appendix: classifier residue and heuristic adjudication

Classification: 70 blocks, 41 signature-specific, 29 heuristic, 0 residue (classification.json, classify_hunks.py 0.1.0, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). The 29 heuristic blocks are 26 TRANS-UNANCHORED exhibit blocks whose translation pairing the anchor pass could not prove (section 6), B54 (the FlyFlowerSong @font-face region, resolved in sections 4 and 10), and the CSS-BODY blocks B59 (the Bauhaus stack's Simhei replacement, a P7 stack rewrite, section 4) and B60 (the header logo's scheme upgrade, section 4). The FIX5 comment-plus-imports block B55 is signature-specific (JPFONT-LOAD), not heuristic. No heuristic block conceals an unrecorded change; in particular the DELIVERY question is settled by topology, not by label: the classifier records no relocation, and the head-module removal with tail delivery is described in section 3 from the bytes.

## License and attribution

- **Title:** 我们曾被许诺过的未来 Frutiger Aero主题版式
- **Author:** Meowait
- **Source:** https://scp-wiki-cn.wikidot.com/theme:frutiger-aero — revision 24
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
