# Review package — theme:simple-yonder-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:simple-yonder-jp — origin EN, population #38 [GOSIGN2-LEDGER (b) row 38]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now b629b310aa3ec98597ef42cd53dcff7ff2401671a26c52b5dae69456ea7f8031); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info (hotlink×6); standing classes dispositioned in register c1 [T1-ROWS row 38; GOSIGN2-LEDGER (b) row 38]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page-overflow 474–494px@320/375 (candidate fixed min-width), rate-preview ⓘ/× glyphs near-invisible (contrast 1.03), T2 sample no machine verdict (webkit never completes), notice×sidebar at 768. [RENDER-ROWS-1 (RENDER-D2 row 38)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: no credit-modal line in this theme's row; no sample credit-modal error recorded [RENDER-ROWS-1 (RENDER-D2 row 38)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 38, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 38]
- FIX5 re-judgement: none — no OPEN items at the ledger determination [GOSIGN2-LEDGER (b) row 38]
- Computed against: canonical commit 5d951775998e4a1eeccf8e8695a6518b328962ee; candidate file pages/theme:simple-yonder-jp.txt sha256:b629b310aa3ec98597ef42cd53dcff7ff2401671a26c52b5dae69456ea7f8031; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete — skeleton by classify_hunks.py 0.1.0; every SLOT in the skeleton is resolved in the sections below and the Appendix.
Candidate: review/simple-yonder-jp/candidate.txt (sha256 521b1e40a82d0abbe02026baff78c64709c3ccc2b9862127ea5f4e6c82fd4fed)
Original: theme:simple-yonder — scp-wiki, revision 166 (sha256 690260203da166d79ce24a5cdde20bcf10bacd080eb652626d6ac5a7584b0954)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| | |
|---|---|
| Verdict | **PASS** — passed at the ledger determination with no OPEN items (GOSIGN2-LEDGER (b) row 38); one of the 286 of 286 pass-eligible themes |
| Stamp state | The generated stamp above names canonical commit 379eb44 and the pre-repair candidate hash, because this package's worktree history ends before the repair landed. The candidate has since changed (the frame remedy, commit 5d95177), so the stamp reads STALE when regenerated against current canonical, exactly as the other post-verdict repair packages do; the verdict lines themselves are the ledger's and do not change |
| Blocking items at ledger time | None — no section (e) items exist for this theme and the supplement carries no simple-yonder entries |
| Wave edits after the port | The preview credit block (gosign2 T1 fixes, commit b816e10); the JP interwiki frame and the credit adaptation line (FIX-P4, f1138e4); the bunny→Google Fonts repoint (FIX4-REPOINT, 443c608); the duplicate Fira Code import removal (FIX4-MOPUP, 379eb44); the reference-revision lines (Phase 17, 8dcac74); the frame self-address remedy (sub-shape (D), 5d95177) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:simple-yonder | theme:simple-yonder-jp |
| Wiki | scp-wiki.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 166 (created 2024-01-10 02:19:29 per sources.tsv), as recorded in the candidate's credit block: **初訳時参照リビジョン:** 166 | — |
| Source of this copy | Refetched 2026-11-17 at the reference revision (mirror store class FETCH-REGEN), via the campaign mirror store | Canonical file `pages/theme:simple-yonder-jp.txt`, created in commit b0cfebd ("Add eight standalone JP theme ports"); its last content change is commit 5d95177 (the frame remedy) |
| Lines / bytes | 862 lines / 19,058 bytes | 730 lines / 16,618 bytes |
| SHA-256 | 690260203da166d79ce24a5cdde20bcf10bacd080eb652626d6ac5a7584b0954 | b629b310aa3ec98597ef42cd53dcff7ff2401671a26c52b5dae69456ea7f8031 |

