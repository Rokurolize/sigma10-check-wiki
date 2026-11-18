# theme:blankstyle-jp — review package

An English theme by Placeholder McD and HarryBlank (March 2021). The JP candidate is a production-adoption row (kind K6): the SCP-JP production page already carries the theme in Japanese, the staff migration for it is recorded as a three-hunk delta (pages/phase17-diff-blankstyle-jp.txt), and the candidate reorganizes the production stylesheet into a single head module so the theme can be applied standalone, as its own closing prose declares. The theme carried one blocking item, ledger item 1 [E] (credit-modal text contrast 1.07), re-judged DISPOSITIONED by FIX5-CONTRA; the disposition is re-derived from this package's bytes in the per-theme record below and confirmed on every leg. Three content drops that neither the original nor the production page makes, and that no record dispositions, are flagged in section 8: the documentation body, the bundled-component delivery zone, and the tag-gated S&C Plastics variant module.

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:blankstyle-jp — origin EN, population #6 [GOSIGN2-LEDGER (b) row 6]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now d74bc016bd058deeb41fb094d0e0cc4fc04cfd6d2e53ffadd9caf226023e2475); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): PASS — baseline 2026-11-16: exit 0, 0 errors / 1 warn / 1 info (no error codes) [T1-ROWS row 6; GOSIGN2-LEDGER (b) row 6]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — credit-modal contrast-credit 1.07 (near-white × unreadable), sample chromium-1366 shows Wikidot 503 (one width unjudgeable), ≡ toggle overlaps body at 320, mobile overflow, sample credit-modal. [RENDER-ROWS-1 (RENDER-A row 6)]
- Engine coverage: full matrix as run by the lane, with one width unjudgeable (sample chromium-1366, transient Wikidot 503; ledger (a) caveat 3) [RENDER-ROWS-1 row; GOSIGN2-LEDGER (a)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16; ROWS-1 phrases the line bare and takes the disposition from the part header) [RENDER-ROWS-1 (RENDER-A row 6)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 7, source LOCALIZE-A]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 7]
- FIX5 re-judgement: item 1 (class E) DISPOSITIONED — FIX5-CONTRA (no edit, no commit): charged colour value absent from the candidate file; candidate is an existing-page diff touching no colour, credit or rate rule; value traced to the shared preview credit module (KB-32 class) [GOSIGN2-LEDGER-SUPPLEMENT (a) item 1]
- Computed against: canonical commit f24b7d0e86e573ee5b9403589d62db5d972af009; candidate file pages/theme:blankstyle-jp.txt sha256:d74bc016bd058deeb41fb094d0e0cc4fc04cfd6d2e53ffadd9caf226023e2475; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

- Package: review/blankstyle-jp. Candidate: theme:blankstyle-jp. Original: theme:blankstyle on scp-wiki (EN), reference revision 119 (the re-translation revision; the first-translation reference was rev 101; rev 119 created 2026-03-26).
- original.txt: byte copy of the mirror-store file orig-blankstyle-rev119.txt (source FETCH 2026-11-17), SHA-256 c53c5675acd9bc1b58cf892a3f150b5465a1cbd0c486e4118cb231b7272cc1a2, 16,600 bytes, 702 lines plus a final unterminated line (diff.md counts 703). The hash equals the sources.tsv row's mirror_sha256.
- candidate.txt: byte copy of pages/theme:blankstyle-jp.txt, SHA-256 cad8a8250396fa900d6a03137c96ab643d9c64f5b6f0aa92749f72ea46681aaa, 15,656 bytes, 687 lines. The file is unchanged since the verdict era (the last commit touching it is 1869877, FIX-CREDIT-D), so the verdict stamp as built read PASS, not STALE, and FIX5-CONTRA's final-state record carries the same candidate hash; the stamp has since been regenerated against the post-build FIX-RDISP3 landing f24b7d0 and now reads STALE, with the record verdict standing.
- Kind K6 (production counterpart): the production page stands in this repo at pages-existing/existing:theme-blankstyle.txt (821 lines); the migration delta is pages/phase17-diff-blankstyle-jp.txt (44 lines, three hunks, read in full for this package). sources.tsv records the production drift status as 一致 (matches), re-measured at f7e6cd103.
- Comparison basis: this package's diff runs EN original → candidate, but the candidate descends from the production page, not directly from the EN text. The classifier's topology pass measures the descent (r4_signal: candidate↔production similarity 0.953 against candidate↔original 0.768). Where the two comparisons diverge, the sections below judge the candidate against the production page and say so.

