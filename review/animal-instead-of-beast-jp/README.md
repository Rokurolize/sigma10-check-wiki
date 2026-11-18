# Review package — theme:animal-instead-of-beast-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:animal-instead-of-beast-jp — origin KO, population #251 [GOSIGN2-LEDGER (b) row 251]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now ca7918c69dfb93606a215b141359af12facdb026bd8292120ed90c1d7d625ff1); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 4 errors / 1 warn / 1 info (pseudo-ref×4); standing classes dispositioned in register c1 [T1-ROWS row 234; GOSIGN2-LEDGER (b) row 251]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — runtime-hotlink site-theme chain + scpko.wdfiles.com / scpko.wikidot.com on both pages; sample credit-modal (preview-form) + 884px@768 overflow; T3 header wordmark faint gray-on-white (machine contrast 1.03). [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-H (KO1))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 250, source LOCALIZE-S2-F]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 250]
- FIX5 re-judgement: items 101 (class C) FIXED, 102 (class E) DISPOSITIONED — FIX5-INFO, commit 9a1c86a: info-module / duplicate credit residue removed FIX5-INFO (no edit): candidate and original value sets byte-identical (--color-1: #F9FCF9 wordmark on both); live probe 2026-11-17: original logo.png HTTP 200 (image/png, 305,687 B), candidate draft-host logo.png HTTP 404; cause is the deferred draft-bucket asset (AGENTS.md ss4/ss6), not a colour binding [GOSIGN2-LEDGER-SUPPLEMENT (a) items 101–102]
- Computed against: canonical commit fa9e84aae02210b174c0480db82e68c1846aeef4; candidate file pages/theme:animal-instead-of-beast-jp.txt sha256:ca7918c69dfb93606a215b141359af12facdb026bd8292120ed90c1d7d625ff1; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (R-disp-2 lane, 2026-11-17)
Candidate: review/animal-instead-of-beast-jp/candidate.txt (sha256 557e67d9c94c85a15ed1d8164e0e3c86c17b64b43db712532ffeae17c471fad0)
Original: theme:animal-instead-of-beast — scpko, revision 5 (sha256 13f26bb59d02bceff8b8e82e39cfe6e2c167ecd6bc3d659c8db909606d44bd8c)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (generated stamp) | Notes |
|---|---|---|
| T1 source check | FINDINGS (classified) | 4 errors / 1 warn / 1 info, all pseudo-ref; standing classes dispositioned in register (c1) |
| T2/T3 render | FINDINGS | Wordmark contrast item is FIX5 item 102, re-derived below; the rest dispositioned in (c2) |
| T4/T5 localize/translation | FINDINGS | 3 display-affecting findings in LOCALIZE-S2-F; the credit-field item is FIX5 item 101 |
| FIX5 item 101 [C] | FIXED (FIX5-INFO, 9a1c86a) | Re-derived on this package's bytes in the per-theme record |
| FIX5 item 102 [E] | DISPOSITIONED (FIX5-INFO, no edit) | Re-derived on this package's bytes in the per-theme record; ground holds |

The stamp reads STALE because the candidate file changed after the 435a6bb-era verdict (the stamp names canonical b5cb724 as its computed-against commit). Both FIX5 re-derivations in the per-theme record were performed on the current candidate bytes in this package, so they hold for the file as it stands regardless of the stamp.

## Provenance

| Side | Source | Revision | SHA-256 |
|---|---|---|---|
| Original | theme:animal-instead-of-beast on scpko (mirror store: orig-animal-instead-of-beast-rev5.txt) | rev 5 | 13f26bb59d02bceff8b8e82e39cfe6e2c167ecd6bc3d659c8db909606d44bd8c |
| Candidate | pages/theme:animal-instead-of-beast-jp.txt (canonical) | — | 557e67d9c94c85a15ed1d8164e0e3c86c17b64b43db712532ffeae17c471fad0 |

## Summary

A Korean standalone theme (no base theme; one inline head module importing its own code block, one frame, one gated body). The port keeps the delivery shape, swaps the credit furniture to the JP preview form with a full TASL record, localizes the tag gate and all prose, repoints its own assets to the draft host, layers the live KO original under its own CSS under the campaign's KB-14 contract, and adds a license box the original does not carry. The delivered CSS is value-identical to the original's (measured below); that identity is the ground of item 102's disposition. Four defect flags are recorded in the per-theme record: both TASL carriers leave the author as a pointer although the original names c_bonefish; the credit title field diverges from the candidate's own body form; a visited-link exhibit still names the plain (non-JP) page; and the JP font supplement loads two faces no stack in the file names.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 5 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| INFO-DEL | 1 |
| JPFONT-LOAD | 1 |
| LICENSE-BOX | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 12 |
| TRANSLATION-ANCHORED | 4 |
| WS-ONLY | 17 |

Counts: 37 blocks, 31 specific, 6 heuristic, 0 residue, 0 skipped (comment text).

## 0. Header / provenance

- Route: derived from the original at the reference revision (rev 5, mirror hash above equals the sources.tsv row). The candidate's own banner note (candidate L76-78) and credit field 初訳時参照リビジョン (L18) both record rev 5 on scpko.
- Topology: no relocation. Both sides carry a 3-line head module-css importing the page's own code block 1, then one [[code type="css"]] block (original L60-615, candidate L72-635). The classifier reports no moves and external own delivery on both sides.

## 1. Credit and attribution

- What: the original's CN-style furniture is absent here; the KO original carries a bare Rate exhibit (orig L14-17), an empty info-module pair (orig L19-23), and credit prose naming the author (orig L25). The candidate carries the JP preview credit block (cand L11-20, B2/B5/B6 spans) with the eight TASL fields, a translated credit prose line (cand L33), and an added license box (cand L637-642, B37) the original does not carry.
- BARE-RATE-DEL (B5): the bare [[module Rate]] exhibit is removed; the preview credit module is already rate-bearing (KB-09). The two exhibit labels remain as plain text (cand L29, L31).
- INFO-DEL (B6): the [[include info:start]] / [[include info:end]] pair is removed; this is FIX5 item 101, re-derived in the per-theme record.
- LICENSE-BOX (B37): the license box is an addition (T4 supplement; the classifier notes the original carried none). Its source note (cand L640) defers image/font provenance to the original's record and to posting-stage confirmation.
- Why: the preview credit form is the JP environment's settled credit carrier (P3/T1); the license box is the population's TASL record for a theme whose original has none (KB-63/KB-60).
- Verify: grep the candidate for `info:start`, `info:end`, `[[module Rate]]` — all counts are 0 (run 2026-11-17). Read cand L11-20 against orig L14-25.
- Disposition: ledger (c3) LOCALIZE-S2-F P3 credit fields FIXED, closing as FIX5 item 101 [GOSIGN2-LEDGER (c3); GOSIGN2-LEDGER-SUPPLEMENT (a) item 101]. The author-field defect inside this block is flagged in the per-theme record (flag A1); it does not reopen item 101, whose charge was the duplicate rating area.

## 2. Includes and components

- What: the tag gate localizes (orig L10 [[iftags +테마]] → cand L9 [[iftags +テーマ]], inside B2's span; B3's pairing of the gate line with the translated heading at cand L27 is a differ seam, resolved in the appendix). The gate spans the whole body on both sides (orig L10-617, cand L9-644). The head frame include repoints :scp-wiki: → :scp-jp: (B2, INCLUDE-REPOINT). The install example (B7) is the escaped include repointed to the candidate itself: orig L28 `@@[[include :scpko:theme:animal-instead-of-beast]]@@` → cand L36 `@@[[include :scp-jp:theme:animal-instead-of-beast-jp]]@@` (COMPONENT-SWAP / ESCAPED-INCLUDE labels on B7).
- Frame layering: the candidate carries two interwiki-style frames. Cand L5-8 (priority=2) delivers the candidate's own code block 1 from the draft host; cand L22-25 (priority=1) delivers the live KO original's code block 1. FIX4-IWB §1 records the history: both frames originally sat at priority=1 (KB-07c duplicate priority, FIXED by raising the candidate's own layer to 2); the priority=1 layer pointing at the live original is the KB-14 A13-6 live-original layering, its target left byte-unchanged by a coordinator-level contract (SWEEP-A2 L95), not a per-theme choice.
- Why: tag names are environment-local (P2/T2, KB-08); the frame stack is the Sigma-10 delivery form; the layering contract keeps the original's live CSS under the port's.
- Verify: read cand L5-25 against orig L5-8; FIX4-IWB's checker row for this theme is 4/1/1 before and after, matching the T1 stamp baseline.
- Disposition: ledger (c3) P6 FIXED (frame waves) [GOSIGN2-LEDGER (c3)]; the FIX4-IWB fix is the landing of that closure.

## 3. Delivery and code loading

- What: self-delivery is the head module import (cand L2, B1: orig L2's scpko local--code address → the candidate's own /1 on the draft host) plus the priority=2 frame (cand L7). Code census: exactly one code block per side ([[code type="css"]], orig L60, cand L72), so the /1 address names the stylesheet block itself (FIX-CODEADDR-conformant; no repoint owed). The candidate additionally wraps the code block in a [[collapsible]] (cand L71, L636; B15/B36 seams) where the original presents it bare — the population's standard source-code presentation.
- Draft-host references (DRAFT-HOST ×5): cand L2 (own code import), L7 (frame theme=), L41 (image-block exhibit asset), L106 (background.png), L112 (logo.png).
- Why: a theme page delivers its own code block by URL in this environment (P4/T9); the draft host is the draft-stage form of the candidate's own files (KB-41, class (iii)), rewritten at posting (class (ii)).
- Verify: grep -c '[[code' on both files returns 1 and 1 (run 2026-11-17); resolve cand L2 and L7 to the block at cand L72-635.
- Disposition: ledger (c3) P4 DISPOSITIONED (delivery class (ii): original-state CDN delivery) [GOSIGN2-LEDGER (c3)]; the draft-host form is recorded, not fixed, at this stage.

## 4. Fonts and assets

- What: the original loads no fonts and declares no font-family anywhere (grep over the whole file: 0). The candidate adds two Google Fonts imports at the head of its code block (cand L73-74, B16, JPFONT-LOAD): Noto Sans JP (400;700) and Noto Serif JP (400;700), under the porter comment at cand L79. No stack or variable in the candidate names either face — the file still declares zero font-family properties, exactly like the original.
- Why: the JP supplement's purpose is to give Japanese text a JP typeface (P7/T5, KB-16); here the theme defines no stacks of its own, so the loads have no in-file consumer.
- Verify: grep -n 'font-family' on both files returns nothing; grep -n 'Noto' on the candidate returns only L73-74 (run 2026-11-17).
- Disposition: no ledger item covers this supplement. It is recorded as flag A4 in the per-theme record for adjudication (the population has both outcomes on record: stack alignment in travellers-book, a recorded observation in share-future-community).

## 5. Header, sidebar, site furniture

- What: no change block touches the header or sidebar rules. That absence is load-bearing: the header rules are byte-identical to the original's, which is the ground of item 102's disposition (measured in the per-theme record: the wordmark rule at orig L107-114 / cand L127-134, the #header background at orig L90-96 / cand L110-116, the :root palette at orig L72-82 / cand L92-102).
- Why: the port changes delivery and language, not this theme's furniture.
- Verify: the normalized code-body comparison in the per-theme record (item 102) covers every header rule.
- Disposition: the T3 wordmark item is FIX5 item 102, DISPOSITIONED [GOSIGN2-LEDGER-SUPPLEMENT (a) item 102].

## 6. Text translation

- What: all reader-visible Korean prose is translated in place: the heading (cand L27), the two exhibit labels (cand L29, L31), the credit prose (cand L33), the install instruction (cand L35), the section headings (cand L39, L43-48, L65, L69), the sample text (cand L54: the keyboard-mash placeholder ㅁㄴㅇㄹ becomes サンプルテキスト), the link exhibits (cand L56-57), and the footnote text (cand L59: 똑똑 → こんこん, the knock-knock onomatopoeia localized). TRANSLATION-ANCHORED ×4 blocks pair one-to-one (B8, B10, B14 + the anchored pair inside B9); the TRANS-UNANCHORED blocks (B4, B11, B12, B13, B15) are the same translations at lines whose shape changed, resolved in the appendix.
- Why: reader-visible text localizes (P10, KB-18); anchors confirm the pairings where they survive.
- Verify: read the pairs in diff.md hunks 1-3; every Korean prose line in the original has a Japanese counterpart at the aligned position.
- Disposition: T4/T5 FINDINGS with 3 display-affecting findings [LOCALIZE-ROWS row 250, source LOCALIZE-S2-F]; the credit-field finding among them closed as item 101.

## 7. Links

- What: no LINK-REPOINT signature fired, but the link exhibits carry one defect: cand L57's visited-link exhibit names the plain form [[[theme:animal-instead-of-beast|訪問済みリンク]]], a page that will not exist on the JP wiki (the candidate is theme:animal-instead-of-beast-jp). The unvisited half of the exhibit is an anchor dummy ([# 未訪問リンク]) on both sides. The source link in the credit block (cand L19) names the recorded host scpko.wikidot.com, matching sources.tsv — no host defect.
- Why: a styling exhibit whose target is a nonexistent page cannot show the visited state it demonstrates; the population's sweep repaired this exact shape elsewhere (greyday, canonical 9e0c700; king-s-palace, canonical f5acc90 — a single -jp insertion in each).
- Verify: read cand L56-57 against orig L48-49; the target is byte-identical to the original's, which resolved on scpko and does not resolve on scp-jp.
- Disposition: no ledger item covers it (it postdates the sweep's classes as a survivor of the same shape). Flagged as A3 in the per-theme record; the candidate is not edited by this lane.

## 8. Structure

- What: EXHIBIT-RESTRUCTURE fired twice, both times as seams rather than exhibit losses. B2 (orig L5 → cand L5-22) is the head cluster where the credit block and the second frame were added around the surviving first frame. B9 (orig L33 → cand L41) is the image-block exhibit whose only change is its asset host repoint to the draft host; the exhibit stands with caption and width unchanged. Exhibit census: every original exhibit (headings, image-block, tabview with footnote, blockquote link pair, code block) is present in the candidate at the aligned position. CSS-BODY (B36) is the code-close seam at the tail: the candidate's [[/code]] lands two lines later because the license box follows it in the body channel; the normalized comparison in the per-theme record shows no CSS content change behind it.
- Why: a sanctioned replacement and a silent deletion share a diff shape (R3), so each instance is adjudicated against the mirror; here the census decides both.
- Verify: the exhibit census above, read off diff.md; the item-102 normalized comparison for B36.
- Disposition: no exhibit disposition is recorded against this theme in the ledger; none is needed — nothing was dropped.

## 9. Formatting only

- WS-ONLY ×17 blocks: trailing spaces added to blank lines inside the code body (e.g. cand L126, L135). No re-indentation blocks. These pair with the value-identity measurement: stripped of trailing whitespace, the code bodies are identical (per-theme record, item 102).

## 10. Porter annotations

- The skeleton reports none because no ANNOTATION signature fired, but three porter texts ride inside other blocks, checked explicitly:
  - The ported banner note (cand L76-78, inside B16): "짐승 대신 동물 / Animal Instead of Beast — Ported for SCP-JP (theme:animal-instead-of-beast rev 5 on scpko)." Its provenance claim matches sources.tsv and the mirror hash.
  - The font comment (cand L79): "日本語フォント (JP localization)" over the supplement imports; the supplement itself is flag A4.
  - The license-box source note (cand L640, inside B37): states that image/font provenance follows the original's record, that KO attachments and webfonts are re-hosted or replaced with Google Fonts equivalents, and that images without a license statement in the original need author confirmation before posting. The asset clause describes the posting-stage end state; at draft stage the two attachments still resolve to the draft host and 404 there (item 102's probes), which is the deferred state dispositioned in section 11 — the note is a posting instruction, not a claim about the draft bytes.
- The original's own banner (Created by c_bonefish / Base Code by Denevola / Logo by DEFECT15 / CC BY-SA 3.0) is carried verbatim at cand L81-90.

## 11. Dispositions and exceptions

- Item 102 (wordmark contrast): DISPOSITIONED — re-derived in the per-theme record.
- (c2) RENDER-S2-H (KO1): the runtime-hotlink site-theme chain and scpko hosts on both pages, DISPOSITIONED as class (ii) posting matter (KB-41/KB-54); the sample credit-modal errors, DISPOSITIONED as the preview form's property (KB-32); the 884px@768 overflow, DISPOSITIONED (KB-33/KB-34) [GOSIGN2-LEDGER (c2)].
- (c3) P4: DISPOSITIONED, delivery class (ii) (section 3). P9: DISPOSITIONED under ruling 2 [GOSIGN2-LEDGER (c3)].
- No HTTP-KEPT instance is derived for this package (derived_presence is empty); the candidate's two asset URLs are draft-host repoints, not kept hotlinks.

## 12. Verification

- T1: the stamp's baseline stands (exit 1, 4/1/1, pseudo-ref ×4); FIX4-IWB re-ran the checker on this file after its frame fix with 0 new errors, and FIX5-INFO's gate for item 101 likewise (4/1/1 before and after).
- T2/T3: FINDINGS as stamped; the wordmark item is item 102 below. T4 follow-up: the reference revision is the upstream latest (rev 5; sources.tsv carries no supersession note for this theme, and none is owed).
- Lane re-runs (2026-11-17, this package's bytes): the item-101 grep census, the item-102 value-set comparison and probes, the code census, and the brace-depth scan — all recorded in the per-theme record. Package acceptance (build_review.py --check, classify freshness, byte-identity of both files) is recorded in the batch report BATCH-RDISP2.md.

## Per-theme record — FIX5 items re-derived

### Item 101 [C] — FIXED (FIX5-INFO, commit 9a1c86a)

- The charge: the bare [[include info:start]] / [[include info:end]] pair left beside the credit module rendered a second rating area on the port (ledger (c3) P3 credit-fields charge).
- The fix, verified in the canonical history: commit 9a1c86a touches this file with exactly 3 deletions — the two info includes and one blank line (git show, run 2026-11-17).
- The current bytes: grep counts on candidate.txt are 0 for info:start and 0 for info:end; the exhibit labels that headed the pair remain as plain text (cand L29, L31). The original's pair stands at orig L22-23, and its first exhibit's bare Rate (orig L16) is likewise absent from the candidate (count 0), removed under the standing KB-09 class.
- Verdict: the FIXED closure holds on the current bytes.

### Item 102 [E] — DISPOSITIONED (FIX5-INFO, no edit)

- The charge: the header wordmark renders faint gray-on-white (machine contrast 1.03), charged as the KB-28 mechanism — a variable-binding defect whose fix would be correcting the binding.
- The disposition's ground: the candidate and the original hold byte-identical value sets; the faintness is caused by the candidate's header background artwork 404ing on the draft host, a deferred draft-bucket asset (AGENTS.md §4/§6), not by any colour binding.
- Re-measurement on this package's bytes (2026-11-17):
  - Custom properties: the sorted definition sets are identical on both sides (7 definitions each, diff empty). --color-1: #F9FCF9 at orig L73 and cand L93.
  - Wordmark rule: #header h1 a::before at orig L107-114 and cand L127-134; content: "SCP 재단 초상동물학부" (orig L108 / cand L128) and color: var(--color-1) (orig L109 / cand L129) are byte-identical.
  - Whole-CSS comparison: after removing the candidate's added head lines (the two font imports and the banner-note fences) and mapping its two draft-host asset URLs back to the original host form, the candidate's code body is byte-identical to the original's — no rule and no value anywhere in the delivered CSS differs. Brace depth ends at 0 and never goes negative on either side.
  - Probes (one GET each, 2026-11-17): the original's https://scpko.wikidot.com/local--files/theme:animal-instead-of-beast/logo.png returns HTTP 200, image/png, 305,687 B — the FIX5 probe's exact figures. The candidate's draft-host logo.png returns HTTP 404. The second repointed asset behaves the same way: original background.png 200 (27,993 B), draft-host background.png 404.
- Second-reviewer walk: the ground is stated in terms a reader can check from this package alone for the identity half (diff the two code bodies; the only deltas are the head additions and the two asset hosts) and with two fetches for the asset half, which this lane re-ran with the same outcome as FIX5's probe. The KB-28 premise — a binding the port got wrong — is absent: there is no differing binding to correct, so any colour edit would have diverged the port from the original to mask a missing file. The disposition holds.

### Defect flags (candidate not edited by this lane)

- A1 — credit author is a pointer in both TASL carriers although the original names the author. Credit field (cand L16): 著作権者： 原語版ページの作成者に同じ（scpko の theme:animal-instead-of-beast). License-box author (cand L638): author=scpko theme:animal-instead-of-beast の作者. The original names c_bonefish in its prose (orig L25, [[*user c_bonefish]]) and its banner (orig L65, "Created by c_bonefish"); the candidate's own prose (cand L33) and banner (cand L85) name him too. This is the pointer family repaired in sci-fi, the-track-changers, and plugsoft: the name exists in the record and in the same file, and both carriers decline to state it.
- A2 — credit title field diverges from the candidate's own body form. Title field (cand L12): 獣ではなく動物 テーマ. The candidate's heading (cand L27) and prose (cand L33) both use 獣のかわりに動物 CSSテーマ as the theme's Japanese name. The steam-guide and voyager repairs settled that the title field follows the page's own Japanese form.
- A3 — visited-link exhibit names the plain form (cand L57; section 7).
- A4 — load-only JP font supplement (cand L73-74; section 4), recorded for adjudication.

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:animal-instead-of-beast-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP2, landing `fa9e84a` (report `R/review-scout/FIX-RDISP2.md`).** Four candidate repairs (as-built 4 substitutions + 4 deletions), all postdating this package's build at `b5cb724`.
- **A1 — credit pointer names nobody.** The original's prose (L25) and banner (L65) name c_bonefish. Credit field (as-built L16) `原語版ページの作成者に同じ（scpko の theme:animal-instead-of-beast）` → `**著作権者:** [[*user c_bonefish]]`; license-box author (L638, now L634) `|author=scpko theme:animal-instead-of-beast の作者]]` → `|author=c_bonefish]]`.
- **A2 — credit title field.** `獣ではなく動物 テーマ` → `獣のかわりに動物 CSSテーマ` at L12, the form the candidate's own body heading (L27) and prose (L33) use.
- **A3 — visited-link exhibit.** L57 `[[[theme:animal-instead-of-beast|訪問済みリンク]]]` → `[[[theme:animal-instead-of-beast-jp|訪問済みリンク]]]`, a single `-jp` insertion (greyday `9e0c700` / king-s-palace `f5acc90` shape).
- **A4 — load-only JP font supplement removed.** Census of the whole delivery chain found the two @imports (`Noto Sans JP`, `Noto Serif JP`, as-built L73–74) had no consumer: zero `font-family` declarations, zero font shorthands, no font-name custom property in the candidate or the original. The two @import lines, their separating blank line, and the orphaned `/* 日本語フォント (JP localization) */` annotation were removed, so the code block again opens with the ported banner comment.
Checker per the report: plain error 4 / warn 0 / info 1 and links error 4 / warn 1 / info 1 before and after; all errors class (iii) pseudo-refs, class (i) 0; the links warn's target changed from the plain name (a page that will never exist on scp-jp) to the candidate's own `-jp` name (a not-yet-posted self-reference that resolves at posting).

## Appendix — residue blocks

All six heuristic blocks are translation or seam mass; each is assigned here. No block is left unresolved, and no new signature is proposed from this package alone (the load-only supplement shape in flag A4 is proposed in the batch report, where the population evidence sits).

- R1 — B4 (orig L12 → cand L29): the heading line and the first exhibit label pair across the head restructure; both sides are the section-6 translations (heading at cand L27, label at cand L29). Assigned to section 6.
- R2 — B11 (orig L46 → cand L54): the tab exhibit's placeholder text, keyboard-mash Korean (ㅁㄴㅇㄹ) rendered as サンプルテキスト. Assigned to section 6.
- R3 — B12 (orig L49 → cand L57): the blockquote link-pair exhibit, translated; its visited-link target is flag A3. Assigned to sections 6 and 7.
- R4 — B13 (orig L51 → cand L59): the footnote exhibit line, translated including the onomatopoeia. Neither side carries a [[footnoteblock]] (grep count 0 on both), so the live footnote has the same (absent) apparatus on both sides — parity, no flag. Assigned to section 6.
- R5 — B15 (orig L60 → cand L68-71): the seam where the candidate adds the [[collapsible]] wrapper and the ソースコード heading above the code block. Assigned to section 3.
- R6 — B36 (orig L614 → cand L634-635): the code-close seam (CSS-BODY primary); no CSS content changes behind it, per the item-102 comparison. Assigned to section 8.

## License and attribution

- **Title:** 짐승 대신 동물 CSS 테마
- **Author:** c_bonefish
- **Source:** https://scpko.wikidot.com/theme:animal-instead-of-beast — revision 5
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
