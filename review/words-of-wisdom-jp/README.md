# Review package — theme:words-of-wisdom-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:words-of-wisdom-jp — origin EN, population #159 [GOSIGN2-LEDGER (b) row 159]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 2c5b26d15b2a7217277a27adcdde56cc93b925e6b81f80b54a4151f66f5a2b25); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 1 warn / 2 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 174; GOSIGN2-LEDGER (b) row 159]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page hidden-* cluster + sidebar-unreachable confined to chromium-375, whose only hotlink host is http.cat = transient 503 capture, not a result; sample credit-modal (preview-form) + 884px@768 overflow + runtime-hotlink site-theme chain. [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-2 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 159, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 159]
- FIX5 re-judgement: item 41 (class B) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 41]
- Computed against: canonical commit 3f0aa788d3a56dfcfb83c698ec2c7a4a9bb44f44; candidate file pages/theme:words-of-wisdom-jp.txt sha256:2c5b26d15b2a7217277a27adcdde56cc93b925e6b81f80b54a4151f66f5a2b25; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:words-of-wisdom` on scp-wiki (EN), revision 12 — `original.txt` in this package (300 lines / 6,098 bytes; `wc -l` reports 299, the last line is unterminated) |
| Candidate | `theme:words-of-wisdom-jp` — `candidate.txt` (342 lines / 8,853 bytes), a byte copy of `pages/theme:words-of-wisdom-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy), in the layered form this theme's `review/sources.tsv` kind records (K5b-3): the candidate layers over `theme:shattered-thoughts-jp` exactly as the original layers over `theme:shattered-thoughts`, and this package's diff covers the theme's own layer only. The base candidate has its own package (`review/shattered-thoughts-jp/`). |

The sources.tsv note for this theme is the K5b-3 layering note above; it makes no supersession claim, and no correction is owed.

Status note: the verdict stamp above reads STALE by design. It was computed against canonical commit 722ceb5 — the frame self-address remedy that dropped this frame's `theme=` parameter (sub-shape (B), section 3) after the FIX5 verdict. The stamp's verdicts describe the pre-remedy file; the per-theme record below re-derives the theme's one blocking item on the current bytes.

Summary: a Wandsmen sub-theme delivered as an inline CSS module layered over Shattered Thoughts, its stylesheet hidden behind a conditional wrapper div. The port preserves the layering and repoints the base import to the JP base candidate's delivery, adds the standard head frame and the preview credit, adds a JP license box the original lacks, applies the pattern-7 font supplement, and translates the body. The theme carried one blocking item, 41 (class B), re-derived in the per-theme record and confirmed. One minor flag arises: the theme's banner comment stands twice in the delivered module (section 8).

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMMENT-TEXT | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DRAFT-HOST | 3 |
| ESCAPED-INCLUDE | 1 |
| FONT-IMPORT | 1 |
| IFTAGS | 3 |
| INCLUDE-REPOINT | 1 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 2 |
| LICENSE-BOX | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 8 |
| TRANSLATION-ANCHORED | 6 |

Counts: 25 blocks, 17 specific, 3 heuristic, 5 residue, 0 skipped. Topology: the stylesheet is an inline module on both sides (the classifier inventories no components and no moves); the layering over the base candidate is section 3. The diff is Tier 1 (+92/-50, 7 hunks).

## 1. Credit and attribution

