# Review package — theme:golden-wind-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:golden-wind-jp — origin CN, population #192 [GOSIGN2-LEDGER (b) row 192]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now f7755f340827e5ebf2d6eeb3e09dd32069914a9204c1aca89565378e788cc2bb); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 12 errors / 0 warns / 2 infos (pseudo-ref×11, hotlink×1); standing classes dispositioned in register c1 [T1-ROWS row 175; GOSIGN2-LEDGER (b) row 192]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample credit-modal (preview-form) + 884px@768 overflow. [RENDER-ROWS-2 (RENDER-S2-F (CN7))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-F (CN7))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 191, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 191]
- FIX5 re-judgement: item 58 (class D) FIXED — FIX5-FONTSA, commit 8eacd6e: loaded-but-unused JP faces now named in stacks; CN faces replaced by Noto Serif JP [GOSIGN2-LEDGER-SUPPLEMENT (a) item 58]
- Computed against: canonical commit c923abfb13007617bf34dd8cbde0512171d5cf10; candidate file pages/theme:golden-wind-jp.txt sha256:f7755f340827e5ebf2d6eeb3e09dd32069914a9204c1aca89565378e788cc2bb; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation; verdict stamp and diff.md are generated and must not be hand-edited).
Candidate: review/golden-wind-jp/candidate.txt (sha256 24e92ce7e49b2df6106dbb2054218adb398a730c6c41dfe981e71001c7808bdc)
Original: theme:golden-wind — scp-wiki-cn, revision 29 (sha256 19b9bb8e990cf8b8096b551f264816a7cd81a156f1319c951fe4702485f58687)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (frozen record) | Where recorded |
|---|---|---|
| Population row | #192 of 287 | review/sources.tsv |
| T1 source check | FINDINGS (classified) | T1-ROWS row 175 |
| T2/T3 render | FINDINGS, all items dispositioned | RENDER-ROWS-2 (RENDER-S2-F (CN7)) |
| T4/T5 localize + translation | FINDINGS, display-affecting 3 | LOCALIZE-ROWS row 191, source LOCALIZE-S2-D |
| Blocking item | (e) item 58 [D], pattern 7 | GOSIGN2-LEDGER (e) |
| FIX5 re-judgement | FIXED (FIX5-FONTSA, commit 8eacd6e) | GOSIGN2-LEDGER-SUPPLEMENT item 58 |
| Overall | PASS in the go-sign determination; stamp reads STALE because the candidate changed after the verdict (two usage-sweep lines) | GOSIGN2-LEDGER + SUPPLEMENT; generated stamp above |

## Provenance

| | |
|---|---|
| Original | theme:golden-wind, scp-wiki-cn, revision 29 (first-translation reference) |
| Original file | review/golden-wind-jp/original.txt, sha256 19b9bb8e990cf8b8096b551f264816a7cd81a156f1319c951fe4702485f58687, 15,498 B |
| Mirror route | COPY class: byte copy of the frozen S2 cache gosign2-lanes/lane-oc-gs-localize-s2-D/orig-golden-wind.txt (R/review-mirrors/INDEX.tsv) |
| Candidate | pages/theme:golden-wind-jp.txt, sha256 24e92ce7e49b2df6106dbb2054218adb398a730c6c41dfe981e71001c7808bdc |
| Follow-up currency | diff-golden-wind-from29.txt records rev29 to rev29, no changes; nothing past the reference revision to follow |
| Provenance route | Derived: translated from the original at revision 29 (not a production adoption; no production JP counterpart exists) |

One record defect rides in review/sources.tsv itself: its note for this row claims the original was "superseded upstream since the reference revision", but the follow-up artifact the same note cites records rev29 to rev29 with no changes. The note's first clause is wrong (the same wrong-note shape corrected centrally for ambrose, alcur, inland-empire, wish-for-miracle and yore); the correction is the coordinator's to land in sources.tsv, and this package follows the artifact.

## Summary

