# Review package — theme:quand-le-soleil-se-couche

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:quand-le-soleil-se-couche — origin FR, population #29 [GOSIGN2-LEDGER (b) row 29]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 8c91dd76d53081f51c32bf7c17922d6299531c03428bb069351604eb69cce414); the verdicts below were computed against that pre-change file, and the record verdict stands: a candidate revised through the campaign's recorded repairs is posted like a PASS row, with the change recorded in its package
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 2 errors / 3 warns / 1 info (pseudo-ref×2); standing classes dispositioned in register c1 [T1-ROWS row 29; GOSIGN2-LEDGER (b) row 29]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — literal unsubstituted `{$sous-titre}` in header on all views of both pages (real defect), WebKit CC "S", 768px notice×sidebar overlap, 884px@768 overflow, notice/code clip, sample credit-modal. [RENDER-ROWS-1 (RENDER-C row 29)]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row [RENDER-ROWS-1 row]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-C row 29)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 0 [LOCALIZE-ROWS row 29, source LOCALIZE-B]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 29]
- FIX5 re-judgement: item 5 (class A) FIXED — FIX5-STRUCTB §5, commit 435a6bb: evidenced default set at the slogan variable; literal {$sous-titre} absent file-wide; spot-verified for this supplement [GOSIGN2-LEDGER-SUPPLEMENT (a) item 5; (c) check 4]
- Computed against: canonical commit 722ceb5c949172bb5185d51ef56ce4119ee4fa91; candidate file pages/theme:quand-le-soleil-se-couche.txt (shared original+port page; no -jp file) sha256:8c91dd76d53081f51c32bf7c17922d6299531c03428bb069351604eb69cce414; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## Status

