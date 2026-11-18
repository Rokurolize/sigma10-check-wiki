# Review package — theme:wilderness-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:wilderness-jp — origin EN, population #157 [GOSIGN2-LEDGER (b) row 157]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 30c77c057b612d684abf937d93e80aae02961b61956c43ccb97fd95f412a1716); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 3 errors / 2 warns / 2 infos (pseudo-ref×3); standing classes dispositioned in register c1 [T1-ROWS row 172; GOSIGN2-LEDGER (b) row 157]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain only; sample T2 no machine verdict (exit 2, no summary). [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- Engine coverage: full matrix as run by the lane; coverage not separately caveated in the row (the row records inconclusive runs, carried verbatim above) [RENDER-ROWS-2 row]
- Credit modal: no credit-modal line recorded [RENDER-ROWS-2 (RENDER-S2-D (EN23))]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 3 [LOCALIZE-ROWS row 157, source LOCALIZE-S2-C]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 157]
- FIX5 re-judgement: item 39 (class B) FIXED — FIX5-FURNA, commit 9e8931f: duplicate bare Rate block removed [GOSIGN2-LEDGER-SUPPLEMENT (a) item 39]
- Computed against: canonical commit b5cb7241f527a44933e45599b41df210690771c4; candidate file pages/theme:wilderness-jp.txt sha256:30c77c057b612d684abf937d93e80aae02961b61956c43ccb97fd95f412a1716; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

## 0. Header / provenance

| | |
|---|---|
| Original | `theme:wilderness` on scp-wiki (EN), revision 56 — `original.txt` in this package (412 lines / 11,006 bytes) |
| Candidate | `theme:wilderness-jp` — `candidate.txt` (423 lines / 12,546 bytes), a byte copy of `pages/theme:wilderness-jp.txt` in this repository |
| Provenance route | Derived from the original at the reference revision (route R1 in the campaign taxonomy): the Wilson's Wildlife theme over Black Highlighter. The port repoints the BHL delivery to the JP distribution, swaps in the preview credit, substitutes the National Park font delivery (the typeface's own stylesheet → the Google Fonts family, recorded in the file), re-hosts the logo as the candidate's own attachment, and translates the body, the header strings and the CSS comments. |

This theme's `review/sources.tsv` note reads "first-translation rev 56": it makes no supersession claim, and no correction is owed for this package.

Status note: the verdict stamp above reads STALE by design. The stamp was computed against canonical commit b5cb724 — the usage-example sweep changed the candidate (its usage lines) after the FIX5 verdict was computed. The stamp's verdicts describe the pre-sweep file; the per-theme record below re-derives the theme's one blocking item on the current bytes, which is the point of the STALE form.

Summary: the Wilson's Wildlife Solutions theme. The port keeps the original's delivery topology exactly (head BHL module, two priority frames, one code block, a colors module, the transpride parameter gate, tail delivery), swaps the bare Rate region for the preview credit, repoints the BHL pair to the JP distribution, moves the National Park typeface from its own @font-face stylesheet to the Google Fonts family with weight-mapped variables (a substitution recorded in the banner and the license entry), re-hosts the trans-pride logo as the candidate's own attachment, and translates the body, header strings and CSS comments. The theme carried one blocking item, 39 (class B), re-derived in the per-theme record. No defect flags arise from this package.

## Class summary

| Label | Blocks |
|---|---|
| BARE-RATE-DEL | 1 |
| COMPONENT-SWAP | 1 |
| CREDIT-PREVIEW | 1 |
| CREDIT-PROSE | 1 |
| CSS-BODY | 4 |
| DELIVERY-HOST | 2 |
| DRAFT-HOST | 4 |
| EXHIBIT-RESTRUCTURE | 6 |
| HEADERVAR | 2 |
| IFTAGS | 1 |
| INCLUDE-REPOINT | 6 |
| JPFONT-LOAD | 1 |
| JPFONT-STACK | 1 |
| LICENSE-BOX | 2 |
| SELF-DELIVERY | 2 |
| TASL-FIELDS | 1 |
| TRANS-UNANCHORED | 42 |
| TRANSLATION-ANCHORED | 7 |
| COMMENT-TEXT | 24 |
| WS-ONLY | 5 |