Provenance route: derived from the original at the reference revision. sources.tsv kinds this row K6 because a production counterpart exists (`pages-existing/existing:theme-simple-yonder.txt`, the live SCP-JP page translated by ukwhatn in 2020), but the candidate is **not** a production adoption (residue class R4 does not apply): the candidate's CSS body measures 0.995-similar to the original's own code exhibit (classifier topology pass), while its whole-file similarity to the production page is only 0.3588. The production relationship is carried instead by `pages/phase17-diff-simple-yonder-jp.txt`, a 24-line patch page that prescribes the migration edit to the production page (add the preview credit block naming rev 166), and by the candidate's credit block, which credits the production translation by name (section 1). sources.tsv records the production drift check for this row as 一致 (matching).

## Summary

The original is a self-delivering exhibit theme: its whole stylesheet sits in a `[[code]]` block served as the page's own local--code /1, loaded by a tail module import and the EN interwiki frame, behind a bare Rate and the EN info-module furniture, with a long sample body and an Extra Mode (`xmode`) tail apparatus. The candidate inlines the same stylesheet into a single `[[module CSS]]`, drops the sample body and the xmode apparatus (its rules survive unconditionally), and carries the JP frame at its head and the preview credit block at its tail. The measured churn is small (diff.md: +45/−174 in 5 hunks; the classifier counts 8 change blocks, all specific). The three EN asset URLs survive byte-identical and are the standing hotlink family, dispositioned class (ii). The theme passed at the ledger determination with no open items; its wave history (a bunny.net episode created and then reverted, a frame that arrived inside a repoint commit, and a post-verdict frame remedy that removed the frame's dead self-address) is invisible in the final diff and is reconstructed in the Per-theme record.

## Classification

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-MOVE | 4 |
| DUPIMPORT-DEL | 1 |
| EXHIBIT-RESTRUCTURE | 2 |
| FONT-IMPORT | 3 |
| IFTAGS | 3 |
| INFO-DEL | 1 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 1 |
| WS-ONLY | 2 |

Counts: 8 blocks — 8 specific (100%), 0 heuristic, 0 residue, 0 skipped. Topology: the original's code-css body (orig L142–609) moved to the candidate's module-css (cand L5–705) at 0.995 similarity. Labels are sets per block; the per-section lists in the classifier's skeleton show each block once, under its primary label, so this README's sections were written from classification.json's block spans, not from the skeleton's section lists. One label change against the pre-repair candidate is itself evidence: DRAFT-HOST no longer fires anywhere, because the candidate no longer carries a draft-host address (section 3).

## Standing sections

### 0. Header and provenance frame

- **What:** The original's head (L1–17) is furniture: the `[[iftags +theme]]` gate, a bare `[[module Rate]]` in a right-aligned div, the EN info-module includes (`:scp-wiki:info:start` / `more` / `end`, orig L11–15), and the intro prose. The candidate's head (L1–8) is the JP frame (`:scp-jp:component:interwiki-style`, priority=1, cand L1–3 — since the frame remedy it carries no theme= parameter, section 3) followed directly by the delivered module CSS (cand L5–704). The credit block sits at the candidate's **tail** (cand L706–730) under its own `[[iftags +テーマ]]` gate, not at the head — a placement difference from the population norm, recorded here so a reviewer is not surprised by it. Provenance route: derived from the original at reference revision 166 (see Provenance); the K6 production relationship is declared there.
- **Why:** P1/P2/P3/P6 rework exactly this frame for the JP environment; each piece is accounted for in sections 1–3.
- **Verify:** Read original L1–17 against candidate L1–8 and L706–730; blocks B1–B8 in classification.json.
- **Disposition:** Recorded; the delivery reading is section 3, the credit reading section 1.

### 1. Credit and attribution

