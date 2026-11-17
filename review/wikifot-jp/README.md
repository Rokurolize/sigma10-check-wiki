# Review package — theme:wikifot-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:wikifot-jp — origin EN, population #42 [GOSIGN2-LEDGER (b) row 42]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 9f1c62357cc784d7d897e82249f19c4d2cd8459f828694c4bd5a2788f8dddc49); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 1 error / 0 warns / 2 infos (pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 42; GOSIGN2-LEDGER (b) row 42]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 1449/851/458/362px at all four widths; font-awesome 4.3.0 `@import` broken as authored (icons never load — real defect); GOSIGN "raw wikitext leak" unconfirmed in current renders; sidebar x=0, invisible ×. [RENDER-ROWS-1 (RENDER-D2 row 42)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-D2 row 42)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 42, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 42]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 42]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:wikifot-jp.txt sha256:9f1c62357cc784d7d897e82249f19c4d2cd8459f828694c4bd5a2788f8dddc49; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/wikifot-jp/candidate.txt (sha256 9f1c62357cc784d7d897e82249f19c4d2cd8459f828694c4bd5a2788f8dddc49)
Original: theme:wikifot — scp-wiki, revision 12 (sha256 db848de7b8bdf36359b3a22a25ea35e32fce7250bc6e71977fb2a82c87d59a4a)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 42); one of the 286 of 286 pass-eligible themes. The generated stamp above reads STALE: the candidate changed after the verdict-era bytes (the usage-example sweep, commit b5cb724, repointed one usage line to the -jp form), so the stamp's verdict lines describe the pre-sweep file |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no wikifot entries |
| Wave edits after the port | A seven-commit per-theme repair chain in November 2026 (dead image reference, exhibit escapes, a markup-balance change and its revert, a malformed div opener, a closing-div removal and its partial restoration); the credit block closed and moved to the head (ad2bade); six credit fields added (gosign2 T1 fixes, b816e10); the reference-revision lines (Phase 17, 8dcac74); the translator normalized to AI (FIX-CREDIT-D, 1869877); one usage line repointed (population sweep, b5cb724) |
| Ledger discrepancy from this package | The ledger credits the FontAwesome 4.3 repair to FIX4-CREDIT (commit 9fbcd94); that commit does not touch this file. The repair module was present from the import (d727e92). Full evidence in section 4 and the Per-theme record |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:wikifot | theme:wikifot-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 12 (created 2024-07-05 14:55:30 per sources.tsv), as recorded in the candidate's credit block: **初訳時参照リビジョン:** 12 | — |
| Source of this copy | Refetched 2026-11-17 at the reference revision (mirror store class FETCH-REGEN), via the campaign mirror store | Canonical file `pages/theme:wikifot-jp.txt`, imported in commit d727e92 ("Canonical sources for the Sigma-10 display-check composition"); its last content change is commit b5cb724 (the usage-example sweep) |
| Lines / bytes | 292 lines / 8,712 bytes | 365 lines / 13,128 bytes |
| SHA-256 | db848de7b8bdf36359b3a22a25ea35e32fce7250bc6e71977fb2a82c87d59a4a | 9f1c62357cc784d7d897e82249f19c4d2cd8459f828694c4bd5a2788f8dddc49 |

Provenance route: derived from the original at the reference revision. No production counterpart was adopted (sources.tsv kind: standard). The candidate is the smaller file of the two by design inverted: it is **longer** than the original (365 vs 292 lines) because it carries the credit block the original lacks and five appended supplement modules (sections 1 and 3); the stylesheet body itself is line-for-line the original's (157 lines on both sides, classifier topology).

## Summary

Wikifot is Erminustay's joke "wiki-format" theme: a 157-line stylesheet carried in a module at the head, a long translated documentation body (jokes, puns, a parody BSOD dark mode), and a darkmode module at the tail. The port translates the body in full (the tab puns are recreated in Japanese), repoints the interwiki frame's site and site segment to JP while keeping its inline CSS payload byte-identical, moves the credit block to the head, and appends five supplement modules after the closing gate — three JP furniture corrections and two credit-module corrections, one of which re-imports FontAwesome 4.3, which the theme's own ThemePreviewer configuration silently disables. The theme's post-import history is a per-theme repair chain of seven commits (two of them a change and its revert) rather than population waves; its one ledger inaccuracy is the FontAwesome fix's attribution, recorded in the Per-theme record.