A Golden Wind (JoJo-inspired) aesthetic theme from SCP-CN, self-contained with no base theme. The port swaps in the JP preview credit block, re-hosts the theme's scattered attachments onto the draft host, adds an interwiki frame and a JP license box, and translates the exhibit body. The theme carried one blocking item, ledger item 58 [D]: its Google Fonts imports loaded Noto Sans JP and Noto Serif JP but no stack referenced them, while the display stacks named Chinese OS faces, so Japanese text fell back to OS defaults. FIX5-FONTSA (commit 8eacd6e) wired Noto Serif JP into the three display stacks; the fix is verified in the per-theme record below, with one precision (Noto Sans JP remains loaded but unused). Three further items stand documented: the credit holder field is a pointer although the file itself names the author twice, one sample image was never re-hosted although two porter texts claim all attachments were, and the header strings remain Chinese under the campaign's ruling-2 ground.

## 0. Header / provenance

- What: original.txt is the frozen mirror of theme:golden-wind at revision 29 (630 lines); candidate.txt is the canonical candidate (670 lines). The classifier found 41 change blocks (35 signature-specific, 6 heuristic, 0 residue); diff.md is Tier 1 (144 changed lines by the generator's count, 10 hunks, full unified diff printed).
- Why: a reviewer must be able to check the port against the exact revision it was made from; the mirror is hash-pinned in review/sources.tsv so any drift is detectable.
- Verify: `sha256sum review/golden-wind-jp/original.txt` against the sources.tsv value above; `python3 review/build_review.py --check`.
- Disposition: provenance stands as recorded, with the sources.tsv note defect flagged above and in the batch report.

## 1. Credit and attribution

- What: the original carries no credit block at all; its attribution is the body prose naming [[*user Dr Roger_F_XL]] as the maker (original L50) and the code banner "Created by Dr Roger_F_XL / CC BY-SA 3.0" (original L86-89). The candidate adds the JP preview credit block (candidate L11-20, block B3) with all eight TASL fields, and its own body prose also names the author (candidate L62). Against those two namings, the credit block's copyright-holder field does not name him: it reads "原語版ページの作成者に同じ（scp-wiki-cn の theme:golden-wind）" (candidate L16), a pointer to the original page instead of the author. The license box the port adds at the tail repeats the same pointer form in its author parameter (candidate L664). T4 recorded the anonymized holder in its batch summary as part of a systematic gap; no ledger register dispositions it for this row (the (c3) entry reads "row charges → (e)" and the row's only (e) item is item 58). It is flagged in the batch report as a defect of the same family the coordinator is repairing in past-oriented-jp, where the identical pointer form was charged and is being replaced with the named author. Two smaller credit facts: the creation-year field reads 2025 (candidate L17), while the theme's own banner says "[2023 Wikidot Theme]" (candidate L118); the original carries no dated credit record, so 2025 is unverifiable from the file, and T4 noted the inconsistency. The source link (candidate L19) points at https://scp-wiki-cn.wikidot.com/theme:golden-wind, the host recorded for the original in review/sources.tsv. The translator field is the bare string AI (set by FIX-CREDIT-D, commit 1869877, from SCP-JP; the ruling-3 form).
- Why: pattern P3 with the TASL record (ruling 3 of RULINGS-20261116): the holder field is where a reader learns whose work this is; a pointer that withholds a name the file itself gives is an attribution defect, not a form choice. The preview form (credit:start-preview) is the campaign form for candidate pages (KB-32).
- Verify: diff block B3; read candidate L11-20 against original L50 and L84-89; read candidate L663-668.
- Disposition: T4 judged P3 APPLIED (minor) on structure; the holder pointer and the year inconsistency stand as its recorded notes, undispositioned in the ledger. The pointer is this package's principal flag.

## 2. Includes and components