- **What:** The original has no credit block; its credit furniture is the bare Rate (orig L4) and the EN info-module includes (orig L11–15, label INFO-DEL), and its attribution lives in the intro prose (orig L18) and the CSS comment header (orig L145–155). The candidate deletes the info includes and the bare Rate (B1, label BARE-RATE-DEL) and adds the preview credit block at the tail (cand L707–717, block B8): `:scp-jp:credit:start-preview` / `end-preview` carrying the eight ruling-3 fields — title Simple Yonderテーマ, translator **ukwhatn**, translation year **2020**, original title "Simple Yonder Theme", copyright holder EstrellaYoshte, creation year 2020, reference revision 166, and the source link to the EN page — plus a ninth line, **翻訳について:** ukwhatn による既存の翻訳を基に改変したものです (adapted from ukwhatn's existing translation, cand L711). The author field was checked against the original's own credit: orig L18 ("by [[*user EstrellaYoshte]]") and the CSS header (orig L147, "By EstrellaYoshte") agree with the block's 著作権者. No license box exists on either side, and none was charged (KB-63 covers dropped boxes; this original never had one).
- **Why:** P3/T1: the preview credit module is the JP environment's rate-bearing credit form, so a separate bare Rate beside it would duplicate the rating widget (KB-09's mechanism, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). Ruling 3 (RULINGS-20261116, in review/AUTHORITIES/) fixes the eight fields, credits campaign translations to AI, and prescribes the adaptation line where a human translation is modified — which is why this block names the human translator ukwhatn with the adaptation line instead of the campaign's AI credit: the candidate descends from the production translation lineage (Provenance). The block arrived in two steps: commit b816e10 (gosign2 T1 fixes) added the eight fields, and FIX-P4 (f1138e4) added the adaptation line (Per-theme record).
- **Verify:** Read candidate L707–717 against the eight-field list; `grep -n 'module Rate' candidate.txt` (absent) against original L4; `grep -n 'info:start' candidate.txt` (absent).
- **Disposition:** Standing (the port's credit form). One minor duplication, recorded not charged: the reference revision is stated twice in the tail, at cand L715 (credit block) and cand L726 (prose tail, added by Phase 17 commit 8dcac74 before the block existed in its full form).

### 2. Includes and components

- **What:** The candidate's complete include list (grep): the JP interwiki-style frame (L1–3) and the credit pair (L707/L717). The original's includes are the info trio (deleted, section 1), `component:image-block` (orig L31, inside the dropped sample body), `component:toggle-sidebar` (orig L627, inside the dropped xmode apparatus, section 8), and the EN interwiki-style include (orig L616–620, replaced by the JP frame). No `:scp-wiki:` include remains in the candidate. No component swap (T8) was needed and no foreign include is kept, so KB-15/KB-54 do not engage. The theme is standalone (no base include on either side), so the bare sigma-plus shape (KB-64) does not occur.
- **Why:** P1: foreign-site includes are repointed to the JP site; ruling 4 (port a needed component with the theme) does not engage — the theme's only component dependencies were exhibit devices, and they left with the exhibits.
- **Verify:** `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- **Disposition:** Standing; no include in the candidate points at an EN-wiki page.

### 3. Delivery and code loading

- **What:** The original delivers its stylesheet out of its own code exhibit: the `[[code type="css"]]` block (orig L145–609) is served as the page's local--code /1 and loaded by the tail module @import (orig L613) and the EN frame's theme= URL (orig L618). The candidate inlines the same body into a single `[[module CSS]]` (cand L5–704) at 0.995 similarity, folding the original's second, tail module's rules (orig L630–860) into the same module; the merge initially duplicated the Fira Code @import, and the duplicate was removed by FIX4-MOPUP (commit 379eb44; the classifier's DUPIMPORT-DEL span inside B4). The frame's history is the section's second half. As ported, the JP frame kept the self-delivery form: its theme= named the candidate's own /1 on the draft host. The candidate contains **no `[[code]]` block at all**, so that address had no target: the FIX-CODEADDR population audit (R/review-scout/FIX-CODEADDR.md) listed simple-yonder-jp in its no-target class. The frameaddr lane then classified the reference UNRESOLVED, a fourth shape the three ruled sub-shapes do not cover (R/review-scout/FIX-FRAMEADDR.md §4): in the original the address was **live** (its block 1, banner "Simple Yonder Theme" at orig L143, is the CSS source), so it is not inherited-dead (A), not introduced (B — the original carries the same frame self-address), and not misdirected (C). The coordinator's ruling for the twelve files of this shape (recorded as sub-shape (D) in the landing commits) applied the (B) remedy: **the theme= parameter line was dropped, the frame include and its priority kept** (commit 5d95177). The candidate's current frame (cand L1–3) is that remedied form, and this package is built against it. The candidate's actual delivery is the module CSS, which is complete; priority is 1 on both sides, and with a standalone base there is no BHL layering stack for it to order.
- **Why:** P4/T9: deliveries are served from JP hosts in this environment; inlining removes the candidate's runtime dependence on the EN wiki's code page — the candidate never reads scp-wiki.wdfiles.com/local--code. The remedy's ground: a frame parameter naming a fragment the delivery restructure abolished is a dead address in the delivered bytes, and the minimal correction is to drop the parameter, not to rebuild the delivery around it (the delivery-rebuild alternative was considered and rejected on proportion when the shape was ruled).
- **Verify:** Read orig L611–620 against cand L1–3 and L5; `grep -c '\[\[code' candidate.txt` = 0; `git show 5d95177 -- pages/theme:simple-yonder-jp.txt` (one line removed); the topology entry in classification.json (similarity 0.995).
- **Disposition:** Remedied post-verdict (commit 5d95177, sub-shape (D)); the stamp consequence is recorded in the Status block. The pre-repair state is the audit's and the frameaddr report's record, cited above.

### 4. Fonts and assets

- **What:** The candidate's import head (cand L6–8) carries three imports: Open Sans and Fira Code from fonts.googleapis.com, and jost.css from scp-wiki.wdfiles.com (the EN theme page's own file, which defines the Jost face the header uses). The two Google Fonts imports are byte-identical to the original's (orig L156–157). That identity is the end of a wave episode the final diff hides: the port as created (b0cfebd) carried the imports on fonts.bunny.net (three lines, the Fira Code import among them duplicated by the module merge); LOCALIZE-B charged them (P5, bunny.net ×3 including the duplicate, "revert to Google Fonts"); FIX4-REPOINT (443c608) repointed all three to googleapis; FIX4-MOPUP (379eb44) then removed the surviving duplicate. Assets: three URLs on scp-wiki.wdfiles.com survive — jost.css (cand L8), bg3.png (cand L80), logo.png (cand L86), all `local--files` paths of the EN theme page (orig L158, L214, L220). They are three of the T1 checker's hotlink errors (section 12) and the localize P5 finding (charged display-affecting, "rehost").
- **Why:** P5/KB-17 (patterns 9c5e907): only SCP-JP storage, Google Fonts, BootstrapCDN and cdnjs may be hotlinked; fonts.bunny.net is outside that list, so the imports returned to the canonical host (ledger (c3) class preamble: pattern 2 bunny set FIXED, simple-yonder named; KB-17: simple-yonder by FIX4-REPOINT). The three image/font files are the opposite case: re-hosting them is a posting-procedure act, class (ii), so the candidate keeps the original-state hosts (KB-58 deferred hosting; the campaign's owner order bars re-upload).
- **Verify:** `grep -n 'fonts.bunny.net\|fonts.googleapis.com' candidate.txt` (bunny absent; two googleapis imports); `grep -n 'scp-wiki.wdfiles' candidate.txt` (exactly L8, L80, L86).
- **Disposition:** Fonts FIXED (ledger (c3): P2 bunny preamble + KB-17, FIX4-REPOINT). Assets DISPOSITIONED (ledger (c3): P5, class (ii) / KB-58). The baseline T1 count of hotlink×6 is the pre-repoint state's count (the three bunny.net imports plus the three scp-wiki.wdfiles assets); the repoint removed the bunny three from the class.

### 5. Header, sidebar, site furniture

- **What:** No HEADERVAR label fired: the theme's `:root` variables (`--themeColor`, `--accentColor`, and the rest, orig L160 ff. → cand L26 ff.) are carried unchanged, and there are no `--header-title`/`--logo-image` overrides to localize. Sidebar and page furniture rules are byte-preserved inside the moved body, including the tail module's `div#side-bar { background-color: var(--whiteColor); }` (orig L632 → cand L476). No JP-specific layout adaptation was made or charged.
- **Why:** P9/T6 variables exist to be overridden where the JP environment requires it; this theme's design carries no site-title variables. P8 adaptation is owed only where the JP furniture's structure differs; no register raises a P8 item for this theme.
- **Verify:** `grep -n 'header-title\|logo-image' original.txt candidate.txt` (absent in both); read the `:root` blocks side by side.
- **Disposition:** Standing; no furniture item was charged for this theme in any register.

### 6. Text translation

- **What:** The candidate's reader-visible prose is its tail section (cand L721–730, label TRANS-UNANCHORED): the "+ Simple Yonder（SCP-JP 移植）" heading, the one-sentence description, the usage line `@@[[include theme:simple-yonder-jp]]@@` in the bare same-site form (cand L725), the credit thanks, and the 出典 (source) line naming the EN page and CC BY-SA 3.0. The original's intro prose (orig L18–26: the description, the import instructions, the Extra Mode instructions) was **not** translated in place — it was dropped with the sample body (section 8); its attribution content survives in the credit block (section 1) and in the CSS comment header, which stays in English verbatim inside the delivered CSS (cand L10–20; residue class R1, porter-visible only). The localize T5 pass raised no finding on the surviving prose.
- **Why:** P10: body and usage text are translated; here the port's documentation form is the compact tail section rather than a translation of the original's long documentation body, and that choice is recorded rather than hidden. The usage line's bare form is the post-sweep correct form (the sweep's premise: usage examples name the -jp posting name).
- **Verify:** Read orig L18–26 against cand L721–730, and the credit block (cand L707–717) for the relocated attribution.
- **Disposition:** Standing (the port itself); the documentation-body replacement is recorded in section 8 with its grounds.

