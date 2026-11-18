# Review package — theme:betwixt-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:betwixt-jp — origin CN, population #167 [GOSIGN2-LEDGER (b) row 167]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 7d10ca5fbcb39ada43395a088b53d1e7a41db43a4310f80ba9a133a000467af7); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 8 errors / 0 warns / 1 info (pseudo-ref×8); standing classes dispositioned in register c1 [T1-ROWS row 145; GOSIGN2-LEDGER (b) row 167]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — REAL WebKit-specific FINDING on both pages: the top-left mobile sidebar-open hamburger renders in chromium but is entirely absent in webkit at 375x812 and 320x640, leaving no visible way to open the sidebar in webkit (screenshot-confirmed; machine `sidebar-unreachable` on all four mobile combos); page-overflow 434px chromium / 438px webkit @320/375; runtime-hotlink incl. candidate-own ah-sandbox hosts, hormress.github.io, nu-scptheme.github.io (judgment-required); sample adds credit-modal (preview-form); decorative 404/ORB assets leave a flat light-blue header (deferred). [RENDER-ROWS-RERUN16 (CN2) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN2)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 1 [LOCALIZE-ROWS row 166, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 166]
- FIX5 re-judgement: item 45 (class F) DISPOSITIONED — FIX5-FUNC §1 (no edit): sidebar block candidate L446-460 byte-identical to original L442-456 (diff IDENTICAL); hover/focus reveal is the theme's own original design; engine-specific rendering of an original-identical mechanism [GOSIGN2-LEDGER-SUPPLEMENT (a) item 45]
- Computed against: canonical commit fa9e84aae02210b174c0480db82e68c1846aeef4; candidate file pages/theme:betwixt-jp.txt sha256:7d10ca5fbcb39ada43395a088b53d1e7a41db43a4310f80ba9a133a000467af7; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (R-disp-2 lane, 2026-11-17)
Candidate: review/betwixt-jp/candidate.txt (sha256 227f057c1e686eeeadf5bb11d74fddd486ba5cd764c14dd092ec4f90dcbcc6ee)
Original: theme:betwixt — scp-wiki-cn, revision 3 (sha256 a32074285fc9481e362ea4b2387eec60c805c5fdc68bf89e5352e263e45ed5a0)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (generated stamp) | Notes |
|---|---|---|
| T1 source check | FINDINGS (classified) | 8 errors / 0 warns / 1 info, all pseudo-ref; standing classes dispositioned in register (c1) |
| T2/T3 render | FINDINGS | The WebKit sidebar finding is FIX5 item 45, re-derived below; the rest dispositioned in (c2) via RERUN16 |
| T4/T5 localize/translation | FINDINGS | 1 display-affecting finding (the film title, section 6) [LOCALIZE-S2-D] |
| FIX5 item 45 [F] | DISPOSITIONED (FIX5-FUNC §1, no edit) | Re-derived on this package's bytes in the per-theme record; ground holds exactly |

The stamp reads STALE because the candidate file changed after the 435a6bb-era verdict (the stamp names canonical b5cb724 as its computed-against commit). The item-45 re-derivation in the per-theme record was performed on the current candidate bytes in this package, so it holds for the file as it stands regardless of the stamp. The T2/T3 verdict is the RERUN16 row, which supersedes the RENDER-ROWS-2 row for this theme under rule S1; the generator already applies that supersession.

## Provenance

| Side | Source | Revision | SHA-256 |
|---|---|---|---|
| Original | theme:betwixt on scp-wiki-cn (mirror store: orig-betwixt-rev3.txt) | rev 3 | a32074285fc9481e362ea4b2387eec60c805c5fdc68bf89e5352e263e45ed5a0 |
| Candidate | pages/theme:betwixt-jp.txt (canonical) | — | 227f057c1e686eeeadf5bb11d74fddd486ba5cd764c14dd092ec4f90dcbcc6ee |

The sources.tsv note for this theme claims the original was superseded upstream since the reference revision. That claim is wrong: the follow-up artifact it cites (diff-betwixt-from3.txt in the campaign record, K5a-i) records rev 3 to rev 3 with no changes, so rev 3 is both the reference revision and the upstream latest. The correct note form is recorded in the batch report for the coordinator's harvest correction; sources.tsv itself is not edited by this lane.

## Summary

