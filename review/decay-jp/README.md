# Review package — theme:decay-jp
New to this package's shorthand? Read the notation key first: [How to read a review package](../HOW-TO-READ.md).

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:decay-jp — origin CN, population #180 [GOSIGN2-LEDGER (b) row 180]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now e1c4e825567dd3d6ab31855105f0af885b7c1c4cfdffaf67a1893fa69e4fd392); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 11 errors / 2 warns / 2 infos (pseudo-ref×11); standing classes dispositioned in register c1 [T1-ROWS row 215; GOSIGN2-LEDGER (b) row 180]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 331px@320 (page) and 331px@320 + 884px@768 (sample); runtime-hotlink site-theme chain; sample credit-modal (preview-form). [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-E (CN4))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 179, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 179]
- FIX5 re-judgement: item 53 (class B) FIXED — FIX5-FURNB, commit 25bb0b4: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 53]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:decay-jp.txt sha256:e1c4e825567dd3d6ab31855105f0af885b7c1c4cfdffaf67a1893fa69e4fd392; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 53 [B] (duplicate bare Rate) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 53: **FIXED** (FIX5-FURNB, commit 25bb0b4); re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c3): P3 credit fields FIXED (credit waves); P10 DISPOSITIONED (lane-recorded severity / specimen class); ledger §(c2) render row: page-overflow (KB-33/KB-34 family), runtime-hotlink site-theme chain (KB-40), credit-modal preview form (KB-32) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Post-verdict change | The usage-example sweep completed the visited-link exhibit's slug to `theme:decay-jp` (canonical commit b5cb724); the stamp therefore reads STALE against the pre-sweep verdict, by design (see "The usage example's posting name") |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:decay | theme:decay-jp |
| Wiki | scp-wiki-cn.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 8, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 8 | — |
| Source of this copy | Mirror store `orig-decay-rev8.txt` (class COPY, byte-true copy of the campaign cache `gosign2-lanes/lane-oc-gs-localize-s2-D/orig-decay.txt`, fetched once by the LOCALIZE-S2-D lane) | Canonical file `pages/theme:decay-jp.txt`, copied at worktree HEAD e821e37 |
| Lines / bytes | 473 lines / 12,352 bytes (the last line carries no trailing newline, so `wc -l` reports 472) | 482 lines / 14,365 bytes |
| SHA-256 | 111c51c6c448335c799a6074e370b6f581d79315ce1e63ec43720512d806143d | e1c4e825567dd3d6ab31855105f0af885b7c1c4cfdffaf67a1893fa69e4fd392 |

One record correction belongs here. The `review/sources.tsv` note for this row claims the original was "superseded upstream since the reference revision", but the follow-up artifact that note itself cites (`diff-decay-from8.txt` in the campaign record) records rev 8 → rev 8, no changes: upstream latest remains revision 8 and this mirror is current. The note's wording is the defect (the same wrong-note shape corrected earlier for ambrose, alcur, and inland-empire); it is flagged for central correction and the package proceeds on the artifact's evidence.

## Summary

Decay is a page-source theme whose own stylesheet lives in a trailing code exhibit that the page imports back into itself; the port keeps that topology exactly, re-hosts every delivery line to the JP draft host, and adds the campaign's standard supplements around it (preview credit block, interwiki-style frame, JP font loads, re-hosted base stylesheets). The measured churn (diff.md: +135/−135 in 15 hunks) is mostly the translation of the long exhibit body plus those supplements. The one blocking defect the sweep found, a duplicated bare Rate module, was removed by FIX5 and is re-derived below. The remaining oddities a reviewer will spot (Chinese link text in two derivation links, one Chinese word inside a translated sentence, the CN canon name in `--header-title`) were all charged by the T4 lane and stand dispositioned with their grounds stated, not hidden.

## Standing sections

### 0. Header and provenance frame

