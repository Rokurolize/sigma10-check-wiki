# Review package — theme:scpedia-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:scpedia-jp — origin EN, population #34 [GOSIGN2-LEDGER (b) row 34]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 0ed4133bccf6e7d5412ae4f4870360c19ef1de643bfbf8520b6976331c847801); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 2 warns / 2 infos (hotlink×3, pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 34; GOSIGN2-LEDGER (b) row 34]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page body empty (tag gate `[[iftags +テーマ]]`, possible stale-cache, not a defect), SCPedia fixed-width EN wordmark clips at ≤768 both engines, notice/sidebar/code overflow, sample credit-modal; T2 sample exit 2 retried once. [RENDER-ROWS-1 (RENDER-D row 34)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-D row 34)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 34, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 34]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 34]
- Computed against: canonical commit d554544b88a5b14936b0f0e67c10361c79179ad3; candidate file pages/theme:scpedia-jp.txt sha256:0ed4133bccf6e7d5412ae4f4870360c19ef1de643bfbf8520b6976331c847801; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/scpedia-jp/candidate.txt (sha256 38c3e0dc6cee775650bbeda76147a742d3dbefe275f750df06d7acab12c1dda6)
Original: theme:scpedia — scp-wiki, revision 57 (sha256 16d11d45b7d2fba1d3430c864c3a51fb36c8255fb529af23dc9cfc0547cc074f)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.
- Provenance route: adopted from the production JP counterpart (kind K6 in review/sources.tsv). The production page theme:scpedia exists on scp-jp; the campaign's migration deliverable for it is pages/phase17-diff-scpedia-jp.txt from Phase 17, and sources.tsv records the production page as matching the reference revision (production drift 一致）. The candidate in this repo is that production form as imported in commit d727e92, plus seven campaign wave edits: the reconcile escaping (ffad285), the dead-image-reference repair (4b52123), the Phase 17 credit frame (8dcac74), the T1 credit-field completion (b816e10), the FIX-CREDIT-D commit (1869877, which also adds the missing interwiki-style frame and repairs a cross-theme link), the FIX4-REPOINT font-host revert (443c608), and the post-verdict usage-example sweep (b5cb724). The sweep postdates the FIX5 verdict head, so the generated stamp above reads STALE; the verdict lines under it describe the pre-sweep file, and the only post-verdict change is the sweep's single usage line.

## Status

| Check | Verdict | Source |
|---|---|---|
| Overall | STALE (stamp) — candidate changed after the verdict; verdicts below describe the pre-change file | GOSIGN2-LEDGER (b) row 34, stamp regenerated at b5cb724 |
| T1 source check | FINDINGS (classified) — exit 1, 5 errors / 2 warns / 2 infos (hotlink×3, pseudo-ref×2) | T1-ROWS row 34 |
| T2/T3 render | FINDINGS — page body empty (tag gate, possible stale-cache, not a defect); SCPedia fixed-width EN wordmark clips at ≤768 both engines; notice/sidebar/code overflow; sample credit-modal; T2 sample exit 2 retried once | RENDER-ROWS-1 (RENDER-D row 34) |
| T4 localize patterns | FINDINGS — 2 display-affecting findings (both P5) | LOCALIZE-ROWS row 34 (LOCALIZE-B) |
| T5 translation text | FINDINGS — judged jointly with T4 by the source report | LOCALIZE-ROWS row 34 |
| FIX5 re-judgement | none — no OPEN items at the ledger determination | GOSIGN2-LEDGER (b) row 34 |

## Provenance

| Side | Identity |
|---|---|
| Original | theme:scpedia, scp-wiki, revision 57; mirror class FETCH-REGEN; sha256 16d11d45b7d2fba1d3430c864c3a51fb36c8255fb529af23dc9cfc0547cc074f (review/sources.tsv) |
| Candidate | pages/theme:scpedia-jp.txt in this repo; sha256 38c3e0dc6cee775650bbeda76147a742d3dbefe275f750df06d7acab12c1dda6 (stamp, computed against canonical commit b5cb724) |
| Production counterpart | theme:scpedia on scp-jp (kind K6); migration deliverable pages/phase17-diff-scpedia-jp.txt |

