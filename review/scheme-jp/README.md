# Review package — theme:scheme-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scheme-jp — origin EN, population #31 [GOSIGN2-LEDGER (b) row 31]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 96c226dbf1b70d6aaa1bdb7f8daaca65d1956b2a5049c806ec810efb73e5a3c1); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 16 errors / 1 warn / 7 infos (pseudo-ref×14, hotlink×2); standing classes dispositioned in register c1 [T1-ROWS row 31; GOSIGN2-LEDGER (b) row 31]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — T2 incomplete (exit 2 both pages ×6, webkit timeout), 768px second notice instance clipped over sidebar, mobile logo clipped, tagline/footer word-split, code block clipped, gold hamburger overlays body/rate, sample credit-modal, 884px@768. [RENDER-ROWS-1 (RENDER-C row 31)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 31)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 31, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 31]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 31]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:scheme-jp.txt sha256:96c226dbf1b70d6aaa1bdb7f8daaca65d1956b2a5049c806ec810efb73e5a3c1; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/scheme-jp/candidate.txt (sha256 96c226dbf1b70d6aaa1bdb7f8daaca65d1956b2a5049c806ec810efb73e5a3c1)
Original: theme:scheme — scp-wiki, revision 30 (sha256 473d7bbee9cb2bdd9b3256f3ea72347b80dccde2857e0ff55d7fe5fe66f109e0)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.
- Provenance route: adopted from the production JP counterpart (kind K6 in review/sources.tsv). The production page theme:scheme exists on scp-jp; the campaign's migration deliverable for it is pages/phase17-diff-scheme-jp.txt from Phase 17, and sources.tsv records the production page as matching the reference revision (production drift 一致）. The candidate in this repo is that production form as imported in commit d727e92, plus five campaign wave edits: the Phase 17 credit frame (8dcac74), the T1 credit-field completion (b816e10), the FIX-CREDIT-D translator normalization (1869877), the FIX4-REPOINT font-host revert (443c608), and the post-verdict usage-example sweep (b5cb724). The sweep postdates the FIX5 verdict head, so the generated stamp above reads STALE; the verdict lines under it describe the pre-sweep file, and the only post-verdict change is the sweep's single usage line.

## Status

| Check | Verdict | Source |
|---|---|---|
| Overall | STALE (stamp) — candidate changed after the verdict; verdicts below describe the pre-change file | GOSIGN2-LEDGER (b) row 31, stamp regenerated at b5cb724 |
| T1 source check | FINDINGS (classified) — exit 1, 16 errors / 1 warn / 7 infos (pseudo-ref×14, hotlink×2) | T1-ROWS row 31 |
| T2/T3 render | FINDINGS — T2 incomplete (exit 2 both pages ×6, webkit timeout); 768px second notice clipped over sidebar, mobile logo clipped, tagline/footer word-split, code block clipped, gold hamburger overlays body/rate, sample credit-modal, 884px@768 | RENDER-ROWS-1 (RENDER-C row 31) |
| T4 localize patterns | FINDINGS — 0 display-affecting findings | LOCALIZE-ROWS row 31 (LOCALIZE-B) |
| T5 translation text | FINDINGS — judged jointly with T4 by the source report | LOCALIZE-ROWS row 31 |
| FIX5 re-judgement | none — no OPEN items at the ledger determination | GOSIGN2-LEDGER (b) row 31 |

## Provenance

| Side | Identity |
|---|---|
| Original | theme:scheme, scp-wiki, revision 30; mirror class FETCH-REGEN; sha256 473d7bbee9cb2bdd9b3256f3ea72347b80dccde2857e0ff55d7fe5fe66f109e0 (review/sources.tsv) |
| Candidate | pages/theme:scheme-jp.txt in this repo; sha256 96c226dbf1b70d6aaa1bdb7f8daaca65d1956b2a5049c806ec810efb73e5a3c1 (stamp, computed against canonical commit b5cb724) |
| Production counterpart | theme:scheme on scp-jp (kind K6); migration deliverable pages/phase17-diff-scheme-jp.txt |