- What: the candidate adds an interwiki-style include the original does not have (candidate L5-8, priority=1, naming its own code address; section 3). The usage exhibit's includes are repointed to :scp-jp: (candidate L74, L78; blocks B18, B19) and both were swept to the -jp self-name after the verdict (the stamp's STALE ground). The sample image uses the unprefixed [[include component:image-block (candidate L22), the population form for this component. The credit includes are covered in section 1.
- Why: patterns P1 and P6: include targets must resolve on scp-jp, and a theme delivering its own code takes the interwiki frame that loads it in the JP environment.
- Verify: `grep -n '\[\[include' ` on both files.
- Disposition: T4 judged P1 APPLIED (minor note on the unprefixed component) and P6 APPLIED (the frame is a correct addition for a non-BHL theme).

## 3. Delivery and code loading

- What: the head module's self-delivery import moves from the CN files host (original L2, scp-wiki-cn.wdfiles.com/local--code/theme:golden-wind/1) to the draft host (candidate L2, local--code/theme%3Agolden-wind-jp/1; block B1), and the added interwiki frame names the same address (candidate L5-8). The theme's CSS sits in a single [[code type="css"]] block on each side (original L82, candidate L98), so the address /1 names the block that holds the CSS; the self-delivery census (FIX-CODEADDR) records this theme as MATCH and no remedy applies. Every attachment reference inside the CSS is re-hosted to the candidate's own draft-host attachment space (blocks B16, B26, B29, B33-B39: the poster, logo, sky animation, character image, and cursor images), with one exception recorded in section 4.
- Why: pattern P4 and T9: delivery must resolve inside the JP environment, and attachments scattered across the original author's personal hosts (roger.wdfiles.com, scpsandboxcn) must move to the candidate's own space or the theme breaks when those hosts change.
- Verify: `grep -n '@import\|url(' ` on both files; count [[code]] blocks (one per side).
- Disposition: T4 judged P4 APPLIED. The draft-host references are T1 class (iii) pseudo-refs (11 of them), dispositioned in register (c1); at posting they become the page's own addresses and attachments.

## 4. Fonts and assets

- What, assets: every original attachment is re-hosted to the draft host except one. The sample image-block still loads https://scp-wiki-cloud.wdfiles.com/local--files/xl/rojo (candidate L23), the exact URL the original uses (original L11), on a host that is in no exception list. T4 charged it as pattern 5 MISSED (its lane could not determine whether the host is CN-side or JP-side) and it is the theme's single T1 hotlink. Two porter texts overstate the position: the code banner comment says all of the original's attachments were re-hosted as candidate attachments (candidate L102-104), and the license-box note says external-host attachments were re-hosted to the candidate page (candidate L666). Both are inaccurate for this one image. The image itself stands as T4 and T1 recorded it; the inaccurate claims are flagged in the batch report.
- What, fonts: the two Google Fonts imports (Noto Sans JP, Noto Serif JP; candidate L110-111) already existed before FIX5; what was missing was any stack referencing them. FIX5-FONTSA (commit 8eacd6e) expanded the porter comment (candidate L106-109) and replaced the Chinese faces in the three display stacks with 'Noto Serif JP': the h1/#page-title stack (candidate L124; block B24), the header logo stack behind 'SJQY' (candidate L141; B27), and the #header h2 stack (candidate L151; B28). The classifier labels B24 and B28 GLYPH-FORM and B27 CSS-BODY; all three are narrated here as the P7 stack rewrites they are. Two precisions: 'Noto Sans JP' is still named in no stack (it occurs only in the comment, candidate L106), so one of the two loaded JP faces remains unused, although the theme's body has no font-family of its own and inherits the site default; and 'SJQY' (candidate L141) names a face nothing loads, on either side (the original names it too, original L109), an inherited state the port preserves.
- Why: pattern P7: a loaded-but-unused JP face does nothing for Japanese text, and stacks naming CN OS faces JP readers do not carry fall back to OS defaults. Pattern P5: an attachment left on a foreign host is a breakage risk and, here, contradicts the file's own claims.
- Verify: `git show 8eacd6e` in the canonical history; `grep -n 'font-family' ` on candidate.txt (L124, L141, L151 for the display stacks) and `grep -n 'Noto Sans JP' ` (comment only); `grep -n 'scp-wiki-cloud' ` on both files.
- Disposition: ledger item 58 [D] (pattern 7) re-judged FIXED by FIX5-FONTSA in GOSIGN2-LEDGER-SUPPLEMENT item 58, and re-derived from the bytes in the per-theme record below. The cloud image is the T1 register's hotlink class (ii) standing item; T4's pattern-5 charge has no separate (c3) line for this row (section 11).

## 5. Header / sidebar / site furniture

- What: the theme draws its header text through CSS content: strings, and both stand verbatim from the original: `content: "SCP基金会"` (candidate L140, from original L108) as the header title, and `content: '意志 信念 觉悟'` (candidate L157, from original L125) as the subtitle, the second containing the simplified character 觉 where Japanese writes 覚. The theme uses no --header-title variables and defines no sidebar text (T4 pattern 8 not applicable).
- Why: pattern P9 covers header and title language; these strings render on every page that uses the theme.
- Verify: `grep -n 'content:' ` on candidate.txt (L140, L157) against original.txt (L108, L125).
- Disposition: T4 charged P9 as MISSED and display-affecting. This row's (c3) entry in GOSIGN2-LEDGER reads "row charges → (e)" and raises no per-pattern P9 line; the campaign-wide ground that closes header language is ruling 2 of RULINGS-20261116 (header and title language is out of scope for migration correctness), which (c3) cites explicitly for the sibling rows' identical charges. The strings stand as the original's; the record states the ground and its route rather than pretending a per-row line exists.

## 6. Text translation

- What: the exhibit body is translated throughout (11 TRANSLATION-ANCHORED blocks plus the unanchored mass): the mock SCP article sample, tab names, the what-is-this and usage sections, and the collapsible labels. Two translation residues stand, both recorded by T5: the image caption 百々羽三人 is kept untranslated (candidate L24, from original L12; T5 read it as a proper noun and asked for a translation or a note), and four Chinese CSS comments remain inside the code block (source-visible only). One content deletion: the original's footnote carried a Baidu encyclopedia link (original L50); the candidate's footnote keeps the JoJo reference and drops the link (candidate L62). T4 judged it the row's only information loss, and minor.
- Why: pattern P10 with T5: reader-visible prose must be Japanese; comments are the recorded exception class, resolved by shape in the appendix.
- Verify: read candidate L22-95 against original L10-80.
- Disposition: T4 judged P10 APPLIED. T5's findings are the two header strings (section 5), the caption, and the observations collected in section 8.

## 7. Links

- What: no standing links to the original site's tag or hub pages exist on either side (T4 pattern 11 not applicable); the credit source link is verified in section 1. One inbound link matters for this theme's record: theme:drunken-alley-jp is an add-on over this theme as its base, and its usage procedure again names the prerequisite (the restored line names theme:golden-wind-jp), after ledger item 55 [I] charged the prerequisite's deletion and FIX5-STRUCTB re-judged it FIXED. A reader of this package can therefore follow the dependency in both directions.
- Why: a base theme's documentation should show what depends on it, especially where the campaign itself had to repair the dependency once.
- Verify: GOSIGN2-LEDGER (e) item 55 and GOSIGN2-LEDGER-SUPPLEMENT item 55; the drunken-alley-jp package (batch R-fix-3) carries the repair's own record.
- Disposition: no link defect in this file.

## 8. Structure

- What: the gate is retagged only (original L4 [[iftags +版式]] to candidate L9 [[iftags +テーマ]], closing at candidate L670). The original's bare [[module Rate]] inside a [[>]] block (original L6-8) is deleted with its wrapper; no empty shell remains (the KB-09 form; the preview credit module is rate-bearing). Two inherited shapes stand as the original's: the usage sample contains an unescaped [[module rate]] inside its blockquote (candidate L80, from original L68), which T4 noted may render a second rate module inside the sample and referred to render confirmation; and two harmless typos ride along, `border: tpx dashed #000` (candidate L498, original L466) and the comment /* CUROSR */ (candidate L650, original L618). The candidate adds one structure the original lacks: the JP license box at the tail (candidate L663-668; block B41), whose attribution accuracy is covered in section 1 and whose re-hosting claim is covered in section 4.
- Why: structure is what a reader's page is built from; inherited defects must be distinguishable from port-introduced ones, and additions must be visible as additions.
- Verify: read candidate L60-88 against original L56-80; `grep -n 'module rate' ` on both files (original L7 and L68; candidate L80 only).
- Disposition: T4 recorded the unescaped sample Rate and the typos as observations, not charges; they stand as the original's shapes. The bare-Rate deletion is the settled KB-09 form.

## 9. Formatting only

- What: five whitespace-only blocks inside the code block (B23, B25, B30, B31, B32: blank-line and spacing adjustments at candidate L120-121, L127-128, L301-302, L307-308, L314-315). No reindent blocks.
- Why: formatting-only mass must be separable from real change so the reviewer does not mistake churn for edits.
- Verify: classification.json label counts (WS-ONLY 5).
- Disposition: nothing to disposition.

## 10. Porter annotations

- What: two porter annotations exist, both at the code block's head: the banner comment (candidate L99-104) giving the original title, the porting credit line, and the re-hosting claim that section 4 shows to be inaccurate for one image; and the FIX5 font comment (candidate L106-109), which is accurate about the Serif wiring (its statement that both JP faces are loaded is also true; only one is wired, section 4). The original's own banner comment (Golden Wind Theme / [2023 Wikidot Theme] / Created by Dr Roger_F_XL / CC BY-SA 3.0) is carried at candidate L117-121. Review-stage comment lines in the diff: 0 of the +92 added lines.
- Why: annotations are the porter's testimony about their own work; where testimony and bytes disagree, the bytes govern and the disagreement is documentation-relevant.
- Verify: read candidate L98-121.
- Disposition: recorded; no separate ledger charge covers annotation accuracy for this row.

## 11. Dispositions and exceptions

- What: the row's complete disposition set. T1: 12 errors / 0 warns / 2 infos at the 2026-11-16 baseline (pseudo-ref x11, the draft-host references of section 3; hotlink x1, the cloud image of section 4), standing classes dispositioned in register (c1). T2/T3: the page's runtime-hotlink chain dispositioned as environment-layer (KB-40) and the sample's credit-modal and 884px@768 overflow under the preview-form and cross-cutting families (KB-33/KB-34), register (c2). T4: the (c3) entry for this row reads "row charges → (e)"; the only (e) item the row produced is item 58 (pattern 7), FIXED by FIX5. The pattern-5 and pattern-9 closures ride on the standing grounds stated in sections 4 and 5 rather than on per-pattern lines for this row, and this package says so rather than inventing lines. The candidate changed twice after the verdict in one commit: the usage sweep (b5cb724) inserted -jp into both usage-exhibit includes (candidate L74, L78), which is why the generated stamp reads STALE.
- Why: a reader must be able to see that every charge against this theme has a named closure, and what the STALE stamp does and does not mean.
- Verify: GOSIGN2-LEDGER (b) row 192, (c1), (c2), (c3) and (e) item 58; GOSIGN2-LEDGER-SUPPLEMENT item 58; `git show b5cb724 -- pages/theme:golden-wind-jp.txt`.
- Disposition: PASS in the go-sign determination (286 of 286 pass-eligible themes), with the section 1 holder pointer standing as a documented, undispositioned defect.

## 12. Verification

- What a reader can re-run from this repo alone: `python3 review/build_review.py --check` (diff.md and this stamp are current); the sha256 checks in section 0; the greps named in sections 2, 3, 4 and 5; `git show 8eacd6e` for the fix wave. A brace-depth scan of both files (comments and strings stripped) ends at depth 0 and never goes negative on either side, so no displaced-brace defect of the anniversary-jp shape is present.
- Why: the package's claims are only worth what a reader can re-derive; every load-bearing claim above names its check.
- Disposition: verification route stands; the T1 baseline counts are the stamp's, and the FIX5 commit records that its change introduced no new class (i) errors.

## Per-theme record: ledger item 58 [D] re-derived

The ledger's blocking item 58 reads: LOCALIZE-S2-D row, pattern 7, JP fonts declared but unused, JP text falls back to OS fonts (display-affecting set); Noto Sans JP / Noto Serif JP are loaded via Google Fonts imports, but no font-family stack references them, and the display stacks name CN OS faces (华文新魏 / 华文楷体). The supplement re-judges it FIXED by FIX5-FONTSA, commit 8eacd6e, "loaded-but-unused JP faces now named in stacks; CN faces replaced by Noto Serif JP".

Re-derivation from the bytes. The imports predate the fix (they are the original port's, candidate L110-111). The commit's diff for this file expands the porter comment above them and makes exactly three stack edits: 'Arial Black', '华文新魏', cursive becomes 'Arial Black', 'Noto Serif JP', cursive (candidate L124); 'SJQY', '华文楷体', cursive becomes 'SJQY', 'Noto Serif JP', cursive (candidate L141); and the same 华文新魏 replacement in the #header h2 stack (candidate L151). All three lines are present in the current candidate, and the Chinese face names survive only inside the FIX5 comment (candidate L108). The supplement's account is exact for the display stacks and for Noto Serif JP. One precision it does not make: Noto Sans JP, the other loaded face, is still named in no stack (section 4); the item's charge was that the display stacks named CN faces while the loaded JP faces went unused, and for the display stacks that charge is fully cured. The FIXED judgement is confirmed from the package's own bytes with that precision recorded.

Discrepancies and standing items recorded by this package: (1) the sources.tsv supersession note is wrong against its own cited artifact (section 0). (2) The credit holder field and the license-box author parameter are pointers although the file names Dr Roger_F_XL twice; no register dispositions them (section 1). (3) The banner comment and license-box note claim complete re-hosting; one image was not re-hosted (section 4). (4) The credit creation year (2025) and the banner year (2023) disagree, and the file offers no ground to prefer either (section 1).

### Post-package repairs (REFRESH3-I) — R-fix-4 (landing c923abf)

Items (2) and (3) above and the Summary's corresponding standing items describe this package as built; the coordinator has since repaired them. Item record `FIX-RFIX4.md` in R/review-scout/ (its golden-wind section, G-1…G-3), landing canonical commit `c923abfc` ("pages: R-fix-4 flags repaired (fmd, frutiger, golden-wind)", 2026-11-17), which postdates this package's build at `ded82a8`. `candidate.txt` has been recopied from the current canonical `pages/theme:golden-wind-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`; the stamp reads **STALE** by design — no re-judgement is fabricated, and the frozen ledger remains the verdict record. What changed in the candidate (+6/−5):

- **G-1** — both attribution carriers now name the author: the credit field (now L16) reads `**著作権者:** Dr Roger_F_XL` and the license-box parameter (now L664) reads `|author=Dr Roger_F_XL]]`, each in the population's established plain-name form (compare frutiger's 著作権者: Meowait and fmd's `|author=AI_Mayca]]`). Closes item (2) above. The name is evidenced twice in the file itself (body L62, code banner L119) and in the original.
- **G-2** — both re-hosting claims corrected to state the delivered exception (the banner comment, now L101–105, and the license-box note, now L666): the attachments are re-hosted except the opening image block's `rojo`, which is still referenced at its original scp-wiki-cloud URL (the file's sole hotlink, candidate L23). The image itself is not moved. Closes item (3) above.
- **G-3 (year record — no edit).** The credit block's 作成年 (candidate L17) reads 2025 while the code banner (candidate L118, carried from original L85) reads `[2023 Wikidot Theme]`. Nothing in either file settles which year the credit field should carry: the banner's 2023 is the theme's own creation stamp, the campaign's 作成年 elsewhere records the original page's creation year, and the original has no credit block or other dated statement to check 2025 against (its only other date-bearing line is the same banner). Per the brief no edit was made; the discrepancy stands recorded here, in item (4) above and in FIX-RFIX4.md G-3 for the coordinator. This is a recorded, not a fixed, item.
- Checker (FIX-RFIX4): 12/0/2 → 12/0/2, finding codes identical; 0 class (i) before and after.

## Change set

| File | Role |
|---|---|
| pages/theme:golden-wind-jp.txt | the candidate (this package's candidate.txt) |
| pages/theme-decoration-sample-golden-wind-jp.txt | decoration sample the render check ran against |

Related candidate outside the change set: theme:drunken-alley-jp, an add-on whose base prerequisite is this theme (section 7). No component ports or base-theme candidates belong to this theme's own change set; it is self-contained.

## Multi-wave provenance

| Wave | Commit | What it changed in this file |
|---|---|---|
| Port creation | 6d745e5 (Stage 2 CN7 integration) | translation, credit block and license box added, delivery repoints, attachment re-hosting |
| FIX-CREDIT-D | 1869877 | translator field SCP-JP to AI (ruling-3 form) |
| FIX5-FONTSA | 8eacd6e | ledger item 58: JP face wired into the display stacks (section 4) |
| Usage sweep | b5cb724 | both usage-exhibit includes to the -jp form (post-verdict; the STALE stamp's ground) |

## Appendix: classifier residue and heuristic adjudication

Classification: 41 blocks, 35 signature-specific, 6 heuristic, 0 residue (classification.json, classify_hunks.py 0.1.0, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). The 6 heuristic blocks are B10, B15, B20 and B21 (exhibit translation blocks the anchor pass could not pair, section 6), B27 (the header-logo stack rewrite, labeled CSS-BODY and narrated as P7 in section 4), and B40 (the code block's closing lines, where the candidate's tail gains the license box of B41). The other two FIX5 stack rewrites, B24 and B28, are signature-specific (GLYPH-FORM). The five WS-ONLY blocks are formatting only (section 9). No heuristic block conceals an unrecorded change.