## Summary

SCPedia is a Wikipedia-skin theme: one CSS payload delivered from a tail module, a serif Linux Libertine face for headings, Roboto for UI text, and a demonstration body built around a wikibox exhibit. Its port history is the most wave-dense in this batch. The production form arrived with the Roboto import on bunny.net, two dead raisa.png references, no interwiki-style frame, and five tail correction modules; the campaign then repaired the image references by pointing them at the live EN file (4b52123), built the credit block in two steps (Phase 17 frame, T1 fields), added the missing frame and normalized the credit inside the FIX-CREDIT-D commit (1869877), reverted Roboto to Google Fonts (443c608), and renamed the usage exhibit in the sweep. The ledger closes the theme with P5 and P7 dispositioned and P6 and pattern 2 fixed. One minor inherited drop is flagged: a small exhibit image inside the wikibox demonstration (section 8). Two classifier leads are corrected on the bytes: the info pair is retained, not deleted (section 1), and only one of the five tail modules is credit CSS (section 5).

## Classification

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 3 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 2 |
| INFO-DEL | 1 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 19 |
| TRANSLATION-ANCHORED | 17 |
| WS-ONLY | 1 |

Across 45 classified blocks: 23 specific (51.1%), 19 heuristic (42.2%), 3 residue (6.7%), 0 skipped. The heuristic mass is the translation queue (the demonstration body is long relative to the file); the residue blocks are resolved in the Appendix, one of them (B38) carrying the flag of section 8.

## 1. Credit and attribution

**What.** The credit block (candidate L8–17) was built in two waves. Phase 17 (8dcac74) added the include pair with 初訳時参照リビジョン 57 and the 元記事リンク to https://scp-wiki.wikidot.com/theme:scpedia. The T1 wave (b816e10) added the six fields: タイトル SCPedia Theme, 翻訳責任者 SCP-JP, 翻訳年 2026, 原題 SCPedia Theme, 著作権者 EstrellaYoshte, 作成年 2021. FIX-CREDIT-D (1869877) normalized the translator line to AI. The classifier spans are CREDIT-PREVIEW and TASL-FIELDS in block B1. Block B5 carries an INFO-DEL span whose skeleton lead claims the info pair was removed; the bytes contradict it, as in the sibling adopted themes: the pair is retained and repointed (candidate L30 [[include :scp-jp:info:start]], L32 [[include :scp-jp:info:end]]), placeholder translated （ページに関する情報。, candidate L31).

**Why.** The field completion follows the same TASL pattern as the rest of the batch (ruling 3): the production page's Sigma-10 form is a campaign production (translation year 2026), so the translator credit is AI after normalization. The holder field names EstrellaYoshte, the original's author, whose name the theme's own files carry (the original's storage paths and the theme's attribution agree). The source link names scp-wiki.wikidot.com, the host recorded in review/sources.tsv; no host discrepancy exists to probe. The info pair's retention is the JP furniture form: the JP info module renders the info pane this theme demonstrates.

**Verify.** Read candidate L8–17 and L30–32. `git show 8dcac74 -- pages/theme:scpedia-jp.txt` and `git show b816e10 -- pages/theme:scpedia-jp.txt` show the two construction steps; `grep -n "info:start\|info:end" candidate.txt` returns the retained pair.

**Disposition.** Ledger PASS, row 34 (stamp STALE for the post-verdict sweep). The skeleton's INFO-DEL lead is a prose-vs-bytes discrepancy, recorded here and in the batch report.

## 2. Includes and components