Counts: 73 blocks, 25 specific, 43 heuristic, 5 residue, 0 skipped (comment text). Topology: module-css ×4 + code-css on both sides, in the same order, no moves.

## 1. Credit and attribution

- The original's credit region (original L16–19) is the unlabelled bare Rate standing ahead of the original-form credit include — this theme's blocking item 39 (per-theme record). The candidate's credit block (candidate L17–27; block B7: BARE-RATE-DEL + CREDIT-PREVIEW + CREDIT-PROSE + TASL-FIELDS) is the preview form with the ruling-3 fields complete: 翻訳責任者 `AI` (L19), 翻訳年 `2026` (L20), 著者 `stormbreath` with the DarkStuff co-production note (L21), 著作権者 `[[*user stormbreath]]` (L23). The T4 lane's section-3 charges for this theme (翻訳責任者/翻訳年 missing; the 著者→著作権者 item-name variance) are resolved in these bytes. Ledger (c3): P3 credit fields FIXED by the credit waves, checker-verified. Jade Skylar, the logo's creator, stands in the code banner (candidate L141) and in the license entry (candidate L395) — the original's own carriers for her.
- Census: `[[module Rate]]` 1 → 0 (class P3 / KB-09, patterns/ at commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa).
- License box (blocks B66, B68): the original's `component:license-box-theme` form (original L378–393, three entries) becomes `:scp-jp:component:license-box-backend` with `author=stormbreath` (candidate L390–404) — class T4 applied as a form swap. Two entries stand: the trans-pride logo (full fields; its 出典 line records it as a derivative of `WWS_Logo_2.2_abrv.png` attached to the EN theme page) and the National Park Font (出典 Google Fonts, with the note that this port loads it from Google Fonts directly). The original's standalone entry for the standard logo is consolidated into the derivative entry's 出典 line; the candidate never loads the standard logo file (neither did the original's CSS — its `--logo-image` default is already the trans-pride file), so no loaded asset lacks an entry. The classifier's "restoration (KB-63)" note on these blocks is its template text for license-box regions; the writer's call, verified entry by entry above, is form swap plus entry consolidation.
- Verify: `grep -c 'module Rate'` on both files (1 / 0); read candidate L17–27 and L390–404 against original L16–19 and L378–393.

## 2. Includes and components

- Live includes: the two head frames (`:scp-jp:component:interwiki-style` at priorities 1 and 2, candidate L7–15; blocks B3 and B5 — their EXHIBIT-RESTRUCTURE primaries are false fires, mere include repoints), the credit pair (section 1), `theme-squares` repointed to `:scp-jp:` (candidate L45–46; block B14), the license pair (section 1), and the tail frame (priority 3, candidate L420–423; block B72, the same false-fire shape).
- Usage examples (block B12; original L27–30 → candidate L37–40): the self-include is repointed to `:scp-jp:theme:wilderness-jp`, and the transpride parameter example is preserved (`transpride=a`, candidate L40) — the parameter the tail gate consumes (section 3).
- The visited-link specimen (candidate L92) names `component:wilderness-theme` — the original's own specimen form (original L82), kept as a specimen; the checker's `link-target-missing` warning for it is recorded in section 11.
- Verify: `grep -n 'include' candidate.txt`.

## 3. Delivery and code loading