### 7. Links

- **What:** The candidate's prose links are the credit block's source link (cand L716, to the EN original — the required ruling-3 back-reference) and the 出典 line (cand L729, the same target). The original intro's links (the author link, orig L18) left with the dropped prose. No tag-page or hub link survives to repoint, so P11 does not engage beyond the back-reference.
- **Why:** P11 repoints links to original-site tag pages and hubs to their JP counterparts where the link survives; here the carrying prose was replaced, and the one surviving link's target is this package's own original.
- **Verify:** `grep -n 'http' candidate.txt` — seven lines: three imports, two asset URLs, and the two credit/source lines (the frame carries no URL since the remedy).
- **Disposition:** Standing; no link item was charged for this theme in any register.

### 8. Structure

- **What:** Inside the CSS body the localize.md closing rule is honored: the stylesheet survives in the original's order at 0.995 similarity, and the JP corrections sit at the frame and the tail, not interleaved. Three structural changes sit outside the CSS body. (a) The sample body is dropped (B3, orig L11–143): the image-block exhibit, the titles collapsible, the tabview, the blockquote/table exhibits, the Extra Mode exhibit (with extra.png and the feature list), and the font specimen. (b) The Extra Mode apparatus is dropped (B5/B8, orig L622–631 and the closers at orig L861–862): the parameter gate `>[[ift{$xmode}gs -theme]]`, the hidden `component:toggle-sidebar` include it wrapped, and the xmode usage line; the gated tail module's **rules** survive, applied unconditionally inside the merged module. (c) The two original module bodies are merged into one (section 3). For (b), the production JP page carries neither the gate nor the toggle-sidebar include either (`grep -n 'xmode\|toggle-sidebar' pages-existing/existing:theme-simple-yonder.txt` — no hits), so the candidate's shape matches the JP lineage's treatment of the same theme.
- **Why:** Residue class R3: a sanctioned replacement and a silent deletion have the same diff shape, so the ground for each is stated. (a) The drop happened at creation (b0cfebd) and was visible to every later check; the localize pass itemized this theme's defects and did not charge the sample body (ledger class I, which charges exhibit restructuring when it reaches live structure, was not raised — the live structure, the CSS body, is intact), and the theme's element rendering is exercised through the decoration sample page (Change set, item 2). (b) The gate's function was to withhold the tail rules from non-theme inclusions; the candidate is a standalone page whose tail rules are its own, and the JP production lineage omits the apparatus as well. (c) The merge is the delivery inlining of section 3.
- **Verify:** `grep -n 'tabview\|image-block\|xmode\|toggle-sidebar' candidate.txt` (all absent) against original L31–143 and L622–631; the production grep in What.
- **Disposition:** Standing (restructuring recorded; no checker error arises from it).

