# Review package — theme:fmd-bhl-theme-jp

<!-- BEGIN GENERATED VERDICT STAMP — do not hand-edit; regenerate with review/build_review.py -->
## Verdict stamp
- Theme: theme:fmd-bhl-theme-jp — origin CN, population #188 [GOSIGN2-LEDGER (b) row 188]
- Overall: STALE — candidate file changed since the verdict was computed (verdict against 435a6bb-era content, file sha256 now 57a6bdf6d5df40f26e6ac5c6f63b88571d365beeb25e7320979e642102499644); verdict not carried over, re-judgement required
> verdicts below describe the pre-change file
- T1 (source check): FINDINGS (classified) — baseline 2026-11-16: exit 1, 5 errors / 1 warn / 1 info (hotlink×4, pseudo-ref×1); standing classes dispositioned in register c1 [T1-ROWS row 166; GOSIGN2-LEDGER (b) row 188]
- T2/T3 (render, combined verdict): FINDINGS — [combined T2/T3] report `FINDINGS` — page runtime-hotlink site-theme chain + candidate-own scpsandboxcn.wdfiles.com (judgment-required); sample credit-modal (preview-form), runtime-hotlink incl. scpsandboxcn.wdfiles.com + sample font host; no page-overflow on either page; T3 clean on both pages, with the caveat that the mobile *-full.png (and sample *-credit.png) are blank transient 503 captures while the same-viewport sidebar/credit shots are real and show the left sidebar opening in both engines (no rule-2 http.cat + hidden-* machine signature on this target). [RENDER-ROWS-RERUN16 (CN6) — supersedes the RENDER-ROWS-2 row for this theme, rule S1]
- Engine coverage: full (chromium+webkit, both pages) [RENDER-ROWS-RERUN16 (CN6)]
- Credit modal: sample credit-modal errors dispositioned preview-form (credit:start-preview has no modal mechanism; GOSIGN-TESTS T2 amendment, 2026-11-16) [RENDER-ROWS-RERUN16 row]
- T4 (localize patterns + follow-up): FINDINGS — display-affecting findings: 4 [LOCALIZE-ROWS row 187, source LOCALIZE-S2-D]
- T5 (translation text): FINDINGS — the source reports judge T4/T5 jointly; one verdict word covers both [LOCALIZE-ROWS row 187]
- FIX5 re-judgement: item 56 (class D) FIXED — FIX5-FONTSB, commit 3911f7b: pattern-7 fix; BIZ UDPGothic GET-verified to serve [GOSIGN2-LEDGER-SUPPLEMENT (a) item 56]
- Computed against: canonical commit c923abfb13007617bf34dd8cbde0512171d5cf10; candidate file pages/theme:fmd-bhl-theme-jp.txt sha256:57a6bdf6d5df40f26e6ac5c6f63b88571d365beeb25e7320979e642102499644; record: GOSIGN2-LEDGER.md + GOSIGN2-LEDGER-SUPPLEMENT.md as of the FIX5 head 435a6bb
<!-- END GENERATED VERDICT STAMP -->

Status: complete (hand-written explanation; verdict stamp and diff.md are generated and must not be hand-edited).
Candidate: review/fmd-bhl-theme-jp/candidate.txt (sha256 8c49f3680a977fb86de7ac7b26c072a6dfd9dd929b2e225dadf9ec8e6d0d7431)
Original: theme:fmd-bhl-theme — scp-wiki-cn, revision 19 (sha256 5b2f160a456f7a376ad2df90e0c3fc908537fc5aa3b661d16f043ec6d6a3cd1e)
Classifier: classify_hunks.py 0.1.0; signature table 2026-11-17.1; patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa

## Status

