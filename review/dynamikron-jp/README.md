# Review package — theme:dynamikron-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:dynamikron-jp — origin EN, population #82 [GOSIGN2-LEDGER (b) row 82]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 31685fbdda9eb908fd1cfe7c7f2a6226e0b9aff2cb9e01879cd8aa33c9ace35b); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 1 warn / 2 infos (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 102; GOSIGN2-LEDGER (b) row 82]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — credit modal wider than 320px viewport both engines + WebKit CC "S" + notice clip ≤375; assets 404/ORB = EN8 deferred; sample T3 none seen. [RENDER-ROWS-1 (RENDER-S2-B)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-S2-B)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 2 [LOCALIZE-ROWS row 82, source LOCALIZE-S2-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 82]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 82]
- Computed against: canonical commit 49a1e493cc9756c0314b065a789dbdb226faf5df; candidate file pages/theme:dynamikron-jp.txt sha256:31685fbdda9eb908fd1cfe7c7f2a6226e0b9aff2cb9e01879cd8aa33c9ace35b; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/dynamikron-jp/candidate.txt (sha256 fd150c0f27888e4ffd662e68d1911e04bebf8fa2b323cdb9aa2acb8a9a3dea59)
Original: theme:dynamikron — scp-wiki, revision 19 (sha256 668a15753d0dd18427b8eed52c3e188c9b0e13a625d6ac6243cf4bd17d)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 82); one of the 286 of 286 pass-eligible themes. The generated stamp above reads **STALE**, not PASS: the candidate was revised after the verdict by the FIX-DYN landing recorded below. The record verdict stands and the row is posted like a PASS row |
| Wave edits | Two FIX3-S2EN edits (the font fix and the rev19 follow-up), both verified hunk by hunk in the Per-theme record. Both ride inside commit 1869877, whose subject names only the FIX-CREDIT-D translator normalization |
| Discrepancies recorded | The ledger's "P6 FIXED (frame waves)" is a verification outcome, not an edit: no priority=3 own-CSS frame exists or was ever added (section 2). The ledger's "P7 FIXED" is broader than the edit: the wave loaded Noto Sans JP and extended one stack of seven (section 4) |
| Defect flagged (now closed) | The Eddie Murphy quote at cand L173 originally changed the subject ("My girl" → みんな). The localize lane flagged it with a suggested correction; the as-built section 6 records the flag. The FIX-DYN landing `49a1e49` (Post-package repairs, below) repaired L173 after the package build, and the current candidate reads 「おれの彼女はパーティーしたがる」; the flag is closed by that landing, not by this package |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:dynamikron | theme:dynamikron-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revisions | First translation 17; re-translation 19, both recorded in the candidate's credit block (cand L10-11). This package's mirror is revision 19 | — |
| Source of this copy | Campaign mirror store, FETCH-MISSING class (fetched 2026-11-17; hash-verified against review/sources.tsv) | Canonical file `pages/theme:dynamikron-jp.txt`, created in commit 184cb65 (Stage 2 EN8 integration); its only later change is commit 1869877 |
| Lines | 902 (generator count, diff.md) | 912 (generator count, diff.md) |
| SHA-256 | 668a15753d0dd18427b8eed52c3e188c9b0e13a625d6ac6243cf4bd17d | fd150c0f27888e4ffd662e68d1911e04bebf8fa2b323cdb9aa2acb8a9a3dea59 |

Provenance route: derived from the original, in two steps. The port was made from revision 17 (the EN8 candidate ran to 916 lines); the FIX3-S2EN follow-up then brought the candidate to revision 19 by applying the upstream 17→19 delta verbatim (section "Multi-wave provenance"). This package's diff is therefore rev19 against a candidate whose rev19 content arrived by follow-up, and the diff's small size (+151/−150 in 20 hunks, Tier 1) is mostly the port's localization, not upstream drift. No production counterpart exists, so the R4 question does not arise. Reference-revision currency: revision 19 is the upstream latest, and it is the mirror itself.

Wave history: the port (184cb65); then a single bundled commit, 1869877, carrying six hunks for this file: the FIX-CREDIT-D translator normalization, the 改訳時参照リビジョン： 19 credit line, and the four FIX3-S2EN hunks (the Noto Sans JP import, the rev19 colour correction, the rev19 scrollbar-block removal, the Michroma stack extension). The Per-theme record verifies each hunk against the FIX3-S2EN report's §4.4 and §4.5 rows.

## Summary