### 9. Formatting only

- **What:** 2 WS-ONLY blocks: the blank-line padding left where the code body's three @imports were lifted to the head (B4, orig L156–158 → cand L22–24, three blank lines), and the clip-path trailing-whitespace cleanup (B6/B7, orig L830–837 → cand L674–681: trailing spaces after the polygon commas removed). The classifier counts 0 re-indentation blocks. Commit 3010ef7 ("Normalize trailing whitespace in the new port sources") is the creation-era pass of the same family.
- **Why:** Formatting-only churn is disclosed as its own class so it is never mistaken for semantic change; this is not R7 wholesale re-indentation (content lines keep their indentation, so follow-up diffs still apply).
- **Verify:** classification.json (2 WS-ONLY blocks, reindent_blocks 0); diff.md hunks 2 and 4.
- **Disposition:** None required.

### 10. Porter annotations

- **What:** none — no signature fired, and direct inspection agrees: the candidate contains no `[!-- ... --]` translator notes and no editor line (`grep -c '\[!--' candidate.txt` = 0). The only added text with no original counterpart is the frame, the credit block, the tail prose section and the font-import repoint, each accounted for in its own section. The CSS comment header is the original's own, carried verbatim, not an annotation.
- **Why:** R2: porter additions are listed so they are never mistaken for original content or for translation; here the ground for "none" is the grep above plus the section-by-section accounting.
- **Verify:** The grep in What.
- **Disposition:** None required.