| Test | Verdict (frozen record) | Where recorded |
|---|---|---|
| Population row | #188 of 287 | review/sources.tsv |
| T1 source check | FINDINGS (classified) | T1-ROWS row 166 |
| T2/T3 render | FINDINGS, all items dispositioned | RENDER-ROWS-RERUN16 (CN6), superseding RENDER-ROWS-2 under rule S1 |
| T4/T5 localize + translation | FINDINGS, display-affecting 4 | LOCALIZE-ROWS row 187, source LOCALIZE-S2-D |
| Blocking item | (e) item 56 [D], pattern 7 | GOSIGN2-LEDGER (e) |
| FIX5 re-judgement | FIXED (FIX5-FONTSB, commit 3911f7b) | GOSIGN2-LEDGER-SUPPLEMENT item 56 |
| Overall | PASS in the go-sign determination; stamp reads STALE because the candidate changed after the verdict (one usage-sweep line) | GOSIGN2-LEDGER + SUPPLEMENT; generated stamp above |

## Provenance

| | |
|---|---|
| Original | theme:fmd-bhl-theme, scp-wiki-cn, revision 19 (first-translation reference) |
| Original file | review/fmd-bhl-theme-jp/original.txt, sha256 5b2f160a456f7a376ad2df90e0c3fc908537fc5aa3b661d16f043ec6d6a3cd1e, 13,509 B |
| Mirror route | COPY class: byte copy of the frozen S2 cache gosign2-lanes/lane-oc-gs-localize-s2-D/orig-fmd-bhl-theme.txt (R/review-mirrors/INDEX.tsv) |
| Candidate | pages/theme:fmd-bhl-theme-jp.txt, sha256 8c49f3680a977fb86de7ac7b26c072a6dfd9dd929b2e225dadf9ec8e6d0d7431 |
| Follow-up currency | diff-fmd-bhl-theme-from19.txt records rev19 to rev19, no changes; nothing past the reference revision to follow |
| Provenance route | Derived: translated and restructured from the original at revision 19 (not a production adoption; no production JP counterpart exists) |

One record defect rides in review/sources.tsv itself: its note for this row claims the original was "superseded upstream since the reference revision", but the follow-up artifact the same note cites records rev19 to rev19 with no changes. The note's first clause is wrong (the same wrong-note shape corrected centrally for ambrose, alcur, inland-empire, wish-for-miracle and yore); the correction is the coordinator's to land in sources.tsv, and this package follows the artifact.

## Summary

A Black-Highlighter-based department theme from SCP-CN. The port swaps the CN credit block for the JP preview credit block, repoints the BHL base delivery to the JP Black-Highlighter distribution, loads the theme's own CSS from the draft host, and translates the exhibit body. The theme carried one blocking item, ledger item 56 [D]: no Japanese font was loaded or wired, so Japanese text fell back to OS defaults and the exhibit's own font claims were false. FIX5-FONTSB (commit 3911f7b) loaded Noto Sans JP and BIZ UDPGothic and rewired the five stack sites; the fix is verified byte by byte in the per-theme record below. Three T4-recorded losses stand unfixed and are documented in section 8: the head module's #page-title rules, the top banner image, and an emptied theme-code collapsible, plus a dropped centering opener no record had named.

## 0. Header / provenance