A VHS-styled Black Highlighter theme by JackalRelated: BHL base by head-module `@import`, a documentation body with a font specimen and a fake VHS-log exhibit, one large CSS exhibit (564 lines, identical line count on both sides), and tail self-delivery by module `@import`. The port's own work is the standard EN8 shape (credit block, bare-Rate deletion, BHL host and frame repoints, bunny.net → Google Fonts in the exhibit, the stylesheet rehost). What makes the theme class U is the follow-up: between the port and the verdict, upstream moved from revision 17 to 19, and FIX3-S2EN both closed the JP-font finding and applied the upstream delta. A reviewer should look hardest at the two places where the register's language outruns the bytes (the P6 "FIXED" that edited nothing, section 2; the P7 "FIXED" that covers one stack of seven, section 4) and at the one translation error nobody's wave touched as built (section 6, since closed by the FIX-DYN landing in Post-package repairs).

## Classification

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 95 change blocks — 64 specific (67.4%), 28 heuristic, 3 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa. Labels are sets per block; the sections below were written from classification.json's label sets, not from the skeleton's per-section lists.

| Label | Blocks |
|---|---|
| TRANSLATION-ANCHORED | 32 |
| TRANS-UNANCHORED | 30 |
| WS-ONLY | 13 |
| DRAFT-HOST | 8 |
| INCLUDE-REPOINT | 5 |
| DELIVERY-HOST | 4 |
| EXHIBIT-RESTRUCTURE | 4 |
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| HEADERVAR | 1 |
| IFTAGS | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |

Topology (classification.json): four components on each side, matching by kind — two head modules (the BHL imports; the exhibit's font imports sit inside the code block), the single code-css exhibit (orig L328-892 / cand L339-902, 564 lines each), and the tail self-delivery module. No component moved, was added, or was dropped; the rev19 scrollbar-block removal is inside the exhibit, not a component change.

## 0. Header / provenance

- What: the package diffs the mirror of `theme:dynamikron` at revision 19 against the canonical candidate `pages/theme:dynamikron-jp.txt`. No delivery relocation: the component census matches by kind and position.
- Why: the mirror is the re-translation reference revision; provenance for every row lives in review/sources.tsv, and this package's original.txt hash equals that row's value.
- Verify: `sha256sum review/dynamikron-jp/original.txt` against review/sources.tsv; `cmp review/dynamikron-jp/candidate.txt pages/theme:dynamikron-jp.txt`.
- Disposition: PASS at the ledger determination (GOSIGN2-LEDGER (b) row 82); stamp STALE after the post-build FIX-DYN repair, with the record verdict standing.

## 1. Credit and attribution

- What: CREDIT-PREVIEW / TASL-FIELDS (B1): the eight-field preview credit block at cand L3-12, where the original carries none. The author field reads `**著作権者:** JackalRelated`, matching the original's attribution. The block carries BOTH revision lines, 初訳時参照リビジョン： 17 and 改訳時参照リビジョン： 19 (cand L10-11); the second line is itself one of the FIX3-S2EN follow-up hunks. The source link's text is 「ソース」, the population-standard form.
- Why: P3 / ruling 3 (the TASL record). The original's bare Rate is deleted (BARE-RATE-DEL, B8): the preview module already bears a rate (KB-09).
- Verify: read cand L3-12; all eight fields present, and the two revision lines state the two-step provenance the Provenance section describes.
- Disposition: the ledger (c3) records no P3 item for this theme beyond the credit-notation pair shared across the EN8 batch (translator in non-user form, since normalized by FIX-CREDIT-D inside 1869877; the 「ソース」 link text, the settled population form).

## 2. Includes and components

- What: INCLUDE-REPOINT ×5: the two interwiki-style frame includes at cand L21 (priority=1, normalize) and cand L26 (priority=2, BHL), repointed to the same-site form with JP theme= arguments; the usage exhibit's escaped includes (B17, COMPONENT-SWAP / ESCAPED-INCLUDE: the exhibit now names `:scp-jp:theme:black-highlighter-theme` and `theme:dynamikron-jp`, cand L99-101); the tail's hidden toggle-sidebar-bhl include after `[[/iftags]]`, carried in the original's own hidden-div form. There is NO priority=3 own-CSS interwiki-style include: the theme's own CSS loads by the tail module `@import` (section 3), which is the original's own tail structure (orig rev17 L906-908, rev19 likewise).
- Why: the ledger (c3) records "P6 FIXED (frame waves; checker-verified)". The bytes contain no frame edit after the port, and no commit adds a priority=3 frame. The checker's actual P6-relevant rules (staff skill scripts/check_source.py) are only: warn on interwiki-style parameters outside {priority, theme, css}, warn when a theme page has no interwiki-style at all, and warn on touching.scpnet-interwiki selectors. No checker rule requires a priority=3 own-CSS frame. The FIXED is therefore a verification outcome under the checker's criterion (frame present in JP form, arguments valid), not an edit; the localize lane's stricter BHL-cascade recommendation (add priority=3; expressly "not a posting blocker") was not taken. This section states exactly that, so a reviewer does not hunt for a frame edit that does not exist.
- Verify: `grep -n "interwiki-style" review/dynamikron-jp/candidate.txt` — two includes, priorities 1 and 2; `grep -n "priority=3" review/dynamikron-jp/candidate.txt` — no hits.
- Disposition: P6 FIXED per the ledger, on the verification ground stated above.

## 3. Delivery and code loading

- What: DELIVERY-HOST ×4 and SELF-DELIVERY ×1 (B95): the head module's BHL pair moved from nu-scptheme.github.io to scp-jp.github.io/Black-Highlighter (cand L17-18); the tail module self-delivers the exhibit by `@import` of own /1 on the draft host (cand L911), with the hidden toggle-sidebar include beside it. The address is correct: exactly one `[[code]]` block (cand L339-902), so /1 names the block that holds the CSS.
- Why: the JP BHL host serves the JP edition of the base (ruling 1's substance); the draft-host self-delivery is class (iii) (KB-41), sanctioned at draft stage.
- Verify: `grep -n "@import" review/dynamikron-jp/candidate.txt` — head pair on scp-jp.github.io, exhibit imports on googleapis (section 4), tail import own /1. Brace-depth scan of the exhibit ends at depth 0 with 46 top-level rules, the same count as the original's exhibit.
- Disposition: T1 baseline pseudo-ref×8 (T1-ROWS row 102) is this delivery's draft-form references, dispositioned at class (iii) in register (c1).

## 4. Fonts and assets

- What: three layers. (1) The port's exhibit imports (B79, FONT-IMPORT): the original's six fonts.bunny.net imports repointed to fonts.googleapis.com (cand L346-351: Wix Madefor Text, Michroma, Anonymous Pro, Jura, IBM Plex Mono, DotGothic16), and the theme's own stylesheet-new.css rehosted from scp-wiki.wdfiles.com to the draft host (cand L352). (2) The FIX3-S2EN font fix (B2, JPFONT-LOAD; B93, JPFONT-STACK): a Noto Sans JP `@import` added at the head module (cand L16, ahead of the BHL pair), and the Michroma declaration at cand L853 extended to `'Michroma', "Noto Sans JP", sans-serif`. (3) What the fix did not touch: the seven variable stacks at cand L367-373 — `--body-font` ('Wix Madefor Text'), `--header-font` ('Clarendon'), `--title-font` ('Alte Haas Grotesk'), `--mono-font` ('Anonymous Mono'), `--UI-font` ('Jura'), `--logs-dialogue-font` ('IBM Plex Mono') carry no JP face; only `--logs-speaker-font` ('DotGothic16') is JP-capable, as it already was in the original. A second Michroma stack, `--UI-font` at cand L639, was likewise not extended.
- Why: P7 (KB-16) asked for a JP font supplement. The wave's documented scope (FIX3-S2EN §4.4) was the import plus the one cited stack, and the bytes match that scope exactly. But the ledger's unqualified "P7 FIXED" reads as coverage the edit does not provide: Japanese glyphs in body, header, title and UI text still fall back past the Latin faces to the generic family tails (sans-serif / serif / monospace), not to the loaded Noto Sans JP. This package records the coverage as it stands: the family is loaded and one display stack names it; the remaining stacks rely on generic fallback.
- Verify: `grep -n "Noto Sans JP" review/dynamikron-jp/candidate.txt` — two hits (the L16 import, the L853 stack). `sed -n '367,373p'` shows the seven stacks.
- Disposition: P7 FIXED per the ledger, on the wave's documented scope; the partial coverage is recorded here and in the batch report as a prose-vs-bytes discrepancy, not edited by this package. Two upstream quirks are carried byte-faithful and noted, not flagged: the mono stack names 'Anonymous Mono' while the import loads 'Anonymous Pro' (both sides, orig L338 / cand L348 against orig/cand stack lines), and 'Clarendon' and 'Alte Haas Grotesk' are named in stacks but loaded by no import on either side (original state).

## 5. Header, sidebar, site furniture

- What: HEADERVAR ×1 (B80) is an asset line inside the exhibit (the header logo URL, rehosted to the draft host). The header variables themselves are intentional blanks on both sides: `--header-title: " "` and `--header-subtitle: " "` — the theme's header is a VHS cassette image, not text.
- Why: the LOCALIZE lane's P9 read for this theme is N-A on exactly this ground; there is no untranslated header string to disposition.
- Verify: `grep -n "header-title\|header-subtitle" review/dynamikron-jp/candidate.txt` — blank values, matching the original.
- Disposition: nothing to disposition.

## 6. Text translation

- What: TRANSLATION-ANCHORED ×32 and TRANS-UNANCHORED ×30: the documentation body, the font specimen labels and the VHS-log exhibit are translated throughout (です・ます register). The rev19 colour correction rides inside this mass as a value change, not text: `--t20-ylo: 247, 185, 0` → `247, 187, 0` (cand L386), one of the FIX3-S2EN follow-up hunks, applied verbatim from the upstream delta.
- Why: P10 (KB-18) for the translation; the colour hunk is upstream parity (revision 19 changed the value; a port frozen at 185 would diverge from the reference it cites).
- Verify: `grep -n "t20-ylo" review/dynamikron-jp/candidate.txt review/dynamikron-jp/original.txt` — 187 on both sides.
- Disposition: T5 FINDINGS at the ledger row, closed by the joint T4/T5 verdict — with one exception the as-built record must state plainly. **As built, the Eddie Murphy quote at cand L173 read 「ねえ、みんなパーティーしたがるの…」 where the original (rev19, the "My girl wants to party all the time…" line) has "My girl" as the subject; みんな ("everyone") changed who wants to party.** The LOCALIZE-S2-A lane flagged the line as a clear meaning divergence and proposed a correction, and no register line dispositions it by name (the ledger's T5 line for the theme is the joint verdict only). **Closed by landing `49a1e49` (FIX-DYN, Post-package repairs below):** the current candidate L173 reads 「ねえ、おれの彼女はパーティーしたがるんだ。…」, taking the proposal's subject and verb form; "all the time" stays compressed, as in both the previous translation and the proposal. The flag no longer stands against the current bytes; this package does not edit the candidate.

## 7. Links

- What: no link signature fired as a primary; the documentation's external references are carried. The usage exhibit's includes name the JP forms (section 2). No EN page link in the prose lacks a counterpart decision: the theme's prose links are the author's own reference links, carried as in the original.
- Why / Verify: `grep -n "scp-wiki.wikidot.com" review/dynamikron-jp/candidate.txt` — the remaining hits are the credit source link (required) and the tail self-delivery's original-side counterpart lines in exhibits.
- Disposition: no P11 item stands against this theme in the ledger (c3).

## 8. Structure

- What: EXHIBIT-RESTRUCTURE ×4 (B3, B5, B12, B94), each on a frame include or the usage exhibit's include lines: mere repoints, adjudicated against the census (one code exhibit each side, same 564-line size; two frame includes each side; one self-delivery each side). No exhibit was restructured or dropped. The one genuine structural deletion inside the exhibit is the rev19 follow-up's removal of the `html::-webkit-scrollbar, body::-webkit-scrollbar { width: 18px; background: #transparent; }` block: upstream deleted it between revisions 17 and 19 (its `background: #transparent` was never valid CSS), and FIX3-S2EN applied the deletion verbatim.
- Why: R3's ground-stating rule; and upstream parity for the scrollbar block (the candidate cites revision 19, so it must not carry a block revision 19 removed).
- Verify: `grep -n "webkit-scrollbar" review/dynamikron-jp/candidate.txt review/dynamikron-jp/original.txt` — the themed scrollbar rules remain; the deleted block's exact `#transparent` form appears on neither side.
- Disposition: the follow-up hunks are FIXED per FIX3-S2EN §4.5 ("both applied verbatim", sourced from diff-dynamikron-from17.txt).

## 9. Formatting only

- What: WS-ONLY ×13, all inside the carried exhibits and documentation (padding normalization of the port). Re-indentation: 0 blocks.
- Why / Verify / Disposition: whitespace-only; the classifier's count is in classification.json. Nothing to disposition.

## 10. Porter annotations

- What: none as a signature, and a hand check agrees: no porter comment block was added; the JP font supplement at cand L16 carries no annotation comment (contrast the fandom package in this batch). The credit block's 改訳時参照リビジョン： 19 line is a TASL field, not an annotation.
- Verify: `grep -n "localization\|JP localization" review/dynamikron-jp/candidate.txt` — no hits.
- Disposition: nothing to disposition; the section is present with its ground, per the format.

## 11. Dispositions and exceptions

- T1 pseudo-ref×8: DISPOSITIONED, class (iii) (register (c1) preamble; T1-ROWS row 102 baseline: exit 1, 8 errors / 1 warn / 2 infos).
- Render items (RENDER-S2-B, EN8 block): the credit modal wider than the 320px viewport in both engines and the WebKit CC "S" reading DISPOSITIONED under KB-36; the notice clip at ≤375px with them; asset 404/ORB items DISPOSITIONED as the EN8 deferred class (KB-47 family).
- T4 P6: FIXED on the verification ground stated in section 2. T4 P7: FIXED on the wave's documented scope, with the coverage caveat stated in section 4.
- The T5 quote defect (section 6) was not dispositioned by any register line; it was this package's open flag, carried to the batch report. It did not disturb the ledger verdict as recorded, which judged the joint T4/T5 FINDINGS with the lane's flag already on record. The flag is now closed by landing `49a1e49` (FIX-DYN, Post-package repairs): the current candidate's L173 subject is おれの彼女, matching the original's "My girl".

## 12. Verification

- T1 (source check): baseline 2026-11-16, T1-ROWS row 102: exit 1, 8 errors / 1 warn / 2 infos (pseudo-ref×8); standing classes dispositioned in register (c1). Re-runnable with the staff checker's check_source.py against candidate.txt.
- T2/T3 (render): RENDER-S2-B EN8 block (RENDER-ROWS-1): FINDINGS, items dispositioned as in section 11.
- T4 follow-up (reference-revision currency): the candidate was brought to the current revision by the FIX3-S2EN follow-up itself (diff-dynamikron-from17.txt, applied verbatim); upstream latest is revision 19, this package's mirror.
- Package checks: `python3 review/build_review.py --check` passes for this package; candidate.txt is byte-identical to the canonical file; original.txt's SHA-256 equals the sources.tsv row.

## Per-theme record

1. **The wave edits, verified hunk by hunk.** The complete 184cb65..HEAD diff for this file (commit 1869877) has exactly six hunks: (1) 翻訳責任者 `SCP-JP` → `AI` (FIX-CREDIT-D); (2) 改訳時参照リビジョン： 19 added to the credit block; (3) the Noto Sans JP `@import` added at the head module, ahead of the BHL pair (cand L16); (4) `--t20-ylo` 185 → 187 (cand L386); (5) the `html::-webkit-scrollbar…#transparent` block removed; (6) the Michroma declaration extended with `"Noto Sans JP"` (cand L853). Hunks (3) and (6) are FIX3-S2EN §4.4's Class 4 font fix; hunks (2), (4) and (5) are §4.5's Class 5 upstream follow-up, which the report sources to diff-dynamikron-from17.txt and marks "both applied verbatim". Every hunk the report claims is present in the bytes, and the bytes contain no hunk the report does not account for, apart from hunk (1), which belongs to the credit wave whose name the commit subject carries.
2. **The commit subject names one wave; three rode in it.** 1869877's subject is the FIX-CREDIT-D translator normalization (163 files). A reader working from subjects alone will miss that this file's FIX3-S2EN edits are inside it. The narration above exists so the package, not the subject line, is the record.
3. **P6's FIXED is a verification, not an edit** (section 2). No priority=3 frame exists; the checker's criterion does not require one; the lane's stricter recommendation was expressly not a posting blocker and was not taken.
4. **P7's FIXED covers one stack of seven** (section 4). The import is real and the cited stack is extended; the variable stacks the lane enumerated were not.
5. **The T5 quote defect was unrepaired and undispositioned by name as built** (section 6). It was the batch's clearest defect flag: a meaning-changing translation error, identified by the check lane with a proposed correction, that no fix wave in the package era picked up. It was closed after the build by landing `49a1e49` (FIX-DYN, Post-package repairs), which repaired candidate L173 to the proposed subject; the current bytes carry おれの彼女.

### Post-package repairs (REFRESH3-F)

**FIX-DYN, landing `49a1e49` (report `R/review-scout/FIX-DYN.md`, item 1, "the
Eddie Murphy quote").** This landing postdates the package build
(`a0a5549`, the U-5 batch commit) and repairs item 5's T5 flag. One
candidate change at L173: the quote's subject
`"ねえ、みんなパーティーしたがるの。…"` →
`"ねえ、おれの彼女はパーティーしたがるんだ。…"` (the three-beat structure
is kept). The original is "My girl wants to party all the time…" —
LOCALIZE-S2-A had flagged みんな ("everyone") as a meaning-changing error
with a proposed correction, which no wave had picked up; the landing
takes the proposal's subject and verb form. "all the time" stays
compressed, as in both the previous translation and the proposal.
Checker per the report: error 8 / warn 1 / info 2 before and after, full
finding list byte-identical (standing pseudo-ref baseline, class (iii)).
This package documents the corrected candidate; its stamp reads STALE
against the pre-repair verdict, by design.

## Change set outside the two diffed files

One companion candidate: `pages/theme-decoration-sample-dynamikron-jp.txt`, the decoration sample that applies this theme on the check wikis. The EN-named `pages/theme:dynamikron.txt` and `pages/theme-decoration-sample-dynamikron.txt` are composition members of the display-check wikis, not the JP candidate.

## Sample-page gap — `component:theme-squares`

The candidate's own documentation exhibit (cand L57) includes `component:theme-squares`, repointed from the original's `:scp-wiki:component:theme-squares` (orig L47) to the campaign's bare working form. `component:theme-squares` is the EN SCP Wiki's colour-swatch component used inside theme documentation; it is not a theme row. No JP port of it exists anywhere in this repository — a scan of `pages/`, `pages-existing/` and every `review/*/candidate.txt` finds no `component:theme-squares-jp` page, and neither check wiki carries a `component:theme-squares*` page. The candidate's colour data is not lost: the swatch variables and values are carried in the file itself (the exhibit's parameter lines at cand L58 ff.).

**Disposition: recorded gap, not a candidate defect.** This lane does not fabricate a component port from nothing; the campaign's ruling-4 route would port the component with the theme at posting if a port is wanted. Until then, `theme-decoration-sample-dynamikron-jp` shows a missing-include notice for that one exhibit. The notice is explained in the dynamikron row's Details column of the /start theme table (generated by `build_start.py` from its `SAMPLE_GAPS` record) so a porter is not left guessing; it does not change the ledger verdict or the posted-on-record-verdict treatment of this row.

## Multi-wave provenance

- Port (from rev17): Stage 2 EN8 integration, commit 184cb65 — credit block, bare-Rate deletion, BHL host repoint, frame repoints, exhibit font-host repoint, stylesheet rehost.
- Check waves: T1 baseline (T1-ROWS row 102); render walk RENDER-S2-B (RENDER-ROWS-1, EN8 block); localize walk LOCALIZE-S2-A (LOCALIZE-ROWS row 82), which raised P6, P7 and the T5 quote flag.
- Fix waves: FIX3-S2EN §4.4 (font) and §4.5 (rev19 follow-up), plus FIX-CREDIT-D (translator normalization), all inside commit 1869877.
- Ledger determination: GOSIGN2-LEDGER (b) row 82, PASS, no section (e) items; go-sign COMPLETION-REPORT.md §10.

## Appendix — residue and heuristic blocks

- R1 — B18 (residue; orig L95 → cand L105): the collapsible label "+ Examples" → "+ 例". A one-line exhibit label translation with no anchor; resolved to section 6 by shape.
- R2 — B61 (residue; orig L208 → cand L218): the VHS-log exhibit's "**> RECORDING STARTED <**" → "**> 録画開始 <**". In-fiction UI text, translated; section 6.
- R3 — B66 (residue; orig L225 → cand L235): the log exhibit's "SPEAKER" → "話者". Same shape as R2; section 6.
- The 28 heuristic blocks resolve by shape: TRANSLATION-ANCHORED and TRANS-UNANCHORED mass in the documentation and exhibits (section 6), WS-ONLY padding (section 9), and CSS comment translations inside the exhibit. No new signature is proposed from this theme; the three residue blocks are all the same shape (short in-fiction or label strings translated without anchors), already covered by the section-6 narration rule.

## License and attribution

- **Title:** Dynamikron Theme
- **Author:** JackalRelated
- **Source:** https://scp-wiki.wikidot.com/theme:dynamikron — revision 19 (revision date 2026-11-15 20:06:24)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