**What.** Three include-level changes beyond the credit pair. (1) The interwiki-style frame at the head (candidate L1–4) does not exist in the original and did not exist in the imported candidate: FIX-CREDIT-D (1869877) added it, priority=1, naming the candidate's own code address (section 3). This is LOCALIZE-ROWS row 34 item (c), P6 missing interwiki-style, recorded FIXED in the ledger. (2) The usage exhibit (candidate L37–38, block B8) reads @@[[include :scp-jp:theme:scpedia-jp]]@@ after the sweep; its COMPONENT-SWAP primary is the classifier's name for the prefix change, ESCAPED-INCLUDE its exhibit form. (3) The bare Rate module is kept (candidate L25) inside its right-aligned exhibit group, with both labels translated （**評価:** and **クレジットモジュール付き評価:**, candidate L24 and L27).

**Why.** The frame addition matters beyond symmetry: without an interwiki-style frame, the theme's stylesheet does not reach the interwiki sidebar rendering path, the gap the P6 pattern exists to catch; the ledger (c3) register records pattern 6 as FIXED for this theme. That the fix rode inside a commit subject-named for credit normalization is a record-keeping wrinkle, noted in the Per-theme record: the commit's diff, not its subject, is the ground. The kept bare Rate is the sanctioned form for this theme by name: the ledger (c2) preamble's labelled paired Rate exhibits exception (FIXPREP / FIX3-A1 §1.1) lists scpedia among the three themes whose bare Rate beside the credit block is the exhibit form. The sweep rename follows the population convention (the -jp posting name resolves at posting).

**Verify.** `git show 1869877 -- pages/theme:scpedia-jp.txt` shows the frame block added at the head alongside the translator line. Candidate L1–4 shows the frame; L24–27 the Rate exhibit group. `git show b5cb724 -- pages/theme:scpedia-jp.txt` shows the usage rename.

**Disposition.** Pattern 6 FIXED (ledger (c3)); ledger PASS, row 34.

## 3. Delivery and code loading

**What.** The payload is the file's single [[code]] block (candidate L162, [[code type="CSS"]]), so its address is /1. Two loads name it: the head frame added by the P6 fix (candidate L3, https://sigma10-jp-test.wdfiles.com/local--code/theme%3Ascpedia-jp/1) and the tail module after the closing [[/iftags]] (candidate L973–975, importing the same address; blocks B1 and B44 carry the DELIVERY-HOST, DRAFT-HOST, and SELF-DELIVERY spans). The original delivers the same way minus the frame: its tail module (original L959–960) imports theme%3Ascpedia/1 from scp-wiki.wdfiles.com, and leaves the module unclosed at end of file; the candidate's module is closed ([[/module]], candidate L975), a completion present since the canonical import.

**Why.** The census is one block, one address, named twice (frame and module), which is the population's standard pairing once the P6 frame exists. The FIX-CODEADDR audit does not list this theme among mismatches or unresolved references, and the census here agrees. The original's unclosed tail module is a Wikidot tolerance the port does not need to reproduce; closing it changes no delivery semantics.

**Verify.** `grep -n "local--code" candidate.txt` returns L3 and L974, both naming /1. `grep -n "\[\[code" candidate.txt` returns the single payload block at L162.

**Disposition.** Ledger PASS, row 34; the DRAFT-HOST form is class (iii), the standing draft-stage form.

## 4. Fonts and assets

**What.** Three font and asset stories. (1) Roboto: the production port carried the import on fonts.bunny.net; FIX4-REPOINT (443c608) reverted it to fonts.googleapis.com (candidate L172), the original's host (original L158 region). This is LOCALIZE-ROWS row 34 item (b), a P5 exception-list violation, and the ledger records pattern 2 as FIXED for this theme via FIX4-REPOINT (KB-17). The stack at candidate L198 (font-family: sans-serif, 'Roboto', sans-serif) is the original's own, retained. (2) The serif face: @import of linuxlibertine.css at the head of the payload (candidate L171, block B42) is repointed from the original's scp-wiki.wdfiles path to the draft host's theme%3Ascpedia-jp copy (class (iii)); the linux_libertinesemibold stacks it feeds are unchanged. No JP face is added anywhere: LOCALIZE item (d), P7, recorded DISPOSITIONED in the ledger without a display-affecting mark. (3) raisa.png, the theme's logo image, appears twice (candidate L43, the image-block exhibit; candidate L958, the --lgurl variable). As imported, both references were dead (a bare filename in the image-block; a draft-host copy in the variable that did not resolve). The dead-reference wave (4b52123) pointed both at the live EN file, https://scp-wiki.wdfiles.com/local--files/theme%3Ascpedia/raisa.png. The localize audit then charged the result as item (a), P5 hotlinked from EN storage in two places, display-affecting; the ledger dispositions P5 (class (ii) / KB-58).

