# Review package — theme:winddew-in-hand-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:winddew-in-hand-jp — origin CN, population #245 [GOSIGN2-LEDGER (b) row 245]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 3c42a8533879b208b03f3f4a340a5b7490bb96c72823faeaa757db22ab1354b3); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 2 warns / 1 info (hotlink×4, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 210; GOSIGN2-LEDGER (b) row 245]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + candidate hosts scpsandboxcn.wdfiles.com, scpsandboxcn.wikidot.com, scptestwiki.wdfiles.com; sample credit-modal (preview-form) + page-overflow 884px@768; T3 re-run, no new screenshot-grounded visual finding; chromium-only coverage (no WebKit verdict). [RENDER-ROWS-G (CN17)]
- Engine coverage: chromium-only, both pages (no WebKit verdict) [RENDER-ROWS-G row, findings cell]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-G (CN17)]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 244, source LOCALIZE-S2-E]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 244]
- FIX5 re-judgement: item 98 (class H) FIXED — FIX5-TEXTA §7, commit 6f6b349: prose links repointed to theme:basalt-jp and theme:admo-jp; usage-example includes given the -jp posting suffix [GOSIGN2-LEDGER-SUPPLEMENT (a) item 98]
- Computed against: canonical commit 3f0aa788d3a56dfcfb83c698ec2c7a4a9bb44f44; candidate file pages/theme:winddew-in-hand-jp.txt sha256:3c42a8533879b208b03f3f4a340a5b7490bb96c72823faeaa757db22ab1354b3; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:winddew-in-hand` on scp-wiki-cn (CN), revision 3 — `original.txt` in this package (458 lines / 10,769 bytes; `wc -l` reports 457, the last line is unterminated) |
| Candidate | `theme:winddew-in-hand-jp` — `candidate.txt` (450 lines / 12,691 bytes), a byte copy of `pages/theme:winddew-in-hand-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the CN Basalt-based theme carried over with the preview credit block and the head frame added in the standard JP forms, the body translation, and the delivery conversion from a live CSS module to the code-block form. Two findings qualify that summary and are flagged rather than narrated away: the base delivery the original carries is absent from the candidate (section 3, flag W1), and the original's two customization exhibits stand inside the candidate's delivered code block instead of its body (section 8, flag W2). |