## Classification

| Label | Blocks |
|---|---|
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 2 |
| TASL-FIELDS | 1 |
| TRANSLATION-ANCHORED | 8 |
| TRANS-UNANCHORED | 23 |

Counts: 38 blocks — 12 specific (31.6%), 21 heuristic (55.3%), 5 residue (13.2%), 0 skipped. Topology: module-css orig L2–159 (157 lines) → cand L15–172 (157 lines); code-other (the documentation body) orig L173–292 → cand L188–365; no moves. The heuristic share is the expected shape for a fully translated joke body (TRANS-UNANCHORED mass); every heuristic and residue block is resolved in the Appendix. Labels are sets per block; this README's sections were written from classification.json's label spans, not from the skeleton's per-section lists.

## Standing sections

### 0. Header and provenance frame

- **What:** The original has no head gate at all: it opens directly with the ThemePreviewer module (orig L1, `theme_url=" "`) and its stylesheet module (orig L3–159); its `[[iftags +theme]]` gate sits mid-page (on the combined line orig L159, with the module close and a `[[>]]` opener), wrapping only the documentation body. The candidate opens with the localized gate (cand L1), the preview credit block (cand L2–12), the ThemePreviewer (cand L14, the theme_url argument byte-identical), and the stylesheet module (cand L16–172); its gate closes after the darkmode module (cand L307), and the five supplement modules sit outside it (cand L310–365). Provenance route: derived from the original at reference revision 12 (see Provenance).
- **Why:** P2: the gate covers the theme's own content in the JP form; the credit block's placement at the head is the population form (it was moved there by commit ad2bade, section 1).
- **Verify:** Read original L1–2 and L170 against candidate L1–15 and L307–310.
- **Disposition:** Recorded; the credit reading is section 1, the delivery reading section 3.

### 1. Credit and attribution

