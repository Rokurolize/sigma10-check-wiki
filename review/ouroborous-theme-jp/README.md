# Review package — theme:ouroborous-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:ouroborous-theme-jp — origin EN, population #25 [GOSIGN2-LEDGER (b) row 25]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 847b7bd5dd34c1c730b258e493964bc30cde09c5b6010df2df963de0ada2220e); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 6 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 25; GOSIGN2-LEDGER (b) row 25]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — 320px page overflow, notice left-clip, header logo clipped, WebKit CC "S", dark-on-dark table/title, sample credit-modal + overflow 337–419px. [RENDER-ROWS-1 (RENDER-C row 25)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 25)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 25, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 25]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 25]
- Computed against: canonical commit 358955eb4013dac2399c414ba8ec2a6e416a3c11; candidate file pages/theme:ouroborous-theme-jp.txt sha256:847b7bd5dd34c1c730b258e493964bc30cde09c5b6010df2df963de0ada2220e; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/ouroborous-theme-jp/candidate.txt (sha256 db95e4d5e9a1dacc3b40203101e1675aa2a99db1c396c971736fd34a96383b16)
Original: theme:ouroborous-theme — scp-wiki, revision 41 (sha256 3854aaf3c5c30aa681bbc9eb458cb4e743641b6c77a2be9f94d1d332231d957c)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## 0. Header / provenance

