# Review package — theme:much-cool-jp (EN → JP port)

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:much-cool-jp — origin EN, population #23 [GOSIGN2-LEDGER (b) row 23]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 92b58e14fc064941785e3c54e57a421a078b035aed34f93faa2fde714f3ad513); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 1 warn / 2 infos (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 23; GOSIGN2-LEDGER (b) row 23]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — WebKit CC-badge stray "S" (cross-cutting), mobile notice left-clip, sidebar x=24, sample overflow 324/884px, sample credit-modal, contrast warn. [RENDER-ROWS-1 (RENDER-C row 23)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 23)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 23, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 23]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 23]
- Computed against: canonical commit 5ddc1a696cad699663b013c730797459316d46c6; candidate file pages/theme:much-cool-jp.txt sha256:92b58e14fc064941785e3c54e57a421a078b035aed34f93faa2fde714f3ad513; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination; this theme had no OPEN items and no §(e) register entry (GOSIGN2-LEDGER (b) row 23) |
| Standing items | **FIXED before the determination** — T4's one finding (pattern 3: credit fields missing at LOCALIZE-ROWS row 23) was closed by the credit completion in commit b816e10, the verdict stamp's computed-against commit; the completed block is what this package reviews. **DISPOSITIONED** — T1's pseudo-ref ×1 (the draft-host frame URL, class (iii)); the render row's items (section 11). **FLAGGED by this package** — one credit rule in the pre-correction selector form, inside a group that was otherwise restated (per-theme record, item 1). **NOTED** — the bare Rate exhibit is kept, on the production page's standing form (item 2) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:much-cool | theme:much-cool-jp (staging name; posting target theme:much-cool) |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 19 (the candidate's credit block records 初訳時参照リビジョン: 19) | — |
| Source of this copy | Fetched fresh for this review from the live EN page at revision 19 (mirror class FETCH-REGEN; hash-verified against review/sources.tsv) | Canonical file `pages/theme:much-cool-jp.txt`, copied at worktree HEAD 4e6b126 |
| Lines / bytes | 592 lines / 10,845 bytes | 632 lines / 12,647 bytes |
| SHA-256 | 864f46ed5ca549ad6cf3c1c7c75d825db16942402ab6386dcd572255f4a05f1a | fb64e90fcece1cec51c2edd0f0bced307e9a7a7a6ae96ad26b41e48eba4b42ae |