- What: original.txt is the frozen mirror of theme:fmd-bhl-theme at revision 19 (502 lines); candidate.txt is the canonical candidate (521 lines). The classifier found 62 change blocks (27 signature-specific, 29 heuristic, 6 residue, all adjudicated in the appendix); diff.md is Tier 1 (255 changed lines by the generator's count, 8 hunks, full unified diff printed).
- Why: a reviewer must be able to check the port against the exact revision it was made from; the mirror is hash-pinned in review/sources.tsv so any drift is detectable.
- Verify: `sha256sum review/fmd-bhl-theme-jp/original.txt` against the sources.tsv value above; `python3 review/build_review.py --check`.
- Disposition: provenance stands as recorded, with the sources.tsv note defect flagged above and in the batch report.

## 1. Credit and attribution

- What: the original's CN credit includes (:scp-wiki-cn:credit:start/end, original L61/L64) around the author line [[*user ai_mayca]] and a department line are replaced by the JP preview credit block (candidate L22-31, block B5) carrying all eight TASL fields. The copyright-holder field names AI_Mayca (candidate L28), matching the author the original names; the source link (candidate L30) points at https://scp-wiki-cn.wikidot.com/theme:fmd-bhl-theme, the host recorded for the original in review/sources.tsv, so there is no wrong-host defect of the jiha family. The title field keeps the Chinese title as a quotation, and the translator field is the bare string AI; the FIX-CREDIT-D wave (commit 1869877) set that field from SCP-JP to AI, the ruling-3 form. Neither side carries a license-box or info block; the only license text is the CSS comment "Logo licensed under CC BY SA 3.0" inside the code block (original L179, candidate L191), carried over.
- Why: pattern P3 with the TASL record (ruling 3 of RULINGS-20261116): the credit block is where a reader verifies whose work this is and under what license the translation is offered. The preview form (credit:start-preview) is the campaign form for candidate pages (KB-32).
- Verify: diff block B5; read candidate L22-31 against original L60-65.
- Disposition: T4 judged P3 APPLIED with two notation findings (Chinese title field, bare translator string), both standing campaign forms; the ledger records no P3 charge for this row.

## 2. Includes and components

- What: the candidate adds a base include the original does not have, [[include:scp-jp:theme:black-highlighter-theme]] (candidate L2), wrapped in a bare [[iftags]] gate (candidate L1-3, block B1). The original imports the same base's CSS only (section 3). The component include is repointed from :scp-wiki-cn: to :scp-jp:component:theme-squares (candidate L36; block B6). The usage exhibit's escaped includes are repointed the same way (candidate L77-78; B15), and the self-include among them was later swept to the -jp self-name (candidate L78, the one post-verdict line, section 11). Three interwiki-style frames are added (priorities 1 and 2 for the base stylesheets, candidate L10-18; priority 3 for the theme's own code, candidate L518-521).
- Why: patterns P1 (include targets resolve on scp-jp), P2 (gate tags localized: the body gate at candidate L20 reads [[iftags +テーマ]] against the original's page-wide [[iftags +版式]]), P6 (the interwiki frame set follows the delivery split). A base the theme's CSS is written against must be included, not merely imported, in the JP delivery form.
- Verify: `grep -n '\[\[include' ` on both files; diff blocks B1, B6, B15, B61, B62.
- Disposition: T4 judged P1, P2 and P6 APPLIED. The bare [[iftags]] opener is a population form (21 candidate files open with one); T4 recorded the same shape in food-jp and referred the empty-gate evaluation to staff/render confirmation. It is recorded here as an observation, not a defect.

## 3. Delivery and code loading

- What: the head module's two BHL stylesheet imports move from bhl.scpwikicn.com to https://scp-jp.github.io/Black-Highlighter/css/min/ (candidate L6-7; block B2). The theme's own CSS sits in a single [[code type="css"]] block on each side (original L172, candidate L184), and the tail module's self-delivery import moves from the CN host's theme:fmd-bhl-theme/code/1 (original L501) to the draft host's local--code/theme%3Afmd-bhl-theme-jp/1 (candidate L516; B61), with the priority-3 interwiki frame naming the same address (candidate L518-521; B62). The address /1 names the file's only code block, so the self-delivery census (FIX-CODEADDR) records this theme as MATCH and no remedy applies. The original's head module also carried #page-title rules that were not carried into either the candidate's head module or its code block; that loss is structural and is recorded in section 8, not hidden here. FIX4-MECH (commit a497307) removed the duplicated BHL @imports that the first port had repeated inside the code block (KB-65); the current file imports each stylesheet once per delivery channel.
- Why: pattern P4 and T9 delivery classes: a candidate must load from hosts that exist in the JP environment, and its self-delivery address must name the block that actually holds its CSS, or the theme silently renders unstyled.
- Verify: `grep -n '@import' ` on both files (candidate: L6, L7, L195-200, L516; original: L3, L4, L183-185, L501); count [[code]] blocks (one per side).
- Disposition: T4 judged P4 APPLIED. The draft-host self-delivery is T1 class (iii) pseudo-ref, dispositioned in register (c1); at posting it becomes the page's own local--code address.

## 4. Fonts and assets

- What, assets: four references to the CN sandbox host (scpsandboxcn.wdfiles.com) are kept, with the scheme upgraded http to https: the exhibit logo image (candidate L56), the --logo-image variable (candidate L215; block B54), and two background images inside the code block (candidate L335 and L438; B56, B57). The original's top banner image (original L20, the fmdBHL file on the same host) has no counterpart anywhere in the candidate; T4 recorded the drop under pattern 5, and it is carried in section 8.
- What, fonts: at verdict time the candidate loaded only the original's Latin faces (PT Mono, Exo, Roboto) and its stacks named Chinese faces (the mono stack named '仿宋', original L208 and L439) or "Noto Sans SC", which was not loaded either. FIX5-FONTSB (commit 3911f7b) added a porter comment and two Google Fonts imports, Noto Sans JP and BIZ UDPGothic (candidate L198-200; B53), and rewired five stack sites: --body-font, --header-font, --title-font and --mono-font in the :root block (candidate L220-223; B55, which the classifier labels CSS-BODY heuristic and which is narrated here as the P7 stack rewrite it is) and the .code-element rule (candidate L454; B58). The exhibit's three font-claim spans (candidate L168-170; B50) were already worded for the fixed state, so the fix also cured T5's two claim-versus-code mismatches from the CSS side.
- Why: pattern P7: Japanese text must render in a Japanese face the file actually loads, or the theme's typography silently falls back to OS defaults. Pattern P5 / KB-58: sandbox attachments are class (ii), re-hosted at posting; keeping them preserves the original's appearance until then.
- Verify: `git show 3911f7b` in the canonical history; `grep -n 'font-family\|--body-font\|--header-font\|--title-font\|--mono-font' ` on candidate.txt (L220-223, L454) and on original.txt (L205-208, L439); the supplement records the BIZ UDPGothic import as GET-verified.
- Disposition: ledger item 56 [D] (pattern 7) re-judged FIXED by FIX5-FONTSB in GOSIGN2-LEDGER-SUPPLEMENT item 56, and re-derived from the bytes in the per-theme record below. Pattern 5 is DISPOSITIONED class (ii) / KB-58 in GOSIGN2-LEDGER (c3).

## 5. Header / sidebar / site furniture

- What: the original's :root:lang(cn) variable block is kept verbatim (candidate L210-237) except for the logo URL scheme (B54) and the FIX5 stack lines (B55). Its --header-title and --header-subtitle keep the Chinese strings (candidate L216-217). No :root:lang(ja) block was added, and the theme defines no sidebar or topbar text of its own beyond these variables.
- Why: pattern P9 covers header and title language. Keeping the block preserves the original's variable definitions for any lang(cn) consumer; the JP header rendering takes the base theme's variables.
- Verify: read candidate L210-237 against original L204-237; `grep -n 'header-title' ` on both files.
- Disposition: T4 charged P9 as MISSED and display-affecting; GOSIGN2-LEDGER (c3) DISPOSITIONED it under ruling 2 of RULINGS-20261116 (header and title language is out of scope for migration correctness). The strings stand as the original's, per that ruling.

## 6. Text translation

- What: the exhibit body is translated throughout: 19 TRANSLATION-ANCHORED blocks and the TRANSLATION-UNANCHORED exhibit mass (26 blocks) cover the headings, tab names, table and formatting samples, and collapsible labels between candidate L36 and L183. The font-claim spans (candidate L168-170) are translated and, after FIX5, true (section 4). CSS comments inside the code block stay in the original's Chinese and English (the SCPF banner comment and section comments); they are source-visible only, the T5 comment class.
- Why: pattern P10 with T5: reader-visible prose must be Japanese; comments are the recorded exception class, resolved by shape in the appendix.
- Verify: read candidate L36-183 against original L28-171; the anchored blocks are listed in classification.json.
- Disposition: T4 judged P10 APPLIED. T5's findings for this theme were the two font-claim mismatches (cured by FIX5, section 4) and the empty collapsible (section 8).

## 7. Links

- What: the only prose link whose host matters is the credit source link, verified in section 1 (host matches the original's recorded host). The component and include links are covered in section 2. No links to the original site's tag or hub pages exist on either side.
- Why: a source link naming a dead or wrong host breaks attribution; the campaign has already repaired that defect family in five candidates (the 2a8a125 host fix), so each package re-checks it.
- Verify: `grep -n 'wikidot.com' ` on candidate.txt and compare hosts with review/sources.tsv.
- Disposition: no link defect. T4 judged P11 not applicable for this theme.

## 8. Structure

- What: four structural facts, in page order. (a) Gate restructure: the original wraps the whole page in [[iftags +版式]] (original L1, closer L498); the candidate gates only the base include at the head (bare form, L1-3) and wraps the body in [[iftags +テーマ]] (candidate L20-513). (b) The original's bare [[module Rate]] inside a [[>]] block (original L58-60) is deleted (block B11, BARE-RATE-DEL); the empty [[>]]/[[/>]] pair survives at candidate L66-67 as dead markup, which T4 noted as a minor residue. (c) The original head module's #page-title rules (original L6-17: centered, font-family var(--header-font), 270%, and a max-width 765px variant at 170%) have no counterpart in the candidate. The candidate does contain a #page-title rule (candidate L399), but it is the counterpart of the original's code-block rule (original L384: border color, uppercase, small-caps), a different rule. The candidate's own porter annotation at the code block's head (candidate L185) says the block consolidates the original's module and code-block CSS, which is inaccurate for these rules. (d) The first centered heading lost its opener: the original centers it with [[=]]/[[/=]] (original L24-26); the candidate keeps the heading and an orphan [[/=]] (candidate L33-34). No campaign record names this; it is recorded here first. (e) The original's theme-code collapsible wrapped the code block (original L171-172); in the candidate the same collapsible stands empty (candidate L175-177; B51) and the code block moved under a new source-code section (candidate L179 onward).
- Why: pattern P2/P8 structure: a dropped rule block changes rendering (the page title loses its centered 270% treatment), an orphan closer and an empty collapsible are reader-visible defects, and a porter annotation that overstates what was carried misleads the next editor.
- Verify: `grep -n 'page-title' ` on both files (original L6, L13, L384; candidate L399 only); read candidate L33-34 against original L24-26; read candidate L175-183.
- Disposition: the Rate deletion is the settled KB-09 form (the preview credit module is rate-bearing) and is not a defect. Items (c), (d) and (e) stand unfixed: T4 charged (c) as a degradation and flagged (e) for deletion, and neither was raised as a blocking (e) item, so the go-sign did not turn on them; they are recorded here so a future editor can repair them with full knowledge. Item (d) is this package's own finding.

## 9. Formatting only

- What: none. The classifier records zero reindent blocks and no whitespace-only block for this pair; every whitespace change rides inside a translated or restructured block.
- Why: formatting-only mass must be separable from real change so the reviewer does not mistake churn for edits.
- Verify: classification.json summary (reindent_blocks 0) and the appendix.
- Disposition: nothing to disposition.

## 10. Porter annotations

- What: two porter annotations exist. The code-block banner (candidate L185) states the consolidation of the original's module and code-block CSS; section 8(c) records the one respect in which it overstates the bytes. The FIX5 font comment (candidate L198) states that Noto Sans JP and BIZ UDPGothic were loaded and wired for Japanese text; it is accurate. Review-stage comment lines in the diff: 0 of the +135 added lines (both annotations predate the review stage; they are port and fix-wave text).
- Why: annotations are the porter's testimony about their own work; where testimony and bytes disagree, the bytes govern and the disagreement is documentation-relevant.
- Verify: read candidate L184-200.
- Disposition: recorded; no separate ledger charge covers annotation accuracy for this row.

## 11. Dispositions and exceptions

- What: the row's complete disposition set. T1: 5 errors / 1 warn / 1 info at the 2026-11-16 baseline (hotlink x4, the four sandbox references of section 4; pseudo-ref x1, the draft-host self-delivery), standing classes dispositioned in register (c1). T2/T3: every RERUN16 item dispositioned in register (c2), including the KB-44 transient-503 capture caveat on the mobile screenshots. T4: P5 DISPOSITIONED class (ii) / KB-58; P9 DISPOSITIONED under ruling 2; P7 charged to (e) as item 56 and FIXED by FIX5. The candidate changed once after the verdict: the usage sweep (commit b5cb724) inserted -jp into the usage exhibit's self-include (candidate L78), which is why the generated stamp reads STALE. The sweep line is a posting-form correction, not a re-judgement item.
- Why: a reader must be able to see that every charge against this theme has a named closure, and what the STALE stamp does and does not mean.
- Verify: GOSIGN2-LEDGER (b) row 188, (c1), (c2), (c3) and (e) item 56; GOSIGN2-LEDGER-SUPPLEMENT item 56; `git show b5cb724 -- pages/theme:fmd-bhl-theme-jp.txt`.
- Disposition: PASS in the go-sign determination (286 of 286 pass-eligible themes), with the section 8 items standing as documented, uncharged residue.

## 12. Verification

- What a reader can re-run from this repo alone: `python3 review/build_review.py --check` (diff.md and this stamp are current); the sha256 checks in section 0; the greps named in sections 2, 3, 4 and 8; `git show 3911f7b` and `git show a497307` for the two fix waves. A brace-depth scan of both files (comments and strings stripped) ends at depth 0 and never goes negative on either side, so no displaced-brace defect of the anniversary-jp shape is present.
- Why: the package's claims are only worth what a reader can re-derive; every load-bearing claim above names its check.
- Disposition: verification route stands; the T1 baseline counts are the stamp's, and FIX5's own commit records that its change added no new checker error.

## Per-theme record: ledger item 56 [D] re-derived

The ledger's blocking item 56 reads: LOCALIZE-S2-D row, pattern 7, JP font not loaded, listed in the row's display-affecting set; no fix wave had loaded a JP face for this candidate, and no disposition ground covers a missing JP face. The supplement re-judges it FIXED by FIX5-FONTSB, commit 3911f7b, "pattern-7 fix; BIZ UDPGothic GET-verified to serve".

Re-derivation from the bytes. Before the fix (the verdict-era file), the code block imported PT Mono, Exo and Roboto only, --mono-font named '仿宋' (original-named CN face, verdict-era candidate L439 area), and the exhibit's mono claim already read "PT Mono / BIZ UDゴシック", a face nothing loaded. The commit 3911f7b diff adds the porter comment and the two imports (Noto Sans JP wght 400;700, BIZ UDPGothic wght 400;700) after the Roboto import, prepends 'Noto Sans JP' in --body-font and --header-font, appends it in --title-font, replaces '仿宋' with 'BIZ UDPGothic' in --mono-font, and makes the same replacement in the .code-element stack. Every one of those lines is present in the current candidate (imports L199-200, variables L220-223, .code-element L454), and no stack names a Chinese OS face any more (the string 仿宋 survives only inside the FIX5 comment at candidate L198, naming the face it replaced; "Noto Sans SC" remains as a fallback entry in --body-font/--header-font, now behind the loaded 'Noto Sans JP'). The supplement's account is exact, and the FIXED judgement is confirmed from the package's own bytes.

Discrepancies and standing items recorded by this package: (1) the sources.tsv supersession note is wrong against its own cited artifact (section 0). (2) T4's "#page-title block dropped" is correct about the head-module rule and must not be read as "no #page-title rule exists"; the candidate's L399 rule is a different rule, the counterpart of original L384 (section 8c). (3) The dropped [[=]] opener at candidate L33-34 is named by no earlier record (section 8d).

### Post-package repairs (REFRESH3-I) — R-fix-4 (landing c923abf)

The three losses listed in the Summary as standing (head-module #page-title rules, top banner image, emptied テーマコード collapsible) and the dropped [[=]] opener in item (3) above describe this package as built; the coordinator has since repaired them. Item record `FIX-RFIX4.md` in R/review-scout/ (its fmd section, M-1…M-4), landing canonical commit `c923abfc` ("pages: R-fix-4 flags repaired (fmd, frutiger, golden-wind)", 2026-11-17), which postdates this package's build at `ded82a8`. `candidate.txt` has been recopied from the current canonical `pages/theme:fmd-bhl-theme-jp.txt` and `diff.md` and the verdict stamp regenerated with `python3 review/build_review.py`; the stamp reads **STALE** by design — no re-judgement is fabricated, and the frozen ledger remains the verdict record. What changed in the candidate (+17/−11):

- **M-1** — the two head-module `#page-title` rules (centered, var(--header-font), 270%; the @media 170%/nowrap block) restored byte-exact from original L5–17 into the head `[[module css]]` after the two BHL @imports (now L8–20); the code-exhibit annotation corrected to state it holds only the code block's CSS (now L190). This closes the "#page-title block dropped" item (2) above.
- **M-2** — the `[[=]]` opener restored before the + テーマカラー heading (now L46–48), balancing the file's `[[=]]`/`[[/=]]` at 2/2. Closes item (3) above.
- **M-3** — two elements, opposite grounds: the empty テーマコード collapsible's premature `[[/collapsible]]`, ---- separator, candidate-introduced + ソースコード heading and second collapsible opener removed (8 lines), so the `[[code]]` block again sits directly inside the original-form collapsible (closes the Summary's emptied-collapsible item); and the empty `[[>]]`/`[[/>]]` alignment wrapper left by FIX5's bare-Rate removal deleted (2 lines). No code line moved; the Rate is not restored.
- **M-4** — the top banner image restored immediately after the credit block as `[[image https://scpsandboxcn.wdfiles.com/local--files/collab%3Amayca/fmdBHL]]` (https on the same host as the file's other image, now L46), closing the Summary's banner-image item. The checker's single new finding is this line's hotlink error, class (ii), the same disposition family as the file's four pre-existing sandbox hotlinks.
- Checker (FIX-RFIX4): 5/1/1 → 6/1/1; the one new finding is M-4's class-(ii) hotlink; 0 class (i) before and after.

## Change set

| File | Role |
|---|---|
| pages/theme:fmd-bhl-theme-jp.txt | the candidate (this package's candidate.txt) |
| pages/theme-decoration-sample-fmd-bhl-theme-jp.txt | decoration sample the render check ran against |

No component ports, sibling candidates or base-theme candidates belong to this theme's change set; its base is the population's shared theme:black-highlighter-theme-jp.

## Multi-wave provenance

| Wave | Commit | What it changed in this file |
|---|---|---|
| Port creation | (integration) | translation, credit swap, delivery repoints, exhibit restructure |
| FIX4-MECH | a497307 | removed the duplicated BHL @imports inside the code block (KB-65) |
| FIX-CREDIT-D | 1869877 | translator field SCP-JP to AI (ruling-3 form) |
| FIX5-FONTSB | 3911f7b | ledger item 56: JP font loads and stack wiring (section 4) |
| Usage sweep | b5cb724 | usage exhibit self-include to the -jp form (post-verdict; the STALE stamp's ground) |

## Appendix: classifier residue and heuristic adjudication

Classification: 62 blocks, 27 signature-specific, 29 heuristic, 6 residue (classification.json, classify_hunks.py 0.1.0, patterns commit 9c5e9079afb01d30cb9fc4ef9d714e5591eb2ffa). The 6 residue blocks are B3, B4, B7, B12, B59 and B60 (unlabeled). Adjudicated by shape: B3 pairs the deleted banner image line with the added priority-1 frame (the deletion is section 8's banner item; the frame is section 2); B4 pairs the original's rule line with the added priority-2 frame (section 2); B7 is the exhibit logo image's http-to-https scheme upgrade (section 4's asset family); B12 is alignment residue from the credit-block swap, pairing the original's credit:start line against a blank candidate line (section 1); B59 and B60 are blank-line alignment residue at the code block's and the page's closing lines. The 29 heuristic blocks are B2 (head module: import repoints plus the section 8(c) rule loss), B52 (the banner comment, resolved in section 10), B55 (the FIX5 variable stacks, narrated as P7 in section 4), B56/B57 (the two sandbox background scheme upgrades, section 4), B58 (the .code-element stack, section 4), and 23 TRANS-UNANCHORED exhibit blocks (B8, B10, B13, B14, B17, B18, B28-B38, B45-B49, B51) whose translation pairing the anchor pass could not prove (section 6). The FIX5 comment-plus-imports block B53 is signature-specific (JPFONT-LOAD), not heuristic. No heuristic block conceals an unrecorded change.