- Topology is identical on both sides (classifier): a head module importing the BHL pair, a small colors module, one code block, the transpride gate module, and the tail module, in the same order. The BHL pair is repointed from `cdn.scpwiki.com` (the nu-scptheme BHL distribution) to `scp-jp.github.io/Black-Highlighter/css/min/` (candidate L3–4; block B2, labeled CSS-BODY heuristic — the host swap is classes P4 / T9 by hand).
- Tail delivery (blocks B71, B73): the tail module imports own `/1` from the draft host (candidate L418) and the priority-3 frame names own `/1` (candidate L422). Census: exactly one code block stands (candidate L135–385, counting every form), and `/1` names it — the stylesheet. Self-delivery census: MATCH (class FIX-CODEADDR).
- The transpride gate (block B70; candidate L407–415) stands in render-time text in the original's blockquoted form, after `[[/iftags]]`, its tag localized (`-theme` → `-テーマ`) and its `--logo-image` re-hosted to the candidate's own attachment. Include-parameter substitution reaches render-time text, so the gate acts — the delivery-chain test the campaign's parallel gate repair established. Its position and form are the original's.
- The page gate `[[iftags +テーマ]]` opens the file at candidate L1, as in the original; the tail delivery stands outside it on both sides.
- Verify: `grep -n 'local--code' candidate.txt` (`/1` twice); count `[[code` blocks (1).

## 4. Fonts and assets

- The font-program substitution (block B29, JPFONT-LOAD; original L126–127 → candidate L136): the original loads `national-park-full.css` from `scp-wiki.wdfiles.com` (the @font-face stylesheet defining the `national_parkthin` / `national_parkregular` / `national_parkheavy` faces) plus Comfortaa 600, Dosis 200 and Nunito 800 from `fonts.bunny.net`. The candidate loads one Google Fonts css2 line: `National Park` wght 200;400;800 with Comfortaa 600, Dosis 200, Nunito 800 and Noto Sans JP 400;700. The three variables are rewritten onto the single family, keeping the original fallbacks and adding Noto Sans JP (candidate L155–157), and the weight differentiation the three @font-face families carried is restored by `font-weight` declarations at the use sites: 200 at candidate L226 and L249, 800 at candidate L282 (blocks B51, B54, B58, labeled CSS-BODY heuristic — a P7-family mapping by hand).
- This is a delivery-channel and family-mapping substitution of the same typeface (same designers, same SIL OFL license), and it is recorded in the file: the banner's font pointer now names `fonts.google.com/specimen/National+Park` (candidate L143–144; the original named nationalparktypeface.com), and the license entry states the port loads it from Google Fonts directly (candidate L399–402). It is therefore not the unrecorded-substitution flag shape.
- Block B62 (JPFONT-STACK; original L301 → candidate L313): the `.rate-points` stack gains `'Noto Sans JP'` (class P7). No face is named-but-unloaded and no loaded family is unapplied: every family in the stacks stands in the candidate L136 load.
- Assets: `--logo-image` is re-hosted from `scp-wiki.wdfiles.com` (`theme%3Awilsons/wws-trans-pride.png`) to the candidate's own draft-host attachment (candidate L162; block B34, HEADERVAR + DRAFT-HOST), and the same re-host stands inside the transpride gate (candidate L411; block B70). The checker's pseudo-ref errors name these draft forms (section 11).
- The porter prose at candidate L29 announces the program (all fonts SIL OFL 1.1 from Google Fonts; Noto Sans JP for Japanese text) — and the announcement matches the bytes (section 10).
- Verify: `sed -n '136p' candidate.txt` against original L126–127; `grep -n 'font-weight' candidate.txt`.

## 5. Header, sidebar, site furniture

- Block B34: `--header-title: "Wilson's Wildlife Solutions"` → 「ウィルソンズ・ワイルドライフ・ソリューションズ」 (candidate L163), and `--header-subtitle: "Where all critters are welcome!"` → 「あらゆる生き物を歓迎する場所」 (candidate L164). The subtitle is a complete prose sentence rendered for every reader, so it translates under the T5 boundary (a sentence a reader reads as prose gets translated); the title is the organization's name, carried in its established Japanese form.
- Verify: `grep -n -- '--header-'` on both files.

## 6. Text translation

- The body and the CSS comments are translated throughout (TRANSLATION-ANCHORED 7 blocks, TRANS-UNANCHORED 42, COMMENT-TEXT 24): the intro and usage prose, the theme-squares specimens, the collapsible labels, and the code block's section comments (`/* イントロ */`, `/* フォント */`, `/* ヘッダー */`, `/* 色 */`, `/* 要素 */`, …). CSS comment translations are expected heuristic mass, resolved in the appendix by shape.
- Verify: the translation spans in `classification.json` against both files.