- Credit block (candidate L7-17; CREDIT-PREVIEW + TASL-FIELDS), nine fields. 著者 names Cole 13 and carries the parent-theme attribution inside the field itself (親テーマ: Shattered Thoughts Theme / yossipossi作、CC BY-SA 3.0、拡張許可済み); 著作権者 is `[[*user Cole 13]]`. The original's byline (original L12, by Cole 13 for chaucer345's Wandsmen) and its permission line (original L16, yossipossi's permission to extend Shattered Thoughts) are both carried; the permission is also expanded in the translated prose (candidate L28). No pointer-in-place-of-a-name defect stands, and no attribution the original carries is dropped.
- The bare `[[module Rate]]` that stood at original L5-7 is this theme's blocking item 41; the per-theme record re-derives its removal. Census: `[[module Rate]]` 1 → 0 (class P3 / KB-09, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa: the preview credit module is rate-bearing).
- License box ADDED (candidate L58-80; LICENSE-BOX): the original has none. The candidate's `license-box-backend` (author=Cole 13) carries an entry for the theme itself (Cole 13, CC BY-SA 3.0), an entry for the base theme Shattered Thoughts (yossipossi, CC BY-SA 3.0, with the source line and the note that the original was read at its revision 34 and will be posted as the JP candidate), entries for the base's two image files, and entries for the theme's own two image files with 作者 and ライセンス honestly entered as 記載なし (the EN source states neither). This is the T4 supplement in the population's established form; nothing is claimed that the original does not support.
- T7 credit-module CSS: none in either file (`grep -c creditButton` = 0 / 0).
- Verify: read candidate L7-17 and L58-80 against original L12-16.

## 2. Includes and components

- Live includes: the head frame (section 3) and the credit pair (section 1).
- Usage examples: the original teaches two includes, its own (original L21) and the base's (original L23-25, the "+* With this:" section). The candidate carries its own example repointed (candidate L33, `:scp-jp:theme:words-of-wisdom-jp`) under the single heading `+* 任意のwikiで:` (candidate L30; blocks B9, COMPONENT-SWAP + ESCAPED-INCLUDE). The base-include example has no counterpart section, and that is adjudicated replaced, not silently dropped: the candidate no longer asks the user to include the base at all, because it imports the base candidate's code itself (candidate L89) and documents the layering in prose (candidate L28) and in the license box (section 1). The original's own delivery was likewise automatic (its L56 `@import`); the "With this" example was documentary.
- No include is duplicated.
- Verify: `grep -n 'include'` on both files; read original L21-25 against candidate L28-33.

## 3. Delivery and code loading

- Layering preserved: the conditional wrapper div stands with its gate tag localized (original L52 `-theme` → candidate L84 `-テーマ`; block B15), and the stylesheet remains an inline `[[module CSS show="true"]]` (candidate L86) inside it. The base import is repointed from the original's `https://scp-wiki.wikidot.com/theme:shattered-thoughts/code/1` (original L56) to the JP base candidate's delivery `https://sigma10-jp-test.wdfiles.com/local--code/theme%3Ashattered-thoughts-jp/1` (candidate L89), per ruling 1 and the cross-theme dependency rule (a dependent theme imports the base theme's JP port candidate delivery, never the raw upstream delivery; KB-14, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa).
- The head frame stands added at candidate L1-3 (priority=1) and carries no `theme=` parameter: delivery is the inline module, so no self-delivery address exists. The parameter the frame carried was dropped after the verdict by the frame self-address remedies (commit 722ceb5, sub-shape (B): parameter dropped, frame kept; the commit message names this theme in its (B) list), recorded here with its citation, not re-litigated. That remedy is the STALE stamp's ground.
- `@charset "utf-8";` stands added as the module's first line (candidate L88).
- Census, counting every code-block form: zero code blocks on either side. Delivery is the inline module, so the code-address census has no reference to check.
- Verify: `grep -n 'local--code\|module CSS' candidate.txt`; `git show 722ceb5 -- pages/theme:words-of-wisdom-jp.txt` for the parameter drop.

## 4. Fonts and assets

- Fonts (class P7): the original's Mate SC load (fonts.bunny.net css2, original L64) becomes a Google Fonts css2 import combining Mate SC with Noto Sans JP wght@400;700 (candidate L91; FONT-IMPORT 1, JPFONT-LOAD 1). The stacks name `'Mate SC', 'Noto Sans JP', serif` (candidate L138, the header rule; candidate L264, the sidebar headings; JPFONT-STACK 2) — the JP face is loaded and referenced, which is exactly the ledger's pattern-7 note for this theme ("JP face loaded and referenced, L143/L269" in the then-current file; the mechanism stands in current bytes at L91/L138/L264).
- One further load stands at candidate L90 (Open Sans). Its consumer is the base layer: `theme:shattered-thoughts-jp`'s stacks name 'Open Sans' (its candidate L216, L238, L246), and this page's module is the channel that delivers the base. Recorded as part of the layering, not as an unapplied load; no stack in the theme's own layer names a face that nothing loads.
- The porter prose at candidate L19 announces the font program — section 10.
- Assets: the theme's two image files are re-hosted to the candidate's own draft-host folder with the scheme upgraded (original L109, `http://scp-wiki.wikidot.com/local--files/theme:words-of-wisdom/WANDPNG%20.png` → candidate L152; original L121, `MRSTAR23.webp` → candidate L164). Both are T1 pseudo-ref loci (section 11) and both are entered in the license box (section 1).
- Verify: `grep -n 'Noto Sans JP\|Open Sans' candidate.txt`.

## 5. Header, sidebar and site furniture

- The sidebar rules are extended to the `#interwiki` DOM (candidate L263-280: the heading, menu-item img, side-block and link rules are each doubled with their `#interwiki` counterparts) where the original names `#side-bar` only (original L220-237). This is a JP-environment supplement: the interwiki sidebar the frame delivers receives the theme's sidebar styling. It is the R6 JP-DOM selector-extension shape (the in-place correction form the R-fix-18 batch proposed naming as a standing class); the classifier's residue blocks B22-B24 are these extensions (appendix).
- The header content string "The Wandsmen" (candidate L136 = original L93) is kept in English: the GoI's name, an identity string under ruling 2, standing.
- Verify: read candidate L263-280 against original L220-237.

## 6. Text translation

- The body is translated throughout (TRANSLATION-ANCHORED 6 blocks, TRANS-UNANCHORED 8): the headings, the intro, the usage prose, the exhibit specimens, and the permission/layering prose (candidate L28, expanded from original L16).
- The credit title field "Words Of Wisdom Theme" is kept in English; the body supplies no Japanese title form, and the string is the theme's name (an identity string under ruling 2), standing, uncharged.
- Verify: the translation spans in `classification.json` against both files.

## 7. Links

- The only page reference in prose is the usage example (section 2): `grep -n '\[\[\[' candidate.txt` returns no hits, the example being an include form. The credit block's `[[*user Cole 13]]` is an attribution carrier (section 1), and the license box's source lines name the base theme's page as provenance text, matching the `@import`'s target (section 3).
- Verify: the grep above; read candidate L58-80.

## 8. Structure

- **Minor flag — duplicated banner comment.** The theme's banner comment stands twice in the delivered module: candidate L94-99, preceded by the porter layer header at candidate L93, and again verbatim at candidate L101-106. The original carries it once (original L57-62). No rules are duplicated, only the comment, so there is no rendering effect; it is nonetheless duplicated content inside the delivered stylesheet, flagged minor with both loci for the coordinator.
- An original defect the port repaired silently: the original module's tail carries an unmatched closing brace (original L298). Measured by depth, not count: the original's module body ends at final depth -1 with the extra close at L298; the candidate's module body ends at depth 0 with no extra close (residue block B25). Browsers ignore an unmatched top-level `}`, so rendering parity holds either way; recorded as an original-defect repair.
- Footnote: one live `[[footnote]]` on each side (original L29, in the tabview specimen; candidate L37) and `[[footnoteblock]]` on neither side — parity, the base layer supplying the footnote rendering (KB-59 family), not a candidate drop.
- Exhibit census: the tabview and typography specimens stand against the original; the base-include example is adjudicated in section 2.
- Verify: `sed -n '93,107p' candidate.txt` against original L57-62; a brace-depth scan over original L55-298 and candidate L87-340 (-1 against 0).

## 9. Formatting only

- None as a standalone class: the classifier reports no WS-ONLY blocks. The diff's seven hunks are the named classes above.
- Verify: the label counts in `classification.json`.

## 10. Porter annotations

- Two R2 annotations: the prose font-program note at candidate L19 (section 4), and the comment-form layer header `/* ===== Words Of Wisdom Theme（本テーマ） ===== */` at candidate L93, marking the theme's own layer at the head of its module. Both statements match the bytes. The L93 header is also the locus of section 8's duplication note: the banner it introduces is the first of the two copies.
- Verify: read candidate L19 and L93.

## 11. Dispositions and exceptions

- Draft-host lines (pseudo-ref x3, the T1 baseline's errors): candidate L89 (the base import), L152 and L164 (the re-hosted attachments) — class (iii) draft forms, rewritten at posting, DISPOSITIONED. The `!important` info (candidate L203) is recorded verbatim.
- Render row (RENDER-ROWS-2, RENDER-S2-D (EN23)): the page's hidden-* cluster and sidebar-unreachable findings are confined to chromium-375, whose only hotlink host is http.cat, a transient 503 capture, not a result; the sample carries the credit-modal errors (preview-form property; `credit:start-preview` has no modal mechanism) and an 884px@768 overflow, plus the runtime-hotlink site-theme chain (KB-40, environment layer) — DISPOSITIONED as recorded in the stamp.
- The (B) frame remedy (section 3) is a recorded post-verdict change, not an exception. No class (i) item stands for this theme beyond the minor banner flag of section 8.

## 12. Verification

- T1 run by this lane on the current candidate (`check_source.py --kind theme`): error 3 / warn 0 / info 1 — all three errors pseudo-ref at L89, L152, L164, the info the `!important` note at L203, and no `double-rate` line. This is exactly FIX5-FURNA's after state (3/0/1); the stamp's baseline (3 errors / 1 warn / 2 infos) describes the pre-FIX5 file.
- T2/T3: FINDINGS with the dispositions in section 11. T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `69fbf0a79c7abc1322252e5ec1f0cec7cd23acc1eb98b88029f3da3ee4e6ad17`); `original.txt` hash equals the sources.tsv value (`bc57f8d4e49d7eb76f3cff49486728bef7b63f99db616adf9212bbd7839d397b`); brace-depth scans as reported in section 8; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 41 (ledger (b) row 159, class B): a duplicate bare `[[module Rate]]` at the port's then-current L9, immediately before `credit:start-preview`, left as an unmade staff call by the localize lane (LOCALIZE-S2-C row and its item 14; display-affecting, two rating widgets rendered).
- What the fix was supposed to change: remove the unlabelled duplicate block, leaving the rate-bearing preview credit as the page's only rating widget. The FURNA lane report's evidence: the block at pre-edit candidate L7-9 was unlabelled (`[[>]]` / `[[module Rate]]` / `[[/>]]`), with no paired exhibit label, so the labelled-exhibit exception does not apply; checker 3/0/2 → 3/0/1, the `double-rate` info cleared, no new errors. The report also records that no class-D item is assigned to this theme: the ledger's (c3) line already dispositions its pattern-7 charge (section 4).
- Supplement re-judgement: FIXED, FIX5-FURNA, commit 9e8931f.
- Re-derived from this package's bytes: the original carries the identical bare Rate at original L5-7, inside its gate. `git show 9e8931f -- pages/theme:words-of-wisdom-jp.txt` removes exactly the `[[>]]` / `[[module Rate]]` / `[[/>]]` block and the following blank line ahead of the credit include. The current candidate contains no `[[module Rate]]` anywhere (`grep -c` = 0), and its only rate-bearing element is `credit:start-preview` (candidate L7-17). This lane's checker run reproduces the after state, 3/0/1.
- Closure: CONFIRMED on current bytes. The verdict stamp is STALE for the later frame remedy (section 3), which does not touch the credit flow; the closure is re-derived from the package, not inherited from the stamp.

## Per-theme record


### Post-package repairs (REFRESH3-D)

FIX-FRAMEADDR (`722ceb5`, sub-shape (B)) lands *before* this package's candidate build (`c12dbde`), so the frame at L1 was already remedied; recopy confirms no byte change from it. The one post-package repair is the duplicate-banner removal below.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Awords-of-wisdom-jp/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- **FIX-RFIX20 — duplicate banner comment** (report `R/review-scout/FIX-RFIX20.md`; landing `3f0aa788d3a56dfcfb83c698ec2c7a4a9bb44f44`, 2026-11-17): the second, byte-identical `/* Words of Wisdom theme … CC BY-SA 3.0 */` banner (7 lines) was removed, so the licence banner now stands once at candidate L94–99. Recopy removed 7 lines (342 → 335).

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-words-of-wisdom-jp.txt` — the render-check sample page for this theme (it includes the candidate at its L1).
2. `pages/theme-decoration-sample-words-of-wisdom.txt` — the production-side sample page.
3. `theme:shattered-thoughts-jp` — the base candidate this theme layers over (section 3); it is a population row of its own with its own package, and this package's diff covers the theme's own layer only.

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-C) produced the port: the preview credit, the license box, the font supplement, and the translation; the bare Rate survived that wave as the unmade staff call, and the wave's record already dispositions the pattern-7 font item.
- FIX5-FURNA (commit 9e8931f) removed the Rate and closed item 41.
- The frame self-address remedies (commit 722ceb5) dropped the frame's `theme=` parameter (sub-shape (B)) — the post-verdict change behind the STALE stamp.

## Appendix — heuristic and residue adjudication

The classifier reports 3 heuristic blocks and 5 residue blocks. All resolve by shape:

- Residue B17: the original's bunny import line (original L64) has no separate added counterpart, because its replacement rides inside B16's span (the combined Google Fonts imports at candidate L90-91) — section 4.
- Residue B22-B24: the `#interwiki` sidebar selector extensions — section 5.
- Residue B25: the dropped stray closing brace (original L298) — section 8.
- The heuristic mass is TRANS-UNANCHORED prose translation (section 6) and the translation component of the license-box block (section 1).

No heuristic or residue block is left unadjudicated. One minor flag arises from this package (the duplicated banner comment, section 8).