A Chinese variant theme built on theme:parallel: the original imports the parallel fragment's code blocks inside a gated head module, adds its own inline rules there, and carries its main CSS as a second inline module outside the gate. The port restructures delivery around the JP base candidate: theme:parallel-jp is included at the head, the main CSS moves from the inline module into the candidate's own code block 5 delivered by URL, the credit furniture swaps to the JP preview form, and a license box is added. One dispositioned blocking item (45, the WebKit sidebar) re-derives exactly on the package bytes. Three defect flags are recorded in the per-theme record: three rules from the original's head module are absent from the whole candidate delivery chain; the meta-title specimen is dropped while its CSS survives; and the intro prose links both predecessor themes to the CN wiki although JP candidates for both exist and one of them is this file's own base include.

## Class summary

| Label | Blocks |
|---|---|
| ANNOTATION | 1 |
| COMMENT-TEXT | 2 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 4 |
| CREDIT-PROSE | 1 |
| DELIVERY-HOST | 1 |
| DELIVERY-MOVE | 7 |
| DRAFT-HOST | 8 |
| ESCAPED-INCLUDE | 1 |
| EXHIBIT-RESTRUCTURE | 1 |
| FONT-IMPORT | 2 |
| GLYPH-FORM | 2 |
| IFTAGS | 2 |
| INCLUDE-REPOINT | 5 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| LICENSE-BOX | 1 |
| LINK-REPOINT | 1 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 27 |
| TRANSLATION-ANCHORED | 31 |

Counts: 71 blocks, 50 specific, 20 heuristic, 1 residue, 0 skipped (comment text).

## 0. Header / provenance

- Route: derived from the original at the reference revision (rev 3, mirror hash above equals the sources.tsv row). The candidate's code banner (cand L276-277) and credit field 初訳時参照リビジョン (cand L21) both record rev 3 on scp-wiki-cn.
- Topology: one relocation, module-css -> code-css at body similarity 0.979 (the main stylesheet, orig L282-861 → cand L268-874). The original's four exhibit code blocks pair with the candidate's first four; the candidate's fifth code block is the moved stylesheet.

## 1. Credit and attribution

- What: the original's credit furniture is the CN credit module with no field lines (orig L37-41: credit:start / credit:more / credit:end around two text lines), plus a bare Rate at orig L34. The candidate carries the JP preview credit block (cand L14-23, B5) with the eight TASL fields, and the three variant credit exhibits in the body swap the same way (B46, B47, B48; e.g. cand L152-154), the CN credit:more line merging out under the preview form's two-part shape. The bare head Rate is removed (KB-09; the preview credit module is rate-bearing); the three exhibit Rates stay live on both sides (orig L167, L178, L189 → cand L150, L161, L172) — they are the variant rating-module exhibits' working specimens, at parity with the original.
- Fields: title 狭間のテーマ（夹缝间） (cand L15) is a Japanese form with the CN name glossed; no body form in the candidate contradicts it, and it stands. Translator of record is AI, the campaign's settled TASL form. The source link (cand L22) names the recorded host scp-wiki-cn.wikidot.com, matching sources.tsv.
- The author field (cand L19) is the pointer form 原語版ページの作成者に同じ（scp-wiki-cn の theme:betwixt）, and the license-box author parameter (cand L877) is likewise theme:betwixt の作者. Unlike the pointer-defect family, the frozen original names no author for this theme in any carrier: a full-text search of original.txt finds an author attribution only for the predecessor works (odeo for theme:shancheng, orig L58; hormress for theme:parallel, carried in the candidate's banner at cand L280 and license box). LOCALIZE-S2-D lists this theme's anonymized 著作権者 among the CN2 batch's credit-completeness gaps; with no name present in the frozen source to restore, the field stands as the only supportable form, recorded here rather than flagged. If the coordinator's record names the author from outside the frozen source, naming them in both carriers is the repair shape.
- LICENSE-BOX (B71): the license box (cand L876-895) is an addition; the original carries none. Its entries name what the record supports: the base theme (Parallel, hormress, via theme:parallel-jp), the theme's own files (author recorded as the original page's creator, license unstated in the original, confirmation before posting), the parallel logos (hormress named), and the fonts with the substitution note (section 4).
- Why: the preview credit form is the JP environment's settled carrier (P3/T1); the license box is the population's TASL record (KB-63/KB-60).
- Verify: read cand L14-23 against orig L33-41; grep original.txt for author attributions and compare with the fields.
- Disposition: ledger (c3) LOCALIZE-S2-D records only P11 DISPOSITIONED (sibling / batch-posting class) for this theme; the credit-completeness observations are the S2-D report's batch findings, carried in the stamp's T4/T5 verdict.