## Class summary

28 classifier blocks: 17 specific, 8 heuristic, 3 residue (appendix). Tier 1 diff: +188 / −201 lines in 14 hunks, 0 of the added lines are review-stage comments. Label counts: CSS-BODY 8, WS-ONLY 7, IFTAGS 4, ASSET-REHOST 3, HEADERVAR 3, JPFONT-STACK 2, FONT-IMPORT 1, JPFONT-LOAD 1, EXHIBIT-RESTRUCTURE 1, INFO-DEL 1, T7-CREDIT-CSS 1, CREDIT-PREVIEW 1, TASL-FIELDS 1, TRANS-UNANCHORED 1. The dominant mass is the channel reorganization (the original's stylesheet sits in a collapsible-wrapped module; the candidate's in one head module) together with the production page's text forms, which the heuristic CSS-BODY blocks record and sections 5 and 9 resolve.

## 1. Credit and attribution

- What: the candidate's credit block (candidate L662–673, inside [[iftags +テーマ]]) carries the ruling-3 fields at L663–672: タイトル BLANKSTYLE CSS（SCP-JP）; 翻訳責任者 iti119; 翻訳年 2022; the adaptation line (iti119 による既存の翻訳を基に改変したものです); 原題 BLANKSTYLE CSS; 著作権者 Placeholder McD、HarryBlank; 作成年 2021; 初訳時参照リビジョン 101; 改訳時参照リビジョン 119; 元記事リンク https://scp-wiki.wikidot.com/theme:blankstyle. The 著作権者 field matches the original's info-block By line exactly (original L30: Placeholder McD, HarryBlank). The co-producers the original thanks (stormbreath, EstrellaYoshte, Croquembouche; original L32) are named in the candidate's closing クレジット line (candidate L681), which also restates both revision numbers (L682–683); the 出典 line (L686) names the SCP-JP production page under CC BY-SA 3.0. The original's info:start/end block (original L26–35) is removed (INFO-DEL, block B2); its content is carried by the credit block and the closing prose. The source link's host is scp-wiki.wikidot.com, the host sources.tsv records for the original; no host substitution.
- Why: ruling 3 (the TASL record; under its human-translation branch an existing human translation keeps its translator's name with an adaptation line, rather than being re-credited to the campaign) and KB-63 (every name the original's credit apparatus carries survives somewhere in the candidate's).
- Verify: read candidate L661–687 against original L9–35.
- Disposition: ledger register (c3): P3 credit fields FIXED (credit waves, checker-verified). The joint T4/T5 row verdict is FINDINGS; the (c3) register closes this class.

## 2. Includes and components

- What: the candidate includes only the credit pair (:scp-jp:credit:start-preview at L662, :scp-jp:credit:end-preview at L673) and the interwiki-style frame (L656–659, section 3). The original's body carries a ListPages sidebox (original L9–24) and the info block (L26–35). The original also bundles four components in its delivery zone (original L121–132): component:toggle-sidebar, a {$fade}-gated component:fade-in include, a {$acs}-gated component:acs-animation include, and component:betterfootnotes; the production page carries all four in :scp-jp: form (production L121–133). The candidate carries none of them. Flagged in section 8.
- Why: ruling 4 and pattern P3 (a component a theme's own delivery bundles is part of the port, not an optional extra).
- Verify: `grep -n '\[\[include' ` on original.txt, candidate.txt, and pages-existing/existing:theme-blankstyle.txt.
- Disposition: no ledger item charges this candidate's include set; the absence is this package's flag (section 8), recorded here so the include census is complete.

## 3. Delivery and code loading

- What: the candidate delivers its whole stylesheet as one head [[module CSS]] (candidate L1–654) opening with the two Google Fonts imports (section 4). It has no [[code]] block and no local--code self-address, so the self-delivery census has nothing to misname. The interwiki-style frame (candidate L656–659) stands at priority=1 with a css= parameter carrying one rule (#interwiki .side-block, font-family 'Noto Sans JP'); the border rule the production page's frame carried inside its css= parameter (production L781) stands in the candidate's stylesheet tail instead (candidate L648–653, with the footnotes-footer rule the original carried in its head module). The original delivers through a head module (the footnotes-footer rule, original L3–7), a collapsible-wrapped [[module CSS show="true"]] (original L136–684), and the variant module (original L686–697). Brace-depth scan: both files end at depth 0 and never go negative.
- Why: patterns P4/P6 and KB-07: delivery must resolve inside the JP environment, and a candidate whose code sits in its head module takes a single priority-1 frame for the interwiki layer, the production page's own frame shape.
- Verify: `grep -n 'module CSS\|module css\|\[/module\]\|local--code' ` on both files.
- Disposition: ledger register (c3): P6 FIXED (frame waves, checker-verified).

## 4. Fonts and assets

- What, fonts: the original imports Montserrat (italic 800 / 800) from fonts.bunny.net inside its stylesheet (original L146). The production page already serves the same face from Google Fonts, and the candidate follows production (candidate L2) and adds a Noto Sans JP load (wght 400;700, candidate L3). The two Montserrat stacks gain 'Noto Sans JP' (candidate L39 and L114; blocks B6, B11, JPFONT-STACK). No stack names a face nothing loads: both named faces are imported at the head, and the remaining stack names are the original's own fallbacks.
- What, assets: the three ASSET-REHOST blocks (B12, B22, B24; candidate L132, L524, L534) are the theme's storage URLs in colon-encoded file%3A form, the production page's forms. The header-variable defaults are unchanged (blocks B7, B8): the --header-title content 'R\0026 C SITE-43' and --header-subtitle 'SUBVERTING COMMON PRACTICE' are the theme's fictional-site identity strings, identical in the original and in the production page.
- Why: pattern P5 (font delivery from exception-listed hosts; bunny.net is not one, Google Fonts is), pattern P7 (JP stacks name a loaded JP face), and ruling 2 (identity strings sit outside migration correctness).
- Verify: `grep -n '@import\|font-family' ` on both files and the production page.
- Disposition: ledger register (c3): P7 FIXED (font wave). The bunny.net → Google Fonts move predates the candidate; it is the production page's own form.

## 5. Header, sidebar, site furniture

- What: the candidate's sidebar rules are the production page's restructured forms. The original's unprefixed #side-bar .side-block.media and .side-block.resources background rules (original L341–345) do not appear; production replaced that mechanism with [style="background-color:…"] attribute-selector rules, and the candidate carries production's set (candidate L620–624), including the #F5D8E0 override that was the .resources rule's value. The fancyborder and fancyhr rules gain production's #page-content prefix (blocks B21, B23; candidate L519, L531). Selector census: the candidate's selector set covers the production main module's set in full (nothing dropped against production; the one candidate-only selector, .footnotes-footer, is production's head-module rule), and against the EN original the candidate lacks only forms production also lacks. That is production drift the candidate inherits, not a candidate drop; the distinction is what section 8's flags are measured against, since they hold against both files.
- Why: the K6 ground: where the candidate follows the production page's measured forms, the production page is the reference. The Phase 22 record (d2a9dc0) adjudicated the reference-revision drifts, and its one candidate-side gap, the missing 1290px #header h2::before rule, was repaired in d3f9af4; the rule stands in the candidate's stylesheet (it is the phase17-diff's third hunk).
- Verify: the selector census in section 12; read pages/phase17-diff-blankstyle-jp.txt (44 lines, three hunks).
- Disposition: production drift status 一致 (matches) in sources.tsv, re-measured at f7e6cd103.

## 6. Text translation

- What: the candidate's prose is the production page's Japanese text. The closing block (candidate L675–687) states the port's provenance and usage in Japanese; against the EN original this registers as TRANS-UNANCHORED mass inside block B27, but it is not a fresh translation: it is the production text carried over, which is the K6 form. The original's documentation-body text is absent together with its body (section 8 flag).
- Why: T5 judges translation text; for a production-adoption row the text under judgement is the production page's existing translation (translator iti119, credited in section 1), and the campaign's part is the re-translation reference revision (119) recorded in the credit block.
- Verify: compare candidate L675–687 with the production page's closing prose.
- Disposition: the joint T4/T5 row verdict is FINDINGS; register (c3) closes P3/P6/P7 FIXED, and no T5 item for this theme stands in register (e).

## 7. Links

- What: the credit source link names https://scp-wiki.wikidot.com/theme:blankstyle, the original's recorded URL in sources.tsv; the host is verified, with no substitution. The closing 出典 line names the SCP-JP production page the candidate descends from. No other external links stand in the candidate; the original's documentation-body links are absent with the body (section 8).
- Why: the credit-link host rule: a candidate link naming a different host than the original's recorded host is a defect; none here.
- Verify: `grep -n 'http' ` on candidate.txt.
- Disposition: none charged.

## 8. Structure

- What (flag): three content regions present in BOTH the original and the production page are absent from the candidate, and no record dispositions any of the three.
  1. The documentation body (original L36–118, inside the collapsible: introduction, usage, the ACS colour-table specimens, the tableb specimens; with the ListPages sidebox at original L9–24). The specimens' CSS survives in the candidate (the .table1 rules at candidate L449–450, .tableb at L479–493) while the markup that uses it is gone.
  2. The bundled-component delivery zone (original L121–132; production L121–133): the hidden holder div, component:toggle-sidebar, the {$fade}-gated component:fade-in include, the {$acs}-gated component:acs-animation include, and component:betterfootnotes, the production page carrying all four in :scp-jp: form. The theme's own documentation states these components are included with the theme.
  3. The tag-gated S&C Plastics variant module (original L686–698, [[iftags +s&c-plastics]]; production L804–816, [[iftags +s&cプラスチック]]): a :root module setting --header-title "S\0026 C PLASTICS" and its subtitle. `grep -n 'PLASTICS\|s&c' ` on the candidate: zero lines.
  Population contrast, measured for this package: of the 25 K6 production-adoption rows, 23 candidates keep their production pages' body shape (candidate line counts at or above the production page's, collapsible counts equal); the outliers are this theme (687 against 821 lines, collapsibles 0 against 1) and scp-human-resources (154 against 305, a separately recorded thin-layer mechanism). The phase-17 migration delta touches none of the three regions, so the production page keeps all three after migration; the drops are specific to this candidate file.
  Counterweight, recorded for the adjudicator: the candidate's closing prose declares its purpose as making the production theme applicable standalone, without depending on an external site's theme page; on that reading the candidate is a CSS-delivery artifact and the production page remains the full record. The drops are flagged because the population form is otherwise uniform and no record states that reading as a disposition.
- Why: the content-presence rule (a silent drop of a documentation body, a bundled component set, or a second CSS module is a flag with line ranges on both sides, never a narrated supplement) and ruling 4.
- Verify: the greps in section 12; the population contrast is reproducible from pages/ and pages-existing/ line and collapsible counts.
- Disposition: flagged for coordinator adjudication (restore the three regions from the production page, or record the delivery-only form as this row's disposition). The candidate is packaged as it stands.

## 9. Formatting only

- What: the WS-ONLY blocks (B5, B10, B14, B15, B20) and the spacing and wrap forms inside the CSS-BODY heuristic blocks (B9, !important spacing; B13, a gradient re-wrapped to one line; B19, height:0 → height: 0) are the production page's text forms for identical declarations.
- Why: formatting class; the values are unchanged, only their written form follows production.
- Verify: compare the named lines against the production page.
- Disposition: no verdict attaches.

## 10. Porter annotations

- What: the candidate's stylesheet opens with the production banner comment (candidate L5–13), whose lines include "Edited by iti119 for SCP-JP" (the block B3 insertion against the EN original). No campaign porter comment stands in the file, and no annotation states anything the bytes refute. The closing prose (L675–687) is the file's provenance statement and is counted as prose in section 6.
- Why: annotations are evidence about intent; a false one is a flag. None here.
- Verify: read candidate L1–16.
- Disposition: none.

## 11. Dispositions and exceptions

- Ledger item 1 [E], the theme's only blocking item: DISPOSITIONED by FIX5-CONTRA (no edit, no commit). Re-derived from the package bytes in the per-theme record below; confirmed on every leg.
- The render row's remaining lines were carried into register (e) as one bundle with item 1 and closed with it. Their individual grounds: the sample chromium-1366 Wikidot 503 is a transient server response (KB-44; the ledger's coverage caveat (3) names this theme's capture explicitly); the sample credit-modal line is the preview-form property (credit:start-preview has no modal mechanism; ruling 5; the stamp's credit-modal line above); the ≡ toggle overlap at 320 and the mobile overflow stand in the row with no separate wave edit and no separate KB attribution, and no candidate-side cause is identifiable from the bytes: the candidate's layout CSS is the production page's own, and the three-hunk migration delta touches no layout, toggle, or overflow surface. The per-theme record states this exactly.
- T4 classes: P3, P6, P7 FIXED in register (c3), checker-verified. T1: this theme's unencoded-colon error was among the 15 FIX-MECH repaired (register (c1)); the T1 baseline at determination is 0 errors (the stamp above).
- K6 shape: parts 1–3 standard; the production page is the third source, accounted in section 0, and the phase17-diff file is named there as the K6 manifest requires. The sources.tsv drift column records production against the reference revision (一致); it does not speak to section 8's candidate-side flags, which are this package's own finding.

## 12. Verification

- What a reader can re-run from this repo alone: `python3 review/build_review.py --check` (diff.md and the stamp above are current); `sha256sum` on original.txt and candidate.txt against section 0; the colour census of the candidate's rate-widget region (candidate L202–277) and the absence grep for the charged value in section 11's record; the selector census (top-level selectors of the candidate's module against the production page's modules and the original's); the brace-depth scan (comments and strings stripped), which ends at depth 0 on both files and never goes negative; and a read of pages/phase17-diff-blankstyle-jp.txt.
- Why: the package's claims are only worth what a reader can re-derive; every load-bearing claim above names its check.
- Disposition: verification route stands; the T1 baseline counts are the stamp's, and the FIX5 lane's own checker run is recorded in the per-theme record.

## Per-theme record: ledger item 1 [E] re-derived

The charge (GOSIGN2-LEDGER (e) item 1): credit block text contrast 1.07 (near-white on near-white), machine-measured and recorded in the render row; a KB-28 confirmed instance. The supplement's re-judgement (GOSIGN2-LEDGER-SUPPLEMENT item 1): DISPOSITIONED, FIX5-CONTRA, on three legs: the charged colour value is absent from the candidate file; the candidate is an existing-page diff touching no colour, credit, or rate rule; and the value traces to the shared preview credit module (KB-32 class).

Re-derivation from the bytes, measured for this package:

1. The charged value is rgb(255,246,240), #FFF6F0 (the credit modal's clear-vote × glyph; RENDER-A row 6 record). A regex grep for every written form (fff6f0, 255,246,240, 255, 246, 240) returns zero hits in candidate.txt, zero in original.txt, and zero in the production page. The value is absent from all three files.
2. The candidate's rate-widget region (candidate L202–277) uses exactly two colours, #333333 and #ffffff: .fa-info color #333333 (L213–215), the widget background #ffffff (L264), .cancel a color #333333 (L269–271), its hover background #333333 with color #ffffff (L272–274). The EN original carries the same values on the same surfaces (.fa-info at original L359, its hover background #333333 at L364, .cancel a color #333333 at L415, hover background #333333 and color #ffffff at L418–420), and so does the production page (.fa-info L346, .cancel a L402, hover L405, with the second creditRate pair at production L675/L684 matching candidate L546/L555). The candidate's credit and rate colours equal both references on every charged surface.
3. The migration delta (pages/phase17-diff-blankstyle-jp.txt, 44 lines, three hunks) adds the credit block's 改訳時参照リビジョン line, changes #page-content font-size 0.8rem → .9rem, and adds the 1290px #header h2::before rule. No colour value and no credit or rate CSS rule is touched; the one credit hunk is a credit field, not a rule.
4. Checker: FIX5-CONTRA's run reported 0 errors / 0 warns / 1 info before and after (the info is !important density); the stamp's T1 baseline (a different run) reads 0 errors / 1 warn / 1 info. The candidate file is byte-identical to the file FIX5 measured (SHA-256 cad8a825…, section 0).
5. The value's source: FIX5-CONTRA §6 records theme:sodium showing the identical rgb(255,246,240) × glyph with the same absence from its candidate; the value belongs to the shared preview credit module every candidate includes (this candidate at L662), the KB-32 class, uniform across themes and not a property of this file.

Second-reviewer walk. Is the ground stated in terms a reader who did none of the work can check? Legs 1 and 2 and the EN-original half of leg 3 verify from this package's own two files alone. The production half of leg 3 needs pages-existing/existing:theme-blankstyle.txt, and the delta needs pages/phase17-diff-blankstyle-jp.txt; both are in this repo, so the whole ground is re-derivable without the campaign record. The walk confirms the ground as stated for the contrast charge. For the bundle's toggle and overflow lines (section 11) the record's ground is thinner: it rests on the delta's silence over layout surfaces, which the same two in-repo files let a reader confirm, but no measurement re-derives those two observations away; they are recorded as closed with the bundle on that basis, not as independently dispositioned. Walk outcome: the disposition stands, with the thinness on the record.

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:blankstyle-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP3, landing `f24b7d0` (report `R/review-scout/FIX-RDISP3.md`).** Three candidate restorations (+129/−0, pure insertions), all postdating this package's build at `1869877`. All three restore regions come from the production page `pages-existing/existing:theme-blankstyle.txt`, the translation of record for this K6 production-counterpart row (translator iti119), cross-checked against the original's ranges.
- **F1a — documentation body restored.** The ListPages sidebox (production L9–24) and the body prose (production L37–118) were restored inside the gate, before the candidate's untouched credit block and closing prose. One sanctioned adaptation: the usage exhibit `@@[[include :scp-jp:theme:blankstyle]]@@` → `@@[[include theme:blankstyle-jp]]@@`, the candidate's own established form. The original's info block was not part of the flagged body and was not restored (its content is carried by the credit block and closing prose, per §1).
- **F1b — bundled-component delivery zone restored.** Production L121–132 verbatim after the gate closes: the hidden holder div, `component:toggle-sidebar`, the `{$fade}`-gated `component:fade-in speed=3`, the `{$acs}`-gated `component:acs-animation`, and `component:betterfootnotes`, all already in the population's `:scp-jp:` form (no `-jp` counterpart exists for any of the four).
- **F1c — S&C Plastics variant module restored.** Production L804–816 (the `[[iftags +s&cプラスチック]]` CSS module with the S&C header variables and the `div#extra-div-1` Big87.png rule), inside the holder div. Its asset URL took the candidate's established colon-encoded `file%3A5722815-48-k39z` form (the production's unencoded colon had introduced an `unencoded-colon` error); the file named is unchanged.
Checker per the report: plain error 0 / warn 0 / info 1 unchanged; links error 0 / warn 0 / info 1 → 0 / 2 / 1, the two warns being production-inherited `link-label` notes on the restored body (Fade-In, ACSコンポーネントバー); class (i) errors 0 before and after; brace depth ends at 0.

## Appendix — residue blocks

- B3 (insertion at candidate L12–13): a blank line and the banner line "Edited by iti119 for SCP-JP", carried from the production page's banner comment. Provenance text, adjudicated; no action.
- B18 (original L333–345, no candidate counterpart): the #side-bar .side-block base rule and the .media / .resources background rules. The candidate carries production's restructured forms for the same surfaces (the base rule in production's text, the backgrounds as attribute-selector overrides, section 5), so this is the production mechanism change, not a rule loss. Adjudicated against the production page.
- B28 (original L699–703, no candidate counterpart): the original's collapsible close and final [[/div]] of its wrapper structure. The candidate has no collapsible wrapper (section 8's form difference), so the tail tokens have no counterpart. Structural, adjudicated.
- The heuristic CSS-BODY blocks resolve as: B4, the bunny.net import line's position (the import itself is section 4); B9, B13, B19, production text forms (section 9); B16 and B17, the #side-bar .side-block rule region restated in production's form (its border declaration gains !important); B21 and B23, production's #page-content prefixes (section 5).

## License and attribution

- **Title:** BLANKSTYLE CSS
- **Author:** Placeholder McD、HarryBlank
- **Source:** https://scp-wiki.wikidot.com/theme:blankstyle — revision 119 (revision date 2026-03-26 17:28:07)
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: iti119 — a human translator credited by the live JP page and retained as the package records it (campaign-rule exception); where the campaign translated, the translator is AI.