| | |
|---|---|
| Verdict | **PASS** — go-sign re-run (this theme is one of the 286 of 286 pass-eligible themes) |
| Blocking items at ledger time | GOSIGN2-LEDGER.md §(e) item 5 [A] (KB-06: the slogan variable's default is the unsubstituted include parameter `{$sous-titre}`, which renders literally in the header) |
| Re-judgment | GOSIGN2-LEDGER-SUPPLEMENT.md row 5: **FIXED** (FIX5-STRUCTB §5, commit 435a6bb); supplement §5 spot-check 4: PASS; re-derived from this package's bytes in the per-theme record below |
| Standing items | **DISPOSITIONED** — ledger §(c3): P3 credit fields FIXED (credit waves), P6 FIXED (frame waves); ledger §(c2) render row: WebKit CC "S" glyph, 768px notice/sidebar overlap, 884px@768 overflow, notice/code clip (cross-cutting classes), sample credit-modal preview form (KB-32) |
| Flagged in this package | No defect flags. Three observations are recorded rather than passed over: the credit block's author field names the adapter where the FR banner names the creator first (section 1), the original's Space Mono import is dropped with no stack consuming it on either side (section 4), and the sample body's footnoteblock stands escaped where the production page carries it live (section 8) |
| Go-sign basis | COMPLETION-REPORT.md §10 (go-sign issued; 81 FIXED / 26 DISPOSITIONED / 0 OPEN across the sweep) |
| Named exception | None for this theme (the sweep's single named exception is theme:amethyst-v2, which has no candidate) |
| Special row | **K7** (SPECIAL-ROWS.md): the candidate keeps the original's fullname; see section 0 |

## Provenance

| | Original | Candidate |
|---|---|---|
| Page | theme:quand-le-soleil-se-couche | theme:quand-le-soleil-se-couche (same fullname, K7) |
| Wiki | fondationscp.wikidot.com | SCP-JP Sigma-10 candidate (canonical repo) |
| Reference revision | 13, as recorded in the candidate's credit block: **初訳時参照リビジョン:** 13 | — |
| Source of this copy | Fresh fetch of the FR page at revision 13 (2026-11-17), via the mirror store (class FETCH-REGEN, hash-verified against review/sources.tsv) | Canonical file `pages/theme:quand-le-soleil-se-couche.txt`, copied at worktree HEAD 933c416 |
| Lines / bytes | 141 lines / 3,436 bytes (the last line carries no trailing newline, so `wc -l` reports 140) | 215 lines / 6,169 bytes (same convention; `wc -l` reports 214) |
| SHA-256 | 8f0b702233d4ab7de88516b118df0ce23e0ba684a5cf8c59ee02f524cca544aa | 8c91dd76d53081f51c32bf7c17922d6299531c03428bb069351604eb69cce414 |

Three pages share this one name on three wikis: the FR original (this package's mirror), the live JP production page (`pages-existing/existing:theme-quand-le-soleil-se-couche.txt`, 201 lines; the start-themes TSV records it as existing, drift status 一致, with no phase17 diff page), and this check-wiki candidate. The candidate's documentation body and credit block are inherited from the production JP port: the credit block (candidate L7–16) is byte-identical to the production page's, and the body matches production except where the check environment required changes. The CSS zone is reworked for the Sigma-10 environment (draft-host file URLs, the inline framework-mapping rules of section 8, the KB-06 default). The provenance route is therefore production-mediated derivation from the FR original at revision 13, declared here per the R4 rule: a reader who diffs the candidate against the FR mirror alone will see production's porting choices (the sample body, the credit form) mixed with the check-environment rework, and this package separates the two where it matters.

## Summary

A small French Sigma-9 theme for the "Quand le Soleil se Couche" canon: a grayscale filter over the stock layout, a flickering SCP header, and its behaviour driven by `ct_*` framework variables that the fondationscp component `modele-theme` consumes. The candidate keeps the original's inline-module delivery, replaces the FR framework component with explicit mapping rules onto the stock Sigma-9 DOM, re-hosts the two images to the draft host, and inherits the production JP page's documentation body and credit block. Measured churn (diff.md, the generator's difflib count): +178/−99 in a single hunk; the differ aligns the pair poorly because the candidate's body is production's sample body, which the FR page does not carry at all. The one blocking item (the literal `{$sous-titre}` slogan) is closed and re-derived below; no defect is flagged.

## Per-theme record — the FIX5 closure of ledger item 5, re-derived

- **The item.** GOSIGN2-LEDGER.md §(e) item 5 [A]: a KB-06 parameter defect. The candidate's own include passes no `sous-titre` argument and the slogan variable set no default, so the literal text `{$sous-titre}` rendered in the header on all views of both pages; render T3 called it a real defect. The ledger located it at L107 of the then-current file. SWEEP-A1 had adjudicated quand the exception to the parameter-interface false-positive rule: this theme's parameter is a genuine defect, not an interface.
- **The re-judgement.** GOSIGN2-LEDGER-SUPPLEMENT.md row 5: FIXED, by FIX5-STRUCTB §5, commit 435a6bb: "evidenced default set at the slogan variable; literal {$sous-titre} absent file-wide". Supplement §5 spot-check 4 records the same grep and the header rule it feeds.
- **What the fix was supposed to change.** Give `--ct_cnt_alt-slogan-txt` a fixed default so views that pass no include argument (direct views, the display-check sample) render a real slogan, while keeping the documented `sous-titre` include parameter working for pages that pass one.
- **Re-derivation from this package's bytes.** (1) The pre-fix state: the mirror carries the defect's source form (original L32: `--ct_cnt_alt-slogan-txt: "{$sous-titre}";`), and the fix commit's diff shows the candidate carried the identical line before 435a6bb. (2) The fix commit changes exactly two things in this file: the slogan line becomes `--ct_cnt_alt-slogan-txt: "太陽が沈む時";` with a trailing comment naming the KB-06 rationale, and the porter banner comment is rewritten to record that the candidate supplies a fixed default for direct views and the sample. (3) Current bytes: candidate L107 carries the default; `grep -F '{$sous-titre}' candidate.txt` returns no matches, file-wide; the variable feeds the header rule at candidate L152–155 (`#header h2 span::before { content: var(--ct_cnt_alt-slogan-txt); … }`). (4) The default is evidenced, not invented: 太陽が沈む時 is the theme's own JP name (credit title, candidate L8; intro, L18), the slogan form of the title the FR original carries. (5) The parameter contract survives: the usage example (candidate L19–21) still documents `|sous-titre=` for includers, exactly as the SCP-JP hub documents it; only the unsubstituted-literal default changed. The closure holds on the current bytes.
- **Post-verdict change.** One line: commit 722ceb5 (frame self-address remedies) dropped the interwiki frame's `theme=` parameter, which pointed at `local--code/theme%3Aquand-le-soleil-se-couche/1`; the candidate contains no `[[code]]` blocks at all, so the address named nothing (sub-shape (B) of FIX-FRAMEADDR.md: the frame include is kept, the dead parameter dropped). The supplement's line numbers for the slogan (L108, feeding L154) are the pre-remedy numbering; the same lines stand at L107 and L153 now. The generated stamp therefore reads STALE rather than carrying the PASS onto changed bytes; the change is outside item 5's scope and is recorded here so the reader can see exactly what moved.

## 0. Header / provenance

- What: the original opens with its `[[iftags +thème]]` gate and intro line (original L1–3), then the framework include (L5–11). The candidate opens with the interwiki-style frame (candidate L1–3, priority=1, no theme= parameter after the 722ceb5 remedy), then the localized gate `[[iftags +テーマ]]` (L5). Provenance route: production-mediated derivation from the FR original at revision 13 (Provenance section above); mirror class FETCH-REGEN, fetched once for the mirror freeze and hash-verified.
- Why: the frame is the environment's standard furniture (P6/T3); the K7 naming rule (SPECIAL-ROWS.md) requires the identity of names across the three wikis to be stated, which the Provenance section does.
- Verify: `sha256sum original.txt` against the review/sources.tsv row; read candidate L1–16 against production `pages-existing/existing:theme-quand-le-soleil-se-couche.txt` L1–14 (identical below the frame).
- Disposition: provenance recorded; no supersession note stands against this theme in review/sources.tsv (its note is the K7 identity note, which the bytes confirm).

## 1. Credit and attribution

- What: the candidate carries the eight-field preview credit block (candidate L7–16), byte-identical to the production page's block: タイトル 太陽が沈む時 テーマ, 翻訳責任者 [[*user koku4]], 翻訳年 2026, 原題 Thème de Quand le Soleil se Couche, 著作権者 [[*user Cyrielle Centori]], 作成年 2024, 初訳時参照リビジョン 13, 元記事リンク to the FR original on fondationscp.wikidot.com (the host recorded for the original in review/sources.tsv). One observation, recorded not flagged: the FR banner (original L18) credits creation to Cauchynambour and the international/English adaptation to Cyrielle Centori, while the block's 著作権者 field names Centori alone. The field's form is the production page's own, inherited byte-identical, and the candidate's banner comment (L93–94) names both roles explicitly ("FR source: Cauchynambour; international/English adaptation credited upstream to Cyrielle Centori"), so no attribution information is absent from the file. The translator credit names koku4, the human production translator: ruling 3's AI credit applies to campaign translations, and a production human credit stands as-is. Neither side carries a separate Rate module; the preview credit module is rate-bearing.
- Why: P3/T1 credit swap with the ruling-3 TASL fields; attribution lines beyond the author field (here, the banner's creator/adaptation split) are part of the credit record and are checked, per the campaign's credit-repair family.
- Verify: `diff` the block against the production page's first 16 lines; read original L15–21 (the banner) against candidate L90–99.
- Disposition: standing (production-inherited form); ledger §(c3) records P3 FIXED by the credit waves for this row.

## 2. Includes and components

- What: three include-level changes. (a) The FR framework include `:fondationscp:component:modele-theme` (original L5–11, with its five `=block` parameters) has no counterpart in the candidate: the component is fondationscp's Sigma-9 framework consumer for the `ct_*` variables and has no JP equivalent; its role is replaced by inline rules (section 8). (b) The credit includes `:scp-jp:credit:start-preview` / `end-preview` are added (candidate L7/16). (c) The interwiki-style frame is added (L1–3). The usage example inside the body is an escaped exhibit naming the candidate's own fullname with the `sous-titre` parameter (L19–21). No include is duplicated.
- Why: P1 include localization and ruling 4 (a needed component is ported with the theme): where no JP component exists, the mechanism is carried inline rather than left pointing at a foreign wiki (the KB-54 ground: a foreign include without a JP equivalent does not stay as a live foreign include).
- Verify: `grep -n '\[\[include' original.txt candidate.txt` and compare the two lists.
- Disposition: standing; no include in the candidate points at fondationscp.

## 3. Delivery and code loading

- What: delivery stays inline-module on both sides. The original's main stylesheet is a `[[module CSS show="true"]]` inside the hidden `-thème` div (original L14–85), followed by an English-variant module (L89–111) and a commented-out module (L116–138). The candidate's main module occupies the same hidden-div position (candidate L89–202, gate tag localized), and a second module (L204–213) carries a JP navigation correction. There is no `local--code` delivery anywhere in the candidate: a census counting every code-block form (`[[code]]`, `[[code type="css"]]`, other typed forms) finds zero code blocks and zero `local--code` references, so the self-delivery audit (FIX-CODEADDR.md) has nothing to name here; the one historical reference (the frame's theme= parameter) was remedied in 722ceb5 and is recorded in the per-theme record, not re-litigated. The two file URLs (logo, candidate L108; body background, L177) sit on the draft host sigma10-jp-test.wdfiles.com in `local--files` form with %3A-encoded page names.
- Why: the original's delivery form is preserved (localize.md's closing rule: structure and channel order are kept); the draft-host file URLs are the draft-stage form of the theme's own attachments.
- Verify: `grep -n 'local--code' candidate.txt` (no matches); `grep -cn '\[\[code' candidate.txt` (0); read candidate L88–89 and L202–213.
- Disposition: draft-host lines are class (iii) draft form, rewritten at posting (class (ii)); they are the T1 register's two pseudo-ref lines for this file.

## 4. Fonts and assets

- What: the original imports Space Mono (original L23, Google Fonts) and references two images on fondationscp.wdfiles.com (logo, L33; body background, L58, both http). The candidate drops the Space Mono import and re-hosts the two images to its own page's attachments on the draft host (candidate L108, L177, https, %3A-encoded). The drop is adjudicated here, not passed over: a `font-family` census of all three files (original, production, candidate) returns zero declarations in each; no stack in either file names Space Mono, so nothing that renders from these files loses a face. The import served the FR framework's own header rendering on fondationscp; the candidate's mapping rules (section 8) set no font-family. Recorded as an observation with that ground. No font is named-but-unloaded or loaded-but-unnamed in the candidate (it declares no font stacks at all and inherits the environment's).
- Why: P5 asset re-hosting to the theme's own storage form; KB-16's load/use census applied in both directions.
- Verify: `grep -c 'font-family' original.txt candidate.txt` (0 and 0); `grep -n 'wdfiles' candidate.txt` (the two draft-host lines).
- Disposition: DISPOSITIONED (class (ii)/(iii) posting-time forms, ledger §(c3) P5 family); the Space Mono drop is recorded above with its census ground.

## 5. Header, sidebar, site furniture

- What: the header variables are localized: `--ct_cnt_alt-header-txt` "Fondation" → "財団" (candidate L102) and the slogan default of the per-theme record (L107). The candidate adds the mapping rules the FR framework supplied implicitly (candidate L119–163): `#header` takes the logo variable as its background, `h1 a::after` renders the alt-header text, `h2 span::before` renders the slogan variable, and link colors come from the theme's two link variables. A second module (L204–213) is a JP-side navigation correction (mobile top-bar drawer toggle separation and submenu containment, P8). The grayscale furniture rules are retained (section 8).
- Why: P9/T6 header variables; the mapping rules are what makes the variable values visible on the stock Sigma-9 DOM the JP environment uses, instead of on fondationscp's framework DOM.
- Verify: read candidate L101–163 against original L26–36 (the variable block) and L39–43 (the flicker header rule).
- Disposition: standing; the header-language item is this theme's own porting choice (the title and slogan are the theme's JP name forms), not a ruling-2 exception.

## 6. Text translation

- What: the intro line is translated (original L2 → candidate L18). The documentation and sample body (candidate L18–85) is the production page's JP text, inherited as recorded in the Provenance section: usage instructions, link specimens, heading specimens, and the tabview sample. In-CSS text (R1): the banner comment is replaced by the porter comment (section 10); the poor-foundation attribution comment is translated in place (original L56 → candidate L175, "Header background adapted upstream from the INT Poor Foundation theme"). The English-variant strings ("Foundation", candidate-absent) are treated in section 8. No reader-visible FR text remains outside quotations of the original in the credit block.
- Why: P10 body translation; R1 separates porter-visible comment text from reader-visible strings so the reviewer can judge each.
- Verify: read candidate L18–85; `grep -n 'Fondation\|soleil' candidate.txt` returns only the credit block's original-title quotation and the banner comment's source note.
- Disposition: standing (the port itself).

## 7. Links

- What: the credit source link names the FR original on fondationscp.wikidot.com, the host recorded in review/sources.tsv (no host substitution). The intro's canon link (`centre-quand-le-soleil-se-couche`, candidate L18) is the production page's JP-side form, kept. The body's remaining links are deliberate specimens (a visited-link specimen naming the theme's own fullname, L25; a 404 specimen, L27), which are exhibits, not navigation.
- Why: P11 link localization; specimen links are judged as exhibits (KB-37 family), not as dead targets.
- Verify: `grep -n 'wikidot.com' candidate.txt` (the one credit link); read candidate L23–27 as specimens.
- Disposition: standing; no dead-target prose link stands in this file.

## 8. Structure

- What: five structural changes beyond translation. (a) The framework include is replaced by inline mapping rules (candidate L117–163, classifier residue B5–B6): the mechanism's definitions are present, as rules consuming the same `ct_*` variables, so this is a mechanism relocation, not a dropped mechanism. (b) The English-variant module (original L87–112, gated `[[iftags +sun-down]]`) is dropped: it is the EN wiki's adaptation block, gated on a tag the JP environment does not use, and its one variable override is superseded by the candidate's own header values. (c) The commented-out module (original L115–139) is dropped: it is inert in the original (inside `[!-- --]`), an EN slogan experiment the FR author never activated. (d) The sample body is added (candidate L18–85), inherited from production; inside it, the footnoteblock stands in escaped exhibit form (`@@[[footnoteblock]]@@`, L85) where production carries it live: the theme page's own footnote (L29) is specimen text, and the escaped form is the population's exhibit form for the block (KB-59 family); recorded as an observation. (e) The two grayscale rule blocks (original L62–65 and L68–71) are merged into one selector list (candidate L181–188, residue B12), and the flicker keyframes are retained with the original's invalid `//text-shadow: none;` line removed (original L47; residue B7–B9). The classifier's CSS-BODY heuristic blocks B17–B18 are the differ's alignment of (b) and (c) against the candidate's tail; their substance is the two drops above.
- Why: the localize.md closing rule (preserve structure; deviations need a name): each deviation is named here with its ground. R3 governs (d): the sample body is a replacement exhibit set with a stated provenance (production), not a silent deletion.
- Verify: `grep -n 'sun-down' candidate.txt` (no matches); read original L114–139 against the candidate's tail (L202–215).
- Disposition: standing (each change grounded above); no checker error arises from any of them.

## 9. Formatting only

- What: minor. The retained CSS is re-indented to a uniform two-space style (the flicker keyframes, residue B7–B9) and colon spacing is normalized in retained declarations (e.g. original L74 `color : black;` → candidate L191 `color: black;`, residue B13–B15). The classifier counts 0 re-indentation blocks pairing after whitespace normalization at block level; the changes above are inside otherwise-changed blocks. A brace-depth scan of both files' CSS regions (comments and strings stripped) ends at depth 0 in every region with no negative excursion: no displaced-brace shape is present.
- Why: formatting churn is disclosed as its own class so it is never mistaken for semantic change (R7).
- Verify: diff.md's single hunk, read with the section-8 grounds; the depth scan is re-runnable from the two files in this package.
- Disposition: none required.

## 10. Porter annotations

- What: four annotations, all load-bearing. (a) The banner comment (candidate L90–99) replacing the FR banner: it records the FR source and its authors, the KO port derivation of the compatibility structure, the SCP-JP hub's documentation of the `sous-titre` parameter, and (as rewritten by FIX5) the fixed-default rationale. (b) The mapping-rules comment (L117–118) explaining why the `ct_*` variables are mapped inline. (c) The inline KB-06 comment on the slogan line itself (L107). (d) The navigation module's comment (L205) naming it an SCP-JP correction. The classifier's ANNOTATION label did not fire as a primary on any block; the annotations ride inside B3/B4, which is why this section is written from a direct read rather than from the skeleton.
- Why: R2 (porter annotations are part of the change record and must never be mistaken for original content).
- Verify: read candidate L90–99, L117–118, L205.
- Disposition: standing.

## 11. Dispositions and exceptions

- What: the standing dispositions for this theme, each argued in its own section: (1) the two draft-host file URLs, class (iii) draft form (section 3); (2) the render-row cross-cutting items (WebKit CC "S" glyph, KB-36 family; the 768px notice/sidebar overlap and 884px overflow; notice/code clip), dispositioned by class in ledger §(c2); (3) the sample credit-modal, preview form (ruling 5; KB-32). The one class (i) defect this theme carried (item 5) was fixed, not dispositioned (per-theme record). No item is left as an unexplained exception.
- Why: a disposition is a decision with grounds, not an omission; this section exists so the full set can be audited in one place.
- Verify: each item names its deciding check in its own section; the ledger rows are cited in the Status table.
- Disposition: DISPOSITIONED (all items above). Patterns cited in this package are patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa (KB-06, KB-32, KB-36, KB-54, KB-59).

## 12. Verification

- What: (a) T1 baseline for this file: exit 1, 2 errors / 3 warnings / 1 info (the 2 errors are the pseudo-ref draft-host lines of section 3), recorded in the stamp; (b) T2/T3 produced dispositions only, apart from the item-5 defect the render lane itself found and FIX5 closed; (c) T4 records 0 display-affecting findings for this row; (d) this package is self-verifying: `python3 review/build_review.py --check` regenerates diff.md from the two byte-faithful copies and compares, and the stamp's STALE state is explained by the one post-verdict line in the per-theme record. Counts in this README are the generator's (difflib, autojunk off): +178/−99.
- Why: verification claims must name the cheapest deciding check and its result, not a general assurance.
- Verify: re-run `python3 review/build_review.py --check` in this repo; `grep -F '{$sous-titre}' candidate.txt` (no matches) for the item-5 closure.
- Disposition: PASS (go-sign re-run, supplement).

## Appendix — residue blocks and unanchored mass

- R1 — B5 (orig L38 → cand L117–121) and R2 — B6 (orig L39–42 → cand L123–162): the inline `ct_*` mapping rules. Assigned to sections 3 and 8(a).
- R3 — B7, R4 — B8, R5 — B9 (orig L46–53 → cand L166–172): the flicker keyframes, re-indented, with the invalid `//` comment line dropped. Assigned to sections 8(e) and 9.
- R6 — B10 (orig L56 → cand L175): the poor-foundation attribution comment, translated. Assigned to section 6.
- R7 — B12 (orig L62–68 → cand L181–185): the grayscale merge. Assigned to section 8(e).
- R8 — B13, R9 — B14, R10 — B15 (orig L74/L78/L82 → cand L191/L195/L199): colon-spacing normalization in three retained rules. Assigned to section 9.
- Heuristic B17 (orig L93–109 → cand L210–211) and B18 (orig L112–139 → cand L214): the differ's alignment of the two dropped EN-side modules against the candidate's tail. Assigned to section 8(b)/(c).
- Unanchored translation mass (TRANS-UNANCHORED spans in B2, B3, B4): the production-inherited body, the banner-comment replacement, and the `:root` rewrite. Resolved by shape: sections 6, 10, and 5 respectively, with no content class of their own.

## Per-theme record


### Post-package repairs (REFRESH3-D)

Recopy was a verified no-op: `candidate.txt` is byte-identical to the current canonical `pages/theme:quand-le-soleil-se-couche.txt`. No repair lands after this package's candidate build, so the record below is the slice's sub-shape and remedy, confirmed present in the built bytes.

- **FIX-FRAMEADDR, sub-shape (B) — Introduced** (report `R/review-scout/FIX-FRAMEADDR.md` §2; landing `722ceb5c949172bb5185d51ef56ce4119ee4fa91`, 2026-11-17): the original carries no interwiki-style frame and no `theme=` self-address in that role; the porting wave introduced the frame with `theme=` naming its own draft-host `local--code/theme%3Aquand-le-soleil-se-couche/1`, a fragment the page does not carry (delivery is the inline `[[module CSS]]`). Remedy: the single `| theme=...` line was deleted; the frame include and its `priority=1` line are kept. Current candidate frame at L1.
- The (B) remedy and the line-number shift of the slogan are already recorded in the per-theme record; this subsection names the sub-shape for the slice.

Stamp treatment follows the jiha-jp / alexylva-university-jp precedents: the regenerated verdict stamp reads STALE, no re-judgement is fabricated, and the frozen GOSIGN2 ledger remains the verdict record.

## Change set outside the two diffed files

The diff covers two files; the port's record is slightly larger. (1) `pages/theme-decoration-sample-quand-le-soleil-se-couche.txt` — the decoration sample page used by the render checks. (2) `pages-existing/existing:theme-quand-le-soleil-se-couche.txt` — the production page, not a port artifact but the mediation source declared in the Provenance section; a reviewer judging the candidate against production will find the slogan default is the one place the candidate is *ahead* of production (production still carries `"{$sous-titre}"`). No fragment or companion files belong to this theme.

## Multi-wave provenance

The candidate's current state is the product of successive waves: the canonical import (d727e92) brought the check-wiki page in; the live-pair reconciliation (ffad285) aligned it with the production pair state; FIX3-B (6ae6516) applied the LOCALIZE-B row fixes; FIX5-STRUCTB (435a6bb) set the slogan default (item 5); and the frame self-address remedies (722ceb5) dropped the dead frame parameter. Citations, in place of a changelog: GOSIGN2-LEDGER.md §(c3) (localize row), §(c2) (render row), §(e) item 5; GOSIGN2-LEDGER-SUPPLEMENT.md row 5 and §5 spot-check 4; REPORT-GOSIGN2-FIX5-STRUCTB.md §5; FIX-FRAMEADDR.md (sub-shape (B)). The go-sign re-run over that record is what the Status block certifies.

## License and attribution

- **Title:** Thème de Quand le Soleil se Couche
- **Author:** Cyrielle Centori
- **Source:** https://fondationscp.wikidot.com/theme:quand-le-soleil-se-couche — revision 13 (revision date 2025-08-12 09:09:31)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: koku4 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