### 11. Dispositions and exceptions

- **What:** Every finding not fixed in the candidate, in one place. (1) The three EN asset URLs (cand L8, L80, L86): T1 hotlink family, DISPOSITIONED class (ii) — posting-time rewrites and original-state asset hosts; re-upload is barred by owner order and deferred hosting is the recorded state (GOSIGN2-LEDGER (c1) hotlink entry; (c3) P5, KB-58). (2) The render findings: candidate-inherent page-overflow 474–494px@320/375 (fixed min-width), rate-preview ⓘ/× glyphs near-invisible (contrast 1.03), notice×sidebar at 768 — DISPOSITIONED in (c2) as the recorded cross-cutting shapes. (3) The T2 sample's missing machine verdict (webkit never completes): a coverage caveat (render_check exit 2), DISPOSITIONED as not a theme defect (ledger (a) caveats). The frame's dead self-address is **not** in this list: it was remedied post-verdict (section 3), not dispositioned. No item for this theme is left as an unexplained exception.
- **Why:** A disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- **Verify:** Each item names its deciding register above; the KB IDs resolve in patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa.
- **Disposition:** DISPOSITIONED (items 1–3).

### 12. Verification

- **What:** (a) T1 source check, baseline 2026-11-16: exit 1, 6 errors / 1 warn / 1 info; the errors are hotlink×6 (section 4 reconciles the count with the pre-repoint state); the warn and info codes are not itemized in the extracted row (T1-ROWS row 38). Register (c1) dispositions the hotlink class as (ii). (b) T2/T3 render: FINDINGS, all items dispositioned in (c2) (section 11, items 2–3); the row records no credit-modal error for this theme (RENDER-ROWS-1, RENDER-D2). (c) T4 localize plus follow-up: FINDINGS with 1 display-affecting item (LOCALIZE-ROWS row 38, source LOCALIZE-B — the P5 EN-storage hotlinks); outcomes P5 DISPOSITIONED / P6 FIXED (ledger (c3)), with the P2 bunny fix recorded in the (c3) class preamble and KB-17. The follow-up side: the reference revision 166 is the revision the production counterpart's drift check was run against, and sources.tsv records that drift as 一致. (d) T5: judged jointly with T4 by the source lane; no display-visible residue was recorded for the surviving prose. (e) This package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and re-derives the verdict stamp (whose state is qualified in the Status block). Counts in this README are the classifier's (8 change blocks) and the generator's (diff.md: +45/−174 in 5 hunks); the two count different units over the same pair.
- **Why:** Verification claims name the cheapest deciding check and its result, not a general assurance.
- **Verify:** Re-run the checker on `pages/theme:simple-yonder-jp.txt`, and `python3 review/build_review.py --check` in this repo.
- **Disposition:** PASS (ledger determination, (b) row 38).