- Delivery: no relocation detected between the sides; each side's components match by kind.
- Provenance route: adopted from the production JP counterpart (kind K6 in review/sources.tsv). The production page theme:ouroborous-theme already exists on scp-jp as a human translation (translator nebula2700, translation year 2024, per the candidate's credit block); the campaign's migration deliverable for it is pages/phase17-diff-ouroborous-theme-jp.txt from Phase 17, and sources.tsv records the production page as matching the reference revision (production drift 一致）. The candidate in this repo is that production form as imported in commit d727e92, plus four campaign wave edits: the reconcile escaping (ffad285), the trailing-whitespace normalization (3010ef7), the Phase 17 reference-revision line (8dcac74), and the T1 credit-field completion (b816e10). Everything else in the diff against the EN original, including the items flagged below, is the production port's own shape, inherited at import.

## Status

| Check | Verdict | Source |
|---|---|---|
| Overall | PASS — no OPEN items | GOSIGN2-LEDGER (b) row 25 |
| T1 source check | FINDINGS (classified) — exit 1, 3 errors / 2 warns / 6 infos (pseudo-ref×3) | T1-ROWS row 25 |
| T2/T3 render | FINDINGS — 320px page overflow, notice left-clip, header logo clipped, WebKit CC "S", dark-on-dark table/title, sample credit-modal + overflow 337–419px | RENDER-ROWS-1 (RENDER-C row 25) |
| T4 localize patterns | FINDINGS — 0 display-affecting findings; the one finding is the pattern-3 credit-field gap, since fixed | LOCALIZE-ROWS row 25 (LOCALIZE-B) |
| T5 translation text | FINDINGS — judged jointly with T4 by the source report | LOCALIZE-ROWS row 25 |
| FIX5 re-judgement | none — no OPEN items at the ledger determination | GOSIGN2-LEDGER (b) row 25 |

## Provenance

| Side | Identity |
|---|---|
| Original | theme:ouroborous-theme, scp-wiki, revision 41; mirror class FETCH-REGEN; sha256 3854aaf3c5c30aa681bbc9eb458cb4e743641b6c77a2be9f94d1d332231d957c (review/sources.tsv) |
| Candidate | pages/theme:ouroborous-theme-jp.txt in this repo; sha256 db95e4d5e9a1dacc3b40203101e1675aa2a99db1c396c971736fd34a96383b16 (stamp, computed against canonical commit b816e10) |
| Production counterpart | theme:ouroborous-theme on scp-jp (kind K6); migration deliverable pages/phase17-diff-ouroborous-theme-jp.txt |

## Summary

Ouroborous is a Black Highlighter based theme: it loads the BHL stylesheets, restates header variables and a large override payload in one [[code]] block, and self-delivers that payload after the tag gate at frame priority 3. The candidate keeps that topology, repoints the BHL delivery to the JP mirror host and the base candidate, re-hosts the logo to JP storage, and carries the production translation's text. The campaign's own edits are small and exactly recorded: a one-line reconcile escaping, a whitespace normalization, and the two-step credit completion (reference-revision line in Phase 17, the four missing TASL fields in the T1 wave) that closes the theme's only localize finding. Two inherited items are flagged or recorded: the production port dropped the original's Typekit font import while keeping the stacks that name its families (section 4, a defect flag), and it deleted the original's bare Rate module (section 8, recorded with its grounds). The render findings are the narrow-width and credit-modal families the ledger dispositions for the whole cohort.

## Classification

| Label | Blocks |
|---|---|
| ASSET-REHOST | 1 |
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| CSS-BODY | 2 |
| DELIVERY-HOST | 5 |
| DRAFT-HOST | 4 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| HEADERVAR | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 5 |
| SELF-DELIVERY | 2 |
| T7-CREDIT-CSS | 3 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 21 |
| TRANSLATION-ANCHORED | 19 |
| WS-ONLY | 110 |

Across 170 classified blocks: 148 specific (87.1%), 20 heuristic (11.8%), 2 residue (1.2%), 0 skipped. The heuristic mass is the translation queue; the WS-ONLY mass is the production port's tab-to-space re-indentation of the CSS payload plus the campaign's trailing-whitespace wave. The residue blocks are resolved in the Appendix.

## 1. Credit and attribution

**What.** The credit block (candidate L34–44) reads: [[include :scp-jp:credit:start-preview]], タイトル ウロボロステーマ, 翻訳責任者 nebula2700, 翻訳年 2024, 作者 Woedenaz, 著作権者 Woedenaz, 原題 Ouroborous Theme, 作成年 2020, 初訳時参照リビジョン 41, 元記事リンク to https://scp-wiki.wikidot.com/theme:ouroborous-theme, [[include :scp-jp:credit:end-preview]]. The classifier spans are CREDIT-PREVIEW and TASL-FIELDS in block B7. As imported, the block lacked four fields; Phase 17 (8dcac74) added the 初訳時参照リビジョン line, and the T1 wave (b816e10) added 翻訳責任者 nebula2700, 翻訳年 2024, 著作権者 Woedenaz, and the 元記事リンク line.

**Why.** The gap was the theme's only localize finding (LOCALIZE-ROWS row 25: pattern 3, credit missing 翻訳責任者/翻訳年/著作権者 label/元記事リンク）, and the ledger (c3) register records pattern 3 as FIXED for this theme. The completed block follows ruling 3's other half: the translator is the human production translator, and the name stays because it matches the live JP creator; campaign translations are credited to AI, adopted human translations keep their translator. The author and holder fields name Woedenaz, carried from the production page's own credit （作者 field, which predates the campaign). The source link names scp-wiki.wikidot.com, the host recorded in review/sources.tsv; no host discrepancy exists to probe.

**Verify.** Read candidate L34–44. `git show 8dcac74 -- pages/theme:ouroborous-theme-jp.txt` shows the single added revision line; `git show b816e10 -- pages/theme:ouroborous-theme-jp.txt` shows the four added field lines and nothing else.

**Disposition.** Pattern 3 FIXED (ledger (c3)); ledger PASS, row 25.

## 2. Includes and components

**What.** The head carries an include the original does not have: candidate L1–3 wraps [[include :scp-jp:theme:black-highlighter-theme]] in a bare [[iftags]] gate (block B1, whose classifier note flags the bare gate as a KB-08 anomaly). The theme's own tag gate follows at candidate L5, [[iftags +テーマ]], against the original's [[iftags +theme]] (IFTAGS span in B1). The component repoints (INCLUDE-REPOINT spans): the two interwiki-style frames at the head (blocks B3/B5, also carrying EXHIBIT-RESTRUCTURE primaries), the theme-squares component (candidate L50, block B9, repointed to :scp-jp:component:theme-squares with its color parameters retained, trailing spaces normalized by wave 3010ef7), and the tail frame (B168). The usage exhibits (candidate L97–98, block B22, ESCAPED-INCLUDE) read @@[[include :scp-jp:theme:black-highlighter-theme]]@@ and @@[[include :scp-jp:theme:ouroborous-theme]]@@.

**Why.** The bare-gate head include is the BHL port form used across the population: the base candidate loads only inside the gate, and ruling 1 settles that cross-theme imports name the JP fixed base candidate. The classifier's anomaly note is about the gate's shape in isolation; against the population form and the ledger's silence, the adjudication is that the form is standard, and the tag localization proper is the +テーマ gate at L5 (P2, KB-08). The usage exhibit naming the plain production page (theme:ouroborous-theme, no -jp) is correct for a kind-K6 theme: the production page exists, adopters include it, and the -jp candidate is its migration candidate, the same convention the ledger dispositions as P1 for the sibling adopted themes. The theme-squares repoint keeps the color exhibit on the JP component port (ruling 4).

**Verify.** Candidate L1–5 shows the two gates in order. `grep -n "theme-squares" candidate.txt` returns L50 with the :scp-jp: prefix. The usage lines are candidate L97–98.

**Disposition.** Ledger PASS, row 25; no include finding is recorded for this theme in any register.

## 3. Delivery and code loading

**What.** The BHL stylesheets load twice over, as in the original: a [[module CSS]] at candidate L6–21 importing normalize.min.css and black-highlighter.min.css from https://scp-jp.github.io/Black-Highlighter/css/min/ (original: nu-scptheme.github.io, same paths), and two interwiki-style frames naming the same files at priorities 1 and 2 (candidate L24–32). The theme's own payload self-delivers after the gate: a [[module CSS]] importing https://sigma10-jp-test.wdfiles.com/local--code/theme%3Aouroborous-theme-jp/1 and a frame at priority=3 naming the same address (candidate L1040–1044, blocks B167/B169; DELIVERY-HOST, DRAFT-HOST, SELF-DELIVERY spans). The original's tail names theme%3Aouroborous-theme/1 on scp-wiki.wdfiles.com at the same priority.

**Why.** The host change for the base files (DELIVERY-HOST spans in B2/B4/B6) serves the BHL sheets from the JP mirror the campaign maintains for this environment, the same host the base candidate itself uses, so the direct imports and the head include of section 2 cannot drift apart. The self-delivery address names the candidate's only [[code]] block, which is the payload in document order; the FIX-CODEADDR audit (R/review-scout/FIX-CODEADDR.md) does not list this theme among mismatches or unresolved references, and the census here agrees. Priority 3 for the theme's own sheet, after the base's 1 and 2, is the original's cascade design retained.

**Verify.** `grep -n "local--code" candidate.txt` returns the two tail lines naming /1. `grep -n "\[\[code" candidate.txt` returns the single payload block. `grep -n "scp-jp.github.io" candidate.txt` returns L7, L8, L27, L32.

**Disposition.** Ledger PASS, row 25; the DRAFT-HOST form is class (iii), the standing draft-stage form.

## 4. Fonts and assets

**What.** One ASSET-REHOST block (B60): --logo-image moves from https://scp-wiki.wdfiles.com/local--files/theme%3Aouroborous-theme/ouroborous_logo.svg (original L193) to the JP storage file-ID URL https://scp-jp-storage.wdfiles.com/local--files/file%3A8260379-47-m0s5/ouroborous_logo.svg (candidate L204), colon-encoded. Two DRAFT-HOST exhibit lines (B16, B19) show the theme's own logo files served from the check-wiki draft host inside the demonstration body. And one CSS-BODY block (B57) is the dropped font import: the original's code block opens with @import url("https://use.typekit.net/mst2dnj.css"); (original L176), and the candidate's code block (candidate L187) has no import line at all. The stacks that import served survive on both sides: --header-font: korolev-condensed, sans-serif (candidate L208) and --title-font: korolev, sans-serif (candidate L209); korolev and korolev-condensed are Typekit families, and no @import or @font-face anywhere in the candidate, or in the BHL base delivery it loads, provides them.

**Why.** The re-host (P5, KB-17) puts the theme's logo on the allowlisted JP storage host in the encoded file-ID form, so the header image resolves in this environment. The exhibit images on the draft host are class (iii), the theme's own files in draft-stage form. The Typekit drop is different: it is a silent delivery loss inherited from the production port. The candidate has never contained the import in any canonical version (all five commits touching the file show zero occurrences), so no campaign wave made the cut; the production page dropped it, and every register passed over it because the stacks still parse and the fallback (sans-serif) renders. Under the campaign's own rule, a family named in a stack but loaded by nothing in the file or its base delivery is a flag, not a supplement, so it is flagged here with its provenance stated.

**Verify.** `grep -n "typekit" candidate.txt original.txt` returns original L176 only. `grep -n "korolev" candidate.txt` returns L208–209. The re-hosted logo is candidate L204 against original L193.

**Disposition.** Ledger PASS, row 25 (no register charges the font import). **Defect flag (this package): font import dropped, dependent stacks kept** — original L176 (@import use.typekit.net/mst2dnj.css at the head of the delivered code block) absent from the candidate, while candidate L208–209 still name korolev-condensed and korolev. Provenance: inherited from the production port at import (commit d727e92), not a campaign wave edit.

## 5. Header, sidebar, site furniture

**What.** Two HEADERVAR blocks (B59, B60): --header-title "The Foundation" and --header-subtitle "Office of the Overseer" are kept in English on both sides (candidate L201–202 against original L190–191), inside the tab-to-space re-indented :root block. One CSS-BODY block (B170) is a supplement module after the tail frame: candidate L1045–1049, a live [[module CSS]] whose English comment reads "SCP-JP Wikidot ouroborous top bar labels: keep top navigation labels whole at narrow widths." and whose single rule sets word-break: keep-all on the top-bar link selectors. The module is present since the canonical import (commit d727e92), so it is the production port's supplement, not a campaign wave's.

**Why.** Header title language is ruling 2 territory: outside migration correctness, so the kept English titles need no disposition and receive none. The top-bar supplement addresses a real JP-environment failure mode (translated top-bar labels splitting mid-word at narrow widths) with one rule scoped to the top bar; it changes no other selector. Its comment is porter voice and is counted in section 10.

**Verify.** `grep -n "header-title\|header-subtitle" candidate.txt` returns the kept values at L201–202. The supplement is candidate L1045–1049, after the priority-3 frame.

**Disposition.** Ledger PASS, row 25. The render findings touching furniture (header logo clipped, notice left-clip, 320px overflow) are the cohort family disposition in section 11.

## 6. Text translation

**What.** TRANSLATION-ANCHORED spans in 19 blocks and TRANS-UNANCHORED spans in 21 blocks: the production translation's prose, the theme-squares color names retained in English as component parameters (the 3010ef7 wave stripped their trailing spaces without translating them), the demonstration body, and headings (the residue pair "+ Examples" → "+ 例" is resolved in the Appendix). The translation is the production translator's (nebula2700, 2024), adopted as-is; FIX-CREDIT-D's population normalization does not touch this file because the translator is a named human.

**Why.** Adopted human translations are the provenance route's substance (P10, KB-18 for the translation mass itself): the campaign reviews them, it does not re-translate them. The color names inside the theme-squares parameters are component data, not prose; leaving them in English matches the component's parameter vocabulary.

**Verify.** Read the pairs in diff.md; the color parameter block is candidate L50–78 against the original's, differing in trailing whitespace only (wave 3010ef7's diff shows exactly those lines).

**Disposition.** T5 FINDINGS judged jointly with T4 (LOCALIZE-ROWS row 25), the finding being the credit gap of section 1, since fixed. Ledger PASS, row 25.

## 7. Links

**What.** No link-specific signature fired, and no prose link changes form: the candidate's outbound links are the credit source link (section 1) and the links inside the demonstration body, which keep the original's targets. The file-URL changes are delivery and asset matters, covered in sections 3 and 4.

**Why.** Nothing in this theme's link set needed repointing beyond the include, delivery, and asset changes already counted; the demonstration body links name the same pages on both sides.

**Verify.** Compare the bracket links in diff.md outside the delivery and credit regions; they pair one-to-one with the original's.

**Disposition.** Ledger PASS, row 25; no link finding is recorded for this theme.

## 8. Structure

**What.** Four EXHIBIT-RESTRUCTURE blocks, one BARE-RATE-DEL block, and the CSS-BODY blocks adjudicated in sections 4 and 5. B3, B5, and B168 are the interwiki-style frames: mere repoints, the standing false fire, with the exhibits around them retained entire. B9 is the theme-squares repoint (section 2). B8 (BARE-RATE-DEL) is the deletion of the original's centered bare Rate module (original L30–32: [[=]], [[module Rate]], [[/=]]); the candidate has no [[module Rate]] anywhere. The deletion is inherited: the candidate has never contained the module in any canonical version, so the production port removed it before import.

**Why.** For the frames and the component, the exhibit census is the ground: every exhibit in the original (theme-squares, usage, demonstration body, code exhibit) has its counterpart in the candidate, so the EXHIBIT-RESTRUCTURE primaries record repoints, not losses. The Rate deletion needs its own ground, because the ledger's labelled-exhibit exception sanctions the opposite choice (a kept bare Rate) for three sibling themes. The ground here is provenance and function: the production JP theme page serves its attribution through the credit block at the head, and the production translator dropped the EN page's standalone Rate module when making that page; the campaign adopted the page as it stands, no register charges the deletion, and the render record's credit-modal line is the preview-form disposition, not a missing-widget finding. The deletion is recorded here so the census is complete, without a defect charge.

**Verify.** `grep -n "module Rate" candidate.txt original.txt` returns original L31 only. `git log --all -S "module Rate" -- pages/theme:ouroborous-theme-jp.txt` returns no commit, confirming the module was never in the canonical file.

**Disposition.** Ledger PASS, row 25; the BARE-RATE-DEL instance is dispositioned by provenance (adopted production form), recorded in the Per-theme record.

## 9. Formatting only

**What.** 110 WS-ONLY blocks, the largest mass in this package after the specific labels. Two sources: the production port re-indented the CSS payload from tabs to spaces (visible throughout the code block, e.g. candidate L200–205 against original L189–194), and the campaign's trailing-whitespace wave (3010ef7) stripped trailing spaces from the theme-squares parameter lines and similar lines across the population.

**Why.** Neither source changes a computed value: indentation inside a stylesheet and trailing spaces on parameter lines are inert, and the wave's purpose was to stop the trailing spaces from breaking parameter parsing at posting. The count is large because the payload is 850 lines of re-indented CSS.

**Verify.** `git show 3010ef7 -- pages/theme:ouroborous-theme-jp.txt` shows the wave's share (trailing-space removals only). Any WS-ONLY block in diff.md pairs lines differing only in leading or trailing whitespace.

**Disposition.** Formatting only; ledger PASS, row 25.

## 10. Porter annotations

**What.** No ANNOTATION signature fired. One porter-voiced text exists, riding inside the CSS-BODY supplement of section 5: the English comment at candidate L1046 ("SCP-JP Wikidot ouroborous top bar labels: keep top navigation labels whole at narrow widths."). It is the production porter's note explaining the supplement rule, present since the canonical import. No other comment in the candidate lacks a counterpart in the original; the payload's CSS comments are the original's own, retained with their rules.

**Why.** Porter annotations are listed so they are never mistaken for original content (R2). This one is identified, located, and attributed to the production port; it documents a supplement the reader can see directly below it, so it informs rather than misleads.

**Verify.** Candidate L1045–1049 shows the comment directly above its rule. `grep -n "SCP-JP" candidate.txt` returns this comment and the :scp-jp: include prefixes only.

**Disposition.** One inherited porter comment, recorded. Ledger PASS, row 25.

## 11. Dispositions and exceptions

**What.** No derived presence label fired for this section, and the theme has no ledger (c3) DISPOSITIONED items; its one register entry is the pattern-3 FIXED of section 1. The standing items to record: (1) the T1 residue (pseudo-ref×3, with 3 errors / 2 warns / 6 infos overall) is the checker's name for the theme's own file references inside its exhibits and code (the draft-host logo images of section 4 and the self-delivery address), class (i) standing in register (c1): not defects. (2) The render findings (320px page overflow, notice left-clip, header logo clipped, WebKit CC "S", dark-on-dark table/title, sample overflow 337–419px) are the narrow-width and dark-on-dark families dispositioned for the whole cohort in FIX3-S2EN §6.5 (X1–X9) / KB-35; the sample credit-modal errors are the preview-form disposition (credit:start-preview has no modal mechanism, GOSIGN-TESTS T2 amendment).

**Why.** Each item rests on evidence inside this package: the pseudo-references resolve to the candidate's own addresses and files; the render findings are recorded against the cohort's family dispositions in the ledger, not against this file's individual bytes, and the ledger's determination for the row is PASS with no OPEN items.

**Verify.** T1-ROWS row 25 for the counts; RENDER-ROWS-1 (RENDER-C row 25) for the finding text; the ledger (c2) preamble and (c3) register for the family dispositions.

**Disposition.** Ledger PASS, row 25, with no section (e) items and no FIX5 re-judgement.

## 12. Verification

**What.** The checks behind this package, each re-runnable from the repo: T1 as recorded (exit 1, 3/2/6, T1-ROWS row 25); T2/T3 as recorded (RENDER-ROWS-1, RENDER-C row 25); the wave diffs for ffad285, 3010ef7, 8dcac74, and b816e10 read against this file; the per-commit presence census for typekit, the Rate module, and the top-bar supplement (all five commits, section 4 and 8 grounds); the FIX-CODEADDR audit consulted (this theme absent from its mismatch and unresolved lists); CSS brace balance by depth (both files end at depth 0 with no negative dip); and `python3 review/build_review.py --check`, which passes over this package (candidate.txt byte-identical to the canonical file; original.txt hash equal to the sources.tsv value).

**Why.** Every factual claim above names the lines, the commit, or the register row that decides it, so a reviewer can re-derive the package without trusting the writer.

**Disposition.** Package complete against the ledger PASS, row 25, with the one defect flag of section 4 carried to the batch report.

## Per-theme record

LOCALIZE-ROWS row 25 (source LOCALIZE-B) records one finding: pattern 3, the credit block's missing 翻訳責任者/翻訳年/著作権者 label/元記事リンク, with 0 display-affecting findings, no unincorporated display-affecting upstream update, and no T5 residue. The ledger (c3) register records pattern 3 FIXED (waves 8dcac74 and b816e10, section 1). T1-ROWS row 25 records exit 1, 3 errors / 2 warns / 6 infos (pseudo-ref×3). RENDER-ROWS-1 (RENDER-C row 25) records the combined T2/T3 FINDINGS quoted in the Status table. Three prose-vs-bytes discrepancies are recorded: (1) the classifier skeleton flags the bare [[iftags]] head gate as a KB-08 anomaly; the bytes show the population-standard BHL base-include form, adjudicated in section 2. (2) The reconcile commit ffad285 ("ouroborous: reconcile") escapes the tail [[footnoteblock]] into literal text (@@[[footnoteblock]]@@, candidate L1037); no prose record states its reason. The change is inert on current bytes because neither side uses [[footnote]] anywhere (grep count 0 in both files), so no footnote rendering is lost; it is narrated here because the wave's subject does not say what it did. (3) The Typekit import drop (section 4) appears in no register at all; the production port made it, the registers' silence about it is a gap in the record, and this package is its first documentation.

## Change set outside the two diffed files

The Phase 17 migration deliverable, pages/phase17-diff-ouroborous-theme-jp.txt in this repo, is the change set that carries this candidate's form onto the production page theme:ouroborous-theme; it is part of the same canonical record. The wave commits 3010ef7 and b816e10 are population commits touching many files; their shares in this file are the lines cited in sections 1 and 9.

## Multi-wave provenance

| Wave | Commit | Change to this file |
|---|---|---|
| Canonical import (production form adopted) | d727e92 | The candidate as the production page stands: translation, BHL repoints, logo re-host, T7 credit-CSS extensions, top-bar supplement; Typekit import and bare Rate module already absent |
| Reconcile | ffad285 | Tail [[footnoteblock]] escaped to @@[[footnoteblock]]@@ (1 line) |
| Trailing-whitespace normalization | 3010ef7 | Trailing spaces stripped (theme-squares parameter lines and similar) |
| Phase 17 | 8dcac74 | 初訳時参照リビジョン： 41 added to the credit block (1 line) |
| T1 credit completion (FIX wave) | b816e10 | 翻訳責任者/翻訳年/著作権者/元記事リンク added to the credit block (4 lines) |

## Appendix — residue blocks

- R1 = B23 (original L88–89 → candidate L100–101): the demonstration heading "+ Examples" → "+ 例", a full heading-text translation with no surviving anchor token, so no signature fires. Translation by shape, counted in section 6.
- R2 = B166 (original L1025–1026 → candidate L1036–1037): the tail [[footnoteblock]] escaping, the ffad285 reconcile line (Per-theme record, item 2). The classifier leaves it unlabeled because escaping changes no anchor; the wave commit is its ground.