- **What:** The original opens with a `[[module ThemePreviewer]]` (original L1) pointing at the Super Liminal base stylesheet on the author's GitHub mirror, then a `[[module css]]` (L2–4) importing the page's own code block 2 from the CN files host. The candidate drops the ThemePreviewer (a preview-only module with no delivery role in the JP environment) and keeps the self-import, re-hosted: `[[module css]]` importing its own /2 from the draft host (candidate L1–3), followed by the interwiki-style frame at priority 1 naming the same /2 (candidate L5–8). The whole page sits inside the tag gate on both sides (original L6 → L473; candidate L10 → L482). Provenance route: derived from the original at reference revision 8 (mirror class COPY; see Provenance).
- **Why:** The header frame is where the original declares its delivery; the candidate's replacement delivery is recorded in section 3. The frame is the P6/T3 supplement (patterns/ KB-07 family; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa).
- **Verify:** Read original L1–9 against candidate L1–10.
- **Disposition:** Recorded; the delivery change is argued in section 3.

### 1. Credit and attribution

- **What:** The original carries a branch credit block (`:scp-wiki-cn:credit:start`/`end`, original L11–18) naming both authors, **作者**: lestday233、YanL777, with the license and derivation prose inside the block (original L15, L17). The candidate carries the preview credit block (`:scp-jp:credit:start-preview`/`end-preview`, candidate L11–21) with the eight standard fields; **著作権者** is [[*user lestday233]]・[[*user YanL777]], both of the original's authors, and the block's prose line (candidate L20) is the merged translation of original L15 and L17 (YanL777's icon/image credit, the Super Liminal derivation, the CC BY-SA 3.0 statement). No author named by the original is dropped. There is no license-box include on either side; the license statement rides in the credit prose, as in the original. The candidate's **タイトル** field keeps the original title 衰残 版式 (the **原題** field quotes the same); the terminology point is the dispositioned type-10 item in section 11.
- **Why:** P3/T1 credit swap (the preview module is the rate-bearing JP form) and ruling 3 (2026-11-16) for the eight fields and the 翻訳責任者： AI credit. The T4 lane had charged six missing credit fields against the early candidate; the credit waves completed them (ledger §(c3): P3 FIXED).
- **Verify:** Read candidate L11–21 against original L11–18; count the eight fields.
- **Disposition:** FIXED (credit waves; ledger §(c3)). The Rate half of that T4 charge is item 53, in the per-theme record.

### 2. Includes and components

- **What:** Original includes: the credit pair (L11/18), the escaped usage include `@@[[include :scp-wiki-cn:theme:decay]]@@` (L27), and `:backrooms-wiki-cn:component:image-block` for the logo exhibit (L32–35). Candidate includes: the interwiki-style frame (L5), the credit pair (L11/21), the escaped usage include `@@[[include :scp-jp:theme:decay-jp]]@@` (L30), and `component:image-block` in the bare same-wiki form (L35) with its image re-hosted to the draft host (L36) and its caption translated (ロゴ). The classifier labels the image-block block EXHIBIT-RESTRUCTURE; adjudicated against the exhibit census, the exhibit is retained with the same role and caption — the change is an include repoint plus an asset re-host, not a dropped or replaced exhibit.
- **Why:** P1 include repoints (branch forms of shared components resolve on scp-jp) and P5 asset re-hosting. No include in the candidate points at a CN-wiki page.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; the escaped usage include's name history is in the per-theme record.

### 3. Delivery and code loading

- **What:** Own-code delivery on both sides. Original: the head module imports `scp-wiki-cn.wdfiles.com/local--code/theme%3Adecay/2`. The code census in document order is: block 1 = the `[[code]]` text exhibit (original L177–180), block 2 = the `[[code type="CSS"]]` stylesheet exhibit (original L216–472), so /2 names the CSS exhibit and the address is live. Candidate: the head module and the frame both name `sigma10-jp-test.wdfiles.com/local--code/theme%3Adecay-jp/2`; its census is block 1 = the text exhibit (candidate L180–183), block 2 = the CSS exhibit (candidate L219–481), so /2 again names the CSS block. The FIX-CODEADDR population audit does not list decay in its no-target class; the address resolves to the block that holds the CSS. The base stylesheet the exhibit itself imports also moves: the original imports `super-liminal.css` from `github.backroomswiki.cn` (original L230), the candidate imports three re-hosted files from the draft host (candidate L237–239: `super-liminal.min.css`, `icon-masks.min.css`, `colmod-style.min.css`). Draft-host URLs are the draft-form class (iii), rewritten to the production host at posting.
- **Why:** P4/T9 delivery repointing and P5 re-hosting: the candidate's runtime no longer depends on the author's GitHub mirror or the CN files host. The topology pass confirms the same component kinds on both sides with no relocations.
- **Verify:** Read candidate L1–8 and L233–240; run the code census with `grep -n '\[\[code' candidate.txt` and match /2 to the second block.
- **Disposition:** DISPOSITIONED in part (the draft-host lines stand as the T1 pseudo-ref class, section 11); the topology itself is the port's standing form.

### 4. Fonts and assets

- **What:** Neither page file declares a `font-family` (grep count 0 on both sides): the stacks live in the base stylesheet. What the candidate adds at the exhibit head is the loads (candidate L233–236: Inter, JetBrains Mono, Noto Sans JP, Noto Serif JP from Google Fonts) where the original loaded no font in-file; the classifier's JPFONT-LOAD/FONT-IMPORT labels fire inside block B57 alongside the delivery re-host. Assets: the author's file URLs on `lestday-lab.wdfiles.com` (logo, body background, note logos, style-block backgrounds; original L267–445 region) are re-hosted one-for-one to draft-host `local--files/theme%3Adecay-jp/` (candidate L276–454). Font Awesome 7.0.0 from cdnjs is kept identically on both sides (original L231, candidate L240).
- **Why:** P7/T5 (the JP font supplement operates at the delivery layer for this theme, since the stacks are the base's) and P5 (asset re-hosting to JP storage; at draft stage the draft host stands in for it). The T1 baseline's 11 pseudo-ref errors are these draft-host lines (section 11).
- **Verify:** `grep -c 'font-family' original.txt candidate.txt` (0 / 0); `grep -n '@import' candidate.txt` for the nine import lines.
- **Disposition:** Standing (loads added); the draft-host asset lines are class (iii) as recorded in section 11.

### 5. Header, sidebar, and site furniture

- **What:** The theme's header variables sit in the CSS exhibit's `:root` (original L265–267 → candidate L274–276). `--header-title: "心隙三局"` is kept byte-identical: it is the CN canon name of the bureau (心隙三局， the "third control and research bureau" of the theme's own credit prose) for whose setting the theme was commissioned. `--header-subtitle` is glyph-converted, `"应许 遗故 物哀"` → `"応許 遺故 物哀"` (R5: 应→応， 许→許； the classifier's GLYPH-FORM span in block B61). `--logo-image` is re-hosted (section 4).
- **Why:** P9/T6 variables are the theme's own; the title's language is dispositioned under ruling 2 (2026-11-16), which places header and title language outside migration correctness (KB-57 family). The T4 lane had recorded the retention as needing staff approval (LOCALIZE-ROWS row 179); the ruling is the approval framework that closed it.
- **Verify:** Read candidate L274–276 against original L265–267.
- **Disposition:** DISPOSITIONED (ruling 2; ledger §(c3) closes the row's charges with this theme's P10 disposition).

### 6. Text translation

- **What:** The exhibit body is translated throughout: 16 TRANSLATION-ANCHORED blocks pair one-to-one (usage prose, headings, collapsible labels, tab text), and the 37 TRANS-UNANCHORED blocks are the same translation mass in restructured lines (the repeated tab filler sentences, the blockquote examples, the NOTE heading). The code exhibit's banner comment is kept verbatim in English on both sides (it is the original's own license banner), and no COMMENT-TEXT label fires in this package: the original's CSS carries no Chinese comments to translate. R5 glyph-form conversions beyond the subtitle: block B53 (original L188 → candidate L191). Two charged residues stand in the translated text, both named here rather than passed over: the derivation link text `恐怖症 主题版式` at candidate L20 and L25 keeps the simplified-Chinese `主题` inside the phobia theme's quoted name (its companion link 超閾限 was glyph-converted), and the word 部件 survives inside the translated horizontal-rule sentence at candidate L40.
- **Why:** P10 body translation; KB-18 for reader-visible strings. The residues are exactly the items LOCALIZE-ROWS row 179 charged as reader-visible Chinese residue (display-affecting, minor).
- **Verify:** Read candidate L23–218 against original L20–214 section by section; `grep -n '主题版式\|部件' candidate.txt` returns L20, L25, L40.
- **Disposition:** DISPOSITIONED (ledger §(c3): P10, lane-recorded severity / specimen class). The 「版式」 terminology variance charged in the same row (type 10) stands with it: the candidate uses the original's 版式 term throughout, including the credit title field.

### 7. Links

- **What:** The candidate's source link points back to the original page (credit block, candidate L19, host scp-wiki-cn.wikidot.com, the recorded host in sources.tsv). The visited-link exhibit (original L41 `[[[theme:decay|已访问的链接]]]` → candidate L44 `[[[theme:decay-jp|アクセス済みのリンク]]]`) now names the candidate's posting name; its history is in the per-theme record. The derivation links in the credit prose (Super Liminal and Phobia on backrooms-wiki-cn) are kept as quotations of the original's derivation statement on both sides; they are credit prose, not delivery, and have no JP counterpart to repoint to.
- **Why:** P11 link repoints apply to the port's own reference surface; dead-target exhibits fail at click time, which is why the slug completion mattered.
- **Verify:** `grep -n 'theme:decay' candidate.txt` (the -jp self-references and the CN source URL only).
- **Disposition:** Standing; the exhibit slug is FIXED by the sweep as recorded below.

### 8. Structure

- **What:** The localize.md closing rule holds: component order, selector and variable names, and the single code-css exhibit structure are preserved (the topology pass reports the same component kinds on both sides and no moves). The structural additions are the supplements (frame, credit block) and the removals are the ThemePreviewer and the bare Rate (sections 0 and 1). The exhibit census matches: the logo image-block exhibit is retained (section 2), the text code exhibit and the CSS exhibit are both present in the same positions. The original defines no include-parameter gates and no `{$...}` slot definitions (grep count 0 on both sides), so there is no documented mechanism whose definitions could be absent; its only mechanism is the tag gate itself, carried over as +版式 → +テーマ (P2).
- **Why:** Structure preservation is what keeps a follow-up diff applicable; naming the additions and removals here is what separates them from silent restructuring (R3).
- **Verify:** Compare the structural maps: `grep -n` for `[[module`, `[[code`, `[[iftags`, `[[tab` in both files.
- **Disposition:** Standing.

### 9. Formatting only

- **What:** Minor. WS-ONLY accounts for 12 of the 74 change blocks (blank-line and spacing pairings at exhibit boundaries); the classifier reports 0 re-indentation blocks. There is no wholesale re-indentation in this package.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change (R7 is not triggered).
- **Verify:** The WS-ONLY rows of the class summary in classification.json.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** None. The candidate contains no `[!-- ... --]` comments and no 訳注 lines (grep count 0), and the classifier's ANNOTATION label did not fire over the 74 blocks; annotations riding inside other labeled blocks were checked for explicitly before writing this section. The only added explanatory text is the credit block's standard field set.
- **Why:** R2 additions must be listed so they are never mistaken for original content; here the ground for "none" is the grep and the classifier together.
- **Verify:** `grep -n '\[!--\|訳注' candidate.txt` returns nothing.
- **Disposition:** None (checked, absent).

### 11. Dispositions and exceptions

- **What:** The standing dispositions for this theme, each argued in its own section: (1) the T1 baseline is 11 errors / 2 warns / 2 infos with all 11 errors `pseudo-ref` — the draft-host local--code and local--files lines, class (iii) draft form (KB-41), rewritten at posting, never "fixed" in the candidate; (2) the render row's dispositions: page-overflow 331px@320 on the page and 331px@320 + 884px@768 on the sample (the cross-cutting static-credit/preview-chrome families, KB-33/KB-34), the runtime-hotlink site-theme chain (KB-40, environment layer, not the candidate), and the sample credit-modal preview form (KB-32; ruling 5: credit:start-preview has no modal mechanism); (3) the T4 residue items (主题版式 ×2, 部件, 版式 terminology) under P10; (4) the `--header-title` CN canon name under ruling 2. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding check in its own section.
- **Disposition:** DISPOSITIONED (all items above).

### 12. Verification

- **What:** The evidence behind the stamp: (a) the FIX5 closure is re-derived from this package's own bytes in the per-theme record (grep-based, re-runnable); (b) the classifier (classify_hunks.py 0.1.0, signature table 2026-11-17.1, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa) labels all 74 change blocks, 40 specific / 34 heuristic / 0 residue, so no block in this package is unadjudicated; (c) a brace-depth scan of the code-css channel ends at depth 0 on both sides and never goes negative, so no displaced closing brace is hiding in the exhibit; (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares. Counts in this README are the generator's (difflib): +135/−135. A GNU-diff count of the same pair gives 211 changed lines; the difference is alignment choice, not content.
- **Why:** Verification claims must name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the greps cited above and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (go-sign re-run, supplement).

## Per-theme record

### The FIX5 closure (ledger item 53 [B])

At ledger time this candidate rendered two rating widgets: the preview credit module (rate-bearing by design) plus a bare `[[module Rate]]` standing in a `[[>]]` float inside the tag gate, the shape the LOCALIZE-S2-D row recorded as Rate 二重化 (type 3). The ledger's item 53 charged it as a defined FIX class that had been executed for other row sets but never for this row, and assembly-verified the bare module still present in the then-current file (cited at its L23). FIX5-FURNB (commit 25bb0b4) removed the bare Rate block, and the supplement re-judged item 53 FIXED.

Re-derived from this package's bytes: the original carries its own bare Rate at original L8, inside the float at L7–9 — normal for an original, whose credit module is not rate-bearing. In the candidate, `grep -n 'module Rate' candidate.txt` returns nothing at all: no bare module, and the float wrapper itself is gone; the only rating surface is the preview credit module at candidate L11. No labelled Rate exhibit existed in this file to be collateral (the original's Rate was the page's own widget, not a specimen). The removal the supplement records is present and complete in the current bytes.

The companion charge in the same T4 row, the six missing credit fields, closed earlier: ledger §(c3) records P3 FIXED by the credit waves, and the current candidate carries all eight fields (candidate L12–19, section 1).

### The usage example's posting name

The visited-link exhibit at candidate L44 is an escaped example line and was not part of the include census in section 2. At verdict time it read `[[[theme:decay|アクセス済みのリンク]]]`, naming the original's slug on the JP branch — a page that does not exist on scp-jp, the exact item LOCALIZE-ROWS row 179 charged as 自己リンク見本の不存在 slug. The usage-example population sweep has since completed the name to this candidate's posting name, `theme:decay-jp` (sweep report SWEEP-USAGE.md in the campaign record, R/review-scout/; canonical commit b5cb724). This package documents the corrected candidate; its stamp reads STALE against the pre-sweep verdict, by design.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is slightly larger. (1) `pages/theme-decoration-sample-decay-jp.txt` — the decoration sample page used by the render checks. (2) The re-hosted base files themselves (`super-liminal.min.css`, `icon-masks.min.css`, `colmod-style.min.css` and the theme's image files), which live as attachments under the candidate's draft-host file area, not as repo files. The theme is standalone in `start-themes.tsv` (no dependency column entries); no fragment or component candidate belongs to its change set.

## Multi-wave provenance

The candidate's current state is the product of successive waves, not of a single porting pass: the S2 localization wave (LOCALIZE-S2-D) produced the initial port (translation, delivery re-hosting, exhibit structure, and, as later found, the surviving bare Rate); the credit waves completed the eight credit fields; the frame waves added the interwiki-style frame (the FIX4-era frame set, which the ledger names only by count — ROLLOUT.md's known limit); the render checks ran as RENDER-S2-E (CN4); FIX5-FURNB removed the bare Rate (item 53); and the usage-example sweep completed the exhibit slug after the verdict. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 53; GOSIGN2-LEDGER-SUPPLEMENT.md row 53; LOCALIZE-ROWS row 179; T1-ROWS row 215. The go-sign re-run over that record is what the Status block certifies.

## License and attribution

- **Title:** 衰残 版式
- **Author:** lestday233・YanL777
- **Source:** https://scp-wiki-cn.wikidot.com/theme:decay — revision 8
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