## Per-theme record

### The frame arrived inside a repoint commit (wave attribution)

The ledger's (c3) register attributes this theme's P6 fix to "the frame waves". The file's own history is narrower: the JP interwiki frame (now cand L1–3) landed in commit f1138e4, whose subject is the FIX-P4 pattern-4 repoint of base-theme CSS imports across 39 files. This file has no base-theme import to repoint; the commit's diff for it is the frame addition plus the credit adaptation line (section 1). The register's outcome is correct — P6 is FIXED in the current bytes — and only the vehicle differs from the wave name; this package follows the git record.

### The frame's dead address and its (D) remedy (post-verdict repair)

The frame FIX-P4 added carried the theme= self-address in the original's own form. Because the port had restructured delivery from the code exhibit to a live module, the address named a fragment that no longer exists. The population audit (FIX-CODEADDR.md) listed the file in the no-target class; the frameaddr lane's classification (FIX-FRAMEADDR.md §4) placed it among the twelve "live-original" references that fit none of the three ruled sub-shapes, and left it unedited pending a ruling; the coordinator's ruling for that shape (sub-shape (D) in the landing commits) applied the drop-the-parameter remedy, landed as commit 5d95177 (one line removed). This package is built against the remedied bytes, and the stamp consequence (STALE on canonical regeneration) is recorded in the Status block. The remedy also changed this package's classification: DRAFT-HOST, which fired on the pre-repair pair, no longer fires, because the candidate carries no draft-host address at all.

### The credit block's provenance is the T1 wave, not a localize charge

The (c3) register lists no P3 outcome for this theme, yet the candidate carries a complete eight-field credit block. Its provenance is commit b816e10 ("gosign2 T1 fixes: credit fields/furniture (rows 1-44), colon encoding, foreign-include rewrites"), which added the block's eight fields in one insertion; the localize lane (LOCALIZE-B) had charged only P5 and P6 for this theme. A reader reconciling the registers against the bytes needs both facts: the block is a T1-checker-class repair (credit-missing-fields is class (i) in the T1 disposition classes), and its absence from (c3) is a register-scope artifact, not a gap in the file.

### The production counterpart and the Phase 17 patch

`pages/phase17-diff-simple-yonder-jp.txt` prescribes, for the live production page, a smaller edit than the candidate embodies: a two-field credit block (reference revision + source link) inserted after the production page's own `[[iftags +テーマ]]` line, leaving the production page's existing Rate furniture in place. The candidate in this repo is the fuller Sigma-10 form (preview credit block with all eight fields plus the adaptation line, bare Rate removed). The two records agree on the fact they exist to record (the migration is anchored to rev 166 with a source back-reference) and differ in form because they govern different pages: the patch page governs the production page's minimal migration, the candidate is the review population's full form. Recorded so the difference is not mistaken for drift.

### Post-package repairs (REFRESH3-E)