## Summary

Scheme is a steampunk gear-and-gold theme that self-delivers one CSS payload (its second code block) through a head module and frame at priority 1, and whose production JP form carries a set of JP-environment adaptations: an added Noto Serif JP font load, JP fallbacks in the serif stacks, interwiki sidebar selector twins, and four tail correction modules for the mobile masthead, navigation, and credit glyph. The campaign's wave edits are the credit block's two-step construction (Phase 17 frame, T1 fields, FIX-CREDIT-D normalization) and the FIX4-REPOINT revert of the production port's AutoLocalize font-host move, which had carried the Song Myung import to bunny.net against the ledger's judgment call. The theme's one dispositioned item is P5 (font hosts outside the exception list). Two classifier leads are corrected on the bytes in the sections below: the info pair is retained, not deleted (section 1), and the tail modules are three header/navigation corrections plus one credit correction, not a single credit-CSS block (section 5). No defect is flagged for this theme.

## Classification

| Label | Blocks |
|---|---|
| COMMENT-TEXT | 17 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 5 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 14 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 3 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 3 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 21 |
| TRANSLATION-ANCHORED | 12 |

Across 70 classified blocks: 34 specific (48.6%), 25 heuristic (35.7%), 11 residue (15.7%), 0 skipped. The specific share is the lowest in this batch because the production port's changes are dominated by single-line CSS URL repoints (DRAFT-HOST), comment translations (COMMENT-TEXT), and sample-text translations that defeat anchor matching; every residue block is resolved by shape in the Appendix, and no block hides a mechanism change.

## 1. Credit and attribution

**What.** The credit block (candidate L13–22) was built in two waves on a page that had none. Phase 17 (8dcac74) added the include pair with two fields （初訳時参照リビジョン 30 and the 元記事リンク to https://scp-wiki.wikidot.com/theme:scheme). The T1 wave (b816e10) added the six missing fields: タイトル Scheme Theme, 翻訳責任者 SCP-JP, 翻訳年 2026, 原題 Scheme Theme, 著作権者 shaftmetal, thd-glasses, Denevola, Fluxman, 作成年 2021. FIX-CREDIT-D (1869877) then normalized the translator line to AI. The classifier spans are CREDIT-PREVIEW and TASL-FIELDS in block B4. Block B7 carries an INFO-DEL span: the skeleton's lead text for that label claims the info module pair was removed, and the bytes contradict it. The pair is retained and repointed (candidate L35 [[include :scp-jp:info:start]], L37 [[include :scp-jp:info:end]]), with the placeholder text translated (hello → こんにちは, candidate L36), exactly the form the sibling adopted themes carry.

**Why.** The six-field gap was LOCALIZE-ROWS row 31 item (b) (P3 missing six credit fields), and the ledger (c3) register records pattern 3 as FIXED for this theme. The two-step build is visible in the commits because Phase 17's deliverable created the frame the T1 audit then measured against the full TASL set. The translator normalization follows ruling 3: this production page's Sigma-10 form is a campaign production (translation year 2026), so the credit names AI, not the SCP-JP placeholder the T1 wave had written. The holder field names the original's four authors as the production credit recorded them; no register contests the attribution. The info pair's retention follows the JP environment's furniture: the JP info module is what renders the info pane here, and deleting the pair would have removed the exhibit the theme page demonstrates.

**Verify.** Read candidate L13–22 and L35–37. `git show 8dcac74 -- pages/theme:scheme-jp.txt` shows the frame and two fields; `git show b816e10 -- pages/theme:scheme-jp.txt` shows the six added field lines; `git show 1869877 -- pages/theme:scheme-jp.txt` shows the one-line translator change. `grep -n "info:start\|info:end" candidate.txt` returns the retained pair on :scp-jp:.

**Disposition.** Pattern 3 FIXED (ledger (c3)); ledger PASS, row 31 (stamp STALE for the unrelated sweep change). The skeleton's INFO-DEL lead is a prose-vs-bytes discrepancy, recorded here and in the batch report: the label fired on the repointed pair, and no info content was deleted.