- **What:** The original has no credit block and no rate device anywhere on the page. The candidate adds the preview credit block at the head (cand L2–12, block B1): `:scp-jp:credit:start-preview` / `end-preview` carrying all eight ruling-3 fields — title Wikifotテーマ, translator AI, translation year 2026, original title "Wikifot Theme", copyright holder Erminustay, creation year 2024, reference revision 12, and the source link to the EN page. The attribution was checked against the original: the page carries no in-page author credit to contradict it, and the ledger's localize row for this theme charged only the missing fields (P3), never the attribution. The block's history: the import (d727e92) carried it mid-page in an unclosed form; commit ad2bade ("close and relocate wikifot credit block") closed it and moved it to the head; the gosign2 T1 fixes (b816e10) added the six fields (translator then reading SCP-JP); FIX-CREDIT-D (1869877) normalized the translator to AI. The theme's credit-module CSS arrives as two appended supplement modules (cand L332–338 and L340–365, section 3): the first re-imports FontAwesome 4.3 (section 4), the second retargets `.creditButton a` to the JP component's direct-child anchor shape and flattens the credits modal box to the theme's white, square, shadowless form.
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form; the fields are ruling 3's eight. The two CSS supplements exist because the theme's own ThemePreviewer setup starves the credit module of its icon font (section 4) and because the EN-shaped credit rules do not match the frozen JP component markup (the T7 family; KB-63/KB-11's shapes).
- **Verify:** Read candidate L2–12 against the eight-field list; `git show ad2bade -- pages/theme:wikifot-jp.txt` for the relocation.
- **Disposition:** Standing. Ledger (c3): P3 credit fields FIXED (credit waves; checker-verified) — the outcome is correct in the bytes.

### 2. Includes and components

- **What:** The candidate's complete include list (grep) is short: the credit pair (cand L3/L12), the interwiki-style frame (cand L15, labels COMPONENT-SWAP + INCLUDE-REPOINT), and the two escaped usage exhibits (cand L189/L192, section 6). The frame's include was repointed `:scp-int:` → `:scp-jp:` with its priority kept at 1, while its long inline `css=` parameter — the theme's own chrome CSS — is **byte-identical** to the original's (orig L2 against cand L15: only the include head changed; the payload is one unchanged line). The original's only other include is the Examples image-block exhibit (orig L180, naming the unuploaded logo.jpg), which the candidate does not carry — it was removed by commit 4b52123 (section 8). No foreign include is kept, so KB-15/KB-54 do not engage. The documentation body also carries the in-body `[[module rate]]` (cand L175, carried from orig L160, each inside its `[[>]]` div): the original's own placement, kept; no register charges a duplicate-rate item for this theme and the classifier fires no BARE-RATE-DEL on it, so it is recorded here as a carried form, not a finding.
- **Why:** P1: foreign-site includes are repointed to the JP site; the frame's css= parameter is one of the three parameters that survive the frame rules, and its payload is the theme's own design, so byte-identity is the correct outcome. Ruling 4 does not engage: the theme's component dependencies are exhibit devices whose JP forms exist.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt`; read the two frame lines side by side (orig L2, cand L15) and confirm the css= payload is identical.
- **Disposition:** Standing; no include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** The theme delivers inline: the stylesheet is a `[[module CSS]]` at the head (cand L16–172), and there is no local--code delivery and no code block in the candidate (`grep -c '\[\[code' candidate.txt` counts only the documentation's escaped usage exhibits). The interwiki frame's theme= parameter is absent on both sides (the frame carries its chrome in the inline css= parameter instead), so this theme has no self-delivery address to audit — it is not in the FIX-CODEADDR population. A depth scan of the stylesheet module ends at **+1 on both sides** (original L3–159, candidate L16–172): the `@media (max-width: 767px)` block opened after the `/{$trans}` comment line (orig L130 / cand L143, the last depth-0 line in each) is never closed before `[[/module]]`. The shape is byte-inherited from the original, identical in both files, and the renders are recorded working — an inherited truncation, not a port defect; it is recorded here so a depth-checking reader does not mistake it for the displaced-brace family (anniversary-jp's defect, where the candidate's scan differed from its original's). The darkmode module differs between the sides and is section 8's item. After the gate, five supplement modules are appended (cand L310–365): (i) a mobile drawer correction (the sidebar toggle's z-index/position at ≤768px), (ii) a narrow image-block correction (max-width at ≤479px), (iii) a narrow gutter correction (the content wrap's padding at ≤479px), (iv) the FontAwesome re-import (cand L332–338), and (v) the credit retarget and modal flattening (cand L340–365). All five carry English "SCP-JP Wikidot ..." rationale comments and were present from the import (d727e92).
- **Why:** P4/T9: inline module delivery is the original's own topology, kept; the supplements are JP-environment corrections scoped to the furniture they fix (P8's mechanism), each stating its reason in its comment so the correction is auditable without this package.
- **Verify:** The depth scan: strip strings/comments from each file's first module and track `{`/`}` depth line by line (both end at +1, last depth-0 line at orig L130 / cand L143); read cand L310–365 for the five supplements.
- **Disposition:** Standing; the inherited +1 depth is recorded as an original-state shape (the renders pass; no register charges it).

### 4. Fonts and assets

- **What:** No font imports exist on either side: the theme's stacks are Verdana throughout (its own specimen at the body tail states the design), so there is no P7 item and no JP supplement — checked and absent, not omitted. The one font-family-adjacent asset is FontAwesome 4.3: the original imports it nowhere either (its credit/info glyphs relied on the base theme's sheet), and the candidate's supplement module (cand L332–338) re-imports it from maxcdn.bootstrapcdn.com (a P5-sanctioned host) with a comment stating the mechanism: the ThemePreviewer's `theme_url=" "` makes Wikidot replace the wiki theme stylesheet import with an empty one, so the Sigma-10 base sheet — and the FontAwesome 4.3 it imports — never loads, leaving the credit module's glyphs (fa-info, fa-plus, fa-minus, fa-times) blank. The ledger's render row records the item as "font-awesome 4.3.0 @import broken as authored (icons never load — real defect)" and marks it FIXED. Assets otherwise: the documentation's table specimen image was repaired from the original's relative `[[=image table.png]]` to the candidate's own draft-host attachment URL (cand, in the "this is a table" specimen), class (ii)/(iii); the Examples image-block's logo.jpg (an unuploaded joke file) was removed by commit 4b52123 (section 8).
- **Why:** P5: the re-import's host is on the sanctioned list. The repair's form (a supplement module rather than an edit to the theme's own CSS) is the port's chosen shape; its mechanism is stated in its own comment.
- **Verify:** Read cand L332–338; `grep -n 'font-awesome\|FontAwesome' original.txt candidate.txt` (original: none; candidate: the supplement only).
- **Disposition:** FIXED per the ledger's render row — with the attribution corrected in the Per-theme record: the fixing commit the ledger names (9fbcd94, FIX4-CREDIT) does not touch this file; the module has been present since the import (d727e92).

### 5. Header, sidebar, site furniture

- **What:** The theme's chrome CSS rides in the frame's inline css= parameter (byte-identical, section 2) and in the stylesheet module. Three of the five supplements are furniture corrections for the JP environment: the mobile drawer (cand L310–316), the narrow image-block (L318–323), and the narrow gutter (L325–330). The render row's sidebar item (sidebar x=0, invisible close glyph) is dispositioned as the theme's design: the sidebar is off-canvas at load by design (closed state), so x=0 is the authored state, not a displacement.
- **Why:** P8: furniture adaptations are owed where the JP environment's structure differs from the EN one; the three supplements are exactly that scope, each with its rationale in its comment.
- **Verify:** Read cand L310–330; the render row's sidebar disposition is in ledger (c2).
- **Disposition:** Standing; the sidebar item is DISPOSITIONED in (c2) as design.

### 6. Text translation

- **What:** The documentation body is translated in full (TRANS-UNANCHORED ×23, TRANSLATION-ANCHORED ×8): the joke prose, the usage lines, the glossary (the "Wikifot" etymology entry, with the Flickr tag URL kept and its link text localized), the tab specimens with their puns recreated in Japanese, and the darkmode BSOD parody (its fake error text translated, its structure kept). Two residue blocks are translation-adjacent mechanics, resolved in the Appendix: the `{{[[/div]]}}` → `@@[[/div]]@@` escape-form conversions (B23, B27, from commit 69c5894) and the "Box box!" → 箱箱！ specimen line (B25). The usage lines read `[[code]][[include :scp-jp:theme:wikifot-jp]][[/code]]` (cand L189, the post-sweep form) and `[[code]][[include theme:wikifot]][[/code]]` (cand L192, the bare same-site form the original also carried in its `:scp-wiki:` + bare pair): on JP the bare form resolves to the existing production page theme:wikifot, so the pair is coherent — the candidate form and the production form, recorded not flagged.
- **Why:** P10: body, usage and sample text are translated; KB-18 covers reader-visible strings. The escape-form change is a rendering-equivalence repair (the `{{ }}` form and the `@@ @@` form both emit the literal closer; the commit record states the exhibits were escaped so the documentation markup parses identically on both wikis).
- **Verify:** Read orig L173–292 against cand L188–307; `grep -n 'include theme:wikifot\|theme:wikifot-jp' candidate.txt` (L189, L192).
- **Disposition:** Standing; the localize lane recorded no display-visible T5 residue for this theme (LOCALIZE-ROWS row 42: "no display-visible T5 residue").

### 7. Links

- **What:** The candidate's prose links are the credit block's source link (cand L11, to the EN original — the required ruling-3 back-reference) and the body's kept external link (the Flickr tag URL in the glossary entry, link text localized). The original's link set is the same. No tag-page or hub links occur.
- **Why:** P11 repoints links to their JP counterparts where the link survives; the surviving external link's target is not a wiki page and stays.
- **Verify:** `grep -n 'http' candidate.txt` and compare against the original's list.
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** The stylesheet body honors the localize.md closing rule exactly: 157 lines on both sides, same order, the only internal differences being the gate-adjacent lines. Three structural items sit outside it. (a) The darkmode module's completion (residue B37): the original's module is a single line ending mid-rule (`overflow:hidden` with no closers; a depth scan of the original's second module ends at +2); the candidate's line completes it with `}}` (cand L306, scan ends at 0). A port repair of truncated CSS, invisible to every register (none charges or credits it). (b) The Examples image-block exhibit (orig, the joke exhibit naming the unuploaded logo.jpg) was removed by commit 4b52123 ("Repair dead theme-documentation image references"), and the gallery images were dropped by 69c5894 — documentation exhibits whose targets do not exist, removed rather than re-hosted (the campaign bars re-upload; a dead exhibit is worse than none). (c) The closing-markup balance pair: commit 7c36767 changed the closing balance and was reverted by 8c70c5a because it destabilized the info-cw include; commit 5e56f38 then removed one `[[/div]]` so the documentation markup parses identically on both wikis, and 8b0a340 split the darkmode div opener onto its own line and restored the third `[[/div]]` — the pair nets to the opener split. The five appended modules (section 3) complete the structural account.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the ground for each is stated. Item (a) is the mirror of section 3's inherited truncation: there the candidate kept the original's shape; here it repaired it, and the difference is recorded because a reviewer comparing depth scans will find exactly one module whose shape changed.
- **Verify:** The depth scans in section 3 and item (a); `git log --follow --oneline -- pages/theme:wikifot-jp.txt` for the repair chain (4b52123, 69c5894, 7c36767, 8c70c5a, 07c09e0, 5e56f38, 8b0a340).
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** No WS-ONLY label fired and the classifier counts 0 re-indentation blocks. The whitespace-visible changes in the diff are the escape-form conversions and the opener split of section 8, which are structural, not formatting. The creation-era whitespace normalization that other themes received (a dedicated commit) does not appear in this file's history.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; here the ground for "none" is the classifier's counts plus the file history.
- **Verify:** classification.json (0 WS-ONLY blocks, reindent_blocks 0).
- **Disposition:** None required.

### 10. Porter annotations

- **What:** The five supplement modules carry English rationale comments (cand L311, L319, L326, L333, L341 region — each opens with an "SCP-JP Wikidot ..." explanation of the correction it makes): porter annotations in module-comment form, listed here so they are never mistaken for original content. The classifier fires no annotation label for them; direct inspection is the ground (the standing lesson from earlier batches: annotations ride inside other blocks). No `[!-- ... --]` translator notes exist (`grep -c '\[!--' candidate.txt` = 0).
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation.
- **Verify:** Read cand L310–365 and note the five comment openers.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The render findings: page-overflow 1449/851/458/362px at all four widths — DISPOSITIONED in (c2) under the KB-33 static-replica and KB-34 preview-chrome families. (2) The GOSIGN "raw wikitext leak" item — DISPOSITIONED as unconfirmed in current renders. (3) The sidebar x=0 / invisible close glyph — DISPOSITIONED as the theme's closed-state design (section 5). (4) The inherited unclosed @media block in the stylesheet module (section 3): an original-state shape, renders recorded working, no register charges it — recorded here so it is a decision, not an omission. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–4).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 1 error / 0 warn / 2 info (pseudo-ref×1; T1-ROWS row 42) — the lightest row in this batch; the pseudo-ref is the self-delivery family, class (ii) per register (c1). (b) T2/T3 render: FINDINGS, dispositioned in (c2) (section 11); the FontAwesome item is the row's one FIXED (section 4). No credit-modal error is recorded for this theme (RENDER-ROWS-1, RENDER-D2). (c) T4 localize plus follow-up: the lightest charge set in the batch — P3 only (credit missing six section-3 items), 0 display-affecting items, no display-visible T5 residue, no unincorporated upstream updates (LOCALIZE-ROWS row 42, source LOCALIZE-B); outcome P3 FIXED (ledger (c3)). No T4 follow-up diff artifact is recorded for this row; the mirror is the 2026-11-17 refetch at the reference revision. (d) T5: judged jointly with T4 by the source lane. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp (which reads STALE for the sweep reason in the Status block). Counts in this README are the classifier's (38 change blocks) and the generator's (diff.md: +150/−82 in 3 hunks).
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:wikifot-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 42).

## Per-theme record

### The FontAwesome fix's ledger attribution is wrong (record discrepancy)

The ledger's render row for this theme marks the FontAwesome 4.3 item FIXED and attributes the fix to "FIX4-CREDIT (9fbcd94) §9", with the correction located at "current file L333-338, assembly-verified". The line numbers are right — the re-import module is at cand L332–338 — but the commit is not: `git show --stat 9fbcd94` does not list this file at all, and `git log -S 'font-awesome' -- pages/theme:wikifot-jp.txt` shows the module present from d727e92, the import commit. FIX4-CREDIT's actual wikifot-adjacent work was on other files. The bytes and the register agree on the outcome (the icons load; the module exists and is assembly-verified) and disagree only on the vehicle. This package follows the bytes: the repair rode in with the port itself, as one of its five creation-time supplements.

### A repair chain instead of population waves (the U-class shape of this theme)

This theme's class-U membership is carried mostly by its own repair chain, not by the population waves that shaped its batch-mates: seven November 2026 commits (4b52123, 69c5894, the pair 7c36767/8c70c5a, 07c09e0, 5e56f38, 8b0a340) fixed documentation defects one at a time — a dead image reference, unescaped exhibit closers, a malformed `[[div_ style=...]]` opener, and two rounds of closing-balance adjustment, one of them a revert after the first attempt destabilized the info-cw include. The revert pair is worth a reviewer's attention: it is the record of a fix that was tried, measured against the live composition, and backed out — the chain's honesty is in the git record, and the current bytes are the post-revert state plus the narrower 5e56f38/8b0a340 pair. The population waves touched the file only for the credit fields (b816e10), the translator normalization (1869877), the revision lines (8dcac74) and the sweep (b5cb724).

### The credit block's two lives

The credit block existed from the import but not in its current place or form: d727e92 carried it mid-page, unclosed; ad2bade closed it and moved it to the head; b816e10 completed its fields there. A reader diffing the import-era file against the original would find the block in the body; the head placement a reviewer sees now is the ad2bade state. Recorded because the block's position is part of the port's furniture story (section 0) and its history is otherwise invisible.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/theme-decoration-sample-wikifot-jp.txt` — the render sample page (an include of the candidate and of the shared `theme-decoration-sample`); it is the "sample" the T2/T3 checks rendered. (2) The delivery itself: the candidate delivers inline (module CSS at the head), so there is no companion code page and no local--code address. (3) The production page theme:wikifot on SCP-JP, which the body's bare usage form names (section 6), is an external reference, not a file in this repo.

## Multi-wave provenance

The candidate's current state is the product of one import, a seven-commit per-theme repair chain, and four population touches: d727e92 imported the port (translation, the five supplement modules including the FontAwesome re-import, the credit block in its mid-page unclosed form); 4b52123 removed the dead image reference; 69c5894 escaped the documentation exhibits and dropped the gallery images; 7c36767's closing-balance change was reverted by 8c70c5a; 07c09e0 repaired the malformed div opener; 5e56f38 and 8b0a340 settled the closing balance; Phase 17 (8dcac74) recorded the reference revision; ad2bade closed and relocated the credit block; the gosign2 T1 fixes (b816e10) completed its fields; FIX-CREDIT-D (1869877) normalized the translator; the usage-example sweep (b5cb724) repointed one usage line, which is why the stamp reads STALE; and the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 42, (c1) pseudo-ref entry, (c2) wikifot entry, (c3) wikifot entry; T1-ROWS row 42; LOCALIZE-ROWS row 42; RENDER-ROWS-1 (RENDER-D2) wikifot row. The go-sign re-run over that record is what the Status block certifies, subject to the Per-theme record's attribution correction.

## Appendix — residue blocks

The classifier emitted five residue blocks and twenty-one heuristic blocks; all are resolved, none required a new signature.

- **R1 — B23 and B27 (residue; orig L241–242 → cand L255–256 and orig L257–258 → cand L271–272, body → body).** The exhibit closers' escape-form conversions: `{{[[/div]]}}` in the original became `@@[[/div]]@@` in the candidate (commit 69c5894). Both forms emit the literal closer; the change makes the documentation markup parse identically on both wikis. Resolved in section 6.
- **R2 — B25 (residue; orig L248–250 → cand L262–264, body → body).** The specimen line "Box box!" translated to 箱箱！ inside the box exhibit. Resolved in section 6 as translation.
- **R3 — B37 (residue; orig L290–291 → cand L305–306, body → body).** The darkmode module line completed with `}}`. Resolved in section 8, item (a): a port repair of the original's truncated CSS (the original module's depth scan ends at +2; the candidate's ends at 0).
- **R4 — B38 (residue; orig L292 → cand L307–365, body → body).** The candidate's tail growth: the closing gate line plus the five appended supplement modules. Resolved in sections 3 and 10.
- **R5 — the heuristic mass (B2–B22, B24, B26, B28–B36).** The translated documentation body: joke prose, usage lines, the glossary, the tab specimens and the BSOD parody, interleaved with the exhibit restructures of section 8. The classifier's "script delta without the anchor majority" note is the honest label for line-by-line translation; each block's content is accounted in sections 6 and 8, and the localize lane recorded no display-visible T5 residue for this theme.