**Why.** The Roboto revert restores the exception-list host the campaign allows for this family (KB-17). The raisa sequence is the honest order of events and the package records it in that order: the wave's job was to make the references resolve, and the EN original file is the only live copy; the disposition's job is to record that the JP environment ultimately wants its own copy, which is a posting-time rehost, not a reason to leave the reference dead in the meantime. The P7 disposition records that the theme's Latin serif identity (Linux Libertine) is its design, and JP text falls back through the stack's Georgia and serif generics, accepted for this theme.

**Verify.** `git show 443c608 -- pages/theme:scpedia-jp.txt` shows the one-line host revert. `git show 4b52123 -- pages/theme:scpedia-jp.txt` shows both raisa lines changing to the EN URL (the image-block line also gaining its full URL form). Candidate L171–172 against the original's corresponding lines shows the libertine repoint and the Roboto host.

**Disposition.** Pattern 2 FIXED (FIX4-REPOINT, KB-17); P5 DISPOSITIONED and P7 DISPOSITIONED (ledger (c3)); ledger PASS, row 34.

## 5. Header, sidebar, site furniture

**What.** One T7-CREDIT-CSS block (B45) appends five live [[module CSS]] blocks after the delivery module (candidate L977–1002), all present since the canonical import (production supplements). Four are furniture corrections with English comments: the masthead correction for the 768–800px tablet band (extra-div-2 left offset), the native history list scroller (seven columns preserved inside their own horizontal scroller at ≤767px), the narrow header correction (top bar moved below the subtitle at ≤767px), and the Sigma-10 base wordmark correction (#header h1 a::after { content: none; }, removing the JP base's Japanese suffix after the title link because SCPedia draws its own wordmark). The fifth is the genuine credit correction: div.creditButton a and .rate-box-with-credit-button div.creditButton retargeted to the JP credit module's DOM, with a long comment explaining the EN/JP structural difference and the #FBFBFB ground pairing.

**Why.** The classifier's single T7 label covers the batch because the modules append together; on bytes, only the fifth is credit CSS (T7, KB-11/KB-12/KB-62: the JP module emits the info anchor as a direct child of .creditButton, so the theme's p-wrapped rules never reach it, and the retargeted declarations preserve the EN color pairing against the JP module's own painting). The furniture four address this theme's recorded render shapes: the fixed-width EN wordmark clipping at ≤768 (the render row's own line) is the wordmark correction's context, and the masthead and header corrections hold the compact header together at the widths the render record exercises. As live modules outside the gate, they apply wherever the theme is included, which is their intent.

**Verify.** Candidate L977–1002 shows all five modules with their comments. `git log --all -S "wordmark correction" -- pages/theme:scpedia-jp.txt` returns only the import commit d727e92.

**Disposition.** Ledger PASS, row 34. The T7 label's over-breadth is recorded as a classifier note, not a discrepancy in any prose record.

## 6. Text translation

**What.** TRANSLATION-ANCHORED spans in 17 blocks and TRANS-UNANCHORED spans in 19 blocks: the disambiguation line at the head (section 7), the exhibit labels, the demonstration body (wikibox, headings, samples), and the prose. The translation is the production form's, adopted with the page. The one WS-ONLY block in the file pairs with the reconcile wave's blank-line removal at the tail (ffad285).

**Why.** Reader-visible text localizes (P10, KB-18). The demonstration body is retained entire apart from the single exhibit image flagged in section 8; the exhibit census there is the ground.

**Verify.** Read the pairs in diff.md from candidate L19 onward; the labels are candidate L24 and L27 against original L8 and L11.

**Disposition.** T5 FINDINGS judged jointly with T4 (LOCALIZE-ROWS row 34); the findings are the P5/P6/P7 items of sections 2 and 4. Ledger PASS, row 34.

## 7. Links

**What.** One link repair, inside the FIX-CREDIT-D commit (1869877). The disambiguation line at the head originally read, in the candidate's first form, with a triple-bracket link [[[theme:eigenvector|]]] carried from the original (original L4). The wave rewrote it to a bracket URL link, [*https://scp-wiki.wikidot.com/theme:eigenvector 英語版のEigenvectorテーマ], with the reader-facing note （英語版・未訳） appended (candidate L20). No other prose link changes form; the license and source links in the body keep the original's targets.

**Why.** There is no JP Eigenvector theme page for a triple link to resolve to; left as a page link inside the JP environment it would point at a missing page and read as a defect of this page. The bracket link names the EN page the sentence actually means (the original's own target), and the note tells the JP reader the target is untranslated, which is the information the sentence exists to give.

**Verify.** `git show 1869877 -- pages/theme:scpedia-jp.txt` shows the line changing alongside the translator normalization and the frame addition. Candidate L19–20 against original L3–5 shows the final form.

**Disposition.** Part of the ledger PASS, row 34; no register charges the link, and the repair is recorded here because the commit's subject does not mention it.

## 8. Structure

**What.** One EXHIBIT-RESTRUCTURE block (B10): the raisa image-block (original L27 → candidate L43), whose primary is the standing false fire; the change inside it is the component repoint plus the dead-reference repair of section 4, and the exhibit itself is retained. The residue pair B38 carries the file's one silent drop: the original's wikibox demonstration contains a small image, [[image https://scp-wiki.wdfiles.com/local--files/estrellayoshte/u.png]] (original L122), inside the wikibox exhibit (original L119–125); the candidate's wikibox exhibit (candidate L135–140) has no image. The image has never existed in the canonical candidate (git log -S "u.png" is empty), so the production port dropped it before import.

**Why.** The exhibit census is otherwise complete: every other exhibit in the original (usage, Rate group, info pair, wikibox, code exhibit, samples) has its counterpart in the candidate. The u.png drop is small (a decorative image inside a demonstration box, hosted on the author's personal storage path) and plausibly a production-side dead-reference judgment, but no record states that, and the campaign's own dead-reference wave (4b52123) repaired this file's other dead references rather than dropping them. It is therefore flagged as a minor defect with its provenance, and the candidate is not edited by this package.

**Verify.** `grep -n "u.png" candidate.txt original.txt` returns original L122 only. The wikibox exhibits are original L119–125 against candidate L135–140.

**Disposition.** Ledger PASS, row 34. **Minor defect flag (this package): one exhibit image dropped** — original L122 (u.png inside the wikibox demonstration) absent from the candidate; provenance inherited from the production port at import (commit d727e92), not a campaign wave edit.

## 9. Formatting only

**What.** One WS-ONLY block: the blank line removed at the tail beside the escaped footnoteblock, part of the reconcile wave's two-line diff (ffad285). No other whitespace-only changes exist in the file.

**Why.** The removal is inert (a blank line between the closing gate and the tail module region) and travels with the escaping change that is its block-mate in the wave.

**Verify.** `git show ffad285 -- pages/theme:scpedia-jp.txt` shows the removed blank line and the escaping together.

**Disposition.** Formatting only; ledger PASS, row 34.

## 10. Porter annotations

**What.** No ANNOTATION signature fired. The porter voice in this file rides inside the tail supplement modules of section 5: five English comments (candidate L978, L985, L990, L995, and the long credit-correction comment at L1000), each naming itself an SCP-JP correction and explaining its rule, plus the reader-facing note （英語版・未訳） in the disambiguation line (candidate L20, section 7). All are production-inherited except the eigenvector note, which the FIX-CREDIT-D wave added as part of the link repair.

**Why.** Porter annotations are listed so they are never mistaken for original content (R2). The module comments are the supplements' own documentation, and the credit comment in particular carries the EN/JP DOM reasoning a future maintainer needs; the eigenvector note is reader-facing by design. None is disguised as original text.

**Verify.** Candidate L977–1002 shows the five comments above their rules. `grep -n "SCP-JP" candidate.txt` returns the comment lines and the :scp-jp: prefixes.

**Disposition.** Porter comments recorded. Ledger PASS, row 34.

## 11. Dispositions and exceptions

**What.** The dispositioned and excepted items: (1) P5 DISPOSITIONED (ledger (c3), class (ii) / KB-58): the raisa.png EN-storage hotlinks (section 4). (2) P7 DISPOSITIONED (ledger (c3), recorded without a display-affecting mark): no JP face added (section 4). (3) The bare Rate beside the credit block is the labelled paired Rate exhibits exception (ledger (c2) preamble item 6), which names scpedia explicitly. (4) The T1 residue (hotlink×3, pseudo-ref×2 within 5 errors / 2 warns / 2 infos) is the standing classes of register (c1): the hotlinks are the raisa pair and the bunny.net Roboto import as the baseline checker saw them, and the pseudo-references are the theme's own file references inside its exhibits. (5) The render record's "page body empty" line carries its own adjudication in the row: the tag gate [[iftags +テーマ]] plus a possible stale cache, not a defect; the wordmark clip and overflow lines are the narrow-width family (FIX3-S2EN §6.5 / KB-35 cohort disposition), the sample credit-modal errors are the preview-form disposition (credit:start-preview has no modal mechanism, GOSIGN-TESTS T2 amendment), and the T2 sample exit 2, retried once, is a coverage caveat.

**Why.** Each item is re-derivable from this package: the raisa lines are candidate L43 and L958; the Roboto line is candidate L172 (post-fix form) with its wave diff in section 4; the Rate group is candidate L23–28; the render text is RENDER-ROWS-1 (RENDER-D row 34).

**Verify.** The cited lines and rows; the exception's theme list is in the ledger (c2) preamble.

**Disposition.** P5 and P7 DISPOSITIONED, patterns 2 and 6 FIXED, in the ledger (c3) register; ledger PASS, row 34, with no section (e) items and no FIX5 re-judgement.

## 12. Verification

**What.** The checks behind this package, each re-runnable from the repo: T1 as recorded (exit 1, 5/2/2, T1-ROWS row 34); T2/T3 as recorded (RENDER-ROWS-1, RENDER-D row 34, with its caveats); the wave diffs for ffad285, 4b52123, 8dcac74, b816e10, 1869877, 443c608, and b5cb724 read against this file; the FIX-CODEADDR audit consulted (this theme absent from its mismatch and unresolved lists) and the code-block census re-derived (section 3); CSS brace balance by depth (both files end at depth 0 with no negative dip); the u.png presence census (section 8); and `python3 review/build_review.py --check`, which passes over this package (candidate.txt byte-identical to the canonical file; original.txt hash equal to the sources.tsv value).

**Why.** Every factual claim above names the lines, the commit, or the register row that decides it, so a reviewer can re-derive the package without trusting the writer.

**Disposition.** Package complete against the ledger PASS, row 34 (stamp STALE for the post-verdict sweep line), with the one minor defect flag of section 8 carried to the batch report.

## Per-theme record

LOCALIZE-ROWS row 34 (source LOCALIZE-B) records five items: (a) P5 raisa.png hotlinked from EN storage in two places (display-affecting); (b) P5 fonts.bunny.net Roboto (exception-list violation); (c) P6 missing interwiki-style; (d) P7 no JP face; (e) a fifth item whose text the vendored row truncates at "(e) …", not recoverable from the record in this repo. The ledger (c3) register records, for this theme: P5 DISPOSITIONED (class (ii) / KB-58), P6 FIXED, P7 DISPOSITIONED (recorded without a display-affecting mark), and pattern 2 FIXED via FIX4-REPOINT. The T4 display-affecting count of 2 corresponds to items (a) and (b). T1-ROWS row 34 records exit 1, 5 errors / 2 warns / 2 infos (hotlink×3, pseudo-ref×2). RENDER-ROWS-1 (RENDER-D row 34) records the combined T2/T3 FINDINGS quoted in the Status table. Three prose-vs-bytes discrepancies are recorded: (1) the skeleton's INFO-DEL lead claims the info pair was removed; the pair is retained and repointed (section 1). (2) The FIX-CREDIT-D commit's subject names only the credit normalization; its diff also adds the interwiki-style frame (the P6 fix) and repairs the eigenvector link (sections 2 and 7). (3) The localize row's item (e) is truncated in the vendored record, so this package can neither narrate nor adjudicate it; the ledger's registers, which are complete for this theme, record no fifth item.

### Post-package repairs (REFRESH3-G)

- **FIX-U8, landing `d554544b88a5b14936b0f0e67c10361c79179ad3`** ("pages: U-8 repairs …", 2026-11-17, R/review-scout/FIX-U8.md item 3): the wikibox exhibit image restored verbatim from the original — `[[image https://scp-wiki.wdfiles.com/local--files/estrellayoshte/u.png]]` at refreshed candidate L138, between the exhibit title line (L136) and the horizontal rule (L140), +1 line. The original's wikibox demonstration carries this image (orig L122); the production port dropped it and no canonical version had it (BATCH-U8 `git log -S "u.png"` empty). The EN host is the candidate's established form for this exhibit's assets — the sibling raisa.png stands at L43 (image-block include) and L959 (CSS variable), kept there by the dead-reference wave 4b52123. Checker: error 4 → 5 / warn 0 / info 2 — the single new finding is a class (ii) hotlink on the restored image, the same class the file's two pre-existing raisa.png hotlinks carry, class (i) 0 before and after.

The regenerated stamp reads `Overall: STALE` against the pre-repair verdict, by design; no re-judgement is fabricated and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The Phase 17 migration deliverable, pages/phase17-diff-scpedia-jp.txt in this repo, is the change set that carries this candidate's form onto the production page theme:scpedia; it is part of the same canonical record. The wave commits b816e10, 1869877, 443c608, and b5cb724 are population commits; their shares in this file are the lines cited in sections 1, 2, 4, and 7.

## Multi-wave provenance

| Wave | Commit | Change to this file |
|---|---|---|
| Canonical import (production form adopted) | d727e92 | The candidate as the production page stands: translation, info pair repointed, Rate kept with translated labels, five tail correction modules, tail delivery module closed; Roboto on bunny.net, raisa references dead, no interwiki frame, u.png already absent |
| Reconcile | ffad285 | Tail [[footnoteblock]] escaped to @@[[footnoteblock]]@@ and one blank line removed |
| Dead image reference repair | 4b52123 | raisa.png image-block name given the full EN URL; --lgurl repointed from the dead draft-host copy to the EN file |
| Phase 17 | 8dcac74 | Credit include pair added with 初訳時参照リビジョン 57 and 元記事リンク |
| T1 credit completion | b816e10 | The six TASL fields added to the credit block |
| FIX-CREDIT-D | 1869877 | Interwiki-style frame added at the head (P6 fix); 翻訳責任者 SCP-JP → AI; eigenvector disambiguation link rewritten to the EN page with an untranslated-target note |
| FIX4-REPOINT | 443c608 | Roboto import reverted fonts.bunny.net → fonts.googleapis.com (1 line) |
| Usage-example sweep (post-verdict) | b5cb724 | Usage exhibit renamed :scp-jp:theme:scpedia → :scp-jp:theme:scpedia-jp; the stamp's STALE state dates from this commit |

## Appendix — residue blocks

- R1 = B3 (original L7–8 → candidate L23–24): the Rate exhibit's label pair, "**Rating:**" → "**評価:**", a full label translation with no surviving anchor (section 2).
- R2 = B9 (original L24–25 → candidate L40–41): the demonstration heading "+ Examples" → "+ 例", by the same shape.
- R3 = B38 (original L121–122 → candidate L137): the wikibox exhibit pair whose original side carries the u.png image line; resolved as the dropped exhibit image of section 8, not as a translation.