## 2. Includes and components

**What.** The tag gate localizes (candidate L11 [[iftags +テーマ]] against the original's +theme; IFTAGS span in B4). The include repoints: the interwiki-style frame at the head (block B2, with an EXHIBIT-RESTRUCTURE primary) and the info pair (section 1). The usage exhibit (candidate L45, block B10) reads @@[[include :scp-jp:theme:scheme-jp]]@@ inside a div.code; its COMPONENT-SWAP primary is the classifier's name for the prefix change on that line, and ESCAPED-INCLUDE records its exhibit form. The bare Rate module is kept (candidate L28 [[module rate]]), below the credit block, with its exhibit labels translated (**評価：**, residue pair B5).

**Why.** The usage line's history is the sweep's: as imported it named :scp-jp:theme:scheme (the production page), and the population sweep (b5cb724) renamed it to the -jp posting name, the name this candidate will be posted under, so the exhibit resolves at posting. The kept bare Rate is the sanctioned form for this theme by name: the ledger (c2) preamble's labelled paired Rate exhibits exception (FIXPREP / FIX3-A1 §1.1) lists scheme among the three themes whose bare Rate beside the credit block is the exhibit form, not KB-09 duplication. The frame's EXHIBIT-RESTRUCTURE primary is the standing false fire on a mere repoint.

**Verify.** `git show b5cb724 -- pages/theme:scheme-jp.txt` shows the single usage line changing. Candidate L28 shows the kept Rate module; the exception text is in the ledger (c2) preamble, item 6.

**Disposition.** Ledger PASS, row 31; the sweep is a coordinator landing recorded in the campaign record, post-verdict by design.

## 3. Delivery and code loading

**What.** The head module (candidate L1–3) imports https://sigma10-jp-test.wdfiles.com/local--code/theme%3Ascheme-jp/2, and the frame (candidate L5–8) names the same address at priority=1 (blocks B1/B3; DELIVERY-HOST, DRAFT-HOST, SELF-DELIVERY spans). The original names theme:scheme/2 on scp-wiki.wdfiles.com the same way. The address is correct against the census: the file has two [[code]] blocks in document order, a plain exhibit block (candidate L75) and the CSS payload (candidate L91), so the payload is /2 on both sides. Fourteen DRAFT-HOST blocks are single-line CSS URL repoints of the theme's own files from the original's storage paths to the draft host's theme%3Ascheme-jp paths (e.g. candidate L137: line.png and header_cogs.jpg background URLs).

**Why.** The self-delivery keeps the original's addressing scheme (the payload was always /2 because an exhibit block precedes it), so the port changes only the host and the page name, nothing about which block loads. The FIX-CODEADDR audit does not list this theme among mismatches or unresolved references, and the census here agrees. The own-file URL repoints put the theme's images on the environment's draft copies of its own storage (class (iii) draft-stage form), so the check-wiki rendering does not hotlink the EN files.

**Verify.** `grep -n "local--code" candidate.txt` returns L2 and L7, both naming /2. `grep -n "\[\[code" candidate.txt` returns L75 and L91 in order. The DRAFT-HOST lines pair one-to-one with the original's file URLs in diff.md.

**Disposition.** Ledger PASS, row 31; class (iii) for the draft-stage forms.

## 4. Fonts and assets

**What.** One FONT-IMPORT / JPFONT-LOAD block (B26): candidate L110 carries two imports on one line, Song Myung from fonts.googleapis.com and Noto Serif JP (wght 700) from fonts.googleapis.com. The original imports Song Myung alone from googleapis (original L99). The production port had moved Song Myung to fonts.bunny.net (an AutoLocalize carry) and added the Noto Serif JP load; FIX4-REPOINT (443c608) reverted the Song Myung host to googleapis, leaving the JP load in place. ELAND_Nice_M is loaded by @font-face from cdn.jsdelivr.net (candidate L112–113), identical to the original's own load (original L101–102). Three JPFONT-STACK blocks (B31, B32, B38) add 'Noto Serif JP' to the serif stacks: candidate L156 and L171 (ELAND_Nice_M, 'Noto Serif JP', BauhausLTDemi, sans-serif) and candidate L270 ('Song Myung', 'Noto Serif JP', 'Nanum Gothic', serif).

**Why.** This is the theme's P5 item and its resolution. LOCALIZE-ROWS row 31 item (a) records the judgment call in full: font hosts outside the exception list, including the carried AutoLocalize bunny move; revert Song Myung to Google Fonts; rehost or drop ELAND_Nice_M. The ledger (c3) register records pattern 2 as FIXED for this theme via FIX4-REPOINT (KB-17) and P5 as DISPOSITIONED (class (ii) / KB-58). The bytes match the call on Song Myung exactly (443c608 changes that one host on that one line). On ELAND_Nice_M, neither rehost nor drop happened: the original's jsdelivr @font-face load is retained verbatim, and the P5 disposition is what covers it, a judgment-call-vs-bytes gap recorded in the Per-theme record. The stack additions are the P7 JP font-stack form: every first-named family is loaded (Song Myung and Noto Serif JP by import, ELAND_Nice_M by @font-face), so no named-not-loaded family arises; BauhausLTDemi is the original's own second stack entry, retained on both sides.

**Verify.** `git show 443c608 -- pages/theme:scheme-jp.txt` shows the single-line host revert. Candidate L110–113 against original L99–102 shows the added JP import and the unchanged @font-face. The stacks are candidate L156, L171, L270 against original L145, L160, L259.

**Disposition.** Pattern 2 FIXED (FIX4-REPOINT, KB-17) and P5 DISPOSITIONED (class (ii) / KB-58), ledger (c3); ledger PASS, row 31.

## 5. Header, sidebar, site furniture

**What.** Two CSS-BODY blocks (B36, B37) extend the sidebar block selectors with interwiki twins: #side-bar .side-block.media gains ", #interwiki .side-block.media" (candidate L256) and .resources likewise (candidate L260). One T7-CREDIT-CSS block (B70) appends four live [[module CSS]] blocks after the closing [[/iftags]] (candidate L1181–1211), all present since the canonical import (production-port supplements, not campaign wave edits). The first, commented "SCP-JP Wikidot Scheme header correction: wrap the masthead and separate the visible JP search control." (candidate L1182), restyles the mobile masthead and search box at max-width 767px and clips an extra div. The second, "navigation correction: keep decorative gears out of pointer hit tests and contain row endpoint submenus." (candidate L1192), sets pointer-events: none on the gear divs and contains the mobile submenus. The third, "scheme narrow header: shrink the fixed gear emblem clear of the wordmark and the top bar." (candidate L1203), shrinks the gear emblem at max-width 480px. The fourth is the genuine credit correction (candidate L1207–1211): its comment explains that the theme colors the credit glyph with the gold rate bar's text color (#6b5829) while the credit button keeps the credit module's dark-red background (#663333), leaving the glyph illegible (contrast 1.46), and its single rule restores the module's own glyph color (#fff6f0) on .rate-box-with-credit-button .creditButton a.fa-info only. The last module is left unclosed at end of file, the same Wikidot tolerance the sibling themes' originals show. The classifier's T7-CREDIT-CSS label names the whole appended batch for its fourth module; on bytes, one of the four is credit CSS and three are header/navigation corrections.

**Why.** The interwiki twins give the JP interwiki sidebar the same media/resources block styling as the local sidebar, which the original (whose environment has no JP interwiki) never needed. The tail modules target the exact failure shapes this theme's render record lists (mobile logo clipped, gold hamburger overlays body/rate, tagline word-split): they are the production port's corrections for the JP masthead, whose search control and labels differ from the EN one. Because they postdate the original and sit outside the gate as live modules, they apply on every page that includes the theme, which is the intent: the corrections are part of the theme's JP delivery, not of its documentation body.

**Verify.** Candidate L256 and L260 show the selector twins. Candidate L1180–1212 shows the two modules with their comments. `git log --all -S "Scheme header correction" -- pages/theme:scheme-jp.txt` returns only the import commit d727e92.

**Disposition.** Ledger PASS, row 31. The T7-CREDIT-CSS mislabel is a prose-vs-bytes discrepancy recorded here and in the batch report; the modules' content is header/navigation correction, adjudicated on its bytes.

## 6. Text translation

**What.** TRANSLATION-ANCHORED spans in 12 blocks, TRANS-UNANCHORED spans in 21 blocks, and COMMENT-TEXT spans in 17 blocks. The prose and sample body translate (including the sample apparatus: 評価 labels, 第99.99.ζ9-99巻 volume lines, marginal notes 傍注, contents lists). The CSS comments translate from both of the original's comment languages: English section markers (GEAR-SMALL → 小歯車, STICK → 棒, STEAM → 蒸気） and Korean (검색창 - SEARCH-BOX → 検索欄 - SEARCH-BOX, keeping the English gloss). The translation is the production form's, adopted with the page; the credit block's 2026 campaign fields are covered in section 1.

**Why.** Reader-visible text and maintainer-visible comments both localize (P10, KB-18); the comment translations matter for this theme because its CSS is organized by named sections (gears, sticks, steam) that a JP maintainer navigates by. The sample body's joke-serious apparatus （第99.99.ζ9-99巻） translates in form, keeping the original's numbering intact.

**Verify.** Read the pairs in diff.md; the comment pairs are visible at candidate L191 (SEARCH-BOX), L383 （小歯車）, L418 （中歯車）, L452 （大歯車）, L590 （棒）, L629 （棒2), L671 （蒸気） against their originals.