## 2. Includes and components

- What: the gate localizes and relocates (B1, B4): orig L1 [[iftags +版式]] → cand L12 [[iftags +テーマ]]. The candidate's gate wraps the body, the code block, and the license box (cand L12-896); the original's gate wraps only its body (orig L1-280), its main module sitting outside. The candidate follows the population's settled form, and its delivery lines (cand L1-10) sit outside the gate — LOCALIZE-S2-D's structural read of this file confirms the load-bearing module is at the page head outside the iftags (its item 286).
- The base include (cand L1, inside B1's span): [[include theme:parallel-jp]] — the base theme arrives as a delivered page, replacing the original's fragment imports (section 3).
- The install example (B10): orig L61 `@@[[include :scp-wiki-cn:theme:parallel bedrock=*]]@@` → cand L43 `@@[[include :scp-jp:theme:betwixt-jp]]@@` — the example now installs the candidate itself; the bedrock parameter the original's example needed is carried as a translator's note at cand L46 (section 10), because the JP form needs no separate base instruction: the page includes its base itself.
- Why: tag names are environment-local (P2/T2, KB-08); a usage example must name the page it sits on (P1); cross-theme imports name the JP fixed base candidate (ruling 1).
- Verify: grep -n iftags on both files (orig L1/L280; cand L12/L896); read cand L1 and L42-46 against orig L60-62.
- Disposition: no ledger item charges this theme's includes; the gate and include forms are the population standard.

## 3. Delivery and code loading

- What: the delivery chain is rebuilt. Original: a gated head module-css (orig L2-27) importing fragment:parallel/code/1 and /2 from scp-wiki-cn (orig L3-4) plus five inline rules (orig L6-26), and the main CSS as a second inline module-css (orig L282-861) outside the gate. Candidate: the base arrives through the L1 include of theme:parallel-jp, whose own delivery chain is documented in review/parallel-jp/; the candidate's own CSS sits in code block 5 (cand L268-874, [[code type="css"]]) under a ソースコード heading and a collapsible (cand L265-267, B65), delivered by the head module import (cand L4) and the priority=1 interwiki-style frame (cand L7-10), both naming https://sigma10-jp-test.wdfiles.com/local--code/theme%3Abetwixt-jp/5.
- Census: the candidate holds exactly five code blocks (cand L193, L209, L236, L256 exhibits; L268 the stylesheet), so the /5 address names the stylesheet block itself — FIX-CODEADDR-conformant, no repoint owed. The original holds four code blocks, all exhibits; its CSS was never code-delivered.
- DELIVERY-MOVE fidelity: the moved block's classified deltas are exactly B66 (font imports, section 4), B67 and B68 (asset repoints: --header-logo and --header-bg at cand L306-307, the content-wrap paper texture at cand L401, all ah-sandbox → draft host with filename case normalized), B69 and B70 (font stacks, section 4), and B71's tail supplement; every other line pairs unchanged. Brace depth over the moved block ends at 0 and never goes negative on either side (orig 578 lines, cand 605 lines inside the wrappers).
- What the move loses is recorded as flags F1 and F2 in the per-theme record: the original's head module carried five inline rules of its own, and three of them are in neither the candidate nor its base; the meta-title specimen the head module's companion div carried is also gone.
- Why: in the JP environment the base is a delivered candidate page, not a code fragment on the CN wiki (ruling 1), and a theme's own stylesheet is delivered from its own code block by URL (P4/T9); the draft host is the draft-stage form (KB-41, class (iii)).
- Verify: the census greps above; read cand L1-10 against orig L1-4; the block-by-block delta list is diff.md hunks 10-11.
- Disposition: ledger (c2) dispositions the runtime-hotlink class (section 11); the restructure itself is the port's settled form for base-layered themes (compare review/parallel-jp/).

## 4. Fonts and assets

- What: the original imports three font faces at its module head (orig L289-291): Oswald, Zhi Mang Xing, and the huangkaihuaLawyerfont face from fontsapi.zeoseven.com. The candidate imports five (cand L269-273, B65/B66): Oswald and Zhi Mang Xing kept, Yomogi added, and the JP supplement loads Noto Sans JP and Noto Serif JP. The zeoseven import is gone, and the lawyer face's name appears nowhere in the candidate (grep count 0; the original names it once, at orig L558).
- The substitution is documented, not silent: the code banner (cand L282-284) and the license-box font entry both state that 黄凯桦律师手写体 is All rights reserved and non-redistributable, and that Zhi Mang Xing and Yomogi substitute for it — the documented-substitution form for a non-redistributable face. B69 (cand L562) is its stack half: "Oswald", "huangkaihuaLawyerfont", "Zhi Mang Xing", cursive → "Oswald", "Zhi Mang Xing", "Yomogi", "Noto Sans JP", cursive. B70 (cand L610, JPFONT-STACK) appends "Noto Serif JP" after the inherited "Noto Serif SC", which stays (it is the original's own stack member).
- Tail supplement (cand L865-873): a :root block appending JP fallbacks to the base's font variables (--body-font-fallback, --header-font-fallback, --UI-font-fallback, --mono-font-fallback each gain "Noto Sans JP" or "Noto Serif JP" behind the SC face). Its first line, --body-font-primary: var(--body-font-primary), is a self-referential no-op carried in the supplement; recorded factually, it changes nothing.
- Glyph forms (B62, B63): 山城图书馆 → 山城図書館 in the location specimen, body (cand L252) and code exhibit (cand L258) — simplified/traditional glyphs localized to the Japanese forms (T5).
- Assets: the three body images repoint from ah-sandbox.wikidot.com to the candidate's draft-host local--files with filename case normalized (cand L28 cm-title-def.svg, L32 parallel-theme-logo.svg, L34 parallel-theme-logo-zh.svg; B6, B7, B8), as do the CSS asset variables (section 3). LOCALIZE-S2-D records this theme's re-hosting as done (its item 2, betwixt ✓).
- Why: JP text needs JP faces loaded and named (P7/T5, KB-16/KB-17); a face that cannot be redistributed cannot be hot-loaded into the JP environment, and the substitution is recorded where a reader can find it.
- Verify: grep -n '@import' on both files; grep -c huangkaihua on the candidate returns 0; every face the candidate's stacks name (Oswald, Zhi Mang Xing, Yomogi, Noto Sans JP, Noto Serif JP) is imported at cand L269-273.
- Disposition: no ledger item charges this theme's fonts; the (c2) hotlink disposition covers the asset hosts (section 11).

## 5. Header, sidebar, site furniture

- What: the mobile sidebar mechanism is item 45's block (cand L446-460), byte-identical to the original's (per-theme record). The header variables repoint (cand L306-307, B67): --header-logo and --header-bg name the candidate's draft-host copies of the title SVG and background JPG.
- Why: the sidebar reveal is the theme's own original design (hover/focus-within), and the header artwork is the theme's own files, re-hosted under the draft-stage form.
- Verify: the hash comparison in the per-theme record; grep -n 'header-logo\|header-bg' on both files.
- Disposition: item 45 DISPOSITIONED (per-theme record); the flat light-blue header on the check wiki (the decorative assets' deferred state) is dispositioned in (c2) under the KB-47 family.

## 6. Text translation

- What: all reader-visible Chinese prose is translated in place: the intro (cand L40), the usage instructions, the element exhibits (headings, collapsibles, tabs, blockquotes, tables at cand L50-263), and the typesetting specimens, including the repeated long-tab line (B21-B31, one shape ×11) and the quote-block exhibits (B38-B41). TRANSLATION-ANCHORED ×31 blocks pair one-to-one; the TRANS-UNANCHORED blocks are the same translations at reshaped lines, resolved in the appendix. CSS comments in the moved block stay in Chinese (COMMENT-TEXT mass, expected; the block's own comments are the original author's working notes, e.g. cand L564).
- One standing finding: the film title. The intro (cand L40) and the year specimen note (cand L218, B55) render 流浪地球 as 『流転の地球』; LOCALIZE-S2-D (its item 7) judges this a mistranslation, and it is this theme's one display-affecting T4 finding in the stamp. It was not taken up as a FIX5 blocking item and stands as a classified finding of record, not a new flag from this lane.
- Why: reader-visible text localizes (P10, KB-18); CSS comments are not reader-visible and are expected heuristic mass.
- Verify: read the pairs in diff.md hunks 2-9; the film-title lines are cand L40 and L218 against orig L58 and L235.
- Disposition: T4/T5 FINDINGS, display-affecting findings: 1 [LOCALIZE-ROWS row 166, source LOCALIZE-S2-D].

## 7. Links

- What: LINK-REPOINT (B9) is the intro sentence (cand L40). Both predecessor links are absolutized to the CN wiki without annotation: theme:parallel as https://scp-wiki-cn.wikidot.com/theme:parallel and theme:shancheng as https://scp-wiki-cn.wikidot.com/theme:shancheng. The original's forms (orig L58) are plain wikilinks naming the CN pages. The credit source link (cand L22) names the recorded host and is sound.
- Why this is flagged (F3 in the per-theme record): JP candidates for both predecessors exist in this population (theme:parallel-jp, theme:shancheng-jp), parallel-jp is this file's own base include (cand L1), and the candidate's own translator's note (cand L46) names theme:parallel-jp as the base — so the sentence's absolutized CN form matches neither the repoint form the population uses where a JP counterpart exists (sunside, the-foundation-sigma repairs) nor the annotated absolutized form used where none exists (pattern 11). The counter-reading is recorded with the flag: the sentence is a provenance statement translated from the original, whose referents are the CN works.
- Verify: read cand L40 against orig L58, cand L1, and cand L46.
- Disposition: no ledger item covers these two links; flagged for adjudication, candidate not edited.

## 8. Structure

- What: EXHIBIT-RESTRUCTURE fired once (B13): the image-block exhibit at cand L52, whose changes are the component repoint to :scp-jp:component:image-block and its asset's draft-host repoint; the exhibit stands with its caption text translated. Exhibit census: every original exhibit (image grid, headings, collapsible, tabview with the long-tab and empty-tab specimens, blockquotes, tables, the variant rate/credit/block specimens, the four code exhibits, the typesetting specimens) is present in the candidate at the aligned position. The one absence is the meta-title specimen (orig L29-31), flagged as F2 — it is a title specimen, not a working exhibit, and its CSS (div.meta-title in the font rule at cand L560, L570) survives without it.
- Residue B64 (orig L280 → cand L263): the differ pairs the original's gate close with the candidate's horizontal rule above the source-code section; the substance is the gate relocation recorded in section 2 (the candidate's gate closes at cand L896), not a lost line.
- Why: exhibit losses need a stated ground (R3); here the census shows the exhibits intact apart from F2.
- Verify: the census above, read off diff.md; grep -n 'meta-title' on the candidate returns only the two CSS rules.
- Disposition: no exhibit disposition is recorded against this theme; F2 is this lane's flag.

## 9. Formatting only

- No WS-ONLY blocks and no re-indentation blocks fired over 71 change blocks: the port introduces no whitespace-only churn. Stated as the section's ground.

## 10. Porter annotations

- The code banner note (cand L275-286, inside B65): names the theme, its base (theme:parallel by hormress, delivered via theme:parallel-jp), and the font substitution with its licensing ground. Form check: the comment opened at cand L275 closes at the end of cand L286, absorbing the "Betwixt: own rules" banner line as its closing line; the pixabay/Wikimedia image-credit comment that follows (cand L287-292, carried from the original) is a separate comment, and the CSS after it is live — verified by the brace-depth scan and the block census in section 3. Cosmetic only.
- The translator's note at cand L46 (inside B11): states that the original also required loading the base theme with a bedrock designation, while the JP form includes theme:parallel-jp itself and needs only the theme-page include. The claim checks against the bytes (cand L1 includes the base; the install example at cand L43 carries no parameter).
- The tail font comment (cand L865) heads the variable supplement in section 4.
- The license-box notes (cand L879-894, inside B71) are the TASL record of section 1.
- ANNOTATION fired once (in B71); the other three ride inside DELIVERY-MOVE, TRANS-UNANCHORED, and LICENSE-BOX blocks and are recorded here explicitly.

## 11. Dispositions and exceptions

- Item 45 (WebKit sidebar): DISPOSITIONED — re-derived in the per-theme record.
- (c2) RENDER-ROWS-RERUN16 (CN2): page-overflow 434px chromium / 438px webkit at 320/375, DISPOSITIONED (KB-33/KB-34); the runtime-hotlink class including the candidate-own sandbox hosts and the base chain's hormress.github.io / nu-scptheme.github.io references, DISPOSITIONED as class (ii) posting matter (KB-41/KB-54); the sample credit-modal errors, DISPOSITIONED as the preview form's property (KB-32); the decorative 404/ORB assets leaving a flat light-blue header, deferred (KB-47 family) [GOSIGN2-LEDGER (c2)].
- (c3) P11: DISPOSITIONED (sibling / batch-posting class) [GOSIGN2-LEDGER (c3)].
- HTTP-KEPT: the classifier derives one instance, at cand L326 — the --bet-year-title-mask data-URI SVG, whose "http" strings are the W3C namespace declarations inside the data URI. That is the signature's known false-fire on data URIs, resolved here; no kept hotlink stands behind it.

## 12. Verification

- T1: the stamp's baseline stands (exit 1, 8/0/1, pseudo-ref ×8 — the eight draft-host delivery references). T2/T3: engine coverage full (chromium + webkit, both pages) per RERUN16; the WebKit finding is item 45 below. T4 follow-up: the cited artifact records rev 3 to rev 3, no changes (see Provenance); the sources.tsv supersession note is wrong and its correction is in the batch report.
- Lane re-runs (2026-11-17, this package's bytes): the item-45 block extraction and hash comparison, the code census, the brace-depth scans, the base-chain selector census behind flag F1, and the author-attribution search behind section 1 — all recorded in the per-theme record. Package acceptance (build_review.py --check, classify freshness, byte-identity of both files) is recorded in the batch report BATCH-RDISP2.md.

## Per-theme record — FIX5 item re-derived

### Item 45 [F] — DISPOSITIONED (FIX5-FUNC §1, no edit)

- The charge: a real, screenshot-confirmed WebKit-specific finding on both pages — the mobile sidebar-open hamburger renders in Chromium but is entirely absent in WebKit at 375x812 and 320x640, leaving the sidebar unreachable on all four mobile engine/viewport combinations.
- The disposition's ground: the sidebar block is byte-identical to the original's; the hover/focus reveal is the theme's own original design; the theme carries no toggle-sidebar include; the port introduced no change to the mechanism — the WebKit absence is engine-specific rendering of an original-identical mechanism.
- Re-measurement on this package's bytes (2026-11-17): candidate L446-460 and original L442-456 extract to byte-identical text (diff empty), SHA-256 eb77448c3a4349f2118790cd4b775803075316316ca7462538d3549f989c596b on both sides — the same ranges FIX5-FUNC cited. The block is the @media (max-width: 1024px) rule that hides div#top-bar div.mobile-top-bar > div.open-menu and reveals the sidebar through div#side-bar:hover and div#side-bar:is(:hover, :focus-within):not(:target). No classifier block spans candidate L446-460: the block sits in an unchanged region of the moved stylesheet, so the port's enumerated deltas (sections 3-4) provably do not touch it. A census of the candidate's includes (parallel-jp, interwiki-style frame, credit pair, image-block, license box) confirms no toggle-sidebar component exists on either side.
- Second-reviewer walk: the ground is checkable from this package alone — extract the two ranges and compare; the mechanism's design intent is readable in the block itself (the reveal selectors are the original author's, not a port repair). Any port-side "fix" (a breakpoint change, a JS-dependent class, an .open-menu override) would diverge the candidate from the original to chase one engine's rendering of the original's own CSS, which is the opposite of the port's contract. The disposition holds.

### Defect flags (candidate not edited by this lane)

- F1 — three rules from the original's head module are absent from the whole delivery chain. The original's head module-css carries five inline rules (orig L6-26): div#page-title { display: none } (L6-8), div.hover / div.hover:hover (L10-17), div.ctn > img (L19-22), div.ctn:hover > img (L24-26). The div.hover pair survives in the base: theme:parallel-jp carries div.hover (its L412) and div.hover:hover (its L419), with parallel's own additions. The other three are in neither file: grep counts for ctn and page-title in theme:parallel-jp are 0 and 0, and the candidate's own block styles div#page-title only for font (cand L559-564, L569-573). The markup they govern survives (the div.ctn / div.hover image-swap divs at cand L31-36), so the title-image swap loses the base image's fade and the theme layer no longer hides the page title. Precedent: LOCALIZE-S2-D treated fmd-bhl-theme's dropped #page-title block from its original as a finding of the same family. The classifier cannot see this loss: the two head modules pair by kind (B2), and the moved-block similarity is computed on the main module only.
- F2 — the meta-title specimen is dropped while its CSS survives. Original L29-31: [[div class="meta-title"]] ##darkblue|{{**@@//@@**}}##夹缝间 版式 [[/div]] — the theme's title specimen. The candidate has no counterpart (its head passes from the credit block straight to the image grid at cand L25), while its CSS still styles div.meta-title (cand L560, L570). No ground for the drop is stated anywhere in the file.
- F3 — the intro prose links (cand L40; section 7).

### Post-package repairs (REFRESH3-L)

The items above describe this package as built. The repair recorded below postdates the package; `candidate.txt` has been recopied from the current canonical `pages/theme:betwixt-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`, so this package now documents the post-repair candidate. The regenerated stamp reads **STALE** by design: no re-judgement is fabricated here, and the frozen ledger (`GOSIGN2-LEDGER.md` + supplement, FIX5 head 435a6bb) remains the verdict record.

**FIX-RDISP2, landing `fa9e84a` (report `R/review-scout/FIX-RDISP2.md`).** Three candidate repairs (+17/−1: three insertions, one line substituted twice over), all postdating this package's build at `b5cb724`.
- **F1 — three head-module rules restored.** Byte-identical to the original (original L6–8, L19–22, L24–26): `div#page-title { display: none; }`, `div.ctn > img { opacity: 1; transition: ease 0.25s; }`, `div.ctn:hover > img { opacity: 0; }`, restored at the head of the candidate's own rule set in code block 5 immediately before `:root`. The `div.hover` pair is untouched (covered by theme:parallel-jp). Brace depth ends at 0.
- **F2 — meta-title specimen restored.** Restored immediately after `[[include :scp-jp:credit:end-preview]]` and directly above the title-image grid, in the original's markup with the candidate's own JP name form: `[[div class="meta-title"]] ##darkblue|{{**@@//@@**}}##狭間のテーマ [[/div]]` (original: 夹缝间 版式). Its CSS (div.meta-title) now has its specimen again.
- **F3 — intro prose links, split decision.** `theme:parallel` (candidate L40→L44) was absolutized to the CN original; repointed to the candidate's own base form `[[[theme:parallel-jp|平行]]]` (the file includes theme:parallel-jp at L1 and its 訳注 already names it). `theme:shancheng` took the annotation branch (pattern 11): target kept, display text now 山城テーマ（中国語版）, because in this sentence shancheng is credited as an aesthetic inspiration (not a dependency or base) and the referent is the CN original work.
Checker per the report: plain error 8 / warn 0 / info 1 unchanged; links error 8 / warn 0 / info 1 → 8 / 1 / 1, the added warn being the F3 repoint's not-yet-posted theme:parallel-jp internal link (resolves at posting); no new class (i) error.

## Appendix — residue blocks

The 20 heuristic blocks are translation mass in three shapes, plus two seams; the single residue block is the gate seam. Each is assigned here.

- B21-B31 (orig L98-118 → cand L81-101): the long-tab exhibit's repeated text line （这是一个长的 tab，它有很多文字。 → これは長いタブです。たくさんの文字が入っています。), eleven instances of one shape. Assigned to section 6.
- B38-B41 (orig L134-140 → cand L117-123): the quote-block exhibit lines, translated. Assigned to section 6.
- B14, B15, B19 (orig L71, L75, L93 → cand L54, L58, L76): prose instruction and specimen translations whose line shape changed (the horizontal-rule explanation, the heading explanation, the specimen exclamation). Assigned to section 6.
- B9 (orig L58 → cand L40): the intro sentence; LINK-REPOINT primary, tier C because the prose translation dominates the line. Assigned to section 7 and flag F3.
- B11 (orig L64 → cand L45-46): the install cluster's tail, carrying the translator's note. Assigned to section 10.
- B64 (residue; orig L280 → cand L263): the gate-close relocation seam. Assigned to sections 2 and 8.

## License and attribution

- **Title:** 夹缝间 版式
- **Author:** 原語版ページの作成者に同じ（scp-wiki-cn の theme:betwixt）
- **Source:** https://scp-wiki-cn.wikidot.com/theme:betwixt — revision 3
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