This package has **no post-package repair to record**: `candidate.txt` was recopied from the current canonical `pages/theme:simple-yonder-jp.txt` and found byte-identical to the as-built copy (its only post-port page commit is 5d95177, which predates this package's build at 85057d0). `diff.md` and the verdict stamp were regenerated with `python3 review/build_review.py` and are unchanged. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

For the record chain: this theme is one of FIX-FRAMED.md's twelve live-original files. Its frame was sub-shape (D) — `theme=` named its own /1 code block, which the candidate (zero `[[code]]` blocks; CSS in live `[[module CSS]]`) cannot contain — treated as (B) with the minimal remedy of dropping the `theme=` line and keeping the frame. The remedy landed at 5d95177; it is already in this package's candidate and is recorded in the per-theme item "The frame's dead address and its (D) remedy (post-verdict repair)" above, so no frame byte postdates the build. No other post-package repair touches this file.

## Change set outside the two diffed files

The diff covers two files; the port's full change set is larger. (1) `pages/phase17-diff-simple-yonder-jp.txt` — the production-migration patch page described above (24 lines), created in the same Phase 17 commit (8dcac74) that added the candidate's prose-tail revision line. (2) `pages/theme-decoration-sample-simple-yonder-jp.txt` — the render sample page (an include of the candidate and of the shared `theme-decoration-sample`); it is the "sample" the T2/T3 checks rendered. (3) `pages-existing/existing:theme-simple-yonder.txt` — the production counterpart itself, held in this repo as the K6 third source; the candidate was measured against it in Provenance. (4) The delivery itself: the candidate's module CSS is inline, so there is no companion code page; since the (D) remedy the frame names no code address at all (section 3).

## Multi-wave provenance

The candidate's current state is the product of one creation and six wave touches, not a single porting pass: b0cfebd created it (inlining, sample-body and xmode-apparatus drops, bunny.net import forms) with 3010ef7 normalizing its trailing whitespace; Phase 17 (8dcac74) recorded the reference revision in its prose tail; the gosign2 T1 fixes (b816e10) added the preview credit block; FIX-P4 (f1138e4) added the JP frame and the credit adaptation line; FIX4-REPOINT (443c608) reverted the bunny imports to Google Fonts; FIX4-MOPUP (379eb44) removed the duplicated Fira Code import the module merge had produced; the ledger determination passed the theme with no OPEN items, so the FIX5 wave had nothing to re-judge; and the frame self-address remedy (5d95177, sub-shape (D)) removed the frame's dead theme= line after the verdict. Citations, in place of a changelog: GOSIGN2-LEDGER.md (b) row 38, (c1) hotlink entry, (c2) simple-yonder entry, (c3) simple-yonder entry and the pattern-2/KB-17 preambles; T1-ROWS row 38; LOCALIZE-ROWS row 38; RENDER-ROWS-1 (RENDER-D2) simple-yonder row; FIX-CODEADDR.md (no-target listing); FIX-FRAMEADDR.md §4 (the live-original classification). The go-sign re-run over that record is what the Status block certifies, subject to its stamp note.

## Appendix — residue blocks

No residue: every block carries a specific label, and there are no heuristic blocks either (8 specific / 0 heuristic / 0 residue). The two blocks a reviewer is most likely to misread are resolved in place: B5 (orig L609–630 → cand L475), whose primary label is EXHIBIT-RESTRUCTURE, carries the SELF-DELIVERY span (the original's tail module import and frame, whose candidate-side counterparts are the head module and the remedied frame) and the xmode-gate deletion of section 8; B3 (orig L11–143 → cand L10) is the sample-body drop of section 8, labeled EXHIBIT-RESTRUCTURE with the INFO-DEL span.

## License and attribution

- **Title:** Simple Yonder Theme
- **Author:** EstrellaYoshte
- **Source:** https://scp-wiki.wikidot.com/theme:simple-yonder — revision 166 (revision date 2024-01-10 02:19:29)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: ukwhatn — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