**Disposition.** T5 FINDINGS judged jointly with T4 (LOCALIZE-ROWS row 31), with 0 display-affecting findings. Ledger PASS, row 31.

## 7. Links

**What.** No link-specific signature fired. The candidate's outbound links are the credit source link (section 1) and the demonstration body's links, which keep the original's targets and forms. The URL changes in the file are the delivery, font, and own-file asset changes of sections 3 and 4.

**Why.** No prose link needed repointing: the theme's body links name the same pages on both sides, and the storage URLs are file loads, not links a reader follows.

**Verify.** Compare the bracket links in diff.md outside the delivery, credit, and CSS regions; they pair one-to-one.

**Disposition.** Ledger PASS, row 31; no link finding is recorded for this theme.

## 8. Structure

**What.** One EXHIBIT-RESTRUCTURE block (B2, the head frame: a mere repoint, the standing false fire) and five CSS-BODY blocks. B36/B37 are the interwiki selector twins (section 5). B47 and B68 are semicolon completions inside the payload (candidate L414: animation: spin 5s linear infinite; gains its semicolon; candidate L1081: color: #ba9e57; likewise), and B53 is a CSS comment translation (/* Firefox */ → /* Firefox用 */, candidate L492). No exhibit, module, or body section present in the original is absent from the candidate; the exhibit census pairs the sample body entire.

**Why.** The semicolon completions are production-port hygiene: a final declaration without a semicolon is valid CSS, but completing it removes a class of merge and minification accidents when the payload is handled by other tools. They change no computed value. The structural additions (interwiki twins, tail modules) are counted in section 5 with their grounds.

**Verify.** The exhibit census is diff.md read end to end; the semicolon pairs are candidate L414 and L1081 against original L403 and L1070.

**Disposition.** Ledger PASS, row 31; no structural finding is recorded for this theme.

## 9. Formatting only

**What.** No WS-ONLY blocks fired for this theme: the classifier found no whitespace-only change blocks across 70 blocks, because the production port's text changes are substantive at every touched line and the campaign's trailing-whitespace wave (3010ef7, which normalized sibling themes) does not touch this file.

**Why.** The section is present to record the ground of the negative: formatting-only mass is genuinely absent here, not merely unlabeled; the residue blocks that might have hidden it are all resolved as translations in the Appendix.

**Verify.** The class summary in classification.json lists no WS-ONLY label; `git log --oneline -- pages/theme:scheme-jp.txt` shows no whitespace-wave commit for this file.

**Disposition.** None required. Ledger PASS, row 31.

## 10. Porter annotations

**What.** No ANNOTATION signature fired. Four porter-voiced texts exist, all production-inherited and all riding inside the tail supplement modules of section 5: the English comments at candidate L1182 (header correction), L1192 (navigation correction), L1203 (narrow header), and L1208 (credit correction). No other comment in the candidate lacks a counterpart in the original.

**Why.** Porter annotations are listed so they are never mistaken for original content (R2). These four name themselves as SCP-JP corrections and sit directly above the rules they explain, so they inform rather than mislead; they are recorded here because the classifier's silence would otherwise leave them undocumented.

**Verify.** Candidate L1181–1211 shows all four comments above their modules. `grep -n "SCP-JP Wikidot" candidate.txt` returns exactly these four lines.

**Disposition.** Four inherited porter comments, recorded. Ledger PASS, row 31.

## 11. Dispositions and exceptions

**What.** The dispositioned and excepted items for this theme: (1) P5 DISPOSITIONED (ledger (c3), class (ii) / KB-58): the font hosts outside the exception list, as resolved in section 4. (2) The bare Rate beside the credit block is the labelled paired Rate exhibits exception (ledger (c2) preamble item 6), which names scheme explicitly. (3) The T1 residue: pseudo-ref×14 and hotlink×2 within 16 errors / 1 warn / 7 infos, the standing classes of register (c1); the pseudo-references are the checker's name for the theme's own file and code references inside its exhibits, and the hotlinks are the P5 font hosts counted by the checker. (4) The render record: T2 incomplete on both pages (exit 2 ×6, webkit networkidle timeout) is a coverage caveat, not a defect; the listed findings (768px notice clipped over sidebar, mobile logo clipped, tagline/footer word-split, code block clipped, gold hamburger overlay, 884px@768) are the narrow-width family dispositioned for the cohort in FIX3-S2EN §6.5 / KB-35, and the sample credit-modal errors are the preview-form disposition (credit:start-preview has no modal mechanism, GOSIGN-TESTS T2 amendment).

**Why.** Each disposition is re-derivable from this package: the font lines are candidate L110–113; the Rate and its labels are candidate L28 and the B5 pair; the T1 counts are T1-ROWS row 31; the render text is RENDER-ROWS-1 (RENDER-C row 31).

**Verify.** The cited lines and rows. The exception's theme list is in the ledger (c2) preamble.

**Disposition.** P5 DISPOSITIONED and patterns 2 and 3 FIXED in the ledger (c3) register; ledger PASS, row 31, with no section (e) items and no FIX5 re-judgement.

## 12. Verification

**What.** The checks behind this package, each re-runnable from the repo: T1 as recorded (exit 1, 16/1/7, T1-ROWS row 31); T2/T3 as recorded (RENDER-ROWS-1, RENDER-C row 31, with the T2-incomplete caveat); the wave diffs for 8dcac74, b816e10, 1869877, 443c608, and b5cb724 read against this file; the FIX-CODEADDR audit consulted (this theme absent from its mismatch and unresolved lists) and the code-block census re-derived (section 3); CSS brace balance by depth (both files end at depth 0 with no negative dip); and `python3 review/build_review.py --check`, which passes over this package (candidate.txt byte-identical to the canonical file; original.txt hash equal to the sources.tsv value).

**Why.** Every factual claim above names the lines, the commit, or the register row that decides it, so a reviewer can re-derive the package without trusting the writer.

**Disposition.** Package complete against the ledger PASS, row 31 (stamp STALE for the post-verdict sweep line), with no defect flag.

## Per-theme record

LOCALIZE-ROWS row 31 (source LOCALIZE-B) records two items: (a) P5, font hosts outside the exception list including the carried AutoLocalize bunny move, with the judgment call quoted in section 4; (b) P3, six missing credit fields. The ledger (c3) register records pattern 2 FIXED (FIX4-REPOINT) and pattern 3 FIXED for this theme, and P5 DISPOSITIONED (class (ii) / KB-58). T1-ROWS row 31 records exit 1, 16 errors / 1 warn / 7 infos (pseudo-ref×14, hotlink×2). RENDER-ROWS-1 (RENDER-C row 31) records the combined T2/T3 FINDINGS quoted in the Status table. Three prose-vs-bytes discrepancies are recorded: (1) the skeleton's INFO-DEL lead claims the info pair was removed; the pair is retained and repointed (section 1). (2) The skeleton's T7-CREDIT-CSS label on B70 names the whole appended batch as credit-module CSS; on bytes only the fourth of the four tail modules is credit CSS, the other three being header and navigation corrections (section 5). (3) The localize judgment call says "rehost or drop ELAND_Nice_M"; the bytes keep the original's jsdelivr @font-face load verbatim, and the P5 disposition, not the call's either/or, is what the file actually rests on (section 4).

## Change set outside the two diffed files

The Phase 17 migration deliverable, pages/phase17-diff-scheme-jp.txt in this repo, is the change set that carries this candidate's form onto the production page theme:scheme; it is part of the same canonical record. The wave commits b816e10, 1869877, and b5cb724 are population commits; their shares in this file are the lines cited in sections 1 and 2.

## Multi-wave provenance

| Wave | Commit | Change to this file |
|---|---|---|
| Canonical import (production form adopted) | d727e92 | The candidate as the production page stands: translation, info pair repointed, Rate kept, Noto Serif JP load added, Song Myung on bunny.net (AutoLocalize carry), interwiki selector twins, tail header/navigation correction modules |
| Phase 17 | 8dcac74 | Credit include pair added with 初訳時参照リビジョン 30 and 元記事リンク (4 lines) |
| T1 credit completion | b816e10 | The six missing TASL fields added to the credit block |
| FIX-CREDIT-D | 1869877 | 翻訳責任者 SCP-JP → AI (1 line) |
| FIX4-REPOINT | 443c608 | Song Myung import reverted fonts.bunny.net → fonts.googleapis.com (1 line) |
| Usage-example sweep (post-verdict) | b5cb724 | Usage exhibit renamed :scp-jp:theme:scheme → :scp-jp:theme:scheme-jp; the stamp's STALE state dates from this commit |

## Appendix — residue blocks

All 11 residue blocks are translations whose lines defeat anchor matching; none hides a mechanism change.

- R1 = B5 (original L14–15 → candidate L25–26): the exhibit label "**Rating: @@" → "**評価: @@" beside the kept Rate module (section 2).
- R2 = B18 (original L53–54 → candidate L64–65): the sample line "**Volume 99.99.ζ9-99**" → "**第99.99.ζ9-99巻**".
- R3 = B21 (original L67–68 → candidate L78–79): the sample marginal note "##red|b.## marginal note 2" → "##red|b.## 傍注2".
- R4 = B22 (original L70–73 → candidate L81–84): the sample volume and contents lines ("**Volume XX.XX.XX-XX**", "**1.** content 1", "**2.** content 2" → 第XX.XX.XX-XX巻， 内容1, 内容2).
- R5 = B33 (original L179–180 → candidate L190–191): the CSS comment "/* ---- 검색창 - SEARCH-BOX ---- */" → "/* ---- 検索欄 - SEARCH-BOX ---- */" (section 6).
- R6–R11 = B45, B48, B50, B58, B60, B62 (original L371–372, L406–407, L440–441, L578–579, L617–618, L659–660 → candidate L382–383, L417–418, L451–452, L589–590, L628–629, L670–671): the CSS section comments GEAR-SMALL → 小歯車, GEAR-MEDIUM → 中歯車, GEAR-LARGE → 大歯車, STICK → 棒, STICK-2 → 棒2, STEAM → 蒸気 (section 6).

## License and attribution

- **Title:** Scheme Theme
- **Author:** shaftmetal, thd-glasses, Denevola, Fluxman
- **Source:** https://scp-wiki.wikidot.com/theme:scheme — revision 30 (revision date 2023-07-23 15:04:30)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