Sources-note correction owed (for the coordinator's harvest; the lane does not edit `review/sources.tsv`): this theme's note claims the original was superseded upstream since the reference revision and cites the follow-up artifact `diff-winddew-in-hand-from3.txt`; the artifact itself records "rev3 → rev3 変更： なし" (no changes). The note is wrong in the ambrose shape. The correct standard form is: "Upstream latest remains rev 3; the S2 artifact records rev3 to rev3, no changes; follow-up diff artifact diff-winddew-in-hand-from3.txt in the campaign record (K5a-i)".

Status note: the verdict stamp above reads PASS, computed against canonical commit 6f6b349, the FIX5-TEXTA commit that closed this theme's blocking item; the candidate has not changed since. The per-theme record below re-derives that closure from the package's bytes and finds it partial: item 98 bundled three charges from one localize row, and the base-delivery charge is not closed in the bytes (flag W1). The stamp records the verdict as issued; this package's record is its byte-level qualification.

Summary: a CN theme built on Basalt (掌上风露), with memo-paper styling, a hidden base include, and a live CSS module. The port swaps in the preview credit, translates the body, converts delivery to the code-block form, and repoints the prose links and usage examples to the JP candidates. It carried one blocking item, 98 (class H), re-derived in the per-theme record: the link and usage-example charges are confirmed fixed; the bundled base-delivery charge is not (flag W1), and the port additionally leaks the original's two customization exhibits into the delivered stylesheet (flag W2).

## Class summary

| Label | Blocks |
|---|---|
| COLON-ENC | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| DELIVERY-MOVE | 3 |
| DRAFT-HOST | 1 |
| EXHIBIT-RESTRUCTURE | 4 |
| IFTAGS | 2 |
| SELF-DELIVERY | 1 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 2 |

Counts: 9 blocks, 6 specific, 2 heuristic, 1 residue, 0 skipped. Topology: the original's live module-css delivery becomes the candidate's code-css delivery (DELIVERY-MOVE x3); the diff is Tier 2 (+331/-339, 670 changed lines by the generator's count, 0 of them review-stage comments).

## 1. Credit and attribution

- Credit block (candidate L3-12; CREDIT-PREVIEW + TASL-FIELDS): eight fields. The original has no credit block; its attribution is the intro prose byline (original L123), and the candidate's block is the standard added JP form. 著作権者 names Jonuarl Reden, matching that byline, which also credits the 和风之旅 theme; that second credit is carried in the candidate's intro prose (candidate L14). No pointer-in-place-of-a-name defect stands, and no attribution line the original carries is dropped. The block's source link (candidate L11) names scp-wiki-cn.wikidot.com, the original's recorded host in review/sources.tsv: the host check passes.
- The credit title field 掌上风露 版式 (candidate L5) keeps the original's simplified-Chinese form. The body supplies no Japanese title form to match, and the string is the theme's name; it stands as an identity string under the ruling-2 boundary, uncharged in the ledger's (e) item. Recorded, not flagged.
- The original's bare `[[module rate]]` (lowercase in the original, at L120 inside its `[[>]]` wrapper at L119-121) is absent from the candidate. That is the correct P3 form (KB-09, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa: the preview credit module is rate-bearing, so a bare Rate beside it renders two widgets); it was never charged for this theme.
- License box: none on either side; nothing was dropped. T7 credit-module CSS: none in either file (`grep -c creditButton` = 0 / 0).
- Verify: read candidate L3-12 against original L119-127; `grep -ci 'module rate'` on both files (1 / 0; case-insensitive, because the original's module name is lowercase).

## 2. Includes and components

- Live includes in the candidate: the credit pair (L3, L12), the image-block exhibit (candidate L158), and the interwiki-style frame (candidate L447-450, section 3). The credit pair and the frame are candidate additions in the standard JP forms; the original carries neither (its credit is prose, section 1, and it has no frame). Usage examples: three `@@`-escaped include lines (candidate L18, L26, L28), all in the `-jp` posting form; they are the usage half of the FIX5 closure (per-theme record).
- The original's live includes are the hidden Basalt base include (original L2, inside the `display:none` div at L1-3) and the image-block (original L283). The base include has no counterpart in any form: flag W1, section 3.
- No include is duplicated. The COMPONENT-SWAP block is the credit apparatus swap (the original's prose byline becomes the preview-credit include pair).
- Verify: `grep -n 'include'` on both files (original: 5 lines — L2, L127, L135, L137, L283; candidate: 7 lines — L3, L12, L18, L26, L28, L158, L447).

## 3. Delivery and code loading

- Delivery conversion (DELIVERY-MOVE x3): the original's live `[[module css]]` (original L4-116) becomes the candidate's single `[[code type="css"]]` block (candidate L321-439), served by a tail `[[module css]]` import the candidate adds (candidate L444-446) and named by the `theme=` of the interwiki-style frame the candidate likewise adds (candidate L447-450), both at `local--code/theme%3Awinddew-in-hand-jp/1`. Census, counting every code-block form: exactly one code block in the candidate (the original has two, both exhibits), and `/1` names it, the stylesheet itself. Self-delivery census: MATCH form (FIX-CODEADDR); no navla-style shape.
- Region diff (original module body L5-115 against candidate code body L323-439): the delivered CSS equals the original's module CSS with exactly two line edits, candidate L326 (`--header-logo` scheme http to https) and candidate L363 (`--bg-img` path colon-encoded `collab%3A`, KB-01), plus the porter banner comment at candidate L322 and the appended exhibit tail that is flag W2 (section 8).
- **Flag W1 — the Basalt base delivery is dropped, and item 98's third charge is not closed.** The original delivers its base through a hidden include at original L1-3 (`theme:basalt` inside a `display:none` div), with five parameter pass-throughs (wide, hidetitle, centertitle, acs-itemnum, disable-acs-anim). The candidate carries no Basalt delivery in any form: no `theme:basalt-jp` include and no `@import` of basalt-jp's code fragment (the census in section 12). Its own CSS only sets `--basalt-*` override variables and memo/blockquote rules that presuppose the base. The population form exists (for example `theme:stargazer-jp` L2 imports basalt-jp's `local--code/1`). The base has been absent since the S2 integration commit 2e202fc, whose file already opens with the gate. Charge history: LOCALIZE-S2-E row CN17-4 charged it as P1; ledger item 98 bundles it ("the same row charges the dropped Basalt base reference"); the FIX5-TEXTA report (section 7 and its closing list) states the base include is "a separate P1/structural charge, not class H — left untouched"; the supplement nevertheless re-judged item 98 FIXED on the link charges alone. Flagged for the coordinator with this evidence; the package is written against the candidate as it stands.
- Gates: neither file carries include-parameter gates, so the render-time gate test has nothing to bite on; the candidate's `[[iftags +テーマ]]` wrappers stand in body text.
- Verify: `grep -n 'basalt' candidate.txt` returns only `--basalt-*` variables and the L32 prose link; compare original L1-3.

## 4. Fonts and assets

- Fonts: neither file loads a font; both inherit the base's program. The candidate's font announcement (candidate L310-312) names Basalt's stacks (Sofia Sans / Inter / JetBrains Mono, with the JP renderings 源ノ角ゴシック / 源ノ明朝). No stack in the theme's own CSS names a face beyond that inheritance. The inheritance is exactly what flag W1 breaks: with no base delivered, the announced program does not run. Recorded as part of W1's evidence, not as a separate flag.
- Assets: four hotlink URLs stand in the candidate (L158, the image-block exhibit's `spacelogo.png` on scptestwiki.wdfiles.com; L326, `wdh.png` on scpsandboxcn.wdfiles.com; L363 and L367 on scpsandboxcn.wikidot.com). They are the ledger (c2) DISPOSITIONED class (ii) set (KB-41 / KB-54 family) and the T1 baseline's four hotlink errors. Candidate L326 also carries an http to https scheme fix on the logo URL.
- Verify: `grep -n 'wdfiles\|local--files' candidate.txt`.

## 5. Header, sidebar and site furniture

- The theme's real header values stand at candidate L324-325: `--header-title` (the theme's Chinese name) and `--header-subtitle: "沐风饮露 倘徉八方"`. Both are identity strings under the ruling-2 boundary (a name and a slogan functioning as a mark), uncharged in (e), and stand. The `--memo-heading: "风露旅社提示你！"` string (candidate L400) is an R1 string-valued variable, likewise uncharged and standing.
- The placeholder pair `--header-title: "主标题"` / `--header-subtitle: "副标题"` at candidate L434-435 is not a second header setting: it is flag W2's leaked exhibit content, and in the delivered stylesheet it overrides the real values (section 8).
- Sidebar and memo rules are the carried CSS of section 3; their Basalt-dependent parts presuppose the base (flag W1).
- Verify: `grep -n -- '--header-' candidate.txt` (four hits: the real pair at L324-325, the leaked pair at L434-435).

## 6. Text translation

- The body is translated throughout (TRANS-UNANCHORED mass): headings, the intro, the usage prose, and the memo/blockquote specimens. Kept Chinese strings are enumerated with their grounds in sections 1 and 5; one CSS comment (`/*透明度*/`, candidate L375) is kept verbatim, porter-visible only.
- Verify: the translation spans in `classification.json` against both files.

## 7. Links

- Candidate L32 `[[[theme:basalt-jp|こちらの説明]]]` and candidate L42 `[[[theme:admo-jp|Admonition]]]`: the FIX5-TEXTA section 7 repoints (per-theme record). Both targets are candidates in this repository (`pages/theme:basalt-jp.txt`, `pages/theme:admo-jp.txt`), so no probe is needed to establish that they resolve at posting.
- No other prose links stand in either file; the L158 image-block `name=` is an asset reference (section 4), and the credit block is section 1.
- Verify: `grep -n '\[\[\[' candidate.txt` (two hits, L32 and L42).

## 8. Structure

- **Flag W2 — the customization exhibits leaked into the delivered code block, and their headings stand orphaned.** In the original, the two customization exhibits (the title example, original L268-272; the icon example, original L276-280) are inert `[[code type="css"]]` display blocks under their prose headings. In the candidate the headings survive bare at candidate L154 (タイトルを変更したい場合) and L156 (アイコンを変更したい場合) with no exhibits under them, and the exhibits' contents are appended verbatim at the end of the delivered code block (candidate L433-438, inside the block at L321-439 that `/1` serves). Brace depth, measured not counted: the original's module CSS ends at depth 0; the candidate's code block ends at depth 1, the unclosed open at candidate L433 (exhibit 1's `:root {`). The original exhibit itself measures depth 1; its missing close is inherited verbatim, inert in the original's display channel. In the delivered channel the consequence is live: the placeholder declarations at candidate L434-435 stand after the theme's real values (candidate L324-325) in the same stylesheet and win at equal specificity, and exhibit 2's `:root` (L436-438) nests inside the unclosed first. Charge history: LOCALIZE-S2-E row CN17-4 charged this shape as P10 (two orphaned headings plus a Chinese snippet leaked into the source); neither item 98's text nor the supplement's closure names it, so it stands unclosed. Precedent: `theme:gp-refresh-jp`'s identical shape was item 59, and FIX5-TEXTA section 1 restored its exhibits translated and closed the same brace as an original technical mistake.
- Exhibit census otherwise: the three usage examples, the image block, and the memo/blockquote specimens all stand against the original. Footnotes: two live `[[footnote]]` on each side (original L285, L314; candidate L160, L189) and `[[footnoteblock]]` on neither side, parity with the original's own form (KB-59 family), not a candidate drop.
- Verify: a brace-depth scan over original L5-115 and candidate L323-439 (0 against 1); read candidate L154-158 against original L266-280.

## 9. Formatting only

- None as a standalone class: the classifier reports no WS-ONLY blocks. The diff's bulk is the delivery conversion of section 3, which re-emits the module body as a code block.
- Verify: the label counts in `classification.json`.

## 10. Porter annotations

- One comment-form annotation: the banner `/* ===== winddew-in-hand ===== */` at candidate L322, heading the delivered code block (class R2, comment carrier). It is a label and states nothing the bytes can refute. The font announcement at candidate L310-312 is carried documentation prose, treated in section 4.
- Verify: `grep -n '=====' candidate.txt`.

## 11. Dispositions and exceptions

- T1 baseline findings: hotlink x4 and pseudo-ref x1 (the `/1` import at candidate L445), classes (ii) and (iii), DISPOSITIONED in the ledger (c2); the `!important` info (candidate L309) is recorded verbatim.
- Render row (RENDER-ROWS-2): page-overflow at 320 and 375 (KB-33 / KB-34 family), the sample credit-modal errors (preview-form property; `credit:start-preview` has no modal mechanism), and the runtime-hotlink site-theme chain (KB-40, environment layer), DISPOSITIONED.
- The kept Chinese identity strings (sections 1, 5) stand under ruling 2, recorded, not exceptions.
- Flags W1 and W2 are class (i) items standing open for the coordinator. This package does not disposition them.

## 12. Verification

- T1 run by this lane on the current candidate (`check_source.py --kind theme`): error 5 / warn 0 / info 1 — the four hotlinks at L158, L326, L363, L367, the pseudo-ref at L445, the `!important` info at L309; no `double-rate` line. The stamp's baseline (5 errors / 2 warns / 1 info) describes the pre-FIX5 file.
- T2/T3: FINDINGS with dispositions only (ledger row (c2)). T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `c3154305b4b131491497ada3db4a86b5cba0ff53781281dc6ab35f109f56460f`); `original.txt` hash equals the sources.tsv value (`cf99b42a9e92b316feacaa26cf72dec0372c81391815d927db4dd2dfc479798b`); brace-depth scans as reported in sections 3 and 8; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 98 (ledger (a) item 98, class H): the item bundles the charges of LOCALIZE-S2-E row CN17-4 against this theme: (i) a P9 prose link (original L141) naming `theme:basalt`; (ii) P9/P11 usage examples and prose references in plain forms; (iii) in the ledger's own words, "the same row charges the dropped Basalt base reference". The row also carried a P10 exhibit charge (section 8) that the ledger item does not name.
- What the fix was supposed to change: FIX5-TEXTA section 7 (commit 6f6b349) repointed the prose links and usage examples to the `-jp` forms. For the base charge, the TEXTA report itself (section 7, repeated in its closing list) states: "The dropped hidden Basalt base include is a separate P1/structural charge, not class H — left untouched."
- Supplement re-judgement: FIXED, FIX5-TEXTA, commit 6f6b349, describing the link and usage-example changes.
- Re-derived from this package's bytes: charges (i) and (ii) are confirmed. Candidate L32 names `theme:basalt-jp`, candidate L42 names `theme:admo-jp` (original L151's plain form), and the three usage examples (candidate L18, L26, L28) all carry the `-jp` posting form. Charge (iii) is not closed: no base delivery exists in the candidate (flag W1, section 3). The row's P10 exhibit charge is likewise unclosed (flag W2, section 8).
- Closure: PARTIAL. The supplement's FIXED stands for the class-H link charges it describes. The bundled base charge and the exhibit charge stand open, and the supplement's account of item 98 is incomplete against both the TEXTA report it summarizes and the bytes. This is recorded as a prose-vs-bytes discrepancy, not as a re-judgement of the theme's other verdicts.

### Post-package repairs (REFRESH3-K)

The items above describe this package as built. The repairs recorded below postdate the package; `candidate.txt` has been recopied from the current canonical `pages/theme:winddew-in-hand-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

- **FIX-RFIX20 items 1–2, landing `3f0aa788d3a56dfcfb83c698ec2c7a4a9bb44f44`** ("pages: R-fix-20 flags repaired (winddew, words-of-wisdom)", 2026-11-17, R/review-scout/FIX-RFIX20.md §§1–2; +19/−6 across three hunks):
  - **Item 1 (W1) — hidden Basalt base include restored.** The candidate had no Basalt delivery in any form. The hidden `display: none` include is restored at the original's head position (refreshed candidate L1–3), repointed under ruling 1 to the JP base candidate in the population's landed form, byte-identical to theme:gp-refresh-jp's L23 include (FIX-GP, canonical 9e0c700): `[[include theme:basalt-jp wide=a|hidetitle={$hidetitle}|centertitle={$centertitle}|acs-itemnum={$acs-itemnum}|disable-acs-anim={$disable-acs-anim}]]`, with all five pass-through parameters unchanged. The include form (not @import) is required because parameters cannot ride an @import. Post-repair census: exactly one Basalt delivery in the file (L2); the only other `theme:basalt-jp` hit is the pre-existing prose link.
  - **Item 2 (W2) — exhibits restored out of the delivered block.** The six lines leaked from the two `[[code type="css"]]` exhibits into the delivered code block were removed; that block now ends at L449 with the `div.papernote` rule. The exhibits stand again under their prose headings as inert display blocks at L158–163 and L167–171, in the population's restored form (byte-identical to gp-refresh's FIX5 copies), with placeholders translated (主标题→メインタイトル, 副标题→サブタイトル, 图片url→画像URL) and exhibit 1's missing closing brace restored — an original technical mistake, closed on restore per the gp-refresh item-59 precedent. Brace-depth scan after: all three code blocks end at depth 0; `--header-title` / `--header-subtitle` are declared exactly once each in the delivered block, with the theme's real values ("风 露 旅 社" / "沐风饮露 倘徉八方"), and no later declaration overrides them. No occurrence of 主标题, 副标题 or 图片url remains anywhere.
- **Ledger item 98 and this repair.** The per-theme record above re-derives item 98 as **PARTIAL**: the FIX5-TEXTA FIXED covered only the class-H link and usage-example charges, while the bundled base-delivery charge (flag W1) and the P10 exhibit charge (flag W2) stood open. This landing repairs both open charges at byte level, so the two flags that made the closure partial are now closed in the recopied candidate. No re-judgement is fabricated here: the frozen ledger's item 98 verdict stands as issued, and this package records the byte-level repair alongside it — the same "the repair has since landed" treatment as the jiha/alexylva precedents.
The status note, multi-wave provenance ("No later wave touched this file: the verdict stamp's computed-against commit is 6f6b349 itself"), and sections 3/8's W1/W2 flags are the as-built record; the stamp now reads STALE against these repairs. Checker (FIX-RFIX20 §3): error 5 / warn 0 / info 1 → 5 / 0 / 1 on both files, finding sets identical item for item (only line numbers moved); class (i) 0 before and after.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-winddew-in-hand-jp.txt` — the render-check sample page for this theme (it includes the candidate at its L1, so flag W1's missing base is visible there as it is on any page using the theme).
2. `pages/theme-decoration-sample-winddew-in-hand.txt` — the production-side sample page.
3. The theme delivers no files of its own beyond the dispositioned hotlink assets (section 4).

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-E) produced the port from CN revision 3; the base include was already absent at the S2 integration commit 2e202fc, and row CN17-4 charged the P1 base drop, the P9 links, and the P10 exhibit leak.
- FIX5-TEXTA (commit 6f6b349) fixed the link and usage-example charges (section 7) and expressly left the base charge untouched.
- No later wave touched this file: the verdict stamp's computed-against commit is 6f6b349 itself, and the usage sweep and snippet audit had nothing to change (the examples were already in `-jp` form after TEXTA).

## Appendix — heuristic and residue adjudication

The classifier reports 2 heuristic blocks and 1 residue block. All resolve by shape:

- The residue and heuristic mass concentrates in the B5-B7 exhibit region (EXHIBIT-RESTRUCTURE primaries), where the classifier's own note reads "no translated counterpart on the added side; the writer's replaced-vs-dropped call is forced". That region is flag W2 (section 8): the exhibits were neither replaced in place nor cleanly dropped, but moved into the delivered stylesheet. Adjudicated as a defect, not a classifier artefact.
- EXHIBIT-RESTRUCTURE labels on the usage-example blocks are the include repoints inside exhibit regions, false fires (section 2).
- DELIVERY-MOVE x3 is the module-to-code conversion of section 3, checked block by block: the module's full body stands in the code block, and no module was dropped in the move (the exhibits' relocation is W2, separately flagged).
- TRANS-UNANCHORED x2 is body prose translation mass (section 6).

Two defect flags arise from this package (W1, section 3; W2, section 8), and one sources-note correction is owed (section 0).