## 7. Links

- Candidate L33: the prose link names `theme:black-highlighter-theme`, the production JP base page. The checker's `link-label` warning proves the target resolves (its live title, "Black Highlighterテーマ", differs from the label 詳しくはこちら）; the label is the port's prose choice, and the warning is recorded verbatim in section 11.
- Candidate L92: the visited-link specimen (section 2).
- The license entries' source links name the EN original page and Google Fonts (sections 1 and 4) — the recorded hosts. No host defect stands for this theme.
- Verify: the `--check-links` output in section 12.

## 8. Structure

- Topology identical (section 3); the code block's rules stand in the original's order. Two inherited defects of the original are carried byte-identically, as parity: the `#page-content .creditButton > p > a::before` selector (candidate L316; original L304) — a ::before icon rule, not one of the six `.creditButton p a` copies the creditbtn lane enumerated under KB-11, and uncharged by T1/T4 — and the missing-semicolon `--wght: 800` declaration (candidate L377; original L365). `--pale-accent` is defined twice on both sides. Whatever these do, they do on both sides.
- Exhibit census: theme-squares, the colors module, the visited-link specimen, the code exhibit and the license entries all stand against the original; nothing was dropped or escaped away.
- CSS brace balance was checked by depth, not count: both files scan to final depth 0 with minimum depth 0.
- Verify: `grep -n 'creditButton' ` on both files; `grep -n 'wght' ` on both files.

## 9. Formatting only

- WS-ONLY 5 blocks (B32, B52, B55, B59, B60): whitespace-only changes inside the code block — the original's tab-indented `:root` lines normalized to spaces, and rule-separation spacing. No rule text changes in these blocks.
- Verify: the WS-ONLY spans in `classification.json`.

## 10. Porter annotations

- None added in comment form: the code banner is the original's, with its font pointer updated to the substituted delivery (section 4) — a record correction riding the banner, not an annotation.
- One prose-carrier annotation: candidate L29, the font-program statement (all fonts SIL OFL 1.1, loaded from Google Fonts; Noto Sans JP serving Japanese text). It announces the section-4 substitution, and its statement matches the bytes.
- Verify: read candidate L29 and L138–145.

## 11. Dispositions and exceptions