Provenance route (kind K6 in sources.tsv): this theme already exists on production SCP-JP as theme:much-cool, in a 2024 translation by nebula2700. The candidate is that production page carried into the Sigma-10 composition under the staging name theme:much-cool-jp; the migration's own record is `pages/phase17-diff-much-cool-jp.txt` (Phase 17), a diff against the current production page. The EN original has been superseded upstream since revision 19; sources.tsv records a follow-up diff artifact in the campaign record for that drift, which is outside this package's scope (the package judges the candidate against the reference revision it declares). Wave history: d727e92 (the canonical sources registration), 8dcac74 (Phase 17, the migration), b816e10 (the gosign2 T1 credit fixes; the verdict stamp's computed-against commit). No FIX5 commit touches this file.

## Summary

The batch's one adoption case: an EN theme whose JP counterpart already exists in production, so the port is a migration of the production page rather than a fresh translation. The candidate keeps the production page's furniture form (a bare Rate exhibit kept alongside the credit block, where the S2 population deletes the Rate), its human translator credit (nebula2700, 2024), its nine-field credit block (the ruling-3 eight plus the production page's own 作者 field), its JP credit CSS (a restated group with modal rules, inherited from the production page), its two narrow-viewport appendix modules with their maintenance annotations, and its storage-hosted assets (the theme's images already live on SCP-JP storage, so P5 is completed in the candidate rather than dispositioned). What the migration adds is the Sigma-10 frame and the draft-host delivery, the JP component repoint for the image-block exhibit, and the hub link's repoint to the JP hub. The one T4 finding (credit fields missing at the localize check) was fixed by the credit completion in b816e10 before the determination. Measured churn is small (diff.md: +75/−40 in 8 hunks; classification.json: 30 change blocks), because most of the file is the production page carried over unchanged.

## Class summary

Auto-classification by review/classify_hunks.py (signature table 2026-11-17.1): 30 change blocks — 16 specific (53%), 14 heuristic (47%), 0 residue, 0 skipped. Pattern citations below name the KB entry; the patterns/ tree state cited throughout is commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.

| Label | Blocks |
|---|---|
| CSS-BODY | 9 |
| TRANS-UNANCHORED | 7 |
| TRANSLATION-ANCHORED | 6 |
| ASSET-REHOST | 3 |
| DRAFT-HOST | 2 |
| SELF-DELIVERY | 2 |
| IFTAGS | 2 |
| T7-CREDIT-CSS | 2 |
| DELIVERY-HOST | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| INFO-DEL | 1 |
| TASL-FIELDS | 1 |
| LINK-REPOINT | 1 |
| ESCAPED-INCLUDE | 1 |
| INCLUDE-REPOINT | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| RESTORATION | 1 |

Adjudication for this README (every block was read against the bytes): the nine CSS-BODY heuristic blocks are single lines inside the exhibit, and they are three different things — the interwiki adaptation pair (B20's added selector, B21's deleted filter rule, section 5), specificity strengthenings in the credit/info zone (for example B22's border gaining `!important`), and the tail appendix modules riding in B30 (sections 5 and 10). B29's RESTORATION label sits on the credit group's restated tail (the added modal and creditRate rules, section 1); nothing in it restores deleted content, and the label is the classifier's name for a block that re-adds lines near a T7 span. B11's EXHIBIT-RESTRUCTURE primary is the image-block include line, whose changes are the component repoint and the asset re-host (sections 2 and 4). The translation mass (13 blocks) is the production translation's prose, counted per line-pair. After adjudication no block is left unexplained, and no residue appendix is needed (0 residue blocks).

## Standing sections

### 0. Header and provenance frame

- **What:** Theme theme:much-cool-jp; original theme:much-cool on scp-wiki at reference revision 19; candidate `pages/theme:much-cool-jp.txt`. Provenance route: adoption and migration of the production JP counterpart (kind K6; the R4-family route), evidenced by the Phase 17 diff record and the credit block's production translator credit — not a fresh derivation from the EN original. The frame is the composition's: the candidate opens with its delivery module (candidate L1–3), the interwiki-style frame (candidate L5–8), and then the localized gate (candidate L10), where the original opens with its delivery module and gate (original L1–5).
- **Why:** Section 0 declares the provenance route and the topology baseline; the gate's tag is P2, the frame is P6/T3.
- **Verify:** The sources.tsv row for much-cool-jp (kind K6 and its notes); the head of `pages/phase17-diff-much-cool-jp.txt`, which names the production page as its target.
- **Disposition:** Standing (the route itself); the delivery changes are recorded in section 3.

### 1. Credit and attribution

- **What:** The original's furniture is a bare `[[module Rate]]` under its caption (original L8–11) and the EN info pane, `[[include info:start]]`/`[[include info:end]]` under a second caption (original L13–17). The candidate deletes the info pane (the INFO-DEL of B6) and installs the JP credit block under a クレジットモジュール caption — but it keeps the Rate exhibit (candidate L13–16, caption 評価モジュール), the production page's standing furniture form; the per-theme record, item 2, records the contrast with the S2 population's swap. The credit block (candidate L21–32) carries nine fields: the ruling-3 eight plus the production page's own 作者 field. Values: title 最高にクールなCSSテーマ; 翻訳責任者 nebula2700; 翻訳年 2024 (the production translation's human credit, kept because this candidate adopts that translation — the attribution rule for adopted pages); 作者 and 著作権者 both c_bonefish (アカウント削除済); 原題 Much Cool CSS Theme; 作成年 2022; 初訳時参照リビジョン 19; the source link (candidate L31) on scp-wiki.wikidot.com, the host sources.tsv records for the original. Author check: c_bonefish is the original's stated author (original L19, "made by [[*user c_bonefish]]"), and no other creator is named anywhere in the original, so no dropped-creator flag arises. History: at the T4 check this block was missing fields (LOCALIZE-ROWS row 23: "pattern 3 (credit missing 翻訳責任者/翻訳年/著作権者/元記事リンク, L22–28)"); the credit completion in b816e10 supplied them, and the block reviewed here is the completed one. T7 credit-module CSS: the theme carries its own credit group, restated in the candidate (the box rules move from `.rate-box-with-credit-button` to `.rate-box-with-credit-button .creditButton` with a color added, candidate L476–481; the `.fa-info` rules gain color and `!important`, candidate L491–499; modal rules for the credit dialog and a `.creditRate` height rule are added, candidate L500–515) — the production page's JP credit styling, carried by the migration. One selector in the restated group is flagged in the per-theme record, item 1.
- **Why:** P3/T1 as the production page embodies it: the EN info pane does not render in the JP environment and is replaced by the JP credit block; the Rate exhibit is the production page's own form (item 2). Ruling 3 fixes the eight fields; the ninth is the adopted page's own record.
- **Verify:** `grep -n 'module Rate\|credit:start\|info:start' candidate.txt` — the Rate at L15 and the preview pair at L21 and L32, no info include; read candidate L21–32 against the fields above.
- **Disposition:** Applied; the T4 credit finding is FIXED (b816e10), not dispositioned.

### 2. Includes and components

- **What:** The candidate's live includes are three: the interwiki-style frame (candidate L5–8, section 3) and the credit pair (section 1). The image-block exhibit is repointed: the original's `[[include component:image-block name=https://scp-wiki.wikidot.com/local--files/theme:much-cool/logo.png …]]` (original L30) becomes `:scp-jp:component:image-block` with the logo's SCP-JP storage address (candidate L44, section 4). The usage example names the production page: the original's `@@[[include :scp-wiki:theme:much-cool]]@@` (original L24) becomes `@@[[include :scp-jp:theme:much-cool]]@@` (candidate L37) — theme:much-cool without the suffix, because that existing production page is this candidate's posting target (section 0). This is the opposite of the plain-slug defect flagged in sibling packages: there the -jp page is the posting target and the example drops the suffix; here the suffix-less page is the target and the -jp name is only the composition's staging name. The deleted info-pane includes are section 1.
- **Why:** P1/T2: components resolve to their JP counterparts; a self-reference names the page that will exist at posting, which the K6 record fixes as theme:much-cool.
- **Verify:** `grep -n '\[\[include' candidate.txt` — the frame, the credit pair, and the image-block exhibit at L44; the escaped example is at candidate L37.
- **Disposition:** Applied; no foreign include kept, no named exception needed.

### 3. Delivery and code loading

- **What:** The original delivers its own CSS by importing its code exhibit from the EN wiki's wikidot.com host (original L2: `@import url('https://scp-wiki.wikidot.com//local--code/theme:much-cool/1')`, with the doubled slash the original ships). The candidate converts the delivery to the standard JP form: the head module imports the exhibit from the draft host (candidate L2: `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Amuch-cool-jp/1`), and the interwiki-style frame follows at priority=1 naming the same address (candidate L5–8). The exhibit itself (original L55–590, 536 lines) stands in the candidate at L69–618 (550 lines); the growth is the section 1 credit restatement and the section 5 interwiki supplement, not added rulesets. Two appendix `[[module CSS]]` blocks stand after the gate's close (candidate L622–627 and L629–632, sections 5 and 10); they are supplements, not delivery.
- **Why:** P4/T9 (own-code delivery re-hosted to JP hosts: EN wikidot.com → the JP draft host, class (iii) mechanics) and P6/T3 (the interwiki-style frame).
- **Verify:** `grep -n 'local--code' candidate.txt` returns candidate L2 and L7 only, both on the draft host.
- **Disposition:** Applied (class (iii) mechanics; T1's single pseudo-ref error is the frame address itself, section 11).

### 4. Fonts and assets

- **What:** Fonts: the exhibit loads one display face, Vollkorn SC, from Google Fonts (original L70 → candidate L84), an allowed host, carried unchanged; the theme names no CJK face in any stack and adds no JP load, because its display type is Latin and body text inherits the environment's JP faces — there is no first-face gap (KB-16) and no P7 item. Assets: all three of the theme's images are re-hosted into the candidate, from the EN wiki's file area to SCP-JP storage: the image-block logo (original L30 → candidate L44, `file:8260379-45-w138` on scp-jp-storage.wdfiles.com), the container background (original L74 → candidate L88, `file:8260379-45-fiuq`), and the header logo (original L80 → candidate L94, `file:8260379-45-w138` again). These are the production page's already-migrated assets, so P5 is completed in the candidate rather than dispositioned — the contrast with the batch's CN themes, whose images await posting-time re-hosting, is the K6 route's doing.
- **Why:** P5 (assets served from JP storage) and P7's negative (no CJK stack to convert).
- **Verify:** `grep -n 'scp-jp-storage\|Vollkorn' candidate.txt` returns the three storage lines and the font load at L84; no `scp-wiki.wikidot.com/local--files` reference remains.
- **Disposition:** Applied.

### 5. Header, sidebar, and site furniture

- **What:** The interwiki adaptation pair, both inside the exhibit. Added: `#interwiki .side-block` joins the side-block background rule (original L305–308 → candidate L319–322), so the JP interwiki sidebar block takes the theme's parchment background. Deleted: the original's `.scpnet-interwiki-frame { filter: invert(1) hue-rotate(245deg) saturate(.8); }` rule (original L351–353) has no counterpart in the candidate — the selector names the EN branch's interwiki frame class, which the JP interwiki component does not emit, and the inversion it applied has no JP object; the deletion is recorded here rather than hidden in the CSS-BODY mass, and no authority charges it (T4: 0 display-affecting findings). The theme sets a header logo (section 4) but no `--header-title` override on either side. The two appendix modules are narrow-viewport furniture: an image-block width correction at phone widths (candidate L622–627) and a file-table containment rule (candidate L629–632), both inherited from the production page with their annotations (section 10). The render row's furniture items (mobile notice left-clip, sidebar x=24) are recorded in section 11.
- **Why:** P8/T6 (environment adaptation): the JP sidebar's blocks and frame are the JP component's, and the port adapts the theme's rules to them in both directions (extend where the object exists, remove where it does not).
- **Verify:** `grep -n 'interwiki' candidate.txt` — the frame include, the added selector at L321, and no `scpnet-interwiki-frame` anywhere.
- **Disposition:** Applied; the render items DISPOSITIONED in section 11.

### 6. Text translation

- **What:** The candidate's Japanese is the production page's 2024 translation (translator nebula2700, section 1), carried by the migration rather than re-translated: the title (最高にクールなCSSテーマ), the about prose (candidate L34, keeping the original's casual register, "GoIFとかのために…作ったんだ"), the usage prose, and the exhibits (headings 見出し1–6, tabs タブ1/タブ2, the link and footnote samples). The classifier's translation mass (TRANSLATION-ANCHORED 6, TRANS-UNANCHORED 7) is that prose counted per line-pair against the EN original; because the candidate's direct ancestor is the production JP page rather than the EN text, the mass overstates the migration's own editing, which the Phase 17 diff record measures separately. One translator's note rides in the footnote sample (candidate L60, section 10). No reader-visible CSS strings exist in this theme beyond the credit zone, and no Chinese text arises (EN origin), so the R5 glyph-form class does not fire.
- **Why:** P10 (body, usage, and sample translation) — satisfied by adoption: the production translation is the translation of record for this theme.
- **Verify:** The body sections of diff.md in order; `pages/phase17-diff-much-cool-jp.txt` for the migration's own delta against production.
- **Disposition:** Standing (the port itself).

### 7. Links

- **What:** One prose-link repoint: the about prose's hub link, `[[[https://scp-wiki.wikidot.com/are-we-cool-yet-hub|Are We Cool Yet]]]` (original L19), becomes `[[[http://scp-jp.wikidot.com/are-we-cool-yet-hub|Are We Cool Yet]]]` (candidate L34) — the JP hub exists, so the link takes the JP counterpart (B7's LINK-REPOINT). The exhibit's visited-link sample keeps naming `theme:much-cool` (candidate L56), the EN page name as a link-text sample, unchanged in substance from the original's. The credit source link (candidate L31) names scp-wiki.wikidot.com, the recorded host, and serves the original.
- **Why:** P11: a prose link takes the JP counterpart where one exists.
- **Verify:** `grep -n 'are-we-cool-yet' candidate.txt` returns candidate L34 only, on the JP host.
- **Disposition:** Standing.

### 8. Structure

- **What:** The declared deviations are the furniture and CSS items already named: the info pane's replacement by the credit block (section 1), the interwiki pair (section 5), and the two appendix modules standing after the gate's close (candidate L622–632), where the original ends at its gate. Variable names, selectors, and rule order inside the exhibit are otherwise preserved, and the exhibit census (image-block, headings, tabview, footnote sample, the code exhibit) corresponds one to one in the same order, so no R3 deletion arises beyond the section 5 rule, which is named there. B11's EXHIBIT-RESTRUCTURE primary is adjudicated in the class summary (an include line's repoint and re-host).
- **Why:** R3's distinction (sanctioned replacement vs silent deletion) is decided by the census and by naming the deviations, not by the label.
- **Verify:** Compare `grep -n '\[\[tabview\|\[\[code\|\[\[include' original.txt candidate.txt`.
- **Disposition:** Standing with the deviations declared; no class I item.

### 9. Formatting only

- **What:** No WS-ONLY or re-indentation class fired for this theme (0 blocks of either): the migration edited the production page in place without reformatting, so there is no formatting churn to disclose.
- **Why:** The formatting section states its ground when empty, so a reviewer does not have to infer it from silence.
- **Verify:** classification.json carries no WS-ONLY label for this package.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** Three annotations, all inherited from the production page rather than added by the migration. (a) The image-block appendix module's comment (candidate L623): "SCP-JP Wikidot narrow image-block correction: include the native right margin and border in its available width." (b) The file-table appendix module's comment (candidate L630): "SCP-JP Wikidot much-cool narrow files: keep the file table inside the viewport at phone widths." (c) A translator's note inside the footnote sample (candidate L60), a `##909090|(訳注: …)##` aside explaining that the original's "knocknock" is treated as an intended knock-knock joke despite the possible dropped letter — the production translator's note, riding inside a TRANSLATION-ANCHORED block, which is why this section is not none despite no ANNOTATION label firing. No `[!-- --]` note exists.
- **Why:** R2: annotations are part of the port's record; the two module comments document the appendix rules' intent (section 5 relies on them), and the footnote note documents a translation judgment a reviewer would otherwise have to guess at.
- **Verify:** `grep -n 'SCP-JP Wikidot\|訳注' candidate.txt` returns candidate L60, L623, and L630.
- **Disposition:** Standing (part of the candidate as reviewed).

### 11. Dispositions and exceptions

- **What:** Three items, each with its ground. (1) T1's single error, pseudo-ref ×1: the draft-host frame address, class (iii) mechanics, DISPOSITIONED in register c1. (2) The render row's items (RENDER-ROWS-1, lane RENDER-C row 23), none charged to the candidate at the ledger determination: the WebKit CC-badge stray "S" (recorded verbatim, a cross-cutting environment item the row itself marks as such); the mobile notice left-clip and the sidebar x=24 (recorded verbatim); the sample's overflow at 324/884px (recorded verbatim); the sample's credit-modal errors (KB-32: the preview form has no modal mechanism, ruling 5); and a contrast warning. (3) The T4 pattern-3 credit finding is not here: it was FIXED by edit (b816e10), and section 1 records it. The per-theme flag (item 1) and note (item 2) are recorded below, not dispositioned.
- **Why:** A disposition is a decision with grounds (AGENTS.md §3 classes (i)/(ii)/(iii); the named KB entries), not an omission; a fixed item is distinguished from a dispositioned one.
- **Verify:** Each item names its deciding record above and in the per-theme record.
- **Disposition:** DISPOSITIONED (items 1–2); item 3 fixed; the per-theme items flagged or noted with evidence.

### 12. Verification

- **What:** (a) T1 source check (T1-ROWS row 23): exit 1, 1 error / 1 warn / 2 infos; the error is pseudo-ref ×1, class (iii); there is no class (i) error. (b) T2/T3 render (RENDER-ROWS-1, RENDER-C row 23): FINDINGS, the items of section 11(2), all dispositioned; engine coverage as run by the lane, not separately caveated in its row. (c) T4/T5 (LOCALIZE-ROWS row 23, LOCALIZE-B): FINDINGS / FINDINGS jointly, display-affecting findings 0; its one pattern finding (credit fields) was fixed by b816e10. (d) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md and the verdict stamp from the two byte-faithful copies in this directory and compares. Counts in this README are the generator's (diff.md): +75/−40 in 8 hunks, 30 classified change blocks.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:much-cool-jp.txt` and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (GOSIGN2-LEDGER (b) row 23; go-sign, COMPLETION-REPORT §10).

## Per-theme record

### Item 1 — the inherited `.creditButton p a` selector (flagged) Repaired after this package was built (FIX-CREDITBTN item 1, commit 1db8300): the selector now reads `.creditButton > a`; see the post-package repairs item below.

The candidate's credit group was actively restated (section 1: the box selector rewritten, the `.fa-info` rules strengthened, modal rules added), yet `.creditButton p a` survives verbatim inside it (original L475–478 → candidate L487–490). The campaign's T7 record (SUPPLEMENT-TYPES T7; KB-11) states the JP credit module emits the anchor as a direct child of `.creditButton`, without the `<p>` wrapper this selector requires, and sibling ports corrected exactly this shape (theme:sodium-jp in place, theme:jiha-jp by restatement). This is the batch's fourth occurrence (theme:mr-reprisal-jp, theme:oneiroi-west-jp in both of its copies, theme:nameless-jp), and the sharpest: the group around the selector was rewritten while the selector itself was carried. The likely mechanism is visible in the provenance — the restatement is the production page's own CSS, maintained outside the campaign's T7 wave — but on the JP DOM the rule cannot match either way. This package flags the selector with its evidence and does not edit the candidate; the theme's T4 row does not charge it.

### Item 2 — the kept bare Rate exhibit (note)

Every S2-wave port in this campaign deletes the original's bare `[[module Rate]]` when it installs the preview credit block, on the ground that the JP credit form is the rate-bearing one (P3; a kept Rate would be the KB-09 duplicate). This candidate keeps its Rate exhibit (candidate L13–16) next to the credit block. The ground is the provenance: the furniture is the production page's standing form, the Phase 17 migration carried it unchanged, and neither T1 nor T4 charges it (T4 records 0 display-affecting findings for this theme). Recorded as a note so the contrast with the population is visible to a reviewer rather than smoothed over; if the coordinator's credit-content pass later harmonizes furniture across the population, this theme's Rate is the line that decision will touch.

### Post-package repairs (REFRESH3-C)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/<fullname>.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-SNIPPET — production-predecessor reference audit (landing 358955e).** `FIX-SNIPPET.md` records the self-reference at candidate L38 as DRIFT ground D1 (own code addresses under `theme%3Amuch-cool-jp`). Commit 358955e inserted `-jp` after the target, `theme:much-cool` → `theme:much-cool-jp`.

**Sequelae — 1db8300, then 5ddc1a6.** The creditbtn landing 1db8300 (below) reverted this line to the plain form in the same edit that corrected the `.creditButton` selector; commit 5ddc1a6 (pages: much-cool snippet insertion restored) re-applied the `-jp` insertion at L38 and added the file's final newline. The current candidate therefore has the `-jp` exhibit and ends with a trailing LF (the package's as-built copy did not).

## Change set outside the two diffed files

The diff covers two files; the port's record is two files larger. `pages/phase17-diff-much-cool-jp.txt` is the migration's own diff against the current production page (the Phase 17 record; its head names theme:much-cool (SCP-JP) as its target and rev 19 as the reference), and `pages/theme-decoration-sample-much-cool-jp.txt` is the decoration sample the render checks ran against (its findings are the sample half of section 11(2)). There are no companion fragments and no shared base file for this theme.

## License and attribution

- **Title:** Much Cool CSS Theme
- **Author:** c_bonefish (アカウント削除済)
- **Source:** https://scp-wiki.wikidot.com/theme:much-cool — revision 19 (revision date 2023-02-25 16:46:05)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: nebula2700 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