- Draft-host lines (pseudo-ref ×3, the T1 baseline's errors): candidate L162 and L411 (the logo `url()` draft forms) and L418 (the `/1` import) — class (iii) draft forms, rewritten at posting.
- Warnings recorded verbatim: `link-label` ×1 (candidate L33, section 7), `link-target-missing` ×1 (candidate L92, the specimen, section 2).
- Render row (RENDER-S2-D, EN23): the page's only line is the runtime-hotlink site-theme chain (KB-40, environment layer) — DISPOSITIONED. The sample's T2 returned no machine verdict (exit 2): a coverage caveat, not a finding.
- The STALE stamp's ground is section 0's status note: the post-verdict change is the usage sweep's lines (section 2), and no re-judgement is fabricated for it.
- No class (i) item stands for this theme, and no defect flag arises from this package.

## 12. Verification

- T1 run by this lane on the current candidate: plain run error 3 / warn 0 / info 1; with `--check-links`, error 3 / warn 2 / info 1 — FIX5-FURNA's after state (3/2/1) exactly; the stamp baseline (3/2/2) describes the pre-FIX5 file, its second info being the `double-rate` line the fix cleared. No `double-rate` finding in either mode.
- T2/T3: FINDINGS with dispositions only (ledger row (c2)).
- T4 follow-up: the FIX5 fix is the follow-up's product; the per-theme record re-derives it.
- Package checks: `candidate.txt` byte-identical to the canonical file (sha256 `30c77c05a1a796b1ab0e5fa9b8fae40e9ee8a6b9ae4c47db0d5c06a3b33e6716`); `original.txt` hash equals the sources.tsv value (`20336b6d9e7acb3fe7ad169987d4f79a06d86ff7d95eb9113719037c3becfa71`); brace-depth scans clean on both files; `build_review.py --check` at acceptance.

## Per-theme record — the FIX5 closure, re-derived

- Blocking item 39 (ledger (b) row 157, class B): a duplicate bare `[[module Rate]]` standing beside the rate-bearing preview credit — two rating widgets render (T1-ROWS row 172; LOCALIZE-ROWS row 157, pattern 3, "display-affecting"). The theme's (c3) line records P1 DISPOSITIONED (the posting-procedure convention class) and P3 FIXED by the credit waves → (e).
- History: LOCALIZE-S2-C checklist item 14 had left the Rate an unmade staff call under the exhibit-exception reading — a labelled paired exhibit may keep a demonstration Rate. Items 37 and 38 are the same history on the sibling themes.
- What the fix was supposed to change: remove the duplicate block, leaving the preview credit as the page's only rating widget — if the exception did not cover the block.
- Supplement re-judgement: FIXED, FIX5-FURNA, commit 9e8931f. The FURNA lane report's evidence: the pre-edit candidate at L16–18 held the unlabelled `[[>]]` / `[[module Rate]]` / `[[/>]]` immediately before `credit:start-preview` (L21); not the labelled paired exhibit the exception covers, so the whole wrapper was removed; checker 3/2/2 → 3/2/1, the `double-rate` info cleared, no new errors.
- Re-derived from this package's bytes: the original carries the identical unlabelled Rate at original L17–19. The current candidate contains no `[[module Rate]]` (`grep -c` = 0), and its preview credit block stands alone at candidate L17–27. This lane's checker runs report no `double-rate` line.
- Closure: CONFIRMED on current bytes — which matters here, because the verdict stamp is STALE (section 0): the closure is re-derived from the package, not inherited from the stamp.

## Change set outside the two diffed files

1. `pages/theme-decoration-sample-wilderness-jp.txt` — the render-check sample page for this theme.
2. The candidate's own delivered file: the re-hosted trans-pride logo attachment (section 4).
3. No base-theme dependency beyond the BHL distribution itself (section 3).

## Multi-wave provenance

- The S2 localization wave (LOCALIZE-S2-C) produced the port: P3 credit fields fixed by the credit waves (resolving the T4 section-3 field charges), the BHL repoint, the font-delivery substitution, and the translation; the bare Rate survived that wave as the unmade staff call.
- FIX5-FURNA (commit 9e8931f) removed the Rate wrapper and closed item 39.
- The usage-example sweep (commit b5cb724) then completed the usage lines' `-jp` names — the post-verdict change behind the STALE stamp.

## Appendix — heuristic and residue adjudication

The classifier reports 5 residue blocks and 43 heuristic blocks. All resolve by shape:

- Residue (unlabeled) B4 and B6: the two head frames' `theme=` URL lines (the normalize and BHL addresses inside the interwiki includes) — include repoints, section 3.
- Residue B30: the banner's font-pointer lines (the license statement carried; the pointer updated to the substituted delivery) — section 4.
- Residue B35 and B63: CSS comment translations (`/* Colors */` → `/* 色 */`; `/* Elements */` → `/* 要素 */`) — section 6.
- Heuristic mass by shape: the TRANS-UNANCHORED and COMMENT-TEXT blocks are the body prose and CSS comment translations (section 6); the EXHIBIT-RESTRUCTURE primaries (B3, B5, B14, B66, B68, B72) are include repoints and the license-box form swap at exhibit loci (sections 1–3), false fires against the exhibit census; the CSS-BODY blocks are the BHL host swap (B2, section 3) and the three font-weight mappings (B51, B54, B58, section 4); the WS-ONLY blocks are section 9.

No heuristic or residue block is left unadjudicated, and no defect flag arises from this package.

## License and attribution

- **Title:** Wilderness Theme
- **Author:** stormbreath
- **Source:** https://scp-wiki.wikidot.com/theme:wilderness — revision 56
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — license deed: https://creativecommons.org/licenses/by-sa/3.0/
- **Adaptation:** This package holds a Sigma-10 migration port of the work; changes were made. See "Summary" and "Standing sections" in this README for what changed and why. Translator: AI (Muse and its delegated agents), per the campaign's standing attribution rule.
